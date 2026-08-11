# Idea Generator: music theory & linguistics attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (creativity + analogy-domain-transfer + pattern-detection). Round 1, far-field pools.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack; every probe is cheapest-first (<1h).
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Music/linguistics facts below are
standard domain knowledge (textbook-level) and are named as such; anything I cannot vouch for at that level is flagged
**"reported standard — verify before use."** Every *idea* is CONJECTURED by construction and carries a kill criterion.
Vectors already killed during generation are recorded with the reason so executioners don't re-derive the death.
**Labeling (per physics-catalog convention):** NEW (invented here, untested) / KNOWN-DEAD (killed in earlier rounds;
cited) / KNOWN-OPEN (a known open problem or a route already flagged in our notes; cited) / TESTED-OPEN (numerically
tested by our own tools or attack notes, still open).
Cross-references: idea-generator-crossdomain.md [CD-V#/W#/A#], idea-generator-physics.md [P#.#], attack-kernel [AK],
attack-lpdual [ALPD], close-inclass-gap [CIG], attack-twobandwidth [ATB], attack-qi-sweep [AQI], attack-nevanlinna
[AN], attack-multiplicity [AM], attack-finitet [AF], attack-f1curve [AF1], attack-vector-catalog [AVC].

---

## 0. The honest map of where we stand (what new *input* could move what — in plain English)

State of the art (PROVEN): the two-moment certificate gives ≥ 0.67250070 (Theorem D; cos(√2u) window optimal, [AK]);
the bandwidth-one certificate class is **closed**: the in-class optimum is 0.68183123 = p₀ + 1/(6·256²) − δ, attained by
the exact rational certificate r(x) = 1 − x (PROVEN, [CIG]); the ceiling `ceiling_law256_signed` is tight (PROVEN Lean,
[AC]); the shadow price of the certified simple fraction p₁ is exactly 1 ([ALPD]) — **nothing inside bandwidth one moves
the constant**. The distinct wall 5/6 is hard for two moments, and the empirically-true world (all simple) is exactly the
certificate's worst case ([AM]). The two-bandwidth joint certificate is a documented clean negative (m₃(1/2) = 5, max
0.8071 < 5/6; [ATB]). QI inequality sweep: negative ([AQI]). Nevanlinna reframe: negative ([AN]).

Therefore (the same conclusion the physics catalog reached, restated): any *constant* gain needs (a) beyond-bandwidth-1
form factor F(α), α > 1 (conjectural, HL-strength), (b) higher-order correlations (the P2 third-moment question), (c) a
proven repulsion/rigidity input (P1.4 — open), or (d) a new *target* with proven machinery (derivative tower, P5).
Finite-T error terms (P6) and the measured slack are diagnostics that change what we believe, not the constant.

**What a far-field pool can realistically contribute, ranked by ambition:**
1. *New proven-input-adjacent vectors* (the rare ones — M5.4, M4.3, M4.1 below).
2. *New diagnostics* (measure how far reality sits from the extremal law on statistics the certificate does not read —
   M2.5/M3.1/M3.3, M2.3, M2.2, M6.1–M6.3 — they change what we believe and price future inputs).
3. *Framings that stop re-derivation* (named pattern → its playbook is either already executed or provably blocked —
   M3.4, M4.2, M4.6, M6.6, M5.2, M5.3).
The persistent wall (beyond-1 F, third moments, repulsion) is *phase* information that a two-moment intensity
certificate cannot see [P6.4]; the music/ling pools independently arrive at the same wall through *tuning*, *masking*,
*meter*, *phonotactics*, and *grammar-power* — which is itself evidence the wall is structural, not technical.

---

## Pool M1 — Music theory / harmony

### M1.1 The overtone series as the moment hierarchy; "beating" of the zero spectrum — NEW (diagnostic)
**Idea:** A harmonic tone's partials sit at integer multiples: 2:1 octave, 3:1 twelfth, 4:1 double octave (standard). Map
the *moment tower* onto the harmonic series: moment k ↔ partial k, GUE values m_k = (1, 4/3, 2, 13/4, …) ↔ the "pure
tuning" the zeros would have under RH+pairs. Two mistuned partials produce *beating* — a slow amplitude modulation at
the frequency difference.
**Analogy → our setting:** the *measured* finite-height moments m_k(T) are "partials" of the zero spectrum; their
mistuning Δm_k(T) = |m_k(measured) − GUE value| is the *beating* of the spectrum. We already know m₃(measured) ≈ 4.8 vs
GUE 2 at finite height ([ATB] §2) — a large mistuning of the "third partial," consistent with the m₂ finite-height
deficit pattern. The NEW step: measure the *T-trend* of Δm₂ and Δm₃ (do they decay like 1/log T, i.e. "in-tune" in the
limit?) — a *tuning curve* of the zeros that tests whether the moment hierarchy is converging to GUE at all.
**What it needs:** real zero data (cached, 34 digits, and computed up to ~10⁴) + the moment estimators (m₂, m₃ exist as
scripts; m₄ to add).
**Feasibility:** Low (compute). **Kill:** if Δm_k does not decay with T, the moment route to GUE values is not just
unproven but empirically unsupported — a documented negative for P2.
**Cheapest probe (<1h):** extend the existing m₃ scripts to T = 200…10⁴, plot Δm₂(T), Δm₃(T), fit the decay exponent.

### M1.2 The audio phase problem ↔ the two-moment intensity certificate — KNOWN-OPEN (reframe of [P6.4]; NEW fragment)
**Idea:** A waveform is not recoverable from its magnitude spectrum alone — phase is missing (standard acoustics). For
*steady-state* tones the phase is largely perceptually irrelevant (that is why magnitude-only sinusoidal synthesis
sounds right for sustained timbres); phase matters for *transients* — onsets, attacks, noise bursts (standard).
**Analogy → our setting:** the two moments (tr, ‖·‖²) are "magnitude-squared" (intensity) data; the beyond-1 form
factor and third moments are the "phase" — already stated [P6.4]. The NEW fragment: in audio the phase information that
matters is carried by *transients*; for us the "transients" are the finite-T boundary/edge terms (the C⁰ window's
Fisher–Hartwig jump, [P5.5], [AF]). So the *finite-T deficit is the phase-carrying window* — a concrete prediction:
decompose the finite-T deficit and the "phase-like" (edge-straddling) part should be the part that smoothing a C∞
window removes (this is exactly M2.4's probe).
**What it needs:** nothing new — M2.4's decomposition.
**Feasibility:** Low. **Kill:** if the edge-decomposition shows the deficit is *not* edge-dominated, the "transient"
reading of P6 is wrong (still a useful negative: the deficit is then a bulk/arithmetic effect).
**Cheapest probe:** folded into M2.4 (<1h).

### M1.3 Harmonic entropy ↔ spectral-structure ambiguity statistic — NEW (diagnostic; fact flagged)
**Idea:** "Harmonic entropy" (Erlich/Sethares — *reported standard, verify before use*) measures the ambiguity of a
pitch interval by the entropy of the clustering of coincident partials of the two tones; a simple ratio has sharply
clustered coincidences (low entropy), a complex ratio spreads them (high entropy). It is a *measure of spectral
structure*, not a model of the ear.
**Analogy → our setting:** a configuration's "interval spectrum" is its pair/gap distribution. The crystal (256-periodic)
has *perfectly clustered* structure (zero-entropy periodicity); GUE has a smooth, structureless pair correlation. NEW:
compute the *harmonic-entropy-style statistic* of the real zero configuration's normalized gap/pair distribution and
report where reality sits between the crystal (low) and GUE (high). If reality is high-entropy (GUE-like), the crystal
is "audibly" implausible as a model of the data — a diagnostic that the ceiling law is a pure combinatorial artifact.
**What it needs:** cached zeros; a small entropy estimator on the pair-coincidence histogram.
**Feasibility:** Low. **Kill:** entropy is not provable from the two moments, so this can never enter a certificate —
it only calibrates belief (label says diagnostic; do not over-fund).
**Cheapest probe (<1h):** histogram of normalized pair distances; Shannon entropy of the binning at several scales; compare crystal vs GUE vs reality.

### M1.4 Voice leading as optimal transport ↔ Wasserstein distance of reality from the extremal law — NEW (diagnostic)
**Idea:** Voice leading maps one chord to another with minimal total pitch movement; the minimal motion between chords is
an optimal-transport (assignment) problem on the pitch line/circle (standard music theory; Tymoczko-style geometry).
**Analogy → our setting:** treat a *window of zeros* as a "chord" and the 256-law's local pattern as the reference
"chord"; the minimal transport cost between the real window and the nearest crystal-compatible configuration is the
*voice-leading distance from reality to the extremal law*. The projection ("nearest crystal configuration matching the
two moments") is computable with the existing LP machinery ([ALPD]/[CIG]).
**What it needs:** the W_T/finitet data + a small assignment/LP solve.
**Feasibility:** Low–Med. **Kill:** if the transport cost is O(1) per window (reality is far from the crystal at every
window), the crystal is a poor geometric model of reality — a diagnostic; if it is small, the crystal is locally
"close" to reality (supports the ceiling's robustness). Either way a measurement, not a certificate input.
**Cheapest probe (<1h):** 1D Wasserstein distance between one window's ordinates and the best-fit 256-periodic pattern (scipy.optimize / closed form for 1D transport).

### M1.5 Just intonation's rational lattice ↔ near-rational ordinate detection — NEW (diagnostic)
**Idea:** Just intonation tunes notes to simple frequency *ratios* (3:2, 4:3, 5:4…), forming a rational lattice
(Tonnetz); equal temperament detunes everything slightly to make the lattice closed (standard).
**Analogy → our setting:** GUE/Montgomery predict the zeros' normalized ordinates carry *no* rational structure. NEW:
test the *rationality hypothesis* directly — histogram how close real normalized ordinates (or their pairwise ratios)
come to simple rationals p/q (small q) at resolution ~1/log T; the GUE null predicts no enhancement over random.
**What it needs:** cached zeros; a nearest-rational search.
**Feasibility:** Low. **Kill:** if no enhancement (expected under pair-correlation conjecture), a documented negative
for "the zeros are harmonically rational"; if enhancement appears, a striking finding worth escalating.
**Cheapest probe (<1h):** for each of ~10⁴ pairs, distance of (γᵢ−γⱼ)·N/T to the nearest p/q, q ≤ 8; histogram vs uniform.

### M1.6 Voicing/spacing ↔ the multiplicity-ambiguity reframe of the 5/6 wall — KNOWN-OPEN (reframe of [AM]; NEW fragment)
**Idea:** A chord's *voicing* — open (spread) or closed (clustered) — changes its sound without changing its pitch
classes (standard). The 5/6 distinct wall says the all-simple world and the "2/3 simple + 1/6 double" world are
spectrally identical at (tr, ‖·‖²) ([AM], PROVEN).
**Analogy → our setting:** the two worlds are *voicings of the same chord* — closed voicing (doubles as clustered
simples) vs open (spread simples). The NEW fragment: write the explicit *revoicing map* — split each double mark into
two simples at separation δ ~ c/N (c small) — and check numerically that the revoicing preserves (tr, ‖·‖²) to the
certificate's tolerance. This makes the wall's mechanism *physical* and identifies the *separation scale* c below which
the certificate cannot hear the difference — the same c that M2.2 (masking width) measures from the other side.
**What it needs:** synthetic configurations + the two-moment computation ([AF] code).
**Feasibility:** Low. **Kill:** if revoicing at *any* c > 1/N breaks the two moments, the wall is thinner than stated
(a real finding); if it survives for a range of c, the voicing-ambiguity picture is confirmed (documentation).
**Cheapest probe (<1h):** synthetic 256-law, split doubles at c ∈ {0.1, 1, 10}·(1/N), recompute tr and ‖·‖².

### M1.7 Well-formed scales / Myhill property ↔ a structural constraint on the extremal law itself — NEW (probe; fact flagged)
**Idea:** Carey–Clampitt *well-formed scales* are generated by a single interval and satisfy the Myhill property: every
generic interval size comes in exactly two specific sizes (e.g., a diatonic scale has two step sizes) — *reported
standard, verify before use*; linked to Sturmian words and continued fractions.
**Analogy → our setting:** the 256-law is a marked lattice — does its *gap set* satisfy a two-sizes property? If the
extremal law is "well-formed," the theory of well-formedness (generation by one generator, continued-fraction
parameterization) constrains the *family of extremal laws* — potentially narrowing the class of ceiling-realizing
configurations and hence the certificate-search space (the class-optimal certificate is already known [CIG], but the
*parameterization* of all ceiling laws is open).
**What it needs:** the law's gap statistics (computable from LawN256 data, [AC]/[CIG]).
**Feasibility:** Low. **Kill:** if the gap set has more than two sizes (not Myhill), the analogy fails — documentation;
if it holds, the extremal-law family may have a closed parameterization worth one LP re-solve.
**Cheapest probe (<1h):** compute the multiset of specific intervals (gap sizes, and 2-gap sums) of the 256-law from its
rational data; count distinct sizes.

---

## Pool M2 — Acoustics / psychoacoustics

### M2.1 Critical bands / constant-Q cochlea ↔ certificate resolution; the log-T "ear" — NEW (framing + TESTED-OPEN extension of [AF])
**Idea:** The ear resolves frequency only within *critical bands* (~1/3 octave, constant-Q at high frequencies); the
cochlea is a tonotopic filter bank (standard psychoacoustics).
**Analogy → our setting:** the bandwidth-one constraint is the certificate's *critical band* — but it is *absolute*
(λ ≤ 1), whereas the *effective* finite-T resolution is ~1/log T, i.e. *constant-Q in log T* — the certificate's ear is
log-frequency, like the cochlea. The measured deficit Δ(T) ≈ c/log T ([AF]) is exactly a constant-Q (logarithmic)
resolution law. NEW: check the *constant* — fit Δ(T) = c/log T over T = 100…700 and test whether c is stable (the
Fisher–Hartwig jump constant, [P5.5]) or drifts; a stable c is a *prediction* for the smoothed-window experiment (the
C∞ window should kill the jump constant and expose the residual arithmetic part).
**What it needs:** [AF]'s existing Δ(T) data + a two-parameter fit.
**Feasibility:** Low. **Kill:** if c is unstable, the 1/log T law is not the right ansatz (a finding for P6).
**Cheapest probe (<1h):** fit log-law to the [AF] table; report c and residuals.

### M2.2 Masking ↔ the certificate's blindness radius; the masking width of a (1,1)-plane — NEW (probe; overlaps [P10.4])
**Idea:** A loud tone raises the detection threshold for neighbors within its masking region; the masking curve is
asymmetric (steep high-frequency side) (standard).
**Analogy → our setting:** an off-line pair (a (1,1)-plane) "masks" the certificate's ability to count nearby on-line
zeros. NEW: quantify the *masking width* — at what separation s does a synthetic (1,1)-plane stop degrading the
certificate's positive-index count? Compute the joint n₊ of p planes as a function of their mutual separation (the
subadditivity probe already spec'd as [P10.4]); the *radius* at which n₊ drops below p is the certificate's
*blindness radius* — the scale below which off-line structure is invisible (and hence unpriced) by the method.
**What it needs:** the Ψ-formula machinery ([AF], [P10.4] probe).
**Feasibility:** Low. **Kill:** if n₊ = p for all separations above exact coincidence (likely — the worst-case bound is
tight, [AM] `lemmaR_tight`), the blindness radius is ~0 and the masking picture is vacuous — but that *is* the
documented finding: the certificate is blind only to exactly-coincident structure, which is why only a *sparsity/local-
clustering input* (P1.4) could ever help. (The masking language makes the needed-input shape precise: a *sparsity +
locality* bound on off-line pairs, not a global repulsion.)
**Cheapest probe (<1h):** two synthetic planes at separation s ∈ {0.1, 0.5, 1, 5}·(1/N); joint n₊ vs 2.

### M2.3 Plomp–Levelt / Sethares consonance curves ↔ pair correlation with a bump kernel; rational-α dips — NEW (probe)
**Idea:** Plomp–Levelt (1965): the sensory dissonance of two tones as a function of frequency ratio has maxima/minima
at simple ratios; Sethares generalized it to arbitrary spectra: dissonance = Σ over partial pairs g(|fᵢ−fⱼ|) — literally
a two-point correlation of a spectrum with a *bump* kernel (standard; this is the task's own hint).
**Analogy → our setting:** our form factor F(α) is the same object (pair correlation with the window kernel). The
consonance theory's content: *harmonic* spectra have *structure at rational α* (dips at 2:1, 3:2, 4:3…). GUE predicts
F ≡ 1 — no rational structure. NEW: *measure* the real pair correlation at rational α ∈ {1/2, 1/3, 2/3, 3/4, 3/2, 2}
with smoothing width ~1/log T; test flatness vs dips. Expected: flat (GUE-consistent); a dip would be a genuine anomaly
worth escalation.
**What it needs:** [CD-V6]/[AF1]-style pair-correlation code, run at rational α.
**Feasibility:** Low. **Kill:** flat everywhere → documented negative for "the zeros are harmonically structured";
any dip → escalate (contradicts the pair-correlation conjecture at that α).
**Cheapest probe (<1h):** pair correlation at the six rational α values, width 1/log T, from cached/computed zeros.

### M2.4 Temporal masking (forward/backward) ↔ window-edge artifacts; edge decomposition of the deficit — NEW (probe)
**Idea:** Masking is temporal too: a masker hides what comes *after* (forward) and, more briefly, *before* (backward)
it (standard). For a windowed certificate, the window's own edges are the "temporal maskers."
**Analogy → our setting:** the C⁰ cosine window has a hard cutoff at ±1/2 (the [AF]/[P5.5] Fisher–Hartwig jump). NEW:
decompose the finite-T deficit Δ(T) by *which pairs cause it* — split the Ψ₂ pair-sum ([AF]) into (a) pairs both inside
the window, (b) pairs straddling an edge, (c) pairs at the edges via the kernel's boundary values. Prediction: the
edge-straddling part (the "temporal masking") dominates and is removable by a C∞ window; the residual is the arithmetic
(pair-correlation) part. This gives a *quantitative decomposition* of P6's error with a testable prediction.
**What it needs:** [AF]'s finitet code (a small modification to the pair-sum loop).
**Feasibility:** Low. **Kill:** if the deficit is *not* edge-dominated, the Fisher–Hartwig picture of the deficit is
wrong (a finding for [P5.5]); if it is, the smoothing experiment has a quantitative target.
**Cheapest probe (<1h):** re-run the [AF] pair-sum with pair-straddle flag; report the straddle fraction of Δ(T).

### M2.5 Missing fundamental / virtual pitch ↔ the crystal's hidden periodicity; periodicity-strength scan — NEW (diagnostic)
**Idea:** The ear recovers a *period* from a set of partials even when the fundamental is absent — virtual pitch
(Schouten/Terhardt, standard).
**Analogy → our setting:** the two-moment data are "partials" from which a *virtual periodicity* (the 256-law) is
compatible — the ceiling is a *virtual-pitch ambiguity* (same content as the phase-retrieval reframe [P6.4], new
vocabulary). NEW fragment: measure whether the *actual data* carry any evidence of that periodicity — the
autocorrelation of the zero sequence (marks = 1) over periods p ∈ [2, 512] (normalized). The crystal has a delta peak
at p = 256; GUE has none; reality's scan tells us whether the ceiling law is "audible" in the data at all.
**What it needs:** cached zeros; an autocorrelation scan (the same battery as M3.1).
**Feasibility:** Low. **Kill:** if reality shows no periodicity peak anywhere, the crystal is a pure combinatorial
artifact — a diagnostic that supports funding the beyond-1/repulsion routes rather than crystal-killing ones.
**Cheapest probe (<1h):** autocorrelation of the rescaled ordinate sequence at p ∈ {2,4,…,512}; report max normalized peak.

### M2.6 Cochlear compression ↔ the inertia map; sensitivity at the threshold edge — KNOWN-OPEN (framing; reframe of [P1.3])
**Idea:** The cochlea compresses a huge dynamic range into a small perceptual range via nonlinear gain; sensitivity is
steepest near threshold (standard).
**Analogy → our setting:** n₊(W_T) compresses N eigenvalues into one count; the "threshold" region is the
small-eigenvalue edge, where the certificate's sensitivity is concentrated. The near-rank-deficiency of the measured
W_T (min eigenvalue ~1e-17·λmax, [AF]) is the "threshold" — and the edge density is the direct, unconditional
measurement of off-line-pair content ([P1.3]/[CD-V1]). NEW contribution: nothing beyond [P1.3] — recorded so the edge
diagnostic is not re-derived under a new name.
**Feasibility:** none (documentation). **Cheapest probe:** none.

---

## Pool M3 — Rhythm / meter

### M3.1 Hierarchical meter (beats, subdivisions) ↔ multi-scale structure; the meter scan — NEW (diagnostic)
**Idea:** Western meter is a nested grid: measure → beat → subdivision (standard). The *strength* of a beat at each
level is measured by accent pattern autocorrelation.
**Analogy → our setting:** GUE predicts the zeros are *metrically uniform* — no hierarchy at any scale; the crystal has
a single grid at 256. NEW: the *meter scan* — subgrid autocorrelation at ratios {1/2, 1/3, 2/3, 1/4, 3/4} of candidate
periods, i.e. the "beat strength" of each subdivision. If reality is flat at every level, the zeros are metrically
featureless (GUE-consistent); any peak is a hierarchy — an anomaly.
**What it needs:** same battery as M2.5.
**Feasibility:** Low. **Kill:** flat (expected) → documented; peak → escalate.
**Cheapest probe (<1h):** fold into M2.5's scan (add the subgrid ratios).

### M3.2 Syncopation / microtiming ↔ deviations from the best-fit grid; the syncopation score — NEW (diagnostic)
**Idea:** Syncopation = accent on an off-beat — a deviation from the grid's expectation; human performance also has
correlated microtiming deviations from the metronome (standard music cognition).
**Analogy → our setting:** the real zeros' deviation from their best-fit periodic grid is "syncopation." NEW: the
*syncopation score* — total squared deviation from the best periodic fit, normalized (a single number per window) — and
the *microtiming correlation* — the correlation structure of the deviations (which IS the pair correlation, already
measured [CD-V6]). The score is a new summary diagnostic: if reality is highly syncopated at every period, no periodic
law models it well (the crystal is a poor model of the data).
**What it needs:** best-fit periodic grid (a small optimization) + [AF] data.
**Feasibility:** Low. **Kill:** score is not provable from the moments — diagnostic only.
**Cheapest probe (<1h):** fit period 256 grid to a real window; report normalized syncopation energy vs the crystal's (≈ 0).

### M3.3 Rhythmic oddity (Toussaint) ↔ aperiodicity of the mark/gap sequence — NEW (diagnostic; fact flagged)
**Idea:** Toussaint's *rhythmic oddity*: a rhythm is "odd" if no rotation divides it into two equal halves (used for
Afro-Cuban clave analysis) — *reported standard, verify exact definition before use*.
**Analogy → our setting:** the crystal is *periodic* (not odd — it has a period-halving rotation at 128, 64, …); reality
is aperiodic (odd). NEW: the *oddity battery* — count the period-halving rotations of the real gap sequence and the
crystal's; report the "oddity" (0 for the crystal, ~maximal for aperiodic data). Diagnostic that quantifies, in rhythm
language, how un-crystal-like the real sequence is.
**What it needs:** the real ordinate sequence (marks = 1); a rotation-autocorrelation routine.
**Feasibility:** Low. **Kill:** diagnostic only; if reality *is* oddly periodic at some period, escalate (an anomaly).
**Cheapest probe (<1h):** rotation-invariance statistic of the real gap sequence over all shifts; compare with the 256-law's.

### M3.4 Hemiola (3 against 2) ↔ the two-window joint certificate — KNOWN-DEAD ([ATB], executed clean negative)
**Idea:** A hemiola is 3 notes in the space of 2 — two meters heard at once (standard). The two-bandwidth joint
certificate [P6.5] is the "hemiola" of the certificate: window at λ = 1 (duplet) + window at λ = 2/3 (triplet; the RS
range kλ < 2 forces λ < 2/3, so the hemiola ratio is exactly the admissible boundary).
**Death (documented, [ATB]):** the correct third moment is m₃(1/2) = 5 (not 2); the admissible-cubic construction gives
0.7593 at λ = 1/2 and 0.8071 at λ = 2/3 — both below 5/6; 5/6 is reached only at λ = 1 where the third moment is not
unconditionally available; no cross-window Schur–Horn-type inequality exists. **The hemiola window at λ = 2/3 does not
break the distinct wall.** Recorded so the rhythm framing is not re-funded as new.
**Cheapest probe:** none (already executed).

### M3.5 Gap-entropy / rhythmic-complexity measures ↔ a third statistic — NEW (diagnostic)
**Idea:** Rhythmic complexity is often measured by the entropy of the inter-onset-interval (gap) distribution, or of the
binary onset sequence (standard-ish; several such measures exist).
**Analogy → our setting:** the crystal's gap set is finite (lattice — low/zero entropy); GUE's gap distribution is known
(Wigner); reality's is measurable. NEW: gap-distribution entropy + the Kolmogorov–Smirnov distance of the real gap
distribution to the crystal's gap set — a model-free "surprisal" summary (overlaps M6.2/M6.3, one battery).
**What it needs:** cached zeros; entropy/KS routines.
**Feasibility:** Low. **Kill:** entropy is not provable from two moments — diagnostic only.
**Cheapest probe (<1h):** KS distance of the empirical gap distribution to (a) the crystal's gap set, (b) the Wigner law.

### M3.6 Swing / groove statistics ↔ cross-window fluctuations; var(Δ(T)) — TESTED-OPEN (extends [AF])
**Idea:** Groove/microtiming research studies the *correlation structure of timing deviations across voices and over
time* (standard music cognition).
**Analogy → our setting:** the cross-window correlation of the finite-T deficit — var(Δ(T)) over adjacent T-windows and
its lag-1 autocorrelation — is the "groove" of the certificate. This feeds the almost-everywhere program ([P9.1]: a
measure-theoretic 67.25% statement) with its fluctuation data.
**What it needs:** [AF]'s finitet code run over multiple adjacent windows.
**Feasibility:** Low. **Kill:** if var(Δ) does not decay, the a.e.-certificate target is empty (a finding for [P9.1]).
**Cheapest probe (<1h):** [AF] code at several adjacent T; report var and lag-1 autocorrelation of Δ.

---

## Pool M4 — Linguistics / phonology

### M4.1 Distinctive features / markedness ↔ marks {0,1,2}; price the "no doubles within δ" constraint — NEW (probe)
**Idea:** Phonology represents segments as feature bundles ([±voice], [±nasal], …); *markedness* says some bundles are
universally dispreferred ("marked") — e.g. voiced obstruents are marked relative to voiceless ones (standard
phonology; the specific universal is contested — use as intuition only).
**Analogy → our setting:** the marks {0, 1, 2} are feature values; "doubles are marked" is the intuitive content of the
missing multiplicity input (P1). The LP says any upper bound on the non-simple fraction transfers **1:1** into the
constant (p₁ shadow price = 1, [ALPD]). NEW: compute the *pricing curve* — solve the certificate LP with the
parametrized family "no two doubles within distance δ" (δ ∈ {0, 1, 2, 4, 8}·(1/N)) and report the certified simple
fraction as a function of δ. This prices *any future* repulsion-on-doubles input exactly (overlaps [P1.4]'s pricing
from the other side).
**What it needs:** the [ALPD]/[CIG] LP with a min-gap-on-doubles constraint (small modification).
**Feasibility:** Low. **Kill:** if even δ = 8·(1/N) does not move the value, doubles-separation inputs are worthless
(a documented negative for the whole class of "doubles are marked" inputs).
**Cheapest probe (<1h):** perturb the 256-law LP: forbid adjacent doubles, re-solve, read the new fraction.

### M4.2 Phonotactics ↔ the admissible-configuration grammar — KNOWN-DEAD (as an input route; documentation)
**Idea:** Phonotactics = the constraints on which sound sequences are well-formed (no "tk" onset in English) (standard).
**Death (documented):** the "grammar" of the certificate (the constraint set {validity at the law's rows, r(1) = 0,
box |r| ≤ 1, slope/curvature budgets}) is *complete inside bandwidth one*: the LP attains the ceiling exactly, and no
missing constraint exists in the class ([ALPD] §5, [CIG]). "Find the missing constraint inside bandwidth one" is
concluded — do not re-fund. The only "ungrammatical" (over-admitted) configurations are those differing in beyond-1 /
third-moment structure.
**Cheapest probe:** none.

### M4.3 Sonority Sequencing Principle ↔ the pointwise F ≥ 0 gradient (re-fund V11 with the proven positivity) — KNOWN-OPEN (reframe of [CD-V11]/[P11])
**Idea:** The Sonority Sequencing Principle: within a syllable, sonority rises to the peak then falls — a *gradient*
ordering constraint that phonologists derive from phonetic "substance" (aerodynamics), not stipulation (standard
phonology).
**Analogy → our setting:** the zeros' "aerodynamic substance" is the *proven* pointwise non-negativity F(α) ≥ 0 for
*all* α (L² representation; unconditional, [CD-V11]). The certificate currently flattens this gradient into two
integrated values; the SSP suggests the *pointwise* family (a constraint at every α ∈ (1, 2)) is the gradient that
should be read, not just the integrals. This is exactly the CGdL20-style SDP ([CD-V11]/[P11]): run the LP with the
*unconditional* pointwise F ≥ 0 constraints outside [0,1] and check whether the value exceeds 0.6725. The SSP framing
adds motivation (a gradient of proven constraints, not a single new datum) but no new math — label KNOWN-OPEN, cite
[CD-V11]/[P11]; do not re-derive.
**What it needs:** the V11/P11 first step (CGdL20 SDP with B24 constraints).
**Feasibility:** Med. **Kill:** [P11]'s kill criterion (error terms force value back to ≤ 0.6725).
**Cheapest probe (<1h):** re-check [P11]'s spec exists; run the SDP with the unconditional pointwise rows.

### M4.4 Optimality Theory / recursive constraint demotion ↔ certificate-discovery heuristic — NEW (search heuristic)
**Idea:** Optimality Theory: a grammar is a *ranked* set of *violable* constraints; the output is the candidate that
best satisfies the ranking (Prince & Smolensky 1993). *Recursive constraint demotion* (RCD, Tesar & Smolensky) learns a
ranking from data by demoting constraints the current winner violates (standard OT).
**Analogy → our setting:** the certificate is a ranked constraint system (moments > integrality > window-box); the
extremal law is the optimal candidate. NEW: use RCD as a *discovery heuristic* for the *enlarged* certificate classes
(the third-moment LP, the two-window LP, the beyond-1 conditional LP) — start from the two-moment certificate, demote
constraints the data violate, promote new ones (third moment), iterate. The LP is already optimal in-class [CIG]; the
heuristic's value is *constructive search* in the not-yet-formulated enlarged classes, where the constraint sets are
still being enumerated.
**What it needs:** a small RCD implementation over the (tr, ‖·‖², tr Â³, integrality) family; the LP machinery to
validate.
**Feasibility:** Low–Med. **Kill:** if RCD's output always coincides with the LP optimum (likely in-class), its value
is limited to the enlarged classes — a scoping finding, not a failure.
**Cheapest probe (<1h):** RCD on synthetic configurations with three candidate constraints; compare with the LP optimum.

### M4.5 Gold's theorem / learnability ↔ the ceiling as an unlearnability result; the k-moment ceiling theorem — NEW (new theorem type)
**Idea:** Gold (1967): any language class containing all finite languages plus one infinite language is not learnable
from *positive evidence alone* (standard computational linguistics).
**Analogy → our setting:** the two-moment data are "positive evidence" that provably cannot separate the crystal from
GUE (the ceiling); the third moment is a second *evidence type*. NEW: frame the ceiling as a *learnability* theorem and
aim for the natural generalization: **the k-moment ceiling theorem** — "a certificate reading the first k moments
cannot certify more than a computable bound" (k = 2 gives 0.6818, PROVEN; k = 3 is open and is P2/V3's question in
disguise; ∞ gives 1 conditionally). Gold's *proof method* (diagonalization against bounded hypotheses) is a template
for such limitation proofs — the ceiling [CIG] is already one instance; the k = 3 case would be priced by the V4
capacity LP ([CD-V4]).
**What it needs:** nothing new to *state*; the k = 3 case is the P2 program.
**Feasibility:** Med (the theorem is a new target; the LP prices each rung). **Kill:** if the V4 LP shows the third
moment cannot move the distinct wall (the crystal's S₃ is near-GUE), the hierarchy collapses at rung 3 — a clean
negative (this is exactly V4's probe, [CD-V4]).
**Cheapest probe (<1h):** the V4 probe (the 256-law's triple-correlation statistic vs GUE value).

### M4.6 Phonological conspiracies (Kisseberth) ↔ the constraint conspiracy of the ceiling — KNOWN-DEAD (documentation; strategic)
**Idea:** Kisseberth's *conspiracies*: independent constraints can conspire to produce the same output pattern (standard
phonology).
**Analogy → our setting:** the ceiling's active constraints (validity row, box at r(0), slope/curvature budgets)
*conspire* to pin the value at 0.68183123 ([ALPD] §4 — the box alone caps it; the curvature saturates degenerately).
The conspiracy is *complete inside bandwidth one*; it breaks only with a new *constraint type* (moments, beyond-1,
repulsion). Strategic statement: any single-constraint tinkering inside the class is exhausted — document, do not
re-fund.
**Cheapest probe:** none.

---

## Pool M5 — Syntax / formal grammar

### M5.1 Chomsky hierarchy / bounded lookahead ↔ the certificate-power hierarchy — NEW (organizing; new theorem type)
**Idea:** The Chomsky hierarchy classifies grammars by generative power; bounded-lookahead parsers (LL(k)) provably
cannot recognize all context-free languages (standard formal language theory).
**Analogy → our setting:** bandwidth-one = lookahead 1; the k-th moment = lookahead k. NEW: the **certificate-power
hierarchy** — "k-moment certificate < (k+1)-moment certificate < full information" — with proven anchors k = 2 →
0.6818 (ceiling, [CIG]), k = 1 → 2/3 (flat window, [AK]), ∞ → 1 (conditional). The hierarchy is *testable at every
rung* (each rung is an LP), and a *provable* hierarchy theorem would organize P2/V3 (rung 3) and the V4/V5 roadmap as
one object. This is mostly organizational — the LP machinery already prices each rung — but it names a *new target
type* (a general k-moment ceiling) the program could aim for.
**What it needs:** nothing new; the anchors exist, the rungs are V4's capacity LPs.
**Feasibility:** Low–Med. **Kill:** if the V4 curve is flat at every rung beyond 2 (the 256-law's higher correlations
are near-GUE — [AVC] flags this as CONJECTURED), the hierarchy collapses — a documented negative.
**Cheapest probe (<1h):** V4's probe (law's S₃ vs GUE).

### M5.2 Minimalist merge ↔ the block structure of W; labeling = inertia — KNOWN-OPEN (framing; reframe of [P10.1])
**Idea:** The Minimalist Program builds all structure by binary *merge*; merged objects need a *label* (the head) to be
interpretable (standard; Chomsky).
**Analogy → our setting:** the functional equation *merges* each zero with its reflection (ρ ↔ 1−ρ̄); off-line pairs are
the "failed merges" — the (1,1)-planes that leak a negative signature (the Bell-pair content of [P10.1], which was
executed and is negative as an input route [AQI]). The NEW fragment is the *labeling* picture: the certificate's
"labeling" of each merged block is the inertia (which sign each block contributes); the rank–trace counts labels. This
is a reframe of [P10.1]/[AQI] with no new provable content — recorded so the syntax vocabulary is not re-funded as new.
**Feasibility:** none (framing). **Cheapest probe:** none.

### M5.3 Derivational complexity ↔ n₋(W_T), the RH-ometer — KNOWN-OPEN (framing; measurement = [CD-V1]/[W-P1])
**Idea:** Minimalism measures structure by *derivational complexity* (number of merge steps) (standard).
**Analogy → our setting:** the minimal number of failed merges = the off-line pair count = n₋(W_T)/2 — the "RH-ometer"
of [CD-W1]/[P-W1]: a single prime-side number that is exactly zero iff all zeros are on the line. Its measured size is
the cleanest single diagnostic of off-line content (the [CD-V1] spectrum experiment, relabeled). No new content.
**Cheapest probe:** the [CD-V1] W_T spectrum run.

### M5.4 Mild context-sensitivity / TAG ↔ the derivative tower; the JOINT derivative-moment certificate — NEW (P5 extension)
**Idea:** Tree-adjoining grammars are *mildly* context-sensitive — strictly more powerful than CFG but much less than
general CSG (standard). The derivative tower (P5): ξ, ξ′, ξ″ are a *family* of recognizers of the *same* configuration,
with FGL constants rising with j (0.85838 → 0.86864, [CD-V9]) — "mildly more powerful" recognizers.
**Analogy → our setting:** NEW: beyond the single-derivative certificates (V9, executed or mechanical) and the dead
interlacing LP ([CD-A4]), price the *joint moment system across the tower*: the moments of the ξ^(j)-zero sets are
*different functionals* of the same zero configuration, and Newton identities relate them across j via the derivative
ratios ξ^(j)/ξ^(j−1) (whose explicit formula exists in the Lean XiPrime files). The joint system (m₁, m₂ for ξ *and*
ξ′ — four constraints on one configuration) is strictly richer than either certificate alone, and does not require the
interlacing that [CD-A4] killed (interlacing gave only a useless lower bound; *moments* are different data).
**What it needs:** (i) the ξ′/ξ explicit formula (Lean XiPrime); (ii) m₁, m₂ of the ξ′-zero set computed numerically
from real zeros; (iii) the joint (tr, ‖·‖²)² LP for the simple-on-line count.
**Feasibility:** Med. **Kill:** if the joint LP value equals max(single-window values) (no cross-window coupling — the
same obstruction as the two-bandwidth [ATB]), the tower gives no joint gain — a documented negative distinguishing the
moment-coupling route from the dead interlacing route.
**Cheapest probe (<1h):** compute m₁, m₂ of the ξ′-zero set from the cached zeros (via the ξ′/ξ ratio), compare with
the ξ values; if m₁(ξ′) ≠ m₁(ξ) with a computable relation, fund the joint LP.

### M5.5 Parsing complexity ↔ certificate complexity classes — NEW (organizing)
**Idea:** Membership/parsing is decidable in polynomial time for CFG but harder at the hierarchy's edges (standard).
**Analogy → our setting:** "is this configuration admissible at level v?" is an LP (polynomial) for the two-moment
class; adding third moments keeps it an LP. NEW: map the certificate's rungs to complexity classes (regular < CF < CS)
as an *organizing* device — the hierarchy M5.1 with complexity labels. Documentation; no new math.
**Cheapest probe:** none.

### M5.6 The pumping lemma ↔ the limitation-proof template; the next-wall candidate — NEW (organizing)
**Idea:** The pumping lemma proves regular languages can't "count" past bounded memory by a pigeonhole argument on
equivalent pumped strings (standard).
**Analogy → our setting:** the ceiling is the same proof shape: bounded data (bandwidth one) → indistinguishable
configurations (the crystal and reality "pump" identically). NEW: the *template* — "any certificate reading statistics
S cannot distinguish configurations differing only in S-invisible structure" — unifies the ceiling [CIG], the 5/6 wall
[AM], and the phase-retrieval twin [P6.4] as one pattern. The *next wall* candidate: configurations differing only in
*third-moment-invisible* structure — i.e., does the 256-law's triple correlation match GUE? If yes, the third moment
cannot move the wall (the V4 probe, [CD-V4]) — the "pumped" family for rung 3. The template turns "find the next input"
into "find the next S-invisible pumped family."
**What it needs:** V4's probe.
**Feasibility:** Low. **Kill:** n/a (organizing; the V4 probe decides the next wall).
**Cheapest probe (<1h):** V4's probe (law's S₃ statistic).

---

## Pool M6 — Information theory of language

### M6.1 Zipf's law ↔ the gap-rank curve — NEW (diagnostic)
**Idea:** Word frequencies follow Zipf's law: rank × frequency ≈ constant (standard).
**Analogy → our setting:** NEW: the *gap-rank curve* of the real zeros — rank the normalized gaps by size and plot
rank × gap. Lattice (crystal): truncated/steep with a few sizes; Wigner (GUE): a known smooth curve; reality: fit the
exponent/slope and classify. A summary statistic distinguishing the crystal from GUE that the two moments do not fix.
**What it needs:** cached zeros; a rank-size fit.
**Feasibility:** Low. **Kill:** diagnostic only (no certificate input).
**Cheapest probe (<1h):** rank-size plot of ~10⁴ gaps; report the fitted exponent.

### M6.2 Surprisal as an off-line detector ↔ per-zero anomaly detection — NEW (diagnostic)
**Idea:** *Surprisal* = −log P(symbol | context); high surprisal = unexpected under the model (standard information
theory of language).
**Analogy → our setting:** NEW: per-zero surprisal under (a) the crystal model (a zero lands on the grid / off-grid) and
(b) a GUE-like model (gap-distribution model); flag zeros with anomalously high surprisal under *both* — a *local*
anomaly detector for off-line/structural candidates. Diagnostic only (cannot prove), but the *distribution* of
surprisal is a new statistic; any zero far outside both models is a genuine anomaly worth checking against the known
data (e.g., the LMFDB file).
**What it needs:** cached zeros; two likelihood models.
**Feasibility:** Low. **Kill:** diagnostic; if the top-surprisal zeros are unremarkable (expected), documented.
**Cheapest probe (<1h):** compute surprisal of each zero under both models; list the top 20 anomalies.

### M6.3 Kolmogorov complexity / LZ-compressibility ↔ model-free structure statistic — NEW (diagnostic)
**Idea:** The algorithmic complexity of a sequence is the length of its shortest description; LZ76 is the standard
computable proxy (standard information theory).
**Analogy → our setting:** the crystal's gap sequence is O(1)-describable (periodic); GUE's has a known compressibility;
reality's is measurable *without assuming a model*. NEW: LZ76 complexity + entropy-rate of the real gap sequence,
normalized, compared with (a) the crystal (≈ 0) and (b) synthetic GUE data. A model-free "how structured is the zero
sequence" number.
**What it needs:** cached zeros; an LZ implementation (small).
**Feasibility:** Low. **Kill:** diagnostic only.
**Cheapest probe (<1h):** LZ76 on the binarized gap sequence (gap < median / ≥ median); compare with synthetic GUE and the crystal.

### M6.4 Redundancy / Shannon channel ↔ the certificate-polytope entropy (V4 quantification) — NEW (quantification)
**Idea:** Natural language is ~50% redundant (Shannon); a channel's *capacity* is the maximum information it can carry
(standard).
**Analogy → our setting:** the two-moment channel's *capacity* is the V4 roadmap ([CD-V4]). NEW: quantify the
*redundancy actually used* — the entropy (log-volume) of the certificate's feasible set (the LP polytope at the
256-law) measures how much of the data's information the certificate consumes; the gap 0.68183 − 0.6725 is the *unused
redundancy* of the two-moment certificate (it wastes information the class could use — fixed by the LP, [ALPD]/[CIG]).
The computable NEW number: *the fraction of feasible-set entropy each added moment consumes* — the V4 capacity curve as
a redundancy curve.
**What it needs:** the [ALPD]/[CIG] LP machinery + polytope sampling/volume estimation (the 256-cell structure is
tractable).
**Feasibility:** Low–Med. **Kill:** if the entropy estimate is dominated by discretization artifacts, the number is
uninformative — document.
**Cheapest probe (<1h):** sample the certificate polytope at the law (hit-and-run or the LP's vertices); estimate log-volume at B, C budgets.

### M6.5 Rate–distortion ↔ the moment-order R-D curve calibration — NEW (calibration)
**Idea:** Rate–distortion theory: the minimal rate needed to represent a source within distortion D (standard).
**Analogy → our setting:** the certificate is a *lossy description* of the configuration at distortion "simple-fraction
error"; the *rate* = the number of moments. NEW: calibrate the first two points of the R-D curve — rate 1 (mean only,
flat window) → 2/3, rate 2 → 0.6725 — and the *slope* (what the marginal moment buys, per the V4/V5 roadmap). This is
the V4/V5 roadmap restated with a distortion label; the calibration is free (both points are known, [AK]).
**What it needs:** nothing new.
**Feasibility:** Low. **Kill:** n/a (calibration/documentation).
**Cheapest probe (<1h):** tabulate the (rate, distortion) points {(1, 2/3), (2, 0.6725)} and annotate with the V5
support-curve prices ([AF1]).

### M6.6 Gricean maxims ↔ the informativeness audit of the certificate — KNOWN-DEAD (as input; documentation)
**Idea:** Grice's maxims: be as informative as required, truthful, relevant (standard pragmatics).
**Analogy → our setting:** the two-moment (MT) certificate *violates* the informativeness maxim — it leaves the
bandwidth-one rows' information unused; the LP-optimal certificate *obeys* it ([ALPD]/[CIG]). The *audit* (the wasted
information = 0.68183 − 0.6725 ≈ 1.4%·N) is already computed. Documentation — the audit is complete; do not re-run.
**Cheapest probe:** none.

---

## Probe results (code-backed, Round 1) — mandatory-protocol verification

Every number below was produced by the cited script (all in the new self-contained dir
`tools/probes_music_ling/`; none of the canonical `tools/` scripts were edited). Commands
were `uv run --quiet --with numpy --with scipy python tools/probes_music_ling/<script>.py`
(from `/home/vstaln/riemann/tools`; scipy only where stated). Labels per the mandatory
protocol: PROVEN / CHECKED NUMERICALLY (script cited) / CONJECTURED / ABANDONED /
INCONCLUSIVE. Data: `tools/data/zeros_computed_10000.txt` (10,000 ordinates, γ ≤ ~9884,
computed) and `tools/data/xiprime_on_line_1_1000.txt` (1,009 ξ′ zeros, γ ≤ ~1419).
Debugging note: `probe_music_bands.py` initially disagreed with the fine scan (m2 = 3.64);
root causes were two bugs (diagonal leak + double counting of ordered pairs, then a missing
factor 2 for the two-sided integral in the GUE expectation) — fixed and re-run; final
numbers are self-consistent (bookkeeping closes: m2 = 1 + O/n both ways).

### R1. Rational-α "consonance" test [M2.3], near-rational clustering [M1.5], meter scan [M3.1] — `probe_music_rational.py`
- Pair correlation g(u) (global-rescale, estimator g = ordered_pairs/(λ²(L−u)du)) vs GUE
  1−sinc²(πu): at rationals {1/3,1/2,2/3,3/4,1,4/3,3/2,2,3} mean |dev| = 5.36%; at
  controls {0.37,0.61,1.13,1.71,2.31,2.89} mean |dev| = 4.03% — **no systematic rational
  structure**; the largest single deviations appear at *controls* (u = 1.71: +3.9%, +3.5σ;
  u = 2.31: +1.6%, +2.2σ) and one rational (u = 3/4: +8.8%, +3.4σ) — single-point noise.
- Meter scan, integer lags u ∈ {1,…,256}: |dev| ≤ 4.2% (u = 256: +4.2%, inside the
  large-lag estimator-bias band; u = 1: −7.5% is the small-u repulsion dip). **No metrical
  periodicity** at any integer lag.
- Near-rational pair distances (ε = 0.01, q ≤ 8): real 0.1477 vs Poisson control 0.1656,
  ratio 0.891 — real pairs are *less* likely near simple rationals than random (the GUE
  repulsion removes the small-distance pairs that sit near small rationals). **No rational
  enhancement.**
- **LABEL: CHECKED NUMERICALLY — all three hypotheses (consonance dips, rational lattice,
  meter) are REFUTED on the real data; the pair correlation is GUE-consistent.** (Same
  conclusion as the small-u follow-up `probe_music_rational_smallu.py`: g below GUE for
  u < 0.45 — stronger repulsion — and above GUE for u ∈ [0.45, 0.8).)

### R2. Periodicity ("virtual fundamental") and rhythmic oddity [M2.5 / M3.3] — `probe_music_periodicity.py`
- Occupancy-grid ACF (bin 0.5, rescaled units): ACF at periods 16..512 all within ~1.5σ of
  zero (noise floor ±0.0071); ACF(256) = +0.0108 (≈ 1.5σ, not a delta-like peak); max
  |ACF| = 0.071 at lag 1 (p = 0.5) — nearest-neighbor repulsion, not periodicity.
  **No "virtual fundamental" at the crystal's period 256 or anywhere.**
- Rhythmic oddity (self-match under shift): 0.43–0.55 at every shift s ∈ {1,…,256}
  (random ≈ 0.5); period-halving rotation s = 128: 0.528. **The real zero sequence is
  aperiodic — "rhythmically odd" — unlike the 256-periodic crystal.**
- **LABEL: CHECKED NUMERICALLY — the crystal's hidden periodicity is inaudible in the
  data; the ceiling law is a pure combinatorial artifact on every periodicity statistic
  measured.** (Diagnostic: strengthens the case that beyond-1/repulsion routes, not
  crystal-killing ones, are the way past 0.6818.)

### R3. Gap-statistics battery [M3.5 / M6.1 / M6.2 / M6.3] — `probe_music_gaps.py`
- KS distance of empirical gaps: 0.0805 vs Wigner-surmise (GUE proxy), 0.2946 vs
  exponential (Poisson); lattice closeness tiny (9.6% of gaps within 0.05 of 1;
  mean |gap−1| = 0.3355).
- Binned gap entropy (same binning, nats): empirical 2.8219 < Wigner 3.0217 < exponential
  3.2988 — the real gaps are *narrower* than Wigner (std 0.4439 vs Wigner 0.522).
- Zipf rank-size fit of sorted gaps: slope −1.835, R² = 0.72 — **not a power law** (no
  Zipfian structure).
- Surprisal top-20 under the Wigner model: all are the expected large-gap events (largest =
  the first gap γ₂−γ₁ ≈ 6.89 raw / 6.98 rescaled); **no anomalous outliers**.
- LZ76 on the binarized (gap<1) sequence: real 1142 vs shuffled control 1166 (ratio 0.98)
  — **no sequential compressible structure**.
- **LABEL: CHECKED NUMERICALLY — the gap statistics are GUE-with-noise; nothing here
  distinguishes reality from the pair-correlation-conjecture world, and no gap-statistic
  input is available to a certificate.** (Diagnostics only, as labeled in the pools.)

### R4. Masking width of a (1,1)-plane [M2.2] — `probe_music_mask.py`
- Model: each off-line pair contributes 2(Re(v)Re(v)ᵀ − Im(v)Im(v)ᵀ) with
  v[k] = Ψ(s − k) (Ψ = cosine-window Fourier transform, closed form from [AF]); sanity:
  single pair n₊ = 1 ✓.
- Two pairs at separation d (grid units, β = 0.5 shallow off-line): **n₊ = 2 for every
  d ≥ 0.005** (masking width ≤ 0.005 mean spacings); n₊ = 1 only at exact coincidence
  (d ≲ 0.002) — which is precisely the multiplicity-2/double-mark world already priced by
  the integrality constraint. Grid convergence: K = 16 truncates (n₊ = 1 artifact); K = 32
  and K = 64 agree.
- **LABEL: CHECKED NUMERICALLY — there is NO exploitable subadditivity ("masking") of the
  off-line positive index above exact coincidence; the p-cost is exactly additive, in
  agreement with `lemmaR_tight` [AM].** Consequence (sharper than the catalog's original
  guess): even if off-line pairs were proven to *cluster*, the certificate would not
  benefit — only a sparsity *bound* (limiting the number of pairs), i.e. a repulsion-type
  input on the pair count itself, could change the p-bookkeeping. M2.2 as an input route
  is ABANDONED (documented here); its probe value was the negative.

### R5. Moment "tuning" [M1.1] and ξ′/ξ coupling [M5.4] — `probe_music_moments.py` + `probe_music_logt_fit.py`
- Flat-window Gram (λ = 1, per-band local rescale, convention of `tools/m3_zeros_check.py`):
  m₂ deficits vs 4/3: −0.0118 (h 14–1420), −0.0347 (1420–5800), −0.0331 (5800–10800),
  −0.0306 (10800–17000); m₃ deficits vs 2: −0.059, −0.118, −0.112, −0.103.
  **deficit·log(h) = 0.276, 0.297, 0.291 over the three high bands (mean 0.288, spread
  0.021) — the deficit follows ~1/log T above h ~ 3000** (the lowest band deviates:
  boundary effects at the start of the sequence). The mistuning does not saturate at these
  heights — consistent with [AF]'s Δ(T) ~ 1/log T and the persistent finite-T gap (P6).
- **M5.4 coupling (same height range, h ≤ 1419): m₂(ξ′) = 1.2294 vs m₂(ξ) = 1.3215**
  (ratio 0.930, |diff| 0.092 ≈ 7% systematic); m₃(ξ′) = 1.9813 vs m₃(ξ) = 1.9407.
  **The ξ′-zero set carries measurably different moment data than the ξ set — the two
  functionals are NOT redundant, so the joint (ξ, ξ′) moment certificate (M5.4) has real
  content and is funded.** Caveats (INCONCLUSIVE parts): ξ′ data available only to
  h ~ 1419 (one band); the `xiprime_on_line` file is assumed to be ξ′ zeros on the line
  (consistent with count, range, and interlacing — to be verified against the generating
  script); higher-height ξ′ moments need computation.
- **LABEL: CHECKED NUMERICALLY (both); M5.4 upgraded from "promising" to "funded on
  measured evidence".**

### R6. Where the finite-T deficit lives [M2.4] — `probe_music_bands.py`
- Flat-window Gram (λ = 1, global rescale, whole 10,000-zero file): m₂ = 1.32031, deficit
  vs 4/3 = −0.01302 (the global-rescale deficit is smaller than the per-band local one —
  different normalizations, both reported).
- Distance-banded ordered off-diagonal vs GUE (two-sided integral): the deficit
  **concentrates at u < 1** (−0.0188 of the total; the u ≥ 1 region is GUE-exact, every
  band within ±0.0001 of expectation). **The kernel-edge/"temporal-masking" hypothesis is
  REFUTED as the dominant mechanism: the finite-T deficit is a short-range (u < 1)
  pair-correlation effect**, consistent with the fine-scan g (below GUE for u < 0.45,
  above for 0.45–0.8, R1/R-smallu) and with [AF]'s observation that the Ψ₂ pair sum
  reproduces Δ(T).
- **LABEL: CHECKED NUMERICALLY — M2.4's edge-masking picture is abandoned as the dominant
  part; the deficit is real, short-range arithmetic information (a documented negative for
  the artifact view, a positive for P6's "the finite-T gap is arithmetic pair-correlation
  structure").**

## TOP 10 (EV × feasibility × cheap-probe)

1. **M5.4 — Joint derivative-moment certificate (ξ, ξ′ moments via Newton identities).**
   **UPGRADED: the measured ξ′/ξ moment data are not redundant** (m₂(ξ′) = 1.2294 vs
   m₂(ξ) = 1.3215 on the same range, R5) — the joint system has real content. Next: verify
   the xiprime file semantics and compute higher-height ξ′ moments, then the joint
   (tr, ‖·‖²)² LP vs 0.86864. Probe: <1h for the moment extension.
2. **M4.3 — Pointwise F ≥ 0 gradient LP (re-fund V11/[P11]).** Still the only proven-input
   route toward > 0.6725. Probe: CGdL20-style SDP with B24 constraints — hours.
3. **M4.1 — Price the "no doubles within δ" constraint (markedness curve).** Un-probed;
   p₁ shadow price = 1 makes any repulsion-on-doubles input 1:1. Probe: LP perturbation — <1h.
4. **M6.4 — Certificate-polytope entropy (V4 quantification).** Un-probed; the redundancy
   number for the capacity roadmap. Probe: polytope sampling — hours.
5. **M1.7 — Myhill / well-formedness check of the 256-law.** Un-probed; a structural
   constraint on the extremal-law family. Probe: gap-size multiset of the law — <1h.
6. **M4.4 — RCD as a certificate-discovery heuristic for enlarged classes.** Un-probed.
   Probe: RCD on synthetic configurations — <1 day.
7. **M2.4 (revised) — Smooth-window experiment with the u<1 concentration as target.** The
   R6 probe shows the deficit is short-range, not edge-driven; the C∞-window experiment
   ([AF]'s recommended next step) now has a quantitative prediction: it should NOT remove
   the u<1 part. Probe: [AF] finitet with a smoothed window — hours.
8. **M3.6 — var(Δ(T)) over adjacent windows (feeds the almost-everywhere theorem [P9.1]).**
   Un-probed. Probe: [AF] code, adjacent windows — <1h.
9. **M2.2 (revised) — sparsity-on-pairs input, not clustering.** The R4 probe shows
   clustering gives nothing; only a bound on the *number* of off-line pairs matters — reframe
   the search as "any upper bound on the off-line pair count" (the p₁ shadow price = 1 form).
   Probe: none new (the input is the open problem).
10. **M5.1/M4.5 — the k-moment ceiling theorem as a target type (priced by the V4 LP).**
    Organizing; the k = 3 rung is the P2/V3 question. Probe: V4's law-S₃ check — <1h.

**Strategic reading (updated after the Round-1 probes):** the music/ling pools produced exactly one genuinely new
*proven-input-adjacent* vector (M5.4), now **funded on measured evidence** (R5: the ξ′ and ξ moment data are
genuinely different). The probes also delivered five clean code-backed negatives that change what we believe
(R1–R4, R6): the real zeros show no rational/consonance structure, no periodicity anywhere, GUE-with-noise gap
statistics, an exactly additive (1,1)-plane cost (masking width ≤ 0.005 spacings), and a finite-T deficit that lives
at u < 1 (not the kernel edge). These negatives (i) confirm the pair-correlation-conjecture world is the right model
of the data at every statistic we measured, (ii) kill the "clustering" route to reducing the off-line p-cost (only a
pair-*count* bound can help), and (iii) relocate the finite-T gap's mechanism to short-range pair correlation. The
remaining un-probed vectors with real value are M4.1 (input pricing), M4.3 (= V11/[P11]), M6.4, M1.7, M4.4.
Everything else is framing that independently re-derives the known walls (phase/intensity [P6.4],
no-missing-constraint [ALPD], multiplicity [AM], two-bandwidth [ATB]) — evidence those walls are structural.

---

## WILD section (deliberately absurd premises; honestly evaluated; each labeled)

### W-ML1. "The zeros are a well-formed scale; RH ⟺ the scale is generated by a single interval" — CONJECTURED (framing; fact flagged)
**For:** the 256-law is a marked lattice whose gap set may satisfy the Myhill two-sizes property (M1.7's probe); if so,
well-formedness theory (generation by one generator, continued-fraction parameterization — *reported standard, verify
before use*) would parameterize the extremal-law family. **Against:** the parameterization concerns the *combinatorial*
law, not ζ's zeros; the zeros' actual ordinates are not a scale with a generator; nothing provable transfers. **Novel
fragment worth keeping:** the Myhill probe (M1.7) is cheap and constrains the ceiling-law family.

### W-ML2. "RH is just intonation of the primes: the zeros are the pure tuning of the prime spectrum; RH ⟺ zero mistuning" — CONJECTURED (framing)
**For:** the moment tower ↔ the harmonic series (M1.1) makes "pure tuning" a vivid image; the *beating* measurement
(mistuning of the finite moments) is a real diagnostic. **Against:** this is Hilbert–Pólya-as-tuning with no operator;
no provable fragment. **Novel fragment:** the tuning-curve probe (M1.1: does Δm_k(T) decay?) is the honest content —
run it.

### W-ML3. "The pumping lemma for the certificate: the zeros' language is beyond regular; RH is the claim that it is beyond CFG" — CONJECTURED (framing)
**For:** the pumping-lemma proof shape (bounded data → indistinguishable pumped twins) is *exactly* the ceiling's shape
(M5.6); naming it organizes the walls. **Against:** no new inequality; the "language of the zeros" is not a formal
language with a grammar. **Novel fragment:** the limitation-proof *template* (M5.6) and its next-wall prediction
(does the law's S₃ match GUE? — the V4 probe) are the transferable content.

### W-ML4. "Counterpoint / species rules are the certificate's grammar; the ceiling is the strict-species limit" — CONJECTURED (pure framing)
**For:** strict counterpoint = a ranked system of hard constraints (perfect consonances only on strong beats, etc.)
whose feasible set is exactly the "admissible species"; the certificate's constraint set is a species. **Against:** no
new math; the species of the 256-law is a restatement of the LP. **Novel fragment:** none beyond the "constraint
system as species" vocabulary — do not fund.

### W-ML5. "The zeros obey a Sonority Sequencing Principle: a proven gap-ratio hierarchy derivable from F ≥ 0" — CONJECTURED (the derivation is the open part)
**For:** F(α) ≥ 0 pointwise (PROVEN) is the only "substance" available; a hierarchy of gap constraints derived from it
would be the SSP analog (M4.3). **Against:** the derivation is exactly the V11/[P11] problem — no new route appears
from the sonority framing. **Novel fragment:** none beyond re-motivating V11 — already TOP-10 #2.

### W-ML6. "RH ⟺ the zero spectrum has zero harmonic entropy (perfect tuning); the certificate measures the detuning" — CONJECTURED (the honest measurement is W-P1's RH-ometer)
**For:** "harmonic entropy" (M1.3) gives a single number for a spectrum's structural ambiguity; RH would be "perfectly
structured." **Against:** the entropy is not provable from any unconditional input; the honest version is n₋(W_T) — the
measured negative index of the compressed Weil form ([CD-W1]/[P-W1], = the [CD-V1] spectrum experiment). **Novel
fragment:** run the [CD-V1] spectrum and report n₋(W_T)/N as the "detuning" — the cleanest single RH-ometer.

---

## Label inventory

- **NEW** (invented here, untested; conjectured by construction): M1.1 (now TESTED, R5), M1.3, M1.4, M1.5 (now
  TESTED-negative, R1), M1.7, M2.2 (now TESTED-negative, R4), M2.3 (now TESTED-negative, R1), M2.4 (now TESTED,
  R6), M2.5 (now TESTED-negative, R2), M3.1 (now TESTED-negative, R1/R2), M3.2, M3.3 (now TESTED-negative, R2),
  M3.5 (now TESTED, R3), M4.1, M4.4, M4.5, M5.1, M5.4 (now TESTED-positive, R5 — FUNDED), M5.5, M5.6, M6.1
  (now TESTED-negative, R3), M6.2 (now TESTED-negative, R3), M6.3 (now TESTED-negative, R3), M6.4, M6.5,
  W-ML1 … W-ML6 (framing).
- **KNOWN-OPEN** (route already flagged in our notes; new framing or fragment only): M1.2 (phase; [P6.4]), M1.6
  (voicing; [AM]), M2.6 (edge sensitivity; [P1.3]), M4.3 (pointwise F ≥ 0; [CD-V11]/[P11]), M5.2 (merge/labeling;
  [P10.1]/[AQI]), M5.3 (derivational complexity; [CD-V1]/[W-P1]).
- **KNOWN-DEAD** (executed negatives / documented to prevent re-derivation): M3.4 (hemiola two-window; [ATB]),
  M4.2 (missing constraint inside bandwidth one; [ALPD]/[CIG]), M4.6 (constraint conspiracy complete; [ALPD]),
  M6.6 (informativeness audit complete; [ALPD]).
- **TESTED-OPEN** (extends our own measured data): M2.1 (Δ(T) ≈ c/log T fit; [AF]), M3.6 (var(Δ(T)); [AF]).
- **Round-1 probe outcomes (code-backed, R1–R6; all CHECKED NUMERICALLY with scripts cited in the probe-results
  section):** R1 (rational-α / near-rational / meter — REFUTED, GUE-consistent), R2 (periodicity / oddity —
  REFUTED, aperiodic), R3 (gap battery — GUE-with-noise, no structure), R4 (masking width ≤ 0.005 spacings —
  p-cost exactly additive, clustering input ABANDONED), R5 (m₂ deficit ~1/log T above h~3000; ξ′/ξ coupling real
  — M5.4 FUNDED), R6 (finite-T deficit concentrated at u<1 — kernel-edge hypothesis REFUTED as dominant).
- **Probe discipline:** every vector above has a <1h cheapest probe using existing machinery (tools/finitet,
  tools/lpdual, tools/m3_*.py, cached 34-digit zeros, and the new `tools/probes_music_ling/` scripts) — nothing
  requires new heavy compute to *start*.

**Honest closing note (updated after the Round-1 code-backed probes):** the music/linguistics angle's strongest NEW
contribution is the joint derivative-moment certificate (M5.4) — a proven-machinery attack on the P5 tower — now
**funded on measured evidence**: the ξ′ zero set carries materially different moment data than the ξ set on the same
height range (m₂: 1.2294 vs 1.3215; R5), so the two functionals are not redundant and the joint moment system is a
genuinely new input. The six probes also delivered five clean negatives that change what we believe: no rational or
periodic structure anywhere in the real data (the 256-crystal is inaudible), GUE-with-noise gap statistics, an
exactly additive off-line (1,1)-plane cost (masking width ≤ 0.005 spacings — only a pair-*count* bound could help),
and a finite-T deficit concentrated at u < 1 (a short-range pair-correlation effect, not a kernel artifact). The
pools independently re-derived the known walls (phase intensity, no-missing-constraint, multiplicity, two-bandwidth)
through tuning, masking, meter, phonotactics, and grammar-power vocabularies — strong evidence those walls are
structural, and a caution against funding their restatements. The persistent wall — beyond-1 F, third moments,
repulsion — is *phase* information, and every far-field pool keeps arriving at the same place: a two-moment
intensity certificate cannot hear it.
