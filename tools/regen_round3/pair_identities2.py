#!/usr/bin/env python3
"""Corrected conjugate-pair identities.
Config: marks at integer positions (values 1,2; DFT B) + n_h marks at half-integers
q+0.5.  Let C(j) = sum_{half marks} e^{2 pi i j q / N} (DFT of half marks' integer
parts), so the half contribution is e^{pi i j/N} C(j).
Then muhat(j) = B(j) + e^{pi i j/N} C(j) and
    f(j) + f(N-j) = 2 (|B|^2 + |C|^2)
    f(j) - f(N-j) = 4 Re( B conj(C) e^{-pi i j/N} )
The earlier script used B_h = e^{piij/N}C in place of C with a +phase: double error.
Also tests the complement-structured model (full lattice + holes H + doubles D,
half marks at the holes' positions):  B(j) = -H(j) + D(j),  C(j) = H(j).
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)

def spectra(int_pos, int_marks, half_q):
    """int marks at integer positions (val 1 or 2), half marks (val 1) at q+0.5."""
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_q:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    f = np.abs(z) ** 2
    B = sum(m * np.exp(2j * np.pi * j * p / N) for p, m in zip(int_pos, int_marks))
    C = sum(np.exp(2j * np.pi * j * q / N) for q in half_q)
    return f, B, C

rng = np.random.default_rng(3)
n_h, d = 12, 41
# complement-structured: full lattice, n_h holes (marks moved to half), d doubles
holes = rng.choice(256, size=n_h, replace=False).tolist()
int_pos = [p for p in range(256) if p not in holes]
int_marks = [2] * d + [1] * (len(int_pos) - d)
rng.shuffle(int_marks)
half_q = holes[:]  # half marks at the same integer parts as the holes (moved)
f, B, C = spectra(int_pos, int_marks, half_q)

err_sum = max(abs(f[jj] + f[254 - jj] - 2 * (abs(B[jj]) ** 2 + abs(C[jj]) ** 2)) for jj in range(127))
err_diff = max(abs(f[jj] - f[254 - jj] - 4 * np.real(B[jj] * np.conj(C[jj]) * np.exp(-1j * np.pi * (jj + 1) / N))) for jj in range(127))
print("corrected identities (B = int marks, C = half marks' int parts):")
print(f"  max |f(j)+f(N-j) - 2(|B|^2+|C|^2)|             = {err_sum:.3e}")
print(f"  max |f(j)-f(N-j) - 4 Re(B conj(C) e^{{-piij/N}})| = {err_diff:.3e}")

# capacity vs ramp requirement at low j, for the complement-structured config
print("\ncomplement-structured config (12 holes->half, 41 doubles):")
for jj in [0, 10, 63, 126, 254]:
    need = 2 * (jj + 1) - 256 if jj < 128 else 2 * (256 - (jj + 1)) - 256
    cap = 4 * abs(B[jj]) * abs(C[jj])
    print(f"  j={jj+1:3d}: asym need ~ {need:7.1f}   4|B||C| = {cap:8.2f}   "
          f"|B|^2+|C|^2 = {abs(B[jj])**2 + abs(C[jj])**2:8.2f}   f(j)={f[jj]:8.2f}")
print("  note: f(1)+f(255) must average 256; f(1)-f(255) must average -254")
