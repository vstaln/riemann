#!/usr/bin/env python3
"""Probe: which configuration families are consistent with the certificate (r=1-x, c0=p0-10922.5/65536)?
For the primal LP's dual to attain value p0, there must be a certificate valid against EVERY family member:
    c0 + sum_j (f_c(j)/256)*(1 - j/256) <= s_c/256  for all c in the family.
If r=1-x violates a candidate config, that config is excluded from the family.
"""
import numpy as np
from itertools import combinations

N = 256
p0 = 10909258999421303588095230195816054408197 / (16000000000000000000000000000000000000000)
c0 = p0 - 10922.5 / 65536
print(f"p0 = {p0:.16f}, c0 = {c0:.16f}")

def check_validity(xs, ms):
    """xs: positions (int k + frac u), ms: marks. Returns (lhs - rhs) where validity needs <= 0."""
    # f(j) = |sum m exp(2pi i j x/256)|^2  for j=1..255
    s_c = sum(1 for m in ms if m == 1)
    lhs = c0
    for j in range(1, N):
        z = sum(m * np.exp(2j*np.pi*j*x/N) for x, m in zip(xs, ms))
        f = abs(z)**2
        lhs += (f / N) * (1 - j / N)
    rhs = s_c / N
    return lhs - rhs, s_c, lhs

# Family A: integer lattice, all 256 positions 0..255, some marks=2 (sum marks=256)
print("\n--- Family A: integer lattice, marks ---")
viol = 0
for d in [1, 2, 4, 8, 16, 32, 40, 64]:
    s = 256 - 2*d
    # double points at positions 0..d-1
    ms = [2]*d + [1]*(256-d)
    xs = list(range(256))
    val, sc, lhs = check_validity(xs, ms)
    print(f"  d={d:3d} s={sc:3d}: validity lhs-rhs = {val:+.4f}  {'VIOLATES' if val > 0 else 'ok'}")
    viol += (val > 0)
print(f"  -> {viol} of the tested lattice-mark configs VIOLATE the certificate r=1-x")

# Family B: half-integer lattice (x = k + 1/2), marks
print("\n--- Family B: half-integer lattice, marks ---")
for d in [1, 2, 8, 32, 64]:
    s = 256 - 2*d
    ms = [2]*d + [1]*(256-d)
    xs = [k + 0.5 for k in range(256)]
    val, sc, lhs = check_validity(xs, ms)
    print(f"  d={d:3d} s={sc:3d}: validity lhs-rhs = {val:+.4f}  {'VIOLATES' if val > 0 else 'ok'}")

# Family C: binary jitter (x = k + 0.5*b_k), all marks 1
print("\n--- Family C: binary jitter eps=1/2, all marks 1 ---")
rng = np.random.default_rng(0)
for trial in range(5):
    b = rng.integers(0, 2, N)
    xs = [k + 0.5*bb for k, bb in enumerate(b)]
    ms = [1]*N
    val, sc, lhs = check_validity(xs, ms)
    print(f"  random jitter #{trial}: validity lhs-rhs = {val:+.6f}  {'VIOLATES' if val > 0 else 'ok'}")

# Family D: single jittered point (lattice + one point moved by eps)
print("\n--- Family D: single jittered point, all marks 1 ---")
for eps in [0.25, 0.5, 1/3, 0.125, 0.75]:
    xs = list(range(N))
    xs[0] += eps
    ms = [1]*N
    val, sc, lhs = check_validity(xs, ms)
    print(f"  eps={eps:g}: validity lhs-rhs = {val:+.6f}  {'VIOLATES' if val > 0 else 'ok'}")

# Family E: TWO jittered points, all marks 1
print("\n--- Family E: two jittered points, all marks 1 ---")
for (i, j) in [(0, 1), (0, 2), (0, 128), (0, 64), (32, 96), (1, 129)]:
    xs = list(range(N))
    xs[i] += 0.5; xs[j] += 0.5
    ms = [1]*N
    val, sc, lhs = check_validity(xs, ms)
    print(f"  jitter {{0,{j}}}: validity lhs-rhs = {val:+.6f}  {'VIOLATES' if val > 0 else 'ok'}")
