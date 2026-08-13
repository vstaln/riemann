#!/usr/bin/env python3
"""Diagnose the negative 2×2 Ritz in cosine ⊕ two-bump.

Belief this changes: whether λ_min < 0 is a genuine negative direction of
Weil's T (which would refute positivity on that a, hence RH) or a
quadrature / polarization artifact.

Checks:
  1. Direct Rayleigh of v = φ + t·bump on a t-grid (no polarization).
  2. n-convergence of that curve.
  3. Same family at a < a2 (primes off): T must stay positive if T is sane.
  4. Polarization residual: Q(φ+b) vs Q(φ)+Q(b)+2 H01.
  5. Fourier-space T on the candidate negative vector.

Usage: python3 tools/weil_first_prime/diagnose_neg.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lower_bound import (  # noqa: E402
    A2,
    A3,
    LOG2,
    linear_two_bump,
    re_psi_line,
)
from probe import T_of_G, T_parts, autocorrelation  # noqa: E402


def pair(a: float, eps: float, n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xs = np.linspace(-a, a, n)
    phi = np.cos(0.5 * math.pi * xs / a)
    _, bump, _ = linear_two_bump(a, 2.0 * eps, n)
    return xs, phi, bump


def rayleigh(v: np.ndarray, xs: np.ndarray, primes: bool) -> dict:
    a = float(xs[-1])
    dx = float(xs[1] - xs[0])
    nrm = float(np.trapezoid(v * v, xs))
    taus, G = autocorrelation(v, dx)
    parts = T_parts(taus, G, a, primes=primes)
    G0 = float(np.interp(0.0, taus, G))
    Glog2 = float(np.interp(LOG2, taus, G, left=0.0, right=0.0))
    return {
        "T": parts["T"],
        "nrm": nrm,
        "G0": G0,
        "G_log2": Glog2,
        "rayleigh": parts["T"] / nrm if nrm > 0 else float("nan"),
        "parts": parts,
    }


def fourier_T(v: np.ndarray, xs: np.ndarray, vmax: float = 120.0, nv: int = 6001) -> dict:
    a = float(xs[-1])
    dx = float(xs[1] - xs[0])
    taus, G = autocorrelation(v, dx)
    G0 = float(np.interp(0.0, taus, G))
    vs = np.linspace(-vmax, vmax, nv)
    Ghat = np.array([float(np.trapezoid(G * np.cos(vv * taus), taus)) for vv in vs])
    re_psi = re_psi_line(np.abs(vs))
    T_psi = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(re_psi * Ghat, vs))
    T_cosh = float(np.trapezoid(2.0 * np.cosh(taus / 2.0) * G, taus))
    T_arch = T_cosh - math.log(math.pi) * G0 + T_psi
    Glog2 = float(np.interp(LOG2, taus, G, left=0.0, right=0.0))
    prime = 0.0
    if 2.0 * a + 1e-14 >= LOG2:
        prime = -math.sqrt(2.0) * LOG2 * Glog2
    plancherel = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(Ghat, vs))
    nrm = float(np.trapezoid(v * v, xs))
    return {
        "T": T_arch + prime,
        "T_arch": T_arch,
        "prime": prime,
        "G0": G0,
        "nrm": nrm,
        "plancherel": plancherel,
        "rayleigh": (T_arch + prime) / nrm,
    }


def scan_t(a: float, eps: float, n: int, primes: bool, ts: np.ndarray) -> list[dict]:
    xs, phi, bump = pair(a, eps, n)
    rows = []
    for t in ts:
        v = phi + t * bump
        r = rayleigh(v, xs, primes=primes)
        r["t"] = float(t)
        rows.append(r)
    return rows


def main() -> None:
    eps = 0.10
    a = A2 + eps
    print(f"target a={a:.12f} eps={eps} (mid-ish first-prime window)")
    print(f"a2={A2:.12f} a3={A3:.12f}")

    print("\n=== n-convergence of direct Rayleigh(φ + t bump), primes on ===")
    ts = np.array([-2.0, -1.0, -0.5, -0.2, 0.0, 0.2, 0.5, 1.0, 2.0, 5.0])
    for n in (501, 1001, 2001, 4001):
        rows = scan_t(a, eps, n, primes=True, ts=ts)
        t_star = min(rows, key=lambda r: r["rayleigh"])
        print(
            f"  n={n:4d}  min_t Rayleigh={t_star['rayleigh']:+.6e} at t={t_star['t']:+.2f}  "
            f"T={t_star['T']:+.6e} nrm={t_star['nrm']:.6e} G0={t_star['G0']:.6e}"
        )
        # also print t=0 (pure cosine) and t=1
        by_t = {round(r["t"], 5): r for r in rows}
        print(
            f"         t=0 (cosine) {by_t[0.0]['rayleigh']:+.6e}  "
            f"t=1 {by_t[1.0]['rayleigh']:+.6e}"
        )
        sys.stdout.flush()

    print("\n=== fine t-scan at n=4001 ===")
    ts_fine = np.linspace(-3.0, 3.0, 31)
    rows = scan_t(a, eps, 4001, primes=True, ts=ts_fine)
    t_star = min(rows, key=lambda r: r["rayleigh"])
    print(f"  min Rayleigh={t_star['rayleigh']:+.8e} at t={t_star['t']:+.3f}")
    print(f"  {'t':>8} {'Rayleigh':>14} {'T':>14} {'G(log2)/G0':>14}")
    for r in rows:
        if abs(r["t"]) < 1e-12 or abs(abs(r["t"]) - 1.0) < 1e-12 or abs(r["t"] - t_star["t"]) < 1e-12:
            g0 = r["G0"]
            print(
                f"  {r['t']:8.3f} {r['rayleigh']:14.6e} {r['T']:14.6e} "
                f"{r['G_log2']/g0 if g0 else float('nan'):14.6e}"
            )
    n_neg = sum(1 for r in rows if r["rayleigh"] < 0)
    print(f"  negative samples: {n_neg}/{len(rows)}")

    print("\n=== polarization residual at n=2001 and n=4001 ===")
    for n in (2001, 4001):
        xs, phi, bump = pair(a, eps, n)
        dx = float(xs[1] - xs[0])
        def Q(v):
            taus, G = autocorrelation(v, dx)
            return T_of_G(taus, G, a, primes=True)
        q0, q1, qsum = Q(phi), Q(bump), Q(phi + bump)
        h01 = 0.5 * (qsum - q0 - q1)
        qpred = q0 + q1 + 2.0 * h01  # tautological
        # check Q(2φ) ≈ 4 Q(φ) (homogeneity)
        q2 = Q(2.0 * phi)
        print(
            f"  n={n}  Q(φ)={q0:.6e} Q(bump)={q1:.6e} Q(φ+b)={qsum:.6e} "
            f"H01={h01:.6e}"
        )
        print(f"         Q(2φ)/Q(φ)={q2/q0:.6f} (want 4)  |Q(2φ)-4Q(φ)|/|Q(φ)|={abs(q2-4*q0)/abs(q0):.3e}")

    print("\n=== same geometry BELOW a2 (a=0.20, width=0.05, primes off) — T must be >0 ===")
    a_lo = 0.20
    width = 0.05
    eps_fake = 0.5 * width
    ts = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
    for n in (1001, 4001):
        xs = np.linspace(-a_lo, a_lo, n)
        phi = np.cos(0.5 * math.pi * xs / a_lo)
        _, bump, _ = linear_two_bump(a_lo, width, n)
        print(f"  n={n}")
        for t in ts:
            v = phi + t * bump
            r = rayleigh(v, xs, primes=False)
            print(f"    t={t:+.1f}  Rayleigh={r['rayleigh']:+.6e}  T={r['T']:+.6e}  G0={r['G0']:.6e}")

    print("\n=== Fourier T vs probe T on φ + t*bump at the apparent minimizer ===")
    xs, phi, bump = pair(a, eps, 4001)
    tmin = t_star["t"]
    v = phi + tmin * bump
    rp = rayleigh(v, xs, primes=True)
    rf = fourier_T(v, xs)
    print(f"  t={tmin:.3f}")
    print(f"  probe   Rayleigh={rp['rayleigh']:+.8e}  T={rp['T']:+.8e}  G0={rp['G0']:.8e} nrm={rp['nrm']:.8e}")
    print(
        f"  fourier Rayleigh={rf['rayleigh']:+.8e}  T={rf['T']:+.8e}  "
        f"plancherel={rf['plancherel']:.8e} G0={rf['G0']:.8e}"
    )
    p = rp["parts"]
    print(
        f"  probe parts: T={p['T']:+.6e} cosh={p['cosh']:+.6e} const={p['const']:+.6e} "
        f"arch_int={p['arch_int']:+.6e} primes={p['primes']:+.6e}"
    )

    print("\n=== VERDICT ===")
    # Recompute min on finest grid
    fine = scan_t(a, eps, 4001, True, np.linspace(-3, 3, 31))
    m = min(fine, key=lambda r: r["rayleigh"])
    lo = scan_t(0.20, 0.025, 4001, False, np.array([-2.0, -1.0, 0.0, 1.0, 2.0]))
    lo_min = min(r["rayleigh"] for r in lo)
    print(f"  finest mixed min Rayleigh at a=a2+0.1: {m['rayleigh']:+.6e} (t={m['t']:+.3f})")
    print(f"  below-a2 mixed min Rayleigh: {lo_min:+.6e}")
    if m["rayleigh"] < 0 and lo_min > 0:
        print("  SIGN: mixed direction negative past a2, positive below a2.")
        print("  Still NOT a disproof: need grid-converged T and Fourier agreement.")
    elif m["rayleigh"] >= 0:
        print("  Direct Rayleigh stayed non-negative on the t-grid — 2×2 negative")
        print("  eigenvalue was a polarization/quadrature artifact.")
    if lo_min < 0:
        print("  FAIL T: negative Rayleigh below a2. T implementation is wrong.")


if __name__ == "__main__":
    main()
