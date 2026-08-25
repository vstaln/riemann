#!/usr/bin/env python3
"""FV parameter-range analysis: three gaps in the OFF/LINE deformation theorem.

Task 1: beta->1/2+ edge  (c = beta-1/2 -> 0+): does L_R^OFF -> 0 uniformly?
        - exact rate of B(u;c) = 1/u^2 - 1/(u-c)^2 - 1/(u+c)^2  as c->0
        - min detectable displacement vs base bound |base| <= B_max
Task 2: delta-general LINE: uniform positivity Re L_LINE >= 0 for ALL delta>0 ?
        - exact far-term correction, tiny-delta threshold
Task 3: window |Im-gamma0|<=8: where does the pushed xi' zero sit for beta in {0.6,0.75,0.9}?
        (continuation from speiser_probe machinery)
"""
import time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, pi, log, sqrt, zeta, gamma, digamma, polygamma, j

mp.dps = 40
t0 = mp.zetazero(1).imag     # HEIGHT of first nontrivial zero; zetazero(1)=0.5+14.1347i

def B(u, c):
    """t0->infty OFF profile: B(u;c) = 1/u^2 - 1/(u-c)^2 - 1/(u+c)^2, u=sigma-1/2."""
    return 1/u**2 - 1/(u-c)**2 - 1/(u+c)**2

def far(x, T):
    """far-point of a conjugate pair at height t0 (T=2t0): (x^2-T^2)/(x^2+T^2)^2."""
    return (x**2 - T**2)/(x**2 + T**2)**2

def L_OFF(u, c, T):
    """Exact Re L_R^OFF at s=sigma+i t0 (near-point part + far terms)."""
    return B(u, c) - far(u - c, T) - far(u + c, T) + far(u, T)

def L_LINE(u, d, T):
    """Exact Re L_R^LINE at s=sigma+i t0: main + far-correction (pair moved UP by d)."""
    main = d**2*(3*u**2 + d**2)/(u**2*(u**2 + d**2)**2)
    return main + far(u, T) - far(u, T + d)  # far-correction = far(u,2t0) - far(u,2t0+d)

# ---------------- TASK 1: beta -> 1/2+ edge ----------------
def task1(T):
    print("=" * 72)
    print("TASK 1: c = beta-1/2 -> 0+  — does L_R^OFF -> 0 uniformly?")
    print("=" * 72)
    us = [mpf('0.05'), mpf('0.1'), mpf('0.2'), mpf('0.3'), mpf('0.45')]
    cs = [mpf('0.4'), mpf('0.2'), mpf('0.1'), mpf('0.05'), mpf('0.025'), mpf('0.0125')]
    print("\n[a] pointwise B(u;c) vs c->0 limit -1/u^2  (u = sigma-1/2 fixed)")
    print("    u       c      B(u;c)        -1/u^2       B + 1/u^2     (B+1/u^2)/c^2")
    for u in us:
        lim = -1/u**2
        for c in cs:
            if c >= u/2:   # stay in |u|>>c pointwise regime, avoid the poles c=u or c=-u
                continue
            b = B(u, c)
            print(f"  {float(u):6.3f}  {float(c):8.4f}  {mp.nstr(b,10):>14s}  {mp.nstr(lim,10):>12s}  "
                  f"{mp.nstr(b - lim,9):>13s}  {mp.nstr((b-lim)/c**2,8):>12s}")
    print("  -> if (B+1/u^2)/c^2 -> const as c->0: pointwise rate is O(c^2), k=2")

    print("\n[b] crossing positions: |u| = c*sqrt(sqrt5-2)?  (k=1 geometric rate)")
    r = sqrt(sqrt(5) - 2)
    for c in (mpf('0.4'), mpf('0.2'), mpf('0.1'), mpf('0.05')):
        # exact zero of numerator -a^4 -4c^2 a^2 + c^4: a^2 = c^2(sqrt5-2)
        a0 = c * r
        # numeric zero of B
        lo, hi = mpf('1e-12'), c
        for _ in range(200):
            mid = (lo + hi)/2
            if B(mid, c) > 0:
                lo = mid
            else:
                hi = mid
        print(f"  c={float(c):5.3f}  exact crossing {mp.nstr(a0,8):>12s}  numeric {mp.nstr(lo,8):>12s}  ratio {mp.nstr(lo/c,8):>10s}")

    print("\n[c] sup_|L_R^OFF| on (0,1): poles persist at u=0 and u=+-c  -> sup = +inf every c>0")
    for c in (mpf('0.4'), mpf('0.1'), mpf('0.01')):
        v1 = abs(L_OFF(mpf('1e-30'), c, T))     # near u=0 pole
        v2 = abs(L_OFF(c + mpf('1e-30'), c, T))  # near u=c pole
        print(f"  c={float(c):5.3f}: |L_OFF(1e-30)|={mp.nstr(v1,5)}  |L_OFF(c+1e-30)|={mp.nstr(v2,5)}")

    print("\n[d] fixed-compacta sup (|u|>=0.05, away from poles) is O(1), limit max|1/u^2|~4")
    for c in (mpf('0.4'), mpf('0.1'), mpf('0.01')):
        m = mpf(0)
        n = 2000
        for i in range(1, n):
            u = -mpf('0.45') + mpf('0.9') * i / n
            if abs(u) < mpf('0.05') or abs(abs(u) - c) < mpf('0.05'):
                continue
            v = abs(L_OFF(u, c, T))
            if v > m:
                m = v
        print(f"  c={float(c):5.3f}: max|L_OFF| over |u|>=0.05 minus pole nbhds = {mp.nstr(m,7)}")

    print("\n[e] min detectable displacement: |B(u0;c)| strictly increasing in c from 1/u0^2")
    print("    c_min = 0 if B_max < 1/u0^2, else closed form c_min = sqrt(u0^2 - (sqrt(5+4 Bmax u0^2)-1)/(1/u0^2+Bmax))")
    def cmin_formula(u0, Bmax):
        if Bmax <= 1/u0**2:
            return mpf(0)
        S = 1/u0**2 + Bmax
        return sqrt(u0**2 - (sqrt(5 + 4*Bmax*u0**2) - 1)/S)
    for u0 in (mpf('0.2'), mpf('0.3')):
        for Bmax in (mpf('5'), 1/u0**2 + mpf('0.5'), 1/u0**2 - mpf('1'), mpf('100')):
            cf = cmin_formula(u0, Bmax)
            # numeric check: solve |B(u0;c)| = Bmax by bisection
            if Bmax > 1/u0**2:
                lo, hi = mpf('1e-15'), u0*mpf('0.9999')
                for _ in range(120):
                    mid = (lo+hi)/2
                    if abs(B(u0, mid)) > Bmax:
                        hi = mid
                    else:
                        lo = mid
                cn = lo
            else:
                cn = mpf(0)
            print(f"  u0={float(u0):4.2f} Bmax={mp.nstr(Bmax,6):>10s}  formula={mp.nstr(cf,8):>12s}  numeric={mp.nstr(cn,8):>12s}  "
                  f"|B(u0;cn)|={mp.nstr(abs(B(u0, cn)),6) if cn>0 else '-':>10s}")

# ---------------- TASK 2: delta-general LINE ----------------
def task2(T):
    print("=" * 72)
    print("TASK 2: Re L_LINE >= 0 for ALL delta>0 ?  (exact, far-correction included)")
    print("=" * 72)
    print("  main(u,d) = d^2(3u^2+d^2)/(u^2(u^2+d^2)^2) > 0;  far-corr = far(u,2t0)-far(u,2t0+d)")
    print("  far'(T) = -2T(3u^2-T^2)/(u^2+T^2)^3 > 0 for T>sqrt3|u|  =>  far(u,2t0) < far(u,2t0+d)")
    print("  => far-corr < 0 for ALL d>0.  Positivity iff main > |far-corr|.")
    print("\n[a] scan Re L_LINE over u-grid for decreasing delta (t0 = gamma1)")
    ds = [mpf('0.3'), mpf('1e-2'), mpf('1e-4'), mpf('1e-6'), mpf('1e-7'), mpf('1e-8')]
    us = [mpf('0.05'), mpf('0.15'), mpf('0.3'), mpf('0.45'), mpf('0.49')]
    print("      delta     |  min over u of Re L_LINE   (u in {0.05..0.49})")
    for d in ds:
        mn = min(L_LINE(u, d, T) for u in us)
        print(f"    {mp.nstr(d,3):>10s}  |  {mp.nstr(mn,10):>14s}")
    print("  -> if min goes NEGATIVE for tiny d: 'ALL delta>0' is REFUTED")

    print("\n[b] exact threshold delta_crit(u): solve main = |far-corr|")
    for u in (mpf('0.2'), mpf('0.3'), mpf('0.4'), mpf('0.49')):
        # L_LINE(u,d) crosses 0; find d* by bisection (d small)
        lo, hi = mpf('1e-40'), mpf('1e-3')
        # ensure sign change: L at hi > 0 (d=1e-3 >> threshold), L at lo < 0 for tiny
        assert L_LINE(u, hi, T) > 0, (u, hi, L_LINE(u, hi, T))
        for _ in range(160):
            mid = (lo + hi)/2
            if L_LINE(u, mid, T) > 0:
                hi = mid
            else:
                lo = mid
        dstar = lo
        approx = u**4/(12*t0**3)   # leading-order: 3d/u^4 = 1/(4 t0^3)
        print(f"  u={float(u):5.2f}: d_crit = {mp.nstr(dstar,8):>12s}   approx u^4/(12 t0^3) = {mp.nstr(u**4/(12*t0**3),8):>12s}  ratio {mp.nstr(dstar/(u**4/(12*t0**3)),6):>8s}")
    print("  worst u=1/2: d_crit(1/2) ~ 1/(16*96*t0^3) - compute directly:")
    print(f"    d_crit(0.5) = {mp.nstr(_dcrit_half(T),8)}  approx 1/(16*12*t0^3) = {mp.nstr(mpf('0.5')**4/(12*t0**3),8)}")

    print("\n[c] delta=0.3 spot-check (the proven theorem): margin = main - |far-corr|")
    for u in (mpf('0.05'), mpf('0.3'), mpf('0.5')):
        v = L_LINE(u, mpf('0.3'), T)
        m = mpf('0.3')**2*(3*u**2 + mpf('0.09'))/(u**2*(u**2 + mpf('0.09'))**2)
        print(f"  u={float(u):5.2f}: Re L_LINE = {mp.nstr(v,10)}  (main={mp.nstr(m,9)}, far-corr={mp.nstr(v-m,9)})")

def _dcrit_half(T):
    # d_crit at u = 1/2 (largest |u| allowed), bisection on exact L_LINE
    u = mpf('0.5')
    lo, hi = mpf('1e-40'), mpf('1e-3')
    for _ in range(160):
        mid = (lo + hi)/2
        if L_LINE(u, mid, T) > 0:
            hi = mid
        else:
            lo = mid
    return lo

# ---------------- TASK 3: window |Im-gamma0| <= 8, pushed xi' zero position ----------------
def task3():
    print("=" * 72)
    print("TASK 3: window |Im-gamma0|<=8: pushed xi'-zero location for beta in {0.6,0.75,0.9}")
    print("=" * 72)
    # reuse speiser_probe machinery (argument-principle winding + |f'| localization)
    from speiser_probe import plant_zeros, xi_prime, rect_pts, winding
    mp.dps = 15
    for beta in (mpf('0.6'), mpf('0.75'), mpf('0.9')):
        c = beta - mpf('0.5')
        zs = [mp.mpc(beta, t0), mp.mpc(1-beta, t0), mp.mpc(beta, -t0), mp.mpc(1-beta, -t0)]
        fp, _ = plant_zeros(zs)
        # FV-consistency self-check: 4 planted zeros = {beta,1-beta} x {+-it0}
        start = time.time()
        # count N in rect E = [0.01,0.499] x [t0-8,t0+8]
        Nw, mn = winding(fp, rect_pts(mpf('0.01'), mpf('0.499'), t0-8, t0+8, 400))
        print(f"\n[beta={float(beta)}]  c={float(c):.2f}  N(left of 1/2, |Im-t0|<=8) = {round(Nw)}  (winding {mp.nstr(Nw,3)}, min|f'|={mp.nstr(mn,2)})  [{time.time()-start:.0f}s]")
        # localize pushed zero: coarse grid then refine
        def loc(relo, rehi, tlo, thi, n):
            best = []
            for i in range(n+1):
                re = relo + (rehi-relo)*i/n
                for k in range(n+1):
                    im = tlo + (thi-tlo)*k/n
                    best.append((float(abs(fp(mp.mpc(re, im)))), re, im))
            best.sort()
            return best[0]
        _, r1, i1 = loc(mpf('0.01'), mpf('0.51'), t0-8, t0+8, 30)
        _, r2, i2 = loc(r1-mpf('0.03'), r1+mpf('0.03'), i1-mpf('0.03'), i1+mpf('0.03'), 30)
        _, r3, i3 = loc(r2-mpf('0.004'), r2+mpf('0.004'), i2-mpf('0.004'), i2+mpf('0.004'), 30)
        print(f"  pushed xi'-zero at Re = {mp.nstr(r3,7)} , Im = {mp.nstr(i3,8)}  |Im - gamma0| = {mp.nstr(abs(i3-t0),7)}")
        print(f"  (coarse Re={mp.nstr(r1,5)},Im={mp.nstr(i1,6)};  mid Re={mp.nstr(r2,6)},Im={mp.nstr(i2,7)})")

if __name__ == '__main__':
    T = 2*t0
    task1(T)
    task2(T)
    task3()
