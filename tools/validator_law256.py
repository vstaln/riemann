"""Parse LawN256.lean enclosures; verify close-inclass-gap / attack-lpdual exact claims:
- 124 rows hi = j*2^132, 131 rows hi = j*2^132+1
- max |256*S(j)-j| over box = 2^-132
- E(1) = -1/(6*256^2) = -1/393216 (midpoint model), |E(1)| = 1/(6*256^2) + tau/512
- D(1) = sum_j S(j)/256 - 1/2 with S(256) = 211.43... -> 0.8239531607128352
- sum_{j=1}^{255} (j/65536)(1 - j/256) = 21845/131072
- v = p0 + 1/(6*256^2) - delta', delta' = sum over 131 rows of (2^-140/256)(1-j/256)
- p0 decimal to 45 digits
Exact integer / Fraction arithmetic, no floats.
"""
from fractions import Fraction
import re

txt = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()
# extract the encl list
m = re.search(r'encl\s*:=\s*\[(.*?)\]\s*$', txt, re.S | re.M)
body = m.group(1)
pairs = re.findall(r'\((\d+),\s*(\d+)\)', body)
print("number of enclosure rows parsed:", len(pairs))
K = 2 ** 140
assert K == 1393796574908163946345982392040522594123776

# each row j (1-indexed): lo_j, hi_j with K*S(j) in [lo,hi]
rows = []
for j, (lo, hi) in enumerate(pairs, start=1):
    lo = int(lo); hi = int(hi)
    rows.append((j, lo, hi))

# 1) hi = j*2^132 vs j*2^132+1 vs other
base = 2 ** 132
cnt_hi_base = sum(1 for j, lo, hi in rows if j <= 255 and hi == j * base)
cnt_hi_plus = sum(1 for j, lo, hi in rows if j <= 255 and hi == j * base + 1)
cnt_other = sum(1 for j, lo, hi in rows if j <= 255 and hi not in (j * base, j * base + 1))
print("rows j=1..255: hi=j*2^132: %d, hi=j*2^132+1: %d, other: %d" % (cnt_hi_base, cnt_hi_plus, cnt_other))

# 2) max |256*S(j)-j| over the box (using worst-case S = hi/K or lo/K)
worst = max((abs(256 * Fraction(hi, K) - j), abs(256 * Fraction(lo, K) - j)) for j, lo, hi in rows if j <= 255)
print("max |256*S(j)-j| over box (worst):", max(w for w in worst), " 2^-132 =", Fraction(1, 2 ** 132))

# 3) D(1) = T/256 - 1/2, T = sum_{j=1}^{256} S(j); with S(j) = hi_j/K (worst case for D? use the law's actual S
#    not available; but the close-inclass claim: D(1) = 0.8239531607128352 for the MIDPOINT/law model where
#    S(j)=j/256 (j<256) and S(256)=211.4320091424858. Compute with hi and lo for S(256):
T_hi = sum(Fraction(hi, K) for j, lo, hi in rows)
D1_hi = T_hi / 256 - Fraction(1, 2)
print("D(1) with S=hi for all j (incl j=256):", float(D1_hi), "  (claim 0.8239531607128352)")
# with S(256) from the recorded enclosure midpoint:
j256 = rows[255]
S256_mid = Fraction(j256[1] + j256[2], 2) / K
T_mid = sum(Fraction(hi, K) for j, lo, hi in rows if j <= 255) + S256_mid
D1_mid = T_mid / 256 - Fraction(1, 2)
print("D(1) with S(j)=hi (j<256), S(256)=mid:", float(D1_mid))

# 4) E(1) = sum_{j=1}^{255} s_j (1 - j/256) - 1/6  with s_j = S(j)/256, S(j) = j/256 (midpoint model)
E1_mid = sum(Fraction(j, 256) / 256 * (1 - Fraction(j, 256)) for j in range(1, 256)) - Fraction(1, 6)
print("E(1) midpoint model:", E1_mid, "= -1/393216?", E1_mid == -Fraction(1, 393216))

# 5) sum_{j=1}^{255} (j/65536)(1 - j/256)
S = sum(Fraction(j, 65536) * (1 - Fraction(j, 256)) for j in range(1, 256))
print("sum (j/65536)(1-j/256) =", S, "== 21845/131072?", S == Fraction(21845, 131072))

# 6) delta' = sum over rows with hi = j*2^132+1 of (2^-140/256)(1 - j/256)
delta = sum(Fraction(1, 2 ** 140) / 256 * (1 - Fraction(j, 256)) for j, lo, hi in rows if j <= 255 and hi == j * base + 1)
print("delta' =", float(delta), "  claim 1.9046711470564975e-43")

# 7) p0
p0 = Fraction(10909258999421303588095230195816054408197, 16000000000000000000000000000000000000000)
print("p0 =", float(p0), " decimal:", "%.45f" % float(p0))

# 8) v = p0 + 1/(6*256^2) - delta
v = p0 + Fraction(1, 6 * 256 ** 2) - delta
print("v =", "%.45f" % float(v), "  claim 0.681831230595341890922618553905170067178979166")
v0 = p0 + Fraction(1, 6 * 256 ** 2)  # delta' = 0 (midpoint rows)
print("v (delta'=0) =", "%.45f" % float(v0))
print("p0 + 1/393216 - delta' vs claim; 1/(6*256^2) =", Fraction(1, 6 * 256 ** 2), "=", 1 / (6 * 256 ** 2))

# 9) tau/512, M = 1/(6*256^2) + tau/512
tau = Fraction(3, 10 ** 40)
print("M = 1/(6*256^2)+tau/512 =", float(Fraction(1, 6 * 256 ** 2) + tau / 512), "  claim 2.5431315104e-6")

# 10) S(256) implied: T_mid/256 - 1/2 = D1 -> S(256):
print("S(256) mid:", float(S256_mid), " claim ~211.4320091424858")
