#!/usr/bin/env python3
"""B3.2 + B1.4 (biology note): sine-kernel (determinantal) null baseline for the
finite-T deficit, and decoy-discrimination statistics (real zeros vs null).

Null process: the determinantal sine process (unit density, sine-kernel
repulsion) -- the correct null with the SAME asymptotic pair correlations as
zeta's zeros (F=1 on [0,1]), sampled via the kernel's spectral expansion
(Bernoulli inclusion of eigenvectors; algorithm as in tools/sine_sim.py,
reimplemented here self-contained).

(a) B3.2: Delta(T) = bound/N - 0.6725007 for real zeros vs Delta_null(N) for
    the sine process at matched N, same cosine-window construction.  If
    Delta ~ Delta_null, the finite-T deficit is construction/sampling artifact
    ("repertoire sampling noise"); the excess is the arithmetic signal.

(b) B1.4: decoy-discrimination z-scores (spacing ratio, counting variance, gap
    skewness, max gap, spacing entropy) between real zeros and null samples.

Run:  uv run --quiet --with numpy --with scipy python -u null_baseline.py
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
I2 = 0.5 + np.sin(SQRT2) / (2 * SQRT2)
C = 1.0 / (SQRT2 * np.pi)
TARGET = 3/2 - (1/SQRT2) * (np.cos(1/SQRT2) / np.sin(1/SQRT2))  # 0.6725007...

# ---------------- shared W construction (cosine window) ----------------
def build_W(s, N):
    V = np.empty((s.size, N))
    for k in range(N):
        t = s - k
        V[:, k] = 0.5 * (np.sinc(C - t) + np.sinc(C + t))
    return (V.T @ V) / I2

def bound_of(W):
    tr = np.trace(W)
    HS2 = np.einsum('ij,ij->', W, W)
    return (2 * tr - HS2) / W.shape[0]

# ---------------- determinantal sine process sampler ----------------
class SineDPP:
    """Sine-kernel DPP on [0, L] via spectral expansion (density 1)."""
    def __init__(self, L, rng):
        M = 2 * int(L)              # grid resolution dx = 1/2
        xs = np.linspace(0, L, M, endpoint=False)
        dx = L / M
        K = np.sinc((xs[:, None] - xs[None, :])) * dx
        evals, evecs = np.linalg.eigh(K)
        mask = evals > 1e-10
        self.xs = xs
        self.evals = evals[mask]
        self.Psi = evecs[:, mask] * np.sqrt(dx)
        self.rng = rng

    def sample(self):
        Psi, evals, rng, M = self.Psi, self.evals, self.rng, self.xs.size
        r_max = Psi.shape[1]
        inc = rng.random(r_max) < evals
        if not inc.any():
            return np.zeros(0)
        PsiJ = Psi[:, inc]
        r = PsiJ.shape[1]
        Pmm = np.einsum('ij,ij->i', PsiJ, PsiJ)
        chosen = []
        while len(chosen) < r:
            if chosen:
                X = np.array(chosen)
                PX = PsiJ[X, :]
                A = PX @ PX.T
                PmX = PsiJ @ PX.T
                sol = np.linalg.solve(A, PmX.T)
                corr = np.einsum('mk,mk->m', PmX, sol.T)
                diag = np.clip(Pmm - corr, 0, None)
            else:
                diag = Pmm
            tot = diag.sum()
            if tot < 1e-9:
                break
            m = rng.choice(M, p=diag / tot)
            chosen.append(m)
        return self.xs[np.array(chosen)]

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
    zs = np.loadtxt('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')[:, 1]
    AF = {100: 50, 150: 86, 200: 123, 250: 161, 300: 203, 350: 245,
          400: 289, 500: 380}
    NSAMP = {50: 24, 86: 20, 123: 18, 161: 16, 203: 14, 245: 12, 289: 10, 380: 8}

    print("=== B3.2: finite-T deficit vs sine-kernel null sampling noise ===")
    print(f"{'T':>5} {'N':>4} {'Delta_real':>11} {'Delta_null mean':>15} {'Delta_null sd':>13}")
    rng = np.random.default_rng(20260217)
    cache = {}
    for T, N in AF.items():
        sel = (zs >= T) & (zs < 2 * T)
        s_real = (zs[sel] - T) * N / T
        d_real = bound_of(build_W(s_real, N)) - TARGET
        if N not in cache:
            cache[N] = SineDPP(N, rng)
        dpp = cache[N]
        dnull = np.empty(NSAMP[N])
        for i in range(NSAMP[N]):
            pts = dpp.sample()
            n = pts.size
            if n < 8:
                dnull[i] = np.nan
                continue
            dnull[i] = bound_of(build_W(pts, n)) - TARGET
        print(f"{T:>5} {N:>4} {d_real:>11.6f} {np.nanmean(dnull):>15.6f} {np.nanstd(dnull):>13.6f}")

    print("\n=== B1.4 decoy-discrimination: real zeros vs sine null (matched N) ===")
    for (T, N, ns) in [(500, 380, 8), (300, 203, 10), (700, 569, 6)]:
        sel = (zs >= T) & (zs < 2 * T)
        s_real = (zs[sel] - T) * N / T
        sr = stats(s_real)
        rng2 = np.random.default_rng(7)
        sn = np.array([stats(SineDPP(N, rng2).sample()) for _ in range(ns)])
        names = ["spacing ratio", "counting var", "gap skewness", "max gap", "spacing entropy"]
        print(f"\nT={T}, N={N}, null samples n={ns}:")
        print(f"{'stat':>16} {'real':>10} {'null mean':>10} {'null sd':>10} {'z':>8}")
        for i, nm in enumerate(names):
            z = (sr[i] - np.nanmean(sn[:, i])) / (np.nanstd(sn[:, i]) + 1e-30)
            print(f"{nm:>16} {sr[i]:>10.4f} {np.nanmean(sn[:, i]):>10.4f} "
                  f"{np.nanstd(sn[:, i]):>10.4f} {z:>8.2f}")

if __name__ == '__main__':
    main()
