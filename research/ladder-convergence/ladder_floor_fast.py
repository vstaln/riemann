#!/usr/bin/env python3
"""FAST pure block-size floor ladder — eps_atom(n) = min tr Psi(G_n)/n over
consecutive gaps u>0, span<=4.  Bounded scan + L-BFGS-B refinement, no DE.

Labels: CHECKED NUMERICALLY (estimate, not an interval certificate).
Run: cd research/ladder-convergence && uv run --quiet --with numpy --with scipy python ladder_floor_fast.py
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(7)
SQ2 = np.sqrt(2.0)
PI = np.pi


def _K(x):
    x = np.asarray(x, dtype=float)
    a = (SQ2 - 2 * PI * x) / 2.0
    b = (SQ2 + 2 * PI * x) / 2.0
    return 0.5 * (np.sinc(a / PI) + np.sinc(b / PI))


K0 = float(_K(0.0))


def k(x):
    return _K(x) / K0


def psi(t):
    return np.where(t <= 2.0, (t - 1.0) ** 2, 2.0 * t - 3.0)


def tr_psi_gaps(u):
    m = len(u) + 1
    y = np.concatenate([[0.0], np.cumsum(u)])
    G = k(y[None, :] - y[:, None])
    w = np.linalg.eigvalsh(G)
    return psi(w).sum()


def pair_sq(u):
    m = len(u) + 1
    y = np.concatenate([[0.0], np.cumsum(u)])
    G = k(y[None, :] - y[:, None])
    return 2.0 * np.sum(G * G) - 2.0 * m  # 2*sum_{i<j} G_ij^2


def sample_gaps(n, N):
    """Dirichlet-scaled + patterned starts on the span<=4 simplex."""
    out = []
    for _ in range(N):
        g = rng.dirichlet(np.ones(n - 1)) * rng.uniform(0.2, 4.0)
        out.append(g)
    # kernel-zero-tile patterned starts (near-orthogonal blocks)
    zs = [1.0572, 2.0300, 3.0202]
    for z in zs:
        g = np.full(n - 1, z / (n - 1))
        if g.sum() <= 4.0:
            out.append(g)
        for z2 in zs:
            g = np.array([z, z2] * ((n - 1) // 2) + [z] * ((n - 1) % 2))
            if g.sum() <= 4.0:
                out.append(g)
    return np.array(out)


def min_floor(n, N=4000):
    starts = sample_gaps(n, N)
    best, best_u = None, None
    vals = np.array([tr_psi_gaps(u) / n for u in starts])
    for i in np.argsort(vals)[:25]:
        u0 = starts[i]

        def pen(u):
            s = u.sum()
            return tr_psi_gaps(np.abs(u)) / n + 1e5 * max(0.0, s - 4.0) ** 2

        r = minimize(pen, u0, method="L-BFGS-B",
                     bounds=[(1e-4, 4.0)] * (n - 1),
                     options={"maxiter": 400})
        if best is None or r.fun < best:
            best, best_u = r.fun, np.abs(r.x)
    # final SLSQP constrained pass
    for i in np.argsort(vals)[:5]:
        u0 = starts[i]
        cons = {"type": "ineq", "fun": lambda u: 4.0 - u.sum()}
        r = minimize(lambda u: tr_psi_gaps(u) / n, u0, method="SLSQP",
                     bounds=[(1e-4, 4.0)] * (n - 1), constraints=cons,
                     options={"maxiter": 300})
        if best is None or r.fun < best:
            best, best_u = r.fun, r.x
    return best, best_u


def main():
    print("=" * 70)
    print("PURE BLOCK-SIZE FLOOR LADDER  eps_atom(n) = min tr Psi(G_n)/n")
    print("domain u>0 span<=4  |  labels: CHECKED NUMERICALLY (estimate)")
    print("=" * 70)
    print(f"K(0) = {K0:.15f}")
    for x in (0.3, 1.0, 1.5, 2.0, 3.0):
        print(f"  k({x}) = {k(x):+.6f}")
    rows = []
    for n in (3, 4, 5, 7, 9, 11, 15, 21, 30):
        b, u = min_floor(n)
        e_pair = pair_sq(u) / (2 * n)
        rows.append((n, b, u.sum(), u.max(), e_pair))
        print(f"n={n:2d}  eps_atom={b:.6e}  eps_block={b*n:.6e}  "
              f"span={u.sum():.4f}  maxgap={u.max():.4f}  E_pair/2n={e_pair:.6e}",
              flush=True)
    # bound formulas
    H0 = 1.5 - (1.0 / SQ2) / np.tan(1.0 / SQ2)
    print("\nH0 =", f"{H0:.15f}")
    for n, b, *_ in rows:
        e = b  # per-atom floor (n>=2, approximating the 7-pt per-atom form)
        # 3-point form: (H0 - e/4)/(1 - e/2)
        b3 = (H0 - e / 4.0) / (1.0 - e / 2.0)
        # 7-point form per ainta: (1345000*H0 - 2680)/1340003 at e=19/5000/7
        print(f"n={n:2d}  eps={e:.4e}  bound_3pt_form={b3:.9f}  "
              f"delta_vs_6725={b3-H0:+.6e}")
    print("\nCEILING 0.6818312305953419 | external best 0.6731929114731422")


if __name__ == "__main__":
    main()
