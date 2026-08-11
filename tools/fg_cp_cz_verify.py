#!/usr/bin/env python3
"""
fg_cp_cz_verify.py — numeric verification of the constants in
Fazzari–Gerspach (arXiv:2412.20099), "The third moment of the logarithm of zeta
and a twisted pair correlation conjecture".

All results CHECKED NUMERICALLY (mpmath, 60 digits). Run:
    uv run --with mpmath --quiet python tools/fg_cp_cz_verify.py

Verified:
  1. c_P = (3/4) * sum_p sum_{m>=2} (1/(m p^m)) * sum_{k+l=m} 1/(k l)   (Thm 1.1 / Prop 3.1),
     with the identity  sum_{k+l=m} 1/(k l) = 2 H_{m-1}/m  (checked directly).
  2. c_Z = -pi^2/4 = (1/8) M_N'''(0) in the limit, M_N(s)=prod_{j=1}^N Gamma(j)Gamma(j+2s)/Gamma(j+s)^2:
     M_N'''(0) -> -2 pi^2 (numerically M_N'''(0) = -2 pi^2 + 6/N + O(1/N^2)).
  3. c_P = (1/8) a'''(0)  (the paper's identification), a(s)=prod_p (1-1/p)^{s^2}
     sum_m binom(s+m-1,m)^2 / p^m  (KS arithmetic factor). a'(0)=0, so a'''(0)=log-a'''(0).
     (Note: the s^3 coefficient of binom(s+m-1,m)^2 is 2 H_{m-1}/m^2, and
      a'''(0) = 6 * sum_p sum_m 2 H_{m-1}/(m^2 p^m);  the 6 is the factorial from the
      third derivative — the naive coefficient read-off is off by 6 and is WRONG.)
  4. c_P + c_Z = -2.2337...  (the conditional full third moment of Re log zeta, Thm 1.1).
  5. Prop 3.1 finite-x diagonal: S(x)=sum_{p^gamma<=x, gamma>=2}(1/(gamma p^gamma))
     sum_{alpha+beta=gamma} 1/(alpha beta)  ->  (4/3) c_P.
  6. Second-moment constant of (1.3): gamma + 1/2 + (1/2) sum_{p,m>=2}(1-m)/(m^2 p^m).
"""
from mpmath import mp, mpf, pi, log, gamma, diff, binomial, harmonic, sqrt, euler, exp, mpc

mp.dps = 60
PMAX = 2000
MMAX = 60


def primes_up_to(n):
    isp = [True] * (n + 1)
    isp[0] = isp[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isp[i]:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [i for i in range(2, n + 1) if isp[i]]


def cp():
    # identity check
    for m in range(2, 13):
        direct = mpf(0)
        for k in range(1, m):
            direct += mpf(1) / (k * (m - k))
        assert abs(direct - 2 * harmonic(m - 1) / m) < mpf(10) ** (-50)
    print("[ok] sum_{k+l=m} 1/(k l) = 2 H_{m-1}/m for m=2..12")
    s = mpf(0)
    for p in primes_up_to(PMAX):
        pm = mpf(p) ** 2
        for m in range(2, MMAX + 1):
            s += 2 * harmonic(m - 1) / (m * m * pm)
            pm *= p
    return mpf(3) / 4 * s


def cz_and_MN():
    c_Z = -pi ** 2 / 4
    print(f"c_Z = -pi^2/4  = {c_Z}")
    for N in (10, 50, 200, 800):
        def logMN(s):
            t = mpc(s)
            tot = mpf(0)
            for j in range(1, N + 1):
                tot += log(gamma(j + 2 * t)) - 2 * log(gamma(j + t))
            return tot
        lp3 = diff(logMN, 0, 3)
        print(f"  M_N'''(0), N={N:<4}: {mp.re(lp3):+.12f}   (limit -2 pi^2 = {-2 * pi ** 2:+.12f})")
    return c_Z


def a_third():
    pr = primes_up_to(2000)

    def la(s):
        s = mpc(s)
        tot = mpf(0)
        for p in pr:
            acc = mpf(0)
            pwm = mpf(1)
            for m in range(0, MMAX + 1):
                acc += binomial(s + m - 1, m) ** 2 * pwm
                pwm /= p
            tot += s * s * log(1 - mpf(1) / p) + log(acc)
        return tot

    a3 = diff(la, 0, 3)
    print(f"log a'''(0) (= a'''(0), Pmax={PMAX}, Mmax={MMAX}): {mp.re(a3):.15f}")
    return a3


def diagonal_sx():
    for x in (1000, 10000, 100000, 1000000):
        s = mpf(0)
        xr = int(x)
        for p in primes_up_to(xr):
            pk = p * p
            g = 2
            while pk <= xr:
                inner = mpf(0)
                for al in range(1, g):
                    inner += mpf(1) / (al * (g - al))
                s += inner / (g * pk)
                pk *= p
                g += 1
        print(f"  S(x={x:>8}): {s:.12f}")


def second_moment_const():
    s = mpf(0)
    for p in primes_up_to(PMAX):
        pm = mpf(p) ** 2
        for m in range(2, MMAX):
            s += (1 - m) / (m * m * pm)
            pm *= p
    return euler + mpf(1) / 2 + s / 2


if __name__ == "__main__":
    print("=" * 78)
    print("FG arXiv:2412.20099 — constant verification (CHECKED NUMERICALLY)")
    print("=" * 78)
    c_P = cp()
    c_Z = cz_and_MN()
    a3 = a_third()
    print()
    print(f"c_P (3/4 formula)                 = {c_P:.15f}")
    print(f"(1/8) a'''(0)                     = {mp.re(a3) / 8:.15f}")
    print(f"|c_P - (1/8)a'''(0)|              = {abs(c_P - mp.re(a3) / 8):.3e}   (should be ~ prime tail)")
    print(f"c_P + c_Z  (conditional 3rd moment)= {c_P + c_Z:.15f}")
    print()
    print("Prop 3.1 diagonal S(x) -> (4/3) c_P =", mpf(4) / 3 * c_P)
    diagonal_sx()
    print()
    print("Second-moment constant (1.3): gamma + 1/2 + (1/2) sum (1-m)/(m^2 p^m) =",
          f"{second_moment_const():.12f}")
