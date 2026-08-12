#!/usr/bin/env python3
"""T-2 independent interlacing check: one xi''-zero per xi'-gap (first 20 gaps), H2(t)=-xi'' real."""
import mpmath as mp
mp.mp.dps = 40
PI = mp.pi

def A(s):
    return (1/s + 1/(s-1) - mp.mpf('0.5')*mp.log(PI) + mp.mpf('0.5')*mp.psi(0, s/2)
            + mp.zeta(s, derivative=1)/mp.zeta(s))
def Ad(s):
    zp = mp.zeta(s, derivative=1)
    return (-1/s**2 - 1/(s-1)**2 + mp.mpf('0.25')*mp.psi(1, s/2)
            + mp.zeta(s, derivative=2)/mp.zeta(s) - (zp/mp.zeta(s))**2)
def xi(s):
    return mp.mpf('0.5')*s*(s-1)*mp.power(PI, -s/2)*mp.gamma(s/2)*mp.zeta(s)
def H2(t):
    s = mp.mpc(mp.mpf('0.5'), t)
    v = -xi(s)*(A(s)**2 + Ad(s))
    return v.real, v.imag   # H2 = -xi''(1/2+it), should be real

# xi'-zeros u_n (verified independently at 60 digits in tools/xiprime_check/check_small_t.py,
# README: one per zeta-gap, first root t=15.5857085898293423445957292355).
US = ['15.5857085898293423445957292355', '22.0979772804009020982460583653',
      '26.2722473569356243750711540382', '31.2317958710097855089118960065',
      '34.1933102690113808807215179314', '38.4982407637544907213571745169',
      '41.7367295224193331427350981285', '44.5417036073809966272692376173',
      '48.6225326852778658468161729295', '50.8390048228159697828179099569',
      '53.9687288597224334661117413328', '57.2629341113391025140841206942',
      '59.9306989737258423521851881633', '62.1099057508713071858658957278',
      '65.7583193064237373440898606707', '67.9264537710552439462471054791',
      '70.418407142594909981414899509', '73.0605435210706675476179764859',
      '76.2254379706120628126703379202', '77.9978720250931747998206833418']
ups = [mp.mpf('0.0')] + [mp.mpf(u) for u in US]  # xi' also has zero at t=0 (odd)

counts, roots, bad = [], [], 0
for i in range(len(ups)-1):
    a, b = ups[i], ups[i+1]
    # coarse sign-change scan, then bisect (proven pattern; ~60 evals/gap at dps=40)
    n_coarse = 64
    ivs, prev, t = [], H2(a)[0], a
    for j in range(1, n_coarse+1):
        t = a + (b-a)*j/n_coarse
        cur = H2(t)[0]
        if prev*cur < 0: ivs.append((t - (b-a)/n_coarse, t))
        prev = cur
    rts = []
    for (la, lb) in ivs:
        for _ in range(150):
            m = (la+lb)/2
            if H2(la)[0]*H2(m)[0] <= 0: lb = m
            else: la = m
        rts.append((la+lb)/2)
    counts.append(len(rts)); roots.append(rts)
    if len(rts) != 1: bad += 1
immax = max(abs(H2(t)[1]) for i in range(len(ups)-1) for t in [ups[i], (ups[i]+ups[i+1])/2, ups[i+1]])
print("gaps checked:", len(counts))
print("one-xi''-per-gap counts:", counts)
print("xi''-roots (first 5 gaps):", [mp.nstr(r[0], 12) for r in roots[:5]])
print("PERFECT_INTERLACING" if bad == 0 else f"MISMATCH: {bad} gaps")
print("max |Im H2| at endpoints/midpoints:", mp.nstr(immax, 5))
print("xi''(1/2) = -H2(0) =", mp.nstr(-H2(0)[0], 15))
assert bad == 0 and immax < mp.mpf('1e-30')
