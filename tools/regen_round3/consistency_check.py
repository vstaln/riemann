#!/usr/bin/env python3
"""Consistency of the recorded data {rows fbar(j)=j, p0, fbar(256)} against the
int+half config model.  Numerically verifies the per-config identities:
  (A) sum_{j=1..255}(|B|^2+|C|^2) = 512(d+n_h) - 2 n_h^2
  (B) sum_{j=1..255} 2Re(B conj(C) e^{-piij/N}) = cross + 2(256-n_h) n_h
      (cross = int<->half pair sum over S(x,x'), the off-grid excess)
  (C) f(256) = (256 - 2 n_h)^2  for int+half configs
then checks whether {rows, p0, fbar(256)} can be simultaneously satisfied.
"""
import numpy as np
import mpmath as mp

N = 256
j = np.arange(1, N + 1)

def config_terms(int_pos, int_marks, half_q):
    """returns (f, B, C, cross) for a config with int marks and half marks at q+0.5."""
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_q:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    f = np.abs(z) ** 2
    B = sum(m * np.exp(2j * np.pi * j * p / N) for p, m in zip(int_pos, int_marks))
    C = sum(np.exp(2j * np.pi * j * q / N) for q in half_q)
    # cross = sum_{i,i' diff frac} m m' S(x_i,x_i')  = sum_j f(j) - 256 sum m^2
    cross = f.sum() - N * (sum(m * m for m in int_marks) + len(half_q))
    return f, B, C, cross

rng = np.random.default_rng(17)
for (n_h, d) in [(12, 41), (12, 52), (26, 41)]:
    holes = rng.choice(256, size=n_h, replace=False).tolist()
    int_pos = [p for p in range(256) if p not in holes]
    int_marks = [2] * d + [1] * (len(int_pos) - d)
    rng.shuffle(int_marks)
    f, B, C, cross = config_terms(int_pos, int_marks, holes)
    S1 = sum(abs(B[jj]) ** 2 + abs(C[jj]) ** 2 for jj in range(255))          # j = 1..255
    S2 = sum(2 * np.real(B[jj] * np.conj(C[jj]) * np.exp(-1j * np.pi * (jj + 1) / N)) for jj in range(255))
    pred_A = 512 * (d + n_h) - 2 * n_h ** 2
    pred_B = cross + 2 * (256 - n_h) * n_h
    print(f"n_h={n_h} d={d}:")
    print(f"  (A) sum_{{-1..255}} (|B|^2+|C|^2) = {S1:10.3f}   pred 512(d+nh)-2nh^2 = {pred_A:10.3f}   diff {S1-pred_A:+.3f}")
    print(f"  (B) sum 2Re(B conj C e^-piij/N) = {S2:10.3f}   pred cross+2(256-nh)nh = {pred_B:10.3f}   diff {S2-pred_B:+.3f}")
    print(f"  (C) f(256) = {f[255]:10.2f}   (256-2nh)^2 = {(256-2*n_h)**2:10.2f}")
    print(f"  cross = {cross:9.3f}   sum_{{-1..255}} f(j) = {sum(f[jj] for jj in range(255)):10.3f}")
    print()

# ---- data-driven constraints ----
print("=" * 70)
print("DATA-DRIVEN CONSISTENCY (rows + p0 + fbar(256) all from LawN256.lean)")
print("=" * 70)
p0 = mp.mpf(10909258999421303588095230195816054408197) / mp.mpf(16000000000000000000000000000000000000000)
Ed = 128 * (1 - p0)                     # E[d] from p0 = 1 - E[d]/128
S256 = mp.mpf(294693210168748317632180492755635579620342098) / mp.mpf(2 ** 140)
fbar256 = 256 * S256
print(f"  E[d] from p0            = {mp.nstr(Ed, 15)}")
print(f"  fbar(256) = 256*S(256)  = {mp.nstr(fbar256, 20)}")
print(f"  sum_{{-1..255}} fbar(j) = 32640 (ramp rows)")
print(f"  required E[cross]       = 32640 + fbar256 - 256*(256 + 2*Ed)  "
      f"= {mp.nstr(32640 + fbar256 - 256 * (256 + 2 * Ed), 12)}")

# For int+half configs with all n_h equal (say), the row-sum identity:
# sum_{j<=255} E[f(j)] = E[512(d+n_h) - 2 n_h^2] + E[cross] + 2(256-n_h)n_h
# with E[d] = 40.726 fixed and E[cross] fixed by data => solve for n_h
import sympy as sp
nh = sp.symbols('nh')
Edv = float(Ed)
Ecross = float(32640 + fbar256 - 256 * (256 + 2 * Edv))
eq = sp.Eq(512 * (Edv + nh) - 2 * nh ** 2 + Ecross + 2 * (256 - nh) * nh, 32640)
sols = sp.solve(eq, nh)
print(f"\n  solve for n_h (all configs int+half, common n_h):")
for s in sols:
    print(f"    n_h = {sp.N(s, 8)}")
f256_probe = 54126.6
for s in sols:
    sv = complex(sp.N(s))
    if abs(sv.imag) < 1e-6:
        nhv = sv.real
        print(f"    -> with n_h = {nhv:.2f}: f(256) = (256-2n_h)^2 = {(256-2*nhv)**2:.1f} "
              f"vs recorded fbar(256) = {float(fbar256):.1f}")
