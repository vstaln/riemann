#!/usr/bin/env python3
"""Resolve the a_2 discrepancy: Gamma-series vs prod(1-1/p^2) = 6/pi^2."""
import mpmath as mp
mp.mp.dps = 70

def primes_upto(n):
    sieve = [True]*(n+1); sieve[0]=sieve[1]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i): sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

Ps = primes_upto(200000)

# Method 1: direct prod(1 - 1/p^2)
a2_direct = mp.mpf(1)
for p in Ps:
    a2_direct *= (1 - 1/mp.mpf(p)**2)
print("prod(1-1/p^2)            =", mp.nstr(a2_direct, 55))
print("6/pi^2                   =", mp.nstr(6/mp.pi**2, 55))
print("ratio                    =", mp.nstr(a2_direct/(6/mp.pi**2), 30))

# Method 2: Gamma-series, small-primes only (p <= 101) to isolate the issue
def a_k_gamma(k, ps):
    total = mp.mpf(1)
    for p in ps:
        pp = mp.mpf(p)
        s = mp.mpf(0); m = 0
        while True:
            term = (mp.gamma(m+k)/(mp.factorial(m)*mp.gamma(k)))**2 / pp**m
            s += term; m += 1
            if term < mp.mpf(10)**(-65): break
        total *= (1 - 1/pp)**(k*k) * s
    return total

Ps_small = primes_upto(100)
print()
print("Gamma-series a_2 (p<=100):", mp.nstr(a_k_gamma(2, Ps_small), 55))
print("direct a_2    (p<=100):   ", mp.nstr(a2_direct, 55))  # recompute restricted
a2_dir_small = mp.mpf(1)
for p in Ps_small:
    a2_dir_small *= (1 - 1/mp.mpf(p)**2)
print("direct a_2    (p<=100):   ", mp.nstr(a2_dir_small, 55))
print("ratio gamma/direct       =", mp.nstr(a_k_gamma(2, Ps_small)/a2_dir_small, 30))

# Method 3: explicit local factor at p=2,3,5 by direct summation vs closed form
for p in (2,3,5):
    x = mp.mpf(1)/p
    s = mp.mpf(0); m = 0
    while True:
        t = (m+1)**2 * x**m
        s += t; m += 1
        if t < mp.mpf(10)**(-60): break
    closed = (1+x)/(1-x)**3
    print(f"p={p}: sum(m+1)^2 p^-m = {mp.nstr(s,30)}  closed (1+x)/(1-x)^3 = {mp.nstr(closed,30)}  local=(1-x)^4*s = {mp.nstr((1-x)**4*s,30)}  1-1/p^2={mp.nstr(1-x**2,30)}")
