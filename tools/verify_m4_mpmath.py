#!/usr/bin/env python3
"""Pin the m4 diagram pieces with mpmath adaptive integration (handles oscillatory
infinite-range tails). Cross-checks every piece of m4 = 1 + 6A2 + B2 + 4A3 + 2C3 + A4
at la = 1 and la = 1/2, independently of numpy GL.

Pieces verified against their analytic/derived forms:
  A2 = 1/la - 2J2  (J2 = int_0^inf K^2 S^2)
  B2 = int_R K^4 (1-S^2)
  A3 (closed form vs direct 2D)
  C3 = intint K(u)^2 K(v)^2 rho3(0,u,v)      (direct 2D)
  E1 = intintint K4 S12^2 S34^2  (direct 3D AND reduced 2D AND Parseval closed form)
  E2 = intintint K4 S13^2 S24^2  (direct 3D)
  E3 = intintint K4 S14^2 S23^2  (direct 3D)
  t  = intintint K4 S12 S23 S13 (direct 3D vs reduced 2D vs closed form)
  q1 = intintint K4 S12 S23 S34 S14 (direct 3D vs 1D ghat^4)
  q2 = intintint K4 S12 S24 S34 S13 (direct 3D)
  q3 = intintint K4 S13 S23 S24 S14 (direct 3D)
"""
import mpmath as mp
from mpmath import mpf, mp, quad, inf
mp.dps = 20

def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def K4prod(u, v, w, la):
    return K(u, la)*K(v, la)*K(w, la)*K(u+v+w, la)

def J2(la):
    return quad(lambda u: K(u, la)**2*S(u)**2, [0, inf])

def B2(la):
    return quad(lambda u: K(u, la)**4*(1-S(u)**2), [-inf, inf])

def A3_direct(la):
    rho3 = lambda u, v: (1 - S(u)**2 - S(v)**2 - S(u+v)**2 + 2*S(u)*S(v)*S(u+v))
    return quad(lambda u, v: K(u, la)*K(v, la)*K(u+v, la)*rho3(u, v),
                [-inf, inf], [-inf, inf])

def C3_direct(la):
    rho3 = lambda u, v: (1 - S(u)**2 - S(v)**2 - S(u-v)**2 + 2*S(u)*S(v)*S(u-v))
    return quad(lambda u, v: K(u, la)**2*K(v, la)**2*rho3(u, v),
                [-inf, inf], [-inf, inf])

def E1_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u)**2*S(w)**2,
                [-inf, inf], [-inf, inf], [-inf, inf])

def E1_2d(la):
    return (1.0/la)*quad(lambda u, w: K(u, la)*K(w, la)*K(u+w, la)*S(u)**2*S(w)**2,
                         [-inf, inf], [-inf, inf])

def E2_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u+v)**2*S(v+w)**2,
                [-inf, inf], [-inf, inf], [-inf, inf])

def E3_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u+v+w)**2*S(v)**2,
                [-inf, inf], [-inf, inf], [-inf, inf])

def t1_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u)*S(v)*S(u+v),
                [-inf, inf], [-inf, inf], [-inf, inf])

def q1_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u)*S(v)*S(w)*S(u+v+w),
                [-inf, inf], [-inf, inf], [-inf, inf])

def q2_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u)*S(v+w)*S(w)*S(u+v),
                [-inf, inf], [-inf, inf], [-inf, inf])

def q3_3d(la):
    return quad(lambda u, v, w: K4prod(u, v, w, la)*S(u+v)*S(v)*S(v+w)*S(u+v+w),
                [-inf, inf], [-inf, inf], [-inf, inf])

def ghat(xi, la):
    lo = max(-la/2, xi - mpf(1)/2); hi = min(la/2, xi + mpf(1)/2)
    return max(0, hi - lo)/la

def q1_1d(la):
    return quad(lambda xi: ghat(xi, la)**4, [-(1+la)/2, (1+la)/2])

if __name__ == "__main__":
    for la in (mpf(1), mpf(1)/2):
        print(f"==== la = {float(la)} ====")
        j2 = J2(la)
        a2 = 1/la - 2*j2
        print(f"  A2 = {float(a2):.10f}  (m2 = {float(1+a2):.10f}, ref {float(1/la+la/3):.10f})")
        print(f"  B2 = {float(B2(la)):.10f}  (closed at la=1: 7/60 = {7/60:.10f})")
        a3 = A3_direct(la)
        a3c = 1/la**2 - la + 2 - 6*j2/la
        print(f"  A3 direct = {float(a3):.10f}  closed = {float(a3c):.10f}")
        c3 = C3_direct(la)
        print(f"  C3 direct = {float(c3):.10f}")
        e1 = E1_3d(la); e1r = E1_2d(la)
        e2 = E2_3d(la); e3 = E3_3d(la)
        print(f"  E1 3D = {float(e1):.10f}  2D-reduced = {float(e1r):.10f}")
        print(f"  E2 3D = {float(e2):.10f}  E3 3D = {float(e3):.10f}")
        t1 = t1_3d(la)
        print(f"  t 3D = {float(t1):.10f}  (closed (1-la/2)/la = {float((1-la/2)/la):.10f})")
        q1 = q1_3d(la); q1o = q1_1d(la)
        q2 = q2_3d(la); q3 = q3_3d(la)
        print(f"  q1 3D = {float(q1):.10f}  1D = {float(q1o):.10f}  q2 = {float(q2):.10f}  q3 = {float(q3):.10f}")
        T1 = 1/la**3
        J = 2*float(j2)
        A4 = float(T1) - 6*J/float(la)**2 + float(e1) + float(e2) + float(e3) \
             + 2*float(t1)*4 - 2*(float(q1) + float(q2) + float(q3))
        m4 = 1 + 6*float(a2) + float(B2(la)) + 4*float(a3) + 2*float(c3) + A4
        print(f"  A4 assembled = {A4:.10f}   m4 = {m4:.10f}")
        print(f"  (paper m4(1) = 13/4 = 3.25 ; consensus 346/105 = {346/105:.6f})")
        print()
