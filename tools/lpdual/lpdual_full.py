#!/usr/bin/env python3
"""Full LP-dual analysis of the near-CUE 256-law certificate. C^1 certificate class."""
import json, numpy as np
from scipy.optimize import linprog

d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
M0 = 2.5431315104166665e-6

w = np.full(N+1, h); w[0] = h/2; w[N] = h/2
W = np.zeros((N+1, N+1))
for j in range(1, N+1):
    W[j,0] = h/2
    for k in range(1, j): W[j,k] = h
    W[j,j] = h/2
R = -np.outer(np.ones(N+1), w) + W
I = np.zeros(N+1); I[0] = h*h/6
for j in range(1, N): I[j] = j*h*h
I[N] = (N-1)/2*h*h + h*h/3
iG = I @ R

def build(M, B, C, box=True, p1=None, s_use=None, Nrows=None, extra_rows=None, extra_p=None):
    """validity on rows 1..M of s_use (default law), plus optional extra rows (extended-grid probe)."""
    if s_use is None: s_use = s; Nrows = N
    if p1 is None: p1 = p0
    n = 1 + (N+1) + N
    c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG
    A_ub, b_ub = [], []
    if M > 0:
        a = np.zeros(n); a[0] = 1; a[1:1+N+1] = (s_use[:M] @ R[1:M+1,:])
        A_ub.append(a); b_ub.append(p1)
    if extra_rows:
        a = np.zeros(n); a[0] = 1
        for (j, sj) in extra_rows: a[1+j] = sj * R[j,:].sum() if False else 0  # placeholder, replaced below
        # proper: r_j = R[j,:] . g ; add s_j * r_j to the sum
        a = np.zeros(n); a[0] = 1
        for (j, sj) in extra_rows:
            a[1:1+N+1] += sj * R[j,:]
        A_ub.append(a); b_ub.append(extra_p if extra_p is not None else p1)
    a = np.zeros(n); a[1+256] = 1; A_ub.append(a); b_ub.append(B)
    a = np.zeros(n); a[1+256] = -1; A_ub.append(a); b_ub.append(B)
    for j in range(N):
        a = np.zeros(n); a[1+j] = -1; a[1+j+1] = 1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)
        a = np.zeros(n); a[1+j] = 1; a[1+j+1] = -1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1+N+1:1+N+1+N] = 1; A_ub.append(a); b_ub.append(C)
    if box:
        for xq in [0.0, 0.25, 0.5, 0.75]:
            for j in range(N):
                t = xq
                if j == N-1 and xq == 0.0: continue
                row = R[j,:].copy()
                row[j]   += h*(t - t*t/2)
                row[j+1] += h*t*t/2
                a = np.zeros(n); a[1:1+N+1] = row; A_ub.append(a); b_ub.append(1.0)
                a = np.zeros(n); a[1:1+N+1] = -row; A_ub.append(a); b_ub.append(1.0)
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
    return res

def unpack(res):
    if not res.success: return None
    c0 = res.x[0]; g = res.x[1:1+N+1]; t = res.x[1+N+1:]
    v = c0 + (iG@g)
    return dict(v=v, c0=c0, g=g, t=t, res=res)

print(f"p0 = {p0:.12f}   M0 = {M0:.6e}   E(1) = {d['E1']:.6e}")

# ================= LP-A': full validity, box on/off, ceiling attainability =================
print("\n### LP-A': full near-CUE validity (rows 1..255).  Ceiling: v* <= p0 + M0*(B+C) ###")
for box in [False, True]:
    print(f"--- box={box} ---")
    for (B, C) in [(1,0),(0,1),(1,1),(2,2),(4,4)]:
        res = build(255, B, C, box=box)
        u = unpack(res)
        pred = p0 + M0*(B+C)
        print(f"  B={B} C={C}: v* = {u['v']:.12f}  (pred {pred:.12f}, diff {u['v']-pred:+.2e})")

# ================= LP-B': interpolation, row sweep M =================
print("\n### LP-B': row sweep — validity on rows 1..M, B=C=1, box ###")
res_255 = build(255, 1.0, 1.0, box=True)
u255 = unpack(res_255)
print("  M=255 (full): v* = %.12f   [p0 + M0(B+C) = %.12f]" % (u255['v'], p0+2*M0))
for M in [1, 2, 4, 8, 16, 32, 64, 128, 192, 240, 250, 254, 255]:
    res = build(M, 1.0, 1.0, box=True)
    u = unpack(res)
    print(f"  M={M:4d}:  v* = {u['v']:.10f}   excess over ceiling = {u['v']-(p0+2*M0):+.6e}")

# ================= LP-C': beyond-bandwidth-1 probe =================
print("\n### LP-C': beyond-bandwidth-1 (CONJECTURAL) — CUE extension to 512 rows, F=1 on [0,2] ###")
# extended rows j=257..512 with s_j = j/512^2 (CUE), validity p1 = simple fraction of the extended law
s_ext = np.array([ (j+1)/512**2 for j in range(512) ])   # rows 1..512 of the 512-grid CUE law
# but our r lives on the 256-grid; use rows 1..256 of the 256-grid law + rows 257..512 treated as
# 'extra' with r evaluated at x=j/512: r(x) for x in (1,2] — our r is defined on [0,1] only!
# Beyond bandwidth 1 means the CERTIFICATE must know F(alpha) for alpha in (1,2), i.e. r on (1,2].
# Model: extend the certificate r to [0,2] with the same C^1 class on [0,2] (256 more knots).
# (Simplified probe below: keep r on [0,1], add rows 257..512 of a 512-grid law, r(x)=0 for x>1.)
print("  probe P1: r restricted to [0,1] (r(x)=0 for x>1), extra rows j=257..512 with p1 swept:")
p1s = [0.6818286874638315, 0.70, 0.80, 0.90, 1.0]
extra = [(j, s_ext[j]) for j in range(256, 512)]   # rows 257..512 (index j)
for p1 in p1s:
    res = build(255, 1.0, 1.0, box=True, extra_rows=extra, extra_p=p1)
    u = unpack(res)
    print(f"    p1={p1:.4f}: v* = {u['v']:.10f}   (p1 + M0(B+C) = {p1+2*M0:.10f})")
