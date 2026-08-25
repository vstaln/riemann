#!/usr/bin/env python3
"""Speiser probe: does a planted off-line zeta-zero push an xi' zero across Re=1/2?

N = (1/(2 pi i)) ∮ f''/f' ds over [re_lo,re_hi] x [t0-8, t0+8]  counts zeros of f'
(left of 1/2 near height t0), f = xi * R (planted).
PRIMARY (per mission): mp.quad of the log-derivative f''/f' at dps=15.
Cross-check: coarse sample-winding of f' (dense only where quad is ambiguous / near-pole).
"""
import time, cmath, math
from mpmath import mp, mpf, pi, gamma, zeta, log, exp, j, digamma, polygamma

mp.dps = 15
t0 = mp.zetazero(1)

def zeta1(s): return zeta(s, 1, derivative=1)
def zeta2(s): return zeta(s, 1, derivative=2)

def xi(s):
    return mpf('0.5') * s * (s - 1) * exp(-s * log(pi) / 2) * gamma(s / 2) * zeta(s)

def xi_logderiv(s):
    return 1 / s + 1 / (s - 1) - log(pi) / 2 + digamma(s / 2) / 2 + zeta1(s) / zeta(s)

def xi_prime(s): return xi(s) * xi_logderiv(s)

def xi_dd_over_prime(s):
    l1 = xi_logderiv(s)
    z, z1, z2 = zeta(s), zeta1(s), zeta2(s)
    l1p = -1 / s**2 - 1 / (s - 1)**2 + polygamma(1, s / 2) / 4 + (z2 * z - z1 * z1) / (z * z)
    return l1 + l1p / l1

def plant_zeros(zs):
    n = len(zs)
    def R(s):
        p = mpf(1)
        for z in zs: p *= (s - z)
        return p
    def Rp(s):
        tot = mpf(0)
        for i in range(n):
            p = mpf(1)
            for k in range(n):
                if k != i: p *= (s - zs[k])
            tot += p
        return tot
    def Rpp(s):
        tot = mpf(0)
        for i in range(n):
            for k in range(n):
                if k == i: continue
                p = mpf(1)
                for m in range(n):
                    if m != i and m != k: p *= (s - zs[m])
                tot += p
        return tot
    def fp(s): return xi_prime(s) * R(s) + xi(s) * Rp(s)
    def fd(s):
        num = xi_dd_over_prime(s) * xi_prime(s) * R(s) + 2 * xi_prime(s) * Rp(s) + xi(s) * Rpp(s)
        return num / fp(s)
    return fp, fd

def rect_pts(re_lo, re_hi, t_lo, t_hi, n):
    pts = []
    for k in range(n):
        pts.append(mp.mpc(re_lo + (re_hi - re_lo) * k / n, t_lo))
    for k in range(n):
        pts.append(mp.mpc(re_hi, t_lo + (t_hi - t_lo) * k / n))
    for k in range(n):
        pts.append(mp.mpc(re_hi - (re_hi - re_lo) * k / n, t_hi))
    for k in range(n):
        pts.append(mp.mpc(re_lo, t_hi - (t_hi - t_lo) * k / n))
    return pts

def winding(f, pts):
    vals = [f(p) for p in pts]
    mn = min(abs(v) for v in vals)
    ph = [cmath.phase(complex(v)) for v in vals]
    tot = 0.0
    for i in range(len(ph)):
        d = ph[(i + 1) % len(ph)] - ph[i]
        d = (d + math.pi) % (2 * math.pi) - math.pi
        tot += d
    return tot / (2 * math.pi), mn

def quad_N(fd, re_lo, re_hi, t_lo, t_hi, maxdeg=16):
    sides = [
        (lambda t: mp.mpc(re_lo + (re_hi - re_lo) * t, t_lo), mpf(re_hi - re_lo)),
        (lambda t: mp.mpc(re_hi, t_lo + (t_hi - t_lo) * t), j * (t_hi - t_lo)),
        (lambda t: mp.mpc(re_hi - (re_hi - re_lo) * t, t_hi), -mpf(re_hi - re_lo)),
        (lambda t: mp.mpc(re_lo, t_hi - (t_hi - t_lo) * t), -j * (t_hi - t_lo)),
    ]
    tot = mpf(0)
    for path, dsdt in sides:
        tot += mp.quad(lambda t: fd(path(t)) * dsdt, [0, 1], maxdegree=maxdeg)
    return tot / (2 * pi * j)

def main():
    tS = time.time()
    print(f"t0 = {mp.nstr(t0, 8)}  dps = {mp.dps}", flush=True)

    # self-check of winding routine
    pts = rect_pts(mpf('0.25'), mpf('0.49'), t0 - 8, t0 + 8, 250)
    N1, _ = winding(lambda s: s - mp.mpc('0.3', t0), pts)
    N2, _ = winding(lambda s: s - mp.mpc('0.3', t0 + 30), pts)
    print(f"self-check winding: inside={round(N1)} (want 1) outside={round(N2)} (want 0)", flush=True)

    rects = {
        'A': (mpf('0.25'), mpf('0.49'), t0 - 8, t0 + 8),   # mission spec
        'B': (mpf('0.05'), mpf('0.49'), t0 - 8, t0 + 8),
        'E': (mpf('0.01'), mpf('0.499'), t0 - 8, t0 + 8),
    }
    s_on = mp.mpc('0.5', t0 + mpf('0.3'))
    configs = {
        'baseline': (xi_prime, xi_dd_over_prime),
        'off1': plant_zeros([mp.mpc('0.9', t0)]),                                    # mission-literal single
        'off4': plant_zeros([mp.mpc('0.9', t0), mp.mpc('0.1', t0),
                             mp.mpc('0.9', -t0), mp.mpc('0.1', -t0)]),               # FE-consistent
        'on1': plant_zeros([s_on]),
        'on4': plant_zeros([mp.mpc('0.5', t0 + mpf('0.3')), mp.mpc('0.5', -(t0 + mpf('0.3')))]),
    }

    res = {c: {} for c in configs}
    flags = {}   # near-pole warnings
    print(f"\n=== QUAD (primary) N per rect  [{time.time()-tS:.0f}s]", flush=True)
    print("config      " + "   ".join(f"rect{r}" for r in rects), flush=True)
    for cname, (fp, fd) in configs.items():
        vals = {}
        for rname, (lo, hi, tl, th) in rects.items():
            q = quad_N(fd, lo, hi, tl, th)
            Nq = round(float(q.real))
            vals[rname] = Nq
            # near-pole probe: coarse min |f'| on this rectangle's boundary
            try:
                _, mn = winding(fp, rect_pts(lo, hi, tl, th, 300))
                near = mn < mpf('1e-3')
            except Exception:
                mn, near = mpf('-1'), False
            flags[(cname, rname)] = near
        print(f"{cname:<10}  " + "  ".join(
            f"{r}:N={vals[r]}{'*' if flags[(cname,r)] else ''}" for r in rects), flush=True)
        res[cname] = vals

    print(f"\n=== WINDING cross-check (coarse 300/side), dense(*) on key combos  [{time.time()-tS:.0f}s]", flush=True)
    for cname, (fp, fd) in configs.items():
        if cname not in ('baseline', 'off1', 'off4', 'on4'):
            continue
        for rname in ('A', 'E'):
            lo, hi, tl, th = rects[rname]
            Nw, mn = winding(fp, rect_pts(lo, hi, tl, th, 300))
            Ni = round(Nw)
            agree = "ok" if Ni == res[cname][rname] else "MISMATCH"
            print(f"  {cname:<10} rect{rname}: wind N={Ni} ({agree}) min|f'|={mp.nstr(mn,3)}", flush=True)

    print(f"\n=== grid min |f'| zones, off4 over [0.01,0.51]x[t0-8,t0+8]  [{time.time()-tS:.0f}s]", flush=True)
    fp4 = plant_zeros([mp.mpc('0.9', t0), mp.mpc('0.1', t0),
                       mp.mpc('0.9', -t0), mp.mpc('0.1', -t0)])[0]
    best = []
    for i in range(41):
        re = mpf('0.01') + (mpf('0.51') - mpf('0.01')) * i / 40
        for k in range(41):
            im = (t0 - 8) + 16 * k / 40
            v = abs(fp4(mp.mpc(re, im)))
            best.append((float(v), re, im))
    best.sort()
    for v, re, im in best[:4]:
        print(f"  |f'| min zone Re={mp.nstr(re,6)} Im={mp.nstr(im,6)} : {mp.nstr(v,5)}", flush=True)

    base_A = res['baseline']['A']
    off1_sep = any(res['off1'][r] - res['baseline'][r] >= 1 for r in rects)
    off4_sep = any(res['off4'][r] - res['baseline'][r] >= 1 for r in rects)
    on_clean = all(res[c][r] - res['baseline'][r] == 0 for c in ('on1', 'on4') for r in rects)
    verdict = ("TYPE_SEPARATES (off4 FE-consistent; off1 single-plant does NOT)" if off4_sep and on_clean and not off1_sep else
               "TYPE_SEPARATES (off4)" if off4_sep and on_clean else
               "NO_TYPE_SEPARATION" if not off4_sep else "INCONCLUSIVE")
    print("\nRESULT " + "  ".join(f"{c}:A={res[c]['A']} B={res[c]['B']} E={res[c]['E']}" for c in configs), flush=True)
    print(f"VERDICT {verdict} | baseline_A={base_A} off1_sep={off1_sep} off4_sep={off4_sep} on_clean={on_clean}", flush=True)
    print(f"elapsed {time.time()-tS:.0f}s", flush=True)

if __name__ == '__main__':
    main()
