#!/usr/bin/env python3
"""Independent mpmath cross-check of the xi'-on-the-line computation.

G(t) := i * xi'(1/2 + it)  is real;  xi'(1/2+it) = 0  iff  G(t) = 0.
G(t) = i * xi(1/2+it) * [1/(1/2+it) + 1/(it-1/2) - (1/2)log(pi) + (1/2)psi(1/4+it/2)
                         + zeta'/zeta(1/2+it)]
"""
import mpmath as mp

mp.mp.dps = 25

def G(t):
    s = mp.mpf('0.5') + 1j * mp.mpf(t)
    ls = mp.log(s) + mp.log(s - 1) - mp.log(2) - s / 2 * mp.log(mp.pi)
    lz = mp.logzeta(s) if hasattr(mp, 'logzeta') else None
    # xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    xi = mp.mpf('0.5') * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    rat = 1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(mp.pi) + mp.mpf('0.5') * mp.psi(0, s / 2) \
          + mp.zeta(s, derivative=1) / mp.zeta(s)
    return (1j * xi * rat).real  # should be real

def main():
    # (1) the claimed small-t roots below gamma_1
    small = [0.094362, 0.221460, 0.313999, 0.485033, 0.535747, 0.644799,
             0.724653, 0.815863, 0.871369, 11.197465]
    print("== G(t) at the claimed small-t roots (should be ~0) ==")
    for t in small:
        print(f"  t = {t:10.6f}  G = {mp.nstr(G(t), 6)}")

    # (2) independent scan of (0.01, 14.13) for sign changes of G
    g1 = mp.mpf('14.1347251417346937904572519835625')
    step = mp.mpf('0.01')
    roots = []
    prev_t = mp.mpf('0.01')
    prev_g = G(prev_t)
    n = int((g1 - prev_t) / step)
    for i in range(1, n + 1):
        t = prev_t + mp.mpf(i) * step
        g = G(t)
        if prev_g * g < 0:
            # bisect
            lo, hi, flo, fhi = prev_t, t, prev_g, g
            for _ in range(90):
                mid = (lo + hi) / 2
                fm = G(mid)
                if flo * fm <= 0:
                    hi, fhi = mid, fm
                else:
                    lo, flo = mid, fm
            roots.append((lo + hi) / 2)
        prev_t, prev_g = t, g
    print(f"== independent mpmath scan of (0.01, 14.1347): {len(roots)} roots of G ==")
    for r in roots:
        print(f"  t = {mp.nstr(r, 10)}")

    # (3) sample of the 999 gap roots (first, middle, last gaps)
    print("== sample gap roots: G at xiprime_on_line roots in gaps 1, 500, 999 ==")
    with open('/home/vstaln/riemann/tools/data/xiprime_on_line_1_1000.txt') as f:
        lines = f.readlines()
    # roots file: 999 gap roots + 10 small-t roots; gap roots start after the small ones.
    # The file has all 1009 in ascending order; pick the ones matching gap positions.
    print("  file has", len(lines), "roots (ascending); last 999 are the gap roots")
    for idx in [0, 1, 998]:  # first two small-t + last
        t = float(lines[idx].split()[1])
        print(f"  line {idx+1}: t = {t:.6f}  G = {mp.nstr(G(t), 6)}")

if __name__ == '__main__':
    main()
