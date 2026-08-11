#!/usr/bin/env python3
"""Verify m3(lambda) by TWO independent routes:
(a) direct 2D quadrature of A3 = intint K(u)K(v)K(u+v) rho3(u,v) du dv (numpy GL on [-R,R]^2)
(b) corrected closed form:  A3 = D - 3B + 2C
        D = 1/la^2            (intint K(u)K(v)K(u+v) du dv = int Khat(xi)^2 Khat(-xi) dxi)
        B = (2/la)*J2(la),    J2 = int_0^inf sinc(pi la u)^2 sinc(pi u)^2 du
                              (since int K(v)K(u+v) dv = (K*K)(u) = (1/la) K(u))
        C = 1 - la/2          (int (Khat*Shat)^3 dxi, la <= 1)
  m3 = 1 + 3*A2 + A3,  A2 = 1/la - 2*J2.
Expected (paper): m3(1) = 2, m2(1) = 4/3, m2(1/2) = 13/6.
"""
import mpmath as mp
from mpmath import sinc, mpf, quad, inf
import numpy as np

mp.mp.dps = 30
def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def J2_mp(la):
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def closed(la):
    J2 = J2_mp(la)
    A2 = 1/la - 2*J2
    D = 1/la**2
    B = (2/la)*J2
    C = 1 - la/2
    A3 = D - 3*B + 2*C
    return float(A2), float(D), float(B), float(C), float(A3), float(1 + 3*A2 + A3), float(J2)

def direct_A3(la, R=200.0, n=700):
    x, w = np.polynomial.legendre.leggauss(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu + vv
    Ku = np.sinc(la*uu); Kv = np.sinc(la*vv); Kw = np.sinc(la*ww)
    Su = np.sinc(uu); Sv = np.sinc(vv); Sw = np.sinc(ww)
    rho3 = 1 - Su**2 - Sv**2 - Sw**2 + 2*Su*Sv*Sw
    integ = Ku*Kv*Kw*rho3
    return float(np.sum(integ * np.outer(ws, ws)))

print(f"{'lam':>5} | {'A2':>12} {'D':>10} {'B':>12} {'C':>10} | {'A3 closed':>12} {'A3 direct':>12} | {'m3 closed':>10} {'m3 direct':>10}")
for s in ("0.5", "2/3", "1.0"):
    la = mpf(s)
    A2, D, B, C, A3c, m3c, J2 = closed(la)
    A3d = direct_A3(float(la))
    m3d = 1 + 3*A2 + A3d
    m2 = 1 + A2
    print(f"{s:>5} | {A2:12.7f} {D:10.5f} {B:12.7f} {C:10.5f} | {A3c:12.7f} {A3d:12.7f} | {m3c:10.7f} {m3d:10.7f}   (m2={m2:.7f}, J2={J2:.7f})")

print("\nChecks: paper m2(1)=4/3, m3(1)=2;  m2(1/2)=13/6;  m3(1/2)=? ;  m2(2/3)=31/18")
