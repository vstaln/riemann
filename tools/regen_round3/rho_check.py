#!/usr/bin/env python3
"""DECISIVE NECESSARY CONDITION: the law's expected pair-correlation.

For ANY law = weighted mixture of marked configs (marks {1,2}, sum m = 256),
the expected autocorrelation
    E[rho(Delta)] = (1/256) sum_{j=1}^{256} fbar(j) e^{-2 pi i j Delta / 256}
must be REAL and >= 0 for every integer Delta = 0..255, because
rho(Delta) = sum_{i,i': x_i - x_i' == Delta mod 256} m_i m_i' >= 0 per config.

Here fbar(j) = 256*S(j) is pinned by the enclosures: fbar(j) = j for j<256,
fbar(256) = 256*S(256) in [54126.5943404763675, +2^-132].

If E[rho(Delta)] < 0 (or has nonzero imaginary part) for any Delta, then NO
mixture of marked configurations can realize the recorded enclosure data --
EnclOK would be REFUTED (a huge finding).  If it's real and >= 0 everywhere,
the data passes this necessary condition (and the constraint profile of rho*
is a precise family-design target for route 2).
"""
import re
import numpy as np

N = 256
K = 2 ** 140
src = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
encl = [(int(a), int(b)) for a, b in re.findall(r'\((\d+), (\d+)\)',
        re.search(r'encl := \[(.*?)\]', src, re.S).group(1))]

# fbar(j) = 256*S(j): use enclosure MIDPOINT per row
lo = np.array([e[0] for e in encl], dtype=float)
hi = np.array([e[1] for e in encl], dtype=float)
mid = (lo + hi) / 2.0 / float(K)          # S(j)
fbar = 256.0 * mid                        # ~ j for j<256, ~54126.6 for j=256
print("fbar(1..5)   =", np.round(fbar[:5], 6))
print("fbar(256)    =", fbar[255])

Delta = np.arange(0, 256)
jj = np.arange(1, N + 1)
rho = np.zeros(256, dtype=complex)
for d in Delta:
    rho[d] = (1.0 / N) * np.sum(fbar * np.exp(-2j * np.pi * jj * d / N))

print()
print("E[rho(Delta)] = (1/256) sum_j fbar(j) e^{-2 pi i j Delta / 256}:")
neg = []
for d in Delta:
    r = rho[d]
    print(f"  Delta={d:3d}: Re = {r.real:+12.4f}   Im = {r.imag:+10.4f}   {'NEGATIVE!' if r.real < -1e-6 else ''}")
    if r.real < -1e-6:
        neg.append(d)
print()
print(f"rows with Re < -1e-6: {neg}")
print(f"max |Im| = {np.max(np.abs(rho.imag)):.6f}")
if not neg and np.max(np.abs(rho.imag)) < 1e-4:
    print("=> NECESSARY CONDITION PASSES: E[rho] real and >= 0 everywhere.")
    print("   (the data survives; rho* is a valid target pair-correlation profile)")
else:
    print("=> NECESSARY CONDITION FAILS: see rows above.")
