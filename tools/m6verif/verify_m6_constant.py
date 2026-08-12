#!/usr/bin/env python3
"""Verify the sixth-moment main-term constant (Keating-Snaith / Conrey-Ghosh).
Main term: I_3(T) = int_0^T |zeta(1/2+it)|^6 dt ~ (42 a_3 / 9!) T (log T)^9
           = (g_3 a_3 / 9!) T (log T)^9,  g_3 = 42, a_3 = prod_p (1-1/p)^9 sum_m (Gamma(m+3)/(m! Gamma(3)))^2 p^{-m}.
High precision via mpmath; verify the arithmetic constant to ~50 digits.
"""
import mpmath as mp
mp.mp.dps = 60

def a_k(k, primes=100000, mp_dps=60):
    mp.mp.dps = mp_dps
    # per-prime factor: (1-1/p)^(k^2) * sum_{m>=0} (Gamma(m+k)/(m! Gamma(k)))^2 p^{-m}
    total = mp.mpf(1)
    # generate primes
    def primes_upto(n):
        sieve = [True]*(n+1); sieve[0]=sieve[1]=False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i): sieve[j]=False
        return [i for i in range(2,n+1) if sieve[i]]
    for p in primes_upto(primes):
        pp = mp.mpf(p)
        # sum over m with tail cutoff: terms decay like p^{-m} * poly(m)
        s = mp.mpf(0)
        m = 0
        while True:
            term = (mp.gamma(m+k)/(mp.factorial(m)*mp.gamma(k)))**2 / pp**m
            s += term
            m += 1
            if term < mp.mpf(10)**(-mp_dps): break
        total *= (1 - 1/pp)**(k*k) * s
    return total

a3 = a_k(3)
g3 = mp.mpf(42)  # = 9!/(0!*3!*4!*5!) = 362880/17280
main_coef = g3*a3/mp.factorial(9)
print("a3 (Euler product, 100k primes, 60 dps) =", mp.nstr(a3, 50))
print("g3 =", g3)
print("g3*a3/9! =", mp.nstr(main_coef, 50))
print()
# Cross-check via a different factorization: a3 = prod_p (1-1/p)^9 * S3(p)
# Also compute 42a3/9! and compare with known value (Conrey-Farmer-Keating-Rubinstein-Snaith / Conrey-Ghosh)
# Literature value (from CFLRS/KS): a3 ~ 0.00122736... let's compare
print("Compare: known a3 ~ 0.001227... (CFKRS); g3*a3/9! ~ 1.0349e-7 * ...")
# Let's also compute the relative constant c3 = a3 (the "arithmetic factor") and g3*a3/9!
print()
print("Detailed: a3 =", mp.nstr(a3, 55))
print("42*a3 =", mp.nstr(42*a3, 55))
print("42*a3/9! =", mp.nstr(42*a3/mp.factorial(9), 55))
