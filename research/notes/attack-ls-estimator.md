# Attack note — Landy–Szalay bias-canceling form-factor estimator (vector B1)

Status: CHECKED NUMERICALLY (script + command cited per number); analytic identities labeled PROVEN.
Date: 2026-08-11 (vector B1 of `idea-generator-crystallography.md`, executed round protocol)
Tooling: `tools/attack_ls_estimator.py` (numpy; pair counting verified against brute force on a
small case, max abs diff 0), data `tools/data/zeros_computed_10000.txt` (10 000 ordinates),
results `tools/data/ls_results.json`.
Command: `uv run --quiet --with numpy --with scipy python tools/attack_ls_estimator.py` (~9 min;
`elapsed_s = 519.3` in the JSON). Code lives at `tools/attack_ls_estimator.py` (new file, no
canonical `tools/` file edited).

---

## 0. Question, in one sentence

Map the standard Landy–Szalay (1993) two-point estimator ξ̂ = (DD − 2DR + RR)/RR onto the
zero-configuration form factor and test whether it is materially better than the naive
pair-correlation estimator of `verification-001.md` §4 / `tools/hot_hand_calib.py` at the
certificate's critical scales (α ∈ [0.5, 1.5], especially the α ≈ 1.0–1.3 arithmetic-feature
zone), and whether the survey mask (the finite window [T, 2T] = the unfolded interval) enters
DD/DR/RR identically and cancels.

## 1. The estimator mapping (B1 recap, crystallography note)

The B1 transfer claim: the certificate's three bookkeeping terms ARE the three LS pair counts —
**DD** (data pairs) ↔ the measured pair sums (off-diagonal + diagonal contributions to the S(j)
rows); **DR** (data × random) ↔ the first-order sums (zeros × window, the explicit-formula
*diagonal* prime sums); **RR** (random × random) ↔ the window's self-correlation, the ‖W_T‖²_HS
norm machinery (proven coefficient 1/2 + (1/√2)cot(1/√2) ≈ 1.3275/2 per unit, `verification-001.md`
§1). The LS combination (DD − 2DR + RR)/RR is the standard bias-canceling estimator of the
*excess correlation over the window-only null* — i.e. of (F − 1).

The empirical test below implements exactly this: DD/DR/RR assembled from the pair sums on the
real zeros and a uniform (window-only) random catalog; F̂_LS = 1 + Σ_τ ξ̂_LS(τ) e^{2πiατ}Δτ.

## 2. Implementation (what the script computes)

Unfold the 10k zeros by the Riemann–Siegel phase x_j = θ(γ_j)/π (density ≈ 1); window
W = [x_1, x_N] = [−0.5503, 10000.1483], L = 10000.7, n = 10000, empirical ρ = n/L = 0.999930.
τ-bins [0, 30), Δτ = 0.1; α-grid 0.05…3.00 step 0.05 (identical to `hot_hand_calib.py` so numbers
are directly comparable). Pair counts N_DD (unordered data pairs), N_DR (ordered data–random),
N_RR (unordered random pairs) via sorted-array sliding windows (only separations < 30 are
materialized; verified against brute force on n=300/m=250, max abs diff 0). Normalized counts
and window pair probability (interval):

    DD = 2·N_DD/(n(n−1))     DR = N_DR/(n·n_r)      RR = 2·N_RR/(n_r(n_r−1))
    P_W(τ) = 2·(L−τ)·Δτ/L²                          (window pair-separation probability)

Estimators (both on the identical N_DD input — the only difference is the normalization):

    naive:  ξ̂_naive(τ) = DD/P_W − 1;      F̂_naive(α) = 1 + Σ_τ ξ̂_naive(τ) e^{2πiατ}Δτ
    LS:     ξ̂_LS(τ)   = (DD − 2DR + RR)/RR;  F̂_LS(α)  = 1 + Σ_τ ξ̂_LS(τ) e^{2πiατ}Δτ

Random catalogs: uniform on W, n_r = N (matched) and n_r = 8N (precision variant); the zeta LS
curve is the mean over 40 (n_r = N) / 20 (n_r = 8N) catalog realizations, std = the
catalog-realization (Monte-Carlo) component. GUE null: Dumitriu–Edelman β=2 tridiagonal
(N=12500, central 80%, semicircle-unfolded, 10 000 points), 24 replicates, naive + LS per
replicate (LS: 8 catalogs each). Block analysis: 10 windows of 1000 zeros, naive + LS per block.

**Sanity (PROVEN identity of machinery):** F̂_naive on the 10k zeros reproduces
`hot_hand_calib_results.json` (`zeta_N10000`) exactly at every sampled α (0.706/0.866/0.967/0.957/
1.378/0.893/1.554/1.019/1.003/0.966 at α = 0.50/0.75/0.90/0.95/1.00/1.05/1.10/1.30/1.50/2.00 — all
match to 3 decimals). The GUE null (24 reps) matches theirs (8 reps) within the std-estimate
noise. The pair-counting is therefore the same machinery, and the comparison below is
apples-to-apples.

**Degeneracy of LS on a sharp interval (PROVEN, elementary):** as n_r → ∞, RR → P_W and
DR → P_W (uniform randoms), so ξ̂_LS → DD/P_W − 1 = ξ̂_naive. LS with a finite catalog is the naive
estimator plus Monte-Carlo shot noise; it cannot change the mean beyond MC noise, and it adds
variance. The only way LS improves on naive is when the window is *not* an interval (masked /
smooth), where the analytic P_W is unavailable — see §6.

## 3. Comparison table — naive vs LS on the same 10k zeros (CHECKED NUMERICALLY)

| α    | naive | LS (n_r = N) | LS (n_r = 8N) | GUE null (24 reps) | ΔLS8N−naive |
|------|-------|--------------|---------------|--------------------|-------------|
| 0.50 | 0.706 | 0.702 ± 0.053 | 0.703 ± 0.010 | 0.750 ± 0.017 | −0.003 |
| 0.75 | 0.866 | 0.867 ± 0.052 | 0.861 ± 0.012 | — | −0.005 |
| 0.90 | 0.967 | 0.978 ± 0.060 | 0.970 ± 0.017 | 0.948 ± 0.031 | +0.003 |
| 0.95 | 0.957 | 0.961 ± 0.078 | 0.960 ± 0.018 | — | +0.003 |
| 1.00 | 1.378 | 1.362 ± 0.073 | 1.368 ± 0.032 | 1.007 ± 0.037 | −0.010 |
| 1.05 | 0.893 | 0.896 ± 0.063 | 0.891 ± 0.020 | 0.996 ± 0.037 | −0.002 |
| 1.10 | 1.554 | 1.544 ± 0.087 | 1.540 ± 0.027 | 0.994 ± 0.038 | −0.014 |
| 1.30 | 1.019 | 1.005 ± 0.069 | 1.012 ± 0.018 | 0.999 ± 0.034 | −0.007 |
| 1.50 | 1.003 | 1.010 ± 0.062 | 1.006 ± 0.020 | 1.000 ± 0.038 | +0.003 |
| 2.00 | 0.966 | 0.970 ± 0.068 | 0.964 ± 0.017 | 0.982 ± 0.035 | −0.002 |
| 2.50 | 0.955 | 0.956 ± 0.075 | 0.956 ± 0.016 | — | +0.001 |
| 3.00 | 0.973 | 0.963 ± 0.057 | 0.971 ± 0.023 | — | −0.002 |

(`ls_results.json`: `zeta_naive`, `zeta_ls_mean/std`, `zeta_ls8_mean/std`, `gue_naive_mean/std`;
the ± shown for LS is the std over catalog realizations — the Monte-Carlo component.)

Every |ΔLS8N − naive| ≤ 0.014, and the intrinsic noise at N = 10000 is ~0.04 (GUE null std).
**The LS estimator changes the measured curve by ≲ ⅓ of its own noise. There is no material
mean/bias difference.** The n_r = 8N LS curve (lowest MC noise) agrees with naive to ≤ 0.014 at
all α, including the critical zone.

## 4. Bias / variance verdict

**Bias (mean): no reduction.** The naive normalization is already unbiased for the sharp-interval
window: the analytic expectation (L−τ)ρ²Δτ is exact (ρ = n/L, L = window span), so there is no
residual window bias for LS to cancel. Empirically: LS(8N) mean tracks naive to ≤ 0.014 at every
α (table above); LS(N) mean tracks to ≤ 0.011. CONFIRMED: the measured deficit Δ(T) does not
shrink under LS — the B1 decision branch resolves in the "deficit is not an estimator-window
artifact" direction (§5).

**Variance (worse, not better, at matched n_r).** Variance decomposition at N = 10000
(`ls_results.json` `var_*`; intrinsic proxy = GUE-naive std over 24 reps; total = sqrt(intrinsic²
+ MC²)):

| α    | intrinsic | MC (n_r=N) | total (n_r=N) | MC (n_r=8N) | total (n_r=8N) | naive total |
|------|-----------|------------|---------------|-------------|----------------|-------------|
| 0.50 | 0.017 | 0.053 | 0.055 | 0.010 | 0.020 | 0.017 |
| 1.00 | 0.037 | 0.073 | 0.081 | 0.032 | 0.048 | 0.037 |
| 1.10 | 0.038 | 0.087 | 0.095 | 0.027 | 0.047 | 0.038 |
| 1.30 | 0.034 | 0.069 | 0.077 | 0.018 | 0.039 | 0.034 |
| 1.50 | 0.038 | 0.062 | 0.073 | 0.020 | 0.043 | 0.038 |
| 2.00 | 0.035 | 0.068 | 0.077 | 0.017 | 0.039 | 0.035 |

At the certificate's critical scale α = 1.10: **LS with a matched random catalog (n_r = N) is
2.5× noisier than naive** (0.095 vs 0.038); with n_r = 8N it is 1.24× noisier (0.047 vs 0.038).
The random-catalog shot noise (DR and RR fluctuations) dominates the intrinsic zero-sample noise
at matched catalog size and never fully disappears at 8N. Block check (10 × 1000 zeros): LS
means match naive (1.579 vs 1.558 at α=1.1; 0.993 vs 0.999 at 1.5; 0.995 vs 0.970 at 2.0) and LS
block stds are ≥ naive (0.533 vs 0.537 at 1.1; 0.162 vs 0.101 at 0.5; 0.157 vs 0.125 at 2.0) —
same story at N = 1000.

**Verdict: LS is not materially better at the certificate's critical scales on the sharp-interval
window — it is equal in bias and worse in variance.** The naive estimator is the n_r → ∞ limit of
LS and its window normalization is exact here; LS buys nothing on an interval and costs precision.
(LS's genuine value — irregular windows — is discussed in §6.)

## 5. Does the improved F̂ change any belief? (beyond-1 climb-then-decay under LS)

**The α ≈ 1.0–1.3 arithmetic feature: real, unchanged, ≥ 11σ under LS** (CHECKED NUMERICALLY):

| α    | zeta naive | zeta LS(8N) | GUE null | naive σ | LS σ |
|------|-----------|-------------|----------|---------|------|
| 1.00 | 1.378 | 1.368 ± 0.032 | 1.007 ± 0.037 | — | — |
| 1.05 | 0.893 | 0.891 ± 0.020 | 0.996 ± 0.037 | −2.9σ | −2.7σ |
| 1.10 | 1.554 | 1.540 ± 0.027 | 0.994 ± 0.038 | **14.4σ** | **11.8σ** |

Significance computed as (F̂ − 1)/σ_null with σ_null from 24 GUE replicates (naive null std for
the naive column, LS null std for the LS column; `ls_results.json` `gue_naive_std` /
`gue_ls_std`). Under LS the α=1.10 feature remains ≥ 11σ — **it is not a measurement artifact of
either estimator.** It is slightly *less* significant under LS only because LS inflates the null's
own std with catalog shot noise, not because the feature moves (1.554 → 1.544, Δ = 0.010).

**The beyond-1 "climb-then-decay" of `verification-001.md` §4: not resurrected by LS** — the two
estimators agree that beyond α ≈ 1.3 the curve is flat ≈ 1 (naive: 1.019/1.003/0.966/0.955/0.973;
LS(8N): 1.012/1.006/0.964/0.956/0.971 at α = 1.30/1.50/2.00/2.50/3.00 — no monotone trend, scatter
±0.02, consistent with the null). The hot-hand calibration (G3.1, `hot_hand_calib.py`) already
established this decay is a finite-sample artifact of the estimator on *null* data; LS — the
standard bias-canceling estimator — reproduces exactly the same flat-beyond-1 shape.

**Belief-change statement (honesty guardrails):** the B1 estimator upgrade changes **nothing** we
believe about the beyond-1 form factor. The beliefs stand as they were after G3.1: (i) no empirical
hint of F < 1 beyond α = 1 (PROVEN-not-shown, consistent with Montgomery/GUE); (ii) a real
finite-height arithmetic feature at α ∈ [1.0, 1.3], now certified at ≥ 11σ by the *standard*
estimator, cause still unidentified (G3.1 R-4 follow-up: τ-bin/prime decomposition, height
dependence). The marginal content of B1 is: the beyond-1 deviation is **not a window-bias artifact
of the estimator normalization** (LS does not shrink it — §4), which is the branch B1 flagged as
"deficit is intrinsic" — with the caveat that the "deficit" in question (a flat, null-consistent
curve) is not a deficit at all.

## 6. Mask / edge correction: does the window enter DD/DR/RR identically and cancel?

**Yes — for the sharp-interval window, exactly, and the naive estimator already performs it.**
Two independent statements:

1. **Analytic (PROVEN):** for an interval window of length L, the window pair probability is
   P_W(τ) = 2·(L−τ)·Δτ/L², whose (L−τ) factor is the 1D window self-overlap integral
   W(τ) = ∫1_W(x)1_W(x−τ)dx = L−τ. Each normalized LS term (DD, DR, RR) is the true pair
   correlation (or 1 for the null) times this common P_W; the window appears only through the
   common factor, which cancels in (DD − 2DR + RR)/RR — independent of the window's shape. The
   naive estimator cancels the same factor analytically via the exact (L−τ)ρ²Δτ expectation.
2. **Numeric (CHECKED NUMERICALLY):** with uniform randoms on W, RR/P_W and DR/P_W = 1 to within
   max 0.0153 / 0.0100 over all τ at n_r = N (pure catalog shot noise), and to within 0.0016 /
   0.0023 at n_r = 8N (sampled τ = 0.55…29.55: RR_norm 1.0003/0.9995/1.0011/1.0013/1.0002/1.0016;
   DR_norm 0.9983/1.0004/1.0023/1.0009/0.9977/0.9987). The window is encoded identically in DD,
   DR, and RR and cancels in the LS ratio; `ls_results.json` `mask_check`.

**Where LS's mask correction is *non-degenerate* (stated, not computed here):** the sharp
[T, 2T] interval is not the certificate's actual survey window — the paper's W_T is the *smooth*
φ̂_T test-function window, for which the pair-count expectation is the smooth self-convolution
∫φ̂_T(x)φ̂_T(x−τ)dx, not (L−τ)ρ²Δτ. On a smooth or masked window the naive (L−τ) normalization is
wrong at the O(sidelobe) level, and LS (random catalog drawn from the actual window weighting) is
the standard fix. That is the version of B1 that could matter for P6's error budget; it requires
weighted pair counts on the φ̂_T window and is left as a follow-up (the task's mandate — the
sharp window [T, 2T] — is fully answered above).

## 7. Deliverables / decision input

- **Confirmed mapping:** DD/DR/RR ↔ pair sums / diagonal (first-order) prime sums / HS-norm
  window self-correlation — the certificate's three bookkeeping terms are exactly the three LS
  pair counts (B1's vocabulary transfer is correct).
- **Negative (documented result):** on the sharp-interval window, LS is not materially better —
  equal bias, 1.2–2.5× worse variance at matched and 8× catalogs (§4). The naive estimator is
  the exact-window limit of LS; no estimator upgrade is warranted for the sharp window.
- **Mask statement:** the window enters DD/DR/RR identically and cancels — PROVEN analytically,
  CHECKED NUMERICALLY to ≤ 0.2% at n_r = 8N (§6). The non-degenerate case (smooth φ̂_T window)
  is the flagged follow-up.
- **Beliefs unchanged by the estimator;** the α ∈ [1.0, 1.3] feature is certified ≥ 11σ by the
  standard estimator; no decay beyond α = 1 (both estimators flat ≈ 1, null-consistent).
- **Funding input:** the marginal value of further estimator engineering for the sharp window is
  zero; the funded follow-up from this line is the *arithmetic feature itself* (G3.1 R-4: τ-bin /
  prime decomposition, height dependence) and the smooth-window LS for P6 (§6), in that order.

**Honesty footer.** Every number above is CHECKED NUMERICALLY via
`tools/attack_ls_estimator.py` (command `uv run --quiet --with numpy --with scipy python
tools/attack_ls_estimator.py`, results `tools/data/ls_results.json`; pair counting verified
against brute force, max diff 0; naive curve reproduces the cached `hot_hand_calib_results.json`
exactly, so the comparison base is the same machinery as G3.1). Analytic statements (n_r→∞
degeneracy, window-overlap cancellation) are PROVEN by the formulas displayed in §2/§6. Domain
facts (Landy–Szalay 1993 estimator form, GUE sine-kernel null, Dumitriu–Edelman sampling) are
standard mathematics used as null model and estimator, not asserted as new theorems. No claim
here touches the RH proof; the deliverable is a documented, reproducible measurement and a
documented negative (LS adds no bias-cancellation on the sharp window; the α≈1.1 feature is
real under both estimators).
