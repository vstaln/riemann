import json, numpy as np
from scipy.optimize import linprog
d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
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
n = 1 + (N+1) + N
c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG
A_ub=[]; b_ub=[]; names=[]
a=np.zeros(n); a[0]=1; a[1:1+N+1]=(s[:255] @ R[1:256,:]); A_ub.append(a); b_ub.append(p0); names.append("validity")
a=np.zeros(n); a[1+256]=1; A_ub.append(a); b_ub.append(1.0); names.append("slope+")
a=np.zeros(n); a[1+256]=-1; A_ub.append(a); b_ub.append(1.0); names.append("slope-")
for j in range(N):
    a=np.zeros(n); a[1+j]=-1; a[1+j+1]=1; a[1+N+1+j]=-1; A_ub.append(a); b_ub.append(0.0); names.append(f"epi{j}+")
    a=np.zeros(n); a[1+j]=1; a[1+j+1]=-1; a[1+N+1+j]=-1; A_ub.append(a); b_ub.append(0.0); names.append(f"epi{j}-")
a=np.zeros(n); a[1+N+1:1+N+1+N]=1; A_ub.append(a); b_ub.append(1.0); names.append("curvsum")
nbox=0
for xq in [0.0,0.25,0.5,0.75]:
    for j in range(N):
        t = xq
        if j == N-1 and xq == 0.0: continue
        row = R[j,:].copy(); row[j] += h*(t-t*t/2); row[j+1] += h*t*t/2
        a=np.zeros(n); a[1:1+N+1]=row; A_ub.append(a); b_ub.append(1.0); names.append(f"box+{j},{xq}"); nbox+=1
        a=np.zeros(n); a[1:1+N+1]=-row; A_ub.append(a); b_ub.append(1.0); names.append(f"box-{j},{xq}"); nbox+=1
A_ub=np.array(A_ub); b_ub=np.array(b_ub)
res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
marg = np.asarray(res.ineqlin.marginals).ravel(); slack = b_ub - A_ub@res.x
print("total box rows:", nbox, " total constraints:", len(names))
act = [(names[i], float(marg[i]), float(slack[i])) for i in range(len(names)) if slack[i] < 1e-7 and abs(marg[i]) > 1e-10]
for nm, ml, sk in act: print(f"  active: {nm:14s} dual={ml:.6e} slack={sk:.2e}")
# curvsum row status
i = names.index("curvsum")
print(f"curvsum: slack={slack[i]:.3e} dual={marg[i]:.6e}")
print("sum t =", res.x[1+N+1:].sum(), " C = 1")
# slope rows
i = names.index("slope+"); j = names.index("slope-")
print(f"slope+: slack={slack[i]:.3e} dual={marg[i]:.6e}   slope-: slack={slack[j]:.3e} dual={marg[j]:.6e}")
