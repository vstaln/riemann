#!/usr/bin/env python3
"""Jensen / Polya-frequency structure checks (section F of the audit)."""
import mpmath as mp
mp.mp.dps = 60

def P(s):
    print(s, flush=True)

def xi(s):
    if abs(s) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    if abs(s - 1) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def xi_c(z):
    return xi(mp.mpc(0.5) + z)

def xi_coeff(k):
    r = mp.mpf("0.7")
    npts = 96
    val = mp.mpc(0)
    for j in range(npts):
        th = 2 * mp.pi * j / npts
        z = r * mp.e ** (mp.j * th)
        val += xi_c(z) / z ** (k + 1) * mp.e ** (mp.j * th)
    return val * r / npts

P("== gamma(j) = j! * [z^{2j}] xi(1/2+z)  (GORZ normalization) ==")
gam = []
for k in range(0, 44, 2):
    c2k = mp.re(xi_coeff(k))
    gam.append(mp.fac(k // 2) * c2k)
for j in range(10):
    P(f"  gamma({j}) = {mp.nstr(gam[j], 15)}")

P("")
P("== Jensen polynomial hyperbolicity (roots real for small d; d<=8 known PROVEN) ==")


def Jpoly(d, n):
    return [mp.binomial(d, j) * gam[n + j] for j in range(d + 1)]

for d, n in [(2, 0), (3, 1), (5, 0), (8, 2), (9, 0), (10, 0)]:
    p = Jpoly(d, n)
    m = max(abs(c) for c in p)
    rts = mp.polyroots([c / m for c in p], maxsteps=2000)
    max_imag = max(abs(mp.im(r)) for r in rts)
    P(f"  d={d:<3d} n={n}: max|Im(root)| = {mp.nstr(max_imag, 5)}  {'hyperbolic' if max_imag < 1e-6 else 'NOT hyperbolic'}")

P("")
P("== PF (Toeplitz a_{j-k}) minors vs Hankel (a_{i+j}) minors of {gamma(j)/j!} ==")
cj = [gam[j] / mp.fac(j) for j in range(len(gam))]
P("Toeplitz minors (a_{j-k}):")
for size in [2, 3, 4]:
    for start in [0, 2]:
        mat = mp.matrix(size)
        for i in range(size):
            for j in range(size):
                idx = start + (j - i)
                mat[i, j] = cj[idx] if 0 <= idx < len(cj) else mp.mpf(0)
        P(f"  size={size} start={start}: det = {mp.nstr(mp.det(mat), 12)}")
P("Hankel minors (a_{i+j}):")
for size in [2, 3, 4]:
    mat = mp.matrix(size)
    for i in range(size):
        for j in range(size):
            mat[i, j] = cj[i + j]
    P(f"  size={size}: det = {mp.nstr(mp.det(mat), 12)}")

P("")
P("== d=2 discriminant = log-concavity of {gamma(j)/j!}:  c_{j+1}^2 >= c_j c_{j+2} ==")
for j in range(6):
    lc = cj[j + 1] ** 2 - cj[j] * cj[j + 2]
    P(f"  j={j}: c_{{j+1}}^2 - c_j c_{{j+2}} = {mp.nstr(lc, 10)}")

P("DONE.")
