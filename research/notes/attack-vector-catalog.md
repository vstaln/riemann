# Attack Vector Catalog — Round 2 (SYNTHESIZER output)

**Agent:** SYNTHESIZER (decision-criteria-weighting + strategy + resource-allocation + epistemology).
**Round:** 1 → 2 handoff. **Date:** 2026-08-11.
**Inputs merged (all in `research/notes/`):** idea-generator-crossdomain.md, idea-generator-literature.md,
attack-kernel.md, attack-ceiling.md, attack-multiplicity.md, attack-mollifier.md, attack-lfunctions.md,
attack-finitet.md, literature-map.md, verification-001.md, round-1-brief.md.
**Method applied (s4h):** decision-criteria-weighting (explicit weights, scores before totals, sense-check),
strategy (terrain / force-economy / kill criteria), resource-allocation (explicit trade-offs),
epistemology (every claim labeled; provenance traced).
**Honesty protocol:** every factual statement about what is PROVEN / DEAD / OPEN carries its source file in
brackets, e.g. `[ceiling §4]` = attack-ceiling.md §4. Nothing below re-derives a result; this is synthesis,
merge, scoring, and ranking only. All scores are JUDGMENT (CONJECTURED), not facts.

---

## 0. The honest map after Round 1 (what is settled, and what the search space actually is)

**PROVEN (Lean, modulo one numerically-checked enclosure) — the hard walls:**
1. **0.67250… is the ceiling of the window choice for ζ's functional.** The cosine
   `cos(√2u)` is the *global* minimizer of the Rayleigh quotient Q(v) (Euler–Lagrange v″+2v=0 + I+T ≻ 0
   convexity, no evenness imposed; numerically confirmed to ~7·10⁻⁹ on a free 4001-point grid). Every
   candidate that numerically beats it (support c > 1/2, λ > 1) violates the bandwidth condition that
   Claim 2.1's Poisson completion requires — those are CONJECTURED DEAD ENDS, not improvements
   `[kernel §2, §3, §5]`. The ξ′-quartic is a lever for ξ′'s *different* functional, **not** for ζ
   (PROVEN NO transfer) `[kernel §4]`.
2. **0.6818… is the bandwidth-one ceiling of the whole certificate class.** No certificate reading
   (mean density, form factor on [0,1], integrality) can certify more than 0.68182868746… simple zeros:
   the 256-periodic near-CUE law realizes the bound and is not ruled out by pair correlation
   `[ceiling §1, §3]`; Lean `Zeta23/PairCeiling`, `ceiling_law256`, `ceiling_stability`; the one
   non-Lean link is `EnclOK` (70-digit interval enclosure of the law's S(j)) — CHECKED NUMERICALLY
   `[ceiling §1]`.
3. **The two-moment rank–trace method prices multiplicity integrality optimally.** 2/3 simple and 5/6
   distinct are LP-optimal constants of the bookkeeping, the inequality is provably tight
   (`lemmaR_tight`), and the empirically-true all-simple world has **zero slack** (Δ = 0): reality sits
   on the wall `[multiplicity §0, §2, §4]`.
4. **No proven sliver of form-factor information for |α| > 1 exists — unconditional or under RH** — in
   any verified source. Everything beyond α = 1 is Hardy–Littlewood / Montgomery-conjecture territory
   `[ceiling §3]`; the paper's own quantification: 0.70/0.80/0.90 would need supports ≈ 1.04/1.26/1.70
   (C Remark 1.1, as reported in `[litmap §4b3]`).
5. **Individual GL(2) transport is provably empty**: a fixed form's zeros are twice as dense (Λ* = 1/2),
   and the certificate is non-positive for λ ≤ 1/2 by the dimension ceiling (C Prop 7.4) — a hard wall
   independent of all analytic inputs; even pair correlation does not move it `[lfunctions §4, §5]`.
6. **Mollifier fusion has no lever**: both methods share the same off-diagonal prime-pair wall; the only
   documented fusion point (CGG98 integrality m² ≥ 3m−2) is already inside the paper (C §7.5(c))
   `[mollifier §5, §6]`.

**PROVEN DEAD (round-1 documented deaths, idea-stage and structural):** A1–A5 `[crossdomain §5]`;
beat-0.6818-by-same-class `[ceiling §4]`; better-window-for-ζ `[kernel §5]`; mollifier-as-lever
`[mollifier §6]`; fund-multiplicity-data `[multiplicity §4]`; individual-GL(2) `[lfunctions §5]`.
Each is recorded in §4 below with its source so round 2 does not re-derive the death.

**TESTED-OPEN (numerically probed, conclusion not final):**
- Finite-T W_T checks: tr W/N → 1, ‖W‖²_HS/N → 1.3275 from below, Δ(T) = bound/N − 0.6725 **positive and
  decaying ~1/log T**; rank = N; synthetic off-line pair has signature (1,1) with n₊ = n₋ = 1; Claim 2.1
  holds with O(1/K) truncation error for the hard-cutoff ψ `[finitet §3–§5]`.
- Empirical form factor F(α): trend only — climbs to ≈ 0.93–1.0 near α = 1, decays beyond; sample noise
  large at N = 3000 `[verif-001 §4]`.
- Guinand–Weil identity, Lemma 3.4 rank–trace (5000/5000 trials), Montgomery–Vaughan (200/200),
  RvM counts vs LMFDB index.db, headline constant to 15 digits: all PASS `[verif-001 §1–§7]`.

**Therefore the round-2 search space is exactly:**
(a) the in-class gap **0.6725 → 0.6818** (proven inputs only — a better *certificate*, not a better
window) `[kernel §5, ceiling §4 keep-alive]`;
(b) **new targets**: ξ′, ξ″, … (constants PROVEN for ξ′; extension mechanical) `[kernel §4, litmap §4c9]`;
Dirichlet families (CONJECTURED in C Rem 7.2(iii)) `[lfunctions §6]`; Selberg-class statement (mechanical)
`[crossdomain V19]`;
(c) **diagnostics that change what we believe**: Weil-form spectrum experiment, method sandbox,
F≡1 support curve, empirical form factor `[crossdomain §0, §6]`;
(d) **pricing the conjectural inputs** (moment-order capacity) so a later round attacks the cheapest
conjecture `[crossdomain V4]`;
(e) **adversarial hardening** of the ceiling's only non-Lean link (EnclOK) `[ceiling §4 keep-alive 2]`.

---

## 1. Decision and criteria (s4h-decision-criteria-weighting, applied without interactive prompts)

**Decision:** which merged attack vectors to fund / sequence in round 2, given scarce compute and the
round-1 wall structure.

**Criteria (independent, observable, decision-relevant) and weights (total 100):**

| Criterion | Weight | Why |
|---|---|---|
| Expected value (EV) | 45 | Directly moves a constant, opens a target, or produces a publishable result |
| Feasibility | 25 | Likelihood of success on proven inputs on hand; small step vs research program |
| Epistemic value | 20 | Changes what we believe *even on a clean negative* (diagnostics, adversarial checks) |
| Compute cost (inverted: 5 = cheap) | 10 | Respects the machine's scarce CPU; Rust/cache discipline |

Scoring scale: 1 (none/poor) … 5 (high/cheap). Compute: 5 ≈ writeup/static analysis only; 4 ≈ small
script or existing code; 3 ≈ extend an existing Rust crate / small LP; 2 ≈ new computation at scale
(10⁴–10⁵ zeros, SDP); 1 ≈ multi-month research program.

---

## 2. Merged vector table (all round-1 candidates, de-duplicated)

**Status codes:** FUNDED-NEXT = named as the most promising next step in a round-1 executioner file;
NEW = proposed, not yet executed; TESTED-OPEN = numerically probed, not concluded; PROVEN DEAD = death
documented with source (§4). **Weighted = 45·EV + 25·Feas + 20·Epis + 10·Comp.** Every score is
CONJECTURED (synthesizer judgment).

| # | Merged vector | Origin(s) | Status | EV | Feas | Epis | Comp | Weighted | One-line justification |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **V2 — In-class certificate LP dual** (0.6725→0.6818) | crossdomain V2; kernel §5; ceiling §4 keep-alive 1 | FUNDED-NEXT | 5 | 4 | 5 | 4 | **465** | Only proven-inputs path to a real constant gain, plus an adversarial re-verification of the ceiling |
| 2 | **V3 — Unconditional third moment tr Â³** (distinct + off-line-plane certificates) | crossdomain V3; multiplicity §4; literature Hej94/RS96 | FUNDED-NEXT | 5 | 3 | 4 | 3 | **410** | Bypasses the two-moment wall; λ<2/3 diagonal evaluation is available; clean negative also settles the question |
| 3 | **L1 — Groskin finite Guinand–Weil dictionary → second trace identity** | literature top-1 (2607.02828) | FUNDED-NEXT | 4 | 4 | 4 | 3 | **390** | Independent prime-side recomputation of tr/‖·‖² cross-checks the Montgomery–Vaughan step; cheap, adversarial-validatable |
| 4 | **V7 — Method sandbox** (RH-true / RH-false worlds) | crossdomain V7 | NEW | 4 | 3 | 5 | 3 | **385** | Answers the strategic question: is the method or the arithmetic the bottleneck? |
| 5 | **V4 — Moment-order capacity LP** (price of each conjectural input) | crossdomain V4 | NEW | 4 | 3 | 4 | 3 | **365** | Turns the conditional roadmap (HL* → 13/18 → 1) into a curve; tells us which conjecture is cheapest to attack |
| 5 | **L4 — CvS truncated Weil form + Sylvester inertia** | literature (2605.20224, 2602.04022) | NEW | 4 | 3 | 4 | 3 | **365** | Nobody has run an inertia/rank count on the CvS matrices; ground-state-on-line may make the on-line part provably full-rank |
| 5 | **V12 — Dirichlet-family program** (family-averaged 2/3) | crossdomain V12; lfunctions §6 | FUNDED-NEXT (probe) | 5 | 2 | 3 | 3 | **365** | Highest prize (new theorem, C Rem 7.2(iii) unclaimed; GL(2) weight aspect beyond); cheap numerical probe runs first |
| 8 | **V5 — F≡1 support curve** (reproduce 1.04/1.26/1.70) | crossdomain V5 | NEW | 3 | 4 | 4 | 4 | **355** | Validates the roadmap; if the curve disagrees with C Rem 1.1 that is a finding; low effort |
| 9 | **V19 — Selberg-class unification theorem** | crossdomain V19 | NEW | 3 | 4 | 3 | 5 | **345** | Guaranteed deliverable: ζ + Dirichlet as corollaries of one axiomatic degree-1 theorem; GL(2) death as class-level statement |
| 9 | **V1 — Weil-form spectrum experiment** (+ C∞ ramp, eigenvalue law, Hankel margin, F(α) empirics) | crossdomain V1/W2/W3/W5/V6; finitet §7 | TESTED-OPEN | 3 | 4 | 4 | 3 | **345** | Measures the method's real slack and the error terms; the C∞-ramp run changes what we believe about the o(1) |
| 9 | **V9 — Derivative tower ξ″, ξ‴** (+ FGL transport) | crossdomain V9; literature FGL | NEW | 4 | 3 | 3 | 3 | **345** | Mechanical extension; FGL's pattern (constants increase with j) suggests new targets with proven machinery |
| 12 | **M28 — EnclOK adversarial re-check** | ceiling §4 keep-alive 2 | FUNDED-NEXT | 2 | 4 | 5 | 4 | **330** | The one live way the ceiling could be wrong; cheap hash-comparison hardens the only non-Lean assumption |
| 13 | **M29 — Beyond-bandwidth-1 probe** (λ=1.04 prime-pair sum; GLSS push) | mollifier §6; literature GLSS25/GM87; ceiling §4 FUND list | FUNDED-NEXT | 3 | 2 | 5 | 4 | **325** | Settles "is there any proven sliver of F beyond 1"; expected negative, but the check itself is the lasting diagnosis |
| 14 | **L2 — Screw-function formulation of the Weil form** | literature (Suzuki 2606.09096, 2206.03682) | NEW | 4 | 2 | 3 | 3 | **320** | Independent derivation of the constant from screw-function regularity; possibly cleaner error terms (feeds V20) |
| 14 | **L8 — Two-form argument (CGG ζ′(ρ) moments + Weil form)** | literature (BHB 1302.5018) | NEW | 4 | 2 | 3 | 3 | **320** | Genuinely unexplored combination; a joint constraint on the same zero set would be new |
| 16 | V17 — DPP rigidity/repulsion input inventory | crossdomain V17 | NEW | 2 | 4 | 4 | 5 | 320 | Definitive inventory of what a certificate could read; if anything proven usable exists the ceiling breaks (expected: none) |
| 17 | V10 — Density + thin-box composition + shallow/deep diagnosis | crossdomain V10 | NEW | 2 | 4 | 4 | 4 | 310 | Likely negative constant, cheap; lasting output is the "shallow off-line pairs are the irreducible unknown" framing |
| 18 | V8 — ξ′ window optimization (quartic is ad hoc) | crossdomain V8; kernel §4 | NEW | 3 | 3 | 3 | 3 | 300 | May push 0.86864 higher; even "quartic is optimal" is a new proven statement |
| 18 | V20 — Effective finite-T version of 67.25% | crossdomain V20 | NEW | 3 | 3 | 3 | 3 | 300 | Explicit E(T) companion to the Lean ε-statements; may be vacuous at feasible T (documentation-only outcome) |
| 18 | L7 — Box-width knob + short-mollifier variational kernel | literature (B25 b-param; CFKLB 2508.11108) | NEW | 3 | 3 | 3 | 3 | 300 | The b-parameter is a genuine knob; j_M kernel formula must first be re-derived (B25 extraction is garbled `[litmap §5]`) |
| 21 | L3 — de Branges-space structure of the Weil completion | literature (Suzuki 2301.00421) | NEW | 3 | 2 | 3 | 4 | 285 | Spectral/embedding theorems to bound the rank of the negative part — speculative, needs de Branges mastery |
| 22 | L9 — P&P "subset + log-moment" decomposition | literature (1805.07741, method only) | NEW | 3 | 2 | 3 | 3 | 275 | Fresh structural move with no analog in the Weil-form line; P&P's own claim is flagged unverified |
| 23 | V6 — Empirical form factor beyond 1 (full run) | crossdomain V6; verif-001 §4 | TESTED-OPEN | 2 | 4 | 3 | 2 | 270 | Mostly confirms conjecture (F≈1); full run folded into V1's data pipeline |
| 24 | V13 — Selberg-CLT / distributional certificate | crossdomain V13 | NEW | 2 | 3 | 3 | 4 | 265 | Variance is fixed by small-α data the law already matches; no mechanism to enter a per-T certificate |
| 25 | V18 — Multi-window Gabor compressions | crossdomain V18 | NEW | 1 | 4 | 2 | 4 | 225 | Extremal configuration re-normalizes; ratio likely unchanged — cheap to confirm |
| 26 | V11 — Unconditional CGdL20-style SDP | crossdomain V11; literature CGdL20 | NEW | 2 | 2 | 3 | 2 | 220 | B24 error terms (1/√log T at constant scale) likely force value back to ≤0.6725; quantifies the "different regime" claim |
| 27 | V15 — Sierra / Berry–Keating finite spectral check (+W1) | crossdomain V15/W1 | NEW | 1 | 3 | 2 | 4 | 200 | No accepted self-adjoint realization; expected non-real eigenvalues or Weyl-law-only agreement |
| 27 | V16 — Finite Hermite–Biehler shadow (+W4) | crossdomain V16/W4 | NEW | 1 | 3 | 2 | 4 | 200 | Reformulation likely ≅ the paper's method renamed; W4's Connes check indistinguishable from signature computations |
| 29 | V14 — Bethe-ansatz equations (LeClair–Mussardo) | crossdomain V14 | NEW | 1 | 3 | 2 | 3 | 190 | Heuristic system; expected failure beyond ~50 zeros; no route to a certificate |
| — | A1–A5 (see §4) | crossdomain §5 | PROVEN DEAD | — | — | — | — | — | Deaths documented with reasons; do not re-derive |

**Sense-check (skill step):** the ranking matches intuition at the top (V2 = the only proven-inputs constant
path; V3 = the wall-bypass; L1 = cheap immediate cross-check; V7 = strategic bottleneck question). The
model's biggest surprises vs raw intuition are (i) V12 at #7 despite feasibility 2 — justified: highest EV
and its cheap probe should run regardless; (ii) V19 and V17 ranking on cheapness — defensible as
guaranteed deliverables / documentation that run in paper-hunting downtime, and flagged as such in the
strategic reading (§5). Nothing in the model's order contradicts the executioner verdicts; where the
weighted total disagrees with intuition the briefs state the caveat.

---

## 3. TOP 15 for Round 2 — ready-to-paste briefs

Each brief: **goal / why it matters (which constant or gap it moves) / inputs needed / method to try /
honesty labels / definition of done.** Labels: PROVEN = in a source or Lean (source cited); CHECKED
NUMERICALLY = verified in round 1; CONJECTURED = hypothesis; ABANDONED = dead (source cited).

---

### #1. V2 — In-class certificate LP dual: close 0.6725 → 0.6818
- **Goal:** find the certificate that realizes (or provably fails to realize) the bandwidth-one ceiling.
- **Why it matters:** the only remaining in-class gap for ζ (PROVEN window-optimal at 0.6725 `[kernel §5]`;
  ceiling 0.6818 PROVEN in Lean `[ceiling §1]`); also an adversarial re-verification of the ceiling
  itself — if any certificate beats 0.6818 + slack against the 256-law, `ceiling_law256` is refuted
  `[ceiling §4 keep-alive 1]`.
- **Inputs needed:** `Zeta23/PairCeiling/{LawN256,CeilingLaw256,Stability,Ceiling,NearCUE}.lean`;
  the exact-rational 256-law (certificate sha256 `cc3de991…` `[ceiling §1]`); a small Rust LP solver
  (to write, ~1 day); attack-ceiling.md §1's stability inequality as the constraint.
- **Method:** the extremal law is the optimum of an exact-rational LP over marked configurations; by LP
  duality its dual is a certificate (c₀, r) with r ∈ C¹[0,1]. Discretize, solve the dual, read off the
  value, verify the certificate exactly (rational/polynomial), then Lean-verify like the paper's own
  certificates.
- **Labels:** ceiling PROVEN (Lean) modulo `EnclOK` CHECKED NUMERICALLY `[ceiling §1]`; the claim "Theorem
  D's certificate is not class-optimal" is CONJECTURED; the LP-dual method is CONJECTURED.
- **Definition of done:** (a) dual optimum ≈ 0.6818 + slack → new certificate → Lean-checked → real
  constant gain + ceiling independently re-verified; (b) dual optimum = 0.6725 exactly → Theorem D is
  class-optimal → documented finding (0.6818 unreachable by smooth certificates); (c) either way, the
  in-class question is closed.

### #2. V3 — Unconditional third moment tr Â³ (distinct-count and off-line-plane certificates)
- **Goal:** feed tr Â³ into the N_d bookkeeping and the hyperbolic-plane count; test whether the two-moment
  walls 5/6 (distinct) and the off-line bound move.
- **Why it matters:** the two-moment method is PROVEN tight and the empirical world has zero slack
  `[multiplicity §0, §4]`; the only documented levers are higher moments or structural exclusion
  `[multiplicity §4]`. The paper's §7.5(e) "odd moments don't lower Λ₁(0)" is about the n₊ functional;
  the distinct functional is different `[crossdomain V3]`. Hejhal 1994 / Rudnick–Sarnak give the
  conditional (RH) triple correlation `[litmap §4b6]`; the diagonal evaluation is available in the
  Rudnick–Sarnak range kλ < 2, i.e. λ < 2/3 for k = 3 `[ceiling §3.4, multiplicity §4]`.
- **Inputs needed:** C §7.5(d,e) (Christoffel bound 1 − Λ_m(0); k_c(m) penalties at higher order);
  `Zeta23/ZeroSide/{RankTraceMult,Mult,TightMult}.lean`; the triple-correlation value (sine-kernel m₃ = 2,
  Hejhal/RS96 — CONJECTURED as an *unconditional* input at λ < 2/3 by the diagonal method); the
  (tr, ‖·‖², tr Â³, integrality, n₊) LP (Rust, small); zeros data `tools/data/zeros_1_1000.txt`.
- **Method:** write down the third-moment evaluation at λ = 2/3·(1−ε) (diagonal computation à la
  Hejhal/Rudnick–Sarnak), assemble the LP for N_d (c = 3 route) and for the hyperbolic-plane count, solve,
  check whether 5/6 (and the off-line bound) improves. Fold L10's "third trace identity / spectrum
  kurtosis constrains the hyperbolic-plane count" reading into the same evaluation `[literature §b16]`.
- **Labels:** walls PROVEN `[multiplicity]`; the evaluation and its effect are CONJECTURED; the clean
  negative (LP shows the third moment cannot move N_d) would be a documented result.
- **Definition of done:** LP solved for N_d with tr Â³; either (a) N_d ≥ 5/6 + ε or the off-line bound
  improves → formalize; or (b) a clean negative: the extremal world saturates the c = 3 inequality with
  equality on the third moment too (moment sequence m_k = 1, 4/3, 2, 13/4 matches GUE) → documented.

### #3. L1 — Finite Guinand–Weil dictionary → second trace identity (Groskin 2607.02828)
- **Goal:** recompute tr W_T and ‖W_T‖²_HS from the prime side via the v ↔ g_v dictionary, independently
  of the Montgomery–Vaughan step; hunt the "archimedean tail order" term as a new constraint.
- **Why it matters:** the single most valuable cheap vector — an adversarial cross-check of the core
  moment computation that the whole method rests on `[literature §c1]`; a second independent trace
  identity is exactly the kind of triangulation the honesty protocol demands.
- **Inputs needed:** Groskin 2607.02828 (PAPER-HUNT, target #1 — abstract-fetched only `[literature §a]`);
  `tools/finitet` W_T code and its measured tr/‖·‖² at T ∈ {100…700} `[finitet §3]`;
  `research/papers/anthropic-informal-note.txt` (Lemma 3.3 structure); verification-001.md's identity
  check `[verif-001 §3]`.
- **Method:** implement the dictionary (every real even Galerkin coefficient vector v ↔ a band-limited
  Guinand–Weil test function g_v with exact equality of quadratic values), compute the prime-side
  explicit-formula sums for the same windows, compare against the Montgomery–Vaughan values.
- **Labels:** dictionary existence PROVEN (per Groskin abstract — CONJECTURED as a usable tool until the
  paper text is in hand); the cross-check itself is NEW; any discrepancy is a CHECKED-NUMERICALLY finding
  to escalate.
- **Definition of done:** second independent computation of tr W_T and ‖W_T‖²_HS agreeing with
  `[finitet §3]` to f64 / expected truncation precision for T = 100…700, plus a written statement of what
  the archimedean tail term is and whether it constrains the certificate. Disagreement = escalate.

### #4. V7 — Method sandbox: certificate on RH-true vs RH-false worlds
- **Goal:** calibrate the method. Does the rank–trace certificate saturate at ≈100% when RH holds, or only
  at ~2/3?
- **Why it matters:** this decides the entire strategy — if the certificate gives ≈2/3 even in an
  RH-true world, the two-moment method is inherently lossy and only new *inputs* help (fund V4/V5's
  roadmap); if it gives ≈1, the deficit is purely arithmetic and the extremal-law obstruction is the whole
  story `[crossdomain V7, §3]`.
- **Inputs needed:** V1's W_T code (`tools/finitet`); empirical ordinates (RH-true world: all zeros on the
  line); a Davenport–Heilbronn-style or synthetic world with a few % off-line `[crossdomain V7]`;
  the paper's note that the DH certificate is "empty" (C Rem 7.2(iii), as reported `[litmap §4c12]`).
- **Method:** run the same pipeline on (a) the real configuration (all on-line), (b) a forced-off-line
  configuration (inject a few % off-line pairs, reuse finitet's synthetic-pair machinery `[finitet §4.7]`),
  (c) optionally the Selberg-zeta analogue (harder). Compare certificate values vs 0.6725.
- **Labels:** method structure PROVEN `[litmap §2]`; the sandbox outcomes are CONJECTURED; the DH "empty
  certificate" is PROVEN-as-stated in C `[litmap §4c12]`.
- **Definition of done:** a table of certificate-value vs world; interpretation written up (lossy-method vs
  arithmetic-deficit). Either answer redirects round 3 correctly.

### #5. V4 — Moment-order capacity LP: the "cost of missing data" roadmap
- **Goal:** quantify exactly what each conjectural correlation input is worth as a *curve* (ceiling vs
  number of inputs), not just the two endpoints 13/18 and 1.
- **Why it matters:** the conditional levers are PROVEN-quantified in C (HL*(4,λ) → 13/18; all moments →
  1 `[ceiling §3.8, mollifier §6]`); V4 converts them into a capacity curve so a later round attacks the
  cheapest conjecture `[crossdomain V4]`.
- **Inputs needed:** V5's LP code (build order: V5 before V4); the 256-law's higher correlation functions
  (from `Zeta23/PairCeiling/LawN256.lean` + `NearCUE.lean`); the GUE/sine-kernel triple-correlation value
  S₃ (Hejhal/RS96 — CONJECTURED as a certificate input).
- **Method:** add the constraint S₃(j,k) = (GUE value) to the marked-configuration LP and re-solve; record
  the new ceiling; repeat for the 4th moment if cheap.
- **Labels:** the law's S₃ being far from GUE is CONJECTURED (a *periodic* process — this is the open
  question the run answers `[crossdomain V4]`); the roadmap endpoints are PROVEN-conditional `[ceiling §3.8]`.
- **Definition of done:** a plotted curve "certified proportion vs number of correlation inputs used"; if
  pinning S₃ does not move the ceiling, that is a documented finding (the roadmap is empty for
  triple-correlation, only higher inputs bite).

### #6. L4 — Sylvester inertia on the Connes–van Suijlekom truncated Weil form
- **Goal:** run the paper's rank–trace / inertia count on the CvS Galerkin matrices (a different
  restriction than the φ̂_T-window) and compare constants.
- **Why it matters:** no one has run an inertia/rank-counting inequality on the CvS/CCM truncated Weil form
  — Groskin's spectra are used for eigenvalue nonnegativity only `[literature §d2]`; the CvS
  ground-state Fourier–Mellin zeros provably lie on the line, so positivity is built in and the on-line
  part may be provably full-rank `[literature §b5]`.
- **Inputs needed:** Groskin 2605.20224 + Connes 2602.04022 (PAPER-HUNT, next-tier list); Rust; the
  inertia machinery mirrored from `Zeta23/ZeroSide/`.
- **Method:** reconstruct (or reimplement) the CvS truncated form at prime cutoffs c = 13…100, bands N;
  compute Sylvester inertia and the rank–trace bound on their matrices; compare with the φ̂_T-window
  constant 0.6725 `[kernel §1]`.
- **Labels:** the CvS truncation and its on-line ground states are CONJECTURED-as-reported (abstracts
  only); the inertia method is PROVEN-in-Lean for W_T `[litmap §2]`.
- **Definition of done:** a comparison table (CvS constant vs 0.6725) at several (c, N); if the CvS
  restriction certifies more than 0.6725, that is a new conditional-ish constant worth formalizing; if
  not, a documented negative with the reason (e.g., different normalization).

### #7. V12 — Dirichlet-family program (family-averaged 2/3) — probe now, program later
- **Goal:** make C Rem 7.2(iii) rigorous: averaging over χ mod q restores bandwidth 1 for the family, giving
  ≥ 2/3 − o(1) of a family's zeros on the line; then attempt the GL(2) weight-aspect family.
- **Why it matters:** the biggest open prize: a new theorem with all PROVEN ingredients (explicit formula,
  RvM, Stirling, MV, character orthogonality, BV-type errors) and an assembly that C explicitly did not
  carry out `[crossdomain V12, lfunctions §5]`; the GL(2) family statement is the one live GL(2) target
  (individual forms are PROVEN dead `[lfunctions §4–§5]`).
- **Inputs needed:** C Rem 7.2(iii) + C Prop 4.2 (Gevrey taper); attack-lfunctions.md's transport map and
  its Dirichlet probe spec `[lfunctions §6]`; LMFDB Dirichlet L-function data or a χ mod q evaluator;
  Petersson/Kuznetsov background (for the GL(2) leg only).
- **Method (probe first):** for fixed large q, T = (log q)^c, compute the family-averaged HS norm with the
  orthogonality-killed off-diagonal; check whether bandwidth-1 restoration is numerically real before
  committing to the Gevrey taper.
- **Labels:** the mechanism is CONJECTURED (C states it "one expects…", unclaimed `[lfunctions §5]`); the
  probe outcome is CONJECTURED; every ingredient is PROVEN `[lfunctions §2]`.
- **Definition of done:** probe: bandwidth restoration holds or fails at q ~ 10⁶–10⁸ — either is a
  documented result that decides funding. Full program (only if probe passes): rigorous family-averaged
  ≥ 2/3 − o(1) for Dirichlet characters, written up; GL(2) weight aspect is a stretch target with DoD =
  the same statement for a newform family or a documented Kloosterman obstruction.

### #8. M28 — EnclOK adversarial re-check (the ceiling's only non-Lean link)
- **Goal:** independently recompute the 256-law's LP solution and the 70-digit interval enclosures of
  S(j), j = 1…256, and compare hashes.
- **Why it matters:** this is the single live way the 0.6818 ceiling could be *wrong* — everything else is
  kernel-proven `[ceiling §1, §4 keep-alive 2]`. If the enclosure is wrong the ceiling collapses.
- **Inputs needed:** the exact-rational certificate and its recorded hash (in attack-ceiling.md / the
  PairCeiling directory); 70-digit interval arithmetic (Python/mpmath is fine at this precision — not
  CPU-bound).
- **Method:** re-solve the marked-configuration LP from scratch (or re-verify the recorded rational
  solution), recompute the S(j) enclosures, compare against `EnclOK`'s recorded values and hash.
- **Labels:** EnclOK is CHECKED NUMERICALLY (round 1) `[ceiling §1]`; the re-check is NEW; everything
  downstream of the enclosures is Lean-`decide`-verified `[ceiling §1]`.
- **Definition of done:** hash match → ceiling's last assumption hardened; mismatch → ceiling collapses →
  escalate immediately (that changes everything).

### #9. V5 — F≡1 support curve (reproduce 1.04 / 1.26 / 1.70)
- **Goal:** reproduce C Rem 1.1's quantification as a curve: certified proportion vs assumed bandwidth A
  with F ≡ 1 on [0, A].
- **Why it matters:** validates the roadmap and gives the exact price of each unit of bandwidth
  `[crossdomain V5]`; also the build-order prerequisite for V4 (its LP code).
- **Inputs needed:** attack-ceiling.md's LP formulation (`Stability.lean` constraint); the 256-law
  machinery; C Rem 1.1's three points (0.70@1.04, 0.80@1.26, 0.90@1.70).
- **Method:** extend the ceiling LP: maximize certificate value against configurations with F ≡ 1 on
  [0, A]; plot proportion vs A; compare with the Remark's points.
- **Labels:** the ceiling LP is PROVEN in Lean `[ceiling §1]`; the Remark's three points are
  PROVEN-as-stated (C Rem 1.1) `[litmap §4b3]`; the curve is CONJECTURED until computed.
- **Definition of done:** curve agrees with the Remark → roadmap validated; disagrees → the Remark needs
  correction (a finding). Either way, exact price per unit bandwidth is on record.

### #10. V19 — Selberg-class unification theorem
- **Goal:** state and prove the axiomatic degree-1 theorem whose corollaries are the ζ and Dirichlet
  theorems (Thms A–E), and whose class-level corollary is the GL(2) death.
- **Why it matters:** a guaranteed deliverable that consolidates the whole method into one statement and
  surfaces any axiom the method silently exploits `[crossdomain V19]`; the GL(2) death becomes a
  class-level statement `[lfunctions §4]`.
- **Inputs needed:** the four held papers (C, N, B24, B25); literature-map.md's 11-ingredient map
  `[litmap §2]`; Selberg-class axioms as cited in C/IK04.
- **Method:** write the axiom set (functional equation, RvM density, explicit formula, Chebyshev-class
  prime sums, MV off-diagonal), map each ingredient to its axiom, derive Thms A–E as corollaries.
- **Labels:** the ingredients are PROVEN `[litmap §2]`; the axiomatization is NEW/CONJECTURED; kill if a
  Selberg-class function fails an axiom in a way the method silently exploits.
- **Definition of done:** a written theorem statement + axiom-ingredient map + corollary derivation for ζ
  and Dirichlet; the class-level GL(2) bandwidth-1/2 statement recorded; suitable as the basis of a future
  Lean-ization.

### #11. V1 — Weil-form spectrum experiment (full run; folds W2/W3/W5/V6)
- **Goal:** (a) C∞-smoothed φ_T run to settle the error-term question; (b) full sorted spectrum of W_T and
  its eigenvalue law vs the extremal law and GUE; (c) Hankel-determinant margin of the ordinate
  distribution (W3); (d) empirical form factor F(α) on [0,3] from 10⁴ zeros (V6); (e) the real-data
  certificate value (W2).
- **Why it matters:** measures the method's real slack in the realized world; the C∞-ramp run decides
  whether the slow ~1/log T approach of ‖W‖²_HS is a kernel artifact (hard cutoff) or a genuine
  zero-statistics effect `[finitet §7]`; the W3 Hankel margin is a genuinely new measurement
  `[crossdomain W3]`.
- **Inputs needed:** `tools/finitet` (extend with a C∞ ramp); `tools/zeta-rs` (higher-T zeros);
  `tools/data/zeros_1_1000.txt`; attack-kernel.md's extremal-law spectrum (2/3 ones, 1/6 twos, 1/6 zeros)
  `[kernel §1, crossdomain V1]`.
- **Method:** reuse finitet's W_T construction; add the χ-ramp smoothing; compute spectra, Hankel
  determinants of the normalized ordinates, and the empirical form factor (Rust).
- **Labels:** finite-T results are CHECKED NUMERICALLY `[finitet §3–§5]`; F(α) empirics are trend-only
  `[verif-001 §4]`; everything new is CONJECTURED until run.
- **Definition of done:** (a) C∞ run: ‖W‖²_HS/N pulls toward 1.3275 substantially → the o(1) is better
  than the idealized model (changes belief about error terms); stays ~3% off → zero-statistics effect
  (confirmed slow). (b) spectrum comparison: near-extremal law → certificate near-optimal in the realized
  world (fund V2 harder is pointless, redirect to new targets); far from it → real slack exists.
  (c)–(e) measurements recorded with margins.

### #12. V9 — Derivative tower ξ″, ξ‴ (+ FGL transport)
- **Goal:** extend the rank–trace certificate to ξ″/ξ‴; test whether the simple-on-line constants increase
  with the derivative order (FGL's pattern).
- **Why it matters:** new-target path with proven machinery; the ξ′ constants are PROVEN (0.85838 flat /
  0.86864 quartic `[kernel §4, litmap §4c9]`) and FGL's pattern suggests ξ″/ξ‴ do better; the derivative
  tower gives joint constraints on the same zero configuration `[crossdomain V9]`; the ξ′-box transport
  would give simple ξ′-zeros feeding Farmer's distinct-zeros chain `[literature §b13]`.
- **Inputs needed:** `Zeta23/XiPrime/` (Lean, for the ξ′/ξ explicit formula pattern); C Rem 7.3; FGL
  (arXiv:0803.0425, abstract-level); `tools/angle_kernel` CG machinery.
- **Method:** derive the explicit formula for ξ″/ξ′ (pattern from ξ′/ξ), compute its functional, run the
  pipeline numerically; if the constant beats 0.86864 (simple) / 0.93432 (distinct), formalize.
- **Labels:** ξ′ constants PROVEN `[kernel §4]`; the ξ″/ξ‴ extension is CONJECTURED; kill if constants
  decrease with j or the functional degenerates (double-pole breaks the (1,1)-plane bookkeeping)
  `[crossdomain V9]`.
- **Definition of done:** a numerically-optimized ξ″ certificate constant with the same machinery; if >
  0.86864 → Lean-ize; if ≤ → documented (with the A4 caution: interlacing gives no upper constraint, so
  higher-order constants do not imply lower-order ones `[crossdomain A4]`).

### #13. M29 — Beyond-bandwidth-1 probe: the λ = 1.04 prime-pair sum
- **Goal:** write the exact off-diagonal prime-pair sum at X = T^{1+ε} (small ε) and check which known
  unconditional upper bound gives a nontrivial constant; numerically measure the sum's actual size.
- **Why it matters:** settles the last live "maybe there is a proven sliver of F beyond 1" question
  `[ceiling §3, §4 FUND]`; this is attack-mollifier's concrete recommended next step `[mollifier §6]` and
  the GLSS25 direction (PCC on average → 100% simple without RH) `[literature §b8]`.
- **Inputs needed:** C §7.5(a) (the wall statement) `[mollifier §5]`; B24 Thm 1 (F on [0,1]); the
  certificate's tolerance (in-class gap = 1.4%, so any polynomial-in-X loss kills it `[crossdomain A5]`);
  sieve / Vinogradov–Korobov bounds from the literature; Rust prime sieve to X ~ 10⁷.
- **Method:** write Σ_{n,m≤T^{1+ε}} Λ(n)Λ(m)g(log n)h(log m) over |log n − log m| ≤ δ; test candidate
  unconditional bounds (sieve, VK zero-free-region-driven); numerically evaluate the sum at
  T ~ 10⁵–10⁶ to see its size vs tolerance.
- **Labels:** the wall is PROVEN `[ceiling §2, mollifier §5]`; A1/A5 deaths are PROVEN DEAD (specific
  bounds fail) `[crossdomain §5]`; the existence of *any* usable unconditional bound is CONJECTURED and
  expected negative.
- **Definition of done:** either a bound with a constant beating the tolerance (breakthrough — escalate),
  or the documented negative: no known bound clears the O(1)-at-constant-scale tolerance, closing the
  "proven sliver" question and validating 1.04/1.26/1.70 empirically.

### #14. L2 — Screw-function formulation of the Weil form (Suzuki)
- **Goal:** re-derive the constant 3/2 − (1/√2)cot(1/√2) from screw-function regularity, giving an
  independent derivation of the off-diagonal control, possibly with cleaner error terms.
- **Why it matters:** an independent path to the same constant is exactly the triangulation the program
  needs; cleaner error terms feed V20 (effective finite-T) `[literature §b2]`.
- **Inputs needed:** Suzuki 2606.09096 + 2206.03682 (PAPER-HUNT target #3); the W_T code
  (`tools/finitet`); the screw-function definition (norm kernel of the Weil form).
- **Method:** express tr W_T and ‖W_T‖²_HS as integrals of the screw function; derive the MV off-diagonal
  control as a theorem about the screw function's regularity.
- **Labels:** the screw-function framework is CONJECTURED-as-reported (abstracts only); the constant and
  the MV control are PROVEN by the paper's route `[litmap §2]`.
- **Definition of done:** an independent derivation reaching 1.3274992963205885… with a written error-term
  comparison vs the MV route; a strictly better error term is a genuine improvement (feeds V20), equality
  is still a validated cross-check.

### #15. L8 — Two-form argument: CGG ζ′(ρ)-moment form + Weil form
- **Goal:** combine the discrete mollified ζ′(ρ)-moment quadratic form (the 19/27 machinery) with the Weil
  form as a joint constraint on the same zero set.
- **Why it matters:** no one has combined them `[literature §b10, §d8]`; the CGG multiplicity device is
  already the paper's Prop 4.4 regrouping (PROVEN `[mollifier §3, litmap §2]`), so the two forms are not
  as orthogonal as they look — a joint constraint is genuinely unexplored.
- **Inputs needed:** BHB 1302.5018 (PAPER-HUNT, next-tier); C §7.5(c); B25 §1 (CGG method summary);
  ζ′(ρ) values at the zeros (zeros file + `tools/zeta-rs` derivative evaluation).
- **Method:** exploratory: write the two quadratic forms on the same zero set, look for a joint
  inequality (e.g., a bound on the number of zeros where both forms are small).
- **Labels:** the CGG device is PROVEN (as transplanted, C §7.5(c) `[mollifier §3]`); the two-form
  combination is CONJECTURED; the 19/27 result is RH-conditional `[litmap §1b]`.
- **Definition of done:** a written structure map + one concrete joint inequality (even weak) or an
  explicit obstruction. This is the exploratory vector — DoD is honest progress or a documented dead end.

---

## 4. PROVEN DEAD — round-1 documented deaths (do not re-derive)

| Vector | Death (one line) | Source |
|---|---|---|
| A1 Goldston–Montgomery variance for beyond-1 off-diagonal | Variance controls fluctuations; the obstruction is the *mean* (Hardy–Littlewood strength) — irrelevant | idea-generator-crossdomain.md §5 |
| A2 Odd/imaginary-window off-line counter | Functional equation pairs ρ with 1−ρ̄ at the same height; contributions cancel exactly: Im(W_T) ≡ 0 | idea-generator-crossdomain.md §5 |
| A3 Small-support Weil positivity as certificate input | Proven positivity lives below the first zero height — no overlap with the bandwidth-1 regime | idea-generator-crossdomain.md §5 |
| A4 Joint (ξ, ξ′) interlacing LP | Interlacing gives only a lower bound (N₀,ξ′ ≥ N₀,ξ − 1), no upper constraint — joint LP is empty; also kills the "ξ′ 85.8% ⇒ ζ" fallacy | idea-generator-crossdomain.md §5 |
| A5 Trivial upper bound on beyond-1 off-diagonal | 2δX² ≫ main term·(X/T); certificate tolerance is O(1) at constant scale — any polynomial-in-X loss kills it | idea-generator-crossdomain.md §5 |
| Beat 0.6818 unconditionally by the same certificate class | Ceiling PROVEN in Lean (modulo EnclOK CHECKED NUMERICALLY); every class input proven-optimal or hard-bounded; no proven beyond-1 input exists | attack-ceiling.md §4, §3 |
| Better window for ζ's functional | Cosine is the global minimizer of Q (Euler–Lagrange + convexity); all numerically-better candidates violate bandwidth; 0.6725 is the window ceiling | attack-kernel.md §5, §3 |
| Mollifier fusion as a lever | Both methods share the same prime-pair wall; the only fusion point (CGG98 integrality) is already inside the paper; two-trace scheme saturated at λ ≤ 1 | attack-mollifier.md §6 |
| Funding multiplicity-distribution data | Empirical all-simple world is the *extremal* case (Δ = 0); bookkeeping LP-optimal; lemmaR_tight — data funding cannot move the constants | attack-multiplicity.md §4 |
| Individual GL(2) transport | Certificate provably empty at Λ* = 1/2 (dimension ceiling, C Prop 7.4); even pair correlation does not help — hard wall | attack-lfunctions.md §4–§5 |

---

## 5. Strategic reading and allocation (s4h-strategy + s4h-resource-allocation)

**Terrain (what to fund / what to avoid):**
- **Fight:** the in-class gap (V2), the third moment (V3), cheap triangulation (L1, V1's C∞ run),
  the strategic sandbox (V7), the roadmap pricing (V4/V5). All use proven inputs or existing code.
- **Avoid re-fighting:** the window (kernel), the ceiling (except adversarially via V2/EnclOK), the
  two-moment multiplicity walls (except via V3), mollifier fusion, individual GL(2), all of A1–A5.
- **Wild/near-dead (V13–V16, V14, W4):** do not fund in round 2; one-line records suffice. They consume
  compute for near-certain negative or redundant outcomes.

**Allocation (compute-poor machine; CPU-bound → Rust, cache everything, run only what changes belief):**

| Claim | Allocation | Trade-off (what it gives up) |
|---|---|---|
| V2 LP dual | 1st | Highest-value use of a small LP solve; gives up nothing — it also hardens the ceiling |
| V3 third moment | 2nd | Needs the triple-correlation evaluation; gives up a clean answer if evaluation is hard — mitigate by doing the λ<2/3 diagonal case first |
| L1 dictionary cross-check | parallel | Gated on paper-hunting; runs while the LP code is being written |
| V1 C∞ run + spectrum | parallel | Uses existing finitet/zeta-rs; cheap marginal compute |
| V7 sandbox | after V1 | Reuses V1's code; no new compute of its own |
| V4/V5 LP roadmap | after V2's code | Reuses the same LP machinery |
| EnclOK re-check | any time | ~1 hour, Python/mpmath |
| V12 probe | small slot | Cheap numerical test that decides a big bet |
| V8/V9/V20, L2/L4/L8 | paper-hunting downtime | Writing/reading-heavy; low compute |
| V13–V16, V14, V18, V11, L3, L9 | **do not fund** | Explicitly under-funded: expected negative/redundant/very-low-EV |

**Force economy:** three one-line strategic rules for round 2 — (1) *never* run a computation that does not
change what we believe (hooks/agents.md); (2) prefer Rust and cached data (finitet/zeta-rs/zeros file);
(3) a clean negative is a deliverable — label it and move on; only the honesty guardrails can stop a line,
and only funding decisions stop a round (hooks/agents.md).

**Victory definition for round 2:** at least one of — a Lean-checked certificate reaching > 0.6725 toward
0.6818 (V2); a proven-or-clean-negative verdict on the third moment (V3); an independent cross-check of the
core moments (L1); the sandbox's bottleneck verdict (V7); or a documented closure of the beyond-1 question
(M29). Each is a genuine research result under the program's operative targets.

---

## 6. Paper-hunting targets (5 most valuable to obtain, and what each unlocks)

| # | Paper (arXiv id) | Unlocks | Value |
|---|---|---|---|
| 1 | **Groskin, "A finite Guinand–Weil dictionary…" (2607.02828)** | L1 (second trace identity — the #3-ranked vector; immediate adversarial cross-check of the core moment computation) + the "archimedean tail order" term as a candidate new constraint | Highest immediate leverage on round-2 execution |
| 2 | **Bombieri, "Remarks on Weil's quadratic functional…" (2000)** | The negative-index observation that C's whole zero-side reading rests on — we currently hold it only as C's citation (C §1.4, §7.4; `[litmap §5]`); also original truncation context for V2/V4/L4 | Validates the foundation of our own method from the primary source |
| 3 | **Suzuki, screw-function papers (2606.09096 + 2206.03682)** | L2 (independent constant derivation from screw-function regularity) and the entry to 2301.00421's de Branges structure (L3) | Independent triangulation + the de Branges rank bound (L3) |
| 4 | **Chirre–Gonçalves–de Laat, SDP pair-correlation kernels (1810.08843)** | V11/L5 (SDP-optimal kernels in the box framework; quantify the "different regime" claim `[ceiling §3.3]`); Cor 7 (0.8825/0.9412 for ξ′ under RH) as comparanda for V8/V9 | The one RH-conditional result that "operates in a different regime" — needed to quantify whether its trick survives B24 error terms |
| 5 | **Montgomery 1973 + Montgomery–Vaughan 1974 (Hilbert's inequality)** | Primary sources of the two core prime-side moments and the MV constant (3π/2) that feed Lemma 3.3 and force the λ ≤ 1 wall; independent verification of constants (B25's kernel formula was already found garbled in extraction `[litmap §5]`) | Deepest layer of validation of the constant chain |

**Next-tier (fetch when budget allows):** Groskin 2605.20224 (CvS truncation numerics, L4), Connes 2602.04022
(2026 survey; L4 context), Goldston–Suriajaya GS25/GS26 (box-hypothesis framing C replaces; V10/L7
context), CCLM17 (Cor 14 — the one-delta extremal problem behind Theorem D; already independently proven in
`[kernel §2]`, so lower priority), CFKLB 2508.11108 (short-mollifier variational kernel, L7), BHB 1302.5018
(L8), P&P 1805.07741 (L9 — method only; conclusion flagged unverified `[literature §a]`), Hejhal 1994 and
GM87 (third-moment and beyond-1 inputs for V3/M29), FGL 0803.0425 (V9), Radziwill 1207.6583 (mollifier
ceiling context for the paper's "not a mollifier method" claim).

---

## 7. Honesty footer

- Every "PROVEN / DEAD / TESTED-OPEN" claim above traces to a round-1 file: `[kernel]` = attack-kernel.md,
  `[ceiling]` = attack-ceiling.md, `[multiplicity]` = attack-multiplicity.md, `[mollifier]` =
  attack-mollifier.md, `[lfunctions]` = attack-lfunctions.md, `[finitet]` = attack-finitet.md,
  `[verif-001]` = verification-001.md, `[litmap]` = literature-map.md, `[crossdomain]` =
  idea-generator-crossdomain.md, `[literature]` = idea-generator-literature.md. Nothing was re-derived here.
- All scores, weighted totals, rankings, and strategic allocations are **CONJECTURED** (synthesizer
  judgment), not facts; they are a proposal for the round-2 planner, to be challenged by the VALIDATOR.
- The one fact-layer caveat carried into round 2, verbatim from the sources: the 0.6818 ceiling is Lean-
  proven **modulo EnclOK, which is CHECKED NUMERICALLY, not kernel-proven** `[ceiling §1]` — hence M28's
  funding. The B25 j_M kernel formula is garbled in the extracted .txt `[litmap §5]` — any L7 work must
  re-derive it before trusting the b-table.
- Deliberately NOT included: any claim that any attack "probably settles RH"; the program's search
  persists, but every vector here is scoped to a rigorous, adversarial-validated increment
  (hooks/agents.md).
