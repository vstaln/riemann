#!/usr/bin/env python3
"""ADJUDICATION part 1: corrected m3(lam) = 3 + 3/lam + 1/lam^2 - lam - 6*J2*(1+1/lam),
J2 = int_0^inf sinc(pi la u)^2 sinc(pi u)^2 du.
Verified against (a) mpmath high precision, (b) direct 2D integral of A3 on [-R,R]^2
at large R (the quantity my earlier 'closed form' contradicted), (c) the sine-process
Monte Carlo (sine_sim.py), (d) zeta-zero empirics (empirical_m3.py).
"""
import mpmath as mp
from mpmath import mpf, quad, inf
import numpy as np
mp.mp.dps = 30

def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def J2(la):
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def m3_closed(la):
    J = J2(la)
    return 3 + 3/la + 1/la**2 - la - 6*J*(1 + 1/la)

def m2_closed(la):
    return 1 + 1/la - 2*J2(la)

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def direct_A3(la, R, n=700):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    Ku = np.sinc(la*uu); Kv = np.sinc(la*vv); Kw = np.sinc(la*ww)
    Su = np.sinc(uu); Sv = np.sinc(vv); Sw = np.sinc(ww)
    rho3 = 1 - Su**2 - Sv**2 - Sw**2 + 2*Su*Sv*Sw
    return float(np.sum(Ku*Kv*Kw*rho3 * np.outer(ws, ws)))

print("corrected m3(lam):  lam   m2(mp)   m3(mp)  2m2-m3   m3 via A3direct(R=100)")
for la_s in ("0.50","0.60","0.66","0.70","0.80","0.90","1.00"):
    la = mpf(la_s)
    m2 = m2_closed(la); m3 = m3_closed(la)
    A3d = direct_A3(float(la), 100)
    m3d = 1 + 3*(float(m2)-1) + A3d
    print(f"{float(la):5.2f}  {float(m2):7.5f}  {float(m3):7.5f}  {float(2*m2-m3):7.5f}  {m3d:.5f}")

print("\nkey checks:")
for la_s, target in (("1.00", 2.0), ("2/3", 13/4), ("0.50", 5.0)):
    la = mpf(la_s)
    print(f"  m3({la_s}) = {float(m3_closed(la)):.6f}   target {target}")
