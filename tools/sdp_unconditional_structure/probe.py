#!/usr/bin/env python3
"""Float probe for the SDP-unconditional-structure note (2026-08-14).

Belief it changes: (1) the classical bandlimited functions are NOT competitive
(Selberg's function is WORSE than Montgomery's hat), so the CGdL SDP layer is
load-bearing, not a cheap trick; (2) the CGdL Gaussian majorant family is NOT
strip-positive at box half-width b = 1/(2 pi), so the CGdL primal cone does NOT
transfer to the unconditional (BGSTB) setting -- the correct cone is the
strip-positive bandlimited class (Tsang-type).

Runtime < 1 min. Uses mpmath (scipy/numpy unavailable on this machine).
"""
import mpmath as mp
mp.mp.dps = 15


def S(x):
    # Selberg's function: in A_LP with last sign change r=1, Fourier in [-1,1].
    if abs(x) < 1e-12:
        return mp.mpf(1)
    if abs(x - 1) < 1e-12:
        return mp.mpf(0)
    return (mp.sin(mp.pi * x) / (mp.pi * x))**2 / (1 - x * x)


# Z(f) = r + (2/r) int_0^r f(x) x dx  (CGdL Lemma 8), r=1.
N = 2001
h = mp.mpf(1) / (N - 1)
xs = [mp.mpf(i) * h for i in range(N)]
vals = [S(x) * x for x in xs]
integ = h / 3 * (vals[0] + vals[-1] + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-2:2]))
Z_S = 1 + 2 * integ
Z_H = mp.mpf(4) / 3  # hat function H(x)=(1-|x|)+, r=1.

print("Z_S (Selberg, r=1)   =", mp.nstr(Z_S, 12))
print("Z_H (hat, r=1)       =", mp.nstr(Z_H, 12))
print("improvement over 4/3 =", mp.nstr(Z_H - Z_S, 12))

# Strip-positivity probe at box half-width b = 1/(2 pi) (BGSTB box in z-units is b0=1).
b = mp.mpf(1) / (2 * mp.pi)
M = 129
uh = mp.mpf(1) / (M - 1)
unodes = [mp.mpf(i) * uh for i in range(M)]
w = [mp.mpf(1)]
w += [4 if i % 2 == 1 else 2 for i in range(1, M - 1)]
w += [mp.mpf(1)]


def K(z):
    # Tsang/Fejer kernel K(z) = (1/pi) int_0^1 (1-u) sech(u) cos(zu) du  (BGSTB (4.2)).
    s = sum(wi * (1 - u) * mp.sech(u) * mp.cos(z * u) for wi, u in zip(w, unodes))
    return (uh / 3) * s / mp.pi


def f(z, lam):
    # CGdL Gaussian majorant f(z) = (1 - z^2/lam^2) e^{-pi z^2}.
    return (1 - z * z / (lam * lam)) * mp.exp(-mp.pi * z * z)


minK, minF = mp.inf, mp.inf
P = 1001
for i in range(P):
    x = mp.mpf(-8) + mp.mpf(16) * i / (P - 1)
    vk = mp.re(K(x + 1j * b))
    vf = mp.re(f(x + 1j * b, mp.mpf('1.3')))
    if vk < minK:
        minK = vk
    if vf < minF:
        minF = vf
print("min Re K(x+ib), Tsang/Fejer, b=1/2pi  :", mp.nstr(minK, 12))
print("min Re f_gauss(x+ib), lambda=1.3      :", mp.nstr(minF, 12))

# Self-check: the computed Z_S must exceed the known hat value 4/3 (paper notes
# Selberg does NOT beat Montgomery), and the Tsang kernel must stay positive
# (consistent with BGSTB Lemma 6(c)) while the Gaussian goes negative.
assert Z_S > Z_H
assert minK > 0
assert minF < 0
print("PASS")
