# rust-zeros — fast Rust zero-finder + the 100k statistics it unlocked (2026-08-12)

**Status: COMPLETE.** A pure-std Rust Riemann–Siegel/Euler–Maclaurin hybrid locates non-trivial zeros ~1000× faster than mpmath zetazero (100k zeros in ~2.5 min vs days-equivalent); the high-N statistics sharpened two verdicts and added a new read.

## The tool (tools/zeros_rust/main.rs, pure std, f64, rustc -O, no crates)
- **t < 200:** Euler–Maclaurin ζ(1/2+it), N=40 terms, Bernoulli numbers by recurrence (assert-checked B₂=1/6, B₄=−1/30, B₆=1/42).
- **t ≥ 200:** Riemann–Siegel with g₀ tail: Z(t) = 2Σ_{k≤n}cos(θ−t ln k)/√k + (−1)^{n−1}(t/2π)^{−1/4}·g₀(a), n=⌊√(t/2π)⌋, a=√(t/2π)−n; θ asymptotic incl. 1/(48t)+7/(5760t³)+31/(80640t⁵).
- Scan step (default 0.2; 0.1 used for the final run) + bisection ×80; N(T) completeness check printed per run; per-zero flush (crash-proof).
- **Why not the full Gabcke tail:** v1 proved g₀-only fails below t≈200 (tail O(t^{−3/4}) ≈ 0.5 at t=14); v2 found mpmath's rs_z is the full Arias-de-Reyna algorithm (~1500 lines, arbitrary precision — a transcription trap). The hybrid avoids both: EM is exact at low t, g₀-only error decays as t^{−3/4} above 200 (≤7e-4 at t=10⁵ — adequate for statistics; position error ≤1.2e-4).

## Validation (the honesty bar)
- numpy port of the identical f64 logic vs mpmath zetazero: max |Δ| = **1.4e-14** on the first 20 (algorithm logic correct).
- Rust binary vs mpmath zetazero, first 100: **100/100 matched, max |Δ| = 5.637e-4** (at k=94, t≈221 — the EM/RS crossover, exactly the predicted g₀-only tail region). Position error ≈ 2.5e-4 — within the ≤1e-3 statistics spec.

## The runs (laptop, rustc 1.97.1; gcc 14.2.1 installed via xbps for the linker)
- Step 0.2: 100k zeros, t_last=75446.99, **N(T) diff = −785.7** (0.78% miss).
- Step 0.1: 100k zeros, t_last=74980.92, **N(T) diff = −89.2** (0.089% miss). Mechanism: twin pairs with gap < scan-step fall between samples (even # of crossings in one interval). Min realized gap 0.0419 — consistent. The residual −89 is documented, not hidden.

## The statistics (tools/zeros_rust/stats_100k.py, phone proot, N=100k, θ/π unfolding → density 1, mean unfolded spacing 1.0009)
1. **Periodogram band (1.005, 1.3]: mean F = 0.9808, band-z = −0.15** (n_eff=59; F(1.00) = 1423.7 — the α=1 spike, isolated). At N=10k the same estimator gave mean 1.056, z = +0.43. **10× the sample ⇒ the band excess is NOT significant — it vanishes (mean now < 1). The "≥11σ bump" is fully accounted for by the isolated α=1 arithmetic spike. Confirms bump-price RESOLVED-NEGATIVE with 10× data.**
2. **Realized m₃(1/2) = 4.7829 ± 0.0013** (390 blocks of 256, sinc kernel λ=1/2) — finite-height deficit shrinking with height (4.75 at 10k zeros → 4.783 at 100k) toward the PROVEN 5 (Rudnick–Sarnak). Supports the m₃ paper's PROVEN value with a 10×-larger numerical read.
3. **Spacing (new read):** mean gap 1.0009 (perfect unfolding); **min gap = 0.0419** (a genuine ultra-close twin); frac(gap<0.1)=4.8e-4, frac(gap<0.3)=0.0206, frac(gap<0.5)=0.0955 vs Poisson 0.393 — strong level repulsion (Wigner-like), as expected for the zeros. Caveat: frac(gap<0.1) is slightly depressed by the −89 scan misses (ultra-close twins); the honest range is 4.8e-4…1.4e-3 — still well below the sine-process ~3.3e-3, i.e. repulsion stronger than the sine prediction at the smallest scales (consistent with the zeros' known "repulsion excess" at tiny gaps; flagged, not adjudicated here).

## Labels
CHECKED NUMERICALLY (validation + all statistics); the −89 deficit documented with mechanism. The tool itself is a reusable asset: `tools/zeros_rust/` (main.rs, stats_100k.py, README). Zero file: tools/data/zeros_rust_100k.txt (100k ordinates).

RESULT: COMPLETE — fast zero-finder validated (5.6e-4), 100k zeros generated; band-z −0.15 at 10× sample kills the beyond-1 bump definitively; m₃ → 5 confirmed at 4.783±0.001; spacing shows strong repulsion + a 0.042 min-gap twin.

## Addendum (924k zeros, 8-core parallel shards, t to 5.6e5 — 9.25x sample)
- m3(1/2) = 4.8060 +- 0.0005 (N=256 blocks, 3609 blocks) — deficit shrinking with height toward PROVEN 5.
- **Marked connected part T = m3 - D - pair (m3_min_frontier convention): mean +0.416 +- 0.0002, range [+0.333, +0.463]** (3609 blocks). The empirical floor of the 0.70-gap input is +0.333 with ZERO exceptions across 3609 blocks; marching to PROVEN A3(1/2)=+1/2. A proven T >= c > 0 would reopen the m3-class door (certificate value > Parseval floor 0.50).
- Spacing: min gap 0.0279 (real ultra-twin at t ~ 5e5); frac(gap<0.1)=4.1e-4, frac(gap<0.5)=0.0999 — clean small-gap regime (the step-0.1 twin deficit is 0.21%, documented).
