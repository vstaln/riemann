#!/usr/bin/env python3
"""
tower_probe.py — derivative-tower numerical probe for the completed zeta function xi(s).
EXECUTOR deliverable script (wave-orch-phone).

Questions:
  Q1. Interlacing: one xi'-zero per zeta-zero gap? one xi''-zero per xi'-gap?
      (Check first ~500 zeta zeros.)
  Q2. Spacing statistics of xi' zeros vs zeta zeros: mean gap, min gap,
      nearest-neighbor ratio distributions (GUE vs Poisson sanity), gap histogram.
  Q3. Signed-kernel candidates: is the xi' zero sequence 'closer to' the Montgomery
      pair-correlation kernel than zeta's own zeros? Compute empirical 1-level density
      at scaled spacing for both, compare to 1 - (sin(pi x)/(pi x))^2.
  Q4. Local extrema of |xi| on the line: stationary points of Z(t) (Hardy Z) interlace
      with zeta zeros; spacing stats of stationary points vs zeros.
  Q5. Kernel-zero check on [0,4] for k(x)=cos(sqrt(2)x)-style kernels: minimum of
      k(u)^2+k(v)^2+k(u+v)^2 over u,v>=0, u+v<=4 (the Gram-stability pressure floor).

All numbers printed with the script that produced them. Honesty labels in output.
Compute: mpmath (proot ubuntu), ~500 zeros, ~few minutes.
"""
import mpmath as mp
import numpy as np
import json, sys, time

mp.mp.dps = 30

def xi_logder(s):
    """(xi'/xi)(s) = 1/s + 1/(s-1) - (1/2)log(pi) + (1/2)psi(s/2) + (zeta'/zeta)(s)"""
    return 1/s + 1/(s-1) - 0.5*mp.log(mp.pi) + 0.5*mp.digamma(s/2) + mp.zeta(1, s, derivative=1)/mp.zeta(s)

def theta(t):
    """Riemann–Siegel theta: Im log Gamma(1/4 + i t/2) - (t/2) log(pi)."""
    return mp.im(mp.log(mp.gamma(mp.mpc(0.25, 0.5*t)))) - 0.5*t*mp.log(mp.pi)

def Zt(t):
    """Hardy Z: e^{i theta} zeta(1/2+it), real for real t."""
    s = mp.mpc(0.5, t)
    return mp.re(mp.exp(mp.mpc(0, theta(t))) * mp.zeta(s))

def PpP(t):
    """P'/P where P = pi^{-1/4}|Gamma(1/4+it/2)| (positive factor): 2t/(t^2+1/4) - (1/2) Im psi(1/4+it/2)."""
    return 2*t/(t*t + 0.25) - 0.5*mp.im(mp.digamma(mp.mpc(0.25, 0.5*t)))

def H1(t):
    """H1(t) = Re[i*xi'(1/2+it)].  Using the Z-form (no zeta division, robust at zeta zeros):
    xi'(1/2+it) = i * (Z(t)*P'(t)/P(t) + Z'(t)) * P(t)  up to a positive factor;
    zeros of Re[i*xi'] coincide with zeros of (Z*PpP + Z').  sign: H = -(Z*PpP + Z') per attack-xiprime."""
    h = mp.mpf('1e-6')
    Zp = (Zt(t+h) - Zt(t-h)) / (2*h)
    return -(Zt(t)*PpP(t) + Zp)

def find_roots(f, t_lo, t_hi, step=0.05, tol=1e-14):
    """Scan [t_lo,t_hi] for sign changes of f; refine with bisection."""
    roots = []
    t = t_lo
    f_prev = f(t_lo)
    while t < t_hi:
        t_next = min(t + step, t_hi)
        f_next = f(t_next)
        if f_prev == 0:
            roots.append(t); f_prev = f_next; t = t_next; continue
        if f_next == 0:
            roots.append(t_next); f_prev = f_next; t = t_next; continue
        if f_prev * f_next < 0:
            a, b = t, t_next
            fa, fb = f_prev, f_next
            for _ in range(80):
                m = (a+b)/2
                fm = f(m)
                if fm == 0 or abs(b-a) < tol:
                    break
                if fa*fm < 0:
                    b, fb = m, fm
                else:
                    a, fa = m, fm
            roots.append((a+b)/2)
        f_prev = f_next
        t = t_next
    return roots

def main():
    out = {}
    N = 500
    # --- zeta zeros from data file (mpmath zetazero is slow at high index; file has 1000)
    zeros = []
    with open('/root/riemann/tools/data/zeros_1_1000.txt') as f:
        for line in f:
            parts = line.split()
            zeros.append(float(parts[1]))
            if len(zeros) >= N:
                break
    gammas = zeros[:N]
    out['n_zeros'] = len(gammas)
    out['gamma_first_last'] = [gammas[0], gammas[-1]]

    # --- Q1a: xi' zeros per zeta gap, first 200 gaps (compute budget)
    t0 = time.time()
    gaps_probe = 200
    xi1_per_gap = []
    for n in range(gaps_probe):
        lo = gammas[n]; hi = gammas[n+1]
        roots = find_roots(H1, lo, hi)
        xi1_per_gap.append(len(roots))
    out['Q1a_gaps_probed'] = gaps_probe
    out['Q1a_hist_xi1_per_gap'] = {str(k): xi1_per_gap.count(k) for k in sorted(set(xi1_per_gap))}
    print('Q1a xi1-per-gap hist:', out['Q1a_hist_xi1_per_gap'], f'({time.time()-t0:.1f}s)', flush=True)

    # --- Q1b: xi'' per xi' gap (first 60 xi' gaps)
    xi1_all = []
    for n in range(gaps_probe):
        lo = gammas[n]; hi = gammas[n+1]
        xi1_all += find_roots(H1, lo, hi)
    xi1_all = sorted(xi1_all)
    # xi'' via numerical derivative of H1 (finite diff on the real function H1)
    def H2(t, h=1e-5):
        return (H1(t+h) - H1(t-h)) / (2*h)
    xi2_per_gap = []
    for n in range(min(60, len(xi1_all)-1)):
        lo = xi1_all[n]; hi = xi1_all[n+1]
        roots = find_roots(H2, lo, hi, step=0.03, tol=1e-10)
        xi2_per_gap.append(len(roots))
    out['Q1b_xi1_gaps'] = len(xi1_all)
    out['Q1b_hist_xi2_per_xi1_gap'] = {str(k): xi2_per_gap.count(k) for k in sorted(set(xi2_per_gap))}
    print('Q1b xi2-per-xi1-gap hist:', out['Q1b_hist_xi2_per_xi1_gap'], flush=True)

    # --- Q2: spacing stats of xi' zeros vs zeta zeros
    xi1_gaps = np.diff(xi1_all)
    zeta_gaps = np.diff(gammas)
    out['Q2_mean_gap_xi1'] = float(xi1_gaps.mean())
    out['Q2_mean_gap_zeta'] = float(zeta_gaps.mean())
    out['Q2_min_gap_xi1'] = float(xi1_gaps.min())
    out['Q2_min_gap_zeta'] = float(zeta_gaps.min())
    # normalized spacings (mean 1): nearest-neighbor ratio R = g_n / g_{n-1} (GUE: mean ~1.0, pdf peaked; Poisson: exponential)
    r_xi = xi1_gaps[1:] / xi1_gaps[:-1]
    r_ze = zeta_gaps[1:] / zeta_gaps[:-1]
    out['Q2_mean_ratio_xi1'] = float(r_xi.mean())
    out['Q2_mean_ratio_zeta'] = float(r_ze.mean())
    out['Q2_std_ratio_xi1'] = float(r_xi.std())
    out['Q2_std_ratio_zeta'] = float(r_ze.std())
    # normalized gap distribution histograms (mean-normalized)
    nz_xi = xi1_gaps / xi1_gaps.mean()
    nz_ze = zeta_gaps / zeta_gaps.mean()
    hist_xi, edges = np.histogram(nz_xi, bins=8, range=(0, 2.5), density=True)
    hist_ze, _ = np.histogram(nz_ze, bins=8, range=(0, 2.5), density=True)
    out['Q2_hist_normgap_xi1'] = [float(x) for x in hist_xi]
    out['Q2_hist_normgap_zeta'] = [float(x) for x in hist_ze]
    print('Q2 spacing stats:', {k: out[k] for k in ['Q2_mean_gap_xi1','Q2_mean_gap_zeta','Q2_min_gap_xi1','Q2_min_gap_zeta','Q2_mean_ratio_xi1','Q2_mean_ratio_zeta']}, flush=True)

    # --- Q3: empirical 1-level density (pair correlation function) at scaled spacing
    # 1-level density: for a normalized sequence with mean spacing 1, g(x) ~ 1 - (sin(pi x)/(pi x))^2 under GUE.
    def pair_corr(seq, x, bandwidth=0.06):
        seq = np.asarray(seq)
        cnt = 0.0
        total = 0
        for i in range(len(seq)):
            d = seq - seq[i]
            sel = (np.abs(d - x) < bandwidth) & (np.abs(d) > 1e-6)
            cnt += sel.sum()
            total += 1
        norm = 2 * bandwidth * total
        return cnt / norm if norm > 0 else float('nan')
    xs = np.linspace(0.25, 2.0, 8)
    out['Q3_gue_pred'] = [float(1 - (np.sin(np.pi*x)/(np.pi*x))**2) for x in xs]
    pc_xi1 = [float(pair_corr(xi1_all, x)) for x in xs]
    pc_zeta = [float(pair_corr(gammas, x)) for x in xs]
    out['Q3_paircorr_xi1'] = pc_xi1
    out['Q3_paircorr_zeta'] = pc_zeta
    print('Q3 pair corr at xs', xs.tolist(), flush=True)
    print('  GUE  :', out['Q3_gue_pred'], flush=True)
    print('  xi1  :', pc_xi1, flush=True)
    print('  zeta :', pc_zeta, flush=True)

    # --- Q4: stationary points of Hardy Z (extrema of |xi|): spacing vs zeros
    # Z(t) = Re(e^{i theta} zeta(1/2+it)); extrema of |xi| are extrema of |Z|.
    def theta(t):
        return -0.5*t*mp.log(mp.pi) + mp.im(mp.log(mp.gamma(mp.mpc(0.25, 0.5*t))))
    def Zt(t):
        s = mp.mpc(0.5, t)
        return mp.re(mp.exp(mp.mpc(0, theta(t))) * mp.zeta(s))
    def Zp(t, h=1e-4):
        return (Zt(t+h) - Zt(t-h)) / (2*h)
    st = []
    t = float(gammas[0]) + 0.01
    f_prev = Zp(t)
    while t < float(gammas[gaps_probe-1]):
        t_next = t + 0.08
        f_next = Zp(t_next)
        if f_prev * f_next < 0:
            a, b = t, t_next
            fa, fb = f_prev, f_next
            for _ in range(60):
                m = (a+b)/2
                fm = Zp(m)
                if fm == 0 or abs(b-a) < 1e-10:
                    break
                if fa*fm < 0:
                    b, fb = m, fm
                else:
                    a, fa = m, fm
            st.append((a+b)/2)
        f_prev = f_next
        t = t_next
    st = np.array(st)
    out['Q4_n_stationary'] = int(len(st))
    st_gaps = np.diff(st)
    out['Q4_mean_gap_stationary'] = float(st_gaps.mean())
    out['Q4_mean_gap_zeta'] = float(np.diff(gammas[:gaps_probe]).mean())
    out['Q4_ratio_stationary_to_zeta_gap'] = float(st_gaps.mean() / np.diff(gammas[:gaps_probe]).mean())
    print('Q4 stationary points:', out['Q4_n_stationary'], 'mean gap', out['Q4_mean_gap_stationary'], flush=True)

    # --- Q5: kernel-zero / pressure floor check for the stability kernel
    # k(x) = [sinc((sqrt2-2pi x)/2) + sinc((sqrt2+2pi x)/2)] / (2 k(0)), k(0) = sqrt2 * sin(1/sqrt2)
    k0 = np.sqrt(2) * np.sin(1/np.sqrt(2))
    def K(x):
        x = np.asarray(x, dtype=float)
        return (np.sinc((np.sqrt(2) - 2*np.pi*x)/(2*np.pi)) + np.sinc((np.sqrt(2) + 2*np.pi*x)/(2*np.pi)))/2 / k0
    # dense grid over u,v>=0, u+v<=4
    Ns = 200
    u = np.linspace(0, 4, Ns)
    U, V = np.meshgrid(u, u)
    M = U + V <= 4
    ku, kv, kuv = K(U[M]), K(V[M]), K(U[M]+V[M])
    # candidates: (a) sum of squares; (b) max abs; (c) sum of abs
    ss = ku**2 + kv**2 + kuv**2
    idx = np.argmin(ss)
    Uf, Vf = U[M], V[M]
    out['Q5_grid_n'] = int(M.sum())
    out['Q5_min_ss_grid'] = float(ss.min())
    out['Q5_argmin_ss'] = [float(Uf[idx]), float(Vf[idx])]
    out['Q5_min_maxabs_grid'] = float(np.max(np.abs([ku, kv, kuv]), axis=0).min())
    out['Q5_min_sumabs_grid'] = float((np.abs(ku)+np.abs(kv)+np.abs(kuv)).min())
    # zeros of k on [0,4]
    zs = []
    prev = K(0.0)
    for x in np.linspace(1e-6, 4.0, 200001):
        cur = K(x)
        if prev*cur < 0:
            zs.append(float(x))
        prev = cur
    out['Q5_n_kernel_zeros_04'] = len(zs)
    out['Q5_kernel_zeros_04'] = [round(z, 5) for z in zs[:20]]
    print('Q5 grid min ss:', out['Q5_min_ss_grid'], 'at', out['Q5_argmin_ss'], 'n_kzeros', out['Q5_n_kernel_zeros_04'], flush=True)

    out['runtime_s'] = time.time() - t0
    out['labels'] = {
        'Q1a': 'CHECKED NUMERICALLY (mpmath, 30 dps, scan step 0.05, bisection 80 iter)',
        'Q1b': 'CHECKED NUMERICALLY (central-difference H2, h=1e-5; step 0.03)',
        'Q2': 'CHECKED NUMERICALLY (numpy stats)',
        'Q3': 'CHECKED NUMERICALLY (box kernel bandwidth 0.06; empirical, not asymptotic)',
        'Q4': 'CHECKED NUMERICALLY (central-diff Zp, h=1e-4; step 0.08)',
        'Q5': 'CHECKED NUMERICALLY (grid 200x200 over u+v<=4; kernel zero scan step 2e-5)',
    }
    with open('/root/riemann/research/waves/wave-orch-phone/results/executor-probe.json', 'w') as f:
        json.dump(out, f, indent=1)
    print('DONE. json written. total', out['runtime_s'], 's', flush=True)

if __name__ == '__main__':
    main()
