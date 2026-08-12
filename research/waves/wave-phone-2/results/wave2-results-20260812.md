# Wave results — 2026-08-12 (c=3 port, T1, 10M pipeline, novel hunt)

## c=3 rank-trace port (agent e41a27ff) — NEW BOUND
N_d >= (3 - C)/2 * N = (1 + H_cos(alpha))/2 * N, C = 1/c(alpha), c = I0^2/(I2+J), J = sin(a)/a^3 - cos(a)/a^2.
At the certified config (alpha=1.49, m=133, psum=1/220): H = 0.6724218860, c = 0.7532513, C = 1.3275781
=> N_d >= 0.83621 * N — BEATS 5/6 = 0.8333 by +0.00288, dominates our 0.8071 (cubic, lambda=2/3).
Corrected via the certified simple bound: 0.83663 (transfer CONJECTURED). Peak at alpha=sqrt(2): 0.83625.
Finite height: needs cosine-window pair-correlation error E(T) < 0.00288 + eps-floor as certified constant.
Labels: PROVEN (arithmetic, rank-trace step, lambda=1 legs 5/6/3/4); CHECKED NUMERICALLY (c, J, peak, tightness); CONJECTURED (mollifier transfer, finite-height errors).

## T1 formalization prep (agent 74578ad7) — LEAN-STYLE STATEMENT READY
The theorem: with hCert (the marked 7-point BandFunc floor >= 8065/1e6 over all x, configuration-universal),
hEF, hRvM, hMV (mean-value), hGamma: for all eps > 0 exists T0: for all T >= T0, (BOUND - eps)*Ncount(T,2T) <= N0simple(T,2T),
BOUND = (H(149/100) - (1/220)(127/133)) / (1 - Phi(8065/1e6*127, 133)/133) = 0.6732660791400007, and BOUND > 3/2 - (1/sqrt2)*cot(1/sqrt2).
Exact closed forms: I0, I2, J, cH, H, Phi — all Lean-checkable rational/radical arithmetic.
GAP: hCert is Arb-interval-verified (python-flint), NOT Lean-checked — would need their NumericCert-style integer checker port.

## 10M pipeline prep (agent 9ba26c05) — FORMULA CATALOG + NEW MEASUREMENTS
New measurements at 924k: T block-autocorrelation rho1 = -0.136+-0.017, rho5 = +0.163+-0.017 (8-10 sigma NON-independence of T-blocks);
small-gap tail exponent 3.81+-0.18 over [0.05,0.15] vs sine-kernel 3; N=64 has NO floor (T_min=0.1893, 1475 blocks < 0.34) — the +1/3 floor is an N>=256 phenomenon;
m3-deficit exponent (5-m3) ~ N^0.330; frac(<0.1) = 4.07e-4 (n=376). pair = 3.29756+-0.00050 (N=64), 3.38993+-0.00033 (N=256).
Pipeline: stats_10m/{load_unfold,block_stats}.py — streaming per-block, 10M f64 = 80 MB fine.

## Novel hunt (agent 7c0e8d55) — THE MISSED DOF
C1 [WINNER]: the 21 pair-weight DOF w_{i,i+r} (span-capacity Sigma_i w <= 2/span) were NEVER swept — P-ascent/alpha
exhausted only the default 2/(7-s) profile. Probe: enumerate rational profiles, coarse-grid score at the record triple,
Arb-verify survivors. Threshold: certified eps >= 8066 at (1.49, 1/1320, 133) => bound >= 0.673268 > record.
Upside capped at the PROVEN in-class 0.6818. Kill-risk: capacity-saturating profiles may be degenerate at the extremal cell.
C2: realized-floor finite-height certificate — F on 7-point consecutive blocks of the 924k zeros (~132k blocks);
threshold: realized min ~ 8500/1e6 stable => finite-T certificate jumps toward in-class.
C3: prime-side second trace identity (Groskin dictionary) — TESTED-OPEN.

## n9 final probe: INCONCLUSIVE (crashed after init; sibling n9/n9b/n9c also buggy; lane marginal anyway per C2 constants)
