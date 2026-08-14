"""Model 3: planted-zero zeta-analogue (Beurling-flavoured).

Goal: a zeta-like object with a PLANTED zero at s0 = 1/2 + delta (off the critical line) and
strictly positive coefficients, to test whether a claim's mechanism would exclude it.

Construction:  Z(s) = zeta(s) * (1 + 2^(1/2+delta) * 2^(-s)).
The factor (1 + c*2^(-s)), c = 2^(1/2+delta), vanishes at  2^(-s) = -1/c
  <=>  s = -(log(1/c) + i(pi + 2 pi k)) / log 2  =  (1/2+delta) - i*(pi+2 pi k)/log 2   (note: log(1/c) = -(1/2+delta) log 2, and the minus sign outside).
So Z has infinitely many planted zeros at Re(s) = 1/2+delta, Im = -(pi+2pi k)/log 2, k in Z (i.e. +- i*(pi+2pi k)/log 2).
Numerically checked below: c = 2^0.6 = 1.5157..., 1 + c*2^(-s0) = 0 at s0 = 0.6 + i*pi/log 2.
Dirichlet coefficients:  Z(s) = sum_n a(n) n^(-s),  a(n) = 1 + c*[n even] > 0  (strictly positive).

HONEST GAP (stated, not hidden): a(n) is not 0/1, so Z is a zeta-ANALOGUE with positive
coefficients, not (yet) a genuine Beurling generalized-prime system.  Single-prime replacements
(finite modifications of the primes) provably cannot plant off-line zeros: every factor
(1 - p^(-s)) vanishes only on Re(s)=0.  The literature constructions of true 0/1 Beurling
systems with off-line zeros are genuinely involved; that step is INCOMPLETE here.  The planted
zero itself is EXACT (algebraic), verified below.

Run: uv run --quiet --with numpy python3 tools/barrier_zoo/model_beurling.py
"""
import mpmath as mp
from common import I

PI = mp.pi
LOG2 = mp.log(2)
DELTA = mp.mpf('0.1')


def coeff_positive_check(c):
    # a(n) = 1 + c*[n even]; verify positivity + the coefficient pattern for n=1..12
    out = []
    for n in range(1, 13):
        a = 1 + (c if n % 2 == 0 else 0)
        out.append((n, a))
    return out


def verify():
    print("== model_beurling: planted-zero zeta-analogue (model 3) ==")
    delta = DELTA
    c = 2 ** (mp.mpf(1) / 2 + delta)          # c > 1 so the zero of (1 + c*2^-s) sits at Re(s) = 1/2+delta
    s0 = (mp.mpf(1) / 2 + delta) + I * (PI / LOG2)          # planted zero, Re = 1/2 + delta
    print(f"  c = 2^(1/2+delta) = {mp.nstr(c, 10)}   planted zero s0 = {mp.nstr(mp.re(s0), 8)} + i*{mp.nstr(mp.im(s0), 8)}")
    print(f"  coefficients a(n) = 1 + c*[n even]  (first 12): "
          f"{[mp.nstr(v, 4) for _, v in coeff_positive_check(c)]}  -- all > 0")
    print(f"  |Z(s0)| = {mp.nstr(mp.fabs(mp.zeta(s0) * (1 + c * 2 ** (-s0))), 10)}   (exact planted zero)")
    s1 = mp.mpf('0.3') + I * mp.mpf('2.7')     # generic point: not a zero
    print(f"  |Z(0.3+2.7i)| = {mp.nstr(mp.fabs(mp.zeta(s1) * (1 + c * 2 ** (-s1))), 10)}   (generic point, nonzero)")
    zk = mp.mpf(1) / 2 + delta + I * (3 * PI / LOG2)       # second planted zero, k=1
    print(f"  |Z(s0 + i*2*pi/log2)| = {mp.nstr(mp.fabs(mp.zeta(zk) * (1 + c * 2 ** (-zk))), 10)}   (second planted zero)")
    assert mp.fabs(mp.zeta(s0) * (1 + c * 2 ** (-s0))) < mp.mpf('1e-30')
    assert mp.fabs(mp.zeta(zk) * (1 + c * 2 ** (-zk))) < mp.mpf('1e-30')
    print("VERDICT: planted zero at Re(s)=1/2+delta (delta=0.1) verified EXACTLY: a zeta-analogue "
          "with strictly positive coefficients and infinitely many zeros OFF the critical line. "
          "Positivity of coefficients alone implies nothing about the line. STATUS: planted-zero "
          "template PROVEN; realizability as a genuine 0/1 Beurling generalized-prime system "
          "INCOMPLETE (coefficients a(n) are 1 or 1+c, not 0/1; literature construction is hard).")
    return {'status': 'PROVEN planted zero / INCOMPLETE as Beurling system',
            's0': str(s0), 'coeffs_positive': True}


if __name__ == '__main__':
    verify()
