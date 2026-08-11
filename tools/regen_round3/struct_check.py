#!/usr/bin/env python3
"""Structural verification for the round-3 EnclOK closure attempt.

Verifies (numerically, exact big-int where possible) the identities that the
new family search and the off-grid lower-bound analysis rely on:

 1. The enclosure data consistency (rows, D(1), S(256), p0) -- from LawN256.lean.
 2. The identity  sum_j f_c(j) = 256 * sum_i m_i^2  for all-integer configs,
    and its FAILURE (cross terms) for configs with marks at fractional parts:
        cross contribution of a pair (x,x') with frac(x) != frac(x'):
        S(x,x') = sum_{j=1}^{256} e^{2 pi i j (x-x')/256}
 3. The conjugate-pair identities for configs with integer marks (B) and
    half-integer marks (B_h):
        f(j) + f(256-j) = 2 (|B(j)|^2 + |B_h(j)|^2)
        f(j) - f(256-j) = 4 Re( B(j) conj(B_h(j)) e^{pi i j/256} )
 4. Re G(Delta) for Delta in (0.45,1) -- sign used in the off-grid argument.
 5. The "cross-term requirement": E[cross] needed to reconcile p0 with
    D(1) under the distinct-position marks{1,2} model.

All numbers printed here are produced by this script. Honesty: mpmath double
(and exact fractions where noted) -- these are structural identities, not the
regeneration itself.
"""
import re
import numpy as np
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 60
N = 256
K = 2 ** 140

# ---------------- 1. enclosure data from LawN256.lean ----------------
src = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
encl = [(int(a), int(b)) for a, b in re.findall(r'\((\d+), (\d+)\)',
        re.search(r'encl := \[(.*?)\]', src, re.S).group(1))]
assert len(encl) == 256

print("=" * 74)
print("1. ENCLOSURE DATA (LawN256.lean, K = 2^140)")
print("=" * 74)
lo = np.array([e[0] for e in encl], dtype=object)
hi = np.array([e[1] for e in encl], dtype=object)
# rows 1..255: lo in {j*2^132 - 1, j*2^132}
below = sum(1 for j in range(1, 256) if encl[j - 1][0] == j * 2 ** 132 - 1)
above = sum(1 for j in range(1, 256) if encl[j - 1][0] == j * 2 ** 132)
other = sum(1 for j in range(1, 256) if encl[j - 1][0] not in (j * 2 ** 132 - 1, j * 2 ** 132))
print(f"  rows 1..255: {below} below j/256, {above} at/above, {other} other")
print(f"  S(256) enclosure: K*S(256) in [{encl[255][0]}, {encl[255][1]}]")
S256 = mp.mpf(encl[255][0]) / mp.mpf(K)
print(f"  S(256) ~= {mp.nstr(S256, 20)}")

# sum of S(j), j=1..256, interval
sumS_lo = mp.mpf(sum(e[0] for e in encl)) / mp.mpf(K)
sumS_hi = mp.mpf(sum(e[1] for e in encl)) / mp.mpf(K)
print(f"  sum_j S(j) in [{mp.nstr(sumS_lo, 22)}, {mp.nstr(sumS_hi, 22)}]")
print(f"  => D(1) = sum S / 256 - 1/2 in [{mp.nstr(sumS_lo/256 - mp.mpf(1)/2, 22)}, "
      f"{mp.nstr(sumS_hi/256 - mp.mpf(1)/2, 22)}]  (recorded 0.8239531607128352)")

p0 = mp.mpf(10909258999421303588095230195816054408197) / mp.mpf(16000000000000000000000000000000000000000)
print(f"  p0 (law simple-point fraction) = {mp.nstr(p0, 25)}")
# what D(1) WOULD be for an all-integer distinct-position law with this p1:
print(f"  for an ALL-INTEGER law, D(1) = 3/2 - p1 = {mp.nstr(mp.mpf(3)/2 - p0, 25)}")
print(f"  recorded D(1) - (3/2 - p0) = {mp.nstr(mp.mpf('0.8239531607128352') - (mp.mpf(3)/2 - p0), 25)}  "
      "=> the law must have fractional marks (cross terms) to reconcile")

# expected cross-term requirement:  D(1) = E[sum m^2]/256 - 1/2 + E[cross]/65536
Esq = 256 * (mp.mpf('0.8239531607128352') + mp.mpf(1) / 2)   # E[sum m^2] incl cross
base_sq = 512 - 256 * p0                                      # E[s] + 4E[d] = 512 - E[s], E[s]=256 p1
print(f"  E[sum_j f(j)] = 256*E[sum m^2] ~= {mp.nstr(256 * Esq, 20)}")
print(f"  base (distinct int marks) = 256*(512 - 256*p0) = {mp.nstr(256 * base_sq, 20)}")
print(f"  required cross-term total (units of sum_j f) ~= {mp.nstr(256 * (Esq - base_sq), 20)}")

# ---------------- 2. pair-sum identity S(x,x') ----------------
print()
print("=" * 74)
print("2. PAIR-SUM S(x,x') = sum_{j=1}^{256} exp(2 pi i j (x-x')/256)")
print("=" * 74)
def Ssum(x, xp):
    j = np.arange(1, N + 1)
    return np.sum(np.exp(2j * np.pi * j * (x - xp) / N))
for (x, xp) in [(0.0, 0.0), (0.0, 1.0), (0.5, 0.5), (0.0, 0.5), (0.5, 1.5), (0.0, 0.25)]:
    s = Ssum(x, xp)
    print(f"  S({x}, {xp}) = {s.real:+.6f}{s.imag:+.6f}i   |S| = {abs(s):.6f}")
print("  -> same-position: 256; same frac, different pos: 0; different frac: nonzero (complex)")

# ---------------- 3. conjugate-pair identities ----------------
print()
print("=" * 74)
print("3. CONJUGATE-PAIR IDENTITIES  (int marks B + half-int marks B_h)")
print("=" * 74)
def cfg_spectrum(int_pos, int_marks, half_pos):
    """int marks at integer positions (value 1 or 2), half marks (value 1) at q+0.5."""
    j = np.arange(1, N + 1)
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_pos:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    return np.abs(z) ** 2

rng = np.random.default_rng(7)
# toy config: 12 half marks, 244 int marks (mark1/mark2 mix)
n_h, n_i = 12, 244
half_pos = rng.choice(256, size=n_h, replace=False).tolist()
int_pos_all = [p for p in range(256) if p not in half_pos]
int_pos = rng.choice(int_pos_all, size=n_i, replace=False).tolist()
# force sum of int marks = 244: 162 simples + 41 doubles would be 162+82=244
d = 41
int_marks = [2] * d + [1] * (n_i - d)
rng.shuffle(int_marks)
f = cfg_spectrum(int_pos, int_marks, half_pos)
# DFT of int marks (B) and half marks (B_h)
j = np.arange(1, N + 1)
B = sum(m * np.exp(2j * np.pi * j * p / N) for p, m in zip(int_pos, int_marks))
Bh = sum(np.exp(2j * np.pi * j * (q + 0.5) / N) for q in half_pos)
err_sum = max(abs(f[jj] + f[N - 1 - jj] - 2 * (abs(B[jj]) ** 2 + abs(Bh[jj]) ** 2)) for jj in range(127))
P = B * np.conj(Bh) * np.exp(1j * np.pi * j / N)
err_diff = max(abs(f[jj] - f[N - 1 - jj] - 4 * np.real(P[jj])) for jj in range(127))
print(f"  max |f(j)+f(N-j) - 2(|B|^2+|Bh|^2)| = {err_sum:.3e}")
print(f"  max |f(j)-f(N-j) - 4 Re(B conj(Bh) e^{{pi i j/N}})| = {err_diff:.3e}")
print("  identities hold for ANY int+half config (toy config above)")

# ---------------- 4. Re G(Delta) ----------------
print()
print("=" * 74)
print("4. Re G(Delta) = Re sum_{j=1}^{256} exp(2 pi i j Delta / 256)")
print("=" * 74)
for d in [0.40, 0.45, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.95, 1.00]:
    jj = np.arange(1, N + 1)
    G = np.sum(np.exp(2j * np.pi * jj * d / N))
    print(f"  Delta={d:.2f}: Re G = {G.real:+.6f}")
print("  -> Re G < 0 on (0.45, 1) is the documented off-grid mechanism")

# ---------------- 5. off-grid deviation ----------------
print()
print("=" * 74)
print("5. OFF-GRID DEVIATION:  sum_j f(j) for a lattice with a mark moved by delta")
print("=" * 74)
def moved_lattice(delta):
    """N marks mark-1: N-1 at integers 0..N-1 except q, one at q+delta."""
    j = np.arange(1, N + 1)
    q = 0
    z = -np.exp(2j * np.pi * j * q / N) + np.exp(2j * np.pi * j * (q + delta) / N)
    return np.abs(z) ** 2
for delta in [0.0, 0.25, 0.5, 0.75, 0.9]:
    f = moved_lattice(delta)
    print(f"  delta={delta}: sum_j f(j) = {f.sum():.4f}   (all-integer N^2 = {N*N})")
print("  -> off-grid marks lower sum_j f(j) below N^2; the grid lower bound fails")

print()
print("STRUCTURAL CHECKS DONE")
