#!/usr/bin/env python3
"""Fix + re-verify the conjugate-pair identities (round-3 structural checks).
For configs with integer marks (B, DFT over integer positions) and half-integer
marks (B_h, DFT over q+0.5):
    f(j) + f(256-j) = 2 (|B(j)|^2 + |B_h(j)|^2)              (j = 1..127)
    f(j) - f(256-j) = 4 Re( B(j) conj(B_h(j)) e^{pi i j/256} )
Also: locate the Re G(Delta) = 0 crossover precisely (documents a correction to
the (0.45,1) claim in regenerate-256law.md), and check the "asymmetry capacity"
of the int+half structure against the ramp requirement E[f(j)-f(N-j)] = 2j-256.
"""
import numpy as np

N = 256
j = np.arange(1, N + 1)

def cfg_spectrum(int_pos, int_marks, half_pos):
    z = np.zeros(N, dtype=complex)
    for p, m in zip(int_pos, int_marks):
        z += m * np.exp(2j * np.pi * j * p / N)
    for q in half_pos:
        z += np.exp(2j * np.pi * j * (q + 0.5) / N)
    return np.abs(z) ** 2

rng = np.random.default_rng(11)
n_h, n_i = 12, 244
half_pos = rng.choice(256, size=n_h, replace=False).tolist()
int_pos_all = [p for p in range(256) if p not in half_pos]
int_pos = rng.choice(int_pos_all, size=n_i, replace=False).tolist()
d = 41
int_marks = [2] * d + [1] * (n_i - d)
rng.shuffle(int_marks)

f = cfg_spectrum(int_pos, int_marks, half_pos)
B = sum(m * np.exp(2j * np.pi * j * p / N) for p, m in zip(int_pos, int_marks))
Bh = sum(np.exp(2j * np.pi * j * (q + 0.5) / N) for q in half_pos)

# CORRECT pairing: j = jj+1 pairs with N - j = 255 - jj  =>  index 254 - jj
err_sum = max(abs(f[jj] + f[254 - jj] - 2 * (abs(B[jj]) ** 2 + abs(Bh[jj]) ** 2)) for jj in range(127))
P = B * np.conj(Bh) * np.exp(1j * np.pi * j / N)
err_diff = max(abs(f[jj] - f[254 - jj] - 4 * np.real(P[jj])) for jj in range(127))
print("conjugate-pair identities (corrected pairing j <-> N-j):")
print(f"  max |f(j)+f(N-j) - 2(|B|^2+|Bh|^2)|          = {err_sum:.3e}")
print(f"  max |f(j)-f(N-j) - 4 Re(B conj(Bh) e^{{piij/N}})| = {err_diff:.3e}")

# ramp asymmetry requirement
print()
print("ramp requires E[f(j) - f(N-j)] = 2j - 256 ; int+half capacity |4 Re P| <= 4|B||Bh|")
for jj in [0, 10, 63, 126]:
    need = 2 * (jj + 1) - 256
    cap = 4 * abs(B[jj]) * abs(Bh[jj])
    print(f"  j={jj+1:3d}: need {need:7.1f}   capacity 4|B||Bh| = {cap:7.2f}   "
          f"|B|^2+|Bh|^2 = {abs(B[jj])**2 + abs(Bh[jj])**2:8.2f}")
print("  -> ramp at low j needs |B|^2 ~ |Bh|^2 ~ 64 with near-maximal phase alignment")

# Re G(Delta) crossover
print()
print("Re G(Delta) = Re sum_{j=1}^{256} exp(2 pi i j Delta / 256): locate the zero")
lo, hi = 0.45, 0.55
for _ in range(60):
    mid = (lo + hi) / 2
    G = np.sum(np.exp(2j * np.pi * j * mid / N))
    if G.real > 0:
        lo = mid
    else:
        hi = mid
print(f"  Re G(Delta) = 0 at Delta ~= {(lo+hi)/2:.6f}   (so < 0 on ({(lo+hi)/2:.4f}, 1), NOT (0.45,1))")
for d in [0.45, 0.499, 0.5, 0.501, 0.55, 0.9]:
    G = np.sum(np.exp(2j * np.pi * j * d / N))
    print(f"  Delta={d:.3f}: Re G = {G.real:+.5f}")
