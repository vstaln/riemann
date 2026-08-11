#!/usr/bin/env python3
"""Independent 60-digit check: zeros of xi' on the critical line, small-t region.

H(t) := i * xi'(1/2+it) is real for real t (xi(1/2+it) is real & even, so its t-derivative is real),
and H(t) = 0  <=>  xi'(1/2+it) = 0.  Two independent formulations are cross-checked:
  (1) H_direct  = Re[i * xi * (xi'/xi)]      -- xi'/xi = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta
  (2) H_zform   = -(Z*(P'/P) + Z')           -- Z = e^{i theta} zeta(1/2+it), P'/P = 2t/(t^2+1/4) - (1/2)Im psi(1/4+it/2)
They agree up to the positive factor P(t) = (t^2+1/4)/2 * pi^{-1/4} |Gamma(1/4+it/2)| (H_direct = P * H_zform),
hence share the same zeros.

Resolves the "suspicious density" question left by a previous agent (which found 10 on-line xi'-zeros
below gamma_1 in tools/data/xiprime_on_line_1_1000.txt): those are artifacts of its f64 pipeline
(theta_small Stirling divergence at |z|<1 and a sign bug in psi_im for |z|<10).

Run:  uv run --quiet --with mpmath python check_small_t.py [ngaps]   (default 20 gaps; 60 digits)
"""
import sys
import time
import mpmath as mp

mp.mp.dps = 60
PI = mp.pi
ZEROS = '/home/vstaln/riemann/tools/data/zeros_1_1000.txt'
PRIOR = '/home/vstaln/riemann/tools/data/xiprime_on_line_1_1000.txt'
CLAIMED_SMALL = [0.094361507680, 0.221459957543, 0.313998564176, 0.485033310957,
                 0.535747427515, 0.644799088829, 0.724653285622, 0.815863219352,
                 0.871368539934, 11.197465161854]


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lp(s):
    return (1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(PI)
            + mp.mpf('0.5') * mp.psi(0, s / 2) + mp.zeta(s, derivative=1) / mp.zeta(s))


def H(t):
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    v = 1j * xi(s) * lp(s)
    return v.real, v.imag


def H_zform(t):
    tt = mp.mpf(t)
    th = lambda u: mp.im(mp.log(mp.gamma(mp.mpf('0.25') + 1j * u / 2))) - u / 2 * mp.log(PI)
    Z = lambda u: (mp.exp(1j * th(u)) * mp.zeta(mp.mpf('0.5') + 1j * u)).real
    pp = 2 * tt / (tt * tt + mp.mpf('0.25')) - mp.mpf('0.5') * mp.im(
        mp.psi(0, mp.mpf('0.25') + 1j * tt / 2))
    Zp = mp.diff(Z, tt)
    return -(Z(tt) * pp + Zp)


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


def root(f, a, b, iters=220):
    fa = f(a)
    for _ in range(iters):
        m = (a + b) / 2
        fm = f(m)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return (a + b) / 2


def main():
    ngaps = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    gs = [mp.mpf(l.split()[1]) for l in open(ZEROS)]
    g1 = gs[0]
    print(f"gamma_1 = {mp.nstr(g1, 40)}")

    # cross-check the two formulations at a few points (H_direct = P * H_zform)
    print("\n-- H_direct vs H_zform (share zeros; ratio = P(t) > 0) --")
    for t in ['0.5', '10.0', '16.0', '50.0', '500.0']:
        h1 = H(t)[0]
        h2 = H_zform(t)
        print(f"  t={t:>6}: H_direct={mp.nstr(h1, 10):>16}  H_zform={mp.nstr(h2, 10):>16}  sign match: {(h1>0)==(h2>0)}")

    # evaluate H at the previous agent's claimed small-t roots
    print("\n-- H at the previous agent's claimed small-t roots (all should be ~0 if genuine) --")
    for t in CLAIMED_SMALL:
        print(f"  t = {t:.12f}   H = {mp.nstr(H(str(t))[0], 6)}   <-- artifact" if abs(H(str(t))[0]) > mp.mpf('1e-20') else
              f"  t = {t:.12f}   H ~ 0")

    # fine scans of (0, gamma_1): no sign changes expected
    print("\n-- scans of (0, gamma_1) for sign changes of H --")
    n1 = len(scan(lambda t: H(t)[0], mp.mpf('0.0001'), g1 - mp.mpf('0.5'), mp.mpf('0.1')))
    n2 = len(scan(lambda t: H(t)[0], mp.mpf('0.0001'), mp.mpf('3.0'), mp.mpf('0.005')))
    print(f"  sign changes in (0.0001, gamma_1-0.5) step 0.1: {n1}")
    print(f"  sign changes in (0.0001, 3.0) step 0.005: {n2}")
    print(f"  H(0.001)={mp.nstr(H('0.001')[0], 8)}, H(5)={mp.nstr(H('5')[0], 8)}, "
          f"H(13.9)={mp.nstr(H('13.9')[0], 8)} (all < 0 => H<0 on (0,gamma_1))")

    # gap roots
    print(f"\n-- first {ngaps} gaps (gamma_i, gamma_{{i+1}}): exactly one xi'-zero each (60 digits) --")
    roots = []
    hist = {}
    t0 = time.time()
    for gi in range(1, ngaps + 1):
        a = gs[gi - 1] + (gs[gi] - gs[gi - 1]) * mp.mpf('0.01')
        b = gs[gi] - (gs[gi] - gs[gi - 1]) * mp.mpf('0.01')
        iv = scan(lambda t: H(t)[0], a, b, (b - a) / 8)
        hist[len(iv)] = hist.get(len(iv), 0) + 1
        for (la, lb) in iv:
            roots.append(root(lambda t: H(t)[0], la, lb))
    print(f"  gap histogram: {dict(sorted(hist.items()))}   ({time.time()-t0:.0f}s)")
    for i, r in enumerate(roots):
        print(f"    gap {i+1}: t = {mp.nstr(r, 25)}")

    # far-out samples
    print("\n-- far-out gaps sampled at 60 digits (every 200th) --")
    h2 = {}
    for gk in [200, 400, 600, 800, 999]:
        a = gs[gk - 1] + (gs[gk] - gs[gk - 1]) * mp.mpf('0.02')
        b = gs[gk] - (gs[gk] - gs[gk - 1]) * mp.mpf('0.02')
        iv = scan(lambda t: H(t)[0], a, b, (b - a) / 10)
        h2[len(iv)] = h2.get(len(iv), 0) + 1
        if len(iv) == 1:
            print(f"    gap {gk}: t = {mp.nstr(root(lambda t: H(t)[0], iv[0][0], iv[0][1]), 18)}")
    print(f"  histogram: {dict(sorted(h2.items()))}")

    # compare gap roots with the prior file (entries 11..1009)
    prior = [mp.mpf(l.split()[1]) for l in open(PRIOR)]
    print("\n-- agreement with previous agent's file for gap roots (entries 11..) --")
    for i in range(min(10, len(roots))):
        d = abs(roots[i] - prior[10 + i])
        print(f"  gap {i+1}: mine={mp.nstr(roots[i], 15)}  prior={mp.nstr(prior[10+i], 15)}  |diff|={mp.nstr(d, 3)}")


if __name__ == '__main__':
    main()
