#!/usr/bin/env python3
"""Poincaré overlap + saturating two-bump + high-frequency K-split.

Belief this changes:
  (1) whether |G(log 2)| ≤ ε² ‖v'‖² is saturated by endpoint ramps
      (lemma shape; if the ratio exceeds 1 the lemma is false);
  (2) whether the geometrically-saturating two-bump family (prime-2 at
      maximum overlap for given ε) already goes negative in T
      (a genuine negative direction would refute positivity on that a);
  (3) the smallest K such that inf_{|v|≥K} Re ψ(1/4+iv/2) beats
      log π + √2 log 2, i.e. high modes are safe even with the crude
      prime bound — which reduces the missing lemma to a low-frequency
      matrix of size O(K a).

T is Bombieri's form via probe.T_of_G (same as the Ritz probe).
Digamma via recurrence + Stirling seed (self-checked against ψ(1)=−γ
and ψ(1/4)=−γ−π/2−3 log 2).

Usage: python3 tools/weil_first_prime/lower_bound.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe import (  # noqa: E402
    A2,
    A3,
    T_of_G,
    autocorrelation,
    even_basis,
)

LOG2 = math.log(2.0)
GAMMA = 0.5772156649015328606
PRIME2_COEFF = math.sqrt(2.0) * LOG2  # T_prime = −this · G(log 2) for even G
PSI_QUARTER = -GAMMA - 0.5 * math.pi - 3.0 * LOG2  # exact


def re_psi_line(xi: np.ndarray, n_rec: int = 80) -> np.ndarray:
    """Re ψ(1/4 + i ξ/2) on a real grid.

    Recurrence: ψ(z) = ψ(z+n) − Σ_{j=0}^{n−1} 1/(z+j),
    seed ψ(w) ∼ log w − 1/(2w) − 1/(12 w²) + 1/(120 w⁴) − 1/(252 w⁶).
    """
    xi = np.asarray(xi, dtype=np.float64)
    out = np.empty(xi.shape, dtype=np.float64)
    for i, x in enumerate(xi.ravel()):
        z = 0.25 + 0.5j * float(x)
        acc = 0j
        zz = z
        for _ in range(n_rec):
            acc += 1.0 / zz
            zz = zz + 1.0
        inv = 1.0 / zz
        inv2 = inv * inv
        inv4 = inv2 * inv2
        inv6 = inv4 * inv2
        psi_w = np.log(zz) - 0.5 * inv - (1.0 / 12.0) * inv2
        psi_w += (1.0 / 120.0) * inv4 - (1.0 / 252.0) * inv6
        out.flat[i] = (psi_w - acc).real  # minus: ψ(z) = ψ(z+n) − sum
    return out.reshape(xi.shape)


def check_psi() -> None:
    def psi_real(z: complex) -> float:
        acc = 0j
        zz = z
        for _ in range(80):
            acc += 1.0 / zz
            zz = zz + 1.0
        inv = 1.0 / zz
        inv2 = inv * inv
        inv4 = inv2 * inv2
        inv6 = inv4 * inv2
        psi_w = np.log(zz) - 0.5 * inv - (1.0 / 12.0) * inv2
        psi_w += (1.0 / 120.0) * inv4 - (1.0 / 252.0) * inv6
        return (psi_w - acc).real

    e1 = abs(psi_real(1.0 + 0j) + GAMMA)
    e2 = abs(psi_real(2.0 + 0j) - (-GAMMA + 1.0))
    e4 = abs(psi_real(0.25 + 0j) - PSI_QUARTER)
    print(f"  ψ(1)+γ          = {psi_real(1.0 + 0j) + GAMMA:.3e}  (want 0)")
    print(f"  ψ(2)+γ−1        = {psi_real(2.0 + 0j) + GAMMA - 1.0:.3e}  (want 0)")
    print(f"  ψ(1/4)−closed   = {psi_real(0.25 + 0j) - PSI_QUARTER:.3e}  (want 0)")
    print(f"  closed ψ(1/4)   = {PSI_QUARTER:.12f}")
    if max(e1, e2, e4) > 1e-12:
        print("FAIL psi sanity")
        sys.exit(1)
    print("  PASS psi sanity")


def linear_two_bump(a: float, width: float, n: int = 4001) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Even endpoint ramps: v(±a)=0, linear on strips of `width`, 0 in the middle.

    Equality case of the strip Poincaré bound (v' constant on each strip).
    For a = a2+ε the saturating choice is width = 2ε (full overlap strips).
    """
    xs = np.linspace(-a, a, n)
    v = np.zeros_like(xs)
    dist_right = a - xs
    dist_left = xs + a
    m_r = (dist_right >= 0.0) & (dist_right <= width)
    m_l = (dist_left >= 0.0) & (dist_left <= width) & ~m_r
    v[m_r] = dist_right[m_r] / width
    v[m_l] = dist_left[m_l] / width
    vp = np.zeros_like(xs)
    vp[m_r] = -1.0 / width
    vp[m_l] = 1.0 / width
    return xs, v, vp


def rayleigh_of_v(v: np.ndarray, xs: np.ndarray, primes: bool) -> dict:
    a = float(xs[-1])
    dx = float(xs[1] - xs[0])
    taus, G = autocorrelation(v, dx)
    T = T_of_G(taus, G, a, primes=primes)
    G0 = float(np.interp(0.0, taus, G))
    Glog2 = float(np.interp(LOG2, taus, G, left=0.0, right=0.0))
    return {
        "T": T,
        "G0": G0,
        "G_log2": Glog2,
        "rayleigh": T / G0 if G0 > 0 else float("nan"),
    }


def two_bump_row(eps: float, n: int = 4001) -> dict:
    a = A2 + eps
    width = 2.0 * eps  # full overlap strips of length 2ε
    if width >= a - 1e-15:
        raise ValueError("strips would overlap the origin; eps too large")
    xs, v, vp = linear_two_bump(a, width, n)
    dx = float(xs[1] - xs[0])
    g0_direct = float(np.trapezoid(v * v, xs))
    vp2 = float(np.trapezoid(vp * vp, xs))
    r_on = rayleigh_of_v(v, xs, primes=True)
    r_off = rayleigh_of_v(v, xs, primes=False)
    g_log2 = r_on["G_log2"]
    # Poincaré ratio: |G(log 2)| / (ε² ‖v'‖²)  should be ≤ 1
    poinc = abs(g_log2) / (eps * eps * vp2) if eps > 0 and vp2 > 0 else float("nan")
    return {
        "eps": eps,
        "a": a,
        "width": width,
        "G0": r_on["G0"],
        "G0_direct": g0_direct,
        "G_log2": g_log2,
        "G_log2_over_G0": g_log2 / r_on["G0"],
        "vp2": vp2,
        "vp2_over_G0": vp2 / r_on["G0"],
        "poincare_ratio": poinc,
        "rayleigh": r_on["rayleigh"],
        "rayleigh_no_prime": r_off["rayleigh"],
        "prime_term_over_G0": -PRIME2_COEFF * g_log2 / r_on["G0"],
        "dx": dx,
    }


def cosine_plus_bump_matrix(eps: float, n: int = 2001) -> dict:
    """2×2 Ritz in span{first even Dirichlet cosine, saturating two-bump}.

    If the lowest generalized eigenvalue is negative, that is a genuine
    negative direction (upper bound on λ_true that has gone below 0).
    """
    a = A2 + eps
    xs = np.linspace(-a, a, n)
    dx = float(xs[1] - xs[0])
    phi = np.cos(0.5 * math.pi * xs / a)
    _, bump, _ = linear_two_bump(a, 2.0 * eps, n)
    # orthonormalize in L² via mass matrix
    cols = np.stack([phi, bump], axis=1)  # (n, 2)
    B = cols.T @ cols * dx
    # Q via polarization
    def Q(c: np.ndarray) -> float:
        v = cols @ c
        taus, G = autocorrelation(v, dx)
        return T_of_G(taus, G, a, primes=True)

    H = np.zeros((2, 2))
    e0, e1 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
    H[0, 0] = Q(e0)
    H[1, 1] = Q(e1)
    H[0, 1] = H[1, 0] = 0.5 * (Q(e0 + e1) - H[0, 0] - H[1, 1])
    # Generalized eigen: H c = λ B c. Do NOT use eigvalsh(B^{-1} H):
    # B^{-1} H is not symmetric when ⟨φ, bump⟩ ≠ 0, and eigvalsh then
    # returns garbage (a spurious negative was observed). Cholesky:
    # B = L L^T,  L^{-1} H L^{-T} y = λ y.
    L = np.linalg.cholesky(0.5 * (B + B.T))
    A = np.linalg.solve(L, H)
    A = np.linalg.solve(L, A.T).T
    A = 0.5 * (A + A.T)
    evals = np.linalg.eigvalsh(A)
    return {
        "eps": eps,
        "a": a,
        "lam_min": float(np.min(evals.real)),
        "lam_max": float(np.max(evals.real)),
        "H00": H[0, 0],
        "H11": H[1, 1],
        "H01": H[0, 1],
        "cos_rayleigh": H[0, 0] / B[0, 0],
        "bump_rayleigh": H[1, 1] / B[1, 1],
        "B01": B[0, 1],
    }


def k_split_table() -> dict:
    """inf_{ξ≥K} Re ψ(1/4+iξ/2) vs the crude high-frequency floor."""
    xi = np.linspace(0.0, 80.0, 16001)
    re_psi = re_psi_line(xi)
    floor_target = math.log(math.pi) + PRIME2_COEFF  # log π + √2 log 2
    rows = []
    k_star = None
    for K in (1.0, 2.0, 3.0, 5.0, 8.0, 10.0, 12.0, 16.0, 20.0, 30.0, 40.0):
        m = xi >= K - 1e-15
        infK = float(np.min(re_psi[m]))
        margin = infK - floor_target
        rows.append((K, infK, margin))
        if k_star is None and margin > 0:
            k_star = K
    # finer search for first K with margin>0
    for K in np.linspace(1.0, 40.0, 391):
        m = xi >= K - 1e-15
        infK = float(np.min(re_psi[m]))
        if infK > floor_target:
            k_star_fine = float(K)
            break
    else:
        k_star_fine = float("nan")
    i_min_diff = None
    logp = np.log(np.maximum(xi, 1.0))
    r = re_psi - logp
    i = int(np.argmin(r))
    return {
        "floor_target": floor_target,
        "rows": rows,
        "k_star": k_star,
        "k_star_fine": k_star_fine,
        "re_psi_0": float(re_psi[0]),
        "inf_re_psi_minus_logplus": float(r[i]),
        "xi_at_that_inf": float(xi[i]),
        "re_psi_at_20": float(re_psi[np.argmin(np.abs(xi - 20.0))]),
    }


def fourier_vs_probe_check() -> None:
    """Cross-check: (1/2π)∫ Reψ Ĝ + 2cosh − log π  vs probe T, a=0.20, no primes."""
    a = 0.20
    xs = np.linspace(-a, a, 801)
    dx = float(xs[1] - xs[0])
    v = np.cos(0.5 * math.pi * xs / a)
    taus, G = autocorrelation(v, dx)
    T_probe = T_of_G(taus, G, a, primes=False)
    G0 = float(np.interp(0.0, taus, G))
    # Ĝ(v) = ∫ G(x) e^{-ivx} dx
    vmax = 80.0
    vs = np.linspace(-vmax, vmax, 4001)
    # G even ⇒ Ĝ(v) = 2 ∫_0^∞ G(x) cos(vx) dx
    Ghat = np.array([float(np.trapezoid(G * np.cos(vv * taus), taus)) for vv in vs])
    re_psi = re_psi_line(np.abs(vs))
    T_psi = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(re_psi * Ghat, vs))
    T_cosh = float(np.trapezoid(2.0 * np.cosh(taus / 2.0) * G, taus))
    T_four = T_cosh - math.log(math.pi) * G0 + T_psi
    plancherel = (1.0 / (2.0 * math.pi)) * float(np.trapezoid(Ghat, vs))
    print("=== Fourier T vs probe T (a=0.20, cosine, no primes) ===")
    print(f"  G0={G0:.8f}  Plancherel (1/2π)∫Ĝ = {plancherel:.8f}  rel={abs(plancherel-G0)/G0:.3e}")
    print(f"  T_probe  = {T_probe:.8e}")
    print(f"  T_fourier= {T_four:.8e}  (2cosh={T_cosh:.6e}  −logπ G0={-math.log(math.pi)*G0:.6e}  ψ={T_psi:.6e})")
    print(f"  rel |T_fourier − T_probe|/|T_probe| = {abs(T_four - T_probe) / max(abs(T_probe), 1e-30):.3e}")


def main() -> None:
    print("=== psi sanity ===")
    check_psi()

    print("\n=== Poincaré constants (elementary, printed for the note) ===")
    print("  For a=a2+ε, overlap strips have width 2ε.")
    print("  |v(a−s)|² ≤ s ∫_0^s |v'(a−u)|² du  ⇒  ‖v‖_{right}² ≤ 2 ε² ‖v'‖_R².")
    print("  |G(log 2)| ≤ ‖v‖_R ‖v‖_L ≤ ε² ‖v'‖².")
    print("  Saturating family: linear ramps of width 2ε (v' constant on strips).")

    print("\n=== Saturating two-bump Rayleigh (width=2ε, primes on) ===")
    hdr = (
        f"{'eps':>10} {'a':>10} {'G(log2)/G0':>13} {'Poincaré':>10} "
        f"{'T/G0 no p':>11} {'T/G0':>11} {'prime/G0':>11} {'‖v\'‖²/G0':>11}"
    )
    print(hdr)
    bump_rows = []
    # stay below a3 and keep strips disjoint from the origin: 2ε < a = a2+ε ⇒ ε < a2
    eps_list = [1e-3, 5e-3, 1e-2, 2e-2, 5e-2, 0.08, 0.10, 0.15, A3 - A2 - 1e-3]
    for eps in eps_list:
        r = two_bump_row(eps, n=4001)
        bump_rows.append(r)
        print(
            f"{r['eps']:10.6f} {r['a']:10.6f} {r['G_log2_over_G0']:13.6e} "
            f"{r['poincare_ratio']:10.4f} {r['rayleigh_no_prime']:11.6f} "
            f"{r['rayleigh']:11.6f} {r['prime_term_over_G0']:11.6f} "
            f"{r['vp2_over_G0']:11.3e}"
        )
        sys.stdout.flush()

    print("\n=== 2×2 Ritz: cosine ⊕ two-bump (even, primes on) ===")
    print(f"{'eps':>10} {'λ_min':>12} {'λ_max':>12} {'cos T/G0':>12} {'bump T/G0':>12}")
    mix_rows = []
    for eps in (1e-2, 5e-2, 0.10, A3 - A2 - 1e-3):
        m = cosine_plus_bump_matrix(eps, n=2001)
        mix_rows.append(m)
        print(
            f"{m['eps']:10.6f} {m['lam_min']:12.6e} {m['lam_max']:12.6e} "
            f"{m['cos_rayleigh']:12.6e} {m['bump_rayleigh']:12.6e}"
        )
        sys.stdout.flush()

    print("\n=== High-frequency K-split (Reψ vs log π + √2 log 2) ===")
    ks = k_split_table()
    print(f"  Reψ(1/4) = {ks['re_psi_0']:.12f}  (closed form {PSI_QUARTER:.12f})")
    print(f"  floor_target logπ + √2 log 2 = {ks['floor_target']:.12f}")
    print(f"  inf (Reψ − log⁺|ξ|) = {ks['inf_re_psi_minus_logplus']:.6f} at ξ={ks['xi_at_that_inf']:.4f}")
    print(f"  {'K':>8} {'inf_{ξ≥K} Reψ':>16} {'margin vs floor':>16}")
    for K, infK, margin in ks["rows"]:
        print(f"  {K:8.1f} {infK:16.6f} {margin:16.6f}")
    print(f"  first tabulated K with margin>0: {ks['k_star']}")
    print(f"  first K on 0.1-grid with margin>0: {ks['k_star_fine']:.2f}")
    # dimension of low even Dirichlet space: (M−1/2) π / a ≥ K  ⇒ M ≥ K a/π + 1/2
    for a, tag in ((A2, "a2"), (0.5 * (A2 + A3), "mid"), (A3, "a3")):
        K = ks["k_star_fine"]
        Mneed = K * a / math.pi + 0.5
        print(f"  even Dirichlet modes with freq ≥ K={K:.2f} at {tag}: M ≳ {Mneed:.2f}")

    print("\n=== Dirichlet even-mode matrix decay (mid-window, primes on) ===")
    # Belief: whether |H_{0j}| decays fast enough that a Gershgorin lower
    # bound on the ground row could stay positive. M=6 N=401 is enough to
    # see the shape; this is exploratory f64, not a certificate.
    from probe import rayleigh_matrix

    a_mid = 0.5 * (A2 + A3)
    Mdec, Ndec = 6, 401
    H, B = rayleigh_matrix(a_mid, M=Mdec, N=Ndec, primes=True)
    H = 0.5 * (H + H.T)
    B = 0.5 * (B + B.T)
    # Rayleigh matrix R = B^{-1/2} H B^{-1/2}; cosine basis ⇒ B ≈ a I
    scale = np.sqrt(np.diag(B))
    R = H / np.outer(scale, scale)
    print(f"  a={a_mid:.6f} M={Mdec} N={Ndec}  B_ii={np.diag(B)}")
    print(f"  R_ii (diagonal Rayleigh) = {np.diag(R)}")
    print(f"  |R_0j| = {np.abs(R[0, :])}")
    gersh0 = R[0, 0] - (np.sum(np.abs(R[0, :])) - abs(R[0, 0]))
    print(f"  Gershgorin lower on mode-0 row = {gersh0:.6e}  (R00={R[0,0]:.6e})")
    gersh = [R[i, i] - (np.sum(np.abs(R[i, :])) - abs(R[i, i])) for i in range(Mdec)]
    print(f"  Gershgorin lowers = {gersh}")
    print(f"  min Gershgorin = {min(gersh):.6e}")
    L = np.linalg.cholesky(B)
    A = np.linalg.solve(L, H)
    A = np.linalg.solve(L, A.T).T
    evals = np.linalg.eigvalsh(0.5 * (A + A.T))
    print(f"  true min eig (Cholesky, {Mdec}-mode subspace) = {float(np.min(evals)):.6e}")

    fourier_vs_probe_check()

    print("\n=== VERDICT ===")
    ratios = [r["poincare_ratio"] for r in bump_rows]
    print(f"  max Poincaré ratio on saturating family = {max(ratios):.6f}  (lemma needs ≤ 1)")
    if max(ratios) > 1.01:
        print("  FAIL: Poincaré lemma numerically violated — do not claim it.")
        sys.exit(1)
    signs = [r["rayleigh"] for r in bump_rows]
    mix_signs = [m["lam_min"] for m in mix_rows]
    i_min = int(np.argmin(signs))
    print(f"  min two-bump Rayleigh = {signs[i_min]:.6e} at eps={bump_rows[i_min]['eps']:.6f}")
    print(f"  min 2×2 (cos⊕bump) Rayleigh = {min(mix_signs):.6e}")
    if any(s < 0 for s in signs + mix_signs):
        print("  NEGATIVE direction found — inspect T (must stay >0 for a<a2) before any RH claim.")
    else:
        print("  No negative direction in saturating two-bump or cos⊕bump 2×2.")
        print("  Narrow bumps are safer (log-growth); G(log2)/G0 → 1/4 (not 0) on this family")
        print("  but ‖v'‖²/G0 → ∞ as ε→0, so the archimedean floor wins.")
    print("  High-frequency modes are crude-prime-safe for K ≥ "
          f"{ks['k_star_fine']:.2f}. Missing lemma = low-frequency matrix.")
    print("  This does NOT prove λ_a>0. Ritz is still an upper bound.")


if __name__ == "__main__":
    main()
