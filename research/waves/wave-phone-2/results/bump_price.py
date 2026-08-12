#!/usr/bin/env python3
"""bump_price.py — decompose & price the alpha~1.1 empirical beyond-1 bump (phone-2 wave).

Reproduces Fhat on [1.0,1.3] (both estimators), computes the rigorous e>=2 prime-power
diagonal spikes (alpha = e*log p / L, L = log(gamma_N/2pi)), and prices the certified
band per attack-pricing-sheet M2/M3. Appends results to bump-price.md as it goes.
Run: uv run --quiet --with numpy python bump_price.py
"""
import numpy as np, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.realpath(os.path.join(HERE, "..", "..", "..", "..", "tools", "data", "zeros_computed_10000.txt"))
OUT = os.path.join(HERE, "bump-price.md")
P0 = 0.6818286874638315

def log(msg):
    print(msg); 
    with open(OUT, "a") as f: f.write(msg + "\n")

def theta(t):
    t = np.asarray(t, float)
    u = t/(2*np.pi)
    return (t/2)*np.log(u) - t/2 - np.pi/8 + 1.0/(48*t) + 7.0/(5760*t**3) + 31.0/(80640*t**5)

def load_zeros(n):
    g = []
    with open(ZEROS) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                try: g.append(float(p[1]))
                except ValueError: pass
            if len(g) >= n: break
    return np.array(g[:n])

def sieve(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def tau_bin_naive(x, alphas, tau_max=30.0, dtau=0.1):
    """F_naive(alpha) = 1 + sum_tau xi(tau) e^{2pi i alpha tau} dtau (LS-note estimator)."""
    n = x.size
    hist = np.zeros(int(tau_max/dtau)+2)
    for i in range(n):
        hi = np.searchsorted(x, x[i]+tau_max, side='left')
        if hi > i+1:
            d = x[i+1:hi] - x[i]
            hist += np.histogram(d, bins=np.arange(0, tau_max+dtau, dtau))[0]
    DD = hist/(n*(n-1)/2.0)
    L = x[-1] - x[0]
    tau = (np.arange(DD.size)+0.5)*dtau
    PW = 2.0*(L-tau)*dtau/L**2
    with np.errstate(divide='ignore', invalid='ignore'):
        xi = np.where(PW > 0, DD/PW - 1.0, 0.0)
    return 1.0 + np.real(np.exp(2j*np.pi*np.outer(alphas, tau)) @ xi)*dtau, DD, PW, tau

def perio(x, alphas):
    e = np.exp(2j*np.pi*np.outer(alphas, x))
    return np.abs(e.sum(axis=1))**2/x.size

log("# bump-price.md (phone-2 wave, EXECUTOR) — decompose & price the alpha≈1.1 bump")
log("Computed by bump_price.py; labels: PROVEN/CONJECTURED/CHECKED-NUMERICALLY per hooks/agents.md.\n")

# ---------- 1. reproduce ----------
x_all = load_zeros(10000)
xu = theta(x_all)/np.pi
grid = np.arange(1.000, 1.3005, 0.005)                      # fine grid [1.0,1.3]
xls  = np.array([1.00, 1.05, 1.10, 1.30])                   # LS-note anchor points
for N, lab in [(1000, "N=1e3"), (3000, "N=3e3"), (10000, "N=1e4")]:
    x = xu[:N]
    L = math.log(x_all[N-1]/(2*np.pi))
    fgrid = perio(x, grid)
    fts = perio(x, xls)                    # periodogram
    fb, DD, PW, tau = tau_bin_naive(x, xls)  # LS-note naive (tau-bin)
    clean = grid > 1.005                    # exclude alpha=1.00 lattice point
    band_mean = fgrid[clean].mean()
    zmax = np.max(np.abs(fgrid[clean]-1.0))  # per-alpha z vs sigma=1 (Exp(1) floor)
    log(f"## 1. reproduce — {lab}  (L = log(gamma_N/2pi) = {L:.4f})")
    log(f"periodogram fine grid [1.0,1.3] step 0.005: mean(F) on (1.005,1.3] = {band_mean:.3f}, "
        f"max|F-1| = {zmax:.2f} (per-alpha sigma = 1: z<={zmax:.2f}); "
        f"F(alpha=1.00) = {fgrid[grid==1.00][0]:.1f} (Gram lattice spike)")
    log(f"periodogram at LS anchors 1.00/1.05/1.10/1.30: {np.round(fts,3).tolist()}")
    log(f"tau-bin naive (LS-note estimator) at 1.00/1.05/1.10/1.30: {np.round(fb,3).tolist()}")
    sel = [(grid[i], fgrid[i]) for i in range(grid.size) if fgrid[i] > 1.6]
    log(f"points > 1.6 on [1.0,1.3]: {sel}\n")

# ---------- 2. rigorous e>=2 prime-power diagonal spikes ----------
log("## 2. rigorous explicit-formula terms (e>=2, diagonal, absolutely convergent)")
for N in (1000, 10000):
    x = xu[:N]
    gN = x_all[N-1]; L = math.log(gN/(2*np.pi))
    p_max = int(math.sqrt(gN))
    ps = sieve(p_max)
    rows = []
    for p in ps:
        lp = math.log(p); e = 2; pe = p*p
        while pe <= gN and e <= 30:
            lpe = e*lp
            a = lpe/L
            if 0.9 <= a <= 1.4:
                h = (N/(16*np.pi**2*L**2))*(lpe**2)/pe   # diagonal spike height, F-units
                rows.append((a, p, e, h, lpe**2/pe))
            pe *= p; e += 1
    rows.sort()
    on = [r for r in rows if 1.0 <= r[0] <= 1.3]
    tot = sum(r[3] for r in on)
    log(f"e>=2 diagonal spikes in [0.9,1.4], N={N} (L={L:.3f}): {len(rows)} total, "
        f"{len(on)} in [1.0,1.3]; sum of heights on [1.0,1.3] = {tot:.4f}")
    log("  top-8 on [1.0,1.3]: " + ", ".join(f"{r[1]}^{r[2]}@a={r[0]:.3f} h={r[3]:.4f}" for r in on[:8]))
    # spike-resonance empirical test: avg Fhat within 0.01 of a spike vs far
    xg = xu[:N]; fg = perio(xg, grid)
    dmin = np.full(grid.size, np.inf)
    for r in rows:
        dmin = np.minimum(dmin, np.abs(grid - r[0]))
    on_r = fg[dmin < 0.01]; off_r = fg[dmin > 0.05]
    log(f"  resonance test (N={N}): mean F near e>=2 spikes = {on_r.mean():.3f} (n={on_r.size}), "
        f"far from spikes = {off_r.mean():.3f} (n={off_r.size})\n")

# ---------- 3. price ----------
log("## 3. price (attack-pricing-sheet M2 range / M3 pointwise)")
for A in (1.03, 1.26, 1.30, 1.7):
    p1 = 1.0 - (1.0-P0)/A**2
    log(f"M2: p1({A}) = 1-(1-p0)/{A}^2 = {p1:.6f};  dv*/dA = 0.6363/A^3 = {0.6363/A**3:.4f}")
A13 = 1.3
p1_13 = 1.0 - (1.0-P0)/A13**2
p1_1  = P0
dA = p1_13 - p1_1
log(f"certified band [1, 1.3]: Delta = p1(1.3) - p1(1) = {p1_13:.6f} - {P0:.6f} = {dA:.6f}; "
    f"v* = {p1_13 + 1/(6*256**2):.6f}  (vs 0.70 target; +0.1299 lands ABOVE 0.80)")
Nc = 256
for eps, lab in [(0.02, "eps=0.02"), (0.25, "eps=0.25"), (0.5, "eps=0.5")]:
    j = int(math.ceil((1+eps)*Nc))
    dp = (1.0-P0)*j/98176.0
    log(f"M3 pointwise at 1+{eps} (j*={j}): dp1/ddelta = {dp:.3e} per unit delta; "
        f"delta for 0.70 = {0.0181713/dp:.1f}; rigorous spike delta~0.01 buys {0.01*dp:.2e}")
log(f"M3 at the e>=2 spike heights (max on-band h~0.02): v* gain = {0.02*((1.0-P0)*262/98176.0):.2e} "
    f"(negligible; spikes are measure-zero -> no M2 band unlock)\n")
log("END bump-price.md")
