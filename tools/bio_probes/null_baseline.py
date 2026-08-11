#!/usr/bin/env python3
"""B3.2 + B1.4 (biology note): GUE null baseline for the finite-T deficit, and
decoy-discrimination statistics (real zeros vs GUE null at matched N).

(a) B3.2: the finite-T deficit Delta(T) = bound/N - 0.6725007 (attack-finitet)
    compared against Delta_null(N) for a GUE (sine-kernel) null process with the
    SAME cosine-window construction and the SAME N.  If Delta ~ Delta_null, the
    whole finite-T deficit is construction/sampling artifact (the "repertoire
    sampling noise"); the excess is the arithmetic signal.

(b) B1.4: decoy-discrimination screen -- candidate statistics computed on real
    zeros vs GUE-null samples at matched N, z = (mean_real - mean_null)/std_null:
      spacing ratio, counting variance, gap skewness, max gap, spacing entropy.

Run:  uv run --quiet --with numpy --with scipy python null_baseline.py
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
I2 = 0.5 + np.sin(SQRT2) / (2 * SQRT2)
C = 1.0 / (SQRT2 * np.pi)
TARGET = 3/2 - (1/SQRT2) * (np.cos(1/SQRT2) / np.sin(1/SQRT2))  # 0.6725007...

# ---------- shared W construction ----------
def build_W(s, N):
    # Psi(s) = (1/2)[sinc(C-s) + sinc(C+s)]  (Rust main.rs: sin(a)/(sqrt2 - 2 pi s) = sin(a)/(2a))
    V = np.empty((s.size, N))
    for k in range(N):
        t = s - k
        V[:, k] = 0.5 * (np.sinc(C - t) + np.sinc(C + t))
    return (V.T @ V) / I2

def bound_of(W):
    tr = np.trace(W)
    HS2 = np.einsum('ij,ij->', W, W)
    return (2 * tr - HS2) / W.shape[0]

# ---------- GUE null points ----------
def gue_points(N, rng):
    """N GUE eigenvalues mapped to unit density on [0, N)."""
    A = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    A = (A + A.conj().T) / 2
    ev = np.linalg.eigvalsh(A)
    return np.sort(N * (ev / (2 * np.sqrt(N)) + 1) / 2)

def stats(s):
    g = np.diff(np.sort(s))
    m = g.mean()
    if m <= 0:
        return None
    gn = g / m
    r = np.minimum(gn[:-1], gn[1:]) / np.maximum(gn[:-1], gn[1:])
    nb = int(np.ceil(np.max(s)))
    counts, _ = np.histogram(s, bins=np.arange(0, nb + 2))
    skew = np.mean((gn - 1) ** 3) / (np.std(gn) ** 3 + 1e-30)
    maxg = np.max(gn)
    hist, _ = np.histogram(gn, bins=20, range=(0, 6))
    p = hist / hist.sum()
    ent = -np.sum(p[p > 0] * np.log(p[p > 0]))
    return np.array([np.mean(r), np.var(counts), skew, maxg, ent])

def main():
    print(f"0.6725007 = {TARGET:.10f}")
    zs = np.loadtxt('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')[:, 1]
    AF = {100: 50, 150: 86, 200: 123, 250: 161, 300: 203, 350: 245,
          400: 289, 500: 380, 600: 472, 700: 569}
    # real deficits recomputed here (should match attack-finitet table)
    print("\n=== B3.2: finite-T deficit vs GUE-null sampling noise ===")
    print(f"{'T':>5} {'N':>4} {'Delta_real':>11} {'Delta_null mean':>15} {'Delta_null sd':>13}")
    rng = np.random.default_rng(20260217)
    for T, N in AF.items():
        sel = (zs >= T) & (zs < 2 * T)
        s_real = (zs[sel] - T) * N / T
        d_real = bound_of(build_W(s_real, N)) - TARGET
        nsamp = 10 if N > 300 else 16
        dnull = np.empty(nsamp)
        for i in range(nsamp):
            dnull[i] = bound_of(build_W(gue_points(N, rng), N)) - TARGET
        print(f"{T:>5} {N:>4} {d_real:>11.6f} {dnull.mean():>15.6f} {dnull.std():>13.6f}")

    # ---------- B1.4 discrimination ----------
    print("\n=== B1.4 decoy-discrimination: real zeros vs GUE null (matched N) ===")
    for (T, N, ns) in [(500, 380, 20), (300, 203, 24), (700, 569, 14)]:
        sel = (zs >= T) & (zs < 2 * T)
        s_real = (zs[sel] - T) * N / T
        sr = stats(s_real)
        rng2 = np.random.default_rng(7)
        sn = np.array([stats(gue_points(N, rng2)) for _ in range(ns)])
        names = ["spacing ratio", "counting var", "gap skewness", "max gap", "spacing entropy"]
        print(f"\nT={T}, N={N}, null samples n={ns}:")
        print(f"{'stat':>16} {'real':>10} {'null mean':>10} {'null sd':>10} {'z':>8}")
        for i, nm in enumerate(names):
            z = (sr[i] - sn[:, i].mean()) / (sn[:, i].std() + 1e-30)
            print(f"{nm:>16} {sr[i]:>10.4f} {sn[:, i].mean():>10.4f} "
                  f"{sn[:, i].std():>10.4f} {z:>8.2f}")

if __name__ == '__main__':
    main()
