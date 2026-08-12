#!/usr/bin/env python3
"""Delsarte-style LP relaxations of the zero-proportion certificate class.

Canonical formulation EXACTLY as tools/lpdual/lpdual_final.py (so the M-sweep
reproduces the certified numbers 1:1), generalized to k cells for the
cell-count relaxation (the Delsarte-style k-th relaxation).

Variables  c0, g_0..g_k (r' at knots, r in C^2, r'' = g' piecewise-constant), t_1..t_k.
r(j/k)    = -1/k * [h/2 g_j + h sum_{j<i<k} g_i + h/2 g_k]   (exact quadrature, r(1)=0),
            R_k[j,i] = -1/(2k) at i=j, -1/k for j<i<k, -1/(2k) at i=k.
Objective  maximize c0 + int_0^1 r(x) x dx = c0 + (I_k @ R_k) . g,
            I_k[0] = h^2/6, I_k[j] = j h^2 (1<=j<k), I_k[k] = (k-1)/2 h^2 + h^2/3.
Constraints
  validity   c0 + sum_{i=1}^M s_i r(i/256) <= p0   (M rows of the near-CUE 256 law)
  slope      |g_k| <= B                            (|r'(1)|)
  curvature  sum_{j=1}^k |g_j - g_{j-1}| <= C      (epigraph t_j)
  box        |r(x)| <= 1  on [0,1]  (knots + cell offsets {0,.25,.5,.75}, exact)
rcoef(x): r(x) = r(j/k) + [g_j h(t-t^2/2) + g_{j+1} h t^2/2],  x = (j+t)/k  (exact).

Experiments
  [1] cell-count relaxation k (validity on ALL 255 rows, box, B=C=1):
      does v*(k) converge to p0+|E(1)| = 0.681831230595 from below or jump above?
  [2] data-row relaxation M (k=256): dropping pair-correlation rows lets the
      certificate claim more (canonical LP-B' sweep, reproduces 0.8899 at M=1).
  [3] budget relaxation (B,C) with box on/off: the box cap v* = p0+|E(1)|.
  [4] max over k of the FULL-DATA relaxation: jump test.

Labels: all numbers CHECKED NUMERICALLY (scipy.optimize.linprog / HiGHS, deterministic).
"""
import json
import numpy as np
from scipy.optimize import linprog

d = json.load(open('../../../../tools/lpdual/law_data.json'))
s_mid = np.array(d['s_mid'])     # 256 rows, S(j)/256, midpoint model S(j) = j/256
p0 = d['p0']
E1 = d['E1']                     # -2.543131510407415e-6 = -1/(6*256^2)
M0 = abs(E1)


def build(k, M, B, C, box=True, p1=None):
    if p1 is None:
        p1 = p0
    h = 1.0 / k
    # --- quadrature matrices (canonical) ---
    w = np.full(k + 1, h); w[0] = h / 2; w[k] = h / 2
    W = np.zeros((k + 1, k + 1))
    for j in range(1, k + 1):
        W[j, 0] = h / 2
        for i in range(1, j):
            W[j, i] = h
        W[j, j] = h / 2
    R = -np.outer(np.ones(k + 1), w) + W          # R[j,i]: coeff of g_i in r(j/k)
    I = np.zeros(k + 1); I[0] = h * h / 6
    for j in range(1, k):
        I[j] = j * h * h
    I[k] = (k - 1) / 2.0 * h * h + h * h / 3.0
    iG = I @ R                                     # objective coeffs on g

    n = 1 + (k + 1) + k
    c = np.zeros(n); c[0] = 1.0; c[1:1 + k + 1] = iG

    def rcoef(x):
        """coeff vector (on g) of r(x), exact quadratic interpolation."""
        j = int(np.floor(x * k))
        if j >= k:
            j = k - 1
        t = x * k - j
        row = R[j, :].copy()
        row[j] += h * (t - t * t / 2)
        row[j + 1] += h * t * t / 2
        return row

    A_ub, b_ub, names = [], [], []
    # validity on rows 1..M of the law
    a = np.zeros(n); a[0] = 1.0
    for i in range(1, min(M, 255) + 1):
        a[1:1 + k + 1] += s_mid[i - 1] * rcoef(i / 256.0)
    A_ub.append(a); b_ub.append(p1); names.append('validity')
    # slope |g_k| <= B
    a = np.zeros(n); a[1 + k] = 1.0; A_ub.append(a); b_ub.append(B); names.append('slope+')
    a = np.zeros(n); a[1 + k] = -1.0; A_ub.append(a); b_ub.append(B); names.append('slope-')
    # curvature sum_{j=1}^k |g_j - g_{j-1}| <= C
    for j in range(1, k + 1):
        a = np.zeros(n)
        a[1 + j] = 1.0; a[1 + j - 1] = -1.0; a[1 + k + j - 1] = -1.0
        A_ub.append(a); b_ub.append(0.0); names.append(f'epi{j}+')
        a = np.zeros(n)
        a[1 + j] = -1.0; a[1 + j - 1] = 1.0; a[1 + k + j - 1] = -1.0
        A_ub.append(a); b_ub.append(0.0); names.append(f'epi{j}-')
    a = np.zeros(n); a[1 + k:1 + k + k] = 1.0
    A_ub.append(a); b_ub.append(C); names.append('curvsum')
    # box |r(x)| <= 1
    if box:
        for j in range(k):
            for xq in [0.0, 0.25, 0.5, 0.75]:
                if j == k - 1 and xq == 0.0:
                    continue
                row = rcoef((j + xq) / k)
                a = np.zeros(n); a[1:1 + k + 1] = row
                A_ub.append(a); b_ub.append(1.0); names.append(f'box+{j},{xq}')
                A_ub.append(-a); b_ub.append(1.0); names.append(f'box-{j},{xq}')
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * n, method='highs')
    return res, iG


print("=" * 80)
print("DELSARTE-STYLE LP RELAXATIONS (exact canonical quadrature)")
print("p0 = %.16f   |E(1)| = %.12e   in-class ceiling p0+|E(1)| = %.12f"
      % (p0, M0, p0 + M0))
print("=" * 80)

print()
print("[1] CELL-COUNT RELAXATION k  (validity rows 1..255, box, B=C=1)")
print("    k | v* | v*-(p0+|E1|) | note")
for k in [2, 3, 4, 8, 16, 32, 64, 128, 256]:
    res, iG = build(k, 255, 1.0, 1.0, box=True)
    if not res.success:
        print(f"{k:4d} | FAIL | - | {res.message}")
        continue
    v = -res.fun
    print(f"{k:4d} | {v:.12f} | {v-(p0+M0):+.3e} | {'exact' if k==256 else 'relaxed'}")

print()
print("[2] DATA-ROW RELAXATION M  (k=256, box, B=C=1)  [canonical LP-B']")
print("    M | v* | vs ceiling | note")
for M in [1, 8, 32, 64, 128, 192, 240, 250, 254, 255]:
    res, iG = build(256, M, 1.0, 1.0, box=True)
    if not res.success:
        print(f"{M:4d} | FAIL | - | {res.message}")
        continue
    v = -res.fun
    note = 'canonical 0.8899029790' if M == 1 else ''
    print(f"{M:4d} | {v:.12f} | {v-(p0+M0):+.6e} | {note}")

print()
print("[3] BUDGET RELAXATION (k=256, all 255 rows): box vs no-box")
print("    B | C | box | v* | (cap p0+|E1| | p0+|E1|(B+C))")
for (B, C, box) in [(1, 0, True), (1, 0, False), (1, 1, True), (1, 1, False),
                    (2, 2, True), (2, 2, False), (4, 4, True), (4, 4, False),
                    (8, 8, True), (8, 8, False)]:
    res, iG = build(256, 255, B, C, box=box)
    if not res.success:
        print(f"{B:4.0f} | {C:4.0f} | {str(box):5s} | FAIL | {res.message}")
        continue
    v = -res.fun
    print(f"{B:4.0f} | {C:4.0f} | {str(box):5s} | {v:.12f} | {p0+M0 if box else p0+M0*(B+C):.12f}")

print()
print("[4] JUMP TEST — max over cell-count relaxations of the FULL-DATA class (box)")
worst = -1.0; worst_k = None
for k in [2, 3, 4, 8, 16, 32, 64, 128, 256]:
    res, iG = build(k, 255, 1.0, 1.0, box=True)
    if res.success:
        v = -res.fun
        if v > worst:
            worst, worst_k = v, k
print(f"    max v* = {worst:.12f} at k={worst_k}   (ceiling {p0+M0:.12f})")
print(f"    excess = {worst-(p0+M0):+.3e}   -> {'JUMP ABOVE' if worst > p0+M0+1e-9 else 'no jump: relaxation sequence stays at/below the ceiling'}")
