#!/usr/bin/env python3
"""Empirical Gram-matrix moments on the first 1000 LMFDB zeros.
Normalized ordinates x_i = (gamma_i/2pi) log(gamma_i/2pi)  (density 1).
G_ij = sinc(pi*la*(x_i-x_j))  (flat window), moments m_k = tr(G^k)/N.
Also cosine window v(s)=cos(sqrt(2) s) on |s|<=1/2: kernel K_c(u) = int v(s)^2 e^{2pi i s u} ds
  (computed numerically), moments of that Gram matrix.
Compare: theory flat m2=1/la+la/3, m3 = 3 + 15/(4la) - la - 6(J2+J3) (my diagram),
paper m3(1)=2.
"""
import numpy as np

zs = np.loadtxt('tools/data/zeros_1_1000.txt')[:, 1]
x = (zs / (2*np.pi)) * np.log(zs / (2*np.pi)) - zs / (2*np.pi) + 7/8
N = x.size
print(f"N = {N}, x-range [{x[0]:.2f}, {x[-1]:.2f}], mean spacing {np.mean(np.diff(x)):.4f}")

def moments(la, xs):
    d = xs[:, None] - xs[None, :]
    G = np.sinc(la * d)
    n = xs.size
    G2 = G @ G
    G3 = G2 @ G
    G4 = G3 @ G
    return (np.trace(G2)/n, np.trace(G3)/n, np.trace(G4)/n)

def cosine_kernel(u):
    # K_c(u) = int_{-1/2}^{1/2} cos^2(sqrt2 s) e^{2 pi i s u} ds  =  int cos^2 * cos(2 pi s u) ds
    # cos^2(a s) = (1 + cos(2 a s))/2
    # int_{-1/2}^{1/2} cos(2 pi s u) ds = sinc(pi u)
    # int_{-1/2}^{1/2} cos(2 a s) cos(2 pi s u) ds = (1/2)[ sinc(pi(u - a/pi)) + sinc(pi(u + a/pi)) ]
    a = np.sqrt(2)
    return 0.5*np.sinc(u) + 0.25*(np.sinc(u - a/np.pi) + np.sinc(u + a/np.pi))

def moments_cos(xs):
    d = xs[:, None] - xs[None, :]
    G = cosine_kernel(d)
    n = xs.size
    G2 = G @ G; G3 = G2 @ G; G4 = G3 @ G
    return (np.trace(G2)/n, np.trace(G3)/n, np.trace(G4)/n)

print("\nflat window, all 1000 zeros:")
for la in (1.0, 0.8, 0.66, 0.6, 0.5):
    m2, m3, m4 = moments(la, x)
    print(f"  la={la:.2f}: m2={m2:.4f} m3={m3:.4f} m4={m4:.4f}  2m2-m3={2*m2-m3:.4f}")

print("\nflat window, interior zeros (indices 51..950, drop edges):")
xi = x[50:950]
for la in (1.0, 0.66):
    m2, m3, m4 = moments(la, xi)
    print(f"  la={la:.2f}: m2={m2:.4f} m3={m3:.4f} m4={m4:.4f}  2m2-m3={2*m2-m3:.4f}")

print("\ncosine window v=cos(sqrt2 s), interior:")
m2, m3, m4 = moments_cos(xi)
print(f"  m2={m2:.4f} m3={m3:.4f} m4={m4:.4f}  2m2-m3={2*m2-m3:.4f}")

# theory reference
print("\ntheory (flat window, corrected closed forms):")
for la in (1.0, 0.8, 0.66, 0.6, 0.5):
    m2t = 1/la + la/3
    # m3 corrected: 3 + 3/la + 1/la^2 - la - 6*J2*(1+1/la); J2 = int0^inf sinc(pi la u)^2 sinc(pi u)^2 du
    from mpmath import mp, mpf, quad, inf
    mp.dps = 25
    J2 = quad(lambda u: mp.sinc(mp.pi*la*u)**2 * mp.sinc(mp.pi*u)**2, [0, inf])
    m3t = 3 + 3/la + 1/la**2 - la - 6*(float(J2))*(1+1/la)
    print(f"  la={la:.2f}: m2={m2t:.4f} m3={m3t:.4f}  2m2-m3={2*m2t-m3t:.4f}")
