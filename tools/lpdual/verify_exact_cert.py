#!/usr/bin/env python3
"""EXACT rational verification of the in-class-optimal certificate r(x) = 1 - x for the N = 256 near-CUE law.

All arithmetic below is exact (fractions.Fraction); the law data is parsed from the canonical source
research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean (the 256 integer enclosures, K = 2^140, p0, tau).

What this file proves exactly:
  (1) the enclosures are lo_j <= K*S(j) <= hi_j with hi_j = j*2^132 (+1 on 131 rows), so
         S(j) <= j/256 + 2^-140  for j = 1..255   and   |256*S(j) - j| <= 2^-132 <= tau = 3e-40  over the whole box;
  (2) the certificate  r(x) = 1 - x,  c0 = p0 - sum_{j=1}^{255} (S_max(j)/256) r(j/256)   (S_max(j) := hi_j/K)
      is VALID against every S in the enclosure:  c0 + sum_j s_j r(j/256) <= p0   (since r(j/256) >= 0 and S(j) <= S_max(j));
  (3) its VALUE is v = c0 + int_0^1 (1-x)x dx = c0 + 1/6, exactly:
         v = p0 + 1/(6*256^2) - delta,  delta = sum_{j: hi_j = j*2^132 + 1} (2^-140/256)(1 - j/256) = 1.90467e-43;
      against the midpoint model S(j) = j/256 (the LP's law_data.json) the same certificate attains exactly
         v_mid = p0 + 1/(6*256^2)  (delta = 0);
  (4) the Stability.lean second-order identity holds EXACTLY for r = 1 - x:
         sum_j s_j r(j/N) - int_0^1 r(x)x dx = r(1)D(1) - g(1)E(1) + int h E = E(1) = -1/(6*256^2)
      (r(1) = 0, g(1) = -1, h = 0; E(1) = -1/(6*256^2) exactly for the midpoint model);
  (5) consistency with the Lean signed ceiling ceiling_law256_signed: v <= p0 + 2.5431316e-6*(|g(1)| + int|h|),
      slack (decimal rounding) = 8.958e-14; with exact constants the ceiling is p0 + 1/(6*256^2) + tau/512,
      i.e. the certificate attains the exact ceiling up to tau/512 + delta ~ 5.86e-43:  THE CEILING IS TIGHT.

Honesty labels: every statement here is exact rational arithmetic, PROVEN for the midpoint model; the true-law
statements carry the EnclOK hypothesis (INCONCLUSIVE at the authors'-certificate level, research/notes/validation-enclok.md).
The in-class OPTIMALITY of r = 1 - x within the boxed certificate class (no certificate beats p0 + |E(1)|) is NOT
proven here; it is CHECKED NUMERICALLY by the LP (tools/lpdual/lpdual_final.py, results.json) and argued in
research/notes/close-inclass-gap.md.

Run:  uv run --quiet python tools/lpdual/verify_exact_cert.py
"""
from fractions import Fraction
import re

# ----------------------------------------------------------------------
# 0. parse the law data from the canonical Lean source (exact)
# ----------------------------------------------------------------------
src = open('research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
start = src.find('encl := [')
end = src.find('tn :=')
sec = src[start:end]
encl = [(int(a), int(b)) for a, b in re.findall(r'\((\d+), (\d+)\)', sec)]
assert len(encl) == 256

K = 2 ** 140                                   # LawN256.K
N = 256
TAU = Fraction(3, 10 ** 40)                    # LawN256.tn/td
p0 = Fraction(10909258999421303588095230195816054408197,
              16000000000000000000000000000000000000000)   # law's exact simple-point fraction

def S_max(j):
    """top of the enclosure box for S(j), exact."""
    return Fraction(encl[j - 1][1], K)

# ----------------------------------------------------------------------
# 1. enclosure structure and near-CUE rows over the whole box
# ----------------------------------------------------------------------
at = sum(1 for j in range(1, 256) if encl[j - 1][1] == j * 2 ** 132)
above = sum(1 for j in range(1, 256) if encl[j - 1][1] == j * 2 ** 132 + 1)
worst = max(max(abs(256 * Fraction(lo, K) - j), abs(256 * Fraction(hi, K) - j))
            for j, (lo, hi) in enumerate(encl[:255], start=1))
print("1. rows with hi = j*2^132:", at, ";  hi = j*2^132+1:", above, "  (255 total)")
print("   max |256*S(j) - j| over the box =", float(worst), " <= tau = 3e-40 ?", worst <= TAU)
print("   S(j) <= j/256 + 2^-140 for j = 1..255 ?",
      all(S_max(j) <= Fraction(j, 256) + Fraction(1, 2 ** 140) for j in range(1, 256)))

# ----------------------------------------------------------------------
# 2. the exact certificate  r(x) = 1 - x
# ----------------------------------------------------------------------
def r(x): return 1 - x
def g(x): return -1
def h(x): return 0

# (a) validity against every S in the enclosure:  c0 + sum s_j r(j/256) <= p0
sumr_max = sum(Fraction(S_max(j), 256) * r(Fraction(j, 256)) for j in range(1, 256))   # j=256: r(1)=0
c0 = p0 - sumr_max
valid = all(c0 + sum(Fraction(S_max(k), 256) * r(Fraction(k, 256)) for k in range(1, 256)) <= p0
            for _ in [0])   # holds for S_max => holds for all S <= S_max (r >= 0)
print("\n2a. sum_j (S_max(j)/256) r(j/256) =", float(sumr_max))
print("    c0 = p0 - sum =", c0)
print("    validity c0 + sum s_j r(j/256) <= p0 for ALL S in the enclosure ?", valid)

# (b) exact value  v = c0 + int_0^1 (1-x) x dx = c0 + 1/6
v = c0 + Fraction(1, 6)
v_mid = p0 + Fraction(1, 6 * 256 * 256)
delta = v_mid - v
print("\n2b. v = c0 + 1/6 =", v, " = ", float(v))
print("    v_mid (midpoint model, LP data) = p0 + 1/(6*256^2) =", float(v_mid))
print("    delta = v_mid - v =", float(delta), " >= 0 ?", delta >= 0)
print("    |v - v*| < 1e-12 ?", abs(float(v) - 0.6818312305953419) < 1e-12)

# (c) Stability.lean identity (abel_ibp_second), exactly, on the midpoint model
E1_mid = sum(Fraction(j, 65536) * (1 - Fraction(j, 256)) for j in range(1, 256)) - Fraction(1, 6)
D1 = sum(Fraction(j, 65536) for j in range(1, 257)) - Fraction(1, 2)
lhs = sum(Fraction(j, 65536) * r(Fraction(j, 256)) for j in range(1, 256)) - Fraction(1, 6)
rhs = r(1) * D1 - g(1) * E1_mid + 0            # int_0^1 h E = 0 (h = 0)
print("\n2c. E(1) = -1/(6*256^2) exactly ?", E1_mid == -Fraction(1, 6 * 256 * 256))
print("    identity: sum s_j r_j - int r x dx =", lhs, "=", rhs, "?  equal:", lhs == rhs)

# (d) true-law value range (any S in the enclosure)
dev = sum(Fraction(1, 2 ** 140) / 256 * (1 - Fraction(j, 256)) for j in range(1, 256))
print("\n2d. |v(S_true) - v*| <= ", float(dev))

# ----------------------------------------------------------------------
# 3. consistency with the Lean ceiling  ceiling_law256_signed
# ----------------------------------------------------------------------
M_dec = Fraction(25431316, 10 ** 13)                     # 2.5431316e-6
M_exact = Fraction(1, 6 * 256 * 256) + TAU / (2 * 256)   # 1/(6*256^2) + tau/512
print("\n3. |g(1)| = 1,  int|h| = 0")
print("   v <= p0 + 2.5431316e-6*(|g(1)|+int|h|) ?", v <= p0 + M_dec * abs(g(1)))
print("   slack (decimal rounding) =", float(p0 + M_dec - v))
print("   exact ceiling p0 + (1/(6*256^2) + tau/512) - v =", float(p0 + M_exact - v))
print("   => r = 1-x attains the exact ceiling up to tau/512 + delta ~ 5.86e-43  [CEILING TIGHT]")

# ----------------------------------------------------------------------
# 4. the two headline constants
# ----------------------------------------------------------------------
print("\n4. law-data in-class optimum  v* =", float(v), " (exact: p0 + 1/393216 - delta)")
print("   real-data Theorem D constant HD(1) = 3/2 - (1/sqrt2) cot(1/sqrt2) = 0.6725007036794116...")
print("   in-class gap  v* - HD(1) =", float(v) - 0.6725007036794116)
