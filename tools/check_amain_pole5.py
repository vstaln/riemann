"""Verify: partial sums of a_2(n) from zeta'/zeta * zeta'^2  ~  -X (log X)^4 / 4!  (order-5 pole at s=1).
zeta'/zeta = -sum Lambda(n)/n^s ;  zeta' = -sum log(n)/n^s ;  zeta'^2 = sum g(n)/n^s, g(n) = sum_{d|n} log d log(n/d).
a_2 = (-Lambda) * g  (Dirichlet convolution)  =>  a_2(n) = -sum_{d|n} Lambda(d) g(n/d).
Conjecture (standard Perron/Shapiro): sum_{n<=X} a_2(n) ~ -X (log X)^4 / 4!.
This is the q=1 (k=1) piece of M_2 for B=1; -2 Re(M_2) ~ + (T/2pi) L^4/12, matching Gonek J1 ~ L^3/12.
"""
import math
from functools import lru_cache

X = 2 * 10**5
# smallest prime factor sieve
spf = list(range(X + 1))
for i in range(2, int(X**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, X + 1, i):
            if spf[j] == j: spf[j] = i

logv = [0.0] * (X + 1)
for n in range(2, X + 1):
    logv[n] = math.log(n)

def lam(n):
    # von Mangoldt: log p if n = p^k
    p = spf[n]
    m = n
    while m % p == 0: m //= p
    return logv[p] if m == 1 else 0.0

def g(n):
    # sum_{d|n} log d * log(n/d)
    s = 0.0
    d = 1
    while d * d <= n:
        if n % d == 0:
            s += logv[d] * logv[n // d]
            if d != n // d:
                s += logv[n // d] * logv[d]
        d += 1
    return s

# a_2(n) = -sum_{d|n} Lambda(d) g(n/d)
S = 0.0
Slog = 0.0
for n in range(2, X + 1):
    # sum over prime powers d | n
    a = 0.0
    p = spf[n]
    # iterate divisors via prime-power accumulation is expensive; instead use divisor loop with Lambda check
    m = n
    # enumerate d|n by trial: use known formula - sum_{p^k || ... } - simpler: loop divisors
    d = 1
    ld = 0.0
    while d * d <= n:
        if n % d == 0:
            for dd in {d, n // d}:
                if dd > 1 and lam(dd) > 0:
                    a -= lam(dd) * g(n // dd)
        d += 1
    S += a
    if n % 50000 == 0:
        pred = -n * (logv[n])**4 / 24.0
        print(f"X={n}: S={S:.6e}  pred={pred:.6e}  ratio={S/pred:.4f}")
print("done; 1/24 =", 1/24)
