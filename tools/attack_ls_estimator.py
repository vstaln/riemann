#!/usr/bin/env python3
"""attack_ls_estimator.py — B1 vector: Landy-Szalay bias-canceling form-factor estimator.

Question (idea-generator-crystallography.md B1): map the standard Landy-Szalay (1993)
two-point estimator xi_hat = (DD - 2DR + RR)/RR onto the zeta-zero form-factor problem and
compare it against the naive pair-correlation estimator used in verif-001 §4 /
tools/hot_hand_calib.py on the same 10k zeros. Is LS materially better at the certificate's
critical scales (alpha in [0.5, 1.5], especially the alpha ~ 1.0-1.3 arithmetic-feature zone)?
Does the survey mask (the finite window [T, 2T], here the unfolded interval [x_1, x_N])
enter DD/DR/RR identically and cancel?

Conventions (identical to hot_hand_calib.py wherever they overlap, so numbers are
directly comparable):
  unfold  zeta:  x_j = theta(gamma_j)/pi          (Riemann-Siegel theta; density 1)
          GUE:   x_j = N * F_semicircle(lambda_j) (Dumitriu-Edelman beta=2, bulk 80%)
  window  W = [x_1, x_N], length L, empirical density rho = n/L
  bins    tau in [0, tau_max=30), dtau = 0.1, bin centers tau_c = (j+0.5)*dtau
  P_W(tau) = 2*(L-tau)*dtau/L^2      (window pair-separation probability, interval)
  DD = 2*N_DD/(n(n-1));  DR = N_DR/(n*n_r);  RR = 2*N_RR/(n_r(n_r-1))
      (N_DD unordered data pairs, N_DR ordered data-random pairs, N_RR unordered random pairs)
  naive:  F_naive(a) = 1 + sum_tau ( DD/P_W - 1 ) e^{2 pi i a tau} dtau
  LS:     xi_LS(tau) = (DD - 2DR + RR)/RR ;  F_LS(a) = 1 + sum_tau xi_LS(tau) e^{2 pi i a tau} dtau
  Note: as n_r -> oo, RR -> P_W and DR -> P_W, so LS -> naive exactly; LS with a finite
  random catalog is naive + Monte-Carlo window/shot-noise cancellation + MC noise.

All numbers below are produced by this script. No fabricated data.
"""
import json, time
import numpy as np

RNG_SEED = 20260811
TAU_MAX = 30.0
DTAU = 0.1
ALPHAS = np.arange(0.05, 3.0001, 0.05)
ZEROS_PATH = "/home/vstaln/riemann/tools/data/zeros_computed_10000.txt"

# ---------------------------------------------------------------- data loading
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

# -------------------------------------------------------------------- GUE
def semicdf(x):
    """Semicircle CDF on [-2,2] with density sqrt(4-x^2)/(2pi)."""
    x = np.clip(x, -2.0, 2.0)
    return (np.arcsin(x/2.0) + (x/2.0)*np.sqrt(1.0 - (x/2.0)**2) + np.pi/2.0) / np.pi

def gue_bulk(N, frac, rng):
    """GUE via Dumitriu-Edelman tridiagonal (beta=2), eigenvalues / sqrt(2N) -> semicircle
    on [-2,2]; keep central 'frac'; unfold by semicircle CDF so mean spacing ~1."""
    from scipy.linalg import eigvalsh_tridiagonal
    d = rng.normal(0.0, np.sqrt(2.0), N)
    dfs = 2.0 * np.arange(N - 1, 0, -1)
    e = np.sqrt(rng.chisquare(dfs))
    ev = np.sort(eigvalsh_tridiagonal(d, e)) / np.sqrt(2.0 * N)
    lo = int(N * (1 - frac) / 2); hi = int(N * (1 + frac) / 2)
    ev = ev[lo:hi]
    return N * semicdf(ev)

# ---------------------------------------------------------------- pair counting
def count_pairs(a, b, tau_max=TAU_MAX, dtau=DTAU, self_pairs=False):
    """Bin the separations |a_i - b_j| in [0, tau_max).

    self_pairs=True  (b is a): count unordered pairs i<j with 0 < a_j - a_i < tau_max.
    self_pairs=False (a, b independent): count all ordered pairs with 0 < |a_i - b_j| < tau_max.
    Uses sorted arrays + searchsorted windows: only pairs with separation < tau_max are
    ever materialized, so cost is O((n+m) * tau_max * rho) instead of O(n*m).
    """
    nb = int(tau_max / dtau)
    counts = np.zeros(nb, dtype=np.int64)
    a = np.sort(np.asarray(a, dtype=float))
    b = np.sort(np.asarray(b, dtype=float))
    n = a.size
    CH = 400
    for i0 in range(0, n, CH):
        i1 = min(i0 + CH, n)
        a_chunk = a[i0:i1]
        if self_pairs:
            hi = np.searchsorted(b, a_chunk[-1] + tau_max, side='right')
            j0 = i0
            b_sub = b[j0:hi]
            d = b_sub[None, :] - a_chunk[:, None]
            jidx = j0 + np.arange(b_sub.size)
            iidx = i0 + np.arange(a_chunk.size)
            mask = (d > 0) & (d < tau_max) & (jidx[None, :] > iidx[:, None])
        else:
            lo = np.searchsorted(b, a_chunk[0] - tau_max, side='left')
            hi = np.searchsorted(b, a_chunk[-1] + tau_max, side='right')
            b_sub = b[lo:hi]
            d = np.abs(b_sub[None, :] - a_chunk[:, None])
            mask = (d > 0) & (d < tau_max)
        d = d[mask]
        if d.size:
            idx = (d / dtau).astype(np.int64)
            np.clip(idx, 0, nb - 1, out=idx)
            np.add.at(counts, idx, 1)
    return counts

# ------------------------------------------------------------------ estimators
def _fft_form(alphas, xi, dtau=DTAU):
    """F(a) = 1 + sum_tau xi(tau) e^{2 pi i a tau} dtau (real part)."""
    nb = xi.size
    tau_c = (np.arange(nb) + 0.5) * dtau
    e = np.exp(2j * np.pi * np.outer(alphas, tau_c))
    return 1.0 + np.real(e @ (xi * dtau))

def estimator_naive(x, alphas, tau_max=TAU_MAX, dtau=DTAU, return_xi=False):
    """hot_hand_calib.py convention: R(tau) = unordered count / ((L-tau)*(n/L)^2*dtau),
    F(a) = 1 + sum (R-1) e^{2pi i a tau} dtau.  (== DD/P_W - 1 with DD, P_W as defined.)"""
    x = np.sort(np.asarray(x, dtype=float))
    n = x.size
    L = x[-1] - x[0]
    N_DD = count_pairs(x, x, tau_max, dtau, self_pairs=True)
    tau_c = (np.arange(N_DD.size) + 0.5) * dtau
    expc = np.maximum(L - tau_c, 1e-9) * (n / L) ** 2 * dtau
    R = N_DD / expc
    F = _fft_form(alphas, R - 1.0, dtau)
    if return_xi:
        return F, R - 1.0
    return F

def estimator_ls(x, y, alphas, tau_max=TAU_MAX, dtau=DTAU, return_xi=False):
    """Landy-Szalay on one random catalog y (n_r points, uniform on the window).
    xi_LS(tau) = (DD - 2DR + RR)/RR with the normalized counts; F_LS = 1 + sum xi e^{...}."""
    x = np.sort(np.asarray(x, dtype=float))
    y = np.sort(np.asarray(y, dtype=float))
    n = x.size
    nr = y.size
    N_DD = count_pairs(x, x, tau_max, dtau, self_pairs=True)
    N_DR = count_pairs(x, y, tau_max, dtau, self_pairs=False)
    N_RR = count_pairs(y, y, tau_max, dtau, self_pairs=True)
    DD = 2.0 * N_DD / (n * (n - 1))
    DR = N_DR / (n * nr)
    RR = 2.0 * N_RR / (nr * (nr - 1))
    xi = (DD - 2.0 * DR + RR) / RR
    F = _fft_form(alphas, xi, dtau)
    if return_xi:
        return F, xi, DD, DR, RR
    return F

def ls_mean_std(x, alphas, n_r, reps, rng, tau_max=TAU_MAX, dtau=DTAU):
    """LS averaged over `reps` random-catalog realizations on the fixed data x.
    Returns (mean F_LS over realizations, std over realizations)."""
    L = x[-1] - x[0]
    Fs = np.zeros((reps, alphas.size))
    RR_norm_av = np.zeros(int(tau_max / dtau))
    DR_norm_av = np.zeros(int(tau_max / dtau))
    for r in range(reps):
        y = np.sort(rng.uniform(x[0], x[-1], n_r))
        F, xi, DD, DR, RR = estimator_ls(x, y, alphas, tau_max, dtau, return_xi=True)
        Fs[r] = F
        nb = int(tau_max / dtau)
        tau_c = (np.arange(nb) + 0.5) * dtau
        P_W = 2.0 * np.maximum(L - tau_c, 1e-9) * dtau / L ** 2
        RR_norm_av += RR / P_W
        DR_norm_av += DR / P_W
    return Fs.mean(axis=0), Fs.std(axis=0), RR_norm_av / reps, DR_norm_av / reps

# =================================================================== main
def main():
    t0 = time.time()
    rng = np.random.default_rng(RNG_SEED)
    out = {"alpha": ALPHAS.tolist(), "script": "tools/attack_ls_estimator.py",
           "command": "uv run --quiet --with numpy --with scipy python tools/attack_ls_estimator.py",
           "seed": RNG_SEED, "tau_max": TAU_MAX, "dtau": DTAU}

    g = load_zeta_ords(ZEROS_PATH, 10000)
    x = unfold_zeta(g)
    x = np.sort(x)
    L = x[-1] - x[0]
    n = x.size
    print(f"zeta window: [{x[0]:.4f}, {x[-1]:.4f}], L={L:.1f}, n={n}, rho={n/L:.6f}")

    # ---- A) zeta, N=10000: naive vs LS (n_r = N, reps=40) vs LS (n_r = 8N, reps=20)
    F_naive = estimator_naive(x, ALPHAS)
    out["zeta_naive"] = F_naive.tolist()
    F_ls, F_ls_std, RRn, DRn = ls_mean_std(x, ALPHAS, n, 40, rng)
    out["zeta_ls_mean"] = F_ls.tolist(); out["zeta_ls_std"] = F_ls_std.tolist()
    F_ls8, F_ls8_std, RRn8, DRn8 = ls_mean_std(x, ALPHAS, 8 * n, 20, rng)
    out["zeta_ls8_mean"] = F_ls8.tolist(); out["zeta_ls8_std"] = F_ls8_std.tolist()
    # mask check numbers (n_r = N run)
    nb = int(TAU_MAX / DTAU)
    tau_c = (np.arange(nb) + 0.5) * DTAU
    P_W = 2.0 * np.maximum(L - tau_c, 1e-9) * DTAU / L ** 2
    mask_taus = [0.55, 1.55, 5.55, 10.55, 20.55, 29.55]
    out["mask_check"] = {
        "taus": mask_taus,
        "RR_norm_nrN": [float(RRn[np.argmin(np.abs(tau_c - t))]) for t in mask_taus],
        "DR_norm_nrN": [float(DRn[np.argmin(np.abs(tau_c - t))]) for t in mask_taus],
        "RR_norm_nr8N": [float(RRn8[np.argmin(np.abs(tau_c - t))]) for t in mask_taus],
        "DR_norm_nr8N": [float(DRn8[np.argmin(np.abs(tau_c - t))]) for t in mask_taus],
        "RR_norm_mean_dev_max": float(np.max(np.abs(RRn - 1.0))),
        "DR_norm_mean_dev_max": float(np.max(np.abs(DRn - 1.0))),
        "RR_norm_rel_std_max": float(np.max(np.abs(RRn - 1.0))),
    }

    # ---- B) GUE null, N=10000: naive and LS (n_r = N, reps=8 per sample)
    GREPS = 24
    gue = []
    for r in range(GREPS):
        xs = np.sort(gue_bulk(12500, 0.8, rng))[:10000]
        Fn = estimator_naive(xs, ALPHAS)
        Fl, Fs, _, _ = ls_mean_std(xs, ALPHAS, 10000, 8, rng)
        gue.append((Fn, Fl))
    gue = np.array(gue)
    out["gue_naive_mean"] = gue[:, 0].mean(axis=0).tolist()
    out["gue_naive_std"] = gue[:, 0].std(axis=0).tolist()
    out["gue_ls_mean"] = gue[:, 1].mean(axis=0).tolist()
    out["gue_ls_std"] = gue[:, 1].std(axis=0).tolist()

    # ---- C) block variance (windows of ~1000 zeros): LS per block, reps=8
    sub = np.array([0.5, 0.9, 1.1, 1.5, 2.0])
    zb = []
    for i in range(10):
        blk = x[i * 1000:(i + 1) * 1000]
        Fn = estimator_naive(blk, sub)
        Fl, Fs, _, _ = ls_mean_std(blk, sub, 1000, 8, rng)
        zb.append((Fn, Fl))
    zb = np.array(zb)
    out["block_alpha"] = sub.tolist()
    out["block_zeta_naive_mean"] = zb[:, 0].mean(axis=0).tolist()
    out["block_zeta_naive_std"] = zb[:, 0].std(axis=0).tolist()
    out["block_zeta_ls_mean"] = zb[:, 1].mean(axis=0).tolist()
    out["block_zeta_ls_std"] = zb[:, 1].std(axis=0).tolist()

    # sanity: mean unfolded spacing
    out["zeta_spacing_mean"] = float(np.diff(x).mean())

    out["elapsed_s"] = round(time.time() - t0, 1)

    # ------------------------------------------------------------------ print
    def idx(a):
        return min(range(ALPHAS.size), key=lambda i: abs(ALPHAS[i] - a))

    print("\n=== A) zeta N=10000: naive vs LS (n_r=N, 40 rand-cat reps) vs LS (n_r=8N, 20 reps) ===")
    print("  alpha   naive     LS(N) mean+-std     LS(8N) mean+-std")
    for a in [0.5, 0.75, 0.9, 0.95, 1.0, 1.05, 1.1, 1.3, 1.5, 2.0, 2.5, 3.0]:
        i = idx(a)
        print(f"  {a:5.2f}  {F_naive[i]:7.3f}   {F_ls[i]:6.3f}+-{F_ls_std[i]:5.3f}     {F_ls8[i]:6.3f}+-{F_ls8_std[i]:5.3f}")

    print("\n=== B) GUE null N=10000 (8 reps): naive vs LS ===")
    print("  alpha   GUE-naive mean+-std   GUE-LS mean+-std")
    for a in [0.5, 0.9, 1.0, 1.05, 1.1, 1.3, 1.5, 2.0]:
        i = idx(a)
        print(f"  {a:5.2f}   {gue[:,0][:,i].mean():6.3f}+-{gue[:,0][:,i].std():5.3f}     {gue[:,1][:,i].mean():6.3f}+-{gue[:,1][:,i].std():5.3f}")

    print("\n=== significance of the alpha=1.10 arithmetic feature (zeta vs GUE null, 24 reps) ===")
    for a in [1.05, 1.10]:
        i = idx(a)
        z_naive = (F_naive[i] - 1.0) / gue[:, 0][:, i].std()
        z_ls_tot = (F_ls[i] - 1.0) / gue[:, 1][:, i].std()
        print(f"  alpha={a:4.2f}: zeta naive {F_naive[i]:.3f} -> (F-1)/sigma_null = {z_naive:5.1f} sigma")
        print(f"             zeta LS     {F_ls[i]:.3f} -> (F-1)/sigma_nullLS = {z_ls_tot:5.1f} sigma")

    print("\n=== variance decomposition at N=10000 (intrinsic proxy = GUE-naive std; MC = std over catalog realizations) ===")
    print("  alpha  intrinsic  LS(N) MC   LS(N) tot  LS(8N) MC  LS(8N) tot   naive tot")
    for a in [0.5, 1.0, 1.1, 1.3, 1.5, 2.0]:
        i = idx(a)
        intr = gue[:, 0][:, i].std()
        mc_n = F_ls_std[i]; mc_8 = F_ls8_std[i]
        tot_n = np.sqrt(intr ** 2 + mc_n ** 2); tot_8 = np.sqrt(intr ** 2 + mc_8 ** 2)
        print(f"  {a:5.2f}  {intr:8.3f}   {mc_n:8.3f}   {tot_n:8.3f}    {mc_8:8.3f}   {tot_8:8.3f}    {intr:8.3f}")
        out[f"var_{a}"] = {"intrinsic": float(intr), "mc_nrN": float(mc_n), "tot_nrN": float(tot_n),
                           "mc_nr8N": float(mc_8), "tot_nr8N": float(tot_8)}

    print("\n=== C) block variance (10 x 1000 zeros): naive vs LS, mean+-std over blocks ===")
    print("  alpha   naive mean+-std       LS mean+-std")
    for j, a in enumerate(sub):
        print(f"  {a:4.1f}   {zb[:,0][:,j].mean():6.3f}+-{zb[:,0][:,j].std():5.3f}    {zb[:,1][:,j].mean():6.3f}+-{zb[:,1][:,j].std():5.3f}")

    print("\n=== mask check (window enters DD/DR/RR identically?) ===")
    print("  RR_norm = RR/P_W, DR_norm = DR/P_W averaged over random-catalog reps (1.0 = window cancels exactly)")
    print("  tau      RRn(n_r=N)  DRn(n_r=N)  RRn(n_r=8N) DRn(n_r=8N)")
    for k, t in enumerate(mask_taus):
        print(f"  {t:5.2f}   {out['mask_check']['RR_norm_nrN'][k]:8.4f}  {out['mask_check']['DR_norm_nrN'][k]:8.4f}  {out['mask_check']['RR_norm_nr8N'][k]:8.4f}  {out['mask_check']['DR_norm_nr8N'][k]:8.4f}")
    print(f"  max |RR_norm-1| over tau (n_r=N): {out['mask_check']['RR_norm_mean_dev_max']:.4f}")
    print(f"  max |DR_norm-1| over tau (n_r=N): {out['mask_check']['DR_norm_mean_dev_max']:.4f}")

    print(f"\n  elapsed {out['elapsed_s']}s")
    with open("/tmp/riemann_ls/ls_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("results -> /tmp/riemann_ls/ls_results.json")

if __name__ == "__main__":
    main()
