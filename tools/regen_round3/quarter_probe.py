#!/usr/bin/env python3
"""Test: balanced quarter marks (n_{1/4} = n_{3/4}) give POSITIVE cross while
keeping f(256) a perfect square.  Config: int marks (1/2) + 12 half marks +
2k balanced quarter marks (k at q+0.25, k at q+0.75).  Sum marks = 256.
Measures cross, f(256), and the total required to hit E[cross] = +378.9.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int
DFT_q1 = np.exp(2j * np.pi * j * 0.25 / N)[:, None] * DFT_int
DFT_q3 = np.exp(2j * np.pi * j * 0.75 / N)[:, None] * DFT_int

def measure(n_h, d, k, seed=9):
    """n_h half marks, d int doubles, k quarter pairs (k at +0.25, k at +0.75)."""
    rng = np.random.default_rng(seed)
    s = N - n_h - 2 * k - 2 * d
    if s < 0:
        return None
    int_pos = rng.choice(N, size=s + d, replace=False)
    int_marks = np.array([1] * s + [2] * d, dtype=float)
    rng.shuffle(int_marks)
    half_q = rng.choice(N, size=n_h, replace=False)
    q1 = rng.choice(N, size=k, replace=False)
    q3 = rng.choice(N, size=k, replace=False)
    z = DFT_int[:, int_pos] @ int_marks
    z = z + DFT_half[:, half_q].sum(axis=1)
    z = z + DFT_q1[:, q1].sum(axis=1) + DFT_q3[:, q3].sum(axis=1)
    f = np.abs(z) ** 2
    sum_m2 = s + 4 * d + n_h + 2 * k
    cross = f.sum() - N * sum_m2
    # f(256) should be (256 - 2 n_h)^2 (balanced quarters cancel)
    return dict(sum255=f[:255].sum(), f256=f[255], cross=cross, sq=(256 - 2 * n_h) ** 2, sum_m2=sum_m2)

print("balanced quarter marks, k pairs (one at +1/4, one at +3/4):")
print(f"{'n_h':>4} {'d':>4} {'k':>4} {'sum255':>10} {'f(256)':>10} {'(256-2nh)^2':>11} {'cross':>9}")
for (nh, d, k) in [(12, 41, 1), (12, 41, 2), (12, 41, 4), (12, 40, 2), (11, 41, 2), (12, 45, 4), (12, 44, 2)]:
    r = measure(nh, d, k)
    if r:
        print(f"{nh:>4} {d:>4} {k:>4} {r['sum255']:>10.1f} {r['f256']:>10.1f} {r['sq']:>11} {r['cross']:>9.1f}")

print()
print("DATA targets: E[sum255] = 32640, E[f(256)] = 54126.6, E[d] = 40.726, E[cross] = +378.9")
