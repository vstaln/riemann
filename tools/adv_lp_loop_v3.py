#!/usr/bin/env python3
"""
ADVERSARIAL LP-VERIFIER LOOP v3 — tangent-plane constraints (handoff step).

The v2 LP (interval-only bounds at point cells) was INFEASIBLE at
psum=1/335, eps=0.005991 even though tawan's coefficients certify 0.00596:
the verifier's convex tangent prune lifts boxes above the naive interval
minimum, and the point-cell rows over-constrain the LP.

v3 adds, for every adverse BOX, the verifier's own convex tangent lower
bound as an LP row.  tangent_lower is AFFINE in (l,c) once the gradient
signs are fixed (they are fixed at the base point l=c=0 and re-checked at
the solution):

    tangent(B) = sum_i p_i u_i + sum_i q_i v_i + W(B)
    u_i = mid_i - s_i r_i,  v_i = w(mid_i) - s_i w'(mid_i) r_i
    p_i = p0 + l_{i-1} - l_i,  q_i = q0 + c_{i-1} - c_i
  => tangent(B) = const(B) + A(B).l + C(B).c

  A_k = u_k - u_{k+1},  C_k = v_k - v_{k+1}   (k = 1..5)
  const = p0 sum u_i + q0 sum v_i + sum_{i<j} a_ij w(span_ij)
          - sum_i s_i r_i sum_{spans [a,b) ni i} a_ab w'(span_ab)

A box enters the LP only when its Hessian lower bound is certified PD
(exact LDL in arb, as in tangent_lower).  The Hessian depends on (l,c)
through q_i, so PD is re-checked at the LP solution and any invalid row is
dropped before the verifier run.

Loop: solve LP -> run the real interval verifier -> add the terminal cell
(and its neighborhoods) to the adverse set -> iterate.

Usage:
  uv run --quiet --with mpmath --with scipy --with numpy --with python-flint \
    python3 tools/adv_lp_loop_v3.py <D> <eps_target> [alpha] [--max-iters N]

Reproduction targets (handoff-psum-lc-frontier.md):
  D=335 eps=0.005991 alpha=1.464  (beating 0.673481 needs eps >= 0.00599038)
"""
import sys, math, re, time
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, 'tools')
from verify_coboundary_floor import (verify_floor, cosine_kernel, KernelArb,
                                     RangeMinimum, _down, _up,
                                     _arb_ldl_positive)

GRID = 4000
Q0 = 1.0 / 3.0
C_BOUND = 0.06

if __name__ == '__main__':
    ALPHA = float(sys.argv[3]) if len(sys.argv) > 3 else 1.464
    D = int(sys.argv[1])
    EPS_TARGET = float(sys.argv[2])
    MAX_ITERS = 4
    if '--max-iters' in sys.argv:
        MAX_ITERS = int(sys.argv[sys.argv.index('--max-iters') + 1])
else:
    ALPHA = 1.464
    D = 335
    EPS_TARGET = 0.005991
    MAX_ITERS = 4

# known terminal cell family at psum=1/335 (handoff, eps=0.00597 fails there)
KNOWN_TERMINALS = [(4220, 8007, 8027, 8027, 7995, 4220)]


def base_config_cells(D):
    """Adverse configs as grid index tuples (same families as v2)."""
    configs = set()
    for e0 in [4219, 4220, 4221, 4223, 4229, 4234]:
        for e1 in [4215, 4217, 4220]:
            configs.add((e0, 8007, 8027, 8027, 7995, e1))
            configs.add((e0, 8013, 8017, 8017, 7982, e1))
    for g4 in [15800, 15828, 15920, 16000]:
        configs.add((8017, 4203, 7982, g4, 8031, 4215))
        configs.add((8024, 4203, 7981, 7998, 8031, 4215))
    for ia in range(3200, 8801, 200):
        for ib in range(3200, 8801, 200):
            configs.add((ia, ib, ia, ib, ia, ib))
    for ia in range(3400, 8601, 400):
        for ib in range(3400, 8601, 400):
            for ic in range(3400, 8601, 400):
                configs.add((ia, ib, ic, ia, ib, ic))
    for pos in range(6):
        for H in [20000, 42000, 84000]:
            for s in [4200, 6000, 7960]:
                g = [s, 4200, 7960, s, 4200, s]
                g[pos] = H
                configs.add(tuple(g))
    for p1 in range(6):
        for p2 in range(p1 + 1, 6):
            g = [4200] * 6; g[p1] = 40000; g[p2] = 40000
            configs.add(tuple(g))
    return sorted(configs)


def build_tables(kernel, cell_count):
    t0 = time.time()
    table = [kernel.w_lower_on_cell(i, GRID) for i in range(cell_count)]
    t1 = time.time()
    second = [kernel.w_second_lower_on_cell(i, GRID) for i in range(cell_count)]
    print(f"  tables built in {t1-t0:.1f}s + {time.time()-t1:.1f}s "
          f"({cell_count} cells)", flush=True)
    return RangeMinimum(table), RangeMinimum(second), len(table)


def span_terms(box):
    """(mid_i, r_i, pair spans) in arb, mirroring the verifier's conventions."""
    from flint import arb, fmpq
    mid = [fmpq(lo + hi + 1, 2 * GRID) for lo, hi in box]
    r = [fmpq(hi - lo + 1, 2 * GRID) for lo, hi in box]
    return mid, r


def tangent_affine(box, kernel, ranges, second_ranges, p0):
    """Affine (A[5], C[5], const) of the tangent lower bound; None if not PD.

    Signs s_i are fixed at base (l=c=0).  PD of the Hessian lower bound is
    certified with base q_i = q0 (exact LDL in arb).
    """
    from flint import arb, fmpq
    q = 6
    pair_list = [(i, j) for i in range(q) for j in range(i + 1, q)]
    low_prefix = [0]; high_prefix = [0]
    for lo, hi in box:
        low_prefix.append(low_prefix[-1] + lo)
        high_prefix.append(high_prefix[-1] + hi)

    # --- Hessian lower bound + PD check (base coefficients) ---
    terms = []
    for i, j in pair_list:
        span = j - i
        left = low_prefix[j] - low_prefix[i]
        right = high_prefix[j] - high_prefix[i] + span - 1
        if right >= second_ranges.length:
            return None
        s2 = second_ranges.query(left, right)
        if s2 == float("-inf"):
            return None
        terms.append((i, span, _down((2.0 / (7 - span)) * s2)))
    for i in range(q):
        lo_i, hi_i = box[i]
        if hi_i >= second_ranges.length:
            return None
        s2 = second_ranges.query(lo_i, hi_i)
        if s2 == float("-inf"):
            return None
        terms.append((i, 1, _down(Q0 * s2)))
    if not _arb_ldl_positive(terms, q):
        return None

    mid, r = span_terms(box)

    # --- base gradient (l=c=0) and signs ---
    wval = {}; w1 = {}
    for i in range(q):
        v, f, _ = squared_kernel_derivatives_arb(arb(mid[i]), kernel)
        wval[i] = v; w1[i] = f
    spans = {}
    for i, j in pair_list:
        point = sum(mid[i:j], fmpq(0))
        v, f, _ = squared_kernel_derivatives_arb(arb(point), kernel)
        spans[(i, j)] = (v, f)
    grad = []
    for i in range(q):
        g = arb(p0) + arb(Q0) * w1[i]
        for (a, b), (_, f) in spans.items():
            if a <= i < b:
                g += arb(2.0 / (7 - (b - a))) * f
        grad.append(g)
    s = [1 if g >= 0 else -1 for g in grad]

    # --- affine coefficients ---
    u = [arb(mid[i]) - s[i] * arb(r[i]) for i in range(q)]
    v = [wval[i] - s[i] * w1[i] * arb(r[i]) for i in range(q)]
    # TRUE gradients: d(tangent)/dl_k = u_{k+1} - u_k (since p_i = p0 + l_{i-1} - l_i),
    # d(tangent)/dc_k = v_{k+1} - v_k. tangent = const + A.l + C.c.
    # (v2 had u_k - u_{k+1}, a sign bug: it certified the reflected problem
    #  tangent(-l,-c) >= target. Fixed 2026-08-14 after adversarial review.)
    A = [float(u[k + 1] - u[k]) for k in range(5)]
    C = [float(v[k + 1] - v[k]) for k in range(5)]
    const = arb(p0) * sum(u, arb(0)) + arb(Q0) * sum(v, arb(0))
    for i, j in pair_list:
        const += arb(2.0 / (7 - (j - i))) * spans[(i, j)][0]
    for i in range(q):
        for (a, b), (_, f) in spans.items():
            if a <= i < b:
                const -= s[i] * arb(r[i]) * arb(2.0 / (7 - (b - a))) * f
    return A, C, float(const)


def squared_kernel_derivatives_arb(x, kernel):
    """(w, w', w'') at ball x (Arb)."""
    from flint import arb
    k, k1, k2 = kernel.kernel_derivatives(x)
    return k * k / kernel.k0sq, 2 * k * k1 / kernel.k0sq, 2 * (k1 * k1 + k * k2) / kernel.k0sq


def pd_with_solution(box, kernel, second_ranges, c):
    """Re-certify PD of the box Hessian with q_i from the LP solution."""
    from flint import arb
    q = 6
    pair_list = [(i, j) for i in range(q) for j in range(i + 1, q)]
    low_prefix = [0]; high_prefix = [0]
    for lo, hi in box:
        low_prefix.append(low_prefix[-1] + lo)
        high_prefix.append(high_prefix[-1] + hi)
    terms = []
    for i, j in pair_list:
        span = j - i
        left = low_prefix[j] - low_prefix[i]
        right = high_prefix[j] - high_prefix[i] + span - 1
        if right >= second_ranges.length:
            return False
        s2 = second_ranges.query(left, right)
        if s2 == float("-inf"):
            return False
        terms.append((i, span, _down((2.0 / (7 - span)) * s2)))
    for i in range(q):
        lo_i, hi_i = box[i]
        if hi_i >= second_ranges.length:
            return False
        s2 = second_ranges.query(lo_i, hi_i)
        if s2 == float("-inf"):
            return False
        c_prev = c[i - 1] if 1 <= i - 1 <= 5 else 0.0
        c_next = c[i] if 1 <= i <= 5 else 0.0
        q_i = Q0 + c_prev - c_next
        terms.append((i, 1, _down(q_i * s2)))
    return _arb_ldl_positive(terms, q)


def adverse_boxes(D, ranges, p0, target, extra_points=()):
    pts = set(base_config_cells(D)) | set(tuple(p) for p in extra_points) | set(KNOWN_TERMINALS)
    boxes = set()
    for p in pts:
        # skip points whose cells exceed the built tables (huge-gap
        # asymptotics are enforced by the kappa_i >= 0 rows instead)
        if any(pi > ranges - 1 for pi in p):
            continue
        for w in (0, 1, 2, 4):
            box = tuple((max(0, p[i] - w), min(ranges - 1, p[i] + w)) for i in range(6))
            boxes.add(box)
    return sorted(boxes)


def solve_lp(boxes, kernel, ranges, second_ranges, p0, target):
    rows = []
    for box in boxes:
        aff = tangent_affine(box, kernel, ranges, second_ranges, p0)
        if aff is None:
            continue
        A, C, const = aff
        rows.append((box, A, C, const))
    A_rows = np.array([[-a for a in A] + [-c for c in C] for _, A, C, _ in rows])
    b_rows = np.array([const - target for _, _, _, const in rows])
    # kappa_i >= 0  <=>  -l_{i-1} + l_i <= p0   (i=1..6, l_0 = l_6 = 0)
    # q_i >= 0      <=>  -c_{i-1} + c_i <= q0   (i=1..6, c_0 = c_6 = 0)
    # (both required for the verifier's box_lower/tangent to be sound)
    kap = []
    for i in range(1, 7):
        row = [0.0] * 10
        if 1 <= i - 1 <= 5:
            row[i - 2] = -1.0
        if 1 <= i <= 5:
            row[i - 1] = 1.0
        kap.append(row)
    for i in range(1, 7):
        row = [0.0] * 10
        if 1 <= i - 1 <= 5:
            row[4 + (i - 2)] = -1.0
        if 1 <= i <= 5:
            row[4 + (i - 1)] = 1.0
        kap.append(row)
    A_rows = np.vstack([A_rows, np.array(kap)])
    b_rows = np.concatenate([b_rows, np.full(6, p0), np.full(6, Q0)])
    bounds = [(None, None)] * 5 + [(-C_BOUND, C_BOUND)] * 5
    res = linprog(np.zeros(10), A_ub=A_rows, b_ub=b_rows, bounds=bounds, method='highs')
    return res, rows


def main():
    p0 = 1.0 / (6.0 * D)
    print(f"== adv LP loop v3 (tangent-plane): D={D}, eps={EPS_TARGET}, alpha={ALPHA} ==", flush=True)
    print(f"  p0 = {p0:.9f}, q0 = {Q0}, |c| <= {C_BOUND}", flush=True)
    kernel = cosine_kernel(ALPHA)
    cutoff_cells = int(math.ceil(_up(EPS_TARGET / (1.0 / 3000.0)) * GRID)) + 1
    cell_count = cutoff_cells + 8
    ranges, second_ranges, ncell = build_tables(kernel, cell_count)

    boxes = adverse_boxes(D, ncell, p0, EPS_TARGET)
    print(f"  adverse boxes: {len(boxes)}", flush=True)

    extra = list(KNOWN_TERMINALS)
    wdict = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
    for it in range(MAX_ITERS):
        boxes = adverse_boxes(D, ncell, p0, EPS_TARGET, extra_points=extra)
        res, rows = solve_lp(boxes, kernel, ranges, second_ranges, p0, EPS_TARGET)
        if not res.success:
            print(f"  iter {it}: LP INFEASIBLE ({res.message[:70]})", flush=True)
            print("  => no (l,c) with |c|<=%.2f makes tangent_lower >= %.7f on the adverse set" % (C_BOUND, EPS_TARGET), flush=True)
            return
        x = res.x
        l = x[:5]; c = x[5:10]
        # drop rows whose PD fails at the solution (Hessian depends on c)
        drop = 0
        for _ in range(4):
            bad = []
            for box, A, C, const in rows:
                if not pd_with_solution(box, kernel, second_ranges, c):
                    bad.append(box)
            if not bad:
                break
            drop += len(bad)
            keep = [r for r in rows if r[0] not in set(bad)]
            A2 = np.array([[-a for a in A] + [-cc for cc in C] for _, A, C, _ in keep])
            b2 = np.array([const - EPS_TARGET for _, _, _, const in keep])
            kap = []
            for i in range(1, 7):
                row = [0.0] * 10
                if 1 <= i - 1 <= 5: row[i - 2] = -1.0
                if 1 <= i <= 5: row[i - 1] = 1.0
                kap.append(row)
            A2 = np.vstack([A2, np.array(kap)])
            b2 = np.concatenate([b2, np.full(6, p0)])
            res = linprog(np.zeros(10), A_ub=A2, b_ub=b2,
                          bounds=[(None, None)] * 5 + [(-C_BOUND, C_BOUND)] * 5, method='highs')
            if not res.success:
                print(f"  iter {it}: LP infeasible after dropping {drop} invalid-PD rows", flush=True)
                return
            x = res.x
            l = x[:5]; c = x[5:10]
            rows = keep
        print(f"  iter {it}: LP FEASIBLE (dropped {drop} PD-invalid rows)", flush=True)
        p = [p0 + (l[i - 1] if 1 <= i - 1 <= 5 else 0.0) - (l[i] if 1 <= i <= 5 else 0.0) for i in range(6)]
        q = [Q0 + (c[i - 1] if 1 <= i - 1 <= 5 else 0.0) - (c[i] if 1 <= i <= 5 else 0.0) for i in range(6)]
        print("    l =", [f"{v:.9f}" for v in l], flush=True)
        print("    c =", [f"{v:.9f}" for v in c], flush=True)
        print("    p =", [f"{v:.10f}" for v in p], flush=True)
        print("    q =", [f"{v:.10f}" for v in q], flush=True)
        r = verify_floor(kernel, wdict, 1.0 / 3000, 6, EPS_TARGET,
                         grid=GRID, cap_scheme='coboundary',
                         pressure_coeffs=list(p), nearest_coeffs=list(q),
                         max_nodes=25000000)
        print(f"  iter {it}: verified={r['verified']} nodes={r['nodes']} "
              f"status={r.get('status','done')}", flush=True)
        if r['verified']:
            print("  *** CERTIFIED ***", flush=True)
            print("  l =", [f"{v:.9f}" for v in l], flush=True)
            print("  c =", [f"{v:.9f}" for v in c], flush=True)
            print("  p =", [f"{v:.10f}" for v in p], flush=True)
            print("  q =", [f"{v:.10f}" for v in q], flush=True)
            return
        reason = r.get('reason', '')
        nums = re.findall(r'\d+', reason)
        if len(nums) < 12:
            print("  no terminal cell coords:", reason[:120], flush=True)
            return
        cell = tuple(int(nums[2 * i]) for i in range(6))
        print(f"  + adding terminal cell {tuple(v / GRID for v in cell)}", flush=True)
        extra.append(cell)


if __name__ == '__main__':
    main()
