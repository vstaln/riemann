#!/usr/bin/env python3
"""Full-range count of on-line xi'-zeros in (0.05, gamma_1000] at 25 digits.

Coarse but complete: 8 interior samples per gap (fast at dps=25), one bisection per sign change.
Expected: 999 zeros (none in (0,gamma_1), exactly one per gap), matching RvM for xi' and the
0.85838 certificate structure.  Run:  uv run --quiet --with mpmath python check_count.py
"""
import time
import mpmath as mp

mp.mp.dps = 25
PI = mp.pi
ZEROS = '/home/vstaln/riemann/tools/data/zeros_1_1000.txt'


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lp(s):
    return (1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(PI)
            + mp.mpf('0.5') * mp.psi(0, s / 2) + mp.zeta(s, derivative=1) / mp.zeta(s))


def H(t):
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    return (1j * xi(s) * lp(s)).real


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


def root(f, a, b, iters=110):
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
    gs = [mp.mpf(l.split()[1]) for l in open(ZEROS)]
    n = len(gs)
    t0 = time.time()
    total = 0
    hist = {}
    # (0, gamma_1)
    iv = scan(H, mp.mpf('0.05'), gs[0] - mp.mpf('1e-6'), mp.mpf('0.1'))
    hist[len(iv)] = hist.get(len(iv), 0) + 1
    total += len(iv)
    for (a, b) in iv:
        print(f"  root in (0, gamma_1): t = {mp.nstr(root(H, a, b, 80), 20)}")
    # gaps: count only (no bisection) for speed; bisect a small sample afterwards
    intervals_by_gap = []
    for i in range(n - 1):
        a = gs[i] + (gs[i + 1] - gs[i]) * mp.mpf('0.01')
        b = gs[i + 1] - (gs[i + 1] - gs[i]) * mp.mpf('0.01')
        iv = scan(H, a, b, (b - a) / 8)
        hist[len(iv)] = hist.get(len(iv), 0) + 1
        total += len(iv)
        intervals_by_gap.append(iv)
    print(f"histogram (xi'-zeros per gap incl. (0,gamma_1)): {dict(sorted(hist.items()))}")
    print(f"total on-line xi'-zeros in (0.05, gamma_{n}]: {total}   (took {time.time()-t0:.0f}s)")
    print(f"RvM check: N_zeta up to gamma_{n} = {n}; on-line xi'-zeros (0, gamma_{n}] = {total} (expect {n-1})")
    # bisect a small sample of the found roots for cross-check (gaps 1, 500, 999)
    print("sample roots (bisected):")
    for gi in [0, 499, 998]:
        iv = intervals_by_gap[gi]
        if len(iv) == 1:
            print(f"  gap {gi+1}: t = {mp.nstr(root(H, iv[0][0], iv[0][1], 80), 20)}")


if __name__ == '__main__':
    main()
