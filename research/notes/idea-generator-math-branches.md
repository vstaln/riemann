# Idea Generator: pure-mathematics branch attack catalog (topology, AG, categories, p-adics, combinatorics, logic)

**Agent:** IDEA GENERATOR (internal-math branch mining; analogy-domain-transfer + brainstorm + logic).
**Round:** 2. **Deliverable:** this file. Numbering: **MB1.x** (topology) … **MB6.x** (logic). Prior catalogs cited as
[CD-V#]/[CD-W#]/[CD-A#] (crossdomain), [V19] (selberg-class-theorem.md), and attack notes [AK] (attack-kernel),
[AC] (attack-ceiling), [AM] (attack-multiplicity), [AF] (attack-finitet), [AL] (attack-lfunctions),
[LP] (attack-lpdual), [SB] (attack-sandbox), [M29] (attack-m29), [NV] (attack-nevanlinna).

**Honesty protocol (per hooks/agents.md):** this file invents no proofs and asserts no new theorems. Every *idea*
is CONJECTURED by construction and carries a kill criterion. Label vocabulary (per the physics catalog's scheme):
**NEW** (invented here) / **KNOWN-DEAD** (killed earlier, cite) / **KNOWN-OPEN** (known open or already-flagged route, cite) /
**TESTED-OPEN** (numerically tested by our own tools, still open). Every quantitative claim below was produced by code
this session (exact commands in §0); nothing is quoted from memory.

**State of the art this catalog must respect (PROVEN / CHECKED NUMERICALLY in prior rounds):**
- The certificate class reads exactly (mean density, form factor on [0,1], integrality of marks); the 256-periodic
  near-CUE law realizes the bandwidth-one ceiling **v ≤ p₀ + |E(1)| = 0.68183123** (Lean `ceiling_law256_signed`,
  tight to 2·10⁻⁸ by the LP [LP]); the in-class gap 0.6725 → 0.6818 is closed by the LP, and **no constraint inside
  bandwidth one moves v; only the certified simple fraction p₁ does (shadow price exactly 1)** [LP §3–§5]. Consequently
  any vector aimed at "a better certificate on the same inputs" is DEAD; live vectors must supply a **new input**
  (beyond-bandwidth-1, higher-order correlation, structural separator, fluctuation), target a **new functional**
  (distinct count, derivative tower, families), or **reorganize** the proof (effective/class-level/formal artifacts).
- The certificate is a **repulsion statement**: value = 2 − (HS constant), HS²/N = 1 + off-diagonal pair sum under the
  kernel; real-world finite-T reads ≈ 0.70 → 0.6725 asymptotically; lattice world saturates ≈ 0.977; Poisson (no
  repulsion) gives an EMPTY certificate [SB].
- Derivative tower: ξ′ = 0.85838/0.86864 simple-on-line, 0.92919/0.93432 distinct (PROVEN, paper §7.3); ξ″/ξ‴ extension
  mechanical [CD-V9]; naive interlacing LP empty [CD-A4].
- GL(2) individual transport = hard wall (bandwidth 1/2, dimension ceiling) [AL]; the axiomatization (A1)–(A5) is a
  NEW/CONJECTURED packaging of PROVEN ingredients, with the GL(2) corollary class-level [V19].
- Known-dead already: odd-window imaginary counter [CD-A2], beyond-bandwidth-1 prime-pair bounds [CD-A1,A5],[M29],
  mollifier fusion wall [attack-mollifier], QI-inequality sweep (no inequality beats Lemma 3.2 on the data budget) [qi-sweep],
  two-form (Weil + CGG) at the same budget [attack-twoform].

---

## 0. Probes actually run this session (code-backed, with commands)

1. **W_T eigenvalue margin profile (idealized hard-cutoff window).** Command:
   `./tools/finitet/target/x86_64-unknown-linux-musl/release/finitet` (existing binary; canonical crate untouched).
   Output (eig5min = five smallest eigenvalues / λmax): T=100 (N=50): 1.08e-6; T=200 (N=123): **1.63e-15**; T=300
   (N=203): 1.24e-17; T=500 (N=380): 6.86e-18; T=700 (N=569): all five ≤ 2.2e-16. rank(e>1e-6) < N at T ≥ 200.
   **Interpretation (CONJECTURED):** the near-nullity grows with N and is NOT the configuration's structure — it is the
   frame-truncation deficit of the hard-cutoff idealization (the k-sum in Claim 2.1 converges only O(1/K) for the hard
   cosine; edge zeros give rows of norm O(1/N)), i.e. an **artifact of the idealized window**, exactly the caveat
   [AF]/[SB] flag. The C∞-smoothed window (`finitet-cinf`) changes the HS constant to ≈ 3.56 at eps = T/N — a *different
   window*, not the certified one (the hard cosine is the certified optimum [AK]). **Consequence for MB4.2/MB5.3:** the
   "margin profile" diagnostic is NOT cleanly measurable with the idealized model; it requires the certified window's
   profile or a boundary treatment. Label: TESTED-OPEN (diagnostic blocked by window realism, not by principle).
2. **General-N marked-configuration LP (min simple fraction over near-CUE rows).** Command:
   `timeout 90 uv run --quiet --with numpy --with scipy python tools/regen_law/lp_smallN.py` (regen_law agent's
   parametrization, run read-only). Output (min p1 / max p1 over the jittered-lattice family, F(j) = j rows exact):
   N=8: **0.50000000** / 0.97290869; N=16: **0.50642965** / 0.96318123; N=32: **0.65168203** / 0.94168454
   (N=256 law: p₀ = 0.68182868746). **Flag (important, see MB2.4/MB5.5):** taken at face value these small-N
   configurations would be admissible adversaries with p₁ < 0.6725, contradicting the PROVEN 0.6725 theorem — so either
   the regen_law power-spectrum parametrization (Σ w_c f_c(j) = j) does not faithfully reproduce the certificate's data
   budget (cumulative discrepancy D, E vs the GUE datum), or a normalization differs. **This is an adjudication task for
   the regen_law agent** (owner of that parametrization), not a refutation of anything proven. The monotone trend
   (0.50 → 0.51 → 0.65 → 0.6818) supports "the ceiling is an N = 256 phenomenon", but the class-level statement remains
   OPEN. Label: TESTED-OPEN with a live contradiction-flag.
3. **Moment-separation arithmetic (exact rationals).** Command:
   `uv run --quiet python -c "…"` (fractions). Tightness-extremal world [AM]/[CD-V1], spectrum (2/3·1, 1/6·2, 1/6·0):
   m₁..m₆ = 1, 4/3, 2, 10/3, 6, 34/3. vs GUE (sine kernel) m₁..m₄ = 1, 4/3, 2, 13/4: **identical through k = 3,
   separate at k = 4 by exactly 1/12.** Label: CHECKED NUMERICALLY (exact arithmetic). Feeds MB6.5 (P2/P3 pricing).

---

## Pool 1 — Topology / homotopy theory

### MB1.1. The derivative tower as a spectral sequence: what is the limit constant of ξ^(j)? — NEW (framing of P5), TESTED-OPEN at low j
**Idea.** A spectral sequence is a hierarchy of pages (E_r, d_r) whose differentials converge to a target. The honest
analogue in our setting is the **filtration of the zero configuration by derivative order**: ξ, ξ′, ξ″, … each yields a
rank–trace certificate (Rolle keeps the zeros real; FGL give the pair-correlation machinery for ξ′ zeros; the j-th
derivative extension is mechanical [CD-V9]), so we get a *sequence of moment vectors* (tr, HS²)_j and a sequence of
certified constants c_j = 0.85838, 0.86864, …. The spectral-sequence question is not "compute c_3, c_4" (P5 as already
scoped) but **does c_j converge, and to what?** FGL's pattern (constants increase with j) plus the interlacing bound
N₀,ξ^(j+1) ≥ N₀,ξ^(j) − O(1) (Rolle, lower bound only — [CD-A4] shows no usable upper bound) suggests c_j → some c_∞ ≤ 1.
**What it needs:** the explicit formula for ξ^(j)/ξ^(j−1) (pattern from the ξ′ supplement), the functional, and a
numerical estimate of c_3, c_4 to see the trend. **Feasibility:** Med (extends [CD-V9]); the framing itself is free and
organizes P6 too (the finite-T ladder's error terms are the "differentials"; their decay rate 1/log T [AF] is the
convergence rate of the spectral sequence — a real organizing device for the effective theorem [CD-V20]).
**Kill:** if c_j decreases after ξ′ (contradicting FGL's trend) or the ξ″ functional is degenerate.
**Cheapest probe (<1h):** compute the ξ″ functional constant numerically by reusing the ξ′ explicit-formula machinery
(check_xiprime.py / tools/xiprime_check exist) — the single new number that starts the trend.

### MB1.2. Refined Morse inequalities: a rank–trace that reads eigenvalue *multiplicities*, not just tr and HS² — NEW (folds into CD-V1 data)
**Idea.** Morse theory's inequalities come in two forms: the coarse (Σᵢ bᵢ ≤ Σᵢ cᵢ, an aggregate like our Lemma 3.4)
and the **refined** (bᵢ ≤ cᵢ separately, using the whole Betti-number sequence — i.e., the full spectrum of the
Hessian). Our rank–trace inequality is structurally a coarse Morse inequality: rank ≥ 2tr − ‖·‖². The refined analogue
would read the *eigenvalue multiplicity profile* of W_T (which the Jacobi eigensolver already computes [AF]) — e.g., the
count of eigenvalues in each dyadic band — and give per-band constraints. The LP closure [LP] shows no certificate on
(tr, HS², integrality, box) beats the ceiling, so the refinement is only live if the *profile* is a new input.
**What it needs:** the empirical profile of the real W_T (available: the eig5min data, caveat MB4.2/§0.1) vs the
tightness-extremal profile (2/3·1, 1/6·2, 1/6·0) and vs the 256-law's profile (not yet computed — see MB5.3).
**Feasibility:** Low–Med (numerics first; the inequality theorem is the hard part).
**Kill:** if the real profile is indistinguishable from the extremal profiles at the certificate's resolution.
**Cheapest probe (<1h):** print the full eigenvalue histogram of W_T at T = 200–500 from the finitet Jacobi code and
compare against the two extremal profiles.

### MB1.3. Sylvester signature as spectral flow across T: a consistency constraint no single-window certificate reads — NEW (kill-risk: CD-V13)
**Idea.** n₊(W_T) − n₋(W_T) = 2·(#on-line) − N is the **signature**, a spectral-flow invariant: as T varies continuously
through dyadic windows, the signature changes only when an eigenvalue of W_T crosses 0 (a zero entering/leaving the
window, or an off-line pair straddling the boundary). The spectral-flow bound is controlled by ‖dW_T/dT‖, which is
computable from the prime side (W_T's entries are prime-side integrals — A3). This yields a **Lipschitz-type constraint
on the signature as a function of T** — a cross-window consistency input that a single-window certificate cannot read.
**Analogy:** Atiyah–Patodi–Singer / spectral-flow reading of the index; the (1,1)-planes are the index jumps.
**What it needs:** a bound on ‖dW_T/dT‖ (prime-side, likely O(1) relative or better) and the T-derivative of the
signature. **Feasibility:** Low–Med (numerical T-sweep with the existing Jacobi code is immediate; the bound is the
work). **Kill:** if the bound is so weak that it is vacuous at the certificate's 1.4% tolerance, or if it reduces to
the fluctuation-statistics dead-end of [CD-V13] (the extremal law is T-periodic, so a *per-T-independent* bound cannot
exclude it — the signature flow of the law is periodic, matching any T-uniform bound).
**Cheapest probe (<1h):** sweep the signature n₊ − n₋ of W_T over a fine T-grid (T = 50…700) with the finitet Jacobi
code and record the jump pattern; compare with the 256-law's predicted periodic jumps.

### MB1.4. The signature as a KO-theory invariant (index-theoretic reading) — NEW-as-relabel (merge with MB1.3)
**Idea.** Sylvester inertia is KO-valued in the K-theory dictionary; the hyperbolic (1,1)-planes are the signature
contributions. The index-theoretic view adds one thing: the signature is *homotopy-invariant in the window*, so the
certificate value's window-dependence (Theorem D optimality [AK]) is a deformation-invariance statement.
**Feasibility:** Low (documentation/organizational). **Honest label:** mostly MB1.3 renamed; keep only if the
homotopy-invariance phrasing suggests a cleaner proof of window-optimality. **Kill:** if nothing beyond [AK]/MB1.3.
**Cheapest probe:** none (write-up only).

### MB1.5. Homotopy of the certificate's feasible set — KNOWN-DEAD (convexity trivializes it)
**Idea.** The certificate class {r ∈ C¹[0,1] : validity rows, box, budgets} is convex (an LP's feasible region), hence
contractible — there is no homotopical obstruction to reaching the optimum (consistent with the LP attaining the
ceiling [LP]). Documented so executioners don't re-fund "topological obstruction in certificate space".
**Kill:** already derived here. **Cheapest probe:** none.

**Pool 1 verdict:** the two live threads are (i) the derivative-tower *limit constant* (MB1.1 — a new target), and
(ii) the signature spectral flow (MB1.3 — a new *kind* of input, cross-window). MB1.2 is a reframing of [CD-V1] with a
sharpened question (multiplicity profile as input); MB1.4/1.5 are relabel/kill.

---

## Pool 2 — Algebraic geometry

### MB2.1. LP deformation theory of the 256-law: is it rigid, and what is the joint-perturbation gradient of p₀? — NEW (extends [LP], TESTED-OPEN)
**Idea.** The 256-law is the optimum of an exact-rational LP over marked configurations; LP sensitivity analysis **is**
the deformation theory of that optimum (the optimal basis gives the Jacobian of p₀ w.r.t. constraint perturbations).
[LP] computed single-row shadow prices (middle rows j = 64–192 worth 1.5–2·10⁻³ each). The new step is the **joint**
gradient and the **uniqueness** question: is the law the *unique* minimizer (rigid) or is there a positive-dimensional
face (deformable)? Rigidity matters because: if the optimum is unique, then *any* strict strengthening of any row
strictly raises the ceiling — i.e., the minimal beyond-bandwidth-1 sliver needed to move p₁ (P3) is priced by the
deformation gradient. **What it needs:** the law's defining LP data (LawN256.lean / cert file) + a second-order
sensitivity pass. **Feasibility:** Low (the LP machinery exists in tools/lpdual and tools/regen_law).
**Kill:** if the LP optimum is a high-dimensional face (then the ceiling is insensitive to row perturbations and the
rigidity premise fails — itself a finding).
**Cheapest probe (<1h):** solve the marked-configuration LP with all 255 rows and a joint perturbation ε·u (random u),
fit ∂p₀/∂ε, and check uniqueness via the count of basic feasible solutions (tools/lpdual + regen_law infrastructure).

### MB2.2. A second, PSD-kernel certificate for the **distinct** count (Bochner's theorem as the geometry) — NEW-salvage (distinct count not covered by window-optimality)
**Idea.** Bochner: a kernel is positive definite iff its Fourier transform is a positive measure. Our ψ = cos(√2u) is
sign-changing ⇒ W_T is indefinite ⇒ the (1,1)-planes. A PSD-kernel variant would give a certificate with *no*
hyperbolic planes — but a different (worse) moment ratio; [AK] proved the cosine is optimal for the ζ functional, so
this cannot move the *on-line* constant. The salvage: the **distinct** count (5/6 wall [AM]) is a different
functional; whether a PSD-kernel certificate (e.g., the Fejér kernel, or the positive part of the cosine) lifts the
distinct constant is not covered by [AK] and is a cheap check. **Analogy:** Kähler metrics = PSD kernels; the
certificate is a curvature inequality for a would-be polarization (the char-p polarization is canonical and positive —
[CD §3]). **What it needs:** the distinct-count functional with a PSD window (reuse the m3/m4 bookkeeping tools).
**Feasibility:** Low. **Kill:** if the PSD window's moment ratio is worse for the distinct functional too (likely —
the same re-normalization argument as [AK]).
**Cheapest probe (<1h):** run the distinct-count certificate with the Fejér kernel on the real zeros at T = 200–500
(extend tools/m4_*.py) and compare 5/6-wall headroom.

### MB2.3. Grothendieck–Riemann–Roch dictionary: the ν_T = µ + λ_T + π_T split as a local-term decomposition — KNOWN-OPEN (reorganization, V19-flavor)
**Idea.** GRR says the character of a pushforward decomposes into local (archimedean/Todd + support/prime) terms. Our
explicit formula's three-term split ν_T = µ + Π_T + P_T (archimedean density, pole term, prime sums — A3) **is** that
local decomposition, already realized. The dictionary's transferable content is *deformation-invariance of the
character* (homotopy invariance of K-theory): the trace and HS-norm are window-deformation-invariant at leading order,
which the variational identity (Thm D) exploits. **What it needs:** a write-up mapping each term of the certificate to
the GRR dictionary (a V19-style reorganization, §2.3 of selberg-class-theorem.md already does the axiom–ingredient map).
**Feasibility:** Low (documentation). **Kill:** if it produces no new inequality (expected) — it is a unification
deliverable, not a constant-mover.
**Cheapest probe:** none (write-up only).

### MB2.4. Class-level ceiling: is 0.6818 the worst case for ALL N, or an N = 256 phenomenon? Tropical/floor-decomposition + the small-N evidence — NEW, TESTED-OPEN (this session, §0.2) — **TOP vector**
**Idea.** The Lean ceiling is proven for the single 256-law instance; the *class-level* statement ("no certificate
valid against *every* near-CUE configuration certifies more than 0.6818") is only argued/CHECKED-NUMERICALLY [AC].
Tropical geometry supplies the structural guess: the ceiling is computed from piecewise-linear (tropical/floor) data —
the law is a lattice object, the "256" is a floor scale — and tropical intersection numbers are *combinatorial* counts,
suggesting a purely combinatorial (Lean-friendly) proof of the worst-case over *all* N. **The session probe (§0.2)
already produced the first class-level datapoints** (regen_law family LP): min p₁ = 0.500 (N=8), 0.506 (N=16), 0.652
(N=32) — monotonically increasing toward 0.6818 — **with a live contradiction flag** (face-value these would violate
the PROVEN 0.6725 theorem, so the parametrization's data budget must be reconciled with the certificate's discrepancy
data first). **What it needs:** (a) adjudication of the regen_law parametrization vs LawN256.lean's cumulative rows;
(b) the general-N statement "min p₁(N) + M(N)·budget ≥ 0.6725 − o(1) for all N" — the small-N laws have *larger* M
(= 1/(6N²) grid discrepancy), so the class ceiling is min_N [p₁(N) + M(N)·(|r′(1)| + ∫|r″|)]; whether N = 256 is the
argmin is the content. **Feasibility:** Med (LP infrastructure exists; the theorem is the work).
**Kill:** if the adjudication shows the small-N configurations are admissible with p₁(N) + M(N)·budget < 0.6725 — that
would be a genuine crisis for the class ceiling (not for the 0.6725 theorem) and would be a major finding, not a kill.
**Cheapest probe (<1h):** the adjudication itself — recompute the small-N min p₁ with the *cumulative* discrepancy rows
(D, E against the GUE datum, M(N) = 1/(6N²)) instead of the power-spectrum rows, and check min_N[p₁(N) + M(N)·2] vs
0.6725 (reuse tools/lpdual's certificate-side LP with the small-N rows).

### MB2.5. Connectedness of the (tr, HS²)-fiber: a topological explanation of the 5/6 wall — NEW (explains, and gives P2 a criterion)
**Idea.** [AM]'s wall: the all-simple world and the 2/3-simple + 1/6-double world are spectrally identical in
(tr, ‖·‖²). Deformation-theoretic reading: the fiber of configurations over the point (N, 1.3275N) — if it is
*connected* (like a linear system), then **no continuous functional of the configuration can separate its points**
without a moment beyond the second; the 5/6 wall is topologically forced. **What it needs:** a connectivity/irreducibility
statement for the (tr, HS²)-fiber, or a numerical proxy (random perturbations preserving the two moments; reachability).
**Feasibility:** Med (numerics: constrained random walk on configuration space; theory: hard).
**Kill:** if the fiber is provably disconnected and a separator on the components exists within two moments (contradicts
[LP], so unlikely — the LP already prices the data).
**Cheapest probe (<1h):** random-walk in configuration space at fixed (tr, HS²) (reuse the sandbox harness [SB]) and
measure the reachable set's diameter — a coarse connectivity diagnostic.

**Pool 2 verdict:** MB2.4 is the strongest single vector in this catalog (it attacks the one soft spot of the ceiling —
the class-level scope — with code already in hand). MB2.1 (rigidity/gradient) and MB2.2 (distinct-count PSD kernel)
are cheap near-term probes; MB2.5 gives P2 a clean criterion.

---

## Pool 3 — Category theory / topos

### MB3.1. Krein–Milman duality: are the near-CUE periodic laws the extreme points of the configuration polytope? — NEW (convex-geometry version of the class ceiling)
**Idea.** The certificate LP and the configuration LP are dual convex programs [LP]; by Krein–Milman the configuration
polytope's optimum is attained at an extreme point. Question: are the extreme points exactly the near-CUE *periodic*
marked laws (period | N)? If yes, the class ceiling = sup over extreme points = sup_N p₀(N), turning MB2.4's
general-N question into a *finite* family of LPs. This is the Yoneda-flavored statement made precise: the certificate
class (a contravariant functor Config → ℝ) is determined by its values on the extreme configurations. **What it needs:**
an enumeration of extreme points for small N (the LP basis structure) and a periodicity theorem. **Feasibility:** Low
for the enumeration (the LP basis is already in tools/lpdual), Med for the theorem.
**Kill:** if the extreme points are *not* periodic laws (then the class ceiling is not a sup over periods, and MB2.4
must be reframed).
**Cheapest probe (<1h):** enumerate the basic feasible solutions of the N = 32/64 configuration LP (scipy `linprog`
basis) and check periodicity of the active configurations.

### MB3.2. Universality / canonical certificate: is the class-optimal certificate always affine r(x) = a(1−x)? — NEW (structure theorem; pairs with MB6.2)
**Idea.** The LP's optimal certificate is (equivalent to) r(x) = 1 − x [LP §4]: r(0) = 1, r(1) = 0, r′ = −1, r″ = 0 —
the *simplest* shape in the class. Universality would mean: for every near-CUE law, the class optimum is attained by an
affine certificate (a 2-parameter family) — a structure theorem that makes the in-class closure trivially checkable and
reduces "what is the best certificate" to a 2-parameter problem. **What it needs:** a proof that affine certificates
dominate in-class (likely via the stability identity: with |E| ≤ M and r(1) = 0, the value is p₁ + M·|r′(1)| + M·∫|r″|;
the box |r| ≤ 1 forces |r′(1)| ≤ 1 + ∫|r″|, so r = 1−x is the extremal choice — the argument sketched in [LP §6]
"argued, not written"). **Feasibility:** Low–Med (the pieces are in [LP]; Lean-able).
**Kill:** if a non-affine certificate beats affine on some row-subset (the row-sweep data in [LP §3] can be checked
directly for affine-optimality per M).
**Cheapest probe (<1h):** rerun the [LP] certificate LP with the constraint "r affine" and compare against the full LP
value at M = 32/128/255 — if equal everywhere, the structure theorem holds numerically.

### MB3.3. Enriched composition of certificates (budgeted concatenation) — KNOWN-DEAD (reduces to CD-A4/CD-V18)
**Idea.** Certificates with the (B, C) budgets [LP] form an enriched category; composing a ζ-certificate with a
ξ′-certificate or a two-window certificate is an enriched composition with a triangle inequality on budgets. Honest
check: composition across functions (ζ + ξ′) is the interlacing LP — empty [CD-A4]; composition across windows is the
multi-window vector [CD-V18] — expected no gain (the extremal configuration re-normalizes). **Kill:** derived here (both
composition operations reduce to dead or tested-empty vectors).
**Cheapest probe:** none.

### MB3.4. Constructive/formal certificate: a rational, Lean-checkable witness for the in-class closure — NEW, high feasibility
**Idea.** The in-class closure (0.6725 → 0.6818) is numerically LP-verified; the authors' dual certificate file
(`cert_N256_blk_b128m.json`, sha256 cc3de991…) is not local. A *constructive* route: exhibit the certificate
r(x) = 1 − x with **rational** coefficients and a formal validity proof against the law's exact-rational rows
(LawN256.lean), Lean-checkable in the existing `PairCeiling` module. This hardens the ceiling chain's last
non-Lean link (EnclOK) from the certificate side and makes the closure a *formal artifact*. **Analogy:** topos-theoretic
"internal logic" — the claim is constructive iff it has a computational witness; LP duality + the simplex method are
constructive, so the witness should exist. **What it needs:** the law's rows (already in Lean), the validity inequality
for r = 1−x, and a Lean term. **Feasibility:** Low–Med (Lean repo exists; the inequality is elementary).
**Kill:** if the exact-rational validity check fails at the 3·10⁻⁴⁰ row tolerance (unlikely — the rows are exact
rationals, the residual is |E(1)| = 2.54·10⁻⁶).
**Cheapest probe (<1h):** compute c₀, r for r(x) = 1−x as exact rationals against LawN256.lean's enclosures (extend
tools/verify_enclok.py's harness) and print the certificate with the residual.

**Pool 3 verdict:** MB3.1 (extreme-point duality) and MB3.2 (affine-optimality structure theorem) are cheap and
directly testable with existing LP code; MB3.4 is the highest-verification-value vector in the catalog (formalizes the
closure). MB3.3 is dead.

---

## Pool 4 — p-adic analysis

### MB4.1. The p-adic moment problem and the second zeta: what the p-adic world can and cannot say — NEW-weak; Dwork-family import = KNOWN-OPEN (CD-V12 in p-adic dress)
**Idea.** Classical moments: (m_k) is a moment sequence of a positive ℝ-measure iff the Hankel matrices are PSD
(= W3 in [CD]). The p-adic moment problem asks when a sequence is a moment sequence of a p-adic measure; the p-adic
zeta (Kubota–Leopoldt) interpolates ζ at negative integers in a different topology. Honest assessment: our certificate
lives on the *archimedean* side (Sylvester inertia is a real signature — invisible p-adically), and the moment sequence
Σ_ρ γ^k is transcendental, so **p-adic purity (the Dwork/Deligne mechanism that proves RH in char p) does not transfer
directly** — this is the documented function-field obstruction [CD §3]. The two *methodological* imports are:
(a) Dwork's *deformation-in-p* idea — prove the certificate inequality for a family of objects (Dirichlet L-functions,
q-aspect) and specialize; this is exactly [CD-V12], CONJECTURED, and the p-adic framing adds nothing; (b) p-adic
*regularity* of the prime-side moments Σ Λ(n)²/n^k — a p-adically meaningful object (k ∈ ℤ) whose analytic
continuation might constrain the archimedean second-moment error (a speculative route to P6). (Note: the task asked to
reference idea-generator-history.md "if it exists" — it does not exist in research/notes/; the Dwork/Deligne history is
carried by [CD §3].)
**Feasibility:** Low (mostly documentation + one numerical regularity check). **Kill:** if the p-adic constraints are
subsumed by the archimedean ones (expected at the two-moment level).
**Cheapest probe (<1h):** compute Σ_{n≤X} Λ(n)²/n^k for k = 1, 2 and a few p, and check the p-adic convergence of the
interpolating series (uv + numpy on the prime-side data — the sums are closed forms: (ζ′/ζ)-type at k ≥ 2).

### MB4.2. Full-rankness / det W_T as a separator: the tightness-extremal world is singular, reality is positive definite — NEW; diagnostic blocked by window realism (§0.1)
**Idea.** The tightness-extremal world [AM] has W with 1/6 zero eigenvalues (spectrum 2/3·1, 1/6·2, 1/6·0) — **singular**.
Reality (all zeros on the line, simple — numerically) has W **positive definite, full rank**. Rank is a p-adically
visible quantity (rank = size of the largest nonvanishing minor), so "det W_T ≠ 0" is a legitimate new input type —
a *separator* the two-moment certificate cannot read (the certificate's rank-trace only uses rank ≥ 2tr − ‖·‖², not
full rank). **This session's probe (§0.1) shows the diagnostic is NOT yet measurable:** the idealized hard-cutoff W_T
is numerically singular (λ_min ~ 1e-16) at T ≥ 300 for *window-artifact* reasons (frame-truncation deficit + edge
rows), and the C∞ window changes the HS constant (different window, not the certified one [AK]). So the honest state:
full-rankness separates the *worlds* in principle, but the *margin* (how far reality is from singular) needs the
certified window's profile. **What it needs:** the certified C∞-window W_T spectrum with a boundary treatment, and the
256-law's own W spectrum (from LawN256.lean) — note the law's spectrum is NOT (2/3,1/6,1/6) (that is the [AM]
tightness world; the 256-law is a *mixture* with p₀ = 0.6818 ≈ 2/3 but its W-spectrum is uncomputed).
**Feasibility:** Med. **Kill:** if the certified-window margin is tiny (real W_T nearly singular) — then full-rankness
is vacuous at every feasible T.
**Cheapest probe (<1h):** compute the 256-law's W-spectrum (and its λ_min, nullity) from LawN256.lean's configuration
data — this single number tells us whether the ceiling law is singular and by how much.

### MB4.3. Integrality as the p-adic half of the certificate: "all marks = 1" would exclude the law — KNOWN-DEAD (multiplicity priced [AM])
**Idea.** The certificate's second input type (integrality of marks) is p-adic in nature (integrality = lying in ℤ_p for
all p). If the marks were certified to be all 1 (all zeros simple), the 256-law (1/6 doubles) would be excluded and the
ceiling would collapse. Honest check: (a) no unconditional statement forces ζ's marks to be 1 beyond o(N) (simple-zero
records are ≫ T log T-scale or RH-conditional 100%); (b) [AM] already proves the two-moment method prices multiplicity
optimally (k₂(2) = 4 tightness) — the mark-distribution *is* the priced input. The p-adic framing relabels the input
without adding content. **Kill:** derived here (cite [AM], [AC §2(c)]).
**Cheapest probe:** none.

### MB4.4. Dwork-style deformation-in-q: uniformity of the certificate in the family parameter as a p-adic-flavored statement — NEW, low confidence
**Idea.** Dwork proved rationality of zeta-functions by p-adic continuation in the parameter; Deligne's proof of RH in
char p is uniform in q. The number-field analogue of "uniform in q" is the Dirichlet-family program [CD-V12]; the new
sub-question is whether the *error terms* of the family-averaged HS norm admit a p-adic (Kummer-type) treatment — the
Gevrey taper of [CD-V12] is forced by archimedean error terms; a p-adic regularity argument might identify the minimal
taper order. **Feasibility:** Low (speculative; the family program itself is CONJECTURED).
**Kill:** if no p-adic input reduces the archimedean error term (the two worlds don't interact at the needed precision).
**Cheapest probe:** none this session (literature-scoped check of the Gevrey-taper necessity in [CD-V12]).

**Pool 4 verdict:** the p-adic branch is the *weakest* pool (positivity is archimedean; the function-field mechanism is
documented as non-transferable [CD §3]); its one live sub-vector is MB4.2's full-rankness separator, which is
*independent* of p-adic technique and owned by the window-realism question.

---

## Pool 5 — Combinatorics

### MB5.1. The zeros as a poset; masses as the Möbius inverse of the cumulative data — KNOWN-OPEN (relabel of the LP rows; folds into MB2.4)
**Idea.** The form-factor rows (cumulative masses) are the *zeta-function* of the poset ordered by height; the point
masses are its Möbius inverse — exactly how the LP consumes rows. The poset framing adds nothing until a poset *statistic*
beyond the cumulative (e.g., an order-dimension or height-profile bound) is provable for near-CUE configurations — no
such input exists. **Kill:** the content is the LP rows [LP]; the Möbius vocabulary is a relabel.
**Cheapest probe:** none.

### MB5.2. q-analogues / elliptic kernel deformations — KNOWN-DEAD (window-optimality [AK])
**Idea.** q-deforming the moment problem (q-binomial moments, elliptic sine kernels) gives a one-parameter family of
kernels; some elliptic kernels have *provable* positivity (the theta-function world of LeClair–Mussardo [CD-V14]).
Honest check: the certificate's kernel is fixed by the window, and the cosine is proven optimal for the ζ functional
[AK]; kernel deformations therefore cannot move the on-line constant, and the elliptic route was validated as
heuristic-only [CD-V14]. **Kill:** derived here (cite [AK], [CD-V14]).
**Cheapest probe:** none.

### MB5.3. Matroid union/intersection on the linear matroid of the v_ρ frame; the **column-rank profile** as a new input — NEW — **TOP-5 vector**
**Idea.** The rank function of the frame {v_ρ} is a *representable matroid rank*; the certificate's rank–trace inequality
is a matroid-polytope facet (r(S) ≤ |S|). Matroid theory's genuinely new theorems for us: (a) **matroid union**
(Edmonds): the rank of the union of the on-line and off-line-pair matroids is given by a min-formula — a *joint*
inequality that prices the on-line × off-line interaction beyond the A/B split of Lemma 3.4; (b) **matroid intersection**:
max |I₁ ∩ I₂| = min_X (r₁(X) + r₂(E∖X)) — a second certificate on the same data. Both consume only (tr, HS²,
integrality) and are therefore inside the LP-proven ceiling [LP] — so the *live* matroid input is the **column-rank
profile**: the ranks of V restricted to grid sub-windows (ranks of each frequency block), a *finer* datum than the
total rank, which the ceiling LP does not read. If the real profile differs from the law's, it is a genuine separator.
**What it needs:** the real V column-rank profile (finitet code has V) vs the law's (from LawN256.lean).
**Feasibility:** Low (numerics) — the theorem (feeding the profile into a certificate) is Med.
**Kill:** if both profiles are full-rank blockwise (plausible — both W are full-rank in the bulk), the input is empty;
the probe answers this.
**Cheapest probe (<1h):** compute the ranks (and smallest singular values) of V's leading frequency sub-blocks at
T = 200–500 from the finitet V construction; compare with the law's block structure (marks at 1/6 of the positions
would create a rank dip at those blocks).

### MB5.4. Design/discrepancy theory: the law as a low-discrepancy design; the real zeros' star-discrepancy as a diagnostic — NEW (diagnostic)
**Idea.** The 256-law's cumulative mass satisfies |256·S(j) − j| ≤ 3·10⁻⁴⁰: an *exact rational* low-discrepancy
structure — a design, not a random point set. Classical discrepancy theory (Koksma–Hlawka, star-discrepancy bounds)
says the *minimum* achievable discrepancy of a natural N-point set is ~ (log N)/N or 1/√N, both ≫ 3·10⁻⁴⁰: no
*realizable* zero configuration can have the law's exactness — but the certificate only needs *compatibility* with the
bandwidth-one data, which the law satisfies, so this cannot kill the law as an adversary (KNOWN-DEAD at the certificate
level). The live diagnostic: measure the real configuration's discrepancy (D(x), E(x) against the GUE datum x²/2) at
the certificate's grid and compare with the law's M = 2.54·10⁻⁶ — if the real |E| is much larger, the real
configuration sits *far* from the certificate's worst case, quantifying the finite-T slack (ties to [SB]'s Δ(T) > 0).
**Feasibility:** Low (the D, E arrays are in [LP]'s data). **Kill:** if the real |E| is dominated by the same
truncation artifacts as §0.1.
**Cheapest probe (<1h):** compute D(x), E(x) for the real zeros at the 256-grid (extend tools/lpdual/extract_law.py)
and print max|E| vs the law's 2.54·10⁻⁶.

### MB5.5. Ehrhart/quasi-polynomial structure of p₀(N): enumeration of near-CUE laws as a function of N — NEW (merges with MB2.4)
**Idea.** The number of N-periodic marked configurations with near-CUE rows is a lattice-point count in a polytope — an
**Ehrhart polynomial/quasi-polynomial** in N; the extremal simple fraction p₀(N) is a function on its vertices. The
"256" (a power of 2) smells like the quasi-period of this quasi-polynomial. If p₀(N) is a quasi-polynomial, computing
it at N = 64, 128, 256, 512 (LP solves, cheap) and fitting the period gives the **general-N ceiling** by extrapolation
— upgrading the single-law Lean theorem to a class statement. **This session's probe (§0.2) gives the first points**
(min p₁ = 0.500/0.506/0.652 at N = 8/16/32 on the regen_law family — parametrization-flag pending). **Feasibility:**
Med (LP machinery + the adjudication of MB2.4). **Kill:** if the adjudication shows the parametrization cannot be
reconciled with the cumulative rows (then the Ehrhart object is ill-defined).
**Cheapest probe (<1h):** the MB2.4 adjudication probe (cumulative-row small-N LPs) doubles as the N = 64/128 datapoints.

**Pool 5 verdict:** MB5.3 (column-rank profile) and MB5.5/MB2.4 (general-N ceiling) are the strong combinatorial
vectors, both with immediate numeric probes on existing code. MB5.4 is a cheap diagnostic.

---

## Pool 6 — Logic / proof theory

### MB6.1. Formalize the *class-level* ceiling ∀N in Lean — NEW, high verification value — **TOP-3 vector**
**Idea.** The Lean ceiling (`ceiling_law256_signed`) is the N = 256 instance; the class-level statement ("no certificate
valid against every near-CUE configuration certifies more than …") is argued, not formalized [AC]. A formal ∀N theorem
would (a) eliminate the last numeric links (EnclOK and the missing dual certificate) from the ceiling chain, and
(b) make the general-N question (MB2.4/MB5.5) a formal obligation — the honest end-state of the wall.
**What it needs:** the certificate/configuration duality already in `PairCeiling` + a parameterized-N statement +
either the p₀(N) family results (MB2.4) or a structure theorem reducing the class to the extreme laws (MB3.1).
**Feasibility:** Med (Lean repo exists; the LP structure is simple; the ceiling's axioms = {propext, choice, Quot.sound}).
**Kill:** if the general-N statement is *false* (small-N laws with larger M-residual dominate — see MB2.4's flag), in
which case the correct formal statement is "min_N [p₁(N) + M(N)·budget]" and the 256-law's special status becomes the
theorem.
**Cheapest probe (<1h):** none this session (formalization); the numeric prerequisite is MB2.4's adjudication probe.

### MB6.2. Normal-form theorem: the optimal in-class certificate is affine (r = 1−x is canonical) — NEW, small, high feasibility
**Idea.** Proof-theoretically, the certificate class has an equivalence relation ("same value and validity set"); the LP
exhibits the affine certificate r = 1−x as a normal form [LP §4]. Prove: **every class-optimal certificate is
equivalent to an affine one.** Mechanism sketched in [LP §6]: with r(1) = 0, |E| ≤ M, the stability ceiling is
p₁ + M(|r′(1)| + ∫|r″|), and the box |r| ≤ 1 forces |r′(1)| ≤ 1 + ∫|r″| — so the affine r = 1−x is the extremal
budget allocation; a proof that the box forces |r′(1)| + ∫|r″| ≥ 1 at the optimum is "argued, not written" [LP §6].
**What it needs:** the missing argument + a Lean statement. **Feasibility:** Low–Med.
**Kill:** if a non-affine certificate strictly beats affine at some row-subset (checkable numerically — MB3.2's probe).
**Cheapest probe (<1h):** MB3.2's probe (affine-restricted LP vs full LP at M = 32/128/255).

### MB6.3. Constructive audit of the wall: does the ceiling need choice? — NEW (low EV, honest)
**Idea.** The Lean ceiling uses {propext, Classical.choice, Quot.sound}. LP duality + simplex are constructive
(finite-dimensional); the C¹/IBP machinery (integration by parts off a countable set) is the plausible
non-constructive step. A choice-free formalization would upgrade the wall to a *constructive* obstruction ("no
computable certificate beats 0.6818" — itself the content of the LP attaining the optimum). **Feasibility:** Med
(Lean work), value: epistemic only.
**Kill:** if choice is structurally needed for the analytic lemmas (document where).
**Cheapest probe:** none (formalization).

### MB6.4. Proof-mining the axioms: independence and sensitivity of (A1)–(A5) — NEW (organizational)
**Idea.** [V19] packaged the method as Theorem T over axioms (A1)–(A5). Proof-mining questions: (i) which axioms are
used where (the axiom–ingredient map [V19 §4] exists — formalize it as an independence audit: is A5 (MV) really needed
for the second moment, or does A4 + A3 suffice at the level of Prop 5.6?); (ii) which axiom, if weakened, breaks which
constant — the method's output-sensitivity to its inputs, in logical dress (the LP shadow prices [LP] are the numeric
shadow of this). **Feasibility:** Low (analysis of existing Lean files + the [V19] map). **Kill:** if the audit finds
no axiom weaker than the theorem's output (expected — the method is minimal by construction).
**Cheapest probe:** none (read-only audit of Zeta23/PrimeSideA.lean + [V19 §4]).

### MB6.5. The separation-margin LP: price P2/P3 inputs by how well they separate the law from reality — NEW, high EV — **TOP-2 vector**
**Idea.** The ceiling's content is *inseparability*: no certificate on the bandwidth-one data separates the 256-law
from the real configuration. Decision-theoretic version: for each candidate new input (third moment P2, fourth moment,
column-rank profile MB5.3, beyond-bandwidth-1 sliver P3), compute its **separation margin** between the law and reality
— the LP/linear-functional analogue of the [LP] shadow-price program. Session arithmetic (§0.3, exact rationals):
the tightness-extremal world [AM] has moments m = (1, 4/3, 2, 10/3, …) and **matches the GUE sequence (1, 4/3, 2,
13/4) through k = 3 — the third moment is exactly blind** (P2's suspicion [CD-V3] confirmed arithmetically for that
world), and **separates at k = 4 by exactly 1/12** — but the fourth moment is beyond the unconditional range
(kλ < 2 ⇒ k = 2 at λ = 1 [CD-V3]). So the pricing table: m₃ margin = 0 (P2 cannot move the tightness world), m₄
margin = 1/12 (conditional only), column-rank profile = probe-pending (MB5.3), p₁-sliver = 1:1 (already known [LP]).
**What it needs:** the 256-law's own m₃/m₄ (from its W-spectrum — probe MB4.2's companion) to extend the table to the
actual ceiling adversary. **Feasibility:** Low (arithmetic + existing m3/m4 tools).
**Kill:** if every computable input's margin is ≤ the certificate's tolerance (1.4% in-class) — that *is* the priced
conclusion (redirect to P3).
**Cheapest probe (<1h):** compute the 256-law's m₃, m₄ from LawN256.lean's configuration (or the law's W-spectrum) and
extend the margin table; tools/m3_moment.py already computes the GUE side.

**Pool 6 verdict:** MB6.2 (normal form) and MB6.5 (margin pricing) are cheap and immediately actionable; MB6.1 is the
high-value formalization end-state; MB6.3/6.4 are honest low-EV audits.

---

## TOP 10 (EV × feasibility × cheap-probe), ranked

1. **MB2.4/MB5.5 — General-N/class-level ceiling + parametrization adjudication** (TESTED-OPEN with live flag; §0.2
   gave min p₁ = 0.500/0.506/0.652 at N = 8/16/32 and exposed a contradiction-flag to adjudicate). Directly attacks the
   one soft spot of the wall (class-level scope [AC]); every piece of code exists.
2. **MB6.5 — Separation-margin pricing of P2/P3** (m₃ is exactly blind — margin 0, CHECKED; m₄ separates by 1/12,
   conditional-only; the table extends to the 256-law and the column-rank profile). Prices the next input purchase.
3. **MB6.1 — Formal class-level ceiling ∀N in Lean** (hardens the wall's last non-Lean links; requires MB2.4's
   numeric prerequisite).
4. **MB5.3 — Column-rank profile of the frame V as a new input** (a separator the ceiling LP cannot read; probe
   immediate on the finitet V; kill-criterion clean).
5. **MB1.3 — Signature spectral flow across T via ‖dW_T/dT‖** (a new cross-window input type; numeric T-sweep is
   immediate; kill-risk = CD-V13 fluctuation dead-end, testable).
6. **MB1.1 — Derivative-tower limit constant (spectral-sequence framing of P5)** (one new number — the ξ″ constant —
   starts a trend; new target, proven machinery).
7. **MB3.4/MB6.2 — Constructive affine certificate (r = 1−x) as a formal Lean artifact** (makes the in-class closure a
   formal artifact; low risk, high verification value).
8. **MB2.1 — LP deformation/rigidity of the 256-law** (joint-perturbation gradient of p₀; prices the minimal P3 sliver;
   extends [LP]'s shadow prices).
9. **MB2.2 — PSD-kernel certificate for the distinct count** (the one window direction [AK] doesn't cover; cheap).
10. **MB5.4 — Real-zeros star-discrepancy diagnostic** (quantifies finite-T slack vs the law's 2.54·10⁻⁶; cheap;
    caveat: window artifacts).

**Strategic reading:** the internal-math branches do NOT resurrect the unconditional simple-zero constant (the LP
closure [LP] and the repulsion reading [SB] rule that out), and they confirm the p-adic/function-field route is dead
[CD §3]. What they add is three things the far-field catalogs cannot: (i) a **class-level attack on the ceiling
itself** (MB2.4 — the general-N statement is the one place the wall is argued, not proven), (ii) a **pricing
machinery for new inputs** (MB6.5 — which new datum is worth attacking), and (iii) **new input *types*** (signature
spectral flow MB1.3, column-rank profile MB5.3, derivative-tower limit MB1.1) that sit outside the ceiling LP's data
budget. The highest-leverage next move is the MB2.4 adjudication probe: it either closes the class-level ceiling or
finds a genuine gap in it.

---

## WILD — honestly labeled provocations

- **W-MB1. "The certificate is a Chern-number inequality for a would-be motive"** (AG): BMY-type Chern inequalities
  are positivity constraints; our rank–trace is a Chern-number-type inequality for the would-be polarization. Honest
  status: this is exactly the function-field obstruction [CD §3] — no motive, no polarization, no transfer. WILD only
  as a *label*, dead as a mechanism.
- **W-MB2. "The (1,1)-planes are a TQFT's saddle points; the signature is a cobordism invariant"** (categories): a
  2D-TQFT's semisimplicity factorizes invariants; the extremal law would be the semisimple limit. Pure analogy; no
  provable content; the signature is already understood as the Sylvester index (MB1.3). WILD.
- **W-MB3. "A p-adic Weil form whose rank (not signature) is the certificate"** (p-adics): the rank is p-adically
  meaningful (MB4.2's kernel); a p-adic linear-algebra certificate would be the "p-adic half" of the wall. Honest
  status: rank is already read by the certificate; the p-adic valuation adds nothing beyond integrality (MB4.3 —
  KNOWN-DEAD). WILD.
- **W-MB4. "The wall is a constructive (Brouwer-style) bar"** (logic): if no *computable* certificate beats 0.6818,
  the wall is a separation theorem of intuitionistic logic. Honest status: the LP attaining the optimum already gives
  the strongest form ("the optimum exists and is attained"); the constructive reading adds an epistemic gloss (MB6.3),
  not a new theorem. WILD.

All WILD vectors are CONJECTURED-by-construction, carry no fabricated literature claims, and are included for
provocation only; none is recommended for funding ahead of the TOP-10.

---

## Label inventory

- **NEW (invented here, each with kill criterion):** MB1.1, MB1.2, MB1.3, MB1.4, MB2.1, MB2.2, MB2.4, MB2.5, MB3.1,
  MB3.2, MB3.4, MB4.2, MB4.4, MB5.3, MB5.4, MB5.5, MB6.1, MB6.2, MB6.3, MB6.4, MB6.5.
- **KNOWN-DEAD (killed here, reason cited):** MB1.5 (convex feasible set ⇒ no homotopy), MB3.3 (reduces to CD-A4/CD-V18),
  MB4.3 (multiplicity priced [AM]), MB5.2 (window-optimality [AK]), MB5.4-as-certificate-input (compatibility is all
  that matters; survives only as the diagnostic half).
- **KNOWN-OPEN (known open or already-flagged route, cited):** MB2.3 (GRR unification, V19-flavor), MB4.1 (p-adic
  moment problem weak; Dwork-family import = CD-V12), MB5.1 (poset/Möbius relabel of the LP rows).
- **TESTED-OPEN (numerically tested this session, still open):** MB1.1 (low-j constants PROVEN [paper §7.3]; limit open),
  MB2.1 (single-row shadow prices [LP]; joint/rigidity open), MB2.4/MB5.5 (§0.2 small-N LP run — CHECKED NUMERICALLY,
  interpretation CONJECTURED + adjudication flag), MB4.2 (§0.1 eig5min run — CHECKED NUMERICALLY, artifact-blocked),
  MB6.5 (§0.3 exact-rational moment table — CHECKED NUMERICALLY).

## Honesty footer

- Every quantitative claim in this file traces to a script run this session or to a cited note:
  §0.1 `./tools/finitet/target/x86_64-unknown-linux-musl/release/finitet` (eig5min table);
  §0.2 `timeout 90 uv run --quiet --with numpy --with scipy python tools/regen_law/lp_smallN.py` (min/max p₁ at
  N = 8/16/32);
  §0.3 `uv run --quiet python -c "…"` with `fractions` (moment table: extremal world (1, 4/3, 2, 10/3, 6, 34/3) vs
  GUE (1, 4/3, 2, 13/4), separation at k = 4 by 1/12).
- The GUE moment values (1, 4/3, 2, 13/4) are taken from the cited sequence in [CD-V3] ("matching GUE") and from the
  m3/m4 tools' diagrammatic computations; the *extremal-world* values were re-derived here in exact rationals.
- No literature claim is fabricated: the Dwork/Deligne history vector exists only via [CD §3] (idea-generator-history.md
  does not exist in research/notes/ — noted per the brief's "if it exists"); the FGL derivative constants are PROVEN in
  the paper [§7.3]; all "standard" combinatorial/geometric facts (Bochner, Krein–Milman, matroid union/intersection,
  Ehrhart, spectral flow, refined Morse inequalities) are named at the level of "standard in the field" and are not
  cited as sources we hold — every *use* of them here is flagged CONJECTURED.
- The small-N LP numbers (§0.2) are reported with the explicit caveat that they live in the regen_law agent's
  parametrization and appear to contradict the PROVEN 0.6725 theorem if taken as class adversaries; this is an
  adjudication task, not a refutation, and is flagged as such in MB2.4/MB5.5.
