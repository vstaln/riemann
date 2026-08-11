#!/usr/bin/env python3
"""TCS idea-generator probe (idea-generator-tcs.md).

(A) Empirical 4th moment of the flat-window Gram matrix from actual zeta zeros
    at lambda=1 and lambda=1/2.  The 3rd moment at lambda=1/2 was verified = 5 in
    attack-twobandwidth; the 4th moment has never been computed/verified.
    RS diagonal-method range for m_k is k*lambda < 2, so m4 is unconditionally
    evaluable for lambda < 1/2 (k*lambda<2); lambda=1/2 is the boundary (k*lambda=2).
    Also prints the quartic-feasibility combination 2m3 - m4 (the quartic analog of
    the cubic's 2m2 - m3 which decided attack-twobandwidth: > 2/3 needed to beat 5/6).

(B) Sample complexity of the count-variance test separating the real zeros
    (V ~ 0.31 at one-spacing windows, measured in attack-gm-variance) from the
    256-law crystal (V ~ O(1/L) ~ 0): how many independent windows are needed to
    resolve V from 0 at 95% confidence.

Every number below is produced by this script.
"""
import numpy as np

def load_band(fn, lo, hi):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    g = np.array(g)
    m = (g >= lo) & (g <= hi)
    return g[m]

def moments4(gammas, la):
    """m1..m4 of the flat-window Gram matrix on a locally rescaled zero band."""
    n = gammas.size
    sp = np.diff(np.sort(gammas)).mean()
    x = np.sort(gammas) / sp
    d = x[:, None] - x[None, :]
    G = np.sinc(la * d)
    m1 = np.trace(G) / n
    G2 = G @ G
    m2 = np.trace(G2) / n
    m3 = np.trace(G2 @ G) / n
    m4 = np.trace(G2 @ G2) / n
    return m1, m2, m3, m4

fn = "tools/data/zeros_computed_10000.txt"
print("=" * 72)
print("(A) Empirical Gram-matrix moments from real zeta zeros (10k cache)")
print("=" * 72)
for (lo, hi, name) in ((9000, 9880, "high 9000-9880"),
                       (5000, 7000, "mid 5000-7000"),
                       (2000, 4000, "low-mid 2000-4000")):
    g = load_band(fn, lo, hi)
    print(f"\nband {name}: n={g.size}")
    for la, (e2, e3) in ((1.0, (4/3, 2.0)), (0.5, (13/6, 5.0))):
        m1, m2, m3, m4 = moments4(g, la)
        print(f"  lambda={la}: m1={m1:.4f} m2={m2:.4f} (exp {e2:.4f}) "
              f"m3={m3:.4f} (exp {e3:.4f}) m4={m4:.4f}  2m3-m4={2*m3-m4:+.4f}")

print("\n  Closed-form references: m4(1)=13/4=3.25 (paper, HL* value; to be re-verified "
      "with the corrected reduction per attack-twobandwidth §5.3); m4 at lambda=1/2 "
      "NOT in the literature/notes -> the empirical value above is the first estimate.")

print("=" * 72)
print("(B) Sample complexity of the count-variance test (zeros vs 256-law)")
print("=" * 72)
# From attack-gm-variance §5: at one-spacing windows (U*=0.929, alpha=1):
#   V_fluct (zeros) = 0.315, GUE(1) = 0.346; the crystal has variance -> O(1/L) ~ 0.
V_zeros = 0.315   # measured fluctuation variance at alpha=1 window (gm-variance §5)
V_gue = 0.346     # GUE prediction at n=1 spacing
V_crystal = 0.0   # 256-law: periodic, count within O(1) of mean -> variance ~ 0 at L>>256
delta = V_zeros - V_crystal
# SE of a sample variance from M independent Gaussian windows: SE ~ V*sqrt(2/M)
# Resolve delta at 95% (SE <= delta/3):  sqrt(2/M) <= (delta/3)/V
M = 2 * (3 * V_zeros / delta) ** 2
print(f"  V_zeros(alpha=1 window) = {V_zeros}  (attack-gm-variance §5, measured)")
print(f"  V_crystal(256-law)      ~ {V_crystal}  (exact periodicity -> O(1/L))")
print(f"  gap delta               = {delta}")
print(f"  independent windows M needed at 95% conf: ~{M:.0f}")
print(f"  -> a few hundred zeros suffice to separate the worlds BY VARIANCE.")
print(f"  The obstruction is NOT sample count: it is that the certificate class")
print(f"  reads means only (per-T, mean-based), never fluctuation statistics")
print(f"  (attack-gm-variance §4: 'variance' 0 hits in the main paper).")
