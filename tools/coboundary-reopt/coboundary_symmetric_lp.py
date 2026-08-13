"""SYMMETRIC-SUBSPACE LP for the coboundary redistribution (l,c).

Executes the one concrete open condition from coboundary-reopt-corrected.md §6
recommendation #2: restrict the redistribution search to the reflection-
symmetric (antisymmetric) subspace that tawan inhabits, re-solve the max-min LP
with the EXACT huge-gap asymptotic rows kappa_i = P0 + l_{i-1} - l_i >= 0, and
check whether any symmetric (l,c) beats tawan's floor 0.007797 on the
578-config family -- and whether its certified eps exceeds 0.0062 at alpha=1.464.

Reflection symmetry of F_B under g -> reflect(g) forces the ANTISYMMETRIC
subspace (derived: l'_m = -l_{6-m} for invariance):
    l = (a1, a2, 0, -a2, -a1),   c = (b1, b2, 0, -b2, -b1)
tawan sits exactly here: a1 = 54/1920000, a2 = -123/1920000,
b1 = b2 = 5971/300000.

In this subspace the huge-gap rows reduce to 3 unique linear constraints:
    a1 <= P0,  a2 - a1 <= P0,  -a2 <= P0      (P0 = 1/1920)
which are exactly kappa_i >= 0 for i = 1..6 (duplicated).

LP decision variables: x = (a1, a2, b1, b2, v).
For each config g with linear coefficients (L, C) and base f0 = F0(g):
    F_B = f0 + (L1-L5) a1 + (L2-L4) a2 + (C1-C5) b1 + (C2-C4) b2
    F_B >= v  <=>  -[(L1-L5),(L2-L4),(C1-C5),(C2-C4)] . x[:4] + v <= f0

Bounds: |a_i| <= 0.0012, |b_i| <= 0.06 (same as the thread's LP).

This is glue to HiGHS (scipy linprog): the LP itself solves in ~0.1s; the
compute-heavy global floor scan is a non-rigorous heuristic (differential
evolution + Nelder-Mead + huge-gap scan), kept separate and labeled as such.
"""
import numpy as np
from scipy.optimize import linprog, minimize, differential_evolution
import time

SQRT2 = np.sqrt(2.0)


def k_alpha(x, alpha):
    x = np.asarray(x, float)
    a = alpha / 2.0
    z1 = np.pi * x - a
    z2 = np.pi * x + a
    return 0.5 * (np.sinc(z1 / np.pi) + np.sinc(z2 / np.pi)) / np.sinc(a / np.pi)


def w_alpha(x, alpha):
    return k_alpha(x, alpha) ** 2


P0 = 1.0 / 1920.0
Q0 = 1.0 / 3.0


def pair_coeffs():
    return {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}


def F0(g, alpha):
    g = np.asarray(g, float)
    y = np.concatenate([[0.0], np.cumsum(g)])
    total = P0 * np.sum(g) + Q0 * np.sum(w_alpha(g, alpha))
    for (i, j), a in pair_coeffs().items():
        total += a * w_alpha(y[j] - y[i], alpha)
    return total


def lin_coeffs(g, alpha):
    g = np.asarray(g, float)
    g0 = np.concatenate([[0.0], g, [0.0]])
    L = np.asarray(g0[1:] - g0[:-1], float)[1:6]
    C = np.asarray(w_alpha(g0[1:], alpha) - w_alpha(g0[:-1], alpha), float)[1:6]
    return L, C


def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + np.dot(L, l) + np.dot(C, c)


def sym_lc(a1, a2, b1, b2):
    """Reconstruct full (l, c) 5-vectors from the symmetric subspace params."""
    l = np.array([a1, a2, 0.0, -a2, -a1])
    c = np.array([b1, b2, 0.0, -b2, -b1])
    return l, c


def p_q_from(l, c):
    l0 = np.concatenate([[0.0], l, [0.0]])
    c0 = np.concatenate([[0.0], c, [0.0]])
    return P0 + (l0[:-1] - l0[1:]), Q0 + (c0[:-1] - c0[1:])


def kappa(l):
    l0 = np.concatenate([[0.0], l, [0.0]])
    return P0 + (l0[:-1] - l0[1:])


# --- tawan baseline (in the symmetric subspace) ---
A1_TAWAN = 54.0 / 1_920_000
A2_TAWAN = -123.0 / 1_920_000
B1_TAWAN = 5971.0 / 300_000
B2_TAWAN = 5971.0 / 300_000
L_TAWAN, C_TAWAN = sym_lc(A1_TAWAN, A2_TAWAN, B1_TAWAN, B2_TAWAN)


def crystal2(alpha, n=14):
    out = []
    for a in np.linspace(0.8, 1.6, n):
        for b in np.linspace(1.4, 2.6, n):
            out.append(np.array([a, b, a, b, a, b]))
    return out


def crystal3(alpha, n=4):
    out = []
    for a in np.linspace(0.85, 1.55, n):
        for b in np.linspace(1.4, 2.5, n):
            for c in np.linspace(0.85, 1.55, n):
                out.append(np.array([a, b, c, a, b, c]))
    return out


def huge_gap_cfg(alpha):
    out = []
    base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
    for pos in range(6):
        for H in [8.0, 14.0, 21.0]:
            g = base.copy()
            g[pos] = H
            out.append(g)
    return out


def intermediate(alpha, n=300):
    rng = np.random.default_rng(12345)
    return [rng.uniform(0.5, 3.0, 6) for _ in range(n)]


def build_578_family(alpha):
    """The exact 578-config family (196 + 64 + 18 + 300 = 578)."""
    cfgs = crystal2(alpha, n=14) + crystal3(alpha, n=4) + huge_gap_cfg(alpha) + intermediate(alpha, n=300)
    assert len(cfgs) == 578, len(cfgs)
    return cfgs


def solve_symmetric_lp(alpha, cfgs, l_bound=0.0012, c_bound=0.06):
    """Maximize v over x=(a1,a2,b1,b2,v): F_B(g) >= v on cfgs, kappa_i >= 0."""
    A, b = [], []
    for g in cfgs:
        L, C = lin_coeffs(g, alpha)
        f0 = F0(g, alpha)
        # F_B = f0 + (L1-L5)a1 + (L2-L4)a2 + (C1-C5)b1 + (C2-C4)b2
        row4 = np.array([-(L[0] - L[4]), -(L[1] - L[3]),
                         -(C[0] - C[4]), -(C[1] - C[3])])
        A.append(np.concatenate([row4, [1.0]]))
        b.append(f0)
    # huge-gap rows kappa_i >= 0 (3 unique in symmetric subspace)
    # a1 <= P0, a2 - a1 <= P0, -a2 <= P0
    for (r4, rhs) in [([1.0, 0.0, 0.0, 0.0], P0),
                      ([-1.0, 1.0, 0.0, 0.0], P0),
                      ([0.0, -1.0, 0.0, 0.0], P0)]:
        A.append(np.array(r4 + [0.0]))
        b.append(rhs)
    A = np.vstack(A)
    bounds = [(-l_bound, l_bound), (-l_bound, l_bound),
              (-c_bound, c_bound), (-c_bound, c_bound), (None, None)]
    c_obj = np.array([0.0, 0.0, 0.0, 0.0, -1.0])
    t0 = time.time()
    res = linprog(c=c_obj, A_ub=A, b_ub=np.array(b), bounds=bounds, method='highs')
    print(f"  LP solved in {time.time()-t0:.1f}s status={res.status} msg={res.message}")
    if not res.success:
        return None
    return res.x


def floor_over(alpha, l, c, cfgs):
    return min(F_B(g, alpha, l, c) for g in cfgs)


def refine_floor(alpha, l, c, cfg, n_restarts=24):
    best = F_B(cfg, alpha, l, c)
    rng = np.random.default_rng(9)
    for _ in range(n_restarts):
        x0 = np.maximum(0.4, cfg + rng.normal(0, 0.3, 6))
        r = minimize(lambda g: F_B(g, alpha, l, c), x0, method='Nelder-Mead',
                     options={'maxiter': 1500, 'xatol': 1e-9, 'fatol': 1e-12})
        if r.fun < best:
            best = r.fun
    return best


def global_floor(alpha, l, c, huge=True):
    """Heuristic (NON-RIGOROUS) global float floor: DE + crystal + huge-gap scan."""
    r = differential_evolution(lambda g: F_B(g, alpha, l, c),
                               [(0.4, 3.5)] * 6, seed=3,
                               popsize=20, maxiter=400, tol=1e-9,
                               polish=True, workers=1)
    best = r.fun
    for pos in range(6):
        for H in np.linspace(5, 21, 9):
            base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
            g = base.copy()
            g[pos] = H
            best = min(best, refine_floor(alpha, l, c, g, n_restarts=6))
            g2 = np.full(6, 1.1)
            g2[pos] = H
            best = min(best, F_B(g2, alpha, l, c))
    return best


if __name__ == "__main__":
    for alpha, name in [(1.49, 'a149'), (1.464, 'a1464')]:
        print(f"\n========== alpha={alpha} ({name}) ==========", flush=True)
        cfgs = build_578_family(alpha)
        print(f"constraint family size = {len(cfgs)}", flush=True)

        fl_t = floor_over(alpha, L_TAWAN, C_TAWAN, cfgs)
        print(f"  tawan floor on 578-family = {fl_t:.9f}", flush=True)

        x = solve_symmetric_lp(alpha, cfgs)
        if x is None:
            print("  LP infeasible/unbounded")
            continue
        a1, a2, b1, b2, v = x
        l, c = sym_lc(a1, a2, b1, b2)
        p, q = p_q_from(l, c)
        kap = kappa(l)
        print(f"  SYMMETRIC LP max-min v* = {v:.9f}", flush=True)
        print(f"  a1={a1:.10f} a2={a2:.10f} b1={b1:.10f} b2={b2:.10f}", flush=True)
        print(f"  l = {np.round(l, 10)}", flush=True)
        print(f"  c = {np.round(c, 10)}", flush=True)
        print(f"  p = {np.round(p, 8)} sum={np.sum(p):.9f}", flush=True)
        print(f"  q = {np.round(q, 8)} sum={np.sum(q):.9f}", flush=True)
        print(f"  kappa = {np.round(kap, 8)} min={kap.min():.9f}", flush=True)
        fl_lp = floor_over(alpha, l, c, cfgs)
        print(f"  floor over LP family: tawan={fl_t:.9f}  symLP={fl_lp:.9f}", flush=True)

        gf_lp = global_floor(alpha, l, c)
        gf_t = global_floor(alpha, L_TAWAN, C_TAWAN)
        print(f"  GLOBAL float floor (heuristic): symLP={gf_lp:.9f}  tawan={gf_t:.9f}", flush=True)
        print(f"  RESULT: symLP {'BEATS' if gf_lp > gf_t else 'LOSES TO (or ties)'} tawan globally", flush=True)
