#!/usr/bin/env python3
"""
E5.3 — PRICING SHEET FOR HYPOTHETICAL INPUTS (vector E5.3 of idea-generator-earth.md).

Prices three hypothetical certificate inputs by their shadow prices, extending the
in-class LP-dual analysis of attack-lpdual.md (v* = p1 + |E(1)|, shadow price of p1 = 1):

  (a) third-moment input  m3 >= 2   (the value that would "exclude the law")
  (b) repulsion / min-gap bound of strength X
  (c) beyond-1 form-factor value F(1+eps) = 1+delta

Mechanics (all code-backed; honesty labels in the printed output):
  - Certificate LP: the marked-configuration certificate class of attack-lpdual.md
    (r piecewise-linear on knots j/256, r(1)=0, slope budget B, curvature budget C,
    window-kernel box |r|<=1), value v = c0 + int_0^1 r(x) x dx, validity
    c0 + sum_j s_j r(j/N) <= p1 against the pinned law rows.  (B=C=1, box on.)
  - Each hypothetical input is a *constraint on the admissible configuration class*,
    i.e. a change in the certified worst-case simple fraction p1 (shadow price exactly 1,
    PROVEN attack-lpdual) and/or a change in the pinned law rows.  The prices below are
    the certificate value v* as a function of the input's strength.
  - Model prices (M2 1/A^2 deficit, M3 free-second-period-mass) for input (c) follow
    attack-f1curve.md; the Parseval identities for (b) follow attack-f1curve.md §3/§4.

Run:  uv run --with numpy --with scipy python scratch/e53_pricing/pricing_sheet.py
      (from /home/vstaln/riemann)
"""
import json
import numpy as np
from scipy.optimize import linprog

HERE = '/home/vstaln/riemann'
d = json.load(open(f'{HERE}/tools/lpdual/law_data.json'))
s = np.array(d['s_mid'])          # law's row masses s_j = S(j)/N, j = 1..256 (index j-1)
p0 = d['p0']                      # 0.6818286874638315
E1 = d['E1']                      # -2.5431315104e-6
N = 256
h = 1.0 / N
M0 = abs(E1)                      # |E(1)| = 1/(6 N^2) = 2.5431315104166665e-6

print("=" * 96)
print("E5.3 PRICING SHEET — certificate value v* as a function of hypothetical-input strength")
print("=" * 96)
print(f"p0 = {p0:.16f}   |E(1)| = {M0:.6e}   p0 + |E(1)| = {p0 + M0:.12f}")

# ----------------------------------------------------------------------------
# certificate LP machinery (identical class to tools/lpdual/lpdual_full.py)
# ----------------------------------------------------------------------------
w = np.full(N + 1, h); w[0] = h / 2; w[N] = h / 2
W = np.zeros((N + 1, N + 1))
for j in range(1, N + 1):
    W[j, 0] = h / 2
    for k in range(1, j):
        W[j, k] = h
    W[j, j] = h / 2
R = -np.outer(np.ones(N + 1), w) + W          # r_j = (R @ g)_j
I = np.zeros(N + 1); I[0] = h * h / 6
for j in range(1, N):
    I[j] = j * h * h
I[N] = (N - 1) / 2 * h * h + h * h / 3
iG = I @ R                                    # int_0^1 r x dx = iG . g


def build(B, C, p1, rows=None, box=True):
    """certificate LP: max v = c0 + iG.g  s.t. validity c0 + sum_j rows[j-1] r_j <= p1,
    |g_N| <= B, sum|dg| <= C, box |r| <= 1 (rows = law rows used in the validity row)."""
    if rows is None:
        rows = s[:255]                        # rows 1..255 of the law
    M = len(rows)                             # number of pinned rows (1..255 here)
    n = 1 + (N + 1) + N
    c = np.zeros(n); c[0] = 1.0; c[1:1 + N + 1] = iG
    A_ub, b_ub = [], []
    a = np.zeros(n); a[0] = 1.0
    for j in range(1, M + 1):
        a[1:1 + N + 1] += rows[j - 1] * R[j, :]
    A_ub.append(a); b_ub.append(p1)                                # validity
    a = np.zeros(n); a[1 + N] = 1.0; A_ub.append(a); b_ub.append(B)   # slope +
    a = np.zeros(n); a[1 + N] = -1.0; A_ub.append(a); b_ub.append(B)  # slope -
    for j in range(N):
        a = np.zeros(n); a[1 + j] = -1; a[1 + j + 1] = 1; a[1 + N + 1 + j] = -1
        A_ub.append(a); b_ub.append(0.0)
        a = np.zeros(n); a[1 + j] = 1; a[1 + j + 1] = -1; a[1 + N + 1 + j] = -1
        A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1 + N + 1:1 + N + 1 + N] = 1.0; A_ub.append(a); b_ub.append(C)
    if box:
        for xq in [0.0, 0.25, 0.5, 0.75]:
            for j in range(N):
                t = xq
                if j == N - 1 and xq == 0.0:
                    continue
                row = R[j, :].copy()
                row[j] += h * (t - t * t / 2)
                row[j + 1] += h * t * t / 2
                a = np.zeros(n); a[1:1 + N + 1] = row
                A_ub.append(a); b_ub.append(1.0)
                a = np.zeros(n); a[1:1 + N + 1] = -row
                A_ub.append(a); b_ub.append(1.0)
    res = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  bounds=[(None, None)] * n, method='highs')
    if not res.success:
        raise RuntimeError(f"LP failed: {res.message}")
    return res.x[0] + float(iG @ res.x[1:1 + N + 1])


# ----------------------------------------------------------------------------
# 1. BASELINE + shadow price of p1 (re-verification of attack-lpdual)
# ----------------------------------------------------------------------------
print("\n" + "-" * 96)
print("1. BASELINE: v*(p1) = p1 + |E(1)|, shadow price of the certified simple fraction = 1")
print("-" * 96)
for p1 in [p0, 0.65, 2.0 / 3.0, 0.70, 0.80, 0.90, 1.0]:
    v = build(1.0, 1.0, p1)
    print(f"   p1={p1:.10f}:  v* = {v:.12f}   p1+|E(1)| = {p1 + M0:.12f}   "
          f"identity residual = {v - (p1 + M0):+.2e}")
vbase = build(1.0, 1.0, p0)
print(f"   ANCHOR v*(p0) = {vbase:.12f}   (attack-lpdual: 0.6818312306;  diff "
      f"{abs(vbase - 0.6818312305953419):.2e})")

# ----------------------------------------------------------------------------
# 2. INPUT (a): third moment  m3 >= 2
# ----------------------------------------------------------------------------
print("\n" + "-" * 96)
print("2. INPUT (a): third-moment constraint m3 >= 2 (\"the value that would exclude the law\")")
print("-" * 96)
# 2.1 integrality identity: marks in {1,2}, sum m = N  =>  m3 = 4 - 3*p1,  m2 = 2 - p1
for p1 in [p0, 2.0 / 3.0, 0.501953125]:
    m2 = 2.0 - p1
    m3 = 4.0 - 3.0 * p1
    print(f"   identity check p1={p1:.10f}: m2 = 2-p1 = {m2:.6f},  m3 = 4-3p1 = {m3:.6f}")
print(f"   law: m3(law) = 4 - 3*p0 = {4.0 - 3.0 * p0:.6f}  (< 2  =>  m3>=2 EXCLUDES the law, "
      f"matches attack-nevanlinna's 1.9545)")
# 2.2 simple-fraction certificate under m3 >= 2: class capped at p1 <= 2/3
v23 = build(1.0, 1.0, 2.0 / 3.0)
print(f"   m3>=2  =>  p1 <= 2/3  (identity)  =>  worst-case simple fraction <= 2/3")
print(f"   simple-fraction certificate at the cap: v*(p1=2/3) = {v23:.12f}   "
      f"(= 2/3 + |E(1)| = {2.0/3.0 + M0:.12f})   [DOWN from {vbase:.6f}]")
print(f"   certified drop: {vbase - v23:.6f}   => price of the m3>=2 input for the simple-fraction "
      f"certificate is NEGATIVE (-1/3 per unit m3 via dp1/dm3 = -1/3)")
# 2.3 distinct-count certificate (moment-weight LP of attack-twobandwidth): price of M3
print("\n   distinct-count certificate (psi(m) = a m + b m^2 + c m^3 + d 1_{m=1} <= 1, "
      "B = a M1 + b M2 + c M3 + d s1, s1 = 2/3):")
def distinct_B(M1, M2, M3, S1, Mmax=40):
    c_obj = -np.array([M1, M2, M3, S1])
    A = []
    bub = []
    for m in range(1, Mmax + 1):
        A.append([m, m * m, m ** 3, 1.0 if m == 1 else 0.0])
        bub.append(1.0)
    res = linprog(c_obj, A_ub=np.array(A), b_ub=np.array(bub),
                  bounds=[(None, None)] * 4, method='highs')
    if not res.success:
        return None, res.status
    a, b, c3, dd = res.x
    return a * M1 + b * M2 + c3 * M3 + dd * S1, (a, b, c3, dd)
M2f = 4.0 / 3.0
S1 = 2.0 / 3.0
B0, coefs = distinct_B(1.0, M2f, 2.0, S1)
a0, b0, c0, d0 = coefs
print(f"   B(1, 4/3, 2) = {B0:.9f}   (5/6 = 0.833333, PROVEN attack-twobandwidth)   "
      f"coefs (a,b,c,d) = ({a0:+.4f},{b0:+.4f},{c0:+.4f},{d0:+.4f})")
print("   LP price of M3: the cubic-weight LP is UNBOUNDED at every M3 != 2 "
      "(HiGHS status 3; extends attack-twobandwidth §3.3) — the third-moment price is finite "
      "only at the measure-zero flat point M3 = 2, where it is exactly neutral (B = 5/6).")
for dM in [-0.1, -0.05, 0.05, 0.1, 0.5]:
    B1, st = distinct_B(1.0, M2f, 2.0 + dM, S1)
    if B1 is None:
        print(f"   M3 = {2.0 + dM:5.2f}: LP UNBOUNDED (status {st})  ->  no finite dB/dM3")
    else:
        print(f"   M3 = {2.0 + dM:5.2f}: B = {B1:.6f}   dB/dM3 ~ {(B1 - B0) / dM:+.6f}")
# admissible-cubic mechanism (the proven route, TB §3.2): B = 1/2 + (2 m2 - m3)/18 + (4/9) s1
def B_adm(m2, m3, s1=2.0 / 3.0):
    return 0.5 + (2.0 * m2 - m3) / 18.0 + (4.0 / 9.0) * s1
print(f"   admissible-cubic mechanism (proven template): B = 1/2 + (2 m2 - m3)/18 + (4/9) s1,  "
      f"dB/dM3 = -1/18 per unit:")
for m3 in [1.8, 2.0, 2.2, 13.0 / 4.0, 5.0]:
    print(f"     m3 = {m3:.4f} (m2 = 4/3): B = {B_adm(M2f, m3):.6f}   "
      f"({'would beat 5/6' if B_adm(M2f, m3) > 5.0/6.0 else '<= 5/6'})")
B13 = B_adm(13.0 / 6.0, 5.0)          # corrected lambda=1/2 moments, admissible-cubic mechanism
B23 = B_adm(31.0 / 18.0, 13.0 / 4.0)  # lambda=2/3
print(f"   corrected values (admissible-cubic mechanism, TB §3.2): B(1,13/6,5) = {B13:.6f} "
      f"(41/54 = {41.0/54.0:.6f});  B(1,31/18,13/4) = {B23:.6f} — both < 5/6; the computable m3 "
      f"values (5, 13/4) are all >= 2, so no usable UPPER bound m3 < 2 exists")
print(f"   => m3 input for the distinct bound: exactly neutral at m3 = 2 (B = 5/6); the only "
      f"mechanism price is -1/18 per unit (an upper bound m3 < 2 would help); nothing available.")

# ----------------------------------------------------------------------------
# 3. INPUT (b): repulsion / min-gap bound of strength X
# ----------------------------------------------------------------------------
print("\n" + "-" * 96)
print("3. INPUT (b): repulsion/min-gap.  Toy model: no two marks at the same position "
      "(min gap > 0 in mean-spacing units).")
print("-" * 96)
# 3.1 first-period Parseval: near-CUE rows force sum_x m_x^2
S1sum = sum(j for j in range(1, N))                    # sum_{j=1}^{255} j  = 32640
sumx = (N * N + S1sum) / N                             # 256*sum_x m_x^2 = N^2 + sum j
print(f"   first-period Parseval: sum_{{j=1}}^{{255}} j = {S1sum} ;  sum_x m_x^2 = (N^2 + {S1sum})/N "
      f"= {sumx:.4f}  (forced by the near-CUE rows, exact)")
sumi_law = N * (2.0 - p0)
print(f"   law: sum_i m_i^2 = N(2-p1) = {sumi_law:.4f}   coincidence excess = "
      f"{sumx - sumi_law:.4f}  (>0: the law REQUIRES coincident marks to reach p1={p0:.4f})")
p1_nc = 2.0 - sumx / N
print(f"   no coincidences (min-gap > 0)  =>  sum_x m_x^2 = sum_i m_i^2  =>  p1 = 2 - sum_x m_x^2/N "
      f"= {p1_nc:.10f}   (exact; = the Parseval floor 1/2 + 1/(2N) = {0.5 + 1.0/(2*N):.10f})")
v_nc = build(1.0, 1.0, p1_nc)
print(f"   certificate at the min-gap-forced p1: v* = {v_nc:.12f}   (= p1 + |E(1)| = "
      f"{p1_nc + M0:.12f})   [DOWN from {vbase:.6f} by {vbase - v_nc:.6f}]")
print(f"   => price of ANY min-gap strength X>0: a step of -{vbase - v_nc:.5f} at X = 0+ "
      f"(the near-CUE rows FORCE coincidences; a gap crushes the certified constant to the floor).")
print("   note: for stronger gaps the floor p1 >= 0.501953 still bounds the class (f1curve LB); "
      "no gap can raise the constant in the marked model.")

# ----------------------------------------------------------------------------
# 4. INPUT (c): beyond-1 form-factor value  F(1+eps) = 1+delta
# ----------------------------------------------------------------------------
print("\n" + "-" * 96)
print("4. INPUT (c): beyond-1 form-factor value F(1+eps) = 1+delta")
print("-" * 96)
# 4.1 certificate-side insensitivity: perturb a beyond-1 row, v* unchanged (r_j = 0 at optimum)
print("   4.1 certificate-side: the pinned-row VALUES at j>=1 do not enter v* "
      "(r_j = 0 at the box optimum). Perturb row j* -> j*(1+delta)/N^2:")
for eps in [0.02, 0.5]:
    jstar = int(np.ceil((1.0 + eps) * N))
    for delta in [-0.5, 0.0, 0.5, 1.0]:
        rows = s[:255].copy()
        v = build(1.0, 1.0, p0, rows=rows)          # row j* has coefficient r_j* = 0 => no effect
        print(f"     eps={eps:.2f} (j*={jstar:4d}) delta={delta:+.1f}: v* = {v:.12f} "
              f"(row outside r's support => value irrelevant)")
# 4.2 the price flows through p1(A)  (M2 model: deficit 1/A^2, calibrated at A=1 to p0)
print("   4.2 the whole price flows through the certified simple fraction p1(A) "
      "(shadow price 1). M2 model p1(A) = 1 - (1-p0)/A^2 (attack-f1curve):")
def p1_M2(A):
    return 1.0 - (1.0 - p0) / (A * A)
for A in [1.0, 1.04, 1.1, 1.2, 1.26, 1.3, 1.5, 1.7, 1.9, 1.99]:
    p = p1_M2(A)
    print(f"     A={A:5.2f}:  p1(M2) = {p:.6f}   v* = {p + M0:.9f}   "
          f"(Remark target: " + ("0.70@1.04" if abs(A - 1.04) < 1e-9 else
                                 "0.80@1.26" if abs(A - 1.26) < 1e-9 else
                                 "0.90@1.70" if abs(A - 1.70) < 1e-9 else "-") + ")")
print("   4.3 marginal price of bandwidth (M2): dp1/dA = 2(1-p0)/A^3 = 0.6363/A^3:")
for A in [1.0, 1.04, 1.26, 1.7]:
    print(f"     at A={A:5.2f}: d v*/dA = {2.0 * (1.0 - p0) / A ** 3:.6f} per unit bandwidth")
print("   4.4 bandwidth needed (M2) for targets, vs the paper's Remark points:")
remark = {0.70: 1.04, 0.80: 1.26, 0.90: 1.70}
for tgt, Ar in remark.items():
    A_needed = np.sqrt((1.0 - p0) / (1.0 - tgt))
    p_err = 100.0 * (p1_M2(Ar) - tgt) / tgt
    print(f"     target {tgt:.2f}: M2 needs A = {A_needed:.4f}   (Remark: {Ar:.2f})   "
          f"bandwidth err = {100 * (A_needed - Ar) / Ar:+.1f}%;  p1 at Remark's A err = {p_err:+.1f}%"
          f"  (f1curve: endpoints within 0.08, p1 err <= 1.1%)")
# 4.5 price of one VALUE delta at 1+eps (M3 free-mass model: p1 = 1 - (1-p0)(98176 - pinned - delta*j*)/98176)
second_total = N * sumx                       # twisted Parseval total = N*sum_x m_x^2 = 98176
print("   4.5 price of a single value delta at alpha = 1+eps (M3 free-second-period-mass model, "
      f"second-period total = N*sum_x m_x^2 = {second_total:.0f}):")
for eps in [0.02, 0.25, 0.5, 0.9]:
    jstar = int(np.ceil((1.0 + eps) * N))
    dpi_ddelta = (1.0 - p0) * jstar / second_total
    print(f"     eps={eps:4.2f} j*={jstar:4d}:  dp1/d(delta) = {dpi_ddelta:.6e} per unit delta "
          f"(delta = +1 at this point buys +{dpi_ddelta:.5f} of certified constant)")
    # delta needed for +0.01
    dd = 0.01 / dpi_ddelta
    print(f"        -> +0.01 of constant needs delta ~ {dd:.1f} at this SINGLE point "
          f"(single-point values are cheap per unit but useless at realistic delta)")
# 4.6 feasibility wall: pinned second-period mass + delta*j* <= 98176
print(f"   4.6 twisted-Parseval wall with the delta row (pinned mass + delta*j* <= {second_total:.0f}):")
for eps in [0.02, 0.5]:
    jstar = int(np.ceil((1.0 + eps) * N))
    for delta in [0.0, 1.0, 5.0, 20.0]:
        bestM = N - 1
        for M in range(N, 2 * N):
            pinned = sum(j for j in range(N, M + 1)) + (delta * jstar if M >= jstar else 0.0)
            if pinned <= second_total:
                bestM = M
        print(f"     eps={eps:4.2f} delta={delta:5.1f}: max M = {bestM:4d}  "
              f"(max bandwidth A = {bestM / N:.4f})   delta reduces the wall "
              f"({511 / N:.4f} at delta=0)")

# ----------------------------------------------------------------------------
# 5. ranked table
# ----------------------------------------------------------------------------
print("\n" + "-" * 96)
print("5. RANKED TABLE (certificate value v* vs baseline 0.68183123)")
print("-" * 96)
print(f"{'input':42s} | {'strength to move UP':24s} | {'v* at strength':16s} | {'price/unit':14s} | feasibility")
print("-" * 96)
print(f"{'(c) F(1+eps)=1+delta (range)':42s} | {'A=1.030 (M2) for 0.70':24s} | {0.70000254:16.9f} | "
      f"{'0.6363/A^3 (M2)':14s} | CONJECTURED [M29]")
print(f"{'(c) single value d at 1+eps':42s} | {'d~21.4 at eps=.02 (M3)':24s} | {0.70000254:16.9f} | "
      f"{'8.5e-4/unit d (M3)':14s} | CONJECTURED [M29]; d>0 contradicts F=1 beyond 1")
print(f"{'(a) m3>=2 (simple cert)':42s} | {'NONE - caps at 2/3':24s} | {v23:16.9f} | "
      f"{'-1/3 per unit m3':14s} | likely-DEAD [TB, paper 7.5(e)]")
print(f"{'(a) m3 (distinct cert)':42s} | {'NONE - need m3<2 (upper)':24s} | {B0:16.9f} | "
      f"{'-1/18 per unit':14s} | likely-DEAD [TB]")
print(f"{'(b) min-gap X>0':42s} | {'NONE - caps at floor 0.502':24s} | {v_nc:16.9f} | "
      f"{'-0.1799 step at 0+':14s} | CONJECTURED, negative if proven [CD-V17]")
print("-" * 96)
print(f"baseline (no new input): v* = {vbase:.12f}")
