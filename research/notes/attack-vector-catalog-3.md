# Attack Vector Catalog — Round 3 (SYNTHESIZER output)

**Agent:** SYNTHESIZER (decision-criteria-weighting + strategy + resource-allocation + epistemology).
**Round:** 2 → 3 handoff. **Date:** 2026-08-11.
**Inputs merged (all in `research/notes/`):** the round-2 closures — attack-lpdual.md, close-inclass-gap.md,
attack-pricing-sheet.md, attack-m29.md, attack-gm-variance.md, attack-nevanlinna.md, attack-twobandwidth.md,
attack-thirdmoment.md, attack-hankel-test.md, attack-selberg-clt.md, attack-cvs-import.md, attack-qi-sweep.md,
attack-mu-sweep.md, attack-kh-triple.md, attack-ihara-sandbox.md, attack-sandbox.md, attack-finitet-cinf.md,
attack-conditioning.md, attack-detection-threshold.md, attack-hot-hand.md, attack-ls-estimator.md,
attack-xiprime.md, attack-multiplicity.md, attack-kernel.md, attack-ceiling.md, attack-f1curve.md,
attack-mollifier.md, attack-lfunctions.md, validation-001.md, validation-enclok.md, attack-twoform.md,
attack-mvconstant.md, attack-finitet.md, attack-dirichlet-family.md, attack-dirichlet-family-exp (code),
attack-mvconstant.md, regenerate-256law.md, selberg-class-theorem.md; the 17 idea catalogs
(idea-generator-*.md); the paper reads — paper-pcc2.md, paper-thirdmoment-pcc.md, paper-finder-001.md,
paper-finder-spectral.md, paper-finder-thirdmoment.md, paper-finder-jensen.md. (attack-joint-deriv-moments.md
does not exist — checked; its content, if any, is subsumed by attack-xiprime.md's derivative-tower section.)
**Method applied (s4h):** decision-criteria-weighting (explicit weights, scores before ranking),
strategy-terrain (fund/avoid), resource-allocation (trade-offs explicit), epistemology (every claim
labeled, provenance traced, epistemic status per thread).
**Honesty protocol (hooks/agents.md):** every PROVEN / DEAD / OPEN claim carries its source file in
brackets, e.g. `[pricing §3]` = attack-pricing-sheet.md §3; `[lpdual]` = attack-lpdual.md; `[ccg]` =
close-inclass-gap.md; `[m29]` = attack-m29.md; `[gmvar]` = attack-gm-variance.md; `[twbw]` =
attack-twobandwidth.md; `[tm]` = attack-thirdmoment.md; `[selclt]` = attack-selberg-clt.md; `[cvs]` =
attack-cvs-import.md; `[sandbox]` = attack-sandbox.md; `[ihara]` = attack-ihara-sandbox.md; `[detthr]` =
attack-detection-threshold.md; `[hot]` = attack-hot-hand.md; `[ls]` = attack-ls-estimator.md; `[xipr]` =
attack-xiprime.md; `[fin]` = attack-finitet.md; `[fincinf]` = attack-finitet-cinf.md; `[cond]` =
attack-conditioning.md; `[mvit]` = attack-multiplicity.md; `[kernel]` = attack-kernel.md; `[ceil]` =
attack-ceiling.md; `[f1c]` = attack-f1curve.md; `[moll]` = attack-mollifier.md; `[lf]` = attack-lfunctions.md;
`[v001]` = validation-001.md; `[enclok]` = validation-enclok.md; `[twoform]` = attack-twoform.md;
`[mvc]` = attack-mvconstant.md; `[dir]` = attack-dirichlet-family.md; `[rgl]` = regenerate-256law.md;
`[sct]` = selberg-class-theorem.md; `[pcc2]` = paper-pcc2.md; `[fg]` = paper-thirdmoment-pcc.md;
`[chem]` = idea-generator-chem.md; `[games]` = idea-generator-games.md; `[add]` = idea-generator-additive.md;
`[mlec]` = idea-generator-ml-eco.md; `[cat1]` = attack-vector-catalog.md (round-1→2 catalog). Nothing below
re-derives a result; this is synthesis, merge, scoring, and ranking. All scores are CONJECTURED
(synthesizer judgment), not facts.

---

## 0. The honest map after Round 2 (what round 2 settled, and what the search space now is)

**Round 2's decisive result — the in-class gap is CLOSED (in-class, not for the real zeros).**
The class-optimal bandwidth-one certificate is exact and rational: r(x) = 1−x with
c₀ = p₀ − Σⱼ(S_max(j)/256)(1−j/256) is valid against the whole 256-law enclosure class and attains
v = p₀ + 1/(6·256²) − δ = **0.6818312305953419** (exact rational arithmetic, `tools/lpdual/verify_exact_cert.py`;
PROVEN) [ccg §1–§2]; the Lean ceiling `ceiling_law256_signed` is TIGHT (in-class optimum lies in an
interval of width ~7.8·10⁻⁴³) [ccg §2]; the LP attains the ceiling to 5·10⁻⁹ and the shadow price of the
certified simple fraction p₁ is **exactly 1** — nothing inside the class moves v except p₁ [lpdual §3–§5,
cvs Check C]. The honest split is strict: the **real-zero constant remains 0.6725** (Thm D, PROVEN); the
law's p₀ = 0.68183 is a law property with no certified real-zero counterpart [ccg §3]. **The 0.6725 → 0.6818
gap is closed in-class; for the real zeros it needs beyond-bandwidth-1 input** [ccg §3, ceil §4].

**Round 2's second result — the pricing sheet (the strategic centerpiece).** Only ONE hypothetical input
has a positive price for the simple-fraction certificate: the **beyond-1 form-factor RANGE [1, 1.03+]**
(dv*/dA = 0.6363/A³ per unit bandwidth, M2 model; reproduces the paper's Remark points 0.70@1.04,
0.80@1.26, 0.90@1.70 to ≤1.1%) [pricing §5–§6]. The third moment m₃ and any min-gap/repulsion bound are
**priced NEGATIVE** for the simple-fraction certificate: m₃ ≥ 2 ⟹ p₁ ≤ 2/3 (exact identity m₃ = 4−3p₁, so
v* ≤ 2/3; price −1/3 per unit) [pricing §3]; min-gap > 0 ⟹ p₁ = 0.50195 (exact Parseval floor; step −0.1799
at X = 0⁺) [pricing §4]. For the distinct-count certificate m₃ is neutral at m₃ = 2 (B = 5/6 exactly) and
its only mechanism price is −1/18 per unit (an upper bound m₃ < 2 would help; none exists — the computable
values are m₃ = 5, 13/4 ≥ 2) [pricing §3, twbw §3.2]. Feasibility labels: beyond-1 CONJECTURED (M29:
every proven bound fails by 3.6·10³–3.7·10⁴×); m₃ likely-DEAD (twbw, paper §7.5(e)); min-gap CONJECTURED
and negative even if proven [pricing §8]. **Funding a negative-priced input is the canonical
opportunity-cost error** [pricing §7].

**The wall structure, all PROVEN (Lean) or documented-dead:**
1. **0.6725 = window ceiling for ζ** — cosine is the unique global minimizer of Q (Euler–Lagrange v″+2v=0 +
   I+T ≻ 0 with the validator-corrected λ_min = 1−2/π² ≈ 0.797; free-grid confirm to 2.2·10⁻¹⁶); every
   numerically-better candidate (c > 1/2, λ > 1) violates Claim 2.1's bandwidth [kernel §2–§3, v001 T2].
   Robustness: 1% window perturbation → ≤0.02% constant change (quadratic flat, κ ≈ 1.05–1.25); the only
   load-bearing spot is the C∞ boundary ramp, cost δ ≈ 0.45·w (linear; O(1/L) if the ramp is at the
   resolution scale) [cond §4].
2. **0.6818 = bandwidth-one certificate-class ceiling** — PROVEN (Lean) modulo the single displayed
   hypothesis EnclOK, which is INCONCLUSIVE (not independently verified, NOT refuted; the authors'
   certificate cert_N256_blk_b128m.json is not public) [enclok, ceil §1]. All downstream constants
   re-verified (checkRows, edgeNonneg, D(1), p₀, e₁) [enclok §3]. The regeneration attempt hit a hard
   blocker: no reconstructed family spans the exact-CUE ramp at N = 256 (infeasible for all tested
   families) — the family is private [rgl §4].
3. **5/6 = two-moment distinct wall** — lemmaR_tight PROVEN; LP-optimal bookkeeping; the empirical all-simple
   world sits exactly on the wall (Δ = 0) [mvit §0, §2].
4. **The third moment cannot break 5/6 unconditionally** — corrected values m₃(1/2) = 5, m₃(2/3) = 13/4,
   m₃(1) = 2 (three independent verifications; the 125/64 script bug retracted) [tm §4, twbw §2]; the
   admissible-cubic certificate gives 0.8071 (λ = 2/3) < 5/6; conditional λ = 1 gives 0.8359 (with Thm D) /
   0.8498 (RH) [tm §5]. K–H: A3(1) = 0 exactly (the third moment is two-point data at λ = 1) [kh §2].
5. **No proven beyond-1 sliver exists — mean, variance, or distributional.** M29: MV-Hilbert bound exceeds
   the tolerance by 3.6·10³–3.7·10⁴× (measured, T = 10⁴–10⁶), every other proven bound equal-or-worse; only
   HL / Montgomery-PCC *values* would clear it (CONJECTURED) [m29]. B10/GM-variance: dictionary inverted
   (window U probes F at α ≲ 1/(Uρ); beyond-1 ⟺ short windows U < 1/ρ ≈ 0.93); no unconditional variance
   statement reaches α > 1 with content; the variance is orthogonal to the certificate ("variance": 0 hits
   in the paper) [gmvar §2, §4, §6]. V13/distributional: DEAD-consistent-with-walls — a phase-randomized
   super-block construction realizes every proven fluctuation input (Selberg CLT shape included) with simple
   fraction exactly p₀ = 0.6818287, so v ≤ p₀ + |E(1)| + o(1) survives any fluctuation certificate
   [selclt §3, §6].
6. **GL(2) individual transport is empty** (dimension ceiling Λ* = 1/2, certificate ≤ 0; even PCC does not
   move it) [lf §4–§5]; the Dirichlet-family mechanism (Rem 7.2(iii)) is the one live family target
   [lf §6].
7. **QI and control inequality sweeps are closed with documented negatives** — no inequality reading the
   certificate's data budget beats Lemma 3.2; the strongest candidate (CS refinement (L′)) is strictly
   stronger pointwise but its gain (trQ₊−2b)²/b vanishes at the sharp configurations [qi §5, mu §4].
8. **The CvS/CCM import is DEAD for the proportion program** (B1 object mismatch, B2 hypothesis gap, B3
   orthogonality — even RH does not move the ceiling; the shadow-price probe pins v* = p₁ + |E(1)|) [cvs
   §6]. The genuinely useful G6-adjacent mechanism is Groskin's tail-budget certification (Cor 3.3) [cvs §7].
9. **The method sandbox answers V7:** the certificate is a pair-correlation functional, NOT an RH
   statement. Lattice (RH-true) saturates ≈ 0.977; ζ zeros ≈ 0.6725; small Ramanujan graphs collapse to
   −0.9…−22.9 (coincident angles); Poisson → empty certificate (DH mechanism) [ihara §3–§6, sandbox §4].
   The 2/3 is the arithmetic of the realized (GUE) pair correlation, not a structural cap.
10. **Empirics:** beyond-1 form-factor "climb-then-decay" is an estimator artifact (Exp(1) noise floor,
    N-independent; the α=1 Gram-lattice spike is an unfolding artifact) — no hint against Montgomery
    [hot §5]; the LS estimator gains nothing on the sharp window [ls §4]; BUT the α ∈ [1.0, 1.3] arithmetic
    feature is REAL (≥11σ under the standard estimator, unchanged under LS) with cause unidentified
    [ls §5, games §639–660].
11. **MV constant sharpening does nothing** (3π/2 lives only in an o(1) error; measured norm ≈ 2.52 < π) [mvc §0].

**Therefore the round-3 search space is exactly:**
(a) **new targets with PROVEN machinery**: the derivative tower ξ″, ξ‴ (constants PROVEN for ξ′; interlacing
CHECKED; extension CONJECTURED) [kernel §4, xipr §5], the Dirichlet-family theorem (probe PASSED; assembly
CONJECTURED) [dir §0, §6], the Selberg-class axiomatic theorem T (WRITTEN; Lean-ization pending) [sct];
(b) **the effective finite-T program (V20)** — the only remaining written-theorem deliverable for the real
zeros with proven inputs [crossdomain V20, fin, fincinf, cond];
(c) **closure of the ceiling's last non-Lean link (EnclOK/S₃)** — blocked on the private family, with
documented routes [enclok, rgl];
(d) **the positive-priced input** (beyond-1 range) as a conditional-input certificate program (RH + uniform
HL / FG twisted PCC), plus the HL*(k₀,λ) → 13/18 roadmap [pricing, fg, pcc2];
(e) **loose-end adjudications**: m₄(1) (four competing values), the α≈1.1 feature, the 6th-moment
literature claim, the multi-window probe, the IPR/slack diagnostics;
(f) **documented negatives to NOT re-fund** (the pricing sheet's kills): m₃-for-simple, min-gap, CvS, the
QI/control sweeps, the distributional certificate, the variance flank, individual GL(2).

---

## 1. Closures ledger (every round-2 closure, with source)

| # | Closure | Verdict | Source |
|---|---|---|---|
| 1 | In-class gap 0.6725 → 0.6818 (V2) | **CLOSED in-class**: exact cert r = 1−x attains p₀ + 1/(6·256²) − δ = 0.6818312305953419; ceiling TIGHT (interval width ~7.8·10⁻⁴³); real constant unchanged (0.6725, Thm D) | [lpdual], [ccg] |
| 2 | No missing constraint inside bandwidth one | v* = p₁ + \|E(1)\| for every p₁ (shadow price of p₁ exactly 1); only beyond-1 / multiplicity input can move v | [lpdual §5], [cvs §5.3] |
| 3 | E5.3 pricing sheet | Only beyond-1 RANGE positive-priced (0.6363/A³); m₃ −1/3 per unit (simple cert) / neutral-at-5/6 (distinct cert); min-gap −0.1799 step; single beyond-1 point priced at ~8.5·10⁻⁴/δ (wrong unit) | [pricing] |
| 4 | M29 beyond-1 mean | **DOCUMENTED NEGATIVE, PROVEN**: MV bound 3.6·10³–3.7·10⁴× over tolerance; grows T^ε/poly(log T); only HL/PCC values (CONJECTURED) clear it | [m29] |
| 5 | B10/GM-variance flank | **DEAD**: dictionary inverted; no unconditional variance at α > 1 with content (Selberg α≈0, Fujii in-band, GM78 β≤1 trivial); variance orthogonal to the certificate | [gmvar §2, §4, §6] |
| 6 | V13 distributional certificate | **DEAD-consistent-with-walls**: p₀-family (super-block phase-randomized law) realizes every proven fluctuation input with p₁ = p₀; ceiling survives any fluctuation certificate | [selclt §3, §6] |
| 7 | V3 single-window third moment | **ABANDONED as unconditional lever**: 0.8071 (λ=2/3) < 5/6; conditional λ=1 gives 0.8359 (Thm D) / 0.8498 (RH) | [tm §5] |
| 8 | P6.5 two-bandwidth joint (third moment) | **CLEAN NEGATIVE**: m₃(1/2) = 5 (task's 2 REFUTED); no cross-window inequality exists; LP optimum exactly 5/6; unconstrained cubic LP unbounded | [twbw §0, §3] |
| 9 | Hankel/realization-theory test (C-BT3) | **FEASIBLE but NON-SEPARATING**: (1,4/3,2) realizable (extremal world); third moment carries zero separation power; the separation is a FOURTH-moment / m₀ phenomenon | [hankel §0] |
| 10 | K–H triple bound (A1) | **RESTATEMENT → DEAD as P2 input**: det ≥ 0 is a tautology; weaker than trivial bounds at every in-band triple; admissible m₃ range [−0.17, 4.10] excludes nothing; A3(1) = 0 exactly | [kh §6] |
| 11 | Nevanlinna/marks reframe (P8.1) | **NEGATIVE as constraint-discovery; POSITIVE as diagnosis**: integrality is satisfied by the law (m₂ = 2−p₀); the gap is a second-moment gap [2−1.3275, 2−1.3182]; "integrality closes the gap" dead on arrival | [nevanlinna §4–§5] |
| 12 | QI sweep (P10.1/P10.3) | **NO**: no QI inequality beats Lemma 3.2 on the data budget; CS refinement (L′) gain vanishes at sharp configs | [qi §5] |
| 13 | Control sweep (C-MU2) | **NO**: independent confirmation; Glover/Perron/Ostrowski–Schneider/D-scaled-μ all fail; two-layer class-level argument | [mu §4] |
| 14 | CvS import (G1/G6) | **DEAD** (B1 object mismatch — W_T fails the divided-difference cocycle by O(1); B2 hypothesis gap — simple/isolated/even unproven; B3 orthogonality — even RH doesn't move the ceiling) | [cvs §6] |
| 15 | V7 method sandbox | **COMPLETE**: certificate = pair-correlation functional; ≈2/3 in RH-true GUE worlds, 0.977 lattice, ~0 Poisson, negative for coincident-atom Ramanujan graphs; deficit = realized arithmetic, not method lossiness | [sandbox §0, §4], [ihara §6] |
| 16 | E4 detection threshold | **COMPLETE**: blind window O(1) pairs (scattered: 1 pair at β≥0.05; top-clustered: 1–1.5%); n₋ = 0 on real data; a hypothetical off-line signal must be nearly silent | [detthr §0, §7] |
| 17 | G3.1 hot-hand beyond-1 trend | **ARTIFACT**: no empirical hint against Montgomery; per-α std ≈ 1 at every N; α=1 spike = Gram-lattice unfolding artifact; verdict over all non-lattice α ∈ (0.05, 3.0] | [hot §5] |
| 18 | B1 Landy–Szalay estimator | **NO BIAS-CANCELLATION on the sharp window**: equal bias, 1.2–2.5× worse variance; the α≈1.1 feature is real under both estimators (≥11σ) | [ls §4–§5] |
| 19 | E5.4 conditioning | **ROBUST**: 1% window perturbation → ≤0.02% constant change; boundary ramp δ ≈ 0.45·w (keep at resolution scale); finitet's window is the exact cosine | [cond §4–§5] |
| 20 | C∞-smoothing (finitet-cinf) | **NO pull toward 1.32750**: smoothing moves HS² above (ε=0.1: 1.355–1.371; ε=T/N: 3.56–3.81, pre-asymptotic until T ≳ 2·10⁵); fixes only the k-truncation; deficit is finite-T zero statistics | [fincinf §7] |
| 21 | MV constant sharpening (P7.1) | **NO effect on 0.6725**: constant lives only in o(1) error; measured sharp norm ≈ 2.5199 < π < 3π/2 | [mvc §0, §4] |
| 22 | P6.5's m₃(1/2) = 2 / m₃(1) = 125/64 | **REFUTED** (corrected: 5, 13/4, 2); parallel-agent bug root-caused (B = 2·J3 and D = 3/(4λ) wrong) | [twbw §2, §6], [tm §4], [v001 7a] |
| 23 | EnclOK | **INCONCLUSIVE — NOT REFUTED**: not independently verifiable (certificate private); downstream chain PROVEN (Lean) and re-checked | [enclok §6] |
| 24 | 256-law regeneration (small-N flag adjudicated) | **BLOCKED at N = 256** (family private; all candidate families infeasible, Chebyshev 6.3–1915); the small-N "contradiction of 0.6725" REFUTED (invalid-config bug; corrected pointwise min p₁ ≥ 0.705 > 0.6725); cumulative-only N=8 dips 0.669–0.687 (MB2.4 nuance, not a refutation) | [rgl §0, §3–§5] |
| 25 | Two-form argument (L8) | **HONEST PROGRESS + OBSTRUCTION**: rank C ≤ N_s PROVEN (unconditional); certificate mechanism verified (295.6/300); direct-sum/second-moment combination OBSTRUCTED (‖C‖²_HS diagonal-dominated); complementarity r = −0.82 (C-failures = close pairs = W's carriers) — explains why the combination is max, not sum | [twoform §0, §3c, §3e] |
| 26 | m₃(1) values, certificate arithmetic, extremal world | **CONFIRMED** (validator reruns) | [v001 7a, 7b, T4] |
| 27 | Dirichlet-family probe | **PASSED (both halves)**: zero-side κ̂ ≈ 4/3 at λ=1 (≤0.04% vs taper prediction); prime-side family average exactly diagonal for X < q (Q_F/D = 1.0000); legality gap λ_single ≈ 0.46–0.54 (empty) vs λ_F ≈ 0.73–0.75 (positive); full theorem CONJECTURED | [dir §0, §6] |
| 28 | PCC I/II read | **NO WALL REOPENS**: unconditional content (Fujii S-moment, GM78 average, GM87 Lemma 9) is in-band; conjecture-in/100%-out only for PCC and AH; the variance side is confirmed, not strengthened | [pcc2 §4] |
| 29 | FG third-moment/twisted-PCC paper | **NO unconditional input at λ ∈ {1/2, 2/3}** (paper's unconditional P³ stops at λ ≤ 1/3); needed values already in-house; twisted F_n documented as the canonical conjectural beyond-1 target (RH-only in-band, RH+HL beyond) | [fg §3, §5] |
| 30 | Selberg-class theorem T | **COMPLETE**: axiomatic degree-one theorem; A–E are corollaries; GL(2) death class-level; no kill found; Lean-izable (low-risk) | [sct §0, §9] |
| 31 | V5 F≡1 support curve | **CONFIRMED**: v*(A) = p₁(A) + 1/(6N²) at every A; bandwidth-2 wall (A ≤ 1.9961, infeasible ≥ 2); M2 reproduces the Remark to ≤1.1%; exact curve needs the private config LP | [f1c §4–§5], [v001 7c] |
| 32 | ξ′ small-t "density hole" | **RESOLVED — artifact**: no zeros of ξ′ on the line in (0, γ₁); exactly one per zeta-zero gap (999/999); the previous agent's 10 small-t roots = ψ-sign bug + θ-Stirling divergence | [xipr §2] |

---

## 2. Open threads ledger (status of every in-flight item)

| Thread | Status | What would close it | Source |
|---|---|---|---|
| **EnclOK** (the ceiling's only non-Lean link) | **OPEN** — not regenerated, not refuted; regeneration blocked on the private family | (1) obtain cert_N256_blk_b128m.json (sha256 cc3de991…); (2) reconstruct family from the LP-dual signature (~244 integer + ~12 half-integer marks, f_c(256) ∈ {53824, 54756}); (3) prove a min-p₁ lower bound valid for off-grid configs (grid bound 3/2−d₁ fails off-grid; Re G(Δ) < 0 on (0.45,1) opens the door) | [enclok §6], [rgl §6] |
| **Small-N marked-LP flag (MB2.4)** | **ADJUDICATED** — the "contradiction" was a buggy generator (Σ marks = N+d); corrected pointwise min p₁ ≥ 0.705 > 0.6725. Genuine residue: cumulative-only N=8 min p₁ 0.669–0.687 (family-dependent upper bound) — is the ceiling an N=256 phenomenon? | lower bound valid off-grid; the authors' family | [rgl §0, §3.2–3.4] |
| **m₄ adjudication (13/4 vs 10/3 vs 346/105 vs 4.64 vs 28/9)** | **UNRESOLVED** — paper claims 13/4 = 3.25 (no derivation in repo); extremal world gives 10/3 (exact arithmetic); third-moment agent's reduction gives 346/105 ≈ 3.2952 (pieces verified, 3D diagram not fully); chem's m4_check diagram converges to ≈ 4.64 (R ≥ 160) — numerically contradicts 13/4; hankel gives extensibility threshold m₄ ≥ 28/9 ≈ 3.111; empirical ≈ 3.07 (finite-height deficit) | direct 3D-diagram integral adjudication (the deciding computation); affects only conditional HL*(4,λ) claims | [tm §4.3], [hankel §5], [chem F4], [nevanlinna §6], [twbw §5.3] |
| **α ≈ 1.0–1.3 arithmetic feature** | **REAL (≥11σ), cause unidentified** — zeta-specific, sample-dependent, present under naive and LS estimators; α=1.10 flips 0.84 → 1.55 between N=3000 and N=10⁴ | τ-bin / prime-power decomposition of the periodogram; height dependence; possible prime-arithmetic origin | [ls §5], [games §639–660] |
| **S₃ probe (V4 moment-capacity: pinning the law's triple correlation)** | **NOT RUN** — the V4 capacity LP (add S₃(j,k) = GUE constraint to the marked-config LP) needs the private configuration family, so it is blocked like EnclOK; the certificate side is insensitive to beyond-1 rows | family recovery (same routes as EnclOK); then record whether pinning S₃ moves the ceiling | [cat1 #5 V4], [rgl] |
| **V20 effective finite-T program** | **NOT EXECUTED** — explicit E(T) companion to the Lean ε-statements | error-chain tracking (Paley–Wiener, Chebyshev, Stirling, MV); validate against finitet numerics; kill if vacuous at feasible T (the cinf pre-asymptotic finding: flat interior needs T ≳ 2·10⁵) | [crossdomain V20], [fin §7], [fincinf §6], [cond §5] |
| **Real-constant audit** | **SETTLED (strict separation)** — 0.6725 is the certified real constant (Thm D, PROVEN); 0.68183 is the law's in-class value, not a real-zero certified fraction; the two claims are distinct and both labeled | — (recorded in [ccg §3]) | [ccg §3], [ceil §1] |
| **Multi-window DPSS (V18 / S2)** | **NOT RUN** — expected no gain (the extremal configuration re-normalizes; oversampling breaks Claim 2.1's Poisson completion); cheap to confirm | one DPSS-multi-window run on W_T; record the ratio | [crossdomain V18], [mlec S2] |
| **Sampling density** | **OPEN, expected-negative** — the certificate's grid density d = λN is the dimension cap; denser in-band sampling doesn't add beyond-1 data (rows near j = N pin the value) | fold into the multi-window probe | [crossdomain V18], [lpdual §3 row sweep] |
| **m₄(λ < 1/2) lane** | **NOT TESTED** — the fourth moment is unconditionally available in RS range kλ < 2 (λ < 1/2 for k = 4), where Prop 7.4 kills the n₊ functional; the DISTINCT-count quartic-weight certificate is untested | derive the admissible quartic weight at λ < 1/2; evaluate against N_d; likely a documented negative ≤ 5/6 | [ceil §3.4], [mvit §4], [tm] |
| **6th-moment (LM1-ADD, Heap–Lindqvist 2024)** | **VERIFY FIRST** — a proven 6th-moment asymptotic = a proven 3-fold additive-correlation main term (the conditional roadmap's strongest input; HL*(k₀,λ) → 13/18 → 1); source NOT in our library | fetch + verify the 6th-moment asymptotic; if real, it feeds the conditional roadmap only | [add LM1-ADD, §466–495] |
| **Derivative tower** | **INTERLACING CHECKED** (one ξ″-zero per ξ′-gap, 20/20; H₂ real); ξ″/ξ‴ certificate constants NOT derived (D₁^(j) machinery is new math, not a corollary) | derive D₁^(2), evaluate κ₁^(2) for flat/quartic; Farmer-style combination over ξ^(j) → distinct-ζ | [xipr §5] |
| **Jensen-ometer probe** | **IN FLIGHT** — 39-paper corpus downloaded (GORZ, Farmer critique 2008.07206, Rodgers–Tao Λ ≥ 0, Polymath, O'Sullivan, CvS spectral truncations); the Farmer critique must be read before any conclusion | read Farmer 2008.07206; decide whether Jensen hyperbolicity (d ≤ 8 proven) bears on the certificate method (expected: no) | [finder-jensen] |
| **Two-form lever: bound on #{‖ζ′(ρ)M(ρ)‖ < θ} from prime data** | **OPEN, no held source** — would turn the r = −0.82 complementarity into an inequality; exactly the shared wall of the mollifier analysis | a bound on the count of small |ζ′M| in terms of pair-correlation/prime data — not in any held paper | [twoform §6], [moll §6] |
| **Box lemma (boxed-class optimum exactly p₀ + \|E(1)\|)** | **ARGUED, NOT WRITTEN** — the only sliver (5.86·10⁻⁴³) between the attained value and the Lean ceiling | write the box lemma as a Lean theorem | [ccg §2] |
| **Admissibility of the paper's cubic at λ < 1** | **OPEN** — 0.8071/0.7593 assume the §7.5(g) Schur–Horn step transfers; either way ≤ 5/6 | transfer proof or counterexample | [twbw §5] |
| **Extremal world's window-B moments** | **OPEN (construction)** — no N_d = 5N/6 configuration known to match the joint two-window data | a rigorous construction or exclusion (new theorem) | [twbw §5] |
| **Selberg-class T Lean-ization** | **PENDING** — suitable, low-risk abstraction layer | the structure type + ζ/L(s,χ) instances | [sct §9] |
| **m₄ = 13/4 provenance** | **UNRESOLVED** — the sequence (1, 4/3, 2, 13/4) is not the extremal world's (10/3); valid Stieltjes sequence but provenance unknown | the m₄ adjudication (above) | [nevanlinna §6], [hankel §5] |
| **G2.6 a.s.-certificate / bankroll target** | **STILL OPEN** — finite-T variance-of-certificate over T-windows; uses in-band F (the pair correlation IS the covariance) | the [P9.1] a.e.-certificate assembly | [games §503, §535] |

---

## 3. Merged surviving vectors (de-duplicated) and scores

**Decision:** which round-3 vectors to fund / sequence, given the pricing-sheet discipline (no negative-priced
input for the simple-fraction certificate; positive-priced or new-target vectors only) and scarce compute.

**Criteria and weights (same as round 2, kept for comparability):** EV 45, Feasibility 25, Epistemic 20,
Compute-cost 10 (5 = cheap). **Weighted = 45·EV + 25·Feas + 20·Epis + 10·Comp.** Status codes:
ALIVE = survives round 2; NEW-TARGET = new object/method family; DOC-NEG = documented negative to record,
not to fund; PRICED-NEG = priced negative (do not fund for the simple cert); BLOCKED = hard input
constraint documented.

| # | Merged vector | Origin(s) | Status | EV | Feas | Epis | Comp | Weighted | One-line justification |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **T-2 — Derivative-tower Farmer-combination** (ξ″/ξ‴ cert + weighted distinct-ζ bound) | [xipr §5]; kernel §4; FGL; Radziwill 1301.3232 | ALIVE / NEW-TARGET | 5 | 2 | 4 | 2 | **375** | Only proven-machinery path to genuinely new constants (ξ′: 0.86864 PROVEN; interlacing CHECKED); ξ″ cert is new math but bounded and checkable; Farmer's 0.6603 distinct-ζ record is the target |
| 2 | **D-1 — Dirichlet-family-averaged theorem** (Rem 7.2(iii)) | [dir]; lf §6 | ALIVE / NEW-TARGET | 5 | 2 | 4 | 2 | **375** | Probe PASSED both halves (zero-side κ̂ ≈ 4/3; prime-side exactly diagonal for X < q); the one unclaimed new theorem with all-PROVEN ingredients; assembly (Gevrey taper, uniformity) is the work |
| 3 | **E-OK — EnclOK / S₃ regeneration closure** | [rgl]; enclok | BLOCKED (input hard) | 4 | 2 | 5 | 4 | **370** | The ceiling's last non-Lean link; three documented routes (cert file, LP-dual family reconstruction, off-grid lower bound); S₃ pinning rides on family recovery; a mismatch would change everything |
| 4 | **V20 — Effective finite-T program** | [crossdomain V20]; fin; fincinf; cond; v001 | ALIVE | 4 | 3 | 4 | 3 | **365** | The only remaining written-theorem deliverable for the real zeros; the cinf pre-asymptotic finding (flat interior needs T ≳ 2·10⁵) makes the outcome honest (possibly documentation-only); ramp cost δ ≈ 0.45·w now quantified |
| 5 | **SCT-L — Selberg-class T Lean-ization** | [sct §9] | ALIVE | 4 | 3 | 4 | 3 | **365** | Guaranteed Lean deliverable consolidating the method; low-risk abstraction layer over existing formalizations |
| 6 | **IPR — spectral-slack diagnostics (C4.1/C4.3)** | [chem C4.1, C4.3]; C6.1 | ALIVE / diagnostic | 3 | 4 | 4 | 5 | **365** | Measures the real spectrum's distance from the crystal (IPR ~ 3/N GUE-like vs O(1) localized) — the cleanest realized-world slack measurement; cheap, existing code |
| 7 | **B1-R — Beyond-1-range conditional-input program** (the only positive-priced input) | [pricing]; m29; fg; pcc2 | ALIVE (CONJECTURED input) | 5 | 1 | 4 | 2 | **350** | dv*/dA = 0.6363/A³ is the only positive price; realistic content = conditional certificates (RH + HL*(k₀,λ) → 13/18; RH + uniform HL via FG Thm 1.9 twisted F_n) + the α≈1.1 feature as empirical hint; M29 keeps the unconditional side dead |
| 8 | **M4 — m₄(λ<1/2) lane + m₄(1) adjudication** | [tm §4.3]; hankel §5; chem C4.2; twbw §5.3 | ALIVE / loose-end | 3 | 3 | 4 | 4 | **330** | Adjudicate 13/4 vs 10/3 vs 346/105 vs 4.64 vs 28/9 (direct 3D diagram is the decider); then the untested λ<1/2 quartic-weight DISTINCT certificate (RS range kλ<2); expected ≤ 5/6 but untested and cheap |
| 9 | **6M — 6th-moment literature verification (LM1-ADD)** | [add LM1-ADD] | ALIVE / verify | 4 | 2 | 3 | 4 | **330** | A verified 6th-moment asymptotic = 3-fold additive-correlation main term (the conditional roadmap's strongest input); source not in library — verify first, then it feeds the conditional line only |
| 10 | **A1.1 — α≈1.0–1.3 arithmetic feature follow-up** | [ls §5]; games; hot | ALIVE / diagnostic | 3 | 3 | 4 | 3 | **320** | The one unexplained REAL empirical deviation near the beyond-1 boundary (≥11σ, both estimators); τ-bin/prime decomposition + height dependence is mechanical and could surface a prime-arithmetic origin |
| 11 | **TF-1 — two-form lever #{small \|ζ′M\|}** | [twoform §6] | ALIVE (no source) | 4 | 1 | 3 | 3 | **295** | Would turn the r = −0.82 complementarity into an inequality; the bound is not in any held source and is the shared mollifier wall — low probability, huge value if found |
| 12 | **MW — Multi-window DPSS probe (V18/S2)** | [crossdomain V18]; mlec S2 | ALIVE / expected-negative | 2 | 4 | 3 | 4 | **290** | Cheap confirm that the extremal configuration re-normalizes (ratio unchanged); one run settles it |
| 13 | **JEN — Jensen-ometer probe** | [finder-jensen] | IN FLIGHT | 2 | 3 | 3 | 4 | **265** | Corpus in hand; Farmer's critique (2008.07206) must be read first; expected no bearing on the certificate method |
| 14 | **C1.2 — isospectral/switching classification** | [chem C1.2] | ALIVE / diagnostic | 2 | 3 | 3 | 4 | **265** | Answers "which worlds are spectrally identical at (tr, ‖·‖²)"; any switching-breaking provable input moves the wall — but no such input is known |
| 15 | **Groskin tail-budget certification (G6-adjacent)** | [cvs §7] | ALIVE (horizontal) | 2 | 3 | 3 | 3 | **255** | The actually-useful Weil-positivity certification rule (Cor 3.3); RH-horizontal, produces no proportion bound — track, don't fund for P1 |
| 16 | **PCC-II HMH template** | [pcc2 §5.4] | ALIVE (conditional template) | 2 | 2 | 3 | 4 | **240** | "Average pair correlation ⟹ 100% simple+critical without RH" is a template; any future unconditional N^⊛(T) control converts directly; conjecture-in/100%-out only |
| 17 | **m₃ for simple cert (V3-lane)** | [pricing §3]; tm; twbw | **PRICED-NEG** | — | — | — | — | — | −1/3 per unit m₃, caps v* at 2/3; likely-DEAD; do not fund (documented negative) |
| 18 | **m₃ for distinct cert** | [pricing §3]; twbw §3.2 | **PRICED-NEG (neutral)** | — | — | — | — | — | 5/6 at m₃ = 2; only an upper bound m₃ < 2 helps; none exists (5, 13/4 ≥ 2); re-fund only via a new mechanism (admissible-cubic transfer to λ < 1) |
| 19 | **min-gap / repulsion for P1** | [pricing §4]; f1c | **PRICED-NEG** | — | — | — | — | — | −0.1799 step at X = 0⁺ (Parseval floor 0.50195); negative even if proven; retires P1.4's "repulsion breaks the ceiling" hope |
| 20 | **Individual GL(2) transport** | [lf §4–§5] | **DEAD** | — | — | — | — | — | dimension ceiling Λ* = 1/2; certificate empty; even PCC doesn't move it |
| 21 | **CvS import** | [cvs §6] | **DEAD** | — | — | — | — | — | B1/B2/B3, each sufficient; even RH doesn't move the ceiling |
| 22 | **QI/control sweeps** | [qi §5]; mu §4 | **DEAD** | — | — | — | — | — | no inequality on the data budget beats Lemma 3.2 |
| 23 | **Beyond-1 variance / distributional** | [gmvar]; selclt | **DEAD** | — | — | — | — | — | variance orthogonal; p₀-family defeats any fluctuation certificate |
| 24 | **M29 beyond-1 mean** | [m29] | **DEAD** | — | — | — | — | — | documented negative, PROVEN; only conjectural values clear the tolerance |
| 25 | **Beat 0.6818 by the same class** | [ccg]; ceil; lpdual | **DEAD** | — | — | — | — | — | in-class optimum attained (r = 1−x); ceiling TIGHT; only p₁ moves v |
| 26 | **Better window for ζ** | [kernel §5]; cond | **DEAD** | — | — | — | — | — | cosine global minimizer; constant robust; only the boundary ramp costs (δ ≈ 0.45·w, keep at resolution scale) |
| 27 | **Mollifier fusion** | [moll §6] | **DEAD** | — | — | — | — | — | same prime-pair wall; fusion point already inside the paper |
| 28 | **K–H triple bound** | [kh §6] | **DEAD** | — | — | — | — | — | tautology; wrong object (multiplicity vs connected moment) |
| 29 | **A1–A5 (round-1 deaths)** | [cat1 §4]; m29 re-confirms | **DEAD** | — | — | — | — | — | documented; do not re-derive |
| 30 | **Empirical beyond-1 trend / α=1 spike** | [hot §5] | **DEAD (as evidence)** | — | — | — | — | — | estimator artifact; the α≈1.1 feature is the real residue (vector #8) |

**Sense-check:** the ranking matches the strategic state — after the in-class closure, the top of the list is
dominated by (i) new-target vectors with proven machinery (derivative tower, Dirichlet family, Selberg T),
(ii) the only positive-priced input as a conditional program, and (iii) the last non-Lean link (EnclOK).
The pricing discipline's effect is visible: the two m₃ lanes and min-gap are pushed off the fundable list
despite their historic prominence, because round 2 priced them negative. The diagnostics (IPR, α≈1.1) rank
high on cheapness and epistemic value — correct, since the program's "run only what changes belief" rule
favors them. Nothing in the model contradicts the executioner verdicts; where the weighted total disagrees
with intuition (e.g. #1/#2 at feasibility 2), the briefs state the caveat.

---

## 4. TOP 10 for Round 3 — ready-to-paste briefs

Each brief: **goal / why it matters / inputs / method / labels / definition of done.** The task-mandated
vectors are (a) V20-effective, (b) S₃/regeneration EnclOK, (c) m₄(λ<1/2), (d) derivative-tower
Farmer-combination, (e) beyond-1-range pricing, (f) the surviving new-target vectors (Dirichlet family,
Selberg T, and the new-target diagnostics).

---

### #1. T-2 — Derivative-tower Farmer-combination (ξ″, ξ‴, …, weighted distinct-ζ bound) [task (d), (f)]
- **Goal:** derive the ξ″ certificate constant (κ₁^(2)(λ,v) via the D₁^(2) pair density), then assemble a
  Farmer-style weighted combination over ξ^(j) toward a distinct-ζ bound beating 0.6603.
- **Why it matters:** the only proven-machinery route to genuinely new constants. ξ′ constants are PROVEN
  in Lean (0.85838 flat / 0.86864 quartic simple∧on-line; 0.92919 / 0.93432 distinct) and numerically
  reproducible at 50 digits (κ₁(1,flat) = 1.1416159452…, κ₁(1,quartic) = 1.1313594848…) [xipr §3–§4]; the
  interlacing is CHECKED at 60 digits (one ξ″-zero in every ξ′-gap including (0, u₁), 20/20; H₂(t) = −ξ″ real)
  [xipr §5]; Farmer's combination is the paper's own history (Farmer 1995: N^d(ζ) > 0.6395; Wu: 0.6603)
  [xipr §5]. The ζ-optimal cosine is NOT optimal for ξ′ (κ₁(1,cos) = 1.1321 > κ₁(1,quartic)) [xipr §3] — the
  tower needs its own window optimization.
- **Inputs:** `Zeta23/XiPrime/` (D₁ series, D1coeff(k) = 2·4^{k+1}·k!/(2k+2)!, Λ⋆ = l/2 + iπ/4) [xipr §3, §5];
  `tools/xiprime_check/` (60-digit mpmath machinery); FGL 0803.0425; Radziwill 1301.3232 (Farmer–Ki settled:
  ζ′-zeros near the line ⟺ small gaps) [finder-001 #52].
- **Method:** (1) derive D₁^(2) (the ξ″-analog density: new coefficient shifts, NOT a corollary) [xipr §5];
  (2) evaluate κ₁^(2)(1,v) for flat / quartic / optimized windows at 50 digits; (3) if the constant is
  competitive (κ₁^(2) ≈ 1.13–1.14), formalize the ξ″ certificate; (4) assemble the Farmer combination with
  the interlacing counts (one ξ^(j+1)-zero per ξ^(j)-gap, i.e. the tower is self-reinforcing: each step's
  certificate supplies the next step's simplicity) toward a distinct-ζ bound > 0.6603.
- **Labels:** ξ′ constants PROVEN (Lean) + CHECKED NUMERICALLY; interlacing CHECKED NUMERICALLY; the D₁^(j)
  extension and the Farmer weights CONJECTURED (new math); kill if κ₁^(2) ≥ κ₁^(1) (constants decrease with j).
- **Definition of done:** (a) a numerically-evaluated ξ″ certificate constant with the same machinery; if >
  0.86864 → Lean-ize; (b) a written Farmer-combination statement with a concrete distinct-ζ bound > 0.6603,
  or the documented obstruction (weights don't assemble / D₁^(2) degenerates).

### #2. D-1 — Dirichlet-family-averaged theorem (C Rem 7.2(iii)) [task (f)]
- **Goal:** make Rem 7.2(iii) rigorous: proportion ≥ 2/3 − o(1) of a Dirichlet-character family's zeros on
  the line, q → ∞, T = (log q)^c.
- **Why it matters:** the one unclaimed new theorem with all-PROVEN ingredients; the probe PASSED both
  halves — zero-side κ̂ ≈ 4/3 at λ=1 for primitive even characters mod q (q = 5..40, window [2000,4000],
  ≤0.04% vs the taper-corrected prime-side prediction), prime-side family average exactly diagonal for
  X < q (Q_F/D = 1.0000 to machine precision; single-character ratio fluctuates 0.2–5.0), legality gap
  λ_single ≈ 0.46–0.54 (empty certificate, ≤ 3−√6) vs λ_F ≈ 0.73–0.75 (positive, → 1 as q → ∞) [dir §0, §3–§5].
- **Inputs:** `research/notes/dirichlet-family-exp/` (Rust: characters, EM Hurwitz zeta, Z_χ zero-finder,
  HS-norm, orthogonality); C Prop 4.2 (Gevrey taper — the paper's own open item); C Lemma 3.2 (block-diagonal
  linearity); RvM for L(s,χ).
- **Method:** (1) push the q-aspect numerics to q ~ 10³–10⁴ at T = (log q)² and (log q)³ (sample of
  characters; κ̂_F(λ_F) → 4/3, H(λ_F) → 2/3 as q grows); (2) write the formal family-level argument: block
  matrix ⊕_χ Ĝ_χ, Lemma 3.2 with tr ⊕ = Σ tr, ‖·‖² = Σ ‖·‖², and the Gevrey-taper Prop 4.2 for the family;
  (3) hand the family-averaged analytic evaluation to a Lean check; (4) only then the GL(2) weight-aspect
  stretch target.
- **Labels:** per-character Theorem E PROVEN (C); orthogonality PROVEN (classical, verified exactly); the
  assembly CONJECTURED (Gevrey taper + uniformity); GL(2) leg CONJECTURED (Petersson/Kuznetsov).
- **Definition of done:** the written family-averaged theorem (or the documented taper obstruction), with
  q-aspect numerics to 10³–10⁴ on record; Lean-ization if the assembly survives.

### #3. E-OK — EnclOK / S₃ regeneration closure [task (b)]
- **Goal:** close the ceiling's last non-Lean link (EnclOK) — or document all three routes exhausted — and,
  if the family is recovered, run the S₃ probe (V4's moment-capacity question).
- **Why it matters:** EnclOK is the SINGLE displayed hypothesis of the 0.68185 ceiling; a regeneration match
  makes the ceiling fully Lean; a mismatch collapses it (that is the one live way the ceiling could be
  wrong) [ceil §4, enclok §6]. The blocker is documented and precise: the authors' configuration family is
  private (cert_N256_blk_b128m.json), and every reconstructed family is infeasible at N = 256 (Chebyshev
  distance 6.3–1915) [rgl §4]. The S₃ probe (would pinning S₃(j,k) = GUE move the ceiling?) is V4's question
  and rides on the same family [cat1 #5].
- **Inputs:** `tools/regen_law/` (LP machinery, valid families); `tools/verify_enclok.py`; the LP-dual
  signature (≈244 integer + ≈12 half-integer marks; f_c(256) ∈ {53824, 54756}) [rgl §6]; the off-grid
  lower-bound question (Re G(Δ) < 0 on (0.45, 1)) [rgl §3.4].
- **Method (routes in priority):** (1) obtain cert_N256_blk_b128m.json (external correspondence — minutes of
  compute once in hand, per the enclok recipe); (2) reconstruct the family from the LP-dual structure seeded
  by the marks signature; (3) prove a min-p₁ lower bound valid for off-grid configurations (genuine open
  math). If any route yields the family: recompute S(j) at ≥45 digits, verify the 256 enclosures, re-run
  checkRows; then add the S₃ = GUE constraint to the config LP and record whether the ceiling moves.
- **Labels:** EnclOK INCONCLUSIVE-not-refuted [enclok]; the blocker HARD (distribution decision) [rgl §5];
  the off-grid lower bound OPEN.
- **Definition of done:** EnclOK resolved to CHECKED NUMERICALLY (independent regeneration) or REFUTED, or
  all three routes documented exhausted with the blocker standing; S₃ price recorded if the family is in
  hand (a V4 capacity point).

### #4. V20 — Effective finite-T version of the 67.25% theorem [task (a)]
- **Goal:** produce the explicit effective statement "≥ 0.6725·N(T,2T) − E(T)" with a written, numerically
  validated E(T), and the honest verdict on where it is non-vacuous.
- **Why it matters:** the only remaining written-theorem deliverable for the REAL zeros (the Lean statements
  are ε-asymptotic; the computational-RH data goes to 10¹³) [crossdomain V20]. Round 2 sharpened the inputs
  it needs: the boundary-ramp cost is exactly linear (δ ≈ 0.45·w; O(1/L) if the ramp is at the resolution
  scale) [cond §4]; the paper-realistic χ-smoothed kernel is PRE-ASYMPTOTIC until T ≳ 2·10⁵ (the flat
  interior needs ε < 1/2 ⟺ T/N < 1/2), so the effective theorem's non-vacuous range is itself a finding
  [fincinf §6]; the validator's honest label on the finite-T overshoot (Δ > 0 at all measured T; decay law
  indeterminate — all fitted asymptotes nonzero) [v001 T3].
- **Inputs:** the error chain of N Lemma 3.3 (Paley–Wiener, Chebyshev–Mertens, Stirling, MV) [cat1 #3 L1,
  mvc §1]; `tools/finitet` numerics (bound/N = 0.705–0.719 over T = 100–1300) [fin §3, sandbox §3,
  detthr §3]; the cinf smoothing tables [fincinf §4]; the conditioning ramp table [cond §4].
- **Method:** track the constants through Lemma 3.3's error terms (each is PROVEN: Paley–Wiener O(1/K),
  Chebyshev ΣΛ² ≪ x log x, Stirling, MV o(1)), assemble an explicit E(T) (including the ramp cost 0.45·w
  at the resolution scale), validate against the finitet measurements at T = 10³–10⁶, and write the "dating"
  section: where does 0.6725 first become visible?
- **Labels:** all ingredients PROVEN; the assembly is NEW; the outcome (non-vacuous vs documentation-only)
  is OPEN until assembled — the cinf finding makes "vacuous at feasible T" the likely branch, which is a
  documented result, not a failure [fincinf §6, crossdomain V20 kill].
- **Definition of done:** a written effective theorem with explicit E(T), a validation table against the
  finitet data, and the verdict (non-vacuous range identified, or the documentation-only conclusion with the
  precise T threshold).

### #5. SCT-L — Selberg-class T Lean-ization
- **Goal:** formalize the axiomatic degree-one theorem T (whose corollaries are Thms A–E) in Lean.
- **Why it matters:** a guaranteed Lean deliverable that consolidates the whole method into one statement and
  surfaces any axiom the method silently exploits [cat1 #10]; the GL(2) death becomes a class-level statement
  [lf §4, sct §0]; the adversarial audit found no kill [sct §0].
- **Inputs:** selberg-class-theorem.md (axioms A1–A5, proof assembly, corollaries); the existing
  zeta-23-lean modules (the analytic inputs are formalized for ζ and L(s,χ); the linear algebra is
  separate) [sct §9].
- **Method:** build the abstraction layer (a structure type carrying A1–A5 + ζ/L(s,χ) instances); derive
  Thms A–E as instances; record the class-level GL(2) bandwidth-1/2 statement.
- **Labels:** T WRITTEN (CONJECTURED as an axiomatization, PROVEN ingredients); Lean-ization LOW-RISK per
  the audit [sct §9].
- **Definition of done:** the Lean structure + A–E instances compile; the axiom-ingredient map and the
  GL(2) corollary recorded.

### #6. IPR — spectral-slack diagnostics (C4.1/C4.3, C6.1)
- **Goal:** measure the real spectrum's distance from the crystal via eigenvector participation ratios.
- **Why it matters:** the cleanest realized-world slack measurement — the crystal's eigenvectors are
  delta-localized (IPR ~ O(1)), GUE bulk eigenvectors have IPR ~ 3/N; where W_T's spectrum sits tells us
  whether the 0.6818 ceiling is "far from tight" in the realized world (delocalized ⇒ real slack exists)
  [chem C4.1]; the energy-resolved IPR asks whether there is a mobility edge (two-phase spectrum) [chem C4.3];
  the localized-fraction scaling (n₋/N vs T) is the off-line-rate readout [chem C6.1].
- **Inputs:** `tools/finitet` W_T spectra; the sandbox harness.
- **Method:** IPR of each eigenvector of W_T at T = 200–600; compare with 3/N and O(1); plot IPR(λ);
  n₋/N scaling.
- **Labels:** measurement, CHECKED NUMERICALLY by construction; interpretation CONJECTURED.
- **Definition of done:** a table + interpretation (delocalized ⇒ the ceiling is not tight in the realized
  world — redirects toward new targets; crystal-like ⇒ the realized world sits near the extremal law).

### #7. B1-R — Beyond-1-range conditional-input program (the only positive-priced input) [task (e)]
- **Goal:** convert the pricing sheet's one positive price (dv*/dA = 0.6363/A³ for F ≡ 1 on [1, 1+ε]) into a
  written CONDITIONAL certificate program: "under RH + HL*(k₀,λ): ≥ 13/18; under RH + uniform HL: the
  roadmap 0.70/0.80/0.90 at supports 1.04/1.26/1.70", with the FG twisted pair-correlation F_n as the
  canonical conjectural target [fg §5–§6].
- **Why it matters:** every unconditional route past 0.6725 is PROVEN dead (M29: 3.6·10³–3.7·10⁴× over
  tolerance) [m29]; the only inputs with positive price are VALUES (HL / Montgomery-PCC), all conjectural
  [pricing §5, §8]. A documented conditional result is still a result (hooks/agents.md); and the FG paper is
  the first rigorous treatment of the exact additive-correlation object the ceiling names as the only
  documented route [fg §5, ceil §4]. The α ≈ 1.0–1.3 arithmetic feature (≥11σ, both estimators, cause
  unidentified) is the empirical hint that something real lives near the boundary [ls §5].
- **Inputs:** the pricing sheet + M2/M3 models [pricing]; FG Prop 1.7 (F_n under RH, in-band) + Thm 1.9
  (smoothed F_n under RH + uniform HL, beyond 1) [fg §1.3]; PCC II's HMH template (conjecture-in /
  100%-out) [pcc2 §5.4]; the M2 curve p₁(A) = 1 − (1−p₀)/A² [f1c §4].
- **Method:** (1) assemble the certificate at bandwidth A with the pricing sheet's shadow-price bookkeeping
  (v* = p₁(A) + |E(1)|, price per unit bandwidth 0.6363/A³); (2) write the conditional statement with
  hypotheses stated explicitly (RH + uniform HL, or RH + Conj 1.5/1.8) — a legitimate, labeled conditional
  result; (3) record F_n + Conj 1.5 in the literature map as the canonical conjectural beyond-1 target;
  (4) the 6th-moment verification (#6M, LM1-ADD) feeds this lane if it survives [add LM1-ADD].
- **Labels:** the prices and the M2 reproduction are CHECKED NUMERICALLY / PROVEN [pricing §8]; the
  conditional theorems are PROVEN-as-stated under their hypotheses (FG) [fg]; the input F(α) beyond 1 is
  CONJECTURED; M29's unconditional negative stands PROVEN [m29].
- **Definition of done:** a written conditional-input certificate (≥ 13/18 under HL*(4,λ); the 0.70/0.80/0.90
  roadmap under F ≡ 1 on [1, A] with A = 1.04/1.26/1.70), each with its hypothesis set and the pricing
  attribution; plus a status paragraph on the FG twisted route (the strongest documented conditional
  statement in the library).

### #8. M4 — m₄(λ<1/2) lane + m₄(1) adjudication [task (c)]
- **Goal:** (1) pin m₄(1) among the competing values; (2) evaluate the quartic-weight (m⁴) DISTINCT-count
  certificate at λ < 1/2.
- **Why it matters:** m₄ is the structural lever the moment machinery points to — the third moment carries
  zero separation power (m₃ = 2 for both worlds), the separation shows up at the FOURTH moment or at m₀
  [hankel §0, §4]; the paper's HL*(4,λ) → 13/18 roadmap is conditional on the m₄ value [mvit §4, ceil §3.8];
  and the current m₄ status is four-way contested: 13/4 (paper, no derivation in repo), 346/105 (third-moment
  reduction, pieces verified) [tm §4.3], 4.64 (chem's converged diagram — numerically contradicts 13/4)
  [chem F4], 10/3 (extremal world, exact) [hankel §5], with the extensibility threshold m₄ ≥ 28/9 [hankel §5]
  and empirical ≈ 3.07 (finite-height deficit) [hankel §6]. At λ < 1/2 the fourth moment is unconditionally
  available (RS range kλ < 2), where Prop 7.4 kills the n₊ functional but the DISTINCT functional is
  untested [ceil §3.4].
- **Inputs:** `tools/m4_check.py`, `tools/m4_adjudicate.py`, `tools/m4_pieces.py`, `tools/hankel_test_cbt3.py`;
  the λ<1/2 Gram-moment machinery [tm]; the admissible-quartic weight template (§7.5(g) pattern).
- **Method:** (1) run the direct 3D-diagram integral at 60 digits (the decider for 13/4 vs 346/105 vs 4.64),
  cross-checked against the sine-process Monte Carlo (L=60: m₄ = 3.165 ± 0.024 raw) [tm §4.3] and the hankel
  threshold; (2) derive the admissible quartic weight at λ < 1/2 (Schur–Horn admissibility, the same
  structure that bounds the cubic LP [twbw §3.3]) and evaluate N_d.
- **Labels:** 10/3 and 28/9 PROVEN (exact arithmetic); 13/4 = paper-value, UNVERIFIED in-repo; 346/105
  piece-verified; 4.64 computed but not adversarially validated [chem F4]; the λ<1/2 quartic certificate
  CONJECTURED (expected ≤ 5/6 — a documented negative would be the honest outcome).
- **Definition of done:** m₄(1) pinned with a code-backed verdict (one value survives adversarial
  re-derivation, with the others' status recorded); the λ<1/2 quartic distinct certificate value recorded
  with its admissibility argument (likely ≤ 5/6, documented).

### #9. 6M — 6th-moment literature verification (LM1-ADD) [+ MW — multi-window DPSS probe (V18/S2), cheap slot]
- **Goal (6M):** verify the Heap–Lindqvist 2024 sixth-moment asymptotic (the source is NOT in our library);
  if verified, record it as the strongest input of the conditional roadmap (a proven 6th-moment = a proven
  3-fold additive-correlation main term, feeding HL*(k₀,λ) → 13/18 → 1) [add LM1-ADD].
- **Goal (MW):** settle the multi-window question with one DPSS run — expected no gain (the extremal
  configuration re-normalizes; oversampling breaks Claim 2.1's Poisson completion) [crossdomain V18, mlec S2].
- **Why it matters:** both are cheap and each changes belief on a live question: 6M decides whether the
  strongest conditional input exists; MW closes the "maybe a second window helps" branch for good.
- **Inputs:** the Heap–Lindqvist paper (fetch); `tools/finitet` + DPSS windows.
- **Method:** fetch + read + numerical consistency check of the 6th-moment asymptotic; one DPSS multi-window
  run on W_T with the ratio recorded.
- **Labels:** both CONJECTURED until run; the MW outcome is expected-negative.
- **Definition of done:** a verified/unverifiable verdict on the 6th-moment claim; a recorded multi-window
  ratio (or the documented reason the probe is vacuous).

### #10. A1.1 — α≈1.0–1.3 arithmetic feature follow-up (G3.1 R-4)
- **Goal:** decompose the real, unexplained empirical feature near α = 1 (spike at 1.00, dip at 1.05, spike
  at 1.10; ≥11σ under both the naive and LS estimators; cause unidentified).
- **Why it matters:** the one genuine empirical deviation at the boundary of the beyond-1 region — the only
  place near α > 1 where real data differs from the GUE null (G3.1 established everything else beyond 1 is
  noise) [hot §5]; if it has a prime-arithmetic origin it is a publishable diagnostic and a hint for the
  beyond-1 lane; if it is a Gram-point/lattice artifact of the θ-unfolding at specific rational α, that is
  a documented negative [ls §5, hot §4].
- **Inputs:** `tools/hot_hand_calib.py`, `tools/attack_ls_estimator.py`, `tools/data/zeros_computed_10000.txt`.
- **Method:** τ-bin / prime-power decomposition of the periodogram at α ∈ {1.00, 1.05, 1.10}; height
  dependence (block 1000-zero windows at increasing heights); compare against the GUE null with the same
  unfolding; test the Gram-lattice hypothesis (x_j − j deviations).
- **Labels:** the feature itself CHECKED NUMERICALLY (≥11σ, both estimators) [ls §5]; the cause OPEN.
- **Definition of done:** a written decomposition: either a prime-arithmetic origin identified (finding), or
  a lattice/unfolding artifact pinned (documented negative), with the height dependence on record.

---

## 5. Kill ledger — everything priced/dead, with source (do not re-derive, do not re-fund for the simple cert)

| Vector | Death (one line) | Source |
|---|---|---|
| Beat 0.6818 unconditionally by the same certificate class | In-class optimum ATTAINED (r = 1−x, exact rational); ceiling TIGHT to ~7.8·10⁻⁴³; only p₁ moves v (shadow price 1) | [ccg §2], [lpdual §5] |
| Better window for ζ (beat 0.6725) | Cosine is the unique global minimizer of Q (validator-corrected λ_min = 0.797); 1% perturbations cost ≤0.02%; candidates with c > 1/2 violate bandwidth | [kernel §5], [v001 T2], [cond] |
| m₃ ≥ 2 as simple-fraction input | NEGATIVE price (−1/3 per unit; m₃ = 4−3p₁ caps p₁ ≤ 2/3); likely-DEAD (values 5, 13/4 ≥ 2; §7.5(e)) | [pricing §3], [twbw], [tm] |
| m₃ as distinct-count input | neutral (5/6) at m₃ = 2; only an upper bound m₃ < 2 helps; none exists; re-fund only via a new mechanism | [pricing §3], [twbw §3.2] |
| Min-gap / repulsion for P1 | NEGATIVE even if proven (−0.1799 step; Parseval floor p₁ = 0.50195); the law's p₀ is paid for by coincidences | [pricing §4], [f1c §4] |
| Beyond-1 mean (M29) | PROVEN negative: MV bound 3.6·10³–3.7·10⁴× over tolerance, grows T^ε/poly(log T); only conjectural values clear it | [m29] |
| Beyond-1 variance (B10) | DEAD: dictionary inverted (beyond-1 ⟺ short windows U < 1/ρ); no unconditional variance at α > 1; variance orthogonal to the certificate | [gmvar §2, §4, §6] |
| Distributional / fluctuation certificate (V13) | DEAD-consistent-with-walls: p₀-family realizes every proven fluctuation input; v ≤ p₀ + \|E(1)\| + o(1) survives | [selclt §3, §6] |
| Individual GL(2) transport | dimension ceiling Λ* = 1/2; certificate empty; even PCC doesn't move it | [lf §4–§5] |
| Mollifier fusion | same prime-pair wall; the only fusion point is already inside the paper (§7.5(c)) | [moll §6] |
| QI inequalities vs Lemma 3.2 | NO: CS refinement (L′) strictly stronger pointwise, zero uniform gain (vanishes at sharp configs) | [qi §5] |
| Control inequalities vs Lemma 3.2 | NO: Glover/Perron/Ostrowski–Schneider/D-μ all fail; two-layer class-level argument | [mu §4] |
| K–H triple bound as P2 input | RESTATEMENT: det ≥ 0 tautology; weaker than trivial bounds; admissible m₃ range excludes nothing; A3(1) = 0 | [kh §6] |
| CvS import (G1/G6) | DEAD: B1 (object mismatch, cocycle fails by O(1)), B2 (hypothesis gap), B3 (orthogonality — even RH doesn't move the ceiling) | [cvs §6] |
| Integrality closes the in-class gap | NO: the 256-law is integer-marked and satisfies m₂ = 2−p₀; the gap is a second-moment gap | [nevanlinna §4–§5] |
| MV constant sharpening (P7.1) | no effect: 3π/2 lives only in o(1) error; measured norm ≈ 2.52 < π | [mvc §0, §4] |
| C∞-smoothing pulls HS² toward 1.3275 | NO: moves above (pre-asymptotic until T ≳ 2·10⁵); only the k-truncation is fixed | [fincinf §7] |
| "0.6725 → 0.68+ by sharper error constants" | no: the certificate value is 2−1/c₁* with no Hilbert/MV constant in its derivation | [mvc §4] |
| Empirical beyond-1 trend / α=1 spike | ARTIFACT (Exp(1) noise floor; Gram-lattice unfolding artifact); no hint against Montgomery | [hot §5] |
| LS estimator bias-cancellation (B1) | no gain on the sharp window; equal bias, 1.2–2.5× worse variance | [ls §4] |
| A1–A5 (round-1 deaths) | documented; M29 re-confirms A5 quantitatively | [cat1 §4], [m29 §4] |
| "small-N near-CUE law contradicts 0.6725" | REFUTED: invalid-config bug; corrected pointwise min p₁ ≥ 0.705; cumulative-only N=8 nuance is not a refutation (category error) | [rgl §0, §3.3] |
| "PCC II reopens M29/B10" | NO: unconditional content is in-band; conjecture-in/100%-out only | [pcc2 §4] |
| "FG paper gives unconditional m₃ at λ ∈ {1/2, 2/3}" | NO: unconditional content stops at λ ≤ 1/3; needed values already in-house; twisted route conditional only | [fg §3, §5] |
| "α=1 spike is Montgomery evidence" | NO: unfolding artifact, one bin wide, grows with N | [hot §4] |
| Two-form direct-sum / second-moment combination | OBSTRUCTED: ‖C‖²_HS diagonal-dominated (80%); the carrier is the first-moment direction | [twoform §3c] |
| "The 2/3 is a method cap" (V7 dichotomy) | FALSE: the certificate saturates ≈0.977 on the lattice; 2/3 is the realized pair-correlation arithmetic | [sandbox §4], [ihara §6] |

---

## 6. Strategic reading and allocation (s4h-strategy-terrain + resource-allocation)

**Terrain — fund vs avoid in round 3:**
- **Fund (in rank order):** T-2 derivative tower, D-1 Dirichlet family, V20 effective, B1-R beyond-1
  conditional program, E-OK EnclOK/S₃ closure, M4 m₄ lane, SCT-L Selberg Lean-ization, A1.1 α≈1.1 feature,
  IPR diagnostics, the 6M + MW cheap slots.
- **Avoid re-fighting:** the window (kernel/cond), the ceiling (except adversarially via E-OK), the two-moment
  walls (except via new targets), the third moment for the simple cert, min-gap, CvS, the QI/control sweeps,
  the variance/distributional flanks, individual GL(2), mollifier fusion, all A1–A5.
- **Do not fund for the simple-fraction certificate:** any vector whose input the pricing sheet prices
  negative (m₃, min-gap) — documented negatives with exact prices stand until a NEW mechanism appears
  [pricing §7–§8].

**Allocation (compute-poor machine; CPU-bound → Rust; cache; run only what changes belief):**

| Claim | Allocation | Trade-off (what it gives up) |
|---|---|---|
| T-2 derivative tower | 1st | Highest EV new-target; gives up a guaranteed constant for a bounded derivation risk (kill if κ₁^(2) ≥ κ₁^(1)) |
| D-1 Dirichlet family | parallel slot | q-aspect numerics to 10³–10⁴ are Rust-cheap; gives up immediate Lean work for the assembly risk |
| V20 effective | 2nd (writing-heavy) | The guaranteed deliverable; gives up speed for completeness — likely documentation-only branch is honest |
| E-OK EnclOK/S₃ | any time | ~1-hour LP runs per family route; low marginal compute; if the cert file is obtainable it is minutes |
| B1-R beyond-1 conditional | after the α≈1.1 probe | Conditional results are cheap to write; the α≈1.1 feature may sharpen the empirical case |
| M4 m₄ lane | cheap slot | adjudication is 1–2 h; the λ<1/2 quartic cert is bounded derivation |
| SCT-L / A1.1 / IPR / 6M / MW | paper-hunting / low-compute downtime | reading-and-writing heavy or single runs |

**Force economy (three rules):** (1) never run a computation that does not change what we believe
(hooks/agents.md); (2) prefer Rust and cached data; (3) a clean negative is a deliverable — the pricing
sheet's m₃/min-gap lines are now priced, so any future proof of such an input slots in at its stated price
without re-running the analysis [pricing §9].

**Victory definition for round 3:** at least one of — a derived ξ″ certificate constant (Lean-izable) or a
Farmer-combination bound > 0.6603 (T-2); the written Dirichlet-family theorem (D-1); the written effective
E(T) with its non-vacuity verdict (V20); EnclOK resolved by regeneration or all routes documented (E-OK);
m₄(1) pinned and the λ<1/2 quartic cert valued (M4); the α≈1.1 feature decomposed (A1.1). Each is a genuine
research result under the program's operative targets.

---

## 7. Honesty footer

- Every PROVEN / DEAD / OPEN claim above traces to a round-2 file cited in brackets; nothing was re-derived
  here. The two facts carried verbatim from the sources with their caveats: (i) the 0.6818 ceiling is
  Lean-proven modulo EnclOK, which is INCONCLUSIVE-not-refuted (authors' certificate private; regeneration
  blocked with three documented routes) [enclok, rgl]; (ii) m₄(1) is UNRESOLVED among 13/4, 10/3, 346/105,
  4.64, 28/9 — the 13/4 conditional-roadmap value is NOT independently verified in this project [tm §4.3,
  hankel §5, chem F4].
- All scores, weighted totals, rankings, and allocations are CONJECTURED (synthesizer judgment), a proposal
  for the round-3 planner, to be challenged by the VALIDATOR. The prices themselves (pricing sheet) are
  PROVEN / CHECKED NUMERICALLY and are not judgment.
- Deliberately NOT included: any claim that any vector "probably settles RH". Every funded vector is scoped
  to a rigorous, adversarial-validated increment; the search persists (hooks/agents.md), and every negative
  here is a documented result with its source, not a reason to stop.
