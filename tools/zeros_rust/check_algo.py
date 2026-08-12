#!/usr/bin/env python3
"""Cross-check the Rust algorithm logic (numpy port, same f64 formulas) vs mpmath zetazero."""
import numpy as np
from mpmath import zetazero

PI = np.pi; TPI = 2*PI

def theta(t):
    u = t/TPI; t3 = t*t*t
    return (t/2)*np.log(u) - t/2 - PI/8 + 1/(48*t) + 7/(5760*t3)

def bern(n):
    b = np.zeros(n+1); b[0] = 1.0
    for m in range(1, n+1):
        s = 0.0; c = 1.0
        for k in range(m):
            s += c*b[k]; c *= (m+1-k)/(k+1)
        b[m] = -s/(m+1)
    return b[n]

def zeta_half_it(t):
    N, K = 40, 20
    lnN = np.log(N)
    re = im = 0.0
    for n in range(1, N):
        ang = -t*np.log(n); mag = 1/np.sqrt(n)
        re += mag*np.cos(ang); im += mag*np.sin(ang)
    a = np.sqrt(N)*np.cos(t*lnN); b = -np.sqrt(N)*np.sin(t*lnN)
    denom = 0.25 + t*t
    re += (-0.5*a + t*b)/denom; im += (-0.5*b - t*a)/denom
    c = N**-0.5*np.cos(t*lnN)/2; d = -N**-0.5*np.sin(t*lnN)/2
    re += c; im += d
    for k in range(1, K+1):
        pr, pi = 1.0, 0.0
        for j in range(2*k-1):
            xr = 0.5 + j
            pr, pi = pr*xr - pi*t, pr*t + pi*xr
        f = 1.0
        for m in range(2, 2*k+1): f *= m
        coef = bern(2*k)/f * N**(-(2*k) + 0.5)
        e, f2 = np.cos(t*lnN), -np.sin(t*lnN)
        tr, ti = pr*e - pi*f2, pr*f2 + pi*e
        re += coef*tr; im += coef*ti
    return re, im

def z_low(t):
    re, im = zeta_half_it(t); th = theta(t)
    return re*np.cos(th) - im*np.sin(th)

def z_high(t):
    x = t/TPI; sq = np.sqrt(x); n = int(np.floor(sq)); a = sq - n
    th = theta(t)
    k = np.arange(1, n+1)
    s = np.sum(np.cos(th - t*np.log(k))/np.sqrt(k))
    sign = -1.0 if n % 2 == 0 else 1.0
    g0 = np.cos(TPI*(a*a - a - 1/16))/np.cos(TPI*a)
    return 2*s + sign*x**-0.25*g0

def z(t):
    return z_low(t) if t < 200 else z_high(t)

# scan first ~20 zeros
t = 14.0; zprev = z(t); zeros = []
while len(zeros) < 20:
    tn = t + 0.2; zn = z(tn)
    if zprev*zn < 0:
        lo, hi, zlo = t, tn, zprev
        for _ in range(80):
            mid = 0.5*(lo+hi); zm = z(mid)
            if zlo*zm < 0: hi = mid
            else: lo, zlo = mid, zm
        zeros.append(0.5*(lo+hi))
    t, zprev = tn, zn

ref = [float(zetazero(k).imag) for k in range(1, 21)]
d = np.abs(np.array(zeros) - np.array(ref))
print("max|delta| first 20:", d.max())
print("my:", np.round(zeros[:10], 5))
print("mp:", np.round(ref[:10], 5))
