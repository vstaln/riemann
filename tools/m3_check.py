#!/usr/bin/env python3
"""m3(lambda) verification:
- closed-form reduction: m3 = 1 + 3*A2 - 3*(2*J3) + 2*C + 3/(4*lam)
  where A2 = 1/lam - 2*J2, J2 = int_0^inf sinc(pi la u)^2 sinc(pi u)^2 du,
  J3 = int_0^inf sinc(pi la u)^3 sinc(pi u)^2 du, C = int (Khat * Shat)^3 dxi = 1 - la/2.
- direct 2D integral of A3 for cross-check at a few lambda.
Uses mpmath high precision for the 1D integrals (fast, robust) and a Gauss-Legendre
2D quadrature (numpy) for the direct check.
"""
import mpmath as mp
from mpmath import sinc, mpf, quad, inf
import numpy as np

mp.mp.dps = 30

def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def J2(la):
    f = lambda u: K(u, la)**2 * S(u)**2
    return quad(f, [0, inf])

def J3(la):
    f = lambda u: K(u, la)**3 * S(u)**2
    return quad(f, [0, inf])

def A2(la): return 1/la - 2*J2(la)

def C_integral(la):
    # (Khat * Shat)(xi), Khat = (1/la)1_{|.|<=la/2}, Shat = 1_{|.|<=1/2}
    def conv(xi):
        lo = max(-la/2, xi-1/2); hi = min(la/2, xi+1/2)
        return max(0, hi-lo)/la
    f = lambda xi: conv(xi)**3
    return quad(f, [-(1+la)/2, (1+la)/2])

def m3_closed(la):
    return 1 + 3*A2(la) - 6*J3(la) + 2*C_integral(la) + mpf(3)/(4*la)

def m2_closed(la):
    return 1 + A2(la)

# ---- direct 2D check of A3 via Gauss-Legendre on [-R,R]^2 ----
def gl_nodes(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def direct_A3(la, R=60.0, n=400):
    # intint K(u)K(v)K(u+v) rho3(u,v) du dv, rho3 = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v)
    x, w = gl_nodes(n)
    # map to [-R, R]
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    Ku = np.sinc(la*uu); Kv = np.sinc(la*vv); Kw = np.sinc(la*ww)
    Su = np.sinc(uu); Sv = np.sinc(vv); Sw = np.sinc(ww)
    rho3 = 1 - Su**2 - Sv**2 - Sw**2 + 2*Su*Sv*Sw
    integ = Ku*Kv*Kw*rho3
    return np.sum(integ*np.outer(ws,ws))

if __name__ == "__main__":
    print("closed-form reduction (mpmath):")
    print(f"{'lam':>6} {'m2':>12} {'m3':>12} {'2m2-m3':>12} {'C(lam)':>10} {'A3dir':>14}")
    for la_s in ("0.40","0.50","0.60","0.65","0.66","0.67","0.70","0.80","0.90","1.00"):
        la = mpf(la_s)
        m2 = m2_closed(la); m3 = m3_closed(la)
        cint = C_integral(la)
        # direct A3, then m3_direct = 1 + 3*A2 + A3_direct
        A3d = direct_A3(float(la))
        m3d = 1 + 3*float(A2(la)) + A3d
        print(f"{float(la):6.2f} {float(m2):12.6f} {float(m3):12.6f} {float(2*m2-m3):12.6f} {float(cint):10.6f} {m3d:14.6f}")
