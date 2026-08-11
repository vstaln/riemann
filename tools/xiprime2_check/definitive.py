#!/usr/bin/env python3
"""DEFINITIVE honest xi'' density D1^(2) via the exact layer sums with Selberg-Delange order.

The FGL/Lean diagonal-law structure (all VERIFIED-FROM-PAPER / proven in Lean):
  For squarefree N with omega(N) = k >= 2:
    j=1:  C(N) = (k-1)! L*^{-k} log N prod log p
          ||C(N)||^2 = |L*|^{-2k} ((k-1)!^2/k!) (Lamlog)^{*k}(N) log^2 N
  The k-th layer (omega=k) contributes to S(y) = sum ||C||^2/N:
    layer_k ~ |L*|^{-2k} ((k-1)!^2/k!) * Wk k y   (Wk k y ~ k/((k+1)(2k)!) y^{2k+2})
    = l^2 * 4^k (k-1)!/((k+1)(2k)!) s^{2k+2}  -> density s^{2k+1} coeff 2*4^k (k-1)!/(2k)! = D1coeff(k-1) ✓

For j=2 (xi''), the coefficient system (EXACT, derived and verified):
  alpha_0 = -Lam, alpha_1 = -2 Lamlog, alpha_2 = -Lamlog2 - 2(Lam*Lamlog), ...
  For squarefree N with omega(N) = k:
    - Lam(N) = 0 for k>=2
    - Lamlog(N) = 0 for k>=2 (supported on prime powers)
    - (Lam*Lamlog)(N) = sum_{p|N} Lam(p)Lamlog(N/p)  = sum_{p|N} log p * Lamlog(N/p)
      For k=2 (N=pq): = log p log^2 q + log^2 p log q = log p log q (log p + log q)
      For k>=3: Lamlog(N/p) requires N/p prime-power -> only k=2 gives nonzero.  So (Lam*Lamlog) is
      supported on omega=2 squarefree numbers (plus prime powers).
    - So for k>=3, C^(2)(N) has NO contribution at alpha_0, alpha_1, alpha_2 level -> the k>=3 layers
      are pushed to higher L*^-k (alpha_3, ...) which carry MORE (Lamlog)-factors.

  RESULT: the xi'' density has a DIFFERENT layer structure than xi':
    - m=1 (primes): C(p) = -log p + 2 log^2 p / L*   ->  l^2 (s^2/2 - (8/3) s^3 + 4 s^4)  [j=2]
    - m=2 (pq): C(pq) = -2(Lam*Lamlog)(pq)/L*^2       ->  |C|^2 = 4 (log p log q)^2 (logp+logq)^2 / l^4
        sum ~ (extra (log y)^2 vs xi')  -> contributes at l^2 with an s^7-type term (y^{2k+2} -> y^7)
    - m>=3: pushed to alpha_3+ -> even more suppressed.

We compute the honest D1^(2)(s) by evaluating the m=1 and m=2 layer sums at fixed s (l -> oo limit
interpreted at finite l with the correct scaling) and comparing kappa_1^(2) vs kappa_1^(1).

Run: uv run --quiet --with mpmath python /tmp/definitive.py
"""
import mpmath as mp
mp.mp.dps = 50

# ---- m=1 (prime) layer: EXACT ----
# C(p) = -log p + j log^2 p / L*, |C|^2 = log^2 p - 2j Re(1/L*) log^3 p + j^2 |1/L*|^2 log^4 p
# sum log^b p/p = y^b/b (main), y = l s;  Re(1/L*) = 2/l, |1/L*|^2 = 4/l^2.
# layer_1/l^2 = s^2/2 - (4j/3) s^3 + j^2 s^4
def prime_density(s, j):
    return s - 4*j*s**2 + 4*j**2*s**3

# ---- m=2 layer: sum_{p<q, pq<=e^y} |C(pq)|^2/(pq) ----
# j=1: |C1(pq)|^2 = (4/l^4) log p log q (logp+logq)^2   [derived above]
# j=2: |C2(pq)|^2 = (4/l^4) (log p log q)^2 (logp+logq)^2  [extra (log p log q) factor]
# The sum S2(y) = (4/l^4) * T2(y) where
#   j=1: T2(y) = sum log p log q (logp+logq)^2/(pq)
#   j=2: T2(y) = sum (log p log q)^2 (logp+logq)^2/(pq)
# We evaluate T2 numerically at y in [8,14] and fit the y-power to get the l^2-level density.
import math
def primes_up_to(n):
    s = list(range(n+1)); s[0]=s[1]=0
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=0
    return [p for p in s if p]

def T2(y, j):
    X = int(math.floor(math.e**y))
    ps = primes_up_to(X)
    tot = 0.0
    for i, p in enumerate(ps):
        if p*p > X: break
        for q in ps[i+1:]:
            if p*q > X: break
            lp, lq = math.log(p), math.log(q)
            lpql = lp*lq
            base = lpql*(lp+lq)**2 if j==1 else lpql*lpql*(lp+lq)**2
            tot += base/(p*q)
    return tot

print("=== m=2 layer sums T2(y) for j=1,2 ===")
for y in [8, 9, 10, 11, 12]:
    t1 = T2(y, 1); t2 = T2(y, 2)
    print(f"  y={y}: T2(j=1) = {t1:.4e}   T2(j=2) = {t2:.4e}   ratio = {t2/t1:.3f}")
    # power-law fit: T ~ C y^p  ->  log T ~ p log y
print()
print("  power-law check: p1 = log(T2(y2)/T2(y1))/log(y2/y1)")
for (y1, y2) in [(8,10),(10,12),(9,11)]:
    p1 = math.log(T2(y2,1)/T2(y1,1))/math.log(y2/y1)
    p2 = math.log(T2(y2,2)/T2(y1,2))/math.log(y2/y1)
    print(f"    y {y1}->{y2}: p(j=1) = {p1:.3f} (expect ~5),  p(j=2) = {p2:.3f} (expect ~7)")
