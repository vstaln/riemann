#!/usr/bin/env python3
"""
tools/m4proper_probe.py — M4-proper: pin the zeta second-derivative moment ratio r'
from real critical-line zero data (Bui-Heath-Brown box-target input).

Question (from research/notes/bui-heathbrown-decomposition-2026-08-18.md):
  Box condition: E/S2 <= 8 b^2 (r + r') with r = 99/1274 = 0.077707... (PROVEN, Montgomery-type
  first-derivative moment ratio) and r' = the zeta''-moment ratio — REFUTED-as-derived = 3/5
  (the Gonek anchor, arXiv:1302.5032, is conditional), unknown O(1)-scale. M4-proper = pin r'
  numerically from real zeros.

Object computed here:
  S1(T) = sum_{0<gamma<=T} |zeta'(rho)|^2      (rho = 1/2 + i gamma, real zeros)
  S2(T) = sum_{0<gamma<=T} |zeta''(rho)|^2
  normalizations: with L = log(T/(2 pi)),
    a1(T) = S1(T) / ((T/(2 pi)) * L^4 / G1_const)   -> 1 if the Gonek/Milinovich-Ng first-moment
           law holds with constant G1_const (classical: sum |zeta'(rho)|^2 ~ (T/2pi) L^4 / 12)
    r'(T) = (S2/S1) / L^2      -> the second-derivative moment ratio in the BHB normalization
           (r' = 3/5 would require S2/S1 ~ (3/5) L^2)

Everything is computed with mpmath at dps=40 (certified well beyond the question).
Zeros: Z(t) sign changes on a coarse grid, refined by mp.findroot on Siegel Z at high precision.
This is a CHECKED NUMERICALLY probe of a ratio — it pins r' at finite height; it does not prove
the limit exists.
"""

import mpmath as mp

mp.mp.dps = 40
PI = mp.mp.pi
TWO_PI = 2 * mp.mp.pi


def find_zeros_upto(Tmax, step=0.4, refine=True):
    """Return refined zero ordinates gamma in (0, Tmax] via Siegel Z sign changes."""
    # coarse sweep at modest precision
    mp.mp.dps = 15
    t0 = mp.mpf("14.0")
    z0 = mp.siegelz(t0)
    zeros = []
    t = t0
    while t < Tmax:
        tn = t + step
        zn = mp.siegelz(tn)
        if z0 == 0 or (z0 * zn < 0):
            # bracket [t, tn] contains a zero — let findroot polish it
            zeros.append(mp.mpf(t))
        z0, t = zn, tn
    mp.mp.dps = 40
    # dedup (defensive) and refined roots via mp.findroot on the bracketed interval
    out = []
    for g in zeros:
        if 0 < g <= Tmax and (not out or g - out[-1] > mp.mpf("1e-6")):
            lo, hi = mp.mpf(g), mp.mpf(g) + mp.mpf(step)
            try:
                r = mp.findroot(mp.siegelz, (lo, hi), solver="bisect",
                                tol=mp.mpf("1e-30"), maxsteps=120)
                out.append(mp.mpf(r))
            except Exception:
                try:
                    r = mp.findroot(mp.siegelz, lo, tol=mp.mpf("1e-25"), maxsteps=40)
                    out.append(mp.mpf(r))
                except Exception:
                    out.append((lo + hi) / 2)
    return out


def main():
    # Tmax chosen so this runs in seconds; ratio should be computed at several heights
    for Tmax in (150, 300, 600, 1200):
        zeros = find_zeros_upto(mp.mpf(Tmax))
        S1 = mp.mpf(0)
        S2 = mp.mpf(0)
        for g in zeros:
            rho = mp.mpc(mp.mpf("0.5"), g)
            # mpmath: zeta(s, a) is the Hurwitz zeta — NOT derivatives.
            # True derivatives via adaptive numerical differentiation:
            z1 = mp.diff(mp.zeta, rho, 1)   # zeta'(rho)
            z2 = mp.diff(mp.zeta, rho, 2)   # zeta''(rho)
            S1 += abs(z1) ** 2
            S2 += abs(z2) ** 2
        N = len(zeros)
        if N == 0:
            continue
        L = mp.log(Tmax / TWO_PI)
        # classical first-moment law (Gonek/Milinovich-Ng conjecture shape): S1 ~ (T/2pi) L^4 / 12
        law1 = (Tmax / TWO_PI) * L ** 4 / 12
        ratio = (S2 / S1) / (L * L)   # r' candidate
        print(f"Tmax={Tmax:>5}  N={N:>4}  S1={mp.nstr(S1,10)}  S2={mp.nstr(S2,10)}")
        print(f"          S1/law1 = {mp.nstr(S1 / law1, 10)}   r' = (S2/S1)/L^2 = {mp.nstr(ratio, 10)}")
        print(f"          r' expected 3/5 = 0.6; |ratio-0.6| = {mp.nstr(abs(ratio - mp.mpf('0.6')), 10)}")


if __name__ == "__main__":
    main()