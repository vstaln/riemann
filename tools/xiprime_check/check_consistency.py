#!/usr/bin/env python3
"""Debug: which of H_direct / H_zform / complex-diff is the true d/dt xi(1/2+it)?"""
import mpmath as mp

mp.mp.dps = 60
PI = mp.pi


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lp(s):
    return (1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(PI)
            + mp.mpf('0.5') * mp.psi(0, s / 2) + mp.zeta(s, derivative=1) / mp.zeta(s))


def H_direct(t):
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    val = 1j * xi(s) * lp(s)
    return val.real, val.imag


def H_deriv_diff(t):
    """d/dt xi(1/2+it) by complex differentiation of xi: xi'(1/2+it) = (1/i) d/dt, so d/dt = i*xi'."""
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    xip = mp.diff(xi, s)  # complex derivative
    return (1j * xip).real, (1j * xip).imag


def H_zform(t):
    tt = mp.mpf(t)
    th = lambda u: mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * u / 2))) - u / 2 * mp.log(PI)
    Z = lambda u: (mp.exp(1j * th(u)) * mp.zeta(mp.mpf('0.5') + 1j * u)).real
    pp = 2 * tt / (tt * tt + mp.mpf('0.25')) - mp.mpf('0.5') * mp.im(
        mp.psi(0, mp.mpf('0.25') + 1j * tt / 2))
    Zp = mp.diff(Z, tt)
    return -(Z(tt) * pp + Zp)


print("== xi(1/2+it) realness + H consistency at t=13.9, 16.152, 15.5857, 50 ==")
for t in ['13.9', '16.152219566157', '15.5857085898', '50.0', '50.8390048']:
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    xv = xi(s)
    # theta & Z
    th = mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * mp.mpf(t) / 2))) - mp.mpf(t) / 2 * mp.log(PI)
    Zv = (mp.exp(1j * th) * mp.zeta(s)).real
    hd_r, hd_i = H_direct(t)
    hd2_r, hd2_i = H_deriv_diff(t)
    hz = H_zform(t)
    print(f" t={t:>16}")
    print(f"   xi        = {mp.nstr(xv.real, 12):>18} + i*{mp.nstr(xv.imag, 4)}")
    print(f"   Z (e^{{iθ}}ζ).real = {mp.nstr(Zv, 12)}")
    print(f"   H_direct  = {mp.nstr(hd_r, 15):>22}  (im={mp.nstr(hd_i,4)})")
    print(f"   H_dirdiff = {mp.nstr(hd2_r, 15):>22}  (im={mp.nstr(hd2_i,4)})")
    print(f"   H_zform   = {mp.nstr(hz, 15):>22}")

print("\n== scan gap 1 (14.13,21.02) at fine step to find all sign changes ==")


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


g1, g2 = mp.mpf('14.1347251417346937904572519835625'), mp.mpf('21.0220396387715549926284795938969')
intervals = scan(lambda t: H_direct(t)[0], g1 + mp.mpf('0.001'), g2 - mp.mpf('0.001'), mp.mpf('0.01'))
print(f" sign changes in gap 1 (step 0.01): {len(intervals)}")
for (a, b) in intervals:
    # bisect
    fa = H_direct(a)[0]
    for _ in range(220):
        m = (a + b) / 2
        fm = H_direct(m)[0]
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    print(f"   root = {mp.nstr((a+b)/2, 30)}")

print("\n== scan gap 10 (48.62,50.84) at fine step ==")
g10, g11 = mp.mpf('48.622533948079'), mp.mpf('50.839004822815')
intervals = scan(lambda t: H_direct(t)[0], g10 + mp.mpf('0.001'), g11 - mp.mpf('0.001'), mp.mpf('0.01'))
print(f" sign changes in gap 10 (step 0.01): {len(intervals)}")
for (a, b) in intervals:
    fa = H_direct(a)[0]
    for _ in range(220):
        m = (a + b) / 2
        fm = H_direct(m)[0]
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    print(f"   root = {mp.nstr((a+b)/2, 30)}")
