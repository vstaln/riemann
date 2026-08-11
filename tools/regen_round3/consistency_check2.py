#!/usr/bin/env python3
"""REDO with VALID configs (sum marks = 256 exactly).
Config: s int simples + d int doubles + n_h half simples,  s + 2d + n_h = 256,
positions = s + d + n_h distinct.
Measures the exact per-config identities:
  sum_{j=1..255} f(j),  f(256),  cross = sum_j f(j) - 256*sum m^2,
  sum_{j=1..255}(|B|^2+|C|^2),  sum_{j=1..255} 2Re(B conj C e^{-piij/N})
and derives the data-driven constraints on the law's averages.
"""
import numpy as np
import mpmath as mp

N = 256
j = np.arange(1, N + 1)

def make_valid(n_h, d, seed):
    s = N - n_h - 2 * d
    rng = np.random.default_rng(seed)
    int_pos_all = rng.choice(N, size=s + d, replace=False).tolist()   # s+d int positions
    int_pos = int_pos_all[:s]
    dbl_pos = int_pos_all[s:]
    int_marks = [1] * s + [2] * d
    half_q = rng.choice(N, size=n_h, replace=False).tolist()
    return int_pos, int_marks, dbl_pos, half_q

def terms(int_pos, int_marks, dbl_pos, half_q):
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos + dbl_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_q:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    f = np.abs(z) ** 2
    B = sum(m * np.exp(2j * np.pi * j * p / N) for p, m in zip(int_pos + dbl_pos, int_marks))
    C = sum(np.exp(2j * np.pi * j * q / N) for q in half_q)
    sum_m2 = sum(m * m for m in int_marks) + n_h
    assert sum(int_marks) + n_h == N
    cross = f.sum() - N * sum_m2
    return f, B, C, cross

for (n_h, d) in [(12, 41), (12, 52), (26, 41)]:
    f, B, C, cross = terms(*make_valid(n_h, d, 5))
    S1 = sum(abs(B[jj]) ** 2 + abs(C[jj]) ** 2 for jj in range(255))
    S2 = sum(2 * np.real(B[jj] * np.conj(C[jj]) * np.exp(-1j * np.pi * (jj + 1) / N)) for jj in range(255))
    print(f"VALID n_h={n_h} d={d}  (s = {N - n_h - 2*d} int simples):")
    print(f"  sum_{{1..255}} f(j)   = {sum(f[jj] for jj in range(255)):10.2f}")
    print(f"  f(256)               = {f[255]:10.2f}    (256-2nh)^2 = {(256-2*n_h)**2}")
    print(f"  cross                = {cross:10.2f}")
    print(f"  sum_{{1..255}}(|B|^2+|C|^2)     = {S1:10.2f}")
    print(f"  sum_{{1..255}}2Re(BconjC e^-..) = {S2:10.2f}")
    print()

print("=" * 72)
print("DATA-DRIVEN CONSTRAINTS  (from LawN256.lean: rows, p0, S(256))")
print("=" * 72)
p0 = mp.mpf(10909258999421303588095230195816054408197) / mp.mpf(16000000000000000000000000000000000000000)
Ed = 128 * (1 - p0)
S256 = mp.mpf(294693210168748317632180492755635579620342098) / mp.mpf(2 ** 140)
fbar256 = 256 * S256
Ecross = 32640 + fbar256 - 256 * (256 + 2 * Ed)
print(f"  E[d] (from p0)          = {mp.nstr(Ed, 15)}")
print(f"  fbar(256)               = {mp.nstr(fbar256, 18)}")
print(f"  E[cross] (required)     = {mp.nstr(Ecross, 12)}")

print()
print("  For int+half configs with common n_h (valid, distinct positions):")
print("  measure E[sum_{1..255}(|B|^2+|C|^2)] and E[2Re term] as functions of n_h, d")
for n_h in [11, 12, 20, 26, 40]:
    row = []
    for d in [30, 41, 52]:
        f, B, C, cross = terms(*make_valid(n_h, d, 7))
        S1 = sum(abs(B[jj]) ** 2 + abs(C[jj]) ** 2 for jj in range(255))
        S2 = sum(2 * np.real(B[jj] * np.conj(C[jj]) * np.exp(-1j * np.pi * (jj + 1) / N)) for jj in range(255))
        row.append(f"d={d}: S1={S1:.0f} S2={S2:.0f} cross={cross:.0f}")
    print(f"  n_h={n_h:2d}: " + "   ".join(row))
