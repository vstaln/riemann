#!/usr/bin/env python3
"""NEW SEED IDEA verification: balanced fractional clusters with POSITIVE cross.

The recorded data (ramp rows fbar(j)=j, p0=0.6818286874, fbar(256)=54126.59)
forces the law to satisfy  E[cross] + 512*E[d] = 21230.594  (derived: cross =
sum_j f(j) - 256*sum m^2, and sum_j fbar = 32640 + 54126.59; p0 gives
E[s]+2E[d]+E[n_frac] = 256, so E[sum m^2] = 256+2E[d]).

For pure int+half configs (n_frac = 0): cross = -2(256-n_h)*n_h < 0, so
E[cross] < 0 and p0 = 1 - E[d]/128 in [0.587, 0.594] -- CONTRADICTS the
recorded p0 = 0.6818286874.  Hence the family MUST contain configs with
positive cross.  Every prior-agent family (half, quarter, eighth, third,
coincident, random fractional) had cross <= 0.

Candidate: balanced fractional clusters whose sum of e^{2 pi i x} = 0 (so
f(256) keeps the perfect-square form (256-2n_h)^2) but whose internal
separations lie in (0, 1/2) (positive cross).  E.g. the quartet at
q + {1/8, 3/8, 5/8, 7/8}: e-sum = 0; internal separations 1/4 (x3), 1/2 (x2),
3/4 (x1).

This script MEASURES cross and f(256)-contribution for several clusters.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)


def Ssum(delta):
    """S(0, delta) = sum_{j=1}^{256} e^{2 pi i j delta / 256}."""
    return np.sum(np.exp(2j * np.pi * j * delta / N))


def cross_of(xs, ms):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m * np.exp(2j * np.pi * j * x / N)
    f = np.abs(z) ** 2
    return f.sum() - N * sum(m * m for m in ms), f


def cluster_test(name, fracs, q=0):
    """marks 1 at q+u for each u in fracs. Returns cross, f(256) contribution, e-sum."""
    xs = [q + u for u in fracs]
    ms = [1] * len(fracs)
    cross, f = cross_of(xs, ms)
    esum = sum(np.exp(2j * np.pi * x / N * N) for x in xs)  # e^{2 pi i x}, x = frac
    esum = sum(np.exp(2j * np.pi * u) for u in fracs)
    f256 = abs(esum) ** 2
    print(f"  {name:44s} cross={cross:+10.2f}  f(256)contrib={f256:8.2f}  e-sum={esum:+.4f}")

print("=" * 74)
print("BALANCED / NEAR-CLUSTER FRACTIONAL MARK GROUPS (single-group cross)")
print("=" * 74)
cluster_test("pair {0.25, 0.75} (sep 1/2)", [0.25, 0.75])
cluster_test("pair {0.1, 0.9} (sep 0.2)", [0.1, 0.9])
cluster_test("pair {0.4, 0.6} (sep 0.2)", [0.4, 0.6])
cluster_test("pair {0.05, 0.45} (sep 0.4)", [0.05, 0.45])
cluster_test("pair {0.2, 0.8} (sep 0.4)", [0.2, 0.8])
cluster_test("quartet {1/8,3/8,5/8,7/8}", [0.125, 0.375, 0.625, 0.875])
cluster_test("quartet {1/8,3/8,5/8,7/8} shifted", [0.125, 0.375, 0.625, 0.875])
cluster_test("triplet {1/3, 2/3, 1}", [1 / 3, 2 / 3, 1.0])
cluster_test("sextet {1/12..11/12 odd}", [1 / 12, 3 / 12, 5 / 12, 7 / 12, 9 / 12, 11 / 12])
cluster_test("3-pair {0.05,0.95},{0.4,0.6},{0.2,0.8}", [0.05, 0.95, 0.4, 0.6, 0.2, 0.8])

print()
print("=" * 74)
print("FULL CONFIG test: 244 int marks (162 s + 41 d) + 12 half + 1 quartet")
print("=" * 74)
rng = np.random.default_rng(4)
n_h, d, k = 12, 41, 1
s = N - n_h - 4 * k - 2 * d
assert s >= 0, s
int_pos = rng.choice(N, size=s + d, replace=False)
int_marks = np.array([1] * s + [2] * d, dtype=float)
rng.shuffle(int_marks)
half_q = rng.choice(N, size=n_h, replace=False).tolist()
q = int(rng.integers(0, N))
xs = list(int_pos) + [q + u for u in [0.125, 0.375, 0.625, 0.875]]
ms = list(int_marks) + [1] * (n_h + 4)
assert sum(ms) == N, sum(ms)
cross, f = cross_of(xs, ms)
print(f"  marks sum = {sum(ms)}  (valid)")
print(f"  cross = {cross:+.2f}   f(256) = {f[255]:.2f}   (target (256-2*12)^2 = 53824)")
print(f"  sum_{{1..255}} f = {f[:255].sum():.2f}")

print()
print("  DATA: E[cross] + 512*E[d] = 21230.594;  recorded p0 = 0.6818287")
print("  one quartet per config: E[n_frac]=4 => E[d] = (81.452-4)/2 = 38.73,")
print("  so E[cross] = 21230.594 - 512*38.73 = +1402.9 (a few quartets reach +378.9)")
