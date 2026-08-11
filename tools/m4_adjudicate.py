#!/usr/bin/env python3
"""ADJUDICATION part 2: m4(lam) with the corrected convolution identities.
m4 = 1 + 6*A2 + D4 + A4
A2 = 1/lam - 2*J2,  D4 = (2/3)/lam
A4 = 1/lam^3 - 12*J2/lam^2 + 3*E - 6*G + (8/lam)*(1-lam/2)
E(lam) = (1/lam) intint S(u)^2 K(u) S(w)^2 K(w) K(u+w) du dw        (2D, numpy GL)
G(lam) = int (Khat*Shat)^4 dxi  (1D)
Check: m4(1) = 13/4 per the paper.
"""
import mpmath as mp
from mpmath import mpf, quad, inf
import numpy as np
mp.mp.dps = 30

def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def J2(la):
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def G4(la):
    def conv(xi):
        lo = max(-la/2, xi-1/2); hi = min(la/2, xi+1/2)
        return max(0, hi-lo)/la
    return quad(lambda xi: conv(xi)**4, [-(1+la)/2, (1+la)/2])

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def E2(la, R, n=700):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, ww = np.meshgrid(xs, xs, indexing='ij')
    v = (np.sinc(uu)**2 * np.sinc(la*uu) * np.sinc(ww)**2 * np.sinc(la*ww) * np.sinc(la*(uu+ww)))
    return (1.0/la) * float(np.sum(v * np.outer(ws, ws)))

def m4_closed(la, R):
    J = float(J2(la)); E = E2(la, R); G = float(G4(la))
    A4 = 1/la**3 - 12*J/la**2 + 3*E - 6*G + (8/la)*(1 - la/2)
    m2 = 1 + 1/la - 2*J
    return 1 + 6*(m2-1) + (2/3)/la + A4, E, G, J

for la in (1.0, 0.8, 2/3):
    for R in (40, 80, 160):
        m4, E, G, J = m4_closed(la, R)
        print(f"la={la:.3f} R={R:4d}: m4 = {m4:.6f}  (E={E:.6f} G={G:.6f} J2={J:.6f})")
    print("   paper target:", "13/4 = 3.25" if abs(la-1) < 1e-9 else "—")
