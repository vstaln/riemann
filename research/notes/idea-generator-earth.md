# Idea Generator: earth-sciences attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (earth-sciences angle; creativity + analogy-domain-transfer + constraint).
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to probe.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems about ζ. Earth-science
facts are named at the level "standard in the field" (normal modes, coda interferometry, Kolmogorov 4/5
law, Coulomb wedge, Gutenberg–Richter, Horton–Strahler, complementary variational principles, 4D-Var/EnKF,
shallow-ice approximation, marine-ice-sheet hysteresis — all textbook-level); anything I cannot fully
verify from our held sources is flagged "verify before citing". Every *idea* is **CONJECTURED** by
construction with a kill/probe criterion and labeled **NEW / KNOWN-DEAD / KNOWN-OPEN / TESTED-OPEN**.
Overlap discipline: crossdomain = idea-generator-crossdomain.md [CD-V#]/[CD-W#]/[CD-A#]; physics =
idea-generator-physics.md [PH-P#]; attack notes: attack-ceiling [AC], attack-kernel [AK], attack-finitet
[AF], attack-multiplicity [AM], attack-lpdual [ALD], attack-twoform [ATF], attack-m29 [M29].

**State of the art this catalog must respect (PROVEN / CHECKED):**
- 67.25% = 3/2 − (1/√2)cot(1/√2) (Theorem D); 2/3 flat; 5/6 distinct; 0.83625 distinct (optimal window);
  bandwidth-one ceiling 0.68182868746… (Lean [AC]).
- **The in-class gap is CLOSED as a certificate-optimality question**: the LP dual attains 0.68183123,
  tight to 5·10⁻⁹; "no missing constraint inside bandwidth one"; the only datum that moves v is the
  certified simple-point fraction p₁ (shadow price exactly 1), which needs **beyond-bandwidth-1** data
  (CONJECTURED, unavailable) [ALD]. This *sharpens* P1: the missing constraint, if any, is not in-class.
- Beyond-1 form factor: every proven bound fails by 3.6·10³–3.7·10⁴× [M29]; only conjectural *values*
  (HL/Montgomery PCC, HL*(k₀,λ)) would clear it. P3 is value-territory only.
- P2 (third moment): tr Â³ unconditionally evaluable exactly in the RS range λ < 2/3 [CD-V3]; §7.5(e)
  proves odd moments don't lower Λ₁(0) for the *on-line* functional; the *distinct* functional is open;
  the two-bandwidth joint certificate (λ=1 two moments + λ=1/2 third moment) is the leading P2 route
  [PH-P6.5].
- Finite-T: Δ(T) = bound/N − 0.6725 > 0 at every tested T, ~1/log T, single-sample wiggle [AF]; likely
  pair-correlation-driven, not a hard-cutoff artifact (the C∞ smoothing test is still open) [AF §7].
- ξ′-tower: 0.85838/0.86864 simple, 0.92919/0.93432 distinct (PROVEN); ξ″/ξ‴ mechanical [CD-V9];
  interlacing gives only a difference lower bound (no ratio/upper constraint) [CD-A4]; a second
  ζ′(ρ)-moment form exists with rank C ≤ N_s PROVEN, constant 19/27 RH-conditional [ATF].

**The problem in structural essence (for analogy mining):**
> We hold a finite self-adjoint matrix W_T (prime-side data only) that is PSD iff RH holds. We can prove
> two scalar moments (trace, Frobenius) plus integrality of a spectral count, and from these bound the
> positive inertia from below (67.25%). A worst-case "adversarial configuration" — a periodic marked
> crystal matching exactly those two moments — saturates the method (0.6818). Real data sits strictly
> above the bound (Δ(T) > 0). We seek a *provable* additional constraint (third moment, beyond-1 data,
> repulsion, fluctuation law) that the crystal violates but the real zeros satisfy. Equivalently: the
> certificate is a "limited-aperture measurement" (bandwidth-one) whose null-space artifacts (the crystal
> family) are indistinguishable from reality; every in-class knob is now priced and turned (shadow prices
> known [ALD]); the only remaining inputs are *new data* beyond the aperture.

---

## Pool 1 — Seismology: normal modes, tomography, coda

### E1.1 Normal-mode splitting as the off-line detector — NEW (diagnostic)
**Idea:** the Earth's free oscillations are a discrete spectrum from a Rayleigh variational problem;
rotation/ellipticity/heterogeneity *split* degenerate multiplets, and the splitting function is inverted
for interior structure. Our W_T is a discrete spectrum from a variational (window-restricted Weil) form;
off-line pairs inject hyperbolic (1,1)-planes whose blocks look like *split multiplets* at the bottom of
the spectrum. The seismological diagnostic: split-multiplet statistics (pattern of a degenerate cluster
under a perturbation) vs the unperturbed multiplet.
**Analogy mapped:** off-line pairs ↔ the perturbation that splits eigenvalue clusters of W_T; RH ↔ "no
splitting" (all on-line); the split pattern ↔ how much interior (off-line) structure is present, measured
from prime-side data alone, no RH.
**Needs:** full W_T spectrum (code exists [CD-V1]/[AF]); a synthetic split-multiplet model for p
(1,1)-planes via the Ψ inner-product formula [AF]/[PH-P10.4].
**Feasibility:** Low–Med. Diagnostic only (a measurement cannot enter a per-T certificate).
**Label:** NEW.
**Cheapest probe (<1h):** at T=200–600, cluster the smallest ~10% of W_T eigenvalues; compare cluster
splitting with the p=0 prediction vs p≥1 synthetic injections (mpmath, existing spectra).

### E1.2 Limited-angle tomography: the ceiling law is the null-space ghost — NEW (framing)
**Idea:** limited-angle tomography (Radon transform with restricted angular aperture) has a
*characterized null space* — the unseen directions — whose reconstruction artifacts ("ghosts") no
reconstruction can exclude. The bandwidth-one certificate is a limited-aperture measurement; the
256-periodic crystal is the canonical ghost of that aperture.
**Analogy mapped:** aperture ↔ bandwidth-1 form factor; ghosts ↔ the extremal law family; more angles ↔
beyond-1 F (M29: closed, values only). The transferable structure: for the Radon transform the ghost set
is a *linear space* — suggesting the extremal configurations form a *family/manifold*, not a single law;
[ALD] already shows the LP optimum is attained (tight), so the open question is the *shape* of the
optimizer set (a flat manifold would explain why the certificate class is exhausted).
**Needs:** none (framing); a perturbation test of the LP optimum (is the ceiling flat in mark-space?).
**Feasibility:** Low.
**Label:** NEW (framing; validates [ALD]'s tightness reading).
**Cheapest probe (<1h):** perturb the 256-law's marks locally, re-solve the [ALD] LP, record whether the
ceiling value is locally flat (manifold of optimizers) or isolated.

### E1.3 Coda-wave decorrelation as the T-window sensitivity diagnostic — NEW (diagnostic)
**Idea:** coda interferometry measures medium change via the *decorrelation* of multiply-scattered waves;
the decorrelation rate is governed by the scattering heterogeneity scale. Our finite-T deficit Δ(T)
(positive, ~1/log T, with single-sample wiggle [AF]) is the "coda" of the certificate; the drift of the
W_T eigenvalue law across *adjacent* T-windows is a direct measurement of the zero configuration's
heterogeneity vs the crystal (exactly periodic ⇒ zero decorrelation).
**Analogy mapped:** coda decorrelation ↔ eigenvalue-law drift across adjacent T-windows; heterogeneity
scale ↔ how fast the law decorrelates in T; crystal ↔ a perfectly correlated (periodic) medium.
**Needs:** W_T spectra across adjacent windows (extend [AF]); a decorrelation statistic (eigenvalue
density overlap).
**Feasibility:** Low.
**Label:** NEW (diagnostic).
**Cheapest probe (<1h):** density-overlap of the W_T eigenvalue law between adjacent windows at
T=100–700; crystal model predicts 1, real data predicts <1 with a T-scale (feeds P6's error picture).

### E1.4 Mode stripping: residual inertia after subtracting the crystal — NEW (diagnostic)
**Idea:** seismologists strip known modes to expose anomalous splitting. Subtract from W_T the best
two-moment-consistent crystal form (built from the 256-law's marks and the v-vectors); the residual
matrix's inertia/size is the *unrealized* slack beyond the extremal law.
**Analogy mapped:** mode stripping ↔ W_real − W_crystal; residual spectrum ↔ the certificate's slack
beyond the crystal (Δ(T)'s spectral face).
**Needs:** W_T (exists) + constructible W_crystal.
**Feasibility:** Low.
**Label:** NEW.
**Cheapest probe (<1h):** build W_crystal, print the residual's Frobenius norm and inertia as a function
of T; compare the residual's trend with Δ(T) [AF].

### E1.5 Modal sum rules: the moment hierarchy as an all-or-nothing structure — NEW (framing on P2)
**Idea:** the free-oscillation spectrum obeys *sum rules* tied to total mass/moment of inertia; sum rules
come in hierarchies indexed by moments of the interior density profile. The zeros' tr W_T = N is the
"mass" sum rule; ‖·‖² is the second; the third is tr Â³ (P2 [CD-V3]).
**Analogy mapped:** sum-rule hierarchy ↔ the moment sequence m_k (GUE 1, 4/3, 2, 13/4…); the interesting
structure: the hierarchy is *partially* available — tr Â³ IS available in the RS range (λ<2/3) while the
bandwidth-one second moment is available at λ≤1 — i.e., *different orders are available in different
bands*; the natural object is a *band-resolved moment curve* m_k(λ).
**Needs:** none (framing); the band-resolved moment curve is the [PH-P6.5]/[CD-V3] computation.
**Feasibility:** Low.
**Label:** NEW (framing on P2).
**Cheapest probe (<1h):** none new (documentation); the m₃(λ) curve is [PH-P6.5]'s LP input.

### E1.6 Ray-path tomography: primes as rays through the zero medium — KNOWN-DEAD-likely (restatement)
**Idea:** travel-time tomography inverts a slowness field from ray integrals; the explicit formula is a
"ray integral" of the zero measure with weight φ̂_T(γ−α). Tomography's limited-angle uniqueness theory is
E1.2; the *travel-time* framing adds only the observation that the "rays" (primes) sample the medium with
band-limited aperture — the aperture is the wall.
**Analogy mapped:** slowness field ↔ zero density; ray integrals ↔ explicit-formula sums; limited-angle
uniqueness ↔ the ceiling (both: what the aperture cannot see is unrecoverable).
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-DEAD-likely (E1.2 restatement; no new input).
**Cheapest probe:** none (recorded).

---

## Pool 2 — Climate dynamics: oscillators, cascade, tipping points, 1/f

### E2.1 Kolmogorov 4/5 law: the third order is the *exact* order — NEW (prior on P2 — the strongest framing here)
**Idea:** in turbulence, the second-order structure function is only *scaling* (K41 with intermittency
corrections), but the *third-order* structure function obeys the *exact* 4/5 law — exact because it
follows from a *conservation law* (energy balance), not dimensional analysis. The parallel structure: our
second moment (form factor on [0,1]) is "scaling-level" — it leaves the crystal undetermined — while the
*third* moment in the RS range is fixed by the *diagonal evaluation*, which is exact (unconditional).
**Analogy mapped:** energy cascade ↔ the moment hierarchy of the zero measure; 4/5-law exactness ↔ the
RS-range tr Â³ evaluation; intermittency corrections ↔ the crystal's two-moment freedom. The *prior*: a
third-order statement can hold *exactly* where the second-order one is non-universal — P2 is not a mere
"next order"; it is the first *conservation-level* statement, and the hunt should be phrased as "find the
conserved quantity behind tr Â³" (in turbulence the 4/5 law's ε IS the dissipation — for us the conserved
quantity is the explicit-formula identity structure at λ<2/3).
**Needs:** none (framing); then [CD-V3]/[PH-P6.5]'s LP with m₃=2.
**Feasibility:** Low.
**Label:** NEW (framing prior; content = P2).
**Cheapest probe (<1h):** none for the framing; the joint LP probe is [PH-P6.5]'s (m₃ = 2, distinct
count: does N_d beat 5/6?).

### E2.2 Critical slowing down: the Selberg CLT variance growth as "approach to the line" — KNOWN-DEAD (input), NEW (rate diagnostic)
**Idea:** approaching a bifurcation, fluctuations grow (critical slowing down: rising variance and
autocorrelation). The zeros' *proven* fluctuation law — Selberg's CLT, S(t) variance ~ (1/2)log log t —
is exactly the "critical slowing down" signature of approaching the line; the crystal has O(1)
fluctuations (deterministic). A certificate that read *fluctuation growth* would exclude the crystal.
**Analogy mapped:** bifurcation approach ↔ zeros approaching the line as T→∞; variance growth ↔ the S(t)
CLT; crystal ↔ the fixed point with no fluctuations.
**Needs:** nothing new: [CD-V13] already analyzed this — the *variance* is fixed by F near 0 (which the
crystal matches), so the leading fluctuation statistic is determined at bandwidth one; the *shape*
(Gaussian vs deterministic) is not readable in-class. The surviving fragment: the *rate* of variance
growth across T-windows is a measurable diagnostic for P6.
**Feasibility:** Low.
**Label:** KNOWN-DEAD as input ([CD-V13]); NEW as rate diagnostic.
**Cheapest probe (<1h):** var(Δ(T)) over adjacent T-windows vs the Selberg-implied rate ([PH-P9.1]'s
probe, reused).

### E2.3 1/f noise and the scale break: band-integrated spectra — KNOWN-DEAD (input), NEW (diagnostic framing)
**Idea:** climate records show 1/f-like spectra with a scale break; the *band-integrated* variance is a
robust estimator when fine structure is noisy. Our beyond-1 form factor is the "beyond-the-break"
structure; the *integrated* object ∫₁^A F is exactly M29's target — and M29's negative says the
*mean* (not the noise) is the obstruction: integration cannot help.
**Analogy mapped:** variance budget (weather vs climate band) ↔ decomposition of Δ(T) into
kernel-boundary vs arithmetic parts ([PH-P5.2]/[PH-P5.5] Fisher–Hartwig decomposition).
**Needs:** the FH/Toeplitz computation [PH-P5.5].
**Feasibility:** Low.
**Label:** KNOWN-DEAD as input ([M29]); NEW as diagnostic framing.
**Cheapest probe (<1h):** the [PH-P5.5] FH-exponent + [AF] fit (kernel-artifact vs arithmetic split).

### E2.4 Tidal admittance: F(α) as the response function; the phase is structurally zero — KNOWN-DEAD (documented)
**Idea:** tidal analysis fits *admittances* band-by-band; band-averaged admittances are stable when
individual constituents are noisy. The zero configuration's "admittance" to the prime forcing is the form
factor F(α); the *phase* of the admittance would be new information — but the FE symmetry forces
Im W ≡ 0 identically ([CD-A2]: the odd-window detector is dead), and the amplitude beyond band 1 is
M29-dead.
**Analogy mapped:** admittance amplitude ↔ F ≥ 0; admittance phase ↔ Im W (identically zero by Schwarz
reflection); band-averaging ↔ the certificate's window averaging (already optimal, [AK]).
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-DEAD ([CD-A2], [M29]).
**Cheapest probe:** none (two documented deaths, one name).

### E2.5 ENSO/MJO oscillator theory: significance testing against a red-noise null — NEW (statistical framing)
**Idea:** climate signal detection tests spectral peaks against a *null* (AR(1) red noise) and controls
false discovery across all frequencies. The certificate's "detection" of off-line structure in the W_T
spectrum is the same problem: the null is the two-moment-consistent law (the crystal), and the
*finite-sample fluctuations* of W_T's spectrum set the significance threshold for E1.1's split clusters.
**Analogy mapped:** red-noise null ↔ the crystal; FDR control ↔ a multiplicity-corrected threshold for
the cluster-splitting statistic; stochastic-oscillator peak broadening ↔ the finite-T spread of the
near-degenerate clusters.
**Needs:** W_T spectra (exists); a bootstrap ensemble of the crystal-W.
**Feasibility:** Low.
**Label:** NEW.
**Cheapest probe (<1h):** bootstrap the crystal-W spectrum, calibrate the cluster-splitting threshold,
apply to E1.1's real data (reuse E1.1's probe).

### E2.6 Cross-window consistency of the explicit formula as a "physical prior" — NEW (likely KNOWN-DEAD after probe)
**Idea:** climate model tuning uses *physical priors* (conservation, energy balance), not arbitrary
smoothness. The certificate's analog of a physical prior: the *same* configuration must satisfy the
explicit formula for *every* window — a cross-λ consistency constraint. But the crystal was built with
F ≡ 1 on [0,1] (up to α=256), so its two-moment data are consistent at every λ ≤ 1 by construction —
the constraint is *automatically satisfied* by the crystal.
**Analogy mapped:** physical priors ↔ cross-window identities of the explicit formula; the crystal's
consistency ↔ why the two-moment cross-window constraint cannot bite.
**Needs:** the crystal's two-moment values at λ=1/2 and λ=1 (computable from F ≡ 1).
**Feasibility:** Low.
**Label:** NEW (likely KNOWN-DEAD after probe).
**Cheapest probe (<1h):** compute the crystal's tr/‖·‖² at λ=1/2, λ=1; verify consistency (expected:
consistent ⇒ dead — the higher-moment version is P2).

---

## Pool 3 — Geology / plate tectonics: wedges, G–R, faults

### E3.1 Coulomb critical wedge: the certificate as a critical taper, now attained — NEW (state-framing)
**Idea:** accretionary wedges self-organize to a *critical taper* — a history-independent variational
optimum that is also a *universal upper bound* (a wedge steeper than critical fails). Our ceiling 0.6818
is the "critical taper" of the certificate class; the 0.6725 certificate was a *subcritical* wedge. [ALD]
has now shown the wedge reaches criticality (LP tight to 5·10⁻⁹).
**Analogy mapped:** critical taper ↔ the attained ceiling; Coulomb yield ↔ the stability inequality
(ceiling_stability [AC]); subcritical wedge ↔ the paper's 0.6725 certificate. The geological reading of
[ALD]: "the wedge is at criticality — the remaining gap is *data* (beyond-1 F), not geometry", which is
the correct current state of P1.
**Needs:** none (state-framing; content already in [ALD]).
**Feasibility:** Low.
**Label:** NEW (state-framing).
**Cheapest probe:** none (recorded; cites [ALD]).

### E3.2 Gutenberg–Richter b-value: moment order fixes tail shape — NEW (framing; overlaps P2/P3)
**Idea:** G–R's b-value is a shape parameter of the magnitude distribution; local b-value anomalies are
precursors. The zeros' spacing-distribution "b-value" is fixed by low moments only at coarse level; the
*tail* (large gaps) is governed by higher moments — exactly P2/P3 territory. The seismological lesson:
b-values are *estimated* from finite catalogs, and the *estimation error of low moments* is the binding
constraint — the crystal and reality agree *within the measurement error of the two moments*;
distinguishing them requires lower-error (higher-order) moments.
**Analogy mapped:** b-value ↔ spacing-distribution slope; precursor anomaly ↔ local moment fluctuations;
catalog error ↔ the two-moment measurement's inability to separate crystal from reality.
**Needs:** none (framing); a spacing-statistics measurement of the cached zeros vs the crystal.
**Feasibility:** Low.
**Label:** NEW (framing).
**Cheapest probe (<1h):** from the cached zeros, compute the local moment ratio over sliding windows;
compare its fluctuation with the crystal's (none) — quantifies "what a b-value anomaly would look like".

### E3.3 Fault stress shadows: a *deterministic* mechanism for repulsion — NEW (roadmap for P1.4)
**Idea:** faults do not nucleate inside the *stress shadow* of an existing fault — a minimum-spacing
effect *provable from elasticity* (deterministic mechanism, not a statistical postulate). The import for
the zero-repulsion hunt ([CD-V17]/[PH-P1.4]): a provable minimum gap for zeros would most plausibly come
from a *local* mechanism — a local identity/inequality inside the explicit formula — not from a global
statistical law. This sets the *target shape* of a repulsion proof.
**Analogy mapped:** stress shadow ↔ a local zero-gap constraint; elasticity ↔ the explicit formula's
local structure; the roadmap: find the "stress field" functional of the explicit formula that forces a
gap at a scale (the known gap bounds are far weaker than the crystal's minimum separation — quantify the
gap between known bounds and what the crystal needs).
**Needs:** none (documented roadmap); a literature note on the strongest known zero-gap bounds and the
crystal's minimal separation (both cheap to assemble).
**Feasibility:** Low.
**Label:** NEW (roadmap; the input itself remains KNOWN-OPEN).
**Cheapest probe (<1h):** assemble the two numbers: best proven zero-gap bound vs the 256-law's minimal
occupied-cell separation; the ratio is the "repulsion deficit" a mechanism would have to close.

### E3.4 Magnetic-anomaly symmetry and the FE: the A2 death in a geological costume — KNOWN-DEAD (documented)
**Idea:** mirrored magnetic anomalies diagnose symmetric spreading; asymmetric anomalies signal
off-axis processes. The FE symmetry (ρ ↔ 1−ρ̄) is our "spreading symmetry"; off-line pairs are the
"asymmetric anomalies" — and the natural detector (odd window, Im W) is *identically zero* by the
symmetry.
**Analogy mapped:** symmetric spreading ↔ FE pairing; the asymmetry detector ↔ Im W ≡ 0 ([CD-A2]).
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-DEAD ([CD-A2]).
**Cheapest probe:** none (recorded; prevents re-derivation).

### E3.5 Plate-circuit closure / triple-junction stability — NEW (framing; content = P2)
**Idea:** plate circuits close consistently (Euler poles compose); triple junctions are stable only for
special geometries — *global consistency constraints* that local data don't reveal. The zeros' "plate
circuit" is the joint constraint set across scales; the crystal *closes the circuit* at two-moment level
for every λ ≤ 1 (E2.6), so the constraint only bites at *higher* moments — i.e., this is P2 under a
geological name.
**Analogy mapped:** plate-circuit closure ↔ cross-scale consistency; triple-junction stability ↔ the
third-moment constraint.
**Needs:** none.
**Feasibility:** Low.
**Label:** NEW (framing; content = P2).
**Cheapest probe:** none (recorded; fold into E2.6/E2.1).

### E3.6 Fault-network fractal dimension: a weak diagnostic — NEW (diagnostic, weak)
**Idea:** fault length distributions are power laws (self-similar networks); the exponent is a network
diagnostic. The correlation dimension of the W_T eigenvalue law is a measured statistic (the
[PH-P10.2] entropy analog).
**Analogy mapped:** network fractal dimension ↔ correlation dimension of the W_T law.
**Needs:** W_T spectra (exists).
**Feasibility:** Low.
**Label:** NEW (diagnostic, weak).
**Cheapest probe (<1h):** correlation dimension of the eigenvalue law at T=100–700 vs the crystal's.

---

## Pool 4 — Hydrology / drainage networks

### E4.1 Horton–Strahler ordering ↔ the derivative tower — NEW (diagnostic; feeds V9)
**Idea:** Strahler order assigns a hierarchy (a stream's order jumps when two equal-order streams merge);
Horton's laws are *empirical scaling ratios* between consecutive orders (bifurcation ratio, length ratio
~ constant). The derivative tower ξ, ξ′, ξ″… is a hierarchy on the *same* zero configuration with
interlacing (Rolle) and rising constants (FGL: 0.858/0.868…). A *ratio* law between levels would be a
joint constraint — but [CD-A4] proved interlacing gives only a *difference* lower bound (no ratio/upper
constraint) ⇒ the ratio form is dead as input. The *measurement* survives: does the constant sequence
across j obey Horton-type geometric growth?
**Analogy mapped:** stream order ↔ derivative order; bifurcation ratio ↔ constant-growth ratio across j;
Horton's laws ↔ empirical scaling of the certificate constants (a diagnostic for [CD-V9]'s tower).
**Needs:** the ξ′/ξ″ constants (V9 machinery) + the FGL pattern.
**Feasibility:** Low–Med (reuse of V9).
**Label:** NEW (diagnostic; A4 noted).
**Cheapest probe (<1h):** fit the known sequence (2/3 → 0.85838 → ?) against geometric growth; report
the "bifurcation ratio".

### E4.2 Drainage density: the two-moment ratio as a robust network diagnostic — NEW (diagnostic, overlaps P6)
**Idea:** drainage density (total channel length per area) is a single robust number characterizing a
network and its environment; *changes* in it signal environmental change. The two-moment ratio 1.3275 is
our "drainage density"; the finite-T measurements (1.265–1.287 [AF]) are the "environmental
realization"; Δ(T) is the "environmental signal".
**Analogy mapped:** drainage density ↔ ‖W‖²/N; environmental change ↔ the T-trend; the hydrologist's
"noise floor" ↔ the window-to-window variance ([PH-P9.1]).
**Needs:** [AF] code extended to adjacent windows.
**Feasibility:** Low.
**Label:** NEW (diagnostic).
**Cheapest probe (<1h):** the [PH-P9.1] variance measurement (does the T-trend of Δ survive the noise
floor?).

### E4.3 Complementary variational principles: primal/dual bracketing, now aimed at *extended* classes — NEW (methodological)
**Idea:** groundwater flow problems admit *dual* (complementary-energy) formulations whose solutions
*bracket* the primal; the complementary-dual *iteration* systematically improves both. The certificate's
LP dual [ALD] is the complementary formulation — but the in-class bracket is now *closed* (tight).
The transferable methodology: the *iteration* applies to *extended* certificate classes — add a new
constraint (third moment, a repulsion input when one exists), re-dualize, iterate — giving a *procedure*
for converting any future proven input into a certificate improvement, rather than a one-shot solve.
**Analogy mapped:** complementary energy ↔ the LP dual; bracketing ↔ the (now closed) in-class gap;
iteration ↔ the improvement cycle on *extended* classes.
**Needs:** the [ALD] machinery; a constraint-extension harness.
**Feasibility:** Med.
**Label:** NEW.
**Cheapest probe (<1h):** one dual-primal iteration at N=256 with a *toy* third-moment constraint (m₃=2);
report whether the new certificate beats 0.6725 (this is [PH-P6.5]'s LP, re-read as an iteration).

### E4.4 Aquifer identifiability / pilot points — NEW (framing; input KNOWN-OPEN)
**Idea:** groundwater inversions are underdetermined; identifiability theory states *what can be
recovered* from given data; pilot-point/zonation methods reduce the parameter space by structural
priors. The analog of zonation = a *structural prior* on the zero configuration (interval/block
structure) — which is the repulsion/rigidity wall (KNOWN-OPEN). The value is the *identifiability
framing*: "what configuration statistics are identifiable from bandwidth-one data?" — the answer (the
two moments, essentially nothing else) is the ceiling theorem's content.
**Analogy mapped:** identifiability ↔ what the certificate class can read; zonation ↔ structural priors.
**Needs:** none.
**Feasibility:** Low.
**Label:** NEW (framing; input KNOWN-OPEN).
**Cheapest probe:** none (documentation).

### E4.5 Flood-frequency / extreme-value statistics — NEW (diagnostic, weak)
**Idea:** flood-frequency analysis fits extreme-value laws (GEV) to maxima; the largest
eigenvalue/gap of the zero configuration ([PH-P4.3]) is the extreme statistic whose "return period" is
the T-scale.
**Analogy mapped:** GEV ↔ extreme statistics of the W_T spectrum.
**Needs:** W_T spectra.
**Feasibility:** Low.
**Label:** NEW (diagnostic, weak).
**Cheapest probe (<1h):** max-gap of the eigenvalue law over T vs the crystal's ([PH-P4.3]'s probe).

### E4.6 Water-budget closure: the P1 wall restated — KNOWN-DEAD-likely (documented)
**Idea:** a basin's water balance is an *identity* (P = R + ET + ΔS) that always closes. The zeros'
"budget identity" is the explicit formula; any *additional* closing identity would be a new constraint —
but the only proven ones are the two moments, and the crystal closes the budget at two-moment level too.
**Analogy mapped:** budget closure ↔ the two-moment identities; a missing "budget term" ↔ the missing
constraint (P1) — which [ALD] shows cannot be in-class.
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-DEAD-likely (P1 wall restated; [ALD]).
**Cheapest probe:** none (recorded).

---

## Pool 5 — Weather forecasting / data assimilation

### E5.1 4D-Var incremental assimilation: crystal as background, prime data as observations — NEW (diagnostic; overlaps [CD-V1])
**Idea:** incremental 4D-Var linearizes around a background, assimilates observations, measures the
*analysis increment*. Analog: start from the extremal crystal as background, "assimilate" the measured
prime-side W_T, measure the increment — its normalized size is a single number whose T-trend is the
readable signal of how far reality sits from the crystal.
**Analogy mapped:** background ↔ crystal; observations ↔ the real W_T; analysis increment ↔ spectral
distance (E1.4's residual).
**Needs:** W_T spectra + W_crystal (both exist/constructible).
**Feasibility:** Low.
**Label:** NEW (diagnostic; overlaps [CD-V1]).
**Cheapest probe (<1h):** the E1.4 residual's Frobenius norm vs T (one number per T).

### E5.2 EnKF localization: the λ=1 wall as the localization radius — KNOWN-DEAD (framing)
**Idea:** EnKF *localizes* covariances (Schur product with a compactly supported function) to kill
spurious long-range correlations — a bias–variance tradeoff. Our off-diagonal control is the
"localization": the certificate trusts pair data only within bandwidth one. Localization theory's knobs:
the *radius* (the "1+ε" question — M29: negative) and the *kernel shape* inside the radius (the window —
cosine-optimal, [AK]). Both knobs are settled.
**Analogy mapped:** covariance localization ↔ MV off-diagonal control; localization radius ↔ λ=1 wall;
localization function ↔ the window.
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-DEAD ([M29], [AK]) — documented DA reading of the two walls.
**Cheapest probe:** none (recorded).

### E5.3 Adjoint sensitivity / observation impact: the pricing sheet for hypothetical inputs — NEW (cheap; extends [ALD])
**Idea:** adjoint methods quantify each observation's impact on the analysis (the gradient). The
certificate's "observation impact" = the gradient of the bound w.r.t. each input. [ALD] already computed
the in-class shadow prices (p₁: price 1; validity constraint: −1; kernel box: −2.54·10⁻⁶). The NEW
deliverable: *extend the pricing sheet to hypothetical inputs* — re-solve the LP with (a) a third-moment
constraint (m₃=2, distinct count), (b) a toy repulsion/min-gap constraint, (c) a beyond-1 F value — and
report the price each would command. This converts the P1/P2/P3 hunt into a ranked *budget*: "a unit of
third-moment data is worth X; a unit of min-gap is worth Y" — and tells us which conjectural input to
fund first (overlaps [CD-V4]'s capacity roadmap, now with actual dual numbers).
**Analogy mapped:** observation impact ↔ certificate sensitivity to inputs; adjoint ↔ LP dual variables.
**Needs:** the [ALD] solver + constraint-extension harness (same as E4.3).
**Feasibility:** Low.
**Label:** NEW.
**Cheapest probe (<1h):** the E4.3 toy-constraint solves — report the shadow prices of the third-moment
and min-gap constraints.

### E5.4 Conditioning of the certificate functional: is the cosine a flat or sharp optimum? — NEW (cheap diagnostic)
**Idea:** the prompt's "butterfly effect" read literally: compute the *second variation* (Hessian) of the
certificate functional at the optimal cosine window. Flat optimum ⇒ the 0.6725 constant is robust to
window perturbations and the bottleneck is arithmetic; sharp optimum ⇒ the window choice is load-bearing
(the paper's Theorem D optimality says *no* window beats it in-class, but the *stability* of the constant
to perturbations is a separate, measurable fact — it tells us how much slack a *slightly wrong* window
implementation could cost, i.e., how fragile the certificate is).
**Analogy mapped:** Lyapunov/conditioning ↔ Hessian of the functional at the optimum; butterfly effect ↔
sensitivity of the constant to the window.
**Needs:** the certificate functional ([AK]'s machinery) + a numeric optimizer.
**Feasibility:** Low.
**Label:** NEW.
**Cheapest probe (<1h):** mpmath finite-difference Hessian at cos(√2u) over window-coefficient
perturbations; report the condition number and the largest eigenvalue's direction.

### E5.5 Forecast-skill attribution: baseline decomposition of the ladder — NEW (framing)
**Idea:** verification decomposes skill into baseline, signal, and ceiling. Our ladder: flat window 2/3 →
cosine 0.6725 → class ceiling 0.6818. Attribution: the window buys 0.6725 − 2/3 ≈ 0.0058 ([AK]'s
content); the arithmetic (exact moment evaluations) buys the rest; the ceiling is now *attained* ([ALD]).
The honest attribution statement — "the window is worth X, the arithmetic Y, and the remaining gap to
0.6818 is now closed as certificate-optimality" — is a clean writeup item and stops funding of in-class
certificate hunts.
**Analogy mapped:** skill score ↔ the certificate gain; baseline ↔ flat window; ceiling ↔ 0.6818.
**Needs:** none (numbers already in hand).
**Feasibility:** Low.
**Label:** NEW (framing).
**Cheapest probe:** none (documentation).

### E5.6 Ensemble-spread vs error consistency: is Δ(T) signal or noise? — NEW (diagnostic, P6)
**Idea:** EnKF checks whether the ensemble spread is *consistent* with the actual error (too-small spread
= filter divergence). Analog: is the finite-T deficit Δ(T) consistent with the theory's own error scale
(B24's O(1/√log T)), or is the measured deficit systematically different? [AF] measured ~1/log T with
single-sample wiggle — the consistency check (compare the wiggle's magnitude with the predicted error
scale) decides whether Δ(T) is "signal" (systematic arithmetic — the certificate has real slack at every
finite T) or "noise" (fluctuation-dominated — the asymptotic constant is approached from above, as [AF]
concludes).
**Analogy mapped:** ensemble spread ↔ the Δ(T) fluctuation; filter divergence ↔ inconsistency with the
theory's error scale.
**Needs:** [AF] data + the B24 error scale.
**Feasibility:** Low.
**Label:** NEW (diagnostic).
**Cheapest probe (<1h):** var(Δ(T)) over adjacent windows vs the B24 O(1/√log T) scale (same probe as
E2.2/E4.2).

---

## Pool 6 — Glaciology / ice sheets

### E6.1 Shallow-ice approximation: the deficit is NOT a thin-layer artifact — NEW (testable disanalogy; P6)
**Idea:** SIA reduces full Stokes to a thin-layer model with provable O(ε²) error (ε = aspect ratio).
The analog: the bandwidth-one truncation's error should scale like a thin-layer parameter (local
spacing/window ratio) — i.e., the finite-T deficit should be a *power law* in the spacing scale. But
[AF] measured ~1/log T — *not* a power law (fit slope 0.12 in log-log vs 1.0 for 1/T). The *disanalogy
is the finding*: the deficit is not a thin-layer truncation artifact; it is pair-correlation/arithmetic
driven — an independent confirmation of [AF] §5's conclusion, and a *prediction* for the C∞-smoothed
window test ([AF] §7): if the C∞ window still gives ~1/log T, the "kernel artifact" hypothesis dies
cleanly.
**Analogy mapped:** aspect ratio ↔ spacing/window ratio; SIA O(ε²) ↔ predicted power-law deficit; the
measured 1/log T ↔ the disanalogy.
**Needs:** [AF] data; power-law ansatz fits (partly in [AF]).
**Feasibility:** Low.
**Label:** NEW (diagnostic; the disanalogy is the content).
**Cheapest probe (<1h):** refit [AF]'s Δ(T) against T^{-θ} (θ free) and log laws; report the rejection of
the SIA-type power law (already half-done in [AF] §5).

### E6.2 Basal-friction inversion: model-based regularization for the missing constraint — NEW (strategic for P1)
**Idea:** basal-slip inversions regularize with *model-based* constraints (the flow law, ice physics),
not arbitrary smoothness; the free boundary (grounding line) is handled via the physics. The import for
P1: the missing constraint, if it exists, should be *derived from the forward model* — i.e., from the
*explicit formula's own structure* (the same configuration must satisfy it for all windows, all test
functions, all derivatives) — not invented as a postulate. Concretely: the cross-window consistency
(E2.6) dies at two-moment level; the *model-based* version is the *higher-moment and derivative-tower*
consistency — pointing at identities *already in the formula* that have not been used (complex test
functions, the tower ξ^(j), multi-window identities). This sharpens the P1 hunt: "look for a *consequence
of the explicit formula*, not an additional hypothesis."
**Analogy mapped:** model-based regularization ↔ constraints derived from the explicit formula; free
boundary ↔ the contact set (P5.1/[ALD]'s active set).
**Needs:** none (strategic).
**Feasibility:** Low.
**Label:** NEW (strategic).
**Cheapest probe:** none (documentation; reframes P1).

### E6.3 Marine-ice-sheet hysteresis: crystal and reality as two stable states — NEW (framing; content = P2/P1.4)
**Idea:** marine ice sheets exhibit hysteresis (two stable states; instability triggered by crossing a
threshold). The zero "system" at fixed two moments has two "stable states": the crystal and reality. The
hysteresis loop's *width* = the gap the certificate cannot close; a perturbation *selects* a branch — any
provable higher-moment/repulsion input selects the real branch and breaks the degeneracy. The new
expectation from hysteresis physics: the degeneracy is broken by the *first perturbation that couples to
the order parameter* — the natural order-parameter coupling here is the skewness (third moment), i.e.,
P2.
**Analogy mapped:** hysteresis width ↔ the crystal-vs-reality gap; threshold crossing ↔ the moment at
which the certificate can distinguish.
**Needs:** none (framing).
**Feasibility:** Low.
**Label:** NEW (framing; content = P2).
**Cheapest probe:** none (fold into E2.1/[PH-P6.5]).

### E6.4 Ice-divide migration: the ξ′ zeros as "divides" — KNOWN-DEAD-likely as input ([CD-A4]); diagnostic value = V9
**Idea:** ice divides migrate as an imbalance diagnostic; the zeros of ξ′ are the "divides" of the |ξ|
landscape. The FGL rising constants (0.858…) are the "divide statistics"; a *joint* divide-to-summit
ratio constraint would be valuable — but [CD-A4] proved interlacing gives only a difference lower bound
(no ratio/upper constraint); and [ATF] shows the ζ′(ρ)-moment form's constant is RH-conditional.
**Analogy mapped:** divide migration ↔ ξ′ zero statistics; imbalance ↔ the ratio N₀,ξ′/N₀,ξ (not usable).
**Needs:** V9 machinery (for the *measured* tower).
**Feasibility:** Low.
**Label:** KNOWN-DEAD-likely as input ([CD-A4]); the measurement is V9's.
**Cheapest probe:** none new (V9's).

### E6.5 Ice-core layer counting: the "dating uncertainty" framing for P6 — NEW (framing)
**Idea:** ice-core chronologies count annual layers; dating uncertainty grows with depth as a random
walk. The zero-counting function's uncertainty (S(t) ~ √(log log t), Selberg) is our "dating
uncertainty"; the crystal's is zero. The import: *deep* (high-T) statements carry irreducible
"dating" error — motivating the effective theorem ([CD-V20]) with a clean physical picture, and setting
the *scale* of the P6 error terms (√(log log T)-class fluctuations, 1/√log T-class B24 errors).
**Analogy mapped:** layer-count uncertainty ↔ S(t) variance; depth ↔ height T.
**Needs:** none (framing).
**Feasibility:** Low.
**Label:** NEW (framing).
**Cheapest probe:** none (documentation; numbers in [AF]/B24).

### E6.6 GIA inversion identifiability — KNOWN-OPEN (weak framing; overlaps E4.4)
**Idea:** glacial isostatic adjustment inversions recover a radial viscosity profile whose *resolution*
is limited (identifiability). Our "profile" is the zero configuration's statistics vs height; the
resolution limit is the bandwidth wall. Weak; overlaps E4.4.
**Analogy mapped:** radial profile ↔ height-dependent zero statistics; resolution limit ↔ λ=1 wall.
**Needs:** none.
**Feasibility:** Low.
**Label:** KNOWN-OPEN (weak framing).
**Cheapest probe:** none (recorded).

---

## TOP 10 (EV × feasibility × cheap-probe) — written against the [ALD]-closed in-class state

1. **E5.3 — Adjoint pricing sheet for hypothetical inputs.** [ALD] priced the in-class data; this prices
   *new* inputs (third moment, min-gap, beyond-1 value) by their shadow prices — the ranked budget for
   P1/P2/P3. Probe: toy-constraint LP solves — under an hour.
2. **E5.4 — Conditioning of the certificate functional.** Is the cosine a flat or sharp optimum? A
   genuinely new, cheap diagnostic of the constant's robustness (second variation). Probe: mpmath Hessian
   — under an hour.
3. **E2.1 — Kolmogorov 4/5-law prior on P2.** The physics precedent that a *third-order* statement can be
   *exact* where second-order is non-universal; reframes P2 as "find the conserved quantity behind
   tr Â³". Probe: none (framing) + the [PH-P6.5] LP.
4. **E1.1 — Normal-mode splitting as the off-line detector (with the E2.5 null threshold).** Calibrated
   diagnostic of how much off-line structure the method would miss; the "RH-ometer" with a significance
   level. Probe: cluster-splitting statistics on existing spectra — hours.
5. **E3.3 — Fault stress-shadow roadmap for repulsion.** Sets the *target shape* of a repulsion proof
   (a local, mechanism-derived gap bound) and quantifies the "repulsion deficit" (best proven bound vs
   crystal separation). Probe: assemble two numbers — under an hour.
6. **E6.1 — SIA disanalogy test.** The deficit is not a thin-layer power-law artifact — a testable
   structural claim about P6 that independently confirms [AF]. Probe: refit [AF]'s Δ(T) — under an hour.
7. **E5.6/E2.2/E4.2 — Ensemble-consistency check (is Δ(T) signal or noise?).** Decides whether the
   finite-T slack is systematic (certificate really has slack) or fluctuation; feeds P6 and the C∞-window
   decision ([AF] §7). Probe: var(Δ(T)) over adjacent windows — hours.
8. **E1.3 — Coda decorrelation of the eigenvalue law.** A second, independent T-window diagnostic of the
   zero configuration's heterogeneity vs the crystal. Probe: density-overlap across adjacent windows —
   hours.
9. **E4.3 — Complementary-dual iteration on *extended* classes.** The methodology for converting any
   future proven input into a certificate improvement (a procedure, since the in-class bracket is closed).
   Probe: one iteration with the toy third-moment constraint — under an hour (shared with E5.3).
10. **E4.1 — Horton's laws for the derivative tower.** Empirical scaling of the certificate constants
    across j; a diagnostic for [CD-V9] and a check on the FGL pattern. Probe: geometric fit of known
    constants — under an hour.

**Strategic reading:** the two strongest NEW contributions are (i) the *pricing sheet extension* (E5.3 —
turning the P1/P2/P3 hunt into a ranked budget, building on the now-computed [ALD] duals) and (ii) the
*Kolmogorov-4/5 prior* (E2.1 — a physics reason to expect P2's third moment to be the *robust* order).
The rest are diagnostics that change what we believe about the method's real slack (E5.4, E1.1, E5.6,
E1.3, E6.1) plus roadmaps (E3.3) and methodologies (E4.3). Nothing here claims to settle RH; the honest
output is a set of cheap probes whose negatives are documented findings. Note the *state shift* vs the
physics/crossdomain catalogs: the in-class certificate hunt (V2/P5.1/P7.6 territory) is now CLOSED by
[ALD], so this catalog deliberately points *past* it (inputs, diagnostics, roadmaps), never re-opening
it.

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

### W-E1. "The zeros are an accretionary wedge in Coulomb equilibrium; RH is the critical taper; the certificate is the yield criterion" — CONJECTURED (framing; content = [ALD])
**For:** wedge criticality is a universal, history-independent bound like the ceiling; the equilibrium is
window-independent like the certificate. **Against:** no new inequality appears; the wedge's criticality
is *attained* ([ALD]) — the geological picture confirms the state, adds no input. **Keep:** the
"criticality attained ⇒ remaining gap is data" statement (E3.1) as a one-line writeup insight.

### W-E2. "The zero configuration is a glacier whose surface is log|ξ|: basal friction = the missing constraint, grounding line = the off-line boundary, marine instability = the crystal-vs-reality gap" — CONJECTURED (framing; content = P1/E6.2)
**For:** the free-boundary vocabulary (grounding line ↔ contact set of the equilibrium problem) has a
real mathematical shadow in [ALD]'s active set. **Against:** there is no "flow law" for zeros; the
mechanics transfer is vocabulary only. **Keep:** the *model-based-regularization principle* (E6.2): the
missing constraint, if any, is a consequence of the explicit formula, not a postulate — the single most
disciplined reading of P1 this catalog produced.

### W-E3. "The zeros obey a turbulence cascade with an exact 4/5-type third-order law — find the 'dissipation rate' ε that tr Â³ fixes" — CONJECTURED (framing; sharpened P2)
**For:** in turbulence the 4/5 law is exact because it follows from *energy conservation*; the analog
question — "what conserved quantity of the explicit-formula structure fixes tr Â³ at λ<2/3?" — is a real
reframing of P2's evaluation ([CD-V3]) with a mechanism-level target. **Against:** the "conservation
law" for the zeros is not identified; the analogy may be purely motivational. **Keep:** the question
itself ("what conservation law makes the RS-range third moment exact?") as the sharpest phrasing of the
P2 evaluation problem.

### W-E4. "The zeros' 'plate circuit' closes only if RH holds — Euler-pole closure forces consistency" — CONJECTURED (likely-false as input)
**For:** the plate-circuit picture is *global consistency from local geometry*, the kind of constraint
the certificate lacks. **Against:** the crystal closes the circuit at two-moment level for every λ ≤ 1
(E2.6, [ALD]); the closure constraint only bites at higher moments — i.e., the claim reduces to P2.
**Honest verdict:** dead as an independent input; E3.5 recorded to prevent re-derivation.

### W-E5. "The 1/log T deficit is an ice-core age-offset random walk: the drift is the accumulation signal, the wiggle the noise — separate them by a Brownian-bridge decomposition" — CONJECTURED (framing; content = P9.1)
**For:** the drift/noise split is exactly the E5.6 consistency question, and a Brownian-bridge-style
decomposition gives a principled *error bar* on the Δ(T) trend. **Against:** the single-sample wiggle in
[AF] is too small a sample for a bridge decomposition; the B24 error scale is the honest prior. **Keep:**
the *error-bar discipline* (report Δ(T) with a theory-scale error band) as a P6 habit.

### W-E6. "Seismic split-mode tomography of the zeros: invert the splitting function of W_T for the off-line density *as a function of spectral depth*" — CONJECTURED (diagnostic; real fragment)
**For:** the eigenvalue-position-resolved off-line density is measurable from W_T's edge structure
(overlaps [CD-V1]/[PH-P1.3]); "spectral depth" is a genuine new coordinate (near the bottom of the
spectrum = near-degenerate clusters = where off-line planes live). **Against:** the inversion is
underdetermined (the two moments don't pin it); it is a diagnostic, not a certificate input. **Keep:**
E1.1 + [PH-P1.3]'s edge-density measurement, relabeled as "splitting-function tomography" — the one wild
vector with a concrete probe.

---

## Label inventory

- **NEW** (invented here, untested; conjectured by construction): E1.1, E1.2, E1.3, E1.4, E1.5, E2.1,
  E2.5, E2.6, E3.1, E3.2, E3.3, E3.5, E3.6, E4.1, E4.2, E4.3, E4.4, E4.5, E5.1, E5.3, E5.4, E5.5,
  E5.6, E6.1, E6.2, E6.3, E6.5, W-E1…W-E6. (Sub-labels: E2.1/E3.3/E4.3/E5.3/E6.2 carry the highest
  expected value; E3.6/E4.5/E6.6 are explicitly weak.)
- **KNOWN-DEAD** (documented in earlier rounds; cited): E1.6 (E1.2 restatement), E2.3 (input; [M29]),
  E2.4 ([CD-A2], [M29]), E3.4 ([CD-A2]), E4.6 (P1 wall; [ALD]), E5.2 ([M29], [AK]), E6.4 ([CD-A4]),
  E2.2-as-input ([CD-V13]; the rate diagnostic survives).
- **KNOWN-OPEN** (core open / flagged in our notes; new framing only): E3.3's repulsion input itself
  ([CD-V17]/[PH-P1.4]), E4.4's structural priors, E6.6.
- **TESTED-OPEN**: E5.6/E2.2/E4.2's variance measurement extends [AF]'s tested Δ(T) > 0 (~1/log T — the
  trend is tested, the asymptote open); E6.1's disanalogy uses [AF]'s data (the C∞-window confirmation is
  the open step [AF] §7).
- **Cheapest-probe discipline:** every vector above has a <1h probe (existing [AF]/[CD-V1] spectra, the
  [ALD] LP machinery, or a two-number literature/data assembly). Nothing requires new heavy compute to
  start.

**Honest closing note:** relative to the physics/crossdomain catalogs, this catalog's highest-value NEW
contributions are (i) the *pricing-sheet extension* (E5.3) that turns the P1/P2/P3 hunt into a ranked
budget using the now-closed [ALD] duals, and (ii) the *Kolmogorov-4/5 prior* (E2.1) that gives a physics
reason to expect P2's third moment to be the robust order. The persistent wall — beyond-1 form factor,
third moments, repulsion — is unchanged by earth-science vocabulary, but two of its faces now carry
sharper targets: a *mechanism shape* for a repulsion proof (E3.3, from fault stress shadows) and a
*conservation-law phrasing* for the third moment (E2.1/W-E3, from the 4/5 law). The in-class certificate
question is closed ([ALD]) and this catalog does not reopen it.
