#!/usr/bin/env python3
"""L_a (Suzuki 2.3) vs prime-2 Hankel on two families.

Belief: the Beurling–Deny jumping form between the two log-2 strips
does *not* dominate the Hankel ∫ u(s)u(2ε−s) ds, because for even v the
Hankel pairs even-symmetric points where |v(x)−v(y)| can be small.
If L_a(two-bump) + C‖v‖² fails to beat |prime2| while T stays positive,
the Dirichlet form is not the absorbing mechanism (archimedean ψ is).

Usage: python3 tools/weil_first_prime/dirichlet_vs_prime.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lower_bound import A2, A3, LOG2, PRIME2_COEFF, linear_two_bump  # noqa: E402
from probe import T_of_G, autocorrelation  # noqa: E402


def L_a(v: np.ndarray, xs: np.ndarray, a: float) -> float:
    """Suzuki (2.3), trapezoid. Diagonal of the double integral is skipped
    (the 1/|x-y| singularity is integrable in 2D against |v(x)-v(y)|² ~ |x-y|²)."""
    n = len(xs)
    dx = float(xs[1] - xs[0])
    w = np.full(n, dx)
    w[0] *= 0.5
    w[-1] *= 0.5
    jump = 0.0
    for i in range(n):
        di = xs[i] - xs
        mask = np.abs(di) > 1e-14
        dv2 = (v[i] - v) ** 2
        jump += float(np.sum((dv2[mask] / np.abs(di[mask])) * w[mask])) * w[i]
    jump *= 0.25
    # log(a²−x²): clip off the endpoints where v=0 anyway
    gap = np.maximum(a * a - xs * xs, 1e-18)
    pot = -0.5 * float(np.sum(np.log(gap) * (v * v) * w))
    return jump + pot


def rayleigh_T(v: np.ndarray, xs: np.ndarray, primes: bool) -> float:
    a = float(xs[-1])
    dx = float(xs[1] - xs[0])
    nrm = float(np.trapezoid(v * v, xs))
    taus, G = autocorrelation(v, dx)
    return T_of_G(taus, G, a, primes=primes) / nrm


def G_log2_over_G0(v: np.ndarray, xs: np.ndarray) -> float:
    dx = float(xs[1] - xs[0])
    taus, G = autocorrelation(v, dx)
    g0 = float(np.interp(0.0, taus, G))
    gl = float(np.interp(LOG2, taus, G, left=0.0, right=0.0))
    return gl / g0, g0


def main() -> None:
    print(f"{'family':<10} {'eps':>8} {'L_a/G0':>12} {'prime/G0':>12} {'T/G0':>12} {'L+p':>12}")
    rows = []
    for eps in (0.01, 0.05, 0.10, A3 - A2 - 1e-3):
        a = A2 + eps
        n = 801
        xs = np.linspace(-a, a, n)
        # cosine
        phi = np.cos(0.5 * math.pi * xs / a)
        # two-bump saturating
        _, bump, _ = linear_two_bump(a, 2.0 * eps, n)
        for name, v in (("cosine", phi), ("twobump", bump)):
            nrm = float(np.trapezoid(v * v, xs))
            La = L_a(v, xs, a)
            ratio, g0 = G_log2_over_G0(v, xs)
            pterm = -PRIME2_COEFF * ratio  # /G0
            Trel = rayleigh_T(v, xs, primes=True)
            rec = {
                "name": name,
                "eps": eps,
                "La": La / nrm,
                "prime": pterm,
                "T": Trel,
                "Lap": La / nrm + pterm,
            }
            rows.append(rec)
            print(
                f"{name:<10} {eps:8.4f} {rec['La']:12.6f} {rec['prime']:12.6f} "
                f"{rec['T']:12.6f} {rec['Lap']:12.6f}"
            )
            sys.stdout.flush()

    print("\n=== VERDICT ===")
    tb = [r for r in rows if r["name"] == "twobump"]
    # If L_a + prime goes negative while T stays positive, Dirichlet form is not the absorber.
    if any(r["Lap"] < 0 < r["T"] for r in tb):
        print("  CHECKED: L_a + prime-2 < 0 on two-bump while T>0.")
        print("  The jumping form does NOT absorb prime 2. Archimedean ψ / Gårding does.")
    elif all(r["Lap"] > 0 for r in tb):
        print("  L_a + prime-2 stayed positive on two-bump (does not prove absorption).")
    print("  Cosine is the dangerous (low-frequency) family; two-bump is Gårding-protected.")


if __name__ == "__main__":
    main()
