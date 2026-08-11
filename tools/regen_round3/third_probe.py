#!/usr/bin/env python3
"""Test the concrete family hypothesis:
  int marks + n_h half marks + k balanced (1/3, 2/3) pairs.
A (1/3,2/3) pair (marks 1,1 at p+1/3, p+2/3): sin cancels, cos sums to -1,
so f(256) = (256 - 2 n_h - k)^2 (perfect square when 2 n_h + k even-ish).
Separation 1/3 => POSITIVE cross contribution.
Checks: f(256), cross sign, sum_{1..255} f vs the data targets.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int
u13, u23 = 1 / 3, 2 / 3
DFT_13 = np.exp(2j * np.pi * j * u13 / N)[:, None] * DFT_int
DFT_23 = np.exp(2j * np.pi * j * u23 / N)[:, None] * DFT_int

def measure(n_h, d, k, seed):
    rng = np.random.default_rng(seed)
    s = N - n_h - 2 * k - 2 * d
    assert s >= 0, s
    int_pos = rng.choice(N, size=s + d, replace=False)
    int_marks = np.array([1] * s + [2] * d, dtype=float)
    rng.shuffle(int_marks)
    half_q = rng.choice(N, size=n_h, replace=False)
    q13 = rng.choice(N, size=k, replace=False)
    q23 = rng.choice(N, size=k, replace=False)
    z = DFT_int[:, int_pos] @ int_marks
    z = z + DFT_half[:, half_q].sum(axis=1)
    z = z + DFT_13[:, q13].sum(axis=1) + DFT_23[:, q23].sum(axis=1)
    f = np.abs(z) ** 2
    sum_m2 = s + 4 * d + n_h + 2 * k
    cross = f.sum() - N * sum_m2
    return dict(sum255=f[:255].sum(), f256=f[255], cross=cross)

print(f"{'n_h':>4} {'d':>4} {'k':>3} {'sum255':>10} {'f(256)':>10} {'(256-2nh-k)^2':>13} {'cross':>10}")
for (nh, d, k) in [(11, 41, 2), (12, 41, 0), (11, 41, 1), (12, 40, 0), (11, 41, 2), (10, 41, 4), (11, 42, 2)]:
    r = measure(nh, d, k, 11)
    print(f"{nh:>4} {d:>4} {k:>3} {r['sum255']:>10.1f} {r['f256']:>10.1f} {(256-2*nh-k)**2:>13} {r['cross']:>10.1f}")
print()
print("DATA: E[sum255] = 32640, E[f(256)] = 54126.6, E[d] = 40.726, E[cross] = +378.9")
