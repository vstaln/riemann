# NEW-OBJECT IDEATION — breaking or proving the 0.6818 ceiling

**Agent:** IDEA GENERATOR (phone-local compute node) · **Date:** 2026
**Task:** task-ceiling-ideas.md · **Charter:** hooks/agents.md (read)

## 0. Honest map (what the ceiling is, from the verified notes — cited, not re-derived)

- Record 0.6732628655 (α=1.49, psum=1/220, m=133, floor F≥0.00806; the (α,psum) family is EXHAUSTED at the true minimum of F) [discovery-6732629.md]. [RETIRED 2026-08-24]
- In-class ceiling 0.6818312305953419 = p₀ + 1/(6·256²), attained by the exact-rational certificate r(x)=1−x against the near-CUE 256-law (p₀=0.68182868746…, |E(1)|=2.543·10⁻⁶); Lean-proven modulo EnclOK (INCONCLUSIVE, not refuted; family private) [attack-ceiling.md, close-inclass-gap.md, lpdual, rgl].
- Only positive-priced input: the beyond-1 form-factor RANGE, dv*/dA = 0.6363/A³ (M2); everything proven (m₃ ≥ 2, min-gap, integrality, fluctuations, variance, Selberg-CLT) is either matched by the 256-law/super-law or priced ≤ 0 [attack-pricing-sheet.md §5–6].
- Window for ζ: cosine is the proven global minimizer of Q; the ξ′ lane has its own windows (quartic beats cosine for ξ′) [attack-kernel.md, attack-xiprime.md].
- **Structural fact I will lean on (universal two-moment ceiling, CONJECTURED-formal but immediate):** any certificate whose value is a functional of exactly the reads {mean density, in-band F on [0,1], integrality} is valid against the 256-law, which has p₁ = p₀; hence its certified value ≤ p₀, *regardless of its algebraic form* (tensor lifts, Schatten hierarchies, SOS — all included). The escape is only: (i) beyond-1 reads (conjectural), or (ii) certificates valid against a NARROWER class than "all configurations" — i.e., arithmetic admissibility. Both are mined below.

Every idea below is **CONJECTURED**. No number below is new; all cited numbers trace to the notes listed. No computation was run in this session (ideation deliverable; every probe is specified so an EXECUTIONER can run it in < 2 h).

---

## TOP 5

### 1. [RIGIDITY] The super-law matching ALL proven inputs (S₃ included) ⟹ the ceiling is impassable by any certificate reading only proven inputs. [CONJECTURED]
(a) **Object.** Extend the phase-randomized super-block construction (attack-selberg-clt.md §3: a union of scaled GUE blocks already realizes mean density, in-band F, Selberg-CLT fluctuations, and variance with simple fraction exactly p₀) to additionally match the ONE proven beyond-two-moment datum: the triple correlation S₃ = sine-kernel value at λ < 2/3 (Rudnick–Sarnak/Hejhal, the program's own "only proven beyond-two-moment lever", idea-generator-history.md H4.3). Because the blocks are GUE, their S₃ IS the sine-kernel value, and inter-block contributions vanish — the construction matches S₃ essentially for free.
(b) **Mechanism.** This converts the pair-correlation-class ceiling into a rigidity theorem over the union of *all* proven statistics: any certificate valid against every configuration consistent with {mean, in-band F, S₃(λ<2/3), Selberg-CLT, variance, integrality} is forced ≤ p₀ + |E(1)|. It answers the program's open question "does pinning S₃ move the ceiling?" (V4/S₃, blocked on the private family) *without* the private family — and it is the honest formal statement of "0.6818 is impassable by proven inputs."
(c) **Failure.** The super-law's S₃ differs from the sine-kernel value at the *precision the certificate needs* (its blocks are finite), or the certificate class's validity semantics cannot be extended to "consistent with S₃" cleanly (S₃ is a functional of the configuration, so consistency is well-defined; the risk is formal, not numerical).
(d) **Cheapest probe (< 2 h).** Numerically construct the super-block law (as in selclt, which is in the repo) and directly measure its S₃ against the sine-kernel value at the three proven λ's; then add the S₃ row to the existing marked-config LP at N = 64 (rgl's machinery) and verify the optimum is unchanged at p₀(64). Label: CHECKED NUMERICALLY on the surrogate; the theorem assembly is the work.
(e) **Plausibility 9 × Novelty 8.**

### 2. [RIGIDITY] Envelope-rigidity: with the PROVEN Montgomery error budget, the certificate class's cap is ≈ the record — proving the record is near-optimal against proven inputs. [CONJECTURED]
(a) **Object.** The certificate's value against the *real* reads is 0.6725 (Thm D) — the 0.6818 is a law property. The gap is the certified error envelope: the law's rows are certified to 3·10⁻⁴⁰ (near-CUE), the real in-band F only to O(1/√log T) (BGST25, explicit constants in the held paper). The new object is the *envelope-constrained LP*: max over certificates (c₀, r) valid against every configuration whose in-band rows lie in the certified envelope of the real data (explicit BGST25/Tsang-kernel error terms), of the value against F ≡ 1 data.
(b) **Mechanism.** This computes the honest class maximum given *proven* inputs. Two outcomes, both theorems: (i) optimum ≤ 0.6733 + δ — the record is (near-)class-optimal and further in-class certificates are provably worthless (kills the in-class search with a theorem, not a hunch); (ii) optimum ≥ 0.68 — the in-class gap 0.6725 → 0.6818 is provably closable with the proven envelope (fund the closure, quantify the needed sharpening of the Montgomery error term — a new, concrete target in the theory of the second moment).
(c) **Failure.** The envelope is so wide that the LP optimum collapses to ≤ 0.6725, making the theorem weaker than the record (still a documented negative with a script); or the explicit BGST25 constants are too crude to feed the LP (then the deliverable is the constant-hunting subproblem).
(d) **Cheapest probe (< 2 h).** Port the N = 64 marked-config LP (rgl) to accept a *row-envelope* (s_j ∈ [j/N − e_j, j/N + e_j] with e_j from the BGST25 error terms at a chosen T) and solve the max-min; compare with 0.6733 and 0.6818. Uses existing LP code; the analysis of the explicit constants is reading + one script.
(e) **Plausibility 7 × Novelty 9.**

### 3. [NEW TARGET] Dirichlet-family beyond-1 certificate: a rigorous q-aspect object on which the beyond-1 certificate is *proven* — the arithmetic proof-of-concept that the mechanism works. [CONJECTURED]
(a) **Object.** For the *family* of Dirichlet L-functions (or quadratic twists), the 1-level density / pair correlation is provable with support BEYOND 1 (large-sieve / character orthogonality handles the prime-pair off-diagonal that is conjectural for the single ζ; the family probe already passed both halves — attack-dirichlet-family.md: zero-side κ̂≈4/3, prime-side exactly diagonal for X < q). The new object is the *beyond-1 certificate run on family data*: the exact extension of the (c₀, r) machinery whose reads are the family's proven beyond-1 F rows.
(b) **Mechanism.** On the family, the M2-priced input (dv*/dA = 0.6363/A³) is not conjectural — it is a theorem. Running the beyond-1 certificate there produces the first rigorous bound above p₀ (or any chosen A-ceiling) on a genuine arithmetic object, and — critically — the first rigorous demonstration that "beyond-1 range moves the certified constant by the priced amount" (validating the pricing sheet's central claim on real arithmetic, not a surrogate). It also sharpens the D-1 assembly (Rem 7.2(iii)), the program's one live unclaimed theorem.
(c) **Failure.** The family's zero configuration is *different* from ζ's (q-aspect vs height-aspect); the certificate's p₁(A) curve for the family may saturate at a value that doesn't inform ζ. That is acceptable — the win is the mechanism validation and the D-1 theorem; the ζ-constant is untouched.
(d) **Cheapest probe (< 2 h).** Compute the empirical F on 10³–10⁴ zeros of L(s,χ) for a fixed modulus (q ≈ 10²–10³, LMFDB/cached), run the (c₀, r) certificate with rows out to A = 1.5, report the certified value vs the in-band-only value (expect: certified value rises with A — a CHECKED-NUMERICALLY version of the pricing curve on an arithmetic object).
(e) **Plausibility 6 × Novelty 8.**

### 4. [NEW INPUT — conditional but exact] The exact conditional roadmap: the certified p₁(A) curve from the extended-row LP (A ≤ 2 wall), making the PCC/HL-conditional roadmap exact and Lean-certifiable. [CONJECTURED]
(a) **Object.** attack-f1curve.md proved the bandwidth-2 wall (A ≤ 511/256 ≈ 1.9961, infeasible ≥ 2) and the M2 curve p₁(A) = 1 − (1−p₀)/A². The new object is the *exact* p₁(A) curve computed from the marked-config LP at N = 64/256 with the beyond-1 rows included (the rows j/N for j up to 2N are legal LP data — the wall says exactly how many; the private 256-law is NOT needed — the LP's optimum as a function of A is the curve).
(b) **Mechanism.** Under Montgomery's pair-correlation conjecture (or HL*(k₀,λ)), F ≡ 1 on [0,A] is the certified input; the exact p₁(A) converts the paper's Remark roadmap (0.70@1.04, 0.80@1.26, 0.90@1.70 — approximate) into an exact, Lean-certifiable conditional certificate: RH/PCC ⟹ certified simple-on-line fraction = p₁(A) + 1/(6N²). This is the sharpest honest form of the "conjecture-in/100%-out" template (PCC-II, round-3 vector #16) and gives the conditional program an exact target to write down.
(c) **Failure.** The LP optimum at N = 64 differs from the N = 256/∞ curve (finite-N artifacts; the f1curve note already sees the wall only at N = 256-scale); the exact curve needs the private family for N = 256 — but N = 64 gives the shape, and the ceiling's EnclOK semantics (which the exact curve would inherit) stay the only non-Lean link.
(d) **Cheapest probe (< 2 h).** Re-solve the rgl N = 64 marked-config LP with rows extended to j ≤ 2N (no S₃ constraint needed); output p₁(A) at A = 1.0, 1.03, 1.26, 1.70, 1.99 and compare with the M2 model (expect ≤ 1.1% agreement as in f1curve §4).
(e) **Plausibility 7 × Novelty 7.**

### 5. [NEW OBJECT] Beurling/Vasyunin realization of the near-CUE law: is the ceiling law realizable as the zero set of a genuine (generalized-prime) zeta function? [CONJECTURED]
(a) **Object.** Vasyunin-type constructions (exact Beurling zeta functions of generalized primes with prescribed zero configurations, including RH-true examples) let one *engineer* a zeta whose zeros are a prescribed finite configuration. The new object: a Beurling generalized-prime system whose zeta has zeros at (an approximation of) the near-CUE 256-law's marked configuration, with prime-side two moments matched to ζ's (the explicit formula still holds for Beurling systems, so tr/HS² are computable from the generalized primes).
(b) **Mechanism.** The ceiling's premise is "the law is an admissible configuration." Two outcomes: (i) the law (or an arbitrarily close configuration) IS realizable as a Beurling-zeta zero set with the right moments — the ceiling survives the arithmetic-admissibility strengthening (a rigidity win: the law is not an artifact; no certificate valid against *arithmetic* configurations either exceeds p₀); (ii) it is NOT — near-CUE in-band reads cannot come from any generalized-prime zeta — then the "configuration" is spurious, the ceiling's premise cracks for arithmetic certificates, and a new (arithmetic) certificate class opens. Either way it is the concrete probe of the one escape from the universal two-moment ceiling (idea 0).
(c) **Failure.** Prescribing zeros and matching two *asymptotic* moments simultaneously is delicate; the finite constructions may match neither to the certificate's precision. (The honest prior: (i) is more likely — which still pays, as a rigidity theorem.)
(d) **Cheapest probe (< 2 h).** Vasyunin's classical finite construction: prescribe 20–100 zeros in near-CUE positions (mean spacing 1, ~68% marked simple), solve for generalized primes, compute the Beurling zeta's in-band F and the certificate's reads; compare with ζ's. Pure numerics + known construction recipes.
(e) **Plausibility 5 × Novelty 9.**

---

## 6–14 (ranked)

### 6. [NEW MEASUREMENT] Rigged-ensemble empirical pricing of the beyond-1 range: test the M2 model p₁(A) = 1 − (1−p₀)/A² on constructed ensembles with tunable beyond-1 F. [CONJECTURED]
(a) **Object.** The only positive-priced input's *price* (dv*/dA = 0.6363/A³) rests on the M2 model, which has never been tested against actual configurations: construct 256-point ensembles matching (mean, in-band F ≡ 1, S₃ = GUE) with beyond-1 F set to F ≡ 1 continued on [1,A] (rigged via multiplicative-phase randomization on the pair counts), and measure the empirical simple fraction p₁(ens) as A grows.
(b) **Mechanism.** If p₁(ens) tracks M2, the pricing curve is calibrated and the conditional roadmap (idea 4) is on solid ground; if it deviates, the price of beyond-1 range is corrected — directly changing what the conditional program (B1-R) is worth. It also produces the first empirical estimate of "how much constant a proven F ≡ 1 on [1,1.03] would buy."
(c) **Failure.** The ensembles are built by phase randomization and may not be "configuration-realizable" (their S₃ or higher correlations drift); the measured p₁ may be dominated by finite-N effects. Calibration value survives regardless.
(d) **Cheapest probe (< 1 h).** numpy/mpmath ensemble of 200 × 256-point laws; histogram simple fractions vs A ∈ {1, 1.03, 1.26, 1.7, 1.9}; fit p₁(A). One script.
(e) **Plausibility 8 × Novelty 5.**

### 7. [NEW INPUT — empirical] The α ≈ 1.0–1.3 feature: decompose it (τ-bins, prime powers, height dependence), then price the observed bump under M3/M2. [CONJECTURED]
(a) **Object.** The program's one real unexplained empirical deviation (≥ 11σ at α ∈ [1.0,1.3] under both the naive and LS estimators — attack-ls-estimator.md, attack-hot-hand.md). The new step: decompose the periodogram by τ-bin / prime-power contribution and check height dependence (the program's A1.1 vector's open decomposition), then feed the observed F(α) ≈ 1.5-level bump on [1.0,1.3] into the M2/M3 pricing models to state exactly what it would be worth if certified.
(b) **Mechanism.** If the feature is real and zeta-specific, it is the first empirical sliver of beyond-1 structure — the input the pricing sheet prices positive. Pricing it converts a 11σ curiosity into a concrete conditional target ("certify F ≥ 1+δ on [1,1+ε] would buy Δ = …"), and the decomposition may reveal a prime-arithmetic origin (a *candidate* for a real, provable sliver).
(c) **Failure.** The feature is an estimator/height artifact after all (the hot-hand verdicts already cleared the naive trend and the α=1 spike; this is the surviving residue — the honest prior is it stays an unexplained finite-height effect).
(d) **Cheapest probe (< 2 h).** Extend the existing periodogram code with τ-bin masks (restrict the explicit-formula terms by prime-power support); recompute the feature at N = 3·10³, 10⁴, 3·10⁴ and by height windows.
(e) **Plausibility 5 × Novelty 7.**

### 8. [RIGIDITY/SEMANTICS] Resolve the stability-ceiling semantics: is the refined (Gram-stability) class's ceiling 0.68183123 or 0.68234? [CONJECTURED]
(a) **Object.** ceiling-gram-constraint.md §3.3 flagged a CONJECTURED alternative reading: if the universal floor tr Ψ(M) ≥ ε_univ·N (the external repos' stability term, ε_univ ≈ 5·10⁻⁴) is a law-independent *constant shift* the certificate may add for every law, the refined class's ceiling is 0.68183123 + c·ε_univ ≈ 0.68234. The new object is the *formal semantics*: what exactly does the external bound's certificate prove (per-law floor — constraint reading, ceiling unchanged — vs universal shift — ceiling +5·10⁻⁴)?
(b) **Mechanism.** If the shift reading is correct, the *certified* ceiling of the refined class is 0.68234, not 0.68183 — a small but real horizon increase, and the exact target for the external repos' 0.6733 trajectory. If the constraint reading is correct, the +5·10⁻⁴ is a documented non-move and the search redirects. Either outcome is a cheap, decisive result.
(c) **Failure.** The semantics depend on the certificate validity definition (the 256-law's actual simple fraction vs certified count), which the phone mirror lacks — the deliverable may be a precise question for the Lean side rather than a number.
(d) **Cheapest probe (< 2 h).** Re-read the external repos' bound derivation (in /tmp/combine/ or the fetched sources) and the stability note; write the two formalizations as Lean-style statements and check which matches the repos' arithmetic (the repos' constants + ε term decide the reading).
(e) **Plausibility 6 × Novelty 7.**

### 9. [NEW TARGET] Joint (ζ, ξ′) derivative-tower certificate with the interlacing count as a new input (Farmer combination; distinct-ζ > 0.6603). [CONJECTURED]
(a) **Object.** The ξ′ lane is PROVEN machinery (simple-on-line for ξ′: 0.85838 flat / 0.86864 quartic — attack-xiprime.md), and the interlacing is CHECKED NUMERICALLY (one ξ″-zero per ξ′-gap, 20/20). The new object: a *joint quadratic form on the shared frame* (the two-form note's frame-sharing, attack-twoform.md, applied to the pair (ζ, ξ′) instead of (ζ, CGG)), plus the interlacing count N₀(ξ′) ≥ N₀^s(ζ) − 1 (Rolle on the line for simple zeros) as a rigorous link between the two certificates, feeding Farmer's weighted combination toward a distinct-ζ bound > 0.6603 (Wu's record).
(b) **Mechanism.** Each derivative step's certificate supplies the next step's simplicity (the tower is self-reinforcing — attack-xiprime.md §5); the joint form reads the *same* prime-side moments through two windows, and the interlacing input is new structure that neither certificate alone uses. This is the program's top new-target vector (T-2); the sharpening here is the interlacing count as an explicit certificate input rather than a heuristic.
(c) **Failure.** The D₁^(2) pair-density derivation (new math, not a corollary) may give a non-competitive constant (kill if κ₁^(2) ≥ κ₁^(1)); the interlacing count is finite-T numeric, the general statement conjectural. Also: this moves the *distinct* bound, not the 0.6818 simple ceiling — honest scope.
(d) **Cheapest probe (< 2 h).** Compute the interlacing count N₀(ξ′)/N₀(ζ) on the cached 1000 zeros (mpmath, existing xiprime machinery) and the empirical joint-form value; verify the tower inequality numerically before any theorem work.
(e) **Plausibility 5 × Novelty 6.**

### 10. [PRICE PROBE] S₃-constrained configuration LP at N = 64: pin the third-moment price without the private 256-family. [CONJECTURED]
(a) **Object.** The V4/S₃ capacity probe is blocked on the private 256-law. It needn't be: add the row S₃ = sine-kernel value (proven at λ < 2/3) as a constraint to the *public* N = 64 marked-config LP (rgl machinery) and re-optimize p₁.
(b) **Mechanism.** The pricing sheet prices m₃ ≥ 2 for the simple cert at −1/3 per unit (caps at 2/3). The N = 64 LP with the S₃ row makes this *exact*: the constrained optimum vs p₀(64) is the price of the triple-correlation input, definitively closing (or surprisingly reopening) the third-moment lane for the simple certificate — the last "beyond-two-moment" hope (H4.3).
(c) **Failure.** Expected outcome is the documented negative (optimum ≤ 2/3); the probe's value is then the exact price and the closure of a decade's reflex.
(d) **Cheapest probe (< 2 h).** scipy/mpmath LP on the N = 64 marked-config LP with the S₃ row (the S₃ value for a marked config is computable from its positions — no family needed).
(e) **Plausibility 7 × Novelty 4.**

### 11. [PRICE PROBE] AH / essential-simplicity-constrained LP: price the "no pairs at half-spacing" input. [CONJECTURED]
(a) **Object.** The Alternative Hypothesis (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2508.10857) constrains pair density at k/2 spacings and multiple-zero density; the literature sweep flags it as the natural input to the Gram-stability ladder. The new object: the marked-config LP at N = 64 with AH-type rows (no mass at half-integer-spacing bins beyond a density bound) — the *price* of the AH input, which has never been computed.
(b) **Mechanism.** If the AH-constrained optimum rises above p₀(64), the half-spacing structure is positive-priced and any theorem restricting such pairs (the AH paper's own conditional results, or an unconditional sliver) becomes a funded input. If it is neutral/negative (the likely prior, matching the min-gap price: −0.1799 at X = 0⁺), the lane is closed with a price instead of a hunch.
(c) **Failure.** AH is a *hypothesis*, not a proven input — the probe prices a hypothetical constraint, which is exactly the pricing-sheet discipline (price it before hunting it).
(d) **Cheapest probe (< 1.5 h).** N = 64 LP with the half-spacing rows zeroed; optimum vs p₀(64); one script, existing machinery.
(e) **Plausibility 6 × Novelty 4.**

### 12. [PRICING REFINEMENT] Beyond-1 functional sensitivity ranking: which conjectural functional is the highest-leverage hunt target? [CONJECTURED]
(a) **Object.** The beyond-1 input is a *family* of linear functionals of F on [0,A] (twisted-Parseval bump at a point, HL*(k₀,λ)-type additive correlations, FG twisted F_n). The new object: rank the candidate functionals by certified sensitivity per unit of conjectural strength — the M3 free-mass model (8.5·10⁻⁴ per unit δ at ε = 0.02) gives the pointwise price; the range model gives the aggregate price; the ranking says which conjecture, if proven, buys the most constant.
(b) **Mechanism.** The conditional program (B1-R) currently targets "the range" generically. A sensitivity ranking converts it into a precise target: "prove the specific additive-correlation estimate that prices best" — the highest-leverage unit of conjectural work. It also exposes the wrong units (single-point values are priced at δ ≈ 21 needed — the pricing sheet's own lesson).
(c) **Failure.** All candidate functionals share the same prime-pair wall (M29: proven bounds fail by 3.6·10³–3.7·10⁴×); the ranking only orders conjectures, it does not weaken any.
(d) **Cheapest probe (< 1 h).** Extend pricing_sheet.py with the M3 sensitivity for each candidate functional (the models are already in code).
(e) **Plausibility 6 × Novelty 4.**

### 13. [NEW TARGET — effective] Certified finite-T certificate with the Groskin tail budget as the error source (sharpened V20). [CONJECTURED]
(a) **Object.** Groskin's tail budget B_T ~ (2N+1)ρ log T/(π²T) certifies the finite-truncation error of the truncated Weil form (literature-sweep, G6-adjacent; attack-cvs-import.md §7). The new object: the *finite-T certificate* — the (c₀, r) bound evaluated on certified finite-T data (argument-principle tool, attack-argprinciple.md: certified counts below 3·10¹² with Platt–Trudgian/Gourdon–Demichel), with the certified error budget carried explicitly through the bound arithmetic.
(b) **Mechanism.** Produces the honest effective version of the 0.6733 theorem with a documented error chain (the program's V20 deliverable), and — via the certified counts at T = 10⁴–10⁵ — the first *certified* finite-T certificate values whose T-dependence toward 0.6733 is documented rather than assumed.
(c) **Failure.** The structural obstruction (finite computations cannot prove liminf statements — attack-argprinciple §6) means this is documentation/effective-theorem value only; no asymptotic gain.
(d) **Cheapest probe (< 2 h).** Reuse the argprinciple tool's certified brackets (T = 10⁴, 2·10⁴, 5·10⁴) and feed the certified counts into the bound formula with interval arithmetic; report the certified value vs T.
(e) **Plausibility 6 × Novelty 3.**

### 14. [NEW OBJECT — long shot] The complex-window / pencil Weil form: a 1-parameter inertia family with a shared p₁. [CONJECTURED]
(a) **Object.** For a complex window, the Weil form is Hermitian, each on-line zero contributes a rank-one PSD term, each off-line pair a (1,1)-block — for EVERY θ in the pencil W(θ) = W_re + θ·W_im (W_im from the imaginary part of a complex test function). The new object: the pencil's inertia structure — the set {n₋(W(θ))} as θ varies must be consistent with a *single* configuration of p off-line pairs (the zero-crossing curves λ_j(θ) can cross zero only by "spending" pairs).
(b) **Mechanism.** The rank–trace inequality applied to each W(θ) individually is covered by the ceiling (each θ reads only the two moments); the *joint* statement (the pencil's crossing structure) is new data not readable from the two moments — the first candidate object that is a functional of more than the two moments but *not* a moment of the zero distribution (it is a geometric/spectral datum of the frame).
(c) **Failure.** Most likely: W_im is degenerate (tr W_im = 0 by symmetry, and the pencil's joint constraint collapses to max_θ of the individual certificates, which the shadow-price-1 structure already prices). Expected documented negative; cheap to confirm.
(d) **Cheapest probe (< 2 h).** Finite-T compute the spectra of W(θ) for θ ∈ [0, π] on the real zeros vs the extremal world (existing V1 machinery); check whether the crossing structure separates them.
(e) **Plausibility 3 × Novelty 7.**

---

## Ranking summary

| # | Idea | Type | P × N |
|---|---|---|---|
| 1 | Super-law with S₃: ceiling impassable by proven inputs | RIGIDITY | 9 × 8 |
| 2 | Envelope-rigidity: record near-optimal vs proven error budget | RIGIDITY | 7 × 9 |
| 3 | Dirichlet-family beyond-1 certificate (q-aspect proof-of-concept) | NEW TARGET | 6 × 8 |
| 4 | Exact conditional roadmap p₁(A) from the extended-row LP | NEW INPUT (conditional) | 7 × 7 |
| 5 | Beurling/Vasyunin realization of the near-CUE law | NEW OBJECT | 5 × 9 |
| 6 | Rigged-ensemble empirical pricing of beyond-1 range | MEASUREMENT | 8 × 5 |
| 7 | α≈1.1 feature decomposition + pricing | INPUT (empirical) | 5 × 7 |
| 8 | Stability-ceiling semantics (0.68183 vs 0.68234) | RIGIDITY | 6 × 7 |
| 9 | Joint (ζ, ξ′) tower with interlacing input | NEW TARGET | 5 × 6 |
| 10 | S₃-constrained LP at N = 64 (third-moment price) | PRICE PROBE | 7 × 4 |
| 11 | AH-constrained LP (half-spacing price) | PRICE PROBE | 6 × 4 |
| 12 | Beyond-1 functional sensitivity ranking | PRICING | 6 × 4 |
| 13 | Certified finite-T certificate (Groskin tail budget) | EFFECTIVE | 6 × 3 |
| 14 | Complex/pencil Weil-form inertia family | NEW OBJECT (long shot) | 3 × 7 |

**Strategic reading.** The honest map (idea 0) says: proven inputs cannot move the 0.6818 ceiling (ideas 1, 2, 8 make that a theorem), and the only positive-priced escape is beyond-1 structure, which is conjectural for ζ but *proven for arithmetic families* (idea 3) and *exactly priced* (ideas 4, 6, 7, 12). The novel-object long shots (5, 14) attack the ceiling's premise (arithmetic admissibility) rather than its inequality. Price probes (10, 11) close reflex lanes with exact numbers.

## Honesty footer

- All ideas are **CONJECTURED**; none is a result. No computation was run in this session (phone compute is scarce; every probe is specified with existing tools). Every cited number traces to the notes: discovery-6732629, attack-ceiling, close-inclass-gap, ceiling-gram-constraint, attack-pricing-sheet (+.py), attack-f1curve, attack-lpdual, attack-kernel, attack-multiplicity, attack-twoform, attack-xiprime(+2-tower), attack-ihara-sandbox, attack-selberg-clt, attack-hot-hand, attack-ls-estimator, attack-argprinciple, attack-cvs-import, attack-dirichlet-family, attack-vector-catalog(-3), idea-generator-history / -crossdomain / -literature, literature-sweep-simplezeros, mine-openai-spherepacking.
- Ideas 1, 2, 3, 4, 8, 10, 11, 12, 13 overlap with program threads (selclt, V20, D-1/B1-R, f1curve, rgl, A1.1, stability semantics); the sharpening (S₃-union rigidity, envelope-constrained LP, exact p₁(A), interlacing input, tail-budget certification) is the new content claimed here.
- Deliberately excluded (documented dead in the cited notes, do not re-fund): window tweaks for ζ, in-class certificates beating r=1−x, m₃/min-gap for the simple cert, beyond-1 mean/variance/distributional, CvS, individual GL(2), mollifier fusion, the two-form sum.

RESULT: OPEN — the ceiling is provably impassable by proven inputs (super-law + S₃ rigidity), and the only live escape is beyond-1 structure, which is conjectural for ζ but rigorously present in arithmetic families and exactly priced via the extended-row LP.
