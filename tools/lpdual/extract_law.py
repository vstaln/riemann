#!/usr/bin/env python3
"""Extract the N=256 law's form factor masses s_j from LawN256.lean enclosures."""
import re, json

src = open('/home/vstaln/riemann/research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean').read()

# K := 1393796574908163946345982392040522594123776
m = re.search(r'K := (\d+)', src)
K = int(m.group(1))
print("K =", K, "~ 2^", K.bit_length()-1)

# encl := [(lo, hi), ...] — multi-line list
m = re.search(r'encl := \[(.*?)\]\n  tn', src, re.S)
pairs = re.findall(r'\((-?\d+), (-?\d+)\)', m.group(1))
print("num enclosures:", len(pairs))
assert len(pairs) == 256

los = [int(a) for a, b in pairs]
his = [int(b) for a, b in pairs]
# s_j = S(j)/256, enclosure: lo_j <= K*S(j) <= hi_j  =>  s_j in [lo/K/256, hi/K/256]
N = 256
s_mid = [(int(lo) + int(hi)) / 2 / K / N for lo, hi in pairs]
s_lo = [int(lo) / K / N for lo, _ in pairs]
s_hi = [int(hi) / K / N for _, hi in pairs]

# p0
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
print("p0 =", repr(p0))
print("1-p0 =", repr(1 - p0))

# totals
T_N_over_N = sum(s_mid)  # = Csum at N = sum_j s_j = T_N / N
print("sum_j s_j (mid) =", T_N_over_N)
print("D(1) = sum s_j - 1/2 =", T_N_over_N - 0.5, " (row-cert |D1| <= 0.82395317)")

# E(1) = integral_0^1 D(x) dx ; D(x) = C(x) - x^2/2, C step = sum_{j/N<=x} s_j
# E(1) = sum_j s_j*(1 - j/N) - 1/6   (cellwise: int_{j/N}^{1} s_j dx = s_j(1-j/N); int x^2/2 = 1/6)
E1 = sum(s_mid[j]*(1 - (j+1)/N) for j in range(N)) - 1/6
print("E(1) (mid) =", E1, " near-CUE bound |E1| <= 1/(6N^2)+tau/(2N) =", 1/(6*N**2))

# near-CUE check: |N*S(j) - j| <= tau=3e-40 for j<N ; S(j)=N*s_j
tau = 3e-40
maxdev = max(abs(N*(N*s_mid[j]) - (j+1)) for j in range(N-1))
print("max |N*S(j)-j| for j<256 (using midpoints) =", maxdev, " tau =", tau)

json.dump({"K": K, "s_mid": s_mid, "s_lo": s_lo, "s_hi": s_hi, "p0": p0,
           "E1": E1, "D1": T_N_over_N - 0.5}, open('law_data.json','w'))
print("wrote law_data.json")
