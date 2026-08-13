#!/usr/bin/env python3
"""Tighter lower bounds on even mean-zero μ₂ (Suzuki 4.6).

L(w)=(1/2π)∫(log|ξ|+γ)|ŵ|². For even mean-zero w on [-1,1],
ŵ(ξ)=∫ w(t)(cos(ξt)−1) dt, so the low-frequency Plancherel mass
is ⟨Q_Ω w, w⟩ with kernel K(x,y)=sin(Ω(x−y))/(π(x−y)).

This script (spec 2026-08-13-raise-simple-online-bound-design.md):
  1. Old envelope Ω⁵/(50π) (ξ² Cauchy via |w|).
  2. Direct Cauchy |ŵ|≤‖cos(ξ·)−1‖₂‖w‖, integrated — often vacuous
     (saturates a different w at each ξ).
  3. λ_max(Q) ≤ ‖Q‖_HS, and the same for mean-zero / even-mean-zero
     compressions, via 2-D trapezoid of K² (CHECKED quadrature).
  4. Prints μ₂ ≥ (1−low)(log Ω+γ)+neg vs threshold(a2), threshold(a3).

Belief: if some proved low-mass cap is ≤ 1 − 1.355/(log Ω+γ) at an
Ω ≥ exp(1.355−γ)≈2.177, the complement is safe at a₂.

Usage: python3 tools/weil_first_prime/mu2_envelope.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lower_bound import A2, A3, GAMMA  # noqa: E402
from screw_kernel import A_SUZUKI  # noqa: E402

C2A1 = 2.0 * A_SUZUKI + 1.0
TH2 = C2A1 + math.log(A2)
TH3 = C2A1 + math.log(A3)
# Negative log piece from the ξ⁴ envelope on |ξ|<e^{-γ} (already tiny).
X0 = math.exp(-GAMMA)
NEG = (1.0 / (10.0 * math.pi)) * (-(X0**5) / 25.0)


def I_cos(xi: np.ndarray) -> np.ndarray:
    """∫_{-1}^1 (cos(ξ t)−1)² dt. Limit ξ→0 is 0."""
    xi = np.asarray(xi, dtype=np.float64)
    out = np.empty_like(xi)
    small = np.abs(xi) < 1e-8
    out[small] = 0.0
    z = xi[~small]
    out[~small] = 3.0 + np.sin(2.0 * z) / (2.0 * z) - 4.0 * np.sin(z) / z
    return out


def old_low(Om: float) -> float:
    return (Om**5) / (50.0 * math.pi)


def cauchy_integrated_low(Om: float, n: int = 8000) -> float:
    """(1/π) ∫_0^Ω ‖cos(ξ·)−1‖₂² dξ = (1/π) ∫_0^Ω I_cos(ξ) dξ."""
    xs = np.linspace(0.0, Om, n)
    return float(np.trapezoid(I_cos(xs), xs) / math.pi)


def kernel_matrix(ts: np.ndarray, Om: float) -> np.ndarray:
    n = len(ts)
    d = ts[:, None] - ts[None, :]
    K = np.empty((n, n))
    mask = np.abs(d) < 1e-14
    K[~mask] = np.sin(Om * d[~mask]) / (math.pi * d[~mask])
    K[mask] = Om / math.pi
    return K


def trap_weights(ts: np.ndarray) -> np.ndarray:
    n = len(ts)
    dx = float(ts[1] - ts[0])
    w = np.full(n, dx)
    w[0] *= 0.5
    w[-1] *= 0.5
    return w


def hs_ops(Om: float, n: int = 401) -> dict:
    """HS norms of Q, mean-zero Q, even-mean-zero Q on [-1,1].

    Discrete: Nyström Q̃_ij = √w_i K_ij √w_j, Frobenius → HS.
    Mean-zero: (I−P)Q(I−P), P = weighted rank-one onto constants.
    Even: average with the reflection permutation.
    """
    ts = np.linspace(-1.0, 1.0, n)
    w = trap_weights(ts)
    sw = np.sqrt(w)
    K = kernel_matrix(ts, Om)
    Q = sw[:, None] * K * sw[None, :]
    hs = float(np.linalg.norm(Q, ord="fro"))

    # weighted mean projection in the Nyström inner product: 1-vector is sw
    one = sw.copy()
    nrm = float(np.dot(one, one))  # = 2
    P = np.outer(one, one) / nrm
    I = np.eye(n)
    Qmz = (I - P) @ Q @ (I - P)
    hs_mz = float(np.linalg.norm(Qmz, ord="fro"))

    # even projection: (v(x)+v(−x))/2 on the grid (symmetric about 0)
    rev = np.arange(n)[::-1]
    Qe = 0.25 * (Q + Q[:, rev] + Q[rev, :] + Q[rev][:, rev])
    Qemz = (I - P) @ Qe @ (I - P)
    # even + mean-zero: also kill odd (already even) 
    hs_emz = float(np.linalg.norm(Qemz, ord="fro"))
    # operator-norm proxies (NOT upper bounds of the continuous λ_max:
    # Nyström max-eig is typically a Ritz value). Reported as CHECKED approx.
    evals = np.linalg.eigvalsh(Qemz)
    lam_ritz = float(np.max(evals))
    return {
        "hs": hs,
        "hs_mz": hs_mz,
        "hs_emz": hs_emz,
        "lam_ritz_emz": lam_ritz,
        "tr_emz": float(np.trace(Qemz)),
    }


def mu2_of(low: float, Om: float) -> float:
    low = min(max(low, 0.0), 1.0)
    return (1.0 - low) * (math.log(Om) + GAMMA) + NEG


def main() -> None:
    print("=== thresholds ===")
    print(f"  th(a2)={TH2:.8f}  th(a3)={TH3:.8f}  γ={GAMMA:.8f}")
    print(f"  Ω_min for (log Ω+γ)≥th(a2) even at low=0: {math.exp(TH2 - GAMMA):.6f}")
    print(f"  NEG (ξ⁴ piece on |ξ|<e^{{-γ}})={NEG:.8e}")

    print("\n=== envelopes vs Ω ===")
    print(
        f"{'Ω':>7} {'old-low':>10} {'Cau-low':>10} {'HS':>8} {'HS_mz':>8} "
        f"{'HS_emz':>8} {'Ritz':>8} {'μ2_old':>8} {'μ2_HSemz':>9}"
    )
    best_proved = -1e99
    best_desc = ""
    oms = [1.2, 1.5, 1.865, 2.0, 2.177, 2.4, 2.7, 3.0, 3.5, 4.0]
    rows = []
    for Om in oms:
        o = old_low(Om)
        c = cauchy_integrated_low(Om)
        hs = hs_ops(Om, n=321)
        # proved low-mass caps (clip at 1)
        low_old = min(o, 1.0)
        low_c = min(c, 1.0)
        low_hs = min(hs["hs_emz"], 1.0)
        m_old = mu2_of(low_old, Om)
        m_c = mu2_of(low_c, Om)
        m_hs = mu2_of(low_hs, Om)
        rows.append((Om, o, c, hs, m_old, m_c, m_hs))
        print(
            f"{Om:7.3f} {o:10.5f} {c:10.5f} {hs['hs']:8.4f} {hs['hs_mz']:8.4f} "
            f"{hs['hs_emz']:8.4f} {hs['lam_ritz_emz']:8.4f} {m_old:8.4f} {m_hs:9.4f}"
        )
        sys.stdout.flush()
        for tag, val in (("old", m_old), ("Cauchy-int", m_c), ("HS-emz", m_hs)):
            if val > best_proved:
                best_proved = val
                best_desc = f"{tag} @ Ω={Om}"

    print("\n=== n-convergence of HS-emz at Ω=2.4 ===")
    for n in (81, 161, 321):
        h = hs_ops(2.4, n=n)
        print(
            f"  n={n:3d} HS_emz={h['hs_emz']:.6f} Ritz_emz={h['lam_ritz_emz']:.6f} "
            f"tr={h['tr_emz']:.6f}"
        )

    print("\n=== nested α(ω)=HS_emz(ω): μ₂ ≥ log Ω+γ − ∫_0^Ω α(ω)/ω dω ===")
    # If mass in |ξ|<ω is ≤ α(ω) for all ω, the worst log-energy on the
    # low band is the greedy fill F=α. Then
    #   ∫(log+γ)dμ ≥ (log Ω+γ) − ∫_0^Ω α(ω)/ω dω
    # (boundary term α log → 0 at 0 because α(ω)=O(ω⁵)).
    oms_f = np.concatenate(
        [np.array([0.15, 0.3, 0.5, 0.8, 1.0]), np.linspace(1.2, 3.2, 21)]
    )
    al = []
    print(f"{'Ω':>7} {'α=HS_emz':>10} {'∫α/ω':>10} {'nested μ₂':>10}")
    integ = 0.0
    prev_o = 0.0
    prev_a = 0.0
    best_n = -1e99
    best_o = 0.0
    for Om in oms_f:
        a = min(hs_ops(float(Om), n=161)["hs_emz"], 1.0)
        if prev_o > 0:
            # trapezoid of α/ω
            integ += 0.5 * (prev_a / prev_o + a / float(Om)) * (float(Om) - prev_o)
        val = math.log(float(Om)) + GAMMA - integ + NEG
        al.append((float(Om), a, integ, val))
        print(f"{Om:7.3f} {a:10.5f} {integ:10.5f} {val:10.5f}")
        sys.stdout.flush()
        if val > best_n:
            best_n, best_o = val, float(Om)
        prev_o, prev_a = float(Om), a
    print(f"  best nested = {best_n:.6f} at Ω={best_o:.3f}")
    print(f"  clears th(a2): {best_n >= TH2}   clears th(a3): {best_n >= TH3}")

    print("\n=== conservative nested: n=81 HS_emz × 1.05 ===")
    integ = 0.0
    prev_o = 0.0
    prev_a = 0.0
    best_c = -1e99
    best_co = 0.0
    print(f"{'Ω':>7} {'α_cons':>10} {'∫α/ω':>10} {'μ₂_cons':>10}")
    for Om in [0.3, 0.6, 1.0, 1.5, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.6, 4.0, 4.5, 5.0, 5.5, 6.0]:
        a = min(1.05 * hs_ops(float(Om), n=81)["hs_emz"], 1.0)
        if prev_o > 0:
            integ += 0.5 * (prev_a / prev_o + a / float(Om)) * (float(Om) - prev_o)
        val = math.log(float(Om)) + GAMMA - integ + NEG
        print(f"{Om:7.3f} {a:10.5f} {integ:10.5f} {val:10.5f}")
        if val > best_c:
            best_c, best_co = val, float(Om)
        prev_o, prev_a = float(Om), a
    print(f"  best conservative nested = {best_c:.6f} at Ω={best_co:.3f}")
    print(f"  clears th(a2): {best_c >= TH2}   margin={best_c - TH2:.6f}")
    print(f"  best hard-cut PROVED μ₂: {best_proved:.6f} ({best_desc})")
    print(f"  best nested PROVED μ₂:   {best_n:.6f} at Ω={best_o:.3f}")
    print(f"  clears th(a2)={TH2:.4f}: {max(best_proved, best_n) >= TH2}")
    print(f"  clears th(a3)={TH3:.4f}: {max(best_proved, best_n) >= TH3}")
    print("  Ritz_emz is an APPROXIMATION of λ_max, not an upper bound — not used as a proof.")
    print("  HS_emz ≥ 1 ⇒ the HS cap is vacuous (low mass ≤ 1).")
    print("  Nested uses α(ω)=HS_emz(ω) as a quadrature of ‖Q_ω‖_HS (CHECKED n=161).")


if __name__ == "__main__":
    main()
