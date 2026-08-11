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
sG = s @ R[1:N+1,:]

n = 1 + (N+1) + N
c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG
A_ub, b_ub = [], []
M = 255
a = np.zeros(n); a[0] = 1; a[1:1+N+1] = (s[:M] @ R[1:M+1,:]); A_ub.append(a); b_ub.append(p0)
B, C = 1.0, 0.0
a = np.zeros(n); a[1+256] = 1; A_ub.append(a); b_ub.append(B)
a = np.zeros(n); a[1+256] = -1; A_ub.append(a); b_ub.append(B)
for j in range(N):
    a = np.zeros(n); a[1+j] = -1; a[1+j+1] = 1; a[1+N+j] = -1; A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1+j] = 1; a[1+j+1] = -1; a[1+N+j] = -1; A_ub.append(a); b_ub.append(0.0)
a = np.zeros(n); a[1+N:1+2*N] = 1; A_ub.append(a); b_ub.append(C)
A_ub = np.array(A_ub); b_ub = np.array(b_ub)
res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
print("success:", res.success, res.message)
c0 = res.x[0]; g = res.x[1:1+N+1]; t = res.x[1+N:]
print("c0 =", c0, " v =", c0 + (iG@g))
print("g_256 =", g[256], " g_0 =", g[0], " max|Δg| =", np.abs(np.diff(g)).max())
print("validity slack =", p0 - (c0 + (s[:255] @ R[1:256,:])@g))
# evaluate every constraint row at the candidate (g=-1, c0=p0-sG_M g, t=0)
g1 = -np.ones(N+1); t1 = np.zeros(N); c0_1 = p0 - (s[:255] @ R[1:256,:])@g1
x1 = np.concatenate([[c0_1], g1, t1])
viol = A_ub@x1 - b_ub
print("max constraint violation at g=-1 point:", viol.max())
print("objective at g=0:", (-c@np.concatenate([[p0], np.zeros(N+1), np.zeros(N)])))
print("objective at g=-1:", (-c@x1))

# manually verify g=-1 point is feasible & better
g1 = -np.ones(N+1)
print("g=-1: r(0)=%f r(1)=%f  iG·g=%f  sG·g=%f" % ((R@g1)[0], (R@g1)[256], iG@g1, sG@g1))
c0_1 = p0 - sG@g1
print("  v(g=-1) =", c0_1 + iG@g1, " > p0?", c0_1 + iG@g1 > p0)
# check the epigraph constraint rows hold for g=-1, t=0
print("  slope rows: |g_256| =", abs(g1[256]), "<= 1 ok")
print("  epi rows: for all j, |g_{j+1}-g_j| =", np.abs(np.diff(g1)).max(), "<= 0 ok")
print("  sum t = 0 <= 0 ok")
print("  validity: c0 + sG·g =", c0_1 + sG@g1, "<= p0 =", p0, " ok:", c0_1 + sG@g1 <= p0)
