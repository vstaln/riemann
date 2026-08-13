"""CORRECTED LP for the coboundary redistribution (l,c).

F_B(g; l,c) = F0(g) + sum_{k=1..5} l_k (g_{k+1}-g_k) + sum_{k=1..5} c_k (w(g_{k+1})-w(g_k))
F0 = sum_j p0 g_j + sum_j q0 w(g_j) + S(y),  p0=1/1920, q0=1/3,
S(y) = sum_{0<=a<b<=6} (2/(7-(b-a))) w(y_b-y_a), y_0=0, y_k=g_1+..+g_k.

EXACT huge-gap asymptotics (derived, and checked numerically):
  as g_i -> oo with g_{-i} fixed,
    F_B = kappa_i g_i + const_i(g_{-i}; l,c) + o(1),
    kappa_i = p_i + l_{i-1} - l_i = p0 + 2(l_{i-1}-l_i)   (l_0=l_6=0)
  If kappa_i < 0, F_B -> -oo: the PRIOR LP's bug (it had kappa_1<0).
  All spans containing g_i, and w(g_i), -> 0.

The corrected LP maximizes v subject to, over the constraint family K:
  (a) period-2/3 crystal configs:           F_B(g) >= v
  (b) huge-gap asymptotics:
        - exact linear:  kappa_i >= v  for each i=1..6
        - sampled finite-cutoff: F_B at g_i = cutoff_max with adversarially
          sampled neighbors >= v   (cutoff_max = 21, verifier's range)
  (c) intermediate grid: uniform sample over [0.5,3.0]^6 and near kernel zeros.

Dual certificate: the LP value v* is the max over (l,c) of min-over-K F_B.
If tawan's (l,c) is feasible and attains min_K F_B >= v*, tawan is optimal
within this relaxation.

PONYTAIL: grid sampling is heuristic; certification is by the interval
verifier (tools/verify_coboundary_floor.py), which is the ground truth.
"""
import numpy as np
from scipy.optimize import linprog, minimize, differential_evolution
import time

SQRT2 = np.sqrt(2.0)

def k_alpha(x, alpha):
    x = np.asarray(x, float); a = alpha / 2.0
    z1 = np.pi * x - a; z2 = np.pi * x + a
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
    L = g0[1:] - g0[:-1]
    C = w_alpha(g0[1:], alpha) - w_alpha(g0[:-1], alpha)
    return np.asarray(L[1:6], float), np.asarray(C[1:6], float)

def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + np.dot(L, l) + np.dot(C, c)

def p_q_from(l, c):
    l0 = np.concatenate([[0.0], l, [0.0]])
    c0 = np.concatenate([[0.0], c, [0.0]])
    return P0 + (l0[:-1] - l0[1:]), Q0 + (c0[:-1] - c0[1:])

def kappa(l):
    l0 = np.concatenate([[0.0], l, [0.0]])
    return P0 + (l0[:-1] - l0[1:])

# ---------------------------------------------------------------------------
# Constraint family K
# ---------------------------------------------------------------------------
def crystal2(alpha, n=16, lo_a=0.8, hi_a=1.6, lo_b=1.4, hi_b=2.6):
    out = []
    for a in np.linspace(lo_a, hi_a, n):
        for b in np.linspace(lo_b, hi_b, n):
            out.append(np.array([a, b, a, b, a, b]))
    return out

def crystal3(alpha, n=7):
    out = []
    for a in np.linspace(0.85, 1.55, n):
        for b in np.linspace(1.4, 2.5, n):
            for c in np.linspace(0.85, 1.55, n):
                out.append(np.array([a, b, c, a, b, c]))
    return out

def huge_gap_cfg(alpha, cutoff=21.0, neighbors=([1.05, 1.98] * 3,)):
    # (g_i, g_{-i}) with g_i = cutoff, neighbors sampled adversarially
    out = []
    base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
    for pos in range(6):
        for H in [8.0, 14.0, 21.0]:
            g = base.copy(); g[pos] = H
            out.append(g)
    return out

def intermediate(alpha, n=400, seed=12345):
    rng = np.random.default_rng(seed)
    out = [rng.uniform(0.5, 3.0, 6) for _ in range(n)]
    # near kernel first zero ~ sqrt( (alpha/2)^2 - ... ) around gap 1.2-1.5
    out += [rng.uniform(0.9, 1.6, 6) for _ in range(n // 2)]
    return out

def build_family(alpha, n2=14, n3=5, nint=500):
    cfgs = []
    cfgs += crystal2(alpha, n=n2)
    cfgs += crystal3(alpha, n=n3)
    cfgs += huge_gap_cfg(alpha)
    cfgs += intermediate(alpha, n=nint)
    return cfgs

# ---------------------------------------------------------------------------
# LP
# ---------------------------------------------------------------------------
def solve_maxmin(alpha, cfgs, l_bound=0.0012, c_bound=0.06, with_asympt=True,
                 v_floor=None):
    A, b = [], []
    for g in cfgs:
        L, C = lin_coeffs(g, alpha)
        f0 = F0(g, alpha)
        A.append(np.concatenate([-L, -C, [1.0]]))
        b.append(f0)
    if with_asympt:
        # EXACT huge-gap constraint: the slope of F_B as g_i->oo (others fixed)
        # is kappa_i = p_i = P0 + (l_{i-1} - l_i).  We need kappa_i >= 0
        # (strictly > 0 for the verifier's one-body pruning to dominate).
        #   P0 + l_{i-1} - l_i >= 0  <=>  -l_{i-1} + l_i <= P0
        # with l_0 = l_6 = 0.  (NOT kappa_i >= v: v is the uniform floor over
        # bounded configs and can exceed the small huge-gap slopes.)
        for i in range(1, 7):
            row = np.zeros(10)              # l_1..l_5 then c_1..c_5; no v
            if i >= 2: row[i - 2] = -1.0    # -l_{i-1}
            if i <= 5: row[i - 1] = +1.0    # +l_i
            A.append(np.concatenate([row, [0.0]])); b.append(P0)
    A = np.vstack(A)
    bounds = [(-l_bound, l_bound)] * 5 + [(-c_bound, c_bound)] * 5 + [(None, None)]
    c_obj = np.zeros(11); c_obj[10] = -1.0
    t0 = time.time()
    res = linprog(c=c_obj, A_ub=A, b_ub=np.array(b), bounds=bounds, method='highs')
    print(f"  LP solved in {time.time()-t0:.1f}s status={res.status} msg={res.message}")
    if not res.success:
        return None, None, None
    x = res.x
    return x[:5], x[5:10], x[10]

# ---------------------------------------------------------------------------
# Float floor checks (NON-rigorous; heuristic only)
# ---------------------------------------------------------------------------
def floor_over(alpha, l, c, cfgs):
    return min(F_B(g, alpha, l, c) for g in cfgs)

def refine_floor(alpha, l, c, cfg, n_restarts=24):
    """Local refinement of a candidate worst config + differential evolution
    over [0.5, 3.5]^6 (the verifier's active domain is bounded ~21; DE over a
    generous box [0.5, 3.5] captures crystals; huge-gap handled separately)."""
    best = F_B(cfg, alpha, l, c)
    rng = np.random.default_rng(9)
    for _ in range(n_restarts):
        x0 = np.maximum(0.4, cfg + rng.normal(0, 0.3, 6))
        r = minimize(lambda g: F_B(g, alpha, l, c), x0, method='Nelder-Mead',
                     options={'maxiter': 1500, 'xatol': 1e-9, 'fatol': 1e-12})
        if r.fun < best: best = r.fun
    return best

def global_floor(alpha, l, c, huge=True):
    """DE over [0.5,3.5]^6 plus explicit huge-gap scan g_i in [5,21]."""
    r = differential_evolution(lambda g: F_B(g, alpha, l, c),
                               [(0.4, 3.5)] * 6, seed=3,
                               popsize=20, maxiter=400, tol=1e-9,
                               polish=True, workers=1)
    best = r.fun
    # huge-gap scan: each coord at H in [5..21], others varied over crystal-ish box
    for pos in range(6):
        for H in np.linspace(5, 21, 9):
            base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
            g = base.copy(); g[pos] = H
            best = min(best, refine_floor(alpha, l, c, g, n_restarts=6))
            # also H with all others small
            g2 = np.full(6, 1.1); g2[pos] = H
            best = min(best, F_B(g2, alpha, l, c))
    return best

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    l_tawan = np.array([54, -123, 0, 123, -54]) / 1_920_000
    c_tawan = np.array([5971, 5971, 0, -5971, -5971]) / 300_000

    for alpha, name in [(1.49, 'a149'), (SQRT2, 'asqrt2')]:
        print(f"\n========== alpha={alpha} ({name}) ==========", flush=True)
        cfgs = build_family(alpha)
        print(f"constraint family size = {len(cfgs)}", flush=True)
        for c_bound in [0.06, 0.02, 0.15]:
            print(f"--- c_bound = {c_bound} ---", flush=True)
            l, c, v = solve_maxmin(alpha, cfgs, c_bound=c_bound)
            if l is None:
                print("  LP infeasible/unbounded"); continue
            p, q = p_q_from(l, c)
            kap = kappa(l)
            print(f"  LP max-min v* = {v:.6f}", flush=True)
            print(f"  kappa (huge-gap slopes) = {np.round(kap, 6)}", flush=True)
            print(f"  p = {np.round(p, 7)}, sum={np.sum(p):.6f}", flush=True)
            print(f"  q = {np.round(q, 6)}, sum={np.sum(q):.6f}", flush=True)
            fl_band = floor_over(alpha, l, c, crystal2(alpha, n=22) + crystal3(alpha, n=7))
            print(f"  floor over dense crystal family = {fl_band:.6f}", flush=True)
            # tawan comparison on the same family
            fl_t = floor_over(alpha, l_tawan, c_tawan, cfgs)
            fl_lp = floor_over(alpha, l, c, cfgs)
            print(f"  floor over LP family: tawan={fl_t:.6f}  LP={fl_lp:.6f}", flush=True)
            # global float floor (expensive; run only for best candidate)
            if v > 0.0066:
                gf = global_floor(alpha, l, c)
                gft = global_floor(alpha, l_tawan, c_tawan)
                print(f"  GLOBAL float floor (DE+huge-gap): LP={gf:.6f}  tawan={gft:.6f}", flush=True)
