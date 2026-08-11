#!/usr/bin/env python3
"""Probe the certificate kernel: for r=1-x, find configs maximizing
viol = c0 + sum_j (f_c(j)/256) r(j/256) - s_c/256  (validity violation).
Binding configs reveal the family structure."""
import numpy as np

N = 256
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
c0 = p0 - 10922.5/65536
j = np.arange(1, N+1)
r_j = 1 - j/N

def R_delta(d, N=256):
    """(1/N) sum_{j=1}^{N} r(j/N) e^{2 pi i j d / N}  (r(1)=0 so j=N term zero)."""
    jj = np.arange(1, N+1)
    return (1.0/N)*np.sum(r_j*np.exp(2j*np.pi*jj*d/N))

# R(Delta) for Delta = m/256 (grid) and some off-grid values
print("R(Delta) for Delta = m/256:")
for m in range(0, 20):
    print(f"  Delta={m}/256: R = {R_delta(m/N):+.6f}")
print("R for half-integer separations:")
for d in [0.5, 1.5, 2.5, 127.5, 128.5, 0.25, 0.75, 1.25]:
    print(f"  Delta={d}: R = {R_delta(d):+.6f}")

# Validity of r=1-x against configs: violation = c0 + sum (f/256) r - s/256
# For a config, sum_j (f_c(j)/256) r(j/256) = sum_{i,i'} m_i m_{i'} R(x_i - x_{i'})
def violation(xs, ms, c0=c0):
    """xs positions (real), ms marks; returns violation (>0 means violates certificate)."""
    viol = c0
    n = len(xs)
    for i in range(n):
        for ip in range(n):
            d = (xs[i] - xs[ip]) % N
            viol += ms[i]*ms[ip]*R_delta(d)
    viol -= sum(1 for m in ms if m == 1)/N
    return viol

# Lattice + k half-integer doubles: f(j) = (5-4cos(pi j/256))|B(j)|^2
# Direct: xs = integers with d removed + doubles at q+0.5
def lattice_doubles_half(d, seed=1):
    rng = np.random.default_rng(seed)
    qs = rng.choice(256, size=d, replace=False)
    xs = [q + 0.5 for q in qs] + [k for k in range(256) if k not in qs]
    ms = [2]*d + [1]*(256-d)
    return xs, ms

for d in (1, 2, 4, 8, 16, 32, 64):
    xs, ms = lattice_doubles_half(d)
    v = violation(xs, ms)
    print(f"lattice + {d} half-integer doubles: violation = {v:+.4f}")

# Lattice + integer doubles (u=0): f(j) = |B(j)|^2
def lattice_doubles_int(d, seed=1):
    rng = np.random.default_rng(seed)
    qs = rng.choice(256, size=d, replace=False)
    xs = [q for q in qs] + [k for k in range(256) if k not in qs]
    ms = [2]*d + [1]*(256-d)
    return xs, ms

for d in (1, 2, 8, 32, 64):
    xs, ms = lattice_doubles_int(d)
    v = violation(xs, ms)
    print(f"lattice + {d} integer doubles: violation = {v:+.4f}")

# What about half-integer SIMPLES (all points shifted)? Same as lattice.
# Try: lattice + d half-int doubles + e half-int SIMPLES (moved points)
def lattice_mixed(d, e, seed=2):
    rng = np.random.default_rng(seed)
    qs = rng.choice(256, size=d+e, replace=False)
    dqs = qs[:d]; eqs = qs[d:]
    xs = [q + 0.5 for q in dqs] + [q + 0.5 for q in eqs] + [k for k in range(256) if k not in qs]
    ms = [2]*d + [1]*e + [1]*(256-d-e)
    return xs, ms

for (d, e) in [(1, 0), (1, 1), (2, 1), (4, 2), (8, 4), (16, 8)]:
    xs, ms = lattice_mixed(d, e)
    v = violation(xs, ms)
    print(f"lattice + {d} half-int doubles + {e} half-int simples: violation = {v:+.4f}")
