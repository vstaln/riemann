#!/usr/bin/env python3
"""924k-zeros stats: marked-T read (the 0.70 gap input) + m3 + spacing at 9.25x sample."""
import numpy as np

def load_zeros(fn, n):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 1:
                try: g.append(float(p[-1]))
                except ValueError: pass
            if len(g) >= n: break
    return np.array(g[:n])

def unfold(g):
    # m3_min_frontier convention: N(t) = (t/2pi)ln(t/2pi) - t/2pi + 7/8 (density 1)
    return (g/(2*np.pi))*np.log(g/(2*np.pi)) - g/(2*np.pi) + 7/8

def block_stats(xs, N, la):
    out = []
    nb = len(xs)//N
    for b in range(nb):
        x = xs[b*N:(b+1)*N]
        d = x[:, None] - x[None, :]
        G = np.sinc(la*d)
        m3 = np.trace(G @ G @ G).real / N
        D = 1.0
        K2 = G*G                       # elementwise square (verbatim m3_min_frontier)
        pair = 3.0*np.sum(K2 - np.diag(np.diag(K2))).real / N
        T = m3 - D - pair
        out.append((m3, D, pair, T))
    return np.array(out)

g = load_zeros("/root/riemann/tools/data/zeros_rust_924k.txt", 924000)
xu = unfold(g)
print(f"loaded {len(g)} zeros, t in [{g[0]:.4f},{g[-1]:.1f}]")

for Nblk in [64, 256]:
    st = block_stats(xu, Nblk, 0.5)
    m3 = st[:,0]; T = st[:,3]
    print(f"N={Nblk}: {len(st)} blocks: m3={m3.mean():.5f} +- {m3.std()/np.sqrt(len(st)):.5f} | "
          f"T: mean={T.mean():+.5f} +- {T.std()/np.sqrt(len(st)):.5f}, range=[{T.min():+.4f},{T.max():+.4f}]")

# spacing diagnostics at high N
gaps = np.diff(xu)
print(f"SPACING: min={gaps.min():.5f}, frac(gap<0.1)={np.mean(gaps<0.1):.6f} (0.924M zeros), "
      f"frac(gap<0.05)={np.mean(gaps<0.05):.6f}, frac(gap<0.5)={np.mean(gaps<0.5):.5f}")
