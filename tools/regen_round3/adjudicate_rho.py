#!/usr/bin/env python3
"""ADJUDICATION of rho_check.py's 'NECESSARY CONDITION FAILS' verdict.

rho_check.py computed  E[rho(Delta)] = (1/256) sum_j fbar(j) e^{-2 pi i j Delta/256}
and found Im != 0 (up to 40.74) at Delta = 1..255, concluding no mixture of marked
configs can realize the enclosure data (EnclOK refuted).

Claim under test: for a config with marks at positions x_i (NOT all integers),
f(j) = |sum_i m_i e^{2 pi i j x_i/256}|^2 is NOT the DFT of an integer-lattice
autocorrelation, so the 'rho real' condition is NOT necessary for off-grid configs.
The DFT-reality condition holds ONLY for all-integer configs (where f(N-j) = f(j)).

Decisive test: build a VALID off-grid config (marks {1,2}, sum m = 256, some marks at
half-integers) and compute its own DFT rho' = (1/256) sum_j f(j) e^{-2 pi i j Delta/256}.
If rho' has Im != 0 for a REAL valid config, the condition is not necessary and
rho_check's verdict is a false alarm for the off-grid family.

Also: confirm the all-integer config gives Im == 0 (the condition IS necessary there),
and confirm the recorded ramp fbar(j) = j (j<256) has f(1) != f(255) => cannot be
all-integer => the true family must be off-grid.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)


def spectrum(xs, ms):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m * np.exp(2j * np.pi * j * x / N)
    return np.abs(z) ** 2


def rho_of(f):
    """rho(Delta) = (1/256) sum_j f(j) e^{-2 pi i j Delta/256}, Delta = 0..255"""
    Delta = np.arange(0, N)
    rho = np.zeros(N, dtype=complex)
    for d in Delta:
        rho[d] = (1.0 / N) * np.sum(f * np.exp(-2j * np.pi * j * d / N))
    return rho


rng = np.random.default_rng(101)

print("=" * 72)
print("TEST 1: valid OFF-GRID config (12 half marks + int marks) - own DFT")
print("=" * 72)
n_h, d = 12, 41
s = N - n_h - 2 * d
int_pos = rng.choice(N, size=s + d, replace=False)
int_marks = np.array([1] * s + [2] * d, dtype=float)
rng.shuffle(int_marks)
half_q = rng.choice(N, size=n_h, replace=False)
xs = list(int_pos) + [q + 0.5 for q in half_q]
ms = list(int_marks) + [1] * n_h
assert sum(ms) == N
f = spectrum(xs, ms)
rho = rho_of(f)
print(f"  marks sum = {sum(ms)}  (valid)")
print(f"  max |Im rho(Delta)| = {np.max(np.abs(rho.imag)):.4f}")
print(f"  min Re rho = {rho.real.min():.4f}")
print(f"  f(1) = {f[0]:.4f}   f(255) = {f[254]:.4f}   (off-grid: f(1) != f(255))")
print("  => if max|Im| > 0: the 'rho real' condition FAILS on a VALID off-grid config,")
print("     so it is NOT a necessary condition for off-grid configs.")

print()
print("=" * 72)
print("TEST 2: valid ALL-INTEGER config - own DFT")
print("=" * 72)
d2 = 41
s2 = N - 2 * d2
int_pos2 = rng.choice(N, size=s2 + d2, replace=False)
int_marks2 = np.array([1] * s2 + [2] * d2, dtype=float)
rng.shuffle(int_marks2)
xs2 = list(int_pos2)
ms2 = list(int_marks2)
assert sum(ms2) == N
f2 = spectrum(xs2, ms2)
rho2 = rho_of(f2)
print(f"  max |Im rho(Delta)| = {np.max(np.abs(rho2.imag)):.2e}")
print(f"  min Re rho = {rho2.real.min():.4f}")
print("  => all-integer configs DO have real rho (Im ~ 1e-14 roundoff).")

print()
print("=" * 72)
print("TEST 3: the recorded ramp is not all-integer-realizable")
print("=" * 72)
fbar = np.arange(1, N + 1, dtype=float)
fbar[255] = 54126.59434047637
print(f"  fbar(1) = {fbar[0]:.1f}   fbar(255) = {fbar[254]:.1f}")
print(f"  all-integer configs satisfy f(j) = f(N-j);  ramp has f(1) != f(255)")
print(f"  => the true family must contain off-grid configs; the DFT-reality test")
print(f"     (which rho_check applied) is INAPPLICABLE to them.")
