#!/usr/bin/env python3
"""bump_price2.py — decompose & price the alpha in [1.0,1.3] periodogram bump (phone-2 wave, v2).

Adjudicates the LS-note vs hot-hand conflict (Fhat(1.00) = 1.378 vs 245.84 on the SAME
zeros/unfolding), reproduces Fhat on fine grids, computes the RIGOROUS e>=2 prime-power
diagonal plane-wave sum D(alpha) (pair-correlation explicit formula, Guinand), tests
correlation of Fhat-1 with D, and prices under M2/M3 (attack-pricing-sheet).

Labels per hooks/agents.md. Every number printed here is produced by THIS script.
Run: cd ~/riemann && uv run --quiet --with numpy python research/waves/wave-phone-2/results/bump_price2.py
"""
import numpy as np, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.realpath(os.path.join(HERE, "..", "..", "..", "..", "tools", "data", "zeros_computed_10000.txt"))
LOG = os.path.join(HERE, "bump_price2.log")
P0 = 0.6818286874638315
E1 = 1.0/(6*256**2)

def log(msg):
    print(msg)
    with open(LOG, "a") as f: f.write(msg + "\n")

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

def perio(x, alphas):
    e = np.exp(2j*np.pi*np.outer(alphas, x))
    return np.abs(e.sum(axis=1))**2/x.size

def n_eff(seq):
    """effective independent sample count from lag-1.. autocorrelation of mean-centered seq."""
    v = seq - seq.mean()
    c0 = np.dot(v, v)
    if c0 <= 0: return 1.0
    n = v.size
    out = 1.0; acc = 0.0
    for k in range(1, min(n//2, 200)):
        r = np.dot(v[k:], v[:-k])/c0
        if r <= 0: break
        acc += (1.0 - k/n)*r
    return n/(1.0 + 2*acc)

g_all = load_zeros(10000)
xu = theta(g_all)/np.pi
grid = np.arange(1.00, 1.3001, 0.005)          # fine grid incl. alpha=1.00
clean = grid > 1.005                            # exclude Gram-lattice spike tail

log("# bump_price2.log — v2 run (date per shell); every number from this script.")
log("")

# ---------- 1. reproduce + adjudicate ----------
log("## 1. reproduce Fhat and adjudicate the notes' conflict")
anchors = np.array([1.00, 1.05, 1.10, 1.25, 1.30])
for N in (1000, 3000, 10000):
    x = xu[:N]
    L = math.log(g_all[N-1]/(2*np.pi))
    fg = perio(x, grid)
    fa = perio(x, anchors)
    bm = fg[clean].mean()
    zmax = np.max(np.abs(fg[clean]-1.0))
    ne = n_eff(fg[clean]-1.0)
    sband = 1.0/np.sqrt(ne)                     # per-alpha sigma ~ 1 (Exp(1) floor, hot-hand)
    log(f"N={N}: Fhat(1.00) = {fg[grid==1.00][0]:.1f}   [LS-note claimed 1.378, hot-hand 245.84]")
    log(f"      anchors 1.00/1.05/1.10/1.25/1.30 = {np.round(fa,3).tolist()}")
    log(f"      band (1.005,1.3] fine-grid: mean(F) = {bm:.3f}, max|F-1| = {zmax:.2f} "
        f"(single-draw z, sigma~1), n_eff = {ne:.1f} -> band-mean sigma = {sband:.3f}, "
        f"band z = {(bm-1.0)/sband:+.2f}")
    log("")

# ---------- 2. rigorous e>=2 prime-power diagonal (pair-correlation explicit formula) ----------
log("## 2. rigorous e>=2 prime-power diagonal (Guinand explicit formula)")
for N in (1000, 10000):
    x = xu[:N]
    gN = g_all[N-1]; L = math.log(gN/(2*np.pi))
    ps = sieve(int(math.sqrt(gN))+1)
    rows = []
    for p in ps:
        lp = math.log(p); e = 2; pe = p*p
        while pe <= gN:
            u = e*lp/L                                   # spike separation u_p,e
            c = lp**e/(pe*L)                             # coefficient (log p)^e/(p^{e/2} L)
            rows.append((u, p, e, c))
            pe *= p; e += 1
    inb = [r for r in rows if 1.0 <= r[0] <= 1.3]
    log(f"N={N} (L={L:.3f}): e>=2 terms total {len(rows)}; on-band u in [1.0,1.3]: {len(inb)}")
    by_e = {}
    for u, p, e, c in inb: by_e.setdefault(e, []).append((p, c, u))
    for e in sorted(by_e):
        lst = by_e[e]
        tot = sum(c for _, c, _ in lst)
        log(f"  e={e}: {len(lst)} terms, sum c = {tot:.4f}   " +
            ", ".join(f"p={p}(c={c:.4f},u={u:.3f})" for p, c, u in lst[:6]))
    # D(alpha): rigorous plane-wave contribution to E[Fhat]-1 (real part)
    us = np.array([r[0] for r in rows]); cs = np.array([r[3] for r in rows])
    D = cs @ np.cos(2*np.pi*np.outer(us, grid))          # shape convention-independent
    fg = perio(x, grid)
    dm = D[clean].mean(); dmin = D[clean].min(); dmax = D[clean].max()
    corr = np.corrcoef(D[clean], fg[clean]-1.0)[0, 1]
    log(f"  D(alpha)=sum c*cos(2pi*alpha*u) on (1.005,1.3]: mean {dm:+.4f}, min {dmin:+.4f}, "
        f"max {dmax:+.4f}, |D| <= {max(abs(dmin), abs(dmax)):.4f}")
    log(f"  corr(Fhat-1, D) on band = {corr:+.3f}   [shape-level match test]")
    log("")

# ---------- 3. price ----------
log("## 3. price (attack-pricing-sheet M2 range / M3 pointwise)")
A = 1.3
p1_13 = 1.0 - (1.0-P0)/A**2
dA = p1_13 - P0
log(f"M2: p1(1.3) = 1-(1-p0)/1.3^2 = {p1_13:.6f}; Delta = p1(1.3)-p1(1) = {dA:.6f}; "
    f"v* = {p1_13 + E1:.6f}  (vs 0.70 target: {p1_13:.4f} {'>' if p1_13 > 0.70 else '<='} 0.70)")
for eps in (0.02, 0.25, 0.5):
    j = int(math.ceil((1+eps)*256))
    dp = (1.0-P0)*j/98176.0
    log(f"M3 pointwise at 1+{eps} (j*={j}): dp1/ddelta = {dp:.3e}; delta for 0.70 = {0.0181713/dp:.1f}")
log("M3 at realistic single-alpha delta ~ O(1) (Exp(1) noise): v* gain ~ 8.5e-4 per unit -> "
    "negligible; point spikes carry no M2 band price.")
log("")
log("END bump_price2.log")
