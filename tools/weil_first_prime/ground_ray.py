#!/usr/bin/env python3
"""Even ground ray at a=a₂: finite-section J+ρ vs threshold, Schur test.

At a=a₂=(log 2)/2 the prime-2 lag is (log 2)/a₂=2, Hankel support is a
point, prime term = 0. Suzuki (4.5) positivity ⇔
    L/‖w‖² + (7/4) a₂ (∫w)²/‖w‖² + ρ-term  ≥  threshold(a₂).
Even mean-zero is already safe (μ₂≥1.641, crude |ρ|≤0.104). This script
attacks the remaining even sector (nonzero mean) — the ground ray.

Belief this changes:
  (1) whether the actual ρ-term (not the c t² lower bound) lifts the
      J-minimizer above threshold;
  (2) whether min Rayleigh(J+ρ) on even Dirichlet V_M stays above
      threshold (Ritz = upper bound of inf — if it dips BELOW, the
      endpoint is not positive on that subspace);
  (3) whether a Schur test Q(ψ)−θ, μ_⊥−θ, |Q(ψ,u)|≤C‖u‖ closes a
      lemma that inf(J+ρ)>threshold on all even w vanishing at ±1;
  (4) sign of the Fourier multiplier of ρ'' (if m(η)<0 then ρ>0
      everywhere — still not a proof, because inf J < threshold).

Usage: python3 tools/weil_first_prime/ground_ray.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from lower_bound import A2, A3, GAMMA, LOG2  # noqa: E402
from mu2_envelope import kernel_matrix, trap_weights  # noqa: E402
from rpp_closed import rpp_closed  # noqa: E402
from screw_kernel import A_SUZUKI  # noqa: E402

A = A_SUZUKI
C2A1 = 2.0 * A + 1.0
TH2 = C2A1 + math.log(A2)
TH3 = C2A1 + math.log(A3)
KAPPA = (7.0 / 4.0) * A2  # rank-one prefactor in (4.5)
NEG_MU2 = (1.0 / (10.0 * math.pi)) * (-(math.exp(-GAMMA) ** 5) / 25.0)


def rho_pp(t: float) -> float:
    t = abs(float(t))
    if t < 1e-14:
        return 0.0
    return rpp_closed(t) + 1.75


def cosine_hankel(h: float) -> float:
    """∫ φ(x)φ(x−h) dx on [-1,1], φ=cos(πt/2). PROVEN elementary."""
    h = abs(float(h))
    if h >= 2.0 - 1e-15:
        return 0.0
    if h < 1e-14:
        return 1.0
    return 0.5 * (2.0 - h) * math.cos(0.5 * math.pi * h) + math.sin(
        0.5 * math.pi * h
    ) / math.pi


def rho_cosine_closed(a: float, n: int = 4001) -> float:
    """ρ-term of unit cosine: −∫ ρ''(s) H(s/a) ds. nrm(φ)=1."""
    S = 2.0 * a
    ss = np.linspace(0.0, S, n)
    vals = np.array([rho_pp(s) * cosine_hankel(s / a) for s in ss])
    return -2.0 * float(np.trapezoid(vals, ss))


def m_eta(eta: float, a: float, n: int = 2001) -> float:
    """m(η)=∫_{-2a}^{2a} ρ''(s) cos(η s) ds."""
    S = 2.0 * a
    ss = np.linspace(0.0, S, n)
    vals = np.array([rho_pp(s) * math.cos(eta * s) for s in ss])
    return 2.0 * float(np.trapezoid(vals, ss))


def mixed_hankel(ts: np.ndarray, u: np.ndarray, v: np.ndarray, lag: float) -> float:
    shifted = np.interp(ts - lag, ts, v, left=0.0, right=0.0)
    return float(np.trapezoid(u * shifted, ts))


def rho_bilin(u: np.ndarray, v: np.ndarray, ts: np.ndarray, a: float, nlag: int = 801) -> float:
    """Bilinear ρ-numerator −∫ ρ''(s) H_{uv}(s/a) ds."""
    S = 2.0 * a
    ss = np.linspace(0.0, S, nlag)
    Hs = np.array([mixed_hankel(ts, u, v, s / a) for s in ss])
    rpp = np.array([rho_pp(s) for s in ss])
    return -2.0 * float(np.trapezoid(rpp * Hs, ss))


def L_bilin(u: np.ndarray, v: np.ndarray, ts: np.ndarray) -> float:
    Lu = L_a(u, ts, 1.0)
    Lv = L_a(v, ts, 1.0)
    Luv = L_a(u + v, ts, 1.0)
    return 0.5 * (Luv - Lu - Lv)


def gen_eigh(H: np.ndarray, B: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """H v = ν B v with B≻0, via Cholesky (not solve(B,H))."""
    chol = np.linalg.cholesky(B)
    tmp = np.linalg.solve(chol, H)
    M = np.linalg.solve(chol, tmp.T).T
    M = 0.5 * (M + M.T)
    evals, evecs_y = np.linalg.eigh(M)
    evecs = np.linalg.solve(chol.T, evecs_y)
    return evals, evecs


def even_dirichlet_section(n: int, M: int, a: float) -> dict:
    ts = np.linspace(-1.0, 1.0, n)
    phis = [np.cos((k + 0.5) * math.pi * ts) for k in range(M)]
    Lmat = np.zeros((M, M))
    Rmat = np.zeros((M, M))
    B = np.zeros((M, M))
    ones = np.zeros(M)
    for j in range(M):
        ones[j] = float(np.trapezoid(phis[j], ts))
        for i in range(j, M):
            u, v = phis[i], phis[j]
            Lmat[i, j] = Lmat[j, i] = L_bilin(u, v, ts)
            Rmat[i, j] = Rmat[j, i] = rho_bilin(u, v, ts, a)
            B[i, j] = B[j, i] = float(np.trapezoid(u * v, ts))
    Jmat = Lmat + KAPPA * np.outer(ones, ones)
    Qmat = Jmat + Rmat
    return {
        "ts": ts,
        "phis": phis,
        "L": Lmat,
        "R": Rmat,
        "B": B,
        "ones": ones,
        "J": Jmat,
        "Q": Qmat,
    }


def hs_even_orth_dirichlet(Om: float, n: int, M: int) -> dict:
    """HS of bandlimit Q_Ω on even functions ⊥ first M even Dirichlet."""
    ts = np.linspace(-1.0, 1.0, n)
    w = trap_weights(ts)
    sw = np.sqrt(w)
    K = kernel_matrix(ts, Om)
    Q = sw[:, None] * K * sw[None, :]
    rev = np.arange(n)[::-1]
    Qe = 0.25 * (Q + Q[:, rev] + Q[rev, :] + Q[rev][:, rev])
    V = np.stack([sw * np.cos((k + 0.5) * math.pi * ts) for k in range(M)], axis=1)
    q, _ = np.linalg.qr(V, mode="reduced")
    P = q @ q.T
    I = np.eye(n)
    Qt = (I - P) @ Qe @ (I - P)
    hs = float(np.linalg.norm(Qt, ord="fro"))
    lam = float(np.max(np.linalg.eigvalsh(Qt)))
    return {"hs": hs, "lam_ritz": lam, "tr": float(np.trace(Qt))}


def nested_mu(alpha_of_omega, Omega: float, ngrid: int = 400) -> float:
    """μ ≥ log Ω + γ − ∫_0^Ω α(ω)/ω dω + NEG, α(0)=0."""
    ws = np.linspace(1e-6, Omega, ngrid)
    avals = np.array([alpha_of_omega(float(w)) for w in ws])
    integ = float(np.trapezoid(avals / ws, ws))
    return math.log(Omega) + GAMMA - integ + NEG_MU2


def main() -> None:
    print("=== constants ===")
    print(f"  a2={A2:.16f}  threshold(a2)={TH2:.16f}")
    print(f"  a3={A3:.16f}  threshold(a3)={TH3:.16f}")
    print(f"  kappa=(7/4)a2={KAPPA:.16f}")
    print(f"  16/π²={(16 / math.pi**2):.16f}")

    print("\n=== 1. cosine: closed Hankel ρ vs J-gap ===")
    # L of cosine via jumping form
    ts_c = np.linspace(-1.0, 1.0, 801)
    psi = np.cos(0.5 * math.pi * ts_c)
    nrm = float(np.trapezoid(psi * psi, ts_c))
    Lpsi = L_a(psi, ts_c, 1.0) / nrm
    iw = float(np.trapezoid(psi, ts_c))
    rank1 = KAPPA * (iw * iw) / nrm
    Jpsi = Lpsi + rank1
    rho_c = rho_cosine_closed(A2)
    # rho_cosine_closed assumes nrm=1; actual nrm of samples ≈1
    rho_c_n = rho_c / nrm
    rho_num = rho_bilin(psi, psi, ts_c, A2) / nrm
    print(f"  ‖ψ‖²={nrm:.12f}  (want 1)")
    print(f"  L/n={Lpsi:.12f}  rank1={rank1:.12f}  J={Jpsi:.12f}")
    print(f"  J−th={Jpsi - TH2:.12e}")
    print(f"  ρ_closed={rho_c_n:.12f}  ρ_quad={rho_num:.12f}")
    print(f"  J+ρ_closed−th={(Jpsi + rho_c_n) - TH2:.12e}")
    print(f"  cosine clears threshold: {Jpsi + rho_c_n > TH2}")

    print("\n=== 2. Fourier multiplier m(η) of ρ'' on [−2a2,2a2] ===")
    etas = np.concatenate(
        [np.linspace(0.0, 20.0, 81), np.array([25.0, 30.0, 40.0, 60.0, 80.0])]
    )
    ms = [m_eta(float(et), A2) for et in etas]
    mmin = min(ms)
    mmax = max(ms)
    imin = int(np.argmin(ms))
    imax = int(np.argmax(ms))
    print(f"  m min={mmin:.8f} at η={etas[imin]:.4f}")
    print(f"  m max={mmax:.8f} at η={etas[imax]:.4f}")
    print(f"  m(0)={ms[0]:.8f}  (∫ ρ'' ; want <0 if ρ''<0)")
    nneg = sum(1 for m in ms if m > 1e-12)
    print(f"  samples with m>0: {nneg}/{len(ms)}")
    print("  sample m(η):")
    for et, m in zip(etas[::10], ms[::10]):
        print(f"    η={et:8.3f}  m={m:+.8f}  −m={-m:+.8f}")
    # ρ-term = (1/2π nrm) ∫ (−m(ξ/a)) |ŵ|² dξ. Sign of −m = sign of ρ weight.

    print("\n=== 3. even Dirichlet section of J and J+ρ ===")
    n, M = 151, 6
    print(f"  n={n} M={M}  (Cholesky generalized eigen)")
    sec = even_dirichlet_section(n, M, A2)
    evJ, vecJ = gen_eigh(sec["J"], sec["B"])
    evQ, vecQ = gen_eigh(sec["Q"], sec["B"])
    evL, _ = gen_eigh(sec["L"], sec["B"])
    print(f"  eig(L)  = {np.array2string(evL, precision=8)}")
    print(f"  eig(J)  = {np.array2string(evJ, precision=8)}")
    print(f"  eig(Q)  = {np.array2string(evQ, precision=8)}")
    print(f"  min J − th = {evJ[0] - TH2:.12e}   (want >0 to clear without ρ)")
    print(f"  min Q − th = {evQ[0] - TH2:.12e}   (Ritz upper bound of inf Q)")
    print(f"  V_M min Q > th: {evQ[0] > TH2}")
    # ground-ray mixing
    cJ = vecJ[:, 0]
    if float(sec["ones"] @ cJ) < 0:
        cJ = -cJ
    print(f"  J-ground coeffs: {np.array2string(cJ, precision=6)}")
    cQ = vecQ[:, 0]
    if float(sec["ones"] @ cQ) < 0:
        cQ = -cQ
    print(f"  Q-ground coeffs: {np.array2string(cQ, precision=6)}")
    # reconstruct Q on J-ground
    nrmc = float(cJ @ sec["B"] @ cJ)
    Q_on_J = float(cJ @ sec["Q"] @ cJ) / nrmc
    J_on_J = float(cJ @ sec["J"] @ cJ) / nrmc
    R_on_J = float(cJ @ sec["R"] @ cJ) / nrmc
    print(f"  on J-ground: J={J_on_J:.12f} ρ={R_on_J:.12f} Q={Q_on_J:.12f} Q−th={Q_on_J-TH2:.12e}")

    print("\n=== 4. L-Gram CS ratios vs φ0=cosine ===")
    L00 = sec["L"][0, 0]
    print(f"  L00={L00:.8f}  B00={sec['B'][0, 0]:.8f}")
    for k in range(1, M):
        L0k = sec["L"][0, k]
        Lkk = sec["L"][k, k]
        cs = abs(L0k) / math.sqrt(abs(L00 * Lkk) + 1e-30)
        Q0k = sec["Q"][0, k]
        print(
            f"  k={k}  L0k={L0k:+.8f}  CS={cs:.6f}  "
            f"ρ0k={sec['R'][0, k]:+.8f}  Q0k={Q0k:+.8f}  "
            f"mean_k={sec['ones'][k]:+.6f}"
        )

    print("\n=== 5. Schur test on {ψ} ⊕ {ψ}⊥ inside V_M ===")
    # Restrict to V_M: Q(αψ+u), u ⊥ ψ in the B-inner product.
    # C_M = max |Q(ψ,u)|/‖u‖_B over u in V_M, u⊥ψ
    # = sqrt of max eig of the Schur off-block, i.e. |Q_{0,1:}| after B-ON.
    # Since B≈I, C_M ≈ sqrt(sum_{k≥1} Q[0,k]²) is a lower bound of the
    # true operator norm of the off-diagonal (Ritz). The TRUE C is ≥ C_M.
    # For a PROOF we need an UPPER bound of C. On V_M, C_M is exact for
    # that subspace. Tail handled in §6.
    cholB = np.linalg.cholesky(sec["B"])
    # orthonormal: y = L^T c, Qy = L^{-1} Q L^{-T}
    tmp = np.linalg.solve(cholB, sec["Q"])
    Qon = np.linalg.solve(cholB, tmp.T).T
    Qon = 0.5 * (Qon + Qon.T)
    q00 = Qon[0, 0]
    off = Qon[0, 1:]
    C_M = float(np.linalg.norm(off))  # exact on V_M: max |Q(ψ,u)|/‖u‖
    Qperp = Qon[1:, 1:]
    ev_perp = np.sort(np.linalg.eigvalsh(Qperp))
    mu_perp_M = float(ev_perp[0])  # exact min Q on V_M ∩ ψ⊥
    print(f"  Q(ψ,ψ) (B-ON)={q00:.12f}  q00−th={q00-TH2:.12e}")
    print(f"  C_M=||Q(psi,.) on V_M perp psi||={C_M:.12f}")
    print(f"  min Q on V_M perp psi = {mu_perp_M:.12f}  -th={mu_perp_M-TH2:.12e}")
    # Schur: need C² < (q00−th)(mu_perp−th)
    gap0 = q00 - TH2
    gap1 = mu_perp_M - TH2
    rhs = gap0 * gap1
    print(f"  (q00−th)(μ⊥−th)={rhs:.12e}  C_M²={C_M**2:.12e}")
    print(f"  Schur on V_M: {C_M**2 < rhs and gap0 > 0 and gap1 > 0}")
    # AM-GM λ-optimal: need 2 C < gap0+gap1?  Standard condition C²<(g0)(g1)
    if gap0 > 0 and gap1 > 0:
        print(f"  margin C² / ((q00−th)(μ⊥−th)) = {(C_M**2) / rhs:.6f}  (<1 passes)")
    else:
        print("  Schur gaps not both positive on V_M")

    print("\n=== 6. tail concentration, even ⊥ V_M (M=3 and M=5) ===")
    # Conservative HS × 1.05 as in mu2_envelope.py
    for Mtail, Om in ((3, 3.2), (3, 4.0), (5, 4.0), (5, 6.0)):
        h = hs_even_orth_dirichlet(Om, n=81, M=Mtail)
        acons = min(1.0, 1.05 * h["hs"])
        # hard-cutoff lower bound (weaker): (1-α)(log Ω+γ)+NEG
        hard = (1.0 - acons) * (math.log(Om) + GAMMA) + NEG_MU2
        print(
            f"  M={Mtail} Ω={Om:.1f}  HS={h['hs']:.6f}  α_cons={acons:.6f}  "
            f"hard μ≥{hard:.4f}  ritz_λ={h['lam_ritz']:.6f}"
        )

    # nested for M=3, Ω=4, α(ω)=1.05 HS(ω) sampled coarsely
    print("  nested μ_tail M=3 (n=81 HS×1.05):")
    cache = {}

    def acons3(om: float) -> float:
        key = round(om, 3)
        if key not in cache:
            cache[key] = min(1.0, 1.05 * hs_even_orth_dirichlet(om, n=81, M=3)["hs"])
        return cache[key]

    for Om in (2.4, 3.2, 4.0, 5.0):
        mu = nested_mu(acons3, Om, ngrid=25)
        print(f"    Ω={Om:.1f}  α({Om})={acons3(Om):.5f}  nested μ≥{mu:.4f}")

    print("\n=== 7. crude |ρ| and odd-sector reminder ===")
    # |ρ| ≤ ∫_{-2a}^{2a} |ρ''(s)| ds  (Young)
    S = 2.0 * A2
    ss = np.linspace(0.0, S, 2001)
    rhoL1 = 2.0 * float(np.trapezoid([abs(rho_pp(s)) for s in ss], ss))
    print(f"  ‖ρ''‖_1 on [-2a2,2a2]={rhoL1:.8f}")
    print(f"  |ρ-term| ≤ {rhoL1:.8f}  (same order as previous 0.104)")
    # odd sine
    ts_o = np.linspace(-1.0, 1.0, 401)
    sine = np.sin(math.pi * ts_o)
    ns = float(np.trapezoid(sine * sine, ts_o))
    Ls = L_a(sine, ts_o, 1.0) / ns
    rs = rho_bilin(sine, sine, ts_o, A2) / ns
    print(f"  odd sine: L={Ls:.8f}  ρ={rs:.8f}  L+ρ−th={Ls + rs - TH2:.8f}")

    print("\n=== VERDICT ===")
    cosine_ok = Jpsi + rho_c_n > TH2
    section_ok = bool(evQ[0] > TH2)
    schur_ok = bool(gap0 > 0 and gap1 > 0 and C_M**2 < rhs)
    print(f"  cosine J+ρ > th: {cosine_ok}")
    print(f"  V_{M} min(J+ρ) > th: {section_ok}  (Ritz; NOT a proof of inf)")
    print(f"  Schur on V_M: {schur_ok}")
    print(f"  min Q − th = {evQ[0] - TH2:.6e}")
    print(f"  m(η) has positive samples: {nneg > 0}")
    if section_ok and schur_ok:
        print("  finite-section Schur PASSES — tail C still needed for a lemma")
    elif section_ok:
        print("  Q-Ritz on V_M is above th; Schur fails ⇒ mixing with ψ⊥ eats the gap")
    else:
        print("  Q-Ritz already below th on V_M ⇒ inf(J+ρ) ≤ that value")
        print("  endpoint a=a2 is NOT certified; may be a true dip or quadrature")


if __name__ == "__main__":
    main()
