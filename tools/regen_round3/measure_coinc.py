#!/usr/bin/env python3
"""Direct measurement of all spectral quantities for int+half configs WITH
coincidences, to pin the exact relations the data must satisfy.
Config: s int simples + d int doubles + (n_h + c) half marks where c half
positions carry TWO marks (coincident), so total marks = s+2d+n_h+c = 256.
Measures: cross, sum_{1..255} f, f(256), sum(|B|^2+|C|^2), sum 2Re(...).
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int

def measure(n_h, d, c, seed):
    rng = np.random.default_rng(seed)
    s = N - n_h - c - 2 * d
    int_pos = rng.choice(N, size=s + d, replace=False)
    int_marks = np.array([1] * s + [2] * d, dtype=float)
    rng.shuffle(int_marks)
    half_q = rng.choice(N, size=n_h, replace=False).tolist()
    coinc_q = rng.choice(N, size=c, replace=False).tolist()  # extra coincident half marks
    # spectrum
    z = DFT_int[:, int_pos] @ int_marks
    z = z + DFT_half[:, half_q].sum(axis=1) + 2.0 * DFT_half[:, coinc_q].sum(axis=1)
    f = np.abs(z) ** 2
    # B, C with multiplicity
    B = DFT_int[:, int_pos] @ int_marks
    C = DFT_half[:, half_q].sum(axis=1) / np.exp(2j * np.pi * j * 0.5 / N)  # int parts
    C = C + 2.0 * DFT_half[:, coinc_q].sum(axis=1) / np.exp(2j * np.pi * j * 0.5 / N)
    sum_m2 = s + 4 * d + n_h + 2 * c
    cross = f.sum() - N * sum_m2
    S1 = sum(abs(B[jj]) ** 2 + abs(C[jj]) ** 2 for jj in range(255))
    S2 = sum(2 * np.real(B[jj] * np.conj(C[jj]) * np.exp(-1j * np.pi * (jj + 1) / N)) for jj in range(255))
    print(f"n_h={n_h} d={d} c={c}: marks={s+2*d+n_h+c}  sum m^2={sum_m2}  "
          f"sum_{{1..255}} f={sum(f[:255]):10.2f}  f(256)={f[255]:10.2f}  "
          f"cross={cross:9.2f}  S1={S1:10.2f}  S2={S2:8.2f}")
    return sum(f[:255]), f[255], cross

print("data targets: sum_{1..255} fbar = 32640, fbar(256) = 54126.59, E[d]=40.726, E[cross]=378.92")
print()
for (nh, d, c) in [(12, 41, 0), (12, 41, 2), (12, 41, 4), (12, 45, 0), (12, 45, 3), (11, 41, 0), (12, 40, 2)]:
    measure(nh, d, c, 5)
