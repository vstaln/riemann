# Idea Generator: cross-domain attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (creativity + analogy + constraint + provocation). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Known facts are
labeled **PROVEN** (verified in sources read: the claude paper P, informal note N, B24/B25, Lean README
L — see literature-map.md) or **CHECKED NUMERICALLY**. Every *idea* is **CONJECTURED** by construction,
and each carries an explicit kill criterion. Vectors I already killed during generation are recorded in
§4 as ABANDONED (idea-stage) with the reason, so executioners don't re-derive the death.
Cross-references: attack-ceiling.md (the 0.6818 bandwidth-one ceiling is REAL), attack-kernel.md (the
cosine window is optimal for ζ), attack-mollifier.md (mollifier fusion is blocked at the same wall),
attack-multiplicity.md (2/3 simple, 5/6 distinct are hard walls of the two-moment method).

## 0. The honest map of where we stand (what new *input* could move what)

The method's output is a function of exactly these inputs (all PROVEN-in-Lean):
mean density (tr W_T = N), form factor on bandwidth 1 (‖W_T‖²_HS = (1/2 + (1/√2)cot(1/√2))·N),
integrality of multiplicities (rank–trace / k_c penalties), block structure (off-line pairs = (1,1)
planes). The ceiling theorem (PROVEN in Lean, `Zeta23/PairCeiling`) says: **no certificate reading
bandwidth-one data + integrality can certify more than 0.6818 simple zeros**, and the extremal law
realizing the ceiling is 256-periodic with F ≡ 1 up to α = 256 — i.e. it is *not* ruled out by the
pair-correlation conjecture. Therefore:

- Any *constant* gain for ζ itself (beyond 0.6818) requires **new input the ceiling law violates**:
  (a) form factor values beyond bandwidth 1 (none proven — this is Hardy–Littlewood territory, §7.5(a)),
  (b) higher-order correlations (triple+; the paper's HL*(k₀,λ) levers — CONJECTURED), (c) structural
  constraints on ζ's zeros that periodic laws violate (repulsion/rigidity/fluctuation structure —
  mostly unproven), (d) multiplicity structure (already priced optimally, attack-multiplicity).
- The *in-class* gap **0.6725 → 0.6818** is reachable with **proven inputs only** (a better certificate,
  not a better window — Theorem D is window-optimal, attack-kernel).
- New *targets* are reachable: ξ′/derivatives (constants PROVEN per paper), Dirichlet families
  (CONJECTURED in the paper, Rem 7.2(iii)), general Selberg-class statement (mechanical).

Vectors are ranked by expected value × feasibility. Effort: Low/Med/High (compute discipline: Rust for
CPU-bound, cache everything, run only what changes belief).

---

## 1. TIER 1 — attack now

### V1. The Weil-form spectrum experiment: the finite-rank "purity check"
- **Domain:** function-field geometry / RMT / statistical mechanics (merged).
- **Mechanism:** in char p, RH is the *purity* of Frobenius eigenvalues, certified by the positivity of
  the polarization (intersection form) on a *finite* 2g-dimensional space; the number-field analogue of
  the polarization is the compressed Weil form W_T, and RH ⟺ W_T ⪰ 0 for all T. The paper proves only
  n₊(W_T) ≥ 0.6725·N from two moments; the *full spectrum* of W_T is computable from the prime side.
- **Mapping:** W_T[k,l] = (T/(N∫φ²))·∫ dτ φ̂_T(τ−α_k)φ̂_T(τ−α_l)·ν_T(τ), ν_T = µ + λ_T + π_T — all prime
  side, no zero data. Diagonalize W_T (T ~ 10³–10⁴, N ~ 10³–10⁴, via B^t·Diag(ν)·B → M×M problem,
  M ~ 3N, Rust + faer). Under RH all eigenvalues ≥ 0; the theorem guarantees n₊ ≥ 0.6725·N.
- **Concrete first step:** build W_T at T = 10³ (N ≈ 1100) in Rust; print tr (≈ N), ‖·‖²_HS (≈ 1.3275·N),
  the full sorted spectrum, n₊, n₋, min/max eigenvalue; compare with (a) the extremal law's spectrum
  (2/3 ones, 1/6 twos, 1/6 zeros), (b) a GUE-like spread, (c) the *entropy/cumulants* of the empirical
  eigenvalue law.
- **What would falsify/kill:** if n₊ − 0.6725·N is tiny AND the eigenvalue law matches the extremal
  law's, the method wastes nothing (bad news: the certificate is near-optimal in the realized world).
  If n₋ ≈ 0 and min eigenvalue ≈ 0 with the law far from the extremal law, the method has real slack —
  fund the certificate search (V2) harder.
- **Effort:** Med. **s4h skill:** s4h-creativity-domain-transfer + s4h-investigation-triangulation.

### V2. The in-class certificate LP dual: close 0.6725 → 0.6818
- **Domain:** orthogonal polynomials / moment problems + machine proof (LP duality, Chebyshev
  alternation, certificate mining à la Flyspeck/kissing-number pipelines).
- **Mechanism:** the ceiling's extremal law is the optimum of a *linear program* over marked
  configurations; by LP duality its *dual* is a certificate (c₀, r). The paper's Theorem D certificate
  (value 0.6725) need not be the class-optimal one — 0.6818 is only an *upper* bound; achievability is
  open.
- **Mapping:** solve the dual LP over r ∈ C¹[0,1] (discretize to N points; the stability inequality
  `ceiling_stability` is the constraint), get the optimal r, verify it exactly (rational/polynomial),
  then Lean-verify like the paper's certificates.
- **Concrete first step:** read `Zeta23/PairCeiling/LawN256.lean`; solve the dual LP numerically
  (Rust LP) for the 256-law; read off the certificate value; compare to 0.6725.
- **Kill:** if the dual's optimum value is exactly Theorem D's 0.6725, the paper's certificate is already
  class-optimal and the 0.6818 ceiling is unreachable by *smooth* certificates — a documented finding.
  If it reaches ≈ 0.6818, we gain a real (small) constant and an adversarial re-verification of the
  ceiling.
- **Effort:** Med. **s4h skill:** s4h-constraint-hardness-testing + s4h-game-theory-mechanism-design.

### V3. Unconditional third moment in the *distinct*-count certificate (Rudnick–Sarnak range)
- **Domain:** RMT / orthogonal-polynomial moment problems.
- **Mechanism:** the paper's §7.5(e) says odd moments don't lower Λ₁(0) — but that claim is about the
  *on-line/simple* (n₊) functional. The *distinct* count (N_d, the c = 3 bookkeeping, 5/6) is a
  different functional; tr Â³ is *unconditionally evaluable* in the Rudnick–Sarnak range kλ < 2
  (λ < 2/3). Whether the third moment lifts the distinct bound 5/6 is a specific, checkable question
  the paper does not answer.
- **Mapping:** the k-moment generalization of the rank–trace inequality has penalties k_c(m) at higher
  order (the paper's §7.5(d) "Christoffel bound 1 − Λ_m(0)" is the mollifier-side analogue); feed
  tr Â³ = m₃·N (sine-kernel value 2, PROVEN-conditional/available at λ < 2/3 by the diagonal method)
  into the N_d bookkeeping and solve the LP.
- **Concrete first step:** write down the third-moment evaluation (Hejhal/Rudnick–Sarnak diagonal
  computation at λ = 2/3·(1−ε)) and the (tr, ‖·‖², tr Â³, integrality, n₊) LP for N_d; check whether
  5/6 improves.
- **Kill:** if the LP shows the third moment cannot move N_d (likely if the extremal world saturates the
  c = 3 inequality with equality on all higher moments too — the all-simple/tight-double world has
  moment sequence m_k = 1, 4/3, 2, 13/4..., matching GUE), the vector is a clean negative — document.
- **Effort:** Med. **s4h skill:** s4h-analogy-structure-mapping + s4h-constraint-scope-reduction.

### V4. Moment-order capacity LP: the "cost of missing data" roadmap
- **Domain:** information theory / complexity (channel capacity, rate–distortion).
- **Mechanism:** the 0.6818 ceiling is the *capacity* of the (mean, form-factor-on-[0,1], integrality)
  channel. Generalize: what is the capacity of the channel that ALSO feeds the triple correlation
  (GUE value S₃), or the 4th moment? This quantifies exactly what each conjectural input is worth —
  the paper's conditional levers (HL*(4,λ) → 13/18; full → 1) become a *curve*.
- **Mapping:** the 256-periodic marked law has computable higher correlation functions; add constraints
  S₃(j,k) = (GUE value) to the configuration LP and re-solve; the ceiling drops by a computable amount.
- **Concrete first step:** compute the law's triple-correlation statistic and re-solve the marked-law LP
  with S₃ pinned to the sine-kernel value; record the new ceiling.
- **Kill:** if pinning S₃ doesn't move the ceiling (the law's S₃ is already near-GUE — it is a
  *periodic* process, so its higher correlations may be far from GUE; check), the roadmap is empty.
- **Effort:** Low–Med. **s4h skill:** s4h-information-entropy + s4h-temporal-futures-mapping.

### V5. The F ≡ 1 support curve: verify the paper's 1.04 / 1.26 / 1.70 quantification
- **Domain:** RMT (pair correlation conjecture as a *parameterized* assumption).
- **Mechanism:** the paper's Remark 1.1 asserts that reaching 0.70/0.80/0.90 by the same route requires
  form-factor information on supports ≈ 1.04/1.26/1.70. This is a *quantification* of the value of a
  sliver of F beyond bandwidth 1 — it should be reproducible as a curve max-simple-fraction vs assumed
  bandwidth A (with F ≡ 1 on [1,A]).
- **Mapping:** re-run the certificate/ceiling LP with the *truncated* pair-correlation-conjecture data
  (form factor ≡ 1 on [0,A]); plot the certified proportion vs A.
- **Concrete first step:** extend the attack-ceiling LP code: maximize the certificate value against
  configurations with F ≡ 1 on [0,A]; compare with the Remark's three points.
- **Kill:** if the curve disagrees with the Remark's numbers, the Remark needs correction (a finding);
  if it agrees, the roadmap is validated and we know the exact price of each unit of bandwidth.
- **Effort:** Low. **s4h skill:** s4h-investigation-claim-decomposition.

### V6. Empirical form factor beyond 1 + spectral form factor from real zeros
- **Domain:** RMT / GUE (Odlyzko-style data analysis).
- **Mechanism:** Montgomery's form factor is a *measurable* object; reality (10⁴–10⁵ zeros computed in
  Rust) shows how close F(α) is to 1 for α > 1, and whether the *fluctuations* match the O(1/√log T)
  error of B24 Thm 1.
- **Mapping:** compute the normalized pair-correlation density and its Fourier transform (spectral form
  factor) for the cached 1000 zeros (34 digits) and for freshly computed zeros up to 10⁵; compare with
  GUE (K(τ) = τ, τ<1; 1, τ>1) and with the trivial bound F ≥ 0.
- **Concrete first step:** Rust: compute 10⁴ zeros (Euler–Maclaurin ζ, as in tools/), the pair
  correlation statistic, the form factor at α ∈ [0,3].
- **Kill:** if F(α) deviates wildly from 1 for α > 1 (not expected), the pair-correlation route is
  suspect; if it hugs 1, reality is consistent with the conjectural input that would crush the ceiling —
  motivating the (conditional) roadmap V5/V4.
- **Effort:** Low. **s4h skill:** s4h-investigation-triangulation.

### V7. The method sandbox: calibrate the certificate on known-true and known-false RH objects
- **Domain:** function fields / trace formulas (Selberg zeta) / L-function controls.
- **Mechanism:** in char p and for compact hyperbolic surfaces, the RH-analogue is *true* and the
  polarization is *canonical*; for Davenport–Heilbronn functions RH is false. Running the *same*
  rank–trace pipeline on all three tells us whether the certificate saturates at 100% when RH holds
  (method = perfect, deficit is arithmetic) or only at ~2/3 (method itself is the bottleneck).
- **Mapping:** the rank–trace machinery needs only (explicit formula, RvM density, Chebyshev-class
  prime sums, MV off-diagonal, FE pairing) — all available for: ζ with RH-forced zeros (replace off-line
  pairs by on-line), Davenport–Heilbronn (known off-line pairs; the paper already notes the certificate
  is "empty" — make it quantitative), and (harder) the Selberg zeta of a compact surface.
- **Concrete first step:** simulate the W_T spectrum (V1's code) on the "RH-true world" (all zeros on
  line, empirical ordinates) and on a "DH-style world" (a few percent off-line) and compare the
  certificate's value vs 0.6725.
- **Kill:** if the certificate also gives ≈ 0.6725 in the RH-true world, the two-moment method is
  inherently lossy and only new *inputs* can help (redirect to V4/V5); if it gives ≈ 1, the deficit is
  purely arithmetic and the extremal-law obstruction is the whole story.
- **Effort:** Med. **s4h skill:** s4h-creativity-perspective-shifting + s4h-investigation-counter-hypothesis.

### V8. Optimize the ξ′ window: the quartic is ad hoc — find the true optimizer of the ξ′ functional
- **Domain:** machine proof / numerical optimization (attack-kernel's CG machinery, reused).
- **Mechanism:** the paper's ξ′ constants (0.86864 quartic vs 0.85838 flat) come from an *ad hoc*
  quartic; the mechanism is explicitly CONJECTURED (paper states constants, not derivation; the
  functional differs from ζ's because ξ′'s explicit formula has different coefficients). The ζ functional
  is proven-optimized by the cosine; the ξ′ functional is *not* — numerical functional minimization may
  push 0.86864 higher.
- **Mapping:** replicate attack-kernel's optimizer on the ξ′ functional (needs the ξ′ explicit formula —
  in `Zeta23/XiPrime/`); minimize the ξ′-quotient over bandwidth-one positive windows.
- **Concrete first step:** recover the ξ′ functional from the Lean `XiPrime` files; run CG over window
  coefficients; compare Q(quartic) vs Q(optimizer).
- **Kill:** if the quartic is already near-optimal (like the cosine for ζ), no gain — but the *exact*
  optimal window/constant would still be a new proven-in-principle statement.
- **Effort:** Med. **s4h skill:** s4h-creativity-alternatives + s4h-constraint-rule-inversion.

### V9. The derivative tower: rank–trace for ξ″, ξ‴, … and Farmer-style combination
- **Domain:** trace formulas / spectral theory (Farmer–Gonek–Lee; the derivative method for distinct
  zeros).
- **Mechanism:** RH ⟹ RH(ξ^(j)) for all j (derivative of a real-rooted real entire function is
  real-rooted — Rolle/Laguerre, PROVEN classical), so the derivative tower is a *family of certificates
  on the same underlying zero data*. The paper made FGL's ξ′ constant unconditional via rank–trace; the
  extension to ξ″/ξ‴ is mechanical (explicit formulas for ξ^(j)/ξ^(j−1)), and FGL's pattern suggests the
  simple-on-line constants increase with j.
- **Mapping:** each ξ^(j) gives a rank–trace certificate; the *counts* interlace (N₀,ξ^(j+1) ≥
  N₀,ξ^(j) − O(1) by Rolle), and the zeros of all derivatives are determined by ζ's zeros — so the tower
  gives *joint* constraints on the same configuration.
- **Concrete first step:** derive the explicit formula for ξ″/ξ′ (pattern from the ξ′/ξ supplement),
  compute its functional, run the pipeline numerically; if the constant beats 0.85838/0.86864, formalize.
- **Kill:** if the constants *decrease* with j (FGL's own numbers go the other way, so this is
  unlikely), or if the ξ″ functional is degenerate (the explicit formula has a double-pole structure
  that breaks the (1,1)-plane bookkeeping), abandon.
- **Effort:** Med–High. **s4h skill:** s4h-analogy-domain-transfer.

### V10. Density + thin-box composition; and the shallow/deep off-line diagnosis
- **Domain:** effective/quantitative analytic number theory.
- **Mechanism:** (a) Unconditional density theorems (Ingham/Huxley/Bourgain, N(σ,T) ≪ T^{2(1−σ)+ε})
  bound the number of *deep* off-line zeros (|β−1/2| ≥ c/log T) by a fraction δ(c)·N; (b) Paley–Wiener
  (the paper's own Lemma 3.1 mechanism) exponentially suppresses the *contribution* of deep zeros to the
  HS norm (|φ̂_T(γ_ρ)| ≪ e^{−c/2+o(1)} at depth c/log T); (c) B25's b-parameterized Tsang-kernel
  positivity gives box-conditional constants C(b). Compose: run B25's machinery on the in-box zeros
  (≥ (1−δ(c))·N of them), bound the cross terms (in-box × out-of-box pairs) by Cauchy–Schwarz ×
  δ(c) × kernel decay, and check whether min_c[(1−δ(c))·C(b) − cross] beats 2/3. The *diagnosis* side:
  shallow off-line pairs (depth < O(1/log T)) are the only structure the method cannot price — density
  theorems cannot touch them, and they are exactly what B25's box hypothesis permits.
- **Mapping:** the honest first step is *bookkeeping*: write the composed bound, check the cross-term
  cost (my rough estimate: the e^b positivity-loss at b ~ 1 eats everything — B25's own table shows
  C(1) = 0.617 already with *all* zeros in the box, and δ(c) ≥ 26% at c = 1 — expect death, but it is
  cheap to settle and the shallow/deep split is itself a valuable framing result).
- **Kill:** if the composed constant ≤ 2/3 for all c (expected), record as documented negative; the
  diagnosis ("the irreducible unknown is the shallow off-line count") is the lasting output.
- **Effort:** Med (likely negative). **s4h skill:** s4h-constraint-hardness-testing.

---

## 2. TIER 2 — fund after Tier 1

### V11. Unconditional CGdL20-style SDP certificate (0.6792 under RH — can it be made unconditional?)
- **Domain:** RMT / semidefinite programming (Chirre–Gonçalves–de Laat majorant method).
- **Mechanism:** CGdL20's 0.6792 uses F ≥ 0 *pointwise* outside [−1,1] as a majorant constraint — but
  their input F ≡ 1 on [−1,1] needs RH. The *unconditional* form factor (B24 Thm 1) has the same
  integrated values on [−1,1] (that is the paper's Lemma 3.3) plus F ≥ 0 for all α (from the L²
  representation, PROVEN) — the question is whether the B24 error terms (O(1/√log T), the T^{−2α} term)
  permit the same SDP *without* RH.
- **First step:** re-run CGdL20's SDP with the B24-unconditional constraints; compare the value with
  0.6725 (paper) and 0.6792 (under RH). **Kill:** if the error terms force the value back to ≤ 0.6725
  (likely — the errors are of size 1/√log T at the *constant* scale), record; the paper's claim that
  CGdL20 "operates in a different regime" gets a quantitative confirmation.
- **Effort:** Med–High. **s4h skill:** s4h-analogy-structure-mapping.

### V12. The Dirichlet-family program: make C Rem 7.2(iii) rigorous (family-averaged 2/3)
- **Domain:** RMT families (Iwaniec–Luo–Sarnak 1-level density machinery) + sieve/Bombieri–Vinogradov.
- **Mechanism:** averaging over χ mod q kills the off-diagonal prime sums by orthogonality, restoring
  bandwidth 1 for the *family*; the paper says this "requires a different (Gevrey-class) taper … and is
  not carried out here" (CONJECTURED in the paper). The *ingredients* are all proven (explicit formula,
  RvM, Stirling, MV, character orthogonality, BV-type error bounds) — the assembly is a research program.
- **First step:** test the mechanism numerically first: for a fixed large q, T = (log q)^c, compute the
  family-averaged HS norm with the orthogonality-killed off-diagonal and check the bandwidth-1
  restoration. **Kill:** if the Kloosterman/error terms fail to be negligible at the required precision
  (the Gevrey taper is forced precisely because the ordinary taper leaves error terms too large).
- **Effort:** High. **s4h skill:** s4h-creativity-domain-transfer + s4h-strategy-terrain.

### V13. Selberg-CLT / distributional certificate: exclude the extremal law by fluctuations
- **Domain:** statistical mechanics / determinantal point processes (rigidity, hyperuniformity).
- **Mechanism:** ζ's counting fluctuations are *proven* Gaussian of size √(log log T) (Selberg's CLT,
  unconditional); the 256-periodic extremal law is a *deterministic crystal* at scale 256 — its
  long-interval count variance is O(1), not √(log log T). If the certificate class could read *any*
  fluctuation-statistic input, the extremal law is excluded and the ceiling collapses.
- **First step:** compute the count-variance statistic for the extremal law vs ζ's actual zeros over the
  grid scale; check whether the leading fluctuation is *determined* by the bandwidth-one form-factor
  data (it is, at leading order — F near 0 fixes the variance) — if so, kill. **Kill:** the variance is
  fixed by small-α form-factor data the law already matches; the *distribution shape* (Gaussian vs
  deterministic) is a different-T statistic with no known mechanism to enter a per-T certificate.
- **Effort:** Med (likely negative). **s4h skill:** s4h-information-entropy + s4h-psychology-cognitive-biases.

### V14. Bethe-ansatz equations for the zeros (LeClair–Mussardo) — validate, then check Re ρ = 1/2
- **Domain:** integrable systems / Hilbert–Pólya (S-matrix bootstrap; a 2010s development).
- **Mechanism:** conjectured algebraic systems whose solutions reproduce the low-lying zeros to high
  precision; if the system *structurally* forces real solutions, it is a Hilbert–Pólya realization.
- **First step:** reproduce LeClair–Mussardo's numerics with the cached 1000 zeros (34 digits) at high
  precision; determine the failure height (their equations are known to be heuristic — where do they
  break?). **Kill:** if the equations fail beyond the first ~50 zeros (expected), or if the system's
  real-solution property is equivalent to RH by inspection.
- **Effort:** Med. **s4h skill:** s4h-investigation-source-trace.

### V15. Sierra / Berry–Keating finite spectral check
- **Domain:** Hilbert–Pólya (the x̂p̂ operator with a self-adjoint-extension trick).
- **Mechanism:** if a specific, explicitly defined operator is self-adjoint on its domain, its spectrum
  is real and RH follows. Sierra's construction gives a Hilbert space where the eigenvalues are
  *conjecturally* the zeros; the self-adjointness of the domain is the (missing) rigorous core.
- **First step:** numerically verify the claimed spectrum against the first 100 zeros and test the
  domain conditions (the "sawtooth" boundary conditions) on finite truncations; check whether any
  truncation produces non-real eigenvalues. **Kill:** non-real eigenvalues at any truncation, or the
  known fact that the construction only matches the Weyl law asymptotically (no exactness beyond
  numerics).
- **Effort:** Low–Med. **s4h skill:** s4h-creativity-provocation (bounded version).

### V16. Finite Hermite–Biehler shadow of the signature method (de Branges / Burnol)
- **Domain:** Hilbert–Pólya / de Branges spaces / Burnol's explicit-formula framework.
- **Mechanism:** RH ⟺ Ξ(t) = ξ(1/2+it) is in the Hermite–Biehler class; the paper's signature method is
  the *finite-dimensional* shadow (the compressed form's positive index). Burnol's framework makes the
  explicit formula a spectral measure of a concrete unitary map — a reformulation that may reveal which
  *test-function classes* admit unconditional positivity.
- **First step:** reformulate the rank–trace inequality as a finite Hermite–Biehler condition and test
  numerically whether a strengthened finite condition holds for the actual Ξ (diagnostic only).
  **Kill:** any reformulation that is exactly equivalent to RH with no new provable fragment (expected
  for the infinite version; the finite version is the paper's method renamed).
- **Effort:** Low–Med. **s4h skill:** s4h-epistemology-epistemic-status.

### V17. DPP rigidity / repulsion inputs — inventory of what a certificate could read
- **Domain:** determinantal point processes (sine kernel, rigidity, repulsion exponents).
- **Mechanism:** the sine-kernel process has strong repulsion (P(two points within ε) ~ ε³) and number
  rigidity; the extremal law has *doubles* (marks = 2) and lattice structure. Any *proven* repulsion or
  "no close pairs" statement for ζ usable inside a certificate would break the ceiling. (Known: only
  weak gap lower bounds are proven; B24's F ≥ 0 is an inequality, not a repulsion value.)
- **First step:** a literature-scoped writeup (what repulsion/rigidity is proven for ζ's zeros,
  unconditional or under RH) with labels. **Kill:** if nothing proven is usable as a certificate input
  (expected — this vector is a documentation deliverable).
- **Effort:** Low. **s4h skill:** s4h-ecology-interdependence.

### V18. Multi-window Gabor compressions (oversampled frames)
- **Domain:** frame theory / approximation theory.
- **Mechanism:** a second window (or higher Gabor density) enlarges the compressed space; the Poisson
  completion (Claim 2.1) breaks with oversampling (aliased modes) — but a *second* window at the same
  critical density is clean and doubles the dimension. The rank–trace scales with dimension; the ratio
  ‖·‖²/tr is what matters — likely no gain, cheap to check.
- **First step:** build the block W for two windows (cosine + flat), compute the two moments, run the
  rank–trace; compare the constant. **Kill:** if the two-moment ratio is unchanged (expected — the
  extremal configuration re-normalizes).
- **Effort:** Low. **s4h skill:** s4h-creativity-alternatives.

### V19. Selberg-class unification theorem
- **Domain:** analytic number theory (Selberg class axioms) / logic (axiomatization).
- **Mechanism:** the rank–trace pipeline uses only: functional equation (ρ ↔ 1−ρ̄ pairing), RvM
  (density), explicit formula (prime sums), Chebyshev-class bounds (ΣΛ(n)²/n), Montgomery–Vaughan
  (off-diagonal). All are consequences of the Selberg-class axioms for degree 1 — the ζ and Dirichlet
  theorems are corollaries of one axiomatic theorem.
- **First step:** state the axiomatic theorem (degree 1, archimedean factor data as parameters) and
  check which axioms are used where; the GL(2) death (bandwidth 1/2 < threshold, C Rem 7.2(ii)) becomes
  a *class-level* statement. **Kill:** if a Selberg-class function fails one of the axioms in a way the
  method silently exploits (e.g., needs more than the axioms give).
- **Effort:** Low–Med. **s4h skill:** s4h-logic-argument-validation.

### V20. Effective finite-T version of the 67.25% theorem
- **Domain:** effective/quantitative analytic number theory + machine proof.
- **Mechanism:** the paper's errors are o_T(1)/O(log T)-class (non-effective); an effective statement
  "≥ 0.6725·N(T,2T) − E(T) with explicit E(T)" is the natural companion to the Lean ε-form statements
  and to the computational-RH data (verification to height 10¹³).
- **First step:** track the constants through N Lemma 3.3's error chain (Paley–Wiener, Chebyshev,
  Stirling, MV) and assemble an explicit E(T); validate against V1's finite-T numerics. **Kill:** if the
  assembled E(T) is larger than the main term's constant gap at every feasible T (i.e., the theorem is
  vacuous for all computable T), it is documentation-only.
- **Effort:** Med–High. **s4h skill:** s4h-writing-technical.

---

## 3. The precise function-field obstruction (brief question 1, answered head-on)

**PROVEN facts about the char-p proofs (Weil, Deligne):** RH for curves over 𝔽_q is the *purity*
statement |α| = q^{1/2} for the eigenvalues of Frobenius on H¹(étale, ℓ-adic). The proof has exactly
three structural ingredients the number-field side lacks:

1. **A finite-dimensional cohomology realization.** H¹ of the curve is a finite-dimensional Q_ℓ-vector
   space (dimension 2g) carrying a Frobenius endomorphism; the zeros ARE its eigenvalues. The number
   field side has no such realization: the "motive" of ζ would be a degree-1 motive over ℚ whose
   existence, functoriality, and finite dimensionality are the (open) standard conjectures. The
   functional equation gives the *duality* (Poincaré duality pairings α ↦ q/α) but not the space.
2. **The polarization.** The Riemann hypothesis in char p is certified by the *positivity of the
   intersection form on the Jacobian* (Néron–Tate/Weil height pairing, i.e. Hodge-index/polarization of
   the Hodge structure). RH for ζ is *by definition* (Weil's criterion) the positivity of the Weil
   quadratic form on ALL test functions. The paper's W_T is the *finite-rank truncation* of the would-be
   polarization; its (1,1) hyperbolic planes from off-line pairs are exactly the failure of positivity.
   In char p there are no off-line "pairs" because the polarization is canonical. **This is the precise
   obstruction: importing the char-p proof = constructing a polarization = proving RH. What transfers is
   the finite-dimensional form of the argument: the rank–trace bound IS the finite-dimensional
   polarization theorem, and its 2/3 deficit is the missing Hodge structure, not a missing technique.**
3. **The Lefschetz trace formula + finite determinacy.** The point count #X(𝔽_q) = Σ(−1)^i tr(F|H^i)
   is a *finite* sum; Newton's identities make the eigenvalue multiset determined by finitely many power
   sums, and the *integrality* of those power sums (traces of Frobenius = integers) is what forces
   algebraic-integer structure. The number-field analogue: the power sums Σ_ρ γ_ρ^k ARE computable from
   primes via the explicit formula, and the Hankel matrices of these moments are the Weil form in
   disguise — finite-rank Hankel positivity is provable (the paper's method); the infinite Hankel
   positivity IS RH. **The transferable *new* idea is the sandbox (V7) and the Newton/Hankel reading
   (W3): test where the finite determinacy provably breaks down.**

The one char-p mechanism with no number-field analogue at all: **Hodge theory gives the polarization
automatically.** Nothing in the number-field toolkit provides even a *sliver* of canonical positivity —
which is why every route reduces to computing moments and signatures of the (conjectural) polarization,
i.e. to the paper's method. This *justifies* funding the certificate-side work (V2, V4, V5, V7) over
more "geometric" imports.

---

## 4. WILD vectors — PROVOCATION (de Bono: deliberately absurd premises, evaluated honestly)

### W1. "The zeros are EXACTLY the eigenvalues of a known operator — only the domain is missing"
- **Domain:** Hilbert–Pólya, strongest form.
- **FOR:** the Sierra/Berry–Keating construction reproduces low-lying zeros numerically; the
  classical-Hamiltonian Weyl law matches the zero density *exactly* in form; a self-adjoint operator
  whose *asymptotic* spectrum matches the zeros would force RH if the exactness could be proven; the
  check is finite-dimensional and cheap.
- **AGAINST:** no accepted construction exists; all known candidates reproduce only the *density*
  (Weyl law), and the zero-by-zero agreement is heuristic; the "sawtooth" quantization is known to be
  non-self-adjoint on natural domains; exactness at the eigenvalue level is exactly as hard as RH.
- **First step:** V15's numerical self-adjointness/spectrum check on finite truncations. **Kill:** any
  non-real eigenvalue or any truncation-order mismatch beyond numerical error.
- **Effort:** Low–Med. **s4h skill:** s4h-creativity-provocation.

### W2. "We only need the first 10¹³ zeros"
- **Domain:** computational data (Gourdon–Demichel verified 10¹³ zeros simple and on the line; our
  tools cache 1000 to 34 digits).
- **FOR:** the verified configuration is a *fact*; the certificate's value on the *real* data directly
  measures the gap between proven (67.25%) and measured (≈100%); if the gap is large, the method's
  slack is a *proof artifact*, justifying the certificate hunt; a finite configuration can be fed to the
  LP as a constraint (the extremal law must be compatible with the real configuration's statistics).
- **AGAINST:** a finite measurement cannot enter a liminf statement; the extremal law was built to match
  bandwidth-one data that a *single* finite configuration also matches approximately; the "measured
  ≈100%" is exactly RH-below-T, which we already know and cannot extend.
- **First step:** the V1 spectrum on the real zeros (which IS the W2 measurement). **Kill:** if the
  real-data certificate value is ≈ 0.6818 (the ceiling), the finite data adds nothing beyond the theory.
- **Effort:** Low (folds into V1/V6). **s4h skill:** s4h-constraint-rule-inversion.

### W3. "RH is the infinite-rank Newton/Hankel moment problem — and the finite ranks are computable"
- **Domain:** function fields (Newton's identities) / classical moment problems.
- **FOR:** the power sums Σ_ρ γ^k are computable from primes (explicit formula, diagonal terms only!);
  the Hankel matrices H_k = [m_{i+j}] are positive semidefinite iff the moments come from a positive
  measure on ℝ (i.e., iff the zeros are on the line!) — so RH ⟺ Hankel positivity of the *moment
  sequence of the zero distribution*, and finite-rank Hankel determinants are *computable diagnostics*
  that should show a clear positivity-with-margin pattern if RH holds.
- **AGAINST:** the moments are not unconditionally computable to the needed precision (off-diagonal /
  far-zero terms pollute them — the same bandwidth wall); the finite Hankel positivity is exactly the
  paper's signature method renamed; the infinite positivity is exactly RH — no free lunch, but the
  *numerical margin* of the finite Hankel determinants is a genuinely new measurement.
- **First step:** compute det H_k for the *normalized* ordinate distribution of the cached zeros and of
  V6's 10⁴ zeros; look at the smallest eigenvalue's margin as k grows. **Kill:** if the margin collapses
  at the resolution of the data (expected at the bandwidth limit), the measurement carries no signal
  beyond V1.
- **Effort:** Low. **s4h skill:** s4h-analogy-structure-mapping + s4h-creativity-provocation.

### W4. "A non-commutative-geometry reformulation admits a computation"
- **Domain:** non-commutative geometry (Connes/Connes–Consani: RH as a Sobolev-type norm inequality).
- **FOR:** Connes's reformulations are rigorous *conditional* equivalences — RH ⟺ a specific norm
  inequality on a specific Hilbert space; such inequalities are *finite-rank checkable*; the Bost–Connes
  partition function is literally ζ.
- **AGAINST:** the equivalence is only as good as the (deep, hard-to-verify) construction; every attempt
  to *use* the reformulation has re-derived known equivalences; the Sobolev inequality's verification
  would be as hard as RH; no computational shortcut is known.
- **First step:** numerically test the Connes–Consani norm inequality on a family of test functions
  (finite subspaces); if it *fails* numerically the formulation is wrong (interesting!); if it holds
  with margin, it's a hint only. **Kill:** the check cannot be distinguished from the paper's own
  signature computations (expected).
- **Effort:** Low. **s4h skill:** s4h-creativity-perspective-shifting.

### W5. "The phantom Frobenius: solve for the 2N×2N matrix whose power sums are the prime moments"
- **Domain:** function-field geometry (the missing operator), numerically inverted.
- **FOR:** the explicit formula gives the power sums tr(F^k) = Σ_ρ γ_ρ^k for the *hypothetical*
  operator; a matrix with those traces exists iff the moment sequence is realizable (Hankel positivity —
  see W3); if a *unitary* choice existed, purity (= RH) would follow; the finite problem is a concrete
  numerical linear algebra problem.
- **AGAINST:** the moments are polluted by off-diagonal terms beyond the bandwidth (same wall); the
  realizability of finite truncations is the paper's method; choosing F unitary is exactly RH; no
  numerical solution can prove the infinite case.
- **First step:** fold into W3/V1 (the Hankel/Hermitian realization of the finite moments). **Kill:**
  same as W3.
- **Effort:** Low. **s4h skill:** s4h-creativity-provocation.

---

## 5. ABANDONED (idea-stage, documented so executioners don't re-derive the death)

### A1. Goldston–Montgomery variance for the beyond-bandwidth-1 off-diagonal
- **Idea:** use the proven second-moment of primes in short intervals to control the λ_T·λ_T
  off-diagonal for X > T (α > 1).
- **Death (derived here):** the GM variance controls *fluctuations*, but the off-diagonal's obstruction
  is its *mean*: Σ_{|log n − log m| ≤ δ} Λ(n)Λ(m) has main term ~ (2δ)·X² (via ψ(x) ~ x), which is
  X/log T ≫ diagonal X·log²X for X = T^{1+ε}. The mean is Hardy–Littlewood-strength input; the variance
  is irrelevant. **The paper's §7.5(a) is the exact statement of this wall.**
- **Effort:** Low (already spent). **s4h skill:** s4h-constraint-hardness-testing.

### A2. Odd-window / imaginary-part off-line counter
- **Idea:** an odd (or complex) window makes the off-line pairs contribute to Im(W_T); rank(Im W) would
  count off-line pairs directly.
- **Death (derived here):** the functional equation pairs ρ with 1−ρ̄ at the *same height*; their
  contributions to Im(vv^t) are exact negatives (v_{1−ρ̄} = conj(v_ρ) in the completed frame, Schwarz
  reflection), so Im(W_T) ≡ 0 identically. No rank to measure.
- **Effort:** Low (already spent). **s4h skill:** s4h-logic-consistency-check.

### A3. Small-support Weil positivity as a certificate input
- **Idea:** proven positivity of the Weil form on small Fourier support could add independent PSD
  constraints to the certificate.
- **Death:** the classical small-support positivity holds only in the trivial regime (Fourier support
  below the first zero height, where the zero sum vanishes and the Γ-part dominates) — it does not
  overlap the bandwidth-1 window regime (support ~1/log T around height T). No usable overlap.
- **Effort:** Low (already spent). **s4h skill:** s4h-investigation-counter-hypothesis.

### A4. Joint (ξ, ξ′) interlacing LP
- **Idea:** Rolle interlacing between real zeros of ξ and ξ′ gives a joint constraint that the
  single-function ceiling law might violate; maximize the simple fraction subject to both certificates
  and interlacing.
- **Death:** interlacing gives only the *lower* bound N₀,ξ′ ≥ N₀,ξ − 1 (a real function's derivative
  can have arbitrarily many more real zeros than the function — the "wiggle" counterexample); there is
  no usable *upper* constraint, so the joint LP is empty. Note: this also kills the naive "85.8% for ξ′
  implies ≥85.8% for ζ" fallacy — it does not.
- **Effort:** Low (already spent). **s4h skill:** s4h-logic-argument-validation.

### A5. Trivial upper bound on the beyond-1 off-diagonal
- **Idea:** bound Σ_{|log n−log m|≤δ}Λ(n)Λ(m) ≤ 2δ·X² by ψ(x) ~ x and feed it to the certificate.
- **Death:** 2δX² ≫ (main term)·(X/T) — the certificate's tolerance is a *constant* (the in-class gap
  0.6725 → 0.6818 is 1.4%); any polynomial-in-X loss kills it. No proven bound with a log-factor gain
  changes this.
- **Effort:** Low (already spent). **s4h skill:** s4h-constraint-scope-reduction.

---

## 6. TOP 10 for immediate attack (expected value × feasibility)

1. **V1 — Weil-form spectrum experiment** (signature/eigenvalue law from the prime side; validates
   Lemmas 3.2/3.3 and measures the method's real slack). Med.
2. **V2 — In-class certificate LP dual** (close 0.6725 → 0.6818 with proven inputs; also an adversarial
   re-check of the ceiling). Med.
3. **V3 — Unconditional tr Â³ in the distinct-count certificate** (λ < 2/3, Rudnick–Sarnak; may beat 5/6
   or cleanly fail). Med.
4. **V5 — F≡1 support curve** (reproduce the 1.04/1.26/1.70 quantification; validate the roadmap). Low.
5. **V4 — Moment-order capacity LP** (what each conjectural correlation input is worth; the conditional
   roadmap). Low–Med.
6. **V6 — Empirical form factor beyond 1** (reality vs conjecture calibration on real zeros). Low.
7. **V7 — Method sandbox** (certificate value on RH-true vs RH-false worlds; is the method the
   bottleneck?). Med.
8. **V8 — ξ′ window optimization** (the quartic is ad hoc; true optimizer may push 0.86864). Med.
9. **V9 — Derivative tower ξ″, ξ‴** (mechanical extension, FGL pattern suggests higher constants). Med–High.
10. **V10 — Density + thin-box bookkeeping + shallow/deep diagnosis** (likely negative; cheap to settle;
    the lasting output is the diagnosis: shallow off-line pairs are the irreducible unknown). Med.

**Strategic reading of the tier-1 list:** V1/V5/V6/V7 are *diagnostics* (they tell us how much headroom
exists and whether the certificate or the arithmetic is the bottleneck — they change what we believe);
V2/V3 are the only *proven-inputs* paths to a new constant for ζ; V8/V9 are new-target paths with proven
machinery. V4 prices the conjectural inputs so a later round can decide which conjecture is cheapest to
attack. Nothing here claims to settle RH; the goal is rigorous movement and honest negative results.

## Label inventory

- PROVEN (in sources read): the 67.25%/2/3/5/6/0.83625 theorems and their inputs; the 0.6818 ceiling
  (Lean); window optimality; the multiplicity walls; the ξ′ constants; B24/B25 form-factor facts; the
  Selberg CLT (classical, as stated in the literature map's chain).
- CONJECTURED (invented here, each with a kill criterion): V1–V20, W1–W5.
- ABANDONED (idea-stage, reason documented): A1–A5.
