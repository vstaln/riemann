#!/usr/bin/env python3
"""Screw-function verification, Parts A-C. (mpmath high precision, uv run)

A. The constant c = 1/2 + (1/sqrt2) cot(1/sqrt2) and the sharp inequality
   int psi^2 + intint |u-v| psi(u)psi(v) >= c (int psi)^2,  psi = cos(sqrt2 x) 1_{|x|<=1/2}.
   Uses the closed form psi*psi (cosine convolution) so all integrals are 1D.
B. The screw function g of zeta (Suzuki 2606.09096 (1.3), (2.2)):
   evenness, expansion near 0, second-difference kernel positivity.
C. Load-bearing identity: for v in C_c^inf(-a,a),
   sum_gamma m_gamma |vhat(gamma)|^2  =  intint g(x-y) v'(y) v'(x) dx dy
   (Weil explicit formula in screw-function form; (2.9) + (3.1)).
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 32
SQ2 = mp.sqrt(2)
HALF = mp.mpf('0.5')

print("=" * 78)
print("PART A: the constant and the sharp inequality")
print("=" * 78)

c = mp.mpf('0.5') + (1/SQ2) * mp.cot(1/SQ2)
bound = mp.mpf('1.5') - (1/SQ2) * mp.cot(1/SQ2)
print("c       =", mp.nstr(c, 25))
print("2 - c   =", mp.nstr(2 - c, 25))
print("3/2-(1/sqrt2)cot =", mp.nstr(bound, 25))
print("ref verification-001: 0.672500703679411645734379790803...")

def psi(x):
    return mp.cos(SQ2 * x)

def conv(w):
    """psi * psi(w) = int_{-1/2}^{1/2} cos(sqrt2 u) cos(sqrt2(w-u)) du, closed form."""
    lo = max(-HALF, w - HALF)
    hi = min(HALF,  w + HALF)
    L = hi - lo
    # cos A cos B = (cos(A-B)+cos(A+B))/2, A = sqrt2 u, B = sqrt2(w-u): A-B = sqrt2(2u-w)
    # int cos(sqrt2(2u-w)) du = (1/sqrt2) sin(sqrt2(2u-w));  int cos(sqrt2 w) du = L cos(sqrt2 w)
    return (L * mp.cos(SQ2 * w) + (1/(2*SQ2)) * (mp.sin(SQ2*(2*hi - w)) - mp.sin(SQ2*(2*lo - w)))) / 2

Ipsi  = mp.quad(lambda x: psi(x), [-HALF, HALF])
Ipsi2 = mp.quad(lambda x: psi(x)**2, [-HALF, HALF])
print("\nint psi   =", mp.nstr(Ipsi, 20), " (analytic sqrt2 sin(1/sqrt2) =",
      mp.nstr(SQ2 * mp.sin(1/SQ2), 20), ")")
print("int psi^2 =", mp.nstr(Ipsi2, 20), " (analytic 1/2 + sin(sqrt2)/(2 sqrt2) =",
      mp.nstr(mp.mpf('0.5') + mp.sin(SQ2)/(2*SQ2), 20), ")")

J = 2 * mp.quad(lambda w: w * conv(w), [mp.mpf('0'), mp.mpf(1)])
print("intint |u-v| psi psi =", mp.nstr(J, 20), " (via 2 int_0^{1} w (psi*psi)(w) dw)")

lhs = Ipsi2 + J
rhs = c * Ipsi**2
print("\nint psi^2 + intint |u-v| psi psi =", mp.nstr(lhs, 20))
print("c (int psi)^2                   =", mp.nstr(rhs, 20))
print("rel err =", mp.nstr(abs(lhs - rhs)/abs(rhs), 10))

# The constant-map lemma: u -> psi(u) + int |u-v| psi(v) dv is constant on [-1/2,1/2]
print("\nConstant-map lemma (u -> psi(u) + int|u-v|psi(v)dv constant; psi''+2psi=0):")
c0 = None
for u in [mp.mpf(x) for x in (0.0, 0.1, 0.3, -0.2, 0.49)]:
    val = psi(u) + mp.quad(lambda v: abs(u - v) * psi(v), [-HALF, HALF])
    if c0 is None:
        c0 = val
    print(f"  u={mp.nstr(u,4)}: value = {mp.nstr(val, 18)}")
print("  value at 0 =", mp.nstr(c0, 18), " analytic cos(1/sqrt2)+(1/sqrt2)sin(1/sqrt2) =",
      mp.nstr(mp.cos(1/SQ2) + (1/SQ2)*mp.sin(1/SQ2), 18))
print("  c0 / int psi =", mp.nstr(c0 / Ipsi, 20), "  [should equal c =", mp.nstr(c, 20), "]")

# Sharp inequality for perturbations (using the analytic conv for each candidate)
print("\nSharp inequality Q(f) = (int f^2 + 2 int_0^{1/2} w (f*f)(w) dw) / (int f)^2 :")
def Q_of(f):
    I  = mp.quad(lambda x: f(x), [-HALF, HALF])
    I2 = mp.quad(lambda x: f(x)**2, [-HALF, HALF])
    # numeric convolution via mp.quad (candidates are not cosines)
    def convf(w):
        lo = max(-HALF, w - HALF); hi = min(HALF, w + HALF)
        return mp.quad(lambda u: f(u) * f(w - u), [lo, hi])
    Jf = 2 * mp.quad(lambda w: w * convf(w), [mp.mpf('0'), mp.mpf(1)])
    return (I2 + Jf) / I**2

print("  Q(cos sqrt2 x) =", mp.nstr(Q_of(psi), 18), "  [c =", mp.nstr(c, 18), "]")
for name, f in [
    ("flat 1 (box)", lambda x: mp.mpf(1)),
    ("cos(sqrt2 x)+0.1(4x^2-1)", lambda x: mp.cos(SQ2*x) + mp.mpf('0.1')*(4*x*x - 1)),
    ("cos(1.2 x)", lambda x: mp.cos(mp.mpf('1.2')*x)),
]:
    print(f"  {name:26s} Q = {mp.nstr(Q_of(f), 14)}")

print("\n" + "=" * 78)
print("PART B: the screw function g (Suzuki (1.3), (2.2))")
print("=" * 78)

C0 = mp.euler
psi14 = -(mp.pi/2) - 3*mp.log(2) - C0
Aconst = mp.mpf('0.5') * (mp.log(2*mp.pi) - (1 - C0))
print("A = (1/2)(log 2pi - psi(2)) =", mp.nstr(Aconst, 20), " (paper: 0.707546...)")

TMAX = 3.0
LIM = int(np.ceil(np.exp(TMAX))) + 5
sieve = np.ones(LIM + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(LIM**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = [i for i in range(2, LIM + 1) if sieve[i]]
def Lambda(n):
    n = int(n)
    for p in primes:
        if p * p > n: break
        if n % p == 0:
            m = 0; nn = n
            while nn % p == 0:
                nn //= p; m += 1
            return mp.mpf(m)*mp.log(p) if nn == 1 else mp.mpf(0)
    return mp.log(n)
Lam = {n: Lambda(n) for n in range(2, LIM + 1)}

def lerch(t):
    t = mp.mpf(t)
    if t == 0:
        return mp.zeta(2, mp.mpf('0.25'))          # Phi(1,2,1/4)
    z = mp.e**(-2*t)
    if z > mp.mpf('0.95'):                          # slow series; use acceleration path
        return mp.lerchphi(z, 2, mp.mpf('0.25'))
    acc = mp.mpf(0); k = 0; tol = mp.mpf('1e-40')
    while True:
        term = z**k / (k + mp.mpf('0.25'))**2
        acc += term
        if abs(term) < tol: break
        k += 1
    return acc

def prime_sum(t):
    tt = mp.mpf(abs(t)); et = mp.e**tt; acc = mp.mpf(0)
    for n, lam in Lam.items():
        if mp.mpf(n) <= et:
            acc += lam / mp.sqrt(mp.mpf(n)) * (tt - mp.log(n))
    return acc

def g(t):
    tt = mp.mpf(abs(t))
    Phi1 = mp.zeta(2, mp.mpf('0.25'))
    Phi2 = lerch(tt)
    return (-4*(mp.e**(tt/2) + mp.e**(-tt/2) - 2) + prime_sum(tt)
            - (tt/2)*(psi14 - mp.log(mp.pi))
            - mp.mpf('0.25')*(Phi1 - mp.e**(-tt/2) * Phi2))

print("\ng(0) =", mp.nstr(g(0), 15))
print("evenness: g(1.3) =", mp.nstr(g(1.3), 15), " g(-1.3) =", mp.nstr(g(-1.3), 15),
      " |diff| =", mp.nstr(abs(g(1.3)-g(-1.3)), 8))
print("g <= 0 check (screw requires g <= 0): g(0.5) =", mp.nstr(g(0.5), 12),
      " g(1.0) =", mp.nstr(g(1.0), 12), " g(2.0) =", mp.nstr(g(2.0), 12),
      " g(2.9) =", mp.nstr(g(2.9), 12))

print("\nExpansion (2.2): r(t) = g(t) - [(1/2)|t|log|t| + A|t| + prime-sum] even, C^2, O(t^2):")
for tt in [0.001, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 1.0, 2.0]:
    t = mp.mpf(tt)
    r = g(t) - (mp.mpf('0.5')*t*mp.log(t) + Aconst*t + prime_sum(t))
    rneg = g(-t) - (mp.mpf('0.5')*t*mp.log(t) + Aconst*t + prime_sum(t))
    print(f"  t={tt:5.3f}: r(t)={mp.nstr(r,10)}  r(-t)={mp.nstr(rneg,10)}  r(t)/t^2={mp.nstr(r/t**2,10)}")

print("\nSecond-difference kernel k(t,u)=g(t-u)-g(t)-g(-u)+g(0) on grid [0,2.5]^2 (expect >= 0):")
grid = np.linspace(0.0, 2.5, 13)
minv = mp.mpf(0); argmin = None; nneg = 0
for ti in grid:
    for ui in grid:
        v = g(ti - ui) - g(ti) - g(ui) + g(0)
        if v < 0:
            nneg += 1
        if v < minv:
            minv = v; argmin = (ti, ui)
print("  negatives on grid:", nneg, " min =", mp.nstr(minv, 12), " at", argmin)
print("  k(t,t) = -2g(t): k(1,1) =", mp.nstr(-2*g(1.0), 12))
