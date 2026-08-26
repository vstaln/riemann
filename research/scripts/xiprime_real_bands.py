#!/usr/bin/env python3
"""Real-xi' certification: count zeros of xi'(s) in [0.25,0.49] x [gamma_k - 8, gamma_k + 8]
for k = 1..6 on actual zeta data. RH (Speiser equivalence) predicts N_k = 0 for ALL k.

N_k = (1/(2 pi i)) ∮ xi''/xi' ds over the rectangle = winding of xi' along the boundary
(robust primary; sample-winding of xi', the reliable method per speiser-probe-2026-08-25).
Any N_k >= 1 triggers a triple-check: (a) independent mp.quad of xi''/xi', (b) halved
window [0.25,0.49] x [gamma_k +- 4] at n=2000/side.

Also records per band: min over left-edge samples of Re(xi'/xi) (negativity margin, < 0
under RH) and wall-clock. dps = 15, n = 2000/side (mission spec).
"""
import time, cmath, math, sys
from mpmath import mp, mpf, pi, gamma, zeta, log, exp, j, digamma, polygamma

mp.dps = 15

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

def quad_N(fd, re_lo, re_hi, t_lo, t_hi, maxdeg=8):
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

def band_report(k, g, half=8, n=2000):
    tb = time.time()
    lo, hi, tl, th = mpf('0.25'), mpf('0.49'), g - half, g + half
    pts = rect_pts(lo, hi, tl, th, n)
    Nw, mn = winding(xi_prime, pts)
    # negativity margin: min Re(xi'/xi) over left-edge samples (last n pts, Re = 0.25)
    neg = min(float(xi_logderiv(p).real) for p in pts[3 * n:])
    return Nw, mn, neg, time.time() - tb

def main():
    tS = time.time()
    print(f"dps={mp.dps} n=2000/side rect [0.25,0.49]x[gamma_k +- 8]", flush=True)
    rows = []
    nbands = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    for k in range(1, nbands + 1):
        g = mp.zetazero(k)
        # cheap machinery self-check: winding of (s - c) inside the band rect = 1, shifted = 0
        pts = rect_pts(mpf('0.25'), mpf('0.49'), g - 8, g + 8, 400)
        s_in, _ = winding(lambda s: s - mp.mpc('0.3', g), pts)
        s_out, _ = winding(lambda s: s - mp.mpc('0.3', g + 30), pts)
        assert abs(s_in - 1) < 1e-6 and abs(s_out) < 1e-6, (k, s_in, s_out)
        Nw, mn, neg, dt = band_report(k, g)
        Ni = round(Nw)
        rows.append((k, g, Ni, Nw, mn, neg, dt))
        print(f"band {k}: gamma_k={mp.nstr(g,8)}  N={Ni} (raw {mp.nstr(Nw,4)})  "
              f"min|xi'|={mp.nstr(mn,2)}  minRe(xi'/xi)|left={neg:.6f}  wall={dt:.0f}s", flush=True)
    line = "N_1..N_6 = " + " ".join(str(r[2]) for r in rows)
    print(line, flush=True)
    nz = [r for r in rows if r[2] != 0]
    if nz:
        print("!!!!! NONZERO N DETECTED: " + ", ".join(f"band {r[0]} N={r[2]} (raw {mp.nstr(r[3],4)})" for r in nz), flush=True)
        # triple-check each nonzero: independent quad + halved window
        for k, g, Ni, Nw, mn, neg, dt in nz:
            print(f"--- triple-check band {k} (gamma_k={mp.nstr(g,8)}) ---", flush=True)
            q = quad_N(xi_dd_over_prime, mpf('0.25'), mpf('0.49'), g - 8, g + 8)
            print(f"  quad  of xi''/xi'  [0.25,0.49]x[g+-8]  = {mp.nstr(q,6)}", flush=True)
            Nw2, mn2, _, dt2 = band_report(k, g, half=4)
            print(f"  winding n=2000/side [0.25,0.49]x[g+-4]  = {round(Nw2)} (raw {mp.nstr(Nw2,4)}) min|xi'|={mp.nstr(mn2,2)}  wall={dt2:.0f}s", flush=True)
    print(f"elapsed {time.time()-tS:.0f}s", flush=True)

if __name__ == '__main__':
    main()
