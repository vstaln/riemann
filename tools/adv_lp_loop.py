#!/usr/bin/env python3
"""
ADVERSARIAL LP-VERIFIER LOOP v2 — interval-exact.

The LP constrains F(g) >= target using the EXACT same evaluation the
interval verifier uses (box_lower at point cells): p_i·g_i/grid exact,
q_i·w_lower_on_cell[g_i], pair terms a_ij·min(w over cell-span range)
via RangeMinimum. So an LP-feasible (l,c) is exactly verifier-certifiable.

Loop: solve LP over adverse config set, run the real interval verifier,
add unresolved terminal cells, iterate until certified or infeasible.

Usage: python adv_lp_loop.py <D> <eps_target> [alpha] [--max-iters N]
"""
import sys, math, re, itertools
import mpmath as mp
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, 'tools')
from verify_coboundary_floor import (verify_floor, cosine_kernel, KernelArb,
                                     RangeMinimum, _down)

ALPHA = float(sys.argv[3]) if len(sys.argv) > 3 else 1.464
D = int(sys.argv[1])
EPS_TARGET = float(sys.argv[2])
MAX_ITERS = int(sys.argv[4]) if len(sys.argv) > 4 else 12
GRID = 4000

def build_table(kernel, grid, cell_count):
    return [kernel.w_lower_on_cell(i, grid) for i in range(cell_count)]

def box_lower_at_point(gcells, kernel, table, ranges, D, l, c, grid=GRID):
    """Exact replicate of verifier box_lower at a POINT cell config (lo==hi).
    gcells: list of 6 grid indices."""
    p0 = 1.0/(6.0*D); q0 = 1.0/3.0
    q = 6
    result = 0.0
    low_prefix = [0]; high_prefix = [0]
    for k in gcells:
        low_prefix.append(low_prefix[-1] + k)
        high_prefix.append(high_prefix[-1] + k)
    # p_i = p0 + (l_{i-1} - l_i)
    for i in range(q):
        l_prev = l[i-1] if 1 <= i <= 5 else 0.0
        l_next = l[i] if i <= 4 else 0.0
        p_i = p0 + l_prev - l_next
        result = _down(result + _down(p_i * (low_prefix[i+1] - low_prefix[i]) / grid))
    # q_i = q0 + (c_{i-1} - c_i)
    for i in range(q):
        c_prev = c[i-1] if 1 <= i <= 5 else 0.0
        c_next = c[i] if i <= 4 else 0.0
        q_i = q0 + c_prev - c_next
        idx = gcells[i]
        if idx < ranges.length:
            result = _down(result + _down(q_i * ranges.query(idx, idx)))
    # pair terms
    for i in range(q):
        for j in range(i+1, q):
            span = j - i
            left = low_prefix[j] - low_prefix[i]
            right = high_prefix[j] - high_prefix[i] + span - 1
            if right >= ranges.length:
                continue
            result = _down(result + _down((2.0/(7-span)) * ranges.query(left, right)))
    return result

def F_affine_interval(gcells, kernel, table, ranges, D):
    """Coeff (l_1..5, c_1..5), const such that box_lower(g) = coeff·(l,c)+const.
    Derived from the exact box_lower expression (linear in l, c)."""
    p0 = 1.0/(6.0*D); q0 = 1.0/3.0
    q = 6
    grid = GRID
    # base (l=c=0) value and coefficient extraction via finite differences
    # is fragile; instead build the affine map symbolically: box_lower is
    # affine in (l,c) because p_i,q_i are affine in (l,c) and everything
    # else is constant. Extract coefficients by direct formula:
    lc = [0.0]*5; cc = [0.0]*5
    const = 0.0
    low_prefix = [0]
    for k in gcells: low_prefix.append(low_prefix[-1] + k)
    # one-body p terms: sum_i p_i g_i, p_i = p0 + l_{i-1} - l_i
    #   = p0*sum g_i + sum_k l_k (g_{k+1} - g_k)  [telescoping]
    const += p0 * sum(gcells) / grid
    for k in range(1, 6):
        lc[k-1] += (gcells[k] - gcells[k-1]) / grid   # coefficient of l_k
    # q terms: sum_i q_i w(g_i), q_i = q0 + c_{i-1} - c_i
    wg = [ranges.query(gcells[i], gcells[i]) if gcells[i] < ranges.length else 0.0
          for i in range(q)]
    const += q0 * sum(wg)
    for k in range(1, 6):
        cc[k-1] += wg[k] - wg[k-1]
    # pair terms: constant (a_ij fixed)
    for i in range(q):
        for j in range(i+1, q):
            span = j - i
            left = low_prefix[j] - low_prefix[i]
            right = left + span - 1
            if right >= ranges.length:
                continue
            const += (2.0/(7-span)) * ranges.query(left, right)
    return lc+cc, const

def base_config_cells(D):
    """Adverse configs as grid index tuples. Includes the known terminal
    cell families: near-symmetric endpoints ~1.055 (idx 4220), alternating
    (2.0, 1.05, ...) with huge 4th gap, period-2/3 crystals, huge gaps."""
    configs = set()
    # near-symmetric family (the iter-0 terminal cell): (1.0548, 2.0192, 1.9992, 2.0025, 1.9992, 1.0548)
    for e0 in [4219, 4220, 4221, 4223, 4229, 4234]:
        for e1 in [4215, 4217, 4220]:
            configs.add((e0, 8007, 8027, 8027, 7995, e1))
            configs.add((e0, 8013, 8017, 8017, 7982, e1))
    # alternating family with big 4th gap: (8017, 4203, 7982, 15900, ...)
    for g4 in [15800, 15828, 15920, 16000]:
        configs.add((8017, 4203, 7982, g4, 8031, 4215))
        configs.add((8024, 4203, 7981, 7998, 8031, 4215))
    # period-2 crystals (a,b,a,b,a,b)
    for ia in range(3200, 8801, 200):
        for ib in range(3200, 8801, 200):
            configs.add((ia, ib, ia, ib, ia, ib))
    # period-3 (a,b,c,a,b,c)
    for ia in range(3400, 8601, 400):
        for ib in range(3400, 8601, 400):
            for ic in range(3400, 8601, 400):
                configs.add((ia, ib, ic, ia, ib, ic))
    # one huge gap
    for pos in range(6):
        for H in [20000, 42000, 84000]:
            for s in [4200, 6000, 7960]:
                g = [4200, 4200, 7960, 4200, 4200, 4200]
                g[pos] = H
                g = [s, 4200, 7960, s, 4200, s]
                g[pos] = H
                configs.add(tuple(g))
    # two huge gaps
    for p1 in range(6):
        for p2 in range(p1+1, 6):
            g = [4200]*6; g[p1] = 40000; g[p2] = 40000
            configs.add(tuple(g))
    return sorted(configs)

def solve_lp(D, configs, target, kernel, table, ranges):
    m = len(configs)
    A_rows = []; b_rows = []
    for gg in configs:
        coeff, const = F_affine_interval(gg, kernel, table, ranges, D)
        A_rows.append([-c for c in coeff]); b_rows.append(const - target)
    A = np.array(A_rows); b = np.array(b_rows)
    bounds = [(None, None)]*5 + [(-0.06, 0.06)]*5
    c_obj = np.zeros(10)
    res = linprog(c_obj, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res

def main():
    print(f"== adversarial LP loop v2 (interval-exact): D={D}, eps={EPS_TARGET}, alpha={ALPHA} ==", flush=True)
    kernel = cosine_kernel(ALPHA)
    cutoff_units = EPS_TARGET / (1.0/3000.0)
    cutoff_cells = int(math.ceil(cutoff_units * GRID)) + 1
    cell_count = cutoff_cells + 8
    table = build_table(kernel, GRID, cell_count)
    ranges = RangeMinimum(table)
    print(f"  table built: {cell_count} cells sha={__import__('hashlib').sha256(np.array(table).tobytes()).hexdigest()[:16]}", flush=True)
    configs = base_config_cells(D)
    print(f"  base configs: {len(configs)}", flush=True)
    wdict = {(i,j): 2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
    for it in range(MAX_ITERS):
        res = solve_lp(D, configs, EPS_TARGET, kernel, table, ranges)
        if not res.success:
            print(f"  iter {it}: LP INFEASIBLE ({res.message[:60]})", flush=True)
            return
        x = res.x
        l = x[:5]; c = x[5:10]
        p0 = 1.0/(6.0*D); q0 = 1.0/3.0
        p = [p0 + (l[i-1] if 1 <= i-1 <= 5 else 0.0) - (l[i] if 1 <= i <= 5 else 0.0) for i in range(6)]
        q = [q0 + (c[i-1] if 1 <= i-1 <= 5 else 0.0) - (c[i] if 1 <= i <= 5 else 0.0) for i in range(6)]
        r = verify_floor(kernel, wdict, 1.0/3000, 6, EPS_TARGET,
                         grid=GRID, cap_scheme='coboundary',
                         pressure_coeffs=list(p), nearest_coeffs=list(q),
                         max_nodes=25000000)
        print(f"  iter {it}: verified={r['verified']} nodes={r['nodes']}", flush=True)
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
        cell = tuple(int(nums[2*i]) for i in range(6))
        print(f"  + adding terminal cell {tuple(v/4000 for v in cell)}", flush=True)
        configs.append(cell)
        configs = sorted(set(configs))
    print("  loop exhausted without certification", flush=True)

if __name__ == '__main__':
    main()
