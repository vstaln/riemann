#!/usr/bin/env python3
"""Final LP-dual analysis: duals, active constraints, row shadow prices, missing-constraint probe."""
import json, numpy as np
from scipy.optimize import linprog

d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
M0 = 2.5431315104166665e-6
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
    A_ub, b_ub, names = [], [], []
    a = np.zeros(n); a[0] = 1; a[1:1+N+1] = (s[:M] @ R[1:M+1,:]); A_ub.append(a); b_ub.append(p1); names.append("validity")
    a = np.zeros(n); a[1+256] = 1; A_ub.append(a); b_ub.append(B); names.append("slope+")
    a = np.zeros(n); a[1+256] = -1; A_ub.append(a); b_ub.append(B); names.append("slope-")
    for j in range(N):
        a = np.zeros(n); a[1+j] = -1; a[1+j+1] = 1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0); names.append(f"epi{j}+")
        a = np.zeros(n); a[1+j] = 1; a[1+j+1] = -1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0); names.append(f"epi{j}-")
    a = np.zeros(n); a[1+N+1:1+N+1+N] = 1; A_ub.append(a); b_ub.append(C); names.append("curvsum")
    if box:
        for xq in [0.0, 0.25, 0.5, 0.75]:
            for j in range(N):
                t = xq
                if j == N-1 and xq == 0.0: continue
                row = R[j,:].copy(); row[j] += h*(t - t*t/2); row[j+1] += h*t*t/2
                a = np.zeros(n); a[1:1+N+1] = row; A_ub.append(a); b_ub.append(1.0); names.append(f"box+{j},{xq}")
                a = np.zeros(n); a[1:1+N+1] = -row; A_ub.append(a); b_ub.append(1.0); names.append(f"box-{j},{xq}")
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
    return res, names, (A_ub, b_ub)

def unpack(res):
    c0 = res.x[0]; g = res.x[1:1+N+1]; t = res.x[1+N+1:]
    return dict(v=c0+(iG@g), c0=c0, g=g, t=t)

print(f"p0={p0:.12f}  E(1)={E1:.6e}  M0={M0:.6e}  p0+|E(1)|={p0+abs(E1):.12f}")

# ---- box caps the gain at |E(1)|: verify B<1 and B>1 ----
print("\n### box |r|<=1: v*(B,C) = p0 + |E(1)|*min(B,1)?  ###")
for (B,C) in [(0.5,0),(1.0,0),(2.0,0),(1.0,2.0),(2.0,2.0),(8.0,8.0)]:
    res,_,_ = build(255, B, C, box=True)
    u = unpack(res)
    print(f"  B={B} C={C}: v*={u['v']:.12f}  (p0+{abs(E1)*min(B,1):.6e} = {p0+abs(E1)*min(B,1):.12f})")

# ---- duals at the full-data optimum ----
print("\n### duals / active constraints at M=255, B=1, C=1, box ###")
res, names, (Aub, bub) = build(255, 1.0, 1.0, box=True)
u = unpack(res)
marg = np.asarray(res.ineqlin.marginals).ravel()
slack = bub - Aub @ res.x
act = [(names[i], marg[i]) for i in range(len(names)) if slack[i] < 1e-8 and abs(marg[i]) > 1e-10]
print(f"v* = {u['v']:.12f}  (= p0 + |E(1)| ? {abs(u['v']-(p0+abs(E1)))<1e-12})")
print("active constraints (dual != 0):")
for nm, ml in act: print(f"   {nm:22s} dual = {ml:.6e}")
# which box rows active?
boxact = [nm for nm,_ in act if nm.startswith('box')]
print(f"  # box rows active: {len(boxact)} of 2044 ; sample: {boxact[:8]}")
print(f"  validity dual = {marg[0]:.6e}")

# ---- row shadow prices: value of each row j (drop-row analysis) ----
print("\n### shadow price of each law row: v*(255 \\ {j}) - v*(255) ###")
v255 = u['v']
for j in [1, 32, 64, 128, 192, 240, 250, 254, 255, 256]:
    # validity on rows 1..255 except j (row j = index j-1; j=256 has r_256=0 anyway)
    rows = [k for k in range(1, 256) if k != j]
    n = 1+(N+1)+N
    c = np.zeros(n); c[0]=1; c[1:1+N+1]=iG
    A_ub=[]; b_ub=[]
    a=np.zeros(n); a[0]=1; a[1:1+N+1]=(s[[k-1 for k in rows]] @ R[np.array(rows),:]); A_ub.append(a); b_ub.append(p0)
    a=np.zeros(n); a[1+256]=1; A_ub.append(a); b_ub.append(1.0)
    a=np.zeros(n); a[1+256]=-1; A_ub.append(a); b_ub.append(1.0)
    for jj in range(N):
        a=np.zeros(n); a[1+jj]=-1; a[1+jj+1]=1; a[1+N+1+jj]=-1; A_ub.append(a); b_ub.append(0.0)
        a=np.zeros(n); a[1+jj]=1; a[1+jj+1]=-1; a[1+N+1+jj]=-1; A_ub.append(a); b_ub.append(0.0)
    a=np.zeros(n); a[1+N+1:1+N+1+N]=1; A_ub.append(a); b_ub.append(1.0)
    r2 = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(None,None)]*n, method='highs')
    v2 = r2.x[0]+(iG@r2.x[1:1+N+1])
    print(f"  drop row j={j:3d}: v* = {v2:.10f}   (gain vs full: {v2-v255:+.6e})")

# ---- missing constraint: shadow price of p1 ----
print("\n### missing-constraint probe: v* as function of p1 (the certified simple fraction) ###")
for p1 in [p0, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.0]:
    res,_,_ = build(255, 1.0, 1.0, box=True, p1=p1)
    u = unpack(res)
    print(f"  p1={p1:.4f}: v* = {u['v']:.10f}   (p1 + |E(1)| = {p1+abs(E1):.10f})  shadow=1.0? {abs(u['v']-(p1+abs(E1)))<1e-10}")
