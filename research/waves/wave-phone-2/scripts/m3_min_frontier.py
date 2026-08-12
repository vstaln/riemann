#!/usr/bin/env python3
"""m3-min-frontier: (1) realized T of the REAL ZEROS at N=64/256 (unmarked connected
part: T = m3 - D - pair, D=1, pair=(3/N)sum K^2), continuum sinc kernel lam=1/2,
theta/pi unfolding; (2) pool LP min p1 with T in realized range (appended later).
Honesty: numbers only from this script; labels in the note.
"""
import numpy as np, sys, time

def load_zeros(fn):
    z = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                z.append(float(p[1]))
    return np.array(z)

def unfold(g):
    # theta/pi unfolding (density 1), per empirical_m3.py
    return (g/(2*np.pi))*np.log(g/(2*np.pi)) - g/(2*np.pi) + 7/8

def block_stats(xs, N, la):
    """xs sorted ordinates; take consecutive N-blocks; return list of (m3, D, pair, T)"""
    out = []
    nb = len(xs) // N
    for b in range(nb):
        x = xs[b*N:(b+1)*N]
        d = x[:, None] - x[None, :]
        G = np.sinc(la*d)
        m3 = np.trace(G @ G @ G).real / N
        D = 1.0
        K2 = G*G
        pair = 3.0*np.sum(K2 - np.diag(np.diag(K2))).real / N   # (3/N) sum_{i!=j} K^2
        T = m3 - D - pair
        out.append((m3, D, pair, T))
    return out

if __name__ == "__main__":
    t0 = time.time()
    fn = "/root/riemann/tools/data/zeros_computed_10000.txt"
    g = load_zeros(fn)
    x = np.sort(unfold(g))
    print(f"zeros loaded: {len(g)}, x-range [{x[0]:.3f},{x[-1]:.3f}], mean spacing {np.mean(np.diff(x)):.4f}")
    for N in (64, 256):
        st = block_stats(x, N, 0.5)
        m3s = np.array([s[0] for s in st]); Ts = np.array([s[3] for s in st])
        print(f"N={N}: {len(st)} blocks | m3 {m3s.min():.3f}..{m3s.max():.3f} mean {m3s.mean():.3f} | "
              f"T {Ts.min():.4f}..{Ts.max():.4f} mean {Ts.mean():.4f} | T-blocks: " +
              " ".join(f"{t:.3f}" for t in Ts))
    print(f"elapsed {time.time()-t0:.1f}s")
