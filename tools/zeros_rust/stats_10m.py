#!/usr/bin/env python3
"""21M-zeros statistics (stats_10m): block m3 / pair / marked-T at multiple N,
T-block autocorrelation (rho_1/rho_5, wave-2 measured -0.136/+0.163), spacing
diagnostics, and m3-deficit scaling. Extends stats_924k.py to the 10^7-height
dataset produced by faster_finder shards.

Usage: python3 stats_10m.py <zeros_file> [max_zeros]
"""
import sys
import numpy as np


def load_zeros(fn, n=None):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 1:
                try:
                    g.append(float(p[-1]))
                except ValueError:
                    pass
            if n and len(g) >= n:
                break
    return np.array(g[:n])


def unfold(g):
    # density-1 unfolding (m3_min_frontier convention)
    return (g / (2 * np.pi)) * np.log(g / (2 * np.pi)) - g / (2 * np.pi) + 7 / 8


def block_stats(xs, N, la):
    """m3 = trace(G^3)/N, pair = 3*sum(K2 off-diag)/N, T = m3 - D - pair (D=1)."""
    out = []
    nb = len(xs) // N
    for b in range(nb):
        x = xs[b * N:(b + 1) * N]
        d = x[:, None] - x[None, :]
        G = np.sinc(la * d)
        m3 = np.trace(G @ G @ G).real / N
        K2 = G * G
        pair = 3.0 * np.sum(K2 - np.diag(np.diag(K2))).real / N
        T = m3 - 1.0 - pair
        out.append((m3, pair, T))
    return np.array(out)


def autocorr(T):
    """lag-1 and lag-5 autocorrelation of the T-block sequence."""
    T = T - T.mean()
    v = np.dot(T, T)
    r1 = np.dot(T[:-1], T[1:]) / v if len(T) > 1 else 0.0
    r5 = np.dot(T[:-5], T[5:]) / v if len(T) > 5 else 0.0
    return r1, r5


def main():
    fn = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else None
    g = load_zeros(fn, n)
    xu = unfold(g)
    print("loaded %d zeros, t in [%.4f, %.1f]" % (len(g), g[0], g[-1]))

    for Nblk in [64, 256, 512]:
        st = block_stats(xu, Nblk, 0.5)
        m3 = st[:, 0]
        pair = st[:, 1]
        T = st[:, 2]
        se = lambda v: v.std() / np.sqrt(len(v))
        r1, r5 = autocorr(T)
        print("N=%d: %d blocks: m3=%.5f +- %.5f | pair=%.5f +- %.5f | "
              "T: mean=%+.5f +- %.5f, min=%+.4f, max=%+.4f | rho1=%+.4f, rho5=%+.4f"
              % (Nblk, len(st), m3.mean(), se(m3), pair.mean(), se(pair),
                 T.mean(), se(T), T.min(), T.max(), r1, r5))

    gaps = np.diff(xu)
    print("SPACING: min=%.5f | frac(<0.1)=%.6f frac(<0.05)=%.6f frac(<0.15)=%.6f"
          % (gaps.min(), np.mean(gaps < 0.1), np.mean(gaps < 0.05), np.mean(gaps < 0.15)))
    # small-gap tail exponent over [0.05, 0.15] (sine-kernel 3)
    sel = gaps[(gaps >= 0.05) & (gaps <= 0.15)]
    if len(sel) > 10:
        # P(gap < x) ~ C x^e  =>  log C + e log x
        xs = np.linspace(0.05, 0.15, 21)
        ys = np.array([np.mean(gaps < x) for x in xs])
        A = np.vstack([np.ones_like(xs), np.log(xs)]).T
        coef, *_ = np.linalg.lstsq(A, np.log(ys), rcond=None)
        print("small-gap tail exponent e = %.3f +- (fit) on [0.05,0.15]" % coef[1])
    # m3-deficit: mean(3 - m3) vs N (deficit exponent)
    print("m3 at N=512: %.5f (deficit vs 3: %.5f)" % (st[:, 0].mean(), 3 - st[:, 0].mean()))


if __name__ == "__main__":
    main()
