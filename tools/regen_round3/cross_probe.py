#!/usr/bin/env python3
"""Probe: is cross = sum_j f(j) - 256*sum m^2 ever POSITIVE for valid marked
configurations (marks {1,2}, sum m = 256, distinct positions)?

Test families:
  A. int marks + n_h half marks (valid, s+2d+nh=256)
  B. int marks + fractional marks at quarters/eighths/thirds (mixed parts)
  C. all marks at random fractional parts in [0,1)
  D. coincident positions (two marks at the same position)
For each, report min/max/mean cross.  This decides whether the recorded
E[cross] = +378.9 (forced by rows+p0+S(256)) is achievable by ANY config
family (in which case the int+half 'signature' model is simply wrong), or
whether cross <= 0 always (in which case the recorded data is internally
inconsistent under the marks{1,2} model -- a major finding).
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)

def cross_of(xs, ms):
    """xs: positions in [0,256) (may repeat), ms: marks. cross = sum_j f - N*sum m^2."""
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m * np.exp(2j * np.pi * j * x / N)
    f = np.abs(z) ** 2
    return f.sum() - N * sum(m * m for m in ms)

def valid_counts(n_h, d):
    s = N - n_h - 2 * d
    return s, d

rng = np.random.default_rng(23)

def report(name, vals):
    a = np.array(vals)
    print(f"{name:34s} min={a.min():10.2f}  max={a.max():10.2f}  mean={a.mean():9.2f}  n={len(a)}")

# A. int + half marks
cv = []
for _ in range(400):
    n_h = int(rng.integers(4, 60)); d = int(rng.integers(5, 60))
    s = N - n_h - 2 * d
    if s < 0: continue
    int_pos = rng.choice(N, size=s + d, replace=False)
    ms = [1] * s + [2] * d
    half_q = rng.choice(N, size=n_h, replace=False)
    xs = list(int_pos) + [q + 0.5 for q in half_q]
    cv.append(cross_of(xs, ms))
report("A. int + half marks", cv)

# B. mixed fractional parts (half, quarter, three-quarter, third, two-third)
cv = []
for _ in range(400):
    d = int(rng.integers(5, 60))
    parts = [0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 0.125, 0.375, 0.625, 0.875]
    # build marks: s + 2d + extra = 256; extra marks at fractional parts (mark 1)
    ne = int(rng.integers(0, 60))
    s = N - 2 * d - ne
    if s < 0: continue
    ms = [1] * s + [2] * d + [1] * ne
    npos = s + d + ne
    base = rng.choice(N, size=npos, replace=False)
    us = rng.choice(parts, size=npos)
    xs = [(b + u) % N for b, u in zip(base, us)]
    cv.append(cross_of(xs, ms))
report("B. mixed fractional parts", cv)

# C. all marks at random fractional parts in [0,1)
cv = []
for _ in range(400):
    d = int(rng.integers(5, 60))
    s = N - 2 * d
    ms = [1] * s + [2] * d
    npos = s + d
    base = rng.choice(N, size=npos, replace=False)
    us = rng.random(npos)
    xs = [(b + u) % N for b, u in zip(base, us)]
    cv.append(cross_of(xs, ms))
report("C. random fractional parts", cv)

# D. coincident positions (marks may share a position)
cv = []
for _ in range(400):
    d = int(rng.integers(5, 60))
    s = N - 2 * d
    ms = [1] * s + [2] * d
    npos = s + d
    # allow repeats: pick npos positions with replacement from half the range
    base = rng.integers(0, 200, size=npos)
    us = rng.choice([0.0, 0.5], size=npos)
    xs = [(b + u) % N for b, u in zip(base, us)]
    cv.append(cross_of(xs, ms))
report("D. coincident positions (repeats)", cv)

# E. the 'moved from lattice' family: full lattice minus m holes + m marks at half,
#    plus d doubles. cross measured.
cv = []
for _ in range(400):
    d = int(rng.integers(5, 60))
    mh = int(rng.integers(1, 40))
    # full lattice 256 marks, remove mh (making holes), add mh half marks,
    # then double d positions (need marks budget: 256 - mh + mh + d = 256+d -> no!
    # doubling adds marks. Instead: remove d marks to make budget for doubles.)
    holes = rng.choice(N, size=mh + d, replace=False)
    half_q = holes[:mh]
    dbl_q = holes[mh:]
    int_pos = [p for p in range(N) if p not in holes]
    ms = [1] * (len(int_pos) - d) + [2] * d
    xs = list(int_pos) + [q + 0.5 for q in half_q]
    assert sum(ms) + mh == N
    cv.append(cross_of(xs, ms))
report("E. lattice+moves+doubles", cv)

print()
print("recorded data requires E[cross] = +378.9  (rows fbar(j)=j, p0=0.6818286874, S(256)=211.4320)")
