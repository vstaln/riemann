#!/usr/bin/env python3
"""Derivative tower check: zeros of xi'' on the critical line (Farmer-style interlacing).

f(t) = xi(1/2+it) (real, even).  f'(t) = i*xi'(1/2+it) (real, odd); zeros: t=0, and one per
zeta-zero gap (gamma_n, gamma_{n+1}).  f''(t) = -xi''(1/2+it) (real, even); by Rolle it has
at least one zero in each interval between consecutive zeros of f': (0,u_1),(u_1,u_2),...
where u_n are the xi'-zeros.  We verify exactly one per interval, all simple.

xi''/xi = A^2 + A' with A = xi'/xi = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta,
A' = -1/s^2 - 1/(s-1)^2 + (1/4)psi'(s/2) + zeta''/zeta - (zeta'/zeta)^2.
Run:  uv run --quiet --with mpmath python check_tower.py   (60 digits)
"""
import time
import mpmath as mp

mp.mp.dps = 60
PI = mp.pi


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def A(s):
    return (1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(PI)
            + mp.mpf('0.5') * mp.psi(0, s / 2) + mp.zeta(s, derivative=1) / mp.zeta(s))


def Ad(s):
    zp = mp.zeta(s, derivative=1)
    return (-1 / s ** 2 - 1 / (s - 1) ** 2 + mp.mpf('0.25') * mp.psi(1, s / 2)
            + mp.zeta(s, derivative=2) / mp.zeta(s) - (zp / mp.zeta(s)) ** 2)


def H2(t):
    """-xi''(1/2+it), real; zeros = xi''-zeros on the line."""
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    v = -xi(s) * (A(s) ** 2 + Ad(s))
    return v.real, v.imag


def scan(f, a, b, step):
    out = []
    n = int((b - a) / step) + 1
    px, pf = a, f(a)
    for i in range(1, n + 1):
        x = a + i * step
        if x > b:
            x = b
        cur = f(x)
        if pf * cur < 0:
            out.append((px, x))
        px, pf = x, cur
        if x >= b:
            break
    return out


def root(f, a, b):
    fa = f(a)
    for _ in range(220):
        m = (a + b) / 2
        fm = f(m)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return (a + b) / 2


def main():
    # xi' zeros (u_n) from the independent small-t run
    us = ['15.5857085898293423445957292355', '22.0979772804009020982460583653',
          '26.2722473569356243750711540382', '31.2317958710097855089118960065',
          '34.1933102690113808807215179314', '38.4982407637544907213571745169',
          '41.7367295224193331427350981285', '44.5417036073809966272692376173',
          '48.6225326852778658468161729295', '50.8390048228159697828179099569',
          '53.9687288597224334661117413328', '57.2629341113391025140841206942',
          '59.9306989737258423521851881633', '62.1099057508713071858658957278',
          '65.7583193064237373440898606707', '67.9264537710552439462471054791',
          '70.418407142594909981414899509', '73.0605435210706675476179764859',
          '76.2254379706120628126703379202', '77.9978720250931747998206833418']
    us = [mp.mpf(u) for u in us]

    # xi''(1/2) sign check
    x2 = mp.diff(xi, mp.mpf('0.5'), 2)
    print(f"xi''(1/2) = {mp.nstr(x2, 20)}  (H2(0) = -xi''(1/2) = {mp.nstr(-x2, 20)})")

    # intervals: (0, u_1), (u_1, u_2), ..., (u_19, u_20)
    intervals = [(mp.mpf('0.001'), us[0])] + [(us[i], us[i + 1]) for i in range(len(us) - 1)]
    print(f"checking {len(intervals)} intervals between consecutive xi'-zeros (60 digits)")
    hist = {}
    t0 = time.time()
    for (a, b) in intervals:
        iv = scan(lambda t: H2(t)[0], a, b, (b - a) / 10)
        hist[len(iv)] = hist.get(len(iv), 0) + 1
        for (la, lb) in iv:
            r = root(lambda t: H2(t)[0], la, lb)
            # simplicity: |d/dt H2| at root
            h = mp.mpf('1e-6')
            d = (H2(r + h)[0] - H2(r - h)[0]) / (2 * h)
            print(f"  xi''-zero in ({mp.nstr(a, 8)}, {mp.nstr(b, 8)}): t = {mp.nstr(r, 25)}   |H2'| = {mp.nstr(abs(d), 5)}")
    print(f"interval histogram (xi'' zeros per interval): {dict(sorted(hist.items()))}")
    print(f"took {time.time()-t0:.1f}s")
    # note on H2 realness
    mx = max(abs(H2(mp.mpf('10.0'))[1]), abs(H2(mp.mpf('60.0'))[1]))
    print(f"max |Im H2| on samples = {mp.nstr(mx, 4)}")


if __name__ == '__main__':
    main()
