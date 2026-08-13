#!/usr/bin/env python3
"""Closed-form r''(t) and Taylor of r(t) (Suzuki (2.2) / §2.2).

PROVEN at source: r = r0 + r1 with
  r0(t) = −4(e^{t/2}+e^{−t/2}−2),
  r1(t) = (1/4) Σ_{n≥2} ζ(2−n,1/4) (−2|t|)^n / n!,
and r1''(t) = e^{t/2}/(2 sinh t) − 1/(2t) for t>0
(Suzuki p.11, after the Bernoulli generating function).

Chain rule: r0''(t) = −2 cosh(t/2). Hence for t>0
  r''(t) = −2 cosh(t/2) + e^{t/2}/(2 sinh t) − 1/(2t),
  r''(0+) = −7/4.

Taylor for t>0 (Hurwitz + polar, even/odd in |t|):
  r(t) = −(7/8) t² − (5/288) t³ − (3/128) t⁴ + O(t^5).

Belief: the fake t⁴ mismatch in remainder_bound.py is the t³ term
(n=3 Hurwitz). ρ''(t) := r''(t)+7/4 ≤ −c t² on (0, 2 a3] would give a
sign-definite remainder for w≥0 in (4.5).

Usage: python3 tools/weil_first_prime/rpp_closed.py
"""
from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from screw_kernel import hurwitz_neg_int, A_SUZUKI  # noqa: E402
from remainder_bound import r_of_t, r_dd, g_arch  # noqa: E402
from lower_bound import A3  # noqa: E402

A = A_SUZUKI


def rpp_closed(t: float) -> float:
    """r''(t) for t>0. Limit t→0+ is −7/4."""
    t = abs(float(t))
    if t < 1e-12:
        return -1.75
    return -2.0 * math.cosh(t / 2.0) + math.exp(t / 2.0) / (2.0 * math.sinh(t)) - 1.0 / (
        2.0 * t
    )


def taylor_coeffs() -> dict:
    """Exact rational coefficients of r(t) for t>0 from polar + Hurwitz n=2,3,4."""
    # polar r0 = −8(cosh(t/2)−1) = −t² − t⁴/48 − t⁶/5760 − ⋯
    # n=2: (1/4) ζ(0,1/4) (−2t)² / 2! = t²/8
    # n=3: (1/4) ζ(−1,1/4) (−2t)³ / 3!
    # n=4: (1/4) ζ(−2,1/4) (−2t)⁴ / 4!
    z0 = hurwitz_neg_int(0, 0.25)  # ζ(0,1/4)=1/4
    z1 = hurwitz_neg_int(1, 0.25)  # ζ(−1,1/4)
    z2 = hurwitz_neg_int(2, 0.25)  # ζ(−2,1/4)
    c2_hur = 0.25 * z0 * ((-2.0) ** 2) / math.factorial(2)
    c3_hur = 0.25 * z1 * ((-2.0) ** 3) / math.factorial(3)
    c4_hur = 0.25 * z2 * ((-2.0) ** 4) / math.factorial(4)
    c2 = -1.0 + c2_hur  # polar −1
    c4 = -1.0 / 48.0 + c4_hur
    return {
        "zeta0": z0,
        "zeta_m1": z1,
        "zeta_m2": z2,
        "c2": c2,
        "c3": c3_hur,
        "c4": c4,
        "c3_frac": -5.0 / 288.0,
        "c4_frac": -3.0 / 128.0,
        "c2_frac": -7.0 / 8.0,
    }


def main() -> None:
    print("=== Hurwitz at 1/4 ===")
    tc = taylor_coeffs()
    print(f"  ζ(0,1/4)  = {tc['zeta0']:.16f}  want 1/4={0.25}")
    print(f"  ζ(−1,1/4) = {tc['zeta_m1']:.16f}  want 5/96={5/96:.16f}")
    print(f"  ζ(−2,1/4) = {tc['zeta_m2']:.16f}  want −1/64={-1/64:.16f}")
    print("=== Taylor coefficients (t>0) ===")
    print(f"  c2 = {tc['c2']:.16f}  −7/8 = {tc['c2_frac']:.16f}")
    print(f"  c3 = {tc['c3']:.16f}  −5/288 = {tc['c3_frac']:.16f}")
    print(f"  c4 = {tc['c4']:.16f}  −3/128 = {tc['c4_frac']:.16f}")

    print("\n=== r''(closed) vs stencil ===")
    print(f"{'t':>10} {'closed':>14} {'stencil':>14} {'diff':>12}")
    for t in (1e-4, 1e-3, 0.01, 0.10, 0.34657, math.log(2.0), 0.8, 2.0 * A3):
        cl = rpp_closed(t)
        st = r_dd(t, h=1e-5)
        print(f"{t:10.5f} {cl:14.8f} {st:14.8f} {cl-st:12.2e}")
    print(f"  r''(0+) closed={rpp_closed(0.0):.8f}  want −7/4")

    print("\n=== t³ is why (r+7/8 t²)/t⁴ blew up ===")
    print(f"{'t':>10} {'(r+7/8 t²)/t^4':>16} {'(+c3 t³)/t^4':>16} {'(+c4 too)':>16}")
    c3 = tc["c3"]
    for t in (1e-3, 2e-3, 5e-3, 1e-2, 0.05, 0.10):
        rt = r_of_t(t)
        raw = (rt + 0.875 * t * t) / (t**4)
        with3 = (rt + 0.875 * t * t - c3 * t**3) / (t**4)
        with4 = (rt + 0.875 * t * t - c3 * t**3 - tc["c4"] * t**4) / (t**4)
        print(f"{t:10.4f} {raw:16.6f} {with3:16.6f} {with4:16.6e}")
    print(f"  −3/128 = {-3/128:.8f}")

    print("\n=== ρ''(t)=r''(t)+7/4  and  −ρ''/t²  on (0, 2 a3] ===")
    S = 2.0 * A3
    n = 2000
    ts = [S * k / n for k in range(1, n + 1)]
    cmin = 1e99
    tmin = 0.0
    rhomax = -1e99
    rhomin = 1e99
    for t in ts:
        rho = rpp_closed(t) + 1.75
        rhomax = max(rhomax, rho)
        rhomin = min(rhomin, rho)
        c = -rho / (t * t)
        if c < cmin:
            cmin = c
            tmin = t
    print(f"  S=2 a3={S:.6f}")
    print(f"  min ρ''={rhomin:.8f}  max ρ''={rhomax:.8f}  (max≤0 ⇒ ρ''≤0 on the window)")
    print(f"  min (−ρ''/t²)={cmin:.8f} at t={tmin:.6f}")
    print(f"  Taylor 9/32={9/32:.8f}  (= −ρ''(0+)/t² limit)")
    print("  samples:")
    for t in (0.05, 0.10, 0.34657, math.log(2.0), 0.8, S):
        rho = rpp_closed(t) + 1.75
        print(f"    t={t:.5f}  ρ''={rho:+.8f}  −ρ''/t²={-rho/(t*t):.8f}")

    # first positive zero of ρ'' if any, up to t=4
    t = 1e-3
    prev = rpp_closed(t) + 1.75
    zero = None
    while t < 4.0:
        t += 0.002
        cur = rpp_closed(t) + 1.75
        if prev <= 0 <= cur or prev >= 0 >= cur:
            if abs(cur) + abs(prev) > 0 and prev * cur <= 0 and t > 0.01:
                zero = t
                break
        prev = cur
    print(f"  first sign-change of ρ'' on (0.01,4]: {zero}")

    print("\n=== VERDICT ===")
    ok_c2 = abs(tc["c2"] - tc["c2_frac"]) < 1e-12
    ok_c3 = abs(tc["c3"] - tc["c3_frac"]) < 1e-12
    ok_c4 = abs(tc["c4"] - tc["c4_frac"]) < 1e-12
    ok_rpp = abs(rpp_closed(0.0) + 1.75) < 1e-12
    print(f"  c2,c3,c4 exact: {ok_c2}, {ok_c3}, {ok_c4}")
    print(f"  r''(0+)=−7/4: {ok_rpp}")
    print(f"  ρ''≤0 on (0,2a3]: {rhomax <= 1e-9}")
    print(f"  min(−ρ''/t²)={cmin:.6f} vs 9/32={9/32:.6f}")


if __name__ == "__main__":
    main()
