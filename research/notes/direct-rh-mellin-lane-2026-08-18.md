# Direct-RH, Mellin/Dirichlet/transfer analytic-object lane — one-way sufficient condition hunt

**Date:** 2026-08-18. **Agent:** adventurer (read-only). **Status:** INITIAL WRITE-AHEAD (partial); refined after closure_dag / operator-lane reads. **Labels:** All claims below are labeled. No numerical result is claimed without an attached Rust probe path (none run yet in this session — see "Cheapest Rust-only test" per candidate).

## 0. Scope (assumption, explicit)

Task: find ONE genuinely new one-way sufficient condition `H(zeta) => RH` whose object is a Mellin transform / Dirichlet series / transfer operator, excluding the closure families listed (Li, Speiser, NB, Laguerre, HB/de Branges, Weil positivity, BSY/Poisson–Jensen, explicit-formula equality, coefficient margins, Hankel/PF, Jensen/GJT, RMT, GS diagonal, near-line density, prior Agy candidates). Required: a **non-vacuous named RH-false control** (a model world where RH is known to fail and on which H's structure can be evaluated), a formal implication statement, the exact missing lemma, a cheapest Rust-only test, and a non-equivalence proof (H not ⟺ RH). If no candidate survives, name the closest route and its exact fatal flaw.

Deflation triage (campaign method): class 1 = known theorem restated; class 2 = equivalent to RH; class 3 = finite numerical check; class 4 = near-tautology/hypothesis smuggles the hard part.

## 1. Lane map (what the ledger already closes INSIDE this lane — cite, do not re-derive)

- Nyman–Beurling / Báez-Duarte `d_N -> 0` and the Beurling operator: ⟺ RH (8C, 8C-certified-dN, 8E, wave8c-burnol-rate-2026-08-18.md). CLOSED.
- Herglotz object `H = Xi'/Xi`: ⟺ RH (g4-2 herglotz-probe). CLOSED.
- Stieltjes S-fraction of Xi'/Xi + Foster reactance: ⟺ RH (g1-1, g1-2, stieltjes-sfraction). CLOSED.
- Turán/Laguerre L_k, T_k: ⟺ RH (8D, wave8d-*). CLOSED.
- Li lambda_n: ⟺ RH (8A, li-structure-audit). CLOSED.
- PNT-error one-way (S2-PNT): von Koch `psi(x)-x = O(sqrt x log x)` is ⟺ RH; the strictly-stronger one-way version `O(sqrt x (log x)^{1/2+eps})` is class-1 (restated theorem, hypothesis strictly stronger than RH -> zero provability). CLOSED (s2-pnt-discriminator-2026-08-18.md).
- Mertens-type `M(x) = O(sqrt x)`: classical one-way sufficient, strictly stronger than RH; Odlyzko–te Riele kills only the pointwise |M(x)| < sqrt x form. Class-1 restatement (explicit-formula family). CLOSED.
- de Bruijn–Newman `Lambda <= 0`/heat deformation: ⟺ RH (dbheat-deformation-2026-08-18.md). CLOSED.
- Multplier/companion products and all "3-4-5"-style positivity: see Candidate A below (this session).
- LP/PF/Schoenberg/Burnol duality: closed (E1, schoenberg-kernel-tp2-2026-08-18.md).
- Moment-functional Stieltjes/J-fraction of the M_k sequence: closed (fresh-hunt-corners corner (e)(i) — same object as closed foster/stieltjes).

## 2. The candidate family — Candidate A: DIRICHLET-MULTIPLIER ZERO-FREE TRANSFER

**Object:** a Dirichlet-series (or Euler-product) multiplier D(s) and the product H(s) = ζ(s)·D(s). Idea: certify a zero-free right half-plane Re(s) > 1/2 for H and for D by a mechanism not available for ζ itself, then conclude ζ ≠ 0 on Re(s) > 1/2.

**Formal implication (PROVEN logic, trivially):**
`[D(s) ≠ 0 on Re s > 1/2] ∧ [ζ(s)D(s) ≠ 0 on Re s > 1/2]  ⟹  ζ(s) ≠ 0 on Re s > 1/2`, i.e. RH.
The logic is a pure product-of-nonzero-factors argument; no analytic content yet.

**Non-equivalence / one-way status:** depends entirely on the choice of D:
- If D is FIXED with a PROVABLE zero-free half-plane Re>1/2 (e.g. D = η-factor (1−2^{1−s})ζ? — no, that changes ζ), then RH ⟹ (ζ≠0 ∧ D≠0) ⟹ ζD≠0, so H ⟺ RH. **Degenerates to class 2.**
- If D is fixed with NO provable zero-free half-plane, then H carries the entire burden: proving ζD ≠ 0 on Re>1/2 is at least as hard as proving ζ ≠ 0 there (a zero of ζ at ρ kills H regardless of D). The hypothesis then smuggles the hard part. **Class 4 (near-tautology with smuggled content).**
- If D is chosen ζ-dependently (D = product over known-zero-free data), circularity.

**Exact missing lemma (the only thing that would make this a real one-way condition):** a theorem that a fixed explicit Dirichlet series D (built from arithmetic data independent of ζ's zeros) has a zero-free half-plane strictly inside Re > 1/2 WITHOUT that theorem being RH-equivalent. 

**Why no such lemma can come from the standard mechanisms (this is the route's fatal flaw — the three mechanisms check, PROVEN-class reasoning):**
1. (*Euler-product / 3-4-5 positivity*): every positivity-certifiable zero-free statement of the form Σ c_j log ζ(s+Δ_j) ≥ 0 needs the shifted arguments in the Euler-convergence half-plane Re > 1. Minimal shift Δ ≥ 0 forces the certified region to abut Re ≥ 1 only. There is no free shift reaching σ = 1/2. Boundary of technique = Re(s) = 1. (This is exactly why the classical 3-4-5 trick certifies ζ ≠ 0 on Re = 1 — the line — and never the strip.)
2. (*Laplace/Stieltjes positivity*): Laplace transforms of positive measures on (0,∞) do NOT have zero-free complex half-planes. Explicit witness: D(z) = 1 + 2e^{−s} + 2e^{−2s} (positive coefficients, i.e. measure μ = δ₀ + 2δ₁ + 2δ₂): zeros solve z² + 2z + 1·(with z = e^{−s})… z = (−1 ± i)/2 ⇒ e^{−s} = (−1±i)/2 ⇒ |e^{−s}| = √2/2 < 1 ⇒ Re s = −log(√2/2) = (1/2)log 2 > 0. Zeros in Re s > 0. (Concrete; a Rust probe can certify these roots.)
3. (*Herglotz / Pick*): Herglotz-type representations that DO force zero-free half-planes are exactly the objects where the positive measure sits on the boundary line — and for every ζ-attached analytic object (Ξ′/Ξ, log ζ integrals) those are ⟺ RH (closed: g4-2, foster, stieltjes).

**RH-false control (Candidate A):** the planted-zero Beurling world (tools/barrier_zoo_rs, ledgered operational): a Beurling system whose zeta ζ_B has a planted zero at 1/2+δ+iγ. In that world, H(zeta_B) with any D is FALSE for the same reason as RH(B): the planted zero kills ζ_B·D. So the control does not test A's mechanism (H fails exactly where RH fails — no discriminating power). The discriminating power of A would have to come from a D that is zero-free in the control while ζ_B is not — but then H is exactly "D zero-free", i.e. independent-of-ζ, and the implication is vacuous (products of the truth of D alone). Verdict on control: **NON-VACUOUS CONTROL DOES NOT EXIST for A; the family is either class-2 (fixed provable D), class-4 (burden-smuggling D), or vacuous.**

**Cheapest Rust-only test (if funded):** probe in tools/ (std-only or rug):
- (t1) certify roots of z² + 2z + 2 = 0 ⇒ the positive-Laplace counterexample zero at Re s = (log 2)/2 (Aberth/Eigen via f64 Newton, exact rational verification), closing mechanism 2 numerically.
- (t2) maximal certified σ₀ for the 3-4-5 product Σₚ-c_j-log(1−p^{−(σ₀+Δ_j)}): expect positivity to fail as soon as (σ₀ + min Δ_j) < 1, pinning mechanism 1's boundary at Re = 1 (pure f64, no arbitrary precision needed).
- (t3) η-transfer mirror: compute zeros of η(σ₀+it) vs ζ(σ₀+it) for σ₀ ∈ (1/2,1), grid t ≤ 100 — expect identical zero sets (factor (1−2^{1−s}) zero-free in the strip), demonstrating class-2 degeneration concretely.
None run yet in this session — these are the funding spec.

## 3. Candidate B: GRAND TRANSFER (all Dirichlet L-functions on their line)

**Formal implication (PROVEN logic):** `[∀ primitive χ, all nontrivial zeros of L(s,χ) lie on Re s = 1/2]  ⟹  RH`. One-way: ζ-RH does not imply GRH. Genuinely one-way in pure logic.

**Fatal flaw:** the non-vacuous-control requirement is unmet. In the named RH-false model worlds available (Davenport–Heilbronn via barrier_zoo_rs; planted-zero Beurling; fake Weil polynomial): the DH function's defining character χ (mod 5, primitive) — its pure L(s,χ₅) is a degree-1 L-function whose RH-status is UNKNOWN — no control can exhibit "GRH true ∧ RH false". The Beurling/Weil controls have no Dirichlet-character L-functions to evaluate at all. So B is untestable by construction: where the hypothesis is evaluable it is ⟺-class-adjacent, where it is non-vacuous it has no model. Classification: class 1 (folk theorem: GRH ⟹ RH, known restatement) with an unconstructible control. CLOSED as a candidate.

## 4. Candidate C: PARITY/ETA TRANSFER — η(s) = (1 − 2^{1−s})ζ(s)

**Formal implication:** zeros of η in the strip 0<Re<1 coincide with zeros of ζ there (the multiplier 1−2^{1−s} vanishes only at s = 1 + 2πik/log 2, Re = 1). Hence `[all zeros of η in 0<Re<1 lie on Re=1/2] ⟺ RH` — **class 2 (equivalent), the "cheapest" possible Mellin transfer and already the textbook Riemann–Siegel/eta identity.** Not one-way; excluded by the task (class-2 closure). The only non-trivial fact: η converges conditionally on Re s > 0, so it is a genuinely Mellin/Dirichlet "analytic object" — but it adds nothing (multiplier zero-free in the strip). CLOSED.

## 5. Candidate D (sweep of remainder of the lane, each one-line verdict)

- Remainder-term/finite-cut objects (partial sums of ζ, ζ − Σ_{n≤x} n^{−s}): class 4/3 — finite data cannot certify a half-plane (needs uniform bounds = RH-equivalent). CLOSED.
- Weighted divisor/moments (Σ Λ(n)(log n)^k n^{−s}): integrate/differentiate of log ζ — explicit-formula equality class. CLOSED.
- Positive-density Mellin of zero-counting F(u) = N(e^u): Fourier side of explicit formula — Weil ⟺ class. CLOSED.
- Lattice/Euler-substitution ratios (ζ(2s)/ζ(s)-type): poles/zeros relocate to s/2; the right-of-1/2 vacuum still encodes exactly ζ's zeros. CLOSED (⟺).
- ℓ²/trace-class transfer matrices with μ-coefficients: Beurling-operator closure (8E). CLOSED.
- Grand-family beyond Dirichlet-L (Selberg class, automorphic): same control problem as B. CLOSED.

## 6. VERDICT (initial; will re-confirm after closure_dag read)

**NO SURVIVOR in the Mellin/Dirichlet/transfer lane.** Every candidate collapses into one of the four deflating classes:
- class 2 (equivalent-to-RH: C, η-family; A with provable D; remainder/lattice/ℓ² objects; positivity-via-Herglotz),
- class 1 (restated known theorem: B as folk-GRH, Mertens-O, PNT-one-way),
- class 4 (hypothesis-smuggling: A with unprovable D),
- empty/technique-bounded (A's positivity mechanisms die at Re = 1).

**CLOSEST ROUTE + EXACT FATAL FLAW (as required):** the closest thing to a genuinely-new one-way sufficient condition in this lane is **Candidate A in its "ζ-independent D with certified zero-free half-plane Re > 1/2" form** — it is the only family whose implication is (i) logically one-way and (ii) would carry real content if the zero-free region of D came from arithmetic structure rather than from ζ. Its exact fatal flaw: **no such arithmetic-certified zero-free half-plane exists by any mechanism, because (a) positivity/Euler-product certification is bounded at Re(s) = 1 (3-4-5 boundary), (b) Laplace-transform positivity does not forbid complex zeros (explicit counterexample in §2), and (c) the only remaining half-plane-certifying structure is Herglotz-type, which for every ζ-attached kernel is ⟺ RH (closed).** Absent that lemma, the hypothesis is at least as hard as RH (smuggling). The route is structurally blocked, not merely unexplored.

## 7. Honest caveats

- This memo is a closure memo unless the refined reads (closure_dag.json, direct-rh-operator-route-2026-08-18.md — the operator-lane twin) contradict it. The operator-lane twin was ABANDONED with a PROVEN obstruction (theta-density log-concavity probe negative; PF∞ already proven impossible for Φ), which independently corroborates the "positivity/PF mechanisms dead" reading here.
- No Rust probe ran in this session. All "mechanism boundary" claims above are mathematical-class reasoning (PROVEN-class: the 3-4-5 at Re=1 is textbook; the Laplace counterexample is explicit and verifiable; the η multiplier's zero set is exact). Funding spec for the three cheap probes is in §2.
- Control discipline was applied per candidate; candidate A and B both fail the non-vacuous-control requirement in different, documented ways.

## 8. REFINEMENT after closure-DAG + twin-lane + skill application (2026-08-18)

### 8.1 Non-duplication check against closure_dag.json (do-not-repeat discipline)
Full DAG node list read. Closest prior nodes to this memo's candidates, and why this memo is NOT a duplicate:
- `operator-lane-polya-density` (twin, direct-rh-operator-route-2026-08-18.md) — covers ONLY the Fourier/operator side (Φ-densities, PF∞, log-concavity of Φ). This memo covers the DISJOINT Dirichlet/Euler-product side: the multiplier/companion zero-free-transfer family (Candidate A), which appears NOWHERE in the DAG. Distinct contribution: the mechanism trichotomy (§2) — (i) Euler-product/3-4-5 positivity bounded at Re(s)=1, (ii) Laplace-transform positivity does not forbid complex zeros (explicit closed-form witness), (iii) Herglotz-type half-plane certification is ⟺-RH closed. The twin's PF∞ closure (Φ ∉ PF∞ PROVEN) is the Fourier-side instance of the same "positivist mechanism boundary"; the two memos triangulate the same wall from opposite sides.
- `agy-fresh2-2026-08-18` — INCONCLUSIVE/NO SURVIVOR (four-channel obstruction, agrees with this memo's verdict; no mechanism analysis, no candidates). This memo supplies what that one lacked: named candidates, formal implications, and per-candidate control analysis.
- `S2-PNT` / `8E-Mellin` / `Herglotz` / `Li-criterion` / `S1-margin` / `Schoenberg-kernel-TP2` / `levinson-variational-Q` / `gs-2026-diagonal-bridge` — all class-2/class-1 closures inside the lane; cited, not re-derived. `gs-2026-diagonal-bridge` (GS 2511.20059, diagonal Σ_{γ=γ′}1 ≤ (C+o(1))N needs unconditional C<2) is noted: it is a RECORD-side object (firewall: proportion ≠ RH), outside this memo's sufficient-condition scope, and its missing input (unconditional diagonal) is itself a near-line/coefficient-margin closure.
- `frontier-smalln0-slice`/`moment-sequence-to-gamma` — confirms the "positive-measure M_n ⇒ Hankel TP on γ(n)" bridge breaks at the first minor; this is the arithmetic-face of Candidate C/remainder-family closure.

**Verdict on duplication: none. The Dirichlet-multiplier zero-free-transfer family (A) was un-screened before this memo; it is now closed by mechanism analysis.**

### 8.2 s4h-investigation-counter-hypothesis applied (to the memo's own verdict)
Hypothesis under investigation: "the Mellin/Dirichlet/transfer lane contains no genuinely-new one-way sufficient condition H(zeta)⟹RH." Rival hypotheses generated and assessed:
- **R1 (missed in-lane object with provable content):** screened η/parity, remainder/finite-cut objects, weighted-log Dirichlet series, lattice ratios ζ(2s)/ζ(s), ℓ² μ-transfer matrices. Each: class 2 (multiplication/renormalization by an explicit zero-free-in-strip factor — zero sets are literally ζ's) or class 4. Assessment: does NOT survive — the "transfer" never changes the zero locus in the strip; every such object's strip zeros = ζ's strip zeros.
- **R2 (the twin's log-concavity residue):** H = "Φ log-concave". Assessment: dual failure — (hypothesis side) the twin's probe found log-concavity fails on Φ's meaningful support (L>0); (theorem side) the would-be sufficiency lemma {ρ even log-concave} ⟹ ρ̂ ∈ LP has no known proof and is expected FALSE (sharp Schoenberg duality needs PF∞). INCONCLUSIVE as a lemma, moot as a candidate. This is the closest any lane-adjacent object came to a live theorem; its exact missing lemma is recorded (see 8.4).
- **R3 (twist/GRH-family built on the SAME modulus as the control):** constituent L(s,χ₅) of the DH world: RH-status UNKNOWN ⟹ the DH control cannot witness "H true ∧ RH false"; no non-vacuous control exists. Same verdict as Candidate B. Assessment: does not survive the control requirement.
- **R4 (classical singleton, M(x)=O(√x)):** provably STRICTLY stronger than RH, one-way; but class 1 (known theorem, explicit-formula family) and excluded by the task's closure list. Assessment: survives as logic, not as novelty.
Discriminating evidence available vs. needed: available — the four-fold collapse pattern (all in-lane transfers either ⟺-degenerate, control-less, hypothesis-failing, or class-1). Needed (decisive test) — the three Rust probes of §2 (t1/t2/t3), which discriminate "mechanism-bound dead" (holds) from "unexplored residue"; funding spec provided, none run (adventurer, read-only).

### 8.3 s4h-logic-argument-validation applied (Candidate A's argument chain)
**Argument:** (P1) ζ·D ≠ 0 on Re>1/2, (P2) D ≠ 0 on Re>1/2, (P3, implicit) D is arithmetic/fixed so that P1 is provable without ζ-zero input ⟹ (C) RH.
**Premise assessment:** P1 ∧ P2 ⟹ C: SOUND (product of zero-free analytic functions; formally valid). P3: the load-bearing premise — NOT ESTABLISHED by any mechanism (trichotomy §2); without P3, P1 is exactly the RH task (hypothesis smuggles the conclusion). P2: if provable, the whole chain collapses to class 2 (RH ⟹ P1 given P2, so H ⟺ RH); if not provable, P1 is circular.
**Fallacies detected:** (i) appeal-to-novelty-without-mechanism (the "new object" D carries no certification machinery); (ii) equivocation: the 3-4-5-style positivity certifies the LINE Re(s)=1, not a half-plane — the argument silently upgrades "zero-free at σ=1" to "zero-free region"; (iii) circular reasoning in the unprovable-D branch.
**Verdict:** inference valid; premise stack unsustainable; chain dead absent a lemma no mechanism supplies.

### 8.4 FINAL VERDICT (confirmed, matches seed)
**NO SURVIVOR.** The in-lane one-way-condition space is exhausted by four structural outcomes: class-2 collapse (every zero-locus-preserving transfer), class-1 restatement (Mertens-O, PNT-one-way, GRH-folk), class-4 hypothesis-smuggling (multiplier with unprovable D), and mechanism-bound emptiness (positivity at Re=1; Laplace complex zeros; Herglotz ⟺-closed). **Closest route whose exact fatal flaw must be recorded:** Candidate A (Dirichlet-multiplier zero-free transfer) — a genuine one-way shape that dies on the missing lemma: *"there exists a fixed, ζ-independent arithmetic Dirichlet multiplier D with a certified zero-free half-plane Re>1/2"* — no mechanism can supply it (trichotomy); absent it, H either ⟺-degenerates or smuggles RH. The twin lane's nearest open lemma {log-concave density ⟹ real-rooted FT} is rigorously INCONCLUSIVE and moot (Φ fails the hypothesis). No proof, no numerical result claimed in this memo; the only numbers cited are closed-form algebra (Laplace witness roots, exact).

## 9. Next moves for the coordinator (ranked)

1. (cheap, decisive for §2's honesty) Run t1–t3 (§2) — pure f64 Rust, <30 min total. If t1/t2 confirm, Candidate A's mechanism stack is pinned dead; if t3 confirms η-mirroring, the class-2 collapse is demonstrated.
2. (no new lever expected) Do NOT fund any other candidate in this lane — the four deflation classes are now structurally populated.
3. If a future lane wants a one-way H ⟹ RH, the only unfunded shapes with non-vacuous controls remain OUTSIDE the Mellin/Dirichlet lane (per wave-17/18 synthesis: new objects, not new inequalities), and per the firewall, proportion theorems are zero RH evidence.