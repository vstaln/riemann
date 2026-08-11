#!/usr/bin/env python3
"""m4 reduction pieces at lambda=1 (mpmath, high precision), saved for reproducibility.
E(1) = int tri2(xi)^3 dxi,  tri2 = 3-fold box convolution on [-1/2,1/2] (Irwin-Hall n=3,
  centered): tri2(x) = 3/4 - x^2 on |x|<=1/2; (3/2-|x|)^2/2 on 1/2<=|x|<=3/2.
G(1) = int tri1(xi)^4 dxi,   tri1 = (1-|x|)+.
These are the two non-trivial diagram pieces of m4(1) = 1 + 6*A2 + D4 + A4 with
A4 = 1 - 6*J2 + 3*E + 8*F - 6*G,  A2 = 1/3, D4 = 2/3, J2 = 1/3, F = 1/2 at lambda=1.
=> m4(1) = 346/105. (The paper states 13/4; derivation not in repo - see attack-thirdmoment.md 4.3.)
"""
import mpmath as mp
from mpmath import mpf, quad
mp.mp.dps = 30

def tri2(x):
    ax = abs(x)
    if ax <= 0.5:
        return mpf(3)/4 - x*x
    if ax <= 1.5:
        return ((mpf(3)/2 - ax)**2)/2
    return mpf(0)

def tri1(x):
    return max(0, 1 - abs(x))

E = quad(lambda x: tri2(x)**3, [-mpf(3)/2, mpf(3)/2])
G = quad(lambda x: tri1(x)**4, [-1, 1])
J2 = quad(lambda u: mp.sinc(mp.pi*u)**4, [0, mp.inf])

A4 = 1 - 12*J2 + 3*E + 8*(mpf(1)/2) - 6*G
m4 = 1 + 6*(mpf(1)/3) + mpf(2)/3 + A4
print("E(1)  =", mp.nstr(E, 20), " (12/35 =", mp.nstr(mpf(12)/35, 20), ")")
print("G(1)  =", mp.nstr(G, 20), " (2/5   =", mp.nstr(mpf(2)/5, 20), ")")
print("J2(1) =", mp.nstr(J2, 20), " (1/3   =", mp.nstr(mpf(1)/3, 20), ")")
print("A4(1) =", mp.nstr(A4, 20))
print("m4(1) =", mp.nstr(m4, 20), " (346/105 =", mp.nstr(mpf(346)/105, 20), "; paper 13/4 =", mp.nstr(mpf(13)/4, 20), ")")
