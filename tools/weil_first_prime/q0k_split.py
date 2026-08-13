#!/usr/bin/env python3
"""Split Q(φ_0,φ_k)=jump+pot+rank1+ρ and hunt a proved O(1/k).

L = jump + pot on [-1,1], a=1 (Suzuki 2.3 / (4.4)):
  jump = (1/4)∬ (u(x)-u(y))(v(x)-v(y))/|x-y|
  pot  = -1/2 ∫ log(1-t²) u(t)v(t) dt.

φ_k=cos(ω_k t), ω_k=(k+1/2)π. Then
  φ_0 φ_k = (1/2)[cos((k+1)π t)+cos(k π t)],
so pot is two cosine moments of log(1-t²). Those moments are O(1/k²)
(one IBP; log(1-t²)φ_0φ_k vanishes at ±1). Rank-one is O(1/k). The
cancellation that the Schur needs must live in jump+rank1.

Belief: if |k (jump_0k + rank1)| is bounded by an explicit constant
independent of k, §23.4 closes. If the bound exceeds ~0.21, Schur still
fails without using the cancellation more sharply.

Usage: python3 tools/weil_first_prime/q0k_split.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from ground_ray import KAPPA, TH2, rho_bilin  # noqa: E402
from ground_ray_cross import mean_k, what_k  # noqa: E402
from lower_bound import GAMMA  # noqa: E402


def phi(k: int, t: np.ndarray) -> np.ndarray:
    return np.cos((k + 0.5) * math.pi * t)


def pot_bilin(u: np.ndarray, v: np.ndarray, ts: np.ndarray) -> float:
    gap = np.maximum(1.0 - ts * ts, 1e-18)
    return -0.5 * float(np.trapezoid(np.log(gap) * u * v, ts))


def cosine_moment_log(n: int, nq: int = 20001) -> float:
    """∫_{-1}^1 log(1-t²) cos(n π t) dt. n=0,1,2,..."""
    ts = np.linspace(-1.0, 1.0, nq)
    gap = np.maximum(1.0 - ts * ts, 1e-18)
    return float(np.trapezoid(np.log(gap) * np.cos(n * math.pi * ts), ts))


def pot_closed_num(k: int) -> float:
    """pot(φ0,φk)= -1/4 ( I(k+1)+I(k) ), I(n)=∫ log(1-t²) cos(nπ t)."""
    return -0.25 * (cosine_moment_log(k + 1) + cosine_moment_log(k))


def main() -> None:
    ts = np.linspace(-1.0, 1.0, 801)
    p0 = phi(0, ts)
    print("=== pot vs jump vs rank1 vs ρ for Q(φ0,φk) ===")
    print(
        f"  {'k':>3} {'pot':>11} {'k² pot':>9} {'jump':>11} {'rank1':>11} "
        f"{'j+r1':>11} {'k(j+r1)':>9} {'ρ':>10} {'k Q':>8}"
    )
    for k in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
        pk = phi(k, ts)
        Lu = L_a(p0, ts, 1.0)
        Lv = L_a(pk, ts, 1.0)
        Luv = L_a(p0 + pk, ts, 1.0)
        L = 0.5 * (Luv - Lu - Lv)
        pot = pot_bilin(p0, pk, ts)
        pot_c = pot_closed_num(k)
        jump = L - pot
        r1 = KAPPA * mean_k(0) * mean_k(k)
        rho = rho_bilin(p0, pk, ts, 0.34657359027997264, nlag=401)
        Q = L + r1 + rho
        print(
            f"  {k:3d} {pot:+11.4e} {k*k*pot:+9.4f} {jump:+11.4e} {r1:+11.4e} "
            f"{jump+r1:+11.4e} {k*(jump+r1):+9.4f} {rho:+10.3e} {k*Q:+8.4f}"
        )
        if k <= 4:
            print(f"       pot_trap={pot:.8e}  pot_I(n)={pot_c:.8e}")

    print("\n=== I(n)=∫ log(1-t²) cos(nπ t) dt  and n² I(n) ===")
    for n in (0, 1, 2, 3, 4, 8, 16, 32, 64):
        I = cosine_moment_log(n)
        print(f"  n={n:3d}  I={I:+.8e}  n²I={n*n*I:+.6f}")

    print("\n=== VERDICT ===")
    print("  If n² I(n) converges, pot = O(1/k²) and cannot cancel rank1=O(1/k).")
    print("  Then jump must cancel rank1; k(jump+rank1) bounded is the lemma.")


if __name__ == "__main__":
    main()
