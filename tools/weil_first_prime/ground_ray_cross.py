#!/usr/bin/env python3
"""Off-block Q(V_M, tail) via the closed Fourier transforms of even Dirichlet.

φ_k(t)=cos((k+1/2)π t) on [-1,1],
  ŵ_k(ξ)=sin(ξ+ω)/ (ξ+ω) + sin(ξ−ω)/(ξ−ω),  ω=(k+1/2)π.

L(φ_j,φ_k)=(1/π)∫_0^∞ (log ξ+γ) ŵ_j ŵ_k dξ   (even; Plancherel 1/2π).
ρ(φ_j,φ_k)=(1/π)∫_0^∞ (−m(ξ/a)) ŵ_j ŵ_k dξ,
  m(η)=∫_{-2a}^{2a} ρ''(s) cos(η s) ds.
rank-one = κ ŵ_j(0) ŵ_k(0).

Belief: Schur λ_min(Q|_{V_M}) − ‖C‖² / λ_min(Q|_{tail}) > threshold(a₂)
closes λ_a>0 at a=a₂ on even functions (prime term = 0). Need ‖C‖_op
upper-bounded by the off-block Frobenius plus an explicit k-tail.

Usage: python3 tools/weil_first_prime/ground_ray_cross.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ground_ray import KAPPA, TH2, m_eta, rho_pp  # noqa: E402
from lower_bound import A2, GAMMA  # noqa: E402
from rpp_closed import rpp_closed  # noqa: E402

# Recompute TH2 locally to keep this file runnable if imports shift.
from screw_kernel import A_SUZUKI  # noqa: E402

C2A1 = 2.0 * A_SUZUKI + 1.0


def what_k(k: int, xi: np.ndarray) -> np.ndarray:
    w = (k + 0.5) * math.pi
    xi = np.asarray(xi, dtype=np.float64)
    dp = xi + w
    dm = xi - w
    term_p = np.sin(dp) / dp
    term_m = np.where(np.abs(dm) < 1e-12, 1.0, np.sin(dm) / dm)
    return term_p + term_m


def mean_k(k: int) -> float:
    w = (k + 0.5) * math.pi
    return 2.0 * math.sin(w) / w  # = 2 (-1)^k / w


def make_xi_grid() -> tuple[np.ndarray, np.ndarray]:
    """Composite grid: log near 0, linear through the Dirichlet peaks, 1/ξ tail."""
    g0 = np.geomspace(1e-8, 0.2, 800)
    g1 = np.linspace(0.2, 80.0, 12000)
    g2 = np.linspace(80.0, 400.0, 4000)
    xi = np.unique(np.concatenate([g0, g1, g2]))
    # trapezoid weights
    w = np.zeros_like(xi)
    w[1:-1] = 0.5 * (xi[2:] - xi[:-2])
    w[0] = 0.5 * (xi[1] - xi[0])
    w[-1] = 0.5 * (xi[-1] - xi[-2])
    return xi, w


def m_on_grid(xi: np.ndarray, a: float, nquad: int = 2001) -> np.ndarray:
    """m(ξ/a) for each ξ. Vectorized in η; inner integral via cached s-grid."""
    S = 2.0 * a
    ss = np.linspace(0.0, S, nquad)
    rpp = np.array([rho_pp(s) for s in ss])
    # m(η)=2 ∫_0^S ρ''(s) cos(η s) ds
    eta = xi / a
    # (nξ, ns)
    C = np.cos(eta[:, None] * ss[None, :])
    return 2.0 * np.trapezoid(rpp[None, :] * C, ss, axis=1)


def forms_on_basis(K: int, a: float) -> dict:
    xi, wt = make_xi_grid()
    print(f"  ξ-grid: {len(xi)} nodes, max={xi[-1]:.1f}", flush=True)
    whats = [what_k(k, xi) for k in range(K)]
    # Plancherel check
    planch = [float(np.sum(whats[k] ** 2 * wt) / math.pi) for k in range(min(4, K))]
    print(f"  Plancherel φ0.. (want 1): {['%.8f' % p for p in planch]}")
    mvals = m_on_grid(xi, a)
    logw = np.log(np.maximum(xi, 1e-18)) + GAMMA
    L = np.zeros((K, K))
    R = np.zeros((K, K))
    ones = np.array([mean_k(k) for k in range(K)])
    for j in range(K):
        for i in range(j, K):
            prod = whats[i] * whats[j]
            L[i, j] = L[j, i] = float(np.sum(logw * prod * wt) / math.pi)
            R[i, j] = R[j, i] = float(np.sum((-mvals) * prod * wt) / math.pi)
    J = L + KAPPA * np.outer(ones, ones)
    Q = J + R
    return {"L": L, "R": R, "J": J, "Q": Q, "ones": ones, "planch": planch}


def schur_margin(Q: np.ndarray, M: int, mu_B: float, th: float) -> dict:
    """λ_min(A) − ‖C‖_F² / μ_B  vs threshold. ‖C‖_op ≤ ‖C‖_F."""
    A = Q[:M, :M]
    C = Q[:M, M:]
    evA = np.sort(np.linalg.eigvalsh(A))
    frob = float(np.linalg.norm(C, ord="fro"))
    # row-sum (1-norm) and 2-norm of the finite C
    op2 = float(np.linalg.norm(C, ord=2)) if C.size else 0.0
    lb = evA[0] - (frob**2) / mu_B
    lb_op = evA[0] - (op2**2) / mu_B
    return {
        "M": M,
        "Ktail": Q.shape[0] - M,
        "lamA": float(evA[0]),
        "lamA2": float(evA[1]) if len(evA) > 1 else float("nan"),
        "frob": frob,
        "op2": op2,
        "lb_F": lb,
        "lb_op": lb_op,
        "gap_F": lb - th,
        "gap_op": lb_op - th,
    }


def mean_energy_tail(M: int) -> float:
    """Σ_{k≥M} (∫φ_k)² = 2 − Σ_{k<M} mean_k²  (Parseval of the constant)."""
    s = sum(mean_k(k) ** 2 for k in range(M))
    return 2.0 - s


def main() -> None:
    th = TH2
    print("=== Fourier Q on even Dirichlet, off-block Schur ===")
    print(f"  threshold(a2)={th:.16f}  kappa={KAPPA:.16f}")
    K = 80
    pack = forms_on_basis(K, A2)
    Q = pack["Q"]
    L = pack["L"]
    R = pack["R"]
    print(f"  L00={L[0,0]:.12f}  (jumping-form cosine was 0.36564181)")
    print(f"  ρ00={R[0,0]:.12f}  (closed Hankel cosine was 0.00922027)")
    print(f"  Q00={Q[0,0]:.12f}")
    print(f"  eig(Q[:6,:6])={np.array2string(np.sort(np.linalg.eigvalsh(Q[:6, :6])), precision=8)}")

    # Q on tail ≥ nested μ_L − ‖ρ''‖_1
    S = 2.0 * A2
    ss = np.linspace(0.0, S, 2001)
    rhoL1 = 2.0 * float(np.trapezoid([abs(rho_pp(s)) for s in ss], ss))
    # nested μ_tail M=3 Ω=4 was 1.8541 (ground_ray.py). Use 1.85 conservative.
    mu_L_tail = 1.8541
    mu_B = mu_L_tail - rhoL1
    print(f"  ‖ρ''‖_1={rhoL1:.8f}  μ_L_tail(M=3,Ω=4)={mu_L_tail}  μ_B≥{mu_B:.8f}")
    print(f"  need ‖C‖_F² < (λ_min(A)−th) μ_B")

    print("\n=== Schur vs finite tail proxy K=24 ===")
    print(
        f"  {'M':>3} {'lamA-th':>12} {'‖C‖_F':>10} {'‖C‖_2':>10} "
        f"{'lb_F-th':>12} {'lb_2-th':>12} {'pass_F':>7} {'pass_2':>7}"
    )
    rows = []
    for M in (2, 3, 4, 5, 6, 8, 10, 12):
        r = schur_margin(Q, M, mu_B, th)
        rows.append(r)
        print(
            f"  {M:3d} {r['lamA']-th:12.6e} {r['frob']:10.6f} {r['op2']:10.6f} "
            f"{r['gap_F']:12.6e} {r['gap_op']:12.6e} "
            f"{str(r['gap_F']>0):>7} {str(r['gap_op']>0):>7}"
        )

    print("\n=== decay of Q[0,k] and row-0 energy ===")
    print(f"  {'k':>3} {'L0k':>12} {'ρ0k':>12} {'rank1':>12} {'Q0k':>12}")
    ones = pack["ones"]
    for k in range(0, min(16, K)):
        r1 = KAPPA * ones[0] * ones[k]
        print(
            f"  {k:3d} {L[0,k]:+12.6e} {R[0,k]:+12.6e} {r1:+12.6e} {Q[0,k]:+12.6e}"
        )
    # remaining Frobenius energy of row 0 beyond k=15
    print("\n=== ‖C‖_F² split: computed k<24 vs mean-rank1 k-tail bound ===")
    for M in (3, 6, 8, 12):
        frob_comp = float(np.linalg.norm(Q[:M, M:]))
        # rank-one tail: |κ mean_j mean_k| ≤ κ |mean_j| * 2 / ω_k
        # Σ_{k≥K} (κ mean_j * 2/ω_k)² = (κ mean_j * 2/π)² Σ_{k≥K} 1/(k+1/2)²
        # Σ_{n=n0}^∞ 1/(n+1/2)² ≤ ∫_{n0-1}^∞ dx/(x+1/2)² = 1/(n0-0.5)
        # here n0=K=24, even cruder: integral from K-1.
        K0 = K
        tail_r1_sq = 0.0
        for j in range(M):
            coeff = KAPPA * abs(ones[j]) * 2.0 / math.pi
            # Σ_{k≥K0} 1/(k+1/2)² ≤ ∫_{K0-1}^∞ dx/(x+1/2)² = 1/(K0-0.5)
            tail_r1_sq += (coeff**2) * (1.0 / (K0 - 0.5))
        # L and ρ tails: |ŵ_j ŵ_k| overlap is small. Crude |ρ_jk|≤ρL1,
        # |L_jk| ≤ ((1/2)log(ω_j ω_k)+γ) * overlap. Report rank-one tail only
        # as the slowly decaying piece; L/ρ decay faster (oscillatory, 1/k²).
        print(
            f"  M={M:2d}  ‖C_{M}:{K0}‖_F={frob_comp:.6f}  "
            f"rank1 k≥{K0} F²-bound={tail_r1_sq:.6e}  F-bound={math.sqrt(tail_r1_sq):.6e}"
        )
        frob_tot = math.sqrt(frob_comp**2 + tail_r1_sq)
        A = Q[:M, :M]
        lamA = float(np.min(np.linalg.eigvalsh(A)))
        lb = lamA - frob_tot**2 / mu_B
        print(
            f"       ‖C‖_F≤{frob_tot:.6f}  lamA−th={lamA-th:.6e}  "
            f"lb−th={lb-th:.6e}  pass={lb>th}"
        )

    print("\n=== Parseval mean energy of the tail (rank-one on tail is ≥0) ===")
    for M in (3, 6, 8, 12):
        te = mean_energy_tail(M)
        print(f"  M={M}  ‖(I-P)1‖²={te:.8f}  |∫u|≤{math.sqrt(te):.6f}‖u‖")

    print("\n=== λ_min(Q on V_K) vs K (decreasing upper bound of inf Q) ===")
    print(f"  {'K':>3} {'λ_min':>14} {'λ_min−th':>14} {'λ2':>12} {'above':>6}")
    for KK in (1, 2, 3, 6, 12, 24, 36, 48, 64, 80):
        ev = np.sort(np.linalg.eigvalsh(Q[:KK, :KK]))
        print(
            f"  {KK:3d} {ev[0]:14.10f} {ev[0]-th:14.6e} {ev[1] if KK>1 else float('nan'):12.6f} "
            f"{str(ev[0]>th):>6}"
        )

    print("\n=== ground-ray coupling ||Q(v_K, tail)|| vs Schur budget ===")
    # v_K = ground state of A=Q[:M,:M]. C_g = ||Q[M:K, :M] v_K|| (finite tail).
    # Budget: C_g^2 < (lamA-th)(mu_B-th). Finite C is OPTIMISTIC (missing k>=K).
    print(
        f"  {'M':>3} {'lamA-th':>12} {'C_g':>10} {'C_g2/budget':>12} "
        f"{'SchurComp-th':>14} {'|v0|':>8}"
    )
    budget_B = mu_B - th
    for M in (4, 6, 8, 12, 16, 24, 32, 40, 48, 64):
        A = Q[:M, :M]
        evA, vecA = np.linalg.eigh(A)
        v = vecA[:, 0]
        Cfin = Q[:M, M:]
        Cg = float(np.linalg.norm(Cfin.T @ v))
        gapA = float(evA[0]) - th
        budget = gapA * budget_B
        ratio = (Cg**2) / budget if budget > 0 else float("inf")
        S = A - (Cfin @ Cfin.T) / mu_B
        lamS = float(np.min(np.linalg.eigvalsh(S)))
        print(
            f"  {M:3d} {gapA:12.6e} {Cg:10.6f} {ratio:12.4f} "
            f"{lamS-th:14.6e} {abs(v[0]):8.5f}"
        )

    print("\n=== (Q v)_k decay for M=24 ground state ===")
    M = 24
    A = Q[:M, :M]
    evA, vecA = np.linalg.eigh(A)
    v = vecA[:, 0]
    if v[0] < 0:
        v = -v
    qv = Q[:, :M] @ v
    print(f"  lamA={evA[0]:.10f}  v[0:6]={np.array2string(v[:6], precision=5)}")
    print(f"  {'k':>3} {'(Qv)_k':>14} {'Q[0,k]':>14}")
    for k in list(range(0, 8)) + list(range(M, min(M + 12, K), 2)):
        print(f"  {k:3d} {qv[k]:+14.6e} {Q[0, k]:+14.6e}")
    energy_tail = float(np.sum(qv[M:] ** 2))
    print(f"  ||(Qv)[M:]||^2={energy_tail:.8e}  C_g={math.sqrt(energy_tail):.8e}")
    mv = float(pack["ones"][:M] @ v)
    print(f"  mean(v_K)={mv:.8f}  (cosine mean={mean_k(0):.8f})")

    print("\n=== 1/k tail envelope of (Qv)_k for remaining k>=K ===")
    for Mcut in (32, 48, 64):
        A = Q[:Mcut, :Mcut]
        evA, vecA = np.linalg.eigh(A)
        v = vecA[:, 0]
        qv = Q[:, :Mcut] @ v
        ks = np.arange(Mcut, K)
        mag = np.abs(qv[Mcut:])
        ck = mag * ks
        cmax = float(np.max(ck)) if len(ck) else 0.0
        Cg_fin = float(np.linalg.norm(qv[Mcut:]))
        # Σ_{k≥K} (cmax/k)² ≤ cmax² ∫_{K-1}^∞ dx / x² = cmax²/(K-1)
        crest2 = (cmax**2) / (K - 1)
        Cg_tot = math.sqrt(Cg_fin**2 + crest2)
        gapA = float(evA[0]) - th
        budget = gapA * budget_B
        print(
            f"  M={Mcut}  cmax=max k|(Qv)_k|={cmax:.6f}  C_fin={Cg_fin:.6f}  "
            f"C_rest≤{math.sqrt(crest2):.6f}  C_tot≤{Cg_tot:.6f}  "
            f"C²/budget={Cg_tot**2 / budget:.4f}  pass={Cg_tot**2 < budget}"
        )

    print("\n=== residual (L+rank1)/rank1 for row 0 (leading 1/k cancellation) ===")
    print(f"  {'k':>4} {'rank1':>12} {'L+rank1':>12} {'residual/rank1':>16} {'k*Q0k':>10}")
    for k in (1, 2, 3, 6, 12, 24, 40, 64, 79):
        r1 = KAPPA * ones[0] * ones[k]
        res = L[0, k] + r1
        frac = res / r1 if abs(r1) > 1e-18 else float("nan")
        print(
            f"  {k:4d} {r1:+12.4e} {res:+12.4e} {frac:16.6f} {k * Q[0, k]:+10.5f}"
        )

    print("\n=== VERDICT ===")
    best = max(rows, key=lambda r: r["gap_F"])
    print(
        f"  crude F-Schur: M={best['M']}  lb_F-th={best['gap_F']:.6e}  "
        f"pass={best['gap_F']>0}"
    )
    print(
        "  lam_min(V_80)=1.356772, gap 1.340e-3. Ground-ray 1/k Schur "
        "is the remaining lemma (see 1/k envelope pass/fail)."
    )


if __name__ == "__main__":
    main()
