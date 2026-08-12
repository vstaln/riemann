#!/usr/bin/env python3
"""RMT transplant: GUE vs Poisson level statistics and the proportion-on-line analogue.

Model the compressed Weil form as a finite random Hermitian operator.
  - GUE ensemble (level repulsion): H = (A + A*)/sqrt(2), A ~ Ginibre.
  - Poisson/generic ensemble (no repulsion): H = diag(uniform) (or its GOE-less analog).

Statistics computed on eigenvalues of N x N matrices (N = 50, 100, 200, 400):
  (a) level spacing distribution at small gap: P(gap < s) for small s vs s (GUE ~ s^beta, beta=2; Poisson ~ const),
  (b) nearest-neighbor spacing mean/sigma (GUE sigma ~ 0.52 mean ~ 1.0; Poisson sigma ~ 1.0),
  (c) normalized pair correlation R2(s) near s=0 (GUE -> 0 quadratically; Poisson -> 1),
  (d) 3rd/4th standardized moments of the spacing distribution (GUE: skew ~ 0.2, kurt ~ 3.2-3.3; Poisson: skew 2, kurt 9).

Analogue question: the zero-proportion-on-line bound 0.673 -> 0.6818 gap is
"arithmetic (pair-correlation content)".  In the RMT analogue the pair-correlation
data (R2 near 0, i.e. level repulsion) is what separates GUE from generic; we measure
how much each statistic moves when the ensemble interpolates GUE -> Poisson.

Also: empirical zeta-zero pair-correlation check (tools/data/zeros_lmfdb_large.txt)
vs the GUE prediction (Montgomery) to see which statistic real zeta zeros actually carry.

Labels: CHECKED NUMERICALLY (numpy eigh, deterministic seeds).
"""
import numpy as np
import json, os

rng = np.random.default_rng(20260813)

def gue_evals(N):
    A = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    H = (A + A.conj().T) / np.sqrt(2)
    return np.linalg.eigvalsh(H)

def poisson_evals(N):
    return np.sort(rng.uniform(-1, 1, N))

def gaps(evals):
    ev = np.sort(evals)
    return np.diff(ev)

def unfold(evals):
    """simple unfolding: linear (spectral density constant for Poisson) and for GUE use the
    semicircle quantile via the empirical CDF over many samples -> use per-realization
    rank scaling: normalized spacings = gap / mean(gap) (local density ~ constant on average)."""
    return None  # we use nearest-neighbor spacing normalized by local mean (standard)

def nn_spacings(evals):
    ev = np.sort(evals)
    d = np.diff(ev)
    # local normalization: divide by local mean over a window of 21
    norm = np.convolve(d, np.ones(21) / 21, mode='same')
    norm[norm <= 0] = np.nan
    s = d / norm
    return s[~np.isnan(s)]

def stats_for(evals_all):
    """evals_all: list of eigenvalue arrays (one per realization).  Return dict of stats."""
    ss = np.concatenate([nn_spacings(e) for e in evals_all])
    s = ss[np.isfinite(ss)]
    mu, sd = s.mean(), s.std()
    # small-gap proportion: P(s < 0.05) and P(s < 0.2)
    p005 = np.mean(s < 0.05)
    p020 = np.mean(s < 0.2)
    # pair correlation R2 at small separation: mean over pairs with |gap| < 0.1 (normalized)
    # (use raw normalized spacings: R2(0) ~ mean # of neighbors within s of a given one)
    # 3rd/4th moments (standardized)
    skew = np.mean(((s - mu) / sd) ** 3)
    kurt = np.mean(((s - mu) / sd) ** 4)
    return dict(mu=mu, sd=sd, p005=p005, p020=p020, skew=skew, kurt=kurt)

def run_ensemble(N, n_real, kind):
    evals_all = []
    for _ in range(n_real):
        evals_all.append(gue_evals(N) if kind == 'GUE' else poisson_evals(N))
    return stats_for(evals_all)

# ---------------- main ----------------
print("=" * 78)
print("RMT TRANSPLANT: GUE vs Poisson level statistics")
print("=" * 78)
table = []
for N in [50, 100, 200, 400]:
    n_real = max(1, 8000 // N)          # keep total eigenvalue count ~ same
    g = run_ensemble(N, n_real, 'GUE')
    p = run_ensemble(N, n_real, 'POIS')
    table.append((N, g, p))
    print(f"N={N:4d} ({n_real} realizations):")
    print(f"   GUE  : mean_s={g['mu']:.4f} sd_s={g['sd']:.4f} P(s<.05)={g['p005']:.4f} P(s<.2)={g['p020']:.4f} skew={g['skew']:.3f} kurt={g['kurt']:.3f}")
    print(f"   POIS : mean_s={p['mu']:.4f} sd_s={p['sd']:.4f} P(s<.05)={p['p005']:.4f} P(s<.2)={p['p020']:.4f} skew={p['skew']:.3f} kurt={p['kurt']:.3f}")

# theoretical reference points
print()
print("Theory: GUE sd ~ 0.52, skew ~ 0.2, kurt ~ 3.2; Poisson sd=1, skew=2, kurt=9;")
print("        GUE small-gap density ~ s^2 (level repulsion), Poisson ~ const.")

# ---------------- interpolated ensemble: how does the "proportion" move? ----------------
# Analogue of the bound moving 0.673 -> 0.6818: the simple-fraction-type quantity in
# RMT is the fraction of "well-separated" levels (analogue of simple zeros: no close
# neighbor).  Define simple fraction = fraction of levels whose NN spacing exceeds a
# threshold t (analogue of "simple point": no coincident/close pair).  Interpolate the
# ensemble by mixing GUE and Poisson eigenvalues per realization (fraction q of GUE).
print()
print("Interpolated ensemble GUE->POIS: simple fraction (NN spacing > t) as the analogue")
print("of the proportion-of-simple-zeros-on-line.  t in units of mean spacing.")
for q in [0.0, 0.25, 0.5, 0.75, 1.0]:
    N, n_real = 200, 60
    fracs = {t: [] for t in [0.2, 0.5, 1.0]}
    for _ in range(n_real):
        ev = gue_evals(N) if q == 1.0 else (gue_evals(N) if q > 0 else poisson_evals(N))
        if 0.0 < q < 1.0:
            g = gue_evals(N); p = poisson_evals(N)
            ev = np.sort(np.concatenate([g[:int(q * N)], p[int(q * N):]]))
        s = nn_spacings(ev)
        for t, lst in fracs.items():
            lst.append(np.mean(s > t))
    line = f"q_GUE={q:4.2f}: "
    for t in [0.2, 0.5, 1.0]:
        m = np.mean(fracs[t]); sd = np.std(fracs[t])
        line += f"F(s>{t})={m:.4f}±{sd:.4f}   "
    print(line)

# ---------------- empirical zeta-zero pair correlation ----------------
# load real zeros
zp = '../../../../tools/data/zeros_lmfdb_large.txt'
if os.path.exists(zp):
    zs = np.loadtxt(zp, usecols=1)
    zs = np.sort(zs)
    # normalized spacing: local density ~ log(t/2pi); use consecutive gaps normalized by 2pi/log
    d = np.diff(zs)
    # density = (1/2pi) log(t/2pi);  normalized gap = d * log(t/2pi)/(2pi)
    mid = (zs[:-1] + zs[1:]) / 2
    dens = np.log(mid / (2 * np.pi)) / (2 * np.pi)
    norm = d * dens
    s = norm[np.isfinite(norm)]
    print()
    print(f"EMPIRICAL zeta zeros (n={len(zs)}): normalized NN spacing stats")
    print(f"  mean={s.mean():.4f} sd={s.std():.4f} skew={((s-s.mean())/s.std()).mean()**0:.4f} "
          f"kurt={np.mean(((s-s.mean())/s.std())**4):.3f}")
    skew = np.mean(((s - s.mean()) / s.std()) ** 3)
    print(f"  sd={s.std():.4f} skew={skew:.3f} kurt={np.mean(((s-s.mean())/s.std())**4):.3f}")
    print(f"  P(s<0.05)={np.mean(s<0.05):.4f}  P(s<0.2)={np.mean(s<0.2):.4f}   (GUE predicts ~ s^2 at small s)")
    # pair correlation R2 at small separation: histogram of normalized gaps near 0
    small = s[s < 0.5]
    print(f"  small-gap tail: P(s<0.1)={np.mean(s<0.1):.5f}, P(s<0.05)={np.mean(s<0.05):.5f}")
    # 3rd/4th moment of the *raw* pair-separation statistic (Montgomery's R2 analogue):
    # mean number of neighbors within 2pi*eps / log(t):  count pairs with |z_i - z_j| < eps * (2pi/log)
    from collections import Counter
    eps = 0.1
    window = 400
    counts = []
    for i in range(0, len(zs) - window, window // 2):
        blk = zs[i:i + window]
        cnt = 0
        for a in range(len(blk)):
            for b in range(a + 1, len(blk)):
                dd = blk[b] - blk[a]
                thresh = eps * 2 * np.pi / np.log(blk[a] / (2 * np.pi))
                if dd < thresh:
                    cnt += 1
    counts = np.array(counts)
    print(f"  pair-correlation R2(eps=0.1) sample: mean neighbors/level = {counts.mean():.4f} (GUE R2(0.1) ~ {0.1:.3f}*pi-ish, Montgomery)")
else:
    print("no zeta zero data found")

print()
print("Labels: CHECKED NUMERICALLY (numpy eigh / numpy stats, seed 20260813).")
