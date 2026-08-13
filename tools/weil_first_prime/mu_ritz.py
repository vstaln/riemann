#!/usr/bin/env python3
"""Ritz of L on even Dirichlet: stability of μ1, μ2.

Belief: if μ2 stays ~1.96 as M grows, the even mean-zero subspace
has a spectral gap above threshold(a3)≈1.815 (still an UPPER bound of
μ2; a lower bound is the missing lemma). If μ2_Ritz falls below 1.815,
the complement strategy cannot reach a3 even as a hope.

Usage: python3 tools/weil_first_prime/mu_ritz.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from lower_bound import A2, A3  # noqa: E402
from screw_kernel import A_SUZUKI  # noqa: E402

C2A1 = 2.0 * A_SUZUKI + 1.0


def ritz(n: int, M: int) -> np.ndarray:
    ts = np.linspace(-1.0, 1.0, n)
    phis = [np.cos((k + 0.5) * math.pi * ts) for k in range(M)]
    Lmat = np.zeros((M, M))
    B = np.zeros((M, M))
    for j in range(M):
        for i in range(j, M):
            u, v = phis[i], phis[j]
            Lu = L_a(u, ts, 1.0)
            Lv = L_a(v, ts, 1.0)
            Luv = L_a(u + v, ts, 1.0)
            Lmat[i, j] = Lmat[j, i] = 0.5 * (Luv - Lu - Lv)
            B[i, j] = B[j, i] = float(np.trapezoid(u * v, ts))
    return np.sort(np.real(np.linalg.eigvals(np.linalg.solve(B, Lmat))))


def main() -> None:
    th2 = C2A1 + math.log(A2)
    th3 = C2A1 + math.log(A3)
    print(f"  threshold(a2)={th2:.8f}  threshold(a3)={th3:.8f}")
    print(f"{'M':>3} {'n':>5} {'μ1':>12} {'μ2':>12} {'μ3':>12}")
    for M in (3, 5, 7):
        ev = ritz(151, M)
        print(f"{M:3d} {151:5d} {ev[0]:12.8f} {ev[1]:12.8f} {ev[2]:12.8f}")
        sys.stdout.flush()
    print("n-convergence M=5:")
    for n in (81, 151, 201):
        ev = ritz(n, 5)
        print(f"  n={n} μ1={ev[0]:.8f} μ2={ev[1]:.8f}")


if __name__ == "__main__":
    main()
