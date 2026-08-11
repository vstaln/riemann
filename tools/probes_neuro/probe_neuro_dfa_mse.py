#!/usr/bin/env python3
"""Probe N-R2 [N6.2 + N6.3]: loss-of-complexity diagnostics for the zero sequence.

Motivation (neurodegeneration pool): physiologic-signal diagnostics measure
long-range correlations (DFA exponent, Peng 1994) and scale-resolved complexity
(multiscale sample entropy, Costa-Goldberger-Peng 2002). The task hint maps
"loss of complexity" to our F^(alpha) beyond 1. Music-ling R3 already measured
single-scale structure (gap entropy, LZ76, Zipf: GUE-with-noise, no structure).
Here we add the two scale-resolved, model-free statistics NOT yet in the battery:
  (a) DFA exponent alpha of the normalized gap sequence (long-range correlation):
      white noise ~ 0.5, 1/f ~ 1.0, periodic/crystal -> 0 (anticorrelated),
      Poisson -> 0.5. The sine-kernel (GUE-like) zeros are the honest null.
  (b) Multiscale sample entropy SampEn(tau) at coarse-grainings tau = 1,2,4,8,16:
      a periodic crystal collapses to ~0 at every scale; GUE-like gaps are
      scale-invariant-ish; a "loss of complexity" would show a drop vs the null.

Worlds (all n = 2000 for comparability): real zeros (segment), sine-kernel synthetic
(GUE-like, DPP sampler copied from tools/sine_sim.py), jittered lattice (crystal
proxy, the 256-law is a marked lattice), Poisson (no repulsion).

Run: cd tools && uv run --quiet --with numpy python probes_neuro/probe_neuro_dfa_mse.py
"""
import numpy as np

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    return np.sort(np.array(g))

def sine_sample(rng, L=60.0, M=1200):
    """Sine-kernel DPP sampler (copy of tools/sine_sim.py sample_config)."""
    xs = np.linspace(-L/2, L/2, M, endpoint=False)
    dx = L/M
    S = np.sinc((xs[:, None] - xs[None, :]))
    K = S * dx
    evals, evecs = np.linalg.eigh(K)
    mask = evals > 1e-10
    evals = evals[mask]; evecs = evecs[:, mask]
    Psi = evecs * np.sqrt(dx)
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
            X = np.array(chosen); PX = PsiJ[X, :]; A = PX @ PX.T
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
    return xs[np.array(chosen)]

def gaps_normalized(pts):
    pts = np.sort(np.array(pts, dtype=float))
    sp = np.diff(pts).mean()
    return np.diff(pts) / sp

def dfa(x, scales=None):
    """Detrended fluctuation analysis: F(s) over box sizes s; returns (scales, F, alpha)."""
    x = np.asarray(x, dtype=float)
    y = np.cumsum(x - x.mean())
    n = y.size
    if scales is None:
        scales = np.unique(np.floor(2 ** np.arange(3, np.log2(n) - 1, 0.25)).astype(int))
        scales = scales[(scales >= 8) & (scales <= n // 4)]
    F = []
    ss = []
    for s in scales:
        nwin = n // s
        if nwin < 2:
            continue
        seg = y[: nwin * s].reshape(nwin, s)
        t = np.arange(s, dtype=float)
        # linear fit per window
        tt = t - t.mean()
        den = (tt * tt).sum()
        slope = (seg * tt[None, :]).sum(axis=1) / den
        inter = seg.mean(axis=1) - slope * t.mean()
        fit = slope[:, None] * t[None, :] + inter[:, None]
        resid = seg - fit
        F.append(np.sqrt((resid * resid).mean()))
        ss.append(s)
    F = np.array(F)
    ss = np.array(ss)
    alpha = np.polyfit(np.log(ss), np.log(F), 1)[0] if F.size >= 3 else np.nan
    return ss, F, alpha

def sampen(x, m=2, r=0.2):
    """Sample entropy (Richman-Moorman). r relative to std (absolute r = r*std)."""
    x = np.asarray(x, dtype=float)
    n = x.size
    if n < m + 2:
        return np.nan
    sd = x.std()
    if sd < 1e-12:
        return 0.0
    eps = r * sd
    def count_matches(mm):
        # template count for length-mm: number of pairs within eps on all mm coords
        # vectorized over all starting indices
        k = n - mm + 1
        X = np.stack([x[i:i + k] for i in range(mm)], axis=1)  # k x mm
        # pairwise: for each pair of rows, max abs diff over coords <= eps
        # use chunking to bound memory
        cnt = 0
        B = 256
        total = 0
        for i0 in range(0, k, B):
            i1 = min(i0 + B, k)
            block = X[i0:i1]           # B x mm
            d = np.abs(block[:, None, :] - X[None, :, :])  # B x k x mm
            match = (d <= eps).all(axis=2)  # B x k
            total += match.sum()
        total -= k  # exclude self-matches (i==j counted once per i)
        return total
    A = count_matches(m + 1)
    B = count_matches(m)
    if B == 0 or A == 0:
        return np.nan
    return -np.log(A / B)

def main():
    rng = np.random.default_rng(20260811)
    n = 2000

    # ---- real zeros (mid-band segment for stationarity) ----
    x10k = load("data/zeros_computed_10000.txt")
    seg = x10k[3000:3000 + n]
    g_real = gaps_normalized(seg)

    # ---- sine-kernel synthetic (GUE-like null) ----
    pts = sine_sample(rng)
    while pts.size < n + 2:
        pts = np.concatenate([pts, sine_sample(rng)])
    g_sine = gaps_normalized(pts[:n + 1])

    # ---- jittered lattice (crystal proxy: marked lattice with jitter) ----
    lattice = np.arange(n + 1) + 0.5 + rng.uniform(-0.2, 0.2, n + 1)
    g_lat = gaps_normalized(lattice)

    # ---- Poisson ----
    poisson = np.cumsum(rng.exponential(1.0, n + 1))
    g_poi = gaps_normalized(poisson)

    worlds = {"real (zeta)": g_real, "sine (GUE)": g_sine,
              "jittered lattice (crystal)": g_lat, "poisson": g_poi}

    print("== N-R2 [N6.2+N6.3] DFA exponent + multiscale sample entropy of normalized gaps ==")
    print("n =", n)
    print("\n--- (a) DFA exponent alpha (F(s) ~ s^alpha; 0.5 white, 1.0 1/f, ~0 periodic) ---")
    for name, g in worlds.items():
        _, _, a = dfa(g)
        print(f"  {name:28s}: alpha = {a:.4f}")

    print("\n--- (b) multiscale sample entropy SampEn(tau), m=2, r=0.2*std ---")
    taus = [1, 2, 4, 8, 16]
    hdr = "  " + "".join(f"{('tau='+str(t)):>10s}" for t in taus)
    print(hdr)
    for name, g in worlds.items():
        row = []
        for t in taus:
            if t == 1:
                cg = g
            else:
                k = g.size - (g.size % t)
                cg = g[:k].reshape(-1, t).mean(axis=1)
            row.append(sampen(cg))
        print(f"  {name:28s}:" + "".join(f"{v:>10.3f}" if v == v else f"{'nan':>10s}" for v in row))

if __name__ == "__main__":
    main()
