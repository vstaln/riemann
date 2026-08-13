#!/usr/bin/env python3
"""realconfig_check.py — EXPLORER: does the bandwidth-one ceiling bind REALITY (GUE-flat
datum S(j)=j) or only the artificial 256-law?

Context (attack-lpdual.md, Round 2): the in-class optimum of the bandwidth-one certificate
class is v* = p0 + |E(1)| = 0.6818312305953419, attained by the near-CUE 256-law. The
constraint-hardness question: is the law's form factor the WORST case for real zeros, or an
artificial adversary reality does not realize? If the GUE-flat datum S(j)=j (the idealized
real zeros — Montgomery F(alpha)=1 on [0,1] is PROVEN under RH and is the empirical null,
attack-hot-hand.md) admits a HIGHER certificate value than the law, the 0.6818 ceiling does
not bind reality.

What this file establishes (all numbers produced here or by exact rational arithmetic):

  (0) the law's rows 1..255 in law_data.json are EXACTLY the GUE-flat datum s_j = j/256^2
      (max |s_mid - j/256^2| = 0 over rows 0..254); the free row 256 carries the residual
      mass and does not enter E(1) or the validity rows (r(1) = 0);
  (1) E(1) for the GUE-flat rows = -1/(6*256^2) = -2.5431315104166665e-6 EXACTLY (fractions);
  (2) LP over the certificate class, validity against the GUE-flat rows BUILT FROM SCRATCH
      (s_flat, independent of law_data.json), B=C=1, box |r|<=1, p1 = p0:
      v* = p0 + |E(1)| = 0.6818312305953419  — IDENTICAL to the value against the law,
      because the validity rows 1..255 are the same numbers;
  (3) the exact certificate r(x)=1-x against the flat datum at p1 = p0:
      v = p0 + 1/(6*256^2) - delta, delta = 0 for the exact flat rows (fractions, PROVEN);
  (4) v*(p1) = p1 + |E(1)| for the flat datum (shadow price of the certified simple
      fraction = 1): the only bandwidth-one datum that moves v is p1; the rows do not.

Honesty: every numeric claim CHECKED NUMERICALLY by this script (or exact rational
arithmetic where stated). The certificate-class LP machinery is the canonical one from
tools/lpdual/lpdual_final.py (reused verbatim for the matrices); the flat datum is built
independently so the comparison is not circular.

Run:  uv run --quiet --with numpy --with scipy python /tmp/lpdual_realcheck/realconfig_check.py
"""
import json
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

N = 256
h = 1 / N
M0 = 2.5431315104166665e-6                       # = 1/(6*256^2) (decimal)
p0 = Fraction(10909258999421303588095230195816054408197,
              16000000000000000000000000000000000000000)   # law's exact simple fraction

# ---------------------------------------------------------------- data
d = json.load(open('/home/vstaln/riemann/tools/lpdual/law_data.json'))
s_law = np.array(d['s_mid'])
p0f = d['p0']

# GUE-flat datum built from scratch: s_j = j/256^2, j = 1..256 (row 256 = free; r(1)=0 so
# its mass never enters the validity sum or E(1); we set it flat for the pure datum).
s_flat = np.array([(j + 1) / 65536.0 for j in range(N)])

# (0) rows 1..255 of the law == the flat datum?
dev = np.abs(s_law[:255] - s_flat[:255]).max()
print("(0) max |s_law[j] - j/256^2| over rows 1..255 =", dev, " (exact match:", dev == 0.0, ")")
print("    law free row 256 mass:", s_law[255], " (does not enter E(1) or validity; r(1)=0)")

# (1) E(1) for the flat rows, exactly
E1_flat_exact = sum(Fraction(j, 65536) * (1 - Fraction(j, 256)) for j in range(1, 256)) - Fraction(1, 6)
print("\n(1) E(1)_flat exact =", E1_flat_exact, "=", float(E1_flat_exact))
print("    == -1/(6*256^2) ?", E1_flat_exact == -Fraction(1, 6 * 256 * 256))
print("    law's E(1) (law_data.json) =", d['E1'])
print("    |E(1)| law =", abs(d['E1']), "  |E(1)| flat =", float(abs(E1_flat_exact)))

# ---------------------------------------------------------------- LP machinery (canonical)
w = np.full(N + 1, h); w[0] = h / 2; w[N] = h / 2
W = np.zeros((N + 1, N + 1))
for j in range(1, N + 1):
    W[j, 0] = h / 2
    for k in range(1, j):
        W[j, k] = h
    W[j, j] = h / 2
R = -np.outer(np.ones(N + 1), w) + W
I = np.zeros(N + 1); I[0] = h * h / 6
for j in range(1, N):
    I[j] = j * h * h
I[N] = (N - 1) / 2 * h * h + h * h / 3
iG = I @ R

def build(s_use, M, B, C, box=True, p1=None):
    if p1 is None:
        p1 = p0f
    n = 1 + (N + 1) + N
    c = np.zeros(n); c[0] = 1; c[1:1 + N + 1] = iG
    A_ub, b_ub = [], []
    a = np.zeros(n); a[0] = 1; a[1:1 + N + 1] = (s_use[:M] @ R[1:M + 1, :])
    A_ub.append(a); b_ub.append(p1)
    a = np.zeros(n); a[1 + 256] = 1; A_ub.append(a); b_ub.append(B)
    a = np.zeros(n); a[1 + 256] = -1; A_ub.append(a); b_ub.append(B)
    for j in range(N):
        a = np.zeros(n); a[1 + j] = -1; a[1 + j + 1] = 1; a[1 + N + 1 + j] = -1
        A_ub.append(a); b_ub.append(0.0)
        a = np.zeros(n); a[1 + j] = 1; a[1 + j + 1] = -1; a[1 + N + 1 + j] = -1
        A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1 + N + 1:1 + N + 1 + N] = 1; A_ub.append(a); b_ub.append(C)
    if box:
        for xq in [0.0, 0.25, 0.5, 0.75]:
            for j in range(N):
                t = xq
                if j == N - 1 and xq == 0.0:
                    continue
                row = R[j, :].copy()
                row[j] += h * (t - t * t / 2)
                row[j + 1] += h * t * t / 2
                a = np.zeros(n); a[1:1 + N + 1] = row; A_ub.append(a); b_ub.append(1.0)
                a = np.zeros(n); a[1:1 + N + 1] = -row; A_ub.append(a); b_ub.append(1.0)
    res = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  bounds=[(None, None)] * n, method='highs')
    assert res.success
    return res.x[0] + (iG @ res.x[1:1 + N + 1])

# (2) LP optimum against the flat datum vs against the law (B=C=1, box, p1=p0)
print("\n(2) LP optimum, validity on rows 1..255, B=C=1, box |r|<=1, p1 = p0:")
v_law = build(s_law, 255, 1.0, 1.0, box=True)
v_flat = build(s_flat, 255, 1.0, 1.0, box=True)
print("    vs law : v* = %.12f" % v_law)
print("    vs flat: v* = %.12f" % v_flat)
print("    p0 + |E(1)|_flat = %.12f" % (p0f + float(abs(E1_flat_exact))))
print("    identical? v_law == v_flat:", abs(v_law - v_flat) < 1e-12)
print("    matches p0+|E(1)|?  ", abs(v_flat - (p0f + float(abs(E1_flat_exact)))) < 1e-12)

# (3) exact certificate r(x) = 1-x against the flat datum, p1 = p0
sumr = sum(Fraction(j, 65536) * (1 - Fraction(j, 256)) for j in range(1, 256))
c0 = p0 - sumr
v_exact = c0 + Fraction(1, 6)
v_mid = p0 + Fraction(1, 6 * 256 * 256)
print("\n(3) exact certificate r=1-x vs flat datum, p1 = p0 (rational arithmetic):")
print("    c0 = p0 - sum_j (j/65536)(1-j/256) =", float(c0))
print("    v  = c0 + 1/6 =", float(v_exact), " = p0 + 1/(6*256^2) ?", v_exact == v_mid)
print("    delta (flat rows are exact -> 0) :", float(v_mid - v_exact))

# (4) v*(p1) for the flat datum: shadow price of the certified simple fraction = 1
print("\n(4) flat datum: v* as a function of the certified simple fraction p1 (B=C=1, box):")
for p1 in [p0f, 0.70, 0.80, 0.90, 1.0]:
    v = build(s_flat, 255, 1.0, 1.0, box=True, p1=p1)
    print("    p1=%.4f: v* = %.10f   (p1 + |E(1)| = %.10f)   shadow=1.0? %s"
          % (p1, v, p1 + float(abs(E1_flat_exact)), abs(v - (p1 + float(abs(E1_flat_exact)))) < 1e-10))

# (5) sanity: LP with only a few flat rows pins v loosely, full 255 rows pin it to the cap
print("\n(5) row sweep with the flat datum (B=C=1, box):")
for M in [1, 32, 64, 128, 192, 240, 254, 255]:
    v = build(s_flat, M, 1.0, 1.0, box=True)
    print("    M=%4d: v* = %.10f" % (M, v))

print("\nDONE")
