#!/usr/bin/env python3
"""(4.6) Fourier formula for L, J-ground-state LB, global min of −ρ''/t².

Suzuki (4.6): L(w) = (1/2π) ∫ (log|z|+γ) |ŵ(z)|² dz
with ŵ(ξ)=∫_{-1}^1 w(t) e^{−iξt} dt  (so ‖w‖²=(1/2π)∫|ŵ|²).

Belief: if (4.6) matches the jumping-form L, then a Paley–Wiener tail
gives a lower bound on μ₂ (second even eigenvalue), reducing the first
prime window to a 1-mode calculation. Independently: if −ρ''/t² has a
positive global min, the ρ lower bound is uniform in a.

Usage: python3 tools/weil_first_prime/l_fourier.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dirichlet_vs_prime import L_a  # noqa: E402
from lower_bound import A2, A3, GAMMA, LOG2, PRIME2_COEFF  # noqa: E402
from remainder_bound import hankel_lag  # noqa: E402
from rpp_closed import rpp_closed  # noqa: E402
from screw_kernel import A_SUZUKI  # noqa: E402

A = A_SUZUKI
C2A1 = 2.0 * A + 1.0


def what_cosine(xi: np.ndarray) -> np.ndarray:
    """Fourier transform of cos(π t/2) on [-1,1]: π cos ξ / ((π/2)²−ξ²)."""
    w = 0.5 * math.pi
    xi = np.asarray(xi, dtype=np.float64)
    out = np.empty_like(xi)
    for i, x in enumerate(xi):
        if abs(abs(x) - w) < 1e-10:
            # L'Hôpital: π (−sin ξ) / (−2ξ) at ξ=±π/2 → π (∓1) / (∓π) = 1
            out[i] = 1.0
        else:
            out[i] = math.pi * math.cos(x) / (w * w - x * x)
    return out


def ft_grid(w: np.ndarray, ts: np.ndarray, ximax: float, nxi: int) -> tuple[np.ndarray, np.ndarray]:
    xi = np.linspace(-ximax, ximax, nxi)
    # ŵ(ξ)=∫ w(t) cos(ξ t) dt  (even w) or with sin (odd)
    even = float(np.trapezoid(w * ts, ts))  # ∫ t w : 0 if even
    # vectorized: trapz w(t) e^{-iξt} = trapz w cos + i ...
    wt = w
    # Riemann: dx * sum w * exp
    dx = float(ts[1] - ts[0])
    # use np for all xi
    phase = np.exp(-1j * xi[:, None] * ts[None, :])
    # trapezoid weights
    wg = np.full(len(ts), dx)
    wg[0] *= 0.5
    wg[-1] *= 0.5
    what = phase @ (wt * wg)
    return xi, what


def L_from_ft(xi: np.ndarray, what: np.ndarray) -> tuple[float, float]:
    """(1/2π)∫ (log|ξ|+γ)|ŵ|²  and Plancherel (1/2π)∫|ŵ|²."""
    dxi = float(xi[1] - xi[0])
    abs2 = np.abs(what) ** 2
    # log|ξ|: clip
    logabs = np.log(np.maximum(np.abs(xi), 1e-18))
    I_L = float(np.sum((logabs + GAMMA) * abs2) * dxi / (2.0 * math.pi))
    I_n = float(np.sum(abs2) * dxi / (2.0 * math.pi))
    return I_L, I_n


def j_ground_state(n: int = 201, M: int = 5) -> dict:
    ts = np.linspace(-1.0, 1.0, n)
    phis = [np.cos((k + 0.5) * math.pi * ts) for k in range(M)]
    Lmat = np.zeros((M, M))
    B = np.zeros((M, M))
    ones = np.zeros(M)
    for j in range(M):
        ones[j] = float(np.trapezoid(phis[j], ts))
        for i in range(j, M):
            u, v = phis[i], phis[j]
            Lu = L_a(u, ts, 1.0)
            Lv = L_a(v, ts, 1.0)
            Luv = L_a(u + v, ts, 1.0)
            Lmat[i, j] = Lmat[j, i] = 0.5 * (Luv - Lu - Lv)
            B[i, j] = B[j, i] = float(np.trapezoid(u * v, ts))
    kappa = (7.0 / 4.0) * A2
    Jmat = Lmat + kappa * np.outer(ones, ones)
    # generalized eigen: J c = ν B c
    evals, evecs = np.linalg.eig(np.linalg.solve(B, Jmat))
    idx = int(np.argmin(np.real(evals)))
    nu = float(np.real(evals[idx]))
    c = np.real(evecs[:, idx])
    w = sum(c[k] * phis[k] for k in range(M))
    if float(np.trapezoid(w, ts)) < 0:
        w = -w
        c = -c
    nrm = float(np.trapezoid(w * w, ts))
    Lw = L_a(w, ts, 1.0) / nrm
    iw = float(np.trapezoid(w, ts))
    ix2 = float(np.trapezoid(ts * ts * w, ts))
    rank1 = kappa * (iw * iw) / nrm
    q2 = 2.0 * iw * ix2  # even
    # c* on (0, 2 a3]
    S = 2.0 * A3
    cstar = min(-(rpp_closed(S * k / 4000) + 1.75) / (S * k / 4000) ** 2 for k in range(1, 4001))
    rho_lo = cstar * (A2**3) * q2 / nrm
    th = C2A1 + math.log(A2)
    return {
        "nu": nu,
        "c": c,
        "L": Lw,
        "rank1": rank1,
        "mean2": (iw * iw) / nrm,
        "rho_lo": rho_lo,
        "cstar": cstar,
        "J_minus_th": Lw + rank1 - th,
        "LB": math.log(1 / A2) - C2A1 + Lw + rank1 + rho_lo,
        "min_w": float(np.min(w)),
        "th": th,
        "nrm": nrm,
    }


def global_cstar(tmax: float = 20.0, n: int = 20000) -> dict:
    cmin = 1e99
    tmin = 0.0
    rhomax = -1e99
    for k in range(1, n + 1):
        t = tmax * k / n
        rho = rpp_closed(t) + 1.75
        rhomax = max(rhomax, rho)
        val = -rho / (t * t)
        if val < cmin:
            cmin = val
            tmin = t
    return {"cmin": cmin, "tmin": tmin, "rhomax": rhomax, "tmax": tmax}


def main() -> None:
    print("=== (4.6) vs jumping L, even cosine ===")
    ts = np.linspace(-1.0, 1.0, 801)
    w = np.cos(0.5 * math.pi * ts)
    nrm = float(np.trapezoid(w * w, ts))
    Ljump = L_a(w, ts, 1.0)
    print(f"  ‖w‖²={nrm:.8f}  L_jump={Ljump:.8f}  L/n={Ljump/nrm:.8f}")
    # Split quadrature of even integrand: log-grid near 0 + linear tail.
    # ŵ closed form; factor 2 for ξ>0. Plancherel and log-weight separately.
    xi_lo = np.geomspace(1e-8, 1.0, 8000)
    xi_hi = np.linspace(1.0, 800.0, 80000)[1:]
    xi = np.concatenate([xi_lo, xi_hi])
    wc = what_cosine(xi)
    # trapezoid on a non-uniform grid
    dxi = np.diff(xi)
    mid_w = 0.5 * (wc[:-1] ** 2 + wc[1:] ** 2)
    mid_log = 0.5 * (
        (np.log(xi[:-1]) + GAMMA) * wc[:-1] ** 2
        + (np.log(xi[1:]) + GAMMA) * wc[1:] ** 2
    )
    In = 2.0 * float(np.sum(mid_w * dxi)) / (2.0 * math.pi)  # ×2 for ±
    IL = 2.0 * float(np.sum(mid_log * dxi)) / (2.0 * math.pi)
    print(f"  split-quad closed ŵ: Plancherel={In:.8f}  L_ft={IL:.8f}  L_ft−L_jump={IL-Ljump:.6f}")
    print(f"  avg log|ξ| = {IL - GAMMA*In:.8f}  (γ·Plancherel={GAMMA*In:.8f})")

    print("\n=== J-ground-state (even Dirichlet Ritz) at a2 ===")
    gs = j_ground_state()
    print(f"  coeffs c={gs['c']}")
    print(f"  ν_Ritz={gs['nu']:.8f}  threshold={gs['th']:.8f}")
    print(f"  L={gs['L']:.8f}  rank1={gs['rank1']:.8f}  (∫w)²/n={gs['mean2']:.8f}")
    print(f"  min w={gs['min_w']:.6f}  (negative ⇒ not nonnegative)")
    print(f"  J-th={gs['J_minus_th']:.8f}  ρ_lo={gs['rho_lo']:.8f}  LB={gs['LB']:.8f}")

    print("\n=== global min of −ρ''(t)/t² ===")
    for tmax in (4.0, 20.0):
        g = global_cstar(tmax=tmax, n=20000)
        print(
            f"  t∈(0,{tmax}]: min={g['cmin']:.8f} at t={g['tmin']:.4f}  "
            f"max ρ''={g['rhomax']:.8f}"
        )

    print("\n=== crude μ₂ lower bound via |ŵ|≤√(2/3)|ξ|‖w‖ on {ŵ(0)=0} ===")
    # On |ξ|<e^{−γ}, log|ξ|+γ<0: use the envelope; drop the positive tail.
    x0 = math.exp(-GAMMA)
    I_neg = -(x0**3) / 9.0  # ∫_0^{x0} (log ξ + γ) ξ² dξ
    crude = 2.0 * I_neg / (3.0 * math.pi)
    print(f"  e^{{-γ}}={x0:.6f}  ∫_0^{{x0}}(log+γ)ξ²={I_neg:.6f}")
    print(f"  L/‖w‖² ≥ {crude:.6f}  (drop |ξ|>e^{{-γ}}; vs th(a2)={C2A1+math.log(A2):.3f})")

    print("\n=== VERDICT ===")
    print("  If L_ft matches L_jump to ~1e-3, (4.6) is implemented with this FT convention.")
    print("  If J-ground LB>0, ρ_lower saves the variational ground state of J at a2.")
    print("  If global min(−ρ''/t²)>0 and max ρ''<0, ρ''<0 for all t in the scan.")
    print("  Crude PW envelope on mean-zero is vacuous if it is ≪ threshold.")


if __name__ == "__main__":
    main()
