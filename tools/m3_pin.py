#!/usr/bin/env python3
"""Pin down m3(1) rigorously.

m3 = 1 + 3*A2 + A3,  A2 = int K^2 (1-S^2),  A3 = intint K(u)K(v)K(u+v) rho3(u,v) du dv
rho3 = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v),  S=sinc(pi x), K=sinc(pi la x)

Closed forms (verified in m3_check.py): D := intint K(u)K(v)K(u+v) dudv = 3/(4 la)
C := intint K(u)K(v)K(u+v) S(u)S(v)S(u+v) dudv = 1 - la/2
B := int K(u)^3 S(u)^2 du  (R-line, even)  -> A3 = D - 3B + 2C,  B = 2*J3, J3 = int_0^inf

Here: verify J2(1)=1/3, J3(1)=115/384, int sinc^3 = 3/4 to high precision (mpmath),
then A3(1), m3(1). Also verify the SLOW tail issue: direct 2D on [-R,R]^2 at R=60,200,600
converging to the closed-form value.
"""
import mpmath as mp
from mpmath import mpf, quad, inf
import numpy as np
mp.mp.dps = 40

def S(u): return mp.sinc(mp.pi*u)

J2_1 = quad(lambda u: S(u)**4, [0, inf])
J3_1 = quad(lambda u: S(u)**5, [0, inf])
I3 = quad(lambda u: S(u)**3, [0, inf])   # half-line
print("J2(1)=int0^inf sinc^4  =", mp.nstr(J2_1, 25), "  (expected 1/3 =", mpf(1)/3, ")")
print("J3(1)=int0^inf sinc^5  =", mp.nstr(J3_1, 25), "  (expected 115/384 =", mpf(115)/384, ")")
print("I3   =int0^inf sinc^3  =", mp.nstr(I3, 25), "  (expected 3/8 =", mpf(3)/8, ")")

la = mpf(1)
A2 = 1/la - 2*J2_1
A3_closed = mpf(3)/(4*la) - 3*(2*J3_1) + 2*(1 - la/2)
m3_closed = 1 + 3*A2 + A3_closed
print("\nA2(1) =", mp.nstr(A2, 25), " A3(1) closed =", mp.nstr(A3_closed, 25), " m3(1) =", mp.nstr(m3_closed, 25))
print("m3(1) as rational vs 125/64 =", mpf(125)/64, "  vs paper 2")

# direct 2D integral, tail convergence check (numpy, f64)
def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def direct_A3(R, n=800):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    Ku = np.sinc(la*uu); Kv = np.sinc(la*vv); Kw = np.sinc(la*ww)
    Su = np.sinc(uu); Sv = np.sinc(vv); Sw = np.sinc(ww)
    rho3 = 1 - Su**2 - Sv**2 - Sw**2 + 2*Su*Sv*Sw
    return float(np.sum(Ku*Kv*Kw*rho3 * np.outer(ws, ws)))

print("\nDirect 2D A3 on [-R,R]^2 (slow '1' and 2C terms have O(logR/R) tails):")
for R in (30, 60, 120, 240, 480):
    print(f"  R={R:5d}: A3_direct = {direct_A3(R):.6f}   (closed form: {float(A3_closed):.6f})")

# Same, but subtract the analytic slow parts first: integrate only the FAST part directly,
# add D and 2C analytically.
def direct_A3_fastpart(R, n=800):
    # fast part integrand: -3 K(u)K(v)K(u+v) S(u)^2  (use symmetric u term; all three equal)
    # plus 2 K(u)K(v)K(u+v) S(u)S(v)S(u+v) - but this decays only 1/(u^2 v^2) ~ slow-ish.
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    ww = uu+vv
    Ku = np.sinc(uu); Kv = np.sinc(vv); Kw = np.sinc(ww)
    Su = np.sinc(uu); Sv = np.sinc(vv); Sw = np.sinc(ww)
    fast = -3*Ku*Kv*Kw*Su**2 + 2*Ku*Kv*Kw*Su*Sv*Sw
    return float(np.sum(fast * np.outer(ws, ws)))

print("\nA3 = D(3/4 analytic) -3B + 2C(1/2 analytic); check -3B+2C via fast-part direct:")
for R in (30, 60, 120, 240, 480):
    val = 0.75 + direct_A3_fastpart(R)
    print(f"  R={R:5d}: A3 = {val:.6f}   (closed: {float(A3_closed):.6f})")
