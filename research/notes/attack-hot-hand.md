# G3.1 — Hot-hand calibration of the empirical beyond-1 form factor

**Agent:** EXECUTIONER. **Vector:** G3.1 (idea-generator-games.md, Pool 3 — sports analytics /
hot-hand framing). **Date:** 2026-08-11.
**Question:** verif-001 §4 reports the empirical zeta form factor F̂(α) "climbs to ≈ 0.93–1.0
near α = 1, decays beyond", with large sample noise at N = 3000. Is there ANY genuine empirical
hint against Montgomery's conjecture (F = |α| for 0 < α < 1, F = 1 for α > 1) beyond α = 1, or is
the climb-then-decay a finite-sample artifact of the estimator — the same statistical trap as the
hot-hand debate (naive aggregate statistics carry built-in noise/structure that reads as signal)?
M29 closed the theory side (no unconditional input beyond 1); this settles the EMPIRICAL status.

**Verdict (up front): ARTIFACT.** At non-lattice α ∈ (1, 3] the zeta F̂(α) is statistically
indistinguishable from the sine-kernel (GUE) null: the α-averaged level over (1, 3] is
**0.859 vs 1.050 ± 0.163** (z = **−1.18σ**) at N = 10⁴ and **1.141 vs 0.998 ± 0.136** (z = **+1.05σ**)
at N = 3000 — both within 1.2σ, opposite signs, no reproducible decay. The per-α fluctuations of
F̂ have **std ≈ 1 at every N** (Exp(1)-distributed, verified at N = 3000 and N = 10⁴) — they do
NOT shrink with sample size, so the "climb-then-decay" is exactly the estimator's built-in noise
floor, and the largest zeta excursion over 55 α-bins (|z| = 5.06) is at the ~85th percentile of
what 55 independent noise draws produce (P(max|z| > 4.54) = 0.19). The only reproducible
zeta-vs-null deviation is a **single-point spike at the integer α = 1** (F̂ = 102 at N = 3000,
246 at N = 10⁴, growing ≈ linearly in N) — the Gram-point lattice artifact of the θ/π unfolding,
present in the data's unfolding and absent in the null's; it is measure-zero in α, carries no
information about the pair-correlation measure, and is NOT Montgomery evidence. No escalation.

---

## 1. The estimator (and its identity with verif-001 §4)

**Estimator (identical for zeta, null, and baseline):** with x_j the mean-spacing-1 unfolded
ordinates,
    F̂(α) = (1/N) · | Σ_{j=1}^{N} e^{2πiα x_j} |²   (standard periodogram form factor).

*Why this is the correct estimator (derived, then verified numerically):* writing
S(α) = Σ_j e^{2πiαx_j}, the empirical pair-count Fourier transform is
(1/N)Σ_{n≠m}e^{2πiα(x_n−x_m)} = |S(α)|²/N − 1; the −1 subtracts the δ(α) mean-field, which for a
finite window [0,W], W≈N, contributes only |(e^{2πiαW}−1)/(2πiα)|²/N = O(1/N) at α ≫ 1/N — so
F̂(α) = |S(α)|²/N is the estimator with the right expectation. For the sine-kernel DPP on a window
of length N (intensity 1, kernel K(x,y) = sin(π(x−y))/(π(x−y))), using ρ₂ = 1 − |K|²,
    E|S(α)|² = N + sin²(παW)/(π²α²) − W(1−|α|)_+  ⇒  E[F̂(α)] = |α| + O(1/N)  (α<1),
                                                                = 1 + O(1/N)  (α>1).
PROVEN (algebra) and CHECKED NUMERICALLY (this run: null mean at α = 0.45 is 0.47±0.49; at
α > 1 the null mean is 0.98–1.05 at both N). The variance: Var(S(α)) = N·min(α,1) ⇒ per-α
std(F̂) ≈ min(α,1)·(1 + O(1/√N)) — **O(1) and N-independent**; measured std/mean = 0.99–1.00
(Exp(1)-like) at both N (see §3). Only α-averaging (or α-smoothing) reduces the noise.

**Identity with verif-001 §4:** the §4 numbers were produced by a script that no longer survives
in tools/ (the surviving `tools/zeta-rs/src/checks.rs` `paircorr` prints the spacing histogram,
not the form factor). The periodogram F̂ above is the standard form factor (matches the §4
description "F(α) ≈ |α| for 0<α<1, climb to ≈0.93–1.0 near α=1, noisy values beyond"); running it
on the same zeros at N=3000 reproduces §4's qualitative picture (values 3.35/1.93 at α = 0.85/0.95,
then scattered values 0.09–3.6 beyond 1). CHECKED NUMERICALLY (this run). We therefore use it as
"the verif-001 estimator"; a future agent re-deriving §4's exact numbers should re-audit this
identity, but the verdict below is robust to the two standard variants (both sit in the band).

## 2. The two estimators' data

- **(a) zeta:** first N ordinates of `tools/data/zeros_computed_10000.txt` (10 000 ordinates
  independently computed by `zeta-rs zeros 10000`, Euler–Maclaurin Z(t) sign-change + bisection;
  first zeros agree with LMFDB). Unfolded by x_j = θ(γ_j)/π (Riemann–Siegel θ, asymptotic series,
  accurate to ~1e-12 for t ≥ 14). Unfolded spacing mean/std: 0.99997/0.38630 (N=3000),
  1.00017/0.39295 (N=10⁴) — mean 1 as required.
- **(b) sine-kernel null (GUE):** per realization, generate the β=2 Hermite tridiagonal
  (Dumitriu–Edelman: diag N(0,2), off-diagonal b_k = √χ²_{2(N−k)}), full eigendecomposition
  (`scipy.linalg.eigvalsh_tridiagonal`), eigenvalues ÷ √(2N) → semicircle on [−2,2] (calibration:
  this tridiagonal matches a Wigner GUE of the correct normalization to max quantile difference
  0.007 at N=800 — scratch script `/tmp/ff_calib3.py`, CHECKED NUMERICALLY), unfold by the exact
  semicircle CDF x = N_gue·F(λ), keep the central 80% → N points of mean spacing 1 on a window of
  length N (verified: 0.9998/0.99998, window 2998/9999, this run). This is the sine-kernel
  process in the bulk (GUE ↔ sine-kernel universality is a theorem; N=10⁴ corrections O(1/N)).
- **(c) Poisson baseline** (no repulsion, F = 1 beyond 1 in expectation): x = cumulative sum of
  N exponential(1) spacings.

Reps: N=3000: GUE 200, Poisson 200; N=10⁴: GUE 40, Poisson 100. Poisson additionally used for
the multiple-comparison calibration (3000/1500 reps) — legitimate because at α>1 Poisson and GUE
share the same Exp(1) per-α noise floor (measured std/mean 0.99–1.00 for both).

## 3. Results

### 3.1 Headline: zeta vs sine-kernel band, N = 10⁴ (the new, better-statistics run)

| α | zeta F̂ | GUE mean | GUE σ | z | Poisson mean | note |
|---|--------|----------|-------|-----|--------------|------|
| 0.45 | 0.008 | 0.472 | 0.493 | −0.94 | 1.270 | |
| 0.85 | 0.355 | 0.939 | 0.941 | −0.62 | 0.970 | |
| 0.95 | 1.549 | 0.740 | 0.774 | +1.04 | 1.032 | |
| 1.00 | 245.840 | 1.106 | 0.991 | — | 0.775 | *lattice spike (see §4)* |
| 1.05 | 1.358 | 0.977 | 0.908 | +0.42 | 1.170 | |
| 1.10 | 0.402 | 0.846 | 1.123 | −0.40 | 0.939 | |
| 1.25 | 1.292 | 1.009 | 1.295 | +0.22 | 1.005 | |
| 1.55 | 0.128 | 1.338 | 1.450 | −0.83 | 1.035 | |
| 1.80 | 2.685 | 1.052 | 0.983 | +1.66 | 1.083 | |
| 2.05 | 0.331 | 0.819 | 0.748 | −0.65 | 0.939 | |
| 2.30 | 0.424 | 1.117 | 1.018 | −0.68 | 1.166 | |
| 2.55 | 0.096 | 1.034 | 0.727 | −1.29 | 0.997 | |
| 2.80 | 5.120 | 0.974 | 0.819 | +5.06 | 0.891 | largest per-α excursion |
| 3.00 | 0.857 | 0.879 | 0.785 | −0.03 | 0.997 | |

**α-averaged level over (1,3] (clean α, 37 bins; the decisive "is it systematically below 1" test):**
zeta **0.859** vs GUE **1.050 ± 0.163** → **z = −1.18σ**. Sub-windows: (1,2] zeta 0.782
(noise-floor std 0.228), (2,3] zeta 0.940 (0.240) — both within ~1σ. Ramp (0,1]: zeta 0.497 vs
GUE 0.479 — dead on. 95% CI on the beyond-1 level: 0.859 ± 1.96·0.163 = **[0.54, 1.18]** —
consistent with Montgomery's 1, and *ruling out* any strong decay (e.g. a level ≤ 0.5) at 95%.

**Per-α multiple comparisons (55 clean bins):** max|z| = 5.06 at α = 2.80; counts |z|>2: 2,
|z|>3: 1 (expected under the Exp(1) noise floor, |F̂−1|>x ⟺ F̂>x+1: ~2.7 and ~1.0 over 55 bins —
observed matches expectation, no excess). The maximum of 55 independent bins has median 3.40 and
p90 5.21 (empirical), and **P(max|z| > 5.06) ≈ 0.12** — the zeta's largest excursion is at the
~87th percentile of the null's max distribution, unremarkable. (For reference P(max|z| > 4.54) =
0.19, P(max|z| > 3.11) = 0.60.)

### 3.2 The verif-001 regime: N = 3000

| α | zeta F̂ | GUE mean | GUE σ | z | note |
|---|--------|----------|-------|-----|------|
| 0.50 | 2.849 | 0.515 | 0.542 | — | half-integer (lattice) |
| 0.85 | 3.350 | 0.809 | 0.894 | +2.84 | |
| 0.95 | 1.929 | 0.928 | 1.027 | +0.97 | |
| 1.00 | 102.432 | 1.115 | 1.061 | — | lattice spike |
| 1.05 | 0.764 | 0.976 | 0.976 | −0.22 | |
| 1.10 | 1.499 | 1.085 | 0.960 | +0.43 | |
| 1.25 | 3.615 | 0.911 | 0.870 | +3.11 | |
| 1.80 | 0.093 | 0.950 | 1.056 | −0.81 | |
| 2.05 | 0.464 | 0.964 | 0.907 | −0.55 | |
| 2.55 | 0.967 | 1.067 | 1.052 | −0.10 | |
| 2.80 | 2.955 | 0.913 | 0.870 | +2.35 | |

α-average (1,3]: zeta **1.141** vs GUE **0.998 ± 0.136** → **z = +1.05σ**. max|z| = 3.11
(P(max>3.11) = 0.59). The verif-001 "climb-then-decay" description is reproduced as pure noise:
the curve near α = 1 (values 3.35, 1.93, 0.76, 1.50, 2.14, 1.09, 3.62, …) is the periodogram
noise floor with the same character as the null.

### 3.3 Noise floor is N-independent (the hot-hand trap, quantified)

GUE per-α std/mean at α>1: 0.97 (N=3000), 1.00 (N=10⁴); Poisson: 0.997/0.994 (std/mean 1.00) at
both N — F̂(α>1) is Exp(1)-distributed at every sample size. **Adding zeros does not reduce the
per-α noise of this estimator at all.** This is the quantitative form of the hot-hand lesson:
a naive aggregate statistic with a built-in, N-independent noise floor of the same order as its
mean cannot be read by eye. Only the α-average shrinks (std ≈ 0.16 at N=10⁴, ∝ 1/√(N·Δα)).

### 3.4 G2.6 companion (block variance, "luck"): no excess variance

10 zeta blocks of 1000 zeros vs 100 GUE blocks of 1000 points, α ∈ {0.9, 1.1, 1.5, 2.0}:
zeta block std [0.75, 1.65, 0.81, 1.08] vs GUE block std [0.98, 1.02, 1.15, 0.96] — the zeta
block-to-block spread at α > 1 is sample noise, no extra variance. (Computed with a one-off
`uv run --quiet --with numpy --with scipy python -c "..."` block loop reusing the canonical
script's `gue_bulk`/`form_factor`; numbers CHECKED NUMERICALLY.)

## 4. The one real deviation — the α = 1 Gram-lattice spike (an estimator artifact, not physics)

At the **integer** α = 1 the zeta F̂ is 102.4 (N=3000) and 245.8 (N=10⁴) vs the null's ≈ 1.1 —
a ratio F̂/N ≈ 0.034, 0.025, i.e. a **constant per-zero phase coherence of ~17%, growing ≈
linearly with N**. Cause: the θ/π unfolding places the zeros at x_j = j − 7/8 + ε_j with the
Gram-point deviations ε_j (measured std of x_j − j: 0.274 at N=3000, 0.983 at N=10⁴ — an O(1),
non-shrinking deviation), so e^{2πi·x_j} keeps a persistent partial alignment (Gram's law: the
zero brackets consecutive Gram points). The CDF-unfolded GUE null has no such coherence at α = 1
(mean ≈ 1), so this spike is a property of the *data's specific unfolding*, not of the pair
correlation. α = 2 and α = 3 show **no** spike (zeta 0.39, 0.86 at N=10⁴), consistent with the
ε_j-structure, not with any conjectured F-value. Half-integers (α = 1.5, 2.5; zeta 0.03, 0.31) sit
below the null for the same lattice reason (the null's exact-CDF unfolding cancels the
alternating sum "too perfectly").

**Why this is NOT Montgomery evidence (PROVEN reasoning):** Montgomery's conjecture concerns the
pair-correlation *measure*; its form factor F(α) = 1 beyond 1 is the Fourier transform of an
absolutely continuous density, and a single point in α carries zero measure. A spike that (i) is
one bin wide, (ii) grows with N (so it cannot be a finite-N shadow of any limit value), and (iii)
is absent at other integers, is an unfolding artifact. The hot-hand reading to avoid: "F̂(1) = 246
≫ 1, the data contradict Montgomery" would be the same error as reading a streak in a
negatively-biased conditional statistic. **All integer and half-integer α are therefore excluded
from the verdict** (documented in the script as "lattice-polluted").

## 5. Verdict

**ARTIFACT — no empirical hint against Montgomery beyond α = 1.**

- The empirical beyond-1 form factor of the first 10⁴ zeta zeros is statistically
  indistinguishable from a finite sample of the sine-kernel (GUE) process of the same size:
  α-averaged level over (1,3] at z = **−1.18σ** (N=10⁴) and **+1.05σ** (N=3000); every
  sub-window and every ramp check within ~1.3σ; the largest per-α excursion (|z| = 5.06 at
  α = 2.80) is at the ~87th percentile of the null's own max-of-55-bins distribution
  (P(max|z| > 5.06) ≈ 0.12) — no multiple-comparison excess (|z|>3 count: 1 of 55 vs ~1.0
  expected under the Exp noise floor).
- The "climb-then-decay" of verif-001 §4 is the estimator's built-in noise: per-α std ≈ 1 at
  every N (Exp(1), verified at both sample sizes) plus the single-point Gram-lattice spike at
  α = 1 (estimator artifact of the θ/π unfolding; §4). The N=3000 run reproduces verif-001's
  qualitative picture; the N=10⁴ run shows the same noise structure with the same verdict.
- α-range of the verdict: **all non-lattice α ∈ (0.05, 3.0]**, in particular the beyond-1
  region (1, 3] where the claim of "decay" lived. Lattice α (integers, half-integers) carry the
  unfolding artifact and are excluded by construction.

## 6. What the verdict implies

1. **The empirical status of P3 is settled (artifact):** there is no empirical hint against
   Montgomery's F = 1 beyond 1 in the low-lying zeros. Any future "the data already show a
   decay / a deviation beyond 1" argument is neutralized: the same estimator, run on a process
   with F ≡ 1 exactly, produces the same climb-then-decay noise and the same α=1 lattice spike.
2. **A finite measurement cannot bound the asymptotic F** (the [CD-W2]/[CD-A1] lesson, now with
   a quantitative form): even with N = 10⁴ zeros, the per-α estimator has O(1) noise at every α
   > 1, so per-α comparisons never gain power; the α-average bounds the beyond-1 *level* to
   [0.54, 1.18] at 95% (N=10⁴) — consistent with 1, excluding strong decays, and far from the
   ~1.4% in-class scale the certificate would need to care about. Nothing here changes the M29
   theoretical closure (no unconditional input beyond 1); the empirical side now agrees.
3. **The sine-kernel (GUE) null is validated as the correct empirical model of the low-lying
   zeros' pair statistics** at the achievable resolution: ramp |α| for α<1 (0.497 vs 0.479 at
   N=10⁴) and plateau 1 beyond (0.859 vs 1.050) both match.
4. **No escalation.** G3.1's probe is closed as a clean negative (hot-hand artifact), matching
   its catalog label "probe; settles the empirical status of the beyond-1 trend".

## 7. Honesty labels & provenance

- **Script (canonical, produced every number in §3–§4):** `tools/hot_hand_calib.py`
  (new file; `tools/` path was unowned — no other agent's file overwritten). Results JSON:
  `tools/hot_hand_calib_results.json`; figure: `tools/hot_hand_calib_fig1.png`.
  **Command:** `uv run --quiet --with numpy --with scipy --with matplotlib python tools/hot_hand_calib.py`
  (seed 20260811; elapsed 1252 s). Rerun to reproduce.
- **Calibration numbers** (tridiagonal-vs-Wigner 0.007, max|z| distributions, null spacing):
  scratch scripts `/tmp/ff_calib3.py`, `/tmp/ff_calib_maxz.py` and the inline block command in
  §3.4 — CHECKED NUMERICALLY, commands in the run log.
- **Estimator expectation E[F̂] = |α|/1 and the N-independent variance** (E|S|² formula,
  Var(S) = N·min(α,1)): PROVEN (algebra, §1) and CHECKED NUMERICALLY (null means/stds, this run).
- **GUE ↔ sine-kernel universality** for the null: PROVEN theorem (Deift, Tao–Vu, Erdős–Yau bulk
  universality); finite-N correction O(1/N) at N = 10⁴ — CONJECTURED-free, standard.
- **Negative recorded:** the first GUE implementation (a prior /tmp draft, `semicdf` on the wrong
  support) produced a null with F̂ ≈ N at every α (all points collapsed to the window edge) —
  a code bug caught by the quantile-vs-Wigner calibration; discarded; the corrected recipe is in
  §2(b). This is recorded so no future agent reuses the broken draft.
- **Estimator identity caveat (INCONCLUSIVE):** the exact script behind verif-001 §4 does not
  survive; we use the standard periodogram F̂, which reproduces §4's qualitative description at
  N=3000 (CHECKED NUMERICALLY). The verdict is robust to the standard variants (all sit in the
  band; the band verdict is driven by the α-average, which is insensitive to ±O(1/N) estimator
  choices).
- Nothing in this note is a new theorem; the deliverable is a documented, code-backed negative
  that settles the empirical status of the beyond-1 trend as an estimator artifact.
- Sources: research/notes/verification-001.md §4; research/notes/attack-m29.md (theory closure);
  research/notes/idea-generator-games.md G3.1; tools/data/zeros_computed_10000.txt;
  tools/zeta-rs (zero computation); tools/probes_music_ling/, tools/probe_additive_b.py
  (prior sine-kernel/GUE usage patterns).
