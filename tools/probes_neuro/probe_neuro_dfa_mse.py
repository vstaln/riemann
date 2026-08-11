#!/usr/bin/env python3
"""Probe N-R2 [N6.2 + N6.3]: loss-of-complexity diagnostics for the zero sequence.

Motivation (neurodegeneration pool): physiologic-signal diagnostics measure
long-range correlations (DFA exponent, Peng 1994) and scale-resolved complexity
(multiscale sample entropy, Costa-Goldberger-Peng 2002). The task hint maps
"loss of complexity" to our F^(alpha) beyond 1. Music-ling R3 already measured
single-scale structure (gap entropy, LZ76, Zipf: GUE-with-noise, no structure).
Here we add the two scale-resolved, model-free statistics NOT yet in the battery:
  (a) DFA exponent alpha of the normalized gap sequence (long-range correlation):
      white noise ~ 0.5, 1/f ~ 1.0, periodic/crystal -> ~0 (anticorrelated),
      Poisson -> 0.5. GUE-bulk eigenvalues (sine-kernel local statistics) are the
      honest null for the zeros.
  (b) Multiscale sample entropy SampEn(tau) at coarse-grainings tau = 1,2,4,8,16:
      a periodic crystal collapses to ~0 at every scale; GUE-like gaps are
      scale-invariant-ish; a "loss of complexity" would show a drop vs the null.

Worlds (all n = 1500 for comparability): real zeros (segment), GUE-bulk synthetic
(eigenvalues of a beta=2 Dumitriu-Edelman tridiagonal, middle bulk rescaled to mean
spacing 1 -- the standard GUE null with sine-kernel local statistics), jittered
lattice (crystal proxy: the 256-law is a marked lattice), Poisson (no repulsion).

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

def gue_bulk_gaps(n, seed=20260811):
    """GUE-eigenvalue spacings: beta=2 Dumitriu-Edelman tridiagonal, N = 2n, middle n
    eigenvalues, rescaled to mean spacing 1 (returns gap array of length n-1)."""
    rng = np.random.default_rng(seed)
    N = 2 * n
    d = rng.normal(0.0, np.sqrt(2.0), N)
    od = np.array([np.sqrt(rng.chisquare(2 * (N - k)) / 2.0) for k in range(1, N)])
    T = np.diag(d) + np.diag(od, 1) + np.diag(od, -1)
    ev = np.linalg.eigvalsh(T)
    mid = ev[N // 2 - n // 2: N // 2 + n // 2 + (n % 2)]
    mid = np.sort(mid)
    g = np.diff(mid)
    return g / g.mean()

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
    """Sample entropy (Richman-Moorman). r relative to std."""
    x = np.asarray(x, dtype=float)
    n = x.size
    if n < m + 2:
        return np.nan
    sd = x.std()
    if sd < 1e-12:
        return 0.0
    eps = r * sd
    def count_matches(mm):
        k = n - mm + 1
        X = np.stack([x[i:i + k] for i in range(mm)], axis=1)  # k x mm
        cnt = 0
        B = 256
        for i0 in range(0, k, B):
            i1 = min(i0 + B, k)
            block = X[i0:i1]
            d = np.abs(block[:, None, :] - X[None, :, :])  # B x k x mm
            cnt += (d <= eps).all(axis=2).sum()
        return cnt - k  # remove self-pairs
    A = count_matches(m + 1)
    B = count_matches(m)
    if B <= 0 or A <= 0:
        return np.nan
    return -np.log(A / B)

def main():
    rng = np.random.default_rng(20260811)
    n = 1500

    x10k = load("data/zeros_computed_10000.txt")
    seg = x10k[3000:3000 + n]
    g_real = gaps_normalized(seg)

    g_gue = gue_bulk_gaps(n)

    lattice = np.arange(n + 1) + 0.5 + rng.uniform(-0.2, 0.2, n + 1)
    g_lat = gaps_normalized(lattice)

    poisson = np.cumsum(rng.exponential(1.0, n + 1))
    g_poi = gaps_normalized(poisson)

    worlds = {"real (zeta)": g_real, "GUE bulk": g_gue,
              "jittered lattice (crystal)": g_lat, "poisson": g_poi}

    print("== N-R2 [N6.2+N6.3] DFA exponent + multiscale sample entropy of normalized gaps ==")
    print("n =", n)
    print("\n--- (a) DFA exponent alpha (F(s) ~ s^alpha; 0.5 white, 1.0 1/f, ~0 periodic) ---")
    for name, g in worlds.items():
        _, _, a = dfa(g)
        print(f"  {name:26s}: alpha = {a:.4f}")

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
            v = sampen(cg)
            row.append(f"{v:>10.3f}" if v == v else f"{'nan':>10s}")
        print(f"  {name:26s}:" + "".join(row))

if __name__ == "__main__":
    main()
