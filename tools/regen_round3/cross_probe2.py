#!/usr/bin/env python3
"""Careful cross probe (fixed).  For 2-mark and small configs, measure
cross = sum_j f(j) - 256 sum m^2 as a function of the position separation.
Tests: (i) two marks at x and x+eps (distinct, eps tiny); (ii) int+half valid;
(iii) random distinct-position configs at various scales.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)

def cross_of(xs, ms):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m * np.exp(2j * np.pi * j * x / N)
    f = np.abs(z) ** 2
    return f.sum() - N * sum(m * m for m in ms)

print("two marks, positions (0, eps):")
for eps in [0.0, 1e-6, 1e-3, 0.01, 0.1, 0.25, 0.4, 0.49, 0.5, 0.6, 0.75, 1.0, 2.0, 10.0]:
    print(f"  eps={eps:8.4f}: cross = {cross_of([0.0, eps], [1, 1]):+12.4f}")

print()
print("two marks at (0, 0.5+eps):  (half-integer pair, small offset)")
for eps in [0.0, 1e-6, 1e-3, 0.01, 0.1, 0.25, 0.49]:
    print(f"  eps={eps:8.4f}: cross = {cross_of([0.0, 0.5 + eps], [1, 1]):+12.4f}")

print()
rng = np.random.default_rng(31)
# random distinct positions, various 'cluster radii': positions = base + u where u in [0, r)
for r in [1e-4, 1e-2, 0.1, 0.5, 1.0]:
    cv = []
    for _ in range(200):
        d = int(rng.integers(0, 30))
        s = N - 2 * d
        base = rng.choice(N, size=s + d, replace=False)
        u = rng.random(s + d) * r
        ms = [1] * s + [2] * d
        xs = [(b + uu) % N for b, uu in zip(base, u)]
        cv.append(cross_of(xs, ms))
    a = np.array(cv)
    print(f"random distinct, u in [0,{r:g}): min={a.min():+11.2f} max={a.max():+11.2f} mean={a.mean():+9.2f}")
