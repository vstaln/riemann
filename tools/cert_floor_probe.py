#!/usr/bin/env python3
"""Fast float-level exploration of the certificate parameter space.

Two searches, both double precision (float) — exploratory, NOT certified:

  (1) floor_probe:  given a window (cosine alpha or trig-poly) and a
      weighted 7-point design (pressure p, weights a_ij summing to span
      capacity 2), estimate the per-window floor
          F(g) = p*sum g_i + sum_{i<j} a_ij w(y_j - y_i)   (g_i >= 0)
      by dense grid sampling + local refinement (Nelder-Mead on 6 gaps).
      This estimates what eps a certificate could certify for that design.

  (2) joint_bound:  given a window's certified H and the float floor eps,
      evaluate the master-chain bound over m (cap=h and cap=phi),
      and report the max.

Kernel w(x) = (K(x)/K(0))^2 evaluated in float with the closed form
  K(x) = sum_j c_j * (sinc((w_j - 2pi x)/2) + sinc((w_j + 2pi x)/2))/2,
  sinc = sin(z)/z.  The cosine window v=cos(alpha s) has K = I0-scaled
  single term with omega=alpha; the trig-poly windows use their coefficients.
"""

from __future__ import annotations

import math
import random
from functools import lru_cache

import numpy as np

# ---------------------------------------------------------------------------
# Kernel in float
# ---------------------------------------------------------------------------

def _sinc(z: float) -> float:
    return 1.0 if z == 0.0 else math.sin(z) / z


class Kernel:
    def __init__(self, coeffs, omegas):
        """omegas in rad/s; K(x) = sum_j coeffs[j] S(omega_j, 2 pi x)."""
        self.coeffs = list(coeffs)
        self.omegas = list(omegas)
        k0 = 0.0
        for c, w in zip(self.coeffs, self.omegas):
            k0 += c * 2 * math.sin(w / 2) / w
        self.k0 = k0
        self.k0sq = k0 * k0

    def K(self, x: float) -> float:
        total = 0.0
        for c, w in zip(self.coeffs, self.omegas):
            a = (w - 2 * math.pi * x) / 2
            b = (w + 2 * math.pi * x) / 2
            total += c * (_sinc(a) + _sinc(b)) / 2
        return total

    def w(self, x: float) -> float:
        k = self.K(x)
        return (k / self.k0) ** 2


@lru_cache(maxsize=None)
def cosine_kernel(alpha: float):
    return Kernel([1.0], [alpha])


def mt_kernel():
    return Kernel([1.0], [math.sqrt(2)])


# ---------------------------------------------------------------------------
# F(g) evaluation
# ---------------------------------------------------------------------------

def make_F(kernel, p, weights, q=6):
    """weights: dict (i,j)->a_ij for 0<=i<j<=q."""
    pair_list = sorted(weights)

    def F(g):
        # g tuple of q+1... actually q gaps => q+1 points; use q gaps.
        y = [0.0]
        for gi in g:
            y.append(y[-1] + gi)
        total = p * sum(g)
        for i, j in pair_list:
            total += weights[(i, j)] * kernel.w(y[j] - y[i])
        return total

    return F, pair_list


def uniform_weights(q=6):
    """canonical a_ij = 2/(q+1-(j-i))"""
    w = {}
    for i in range(q + 1):
        for j in range(i + 1, q + 1):
            w[(i, j)] = 2.0 / (q + 1 - (j - i))
    return w


def trmdy_weights():
    """exact rationals / 1e6 from trmdy design.py."""
    num = {
        (0, 1): 239_252, (0, 2): 528_172, (0, 3): 965_879, (0, 4): 1_000_000,
        (0, 5): 1_000_000, (0, 6): 2_000_000,
        (1, 2): 381_335, (1, 3): 465_776, (1, 4): 34_121, (1, 5): 0,
        (1, 6): 1_000_000, (2, 3): 379_413, (2, 4): 12_104, (2, 5): 34_121,
        (2, 6): 1_000_000, (3, 4): 379_413, (3, 5): 465_776, (3, 6): 965_879,
        (4, 5): 381_335, (4, 6): 528_172, (5, 6): 239_252,
    }
    return {k: v / 1e6 for k, v in num.items()}


def tawan_redistributed_weights():
    """F_B from BELLMAN_COBBOUNDARY_PROOF.md: p=(946,1177,877,877,1177,946)/1920000,
    q=(31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5).
    The nearest coefficients q_i multiply w(g_i) with signs
    (+w1+w2-w4-w5) * 5971/300000 + linear part.  Reconstruct the pair form:
    U(g1..g5) = (54 g1 -123 g2 +123 g4 -54 g5)/1920000
                + 5971/300000 [w(g1)+w(g2)-w(g4)-w(g5)]
    F_B = F_0 + U(g2..g6) - U(g1..g5).
    We implement F_B directly with uniform F_0 (p0=1/3000).
    """
    return None  # handled specially


def tawan_FB(kernel):
    """F_B(g1..g6) for the cosine window kernel, uniform F0."""
    p0 = 1.0 / 3000.0

    def U(g):
        # g = (g1..g5)
        lin = (54 * g[0] - 123 * g[1] + 123 * g[3] - 54 * g[4]) / 1_920_000
        wq = 5971.0 / 300000.0
        wsum = wq * (kernel.w(g[0]) + kernel.w(g[1]) - kernel.w(g[3]) - kernel.w(g[4]))
        return lin + wsum

    def F(g):
        g = list(g)
        y = [0.0]
        for gi in g:
            y.append(y[-1] + gi)
        f0 = p0 * sum(g)
        w = uniform_weights(6)
        for i in range(7):
            for j in range(i + 1, 7):
                f0 += w[(i, j)] * kernel.w(y[j] - y[i])
        fb = f0 + U(g[1:]) - U(g[:5])
        return fb

    return F


def redistributed_F(kernel):
    """F_B via the p/q coefficient form: p_i g_i + q_i w(g_i) sums, plus the
    longer-span terms from F0.  Equivalent to tawan_FB."""
    p_coeff = [946, 1177, 877, 877, 1177, 946]
    p_coeff = [c / 1_920_000 for c in p_coeff]
    q_coeff = [31343 / 100_000, 1 / 3, 105971 / 300_000, 105971 / 300_000,
               1 / 3, 31343 / 100_000]

    def F(g):
        y = [0.0]
        for gi in g:
            y.append(y[-1] + gi)
        total = 0.0
        for i in range(6):
            total += p_coeff[i] * g[i]
            total += q_coeff[i] * kernel.w(g[i])
        w = uniform_weights(6)
        for i in range(7):
            for j in range(i + 1, 7):
                total += w[(i, j)] * kernel.w(y[j] - y[i])
        return total

    return F


# ---------------------------------------------------------------------------
# Floor estimation via grid + local refinement
# ---------------------------------------------------------------------------

def floor_estimate(F, q=6, grid=120, refine=600, seed=1):
    """Sample g in [0,4]^q (grid per coord), keep min, then Nelder-Mead-like
    local refine from the best few seeds.  Float, exploratory only."""
    rng = random.Random(seed)
    best_val = float("inf")
    best_pt = None
    # coarse grid
    pts = [i * 4.0 / grid for i in range(grid + 1)]
    # sample random points too
    for _ in range(3000):
        pt = tuple(rng.uniform(0, 5) for _ in range(q))
        v = F(pt)
        if v < best_val:
            best_val, best_pt = v, pt
    for p0 in pts:
        for _ in range(3):
            pt = tuple(rng.uniform(0, 4) for _ in range(q))
            v = F(pt)
            if v < best_val:
                best_val, best_pt = v, pt
    # local refine (coordinate descent, several passes)
    pt = list(best_pt)
    for _ in range(refine):
        improved = False
        for i in range(q):
            cur = pt[i]
            for scale in (0.5, 0.2, 0.05, 0.01):
                for delta in (-scale, scale):
                    cand = list(pt)
                    cand[i] = max(0.0, cand[i] + delta * max(1.0, cur))
                    v = F(tuple(cand))
                    if v < best_val - 1e-15:
                        best_val = v
                        pt = cand
                        improved = True
        if not improved:
            break
    return best_val, tuple(pt)


# ---------------------------------------------------------------------------
# Joint bound evaluation
# ---------------------------------------------------------------------------

def h_profile(E: float) -> float:
    return E if E <= 1 else 2 * math.sqrt(E) - 1


def phi_m(A: float, m: float) -> float:
    if A <= m / (m - 1):
        return A
    return 2 * math.sqrt((m - 1) * A / m) - 1 + A / m


def master_bound(H, eps, p, m, q, cap):
    A = eps * (m - q)
    R = h_profile(A) if cap == "h" else phi_m(A, m)
    eta = R / A
    Bp = q * p
    return (m * H - eta * Bp * (m - 1)) / (m - R)


def tawan_bound(H, eps_local, m, tax):
    A = eps_local * (m - 6)
    B = phi_m(A, m)
    return (H - tax) / (1 - B / m)


def tax_m(m):
    return (m - 6) / (320.0 * m)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("FLOAT-LEVEL EXPLORATION (labels: CONJECTURED until interval-certified)")
    print("=" * 78)

    # --- sanity: reproduce the certified numbers -----------------------------
    # ainta: MT kernel, uniform weights, p=1/3000: F >= 19/5000
    kmt = mt_kernel()
    F_ainta, _ = make_F(kmt, 1.0 / 3000.0, uniform_weights(6))
    v, pt = floor_estimate(F_ainta)
    print(f"[sanity] ainta uniform MT floor est: {v:.6f} (certified 0.0038)  argmin gaps {[round(x,3) for x in pt]}")

    # trmdy: trig-poly window, weighted design, p=1/2300
    c_tr = [1_000_000_000, 3_322_500, -7_609_135, 1_190_194, -731_476, -1_680_572, 1_141_360]
    oms_tr = [math.sqrt(2)] + [2 * math.pi * j for j in range(1, 7)]
    ktr = Kernel(c_tr, oms_tr)
    F_tr, _ = make_F(ktr, 1.0 / 2300.0, trmdy_weights())
    v, pt = floor_estimate(F_tr)
    print(f"[sanity] trmdy weighted floor est:   {v:.6f} (certified 0.005)  argmin {[round(x,3) for x in pt]}")

    # tawan: cosine 1.47, redistributed F_B
    ktw = cosine_kernel(1.47)
    F_tw = redistributed_F(ktw)
    v, pt = floor_estimate(F_tw)
    print(f"[sanity] tawan F_B floor est:         {v:.6f} (certified 0.00577)  argmin {[round(x,3) for x in pt]}")

    print()

    # --- (1) alpha scan for the cosine window: floor of F_B vs alpha ---------
    print("--- cosine window: redistributed F_B floor vs alpha (CONJECTURED) ---")
    best_alpha, best_floor, best_H = None, 0.0, None
    for alpha in [a / 100 for a in range(120, 171, 2)]:
        k = cosine_kernel(alpha)
        F = redistributed_F(k)
        v, _ = floor_estimate(F, refine=400)
        # H(alpha)
        i0 = 2 * math.sin(alpha / 2) / alpha
        i2 = 0.5 + math.sin(alpha) / (2 * alpha)
        const = math.sin(alpha / 2) / alpha + 2 * math.cos(alpha / 2) / (alpha * alpha)
        jv = -2 * i2 / (alpha * alpha) + const * i0
        c = i0 * i0 / (i2 + jv)
        H = 2 - 1 / c
        if v > best_floor:
            best_floor, best_alpha, best_H = v, alpha, H
    print(f"  best alpha={best_alpha}  floor~{best_floor:.6f}  H~{best_H:.8f}")

    print()
    print("--- cosine window: full joint bound over m at best-alpha (CONJ) ---")
    # at the best alpha, sweep m with the *float floor* (not certified):
    best_joint = None
    for m in [64, 96, 128, 160, 183, 200, 224, 256, 288, 320]:
        A = best_floor * (m - 6)
        B = phi_m(A, m)
        tax = tax_m(m)
        b = (best_H - tax) / (1 - B / m)
        if best_joint is None or b > best_joint[1]:
            best_joint = (m, b)
    print(f"  best joint (float floor, H float): m={best_joint[0]}  bound~{best_joint[1]:.8f}")

    print()
    print("--- alpha scan detail (top 8 by floor) ---")
    rows = []
    for alpha in [a / 100 for a in range(120, 171, 1)]:
        k = cosine_kernel(alpha)
        F = redistributed_F(k)
        v, _ = floor_estimate(F, refine=300)
        i0 = 2 * math.sin(alpha / 2) / alpha
        i2 = 0.5 + math.sin(alpha) / (2 * alpha)
        const = math.sin(alpha / 2) / alpha + 2 * math.cos(alpha / 2) / (alpha * alpha)
        jv = -2 * i2 / (alpha * alpha) + const * i0
        c = i0 * i0 / (i2 + jv)
        H = 2 - 1 / c
        # joint bound at m=183
        A = v * (183 - 6)
        B = phi_m(A, 183)
        b = (H - tax_m(183)) / (1 - B / 183)
        rows.append((v, alpha, H, b))
    rows.sort(reverse=True)
    for v, alpha, H, b in rows[:8]:
        print(f"  alpha={alpha:5.2f}  floor~{v:.6f}  H={H:.8f}  bound(m=183)~{b:.8f}")

    # --- (2) trig-poly windows: hold trmdy weights, scan scalar on the last
    # coefficients?  Keep it focused: recompute the trmdy floor with the
    # tawan redistributed design (does the coboundary help trig-poly?) -------
    print()
    print("--- trig-poly window (trmdy) with coboundary redistribution (CONJ) ---")
    # We approximate the coboundary benefit: the tawan design redistributes
    # pressure; apply the same p/q coefficients to the trmdy kernel.
    p_coeff = [946, 1177, 877, 877, 1177, 946]
    p_coeff = [c / 1_920_000 for c in p_coeff]
    q_coeff = [31343 / 100_000, 1 / 3, 105971 / 300_000, 105971 / 300_000,
               1 / 3, 31343 / 100_000]

    def F_tr_cob(g):
        y = [0.0]
        for gi in g:
            y.append(y[-1] + gi)
        total = 0.0
        for i in range(6):
            total += p_coeff[i] * g[i]
            total += q_coeff[i] * ktr.w(g[i])
        w = uniform_weights(6)
        for i in range(7):
            for j in range(i + 1, 7):
                total += w[(i, j)] * ktr.w(y[j] - y[i])
        return total

    v, pt = floor_estimate(F_tr_cob)
    print(f"  trmdy kernel + tawan p/q redistribution: floor~{v:.6f}  (vs 0.005 weighted, 0.00577 tawan cosine)")

    # --- (3) m-sweep with the *certified* floors for each family ------------
    print()
    print("--- joint bound with CERTIFIED ingredients only (all three families) ---")
    # ainta: H0, eps=19/5000, p=1/3000, m=269 (cap h).  Tawan: H_tw, eps_local
    # =577/1e5, m=183.  trmdy: H_tr, eps=1/200, p=1/2300, m=257.
    print(f"  ainta  : {master_bound(0.6725007036794116, 19/5000, 1/3000, 269, 6, 'h'):.15f}")
    print(f"  trmdy  : {master_bound(0.67245704141454, 1/200, 1/2300, 257, 6, 'h'):.15f}")
    print(f"  tawan  : {tawan_bound(0.6724587094007293, 577/1e5, 183, 59/19520):.15f}")
    print("  ceiling: 0.68183123059534187426")


if __name__ == "__main__":
    main()
