#!/usr/bin/env python3
"""Probe M2.3 + M1.5 (music-ling catalog): rational-alpha pair-correlation "consonance" test.

Questions:
  (a) [M2.3] Does the real zero pair-correlation g(u) (density-1 rescaled) deviate from the
      GUE prediction 1 - sinc^2(pi u) at RATIONAL u = p/q, in a way it does not at control
      (irrational) u? Plomp-Levelt consonance theory says harmonic spectra have dips at
      simple ratios; GUE says flat.
  (b) [M1.5] Do pair distances cluster near simple rationals more than a Poisson control?
  (c) [M3.1-meter] g(u) at integer lags 1..256 ("meter scan" coarse).

Estimator: g(u) = ordered_pairs(dist in [u,u+du)) / (lambda^2 * (L-u) * du),  lambda = n/L ~ 1.
Data: tools/data/zeros_computed_10000.txt (10,000 zeta ordinates, computed).
Expected: all deviations within noise -> GUE-consistent (documented negative for "harmonic" structure).
"""
import numpy as np

DATA = "data/zeros_computed_10000.txt"

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    return np.sort(np.array(g))

def rescale(x):
    n = x.size
    L = x[-1] - x[0]
    sp = L / (n - 1)
    return (x - x[0]) / sp, L / sp, n

def pair_counts(u, U, du):
    """Ordered pair counts in distance bands [k*du, (k+1)*du), k=0.., for dist <= U."""
    n = u.size
    nb = int(np.ceil(U / du))
    counts = np.zeros(nb)
    # sliding window via searchsorted on sorted u
    for i in range(n):
        lo = i + 1
        hi = np.searchsorted(u, u[i] + U, side='right')
        if hi > lo:
            d = u[lo:hi] - u[i]
            idx = (d / du).astype(int)
            counts[idx] += 1
    return counts

def g_from_counts(counts, du, L, lam):
    """g(u) estimator at bin centers."""
    nb = counts.size
    g = np.zeros(nb)
    for k in range(nb):
        umid = (k + 0.5) * du
        g[k] = counts[k] / (lam * lam * max(L - umid, 1e-9) * du)
    return g

def gue(u):
    s = np.sinc(u)  # numpy sinc(x) = sin(pi x)/(pi x)
    return 1.0 - s * s

def band_avg(g, du, ustar, w):
    """Mean g over [ustar-w, ustar+w]."""
    k0 = int(np.floor((ustar - w) / du))
    k1 = int(np.floor((ustar + w) / du))
    k0 = max(k0, 0)
    k1 = min(k1, g.size - 1)
    return g[k0:k1 + 1].mean()

def main():
    x = load(DATA)
    u, L, n = rescale(x)
    lam = n / L
    print(f"n={n}  L(rescaled)={L:.1f}  lambda={lam:.4f}  logT~{np.log(x[-1]):.2f}")

    # ---- fine scan: rationals vs controls at width w ~ 1/log T ----
    du = 0.05
    U = 8.0
    w = 0.10
    counts = pair_counts(u, U, du)
    g = g_from_counts(counts, du, L, lam)
    rationals = [1/3, 1/2, 2/3, 3/4, 1.0, 4/3, 3/2, 2.0, 3.0]
    controls = [0.37, 0.61, 1.13, 1.71, 2.31, 2.89]
    print("\n== fine scan (du=%.2f, U=%.0f, window w=%.2f) ==" % (du, U, w))
    print("u        g_meas   g_GUE    dev%      |dev|/noise")
    rows = []
    for ustar in rationals + controls:
        gm = band_avg(g, du, ustar, w)
        gg = gue(ustar)
        dev = (gm - gg) / gg * 100.0
        # noise estimate: sqrt(2*var) from bins in the window, Poisson-ish
        k0 = max(int(np.floor((ustar - w) / du)), 0)
        k1 = min(int(np.floor((ustar + w) / du)), g.size - 1)
        vals = g[k0:k1 + 1]
        noise = (vals.std() / np.sqrt(vals.size)) / gg * 100.0 if vals.size > 1 else np.nan
        tag = "R" if ustar in rationals else "C"
        rows.append((ustar, gm, gg, dev, noise, tag))
        print(f"{ustar:5.2f}  {gm:7.4f}  {gg:7.4f}  {dev:+7.2f}%   {dev/noise:+5.1f}")
    r_dev = np.array([r[3] for r in rows if r[5] == 'R'])
    c_dev = np.array([r[3] for r in rows if r[5] == 'C'])
    print(f"\nmean |dev| rationals = {np.abs(r_dev).mean():.2f}%   controls = {np.abs(c_dev).mean():.2f}%")

    # ---- meter scan: integer lags 1..256 (coarse) ----
    print("\n== meter scan (integer lags, du=0.5, U=300) ==")
    du2 = 0.5
    counts2 = pair_counts(u, 300.0, du2)
    g2 = g_from_counts(counts2, du2, L, lam)
    for k in [1, 2, 3, 4, 8, 16, 32, 64, 128, 256]:
        if k < g2.size:
            gm = g2[k]
            gg = gue(k)
            print(f"u={k:4d}  g_meas={gm:7.4f}  g_GUE={gg:7.4f}  dev={(gm-gg)/gg*100:+7.2f}%")

    # ---- M1.5 near-rational clustering: real pairs vs Poisson control ----
    print("\n== M1.5 near-rational distance clustering (eps=0.01, q<=8) ==")
    def frac_rational(du_all):
        # du_all: array of distances
        best = np.full(du_all.size, 1e9)
        for q in range(1, 9):
            for p in range(1, 3 * q + 1):
                r = p / q
                if r > 8:
                    continue
                best = np.minimum(best, np.abs(du_all - r))
        return best
    # sample a subset of distances up to U for speed
    rng = np.random.default_rng(42)
    pairs = []
    for i in range(n):
        lo = i + 1
        hi = np.searchsorted(u, u[i] + 8.0, side='right')
        if hi > lo:
            d = u[lo:hi] - u[i]
            pairs.append(d)
    d_all = np.concatenate(pairs) if pairs else np.array([])
    if d_all.size > 200000:
        d_all = rng.choice(d_all, 200000, replace=False)
    fr_real = frac_rational(d_all)
    real_frac = np.mean(fr_real < 0.01)
    # Poisson control: uniform points, same n, L
    uctrl = np.sort(rng.uniform(0, L, n))
    pairs_c = []
    for i in range(n):
        lo = i + 1
        hi = np.searchsorted(uctrl, uctrl[i] + 8.0, side='right')
        if hi > lo:
            pairs_c.append(uctrl[lo:hi] - uctrl[i])
    dc = np.concatenate(pairs_c) if pairs_c else np.array([])
    if dc.size > 200000:
        dc = rng.choice(dc, 200000, replace=False)
    fr_ctrl = frac_rational(dc)
    ctrl_frac = np.mean(fr_ctrl < 0.01)
    print(f"real pairs near rational (eps<0.01): {real_frac:.6f}")
    print(f"Poisson control near rational:       {ctrl_frac:.6f}")
    print(f"ratio real/control:                  {real_frac/ctrl_frac:.3f}")
    print(f"(ratio ~ 1 -> no rational structure; GUE-consistent)")

if __name__ == "__main__":
    main()
