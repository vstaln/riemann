# SPEC — faster Riemann-zeta zero-finder (pure-std Rust) — from agent 89a40d53

Status: SPEC DELIVERED, implementation PENDING (agent died on output cap twice). Baseline: 100,000 zeros in 42 s wall (~2380 zeros/s, t_last=75446.99, N(T) diff -785.72) with the v3 hybrid (EM zeta N=40 + Bernoulli t<200, RS-g0 t>=200, theta asymptotic, scan step 0.2 + bisection x80) on laptop (Void, Ryzen 5 3500U, 8 threads, rustc 1.97.1).

## Ranked options (expected speedup vs cost)
1. **Batch/row-update Riemann-Siegel (RECOMMENDED).** Factor Z(t) = 2*sum cos(theta - t ln n)/sqrt(n) + corr into cos(theta)*A(t) + sin(theta)*B(t) with A = sum c_n/sqrt(n), B = sum s_n/sqrt(n), update (c_n,s_n) = (cos,sin)(t ln n) per grid step via rotation by (cos,sin)(h ln n): 4 mul + 2 add per (n, step), independent per n -> auto-vectorizable. Kills the ~100-cycle/term log+cos of the baseline; scan becomes ~O(1)-per-eval. **Expected 30-100x on eval cost; low-medium implementation cost.**
2. **std::thread sharding (8 cores).** Trivial cost, ~8x.
3. **Fewer refinement evals:** baseline wastes 80 bisections/zero (~92% of runtime). Grid IQI + 1 Newton (analytic Z') -> ~3 evals/zero. Medium cost, ~20-40x on refinement.
4. **Gabcke c0-c4 corrections** — removes O(t^{-3/4}) RS residual -> uniform method t>=40, better accuracy. Defer to v2.
5. **Gram-point/Taylor method** — O(1)/point after Gram setup; comparable to (1)+(3), more moving parts. Skip.
6. **EM/RS crossover tuning** — negligible (t<200 holds only ~79/100k zeros). Skip.
7. **Odlyzko-Schonhage FFT** — 10^6/s class but heavy convolution in pure std; stretch, not now.

## Recommended v1
(1)+(2)+(3): batch RS-g0 scan (same formula as baseline -> identical accuracy), h=0.02 (fixes baseline's -0.78% miss rate; measured: step 0.05 gives diff +0.18 vs -55.8 at 0.2), blocks of 4096 steps, 8 threads over [14, T_hi), per-zero refinement = IQI on 3 grid points + 1 Newton step (analytic Z', bisection fallback), N(T) completeness check.

## v1.1 (if scan dominates)
Drop g0 correction from scan (shifted-root argument, safety-net rescan), recurse the theta-rotation too.

## Miss-rate mechanism (documented)
step 0.2 -> -785.7 = 0.78% miss; step 0.1 -> -89.2; twin pairs with gap < scan step (min realized gap 0.0419); step 0.05 recovers completeness (diff +0.18).

## Validation (LMFDB canonical, 2026-08-12)
Rust v3 zeros vs LMFDB first 11,000 (zeros_lmfdb_11k.txt): max |dt| = 6.332813e-4 at zero 364 (t~630.8, EM/RS crossover), mean 1.805e-5, 100% < 1e-3, 6.35% < 1e-6, indexes aligned. Bar met.
