#!/usr/bin/env python3
"""Dirichlet matrix of T via the Fourier multiplier (explicit sinc).

φ_j(x)=cos(ω_j x) on [-a,a], ω_j=(j+1/2)π/a.
φ̂_j(ξ) = 2 ω_j (-1)^j cos(a ξ) / (ω_j² − ξ²)   (even FT ∫ φ e^{-iξx} dx),
with removable singularity at ξ=±ω_j equal to a.

H_jk = (1/2π) ∫_{-∞}^{∞} M_a(ξ) φ̂_j(ξ) φ̂_k(ξ) dξ,
M_a from multiplier.py (Bombieri 12.3 + prime 2).

Belief: frequency-side integrand is C^∞ (removable poles) decaying as
log|ξ|/ξ^4, so the 10^{-5} τ-quadrature bias of T_of_G should disappear.

Usage: python3 tools/weil_first_prime/dirichlet_ft.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multiplier import M_a  # noqa: E402
from probe import A2, A3  # noqa: E402


def omega(j: int, a: float) -> float:
    return (j + 0.5) * math.pi / a


def phihat(j: int, a: float, xi: np.ndarray) -> np.ndarray:
    """Even Fourier transform ∫_{-a}^a cos(ω_j x) e^{-iξx} dx.

    Closed form: 2 ω_j (-1)^j cos(a ξ) / (ω_j² − ξ²), with value a at ξ = ±ω_j.
    """
    w = omega(j, a)
    xi = np.asarray(xi, dtype=np.float64)
    sgn = 1.0 if (j % 2 == 0) else -1.0  # (-1)^j
    den = w * w - xi * xi
    out = np.empty_like(xi)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = 2.0 * w * sgn * np.cos(a * xi) / den
    out = np.where(np.abs(den) < 1e-10 * (w * w + 1.0), a, out)
    return out


def H_from_M(a: float, Mmodes: int, primes: bool, xi_max: float = 200.0, n: int = 20001) -> np.ndarray:
    xi = np.linspace(-xi_max, xi_max, n)
    m = M_a(a, xi, primes=primes)
    hats = [phihat(j, a, xi) for j in range(Mmodes)]
    H = np.zeros((Mmodes, Mmodes))
    for j in range(Mmodes):
        for k in range(j, Mmodes):
            integ = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(m * hats[j] * hats[k], xi))
            H[j, k] = H[k, j] = integ
    return H


def main() -> None:
    print("=== φ̂ sanity: φ̂_j(ω_j) limit = a,  (1/2π)∫ |φ̂|² = ‖φ‖² = a ===")
    a = 0.20
    xi = np.linspace(-120.0, 120.0, 24001)
    for j in (0, 1, 2):
        h = phihat(j, a, xi)
        w = omega(j, a)
        # value near ω
        i = int(np.argmin(np.abs(xi - w)))
        plan = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(h * h, xi))
        print(f"  j={j} ω={w:.6f}  φ̂(near ω)={h[i]:.6f} (want a={a})  Plancherel={plan:.6f} (want a)")

    print("\n=== min eig via M-integral vs known probes ===")
    print(f"{'label':<16} {'a':>10} {'M':>3} {'nξ':>6} {'λ_min':>14} {'R00':>12}")
    specs = [
        ("a20-M4", 0.20, 4, 20001, False),
        ("a2-M4", A2, 4, 20001, True),
        ("a2-M6", A2, 6, 20001, True),
        ("mid-M4", 0.5 * (A2 + A3), 4, 20001, True),
        ("mid-M6", 0.5 * (A2 + A3), 6, 20001, True),
        ("mid-M8", 0.5 * (A2 + A3), 8, 20001, True),
        ("a3-M6", A3, 6, 20001, True),
    ]
    results = {}
    for label, aa, Mm, nxi, pr in specs:
        H = H_from_M(aa, Mm, pr, xi_max=200.0, n=nxi)
        R = H / aa
        lam = float(np.min(np.linalg.eigvalsh(0.5 * (R + R.T))))
        results[label] = (lam, R)
        print(f"{label:<16} {aa:10.6f} {Mm:3d} {nxi:6d} {lam:14.6e} {R[0,0]:12.6e}")
        sys.stdout.flush()

    print("\n=== ξ-grid convergence at mid M=4 ===")
    a_mid = 0.5 * (A2 + A3)
    for nxi, xmax in ((5001, 80.0), (10001, 120.0), (20001, 200.0), (40001, 300.0)):
        H = H_from_M(a_mid, 4, True, xi_max=xmax, n=nxi)
        R = H / a_mid
        lam = float(np.min(np.linalg.eigvalsh(0.5 * (R + R.T))))
        print(f"  nξ={nxi:5d} xmax={xmax:6.1f}  λ={lam:.10e}  R00={R[0,0]:.10e}")

    print("\n=== a-sweep, prime 2 only, frequency-side H (nξ=20001, xmax=200) ===")
    print(f"{'a':>10} {'eps':>10} {'M6':>14} {'M8':>14}")
    sweep_as = [
        A2, A2 + 1e-3, A2 + 0.01, A2 + 0.02, A2 + 0.05,
        A2 + 0.10, 0.5 * (A2 + A3), A2 + 0.15, A3 - 0.02,
        A3 - 0.005, A3 - 1e-3, A3 - 1e-4,
    ]
    for aa in sweep_as:
        H6 = H_from_M(aa, 6, True, xi_max=200.0, n=20001)
        H8 = H_from_M(aa, 8, True, xi_max=200.0, n=20001)
        l6 = float(np.min(np.linalg.eigvalsh(0.5 * (H6 + H6.T) / aa)))
        l8 = float(np.min(np.linalg.eigvalsh(0.5 * (H8 + H8.T) / aa)))
        print(f"{aa:10.6f} {aa - A2:10.6f} {l6:14.6e} {l8:14.6e}")
        sys.stdout.flush()

    print("\n=== VERDICT ===")
    print(f"  a20 M=4 λ={results['a20-M4'][0]:.8e}  (τ-method ~1.07327e-1)")
    print(f"  a2  M=6 λ={results['a2-M6'][0]:.8e}  (τ-method ~1.56e-3)")
    print(f"  mid M=8 λ={results['mid-M8'][0]:.8e}")
    print("  If this is grid-stable and positive, the 10^{-5} is a real subspace gap,")
    print("  not a τ-trapezoid artifact. Still an UPPER bound on λ_true.")


if __name__ == "__main__":
    main()
