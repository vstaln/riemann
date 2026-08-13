#!/usr/bin/env python3
"""Even-Dirichlet matrix of Weil T from closed-form cross-correlations.

φ_j(x) = cos(ω_j x) on [-a,a], ω_j = (j+1/2) π/a, φ_j(±a)=0.
C_jk(τ) = ∫ φ_j(x) φ_k(x-τ) dx has an elementary antiderivative.
H_jk = T[ (C_jk + C_kj)/2 ] with T from probe.T_of_G.

Belief this changes: whether the 10^{-5} mid-window Ritz gap is a spatial-grid
artifact, and how large |H_0j| stays when G is exact (Gershgorin already failed
on the gridded matrix).

Usage: python3 tools/weil_first_prime/dirichlet_matrix.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe import A2, A3, T_of_G, T_parts  # noqa: E402


def omega(j: int, a: float) -> float:
    return (j + 0.5) * math.pi / a


def _int_cos_linear(p: float, q: float, lo: float, hi: float) -> float:
    """∫_{lo}^{hi} cos(p x + q) dx."""
    if abs(p) < 1e-14:
        return (hi - lo) * math.cos(q)
    return (math.sin(p * hi + q) - math.sin(p * lo + q)) / p


def C_jk(j: int, k: int, a: float, tau: float) -> float:
    """∫ φ_j(x) φ_k(x-τ) dx, any real τ. Zero if |τ| ≥ 2a."""
    if tau >= 2.0 * a - 1e-15 or tau <= -2.0 * a + 1e-15:
        return 0.0
    wj, wk = omega(j, a), omega(k, a)
    # x ∈ [-a,a] ∩ [τ-a, τ+a]
    lo = max(-a, tau - a)
    hi = min(a, tau + a)
    if hi <= lo:
        return 0.0
    # cos(wj x) cos(wk(x-τ)) = (1/2)[ cos((wj+wk)x - wk τ) + cos((wj-wk)x + wk τ) ]
    return 0.5 * (
        _int_cos_linear(wj + wk, -wk * tau, lo, hi)
        + _int_cos_linear(wj - wk, wk * tau, lo, hi)
    )


def G_sym_samples(j: int, k: int, a: float, n_tau: int) -> tuple[np.ndarray, np.ndarray]:
    """Even-in-τ samples of (C_jk(τ)+C_kj(τ))/2 on a symmetric grid."""
    taus = np.linspace(-2.0 * a, 2.0 * a, n_tau)
    gs = np.empty_like(taus)
    for i, t in enumerate(taus):
        gs[i] = 0.5 * (C_jk(j, k, a, float(t)) + C_jk(k, j, a, float(t)))
    return taus, gs


def H_entry(j: int, k: int, a: float, primes: bool, n_tau: int = 2001) -> float:
    taus, G = G_sym_samples(j, k, a, n_tau)
    return T_of_G(taus, G, a, primes=primes)


def mass(j: int, a: float) -> float:
    """‖φ_j‖² = a (exactly, ∫_{-a}^a cos²(ω_j x) dx = a)."""
    return a


def self_checks() -> None:
    a = 0.20
    # C_jj(0) = ‖φ_j‖² = a
    for j in range(4):
        c0 = C_jk(j, j, a, 0.0)
        if abs(c0 - a) > 1e-10:
            print(f"FAIL C_{j}{j}(0)={c0} want {a}")
            sys.exit(1)
    # orthogonality at τ=0
    for j in range(3):
        for k in range(j + 1, 4):
            c0 = C_jk(j, k, a, 0.0)
            if abs(c0) > 1e-10:
                print(f"FAIL C_{j}{k}(0)={c0} want 0")
                sys.exit(1)
    # G even: C_jk(τ)+C_kj(τ) even in τ
    t = 0.07
    s1 = C_jk(0, 1, a, t) + C_jk(1, 0, a, t)
    s2 = C_jk(0, 1, a, -t) + C_jk(1, 0, a, -t)
    if abs(s1 - s2) > 1e-12:
        print("FAIL G not even", s1, s2)
        sys.exit(1)
    print("  PASS C_jk self-checks (mass, orthogonality, evenness)")


def build_R(a: float, M: int, primes: bool, n_tau: int) -> tuple[np.ndarray, np.ndarray]:
    H = np.zeros((M, M))
    for j in range(M):
        H[j, j] = H_entry(j, j, a, primes, n_tau)
        for k in range(j + 1, M):
            H[j, k] = H[k, j] = H_entry(j, k, a, primes, n_tau)
    B = a * np.eye(M)
    R = H / a  # Rayleigh matrix, B = a I
    return H, R


def min_eig_R(R: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh(0.5 * (R + R.T))))


def main() -> None:
    print("=== C_jk self-checks ===")
    self_checks()

    print("\n=== closed-form G vs probe: φ_0 Rayleigh at a=0.20 (no primes) ===")
    a = 0.20
    taus, G = G_sym_samples(0, 0, a, 2001)
    T = T_of_G(taus, G, a, primes=False)
    print(f"  G(0)={G[len(G)//2]:.12f}  (want a={a})")
    print(f"  T/a = {T/a:.12f}")

    print("\n=== min eig of exact-G Dirichlet matrix ===")
    print(f"{'label':<16} {'a':>10} {'M':>3} {'nτ':>5} {'primes':>6} {'λ_min':>14} {'R00':>12}")
    specs = [
        ("a20", 0.20, 4, 1001, False),
        ("a2", A2, 4, 1001, True),
        ("a2-M6", A2, 6, 1001, True),
        ("mid-M4", 0.5 * (A2 + A3), 4, 1001, True),
        ("mid-M6", 0.5 * (A2 + A3), 6, 1001, True),
        ("mid-M8", 0.5 * (A2 + A3), 8, 1001, True),
        ("a3-M6", A3, 6, 1001, True),
    ]
    results = {}
    for label, aa, M, nt, pr in specs:
        H, R = build_R(aa, M, pr, nt)
        lam = min_eig_R(R)
        results[label] = (lam, R)
        print(f"{label:<16} {aa:10.6f} {M:3d} {nt:5d} {int(pr):6d} {lam:14.6e} {R[0,0]:12.6e}")
        sys.stdout.flush()

    print("\n=== |R_0j| at mid-window, M=8, closed-form G ===")
    R = results["mid-M8"][1]
    print("  j  Rjj          |R0j|        |R0j|/R00")
    for j in range(R.shape[0]):
        print(
            f"  {j:1d}  {R[j,j]:12.6e} {abs(R[0,j]):12.6e} {abs(R[0,j])/abs(R[0,0]):10.3f}"
        )
    schur = R[0, 0] - sum(R[0, j] ** 2 / R[j, j] for j in range(1, R.shape[0]))
    print(f"  naive diagonal Schur  R00 − Σ_j |R0j|²/Rjj = {schur:.6e}")
    print(f"  (negative Schur + positive min-eig ⇒ positivity is a coherent cancellation)")

    print("\n=== nτ-convergence of λ_min at mid, M=4 ===")
    a_mid = 0.5 * (A2 + A3)
    for nt in (501, 1001, 2001):
        _, R = build_R(a_mid, 4, True, nt)
        print(f"  nτ={nt:4d}  λ_min={min_eig_R(R):.8e}  R00={R[0,0]:.8e}")

    print("\n=== VERDICT ===")
    print(f"  λ_min(a2, M=6)  = {results['a2-M6'][0]:.6e}  (should be ~1.5e-3, >0)")
    print(f"  λ_min(mid, M=8) = {results['mid-M8'][0]:.6e}")
    print("  Closed-form G removes the spatial grid; remaining error is 1D τ-quadrature.")
    print("  Still an UPPER bound on λ_true (finite subspace). Not a proof.")


if __name__ == "__main__":
    main()
