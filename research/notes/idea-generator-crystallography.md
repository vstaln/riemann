# Idea Generator: crystallography/diffraction & astronomy/LSS attack catalog

**Agent:** IDEA GENERATOR (analogy-domain-transfer + creativity-brainstorm + constraint-rule-inversion; cross-domain round 2).
**Purpose:** feed the EXECUTIONER agents. Two previously-unmined experimental-science domains, 10 vectors each.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Physics/crystallography/astronomy facts
below are standard results named at the level of "standard in the field" — anything I cannot verify from the sources we
hold is labeled **reported standard — verify before use**. Every *idea* is CONJECTURED by construction and carries a kill
criterion. Labels: **NEW** (invented here, untested) / **KNOWN-OPEN** (core already flagged in our notes; new framing or
new procedure only) / **KNOWN-DEAD** (immediately reducible to a documented wall) / **TESTED-OPEN** (tested by our tools,
still open). Overlap discipline: crossdomain catalog = idea-generator-crossdomain.md **[CD-V#]/[CD-W#]/[CD-A#]**; physics
catalog = idea-generator-physics.md **[P#.#]**; attack notes **[AK]**=kernel, **[AC]**=ceiling, **[AM]**=multiplicity,
**[AF]**=finitet, **[AL]**=lfunctions, **[M29]**=attack-m29, **[Nev]**=attack-nevanlinna, **[LP]**=attack-lpdual.

**State of the art these vectors must respect (PROVEN, from our notes):**
- In-class: the bandwidth-one certificate class attains v\* = 0.68183123 = p₀ + |E(1)| (LP-dual, CHECKED NUMERICALLY [LP]);
  the two-moment MT certificate 0.6725 is strictly suboptimal *inside* the class; **no missing constraint exists inside
  bandwidth one**; the only datum that moves v is the certified simple fraction p₁ (shadow price 1) [LP].
- The wall: raising p₁ needs beyond-bandwidth-1 pair-correlation input (F(α), α>1) or a multiplicity constraint — both
  CONJECTURED/unavailable [AC][LP]. M29 (documented negative, PROVEN): every *unconditional bound* on the off-diagonal
  prime-pair sum at X = T^{1+ε} fails the O(1)-at-constant-scale tolerance by 3.6·10³–3.7·10⁴×; the only clearing inputs
  are *values* (HL / Montgomery pair correlation) — CONJECTURED. **M29 covers the *mean* of the pair sums only.**
- P2 (5/6 distinct wall): third moment m₃ ≥ 2 would exclude the 256-law (m₃(law) = 1.9545 < 2, CHECKED [Nev]) but m₃ ≥ 2
  is not provable (§7.5(e): RS range λ < 2/3 only; odd moments don't lower Λ₁(0) for the n₊ functional) [Nev][CD-V3][P6.5].
  The two-bandwidth joint certificate [P6.5] is the top proven-input P2 route and has been probed (tools/lp_twobandwidth.py).
- P6 (finite-T): Δ(T) = bound/N − 0.6725 > 0 at every tested T, ~1/log T, driven by the off-diagonal pair sum
  (offdiag/N ≈ 0.27–0.29 vs asymptotic c−1 = 0.3275) [AF]. Hard-cutoff cosine (C⁰, |z|^{−1} decay, O(1/K) truncation)
  vs the paper's C∞ window (|z|^{−2}, O(1/K²)): the smoothed-window run is [AF]'s own recommended next step.

---

# DOMAIN A — X-ray/neutron crystallography & diffraction

**Abstraction (no domain vocabulary).** We observe the *squared Fourier magnitudes* (intensities) of a positive point
measure on a bounded frequency band, and we want to constrain the measure's structure (how much of it is "atomic" with
integer weights on a line). The intensities are windowed and the window's shape (sharp vs smooth) distorts the readings in
a known, parameterized way. The missing information is the *phase* of the measure's Fourier transform outside the band.

That is literally the crystallographic phase problem: intensities |F(h)|² at measured reflections, unknown phases,
atomicity (nonnegative density with integer-ish weights) as the prior, and instrument-resolution (window) smearing as the
experimental reality. The domain-transfer moves below mine the *solution machinery* crystallographers built for exactly
this structure.

## A1. Karle–Hauptman determinants: the PSD Gram is automatic; the *triple-product bound* is the P2 price-list — NEW (framing + quantification; overlaps [P6.4], [CD-V3])
**Idea.** K–H (1950): for a nonnegative density, the matrix [E(h−k)] over any index set is PSD (Gram matrix of
Σⱼ fⱼ zⱼʰ z̄ⱼᵏ with fⱼ ≥ 0), and its 2×2/3×3 subdeterminants are the "Hankel-type inequalities on |F|²" of direct
methods. Mapped: our "density" is the zero multiplicity measure m_ρ ≥ 1 (positive integers — atomicity is *given*), the
"structure factors" E(α) = (1/N)Σ_ρ m_ρ e^{iαγ_ρ} are the *phase-bearing* first-order sums, and the certificate's rows
S(j) are the *intensities*. Two honest findings: (i) the K–H PSD is **automatic** for us — the phases E(α) at in-band
frequencies are *known prime sums* (explicit formula), so the Gram is PSD as a tautology (this is B24's F ≥ 0 in matrix
form). (ii) The *3×3* K–H determinant is not a tautology: it couples three intensities to the *triple correlation*
T(j₁,j₂,j₃) = Σ_ρ m_ρ e^{i(α₁−α₂+α₃)γ_ρ}-type sums via det ≥ 0 — a **provable upper bound |T| ≤ f(S(j₁),S(j₂),S(j₃))** on
the third-moment object *in terms of pair data alone*.
**Analogy to our setting.** Intensities ↔ S(j) rows (known); phases ↔ in-band E(α) (known prime sums); triple product ↔
tr Â³ (the P2 input, phase-carrying); the 3×3 K–H bound ↔ an admissible *range* for m₃ given the pair data.
**What it needs.** The 3×3 determinant inequality written for the *windowed* zero measure; the admissible range of m₃.
**Feasibility.** Med. **Value.** The crystallographic logic explains *why* P2's input is the third moment (it is the
lowest-order phase-carrying statistic — see A2), and the K–H bound gives a *quantified price*: solve the distinct-count
LP [P6.5] with m₃ ranging over the K–H-allowed interval and plot ceiling(m₃) — a roadmap exactly parallel to [P1.4]'s
ceiling(ε), but for the third moment, with the allowed range *provable* from pair data. If the K–H bound is so loose that
m₃ = 2 (GUE) is allowed, no constraint (expected — clean negative); if it *excludes* 2, the wall is provably unreachable
by *any* third-moment input — a documented finding either way.
**Probe (<1h):** mpmath: for the 256-law's S(j) rows, write the 3×3 K–H determinant, maximize |T| over phases; report the
implied m₃ range vs the GUE value 2 vs the law's 1.9545.

## A2. Sayre equation / tangent formula: the third moment is the *connected* (phase-carrying) part — and the Sayre-residual diagnostic — NEW (diagnostic; overlaps [P3.1], [P9.4])
**Idea.** Direct methods live on the *triple product*: the Sayre equation F(h) ∝ Σ_k F(k)F(h−k) (convolution idempotence
of the density) and the tangent formula's structure invariants E(h)E(k)E(−h−k). The *generalized* statement that survives
for non-idempotent measures: the triple correlation factorizes as (pair-correlation products) + **connected part**, and
the connected part is exactly the phase-carrying piece. For a *crystal-like* configuration the connected 3-point
function is small/periodic; for the GUE/sine-kernel process it is a specific non-zero function (Dyson 1962 — reported
standard). Our tr Â³ is precisely the connected third moment.
**Analogy to our setting.** Sayre-residual Σⱼ|S(j) − Σₖ S(k)S(j−k)| ↔ a *phase-consistency* statistic of the zero
configuration: near-zero ⇒ crystal-like (factorizing); GUE-sized ⇒ disordered. The residual is computable from real zeros
at finite T — a *numerical shadow* of the P2 input before any theorem (same spirit as [P3.1]'s counting-skewness probe,
different statistic).
**What it needs.** The connected triple correlation (or its Fourier proxy) computed from cached/10⁴ zeros; the two
predictions (crystal ≈ 0; GUE = Dyson value).
**Feasibility.** Low–Med. **Value.** Decides empirically whether the third-moment route to 5/6 has any *signal*: if the
measured connected part is GUE-sized, the third moment is a live input (fund [P6.5]); if it is crystal-like, the data
are closer to the ceiling law than to GUE (bad news for the roadmap).
**Probe (<1h):** Rust/mpmath on cached zeros: compute Σⱼ|S(j) − Σₖ S(k)S(j−k)| for the windowed pair sums at T ≈ 200–600;
compare with the crystal (law) and GUE predictions.

## A3. Burg maximum-entropy spectral extrapolation: a *nonparametric* beyond-1 form-factor estimator — NEW (measurement tool for P3; overlaps [CD-V6], [P2.1])
**Idea.** Signal processing: given the first m autocorrelation lags, the *maximum-entropy* spectrum (Burg, 1967 — reported
standard) is the unique flat-extension consistent with the lags, computed by the Yule–Walker AR(m) fit; it is the
canonical *least-assuming* continuation beyond the measured band. Our S(j) rows *are* the first ~255 autocorrelation
lags of the windowed zero configuration.
**Analogy to our setting.** Autocorrelation lags ↔ S(j) rows; MEM spectrum ↔ a *default* prediction of F(α) for α > 1;
deviation of the *measured* beyond-1 F from the MEM prediction ↔ structure beyond the least-assuming continuation.
**What it needs.** Yule–Walker from the *measured* (noisy, windowed) rows; the MEM spectrum; comparison with the GUE
value F = 1 and with the empirical beyond-1 F (the [CD-V6] probe).
**Feasibility.** Low. **Value.** Two honest uses. (i) In the *near-CUE* limit the MEM is degenerate — an almost-flat
spectrum extrapolates flat — so it *confirms* F ≡ 1 as the least-assuming prior (a cheap check of the roadmap's base
assumption). (ii) On the *measured finite-T* rows the MEM *deconvolves* the window and extrapolates — a nonparametric
competitor to A/BAO template fitting (B3) for the empirical beyond-1 measurement. Diagnostic only — cannot enter a
certificate.
**Probe (<1h):** numpy/scipy Yule–Walker on the [AF]-style measured S(j) rows; plot the MEM spectrum vs F ≡ 1.

## A4. Debye–Waller / Wilson plot: multiplicative-envelope decomposition of the finite-T deficit — NEW (P6 decomposition; overlaps [P5.5]'s Fisher–Hartwig baseline, different procedure)
**Idea.** Crystallography: observed intensity = structure intensity × **Debye–Waller factor** e^{−2B(sinθ/λ)²} (thermal
smearing — smooth, *multiplicative*, damped at high angle), and the **Wilson plot** ln(I/⟨f²⟩) vs q² extracts B as the
slope. The Bragg-vs-diffuse split (sharp reflections vs smooth background) is the standard thermal/structural
separation.
**Analogy to our setting.** The finite-T deficit Δ(T) = bound/N − 0.6725 is the "observed-minus-structural" signal; the
*kernel artifact* (hard-cutoff C⁰ window vs C∞ [AF]) is the "thermal" (smooth, multiplicative, window-determined) part;
the *arithmetic* part (pair-correlation error, ~1/√log T per B24) is the "structural" (Bragg) part. A Wilson-plot-style
fit ln(S_meas(j)/S_ideal(j)) vs (j/N)² over the certificate rows separates the envelope slope (kernel smearing) from the
residual (arithmetic).
**What it needs.** The [AF] measured rows and ideal-model rows at several T; a log-envelope fit.
**Feasibility.** Low. **Value.** A clean, standard *procedure* for exactly the decomposition [P5.2]/[P5.5] call for, and a
checkable prediction: if the deficit is kernel-dominated, the envelope slope should scale with the window's second
moment; if arithmetic-dominated, it should scale like 1/√log T — directly informing the P6 error budget and the
smoothed-window run [AF] recommends.
**Probe (<1h):** fit ln(Δ(j)-structure) vs (j/N)² on existing [AF]/finitet data; report the slope's T-scaling.

## A5. Termination-error analysis / Lorch modification: the *exact* truncation-error law for step vs smooth windows — NEW (P6, direct transfer; supports [AF]'s smoothed-window recommendation)
**Idea.** Total-scattering (PDF) analysis: the pair distribution function is computed from a *truncated* intensity range,
and truncation produces **termination ripples** — the standard quantitative statement: a step (sharp) data cutoff at Q
produces O(1/Q)-amplitude sinc ripples in real space; the standard correction is the **Lorch modification** (smooth
window sin(πq/Q)/(πq/Q)) which suppresses the ripples at the cost of resolution (Lorch 1969 — reported standard). This
is *exactly* our window question: the hard-cutoff C⁰ cosine (|z|^{−1} decay, O(1/K) truncation error [AF]) vs the C∞
window (|z|^{−2}, O(1/K²)) — the termination-error law is the *precise* finite-T statement, and the Lorch modification
is the *recommended smoothed window*, matching [AF]'s own next-step.
**Analogy to our setting.** Data cutoff Q ↔ window bandwidth (1/log T in γ-units); termination ripples ↔ the finite-T
error terms; step vs Lorch window ↔ hard-cutoff cosine vs C∞ χ-ramp window; the O(1/Q) vs O(1/Q²) scaling ↔ the [AF]
measured Δ ~ 1/log T (the *slower than both* arithmetic part is then cleanly separated, cf. A4).
**What it needs.** The termination-error formula written for the cosine and a C∞ window; one targeted run of the smoothed
window at the same T (the [AF] recommendation).
**Feasibility.** Low. **Value.** The crystallographic literature already *has* the quantitative answer to "hard-cutoff vs
smooth window" — the smoothed window's error control is strictly better, and the *residual* deficit after Lorch-style
smoothing is the arithmetic part by definition. This makes the P6 decomposition *standard practice* rather than ad hoc.
**Probe (<1h):** compute the termination-error amplitude for the cosine vs a C∞-ramped window on the ideal model at
T = 400; compare with the [AF] Δ-curve.

## A6. Powder auto-indexing ↔ crystal-compatibility test of the ceiling law — NEW (diagnostic; overlaps [P4.1], [CD-V7])
**Idea.** Auto-indexing (ITO/DICVOL/Treor — reported standard) answers: *is this 1-D diffraction pattern compatible with
any lattice?* It extracts peak positions and tests lattice fit. Our question is the mirror: *is the measured finite-T
pair-correlation data compatible with any periodic marked law matching the near-CUE rows?* The ceiling's 256-law is such
a law by construction, but the *full measured* data (all j, including the measured deviations from near-CUE) may not be
compatible with *any* periodic law — an *empirical* (non-proof) weakening of the ceiling's phenomenological status.
**Analogy to our setting.** Diffraction peaks ↔ S(j) rows; lattice fit ↔ periodic-marked-law fit; the *Wilson-statistics*
arm (the distribution of row fluctuations: zero for a perfect crystal, Gaussian for GUE/disorder) gives a second,
statistical test of "how crystal-like is the data".
**What it needs.** The measured S(j) (all j) from [AF]-style data; a periodic-law fitter (the [AC] machinery at N = 256 +
freedom in the law).
**Feasibility.** Low–Med. **Value.** Purely diagnostic, but it changes what we believe: if reality is *empirically
incompatible* with every periodic marked law, the ceiling's adversary is a mathematical artifact of the certificate
class, not a plausible physical configuration — sharpening the case for funding the beyond-1 arithmetic (B10) over
further in-class work.
**Probe (<1h):** fit the measured finite-T S(j) to the 256-law family (least squares over the law's freedom); report the
residual and the Wilson-style fluctuation statistic.

## A7. Rietveld / profile-fitting with a pseudo-Voigt instrument-resolution function: systematic P6 exponent extraction — NEW (P6 methodology; overlaps [P5.2], [P1.2])
**Idea.** Rietveld refinement fits a full profile to a parameterized model (structure + thermal + **instrument
resolution function**) simultaneously. The standard IRF is a **pseudo-Voigt** (Gaussian + Lorentzian mixture): the
Gaussian part models instrument/broadening artifacts (compact, window-determined), the Lorentzian part models intrinsic
long-tailed line shapes. Fit the finite-T pair-sum curve with a pseudo-Voigt-shaped error model and *read off the two
components' exponents*: Gaussian-strong ⇒ kernel artifact; Lorentzian-strong ⇒ arithmetic (long-tailed) error.
**Analogy to our setting.** Instrument broadening ↔ the window; Gaussian component ↔ kernel/cutoff artifact (the C∞ vs
hard-cutoff question); Lorentzian component ↔ the arithmetic pair-correlation error (slow, 1/√log T-class); the
*simultaneous* fit is the systematic replacement for the current ad-hoc fits of Δ(T) [AF].
**What it needs.** The [AF] data; a pseudo-Voigt fitter (scipy curve_fit); a parameterized model of the window.
**Feasibility.** Low–Med. **Value.** The standard, defended fitting methodology for exactly the "which part is which"
question of P6 — and a *prediction*: if the Lorentzian amplitude dominates, the arithmetic error is irreducible at
this T, whereas a dominant Gaussian part would shrink under the smoothed window (folding into A5's probe).
**Probe (<1h):** pseudo-Voigt fit to the [AF] Δ(T)/off-diagonal curves; report the two components' exponents.

## A8. MIR / isomorphous-replacement *multi-derivative phasing*: combine ζ, ξ′, ξ″ as "derivatives" — NEW (speculative methodology; overlaps [CD-V9], [P2.5]; bounded by [CD-A4])
**Idea.** Macromolecular phasing solves the phase problem by measuring *isomorphous derivatives* (the same structure +
heavy atoms) and combining them: the *difference* statistics isolate the heavy-atom (phase-carrying) part. Our family of
"derivatives" of the same underlying zero configuration: the derivative tower ξ′/ξ″ (zeros of ξ^(j) interlace the zeros
of ξ — [CD-A4] killed the *pointwise* interlacing LP, but the *statistical* comparison is untouched) and the σ-shifted
ζ(σ+it) family (A9).
**Analogy to our setting.** Heavy-atom derivatives ↔ ξ′, ξ″; isomorphous difference ↔ the *difference* of the two-moment
constants / form-factor statistics across the tower; the heavy-atom substructure ↔ the "extra" zeros of ξ′ and their
statistics. The crystallographic lesson: combining several derivatives' *incomplete* data can recover phase information
no single derivative carries.
**What it needs.** The ξ′/ξ″ two-moment constants computed empirically (P2.5's probe already computes ξ′); the *difference
pattern* (constants as a function of j: 0.858/0.868 → ?); a statistical model of what the differences encode.
**Feasibility.** Med (mostly compute). **Value.** A genuinely new *methodology* for P5's target family — not a single-
object certificate but a *joint* statement across the tower, with the crystallographic precedent that the *differences*
are where the information is. Honest risk: no exact isomorphous relation exists (the derivative zeros aren't a rigid
translation of ζ's), so the deliverable may be diagnostic only.
**Probe (<1h):** from cached zeros, compute the two-moment constants of ξ′'s zeros (P2.5 machinery) and the ζ-vs-ξ′
*constant gap*; report whether the gap's pattern matches a "derivative phasing" model.

## A9. σ-shift as *anomalous dispersion*: the off-line content via the σ ≠ 1/2 form factor — NEW (diagnostic for the off-line structure; overlaps [CD-V7])
**Idea.** Anomalous scattering (at an absorption edge the scattering factor becomes complex, breaking Friedel's law and
phasing the structure). Our analog of "complex scattering factor": the σ-shifted ζ(σ + it) at σ ≠ 1/2. Its zeros'
statistics deviate from the critical-line statistics *in a computable, parameterized way* (the explicit formula for
ζ(σ+it) has the same prime sums with σ-dependent prefactors), and the deviation is a *direct measurement* of how the
configuration would look if its zeros drifted off the line — i.e., a prime-side-computable diagnostic of the off-line
content that does *not* require RH to run.
**Analogy to our setting.** Anomalous dispersion ↔ σ-shift; Friedel-pair breaking ↔ σ-dependence of the pair sums; the
measured σ-difference ↔ a bound on "how much off-line structure the data permit."
**What it needs.** The explicit formula for ζ(σ+it) (mechanical from the ζ machinery); the σ-shifted pair sums computed
from primes for σ = 1/2 ± δ; comparison with the RH-world template.
**Feasibility.** Med (new code, mechanical). **Value.** Diagnostic, but the *right* diagnostic: every certificate-side
wall (LP, Nev, M29) is about *not knowing* the off-line content; this measures it directly from the prime side. A clean
σ-difference ≈ 0 says the data are consistent with zero off-line structure (reality on the RH side — motivating the
conjectural roadmaps); a detectable difference *prices* the off-line content.
**Probe (<1h):** mpmath: compute the σ-shifted pair sums for σ = 1/2 ± 0.01, 1/2 ± 0.05 at T ≈ 200; report the deviation
from the σ = 1/2 values.

## A10. Inverse Ornstein–Zernike: extract the zeros' *effective pair potential* — NEW (diagnostic for repulsion/rigidity; overlaps [P1.4], [CD-V17], [P3.1])
**Idea.** Liquid theory: the pair correlation h = g − 1 and the direct correlation c are linked by the **Ornstein–Zernike
equation** h = c + c*h·ρ; the **inverse OZ** (Henderson–Abraham–Barker — reported standard) iteratively recovers the
*effective pair potential* u(r) from the measured g(r). For the Dyson log-gas (the GUE/sine-kernel world) the effective
potential is u(τ) ∝ −log|τ|; for a crystal it is long-range and oscillatory; for a generic liquid it is short-range.
**Analogy to our setting.** Measured pair correlation ↔ the finite-T S(τ); effective potential ↔ a *summary statistic*
of the zeros' interaction structure; the log-form ↔ the GUE/determinantal signature; the deviation from log-form ↔ the
non-GUE content (a quantitative, model-free repulsion/rigidity reading — the input family [P1.4]/[CD-V17] price as
ceiling(ε)).
**What it needs.** The measured pair correlation from cached/10⁴ zeros; an IZO iteration (standard numerics).
**Feasibility.** Low–Med. **Value.** Turns the open "what repulsion input would buy" question [P1.4] into a *measured*
quantity: the fitted potential's shape and range, and specifically whether a −log|τ| fit holds — the empirical content of
the determinantal (GUE) hypothesis at the pair level. Diagnostic only.
**Probe (<1h):** IZO (or the simpler Henderson–Abraham–Barker iteration) on cached-zero pair correlations; plot the
fitted potential vs −log|τ|.

---

# DOMAIN B — Astronomy / large-scale structure & cosmology

**Abstraction (no domain vocabulary).** We estimate the *spectral density* (power spectrum / correlation function) of a
discrete point process from a *windowed, finite-volume* sample, with a known selection function (window), a known
shot-noise (self/mean) term, and sample variance that cannot be averaged away (only finitely many modes). We want
(a) bias-corrected estimates of the spectrum's *values*, (b) honest error bars on those values, and (c) a quantified
statement of how much *off-diagonal leakage* (window sidelobes mixing neighboring frequencies) contaminates the
measurement.

That is the standard survey-power-spectrum problem of cosmology (FKP, Landy–Szalay, MASTER, BAO analysis). The transfer
below imports the *estimator technology* — the exact thing our program is missing for P3 (empirical beyond-1 form factor)
and P6 (finite-T error terms).

## B1. Landy–Szalay estimator: the certificate's three ingredients ARE the DD/DR/RR pair counts — bias-canceling finite-T form-factor estimation — NEW (P3 + P6, highest-practical-value transfer)
**Idea.** The Landy–Szalay (1993 — reported standard) estimator of the correlation function,
ξ̂(r) = (DD − 2DR + RR)/RR, combines the data–data, data–random, and random–random pair counts to *cancel the leading
window and shot-noise bias* with near-minimum variance. Map the three terms onto our bookkeeping:
- **DD** (data pairs) ↔ the measured pair sums — the off-diagonal + diagonal contributions to the S(j) rows;
- **DR** (data × random) ↔ the *first-order* sums (zeros × window) — the explicit-formula *diagonal* prime sums;
- **RR** (random × random) ↔ the window's self-correlation — the ‖W_T‖²_HS norm machinery (the proven 1.3275·N).

All three terms are *already computed* in the paper; the LS *combination* (DD − 2DR + RR)/RR is the standard
bias-canceling estimator of the *excess correlation over the window-only null* — precisely the deviation of the true
form factor from 1.
**Analogy to our setting.** Survey window ↔ φ̂_T; random catalog ↔ the mean-field (window-only) configuration; the LS
excess ↔ (F − 1); the estimator's near-optimality ↔ the *best finite-T measurement* of the beyond-1 form factor.
**What it needs.** The three terms assembled from existing [AF]/finitet machinery; the LS combination computed on the
finite-T data; comparison of the LS-estimated rows with the raw rows.
**Feasibility.** Low–Med (all terms exist). **Value.** Two deliverables in one: (i) P3's empirical probe (V6/[CD-V6])
gets the *standard* bias-canceling estimator instead of raw histogramming; (ii) P6's error budget gets a direct check —
if the LS combination shrinks the measured deficit Δ(T), part of Δ is a *window-bias artifact* that the paper's method
already pays (documented improvement); if not, the deficit is intrinsic (the [AF] conclusion stands, now certified by a
standard estimator).
**Probe (<1h):** on [AF]-style data, assemble DD/DR/RR from the existing pair sums and report the LS-excess rows vs the
raw rows; check whether Δ(T) shrinks.

## B2. FKP window forward-modeling + variance law: the systematic P6 error bookkeeping — NEW (P6; overlaps [P9.1], [P9.2])
**Idea.** FKP (1994 — reported standard): the estimated power is the true spectrum *convolved with the survey window*
plus shot noise; the FKP rules are (i) *never deconvolve* — forward-model the convolution and fit; (ii) subtract the
shot-noise term exactly; (iii) the estimator's variance is [(P + shot)]² × (window normalization) — the
**cosmic-variance + shot-noise law**. Every element maps: our ⟨S(j)⟩ = ∫F(α)·W_T(j,α)dα + (error terms) is the windowed
measurement; the "shot noise" is the diagonal prime sum D; the variance law predicts the *sample variance* of Δ(T).
**Analogy to our setting.** Survey window ↔ W_T (width ~1/T in α); shot noise ↔ diagonal D; cosmic variance ↔ the
fluctuation of the finite-T certificate value; the FKP variance formula ⟨(ΔP)²⟩ = (P+shot)² ↔ a *predicted scaling law*
for var(Δ(T)) — the theory the [P9.1]/[P9.2] probes were measuring without one.
**What it needs.** The window resolution Δα; the FKP variance formula evaluated with our terms; comparison with the
measured var(Δ(T)) over adjacent windows.
**Feasibility.** Low. **Value.** (i) A *prediction*: var(Δ(T)) should follow the (P + shot)² law — a checkable statement
about the finite-T error terms [P9.1]; (ii) the forward-modeling discipline reframes the certificate's finite-T
validity as a *convolved measurement* with a quantified resolution limit — the natural frame for the effective theorem
[CD-V20].
**Probe (<1h):** compute the FKP variance formula for the [AF] windows; compare with the measured scatter of Δ(T).

## B3. BAO template fitting + reconstruction: the standard way to measure a known-scale signal in noise — NEW (P3 measurement methodology; directly upgrades [CD-V6])
**Idea.** BAO analysis measures the correlation function *peak at a known scale* through noise by (i) **template
fitting** — fit the theoretical template (linear-theory P(k) with the BAO wiggle), not the raw ξ; (ii) reporting the
peak's *significance*; (iii) **reconstruction** — estimate and remove the displacement smearing to sharpen the peak
(Eisenstein et al. 2007 — reported standard).
**Analogy to our setting.** Our F(α) near and beyond α = 1 is a "known-scale signal in noise": the theoretical template
is B24's proven formula F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T) (valid α ≤ 1) continued by the GUE value 1 beyond.
Template fitting: fit the B24 template (with the correction term as a free parameter) to the measured form factor and
report the significance of the (F − 1) deviation beyond α = 1 — the *honest* statement of how solid the empirical
beyond-1 evidence is. Reconstruction: remove the finite-T window smearing (forward-model in B2) to sharpen the beyond-1
measurement.
**What it needs.** The measured form factor (V6 machinery); the B24 template; a χ²/significance fit.
**Feasibility.** Low–Med. **Value.** The empirical P3 probe (V6) currently raw-histograms; BAO practice says the
*correct* output is a template fit + significance — turning a suggestive plot into a quantified statement ("the measured
deviation from F = 1 beyond α = 1 is 1.2σ, consistent with GUE") and a decision input for the conjectural roadmap
[CD-V5].
**Probe (<1h):** χ² template fit (B24 form) to the cached-zeros form factor at α ∈ [0,3]; report the fitted correction
term and its significance.

## B4. Slepian / prolate concentration: the *absolute floor* on out-of-band window leakage — NEW (P6 constant; supports [AF])
**Idea.** Multitaper spectral estimation (Thomson 1982 — reported standard) is built on **Slepian sequences / prolate
spheroidal wavefunctions**, with the *concentration theorem*: for a window of given time support, the fraction of its
energy inside a given frequency band is bounded by the first prolate eigenvalue — the *best possible* in-band
concentration. This is the *absolute floor* on how much beyond-band one information any finite-support window must leak
into the in-band measurement.
**Analogy to our setting.** The certificate reads F on [0,1] "as if" the window were perfectly band-limited; the
finite-T window has sidelobes beyond α = 1, and the *out-of-band leakage* ∫_{|α|>1}|φ̂_T|²/∫|φ̂_T|² is the irreducible
contamination of the in-band rows by the beyond-1 form factor. The Slepian bound gives the *optimal* (minimal) leakage
for the window's support — a single P6-relevant constant, and a quantitative statement of how much beyond-1 F is
*irreducibly mixed* into the bandwidth-one data.
**What it needs.** The prolate concentration ratio for the cosine window (numerical Slepian computation); the leakage
fraction for the C∞ window too.
**Feasibility.** Low. **Value.** (i) A P6 error-budget number: the leakage is the *weight* of the beyond-1 F in every
in-band row — the quantitative form of "B24's range ends at α = 1" [M29]; (ii) confirmation of the cosine's optimality
[AK] (the cosine is the band-limited concentration-optimal window of its class); (iii) the C∞-window leakage comparison
is the theory behind [AF]'s smoothed-window recommendation.
**Probe (<1h):** compute the leakage fraction for the cosine and a C∞-ramped window at the same support; report the two
numbers.

## B5. Cosmic variance: the mode-counting floor quantifies *why* the ceiling holds — NEW (framing + quantification; overlaps [P2.2], [P6.2])
**Idea.** Cosmic variance: a finite survey samples finitely many Fourier modes; the power estimate's variance is
~[P + shot]²/(# modes), so the *relative* resolution of any measurement is ~1/√(mode count). For the certificate: the
mode count is N (the zeros in [T,2T]); the crystal (256-law) and reality differ from the certificate's class *only at
the fluctuation level*, ~1/√N, below the certificate's resolution.
**Analogy to our setting.** Survey volume ↔ the [T,2T] window; mode count ↔ N; cosmic variance ↔ the empirical
indistinguishability of the crystal from reality at the certificate's resolution — a *quantified restatement of the
ceiling theorem's robustness* [AC][LP]: the certificate class reads *mean* data, and the mean data are what the law
matches.
**What it needs.** The mode-counting formula var ~ c/N fitted to the measured fluctuation of the certificate value
across T (the [P9.1] measurement, now with a predicted law).
**Feasibility.** Low (free). **Value.** A clean, quantitative *explanation* of the ceiling's persistence that also
predicts var(Δ(T)) ~ c/N — testable immediately; and the strategic conclusion (already in [LP]/[P6.2]) that only *new
inputs* (beyond-1 data or fluctuation-statistic inputs the class cannot read) can move the wall — now with the mode-
counting number as the resolution limit.
**Probe (<1h):** fit var(Δ(T)) vs 1/N on [AF] data; report the exponent.

## B6. Survey-mask leakage: the off-diagonal sums ARE window leakage — M29 reframed with one computable number — NEW (P3/P6 quantification; overlaps [M29], [CD-A1], [CD-A5])
**Idea.** Survey masks cause **mode coupling**: masked power = ∫P(k′)|W(k−k′)|²dk′, and the window's *k-space footprint*
(its sidelobes) quantifies the leakage. The astronomical practice is to *compute the window's full footprint* and fold it
into the model (never ignore it). Our off-diagonal prime-pair sums are exactly this: the leakage of the certificate's
window — power from beyond-1 α flowing into the in-band measurement through the window sidelobes.
**Analogy to our setting.** Mask footprint ↔ |φ̂_T|² sidelobes; leaked power ↔ the off-diagonal sums (M29's O₁); the
leakage *fraction* (B4's number) ↔ the *weight* of the beyond-1 F in the in-band rows — the quantitative bridge between
"the certificate reads [0,1]" and "the measurement is contaminated by (1,∞)".
**What it needs.** The leakage fraction (B4); a decomposition of the [AF] measured off-diagonal deficit into
window-leakage vs intrinsic-pair-correlation parts.
**Feasibility.** Low. **Value.** M29's documented negative is about the *mean* off-diagonal *bound*; the leakage
reframing gives the *measurement-side* statement: how much of the *observed* deficit could be window leakage vs real
beyond-1 structure — the correct error budget for P3's empirical claims (a raw measured beyond-1 deviation cannot be
interpreted without subtracting the leakage).
**Probe (<1h):** decompose the [AF] off-diagonal deficit into leakage (B4 number × F-beyond-1 model) vs intrinsic parts.

## B7. Optimal quadratic estimators / MASTER mode-coupling inversion: design the *finite-T-optimal* row estimator — NEW (P6 error *reduction*; overlaps [P5.2], [P1.2])
**Idea.** Power-spectrum estimation has a *provably optimal* family: **quadratic (Tegmark) estimators** minimize the
variance of band-power estimates subject to no bias, and the **MASTER method** (Hivon et al. 2002 — reported standard)
computes the window's *mode-coupling matrix* M (the exact linear map from true to estimated band powers) and performs a
*regularized inversion* to unbias the estimate (banded coupling matrices are stably invertible). For us: the window
couples the certificate rows S(j); the coupling matrix M(j,j′) is computable; the optimal (variance-minimizing, unbiased)
linear combination of the raw sums is the *best finite-T estimator* of the rows.
**Analogy to our setting.** Mode-coupling matrix ↔ M(j,j′) of our window (banded, local in α); regularized inversion ↔ a
*partial deconvolution* of the window (FKP says full deconvolution is ill-posed; MASTER says the banded case is stably
invertible); optimal weights ↔ the finite-T-optimal certificate data.
**What it needs.** M(j,j′) computed for the window (linear algebra on existing Ψ data); the optimal-weight solve; the
bias-variance tradeoff curve.
**Feasibility.** Med. **Value.** The *error-reduction* path for P6: if the optimal estimator's bias is below the
measured Δ(T), part of the deficit is estimator-suboptimality, recoverable by standard methods; if the bias is
irreducible, the [AF] conclusion is certified. Either way, the certificate's finite-T data get the standard optimal-
estimation treatment rather than raw sums.
**Probe (<1h):** compute the coupling matrix M(j,j′) for the [AF] window; report its bandwidth (how local the leakage
is) and the condition number of the banded inversion.

## B8. Kaiser-model RSD fitting: a *parameterized* off-line distortion with a fitted amplitude — NEW (diagnostic for off-line content; overlaps A9, [CD-V7])
**Idea.** Redshift-space distortions: peculiar velocities distort the line-of-sight clustering by a *smooth multiplicative
factor* — the Kaiser model P_s(k) = (1 + βμ²)²P_r(k) (reported standard) — and the fitted β measures the distortion
amplitude. The off-line-zeros analog: if zeros drifted off the line by β′, the *effective* measured correlation is
distorted by a smooth multiplicative damping (each off-line zero contributes e^{−(σ−1/2)|·|}-type factors through the
explicit formula).
**Analogy to our setting.** Peculiar velocities ↔ off-line drift; Kaiser factor ↔ the damping model; fitted β ↔ an
*upper bound on the off-line content* implied by the data; the μ-anisotropy ↔ (no line of sight — dropped).
**What it needs.** The measured form factor (V6 machinery); the damping model; a fit + bound.
**Feasibility.** Low–Med. **Value.** Same goal as A9 (measure the off-line content) with a *standard fitting procedure*
and a defensible bound; complements B3's template fit (the template is the RH-world, the RSD-style fit quantifies the
worst-case off-line drift the data tolerate). Diagnostic only.
**Probe (<1h):** fit the damping model to the cached-zeros form factor; report the implied off-line fraction bound.

## B9. Halo-model one-halo/two-halo split: the Poisson-ness test of the beyond-1 form factor — NEW (statistical diagnostic for P3; overlaps [P9.2], [CD-V6])
**Idea.** The halo model splits the correlation into a **one-halo** term (within-cluster pairs — *Poisson-like*, variance
= mean) and a **two-halo** term (between-cluster pairs — *correlated*, tracing the linear field) (reported standard).
The scale where one-halo dominates is where the field is shot-noise-limited. For us, the diagonal (self) prime sums are
the "one-halo" (Poisson) part and the off-diagonal (cross) sums are the "two-halo" (correlated) part — the split M29
already measured (S_pair(δ=1)/D = 0.04–0.41).
**Analogy to our setting.** One-halo ↔ diagonal D (Poisson, exactly known); two-halo ↔ off-diagonal O₁ (correlated,
M29's obstruction); the Poisson-ness test ↔ *is the beyond-1 form factor "shot noise" (F ≡ 1, the HL value) or
correlated structure (F ≠ 1)?* — a statistical decision on the P3 question.
**What it needs.** The beyond-1 empirical F (V6); the Poisson-vs-correlated test (compare the measured pair-sum
fluctuation to its mean).
**Feasibility.** Low. **Value.** A *decision statistic* for P3: if the beyond-1 measurements are consistent with Poisson
(shot-noise-like), the F ≡ 1 hypothesis is supported and the conjectural roadmap [CD-V5] rests on solid empirical
ground; if not, the deviation needs a structural explanation (a real finding).
**Probe (<1h):** variance-vs-mean test on the beyond-1 empirical pair sums from cached zeros.

## B10. Goldston–Montgomery *variance* as a different functional of the beyond-1 form factor — a potential proven sliver M29 did not test — NEW-CONJECTURED (P3, the highest-EV vector; bounded by a bookkeeping check)
**Idea.** M29 (documented negative, PROVEN) kills the *mean* off-diagonal pair sums at X = T^{1+ε}. But the certificate's
data admit a *second* functional of the beyond-1 form factor: the **counting-function variance** over windows — the
windowed integral of F — which the **Goldston–Montgomery / Selberg variance theorems** (PROVEN in the analytic-number-
theory sense, exact range to verify) control *unconditionally*, where the *mean* (HL) is not proven. The variance is the
*second moment of the counting error*, a genuinely different object from the first-moment pair sums M29 bounded. The
mapping: window length U at height T corresponds to form-factor scale α = U/T, so *beyond-1 data = long windows (U > T)*,
and the question is whether *any proven* variance statement reaches U > T (or a weighted window with support there).
**Analogy to our setting.** Cosmic/sample variance ↔ the counting fluctuation; the GM variance ↔ the proven control on
it; the certificate's own HS norm ‖W_T‖² is already the windowed ∫F — the *variance* route asks whether a *different
window (longer, or α-weighted)* has proven content beyond the [0,1] data.
**What it needs.** The exact proven range of the zero-counting variance theorem (Goldston–Montgomery 1987 / Selberg;
verify the stated range in the literature — we do not hold the paper); the window ↔ α bookkeeping (α = U/T); the form-
factor integral's finite part (the windowed variance is finite where ∫F diverges).
**Feasibility.** Med (bookkeeping + literature check + small numerics). **Value.** The *only* vector in this catalog that
could reopen M29's documented negative from a *different functional*: variance statements are proven where means are
not, and the certificate's fluctuation-sensitive variants ([P9.1]'s a.s.-certificate; the two-moment class's *variance*
analog) would use a proven beyond-1-integral input. Honest kill criterion: if every proven variance range maps to α ≤ 1
only (expected if the proven windows satisfy U ≪ T), the vector is a documented confirmation of the wall from the
variance side — still worth writing down because M29's negative is about means and this closes the *variance* flank.
**Probe (<1h):** bookkeeping — write the windowed counting variance in form-factor language, list the proven window
ranges from the GM/Selberg statements in the paper's own bibliography [M29 §4's table is the model], and mark which
ranges cross α = 1.

---

# TOP 10 (EV × feasibility × cheap-probe)

1. **B10 — GM/Selberg variance as a beyond-1 functional (the M29 flank).** The only vector that could reopen the
   beyond-α=1 documented negative from a *different functional* (variance vs mean); probe is bookkeeping + literature
   check. EV highest; feasibility Med; expected negative, documented either way. Probe <1h.
2. **B1 — Landy–Szalay bias-canceling estimator (DD/DR/RR = pair sums / diagonal / HS norm).** The standard estimator
   applied to the certificate's own terms; simultaneously upgrades P3's empirical measurement and checks P6's deficit.
   Probe: assemble from existing [AF] terms — under an hour.
3. **B3 — BAO template fitting + significance for the beyond-1 form factor.** Turns V6 from a plot into a quantified
   statement (fit B24 template, report the (F−1) significance). Directly usable now. Probe: χ² fit on cached data.
4. **A5 — Termination-error / Lorch analysis for the C∞ vs hard-cutoff window.** The exact truncation-error law is the
   P6 question; the Lorch modification is the recommended smoothed window [AF] already wants. Probe: compute the two
   windows' termination amplitudes on the ideal model.
5. **B4 — Slepian/leakage fraction: the absolute floor on out-of-band contamination.** A single P6 number (how much
   beyond-1 F leaks into the in-band rows) plus the theory behind the smoothed-window recommendation. Probe: two
   leakage integrals — under an hour.
6. **A1 — K–H triple-product bound prices the third-moment input.** The admissible m₃ range from pair data + the
   distinct-count LP = a P2 roadmap parallel to [P1.4]'s ceiling(ε); clean negative or positive in a day. Probe: 3×3
   K–H determinant on the law's rows.
7. **B2 — FKP variance law for Δ(T).** A checkable prediction (var(Δ(T)) = (P + shot)²-law) that turns [P9.1]'s
   measurement into a theory test, and the forward-modeling frame for the effective theorem. Probe: formula vs [AF]
   scatter.
8. **A7 — Rietveld/pseudo-Voigt decomposition of P6's error terms.** The standard profile-fitting procedure for "kernel
   vs arithmetic" with defended exponents. Probe: pseudo-Voigt fit to [AF] curves.
9. **A2 — Sayre-residual / connected-triple diagnostic for P2.** Measures whether reality is crystal-like (factorizing)
   or GUE-like (connected) — the empirical signal test for the third-moment route before funding [P6.5] further.
   Probe: residual on cached zeros.
10. **B5 — Cosmic-variance mode-counting quantification of the ceiling's robustness.** Explains *why* the ceiling
    persists (the class reads means; the crystal matches the means) and predicts var(Δ(T)) ~ c/N; free probe.

**Strategic reading.** Two *different-functional* bets stand out: B10 (variance flank on the M29 wall) and A1/A2
(third-moment price/consistency for P2). The estimator-technology transfers (B1, B3, B7, B2) upgrade the *measurement
side* of P3 and P6 — they change what we believe about the empirical evidence and the finite-T error structure *without
any new arithmetic*. The window-physics transfers (A5, B4, A4) give P6 the *standard* answers to the C∞-vs-hard-cutoff
question that [AF] flagged as its own next step. Nothing here claims a new theorem; the honest output is a ranked set of
cheap probes whose negatives are documented findings, plus one genuinely risky shot at the beyond-1 wall (B10).

---

# WILD section (deliberately provocative; honestly evaluated; each labeled)

### W-C1. "The zeros are a crystal at zero temperature; the 256-law is the T = 0 structure; reality is the T ≠ 0 smeared structure; the certificate gap is thermal expansion" — CONJECTURED (framing; content is A4, not a theorem)
**For:** the Debye–Waller framing (A4) is real: smearing is multiplicative, smooth, and separates cleanly from
structure. The "thermal expansion" (the deficit growing/shrinking with T) is measurable.
**Against:** there is no dynamics — the "temperature" is a bookkeeping variable, not a Hamiltonian; the crystal is not a
ground state of any known potential for the zeros (the Dyson log-gas is the only candidate [A10], and it is conjectural
for the zeros). **Honest verdict:** the useful content is the envelope decomposition (A4); the thermodynamic numerology
adds nothing provable. Label: KNOWN-OPEN as framing, DEAD as an input route.

### W-C2. "Oversampled phase retrieval (Fienup/SHARP): measure the form factor on a *finer* α-grid in [0,1] and recover the phase by iterative support constraints" — KNOWN-DEAD (honest kill)
**For:** crystallographic/microscopy phase retrieval recovers phases from oversampled intensities with a compact-support
prior.
**Against:** the support constraint is the engine, and the zero configuration's autocorrelation has *no* compact support
in γ (the measure is not compactly supported after windowing); moreover our in-band *phases* are already known prime
sums (A1) — oversampling [0,1] cannot reach the missing α > 1 data, which is the entire wall [M29]. No support
constraint, no new band: the bandwidth wall kills it. Label: KNOWN-DEAD, cheap to confirm (a 1-line argument, done above).

### W-C3. "BAO reconstruction as a Hilbert–Pólya route: reverse-engineer the displacement field that would sharpen the beyond-1 form factor to a crystal δ-peak" — CONJECTURED (framing only)
**For:** reconstruction sharpens the BAO peak by inverting the non-linear smearing; the "sharpened" beyond-1 F would be
the crystal's δ-structure; the reconstruction's residual field would be the "off-line displacement".
**Against:** reconstruction needs a *model* of the displacement (the non-linear evolution), which for the zeros is
exactly the unknown arithmetic (HL-strength); the residual field has no certificate meaning. **Honest verdict:** the
*measurement* version (B3's reconstruction = finite-T window deconvolution) is real; the *Hilbert–Pólya* reading is
vocabulary. Label: NEW (measurement), DEAD (as a route to a theorem).

### W-C4. "CMB acoustic-peak ratios: the *ratios* of the certificate rows are robust cosmological-parameter constraints — a Bayesian peak-ratio analysis gives a *posterior* on the beyond-1 F" — NEW (quantification)
**For:** Planck/WMAP constrain parameters from peak *ratios* because ratios are robust to calibration; our near-CUE rows'
ratios (S(j₁)/S(j₂) fixed by F ≡ 1) are the same kind of robust summary — a Bayesian analysis of the measured ratios
yields a *posterior distribution* on the beyond-1 F (the probabilistic version of the conjectural roadmap [CD-V5]).
**Against:** the posterior is only as good as the prior over configurations (the crystal vs reality), which is the open
question; the output is a heuristic quantification, not a certificate input. **Honest verdict:** the *content* folds into
B3's template fit (significance reporting); the "posterior roadmap" is a clean way to present the V5 price curve with
error bars. Label: NEW (quantification), MEDIUM value.

### W-C5. "Fit the zeros' effective pair potential (IZO, A10); if it is the Dyson log-gas with a Debye screening length, the screened potential *predicts* the decay of (F − 1) beyond α = 1" — CONJECTURED (diagnostic content real, prediction heuristic)
**For:** the log-gas identification is the GUE/fermion hypothesis; a fitted screening length gives a *parametric model*
of the beyond-1 F decay — a concrete, testable prediction against the measured F.
**Against:** the screening length is fit from the same data being predicted; the Dyson identification for the zeros is
conjectural (it is RH + pair-correlation-conjecture territory); no theorem follows. **Honest verdict:** the fit is a
cheap diagnostic that sharpens the empirical P3 statement; the prediction is a heuristic. Label: NEW (diagnostic),
CONJECTURED (as a predictor).

---

# Label inventory

- **NEW** (invented here, untested, each with a kill criterion/probe): A1 (K–H triple-product price), A2 (Sayre-residual
  diagnostic), A3 (Burg MEM estimator), A4 (Wilson-plot/Debye–Waller decomposition), A5 (termination-error/Lorch),
  A6 (indexing/crystal-compatibility), A7 (Rietveld/pseudo-Voigt), A8 (MIR multi-derivative phasing), A9 (σ-shift
  anomalous dispersion), A10 (inverse OZ potential), B1 (Landy–Szalay), B2 (FKP variance law), B3 (BAO template),
  B4 (Slepian leakage floor), B5 (cosmic-variance mode counting), B6 (mask-leakage reframing of M29), B7 (optimal
  quadratic estimator/MASTER), B8 (Kaiser-model off-line fit), B9 (halo-model Poisson test), B10 (GM-variance beyond-1
  flank — flagged CONJECTURED with the sharpest kill criterion), W-C4, W-C5.
- **KNOWN-OPEN** (core open / already flagged; new procedure or framing only): A1's *PSD direction* (reduces to B24
  F ≥ 0 — automatic), A8 (bounded by the [CD-A4] interlacing death for pointwise use), B5's *conclusion* (the ceiling's
  robustness — matches [LP]/[AC]), B10's *proven-range question* (exact range of the zero-counting variance theorem —
  verify in the literature before use).
- **KNOWN-DEAD** (immediately reducible to a documented wall): W-C2 (no compact support + no new band); A1's *constraint*
  direction (K–H PSD is a tautology for the zeros — phases are known prime sums); any "deconvolve the window" framing
  without the banded-inversion caveat (B7's regularized inversion is the survivable version).
- **TESTED-OPEN**: none directly tested in our notes yet (all probes are new); the *data* they consume ([AF]'s Δ(T),
  cached zeros, the [LP] LP machinery) are TESTED-OPEN states carried over.

**Honest closing note.** The two strongest NEW contributions are (i) **B10** — the only vector that attacks the
beyond-α=1 wall from a *different functional* (the proven GM/Selberg *variance* of the zero counting, vs M29's
*mean* pair sums) — likely negative after bookkeeping but cheap to settle and would genuinely reopen P3 if positive;
and (ii) the **estimator-technology package (B1, B3, B7, B2)** — the standard survey-estimation machinery maps term-for-
term onto the certificate's own bookkeeping and upgrades both the empirical P3 measurement and the P6 error analysis
*using only what the paper already computes*. The window-physics transfers (A5, B4, A4, A7) supply the standard answers
to the C∞-vs-hard-cutoff question [AF] flagged as its own next step. The crystallographic direct-methods material (A1,
A2, A3) mostly *explains* why P2's input is the third moment (it is the lowest-order phase-carrying statistic — the
same conclusion as [P6.4], now with the K–H price-list and the Sayre-residual test as concrete deliverables). The
persistent wall — beyond-1 form factor, third moments, repulsion — remains, but the astronomy domain adds one honest
crack (B10) and a set of standard tools for *measuring* the wall's data side cleanly.
