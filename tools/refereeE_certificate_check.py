#!/usr/bin/env python3
"""Referee 6E — exact-rational + mpmath verification of the certificate identity.

Checks:
  1. sum_{j=1}^{256} j/256^2 = 257/512 ; D(1) = 1/512 ; E(1) = -1/(6*256^2)
  2. chain value v = (H(1.464)-tau)/(1-B/171), tau=11/3648, B=1.02292821035354
  3. beta*v = v-(H-tau) ; knot-sum requirement for reading A (c0=H-tau)
  4. r=1-x: sum (j/256^2)(1-j/256) = 1/6 - 1/(6*256^2) (stability identity, E(1))
  5. ceiling value p0 + 1/(6*256^2) = 0.6818312305953...
  6. j=256 term consistency: (1/256)*r(1) on both sides; = 0 if r(1)=0
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 60

# --- exact rationals ---
S = sum(Fraction(j, 256 ** 2) for j in range(1, 257))
D1 = S - Fraction(1, 2)
E1 = sum(Fraction(j, 256 ** 2) * (1 - Fraction(j, 256)) for j in range(1, 257)) - Fraction(1, 6)
print("sum j/256^2           =", S, "= 257/512?", S == Fraction(257, 512))
print("D(1)                  =", D1, "= 1/512?", D1 == Fraction(1, 512))
print("E(1)                  =", E1, "= -1/393216?", E1 == -Fraction(1, 393216))

# r = 1-x discrete vs continuum
S_r = sum(Fraction(j, 256 ** 2) * (1 - Fraction(j, 256)) for j in range(1, 257))
print("sum (j/256^2)(1-j/256)= %s = 1/6 - 1/393216?" % S_r, S_r == Fraction(1, 6) - Fraction(1, 393216))
print("  = 1/6 + E(1)?       ", S_r == Fraction(1, 6) + E1, "  float:", float(S_r), "vs 1/6=", 1/6)

# --- chain value ---
alpha = mp.mpf("1.464")
m = 171
tau = mp.mpf(Fraction(11, 3648))
B = mp.mpf("1.02292821035354")
a2 = mp.mpf(2)
I0 = 2 * mp.sin(alpha / 2) / alpha
I2 = mp.mpf(1) / 2 + mp.sin(alpha) / (2 * alpha)
J = -(2 / alpha ** 2) * I2 + (mp.sin(alpha / 2) / alpha + 2 * mp.cos(alpha / 2) / alpha ** 2) * I0
c1 = I0 ** 2 / (I2 + J)
H = 2 - 1 / c1
beta = B / m
v = (H - tau) / (1 - beta)
print("H(1.464)              =", mp.nstr(H, 20))
print("tau                   =", mp.nstr(tau, 20), " exact 11/3648")
print("B/m                   =", mp.nstr(beta, 20))
print("v=(H-tau)/(1-B/m)     =", mp.nstr(v, 20))
print("  record              = 0.6734808616745137")
print("beta*v                =", mp.nstr(beta * v, 20))
print("v-(H-tau)             =", mp.nstr(v - (H - tau), 20))
print("v-H                   =", mp.nstr(v - H, 20))
print("beta*v - tau          =", mp.nstr(beta * v - tau, 20))
print("required knot-sum (A) = beta*v    =", mp.nstr(beta * v, 16))
print("required knot-sum (B) = beta*v-tau=", mp.nstr(beta * v - tau, 16))

# --- ceiling value ---
p0 = Fraction(10909258999421303588095230195816054408197, 16000000000000000000000000000000000000000)
v_ceil = p0 + Fraction(1, 6 * 256 ** 2)
print("p0                    =", mp.nstr(mp.mpf(p0), 20))
print("v_ceil = p0 + 1/393216=", mp.nstr(mp.mpf(v_ceil), 20), " claim 0.681831230595341890922618553905170067178979166")

# --- j=256 consistency ---
print("s_256 = 256/256^2     =", Fraction(256, 256 ** 2), "= 1/256")
print("(1/256)*r(1) both sides; r(1)=0 -> 0; near-CUE law row256 free s_256 ~ 211.43/256 =", mp.nstr(mp.mpf(211.4320091424858) / 256, 10))
