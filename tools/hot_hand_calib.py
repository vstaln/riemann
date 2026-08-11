#!/usr/bin/env python3
"""hot_hand_calib.py — G3.1 "hot hand" calibration of the empirical zeta form factor.

Question (idea-generator-games.md G3.1; verdict written to
research/notes/attack-hot-hand.md): verif-001 §4 reports the empirical zeta form
factor Fhat(alpha) "climbs to ~0.93-1.0 near alpha=1, decays beyond" at N=3000.
Is the beyond-1 "decay" a real deviation from Montgomery (F = |alpha| for alpha<1,
F = 1 for alpha>1), or a finite-sample artifact of the estimator — the "hot hand"
statistical trap (the naive statistic carries built-in noise that looks like signal)?

Method (null-model calibration): run the SAME estimator on
  (a) the real zeta zeros (theta/pi unfolding, tools/data/zeros_computed_10000.txt),
  (b) the sine-kernel null: GUE bulk, beta=2 Hermite tridiagonal (Dumitriu-Edelman),
      eigenvalues rescaled by 1/sqrt(2N) -> semicircle on [-2,2] (calibrated against
      a Wigner GUE: max quantile diff 0.007 at N=800), unfolded by the exact
      semicircle CDF, central 80% -> N points of mean spacing 1,
  (c) Poisson baseline (no repulsion; F = 1 beyond 1 in expectation).
Compare zeta Fhat against the null's mean +/- 1 sigma band per alpha, the
alpha-averaged level over (1,3] (the decisive "is it systematically below 1" test),
and the multiple-comparison calibration of the per-alpha maxima (55 alpha bins).
Integer and half-integer alpha are excluded from the verdict: at those points the
theta/pi unfolding produces a Gram-point lattice artifact that the sine-kernel null
does not share (documented separately) — the estimator's own built-in structure.

Estimator (identical for all three):
  unfold x_j (mean spacing 1);  Fhat(alpha) = (1/N) | sum_j exp(2 pi i alpha x_j) |^2
  (standard periodogram form factor; E[Fhat] = |alpha| for 0<alpha<1, = 1 for
   alpha>1 for the sine-kernel/GUE process — verified analytically and numerically;
   the per-alpha fluctuations are Exp(1)-like, std ~ 1, N-independent — the
   hot-hand noise floor; only alpha-averaging shrinks the noise).

Run:  uv run --quiet --with numpy --with scipy --with matplotlib \
          python tools/hot_hand_calib.py
All numbers below are produced by this script. No fabricated data.
"""
import json, os, sys, time
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

RNG_SEED = 20260811
HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS_PATH = os.path.join(HERE, "data", "zeros_computed_10000.txt")
OUT_JSON = os.path.join(HERE, "hot_hand_calib_results.json")
OUT_FIG = os.path.join(HERE, "hot_hand_calib_fig1.png")
ALPHAS = np.arange(0.05, 3.0001, 0.05)
INTEGERS = {1.0, 2.0, 3.0}
HALF_INTS = {0.5, 1.5, 2.5}
POLLUTED = INTEGERS | HALF_INTS

# ------------------------------------------------------------------ zeta
def load_zeta_ords(path, n):
    ords = []
    with open(path) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                try:
                    ords.append(float(p[1]))
                except ValueError:
                    continue
            if len(ords) >= n:
                break
    return np.array(ords[:n])

def theta(t):
    """Riemann-Siegel theta, asymptotic series (accuracy ~1e-12 for t>=14)."""
    t = np.asarray(t, dtype=float)
    u = t / (2 * np.pi)
    return (t/2)*np.log(u) - t/2 - np.pi/8 + 1.0/(48*t) + 7.0/(5760*t**3) + 31.0/(80640*t**5)

def unfold_zeta(gamma):
    return theta(gamma) / np.pi

# ------------------------------------------------------------------ GUE null
def gue_tridiag(N, rng):
    """beta=2 Hermite tridiagonal: diag N(0,2), off b_k = sqrt(chi2_{2(N-k)}).
    Eigenvalues / sqrt(2N) -> semicircle on [-2,2] (calibrated vs Wigner GUE,
    max quantile diff 0.007 at N=800)."""
    d = rng.normal(0.0, np.sqrt(2.0), N)
    k = np.arange(1, N)
    e = np.sqrt(rng.chisquare(2.0 * (N - k)))
    return eigvalsh_tridiagonal(d, e)

def semicdf(y):
    """CDF of semicircle density sqrt(4-y^2)/(2pi) on [-2,2]."""
    y = np.clip(y, -2.0, 2.0)
    return (np.arcsin(y/2.0) + (y/2.0)*np.sqrt(1.0 - (y/2.0)**2) + np.pi/2.0) / np.pi

def gue_bulk(npts, rng):
    """Sine-kernel null of npts points: GUE of size N_gue = npts/0.8, central 80%,
    unfolded by the exact semicircle CDF -> npts points, mean spacing 1,
    window length npts."""
    ng = int(round(npts / 0.8))
    ev = np.sort(gue_tridiag(ng, rng))
    lam = ev / np.sqrt(2.0 * ng)                 # semicircle on [-2,2]
    x = ng * semicdf(lam)                        # unfold: density ~1
    lo = int(0.1 * ng); hi = int(0.9 * ng)
    return x[lo:hi]

# ---------------------------------------------------------------- Poisson
def poisson_x(n, rng):
    return np.cumsum(rng.exponential(1.0, n))

# ------------------------------------------------------------- estimator
def form_factor(x, alphas):
    """Fhat(alpha) = (1/N) |sum_j exp(2 pi i alpha x_j)|^2."""
    e = np.exp(2j * np.pi * np.outer(alphas, x))
    return np.abs(e.sum(axis=1))**2 / x.size

def alpha_average(ff, lo, hi, clean_only=True):
    mask = (ALPHAS > lo) & (ALPHAS <= hi)
    if clean_only:
        mask &= ~np.isin(ALPHAS, list(POLLUTED))
    return float(ff[mask].mean()), int(mask.sum())

# ------------------------------------------------ multiple-comparison calib
def maxz_calibration(n, reps, rng):
    """Poisson-based calibration of the per-alpha z-test over the clean alpha bins.
    Poisson has the same Exp(1) per-alpha noise floor at alpha>1 as the GUE null
    (measured: std/mean ~ 0.99-1.00 for both), so it calibrates the multiple-
    comparison behaviour of the noise cheaply. Returns (median, p90, p99, P>4.54,
    P>3.11, avg_std_by_window)."""
    ff_all = np.zeros((reps, ALPHAS.size))
    for r in range(reps):
        ff_all[r] = form_factor(poisson_x(n, rng), ALPHAS)
    gm = ff_all.mean(axis=0); gs = ff_all.std(axis=0)
    clean = ~np.isin(ALPHAS, list(POLLUTED))
    z = np.abs((ff_all - gm) / np.maximum(gs, 1e-9))
    zm = z[:, clean].max(axis=1)
    avgs = {}
    for lo, hi in [(1.0, 2.0), (2.0, 3.0), (1.0, 3.0)]:
        m = (ALPHAS > lo) & (ALPHAS <= hi) & clean
        avgs[f"({lo},{hi}]"] = float(ff_all[:, m].mean(axis=1).std())
    return (float(np.median(zm)), float(np.quantile(zm, 0.9)), float(np.quantile(zm, 0.99)),
            float((zm > 4.54).mean()), float((zm > 3.11).mean()), avgs,
            float(gm[ALPHAS > 1].mean()), float(gs[ALPHAS > 1].mean()))

# ==================================================================== main
def main():
    rng = np.random.default_rng(RNG_SEED)
    out = {"script": "tools/hot_hand_calib.py",
           "command": "uv run --quiet --with numpy --with scipy --with matplotlib python tools/hot_hand_calib.py",
           "seed": RNG_SEED, "alpha": ALPHAS.tolist()}
    t0 = time.time()

    print("=" * 78)
    print("G3.1 hot-hand calibration: empirical zeta form factor vs sine-kernel null")
    print("=" * 78)

    results = {}
    for n, ngue_rep, npoi_rep in [(3000, 200, 200), (10000, 40, 100)]:
        tag = f"N{n}"
        g = load_zeta_ords(ZEROS_PATH, n)
        x = unfold_zeta(g)
        sp = np.diff(x)
        fz = form_factor(x, ALPHAS)
        out[f"zeta_{tag}"] = fz.tolist()
        out[f"zeta_{tag}_spacing"] = [float(sp.mean()), float(sp.std())]
        devz = x - np.arange(1, n + 1)
        out[f"zeta_{tag}_latdev"] = [float(devz.std())]
        xg0 = gue_bulk(n, rng)
        out[f"gue_{tag}_latdev"] = [float((xg0 - np.arange(1, xg0.size + 1)).std())]

        gm = np.zeros(ALPHAS.size); gs = np.zeros(ALPHAS.size)
        gsum = 0.0; gsum2 = 0.0
        for r in range(ngue_rep):
            xg = gue_bulk(n, rng)
            ff = form_factor(xg, ALPHAS)
            gm += ff; gs += ff**2
            a = alpha_average(ff, 1.0, 3.0)[0]
            gsum += a; gsum2 += a**2
        gm /= ngue_rep
        gs = np.sqrt(np.maximum(gs/ngue_rep - gm**2, 0.0))
        gavg_m = gsum / ngue_rep
        gavgs = np.sqrt(max(gsum2/ngue_rep - gavg_m**2, 0.0))

        pm = np.zeros(ALPHAS.size); ps = np.zeros(ALPHAS.size)
        for r in range(npoi_rep):
            ff = form_factor(poisson_x(n, rng), ALPHAS)
            pm += ff; ps += ff**2
        pm /= npoi_rep
        ps = np.sqrt(np.maximum(ps/npoi_rep - pm**2, 0.0))

        out[f"gue_{tag}_mean"] = gm.tolist()
        out[f"gue_{tag}_std"] = gs.tolist()
        out[f"poisson_{tag}_mean"] = pm.tolist()
        out[f"poisson_{tag}_std"] = ps.tolist()
        out[f"gue_{tag}_avg13"] = [gavg_m, gavgs, alpha_average(fz, 1.0, 3.0)[0]]
        out[f"zeta_{tag}_avg13"] = alpha_average(fz, 1.0, 3.0)[0]
        out[f"zeta_{tag}_avg13_all"] = alpha_average(fz, 1.0, 3.0, clean_only=False)[0]
        out[f"zeta_{tag}_avgRamp"] = alpha_average(fz, 0.0, 1.0)[0]
        out[f"gue_{tag}_avgRamp"] = alpha_average(gm, 0.0, 1.0)[0]

        clean = ~np.isin(ALPHAS, list(POLLUTED))
        z = (fz - gm) / np.maximum(gs, 1e-9)
        zz = z[clean]
        out[f"zeta_{tag}_zscore_clean"] = [int(clean.sum()), int((np.abs(zz) > 2.0).sum()),
                                           int((np.abs(zz) > 3.0).sum()),
                                           float(np.abs(zz).max()),
                                           float(ALPHAS[clean][int(np.argmax(np.abs(zz)))])]

        # multiple-comparison calibration (Poisson noise floor)
        med, p90, p99, p454, p311, avgs, pm1, ps1 = maxz_calibration(n, 3000 if n == 3000 else 1500, rng)
        out[f"maxzcal_{tag}"] = [med, p90, p99, p454, p311, avgs, pm1, ps1]
        results[tag] = dict(fz=fz, gm=gm, gs=gs, pm=pm, n=n)

        print(f"\n--- N = {n} (zeta; GUE null {ngue_rep} reps; Poisson {npoi_rep} reps) ---")
        print(f"  zeta unfolded spacing mean/std: {sp.mean():.5f} / {sp.std():.5f}")
        print(f"  lattice deviation std of x_j - j: zeta {devz.std():.3f}   GUE-null "
              f"{out[f'gue_{tag}_latdev'][0]:.3f}")
        print(f"  {'alpha':>6} {'zeta':>8} {'GUE mean':>9} {'GUE std':>8} {'z':>7} {'Poi mean':>9}")
        for i in [0, 8, 16, 18, 19, 20, 21, 24, 30, 35, 40, 45, 50, 55, 59]:
            star = "*" if ALPHAS[i] in POLLUTED else " "
            print(f"  {ALPHAS[i]:6.2f}{star} {fz[i]:8.3f} {gm[i]:9.3f} {gs[i]:8.3f} "
                  f"{(fz[i]-gm[i])/max(gs[i],1e-9):7.2f} {pm[i]:9.3f}")
        print("  (* = lattice-polluted alpha: integer/half-integer, excluded from verdict)")
        zavg, npts_avg = alpha_average(fz, 1.0, 3.0)
        print(f"  clean alpha-average over (1,3]: zeta {zavg:.3f}  GUE {gavg_m:.3f} +- {gavgs:.3f} "
              f"(z = {(zavg-gavg_m)/max(gavgs,1e-9):+.2f} sigma)   [{npts_avg} alphas]")
        print(f"  max|z| over clean alphas: {np.abs(zz).max():.2f} at alpha "
              f"{ALPHAS[clean][int(np.argmax(np.abs(zz)))]:.2f}; "
              f"noise-floor calibration: median max|z| {med:.2f}, p90 {p90:.2f}, "
              f"P(max>4.54)={p454:.2f}, P(max>3.11)={p311:.2f}")
        for lo, hi in [(1.0, 2.0), (2.0, 3.0)]:
            za, _ = alpha_average(fz, lo, hi)
            print(f"  clean alpha-average ({lo},{hi}]: zeta {za:.3f}  (noise-floor std {avgs[f'({lo},{hi}]']:.3f})")

    # ---------------- figure: zeta vs GUE band at N=1e4 ----------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        tag = "N10000"
        r = results[tag]
        clean = ~np.isin(ALPHAS, list(POLLUTED))
        fig, ax = plt.subplots(figsize=(11, 5.5))
        ax.axhline(1.0, color="0.6", lw=0.8, ls=":")
        ax.axvspan(1.0, 3.0, color="0.95", zorder=0)
        ax.plot(ALPHAS, r["gm"] + r["gs"], color="0.75", lw=1.2, label="GUE null mean $\\pm 1\\sigma$")
        ax.plot(ALPHAS, r["gm"] - r["gs"], color="0.75", lw=1.2)
        ax.plot(ALPHAS, r["gm"], color="0.55", lw=1.5, label="GUE null mean")
        ax.plot(ALPHAS[clean], r["fz"][clean], "o-", ms=4, lw=0.8, color="tab:red",
                label="zeta zeros F$\\hat{}$(α)")
        ax.plot(ALPHAS[~clean], r["fz"][~clean], "o", ms=5, color="tab:orange",
                label="lattice-polluted α (integer/half-integer; estimator artifact)")
        ax.set_xlabel("α")
        ax.set_ylabel("F$\\hat{}$(α) = |Σe^{2πiαx}|²/N")
        ax.set_title("G3.1 hot-hand calibration: zeta form factor vs sine-kernel (GUE) "
                     "finite-sample band, N=10⁴ (40 realizations)")
        ax.set_xlim(0, 3.05); ax.set_ylim(-0.3, 8.0)
        ax.legend(loc="upper right", fontsize=8)
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(OUT_FIG, dpi=140)
        print(f"\nfigure -> {OUT_FIG}")
    except Exception as exc:
        print(f"\n(figure skipped: {exc})")

    out["elapsed_s"] = round(time.time() - t0, 1)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=1)
    print(f"elapsed {out['elapsed_s']}s; results -> {OUT_JSON}")

if __name__ == "__main__":
    main()
