#!/usr/bin/env python3
"""Exact identity verification on the LP-optimal certificate (exact E formula)."""
import json, numpy as np
from scipy.optimize import linprog
d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
E1 = d['E1']

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

def build(M, B, C, box=True, p1=None):
    if p1 is None: p1 = p0
    n = 1 + (N+1) + N
    c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG
    A_ub, b_ub = [], []
    a = np.zeros(n); a[0] = 1; a[1:1+N+1] = (s[:M] @ R[1:M+1,:]); A_ub.append(a); b_ub.append(p1)
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
                row = R[j,:].copy(); row[j] += h*(t - t*t/2); row[j+1] += h*t*t/2
                a = np.zeros(n); a[1:1+N+1] = row; A_ub.append(a); b_ub.append(1.0)
                a = np.zeros(n); a[1:1+N+1] = -row; A_ub.append(a); b_ub.append(1.0)
    res = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(None,None)]*n, method='highs')
    return res

res = build(255,1,1,box=True)
c0 = res.x[0]; g = res.x[1:1+N+1]
r = R@g
intr = (I*r).sum(); rowsum = s[:255]@r[1:256]
lhs = rowsum - intr
# exact E(x) = sum_{x_i <= x} s_i (x - x_i) - x^3/6
def Eexact(x):
    xi = np.arange(1,257)/N
    mask = xi <= x
    return (s[mask]*(x - xi[mask])).sum() - x**3/6
D1 = s.sum()-0.5
g1 = 256*(r[256]-r[255])
int_hE = sum((g[j+1]-g[j])*Eexact((j+0.5)/N) for j in range(N))   # h=(g_{j+1}-g_j)*256, cell width 1/256, midpoint E
rhs = r[256]*D1 - g1*E1 + int_hE
print(f"sum s_j r_j - int r x dx = {lhs:.6e}")
print(f"r(1) D(1) - g(1) E(1) + int h E = {rhs:.6e}")
print(f"diff = {abs(lhs-rhs):.2e}   (identity holds if < 1e-7)")
print(f"gain = int - rowsum = {intr-rowsum:.6e}   |E(1)| = {abs(E1):.6e}")
print(f"r(0)={r[0]:.4f} r(1/2)={r[128]:.4f} r(1)={r[256]:.4f} r'(1)={g1:.4f}  int|r''|={np.abs(np.diff(g)).sum():.4f}")
