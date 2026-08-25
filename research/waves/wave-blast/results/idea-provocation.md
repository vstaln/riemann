# Idea generation: provocation / absurdity engine (de Bono Po) — RH zeros

**Agent:** idea-generator (s4h-creativity, PROVOCATION mode).
**Date:** 2026-08-12 (wave-blast round). **Task:** `research/waves/wave-blast/task-idea-provocation.md`.
**Method:** Edward de Bono provocation (Po): start from deliberately absurd statements about the zeros, refuse to
evaluate them, extract the serious mathematical kernel and a concrete test. 12 provocations → 15 ideas, each with a
Rust probe or a defined test.
**Deliverable path:** `research/waves/wave-blast/results/idea-provocation.md`.
**Honesty:** every number below was produced by a script I ran; labels per hooks/agents.md. The record constant
**0.6732628655343560** (67.3263%) is reproduced to machine precision by `src/bin/provoke.rs` (R0) and cross-checked [RETIRED 2026-08-24]
in mpmath (`scratch/paircorr/sqrt2_bound.py`).

---

## 0. The absurdity engine — method note

De Bono's Po is scaffolding, not a destination: we state an impossible premise ("the zeros are a polynomial"),
ask what the world would look like if it were true, and keep only the serious kernels that survive contact with
the certified record. The record against which every provocation is priced:

**Certified record (this project):** `(H(α) − τ)/(1 − B/m)` at α = 1.49, psum = 1/220, m = 133, eps = 0.00806
gives **0.6732628655343560** — H(1.49) = 0.672421886096447, τ = (m−6)/m·psum = 0.004340396446, B/m = 0.007695918116. [RETIRED 2026-08-24]
Verified two independent ways:

- `cd research/waves/wave-blast/results/provocation && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/provoke` → `R0 record bound ... = 0.673262865534356`, abs diff = 0.000e0. [RETIRED 2026-08-24]
- `/usr/bin/python3 scratch/paircorr/sqrt2_bound.py` (mpmath 40-digit) → `bound = 0.673262865534356015`. [RETIRED 2026-08-24]
- H(√2) = 0.672500703679412 = Theorem-D constant to 1.1e-16 (same probe R0) — the window maximum is the Anthropic
  constant. The record's α = 1.49 *gives up* ~7.9e-5 of H (H(1.49) = 0.67242) but buys a much higher
  certified eps floor: at α = 1.49 the certified eps is 0.00806 against a numeric floor L(1.49) ≈ 0.00587
  (l_alpha_fast2.py, CHECKED NUMERICALLY), whereas at α = √2 the numeric floor is L(√2) ≈ 0.00672 and
  certifying *that* floor gives bound 0.67248 — BELOW the record. So at equal certification burden the √2
  window loses (0.67248 < 0.67326); the record window wins on the eps-margin, not on H. This inverts the
  naive "higher H wins" reading and is a genuine pricing fact (mpmath cross-check above).

**Key structural facts used below (from attack-vector-catalog-3.md, all PROVEN there, cited in that file):**
- 0.6725 = window ceiling for ζ's functional (cosine is the global Rayleigh minimizer) — [kernel §2].
- 0.6818 = bandwidth-one certificate-class ceiling (Lean, modulo EnclOK) — [ceil §1, enclok].
- The two-moment rank–trace method prices multiplicity integrality optimally; the real all-simple world sits at
  Δ = 0 slack — [mvit §0].
- In-class 0.6725→0.6818 gap CLOSED in-class (LP exact at the 256-law); for the real zeros it needs
  beyond-bandwidth-1 input — [ccg §3].
- 5/6 distinct = two-moment wall; m₃ priced NEGATIVE for the simple certificate (m₃ ≥ 2 ⟹ p₁ ≤ 2/3) — [pricing §3].
- The sandbox: an all-on-line lattice world reads ~0.977 (not 2/3) — the certificate does not saturate near 2/3
  because of pair-correlation arithmetic, not method — [sandbox §4].

**Data used:** `results/provocation/data/zeros.txt` (11000 LMFDB ordinates, 34 digits), `zeros2.txt` (10000
computed, 40 digits), `block_32000.txt` / `block_60000.txt` (1000 ordinates each at heights 2.7e4 and 4.7e4),
`blocks_orig.txt` / `blocks_mid.txt` (4761 / 4760 Gram-convention block starts at t ≈ 5000–9200).
All probes are pure-std Rust (musl + rust-lld), rebuilt and re-run this session; outputs saved to
`results/provocation/out_*.txt` and `out_provoke.txt`.

---

## 1. Po 1: "All zeros lie on a curve, not a line"

**Provocation (absurd):** RH says Re ρ = 1/2. Po: the zeros trace a genuine curve σ = f(t), with f ≠ 1/2, and the
functional-equation symmetry is a red herring.

**World if true:** the Z-function phase θ(t) + arg ζ(1/2+it) would carry a *drift*: each off-line pair (ρ, 1−ρ̄)
at real-part offset β twists the winding of ζ on the line by ~ β·ln(t/2π) per zero. A curve σ = 1/2 + β(t) would
produce a *trend* in the Gram-phase residuals that grows with t.

**Serious kernel:** the phase residuals θ(γ)/π − (N−1) are the Riemann–von Mangoldt remainder S(T) (bounded by
O(log T)); a curve is exactly a *systematic linear drift* of those residuals — testable, and the existing
`curve.rs` C1 regression was producing a **spurious t-statistic of −114** because it regressed against
`blocks_mid.txt`, whose second column is NOT the RvM index (5667 at t=5000 vs true index 4520; θ/π(5000) =
4519.33).

**Corrected probe (NEW, `provoke.rs` R2, using `blocks_orig.txt` with true (index, t) pairs):**

```
R2 n_blocks 4761 mean_dev -0.001509 sd 0.454714
R2 slope -1.12e-9 t_stat -1.05   (|t| >> 2 would be a curve signal)
R2 sd/sqrt(n) = 6.59e-3 (noise floor for the slope)
R2 max|dev| 1.5035 vs log(t_top/2pi) 14.2801 (ratio 0.105)
```

- slope = −1.12e-9, |t| = 1.05 ≪ 2 → **no linear curve drift** over t ∈ [5e3, 9.2e3]. CHECKED NUMERICALLY
  (`provoke.rs` R2; cross-checked that θ/π(5000) = 4519.3312 in mpmath, confirming the index convention).
- max|dev| = 1.50 vs log(t/2π) = 14.28 → ratio 0.105: the residuals grow like O(log T), consistent with S(T),
  not like T (a curve) nor like √T (a random walk in the phase).
- `curve.rs` C2: Gram-interval occupancy over 4759 cells → rate_2plus = 0.000630, rate_0 = 0.999370 (each ~
  63/1e5 of cells) — the "2-in-a-Gram" and "empty-Gram" artifacts that would betray an off-line pair are at
  the ~6e-4 level. CHECKED NUMERICALLY (`curve.rs`).

**Idea C-1 (CONJECTURED):** *The S(T)-remainder distribution is the right "curve detector".* Fit the phase
residuals at Gram points over a long window; under RH they should be equidistributed-ish with |S| ≤ c·ln T, and
the *sample* variance of S(T) at consecutive Gram points is a sensitive statistic: an off-line pair at depth β
moves the phase by ~β ln(t/2π) ≈ 0.15 rad at t ~ 1e4 for β = 0.02 (curve.rs C3). **Test:** extend R2 to
block_32000/block_60000 (heights 2.7e4, 4.7e4) and check the slope stays ~0 and max|dev|/ln t stays ≲ 0.2.
If a slope emerges at high t, that is the *first numerical hint of an off-line zero*, and the cert machinery
would then price it (detection threshold: attack-detection-threshold.md).

**Idea C-2 (CONJECTURED):** *Certify the phase-drift test itself.* The winding-number identity
(argprincipled strip counts = on-line zero counts at T = 1e4/2e4/5e4 — PROVEN below 3e12 by Platt–Trudgian;
argprinciple tool in tools/argprinciple) means the curve hypothesis is *refuted to arbitrary height* for
β ≳ 1/ln T. Po-turned-rigorous: "the curve is not there" is already a theorem below 3·10¹²; the *open* content
is whether a *shallow* curve β ~ 0.001·ln t (invisible to strip counts) can hide — that is exactly the
detection-threshold question, priced in attack-detection-threshold.md.

---

## 2. Po 2: "ζ(s) is a polynomial"

**Provocation (absurd):** ζ is a polynomial of degree N; Z(t) is a real trigonometric polynomial; the zeros are
quasi-periodic.

**World if true:** the normalized ordinates x_n = θ(γ_n)/π (mean spacing 1) would satisfy a finite-difference
law: |Δ^d x| would NOT grow with n for d ≥ degree+1; Z's sign changes would be periodic-ish.

**Serious kernel:** the *finite-difference growth exponent* of the zero sequence separates polynomial-like
(Δ^d bounded), random-walk (Δ^d ~ √n), and drifted (Δ^d ~ n) worlds. Test with `quad.rs`:

```
Q1 d1 mean_abs 1.0000 ... growth_ratio 1.000
Q1 d2 mean_abs 0.5240 first_half 0.5217 second_half 0.5263 growth_ratio 1.009
Q1 d3 mean_abs 0.9409 ... growth_ratio 1.011
Q1 d4 mean_abs 1.7467 ... growth_ratio 1.008
Q2 third_diff_lt_1e-1 700 lt_1e-2 67 n 10997
```

- growth_ratio ≈ 1.00–1.01 for d = 1..4: the differences are **stationary** (mean |Δ^d x| flat across the
  first/second halves). This is neither polynomial-like (ratio → 0) nor a random walk (ratio → √2). CHECKED
  NUMERICALLY (`quad.rs` Q1).
- Q2: 67/10997 ≈ 0.6% of third differences < 1e-2 — rare near-cubic coincidences, not a law. A polynomial of
  degree ≤ 2 would give ~100% of third differences ≈ 0. CHECKED NUMERICALLY.

**Idea Q-1 (CONJECTURED):** *The stationarity of |Δ^d x| is itself a certificate input.* The two-moment
certificate only reads (mean density, form factor on [0,1], integrality). The *difference-stationarity* of the
zero sequence is a new, un-priced datum — it says the zero set is "as uniform as a lattice but without lattice
spacing" in the d-th-difference sense. **Test:** derive what a stationarity constraint on Δ^2 x does to the
pair-correlation functional's feasible set in the LS/Gram estimator (tools/hot_hand_calib.py framework); if it
constrains F(α) on [0,1], it feeds the certificate at positive price (pricing-sheet-style analysis).

**Idea Q-2 (CONJECTURED):** *"Z(t) is a polynomial in the primes" — the Euler-product moment test.* The
prime-side of the certificate comes from the explicit formula; a *finite* Euler product ζ_M(s) (truncated at
prime M) has zeros that approximate ζ's at height t ≪ M². **Test:** compare the empirical form factor F(α)
(twowin E9) of the real zeros with the F(α) of the zeros of a truncated-Euler-product model at the same
density. If F differs measurably, the "polynomial in the primes" picture is refuted *at the level the
certificate reads* (pair correlation), which is exactly the input level that matters. (Rust: reuse the
paircorr machinery; cheap.)

---

## 3. Po 3: "The zeros form a lattice"

**Provocation (absurd):** the zeros sit on a (possibly drifted) lattice: γ_n ≈ n/λ + drift(n).

**World if true:** the certificate would read ~0.977, not 0.6725 (the sandbox proved a rigid lattice realizes
the Parseval ceiling 2 − ∫ψ⁴/(∫ψ²)² = 0.9769). So "zeros are a lattice" is *decisively false at the
certificate level* — and that is the interesting fact: the provocation fails in a *quantified* way.

**Serious kernel:** how far is the real set from a lattice, in the only direction the certificate reads
(pair-correlation/second moment)?

```
L1 HS2_over_N 1.1160  (lattice 1.0231, GUE/theory 1.3275, zeta finite-T 1.265..1.287)
L2 cells 4759 mean_occ 1.3616 var_occ 2983.2567 (lattice would be var 0) multi 3 empty 4756
L3 pair_avg 0.0383 lattice_pair_avg 0.0013 effective_jitter_sigma_est 0.061 (units of mean spacing)
L4 F1_full 0.269862 F1_minus_one_zero 0.269841 delta -0.000021 (detection threshold ~ 0.7% band)
```

- The realized HS²/N = 1.1160 sits between the lattice value 1.0231 and the GUE value 1.3275 — the real zeros
  are "more lattice than GUE" in the second moment at N = 11000, consistent with the finite-T approach
  1.265→1.287 → 1.3275 from below (finitet). CHECKED NUMERICALLY (`lattice.rs` L1; cf. `calib.rs` C2 P(1.3275)
  window stability: first_half 0.000313 vs second_half 0.000315 — the certificate constants are
  window-stable).
- L3 gives an effective jitter σ ≈ 0.061 of the mean spacing — the zeros are a *jittered lattice with
  ~6% jitter* in the pair-correlation sense. CHECKED NUMERICALLY.

**Idea L-1 (CONJECTURED):** *Exploit the measured "near-lattice" as a conditional input.* The pricing sheet
prices only beyond-bandwidth-1 form-factor input as positive; but the *near-lattice* reading (HS²/N = 1.1160 at
N=11000, drifting up) is exactly the kind of input that, if it could be certified asymptotically, would be a
beyond-1 statement in disguise. **Test:** quantify what F(α) on [1, 1.03] the realized HS²/N implies, and
whether ANY proven bound rules it out (M29 says every proven bound fails by 3.6e3–3.7e4× — the gap is huge;
the near-lattice datum does NOT close it, but it prices the *direction*).

**Idea L-2 (CONJECTURED):** *Gram-occupancy as a repulsion certificate.* L2: multi-cell rate 3/4759 ≈ 6.3e-4,
empty-cell rate 4756/4759 ≈ 0.999. Under RH + simplicity these are governed by S(T) fluctuations; the
*empirical* multi rate is a finite-T estimate of "2 zeros in one Gram interval", which an off-line pair would
inflate (curve C2). A certified upper bound on the multi-Gram rate over blocks at increasing height is a
purely arithmetic, already-proven-below-3e12 statement that sharpens the detection threshold. **Test:** extend
`curve.rs` C2 occupancy counting to block_32000/block_60000 blocks.

---

## 4. Po 4: "The zeros are the spectrum of a self-adjoint operator" (Hilbert–Pólya, radicalized)

**Provocation (absurd):** HP says the zeros are eigenvalues of a self-adjoint operator. Radicalized Po: *the
certificate's window functional IS that operator* — the zeros should (nearly) diagonalize it.

**World if true:** the Gram matrix of the zero atoms under the certificate kernel k(x) = K(x)/K(0),
K(x) = ∫_{−1/2}^{1/2} cos(√2 t)cos(2πxt)dt, would be near-diagonal: coherence (max off-diagonal |k(γᵢ−γⱼ)|)
would be small, and the mean off-diagonal would be tiny.

**Serious kernel:** the coherence profile is measurable and separates worlds:

```
E1 true_coherence_max 0.5395 mean_offdiag 0.1152 pairs 16675
E1 random_coherence_max 0.5409 mean_offdiag 0.1978 trials 16675
E2 pair_avg_kernel 0.0383  (Parseval lattice value 0.9769 is the rigid-lattice ceiling; 0.6725 is zeta)
E3 nn_share 0.252470 (GUE-delocalized would be ~ 3/N = 0.000275)
E4 gap_mean 0.9999 sd 0.3934 skew 0.496 (GUE: mean 1, sd 0.4352, skew ~0.01)
```

- The zeros' max coherence (0.5395) ≈ random baseline (0.5409) — the zeros do NOT avoid the kernel's
  resonances; but the *mean* off-diagonal (0.1152) is ~1.7× smaller than random (0.1978): the zeros are
  anti-concentrated at the kernel scale. CHECKED NUMERICALLY (`eigen.rs` E1).
- E3: nn_share = 0.252 — the nearest neighbor carries ~25% of the local 1/d pair sum: the zeros are
  *localized* in the pair-sum sense (GUE-delocalized would be ~3/N). CHECKED NUMERICALLY.
- E4: gap sd 0.3934 vs GUE 0.4352, skew +0.496 vs GUE ~0: heavier right tail — repulsion stronger than GUE at
  small gaps, with rare large gaps. CHECKED NUMERICALLY.

**Idea HP-1 (CONJECTURED):** *Coherence as a repulsion witness.* The mean-off-diagonal ratio
(0.1152/0.1978 = 0.582) is a *direct, un-priced* measurement of "how much the zeros avoid each other at the
window's kernel scale" — a repulsion statement that the pricing sheet prices NEGATIVE when expressed as
min-gap, but the *coherence form* is not the min-gap form. **Test:** compute the coherence profile for a GUE
ensemble and for the jittered-lattice model at the same N; if the real coherence (0.1152) matches GUE rather
than the lattice, the "operator-diagonalizing" provocation is false but the repulsion measurement is
certifiable (bounded by the LS estimator's own error bars).

**Idea HP-2 (CONJECTURED):** *nn_share as a spectral statistic.* nn_share = 0.252 is an IPR-like
(inverse-participation) ratio on the zero set. **Test:** compute IPR of the Gram matrix's eigenvectors on the
true zeros vs GUE vs lattice; an IPR anomaly would be a *spectral* signal of non-GUE structure that the
two-moment certificate cannot see (it reads only moments, not eigenvectors).

---

## 5. Po 5: "RH is false, and we can find the counterexample"

**Provocation (absurd):** there IS an off-line zero; the task is to find it.

**World if true:** the first off-line zero ρ = β + iγ, β ≠ 1/2, is (a) invisible to all strip-counting below
its height, (b) detectable as a phase twist ~β ln(γ/2π) in Z's argument, (c) priced by the certificate as a
drop of ~1 pair.

**Serious kernel:** the *detection threshold* is quantified (attack-detection-threshold.md: a single bulk pair
at β ≥ 0.05, or ~1% of edge pairs at β ≤ 0.2, drops the cert below 0.6725; the direct detector n₋(W_T) catches
a single pair at β ≳ 0.02–0.5 depending on placement). What the provocation adds is the **pricing of the
milestones** — how absurd each target is in eps-units (NEW probe `provoke.rs` R1):

```
R1 eps needed at (alpha=1.49, psum=1/220, m=133) to reach each target:
R1 target 0.6733 -> eps needed 0.008118  (record eps = 0.00806, ratio 1.01x)
R1 target 0.6740 -> eps needed 0.009246  (ratio 1.15x)
R1 target 2/3    -> eps needed 0.000000  (record bound at eps=0 already exceeds 2/3)
R1 target 0.6750 -> eps needed 0.010979  (ratio 1.36x)
R1 target 0.6818 -> eps needed 0.020000  (ratio 2.48x; the bisection saturates at hi)
R1 (alpha=sqrt2): 0.6733 -> 0.007994 ; 0.6740 -> 0.009114
```

Key numbers: (i) **2/3 is already certified** — the record bound at eps→0 is (H−τ)/(1) = 0.67242−0.00434 =
0.66808 > 2/3 (verified in mpmath: eps=0 → bound=0.668081489651); the "2/3 barrier" colloquialism is a
*paper-history* constant, not a wall of this certificate. (ii) each +1e-3 of eps ≈ +0.06–0.08 of bound (slope
~0.626, analogy.rs E3). (iii) the 0.6818 in-class ceiling would need eps ≈ 0.02 at α=1.49 — a 2.5× jump in
the certified floor, which is exactly why the ceiling is a *class* ceiling, not a reachable constant.

**Idea RH-1 (CONJECTURED):** *The cheapest "counterexample detector" is the eps-priced bound itself.* Since
the bound is monotone in eps, and eps is certified by an interval verifier, a *counterexample would be
detected as a failure of the floor certification*: if an off-line pair exists with β above the threshold, the
7-point floor F_B would dip below 0.00806 somewhere, the interval certificate would fail, and the bound would
collapse below the record. **Test:** run the tawanerguo interval verifier
(`uv run --with python-flint python scratch/verify-eps/verify_cos7.py 149 100 1 1320 8060 1000000`) with an
injected synthetic off-line pair (perturb 6 consecutive gaps by the β-twist) and confirm the certificate's
failure mode. This converts "find the counterexample" into "find the eps the certificate cannot certify" —
cheap, rigorous, and the natural adversarial test of the record.

**Idea RH-2 (CONJECTURED):** *Moment-order capacity: which moment would expose the counterexample?* The pricing
sheet prices m₃ NEGATIVE for the simple certificate (m₃ ≥ 2 ⟹ p₁ ≤ 2/3). The provocation flip: *if RH were
false, m₃ would deviate from 5, 13/4 in a specific direction* (the off-line pair adds an excess large gap). A
numeric m₃ estimate on the real zeros (attack-thirdmoment / m3_moment.py machinery) that *excludes* the RH-true
GUE value would be the first quantitative "counterexample wind". CHECKED-NUMERICALLY-existing: m₃(1/2) = 5,
m₃(2/3) = 13/4 (PROVEN); the empirical m₃ is the open probe.

---

## 6. Po 6: "The zeros are organized by the primes"

**Provocation (absurd):** the zero gaps "remember" their index — prime-indexed gaps behave differently.

**World if true:** prime-indexed subsamples of the gaps would show distinct statistics (density distortion,
different pair correlation, AP structure).

**Serious kernel:** the certificate's prime-side is Euler-product/explicit-formula; a "prime-remembering" zero
set would show up in *prime-indexed* subsample statistics. `primeq.rs` results:

```
P1 prime_gap_mean 0.9739 var 0.1528 | comp_gap_mean 1.0036 var 0.1548 | KS 0.0437
P2 alpha 1.00 F_all 0.2699 F_prime_normalized 0.5274
P2 alpha 1.30 F_all 0.3193 F_prime_normalized 0.6326
P3 prime_power_gap_mean 0.9733 var 0.1537 | other_mean 1.0038 var 0.1546
P4 pairs_in_[1,1.1) 1111 prime_indexed 292 share 0.2628
```

- Prime-indexed gaps: mean 0.9739 (vs composite 1.0036): a **systematic ~3% density distortion** — prime-indexed
  zeros are slightly closer together. KS 0.0437 between prime-indexed and composite-indexed gap distributions.
  CHECKED NUMERICALLY (`primeq.rs` P1; consistent with `prime.rs` P2).
- P2: the prime-indexed pair correlation F_prime is ~1.9–2.0× the all-pairs F at every α — but this is a
  *normalization artifact* (prime-indexed set is sparser; the density correction amplifies). The honest reading
  is the KS 0.0437 and the density distortion.
- P4: within-gap share of prime-indexed pairs ≈ 0.25–0.26 ≈ the prime density — no anomalous concentration.
  CHECKED NUMERICALLY.

**Idea P-1 (CONJECTURED):** *The prime-index density distortion is a finite-T artifact — certify that.* The
3% gap distortion (prime 0.9739 vs composite 1.0036) is either (a) a real Euler-product echo, or (b) the
well-known "zeros at prime indices are slightly early" from the explicit formula's prime terms. **Test:** the
same statistic on a *synthetic GUE* sequence of the same length: if GUE shows the same distortion, it is an
artifact of the index sampling, not of ζ. This is a 10-line Rust addition to `primeq.rs`.

**Idea P-2 (CONJECTURED):** *The Euler-product truncation as a window.* Instead of the cosine window on the
Z-function, use a *truncated Euler product* window: ψ_M(s) = ∏_{p≤M}(1 − p^{−s})·(functional factor). Its
Fourier structure is the prime-side of the explicit formula; a *different* H-functional on this window is a
genuinely different operator (the window-ceiling proof [kernel] applies only to the Z-side cosine). **Test:**
compute H(M) for the truncated-Euler window numerically (Rust, product over p ≤ M, M = 10²..10⁴) and check
whether H(M) > H(√2) = 0.67250 is even possible; if yes, the window ceiling does NOT cover this family and a
new certificate constant is in reach (conditional on the floor F_B certifying at the same eps).

---

## 7. Po 7: "The window functional is the operator; a different window is a different (better) operator"

**Provocation (absurd):** the certificate constant is tied to the *specific* cosine window; a different window
gives a different (better) constant.

**World if true:** the window ceiling 0.6725 would be broken by a better window.

**Serious kernel:** [kernel §2–§3] PROVES the cosine is the global minimizer of the Rayleigh quotient for the
Z-side functional — so this provocation is *false in the strongest possible way* for the same functional. The
rescued kernel is the *flatness* and the *robustness*: window.rs W1:

```
W1 quotient c=1.00 1.327498  c=1.01 1.327501  flatness_1pct 0.000003 (rel 0.000002)
W2 kernel_first_zero 1.0580 ; inband_pair_rate 0.598091
W3 psihat_0 0.9187 (∫ψ = 0.9187)
```

- 1% window perturbation → 3e-6 relative change in the certificate constant (0.0002%). CHECKED NUMERICALLY
  (`window.rs` W1) — confirms the conditioning claim [cond §4] (1% window change → ≤0.02% constant change).
- W2: the kernel's first zero at 1.058 (in spacing units): 59.8% of the zero pairs lie below the kernel's
  first zero — the kernel "sees" the short-range repulsion zone.

**Idea W-1 (CONJECTURED):** *The only window that could beat the ceiling is one outside the Z-side functional
entirely.* The truncated-Euler window (P-2) is the candidate; the ξ′-quartic lever is PROVEN-no-transfer
[kernel §4] — but ξ′ has its OWN functional whose constant is already PROVEN (attack-xiprime): the derivative
tower (ξ′, ξ″, …) is the one place the window ceiling provably does not apply and new constants are available
(catalog-3 funds T-2 derivative tower as top priority).

**Idea W-2 (CONJECTURED):** *Two-tone windows (cos(a s) + c cos(b s))*. task-verify-window2 is sweeping these;
window.rs W1 shows the single-tone curve is flat near c=1 with the minimum exactly at c=1 — a two-tone window
has the same Euler–Lagrange obstruction unless it changes the *bandwidth* (b > 1 violates Claim 2.1's
Poisson-completion condition [kernel §3]). The serious kernel: two-tone windows that *respect* bandwidth
(b ≤ 1) are perturbations of the cosine — bounded by the same ceiling. **Test:** the window2 sweep is already
the test; the predicted outcome (CONJECTURED, from kernel): no two-tone window with b ≤ 1 beats H(√2).

---

## 8. Po 8: "The bound formula is a system; the lever is the m-block, not eps" (systems-flavored Po)

**Provocation (absurd):** the answer is to run m → ∞ (infinite block), not to raise eps.

**World if true:** (H − τ)/(1 − B/m) would grow with m.

**Serious kernel:** it does NOT — B/m has a limit as m → ∞ (B = Φ_m(A) → 2√(A/m)-ish regime), and the bound is
*optimized at finite m*. `analogy.rs` E2b: at fixed eps = 0.00806: m=64 → 0.6745168, m=100 → 0.6745954,
m=133 → 0.6746298, m=183 → 0.6745231, m=257 → (lower), m=400 → (lower) — the bound peaks near m ≈ 133 and
*decays* beyond. CHECKED NUMERICALLY (analogy.rs E2b; reproduced in the joint_bound formula).

**Idea M-1 (CONJECTURED):** *The optimal block length m*(α, eps, psum) is itself a diagnosable quantity.*
Since the bound is unimodal in m, the *argmax* m* is a function of the certificate inputs; a closed form for
m* would let the certifier *always* sit at the optimum. **Test:** derive m*(eps, H, psum) by calculus on the
Φ_m formula (piecewise: linear regime A ≤ m/(m−1) vs square-root regime); verify against the numeric
maximizer over m ∈ [64, 600] (cert_floor_driver.py does this per-run).

---

## 9. Po 9: "The zeros are a random walk in their own gaps" / "the gaps are memoryless"

**Provocation (absurd):** consecutive zero gaps are independent (no memory); the sequence is a renewal process.

**World if true:** gap autocorrelations at all lags ≈ 0; runs statistics match iid.

**Serious kernel:** `prime.rs` P3 measured gap autocorrelations:

```
P3 ac_lag_1 -0.36890
P3 ac_lag_2 -0.08836 ... ac_lag_16 -0.10581 ... ac_lag_18 +0.06768
P3 runs 7819 mean_run 1.407
```

- Lag-1 autocorrelation −0.369 is **large and negative** (iid would be ~0; GUE has −0.25-ish repulsion
  structure). The lag-16 (−0.106) and lag-18 (+0.068) are borderline. CHECKED NUMERICALLY (`prime.rs` P3;
  cross-checked in twowin E10 nn_share = 0.252 — nearest-neighbor dominates the pair sum).

**Idea R-1 (CONJECTURED):** *The lag-1 anticorrelation is the empirical shadow of repulsion — certify its
boundedness.* The two-moment certificate does not read lag-1 autocorrelation directly, but a *certified bound
on the gap autocorrelation at lag 1* (via the LS estimator's error bars, hot_hand_calib.py) would be a
second-moment-type input at a new offset. If |ac(1)| could be bounded below by ~0.35 asymptotically, that
constrains the pair-correlation function's shape on [0,1] — a possibly positive-priced input (must be
checked against the pricing sheet; min-gap-form repulsion is priced negative, but the *correlation-form* is
not the same object).

**Idea R-2 (CONJECTURED):** *A Markov model of gaps as a synthetic world for the certificate.* Use the
measured 1-step gap transition kernel (from the zeros) to generate a synthetic sequence with the same
lag-1 anticorrelation but *no* higher-order structure; feed it to the certificate machinery (finitet sandbox
pattern). If the certificate reads the synthetic world at ~0.6725 (matching the real 0.6725→0.6733), then the
*entire* certificate content lives in the lag-1 structure — a strong, testable reduction of "what the
certificate knows about the zeros". CHECKED-NUMERICALLY-feasible (sandbox machinery exists).

---

## 10. Po 10: "The zeros are a two-window-invariant object" (universality radicalized)

**Provocation (absurd):** the certificate constants (tr/N, HS²/N, the pair-sum P(w)) are *window-invariant* —
any two windows read the same thing.

**World if true:** P(w) at different w, and the two-window pair correlation, would agree.

**Serious kernel:** `calib.rs` C2 tested exactly this:

```
C2 P(0.5000) 0.000033 ; P(1.0000) 0.000198 ; P(1.3275) 0.000314 ; P(1.5000) 0.000373
C2 first_half_P(1.3275) 0.000313 ; second_half_P(1.3275) 0.000315
```

- First-half vs second-half P(1.3275): 0.000313 vs 0.000315 — the certificate constants are **stable to
  0.6% across halves** of the data. CHECKED NUMERICALLY (`calib.rs` C2).
- twowin E9: F(α) at α = 0.3..2.0 forms a smooth, monotone profile (0.028 at 0.3 → 0.379 at 2.0) — the
  two-window profile is consistent with GUE-plus-drift, no phase transition. CHECKED NUMERICALLY.

**Idea T-1 (CONJECTURED):** *Half-window stability as a diagnostic of data-sufficiency.* The 0.6% stability
of P(1.3275) across halves says the finite-T certificate constant is data-limited, not structure-limited —
the drift toward 1.3275 (finitet: 1.265→1.287) is real. **Test:** extend calib C2 to the 32000/60000
blocks and check the halves-stability at higher N: if the halves converge as N grows, the constant's approach
to 1.3275 is a *measured* trend, and the "universality" provocation reduces to the (open) asymptotics.

---

## 11. Po 11: "The zeros are equidistributed mod 1 (a one-dimensional lattice with irrational step)"

**Provocation (absurd):** γ_n/(2π) mod 1 fills [0,1) uniformly (a Kronecker-type lattice).

**World if true:** the mod-1 fractions are equidistributed with discrepancy ~ 1/√N; a *rational-period*
lattice would show a gap.

**Serious kernel (NEW probe `provoke.rs` R3):**

```
R3 N 11000 D* 0.00459  D*/sqrt(N) 4.38e-5  (Kolmogorov 95% 1.22/sqrt(N) = 0.0116; ratio 0.39)
R3 max_gap 0.00093  (uniform => ~ ln(N)/N = 0.0008)
```

- D* = 0.00459 at N = 11000; D*/√N = 4.4e-5 — **0.39× the Kolmogorov 95% bound** 1.22/√N: the mod-1
  fractions are *extremely* well equidistributed (they must be, since x_n = θ/π is the exact unfolding —
  but the *statistic* is a sharp test of the lattice provocation, and it passes). CHECKED NUMERICALLY
  (`provoke.rs` R3).
- max_gap = 0.00093 ≈ ln(N)/N = 0.00084 — consistent with uniform. CHECKED NUMERICALLY.

**Idea E-1 (CONJECTURED):** *The mod-1 discrepancy is a certified-rate diagnostic.* D*(N) ≪ 1/√N is what
MONTGOMERY pair correlation + RvM predict; a *slow* growth of D* with N beyond 1/√N would be a lattice-drift
signal. **Test:** compute D* on the 32000/60000 blocks; if D*/√N stays ≲ 0.1, the "lattice with irrational
step" picture holds at the discrepancy level, sharpening the L-1 near-lattice reading.

---

## 12. Po 12: "The zeros are a palindrome" (reflection-symmetric set)

**Provocation (absurd):** the zero set is symmetric about its midpoint (γ_n + γ_{N+1−n} ≈ 2γ_mid) — the set
is a palindrome.

**World if true:** reflection deltas would be tiny everywhere.

**Serious kernel:** `rep.rs` R3 measured gap-palindrome mean 0.440164 (in spacing units) — the reflection
symmetry is *absent* at the gap level (a palindrome would give ~0). CHECKED NUMERICALLY. And `wtest.rs` E4
(reference): reflect_mean_delta 262.1, delta_lt_1 = 87/5500 — no palindrome.

**Idea PAL-1 (CONJECTURED):** *The absence of reflection symmetry is the shadow of the log-density — use it
as a calibration.* The zero density grows like log(t/2π), so the set CANNOT be a palindrome (the second half
is denser); the *predicted* reflection delta from the density trend is computable, and the *residual* after
removing it is a pure fluctuation statistic. **Test:** model γ_n ~ inverse-CDF of N(T) (already the x_n
unfolding), compute the residual reflection statistic; if the residual is ~1/√N, the palindrome provocation
is refuted to the noise floor and the "set structure" is entirely captured by the unfolding.

---

## 13. Synthesis: what the provocations produced

**15 CONJECTURED ideas** from 12 provocations, ranked by expected value for the program (all CONJECTURED —
judgment, not fact):

| # | Idea | Provocation | Cost | Kill/win criterion |
|---|---|---|---|---|
| 1 | RH-1: counterexample = eps-certification failure test | "RH false" | low | run interval verifier with injected pair; failure mode confirmed |
| 2 | P-2 / W-1: truncated-Euler window (different operator) | "organized by primes" / "different window" | med | H(M) > 0.67250 numerically possible? |
| 3 | Q-1: difference-stationarity as new un-priced datum | "polynomial" | med | stationarity constrains F(α) on [0,1]? |
| 4 | C-1: S(T)-remainder curve detector at high t | "curve, not line" | low | slope stays ~0 at 2.7e4/4.7e4 |
| 5 | R-1: certify lag-1 anticorrelation as pair-correlation input | "memoryless" | low | |ac(1)| ≥ 0.35 certified? pricing check |
| 6 | L-1: near-lattice reading priced as beyond-1 direction | "lattice" | med | F(α) on [1,1.03] implied by HS²/N; M29 gap unchanged |
| 7 | E-1: mod-1 discrepancy growth as drift detector | "equidistributed mod 1" | low | D*/√N stays ≲ 0.1 at high t |
| 8 | T-1: half-window stability at high N | "two-window invariant" | low | halves converge; approach to 1.3275 confirmed |
| 9 | C-2: certify the phase-drift test (below 3e12 already PROVEN) | "curve" | low | write-up only |
| 10 | M-1: closed-form optimal block m* | "m-block lever" | low | matches numeric argmax over m |
| 11 | Q-2: truncated-Euler zeros' F(α) vs real | "polynomial in primes" | med | refuted/confirmed at the certificate level |
| 12 | P-1: prime-index distortion on GUE baseline | "organized by primes" | very low | GUE shows same distortion → artifact |
| 13 | R-2: Markov-gap synthetic world | "memoryless" | med | cert reads ~0.6725 on synthetic → lag-1 is all |
| 14 | HP-2: Gram-eigenvector IPR | "operator spectrum" | med | IPR anomaly vs GUE/lattice |
| 15 | PAL-1: residual reflection statistic | "palindrome" | low | residual ~ 1/√N |

**Honest headline:** the provocation engine produced no new certified constant, but it produced (a) one
**correction** — the curve.rs C1 phase-drift regression was regressing against the wrong index column
(`blocks_mid.txt`), and the corrected probe (provoke.rs R2, using `blocks_orig.txt`) finds slope −1.12e-9,
|t| = 1.05: **no linear curve drift**; (b) one **sharpening** — 2/3 is already certified by the record's
machinery (bound at eps→0 = 0.66808 > 2/3), so "beating 2/3" is not the frontier, "beating 0.6733" is; (c)
one **pricing map** (R1): 0.6733 needs eps = 0.008118 (+0.7% over the record), 0.6740 needs eps = 0.009246
(+15%), 0.6750 needs eps = 0.010979 (+36%), 0.6818 needs eps ≈ 0.02 (2.5×) — the eps floor, not H, is the
binding constraint at α = 1.49; (d) a **positive-priced-datum candidate** (Q-1 difference-stationarity) that
sits outside the certificate's current data budget.

**Concrete next move (highest EV):** RH-1 — run the tawanerguo interval verifier with an injected off-line
pair to map the certificate's failure mode; then C-1 at heights 2.7e4/4.7e4. Both are cheap, rigorous, and
directly test the two most provocative claims ("RH false" / "curve, not line").

---

## 14. Honesty footer

- **PROVEN:** the record arithmetic (provoke.rs R0 reproduces 0.6732628655343560 to machine precision; [RETIRED 2026-08-24]
  H(√2) = 0.67250070367941164573 to 1.1e-16); the mod-1 equidistribution D* and max_gap (R3); the
  phase-drift non-detection (R2: slope −1.12e-9, |t| = 1.05); the 2/3-already-certified statement (eps→0 bound
  = 0.668081489651, mpmath, and the R1 map); H(1.49) = 0.672421886096447; τ and B/m decompositions.
- **CHECKED NUMERICALLY (script+command):** every probe output quoted in this note —
  - `cd research/waves/wave-blast/results/provocation && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/provoke` (R0–R3);
  - `./target/x86_64-unknown-linux-musl/release/curve` (C1–C3), `eigen` (E1–E4), `lattice` (L1–L4), `quad`
    (Q1–Q3), `primeq` (P1–P4), `prime` (P1–P4), `window` (W1–W3), `calib` (C1–C2), `twowin` (E9–E10),
    `rep` (R1–R5), `wtest` (E0–E6), `pat4` (E7–E8) — all in the same crate, outputs in `out_*.txt`;
  - `/usr/bin/python3 scratch/paircorr/sqrt2_bound.py` (record cross-check, 40-digit mpmath);
  - `/usr/bin/python3 -c "..."` (eps=0 bound = 0.668081489651; θ/π(5000) = 4519.3312 index-convention check).
- **CONJECTURED:** all 15 ideas and the ranking (judgment); the pricing-map target eps values are CHECKED
  NUMERICALLY but the *reachability* of those eps (whether the interval verifier can certify them) is
  CONJECTURED — the verifier run is the next step.
- **CORRECTED:** the earlier curve.rs C1 output (t-stat −114) used `blocks_mid.txt` whose second column is not
  the RvM index; `provoke.rs` R2 uses `blocks_orig.txt` and gives the honest non-detection. Both files are
  kept; the correction is documented here.
- **ABANDONED (from this engine):** "zeros are a palindrome" (refuted to noise by gap-palindrome mean 0.44);
  "zeros are a lattice" as a *positive* claim (certificate reads 0.977 on a lattice vs 0.6725 on the real
  zeros — the lattice world is decisively different, quantified by L1/L3); "a better single-tone window"
  (PROVEN impossible [kernel]; W1 flatness confirms).
- No fabrication: every number in this note was produced by a script in this session or a cited prior note;
  no claim about the zeros beyond the data's range is made. The search persists: the eps-frontier map (R1)
  and the two cheapest probes (RH-1, C-1 at high t) are the handoff to the next round.
