#!/usr/bin/env python3
"""Reproduce the XiPrime certificate constants from the D1 density (Lean Zeta23/XiPrime).

kappaXi(1, v) = [int v^2 + 2*int_0^1 D1(r)*(v*v)(r) dr] / (int v)^2
D1(r) = r - 4 r^2 + sum_k D1coeff(k) r^{2k+3},  D1coeff(k) = 2*4^{k+1} k!/(2k+2)!
vFlat = 1;  vQuartic(s) = 1 - (7/100)(2s)^2 - (51/200)(2s)^4.
Claimed: kappaXi(1,vFlat) in [kap9Flat, kap9Flat+eps9], 2-kappa1 >= 0.85838371, 3/2-kappa1/2 >= 0.92919185;
         kappaXi(1,vQuartic) in [kap9Quartic, kap9Quartic+eps9*(2777/3000)^2], 2-kappa1 >= 0.86864017, 3/2-kappa1/2 >= 0.93432008.
"""
import mpmath as mp

mp.mp.dps = 50
PI = mp.pi


def D1coeff(k):
    k = int(k)
    return 2 * mp.power(4, k + 1) * mp.factorial(k) / mp.factorial(2 * k + 2)


def D1(r, K=60):
    r = mp.mpf(r)
    s = r - 4 * r * r
    for k in range(K):
        s += D1coeff(k) * r ** (2 * k + 3)
    return s


def D1trunc1(r):
    r = mp.mpf(r)
    return r * (1 - 2 * r) ** 2


def vFlat(s):
    return mp.mpf(1)


def vQuartic(s):
    x = 2 * mp.mpf(s)
    return 1 - mp.mpf(7) / 100 * x * x - mp.mpf(51) / 200 * x ** 4


def vCos(s):
    return mp.cos(mp.sqrt(2) * mp.mpf(s))


def vConv(v, r):
    r = mp.mpf(r)
    return mp.quad(lambda s: v(s) * v(s + r), [-mp.mpf('0.5'), mp.mpf('0.5') - r])


def kappaXi(v, K=60):
    Iv = mp.quad(lambda s: v(s), [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: v(s) ** 2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    J = 2 * mp.quad(lambda r: D1(r, K) * vConv(v, r), [0, 1])
    return (Iv2 + J) / (Iv * Iv)


def main():
    eps9 = mp.mpf(1024) / mp.mpf(2990212875)
    kap9Flat = mp.mpf(100905635384) / mp.mpf(88388425125)
    kap9Quartic = mp.mpf(277244140547469154168336) / mp.mpf(245053976636191319722125)

    print("== D1 coefficients ==")
    for k in [0, 1, 2, 9]:
        print(f"  D1coeff({k}) = {mp.nstr(D1coeff(k), 20)}  (ratio to next: {mp.nstr(D1coeff(k+1)/D1coeff(k), 20)})")
    print(f"  D1coeff(9) should be 1024/3273645375 = {mp.nstr(mp.mpf(1024)/mp.mpf(3273645375), 20)}")
    print(f"  eps9 = {mp.nstr(eps9, 20)}")
    # D1 = D1trunc1 + tail, D1trunc1 = r(1-2r)^2
    r = mp.mpf('0.37')
    print(f"  D1(0.37) = {mp.nstr(D1(r), 20)},  D1trunc1(0.37) = {mp.nstr(D1trunc1(r), 20)},  diff = {mp.nstr(D1(r)-D1trunc1(r), 20)}")
    # D1 nonneg on [0,1]: sample min
    mn = min(D1(mp.mpf(x)) for x in [i/100 for i in range(101)])
    print(f"  min D1 on [0,1] grid = {mp.nstr(mn, 12)} (>=0 expected)")

    print("\n== kappaXi(1, v) at 50 digits ==")
    for name, v in [("vFlat", vFlat), ("vQuartic", vQuartic), ("vCos(sqrt2*s)", vCos)]:
        k1 = kappaXi(v)
        print(f"  {name:>16}: kappa1 = {mp.nstr(k1, 20)}   2-kappa1 = {mp.nstr(2-k1, 20)}   3/2-kappa1/2 = {mp.nstr(mp.mpf('1.5')-k1/2, 20)}")

    print("\n== bounds check ==")
    kf = kappaXi(vFlat)
    kq = kappaXi(vQuartic)
    print(f"  flat:    kap9Flat = {mp.nstr(kap9Flat, 20)}")
    print(f"           kappa1   = {mp.nstr(kf, 20)}")
    print(f"           kap9Flat+eps9 = {mp.nstr(kap9Flat+eps9, 20)}")
    print(f"           in [kap9Flat, kap9Flat+eps9]? {kap9Flat <= kf <= kap9Flat+eps9}")
    print(f"           2-kappa1  = {mp.nstr(2-kf, 20)}  >= 0.85838371? {2-kf >= mp.mpf('0.85838371')}")
    print(f"           1.5-kappa1/2 = {mp.nstr(mp.mpf('1.5')-kf/2, 20)}  >= 0.92919185? {mp.mpf('1.5')-kf/2 >= mp.mpf('0.92919185')}")
    q_eps = eps9 * (mp.mpf(2777)/mp.mpf(3000))**2
    print(f"  quartic: kap9Quartic = {mp.nstr(kap9Quartic, 20)}")
    print(f"           kappa1      = {mp.nstr(kq, 20)}")
    print(f"           kap9Q+eps9*(2777/3000)^2 = {mp.nstr(kap9Quartic+q_eps, 20)}")
    print(f"           in [kap9Quartic, +eps9*(2777/3000)^2]? {kap9Quartic <= kq <= kap9Quartic+q_eps}")
    print(f"           2-kappa1  = {mp.nstr(2-kq, 20)}  >= 0.86864017? {2-kq >= mp.mpf('0.86864017')}")
    print(f"           1.5-kappa1/2 = {mp.nstr(mp.mpf('1.5')-kq/2, 20)}  >= 0.93432008? {mp.mpf('1.5')-kq/2 >= mp.mpf('0.93432008')}")

    # published five-digit interface constants
    print("\n== published constants check (>= with strict >) ==")
    print(f"  flat:    2-kappa1 > 0.85838? {2-kf > mp.mpf('0.85838')};  1.5-k/2 > 0.92919? {mp.mpf('1.5')-kf/2 > mp.mpf('0.92919')}")
    print(f"  quartic: 2-kappa1 > 0.86864? {2-kq > mp.mpf('0.86864')};  1.5-k/2 > 0.93432? {mp.mpf('1.5')-kq/2 > mp.mpf('0.93432')}")


if __name__ == '__main__':
    main()
