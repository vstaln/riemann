# Idea Generator: neuroscience & systems-medicine attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (analogy-domain-transfer + brainstorm + judgment-under-uncertainty). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack; every probe is cheapest-first (<1h).
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Neuroscience / systems-medicine facts
below are standard textbook-level knowledge (Kuramoto, echo-state networks, compartment models, DFA, multiscale entropy,
EEG slowing) and are named as such; anything I cannot vouch for at that level is flagged **"reported standard — verify
before use."** Every *idea* is CONJECTURED by construction and carries a kill criterion. Vectors killed during generation
are recorded with the reason. **Code-backed verification:** every number in the Probe Results section was produced by the
cited script (new self-contained dir `tools/probes_neuro/`; none of the canonical `tools/` scripts were edited).
**Labeling** (per physics-catalog convention): NEW (invented here, untested) / KNOWN-DEAD (killed in earlier rounds; cited)
/ KNOWN-OPEN (a known open problem or route already flagged in our notes; cited) / TESTED-OPEN (numerically tested by our
own tools, still open).
**Cross-references:** idea-generator-crossdomain.md [CD-V#/W#/A#], idea-generator-physics.md [P#.#],
idea-generator-biology.md [B#.#], idea-generator-music-ling.md [ML#], idea-generator-ml-eco.md [ECO-B#], attack-kernel
[AK], attack-ceiling [AC], attack-lpdual [ALP], attack-nevanlinna [AN], attack-multiplicity [AM], attack-finitet [AF],
attack-sandbox [AS], attack-twobandwidth [ATB], attack-f1curve [AF1], close-inclass-gap [CIG]. Empirical F̂(α) status:
`tools/data/hot_hand_calib_results.json` (no attack-hot-hand.md exists; the JSON is the only hot-hand artifact — see
§0).

---

## 0. The honest map of where we stand (what new *input* could move what)

State of the art (PROVEN / CHECKED NUMERICALLY in prior notes): the two-moment certificate gives ≥ 0.67250070
(Theorem D; cosine window optimal [AK]); the bandwidth-one class is CLOSED at **0.68183123 = p₀ + |E(1)|**, the LP dual
attains the Lean ceiling, the shadow price of the certified simple fraction p₁ is **exactly 1**, and no missing
constraint exists inside bandwidth one ([ALP], [CIG]). The Nevanlinna reframe is a documented negative: the gap
0.6725 → 0.6818 is a **second-moment gap Δm₂ = 0.0093**; the 256-law is itself integer-marked so integrality cannot
exclude it; a third-moment lower bound m₃ ≥ 2 would separate the law (m₃(law) = 1.9545 < 2) but is unprovable in the
Rudnick–Sarnak range ([AN]). The two-bandwidth third-moment certificate is a clean negative (m₃(1/2) = 5, max 0.8071 <
5/6; [ATB]). The sandbox: the certificate is a **repulsion statement, not an RH statement** — real world reads ≈ 0.70
at finite T trending to 0.6725, lattice world ≈ 0.977, Poisson world empty; a few % of off-line pairs break 0.6725
([AS]). Music-ling probes: the finite-T deficit concentrates at u < 1 (short-range arithmetic, not kernel-edge; [ML-R6]);
m₂/m₃ deficits decay ~1/log T above h ≈ 3000 with amplitude 0.288 ([ML-R5]); the ξ′ zero set carries genuinely
different moment data (m₂(ξ′) = 1.2294 vs m₂(ξ) = 1.3215), funding the joint derivative-moment certificate ([ML-R5],
M5.4). Empirical F̂(α): within [0,1] tracks GUE; the beyond-1 blocks (1.5, 2.0) read ≈ 1.0 (plateau, GUE-consistent)
(`hot_hand_calib_results.json`, block_alpha 1.5/2.0 → block_zeta_mean 1.00/0.97; CHECKED NUMERICALLY in that artifact).

**What this pool can realistically contribute, ranked by ambition:**
1. *New proven-input-adjacent vectors* — rare; the strongest is N5.1 (Prony/identifiability from measured moments), which
   now has a code-backed probe (N-R1) with two real findings (implied p₁ matches the finite-T certificate; the 4th-moment
   deficit is ~5× the 2nd-moment deficit in relative terms — a quantified caution for P2).
2. *New diagnostics* — N6.3 (DFA rigidity: bulk zeros more anticorrelated than GUE — code-backed, N-R2), N6.2 (multiscale
   entropy: no complexity loss — code-backed negative), N3.2 (Fiedler/algebraic-connectivity rigidity), N6.1 (spectral
   band-ratio), N2.2 (cluster-size distribution), N1.1 (Kuramoto soft-mode edge scaling).
3. *Framings that stop re-derivation* — N1.5 (moment mistuning, = [ML-M1.1]), N2.3 (= W-B1's window-sweep), N5.3 (SIR =
   [ECO-B4]/E4), N4.2 (capacity = [B6.2]), N6.5 (= [ECO-B1]).
The persistent wall — beyond-1 F, third moments, repulsion — is *phase* information a two-moment intensity certificate
cannot see [P6.4]; neuroscience arrives at the same wall through *synchrony order parameters*, *criticality*, *connectome
spectra*, *reservoir stability*, and *complexity diagnostics* — independent evidence the wall is structural.

**Abstracted problem (the object this pool maps to):** a configuration of N marked points, two scalar intensity
measurements (mean, pair-correlation intensity on one bandwidth), and a decoy configuration matching both measurements
exactly but with a worse line-fraction; the certificate cannot exclude the decoy; the only escapes are a third
measurement (phase — third moment / beyond-1 F) or a proven repulsion/rigidity constraint. In one sentence: **"an
intensity-only two-measurement discriminator has a decoy twin; only phase (higher-order) or rigidity (repulsion) data
can break it."** Neuroscience and systems medicine are full of this shape: order parameters that cannot distinguish
microstates, critical systems whose moments do not close, reservoirs that are stable-but-not-characterized by a spectral
radius, compartment models unidentifiable from limited decay data, and complexity diagnostics that separate healthy from
pathological spectra.

---

## Pool 1 — Neural oscillations / synchrony: Kuramoto, phase-locking, common input

**Core mapping:** the certificate class's "order parameter" = the certified simple fraction; the Kuramoto order
parameter squared r² = (1/N²)Σ_{ij}cos(θᵢ−θⱼ) is *literally a pair-sum of phases* — the same shape as our ‖W‖²_HS
(off-diagonal pair sum of Gabor features). The Kuramoto critical coupling K_c is the spectral-radius line-crossing of the
linearized incoherent state — a single number that separates "synchronized" from "incoherent", exactly how 0.6818
separates "certifiable" from "not". The zeros' analog of the Kuramoto order parameter (the Fourier mode of the zero
phases) is *unconditionally computable from the prime side* — but that is already P2.1's W_T-level spectral form factor
(cross-ref; do not duplicate).

### N1.1 The 0.6818 wall as a Kuramoto critical coupling; soft-mode edge scaling — NEW (diagnostic refinement of [CD-V1]/[P1.3])
- **Idea:** in the Kuramoto model the *stability of the incoherent state* is governed by a discrete eigenvalue of the
  linearized operator crossing zero at K_c (Strogatz–Mirollo 1991 — *reported standard, verify before use*); at finite N
  the critical coupling is smeared over a width ~N^{−2/3} and the order parameter below K_c scales as N^{−1/3}
  (finite-N Kuramoto — *reported standard*). Our wall: the certificate's "incoherent state" (the 256-law) becomes stable
  at 0.6818; the near-zero eigenvalues of W_T (min eigenvalue ~1e-17·λmax, [AF]) are the "soft modes" of the certificate.
- **Analogy → our setting:** the *density of small positive eigenvalues* of W_T (the [CD-V1]/[P1.3] edge histogram) is the
  finite-N shadow of the mode that crosses at criticality; the *prediction*: if reality sits at the certificate's
  critical point, the soft-mode density follows the Kuramoto finite-N scaling; if it follows a GUE edge instead, the
  certificate class is not the right "ensemble" for reality.
- **Needs:** W_T spectra at several T (exists, [AF]/[CD-V1] machinery); a fit of the near-zero eigenvalue density vs N.
- **Feasibility:** Low. **Kill:** if the edge density is GUE-like at every T (no scaling collapse), the criticality
  reading is decorative — record as diagnostic only. Value: refines P1.3's edge statistic with a physics prior and gives
  the finite-T scaling its first quantitative target.
- **Cheapest probe (<1h):** reuse [AF]/[CD-V1] spectra; histogram the smallest 5% of eigenvalues at T = 200–700; compare
  the density's N-scaling with N^{−2/3} (Kuramoto) vs the GUE edge prediction.

### N1.2 Arnold tongues / phase-locking ↔ the bandwidth-one window as a locking region — NEW (re-quantification of [AS])
- **Idea:** phase-locking occurs in *Arnold tongues* — parameter regions where the oscillator's frequency locks to the
  drive; the tongue's width is the *locking range*, outside which the oscillator slips. For a *detuned* oscillator (off
  the resonance), locking fails — the detuning is the analog of our off-line depth β.
- **Analogy → our setting:** the certificate "locks" to the on-line structure within a detuning tolerance; [AS] measured
  the crossing: shallow off-line pairs (β = 0.1) survive to f ≈ 0.02–0.05, deep pairs (β = 0.3) break 0.6725 between
  f = 0.01 and 0.02. The sandbox's β-f table IS the Arnold tongue of the certificate. The NEW fragment: report the
  tongue boundary as a *curve* β_c(f) (one line from [AS]'s existing table) so any future repulsion input knows exactly
  what depth of off-line structure it must exclude.
- **Needs:** nothing new — a re-plotted [AS] table. **Feasibility:** Low (one-line). **Kill:** n/a (documentation of an
  existing measurement in locking vocabulary).

### N1.3 Common-input problem ↔ the off-diagonal as shared variance — NEW (one-line re-analysis of [AF])
- **Idea:** neurons receiving *common input* show correlated spiking; the common-input literature estimates the
  *shared-variance fraction* from pairwise spike statistics (standard neurophysiology). Correlated noise = the
  off-diagonal of the covariance.
- **Analogy → our setting:** the off-diagonal pair sum is the "shared variance" of the zero configuration; the
  measured split in the [AS] world-(a) table (diag ≈ 1.140, offdiag ≈ 0.151 per N at T = 500) gives a
  **shared-variance fraction ≈ 0.151/1.291 ≈ 0.12** — the fraction of the second moment carried by pairs. The NEW
  fragment: decompose the finite-T deficit Δ(T) into the diagonal (single-zero) vs off-diagonal (shared/pair) parts —
  [ML-R6] already says the deficit is short-range pair correlation, so the prediction is "mostly shared"; the honest
  one-line check is a re-split of [AF]'s data.
- **Needs:** [AF]'s finitet pair-sum (small modification). **Feasibility:** Low. **Kill:** if the deficit is *not*
  pair-dominated (contradicting [ML-R6]), a real finding. Otherwise: confirms R6 with a second bookkeeping.

### N1.4 EEG frequency bands ↔ the α-window decomposition — NEW (diagnostic; overlaps [P10.2])
- **Idea:** EEG separates power into delta/theta/alpha/beta/gamma bands; clinical diagnostics use *band-power ratios*
  (e.g., theta/alpha) as spectral biomarkers (standard). The bands are a coarse spectral decomposition.
- **Analogy → our setting:** our "bands" are the bandwidth-A windows — [AF1]'s F ≡ 1 on [0,A] curve is the "band-power
  profile" of the certificate's input space. The NEW statistic: the *band-ratio* of W_T's spectrum — the mass of
  eigenvalues below/above the median (or below/above the crystal's eigenvalues {1,2}) — a single spectral-shape number
  comparing reality vs crystal vs GUE at *fixed two moments*.
- **Needs:** [AF]/[CD-V1] spectra. **Feasibility:** Low. **Kill:** if the ratio is identical across worlds (the moments
  fix the shape too), the spectrum carries no additional slack — a P7 negative. Value: another spectral-shape slack probe
  (complements P10.2's entropy).
- **Cheapest probe (<1h):** from [AF]/[CD-V1] spectra, print mass(λ < median)/mass(λ ≥ median) for real vs crystal vs
  GUE-synthetic.

### N1.5 Moment "beating" / detuning — KNOWN-DEAD (as new; = [ML-M1.1], probe done [ML-R5])
- **Idea:** two mistuned partials produce beating; the measured finite-T moments are "partials" whose mistuning
  Δm_k(T) is the beating of the spectrum.
- **Death (documented, [ML-R5]):** already measured — m₂/m₃ deficits decay ~1/log T above h ≈ 3000, amplitude 0.288;
  this vector's probe is done. Recorded to prevent re-derivation.

---

## Pool 2 — Criticality in neural systems: SOC, avalanches, the critical brain

**Core mapping:** the task hint asks whether the ZERO CONFIGURATION is a "critical system" (power-law-ish gap statistics
+ rigidity). Honest answer, from existing probes: **NO on the power-law reading, YES on the marginal reading.** The gap
statistics are Wigner, not power-law (KS 0.08 vs Wigner, Zipf fit not a power law, [ML-R3]) — the zeros are *not*
avalanche-critical. But the *counting process* is marginally/critically structured: count variance grows like log
(Selberg CLT, √(log log T); unconditional [CD-V13]), and the finite-T deficit decays logarithmically (~1/log T, [AF],
[ML-R5]) — the signatures of a marginal (critical) system, not an exponential/Gompertz approach (N5.4). Criticality
theory's lesson about moment structure: **at criticality the order-parameter moments do not close** — the first two
moments fix the mean-field behavior but the *universality class* lives in higher moments and fluctuations. That is a
structural explanation (independent of [B3.1]/[P9.4]) of why the third moment is the natural next input: a critical
system is *generically* two-moment-undetermined.

### N2.1 Criticality ↔ the two-moment insufficiency is generic, not special — NEW (framing; the honest adjudication of the hint)
- **Idea:** in equilibrium critical phenomena, observables near T_c satisfy scaling O(L) = L^{−κ}·f((T−T_c)L^{1/ν});
  the *moments of the order parameter* are not independent — but the *first two* fix only the Gaussian/mean-field part;
  the anomalous dimension (universality class) shows up first in the third/fourth cumulant (reported standard).
- **Analogy → our setting:** the certificate is the mean-field (two-moment) order parameter; the 256-law and reality are
  *two configurations with identical mean-field data but different higher cumulants* — exactly the situation criticality
  theory says is generic. The zeros' log-variance (Selberg CLT) is the "divergent susceptibility" at the critical point;
  the crystal has O(1) variance — it is the *ordered phase*, not the critical point.
- **Needs:** none new. **Feasibility:** Low (documentation). **Kill:** n/a. Value: explains *why* two moments fail
  *generically* and why fluctuation inputs ([CD-V13], [B3.3]) are the principled (but per-T-unreachable) escape.

### N2.2 Avalanche / cluster-size distribution at ε-neighborhoods — NEW (probe; overlaps [B1.4])
- **Idea:** neuronal avalanches are clusters of near-simultaneous activity with power-law size distribution (Beggs–Plenz
  2003 — *reported standard*); the *cluster-size* observable for a point process is the distribution of connected
  component sizes in the graph with edges between points closer than ε.
- **Analogy → our setting:** the gap-level avalanche idea is already REFUTED ([ML-R3]: gaps are Wigner, not power-law);
  the *cluster-size* statistic at ε ∈ {0.5, 1, 2} mean spacings is a *new* repulsion diagnostic not in R3's battery —
  GUE/sine: Poisson-tail cluster sizes (no giant cluster); crystal: one giant cluster; Poisson: a spectrum with large
  clusters. Reality's cluster distribution measures the repulsion the certificate cannot read.
- **Needs:** cached zeros + a small connected-components routine. **Feasibility:** Low. **Kill:** if reality's
  cluster-size distribution matches GUE at every ε (expected), a documented negative that closes the "avalanche"
  reading; if it shows excess large clusters, an anomaly worth escalating.
- **Cheapest probe (<1h):** cluster-size histogram at ε ∈ {0.5, 1, 2} for real vs synthetic GUE vs crystal vs Poisson.

### N2.3 Finite-size scaling / universality of the deficit amplitude — KNOWN-OPEN (cross-ref [W-B1]; amplitude TESTED-OPEN [ML-R5])
- **Idea:** at criticality, finite-size corrections are *universal* in shape (the amplitude and exponent carry the
  universality class). Our finite-T deficit Δ(T) ≈ c/log T with measured amplitude c ≈ 0.288 above h ≈ 3000
  ([ML-R5], CHECKED NUMERICALLY). The *universality* question: is c window-independent (arithmetic, universal) or
  window-dependent (kernel artifact)? [ML-R6] says the deficit is short-range arithmetic (u < 1), which *predicts*
  c is universal — the window-sweep test (biology [W-B1]) decides.
- **Analogy → our setting:** FSS collapse ↔ the deficit's T-scaling; the amplitude = the "critical exponent".
- **Needs:** [AF]'s finitet with 2–3 windows (the [W-B1] probe). **Feasibility:** Low (already spec'd as [W-B1]; do not
  duplicate — this entry records the *prediction* from [ML-R6]: smoothing the window should NOT change c).
- **Kill:** if c changes with the window, [ML-R6]'s u<1 attribution is wrong (a finding).

### N2.4 Branching ratio of the zero process — NEW (one-line measurement from [AS])
- **Idea:** critical neural systems have branching ratio σ ≈ 1 (average descendant count; Beggs–Plenz — *reported
  standard*). The zero process's analog "branching ratio" = the ratio of shared (pair/off-diagonal) to independent
  (diagonal) second-moment mass.
- **Analogy → our setting:** from [AS] world (a) (T = 500): offdiag/diag ≈ 0.151/1.140 ≈ **0.13** — the zero process is
  *sub-branching* (σ ≈ 0.13 ≪ 1), i.e. strongly rigid, far from critical σ = 1 and far from Poisson's σ ≈ 1. This
  quantifies the "repulsion statement" reading of the certificate [AS] in one number.
- **Needs:** nothing new (re-derive the ratio from [AS]'s table). **Feasibility:** Low. **Kill:** n/a (measurement).

---

## Pool 3 — Network neuroscience: connectome spectra, eigenmodes, the rich club

**Core mapping:** W_T is a "connectome" of the zero grid (pairwise contacts mediated by the zero measure); its
eigenmodes are connectome harmonics. Spectral graph theory's standard content: the *Fiedler value* (second-smallest
Laplacian eigenvalue, algebraic connectivity) measures how tightly a graph is connected — a *rigidity* number; the
*degree distribution* detects hubs (the rich club). All diagnostics (no proven certificate input), but they measure the
*repulsion strength* the certificate provably cannot read — pricing P1.4's open problem from the data side.

### N3.1 Connectome eigenmodes of W_T: participation ratio / localization — NEW (diagnostic; overlaps [P5.3]/[P10.2])
- **Idea:** connectome harmonics (Atasoy et al. — *reported standard, verify before use*) decompose brain activity into
  eigenmodes of the structural Laplacian; eigenmode *localization* (inverse participation ratio) distinguishes
  delocalized (homogeneous) from localized (modular) structure.
- **Analogy → our setting:** the inverse participation ratio (IPR) of W_T's eigenvectors — delocalized plane waves (both
  GUE-like *and* the translation-invariant crystal), localized only if the zero structure is modular. The honest
  expectation: IPR ~ 1/N everywhere (both nulls are delocalized), so this is a *null-confirming* diagnostic; a localized
  mode would be a real anomaly.
- **Needs:** W_T spectra ([AF]/[CD-V1]). **Feasibility:** Low. **Kill:** if all eigenvectors are delocalized (expected),
  document — the zero structure is homogeneous at every scale, consistent with [ML-R2]'s periodicity negatives.

### N3.2 Fiedler value / algebraic connectivity of the δ-neighborhood zero graph — NEW (probe; the pool's headline)
- **Idea:** the Fiedler eigenvalue λ₂(L) of a graph's Laplacian is its algebraic connectivity: rigid/well-connected
  graphs have large λ₂, fragmented graphs λ₂ ≈ 0 (Fiedler 1973, standard). For a point set with edges between points
  closer than δ, λ₂ measures the set's *rigidity* — the repulsion strength the certificate cannot read ([P1.4],
  KNOWN-OPEN as an input).
- **Analogy → our setting:** build the δ-neighborhood graph of the real zeros (δ ∈ {0.5, 1, 2} mean spacings); report
  λ₂ and the degree distribution vs (a) rigid lattice, (b) synthetic GUE, (c) Poisson. Prediction: lattice λ₂ high,
  Poisson ~ 0, real and GUE intermediate with real > GUE (consistent with [ML-R1]'s fine-scan: g below GUE for
  u < 0.45, and with the DFA finding N-R2 below). A quantified rigidity ladder prices what a *provable* repulsion input
  would have to beat.
- **Needs:** cached zeros; a sparse Laplacian eigen routine (numpy/scipy). **Feasibility:** Low. **Kill:** if real ≈
  GUE at every δ (no extra rigidity), the rigidity reading is unsupported by this statistic — record.
- **Cheapest probe (<1h):** δ-neighborhood graph at δ = 1 for the 1000 LMFDB zeros vs GUE-synthetic vs lattice;
  report λ₂ and the top-degree nodes (the "rich club" check N3.3 folds in here).

### N3.3 Rich club / hub detection — NEW (diagnostic; folds into N3.2's probe)
- **Idea:** the rich club is the subgraph of high-degree nodes with denser-than-expected connectivity (van den Heuvel &
  Sporns — *reported standard*). For a random/GUE graph, the top-degree nodes connect at the expected density; a "rich
  club" in the zero graph would be a structural anomaly.
- **Analogy → our setting:** run the rich-club coefficient on the δ-neighborhood zero graph vs GUE null. Expected: no
  enrichment (the zeros are homogeneous). **Kill:** if no enrichment (expected), documented negative; if enrichment
  appears, escalate (a genuine structural anomaly).

### N3.4 Dynamical systems on networks ↔ stability of coupled oscillator networks — KNOWN-OPEN (framing; = N1.1)
- **Idea:** the stability of large coupled oscillator networks is governed by the spectral radius of the coupling
  operator (the master-stability-function framework — *reported standard*) — a line-crossing exactly like the
  certificate's critical value.
- **Verdict:** this is N1.1's content (the Kuramoto critical coupling) restated at the network level. Recorded to
  prevent re-derivation; the only honest fragment is N1.1's soft-mode probe.

---

## Pool 4 — Reservoir computing / echo state networks: spectral radius as a line-crossing

**Core mapping:** a reservoir (random recurrent network) is a feature extractor whose *stability* is certified by the
spectral radius ρ(W) < 1 (the echo state property, ESP — sufficient condition; Jaeger 2001, standard). The reservoir
literature's central lesson: **the spectral-radius condition is sufficient but not necessary** — reservoirs can be
stable with ρ > 1 (Yildiz–Jaeger–Kiebel — *reported standard, verify before use*). That maps 1:1 onto our structure:
the two-moment certificate is a *sufficient* condition reading spectral (intensity) data, and the *gap* between the
sufficient certificate (0.6725), the class-optimal certificate (0.6818), and reality (1, numerically) is the ESP gap.
The second reservoir lesson: **memory capacity is bounded by the number of units** (Jaeger's capacity bound — *reported
standard*) — the same *dimension cap* as Prop 7.4's λN.

### N4.1 The ESP gap ↔ the certificate-optimality gap — NEW (framing)
- **Idea:** the ESP literature spends real effort characterizing *necessary* conditions (in terms of the singular-value
  structure, not the spectral radius) because the sufficient condition misses stable reservoirs. Our analog: the
  two-moment conditions are sufficient-certificate inputs, and the *necessary* structure for on-line-ness is exactly
  what we lack — the off-line worlds that satisfy tr ≈ N ([AS]) are the "stable reservoirs with ρ > 1".
- **Analogy → our setting:** sufficient-but-not-necessary spectral conditions ↔ 0.6725 (sufficient) vs 0.6818
  (class-optimal) vs reality (≈1 measured). Value: a clean vocabulary for why *sufficiency* is all we can certify, and a
  caution against "necessary-condition" searches that would require beyond-1 data.

### N4.2 The dimension cap is a capacity theorem — NEW (framing; cross-ref [B6.2])
- **Idea:** Jaeger's capacity bound (total memory capacity ≤ number of reservoir units) is a *linear* capacity in
  dimension — same shape as Prop 7.4's λN independent measurements. The reservoir literature's *per-unit* capacity
  analysis (which input frequencies are remembered) is the analog of the *per-α* capacity of the certificate.
- **Analogy → our setting:** the per-α value of a unit of bandwidth IS [B6.2]'s per-row shadow-price curve (biology
  catalog: middle rows 64–192 individually most valuable, ~1.5–2·10⁻³ each; beyond-1 rows would be new input). The
  reservoir framing makes Prop 7.4 a capacity theorem and points at [B6.2]'s probe — do not duplicate the probe here.
- **Kill:** n/a (framing + cross-ref).

### N4.3 Effective rank / readout dimension of the certificate — NEW (framing; stops re-derivation)
- **Idea:** reservoirs are read out by a linear layer trained on the reservoir state; the *effective rank* of the state
  covariance bounds what the readout can extract. Our "readout" is the rank–trace inequality reading tr and ‖·‖².
- **Analogy → our setting:** the effective rank R_eff = (tr)²/‖·‖² ≈ 0.75N is a *function of the two moments* (no new
  information), and the thresholded rank of W_T is ≈ N in the real world ([AS]) — so the certificate extracts ~N
  independent measurements and reads *two* scalars from them. The honest content: the "readout" is not information-
  starved at the feature level; the starve is in the *scalar statistics* (the moments), i.e., the wall is in the
  input class, not the compression. This stops "more features" ideas at the framing stage.

### N4.4 ESP contractivity ↔ the rank–trace inequality as a contraction bound — NEW (framing)
- **Idea:** the ESP sufficient condition is a *contraction* condition (the state map is a contraction in a suitable
  norm); the rank–trace inequality rank(W) ≥ 2tr − ‖W‖² is the same *type* of object (a norm-inequality certificate on
  a positive matrix).
- **Analogy → our setting:** both are *sufficiency certificates from spectral data*; neither is necessary. The mapping
  adds no new math but explains the certificate's "repulsion, not RH" character ([AS]) in operator language: the
  certificate certifies *contractivity* of the zero-pairing structure, and contractivity is compatible with off-line
  content at the o(N) level — exactly the paper's C Rem 7.2(iii) "empty certificate" mechanism ([AS] Poisson world).

---

## Pool 5 — Systems medicine / pharmacology: compartment models, identifiability, R₀, tumor growth

**Core mapping:** a k-compartment pharmacokinetic model is a sum of k exponentials whose *eigenvalues are elimination
rate constants* — a spectral ladder; the classical identifiability theory (Prony's method; structural identifiability
of compartment models, Godfrey/Walter–Pronzato — *reported standard, verify before use*) says a k-exponential signal is
determined by 2k moments (2k−1 free parameters). Our moment ladder 2/3 (2 moments) → 5/6 or better (3 moments) → 13/18
(4 moments) → 1 (∞) is *the same identifiability ladder*: two components (marks {1,2}) need three moments — matching
[B3.1]'s mixture-identifiability conclusion from the PK/exponential-sum side. SIR/R₀ is already mined in
[ECO-B4]/E4 — referenced, not duplicated.

### N5.1 Prony / identifiability ladder: two components need three moments; reconstruction from measured moments — NEW (probe run: N-R1; the pool's headline)
- **Idea:** the {1,2}-mark model (marks ∈ {1,2}, Σ marks = N) predicts the *entire* moment sequence from m₂ alone:
  m₃ = 3m₂ − 2, m₄ = 7m₂ − 6 (in the submeasure normalization — the same family the near-CUE law saturates: (1.31817,
  1.9545, 3.2272) satisfies both identities exactly, [AN]). Prony's method (k exponentials from 2k moments, standard)
  is the *reconstruction* side: from measured (m₁, m₂, m₃), fit a free 2-atom measure and predict m₄ — a self-consistency
  check of the two-component model at finite T.
- **Analogy → our setting:** compartment identifiability ↔ which multiplicity structure the measured moments can
  identify; the third moment is the minimal order for a 2-component mixture (same conclusion as [B3.1], now from the
  exponential-sum side); the *measured* finite-T moments are the "decay data" from which the model order is estimated.
- **Needs:** the flat-window Gram moments (m₂, m₃, m₄) at several heights + the identities + a Prony fit. **PROBE DONE
  (N-R1)** — findings: (i) implied p₁ = 2 − m₂ ≈ 0.68–0.70 matches the finite-T certificate range (~0.69–0.72, [AS]
  world (a)) — the {1,2}-mark identity is internally consistent with the certificate at finite T; (ii) m₃ sits on the
  curve (residual r₃ ≈ −0.01…−0.02) but m₄ is *far below* it (r₄ ≈ −0.14…−0.19): the finite-T 4th-moment deficit
  (≈ 10–12%) is ~5× the 2nd-moment deficit (≈ 2.3%) in relative terms — a quantified caution that higher-moment inputs
  (P2) carry larger finite-T error terms; (iii) the free 2-atom Prony fit puts atoms at ≈ 0.4 and ≈ 1.53 (not {1,2}) and
  *under*predicts m₄ — the finite-T spectrum is smeared beyond a pure two-atom law; (iv) measured m₄ ≈ 2.94–3.07 is
  below BOTH 10/3 (mark/Gram) and 13/4 (HL*) — the [AN] 13/4-vs-10/3 provenance question is NOT adjudicated by
  finite-T data (both are far above the measured value).
- **Feasibility:** Low (probe done). **Next (funded):** null calibration — the same identities for a sine/GUE-like
  sample at the same n and Gram convention (does the GUE null also sit off the {1,2}-curve at finite N? expected yes,
  since GUE is not a two-atom law — the *size* of the null deviation calibrates how much of r₄ is finite-N smearing vs
  genuine structure); then the [CD-V4] capacity LP with the corrected moment-error budget.
- **Label:** NEW; TESTED-OPEN (N-R1 run; null calibration outstanding).

### N5.2 Compartment identifiability ↔ the moment-order capacity curve — NEW (framing; cross-ref [CD-V4])
- **Idea:** structural identifiability theory asks *which parameters are identifiable from which measurements*; the
  certificate's question is *which configurations are identifiable from which moments*. The [CD-V4] capacity LP (the
  certified fraction as a function of moment order) IS the identifiability curve of the certificate class.
- **Analogy → our setting:** model order ↔ moment order; identifiable parameters ↔ distinguishable configurations; the
  k = 2 rung (0.6818, PROVEN) and the k = ∞ rung (1, conditional) are the endpoints of the ladder.
- **Kill:** n/a (framing; the LP is the [CD-V4] probe).

### N5.3 SIR / R₀ threshold — KNOWN (referenced; mined in [ECO-B4]/E4)
- **Idea:** R₀ is the spectral radius of the next-generation matrix; epidemic thresholds are *mean-based* and miss tail
  events — the exact shape of our wall.
- **Verdict:** this is [ECO-B4]/E4's content ([ECO-B4] §B4, W-B1 in the ml-eco catalog). Do not duplicate; record the
  cross-ref so the epidemiology pool is not re-mined.

### N5.4 Tumor-growth / Gompertz approach ↔ the finite-T deficit's approach rate — NEW (framing; cross-ref N2.3)
- **Idea:** Gompertz growth approaches its plateau *exponentially* (standard growth modeling). The finite-T deficit
  Δ(T) ≈ c/log T ([AF], [ML-R5]) does NOT approach exponentially — the finite-T correction is *marginally divergent*
  (logarithmic), the signature of a critical/marginal system rather than a saturating one.
- **Analogy → our setting:** the approach-rate classifies the mechanism (log ↔ arithmetic pair correlation, per
  [ML-R6]; exponential ↔ would-be saturation); the honest content: the deficit is NOT "converging fast" — it is
  *logarithmically* persistent, which is why P6's error terms matter at every computable T. Cross-ref N2.3/[W-B1] for
  the universality test.
- **Kill:** n/a (framing + cross-ref).

### N5.5 Hallmarks of cancer as constraints ↔ the moment hierarchy as hallmarks of on-line-ness — KNOWN-OPEN (framing only)
- **Idea:** the hallmarks of cancer are *acquired capabilities* (enabling constraints) that let a tumor grow; the
  certificate's "acquired capabilities" are its *inputs* (moment order, bandwidth) — each new input enables more
  certification, like each hallmark enables more malignancy.
- **Verdict:** pure framing; the honest content is the moment-order capacity curve (N5.2/[CD-V4]). Recorded so the
  metaphor is not re-funded as new.

---

## Pool 6 — Neurodegeneration / brain states: spectral slowing, loss of complexity

**Core mapping:** clinical EEG diagnostics read *spectral shifts* (slowing: power moves to low frequencies in
Alzheimer's — standard) and *complexity loss* (multiscale entropy, DFA — Lipsitz–Goldberger 1992; Costa–Goldberger–Peng
2002 — *reported standard*). Both map to our F̂(α) and the eigenvalue law of W_T: the spectral form factor IS the power
spectrum of the zero process, and the eigenvalue law of W_T is the "EEG" of the certificate. The task hint — "loss of
complexity in aging ↔ our F̂(α) beyond 1?" — is answered head-on below with two code-backed probes.

### N6.1 EEG slowing / band-power ratios ↔ a spectral-ratio diagnostic — NEW (diagnostic; overlaps [P10.2])
- **Idea:** EEG slowing is quantified by band-power ratios (theta/alpha); the analog for the certificate is a
  *spectral-shape ratio* of W_T's eigenvalue law — mass below/above a cutoff (e.g., the median, or the crystal's
  eigenvalues {1,2}).
- **Analogy → our setting:** at *fixed two moments* (tr, ‖·‖²), the eigenvalue law's shape is NOT determined — the
  ratio measures the residual spectral freedom (the P7 "real slack" question). Real vs crystal vs GUE-synthetic: if the
  ratio is identical, the spectrum is moment-determined and the method has no shape slack; if different, reality has
  spectral structure the moments cannot see (motivating a search for a provable shape input).
- **Needs:** W_T spectra ([AF]/[CD-V1]). **Feasibility:** Low. **Kill:** if identical across worlds (expected-ish), a
  documented P7 negative.
- **Cheapest probe (<1h):** mass-ratio below/above the median eigenvalue for real vs crystal vs GUE at T = 200–700.

### N6.2 Multiscale sample entropy of the zero sequence — NEW; PROBE DONE (N-R2, part b) — TESTED (negative)
- **Idea:** multiscale entropy (MSE) coarse-grains a signal by factors τ and recomputes sample entropy at each scale;
  healthy systems show *more* complexity at long scales, and complexity loss (disease/aging) shows up as a *drop* at
  coarse scales (Costa–Goldberger–Peng — *reported standard*).
- **Analogy → our setting:** the "signal" is the normalized gap sequence of the zeros; coarse-graining by τ averages τ
  consecutive gaps (a scale-resolved statistic NOT in [ML-R3]'s single-scale battery). **PROBE DONE (N-R2):** SampEn(τ)
  for τ = 1,2,4,8,16 — real: 2.09, 2.20, 2.04, 2.25, 2.12 (flat, no collapse); GUE bulk: 1.92–2.38 (flat); jittered
  lattice: 1.75–2.49; Poisson: 1.65–2.34. **The real zero sequence shows NO scale-resolved complexity loss — it is
  GUE-consistent at every coarse-graining** (CHECKED NUMERICALLY, `probe_neuro_dfa_mse.py`).
- **Feasibility:** Low (done). **Kill/verdict:** the "loss of complexity" reading of the hint is a documented negative
  — the zeros are as complex as the GUE null at every scale, consistent with [ML-R3]'s single-scale negatives.

### N6.3 Detrended fluctuation analysis (DFA) of the zero gaps — NEW; PROBE DONE (N-R2, part a) — TESTED (finding + artifact)
- **Idea:** the DFA exponent α classifies long-range correlation (α = 0.5 white, 1.0 1/f, < 0.5 anticorrelated;
  periodic → ~0) (Peng 1994 — *reported standard*). The gap sequence of a repulsive point process is anticorrelated
  (long gap → short gap), so α < 0.5; the *strength* of the anticorrelation measures rigidity.
- **Analogy → our setting:** DFA on normalized gaps for four worlds (n = 1500): **bulk real zeros α ≈ 0.02–0.09
  (4 segments) vs GUE bulk α ≈ 0.20–0.22 (3 seeds, robust) vs Poisson 0.53 vs jittered lattice ≈ 0.03** (CHECKED
  NUMERICALLY, `probe_neuro_dfa_mse.py`). **The bulk zero gaps are ~2–6× more anticorrelated than the GUE null —
  scale-resolved evidence the zeros are more rigid than GUE**, corroborating [ML-R1]'s fine-scan (g below GUE for
  u < 0.45) and the sandbox's repulsion reading [AS]. Artifact found: the *low-height* segment (zeros 1–1500, and the
  LMFDB 1–1000 file) gives α ≈ 0.78–0.81 — inflated by the anomalously large first gaps (γ₂−γ₁ ≈ 6.89; the boundary
  effect [ML-R5] already flagged for the lowest band). **Caution:** any gap-statistic analysis using the first ~1000
  zeros must exclude or normalize the boundary, or it reads α ≈ 0.8 spuriously.
- **Feasibility:** Low (done). **Next:** more realizations + a window-parameter sweep (a diagnostic that changes what
  we believe about the P7 slack: the rigidity axis crystal (0.03) < real (0.02–0.09) < GUE (0.20) < Poisson (0.53)
  places reality just off the crystal end — consistent with "the certificate is a repulsion statement").
- **Label:** NEW → TESTED (finding), with the boundary-artifact caution documented.

### N6.4 Loss of complexity ↔ F̂(α) beyond 1 — answered (cross-ref [ML-R3], N-R2, hot-hand JSON)
- **Idea:** the task hint asks whether the beyond-1 form factor is the "loss of complexity" of the zero spectrum.
- **Honest answer (three independent measurements, all CHECKED NUMERICALLY):** (i) the empirical beyond-1 blocks read
  F̂ ≈ 1.0 (plateau, GUE-consistent — `hot_hand_calib_results.json`, block_alpha 1.5/2.0 → 1.00/0.97); (ii) single-scale
  entropy/compressibility: GUE-with-noise, no structure ([ML-R3]); (iii) multiscale entropy (N-R2): flat, no
  complexity loss at any scale. **The zero spectrum shows no "loss of complexity" anywhere — it is uniformly GUE-like,
  i.e., "healthy" on every complexity diagnostic we have.** A complexity drop would have been a real anomaly; its
  absence is a documented negative that closes this hint.
- **Kill:** n/a (answered).

### N6.5 Counting-function variance / index of dispersion — KNOWN (cross-ref [ECO-B1])
- **Idea:** var/mean of zero counts over boxes with the log factor (Selberg CLT) vs the crystal's O(1) variance is the
  fluctuation separator.
- **Verdict:** this is [ECO-B1]'s index-of-dispersion probe (ml-eco catalog). Cross-referenced, not duplicated.

---

## Probe results (code-backed, Round 1) — mandatory-protocol verification

All scripts live in the new self-contained dir `tools/probes_neuro/` (none of the canonical `tools/` scripts were
edited). Commands: `cd tools && uv run --quiet --with numpy python probes_neuro/<script>.py`. Data:
`tools/data/zeros_computed_10000.txt`, `tools/data/zeros_1_1000.txt`. Labels per the mandatory protocol:
PROVEN / CHECKED NUMERICALLY (script + command cited) / CONJECTURED / ABANDONED / INCONCLUSIVE.

### N-R1. {1,2}-mark identifiability curve + Prony fit [N5.1] — `probe_neuro_moments_prony.py`
Flat-window Gram (λ = 1, per-band local rescale, convention of [ML-R5]); m_k = tr(G^k)/n via Frobenius identities
(one matmul per band). Band results (n = 1000/3000/3000/3000, heights h ≈ 14–1420 / 1420–5800 / 5800–10800 /
10800–17000):

| band | m2 | m3 | m4 | r3 = m3−(3m2−2) | r4 = m4−(7m2−6) | p1 = 2−m2 |
|---|---|---|---|---|---|---|
| 0–1000 | 1.3215 | 1.9407 | 3.0656 | −0.0239 | −0.1852 | 0.6785 |
| 1000–4000 | 1.2986 | 1.8816 | 2.9358 | −0.0142 | −0.1546 | 0.7014 |
| 4000–7000 | 1.3002 | 1.8882 | 2.9527 | −0.0124 | −0.1488 | 0.6998 |
| 7000–10000 | 1.3027 | 1.8970 | 2.9760 | −0.0111 | −0.1430 | 0.6973 |

- **Implied simple fraction p₁ = 2 − m₂ ≈ 0.68–0.70 matches the finite-T certificate range (~0.69–0.72, [AS] world
  (a))** — the {1,2}-mark identity is internally consistent with the certificate at finite T (CHECKED NUMERICALLY).
- **m₃ is on the {1,2}-curve (r₃ ≈ −0.01…−0.02); m₄ is far below it (r₄ ≈ −0.14…−0.19).** Relative deficits vs the
  GUE limits: m₂ ≈ 2.3%, m₃ ≈ 5–6%, m₄ ≈ 10–12% — **the finite-T moment deficit grows roughly linearly in moment
  order**, a quantified caution for P2 (higher-moment inputs carry larger finite-T error terms).
- **Free 2-atom Prony fit** (from m₁, m₂, m₃): atoms ≈ 0.40 and ≈ 1.53 with weight ≈ 0.52 — NOT near {1,2}; predicted
  m₄ ≈ 2.82–2.94 *below* measured (2.94–3.07). The finite-T spectrum is smeared beyond a pure two-atom law (neither
  the {1,2}-model nor the free 2-atom fit explains m₄).
- **m₄ measured ≈ 2.94–3.07 is below BOTH 10/3 (mark/Gram) and 13/4 (HL*)** — the [AN] 13/4-vs-10/3 provenance
  question is NOT adjudicated by finite-T data (both values are far above the measurement).
- **Honest caveats:** the Gram moments are the finite-T (finite-N) estimators with known bias structure; no
  GUE-null calibration at the same n and convention is in this probe (the null would quantify how much of r₄ is
  finite-N smearing — listed as the funded next step); band 1 (lowest height) carries the boundary effect [ML-R5].
- **LABEL: CHECKED NUMERICALLY (all numbers above); N5.1 upgraded from "promising" to "funded on measured
  evidence".**

### N-R2. DFA exponent + multiscale sample entropy [N6.2, N6.3] — `probe_neuro_dfa_mse.py`
Worlds at n = 1500 (real = zeros 3000–4500; GUE bulk = middle eigenvalues of a β=2 Dumitriu–Edelman tridiagonal,
rescaled to mean spacing 1; jittered lattice = crystal proxy; Poisson). DFA on normalized gaps, scales 8–375;
SampEn(m = 2, r = 0.2·std) at τ = 1,2,4,8,16.

- **DFA α:** real 0.034; GUE bulk 0.191; jittered lattice 0.026; Poisson 0.532. Robustness: real bulk segments
  0.0217/0.0279/0.0524/0.0859 (segs 8000/4000/2000/6000); GUE seeds 0.201/0.218/0.211; **low-height segment (zeros
  1–1500) and the LMFDB 1–1000 file read α ≈ 0.78–0.81 — a boundary artifact from the anomalously large first gaps
  (γ₂−γ₁ ≈ 6.89), the [ML-R5] lowest-band effect.**
- **SampEn(τ):** real 2.04–2.25 (flat); GUE 1.92–2.38 (flat); lattice 1.75–2.49; Poisson 1.65–2.34. **No
  scale-resolved complexity loss anywhere.**
- **Reading:** (a) the bulk zero gaps are ~2–6× more anticorrelated than the GUE null — scale-resolved evidence of
  extra rigidity (corroborates [ML-R1] fine-scan, [AS] repulsion reading); (b) the zeros show no complexity loss at
  any scale (closes the "loss of complexity" hint); (c) the low-height boundary artifact is a caution for anyone using
  the first ~1000 zeros for gap statistics.
- **LABEL: CHECKED NUMERICALLY (finite data, diagnostics — single realization per world, n = 1500, fixed DFA/SampEn
  parameters; not theorems).**

---

## TOP 10 (EV × feasibility × cheap-probe)

1. **N5.1 — Prony / {1,2}-mark identifiability (PROBE DONE, N-R1):** implied p₁ ≈ 0.70 matches the finite-T
   certificate; m₄ deviates ~5× (relative) more than m₂ — a quantified finite-T caution for P2, and the [AN]
   13/4-vs-10/3 question is not adjudicated. Next: GUE-null calibration at the same n/convention (<1h), then the
   [CD-V4] capacity LP with the corrected moment-error budget. Low.
2. **N6.3 — DFA rigidity of the bulk zeros (PROBE DONE, N-R2):** real α ≈ 0.02–0.09 < GUE 0.20–0.22 — the zeros are
   more rigid than GUE at DFA scales 8–375; the low-height boundary artifact (α ≈ 0.8) is a documented trap. Next:
   realization/window sweep — a P7 slack diagnostic. Low.
3. **N6.2 — Multiscale entropy (PROBE DONE, N-R2):** no complexity loss at any scale — the "loss of complexity" hint
   is closed as a documented negative. Low (done).
4. **N3.2 — Fiedler value / algebraic-connectivity rigidity ladder** (δ-neighborhood zero graph vs lattice/GUE/
   Poisson; degree distribution = rich-club check folds in). A new, cheap rigidity measurement pricing P1.4 from the
   data side. Probe: δ = 1 graph on the LMFDB zeros — <1h.
5. **N1.1 — Kuramoto soft-mode edge scaling** (refines [P1.3]/[CD-V1] with the finite-N criticality prediction for the
   near-zero eigenvalue density of W_T). Probe: edge histogram at T = 200–700 — <1h.
6. **N6.1 — Spectral band-ratio** (mass below/above the median eigenvalue of W_T: does reality have spectral shape
   slack at fixed two moments? — a P7 probe). Probe: [AF]/[CD-V1] spectra — <1h.
7. **N2.2 — Cluster-size distribution at ε-neighborhoods** (the avalanche observable that [ML-R3] did not test;
   overlaps [B1.4]'s decoy screen). Probe: connected components at ε ∈ {0.5, 1, 2} — <1h.
8. **N2.3 — Deficit-amplitude universality prediction** (from [ML-R6]'s u<1 attribution: smoothing the window should
   NOT change c ≈ 0.288 — a quantitative prediction for [W-B1]'s window-sweep). Probe: [W-B1]'s, cross-ref — <1h.
9. **N1.2 — The β-f "Arnold tongue" of the certificate** (re-plot of [AS]'s crossing table as a curve — the exact
   depth of off-line structure a future repulsion input must exclude). One line — minutes.
10. **N4.2 — The dimension cap as a capacity theorem** (Prop 7.4 ↔ Jaeger's memory-capacity bound; the per-α capacity
    is [B6.2]'s per-row shadow-price curve — cross-ref, don't duplicate). Framing that stops re-derivation.

**Strategic reading:** neuroscience + systems medicine produced exactly **one proven-input-adjacent vector with
code-backed evidence** (N5.1, probe N-R1: the {1,2}-mark identifiability curve holds at finite T through m₃ and fails
at m₄, with the implied p₁ matching the finite-T certificate — and a quantified 4th-moment deficit that P2 must price),
**two new diagnostics with code-backed findings** (N-R2: DFA rigidity of the bulk zeros, and the flat multiscale
entropy), and a cluster of cheap P7-slack probes (N3.2, N6.1, N2.2, N1.1) plus framings that stop re-derivation (N1.5,
N2.3, N2.4, N4.1–N4.4, N5.2–N5.5, N6.4, N6.5). The pool independently re-derives the known walls through *synchrony
order parameters* (intensity-only, cannot see phase — [P6.4]), *criticality* (two moments generically insufficient at
criticality), *reservoir stability* (sufficient-not-necessary spectral conditions), *identifiability* (2 components
need 3 moments — [B3.1] from the PK side), and *complexity diagnostics* (the zero spectrum is uniformly GUE-like —
"healthy"). The persistent wall — beyond-1 F, third moments, repulsion — is unchanged, and this pool's honest
contribution is: (i) the m₄ finite-T deficit measurement (new, code-backed, relevant to P2's error budget), (ii) the
DFA rigidity finding (new scale-resolved repulsion diagnostic), and (iii) the confirmation that the empirical beyond-1
F̂ ≈ 1 plateau and the flat complexity profile are consistent with the pair-correlation-conjecture world at every
statistic we can measure.

---

## WILD section (deliberately absurd premises; honestly evaluated; each labeled)

### W-N1. "The zeros are a critical brain: RH ⟺ the zero process sits at a phase transition; the certificate is the mean-field order parameter" — CONJECTURED (framing; the falsifiable fragment is [W-B1]'s window-sweep)
**For:** the log-variance of counts (Selberg CLT, unconditional [CD-V13]), the logarithmic deficit (~1/log T, [AF],
[ML-R5]), and the shadow price of p₁ = exactly 1 ([ALP]) — which in order-parameter language is a *divergent
susceptibility* (marginal at criticality). The sandbox's two horns ("≈2/3 in an RH-true world", "not structurally
capped") are both compatible with a mean-field description at a critical point — a nice unification.
**Against:** the gap statistics are Wigner, not power-law ([ML-R3]); "criticality" is an analogy; no new inequality
appears. **Novel fragment worth keeping:** the susceptibility reading of the shadow price (p₁'s marginal = 1 ↔
critical) is a real observation about the LP structure, and the universality test of the deficit amplitude
([W-B1]/N2.3) is the falsifiable consequence.

### W-N2. "The connectome of the zeros has a rich club: a small set of grid positions carries most of the pair correlation" — CONJECTURED (likely false; probe = N3.2's degree distribution)
**For:** if the beyond-1 form-factor structure were concentrated on a few "hub" separations, a *sparsity* input
(bounding the off-line pair count) could enter the certificate — the only documented form of repulsion input that
matters ([ML-R4]: clustering gives nothing; only a pair-*count* bound helps).
**Against:** every statistic we measured says the zeros are homogeneous (no hubs, no periodicity, GUE-with-noise);
the rich-club coefficient of the zero graph is expected ≈ null. **Honest verdict:** run the degree distribution once
inside N3.2's probe; expected flat.

### W-N3. "Reservoir computing IS the method: primes are the input, the zeros are the reservoir state, the readout layer is trained by RH" — CONJECTURED (renaming; honest content = N4.2/N4.3)
**For:** the reservoir's spectral-radius stability condition ↔ the certificate's critical value; the readout (a linear
layer) ↔ the rank–trace inequality; the capacity bound ↔ the dimension cap. The renaming is faithful.
**Against:** "training the readout" = solving the LP, which is closed in-class ([ALP]/[CIG]); no new input emerges;
the ESP-sufficient-not-necessary lesson (N4.1) is the only transferable fragment, and it restates the wall. **Honest
verdict:** keep the vocabulary for N4.1–N4.4; do not fund as a new route.

### W-N4. "Alzheimer's of the certificate: the zeros lose complexity as T grows — RH is the healthy brain, and the finite-T deficit is the spectral slowing" — CONJECTURED (falsifiable fragment = N6.3's DFA-vs-height drift)
**For:** if the zero sequence's complexity *drifted* with height (DFA α moving toward the crystal value 0.03 as h
grows), that would be a real, measurable "progression" — a new diagnostic direction.
**Against:** the measured bulk DFA α is already ≈ 0.03 (crystal-near) at every bulk height, and the *low-height* value
(0.8) is a boundary artifact, not a drift — the first data point is against any complexity-loss-with-height reading.
**Novel fragment worth keeping:** run DFA on several non-overlapping bulk segments *as a function of height* (one
small extension of N-R2) — if α is height-independent, the "progression" reading is dead (expected); if it drifts, an
escalation.

---

## Label inventory

- **NEW** (invented here; probes run where marked): N1.1, N1.2, N1.3, N1.4, N2.1, N2.2, N2.4, N3.1, N3.2, N3.3, N4.1,
  N4.2, N4.3, N4.4, N5.1 (TESTED-OPEN via N-R1), N5.2, N5.4, N5.5, N6.1, N6.2 (TESTED via N-R2, negative), N6.3
  (TESTED via N-R2, finding + artifact), N6.4 (answered), W-N1…W-N4 (framing, conjectured by construction).
- **KNOWN-DEAD / REFUTED (as new; documented to prevent re-derivation):** N1.5 (= [ML-M1.1]/[ML-R5], probe done), N2.1's
  power-law reading (gaps are Wigner, [ML-R3]), N5.3 (SIR = [ECO-B4]/E4), N6.5 (= [ECO-B1]).
- **KNOWN-OPEN** (route already flagged in our notes; new fragment only): N2.3 (deficit-amplitude universality, cross-ref
  [W-B1]), N3.4 (= N1.1), N5.5 (framing), and the persistent inputs: beyond-1 F (P3), third moment (P2), repulsion
  (P1.4) — unchanged by this pool.
- **TESTED-OPEN** (code-backed, this note): N5.1's probe N-R1 (implied p₁ = 2 − m₂ ≈ 0.70 matches the finite-T
  certificate; r₃ ≈ −0.01…−0.02; r₄ ≈ −0.14…−0.19; m₄ ≈ 2.94–3.07 below both 10/3 and 13/4; free 2-atom fit at
  0.40/1.53), N6.2's probe N-R2b (multiscale entropy flat: 2.04–2.25 vs GUE 1.92–2.38), N6.3's probe N-R2a (bulk DFA
  α 0.02–0.09 vs GUE 0.20–0.22; low-height boundary artifact α ≈ 0.78–0.81).
- **Reported-standard domain facts (verify before use):** Kuramoto order parameter and critical coupling; Strogatz–
  Mirollo incoherent-state stability; finite-N Kuramoto N^{−2/3}/N^{−1/3} scalings; Arnold tongues; common-input
  correlated spiking; Beggs–Plenz avalanches and branching ratio; Chialvo critical-brain hypothesis; connectome
  harmonics (Atasoy); rich club (van den Heuvel–Sporns); Fiedler algebraic connectivity; echo state property
  (Jaeger 2001) and its sufficient-not-necessary status (Yildiz–Jaeger–Kiebel); Jaeger's memory-capacity bound; Prony's
  method; compartment-model structural identifiability (Godfrey; Walter–Pronzato); Gompertz growth; EEG slowing in
  Alzheimer's; loss-of-complexity hypothesis (Lipsitz–Goldberger); multiscale entropy (Costa–Goldberger–Peng); DFA
  (Peng); Dumitriu–Edelman tridiagonal GUE representation.

**Honest closing note:** the neuroscience + systems-medicine angle's strongest NEW contributions are (i) **N5.1 with
probe N-R1** — the {1,2}-mark identifiability curve holds at finite T through m₃ (implied p₁ ≈ 0.70 = the finite-T
certificate) and fails at m₄, with the finite-T moment deficit growing roughly linearly in order (≈ 2.3% / 5–6% /
10–12% at m₂/m₃/m₄) — a quantified, code-backed caution for P2's error budget; (ii) **N6.3 with probe N-R2** — the
bulk zero gaps are ~2–6× more anticorrelated than the GUE null (scale-resolved rigidity, corroborating [ML-R1] and
[AS]), with a documented low-height boundary artifact (first ~1000 zeros give spurious α ≈ 0.8); and (iii) the
head-on answer to the "loss of complexity ↔ F̂ beyond 1" hint: the zero spectrum is uniformly GUE-like (flat
multiscale entropy, F̂ ≈ 1 plateau beyond 1) — no complexity loss anywhere, a documented negative. The persistent wall
is unchanged, but this pool adds one quantified input-price (the m₄ error), one new rigidity diagnostic, and one
closed question — and its many framings independently re-derive the known walls through *synchrony*, *criticality*,
*reservoir stability*, *identifiability*, and *complexity* vocabularies, which is itself evidence the walls are
structural.
