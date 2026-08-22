#!/usr/bin/env python3
"""Speiser negativity program: verify decomposition (D)
   zeta'(s)/zeta(s) = B(s) + sum_{gamma>0} 2/(s - (1/2 + i*gamma)),
   B(s) = -1/s - 1/(s-1) - log(pi)/2 - digamma(s/2)/2,
against 40-digit mpmath ground truth (task-mandated recheck of wave-rh5 INCONCLUSIVE item).
Run: uv run --with mpmath python tools/jensen_probe/scripts/speiser_decomp_check.py
"""
import mpmath as mp

mp.mp.dps = 40
ZEROS = "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt"

gammas = []
with open(ZEROS) as f:
    for line in f:
        parts = line.split()
        if len(parts) < 2 or not line.split()[0].isdigit():
            continue
        gammas.append(float(parts[1]))
print(f"loaded {len(gammas)} zeros, last gamma={gammas[-1]}")


def B(s):
    return -1 / s - 1 / (s - 1) - mp.log(mp.pi) / 2 - mp.digamma(s / 2) / 2


def decomp(s, tmax=None):
    g = [x for x in gammas if tmax is None or x <= tmax]
    Z = mp.mpc(0)
    half = mp.mpf("0.5")
    for x in g:
        r = s - (half + 1j * x)
        Z += 2 / r
    return B(s) + Z


def truth(s):
    return mp.diff(lambda w: mp.zeta(w), s)


for name, sre, sim, expected in [
    ("A", "0.05", "16", "-0.6281573984651"),
    ("B", "0.45", "22016", "-33.35930407273"),
]:
    s = mp.mpf(sre) + 1j * mp.mpf(sim)
    tv = truth(s)
    dv = decomp(s)
    err = abs(tv - dv)
    print(f"point {name}: s={sre}+{sim}i")
    print(f"  truth  Re(zeta'/zeta) = {mp.re(tv)}")
    print(f"  decomp Re(zeta'/zeta) = {mp.re(dv)}")
    print(f"  |diff| = {mp.nstr(err, 4)}   expected~{expected}")
    # truncation study: drop zeros above cutoffs
    for cut in (30000, 50000, 70000):
        if float(sim) < cut:
            d2 = decomp(s, tmax=cut)
            print(f"  tmax={cut}: |full-cut| = {mp.nstr(abs(dv - d2), 4)}")

# extra sanity: a third point, no wave reference
s = mp.mpf("0.3") + 1j * mp.mpf("50")
print(f"point C: s=0.3+50i  truth={mp.nstr(mp.re(truth(s)), 20)}  "
      f"decomp={mp.nstr(mp.re(decomp(s)), 20)}  "
      f"|diff|={mp.nstr(abs(truth(s)-decomp(s)), 4)}")

# monotonicity probe (3c): Re(zeta'/zeta) along sigma at fixed t
print("\nmonotonicity probe: Re(zeta'/zeta)(sigma+it)")
for t in ("16", "141", "1000", "7013"):
    row = []
    prev = None
    mono = True
    for sg in ("0.05", "0.10", "0.15", "0.20", "0.25", "0.30", "0.35",
               "0.40", "0.45"):
        v = float(mp.re(truth(mp.mpf(sg) + 1j * mp.mpf(t))))
        if prev is not None and v >= prev:
            mono = False
        prev = v
        row.append(f"{v:.4f}")
    print(f"  t={t:>6}: " + " ".join(row) + f"  strictly_decreasing_in_sigma={mono}")
