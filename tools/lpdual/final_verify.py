#!/usr/bin/env python3
"""Verify the Stability.lean identity numerically on the LP-optimal certificate; save full results."""
import json, numpy as np
from scipy.optimize import linprog

d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
M0 = 2.5431315104166665e-6; E1 = d['E1']

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
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
    return res

def unpack(res):
    c0 = res.x[0]; g = res.x[1:1+N+1]; t = res.x[1+N+1:]
    return dict(v=c0+(iG@g), c0=c0, g=g, t=t)

out = {}
out['p0'] = p0; out['M0'] = M0; out['E1'] = E1
out['p0_plus_absE1'] = p0 + abs(E1)

# 1. ceiling attainability (no box)
print("## ceiling attainability (no box): v* vs p0 + M0*(B+C)")
out['ceiling_no_box'] = []
for (B,C) in [(1,0),(0,1),(1,1),(2,2),(4,4)]:
    res = build(255,B,C,box=False); u = unpack(res)
    out['ceiling_no_box'].append((B,C,u['v']))
    print(f"  B={B} C={C}: v*={u['v']:.12f} pred={p0+M0*(B+C):.12f} diff={u['v']-(p0+M0*(B+C)):+.2e}")

# 2. box caps at |E(1)|*min(B,1)
print("## box |r|<=1: v*(B,C) = p0 + |E(1)|*min(B,1)")
out['box_cap'] = []
for (B,C) in [(0.5,0),(1,0),(2,0),(1,2),(8,8)]:
    res = build(255,B,C,box=True); u = unpack(res)
    out['box_cap'].append((B,C,u['v']))
    print(f"  B={B} C={C}: v*={u['v']:.12f}  (p0+|E1|*min(B,1)={p0+abs(E1)*min(B,1):.12f})")

# 3. identity check on the LP optimum (B=1,C=1, box)
res = build(255,1,1,box=True); u = unpack(res)
g = u['g']; r = R@g
lhs = (s[:255]@r[1:256]) - (I*r).sum()          # sum s_j r_j - int r x dx
g1 = 256*(r[256]-r[255]); D1 = s.sum()-0.5
h_epi = np.diff(g)*256                            # piecewise-constant r''=g' on cells: h_j = (g_{j+1}-g_j)*256
# int h E via E(x) computed numerically
xf = np.linspace(0,1,2049)
# E(x) = int_0^x (C - t^2/2) dt ; C piecewise constant with masses s_j at j/256
Cstep = np.zeros_like(xf)
for j in range(1,256):
    Cstep[xf >= j/N] += s[j-1]
E = np.array([np.trapezoid(Cstep[xf<=x] - xf[xf<=x]**2/2, xf[xf<=x]) for x in xf])
def Eval(x): return np.interp(x, xf, E)
int_hE = 0.0
for j in range(N):
    # cell [j/N,(j+1)/N): h = (g[j+1]-g[j])*256, E ~ linear-ish; use midpoint
    int_hE += (g[j+1]-g[j])*256 * Eval((j+0.5)/N) / 256
rhs = r[256]*D1 - g1*E1 + int_hE
print(f"## identity on LP optimum:  sum-int = {lhs:.6e},  r1 D1 - g1 E1 + int hE = {rhs:.6e},  diff = {abs(lhs-rhs):.2e}")
print(f"## LP optimum certificate: r(0)={r[0]:.6f} r(1/2)={r[128]:.6f} r(1)={r[256]:.6f}, r'(1)={g1:.4f}, gain=int-rowsum={ (I*r).sum() - (s[:255]@r[1:256]):.6e}")

# 4. interpolation sweep (rows)
print("## row sweep M (B=C=1, box):")
out['row_sweep'] = []
for M in [1,2,4,8,16,32,64,128,192,240,250,254,255]:
    res = build(M,1,1,box=True); u = unpack(res)
    out['row_sweep'].append((M,u['v']))
    print(f"  M={M:4d}: v*={u['v']:.10f}")

# 5. missing constraint: p1 sweep
print("## p1 sweep (shadow price of the simple-fraction datum):")
out['p1_sweep'] = []
for p1 in [p0,0.70,0.80,0.90,1.0]:
    res = build(255,1,1,box=True,p1=p1); u = unpack(res)
    out['p1_sweep'].append((p1,u['v']))
    print(f"  p1={p1:.4f}: v*={u['v']:.10f} (p1+|E1|={p1+abs(E1):.10f})")

# 6. row shadow prices
print("## row shadow prices (drop-row):")
out['row_shadow'] = []
v255 = out['row_sweep'][-1][1]
for j in [1,32,64,128,192,240,250,254,255,256]:
    rows = [k for k in range(1,256) if k != j]
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
    out['row_shadow'].append((j, v2-v255))
    print(f"  drop row j={j:3d}: v* gain = {v2-v255:+.6e}")

# 7. duals at optimum
res, = (build(255,1,1,box=True),)
n = 1+(N+1)+N
c = np.zeros(n); c[0]=1; c[1:1+N+1]=iG
A_ub=[]; b_ub=[]
a=np.zeros(n); a[0]=1; a[1:1+N+1]=(s[:255] @ R[1:256,:]); A_ub.append(a); b_ub.append(p0)
a=np.zeros(n); a[1+256]=1; A_ub.append(a); b_ub.append(1.0)
a=np.zeros(n); a[1+256]=-1; A_ub.append(a); b_ub.append(1.0)
for j in range(N):
    a=np.zeros(n); a[1+j]=-1; a[1+j+1]=1; a[1+N+1+j]=-1; A_ub.append(a); b_ub.append(0.0)
    a=np.zeros(n); a[1+j]=1; a[1+j+1]=-1; a[1+N+1+j]=-1; A_ub.append(a); b_ub.append(0.0)
a=np.zeros(n); a[1+N+1:1+N+1+N]=1; A_ub.append(a); b_ub.append(1.0)
# box rows with names
names = ["validity","slope+","slope-"] + [f"epi{j}{q}" for j in range(N) for q in "+-"] + ["curvsum"]
for xq in [0.0,0.25,0.5,0.75]:
    for j in range(N):
        t = xq
        if j == N-1 and xq == 0.0: continue
        row = R[j,:].copy(); row[j] += h*(t-t*t/2); row[j+1] += h*t*t/2
        a=np.zeros(n); a[1:1+N+1]=row; A_ub.append(a); b_ub.append(1.0); names.append(f"box+{j},{xq}")
        a=np.zeros(n); a[1:1+N+1]=-row; A_ub.append(a); b_ub.append(1.0); names.append(f"box-{j},{xq}")
A_ub=np.array(A_ub); b_ub=np.array(b_ub)
res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
marg = np.asarray(res.ineqlin.marginals).ravel(); slack = b_ub - A_ub@res.x
active = [(names[i], float(marg[i])) for i in range(len(names)) if slack[i] < 1e-8 and abs(marg[i]) > 1e-12]
print("## active constraints at the optimum (dual != 0):")
for nm, ml in active: print(f"   {nm:16s} dual = {ml:.6e}")
out['active'] = active

json.dump(out, open('results.json','w'), indent=1)
print("\nsaved results.json")
