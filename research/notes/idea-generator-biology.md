# Idea Generator: biology & genetics attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (biology/genetics angle). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Biological facts below
are standard results (minimum frustration, Go models, May 1972, Kauffman NK, Haldane cost, Fisher's
fundamental theorem, missing heritability, GREML/GCTA, V(D)J repertoire statistics, finite-mixture
identifiability, Horvath clock) named at the level of "standard in the field"; anything I cannot verify
from the sources we hold is labeled **reported standard — verify before use**. Every *idea* is
CONJECTURED by construction, labeled **NEW** (invented here, not in previous catalogs) /
**KNOWN-DEAD** (killed in earlier rounds; cite) / **KNOWN-OPEN** (a known open problem or route already
flagged in our notes; cite the crossdomain/physics numbering) / **TESTED-OPEN** (numerically tested by our
own tools or attack notes, still open).
Overlap discipline: crossdomain catalog = idea-generator-crossdomain.md, cited [CD-V#]/[CD-W#]/[CD-A#];
physics catalog = idea-generator-physics.md, cited [P#.#]; attack notes = attack-kernel [AK],
attack-ceiling [AC], attack-finitet [AF], attack-lpdual [ALP], attack-multiplicity [AM].
No `[MLECO]` note exists in research/notes/ (checked); the ecology pool is **skipped per brief** — its
content is covered under the branching/cascade reading [P9.5] and the density/diagnosis vectors [CD-V10].

**State of the art the biology must respect (PROVEN / CHECKED NUMERICALLY):**
- Two-moment method: tr W_T = N, ‖W_T‖²_HS = 1.3274993·N (cosine window, Theorem D), certificate 0.6725007;
  2/3 flat; 5/6 distinct; 0.83625 distinct (optimal window) — [AM].
- **In-class ceiling is TIGHT at v* = p₀ + |E(1)| = 0.68183123** — the LP dual attains the Lean ceiling;
  the two-moment Montgomery–Taylor certificate is strictly suboptimal *inside* the class; the only datum
  that moves v is the certified simple fraction p₁ itself (shadow price exactly 1), which needs
  beyond-bandwidth-1 pair correlation or a multiplicity bound — both CONJECTURED/unavailable [ALP].
- 5/6 distinct wall: the all-simple world and the "2/3 simples + 1/6 doubles" world are spectrally
  identical in (tr, ‖·‖²); third moment (tr Â³) is the documented bypass, unconditional in the
  Rudnick–Sarnak range λ < 2/3 [CD-V3]; **CHECKED NUMERICALLY here: every integer-spectrum twin of the
  extremal law shares m₃ = 2 = the GUE/HL* value** (this note, §Pool 4) — so the *canonical twins* are
  third-moment-identical and the bypass must act through LP-tightening, not twin-exclusion.
- Moment hierarchy (HL*/GUE, conditional): m_k = 1, 4/3, 2, 13/4; HL*(4,λ) → 13/18 simple; all moments → 1
  (paper Prop 4.5) [AM], [P9.4].
- Finite-T: bound/N − 0.6725 = Δ(T) > 0 at every tested T, decaying ~1/log T, attributed to kernel
  artifacts [AF]; Selberg CLT count fluctuations √(log log T) unconditional [CD-V13].
- Row shadow prices of the 256-law LP: middle rows j = 64..192 individually most valuable (1.5–2·10⁻³
  each); collectively all 255 near-CUE rows pin v to 2.5·10⁻⁶ of p₀; one row alone allows ≈ 0.89 [ALP].

**Abstracted problem (the object biology must map to):** given a configuration of N marked points and two
scalar "measurements" (mean density, pair-correlation intensity on one bandwidth), certify the fraction
that lies on a distinguished line; a *decoy* configuration exists that matches both measurements exactly
but has a worse line-fraction; the certificate cannot exclude the decoy; the only escape is a third
measurement (three-point correlation) or information beyond the one bandwidth. In one sentence: **"an
intensity-only two-measurement discriminator has a decoy twin; the third measurement is the minimal way to
break the twin."** Biology is full of exactly this shape: native-vs-decoy folds, self-vs-non-self
repertoires, genetic-vs-environment variance partitions, mixture deconvolutions.

---

## Pool 1 — Protein folding / fitness landscapes: the decoy twin and the funnel

**Core mapping:** the "sequence" = the primes (the explicit formula generates the configuration); the
"native state" = all zeros on the line; the **contact map = our Gram matrix W** (pairwise "contacts"
between grid residues mediated by the zero measure); the two moments = contact-map *statistics*; the
256-periodic crystal = a **misfolded decoy with identical contact statistics**; the certificate = a
Go-model energy gap (a bound on native contacts). The folding literature's central lesson is that
pairwise contacts alone cannot distinguish a fold from its decoys — exactly our ceiling.

### B1.1 Designability count of the two-moment class — NEW (probe; the pool's headline)
- **Idea:** in protein design, *designability* = the number of sequences folding to one structure. Here:
  count the marked configurations realizing the crystal's (tr, HS²) + integrality + near-CUE rows — the
  *degeneracy of the certificate's data*. If the family is astronomically large, the wall is robust and
  no *local/pairwise* input can ever win; the third moment's power = how much it shrinks the family.
- **Analogy:** contact-map degeneracy (two folds, identical contact statistics) ↔ crystal vs reality
  (identical two moments, different line-fraction); designability ↔ certificate-data degeneracy.
- **Needs:** enumerate/bound the feasible set of the N = 256 marked LP (machinery: tools/regen_law/
  lp_scale2.py, tools/lpdual/) at the optimum — the *count* is the new object.
- **Feasibility:** Low–Med. **Kill:** if the family is a single point (only the 256-law), the degeneracy
  is an artifact of the LP's corner and the robustness argument changes.
- **Cheapest probe (<1h):** sample the N = 256 feasible set at the optimum; count distinct mark patterns
  satisfying the 255 near-CUE rows + two moments to the τ = 3·10⁻⁴⁰ tolerance.

### B1.2 Contact-order ↔ bandwidth curve — NEW (framing; validates [CD-V5])
- **Idea:** *contact order* (fraction of local contacts) predicts folding rate: high local-contact
  content = slow, hard folding (Baker/Plaxco, standard). The certificate's "contact order" = the
  bandwidth A of the pair-correlation input; [CD-V5]'s F≡1-on-[0,A] curve (A = 1.04/1.26/1.70 for
  0.70/0.80/0.90) is literally a **"folding rate vs contact order" curve**.
- **Analogy:** contact order ↔ bandwidth λ; folding rate ↔ certified fraction; the "nonlocal contacts"
  needed for a fast fold ↔ the beyond-1 form factor.
- **Needs:** re-analysis of [CD-V5]'s numbers; the folding prior: the curve should be **monotone,
  concave (diminishing returns per unit bandwidth), saturating at 1** — a checkable shape constraint on
  the roadmap's own numbers.
- **Feasibility:** Low. **Kill:** if the computed curve violates monotone-concave-saturation, Remark 1.1's
  numbers need re-checking (a finding); if it satisfies the prior, the roadmap is physically sane.
- **Cheapest probe (<1h):** fit [CD-V5]'s three points to 1 − c/A^a; check the shape.

### B1.3 Frustration index of the zero configuration — NEW (diagnostic)
- **Idea:** the *frustration index* (Frustratometer, Wolynes et al.) measures per-residue deviation from
  a minimally frustrated landscape; minimally frustrated proteins fold robustly. Here: a per-scale /
  per-α "frustration profile" of the real W_T — deviation of sub-block spectra and per-α pair correlation
  from the crystal/GUE prediction.
- **Analogy:** per-residue frustration ↔ per-scale deviation; low frustration ↔ all higher statistics
  near-GUE (a "well-funneled" zero configuration).
- **Needs:** W_T spectra (exists, [CD-V1]/[P4.3]) + the per-α pair correlation ([CD-V6]) assembled into a
  profile.
- **Feasibility:** Low. **Kill:** if the profile is flat (no scale departs from GUE), the crystal is
  spectrally indistinguishable at all scales — confirms the ceiling's robustness; documented negative.
- **Cheapest probe (<1h):** reuse tools/finitet; print per-row pair-correlation deviations vs
  GUE/crystal at T = 200..700.

### B1.4 Decoy-discrimination screening — NEW (empirical pricing of ALL candidate inputs)
- **Idea:** in structure prediction a scoring function is validated by *threading*: can it rank native
  above decoys? The two-moment certificate is the scoring function, the crystal is the top decoy. Screen
  candidate *statistics* (spacing ratio, counting variance, skewness/third moment, max gap, entropy) for
  discrimination power between real zeros and crystal-sampled configurations.
- **Analogy:** threading/decoy discrimination ↔ ranking real zeros above crystal samples; the statistic
  with the largest margin is the one worth making provable.
- **Needs:** crystal-ensemble generator (tools/regen_law) + real zeros (tools/data/zeros_1_1000.txt,
  zeros_computed_10000.txt) + a statistics library.
- **Feasibility:** Low. **Kill:** if no cheap statistic separates the two (all margins within sampling
  noise), the two moments are empirically information-complete — the wall is real at every observable
  order.
- **Cheapest probe (<1h):** 10³ crystal samples × 5 statistics vs the 1000/10000 real zeros; report
  separation z-scores. Complements [CD-V4] (which prices *provable* inputs) by pricing *empirical*
  separability.

### B1.5 Minimum frustration / Levinthal-paradox reframe — KNOWN-OPEN (framing)
- **Idea:** the Levinthal paradox (astronomical search) is resolved by *funnel* structure; our certificate
  resolves the "which configuration" search only to 67% — the missing funnel = the higher-order
  correlations that would guide the search. Minimum-frustration (Go-model) would certify the global
  minimizer is the right one; our Go model is the Weil form and 0.6725 is the energy gap's shadow.
- **Analogy:** funnel ↔ the gap between two-moment data and full correlation data; frustration ↔ the
  off-diagonal HL-strength prime terms.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing-only). Redirects to B1.4 / B3.1 for
  the funnel-completing inputs, which are P2/P3 — KNOWN-OPEN as an input route.

---

## Pool 2 — Gene regulatory networks / dynamical systems: inertia, motifs, realization

**Core mapping:** the certificate is an *inertia* statement (Sylvester) on the "interaction matrix" W; RH
= the zero-system's stable fixed point (all on the line); the dimension cap (Prop 7.4: λN independent
measurements) is a *realization-theory* bound; the only *proven* sign constraint on the system is F ≥ 0.

### B2.1 Realization theory: the certificate as a bounded-real-lemma bound — NEW (reframes [P8.1])
- **Idea:** the KYP/bounded-real lemma (control theory, standard): a transfer function is positive-real
  iff an LMI admits a PSD solution, and the *state dimension* caps what finite data can certify. The
  certificate's dimension cap is exactly a realization bound: the two-moment data admit a minimal
  (λN-dimensional) realization, and the crystal IS that minimal realization; a third moment forces a
  higher-order realization — the price is the extra state dimension.
- **Analogy:** minimal realization ↔ the 256-law; model order ↔ moment order.
- **Needs:** none new — this is [P8.1]'s Nevanlinna parametrization in control vocabulary.
- **Feasibility:** Low. **Kill:** if the identification is purely verbal (no new constraint), record as
  framing-only. Value: independent confirmation of the in-class closure [ALP] from a second formalism.
- **Cheapest probe (<1h):** fold into P8.1's principal-representation computation; nothing new to run.

### B2.2 Motif census: the three-point correlation as the feed-forward loop — NEW (sharpened P2 probe)
- **Idea:** network science: *motifs* are over-represented subgraphs; the 3-node feed-forward loop is the
  canonical motif with an established function. The zeros' 3-node motif = the triple correlation; the
  crystal's motif census vs reality's is the discrimination test. Run the *full* 3-node census (not just
  skewness) on real zeros vs the crystal — the census tells us which specific 3-point statistic carries
  the strongest signal (the one to make provable).
- **Analogy:** FFL ↔ the 3-point correlation; motif over-representation ↔ deviation from GUE/crystal.
- **Needs:** real zeros (tools/data) + crystal generator + 3-point code (tools/m3_zeros_check.py,
  tools/empirical_m3.py exist — extend to the census).
- **Feasibility:** Low–Med. **Kill:** if every 3-node statistic is within noise (the crystal is
  third-order-compatible with reality), P2 is empirically dead — a documented negative redirecting funds.
- **Cheapest probe (<1h):** 3-point histogram of real zeros (1000 + 10000) vs crystal samples;
  per-shape deviations.

### B2.3 May's paradox: random vs structured interaction matrices — KNOWN-OPEN (framing)
- **Idea:** May (1972, standard): random interaction matrices destabilize as size grows (threshold
  λ_c ~ 1/√(SC)); real systems sit below the threshold. The crystal = the maximally-random
  (max-entropy) matrix consistent with the two moments; the ceiling = the May threshold of the certificate
  class. Reality's measured margin Δ(T) > 0 [AF] is the "stability margin" — but it is artifact-level and
  cannot enter a per-T certificate.
- **Analogy:** random-vs-structured stability ↔ crystal-vs-reality; the threshold ↔ the ceiling.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing-only; reinforces [AF]).
- **Cheapest probe:** none (documentation).

### B2.4 Sign-pattern inventory: F ≥ 0 as the monotone-system constraint — KNOWN-OPEN (documentation)
- **Idea:** monotone/sign-stable systems have unique globally stable fixed points; a *provable* sign
  constraint on the interaction structure would be a certificate input. Our provable sign constraint is
  F(α) ≥ 0 (L² representation, PROVEN), already used *conditionally* by CGdL20 [CD-V11]. Inventory any
  OTHER proven positivity/sign constraint on ζ's correlations usable inside a certificate.
- **Analogy:** sign patterns / M-matrix stability ↔ Weil-form positivity; the sign pattern is what a
  "monotone system" proof reads.
- **Needs:** a scoped literature writeup (overlaps [CD-V17]'s repulsion inventory — merge).
- **Feasibility:** Low. **Kill:** if nothing beyond F ≥ 0 exists (expected), record — prevents re-funding.
- **Cheapest probe (<1h):** the inventory writeup itself.

### B2.5 Lyapunov-function degree = moment order — NEW (framing)
- **Idea:** the two-moment certificate = a Lyapunov argument with a *degree-2* Lyapunov function (squared
  norm of the compressed form); the missing third moment = a *degree-3* Lyapunov function. Lyapunov's
  theorem: stability can be certified by ANY Lyapunov function; the certificate's value is capped by the
  degree of Lyapunov function it can *prove* positive — the rank–trace inequality is the dissipation
  bound.
- **Analogy:** Lyapunov function ↔ the quadratic form W; degree ↔ moment order.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing-only). Unifies P2/P9.4's hierarchy
  in dynamical vocabulary.

---

## Pool 3 — Immune system: repertoire generation, selection, self/non-self

**Core mapping:** the zeros = an immune *repertoire* generated by a structured pseudo-random process (the
primes); the certificate = *selection*; the crystal = an *autoimmune twin* the selection cannot reject
(same repertoire statistics, different "self" content); the third moment = the *self/non-self
discrimination* that naive repertoire statistics provably cannot supply.

### B3.1 Mixture deconvolution: the third moment is the *minimal sufficient statistic* for on/off-line separation — NEW (headline; structural reason for the P2 bypass)
- **Idea:** the zero configuration is a *mixture* of two populations (on-line atoms, off-line (1,1)-planes)
  and the certificate must bound the on-line proportion. Classical finite-mixture theory (Pearson 1894
  method-of-moments; Teicher 1963 identifiability — **reported standard, verify before use**): a
  2-component mixture is NOT identified by (mean, variance) — two different mixtures share the first two
  moments, and the crystal is exactly such a twin — but IS identified once the third moment (skewness) is
  included. **This is the structural reason the third moment is the documented bypass: it is the minimal
  moment order at which the on/off-line mixture becomes identifiable.**
- **Analogy:** mixture deconvolution ↔ separating on-line from off-line zeros; twin mixtures ↔ crystal vs
  reality; higher-order moments for more components ↔ the HL*(k) hierarchy (k populations need moments up
  to order 2k−1).
- **Needs:** (i) write the 2-component mixture model for the zero measure (components = on-line atoms +
  off-line pairs; moments = traces of Â^k); (ii) verify the identifiability order on the actual k_c
  penalty structure (2 moments fail, 3 succeed); (iii) the corollary for k components ↔ moment order 2k−1,
  matched against the multiplicity walls [AM].
- **Feasibility:** Low–Med. **Kill:** if the crystal is *not* a valid 2-component mixture twin of reality
  (i.e., the mixture model cannot reproduce the (tr, HS²) coincidence), the identifiability theorem does
  not apply — document the failure mode.
- **Cheapest probe (<1h):** mpmath: two explicit 2-component mixtures with identical (mean, variance) and
  different third moments, built from the actual {1,2} mark structure; confirm the third moment separates
  them (partially done here in §Pool 4 for the *twin spectra* — the mixture-model version is the new step).
- **Label:** NEW (the transfer is new here; the identifiability theorem is reported standard).

### B3.2 Repertoire sampling-noise baseline: the finite-T deficit is sampling noise; the excess is signal — NEW (P6 decomposition, overlaps [P5.5])
- **Idea:** immune repertoires are *sampled* (10⁸ of 10¹⁵ receptors present); observed statistics =
  generative model + sampling noise, and *selection strength* is read from the excess over the null's
  expected sampling noise (sonia/OLGA-style generative modeling, standard). Our finite-T deficit
  Δ(T) ~ 1/log T should be compared against the expected sampling noise of the null generative model
  (GUE/crystal at the same N); the **excess is the arithmetic signal**, and the ratio
  (observed/null) is the "selection factor" to track across T.
- **Analogy:** sampling noise ↔ finite-T artifact; selection factor ↔ the excess deficit.
- **Needs:** (i) Δ_null(N) for the sine process / crystal at N = 50..570 (tools/sine_sim.py exists);
  (ii) the ratio Δ(T)/Δ_null(N) plotted over T.
- **Feasibility:** Low. **Kill:** if Δ(T) ≈ Δ_null(N) at all T (ratio ≈ 1), the entire finite-T deficit is
  artifact (consistent with [AF]) — the documented negative that *closes* the "signal" side of P6.
- **Cheapest probe (<1h):** sine_sim at N = 50..570; compare with [AF]'s Δ(T) table.

### B3.3 Central tolerance: self/non-self needs a *global* constraint — KNOWN-OPEN (documentation; stops re-funding)
- **Idea:** the immune system solves self/non-self with *central tolerance* (thymic selection) — a global,
  organism-level check beyond pairwise repertoire statistics. The zeros' analog of central tolerance = the
  global fluctuation/rigidity structure (Selberg CLT variance √(log log T), unconditional [CD-V13];
  rigidity — [CD-V17]); the crystal violates it (deterministic, zero variance). But: like tolerance, the
  global check is per-*organism* (per-T), with no proven mechanism to enter a per-T certificate.
- **Analogy:** thymic selection ↔ global fluctuation constraints; autoimmunity ↔ the certificate's failure
  to reject the crystal.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none — this is the documented statement that
  rigidity/fluctuation inputs ([CD-V13], [P9.1]) are out of reach for per-T certificates; do not re-fund.
- **Cheapest probe:** none (already documented).

### B3.4 Clonal selection ↔ the LP/duality iterations — NEW (framing)
- **Idea:** affinity maturation = rounds of mutation + selection converging to high-affinity clones; the
  LP-dual iterations [CD-V2]/[ALP] are the same: each primal/dual pass refines the certificate, and the
  convergence 0.6725 → 0.68183123 is a *completed maturation* — the class is fully selected; no further
  rounds within the same data help (the box-cap [ALP]).
- **Analogy:** maturation rounds ↔ LP iterations; the affinity ceiling ↔ the box-cap 0.68183123.
- **Needs:** none. **Feasibility:** Low. **Kill:** none (framing). Strategic clarity: the in-class
  certificate is "fully matured"; only new *data types* (antigens) can advance it.

### B3.5 Repertoire holes: sampling holes vs true holes — NEW (framing, folds into B3.2)
- **Idea:** repertoire "holes" (missing specificities) split into sampling holes (present in the
  generative distribution) and true holes (deleted by selection); only a generative model distinguishes
  them. Our "holes" = configurations the certificate cannot exclude (the crystal family); distinguishing
  artifact-holes from real-holes needs the null model — the same probe as B3.2.
- **Analogy:** sampling vs true holes ↔ artifact vs real exclusions.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (fold into B3.2's probe).

---

## Pool 4 — Evolution as search: fitness landscapes, fixed points, the cost of selection

**Core mapping:** certificate value = *fitness*; moment order = *interaction order* (epistatic degree);
the crystal = an *evolutionarily stable strategy* of the two-moment fitness function; the moment hierarchy
2/3 → 5/6 → 13/18 → 1 = a *substitution sequence*; the finite-T deficit = *mutation pressure* decaying as
the population (T) grows.

### B4.1 NK ruggedness: moment order = interaction order K — NEW (arithmetic calibration, CHECKED NUMERICALLY here)
- **Idea:** Kauffman's NK model (standard): ruggedness (number of local optima) grows with the epistatic
  degree K; K = 0 (additive) is single-peaked, K = N is fully random. Our certificate's "K" = the highest
  moment it reads: K = 1 (two moments) → maximally rugged (many crystals = local optima); K = 2 (three
  moments) → smoothed. The NK *prediction* is that the third moment breaks the twin degeneracy of the 5/6
  wall. **The arithmetic check (done here): FALSE for the canonical twins** — every integer-spectrum twin
  of the extremal law with the same (tr, HS²) has m₃ = 2, identical to the extremal twin and to the
  GUE/HL* value (CHECKED NUMERICALLY, all 30 spectra of (6,8)). So the third moment cannot act by
  *excluding the twins*; it can only act by *tightening the LP* elsewhere — which is exactly [P6.5]'s
  open question, and the NK prior now shifts toward [CD-V3]'s kill criterion (a clean negative).
- **Analogy:** K ↔ moment order; local optima ↔ spectrally-twin configurations; ruggedness ↔ degeneracy.
- **Needs:** (i) the twin arithmetic (DONE here); (ii) the full (tr, ‖·‖², m₃, integrality) LP — P6.5.
- **Feasibility:** Low. **Kill/decide:** if P6.5's LP shows no tightening, P2 is a clean negative; the
  prior for that outcome is now quantified.
- **Cheapest probe (<1h):** done — the m₃ = 2 twin identity (this note); next is P6.5's LP with m₃ = 2.
- **Label:** NEW (probe done here); the NK analogy itself is framing.

### B4.2 ESS: the ceiling is an evolutionarily stable strategy — NEW (framing)
- **Idea:** an ESS cannot be invaded by any alternative *present in the population*. The two-moment
  certificate class is ESS-stable: no certificate using the same inputs exceeds the ceiling (the ceiling
  theorem is the invasion-proofness). New *data types* are invading mutations whose entry changes the
  fitness landscape (the ceiling moves).
- **Analogy:** ESS ↔ ceiling stability; invaders ↔ third moment / beyond-1 F.
- **Needs:** none. **Feasibility:** Low. **Kill:** none (framing). Strategic reading: only input-level
  mutations can invade; method-level mutations within the class cannot — reinforces funding P2/P3.

### B4.3 Haldane's cost of selection: the cost–benefit ledger for inputs — NEW (meta-tool)
- **Idea:** Haldane (standard): each substitution carries a selection cost; a population fixes alleles
  only so fast. Analog: each input type (moment order, bandwidth) carries a *cost* (analytic difficulty)
  and a *benefit* (certified proportion — [CD-V4]'s capacity curve, [CD-V5]'s support curve). Build the
  ledger: benefit per unit cost, ranked — a funding-priority tool.
- **Analogy:** substitution load ↔ analytic cost; fitness benefit ↔ certified proportion.
- **Needs:** [CD-V4]/[CD-V5] numbers + effort estimates. **Feasibility:** Low. **Kill:** none (meta-tool).

### B4.4 Fisher's fundamental theorem ↔ the moment hierarchy — NEW (framing, overlaps [P9.4])
- **Idea:** Fisher (standard): the rate of fitness increase equals the additive genetic variance. Analog:
  the certificate's rate of progress per moment order = the variance explained by that order; the moment
  hierarchy 2/3 → 5/6 → 13/18 → 1 ([AM]) is the progress curve of the expansion, and each step size is
  that order's "additive variance". P9.4's Edgeworth reading is the same content.
- **Analogy:** additive variance ↔ per-order certificate gain.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing).

---

## Pool 5 — Genetics of complex traits / heritability: variance decomposition, missing heritability

**Core mapping:** the two-moment certificate = a **variance decomposition** (tr = mean, HS² = variance
explained); the second-moment gap = **missing heritability**; and the missing-heritability literature has
*already run this playbook* — its resolution prescribes our funding order.

### B5.1 Missing-heritability roadmap isomorphism — NEW (framing; the pool's centerpiece)
- **Idea:** GWAS "missing heritability" split into artifacts (estimation bias, LD structure) + real effects
  (rare variants, epistasis, G×E). Our second-moment gap: the *in-class* part was the artifact — CLOSED by
  the LP dual [ALP]; the remaining gap is real and maps: **beyond-bandwidth-1 F ↔ rare variants**
  (hard-to-measure, carry most of the missing signal once measured properly); **third moment ↔ epistasis**
  (interaction variance invisible to single-locus scans); **finite-T artifacts ↔ G×E** (environmental
  confounding).
- **Analogy:** missing heritability ↔ second-moment gap; rare variants ↔ beyond-1 F; epistasis ↔ third
  moment; G×E ↔ kernel artifacts.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing). **Value:** the missing-heritability
  playbook (measure rare variants better FIRST, then add epistasis kernels, correct environment) prescribes
  our order: beyond-1 F (P3) before third moment (P2), with P6 (finite-T "environmental control") running
  in parallel — an independent justification of the roadmap.
- **Cheapest probe:** none (documentation).

### B5.2 Epistasis GRM / Hadamard-power kernel statistic — NEW (probe)
- **Idea:** variance-component genetics estimates epistasis by adding *elementwise-power GRMs* (G×G kernel
  = Hadamard square of the relationship matrix; GREML/GCTA methodology, standard). The analog object for
  the zero configuration: the Hadamard cube W∘W∘W and its trace — a *third-order kernel statistic*
  distinct from tr Â³ (which mixes W-powers along closed walks). Compute it on real zeros vs the crystal:
  a second, independent third-order probe for P2 (complements the skewness probe [P3.1]).
- **Analogy:** epistasis kernel ↔ Hadamard-power of W; G×G variance component ↔ third-order certificate
  input.
- **Needs:** real zeros + crystal generator + the cube trace (trivial from the W_T matrix in tools/finitet).
- **Feasibility:** Low. **Kill:** if tr(W∘W∘W) correlates perfectly with the skewness statistic (same
  information), fold into [P3.1]; document.
- **Cheapest probe (<1h):** from [AF]'s W_T matrices, tr(W∘W∘W)/N at T = 100..700 vs the crystal's.

### B5.3 GREML variance-component reading: the gap is estimation variance; only new kernels reduce it — NEW (framing)
- **Idea:** GREML: h² is estimated from the GRM; the SE is fixed by the effective number of independent
  pairs — no within-kernel shrinkage. The certificate's "SE" = the second-moment gap (the ceiling); it
  cannot shrink within the two-moment kernel — exactly [ALP]'s finding. New kernels (B5.2, third moment)
  are the only variance reducers.
- **Analogy:** GRM ↔ W; SE of h² ↔ the ceiling gap; new kernels ↔ higher moments.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing; independent restatement of the
  in-class closure).

### B5.4 LD structure ↔ kernel bandwidth — NEW (framing)
- **Idea:** linkage disequilibrium (correlation of nearby markers) defines LD blocks; signals within a
  block are redundant. The zeros' "LD" = the pair correlation at scale ~1/log T (bandwidth one); the
  λ ≤ 1 window is an LD block; long-range LD / rare variants = beyond-1 F.
- **Analogy:** LD blocks ↔ the bandwidth-one window; long-range LD ↔ beyond-1 F.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (framing; supports B5.1's order).

---

## Pool 6 — Epigenetics (in place of ecology, which is covered under [P9.5]): same genome, different marks

**Core mapping:** the genome = the zero *configuration* (fixed); the marks {1,2} = the *epigenome*
(multiplicities, mostly m = 1 = unmethylated, some m = 2 = doubly marked); the certificate reads only the
*marginal* mark budget (Σ marks = N via tr); the *joint* mark placement is third-order information.

### B6.1 Methylation-map framing of the marks — NEW (framing; as an input, KNOWN-OPEN)
- **Idea:** the crystal's mark map (2/3 ones, 1/6 twos, 1/6 zeros, 256-periodic) is a *deterministic
  methylome*; reality's is (empirically) all-ones. The certificate reads only marginal budgets; the joint
  mark placement — *which loci are double-marked, and whether doubles cluster* — is third-order
  information the two moments cannot see.
- **Analogy:** methylation pattern ↔ the mark map; marginal budget ↔ tr; co-regulation ↔ joint mark
  placement.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none; the concrete transfer is B6.3's census.
- **Cheapest probe:** none (framing).

### B6.2 The row shadow prices are the certificate's "epigenetic clock" — NEW (targeted probe for P3)
- **Idea:** Horvath's epigenetic clock (standard) predicts age from ~350 CpGs — a small subset carries the
  signal. attack-lpdual's row shadow prices: middle rows (j = 64..192) are individually most valuable
  (1.5–2·10⁻³ each); collectively all 255 near-CUE rows pin the value to 2.5·10⁻⁶; one row alone allows
  ≈ 0.89. The shadow-price vector IS the clock weights of the certificate — and it locates WHICH beyond-1
  rows would move p₁ most.
- **Analogy:** clock CpGs ↔ high-shadow-price rows; subset robustness of the clock ↔ the row sweep (LP-B′).
- **Needs:** extend the lpdual LP with *synthetic* beyond-1 rows (F = 1 on [1,A]); read the per-row
  marginal. This refines [CD-V5]'s aggregate curve into a per-row target for the cheapest P3 input.
- **Feasibility:** Low. **Kill:** if all beyond-1 rows have equal marginal value (flat per-row curve), the
  aggregate curve is the whole story — record.
- **Cheapest probe (<1h):** add rows j = 257..320 with F = 1 to tools/lpdual; report marginals.

### B6.3 Mark co-regulation census: the crystal's joint mark placement vs third-order input — NEW (overlaps [CD-V4])
- **Idea:** epigenetic co-regulation = correlation of mark states across loci. The crystal's mark field is
  explicit and periodic; its *third-order mark statistic* (triple correlations of the mark field) is
  computable now. Pinning it into the capacity LP ([CD-V4]'s probe) prices the *mark-placement* input
  separately from the *count* input.
- **Analogy:** co-regulated methylation ↔ correlated marks; the mark field's third moment ↔ a higher-order
  input.
- **Needs:** the 256-law's mark field (LawN256.lean) + the capacity LP.
- **Feasibility:** Low. **Kill:** if the crystal's mark triple-correlations are already GUE-like, the
  placement carries no signal (the law is third-order-innocent) — record; if far from GUE, the law is
  third-order-guilty and P2's value rises.
- **Cheapest probe (<1h):** triple-correlation of the 256-law mark field vs the GUE value 2.

### B6.4 Epigenetic reprogramming ↔ the finite-T flow — KNOWN-OPEN (framing), trend TESTED-OPEN [AF]
- **Idea:** marks are erased and re-established in development ("reprogramming"); the finite-T flow
  (Δ(T) ~ 1/log T, [AF]) is the zeros' reprogramming between scales. If it is convergent (deficit → 0),
  the finite-T slack is transient; the honest content: Δ(T) > 0 *decaying* means the certificate is
  "reprogramming toward" the crystal-compatible value — i.e., no asymptotic slack from finite-T [AF].
- **Analogy:** developmental reprogramming ↔ the T-flow; convergence ↔ the asymptotic-slack question.
- **Needs:** none new. **Feasibility:** Low. **Kill:** none (honest restatement of [AF]).
- **Cheapest probe:** none (documentation).

---

## TOP 10 (EV × feasibility × cheap-probe)

1. **B3.1 — Mixture identifiability: the third moment is the minimal sufficient statistic for on/off-line
   deconvolution.** The structural *reason* the P2 bypass exists and a prediction of the moment order for
   k-component mixtures (check against the multiplicity walls [AM]). Probe: two explicit 2-component
   mixtures with identical (mean, variance) — under an hour.
2. **B4.1 — Twin-moment arithmetic (DONE here): every integer-spectrum twin of the extremal law shares
   m₃ = 2 = GUE/HL\***. Shifts the P2 prior toward [CD-V3]'s clean-negative kill criterion; the next step
   is P6.5's LP, now with a quantified expectation. Probe: done; P6.5's LP follows.
3. **B1.1 — Designability count of the two-moment class.** Quantifies wall robustness (how many crystals
   fit the data) and the third moment's shrinkage power. Probe: sample the N = 256 feasible set — hours.
4. **B6.2 — Per-row beyond-1 shadow-price curve.** Locates the cheapest P3 input (which α > 1 row buys the
   most p₁), refining [CD-V5] into a per-row target. Probe: synthetic F = 1 rows in tools/lpdual — under an
   hour.
5. **B1.4 — Decoy-discrimination screening.** Empirically prices ALL candidate inputs (spacing, variance,
   skewness, entropy) in one pass; the largest-margin statistic is the one to make provable. Probe:
   10³ crystal samples × 5 statistics — under an hour.
6. **B5.2 — Epistasis Hadamard-cube kernel statistic tr(W∘W∘W).** A second, independent third-order probe
   for P2, distinct from skewness. Probe: [AF]'s W_T matrices — under an hour.
7. **B3.2 — Repertoire sampling-noise baseline.** P6 decomposition: Δ(T) vs the null model's expected
   sampling noise; the excess is the arithmetic signal; a ratio ≈ 1 closes P6's signal side. Probe:
   sine_sim at N = 50..570 — under an hour.
8. **B1.3 — Frustration index of the zero configuration.** Locates WHICH scales/α carry real deviation
   from the crystal, guiding P3. Probe: per-row deviations from [AF]'s W_T — under an hour.
9. **B2.2 — Motif census: the full 3-node statistic sweep.** Sharpens P2's probe from skewness to the
   complete third-order census; identifies the strongest third-order signal. Probe: 3-point histograms —
   hours.
10. **B1.2 — Contact-order curve validation.** Imposes the folding shape prior (monotone-concave-
    saturating) on [CD-V5]'s 1.04/1.26/1.70 numbers — a cheap adversarial check of the roadmap. Probe:
    fit — minutes.

**Strategic reading:** biology's yield is (i) **B3.1** — a structural explanation of *why* the third
moment is the minimal bypass (mixture identifiability), (ii) **B4.1** — an honest prior *against* a cheap
P2 win (the twins share m₃ = 2, checked here), which sharpens the value of running P6.5's LP early, (iii)
**B6.2/B1.1/B1.4** — three cheap measurements that price where and how much the wall could move, and (iv) a
large set of honest reframings ([B1.5], [B2.1], [B2.3], [B2.4], [B3.3], [B5.1], [B5.3], [B5.4], [B6.4])
that mostly stop re-derivation and give vocabulary. **No biology vector invents a new proof input** — the
inputs remain beyond-1 F (P3), the third moment (P2), and provable repulsion/rigidity (KNOWN-OPEN); biology
contributes *which* to fund, *how to expect it to behave*, and *three new cheap diagnostics* (designability
count, shadow-price clock, decoy screen).

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

### W-B1. "The 1/log T deficit is critical slowing down at a T = ∞ phase transition; the crystal and reality are coexisting phases of the certificate's Landau free energy" — CONJECTURED (wild; falsifiable in a day)
**For:** two configurations with identical two moments = two "phases" with identical free energy at the
two-moment truncation — a *degenerate Landau theory*; critical phenomena predict *divergent relaxation*
(critical slowing down) at the transition; the certificate's order parameter (the simple fraction) would
relax logarithmically. The wild content is *falsifiable*: if the deficit exponent is set by the window
(kernel artifact, [AF]), it must be **window-dependent**; if it is universal (arithmetic), window-
independent. Run Δ(T) with 2–3 different windows.
**Against:** the phase-transition reading is an analogy; the kernel-artifact attribution is the current
belief. **Novel fragment:** the window-sweep falsification test is real, cheap, and decides between the
two readings — either outcome is a finding (artifact confirmed, or a new P6 anomaly).
**Cheapest probe:** extend tools/finitet to a flat and a smoother window; compare Δ(T) exponents.

### W-B2. "The primes' 'genetic code' is mutation-optimized: the certificate's robustness to prime-data perturbation is the code's fitness" — CONJECTURED (wild framing; the sensitivity probe is real)
**For:** Freeland–Hurst (standard; verify before use) showed the genetic code *minimizes* the impact of
point mutations — a proven optimization of an error-correcting code. Analog: measure the two-moment
certificate's robustness to perturbing the prime-side input (λ_T sums, Chebyshev terms) by relative error
ε; if the certificate is insensitive to exactly the perturbations it cannot control (the P6 error terms),
the finite-T story is robust; if sensitive, P6's errors bite at the constant scale.
**Against:** the "optimization" claim is untestable directly (we cannot see all alternative certificates);
only the sensitivity analysis survives. **Novel fragment:** a quantitative P6 error-sensitivity map
(which prime-side term's uncertainty costs the most certificate value).
**Cheapest probe:** perturb the prime sums in the W_T construction by ε = 10⁻³..10⁻¹; measure the
certificate value's response at T = 200..700.

### W-B3. "The zeros are an adapted immune repertoire; RH is the final adaptation state; the third-order diversity statistic is the adaptation order parameter with a universal value" — CONJECTURED (likely equivalent-formulation; probe overlaps existing)
**For:** if the primes are the antigenic environment and the zeros the co-adapted repertoire, then a
*provably adapted* system has a universal third-order diversity statistic (RMT S₃ = 2), and the P2 bypass
is the statement "the repertoire reached RMT-optimal diversity". The wild fragment: the *empirical
convergence law* of the zeros' third-order statistic to the universal value is measurable and has a
specific error exponent.
**Against:** the universality claim IS RH + pair correlation (no new theorem); the "adaptation" is
renaming; the convergence-law probe is [P3.1]/B2.2's probe. **Honest verdict:** keep the framing as a
mnemonic; do not fund beyond the existing third-moment probes.

---

## Label inventory

- **NEW** (invented here, untested or probe-now): B1.1, B1.2, B1.3, B1.4, B2.1, B2.2, B2.5, B3.1, B3.2,
  B3.4, B3.5, B4.1 (twin arithmetic CHECKED NUMERICALLY here), B4.2, B4.3, B4.4, B5.1, B5.2, B5.3, B5.4,
  B6.1, B6.2, B6.3, W-B1, W-B2, W-B3 (conjectured by construction, each with a kill criterion).
- **KNOWN-OPEN** (core is open / already flagged in our notes; new framing only): B1.5 (funnel-completing
  inputs = P2/P3), B2.3 (May threshold ↔ ceiling), B2.4 (sign-pattern inventory; overlaps [CD-V17]),
  B3.3 (central tolerance = global/rigidity inputs, overlaps [CD-V13]/[P9.1]), B6.4 (asymptotic-slack
  question), and B6.1/B5.1/B5.3/B5.4 as *inputs*.
- **KNOWN-DEAD** (framing-only, or documented in [CD-A#]/attack notes): none invented-dead here; the
  closest are B2.3 and B3.3, which are KNOWN-OPEN-with-documented-death (their only inputs are
  artifact-level or per-T-unreachable, citing [AF] and [CD-V13]).
- **TESTED-OPEN**: B4.1's twin-moment identity (CHECKED NUMERICALLY in this note — all 30 integer spectra
  of (6,8) have m₃ = 2); B6.4's trend (via [AF]'s Δ(T) > 0, ~1/log T — the trend, not the asymptote, is
  open); the rest of the diagnostics are probe-now states.
- **Reported-standard biology facts (verify before use):** finite-mixture identifiability (Pearson 1894;
  Teicher 1963), Freeland–Hurst code optimization, Horvath epigenetic clock, GREML/GCTA Hadamard kernels,
  sonia/OLGA generative repertoire models, May 1972, Kauffman NK, Haldane cost, Fisher's fundamental
  theorem, contact order, minimum frustration, Go models.

**Honest closing note:** the biology angle's strongest NEW contributions are (i) **B3.1** — the
mixture-identifiability argument that the third moment is the *minimal sufficient statistic* for
on/off-line deconvolution (a structural reason, not just "P2 is open"), (ii) **B4.1** — the arithmetic
calibration (checked here) that the canonical 5/6-wall twins *share* the GUE third moment, setting a
quantified prior for P6.5's LP, (iii) **B6.2** — the shadow-price-as-epigenetic-clock probe that locates
the cheapest beyond-1 input row, and (iv) the cheap diagnostics (designability count B1.1, decoy screen
B1.4, sampling-noise baseline B3.2, frustration index B1.3, epistasis kernel B5.2) that price the input
space empirically. The persistent wall — beyond-1 F, third moments, repulsion — is unchanged, but the
biology lens says *why*: like native-vs-decoy, self-vs-non-self, and genetic-vs-environment discrimination,
the two-moment "intensity" data cannot identify the structure; the third measurement (phase) is the minimal
identifying input, and the missing-heritability playbook says measure the "rare variant" (beyond-1 F)
first.
