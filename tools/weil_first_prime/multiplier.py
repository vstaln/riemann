#!/usr/bin/env python3
"""Fourier multiplier of Weil T on the first-prime window.

Bombieri (12.3) + prime 2: for even G = v*ṽ, Ĝ ≥ 0,
  T[G] = (1/2π) ∫ M_a(ξ) Ĝ(ξ) dξ
with
  M_a(ξ) = k̂_a(ξ) + Re ψ(1/4 + iξ/2) − log π − √2 log 2 · 1_{2a ≥ log 2} cos(ξ log 2)
  k̂_a(ξ) = ∫_{-A}^{A} 2 cosh(x/2) cos(ξ x) dx,   A = 2a.

If inf_ξ M_a(ξ) > 0 then T ≥ (inf M) ‖v‖² on that a. Paley–Wiener is not
needed: Ĝ = |v̂|² ≥ 0 for every v.

Belief this changes: whether first-prime survival is a 1D infimum of an
explicit function (a proof, once the inf is certified) or whether M dips
below 0 and the type constraint is load-bearing (Yoshida's matrix).

Usage: python3 tools/weil_first_prime/multiplier.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lower_bound import LOG2, PRIME2_COEFF, re_psi_line, PSI_QUARTER  # noqa: E402
from probe import A2, A3, T_of_G, autocorrelation  # noqa: E402


def Iexp(alpha: float, A: float, xi: np.ndarray) -> np.ndarray:
    """∫_0^A e^{αx} cos(ξ x) dx, vectorized in ξ."""
    xi = np.asarray(xi, dtype=np.float64)
    d = alpha * alpha + xi * xi
    end = np.exp(alpha * A) * (alpha * np.cos(xi * A) + xi * np.sin(xi * A)) / d
    start = alpha / d
    out = end - start
    # ξ=α=0 limit: ∫_0^A 1 dx = A; α=0,ξ=0 already handled if d=0
    d0 = d < 1e-30
    if np.any(d0):
        out = np.where(d0, A if abs(alpha) < 1e-15 else (np.exp(alpha * A) - 1.0) / alpha, out)
    return out


def khat(a: float, xi: np.ndarray) -> np.ndarray:
    """FT of 2 cosh(x/2) 1_{|x|≤2a}."""
    A = 2.0 * a
    return 2.0 * (Iexp(0.5, A, xi) + Iexp(-0.5, A, xi))


def M_a(a: float, xi: np.ndarray, primes: bool) -> np.ndarray:
    xi = np.asarray(xi, dtype=np.float64)
    re_psi = re_psi_line(np.abs(xi))
    m = khat(a, xi) + re_psi - math.log(math.pi)
    if primes and (2.0 * a + 1e-14 >= LOG2):
        m = m - PRIME2_COEFF * np.cos(xi * LOG2)
    return m


def inf_M(a: float, primes: bool, xi_max: float = 80.0, n: int = 40001) -> dict:
    xi = np.linspace(0.0, xi_max, n)  # even in ξ
    m = M_a(a, xi, primes=primes)
    i = int(np.argmin(m))
    return {
        "a": a,
        "inf": float(m[i]),
        "xi_at_inf": float(xi[i]),
        "M0": float(m[0]),
        "M_end": float(m[-1]),
    }


def fourier_T_via_M(v: np.ndarray, xs: np.ndarray, primes: bool, vmax: float = 80.0, nv: int = 8001) -> float:
    """T = (1/2π) ∫ M(ξ) Ĝ(ξ) dξ, for a cross-check against probe."""
    a = float(xs[-1])
    dx = float(xs[1] - xs[0])
    taus, G = autocorrelation(v, dx)
    vs = np.linspace(-vmax, vmax, nv)
    Ghat = np.array([float(np.trapezoid(G * np.cos(vv * taus), taus)) for vv in vs])
    m = M_a(a, vs, primes=primes)
    return (1.0 / (2.0 * math.pi)) * float(np.trapezoid(m * Ghat, vs))


def main() -> None:
    print("=== khat sanity: k̂(0) = ∫_{-A}^A 2 cosh(x/2) dx = 8 sinh(A/2) wait ===")
    # ∫_{-A}^A 2 cosh(x/2) dx = 8 sinh(A/2)
    for a in (0.10, 0.20, A2, 0.5 * (A2 + A3)):
        A = 2.0 * a
        k0 = float(khat(a, np.array([0.0]))[0])
        closed = 8.0 * math.sinh(A / 2.0)
        # wait: ∫_{-A}^A 2 cosh(x/2) dx = 4 * 2 sinh(A/2) = 8 sinh(A/2). Yes.
        print(f"  a={a:.6f}  k̂(0)={k0:.12f}  8 sinh(a)={8*math.sinh(a):.12f}  8 sinh(A/2)={closed:.12f}  err={k0-closed:.3e}")

    print("\n=== Fourier-M T vs probe T (a=0.20, cosine, no primes) ===")
    a = 0.20
    xs = np.linspace(-a, a, 801)
    v = np.cos(0.5 * math.pi * xs / a)
    dx = float(xs[1] - xs[0])
    taus, G = autocorrelation(v, dx)
    Tp = T_of_G(taus, G, a, primes=False)
    Tf = fourier_T_via_M(v, xs, primes=False)
    nrm = float(np.trapezoid(v * v, xs))
    print(f"  T_probe={Tp:.8e}  T_M={Tf:.8e}  rel={abs(Tf-Tp)/abs(Tp):.3e}  T/‖v‖² probe={Tp/nrm:.8e}")

    print("\n=== inf_ξ M_a(ξ)  (if >0, positivity of T on that a) ===")
    print(f"{'label':<18} {'a':>10} {'primes':>6} {'inf M':>14} {'ξ*':>10} {'M(0)':>12} {'M(80)':>12}")
    rows = []
    for label, aa, pr in [
        ("a=0.10", 0.10, False),
        ("a=0.20", 0.20, False),
        ("a2-noprime", A2, False),
        ("a2-prime", A2, True),
        ("a2+1e-3", A2 + 1e-3, True),
        ("a2+0.01", A2 + 0.01, True),
        ("mid", 0.5 * (A2 + A3), True),
        ("a3", A3, True),
        ("a2+0.05", A2 + 0.05, True),
    ]:
        r = inf_M(aa, pr)
        rows.append((label, r))
        print(
            f"{label:<18} {r['a']:10.6f} {int(pr):6d} {r['inf']:14.6e} "
            f"{r['xi_at_inf']:10.4f} {r['M0']:12.6e} {r['M_end']:12.6e}"
        )
        sys.stdout.flush()

    print("\n=== M_mid(ξ) samples (a=(a2+a3)/2, primes on) ===")
    a_mid = 0.5 * (A2 + A3)
    for xi in (0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0, 16.8, 20.0, 40.0, 80.0):
        m = float(M_a(a_mid, np.array([xi]), True)[0])
        print(f"  ξ={xi:8.2f}  M={m:+.8f}")

    print("\n=== VERDICT ===")
    infs = [(lab, r["inf"], r["xi_at_inf"]) for lab, r in rows]
    worst = min(infs, key=lambda t: t[1])
    print(f"  worst inf M = {worst[1]:.6e} at {worst[0]} (ξ*={worst[2]:.4f})")
    pos = [t for t in infs if t[1] > 0]
    neg = [t for t in infs if t[1] <= 0]
    if neg:
        print("  M dips ≤ 0 on some listed a — pointwise multiplier does NOT prove positivity.")
        print("  Paley–Wiener type constraint is load-bearing (Yoshida matrix).")
    if pos:
        print("  M > 0 on: " + ", ".join(t[0] for t in pos))
    print("  LABEL: CHECKED NUMERICALLY on a 0..80 grid, n=40001. Not an interval inf.")


if __name__ == "__main__":
    main()
