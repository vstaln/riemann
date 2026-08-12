import json, numpy as np
from scipy.optimize import linprog
d = json.load(open('../../../../tools/lpdual/law_data.json'))
s_mid = np.array(d['s_mid']); p0 = d['p0']; M0 = abs(d['E1'])
k=256; h=1.0/k
w = np.full(k+1, h); w[0]=h/2; w[k]=h/2
W = np.zeros((k+1,k+1))
for j in range(1,k+1):
    W[j,0]=h/2
    for i in range(1,j): W[j,i]=h
    W[j,j]=h/2
R = -np.outer(np.ones(k+1), w) + W
I = np.zeros(k+1); I[0]=h*h/6
for j in range(1,k): I[j]=j*h*h
I[k]=(k-1)/2*h*h+h*h/3
iG = I@R
def rcoef(x):
    j=int(np.floor(x*k));
    if j>=k: j=k-1
    t=x*k-j
    row=R[j,:].copy(); row[j]+=h*(t-t*t/2); row[j+1]+=h*t*t/2
    return row
def build(M,B,C,box=True):
    n=1+(k+1)+k
    c=np.zeros(n); c[0]=1; c[1:1+k+1]=iG
    A,b=[],[]
    a=np.zeros(n); a[0]=1
    for i in range(1,min(M,255)+1):
        a[1:1+k+1]+=s_mid[i-1]*rcoef(i/256.0)
    A.append(a); b.append(p0)
    a=np.zeros(n); a[1+k]=1; A.append(a); b.append(B)
    a=np.zeros(n); a[1+k]=-1; A.append(a); b.append(B)
    for j in range(1,k+1):
        a=np.zeros(n); a[1+j]=1; a[1+j-1]=-1; a[1+k+j-1]=-1; A.append(a); b.append(0)
        a=np.zeros(n); a[1+j]=-1; a[1+j-1]=1; a[1+k+j-1]=-1; A.append(a); b.append(0)
    a=np.zeros(n); a[1+k:1+k+k]=1; A.append(a); b.append(C)
    if box:
        for j in range(k):
            for xq in [0.0,0.25,0.5,0.75]:
                if j==k-1 and xq==0.0: continue
                row=rcoef((j+xq)/k)
                a=np.zeros(n); a[1:1+k+1]=row; A.append(a); b.append(1)
                a=np.zeros(n); a[1:1+k+1]=-row; A.append(a); b.append(1)
    A=np.array(A); b=np.array(b)
    res=linprog(-c,A_ub=A,b_ub=b,bounds=[(None,None)]*n,method='highs')
    return res
# C=0 case: g must be constant
res = build(255,1,0,box=True)
print("B=1 C=0 box:", res.success, -res.fun)
g = res.x[1:1+k+1]
print("g[0],g[128],g[256]:", g[0], g[128], g[256])
print("max|g-g_avg|:", np.max(np.abs(g-g.mean())), "g_avg:", g.mean())
# check r(x)=1-x feasibility manually: g = -1 constant
c=np.zeros(1+k+1+k); c[0]=1; c[1:1+k+1]=iG
gtest = -np.ones(k+1)
v = c[0]*res.x[0] + 0
# objective value for g=-1, c0 = p0 - sum s r
r = R@gtest
c0 = p0 - s_mid[:255]@r[1:256]
val = c0 + iG@gtest
print("manual r=1-x: c0 =", c0, "v =", val, " (= p0+|E1| ?)", val-(p0+M0))
print("r(0):", r[0], " r(1):", r[256])
