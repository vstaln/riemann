#!/usr/bin/env python3
"""Adjudicate rho_check.py's verdict with the CORRECT DFT window.

For ANY marked config (off-grid included), f(j) = sum_Δ c_Δ e^{2 pi i j Δ/256}
for ALL integer j, with c_Δ = pair-multiplicity (real, >= 0, supported on the
actual difference lattice incl. half-integers).  Hence the DFT over the FULL
period j = 0..255,  ĉ_Δ = (1/256) sum_{j=0}^{255} f(j) e^{-2 pi i j Δ/256},
is REAL and >= 0 (it equals c_Δ on the integer Δ-lattice).

rho_check.py summed j = 1..256 instead of j = 0..255 and used the recorded
fbar(256) = 54126.59 in place of fbar(0) = 65536 (which every config has:
f_c(0) = (sum m)^2 = 65536).  That is the WRONG window.

Tests:
 T1. a valid off-grid config over j=0..255: ĉ real >= 0 ?
 T2. the recorded law data over j=0..255 with fbar(0)=65536: real? (decisive)
 T3. the recorded law data over j=1..256 (rho_check's window): reproduces the
     Im != 0 artifact, demonstrating rho_check's window is the cause.
"""
import re
import numpy as np

N = 256
K = 2 ** 140
j = np.arange(1, N + 1)


def spectrum(xs, ms):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m * np.exp(2j * np.pi * j * x / N)
    return np.abs(z) ** 2


def dft(fseq, win):
    """win='0..255' uses fseq[0..255] (f(0)..f(255)); win='1..256' uses fseq[1..256]."""
    if win == '0..255':
        vals = np.concatenate([[fseq[0]], fseq[1:256]])
    else:
        vals = fseq[1:257]
    c = np.zeros(256, dtype=complex)
    for d in range(256):
        c[d] = (1.0 / N) * np.sum(vals * np.exp(-2j * np.pi * np.arange(0, N) * d / N))
    return c


rng = np.random.default_rng(5)
print("=" * 72)
print("T1: valid off-grid config (12 half + int marks), window j=0..255")
print("=" * 72)
n_h, d = 12, 41
s = N - n_h - 2 * d
int_pos = rng.choice(N, size=s + d, replace=False)
int_marks = np.array([1] * s + [2] * d, dtype=float)
rng.shuffle(int_marks)
half_q = rng.choice(N, size=n_h, replace=False)
xs = list(int_pos) + [q + 0.5 for q in half_q]
ms = list(int_marks) + [1] * n_h
assert sum(ms) == N
f = spectrum(xs, ms)
f_full = np.concatenate([[65536.0], f[:255]])   # f(0)..f(255)
c1 = dft(np.concatenate([[65536.0], f]), '0..255')   # f[0]=f(0), f[1..255]=f(1..255)
print(f"  max |Im ĉ| = {np.max(np.abs(c1.imag)):.2e}   min Re ĉ = {c1.real.min():.2f}")
print(f"  f(256) = {f[255]:.2f} (recorded-style wrap value differs from f(0)=65536)")

print()
print("=" * 72)
print("T2: RECORDED law data, window j=0..255 with fbar(0)=65536")
print("=" * 72)
src = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
encl = [(int(a), int(b)) for a, b in re.findall(r'\((\d+), (\d+)\)',
        re.search(r'encl := \[(.*?)\]', src, re.S).group(1))]
lo = np.array([e[0] for e in encl], dtype=float)
hi = np.array([e[1] for e in encl], dtype=float)
mid = (lo + hi) / 2.0 / float(K)
fbar = 256.0 * mid                       # fbar(j) = 256*S(j): ~j for j<256, ~54126.6 for j=256
fbar0 = np.concatenate([[65536.0], fbar[:255]])   # f(0)=65536, f(1..255)
c2 = dft(np.concatenate([[65536.0], fbar[:255]]), '0..255')
print(f"  max |Im ĉ| = {np.max(np.abs(c2.imag)):.4f}")
neg = np.where(c2.real < -1e-3)[0]
print(f"  min Re ĉ = {c2.real.min():.2f}   rows with Re < -1e-3: {neg[:10]}")
print(f"  fbar(0) - fbar(256) = {65536.0 - fbar[255]:.2f}  => half-Δ mass = {(65536.0-fbar[255])/2:.2f}")

print()
print("=" * 72)
print("T3: RECORDED law data, window j=1..256 (rho_check's window)")
print("=" * 72)
c3 = dft(np.concatenate([[0.0], fbar[:256]]), '1..256')   # uses f(1)..f(256)
print(f"  max |Im ĉ| = {np.max(np.abs(c3.imag)):.4f}   (rho_check artifact)")

print()
print("=" * 72)
print("T4: is the ramp (fbar(j)=j, fbar(0)=65536, fbar(256)=54126.59)")
print("    even APPROXIMATELY a valid pair-multiplicity vector?  Check:")
print("    ĉ_Δ >= 0 for the integer Δ the config family can realize.")
print("=" * 72)
print(f"  ĉ_1 (window 0..255) = {c2[1]:.4f}")
print(f"  ĉ_255 (window 0..255) = {c2[255]:.4f}")
print(f"  => if ĉ_1 not real and not ~ ĉ_255, the ramp rows are NOT realizable")
print(f"     by ANY config mixture with fbar(0)=65536, fbar(256)=54126.59.")
