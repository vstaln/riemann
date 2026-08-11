"""Verify attack-kernel claims:
1. spectrum of T: v |-> int |u-v| v(v) on [-1/2,1/2]: largest pos eig ~2/2.4^2=0.347,
   most negative ~ -2/5.43^2 = -0.0679, so I+T min eig ~ 0.93 (positive definite).
2. v0(u)=cos(sqrt2 u): v0 + A(u) == const EXACTLY on the grid including boundary.
3. global minimizer of Q over free grid == cosine.
"""
import mpmath as mp
mp.mp.dps = 30

# --- discretize kernel K(u,v)=|u-v| on [-1/2,1/2], N points, midpoint rule ---
N = 800
h = 1.0 / N
us = [mp.mpf(i) * h + h / 2 - mp.mpf(1) / 2 for i in range(N)]
K = [[abs(u - v) for v in us] for u in us]
# multiply by h: (T f)(u) ~ sum_j |u-v_j| f(v_j) h
for i in range(N):
    for j in range(N):
        K[i][j] *= h
# eigendecomposition via mpmath
ev = sorted(mp.eig(mp.matrix(K), left=False, right=False))
print("discrete eigenvalues of T (N=%d):" % N)
print("  largest 3: ", [mp.nstr(e, 6) for e in ev[-3:]])
print("  smallest 3:", [mp.nstr(e, 6) for e in ev[:3]])
print("  min eigenvalue of I+T: %.6f" % float(1 + ev[0]))
print("  largest eigenvalue of I+T: %.6f" % float(1 + ev[-1]))
# analytic predictions
import math
# tanh(k/2)=2/k smallest k:
lo, hi = 2.0, 2.6
for _ in range(60):
    m = (lo + hi) / 2
    if (m / 2) * math.tanh(m / 2) > 1:
        hi = m
    else:
        lo = m
kpos = (lo + hi) / 2
print("analytic: k_pos = %.4f  lam_max = 2/k^2 = %.5f" % (kpos, 2 / kpos ** 2))
# tan(k/2) = -2/k smallest k in (pi, 2pi)
lo, hi = math.pi, 2 * math.pi
for _ in range(80):
    m = (lo + hi) / 2
    if math.tan(m / 2) < -2 / m:
        hi = m
    else:
        lo = m
kneg = (lo + hi) / 2
print("analytic: k_neg = %.4f  lam_min = -2/k^2 = %.5f  -> I+T min eig ~ %.5f" % (kneg, -2 / kneg ** 2, 1 - 2 / kneg ** 2))

# --- 2) v0 + A constant ---
def A(u):
    s = mp.mpf(0)
    for j in range(N):
        v = us[j]
        s += abs(u - v) * mp.cos(mp.sqrt(2) * v) * h
    return s
vals = [mp.cos(mp.sqrt(2) * u) + A(u) for u in us]
mx = max(abs(v - vals[N // 2]) for v in vals)
print("max deviation of cos(sqrt2 u)+A(u) from its midpoint value over grid: %.2e" % float(mx))
print("value at 0: cos(1/sqrt2)+ (1/sqrt2) sin(1/sqrt2) =", mp.nstr(mp.cos(1 / mp.sqrt(2)) + mp.sin(1 / mp.sqrt(2)) / mp.sqrt(2), 10))
print("cos(1/sqrt2) =", mp.nstr(mp.cos(1 / mp.sqrt(2)), 10), " (boundary value, nonzero)")

# --- 3) free-grid minimization of Q(v)= (int v^2 + intint |u-v| vv) / (int v)^2 ---
# solve (I+T) v = mu * 1  on the grid, then rescale so int v = 1; Q = (v,(I+T)v) since int v = 1
# Build matrix M = I + K
M = [[mp.mpf(1) if i == j else K[i][j] for j in range(N)] for i in range(N)]
b = [mp.mpf(1)] * N
sol = mp.lu_solve(M, b)
s = sum(sol) * h
sol = [x / s for x in sol]  # int v = 1
# Q = <v,(I+T)v> ; also compute the cosine's Q on the grid with int=1
Qv = sum(sol[i] * (sum(M[i][j] * sol[j] for j in range(N)) * h) for i in range(N)) * h
# cos normalized: c(u)=cos(sqrt2 u)/int cos
c = [mp.cos(mp.sqrt(2) * u) for u in us]
sc = sum(c) * h
c = [x / sc for x in c]
Qc = sum(c[i] * (sum(M[i][j] * c[j] for j in range(N)) * h) for i in range(N)) * h
print("free-grid Q* (no evenness): %.12f ; Q(cos/∫cos): %.12f ; diff %.2e" % (float(Qv), float(Qc), float(abs(Qv - Qc))))
print("asymmetry of free-grid minimizer (max |v(u) - v(-u)|):", float(max(abs(sol[i] - sol[N - 1 - i]) for i in range(N // 2))))
print("analytic Q: 1/2 + (1/sqrt2) cot(1/sqrt2) = %.12f" % float(mp.mpf(1) / 2 + mp.cot(1 / mp.sqrt(2)) / mp.sqrt(2)))
