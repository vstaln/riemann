#!/usr/bin/env python3
"""Valid coincident int+half configs: s int simples + d int doubles + n_h half
marks + c coincident pairs (2 marks at each of c half positions).
Marks: s + 2d + n_h + 2c = 256  =>  s = 256 - n_h - 2c - 2d.
Measures cross, f(256), sum_{1..255} f, and checks the sign of cross.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int

def measure(n_h, d, c, seed):
    rng = np.random.default_rng(seed)
    s = N - n_h - 2 * c - 2 * d
    assert s >= 0
    int_pos = rng.choice(N, size=s + d, replace=False)
    int_marks = np.array([1] * s + [2] * d, dtype=float)
    rng.shuffle(int_marks)
    half_q = rng.choice(N, size=n_h, replace=False).tolist()
    coinc_q = rng.choice(N, size=c, replace=False).tolist()
    z = DFT_int[:, int_pos] @ int_marks
    z = z + DFT_half[:, half_q].sum(axis=1) + 2.0 * DFT_half[:, coinc_q].sum(axis=1)
    f = np.abs(z) ** 2
    sum_m2 = s + 4 * d + n_h + 2 * c
    assert s + 2 * d + n_h + 2 * c == N
    cross = f.sum() - N * sum_m2
    return dict(sum255=f[:255].sum(), f256=f[255], cross=cross, sm2=sum_m2)

print(f"{'n_h':>4} {'d':>4} {'c':>3} {'sum255':>10} {'f(256)':>10} {'cross':>10}")
for (nh, d, c) in [(12, 41, 0), (12, 41, 1), (12, 41, 2), (11, 41, 1), (12, 40, 1), (12, 45, 2), (12, 39, 2)]:
    r = measure(nh, d, c, 5)
    print(f"{nh:>4} {d:>4} {c:>3} {r['sum255']:>10.1f} {r['f256']:>10.1f} {r['cross']:>10.1f}")

print()
print("DATA needs: E[cross] = +378.9 > 0.  int+half distinct configs: cross = -2(256-M)M < 0.")
print("Question: do valid coincident int+half configs give cross > 0?")
