#!/usr/bin/env python3
"""Tail-subtracted direct verification of A3(lambda).

A3 = intint K(u)K(v)K(u+v) rho3 du dv, rho3 = 1 - Su^2 - Sv^2 - Sw^2 + 2 Su Sv Sw.
Slow parts (as R->inf): '1' term -> D = 1/la^2  (analytic), '2SSS' term -> 2C = 2(1-la/2) (analytic).
Fast part: -3 intint K(u)K(v)K(u+v) S(u)^2 du dv  = -3B,  B = (2/la) J2.
So: A3 = D + 2C + direct_fast,  where direct_fast integrates ONLY the fast part on [-R,R]^2.
Converges quickly. Compare with closed form. Also Monte Carlo for m3(1) via sine process.
"""
import numpy as np

def direct_fast(la, R=120.0, n=800):
    x, w = np.polynomial.legendre.leggauss(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu + vv
    Ku = np.sinc(la*uu); Kv = np.sinc(la*vv); Kw = np.sinc(la*ww)
    Su = np.sinc(uu)
    # only the -3 S(u)^2 term (symmetric; could equally use v or w)
    fast = -3.0*Ku*Kv*Kw*Su**2
    return float(np.sum(fast * np.outer(ws, ws)))

print(f"{'lam':>5} | {'D':>8} {'2C':>8} {'fast':>10} | {'A3=sum':>10} {'A3 closed':>10} | {'m3':>8}")
for s, D, C in (("0.5", 4.0, 0.75), ("0.6666666667", 2.25, 2/3), ("1.0", 1.0, 0.5)):
    la = float(s)
    A2 = 1/la - 2*(5/12 if s=="0.5" else (7/18 if s=="2/3" else 1/3))
    # recompute J2 via mpmath-free closed forms known: J2(1/2)=5/12, J2(2/3)=7/18, J2(1)=1/3
    f = direct_fast(la)
    A3 = D + 2*C + f
    m3 = 1 + 3*A2 + A3
    print(f"{s:>5} | {D:8.4f} {2*C:8.4f} {f:10.6f} | {A3:10.6f} {D-3*(2/la)*(5/12 if s=='0.5' else (7/18 if s=='2/3' else 1/3))+2*C:10.6f} | {m3:8.6f}")
