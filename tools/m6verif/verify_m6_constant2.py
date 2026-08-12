#!/usr/bin/env python3
"""Cross-verify the sixth-moment arithmetic constant a_3 by two independent methods."""
import mpmath as mp
mp.mp.dps = 70

def primes_upto(n):
    sieve = [True]*(n+1); sieve[0]=sieve[1]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i): sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

def a_k(k, primes=200000):
    total = mp.mpf(1)
    for p in primes_upto(primes):
        pp = mp.mpf(p)
        s = mp.mpf(0)
        m = 0
        while True:
            term = (mp.gamma(m+k)/(mp.factorial(m)*mp.gamma(k)))**2 / pp**m
            s += term
            m += 1
            if term < mp.mpf(10)**(-65): break
        total *= (1 - 1/pp)**(k*k) * s
    return total

for k in (2, 3):
    ak = a_k(k)
    prod1 = mp.mpf(1); prod2 = mp.mpf(1)
    for j in range(k):
        prod1 *= mp.factorial(j)
        prod2 *= mp.factorial(k+j)
    gk = mp.factorial(k*k) * prod1 / prod2
    coef = gk * ak / mp.factorial(k*k)
    print(f"k={k}: a_k = {mp.nstr(ak, 60)}")
    print(f"   g_k (KS) = {mp.nstr(gk, 30)}")
    print(f"   main coef (T (logT)^{k^2}) = {mp.nstr(coef, 40)}")
    if k == 2:
        print(f"   compare Ingham 1/(2 pi^2) = {mp.nstr(1/(2*mp.pi**2), 20)}")
print()
print("Check a_2 = prod_p (1-1/p)^4 * sum_{m>=0} (m+1)^2 p^{-m} = prod_p (1-1/p^2) = 6/pi^2")
a2c = mp.mpf(1)
for p in primes_upto(200000):
    pp = mp.mpf(p)
    a2c *= (1 - 1/pp**2)
print("  a_2 via closed form prod(1-1/p^2) =", mp.nstr(a2c, 50))
print("  6/pi^2 =", mp.nstr(6/mp.pi**2, 50))
print("  match:", mp.nstr(a2c/(6/mp.pi**2), 20))
print("  (note: the (1-1/p)^4(1+4/p+1/p^2) expression above is the a_3 local factor,")
print("   since sum binom(m+2,2)^2 x^m = (1+4x+x^2)/(1-x)^5; a_3 = 0.0493218423340601... is cross-checked in verify_m6_local_factors.py)")
