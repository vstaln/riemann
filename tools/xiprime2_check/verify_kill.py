#!/usr/bin/env python3
"""VERIFICATION of A^(2)(x) with more coefficient terms (k up to 3) to confirm the kill.
Run: uv run --quiet --with mpmath python /tmp/verify_kill.py
"""
import mpmath as mp
mp.mp.dps = 30
import math
from functools import lru_cache

def factor(n):
    f={}; m=n; p=2
    while p*p<=m:
        while m%p==0: f[p]=f.get(p,0)+1; m//=p
        p += 1 if p==2 else 2
    if m>1: f[m]=f.get(m,0)+1
    return f
def lam(n):
    if n==1: return 0.0
    f=factor(n)
    if len(f)==1 and 1 in f.values(): return math.log(list(f)[0])
    return 0.0
def lamlog(n): return lam(n)*math.log(n)
def lamlog2(n): return lam(n)*math.log(n)**2
@lru_cache(maxsize=None)
def divs(n):
    d=1; ds=[]
    while d*d<=n:
        if n%d==0:
            ds.append(d)
            if d!=n//d: ds.append(n//d)
        d+=1
    return ds
def conv(f,g,n): return sum(f(d)*g(n//d) for d in divs(n))

# alpha_3^(2): from the exact expansion W2 - L = Z + 2Z'/L + (Z'' - 2ZZ')/L^2 + (Z''' - 2ZZ'' - 2Z'Z' + 4Z^2Z')/L^3...
# Let me derive the L^-3 term: B3/B2 expanded to L^-3 (from the earlier sympy: the t^3 coefficient):
#   t^3: -2lp^2 + 2lp z^2 - 4 lp zp - 2 lpp z + 2 z^2 zp - 2 z zpp - 2 zp^2
#   dropping lp, lpp (L' ~ 0):  2 z^2 zp - 2 z zpp - 2 zp^2
#   In Dirichlet: z = -Lam, zp = -Lamlog, zpp = -Lamlog2:
#     z^2 zp = (Lam^{*2}) * (-Lamlog) -> - (Lam^{*2} * Lamlog) conv... signs:
#     z = -L, zp = -Llog, zpp = -Llog2.
#     2 z^2 zp = 2 (-L)^{*2} * (-Llog) = 2 (L*L) * (-Llog) conv = -2 conv(L*L, Llog)
#     -2 z zpp = -2 (-L)(-Llog2) = -2 (L * Llog2) conv = -2 conv(L, Llog2)
#     -2 zp^2 = -2 (-Llog)(-Llog) = -2 (Llog * Llog) conv = -2 conv(Llog, Llog)
#   alpha_3^(2) = -2 conv(L*L, Llog) - 2 conv(L, Llog2) - 2 conv(Llog, Llog)
def lam2(n): return conv(lam, lam, n)
def alpha2(k, n):
    if k==0: return -lam(n)
    if k==1: return -2*lamlog(n)
    if k==2: return -lamlog2(n) - 2*conv(lam, lamlog, n)
    if k==3: return -2*conv(lam2, lamlog, n) - 2*conv(lam, lamlog2, n) - 2*conv(lamlog, lamlog, n)
    return 0.0

def A2(x, L, K=3):
    tot = 0.0
    for n in range(1, int(x)+1):
        c = 0.0
        for k in range(K+1):
            a = alpha2(k, n)
            if a != 0: c += a/(L**k)
        tot += c*c
    return tot

print("=== A^(2)(x) with K=2 vs K=3 (truncation stability) ===")
L = 10.0
for x in [100, 200, 400]:
    a2k2 = A2(x, L, 2); a2k3 = A2(x, L, 3)
    print(f"  x={x}: A2(K=2) = {a2k2:.1f}  A2(K=3) = {a2k3:.1f}  ratio = {a2k3/a2k2:.3f}")
print()
print("=== A^(1)(x) for comparison (K=3) ===")
def alpha1(k,n):
    if k==0: return -lam(n)
    if k==1: return lamlog(n)
    if k==2: return conv(lamlog, lam, n)
    if k==3: return conv(lamlog, lam2, n)
    return 0.0
def A1(x, L, K=3):
    tot = 0.0
    for n in range(1, int(x)+1):
        c = 0.0
        for k in range(K+1):
            a = alpha1(k,n)
            if a != 0: c += a/(L**k)
        tot += c*c
    return tot
for x in [100, 200, 400]:
    a1 = A1(x, L); a2 = A2(x, L)
    print(f"  x={x}: A1 = {a1:.1f}  A2 = {a2:.1f}  A2/A1 = {a2/a1:.2f}")
