#!/usr/bin/env python3
"""Precise cross-accounting for the recorded law under the int+half signature.

Identity (measured in consistency_check2): for a valid int+half config,
  cross = sum_{j=1}^{256} f(j) - 256*sum m^2 = -2*(256-n_h)*n_h
because each int<->half pair contributes 2*Re[S(half-integer)] = -2.

But wait: this ignores PAIRS WITHIN the int class at DIFFERENT integer positions
(S = 0) and pairs within the half class (S = 0) -- correct.  It also ignores the
diagonal (S(0)=256).  So for int+half distinct configs cross is exactly negative.

Now with balanced clusters (e-sum = 0, so f(256) unchanged):
  cross = base_cross + cluster_cross
  base_cross = -2*(256 - n_h - 4k)*n_h   (n_h half marks, 4k quartet marks)
  cluster_cross = +861.2 per quartet  (measured)
This script recomputes the REQUIRED E[cross] from the data (rows + p0 + S(256))
under various assumptions about fractional-mark structure, to pin the target.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
N = 256
K = 2 ** 140

p0 = mp.mpf(10909258999421303588095230195816054408197) / mp.mpf(16000000000000000000000000000000000000000)
S256 = mp.mpf(294693210168748317632180492755635579620342098) / mp.mpf(2 ** 140)
fbar256 = 256 * S256
Esum_f = 32640 + fbar256          # sum_{j=1}^{256} E[f(j)] = rows(32640) + f(256)
print("DATA (from LawN256.lean):")
print(f"  p0 = {mp.nstr(p0, 20)}   -> E[s] = {mp.nstr(256*p0, 10)}")
print(f"  fbar(256) = {mp.nstr(fbar256, 20)}")
print(f"  E[sum_j f(j)] = {mp.nstr(Esum_f, 20)}")
print()

# mark budget: E[s] + 2E[d] + E[n_frac] = 256  (n_frac = number of fractional mark-1 marks)
Es = 256 * p0
print("Required E[cross] under different fractional structures:")
for (label, En_frac, Efrac_marks) in [
    ("all-integer (n_frac=0)", 0, 0),
    ("12 half marks", 12, 12),
    ("12 half + 4 quartet", 16, 16),
    ("12 half + 8 quartet", 20, 20),
    ("12 half + 12 quartet", 24, 24),
]:
    # E[s] counts ALL mark-1 marks (int simples + fractional).  Int simples s_i:
    # s_i = E[s] - E[n_frac]  (fractional marks are mark-1).  E[d] from budget:
    Ed = (N - Es - En_frac) / 2
    # sum m^2 = s_i + 4*Ed + n_frac*1 (fractional marks mark-1)
    Esumm2 = (Es - En_frac) + 4 * Ed + En_frac
    # E[cross] = E[sum f] - 256*E[sum m^2]
    Ecross = Esum_f - 256 * Esumm2
    print(f"  {label:26s}: E[n_frac]={En_frac:3d}  E[d]={float(Ed):8.3f}  "
          f"E[sum m^2]={float(Esumm2):9.3f}  ->  E[cross] = {float(Ecross):+10.1f}")

print()
print("Cross from int+half structure alone (all configs int+half, distinct):")
for nh in [11, 12]:
    print(f"  n_h={nh:2d}: base cross = -2*(256-{nh})*{nh} = {-2*(256-nh)*nh}")
print()
print("=> int+half distinct CANNOT give positive cross.  Need balanced clusters:")
print("   quartet {1/8,3/8,5/8,7/8}: cross = +861.2, e-sum = 0 (f(256) unchanged).")
print("   with 12 half marks:  base = -2*(256-12-4k)*12;  + k*861.2")
for k in [0, 1, 2, 3, 4]:
    base = -2 * (256 - 12 - 4 * k) * 12
    print(f"     k={k} quartets: base={base:+7d}  +{k}*861.2 = {base + k*861.2:+9.1f}")
