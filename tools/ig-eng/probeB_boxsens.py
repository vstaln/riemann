#!/usr/bin/env python3
"""Probe B — superdirectivity / fragility audit of the in-class 0.6818 closure.
Question: how much does the certified value move when the modeling assumption behind the
box |r|<=1 is perturbed by +-delta? (The box comes from window kernels 0<=phi<=1.)
Copies the canonical LP machinery (tools/lpdual/lpdual_full.py) into /tmp (never edits canonical)."""
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

def build_box(B, C, boxbound):
    n = 1 + (N+1) + N
    c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG
    A_ub, b_ub = [], []
    a = np.zeros(n); a[0] = 1; a[1:1+N+1] = (s[:N] @ R[1:N+1,:])   # rows 1..255 (s has 256 entries, s[:N] = rows 1..255)
    A_ub.append(a); b_ub.append(p0)
    a = np.zeros(n); a[1+256] = 1; A_ub.append(a); b_ub.append(B)
    a = np.zeros(n); a[1+256] = -1; A_ub.append(a); b_ub.append(B)
    for j in range(N):
        a = np.zeros(n); a[1+j] = -1; a[1+j+1] = 1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)
        a = np.zeros(n); a[1+j] = 1; a[1+j+1] = -1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1+N+1:1+N+1+N] = 1; A_ub.append(a); b_ub.append(C)
    for xq in [0.0, 0.25, 0.5, 0.75]:
        for j in range(N):
            t = xq
            if j == N-1 and xq == 0.0: continue
            row = R[j,:].copy()
            row[j]   += h*(t - t*t/2)
            row[j+1] += h*t*t/2
            a = np.zeros(n); a[1:1+N+1] = row; A_ub.append(a); b_ub.append(boxbound)
            a = np.zeros(n); a[1:1+N+1] = -row; A_ub.append(a); b_ub.append(boxbound)
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
    if not res.success: return None
    return res.x[0] + (iG @ res.x[1:1+N+1])

print(f"p0 = {p0:.12f}  M0 = {M0:.3e}  p0+|E1| = {p0+abs(d['E1']):.12f}")
print("\n=== box-perturbation sensitivity (B=C=1, full validity rows 1..255) ===")
print("boxbound      v*          dv/dbox")
vals = {}
for bb in [1.0, 1.0+1e-6, 1.0+1e-5, 1.0-1e-6, 1.0-1e-5, 1.1, 1.5, 2.0, 0.99, 0.95, 0.9]:
    v = build_box(1.0, 1.0, bb)
    if v is not None: vals[bb] = v
order = sorted(vals)
for i, bb in enumerate(order):
    s = f"{bb:.7f}   {vals[bb]:.12f}"
    if i > 0:
        s += f"   {(vals[bb]-vals[order[i-1]])/(bb-order[i-1]):+.3e}"
    print(s)
# report sensitivity at 1.0
lo, hi = vals.get(1.0-1e-6), vals.get(1.0+1e-6)
print(f"\ndv/dbox at 1.0 (central diff, 1e-6): {(hi-lo)/2e-6:+.3e}")
print(f"gain of the in-class closure = v*(1.0) - 0.6725007037 = {vals[1.0]-0.6725007037:.6e}")
print(f"relative fragility: (dv/dbox)/gain = {(hi-lo)/2e-6/(vals[1.0]-0.6725007037):+.3e} per unit box change")
