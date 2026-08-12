#!/usr/bin/env python3
"""rust-zeros stats at N=100k: periodogram band-z, marked m3(1/2), spacing diagnostics.
Numbers only from this script; zeros = tools/data/zeros_rust_100k.txt (rust-zeros v3 hybrid).
"""
import numpy as np

def theta(t):
    t = np.asarray(t, float)
    u = t/(2*np.pi)
    return (t/2)*np.log(u) - t/2 - np.pi/8 + 1.0/(48*t) + 7.0/(5760*t**3) + 31.0/(80640*t**5)

def load_zeros(n):
    g = []
    with open("/root/riemann/tools/data/zeros_rust_100k.txt") as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                try: g.append(float(p[1]))
                except ValueError: pass
            if len(g) >= n: break
    return np.array(g[:n])

def n_eff(seq):
    v = seq - seq.mean(); c0 = np.dot(v, v)
    if c0 <= 0: return 1.0
    n = v.size; out = 1.0; acc = 0.0
    for k in range(1, min(n//2, 200)):
        r = np.dot(v[k:], v[:-k])/c0
        if r <= 0: break
        acc += (1.0 - k/n)*r
    return n/(1.0 + 2*acc)

N = 100000
g = load_zeros(N)
xu = theta(g)/np.pi
print(f"loaded {len(g)} zeros, t in [{g[0]:.4f}, {g[-1]:.1f}], mean unfolded spacing {np.mean(np.diff(xu)):.5f}")

# ---- 1. periodogram band (1.005, 1.3] — same estimator as bump_price2.py ----
grid = np.arange(1.00, 1.3001, 0.005)
clean = grid > 1.005
e = np.exp(2j*np.pi*np.outer(grid, xu))
F = np.abs(e.sum(axis=1))**2/xu.size
fg = F[clean]; bm = fg.mean(); ne = n_eff(fg-1.0); sband = 1.0/np.sqrt(ne)
print(f"PERIOD: F(1.00)={F[0]:.1f}  band(1.005,1.3] mean={bm:.4f} n_eff={ne:.1f} band-z={+(bm-1.0)/sband:+.3f}")

# ---- 2. marked m3(1/2) (marks all 1 => unmarked windowed third moment) ----
def block_m3(x, la):
    """windowed m3 = tr(G^3)/N on a block, G = sinc(pi*la*(xi-xj)) (theta/pi unfolded, density 1)."""
    d = x[:, None] - x[None, :]
    G = np.sinc(la*d)
    return np.trace(G @ G @ G).real / x.size
m3s = []
Nblk = 256
nb = len(xu)//Nblk
for b in range(nb):
    m3s.append(block_m3(xu[b*Nblk:(b+1)*Nblk], 0.5))
m3s = np.array(m3s)
print(f"M3(1/2): N=256 blocks: {nb} blocks, mean={m3s.mean():.4f} ± {m3s.std()/np.sqrt(nb):.4f} (PROVEN 5, finite-height deficit up from 4.75@N=256-10k)")

# ---- 3. spacing diagnostics (unfolded gaps) ----
gaps = np.diff(xu)
print(f"SPACING: mean={gaps.mean():.5f} (unfolded => 1 expected), min={gaps.min():.5f}, max={gaps.max():.5f}")
frac_01 = (gaps < 0.1).mean(); frac_03 = (gaps < 0.3).mean(); frac_05 = (gaps < 0.5).mean()
# sine-process (Wigner-ish) small-gap predictions: P(<s) ~ (pi^2/3)s^3 for tiny s; Poisson: ~s
print(f"  frac(gap<0.1)={frac_01:.5f} (Poisson 0.095, sine-kernel ~0.0033) | frac<0.3={frac_03:.5f} | frac<0.5={frac_05:.5f}")
w = (gaps < 0.5).sum()
print(f"  count gap<0.5 = {w} of {gaps.size}")
