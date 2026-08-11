#!/usr/bin/env python3
"""PURE block-size floor ladder for the Gram-stability refinement.

For a block of n consecutive simple-zero atoms with consecutive gaps
u_1..u_{n-1} (all > 0, span = sum u_i <= 4), the Gram matrix is
G_ij = k(y_j - y_i), y_j = u_1+...+u_j, k = K/K(0) the Montgomery-Taylor
overlap kernel.  The per-atom stability floor is

    eps_atom(n) = min_{u>0, span<=4}  tr Psi(G_n) / n,

Psi(t) = (t-1)^2 on [0,2], 2t-3 beyond, applied to the eigenvalues of G_n.

This script computes eps_atom(n) by
  (a) a dense random pre-scan on the simplex  (Dirichlet + exponential spans
      + structured "kernel-zero-tile" patterned starts),
  (b) local refinement (L-BFGS-B on a span-penalty objective) from the best
      starts,
  (c) an exact SLSQP constrained pass from the best few starts,
  (d) differential_evolution cross-check for n <= 11.

Labels: CHECKED NUMERICALLY (estimate, not an interval certificate).

Run:  cd /home/vstaln/riemann/research/ladder-convergence
      uv run --quiet --with mpmath --with numpy --with scipy python ladder_floor.py
"""
import json
import time

import numpy as np
from scipy.optimize import minimize, differential_evolution

rng = np.random.default_rng(20260812)

SQ2 = np.sqrt(2.0)
PI = np.pi


def _K(x):
    """K(x) = int_{-1/2}^{1/2} cos(sqrt2 t) cos(2 pi x t) dt, entire sinc form."""
    x = np.asarray(x, dtype=float)
    a = (SQ2 - 2 * PI * x) / 2.0
    b = (SQ2 + 2 * PI * x) / 2.0
    return 0.5 * (np.sinc(a / PI) + np.sinc(b / PI))


K0 = float(_K(0.0))


def k(x):
    return _K(x) / K0


def psi(t):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 2.0, (t - 1.0) ** 2, 2.0 * t - 3.0)


def gram_from_gaps(u):
    """G for a single gap vector u (length n-1)."""
    y = np.concatenate([[0.0], np.cumsum(u)])
    d = np.abs(y[:, None] - y[None, :])
    return k(d)


def tr_psi_gaps(u):
    """tr Psi(G_n(u)) / n."""
    u = np.asarray(u, dtype=float)
    G = gram_from_gaps(u)
    lam = np.linalg.eigvalsh(G)
    return float(np.sum(psi(lam))) / len(lam)


def batched_tr_psi(U, chunk=2048):
    """Vectorized tr Psi(G)/n over a (Ns, n-1) gap matrix. Returns (Ns,)."""
    Ns, m = U.shape
    n = m + 1
    out = np.empty(Ns)
    for s in range(0, Ns, chunk):
        P = U[s:s + chunk]
        y = np.concatenate([np.zeros((P.shape[0], 1)), np.cumsum(P, axis=1)], axis=1)
        d = np.abs(y[:, :, None] - y[:, None, :])          # (chunk, n, n)
        G = k(d)
        lam = np.linalg.eigvalsh(G)                         # batched
        v = np.where(lam <= 2.0, (lam - 1.0) ** 2, 2.0 * lam - 3.0)
        out[s:s + chunk] = v.sum(axis=1) / n
    return out


def pair_sq(U, chunk=4096):
    """S2 = sum_{i<j} k(y_j-y_i)^2 over a (Ns, n-1) gap matrix."""
    Ns, m = U.shape
    n = m + 1
    out = np.empty(Ns)
    tri = np.triu(np.ones((n, n), dtype=bool), 1)
    for s in range(0, Ns, chunk):
        P = U[s:s + chunk]
        y = np.concatenate([np.zeros((P.shape[0], 1)), np.cumsum(P, axis=1)], axis=1)
        d = np.abs(y[:, :, None] - y[:, None, :])
        w = k(d) ** 2
        out[s:s + chunk] = w[:, tri].sum(axis=1)
    return out


# ---------------------------------------------------------------------------
# Sampling strategies over the gap domain  {u>0, sum u <= 4}
# ---------------------------------------------------------------------------
SPAN = 4.0


def sample_dirichlet(Ns, m):
    """Uniform over the simplex  sum u = 4  (boundary of the domain)."""
    return SPAN * rng.dirichlet(np.ones(m), Ns)


def sample_exponential(Ns, m):
    """Interior points: exponential gaps rescaled to a random span in (0,4]."""
    raw = rng.exponential(size=(Ns, m)) + 1e-4
    spans = SPAN * rng.random(Ns) ** 0.3          # bias toward larger spans
    return raw * (spans[:, None] / raw.sum(axis=1, keepdims=True))


KERNEL_ZEROS = np.array([1.057278, 2.030068, 3.020243])
TILES = [np.array([1.057278, 2.030068]),
         np.array([2.030068, 1.057278]),
         np.array([1.057278, 1.057278]),
         np.array([1.057278, 3.020243]),
         np.array([2.030068, 2.030068])]


def sample_patterned(Ns, m):
    """Tiles of kernel-zero gaps, rescaled to spans <= 4 (always feasible)."""
    out = np.empty((0, m))
    while len(out) < Ns:
        tile = TILES[rng.integers(len(TILES))]
        rep = int(np.ceil(m / len(tile)))
        g = np.tile(tile, rep)[:m]
        if rng.random() < 0.5:
            g = g[::-1]
        g = g + rng.normal(0, 0.06, m)
        g = np.abs(g) + 1e-4
        # rescale so that total span <= 4 with a random fill factor
        scale = (0.15 + 0.85 * rng.random()) * SPAN / g.sum()
        g = g * scale
        out = np.vstack([out, g[None, :]])
    return out[:Ns]


def refine_penalty(obj, starts, m, P=1e6, niter=300):
    """L-BFGS-B on  obj(u) + P*max(0,sum u - 4)^2  from each start."""
    bnds = [(1e-4, SPAN)] * m

    def pen(u):
        s = float(np.sum(u))
        return obj(u) + P * max(0.0, s - SPAN) ** 2

    best = (1e300, None)
    for g0 in starts:
        r = minimize(pen, g0, method='L-BFGS-B', bounds=bnds,
                     options={'ftol': 1e-14, 'maxiter': niter})
        if r.fun < best[0]:
            best = (r.fun, r.x.copy())
    return best


def refine_slsqp(obj, starts, m, niter=300):
    """Exact constrained pass: min obj(u) s.t. sum u <= 4."""
    bnds = [(1e-4, SPAN)] * m
    cons = {'type': 'ineq', 'fun': lambda u: SPAN - np.sum(u)}
    best = (1e300, None)
    for g0 in starts:
        r = minimize(obj, g0, method='SLSQP', bounds=bnds, constraints=cons,
                     options={'ftol': 1e-14, 'maxiter': niter})
        if r.fun < best[0]:
            best = (r.fun, r.x.copy())
    return best


def min_floor(n, Ns_dir, Ns_exp, Ns_pat, nref=300, do_de=True):
    """Return (best_per_atom, best_gaps, details)."""
    m = n - 1
    t0 = time.time()
    U = np.vstack([sample_dirichlet(Ns_dir, m),
                   sample_exponential(Ns_exp, m),
                   sample_patterned(Ns_pat, m)])
    vals = batched_tr_psi(U)
    order = np.argsort(vals)
    best_samp = float(vals[order[0]])
    best_gaps = U[order[0]].copy()
    details = {'samples': len(U), 'sample_best': best_samp,
               'sample_argmin': [float(x) for x in best_gaps]}

    # pair-square floor E/2 = min sum_{i<j} k(y_j-y_i)^2  (drives the
    # certified bound via tr Psi(G) >= min(1, E)); report on the SAME argmin
    # candidate set for comparability.
    ps = pair_sq(U)
    order_p = np.argsort(ps)
    details['pair_sq_best'] = float(ps[order_p[0]])
    details['pair_sq_argmin'] = [float(x) for x in U[order_p[0]]]

    # local refinement
    obj = lambda u: tr_psi_gaps(u)
    starts = [U[i] for i in order[:nref]]
    rp = refine_penalty(obj, starts, m)
    details['lbfgsb_best'] = rp[0]
    if rp[0] < best_samp:
        best_samp, best_gaps = rp[0], rp[1].copy()

    rs = refine_slsqp(obj, [best_gaps] + [U[i] for i in order[:20]], m)
    details['slsqp_best'] = rs[0]
    if rs[0] < best_samp:
        best_samp, best_gaps = rs[0], rs[1].copy()

    # differential_evolution cross-check for small n
    if do_de and m <= 10:
        def de_obj(u):
            return tr_psi_gaps(u) + 1e6 * max(0.0, float(np.sum(u)) - SPAN) ** 2
        de = differential_evolution(de_obj, [(1e-4, SPAN)] * m,
                                    maxiter=600, popsize=15, tol=1e-12,
                                    seed=42, polish=True, workers=1)
        details['de_best'] = de.fun
        if de.fun < best_samp:
            best_samp, best_gaps = de.fun, de.x.copy()

    details['elapsed'] = time.time() - t0
    return best_samp, best_gaps, details


def main():
    print("=" * 78)
    print("PURE BLOCK-SIZE FLOOR LADDER   eps_atom(n) = min tr Psi(G_n)/n")
    print("domain: u>0, span<=4   labels: CHECKED NUMERICALLY (estimate)")
    print("=" * 78)

    # --- sanity: kernel constants ---
    print("\n[kernel sanity]")
    print(f"  K(0) = {K0:.15f}")
    for x in (1.0, 1.5, 2.0, 3.0):
        print(f"  k({x}) = {k(x):+.6f}")
    xs = np.linspace(0.05, 4.0, 40000)
    kv = k(xs)
    sc = np.where(np.diff(np.sign(kv)) != 0)[0]
    print("  kernel zeros on (0,4]:", [f"{xs[i]:.4f}" for i in sc])

    # --- n=3,4 reproductions first ---
    print("\n[reproduction n=3, n=4]")
    for n in (3, 4):
        nd, ne_, np_ = (60000, 40000, 20000)
        b, g, det = min_floor(n, nd, ne_, np_, do_de=True)
        print(f"  n={n}: eps_atom={b:.6e}  per-block={b*n:.6e}  "
              f"argmin gaps={np.round(g,4).tolist()}  span={g.sum():.4f}  "
              f"(details: {det['sample_best']:.3e} / {det['lbfgsb_best']:.3e} / "
              f"{det.get('slsqp_best',0):.3e} / de={det.get('de_best',0):.3e})")

    # --- main ladder ---
    sizes = [5, 7, 9, 11, 15, 21, 30]
    budgets = {5: (80000, 60000, 30000), 7: (80000, 60000, 30000),
               9: (70000, 50000, 30000), 11: (60000, 40000, 30000),
               15: (50000, 30000, 20000), 21: (40000, 20000, 15000),
               30: (30000, 15000, 10000)}
    results = {}
    print("\n[main ladder]")
    print(f"{'n':>3} {'eps_atom':>13} {'eps_block':>13} {'span*':>7} {'maxgap':>7} {'elapsed':>7}")
    for n in sizes:
        nd, ne_, np_ = budgets[n]
        b, g, det = min_floor(n, nd, ne_, np_, do_de=(n <= 11))
        results[n] = {'eps_atom': b, 'argmin': [float(x) for x in g],
                      'span': float(g.sum()), 'maxgap': float(g.max()),
                      'details': det}
        print(f"{n:3d} {b:13.6e} {b*n:13.6e} {g.sum():7.4f} {g.max():7.4f} "
              f"{det['elapsed']:6.1f}s")

    with open("ladder_floor_results.json", "w") as f:
        json.dump(results, f, indent=1, default=float)
    print("\nsaved ladder_floor_results.json")


if __name__ == "__main__":
    main()
