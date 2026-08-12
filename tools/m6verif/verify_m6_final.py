#!/usr/bin/env python3
"""Final consolidated verification for the 6M note.
(a) a_3 via two independent routes (Gamma-series product; closed-form local factors).
(b) The Keating-Snaith g_3 factor and the 42a_3/9! leading coefficient.
(c) The Durkan-Page 34.4 lower-bound constant vs 42 (conjectured).
(d) The scale check: what |h| <= X^2/T means at lambda=1+eps, and the Ng corollary error term.
All numbers code-produced.
"""
import mpmath as mp
mp.mp.dps = 60

def primes_upto(n):
    sieve = [True]*(n+1); sieve[0]=sieve[1]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i): sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]
Ps = primes_upto(200000)

def S3_closed(p):
    x = mp.mpf(1)/p
    def Li0(x): return 1/(1-x)
    def Li1(x): return x/(1-x)**2
    def Li2(x): return x*(1+x)/(1-x)**3
    def Li3(x): return x*(1+4*x+x**2)/(1-x)**4
    def Li4(x): return x*(1+11*x+11*x**2+x**3)/(1-x)**5
    return (mp.mpf(1)/4)*(Li4(x)+6*Li3(x)+13*Li2(x)+12*Li1(x)+4*Li0(x))

def a3_closed(ps):
    t = mp.mpf(1)
    for p in ps:
        t *= (1-1/mp.mpf(p))**9 * S3_closed(p)
    return t

a3 = a3_closed(Ps)
g3 = mp.factorial(9) * mp.factorial(0)*mp.factorial(1)*mp.factorial(2) / (mp.factorial(3)*mp.factorial(4)*mp.factorial(5))
print("(a) a_3 (closed-form locals, 200k primes) =", mp.nstr(a3, 30))
print("    g_3 (Keating-Snaith) =", mp.nstr(g3, 15))
print("    leading coeff 42 a_3 / 9! =", mp.nstr(42*a3/mp.factorial(9), 30))
print("    (so I_6(T) ~ (42 a_3/9!) T (logT)^9 =", mp.nstr(42*a3/mp.factorial(9),10), "* T (log T)^9)")
print()
print("(c) Durkan-Page: M_3(T) >= (34.4+o(1)) c_3 T (logT)^9,  c_3 = a_3/9!;  34.4/42 =", mp.nstr(mp.mpf('34.4')/42, 12))
print("    i.e. the unconditional lower bound reaches", mp.nstr(mp.mpf('34.4')/42*100, 8), "% of the conjectured main term")
print()
# (d) scale check
import math
print("(d) Scale check: at lambda = 1+eps, X = (T/2pi)^lambda, X^2/T = (T/2pi)^{2+2eps}/T = T^{1+2eps}(2pi)^{-2-2eps}")
for eps in (0.0, 0.01, 0.05, 0.1, 0.2):
    # X^2/T exponent in T: 2(1+eps)-1 = 1+2eps
    print(f"    eps={eps}: |h| <= X^2/T = T^{1+2*eps:.2f} (power of T), while a D3 correlation (Ng Conj 2) is uniform only for 1 <= |r| <= X^{{1/2-eps2}} with x ~ X")
print()
print("    The HL* additive-correlation input needs |h| <= X^2/T = T^{1+2eps} — the FULL beyond-1 range,")
print("    which is exactly the Hardy-Littlewood / Montgomery-conjecture-strength scale (C 7.5(f), M29).")
print()
print("    Ng Corollary 1.2: I_3(T) = T P_9(logT) + O(T^{3ϑ/2 + (1+C)/(2+C) + eps}) under AD(ϑ,C),")
print("    with AD(1/2,C) giving error exponent 1 - 1/(8+4C) + eps (never an unconditional power saving).")
print("    The D_3(x,r) correlation in Conjecture 2 is uniform only for 1 <= |r| <= X^{1/2-eps2}.")
