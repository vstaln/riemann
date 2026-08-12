#!/usr/bin/env python3
"""Single-config coherence probe: can ONE marked config approach the ramp
f(j)=j (j=1..255)?

Derived capacity bounds (from pair identities, verified numerically):
  ramp needs f(1)+f(255) = 256 and f(1)-f(255) = -254.
  For int+half config: f(j)+f(N-j) = 2(|B(j)|^2+|C(j)|^2), so at j=1:
    |B(1)|^2 + |C(1)|^2 = 128.
  f(1)-f(255) = 4 Re(B(1) conj(C(1)) e^{-pi i/256})  needs -254
    => |B(1)||C(1)| >= 63.5 with near-antiphase.
  Max |B||C| given |B|^2+|C|^2 = 128 is 64 (at |B|=|C|=8).
  => the half marks must have coherence |C(1)| ~ 8 and the int marks
     |B(1)| ~ 8 with the right phase.  Random families give |C(1)|~sqrt(12)
     and small |B(1)|, hence the stuck Chebyshev distance ~86.

Here we HAND-BUILD configs with controlled coherence and measure the sup
distance of a single config to the ramp, to see if the ramp is in reach.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)


def spectrum(int_pos, int_marks, half_q):
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_q:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    return np.abs(z) ** 2


def supdist(f):
    return np.max(np.abs(f[:255] - np.arange(1, 256)))


def report(name, int_pos, int_marks, half_q):
    f = spectrum(int_pos, int_marks, half_q)
    d = supdist(f)
    w = np.argsort(-np.abs(f[:255] - np.arange(1, 256)))[:5]
    worst = [(int(ww + 1), round(float(f[ww] - (ww + 1)), 2)) for ww in w]
    print(f"{name:34s} sup={d:9.2f}  worst={worst}  f(1)={f[0]:8.2f} f(255)={f[254]:8.2f}  sum255={f[:255].sum():8.0f}")

rng = np.random.default_rng(9)

# Baseline: random int+half (prior families)
n_h, d = 12, 41
s = N - n_h - 2 * d
int_pos = rng.choice(N, size=s + d, replace=False)
int_marks = np.array([1] * s + [2] * d, dtype=float)
rng.shuffle(int_marks)
half_q = rng.choice(N, size=n_h, replace=False)
report("baseline random int+half", int_pos, int_marks, half_q)

# 1. tight half cluster: 12 half marks at q, q+1, ..., q+11 (half-integers)
for q0 in [0, 37, 100, 200]:
    hq = [(q0 + ell) % N for ell in range(12)]
    report(f"tight 12-cluster q0={q0}", int_pos, int_marks, hq)

# 2. partial coherence: two clusters of 6 (q and q+128)
for q0 in [0, 64, 128]:
    hq = [(q0 + ell) % N for ell in range(6)] + [(q0 + 128 + ell) % N for ell in range(6)]
    report(f"2x6 clusters q0={q0}", int_pos, int_marks, hq)

# 3. exact AP with step 22 (wraps to give |C(1)|~8): half marks at q + 22*ell
for step in [21, 22, 23, 43]:
    hq = [(q0 := 0) + (step * ell) % N for ell in range(12)]
    report(f"AP step={step}", int_pos, int_marks, hq)

# 4. also vary d and n_h for the tight cluster
for (nh2, d2) in [(8, 41), (10, 41), (12, 41)]:
    s2 = N - nh2 - 2 * d2
    ip2 = rng.choice(N, size=s2 + d2, replace=False)
    im2 = np.array([1] * s2 + [2] * d2, dtype=float)
    rng.shuffle(im2)
    hq2 = [(37 + ell) % N for ell in range(nh2)]
    report(f"tight {nh2}-cluster d={d2}", ip2, im2, hq2)

print()
print("NOTE: single configs can't hit the ramp pointwise (sup ~>100);")
print("the LP mixes configs. This probe shows the SPECTRUM SHAPES available.")
