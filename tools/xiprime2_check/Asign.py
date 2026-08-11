#!/usr/bin/env python3
"""FINAL honest computation: D1^(2) and kappa_1^(2) from the FORM FACTOR structure.

VERIFIED-FROM-PAPER (FGL Theorem 1.1 + (5.11)-(5.14)):
  F_1(alpha) = |alpha| + (1+o(1)) alpha T^{1-2|alpha|} log T (1 - 4|alpha| + 2 sum_{k>=1} (k-1)!/(2k)! (2|alpha|)^{2k}) + o(1)
  The pair density D1(r) is the Fourier-transform side: D1(r) = r - 4r^2 + sum D1coeff(k) r^{2k+3}.
  Mapping: |alpha|-ramp -> r (density);  the -4|alpha| -> -4r^2; the 2(k-1)!/(2k)!(2|alpha|)^{2k}
  -> D1coeff(k-1) r^{2k+1}-type terms (with D1coeff(k-1) = 2*4^k (k-1)!/(2k)!).

For xi'' (j=2), the alpha_k^(2) coefficient system (EXACT, verified):
  alpha_0 = -Lam, alpha_1 = -2 Lamlog, alpha_2 = -Lamlog2 - 2(Lam*Lamlog), ...
The A(x) = sum |sum alpha_k/L^k|^2 has:
  A_{0,1} cross term: doubled (factor 2)  ->  the -4|alpha| in F_1 becomes -8|alpha|
  A_{1,1} = 4 (Lamlog)^2               ->  the (2|alpha|)^2-term coefficient 4x
  A_{k,k} for k>=2: new log^2-structure (Lamlog2 terms) -> higher-order corrections
The honest xi'' form factor:  F_1^(2)(alpha) = |alpha| + alpha T^{1-2|alpha|} log T (1 - 8|alpha| + 2*4 sum_{k>=1}(k-1)!/(2k)!(2|alpha|)^{2k} + ...) 
  -> density D1^(2)(r) = r - 8 r^2 + 16 r^3 + 4 sum_{k>=1} D1coeff(k) r^{2k+3} (the k>=1 terms scaled by 4)
  BUT the -8r^2 with the +16r^3 + 4*(...) is what we computed: kappa^(2) ~ 1.90.  That's WORSE.
  
Hmm.  Is that the honest answer, or is my "cross term doubles" wrong?  Let me think about the SIGN.
For xi', A_{0,1}(x) = sum_{n<=x} alpha_0(n) alpha_1(n) = sum -Lam(n) * Lamlog(n) = -sum Lam^2(n) log n
  ~ -x log^2 x (Lam^2 supported on primes ~ sum log^2 p ~ x log x... wait sum_{p<=x} log^3 p/p ... no,
  A_{0,1} = sum_{n<=x} -Lam(n) Lamlog(n) = -sum_{p<=x} log p * log^2 p = -sum log^3 p ~ -x log^2 x?? 
  The A(x) formula: A(x) = x log x (1 - 2 logx/L + ...) — the 2logx/L = A_{0,1}-type term.  A_{0,1} ~ x log^2 x (one log from sum Lam^2, one from the L-normalization).
For xi'', A_{0,1} = sum -Lam * (-2 Lamlog) = +2 sum Lam Lamlog = +2 sum log^3 p ~ +2 x log^2 x.
  So the cross term changes sign AND doubles!  The -2(logx/L) becomes +4(logx/L) -> the -4r^2 becomes +8r^2 ?!
  This would make D1^(2)(r) = r + 8r^2 + ... — POSITIVE cross term, and kappa SMALLER (better)!
  I need to get the SIGN right.  The FGL A(x) has "-2(logx/L)": the minus sign comes from
  Re(alpha_0 conj(alpha_1)/L) = Re(-Lam * conj(Lamlog)/L) = Re(-Lam Lamlog / L) = -(Lam Lamlog)/L real
  = -Lam^2 log n / L -> summed -x log^2 x / L -> in A(x) = x log x(...): the term -2 logx/L * x logx = -2 x log^2 x / L ✓.
  For xi'': Re(alpha_0 conj(alpha_1)/L) with alpha_1 = -2 Lamlog: Re(-Lam * conj(-2Lamlog)/L) = Re(+2 Lam Lamlog / L) = +2 Lam^2 log n / L
  -> +2 x log^2 x / L -> in A(x): +4 x log^2 x / L... wait: A(x) = x logx (1 - 2 logx/L + ...): the coefficient of logx/L is -2 for xi'.
  For xi'': +4 (logx/L)?  The cross term is 2 Re(alpha_0 conj(alpha_1)) summed / L = 2 * (+2 x log^2 x)/L = 4 x log^2 x/L
  -> A^(2)(x) = x log x (1 + 4 logx/L + ...)  -> F_1^(2) = |alpha|(1 + 4|alpha| + ...) -> D1^(2)(r) = r + 8r^2 + ...
  WAIT that changes the SIGN of the -4r^2!  Let me double check with the known F_1: F_1(alpha) = |alpha| + alpha T^{1-2alpha} logT (1 - 4 alpha + ...).
  The -4 alpha: from 2 Re(alpha_0 conj alpha_1)/L * (something) ... 

OK I clearly need to be extremely careful with signs and normalizations.  Let me just directly COMPUTE the 
honest A^(2)(x) numerically from the exact alpha_k^(2), and compare with A^(1)(x) = the paper's (5.8).
This removes ALL sign/normalization ambiguity.
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

# coefficient systems
def alpha1(k,n):
    if k==0: return -lam(n)
    if k==1: return lamlog(n)
    if k==2: return conv(lamlog, lam, n)   # (Lamlog)*Lam
    return 0.0
def alpha2(k,n):
    if k==0: return -lam(n)
    if k==1: return -2*lamlog(n)
    if k==2: return -lamlog2(n) - 2*conv(lam, lamlog, n)
    return 0.0

def A(x, j, L):
    """A_j(x) = sum_{n<=x} |sum_{k<=2} alpha_k^(j)(n)/L^k|^2"""
    tot = 0.0
    X = int(x)
    for n in range(1, X+1):
        c = 0.0
        for k in range(3):
            a = (alpha1(k,n) if j==1 else alpha2(k,n))
            if a != 0: c += a/(L**k)
        tot += c*c
    return tot

# The paper's A(x) (5.8) at L = 10, x = e^v:
def Apaper(x, L, K=8):
    lx = math.log(x)
    tot = x*lx*(1 - 2*(lx/L) + sum(2*math.factorial(k-1)/math.factorial(2*k)*(lx/L)**(2*k) for k in range(1,K+1)))
    return tot

print("=== A^(j)(x) vs the paper's A(x): signs and coefficients ===")
L = 10.0
for x in [50, 100, 200, 500]:
    a1 = A(x, 1, L); a2 = A(x, 2, L); ap = Apaper(x, L)
    print(f"  x={x:4d}: A^(1)={a1:14.3f}  A^(2)={a2:14.3f}  A_paper={ap:14.3f}  A2-A1={a2-a1:12.3f}")
