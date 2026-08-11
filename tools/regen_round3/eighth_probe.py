#!/usr/bin/env python3
"""Test: balanced (1/8, 3/8) mark pairs give positive cross while leaving
f(256) = (256 - 2 n_h)^2 UNCHANGED (cos(2pi/8) = -cos(2pi*3/8), sin cancels).
Config: int marks + n_h half marks + k balanced pairs (k marks at p+1/8,
k marks at q+3/8).  Sum marks = 256.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int
u18 = 0.125; u38 = 0.375
DFT_18 = np.exp(2j * np.pi * j * u18 / N)[:, None] * DFT_int
DFT_38 = np.exp(2j * np.pi * j * u38 / N)[:, None] * DFT_int

def measure(n_h, d, k, seed):
    rng = np.random.default_rng(seed)
    s = N - n_h - 2 * k - 2 * d
    assert s >= 0
    int_pos = rng.choice(N, size=s + d, replace=False)
    int_marks = np.array([1] * s + [2] * d, dtype=float)
    rng.shuffle(int_marks)
    half_q = rng.choice(N, size=n_h, replace=False)
    q1 = rng.choice(N, size=k, replace=False)
    q3 = rng.choice(N, size=k, replace=False)
    z = DFT_int[:, int_pos] @ int_marks
    z = z + DFT_half[:, half_q].sum(axis=1)
    z = z + DFT_18[:, q1].sum(axis=1) + DFT_38[:, q3].sum(axis=1)
    f = np.abs(z) ** 2
    sum_m2 = s + 4 * d + n_h + 2 * k
    cross = f.sum() - N * sum_m2
    return dict(sum255=f[:255].sum(), f256=f[255], cross=cross)

print(f"{'n_h':>4} {'d':>4} {'k':>3} {'sum255':>10} {'f(256)':>10} {'(256-2nh)^2':>12} {'cross':>10}")
for (nh, d, k) in [(12, 41, 0), (12, 41, 1), (12, 41, 2), (12, 41, 3), (11, 41, 2), (12, 40, 2)]:
    r = measure(nh, d, k, 7)
    print(f"{nh:>4} {d:>4} {k:>3} {r['sum255']:>10.1f} {r['f256']:>10.1f} {(256-2*nh)**2:>12} {r['cross']:>10.1f}")
print()
print("DATA: E[cross] = +378.9, E[f(256)] = 54126.6 (n_h in {11,12} mixed), E[d] = 40.726")
