#!/usr/bin/env python3
"""Even/odd/mean-zero Poincaré for Suzuki (4.5) — the local-δ obstruction.

(4.5) on [-1,1]:
  R = log(1/a)−(2A+1) + L/‖w‖² + (7/4)a (∫w)²/‖w‖²
      + ρ-term + prime-Hankel
with ρ-term = −a/‖w‖² ∬ ρ''(a(x−y)) w w,  ρ''=r''+7/4.

Already CHECKED: the cosine has
  log-c+L+rank1 = −0.00657 at a₂  (below threshold),
  ρ-term = +0.00922  (saves it).
So any proof that *drops* ρ cannot cross a₂ even on the approximate
ground state. This script:

  1. Splits L = jump + potential on even/odd/plateau families.
  2. Ritz of L (μ1 upper bound) and of J_a = L+(7/4)a(∫)².
  3. For w≥0: ρ''≤−c t² ⇒ ρ-term ≥ 2c a³ (∫w)(∫x² w)/‖w‖²
     (even: ∬(x−y)² ww = 2(∫w)(∫x² w)). Checks whether J+ρ_lower
     clears the threshold on the nonnegative unimodal family.
  4. Odd / mean-zero even: rank-one vanishes; compare L to threshold.

Belief: if J+ρ_lower stays above threshold+prime on the unimodal
nonnegative family *and* mean-zero L is above threshold, that is a
candidate lemma for explicit δ — still a local theorem, not RH.
If the plateau (almost-constant) undercuts, the dangerous direction
is the boundary-layer, not the cosine.

Usage: python3 tools/weil_first_prime/poincare_even.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from lower_bound import A2, A3, LOG2, PRIME2_COEFF, linear_two_bump  # noqa: E402
from remainder_bound import hankel_lag  # noqa: E402
from rpp_closed import rpp_closed  # noqa: E402
from screw_kernel import A_SUZUKI  # noqa: E402

A = A_SUZUKI
C2A1 = 2.0 * A + 1.0
THRESHOLD = lambda a: C2A1 + math.log(a)  # need L/n + rank1 + ρ + prime ≥ this
# wait: R = log(1/a)−(2A+1) + ⋯ = −( (2A+1)+log a ) + ⋯
# positivity ⇔ L/n + rank1 + ρ + prime ≥ (2A+1)+log a.


def L_split(w: np.ndarray, ts: np.ndarray) -> dict:
    """L = jump + potential on [-1,1] (a=1 in (2.3)/(4.4))."""
    n = len(ts)
    dx = float(ts[1] - ts[0])
    wt = np.full(n, dx)
    wt[0] *= 0.5
    wt[-1] *= 0.5
    jump = 0.0
    for i in range(n):
        di = ts[i] - ts
        mask = np.abs(di) > 1e-14
        dv2 = (w[i] - w) ** 2
        jump += float(np.sum((dv2[mask] / np.abs(di[mask])) * wt[mask])) * wt[i]
    jump *= 0.25
    gap = np.maximum(1.0 - ts * ts, 1e-18)
    pot = -0.5 * float(np.sum(np.log(gap) * (w * w) * wt))
    nrm = float(np.trapezoid(w * w, ts))
    return {"jump": jump, "pot": pot, "L": jump + pot, "nrm": nrm}


def moments(w: np.ndarray, ts: np.ndarray) -> dict:
    nrm = float(np.trapezoid(w * w, ts))
    iw = float(np.trapezoid(w, ts))
    ix2 = float(np.trapezoid(ts * ts * w, ts))
    iabs = float(np.trapezoid(np.abs(w), ts))
    return {"nrm": nrm, "int": iw, "intx2": ix2, "intabs": iabs}


def plateau(ts: np.ndarray, eta: float) -> np.ndarray:
    """Even, w(±1)=0: 1 on [|t|≤1−η], linear ramps on the ends. η∈(0,1]."""
    eta = min(max(eta, 1e-6), 1.0)
    w = np.ones_like(ts)
    for i, t in enumerate(ts):
        at = abs(float(t))
        if at > 1.0 - eta:
            w[i] = max(0.0, (1.0 - at) / eta)
    return w


def cosine(ts: np.ndarray) -> np.ndarray:
    return np.cos(0.5 * math.pi * ts)


def sine(ts: np.ndarray) -> np.ndarray:
    return np.sin(math.pi * ts)


def mean_zero_even(ts: np.ndarray) -> np.ndarray:
    """Even Dirichlet, mean cancelled: φ0 − c φ1, φk=cos((k+1/2)π t)."""
    p0 = np.cos(0.5 * math.pi * ts)
    p1 = np.cos(1.5 * math.pi * ts)
    m0 = float(np.trapezoid(p0, ts))
    m1 = float(np.trapezoid(p1, ts))
    return p0 - (m0 / m1) * p1


def cstar(S: float, n: int = 4000) -> float:
    """min_{t∈(0,S]} (−ρ''(t)/t²)."""
    cmin = 1e99
    for k in range(1, n + 1):
        t = S * k / n
        rho = rpp_closed(t) + 1.75
        c = -rho / (t * t)
        if c < cmin:
            cmin = c
    return cmin


def prime_of(ts: np.ndarray, w: np.ndarray, a: float, nrm: float) -> float:
    if 2.0 * a + 1e-14 < LOG2:
        return 0.0
    lag = LOG2 / a
    return -PRIME2_COEFF * hankel_lag(ts, w, lag) / nrm


def family_row(name: str, w: np.ndarray, ts: np.ndarray, a: float, c: float) -> dict:
    sp = L_split(w, ts)
    mo = moments(w, ts)
    nrm = sp["nrm"]
    Lw = sp["L"] / nrm
    rank1 = (7.0 / 4.0) * a * (mo["int"] ** 2) / nrm
    # ρ_lower for w with ww-autocorrelation of (x−y)²: even identity
    # ∬(x−y)² w(x)w(y) = 2(∫w)(∫ x² w) − 2(∫ x w)²
    ix = float(np.trapezoid(ts * w, ts))
    q2 = 2.0 * mo["int"] * mo["intx2"] - 2.0 * ix * ix
    rho_lo = c * (a**3) * q2 / nrm  # 2c a³ (∫w)(∫x²w)/n for even
    # For w≥0, ρ''≤−c s² ⇒ ∬ ρ''(a(x−y))ww ≤ −c a² ∬(x−y)² ww
    # ρ-term = −a ∬ρ''/n ≥ c a³ q2 / n.  (note: 2 already in q2)
    p = prime_of(ts, w, a, nrm)
    th = C2A1 + math.log(a)
    logc = math.log(1.0 / a) - C2A1
    J = Lw + rank1
    LB = logc + Lw + rank1 + rho_lo + p  # valid lower bound of R IF w≥0 and ρ''≤−c s²
    return {
        "name": name,
        "a": a,
        "L": Lw,
        "jump": sp["jump"] / nrm,
        "pot": sp["pot"] / nrm,
        "rank1": rank1,
        "mean2": (mo["int"] ** 2) / nrm,
        "rho_lo": rho_lo,
        "prime": p,
        "th": th,
        "J_minus_th": J - th,
        "LB": LB,
        "logc_L": logc + Lw,
    }


def l_ritz_even(ts: np.ndarray, M: int = 6) -> dict:
    """Ritz of L on even Dirichlet span. Upper bounds on μ1, μ2."""
    n = len(ts)
    phis = []
    for k in range(M):
        phis.append(np.cos((k + 0.5) * math.pi * ts))
    Lmat = np.zeros((M, M))
    B = np.zeros((M, M))
    ones = np.zeros(M)
    for j in range(M):
        ones[j] = float(np.trapezoid(phis[j], ts))
        for i in range(j, M):
            # L is a quadratic form, not bilinear-ready from L_a of sums
            # polarize: L(u+v)−L(u)−L(v)
            u, v = phis[i], phis[j]
            Lu = L_a(u, ts, 1.0)
            Lv = L_a(v, ts, 1.0)
            Luv = L_a(u + v, ts, 1.0)
            Lmat[i, j] = Lmat[j, i] = 0.5 * (Luv - Lu - Lv)
            B[i, j] = B[j, i] = float(np.trapezoid(u * v, ts))
    evals = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(B, Lmat))))
    # joint J at a2: L + κ |1⟩⟨1| with κ=(7/4)a2, form κ (∫w)² = κ ones^T c c^T ones
    a = A2
    kappa = (7.0 / 4.0) * a
    Jmat = Lmat + kappa * np.outer(ones, ones)
    jevals = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(B, Jmat))))
    return {"mu": evals, "nu_a2": jevals, "ones": ones, "Bdiag": np.diag(B)}


def main() -> None:
    n = 401
    ts = np.linspace(-1.0, 1.0, n)
    S = 2.0 * A3
    c = cstar(S)
    print("=== constants ===")
    print(f"  A={A:.12f}  2A+1={C2A1:.12f}")
    print(f"  a2={A2:.12f}  a3={A3:.12f}")
    print(f"  threshold(a2)=(2A+1)+log a2={C2A1 + math.log(A2):.8f}")
    print(f"  c*=min(−ρ''/t²) on (0,2a3]={c:.8f}  (9/32={9/32:.8f})")

    print("\n=== L split (a-independent, on [-1,1]) ===")
    print(f"{'family':<16} {'L':>10} {'jump':>10} {'pot':>10} {'(∫w)²/n':>10}")
    families = [
        ("cosine", cosine(ts)),
        ("sine-odd", sine(ts)),
        ("mean0-even", mean_zero_even(ts)),
        ("tent", plateau(ts, 1.0)),
        ("plateau-0.05", plateau(ts, 0.05)),
        ("plateau-0.20", plateau(ts, 0.20)),
        ("plateau-0.50", plateau(ts, 0.50)),
    ]
    # two-bump at a=a2+0.05 scaled to [-1,1]
    a_tb = A2 + 0.05
    xs = np.linspace(-a_tb, a_tb, n)
    _, bump, _ = linear_two_bump(a_tb, 2.0 * 0.05, n)
    w_tb = np.interp(ts, xs / a_tb, bump)
    families.append(("twobump-sc", w_tb))

    for name, w in families:
        sp = L_split(w, ts)
        mo = moments(w, ts)
        print(
            f"{name:<16} {sp['L']/sp['nrm']:10.6f} {sp['jump']/sp['nrm']:10.6f} "
            f"{sp['pot']/sp['nrm']:10.6f} {(mo['int']**2)/sp['nrm']:10.6f}"
        )

    print("\n=== (4.5) lower bound on nonnegative families (ρ''≤−c s²) ===")
    print(
        f"{'family':<16} {'a':>7} {'L':>9} {'rank1':>9} {'J-th':>9} "
        f"{'ρ_lo':>9} {'prime':>9} {'LB':>9}"
    )
    as_ = [0.20, A2, A2 + 0.01, 0.5 * (A2 + A3), A3 - 1e-3]
    nonneg = [f for f in families if f[0] not in ("sine-odd", "mean0-even")]
    any_neg_lb = False
    for a in as_:
        for name, w in nonneg:
            row = family_row(name, w, ts, a, c)
            if row["LB"] < 0:
                any_neg_lb = True
            print(
                f"{name:<16} {a:7.4f} {row['L']:9.5f} {row['rank1']:9.5f} "
                f"{row['J_minus_th']:9.5f} {row['rho_lo']:9.5f} "
                f"{row['prime']:9.5f} {row['LB']:9.5f}"
            )

    print("\n=== odd / mean-zero even: no rank-one ===")
    print(f"{'family':<16} {'a':>7} {'log-c+L':>10} {'ρ_lo':>9} {'prime':>9} {'LB':>9}")
    for a in as_:
        for name, w in families:
            if name not in ("sine-odd", "mean0-even"):
                continue
            row = family_row(name, w, ts, a, c)
            print(
                f"{name:<16} {a:7.4f} {row['logc_L']:10.5f} {row['rho_lo']:9.5f} "
                f"{row['prime']:9.5f} {row['LB']:9.5f}"
            )

    print("\n=== Ritz of L on even Dirichlet (UPPER bounds on μ_k) ===")
    # smaller grid for the M² polarizations of L (each L_a is n²)
    tsR = np.linspace(-1.0, 1.0, 201)
    rt = l_ritz_even(tsR, M=5)
    print(f"  μ_Ritz = {rt['mu']}")
    print(f"  ν_Ritz(J at a2) = {rt['nu_a2']}")
    print(f"  threshold(a2) = {C2A1 + math.log(A2):.8f}")
    print("  (Ritz is an UPPER bound of inf J: if ν1 < threshold, J without ρ fails.)")

    print("\n=== cosine gap arithmetic at a2 (must match remainder_bound) ===")
    row = family_row("cosine", cosine(ts), ts, A2, c)
    print(
        f"  L={row['L']:.6f} rank1={row['rank1']:.6f} J-th={row['J_minus_th']:.6f} "
        f"ρ_lo={row['rho_lo']:.6f} LB={row['LB']:.6f}"
    )
    print("  If J-th<0 and ρ_lo > −(J-th), ρ_lower alone would save the cosine.")

    print("\n=== VERDICT ===")
    print(f"  c*={c:.6f}")
    print(f"  any nonnegative-family LB<0: {any_neg_lb}")
    if rt["nu_a2"][0] < C2A1 + math.log(A2):
        print("  CHECKED: inf J_a2 ≤ ν_Ritz < threshold ⇒ dropping ρ fails at a2.")
    print("  Mean-zero/odd: rank-one=0; if log-c+L>0 through a3 they are locally safe.")


if __name__ == "__main__":
    main()
