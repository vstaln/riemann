#!/usr/bin/env python3
"""Window scan at fixed bandwidth lambda: does any window v (supported on [-la/2, la/2],
int v^2 = 1) give 2*m2 - m3 >= 2/3 (needed to beat 5/6 with s1=2/3N) or >= 0.62
(needed with s1=0.6725N)?

Kernel K(u) = int v(s)^2 e^{2 pi i s u} ds  (even, K(0)=1).
Moments (diagram, determinantal):
  m2 = 1 + A2,          A2 = int K(u)^2 (1 - S(u)^2) du
  m3 = 1 + 3 A2 + A3,   A3 = D - 3 B + 2 C
  D = int K(u) (K*K)(u) du
  B = int K(u) (K*K)(u) S(u)^2 du
  C = int (Khat * Shat)(xi)^3 dxi
  S(u) = sinc(pi u), Shat = 1_{|xi|<=1/2}, Khat = FT of K.
All 1D. Numerics: mpmath or numpy GL.
"""
import numpy as np
from mpmath import mp, mpf, quad, inf
mp.dps = 20

def S(u): return mp.sinc(mp.pi*u)

def kernel_from_v(v, la, N=2001, U=120.0):
    """K(u) for |u| <= U via direct quadrature of int_{-la/2}^{la/2} v(s)^2 e^{2pi i s u} ds.
    v given as a callable on [-la/2, la/2]; normalized int v^2 = 1 by the caller."""
    xs = np.linspace(-la/2, la/2, 10001)
    vs = v(xs)
    w = np.ones_like(xs); w[0]=0.5; w[-1]=0.5   # trapezoid
    I2 = np.sum(vs**2 * w) * (la/10000)
    vs = vs / np.sqrt(I2)                        # ensure int v^2 = 1
    us = np.linspace(-U, U, N)
    # K(u) = int v^2 cos(2 pi s u) ds (even)
    Ku = np.array([np.sum(vs**2 * np.cos(2*np.pi*xs*u) * w) * (la/10000) for u in us])
    return us, Ku

def conv_even(f, g, us, du):
    """(f*g)(u) for even f,g sampled on grid us (uniform step du), via FFT."""
    n = us.size
    # assume us = (-U..U) with du; zero-pad? approximate cyclic conv on 2x range
    ext = np.concatenate([f, np.zeros(n), f])   # not correct; use scipy-like via numpy fft with full padding
    # simpler: use direct O(n^2) for small n
    out = np.empty(n)
    for i in range(n):
        # (f*g)(us[i]) = int f(t) g(us[i]-t) dt ~ sum_j f(us[j]) g(us[i]-us[j]) du
        # g(us[i]-us[j]) not on grid; use linear interp
        idx = (us[i] - us)  # want g at these points; nearest grid
        j = np.rint((us[i] - us)/du).astype(int)
        ok = (j >= 0) & (j < n)
        out[i] = np.sum(f[ok]*g[j[ok]])*du
    return out

def moments_flat(la):
    """flat window closed forms (checked vs direct 2D)."""
    J2 = quad(lambda u: mp.sinc(mp.pi*la*u)**2 * S(u)**2, [0, inf])
    m2 = 1 + 1/la - 2*J2
    m3 = 3 + 3/la + 1/la**2 - la - 6*J2*(1+1/la)
    return m2, m3

print("flat-window reference at lambda = 2/3:")
m2, m3 = moments_flat(mpf(2)/3)
print(f"  m2 = {float(m2):.6f}  m3 = {float(m3):.6f}  2m2-m3 = {float(2*m2-m3):.6f}  (need >=2/3={2/3:.4f} or >=0.62)")

# Cosine-type windows v(s) = A*cos(w s) on [-la/2, la/2]
def scan():
    la = 2/3
    for w in (0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, np.pi/2, 5.0, 6.0, 8.0, 10.0):
        if w == 0:
            v = lambda s: np.ones_like(s)
            label = "flat"
        else:
            v = lambda s, w=w: np.cos(w*s)
            label = f"cos({w:.1f}s)"
        us, Ku = kernel_from_v(v, la)
        du = us[1]-us[0]
        # A2
        Ku_mp = [mp.sinc(mp.pi*la*0.0)]  # placeholder
        # do A2, D, B numerically on grid; C via 1D mpmath
        Su = np.sinc(us)
        A2 = np.sum(Ku**2 * (1 - Su**2)) * du
        KK = conv_even(Ku, Ku, us, du)          # (K*K)(u)
        D = np.sum(Ku * KK) * du
        B = np.sum(Ku * KK * Su**2) * du
        # C = int (Khat*Shat)^3 ; Khat = FT(K). Compute Khat on a fine xi grid, convolve with box, cube, integrate.
        # use Parseval-free: C = intintint K K K S S S -> reduce via (KS*KS*KS) is 2D-ish; use:
        # C = int (KS * (KS*KS))(u) du, KS = K*S
        KSu = Ku * Su
        KSKS = conv_even(KSu, KSu, us, du)
        C = np.sum(KSu * KSKS) * du
        m2v = 1 + A2
        m3v = 1 + 3*A2 + (D - 3*B + 2*C)
        print(f"  {label:12s}: m2 = {m2v:.5f}  m3 = {m3v:.5f}  2m2-m3 = {2*m2v-m3v:.5f}  (flat 2m2-m3 = {float(2*m2-m3):.5f})")

scan()
