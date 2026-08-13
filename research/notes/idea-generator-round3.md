# Idea Generator — Round 3: Cross-Domain Attack Catalog

**Agent:** idea-generator (subagent, architect profile).
**Date:** 2026-08-13. **Round:** 2 → 3.
**s4h methods applied:** s4h-analogy-domain-transfer (structural similarity between RH and solved
problems in unrelated fields) + s4h-creativity-provocation (deliberately impossible statements as
springboards, each inverted into a testable hypothesis). Every idea below is a *hypothesis to kill*,
not a claim.

**Scope discipline:** Round 2's catalog (`attack-vector-catalog.md`) already funds V1–V20, L1–L9,
M28/M29, and records A1–A5 as PROVEN DEAD. This file **excludes** all of those. The structural verdict
(`structural-final-verdict.md`) says the frontier is now the *simple fraction p₁* (multiplicity /
beyond-bandwidth-1 form factor), NOT certificate optimization — so the genuinely new ideas below
disproportionately import machinery that could yield a **new unconditional multiplicity or
correlation input**, or a **new certificate class** outside the exhausted coboundary family.

**Honesty:** every idea is CONJECTURED. No theorem or citation below is asserted as real; every
"maps to X in the literature" note names the *structural* cousin only, to be chased by a literature
agent before any belief is updated. Kill-criteria are the minimal computation that refutes each idea.

---

## 1. Anderson localization / Wegner estimate (physics: spectral theory of random operators)

**(a) Import + analogy.** In disordered quantum systems, *extended* (delocalized) eigenstates are
generic and *localized* states are measure-zero pathologies suppressed by a **Wegner estimate**: the
eigenvalue count in a tiny interval [E, E+ε] is ≲ C·ε, so eigenvalues cannot pile up (degeneracies
cost "energy" and are exponentially unlikely). **Provocation:** "off-line zeros are free" → invert:
off-line zero pairs (ρ, 1−ρ̄) should appear as *near-degenerate low eigenvalues* of the truncated Weil
form W_T, because they contribute an extra soft mode to the quadratic form. If W_T behaves like a
disordered operator with a Wegner estimate, those near-degeneracies are forbidden and p₁ is forced up.

**(b) Concrete object.** The truncated Weil form W_T on the window `tools/finitet` constructs; its
eigenvalue counting function N(λ) on a small window [0, ε]. An off-line pair is CONJECTURED to create
a pair of eigenvalues within ~ (distance off-line) of each other near the bottom of the spectrum.

**(c) Minimal check.** Numerically (Rust, reusing `tools/finitet`): (i) measure N(ε) for ε ↓ 0 and
test whether N(ε) ≤ C·ε (Wegner-type) or exhibits a jump (degeneracy pile-up); (ii) in the synthetic
forced-off-line world already built in `finitet` §4.7, inject one off-line pair and check whether it
materializes as a near-degenerate eigenvalue pair. Kill = no eigenvalue signature of off-line pairs;
survive = a *proven* Wegner estimate for W_T would bound the number of near-degenerate low modes and
hence the multiplicity Σ(m_ρ − 1), which is exactly the missing p₁ input.

**(d) Verdict: PROMISING.** Maps to Wegner's 1981 estimate for random Schrödinger operators and to
Montgomery pair correlation (which already forces eigenvalue repulsion); the novel content is turning
repulsion into a *multiplicity* bound, which no round-1/2 file does.

---

## 2. Renormalization-group decimation of the explicit formula (physics: RG / multiscale analysis)

**(a) Import + analogy.** In RG, coarse-graining high-frequency modes leaves a scale-invariant fixed
point; the flow of couplings between scales either runs to a fixed point (massless theory) or to 0/∞
(massive). **Provocation:** "the prime side is one scale" → invert: the explicit formula's
off-diagonal prime-pair sum Σ_{p,q} Λ(p)Λ(q)⟨g(log p), g(log q)⟩ is naturally graded by dyadic bands
of log p. Decimate band-by-band (block the highest log p band, renormalize the effective window).
RH = the decimation flow has a single nontrivial fixed point (the sine-kernel / GUE), and the fixed
point is the 256-periodic near-CUE law's *continuum* completion.

**(b) Concrete object.** The band-truncated off-diagonal quadratic form Q^{(k)} obtained by
restricting Λ(p) to the k-th dyadic band 2^k ≤ p < 2^{k+1}; the RG "coupling" g_k = Q^{(k)}/Q^{(k−1)}.

**(c) Minimal check.** Compute g_k for k = 1…~20 (X up to ~10⁷, Rust sieve) and test whether g_k
converges to a constant (fixed point) or decays/grows. Prediction to falsify: g_k → const ≈ 2
(sine-kernel scale), NOT → 0 or ∞. Survive = scale invariance of the prime-pair structure is a real
property, motivating a transfer-matrix / exact-RG treatment of the beyond-bandwidth-1 form factor
(the F(α), |α|>1 question that `structural-final-verdict.md` calls the whole game).

**(d) Verdict: SPECULATIVE.** Maps to Kadanoff block-spin decimation; the "prime side is
self-similar across log-scales" hypothesis is UNVERIFIED and might simply reflect the
Hardy–Littlewood / prime-number-theorem uniformity already used in the literature.

---

## 3. Stabilizer-code distance (cryptography: quantum error correction)

**(a) Import + analogy.** A quantum stabilizer code is the simultaneous +1 eigenspace of a set of
commuting symmetries (stabilizers); *logical errors* are operators that commute with the stabilizer
but act nontrivially on the code, and the code's **distance** = minimum weight of a logical error.
**Provocation:** "the functional equation is just a symmetry" → invert it into a *code*: the
functional equation s ↔ 1−s (with its reflection on ordinates γ ↔ −γ, ρ ↔ 1−ρ̄) is the stabilizer;
on-line zeros are codewords; an off-line pair (ρ, 1−ρ̄) is a *logical error* of weight 2.

**(b) Concrete object.** The finite analogue: the commutant of the reflection operator on the
Galerkin subspace where W_T lives — i.e. the algebra of matrices commuting with the symmetry that the
functional equation induces on the coefficient vectors v (this is exactly the even/odd split the
method already exploits, but treated as a *code* with a distance).

**(c) Minimal check.** Compute (Rust, `tools/finitet` matrices) the dimension of the commutant of the
reflection on the N-dimensional Galerkin space and the minimum "weight" (number of off-line
coordinates) a vector in the code space can have. Prediction to falsify: the code distance d satisfies
d ≥ 2·(N₀/N) with N₀ the on-line count, forcing off-line pairs to be weight-≥2 errors. Kill = the
commutant structure carries no information beyond the inertia count (n₊, n₋) already measured; survive
= the code distance is a *new* invariant bounding the number of off-line pairs from the symmetry alone.

**(d) Verdict: SPECULATIVE.** Maps to stabilizer codes (Gottesman 1997) and to the even/odd
decomposition of the Weil form (PROVEN, `[kernel]`); the risk is that "code distance" is exactly the
rank–trace inertia already computed, i.e. ALREADY-KNOWN in disguise.

---

## 4. Channel polarization (information theory: polar codes)

**(a) Import + analogy.** Polar codes synthesize N "virtual channels" from a base channel; under the
polar transform, each virtual channel's **Bhattacharyya parameter** Z ∈ [0,1] polarizes to 0 (clean,
reliable) or 1 (pure noise). **Provocation:** "every zero is individually uncertain" → invert: the
finite off-diagonal prime-pair covariance matrix C (the Gram matrix of the g(log p) vectors) is the
"channel"; its eigen-directions with large eigenvalue are the reliable channels (they *carry* the
on-line zeros), and directions with eigenvalue → 0 are the pure-noise channels (they would *have to*
carry off-line zeros).

**(b) Concrete object.** The eigendecomposition of C (the same matrix whose HS norm
‖W_T‖²_HS/N → 1.3275 is already measured, `[finitet §3]`); the polar-transform analogue is
repeatedly applying the 2×2 kernel to the sorted eigenvalue list and tracking Z.

**(c) Minimal check.** Compute the sorted eigenvalue spectrum of C and the induced Bhattacharyya
parameters Z_i = 2√(λ_i λ_{i+1})/(λ_i + λ_{i+1})-type functional; test whether the Z_i concentrate
near {0,1} (polarization) with a *sharp* transition, and whether the number of near-1 (noise)
channels matches the deficit 1 − 0.6725. Kill = smooth spread of Z_i (no polarization ⇒ no new
information); survive = a sharp noise-channel count that *bounds* the off-line fraction from the
covariance spectrum alone.

**(d) Verdict: SPECULATIVE.** Maps to Arıkan 2009 polar codes; the eigenvalue spectrum of C is
partially measured in V1 but not interpreted as a polarization channel, so the *reading* is new even
though the matrix is old.

---

## 5. Toeplitz / Fisher–Hartwig symbol of the window (spectral theory)

**(a) Import + analogy.** For Toeplitz/Hankel determinants generated by a symbol with jump-type or
algebraic singularities, the Szegő–Widom / Fisher–Hartwig asymptotics decompose the determinant into a
smooth (Szegő) part plus explicit singularity contributions — a *jump* in the symbol is exactly what
breaks the leading-order law. **Provocation:** "the window is smooth" → invert: the certificate's
generating function (the window φ̂_T's z-transform) has a *Fisher–Hartwig singularity* precisely when
off-line zeros are present, because off-line zeros put a branch point on the critical line that
punctures the symbol.

**(b) Concrete object.** The symbol a(z) = Σ φ̂_T(n) z^n of the window (a Laurent polynomial/analytic
function on the unit circle); its Fisher–Hartwig singularity set; the Hankel-determinant / spectral
asymptotics of the truncated W_T generated by it.

**(c) Minimal check.** Compute log det(W_T restricted) vs the Szegő–Widom prediction for the *smooth*
symbol, and test whether the residual is of order O(1) (smooth ⇒ no off-line) or contains a
Fisher–Hartwig term of the form ∝ (1−z)^{-α} with α ≠ 0. Kill = residual matches smooth Szegő
exactly (off-line zeros leave no symbol singularity); survive = a nonzero FH exponent α is a
*diagnostic* that, inverted, gives a criterion for on-line-ness.

**(d) Verdict: ALREADY-KNOWN (partial).** Maps to the classical Szegő theorem and Fisher–Hartwig
(1968); the Hankel-determinant margin is W3 `[crossdomain V6/W3]`, but the *symbol-level*
Fisher–Hartwig reading of the window's z-transform is not in any round-1/2 file — worth a one-shot
check only, given the W3 overlap.

---

## 6. Permutation-pattern avoidance in the spacing sequence (combinatorics)

**(a) Import + analogy.** Stanley–Wilf theory: a permutation class avoiding a fixed pattern π grows
at most exponentially (growth rate = Stanley–Wilf limit), whereas unconstrained permutations grow
factorial. **Provocation:** "zeros are a random permutation" → invert: map the normalized spacing
sequence of the zeros to a permutation (via the rank of consecutive gaps); an off-line zero pair
CONJECTURED to force a specific forbidden pattern (a long monotone run in the gap ranks, because an
off-line pair "traps" a gap). If the pattern is forbidden and the zero permutation is pattern-avoiding
with sub-exponential growth, off-line pairs are excluded combinatorially.

**(b) Concrete object.** The permutation π_N induced by ranking the first N consecutive normalized
gaps δ_n = (γ_{n+1} − γ_n)/(2π/log γ_n); the specific pattern (e.g. 321-avoidance, or a longer
monotone block) hypothesized to encode off-line pairs.

**(c) Minimal check.** From `tools/data/zeros_1_1000.txt`: (i) test whether the empirical π_N avoids
some nontrivial pattern τ; (ii) inject one synthetic off-line pair and check whether the forbidden
pattern appears. Kill = no pattern is avoided (the spacing permutation is pattern-universal, so this
route carries no constraint); survive = a forbidden pattern τ whose avoidance is *provable* from pair
correlation, giving a combinatorial p₁ input.

**(d) Verdict: SPECULATIVE.** Maps to Stanley–Wilf / Marcus–Tardos (2004); the "zeros avoid a spacing
pattern" hypothesis is CONJECTURED and could well fail immediately (spacings are known to be
GUE-random in a way that is pattern-rich), which is why the kill-check is one cheap script.

---

## 7. Free probability: R-transform of the zero empirical measure (operator algebras)

**(a) Import + analogy.** Voiculescu's free probability assigns to an operator its R-transform
(free cumulants); the semicircle law is the free CLT fixed point (all free cumulants ≥3 vanish), and
*free skewness/asymmetry* (odd cumulants) measures departure from the semicircle. **Provocation:**
"the zeros are semicircular" → invert: the *empirical* zero measure (rescaled ordinates) should have
vanishing odd free cumulants if and only if zeros are symmetrically on-line; an off-line pair breaks
the γ ↔ −γ reflection symmetry and must show up as a nonzero free skewness κ₃.

**(b) Concrete object.** The R-transform R(z) (free cumulants κ₁, κ₂, κ₃, …) of the empirical measure
μ_N = (1/N)Σ δ(γ_n / log γ_n), computed via the free Cauchy transform G(z) and functional inverse.

**(c) Minimal check.** Compute κ₁…κ₄ of μ_N from the zeros file (Rust, self-contained; free cumulants
from the moments via the free-cumulant moment-cumulant relations), and test κ₃ ≈ 0. Prediction to
falsify: κ₃ (odd part) → 0 as N → ∞ with a rate; a persistent nonzero κ₃ would be a *measured*
asymmetry diagnostic that, if provably related to off-line pairs, becomes a p₁ input. Kill = κ₃
vanishes but carries no off-line content (it is just the reflection symmetry, already known).

**(d) Verdict: PROMISING (new computation, cheap).** Maps to Voiculescu's free CLT and to
Keating–Snaith / GUE heuristics (semicircle is the expected limit); the *free-cumulant* reading and the
κ₃ ↔ off-line asymmetry link are not in any round-1/2 file and the check is a few lines of Rust.

---

## 8. Loss-landscape sharpness / Hessian descent beyond coboundary (ML)

**(a) Import + analogy.** Overparameterized models have flat loss minima with a Hessian whose
negative/zero eigen-directions signal either genuine descents or degenerate flatness ("double descent",
sharpness-aware minimization). **Provocation:** "the coboundary family is exhausted" → invert: the
record 0.673481 sits at a *saddle*, not a minimum, of the certificate objective over the *full*
coefficient space, and a Hessian eigen-decomposition reveals a descent direction that the coboundary
search (which only moved α, psum, coefficients along one curve) never probed.

**(b) Concrete object.** The certificate objective ℒ(coeffs) = (bound − 0.6818287) over the
full finite-dimensional coefficient space of the window (not just the one-parameter coboundary
curve); its Hessian ∇²ℒ at the certified optimum.

**(c) Minimal check.** Symbolically/numerically compute ∇²ℒ at the record 0.673481 configuration
(Rust `rug` for the exact-rational linearization) and find its smallest eigenvalue. Kill = Hessian
positive-semidefinite (0.673481 is a true local minimum of the full space ⇒ coboundary genuinely
exhausted, confirmed); survive = a negative eigenvalue ⇒ an explicit descent direction exists that
the coboundary search missed ⇒ a real constant gain with no new arithmetic input (contradicts the
"exhausted" verdict and is immediately actionable).

**(d) Verdict: SPECULATIVE.** Maps to sharpness-aware minimization / NTK (Jacot et al.) and to the
LP-dual vector V2 `[crossdomain]`; V2 targets the *certificate class*, whereas this targets the
*geometry of the existing optimum*, so it is distinct but low-probability — the structural verdict's
shadow price of p₁ being exactly 1 suggests the optimum is genuinely on the wall.

---

## 9. Epistasis / Walsh expansion of the explicit-formula fitness (biology)

**(a) Import + analogy.** In evolutionary genetics, the fitness landscape over loci is decomposed in
a Walsh–Fourier basis; **epistasis** = nonzero interaction coefficients (non-additive effects between
loci), and *submodular* landscapes (all pairwise interactions one-signed) have a single global optimum
reachable by hill-climbing. **Provocation:** "the zeros are a local optimum" → invert: treat prime
powers p^k as "loci", the explicit-formula functional value as "fitness", and the on-line configuration
as the *unique global optimum*. RH = the fitness landscape is submodular (single optimum at
all-on-line), which is testable at finite truncation.

**(b) Concrete object.** The Walsh–Fourier coefficients of the truncated explicit-formula functional
F(γ-configuration) = Σ_n Λ(n)/n^{1/2}·(interaction term) over the "loci" n = prime powers ≤ X;
specifically the sign of the pairwise epistasis terms between (p, q) blocks.

**(c) Minimal check.** Compute the pairwise Walsh coefficients (epistasis) of F for X ~ 10⁵ (Rust),
and test whether all pairwise terms share one sign (submodularity). Kill = mixed-sign epistasis
(landscape is rugged ⇒ no unique on-line optimum follows from this route); survive = one-signed
epistasis ⇒ a *proven* submodularity statement would certify the all-on-line configuration as the
global optimum — a genuine (if ambitious) route to p₁ = 1 on the truncated model.

**(d) Verdict: SPECULATIVE.** Maps to Weinberger's NK-model / Walsh epistasis and to submodular
optimization (Nemhauser); the explicit formula's off-diagonal *is* the epistasis, so this is a
re-reading of the MV off-diagonal wall rather than new arithmetic — likely to terminate at the same
prime-pair obstruction.

---

## 10. Modular bootstrap on the ξ character expansion (physics: conformal field theory)

**(a) Import + analogy.** In CFT, the **modular bootstrap** is a systematic SDP over characters that
proves *positivity bounds* on the operator spectrum (dimensions, spins) by exploiting the modular
symmetry of the partition function. **Provocation:** "the functional equation is just one identity" →
invert: ξ's functional equation (equivalently the θ-series modular identity) is a *modular symmetry*,
the zeros are the "operator dimensions", and RH = the bootstrap's SDP — run at higher derivative /
spin level than the one-quadratic-form certificate — forces all dimensions real (zeros on a line).

**(b) Concrete object.** The character/positive-definite decomposition of the ξ functional equation
(i.e. the Weil explicit-formula positivity as a *family* of SDP constraints indexed by a spin/derivative
parameter, not just the single quadratic form the current method uses).

**(c) Minimal check.** Formulate the finite-dimensional SDP (semidefinite program, e.g. the numerics
via a small Rust LP/SDP or interval-verified relaxation) over the character expansion at levels
j = 0, 1, 2 and read off the certified proportion. Prediction to falsify: the level-j SDP reproduces
exactly the known 0.6725 at j = 0 and does NOT increase with j (⇒ the bootstrap adds nothing over the
quadratic form). Survive = the SDP value grows with j ⇒ a systematic hierarchy that could exceed
0.6818 in-class (a new certificate *family*).

**(d) Verdict: ALREADY-KNOWN (in disguise) / SPECULATIVE hybrid.** Maps to the modular bootstrap
(Rattazzi–Rychkov–Tonni 2008; numerical SDPB) and to the Weil positivity that the whole 67.25% method
is built on; the "hierarchy of moments" reading is essentially V4's roadmap `[crossdomain V4]` wearing
CFT clothes. The one genuinely new bit is the *spin-parameterized* character decomposition, worth a
single SDP experiment to falsify the "it's just Weil positivity" hypothesis.

---

## Honesty footer

- Every idea is **CONJECTURED**; none is a claimed result. Each (d) verdict names the nearest
  *structural* cousin in the literature for a later literature agent to chase — not an asserted
  citation of a theorem. No bibliography is fabricated.
- Explicit non-goals honored: nothing here re-lists V1–V20 / L1–L9 / M28–M29 / A1–A5; nothing claims
  to "settle RH"; each idea is scoped to a kill-check that is a cheap Rust script against
  `tools/finitet`, `tools/zeta-rs`, or `tools/data/zeros_1_1000.txt`.
- Kill-first ordering (cheapest decisive check → most ambitious): #7 (free cumulants, ~20 lines) and
  #6 (pattern avoidance, ~20 lines) first; then #1, #8, #5, #2 (reuse `tools/finitet`); then #3, #4,
  #9, #10 (need new matrix/SDP code). Any clean negative is a documented result per hooks/agents.md.
- Only the honesty guardrails can stop a line; a refuted idea is relabeled ABANDONED with the reason,
  and the search continues.
