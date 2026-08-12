import json, numpy as np
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
    j=int(np.floor(x*k))
    if j>=k: j=k-1
    t=x*k-j
    row=R[j,:].copy(); row[j]+=h*(t-t*t/2); row[j+1]+=h*t*t/2
    return row
# candidate: g = -1 (constant), r = 1 - x
g = -np.ones(k+1)
r = R@g
print("r(0):", r[0], "r(1):", r[k], "min r:", r.min(), "max r:", r.max())
# validity: c0 + sum s r <= p0 ; sum over rows 1..255
sr = s_mid[:255] @ r[1:256]
c0 = p0 - sr
print("sum s r =", sr, " c0 =", c0)
print("validity tight?", abs(c0+sr-p0))
# objective
v = c0 + iG@g
print("objective v =", v, " vs p0+|E1| =", p0+M0)
# check box: r at knots and midpoints
maxr = 0
for j in range(k):
    for xq in [0.0,0.25,0.5,0.75]:
        if j==k-1 and xq==0.0: continue
        row = rcoef((j+xq)/k)
        val = row@g
        maxr = max(maxr, abs(val))
print("max |r(x)| over box samples:", maxr, "(must be <=1)")
# curvature: sum |g_j - g_{j-1}| = 0?  slope |g_k| = ?
print("curvature:", np.sum(np.abs(np.diff(g))), " slope |g_k|:", abs(g[-1]))
