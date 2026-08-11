#!/usr/bin/env python3
"""Window scan at lambda=2/3 with EXACT kernels (mpmath 1D integrals).
v(s) = A cos(w s) on [-la/2, la/2], A^2 = 1/(la/2 + sin(w la)/(2w)).
K(u) = A^2 * la/2 * [ sinc(pi la u) + (1/2)( sinc(la(w+pi u)) + sinc(la(w-pi u)) ) ]
(validated at w=0 against the flat-window closed form m2, m3).
m2 = 1 + A2, A2 = int K^2 (1-S^2)
m3 = 1 + 3A2 + A3, A3 = D - 3B + 2C
D = int K(u) (K*K)(u) du = int Khat(xi)^3 dxi   [Parseval]
B = int K(u) (K*K)(u) S(u)^2 du                [1D, K*K via numeric convolution below]
C = int (Khat * Shat)^3 dxi, Khat = FT(K), Shat = 1_{|xi|<=1/2}
Khat(xi) = A^2 * la/2 * [ (1/la) 1_{|xi|<=la/2}
    + (1/2)( (1/la) e^{2pi i (w/(2pi))... } -> for even: (1/(2la))(1_{|xi-w/pi|<=la/2} + 1_{|xi+w/pi|<=la/2}) * ... ]
Actually compute Khat(xi) directly by quadrature of K(u) cos(2 pi xi u).
"""
import numpy as np
from mpmath import mp, mpf, quad, inf
mp.dps = 20

def S(u): return mp.sinc(mp.pi*u)

def Kfun(u, la, w):
    if abs(w) < 1e-12:
        return mp.sinc(mp.pi*la*u)
    A2 = 1/(la/2 + mp.sin(w*la)/(2*w))
    return A2*la/2*(mp.sinc(mp.pi*la*u) + 0.5*(mp.sinc(la*(w+mp.pi*u)) + mp.sinc(la*(w-mp.pi*u))))

def A2(la, w):
    return quad(lambda u: Kfun(u, la, w)**2*(1-S(u)**2), [-inf, inf])

def KstarK(u, la, w):
    # numeric convolution (K*K)(u) on a grid, then evaluate by interpolation
    return None

def Dterm(la, w):
    # D = int K (K*K) = int Khat^3 ; compute Khat on a fine grid and integrate
    # Khat(xi) = int K(u) cos(2 pi xi u) du  (K even)
    return None

def Bterm(la, w):
    return None

def Cterm(la, w):
    # C = int (Khat*Shat)^3; compute Khat on grid, convolve with box [1/2], cube, integrate
    return None

def grid_Khat(la, w, N=6001, U=300.0):
    us = np.linspace(-U, U, N)
    Ku = np.array([float(Kfun(mpf(u), la, w)) for u in us])
    du = us[1]-us[0]
    def khat(xi):
        # int K(u) cos(2 pi xi u) du ~ sum Ku cos(2 pi xi u) du
        return np.sum(Ku*np.cos(2*np.pi*xi*us))*du
    return khat, us, Ku, du

def compute(la, w, N=6001, U=300.0):
    A2v = float(A2(la, w))
    khat, us, Ku, du = grid_Khat(la, w, N, U)
    # D = int Khat^3 dxi
    xi = np.linspace(-4, 4, 20001)
    Kh = np.array([khat(x) for x in xi])
    D = np.sum(Kh**3)*(xi[1]-xi[0])
    # B = int K(u)(K*K)(u) S^2 du: (K*K)(u) = int Khat(xi)^2 e^{2pi i u xi} dxi (K even -> real cos)
    def KK(u_arr):
        u_arr = np.atleast_1d(u_arr)
        return np.einsum('k,uk->u', Kh**2, np.cos(2*np.pi*np.outer(u_arr, xi)))*(xi[1]-xi[0])
    B = np.sum(Ku*KK(us)*np.sinc(us)**2)*du
    # C = int (Khat*Shat)^3 dxi ; (Khat*Shat)(xi) = int Khat(t) 1_{|xi-t|<=1/2} dt
    Kbox = np.zeros_like(xi)
    for i, x in enumerate(xi):
        m = (np.abs(xi - x) <= 0.5)
        Kbox[i] = np.sum(Kh[m])*(xi[1]-xi[0])
    C = np.sum(Kbox**3)*(xi[1]-xi[0])
    m2 = 1 + A2v
    m3 = 1 + 3*A2v + (D - 3*B + 2*C)
    return m2, m3, D, B, C

# validate against flat closed forms at w=0
for la in (mpf(2)/3, mpf(1)):
    la2 = float(la)
    J2 = quad(lambda u: mp.sinc(mp.pi*la*u)**2*S(u)**2,[0,inf])
    m2c = 1+1/la-2*J2
    m3c = 3+3/la+1/la**2-la-6*J2*(1+1/la)
    m2, m3, D, B, C = compute(la2, 0.0)
    print(f"flat la={la2}: closed m2={float(m2c):.5f} m3={float(m3c):.5f} | grid m2={m2:.5f} m3={m3:.5f}")

print("\ncosine window scan at lambda=2/3 (2m2-m3 must be >= 2/3 = 0.6667 to beat 5/6 with s1=2/3N; >= 0.62 with s1=0.6725N):")
la = 2/3
for w in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0):
    m2, m3, D, B, C = compute(la, w)
    print(f"  cos({w:.2f}s): m2={m2:.5f} m3={m3:.5f}  2m2-m3={2*m2-m3:.5f}")

