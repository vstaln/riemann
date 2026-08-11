# Idea Generator: quantum-chemistry / molecular-orbital / condensed-matter attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (analogy-domain-transfer + brainstorm + epistemology applied). Round 1, chemistry pool.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack; every probe is < 1 h.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Chemistry/condensed-matter
facts below are standard textbook/field facts (Hückel moments, Wiberg/Mulliken traces, Coleman/Klyachko
N-representability, Wilson GF method, Anderson localization, isospectral graphs). **None of the chemistry
literature is held in research/papers/** — every such fact is labeled REASONABLY BELIEVED (standard) and must
be verified against a held source before it is cited in any paper. Every *idea* is CONJECTURED by
construction and carries a label NEW / KNOWN-DEAD / KNOWN-OPEN / TESTED-OPEN plus a kill criterion.
**Anti-duplication discipline:** crossdomain catalog = idea-generator-crossdomain.md [CD-V#/W#/A#]; physics
catalog = idea-generator-physics.md [P#.#]; attack notes = attack-kernel [AK], attack-ceiling [AC],
attack-multiplicity [AM], attack-nevanlinna [AN], attack-qi-sweep [QI], attack-finitet [AF],
attack-twobandwidth [TB], attack-lpdual [LD]. Anything already mined there is *referenced, not re-derived*;
this catalog adds only what is genuinely chemistry-flavored or genuinely new.

---

## 0. Where we stand (the honest map; what chemistry could possibly move)

**PROVEN (Lean / derived in our notes), recap:**
- Two-moment method: tr Â = (1+o(1))N, ‖Â‖²_F = (C+o(1))N, C = 1/c₁* = 1/2 + (1/√2)cot(1/√2) = 1.3274993
  (cosine window, global optimizer [AK]); certificate value 2 − C = 0.6725007 (Thm D); 2/3 flat; 5/6 distinct;
  0.83625 distinct optimal-window [AM].
- Bandwidth-one ceiling **0.68182868746** realized by an exact-rational 256-periodic near-CUE marked law
  (marks ∈ {1,2}, Σ marks = 256) [AC]; LP-optimal certificate tight at 0.68183123 [LD]; **there is no missing
  constraint inside bandwidth one** — the in-class gap is a **second-moment gap Δm₂ = 0.0093** [AN, LD].
- Integrality identity m₂ = 2 − p₁ for marks ∈ {1,2} (PROVEN, trivial) [AN §3]; the 0.6818 law satisfies it,
  so integrality cannot exclude it [AN]; a third-moment lower bound m₃ ≥ 2 would exclude the law
  (m₃(law) = 1.9545 < 2) but is **unprovable** (§7.5(e): odd moments don't lower Λ₁(0) for the on-line
  functional) [AN §4].
- Third moment: m₃(λ) closed form — m₃(1) = 2, m₃(2/3) = 13/4, m₃(1/2) = 5 (PROVEN [TB]); two-bandwidth
  joint certificate **REFUTED** (admissible-cubic gives 0.7593 at λ=1/2, 0.8071 at λ=2/3, both < 5/6) [TB].
- 5/6 distinct wall: the all-simple world and the 2/3-simple + 1/6-double world are spectrally identical in
  (tr, ‖·‖²); the method cannot separate them [AM]. lemmaR_tight: the inequality is tight on the certificate's
  data budget [AM, QI].
- QI sweep: **no quantum-information inequality beats the rank–trace on the data budget**; the CS refinement's
  gain (trQ₊−2b)²/b vanishes at sharp configurations [QI]. **Coleman/Garrod–Percus/Klyachko-type
  N-representability bounds were NOT in the sweep** (verified: [QI §3] covers CS purity–rank, Q₊-side CS,
  purity–negativity, Schmidt-number, PPT, subadditivity, entropy, higher moments) — Pool 3 below extends.
- ξ′: 0.85838/0.86864 simple-on-line, 0.92919/0.93432 distinct (PROVEN); ξ′-zero data on the line exists for
  the first 1000 ζ-zeros (tools/data/xiprime_on_line_1_1000.txt, 1009 roots incl. 9 small-t roots below γ₁)
  [CD-V8, V9]. Derivative tower: ξ″/ξ‴ mechanical extension [CD-V9]; naive *pairwise* interlacing LP dead
  [CD-A4]. Finite-T: bound/N − 0.6725 = Δ(T) > 0, decaying ~1/log T, near-rank-deficient min eigenvalue
  (~1e-17·λmax) [AF].
- m₄(1) = 13/4 is the paper's claim (checked against in tools/m4_check.py, determinantal diagram); the
  extremal-world submeasure has m₄ = **10/3** (CHECKED); the 256-law has m₄ = 3.2272 (CHECKED); the 13/4 vs
  10/3 discrepancy (off-diagonal 4-point part) is flagged UNRESOLVED in [AN §6].

**Open problems this catalog targets:**
- **P1** — the missing in-class constraint (the second-moment gap 0.6725 → 0.6818; what the 256-law violates).
- **P2** — break the 5/6 distinct wall (third moment / higher correlation inputs).
- **P5** — the derivative tower (ξ′, ξ″, …).
- **P6** — finite-T error terms (the effective theorem; the ~1/log T deficit).

**Abstracted problem (analogy-domain-transfer, Step 1):** a probability measure on the line with
integer-valued atomic masses (marks ∈ {1,2}) and total mass N, constrained by its first two moments (mean 1;
second moment 4/3 or 1.3275) and a bandwidth-one correlation condition, must be proven to have ≥ 67.25% of
its atoms of mass 1 ("simple zeros"). Two *lattice-like* extremal worlds achieve the worst case; the missing
input is any provable constraint they violate. Chemistry and condensed matter are the sciences of (i)
occupancy distributions with integrality constraints, (ii) moment problems for spectral densities, (iii)
trace statistics of density matrices, (iv) positivity/representability hierarchies, (v) localization
measures, and (vi) secular-equation structure — each maps onto one of the six pools below.

---

## Pool 1 — Hückel / tight-binding spectral moments: the moments→DOS inversion literature

The chemistry moment problem: for a Hückel/tight-binding Hamiltonian H on a molecular graph (H = αI + βA, A
the adjacency matrix), the k-th moment of the DOS μ_k = (1/N)tr(H^k) **counts closed walks of length k** on
the graph (REASONABLY BELIEVED, standard: tr(A^k) = # closed walks — pure linear algebra, PROVEN-class). The
"moments method" of solid-state theory (Cyrot-Lackmann; the recursion method of Haydock–Heine–Kelly)
reconstructs the DOS from moments via Lanczos tridiagonalization + a continued fraction; Burdett's
"chemical bond" program reads bonding/anti-bonding structure off the moment sequence (REASONABLY BELIEVED —
reported in the task brief; not held, verify before citing). The literature's answer to the two-moment
underdetermination is *additional input*: compact support, maximum entropy, a band-edge "terminator", or
quadrature order — exactly the structure our Nevanlinna reframe [AN] already exposed.

### C1.1 The extremal worlds ARE Gauss-quadrature (principal-representation) measures — verify and read off the m₄ pricing — TESTED-OPEN (extends [AN §2]; quadrature bit NEW)
**Idea:** attack-nevanlinna computed the principal representations P⁻, P⁺ of the (1, 4/3) moment problem; the
certificate's sharp worlds (2/3-simple + 1/6-double submeasure and the 256-law) are the *atomic extreme
points* of their moment class — in quadrature language they are the **Gauss/Radau/Lobatto-node measures** of
the problem. Chemistry's quadrature-error theorem then *prices* how much higher-moment data pins the world:
the Gauss error term is controlled by the next unused moment (m₃, then m₄). Concretely: the 256-law lives at
(m₁, m₂) = (1, 1.3182); its *own* principal representations are computable now, and the quadrature error
bound says m₄ (or m₃) separates the law from any other member of its class by an explicit amount.
**Analogy:** Gauss quadrature ↔ the certificate's atomic worst cases; quadrature order ↔ number of moments;
quadrature remainder ↔ the missing-constraint price.
**Needs:** (i) principal representations of (1, 1.3182) with integer-grid atoms (machinery exists in
tools/nevanlinna_check.py); (ii) the Gauss-error bound statement for the (1, m₂) class.
**Feasibility:** Low (reuse). **Label:** TESTED-OPEN — the [AN] machinery is done; the quadrature-error
identification and the (1, 1.3182) computation are new.
**Cheapest probe:** tools/nevanlinna_check.py extended: principal representations of (1, 1.3182); is the
(0.68183, 0.15909, 0.15909)-mass measure among them? — 30 min.

### C1.2 Isospectral graphs / Godsil–McKay switching as the classification of the certificate's degeneracy class — NEW
**Idea:** chemistry's isospectral-graph theory (Collatz–Sinogowitz; Schwenk: almost all trees are cospectral;
Godsil–McKay switching: a local operation that preserves the full spectrum — REASONABLY BELIEVED, standard)
classifies *exactly* how distinct structures share spectra. The 5/6 wall [AM] is a *cospectrality*
statement: the all-simple world and the 2/3+1/6 world have identical (tr, ‖·‖²). The transfer: model a marked
configuration as a weighted graph (nodes = zeros; weights = marks; edge weights = the Gabor inner products
|⟨v_ρ, v_ρ′⟩| = |Ψ(s_ρ−s_ρ′)|, known [AF]); then the certificate's two-moment class is generated by a
switching-like operation, and **any provable input that is not switching-invariant moves the wall**. If the
two-moment class provably equals the GM-switching class on the Gabor geometry, we get a *complete
classification* of the degeneracy — the exact answer to "which worlds are spectrally identical" of [AM §0].
**Analogy:** isospectral molecules ↔ two-moment-indistinguishable zero configurations; GM-switching ↔ the
operation generating the degeneracy class.
**Needs:** (i) small synthetic marked configurations with Gabor weights; (ii) the two-moment class (LP, [AC]
machinery) vs the switching orbit; (iii) a statement about which class is bigger.
**Feasibility:** Low–Med (small numerics). **Label:** NEW.
**Cheapest probe:** 20-node synthetic configurations: enumerate the two-moment-equivalent marked worlds and
test GM-switching closure — 1–2 h.

### C1.3 Band-edge / "terminator" input = the largest eigenvalue — reference [P4.3], KNOWN-OPEN
**Idea:** the recursion method's band edges are determined by *all* moments; the "terminator" (asymptotic
DOS shape) is extra input chemistry needs beyond the moments. Our analog of the band edge is λmax of Â (the
double-mark eigenvalue 2 for the worlds); a provable edge bound would be a new input — but none is known, and
the trivial bound (λmax ≤ ‖·‖_F = √1.3275N ≫ 2) is useless. **Reference:** physics catalog [P4.3] already
measures λmax as a diagnostic; nothing new here. **Label:** KNOWN-OPEN (input), no new fragment.
**Cheapest probe:** none (P4.3's probe stands).

### C1.4 Alternant (bipartite) symmetry — KNOWN-INCORPORATED (documented to prevent re-derivation)
**Idea:** bipartite graphs force μ_odd = 0 (DOS symmetric). The zero configuration's "symmetry" is the
functional-equation involution ρ ↦ 1−ρ̄ (same height, conjugate) — which is *already* the (1,1)-plane
bookkeeping of Lemma 3.1 and the pairing in [AM]. No new moment relation is forced beyond what the paper
uses. **Label:** KNOWN-INCORPORATED. **Cheapest probe:** none.

### C1.5 Max-entropy DOS under (m₁, m₂) vs the crystal's zero entropy — NEW (diagnostic, overlaps [P10.2])
**Idea:** the max-entropy measure under (m₁, m₂) (shifted truncated Gaussian/exponential-type density,
REASONABLY BELIEVED standard) has the largest entropy in the class; the certificate's extremal worlds are
atomic (entropy 0). The *entropy deficit* of the worlds vs the maxent bound is the "price of atomicity" — a
diagnostic of how far the worst case sits from the maximum-entropy (most featureless) member of the class.
**Analogy:** maxent DOS reconstruction ↔ the featureless null; entropy deficit ↔ the method's "surprise" at
the atomic worst case.
**Needs:** the explicit maxent density for (1, 4/3) and its entropy.
**Feasibility:** Low (compute). **Label:** NEW (diagnostic; overlaps P10.2 — reference). **Cheapest probe:**
20-min computation of H_maxent vs H(crystal) = 0.

### C1.6 Recursion-method continued-fraction positivity and CMS interval bounds on [1,2] — KNOWN-DEAD-ish (folds into [AN §3]; document)
**Idea:** the Lanczos/Jacobi continued fraction of a moment sequence has positive coefficients iff the moments
are realizable; the Chebyshev–Markov–Stieltjes inequalities bound interval masses from (m₁, m₂). On the mark
support [1, 2] with (1, 4/3), these reproduce *exactly* the integrality bookkeeping m₂ = 2 − p₁ and the unique
integer-grid solution (2/3, 1/6, 1/6) already derived and CHECKED in [AN §3] — **no new constraint** from the
support structure. (The continued-fraction positivity for higher moments is the Herglotz–Padé route already
in [P3.5, P8.3]; a truncated CF is necessary-only — [CD-W3]-style wall.) **Label:** KNOWN-DEAD as new input.
**Cheapest probe:** none (already computed in [AN]).

**Pool-1 honest verdict:** the moments→DOS inversion literature *confirms* the (m₁, m₂, m₃) underdetermination
(its reconstruction machinery needs many moments) and contributes **no** provable "missing constraint" beyond
what [AN] already derived; its two genuinely transferable structures are the **quadrature/principal-
representation identification** (C1.1) and the **isospectral-classification framing** (C1.2).

---

## Pool 2 — Bond order / occupancy as traces: Wiberg/Mulliken statistics and idempotency bounds

Wiberg index W_AB = Σ_{i∈A}Σ_{j∈B}|P_ij|² and Mulliken populations are **trace statistics of the density
matrix P** (closed shell: P² = P idempotent, tr P = N, 0 ≤ eigenvalues ≤ 1) (REASONABLY BELIEVED, standard).
The certificate's marks m_ρ ∈ {1,2} are *occupancy-type* numbers; ‖·‖²_HS is a purity-type statistic — the
whole method is a "density-matrix theory" of the zero configuration. What chemistry knows about occupancies
at integer and non-integer values is the pool's raw material.

### C2.1 The penalty k_c(m) IS the occupancy-defect / idempotency bound — NEW (identification)
**Idea:** for m ≤ c, k_c(m) = 2cm − m² = c² − (c − m)², and this decomposes cleanly as
k_c(m) = c·m + c²·(m/c)(1 − m/c): the linear "occupancy" term c·m plus the *idempotency defect*
u(1−u) of the normalized occupancy u = m/c (CHECKED: for c = 2, 2m + m(2−m) = 4m − m² = k₂(m)).
The rank–trace inequality (Lemma 3.2) is therefore a *Fermi/idempotency bound* in disguise: it says
the PSD (on-line) rank is at least the "coherent occupancy content" minus the off-line cost. Chemistry's hard-core-boson picture completes the identification: marks ∈ {0,1,2}
(empty / singly / doubly occupied) with Σ marks = N is exactly a hard-core-boson occupancy distribution —
the certificate's extremal world (2/3 single, 1/6 double, 1/6 empty) is a hard-core-boson occupancy
distribution, and the "no more than 2 per site" constraint is the integrality input. **What this buys:** a
clean interpretation of why the walls sit where they do (the method is a *fermionic-occupancy bound on a
bosonic-occupancy world*), and a pointer that any *occupancy-inequality* from the hard-core-boson/Hubbard
literature is a candidate missing constraint — of which the only provable one known is integrality itself.
**Analogy:** density-matrix idempotency ↔ the rank–trace certificate; hard-core-boson double occupancy ↔ the
marks = 2 atoms.
**Needs:** none (identification; a 2-page writeup). **Feasibility:** immediate. **Label:** NEW (framing +
identification). **Cheapest probe:** none (pure identification).

### C2.2 Wiberg/Mulliken-style block trace statistics of W_T: the "bond order" and the local DOS — NEW (diagnostic)
**Idea:** W_T is prime-side data, so *any* statistic of the matrix is measurable: the **local density of
states** ρ_k = W_T[k,k]/tr(W_T) (the diagonal of the compressed form — the LDOS analogue), the **bond orders
between grid regions** ‖W_T[I,J]‖²_F for blocks I,J, and their total = ‖W_T‖²_F (the "Wiberg sum"). The LDOS
*shape* (flat = delocalized/featureless vs peaked = lattice-like) is a direct diagnostic of how far the real
configuration sits from the crystal worlds; the block bond orders are the *spatial* footprint of the
off-diagonal structure.
**Analogy:** LDOS ↔ the diagonal of W_T; bond order between atoms ↔ block Frobenius norms; Wiberg sum ↔
‖W_T‖²_F.
**Needs:** the W_T matrix (exists in tools/finitet). **Feasibility:** Low (measure). **Label:** NEW
(diagnostic). **Cheapest probe:** print diag(W_T)/N, its entropy and IPR, at T = 200–600 — 30 min.

### C2.3 Generalized Pauli constraints (Klyachko / Borland–Dennis) as the *form* of the missing constraint — NEW (form-identification; input KNOWN-OPEN)
**Idea:** the pure-state N-representability of a fermionic 1-RDM is a finite set of *linear inequalities* on
the occupancy spectrum — the generalized Pauli constraints (Borland–Dennis for 3 fermions in 6 modes: the
spectrum satisfies linear identities/inequalities beyond 0 ≤ λ ≤ 1 and Σλ = N; Klyachko 2006: the general
pure-state case — REASONABLY BELIEVED, standard). The certificate's mark space is already *fully described*
by the linear constraints {m_j ∈ {1,2}, Σm = N} (any such multiset is realizable by some Hermitian
compression — "ensemble representability" is trivial here, cf. C3.2). The transferable lesson: **any missing
constraint on the marks must be a linear inequality that is NOT implied by {marks ∈ {1,2}, Σm = N} — i.e. it
must come from a structural (2-body/representation-theoretic) hypothesis, not from the occupancy bounds
alone.** This converts "find the missing constraint" into "find the structural hypothesis" — the same
conclusion as [AN §5, LD]: the input must be beyond-bandwidth-1 / 2-body data.
**Analogy:** generalized Pauli constraints ↔ the missing mark inequalities; ensemble vs pure N-representability
↔ any-Hermitian-realization vs structural.
**Needs:** a literature-scoped 1-page writeup; the trivial computation that {1,2}, Σm=N admits no other linear
constraints.
**Feasibility:** Low. **Label:** NEW (form), KNOWN-OPEN (input). **Cheapest probe:** 30-min writeup + the
trivial polytope check (the feasible (p₁, m₂) segment is exactly m₂ = 2 − p₁, [AN §3]).

### C2.4 Fractional-occupancy defect as the finite-T departure statistic (P6) — NEW (P6 diagnostic)
**Idea:** at "electronic temperature" the density matrix is non-idempotent; the occupancy defect
tr(ρ − ρ²) = Σ λ_j(1−λ_j) measures departure from the integral world. At finite T our windowed operator Â
has eigenvalues that are *not exactly* the integer marks (near-rank-deficiency, min eigenvalue ~1e-17 [AF]) —
the defect D(T) = Σ_j λ_j(c−λ_j)-style (for the marks class, D = 0 iff integral) is a natural P6 diagnostic:
measure D(T) and its decay vs the [AF] ~1/log T deficit. If D(T) decays slower/faster, it splits the
finite-T error into "spectral non-integrality" vs "pair-correlation" parts.
**Analogy:** fractional-occupation DFT entropy ↔ the finite-T departure of the marks from integers.
**Needs:** the [AF] W_T spectra (exist). **Feasibility:** Low. **Label:** NEW (P6 diagnostic). **Cheapest
probe:** eigenvalue deviations from {1,2} at T = 200–700; fit the decay — 1 h.

### C2.5 Mulliken net-population per cell — KNOWN-INCORPORATED / LOW VALUE
**Idea:** per-site gross populations satisfy bounds (0 ≤ q_i ≤ 2, closed shell) — the analog is per-grid-cell
"populations" of the zero configuration, bounded by the marks — which is the integrality input already
priced. **Label:** KNOWN-INCORPORATED (folds into C2.2's diagnostic). **Cheapest probe:** none.

**Pool-2 honest verdict:** the trace-statistics pool contributes (i) the clean *identification* that the whole
method is an occupancy/idempotency bound (C2.1), (ii) a *form* for the missing constraint (a non-obvious
linear inequality on the marks — C2.3), and (iii) diagnostics (C2.2, C2.4). No new provable input yet — the
occupancy bounds available are exactly the integrality already priced.

---

## Pool 3 — DFT / Hohenberg–Kohn / Kohn–Sham: the N-representability problem

**Sweep-overlap check (task requirement):** attack-qi-sweep [QI] covered CS purity–rank, Q₊-side CS,
purity–negativity, Schmidt-number bounds, PPT, n₊-subadditivity, entropy, and higher moments — **it did NOT
cover the N-representability literature** (Coleman's 1-RDM theorem, Garrod–Percus G-conditions, the D/Q/G
positivity hierarchy, Klyachko's generalized Pauli constraints, ensemble-vs-pure representability). Pool 3 is
therefore a genuine *extension* of the sweep, not a duplication. The honest structural caveat (carried from
[QI §3.4]): the certificate's matrices act on a single Hilbert space with **no fermionic Fock / bipartite
structure**, so the 2-RDM inequalities do not apply verbatim — the transfer is at the level of the
*hierarchy form* and the *polytope structure*.

### C3.1 Garrod–Percus / D–Q–G positivity hierarchy: the "2-body level" check on the (1,1)-structure — NEW (extends [QI])
**Idea:** chemistry's central N-representability fact: the 1-RDM (occupancy) conditions are *vastly* weaker
than the 2-RDM conditions; the Garrod–Percus G-condition (a matrix-positivity inequality relating the 2-RDM
to the 1-RDM) and the D/Q/G hierarchy are the practical "higher levels" (REASONABLY BELIEVED, standard). The
transfer: the certificate (rank–trace on the marks) is the **Coleman level** (occupancy bounds — Coleman
1963: 0 ≤ λ ≤ 1, Σλ = N are necessary *and sufficient* for ensemble representability); the "G-level" would be
a *pairwise* (2-body) matrix inequality on the (1,1)-block structure. The sweep's §4 machinery can test the
natural GP-type candidate numerically on the actual v-vector structure. Expected verdict (honest prior): the
G-type inequality reduces to the CS refinement (L′) already shown to vanish at sharp configurations [QI §2.2]
— but *running it closes the Coleman gap in the sweep* as a documented result rather than an assumption.
**Analogy:** D/Q/G hierarchy ↔ the certificate hierarchy (occupancy → pairwise); Coleman level ↔ Lemma 3.2.
**Needs:** (i) the GP-type inequality stated for the (1,1)-block data; (ii) a numeric check on [QI]'s TEST-B
pairs.
**Feasibility:** Low (reuse tools/qi_sweep.py). **Label:** NEW (sweep extension), expected documented
negative. **Cheapest probe:** add the G-condition-type inequality to tools/qi_sweep.py on the per-pair blocks
— 1 h.

### C3.2 Ensemble vs pure N-representability: are the sharp worlds pure-state (principal) members? — TESTED-OPEN (merges C1.1)
**Idea:** Coleman's conditions certify *ensemble* (mixed-state) representability; pure-state representability
is strictly tighter (Klyachko). Our certificate's worlds are trivially *ensemble-realizable* (any marks
{1,2}, Σm = N is some Hermitian compression); the interesting question is whether the sharp worlds are the
*pure-state* (Nevanlinna-extremal / principal) members of their moment class — which [AN §2] machinery can
answer for the 256-law at its own (1, 1.3182). If the worlds ARE principal representations, the "pure-state"
reading does not exclude them (consistent with [AN]'s negative); if they are NOT (some interior measure), a
pure-state-type constraint is a live candidate missing input.
**Analogy:** ensemble vs pure N-representability ↔ any-Hermitian-realization vs principal-representation.
**Needs:** the (1, 1.3182) principal representations (same computation as C1.1). **Feasibility:** Low.
**Label:** TESTED-OPEN (expected negative, consistent with [AN]). **Cheapest probe:** same as C1.1 (merge).

### C3.3 The Hohenberg–Kohn / Kohn–Sham variational principle as the window optimizer — KNOWN-OPEN (references [P5.1, P3.3]; NEW fragment: variational collapse)
**Idea:** the Rayleigh quotient Q(v) with the |u−v| kernel is a Hartree-type functional (kinetic + 1D Coulomb
interaction) whose ground state is the cosine [AK]; the "exchange-correlation potential" is the LP dual (the
missing certificate) — this is the physics catalog's equilibrium-measure/external-field route [P5.1, P3.3]
renamed. The NEW chemistry-specific fragment: DFT's *variational-collapse* phenomenon (unrestricted/Symmetry-
broken solutions, discontinuities of v_xc) predicts the *shape* of the optimal certificate — the LP dual
should have contact-set/barrier structure with possible *discontinuities* at the active constraints
(consistent with [LD]'s tight LP: active duals at the validity-at-the-law and |r| ≤ 1 box constraints).
**Analogy:** KS self-consistent field ↔ the window variational problem; v_xc ↔ the LP dual certificate.
**Needs:** the [LD]/[AC] dual variables (already computed). **Feasibility:** Low (documentation + read-off).
**Label:** KNOWN-OPEN (references P5.1/P3.3), NEW fragment (collapse/shape prediction). **Cheapest probe:**
read the [LD] dual output for active-set/contact structure — 20 min.

### C3.4 The "integer-electron derivative discontinuity" as the c-cap jump (2/3 vs 5/6) — NEW (framing; already LP-computed)
**Idea:** DFT's band gap is a *derivative discontinuity* of E(N) at integer N (Perdew–Levy–Sham, REASONABLY
BELIEVED standard). Our certificate value as a function of the mark cap c jumps at integer c: c=2 → 2/3
(simple), c=3 → 5/6 (distinct), c=4 → 0.668 [AM §2 — already CHECKED NUMERICALLY]. The transfer is an
*identification* (the c-jump is the "integer-electron" discontinuity) that explains why the walls sit at
integer caps — no new provable input; the c=4 value is already computed and shows the optimum cap is c=3.
**Label:** NEW (framing); content already in [AM]. **Cheapest probe:** none (already computed).

### C3.5 The N-representability hierarchy as a pricing roadmap: 2-body inputs are worth vastly more than 1-body — NEW (roadmap)
**Idea:** chemistry's hard-won lesson is that the 1-RDM conditions are almost contentless compared to the
2-RDM conditions (the 2-RDM N-representability problem remains open and is "the central problem of density
matrix theory" — Coleman's phrase, REASONABLY BELIEVED). The transfer prices our program: every input that
can move constants ≥ 0.70 is *2-body* (pair correlation beyond bandwidth 1; repulsion/rigidity; the third
moment) and every 1-body input (marks, occupancy bounds, integrality) is already optimally priced. This is a
strategic statement, not a theorem — it says funding should track the 2-body inputs ([CD-V3/V4/V5], P1.4,
repulsion) and that no 1-body surprise is coming.
**Analogy:** 1-RDM vs 2-RDM conditions ↔ 1-body (marks) vs 2-body (correlation) certificate inputs.
**Needs:** none. **Feasibility:** immediate. **Label:** NEW (roadmap). **Cheapest probe:** none.

### C3.6 Kohn–Sham *self-consistency* as a new constraint family? — KNOWN-DEAD as input (honest)
**Idea:** in KS-DFT the potential is *self-consistently determined* by the density, adding equations, not just
inequalities. The analog for the zeros would be a *fixed-point equation* satisfied by the zero density — but
the only such equation known is the explicit formula itself (which the certificate already uses), and any
self-consistency statement would be exactly RH. **Label:** KNOWN-DEAD as a new input (equivalent-formulation
wall, cf. [CD-W4]). **Cheapest probe:** none.

**Pool-3 honest verdict:** N-representability is the strongest *form*-level match in this catalog (the
certificate IS a Coleman-level occupancy bound; the missing input is a 2-body/positivity constraint), but the
fermionic structure does not transfer verbatim, and the one checkable new item (C3.1, the GP-type sweep
extension) is expected to be a documented negative like [QI]. The pool's lasting value is the roadmap (C3.5)
and the pure-state reading (C3.2).

---

## Pool 4 — Delocalization / participation ratios: IPR as a fourth-moment statistic

The inverse participation ratio IPR = Σ|ψ_i|⁴ of a normalized eigenvector (≈ 1/N delocalized, ≈ O(1)
localized) is the standard localization order parameter (Anderson 1958; REASONABLY BELIEVED standard). IPR is
a fourth-moment-type statistic (the quartic moment of the site-resolved spectral measure). The zeros' Gabor
coefficient vectors v_ρ are *explicit* (delocalized by construction — |v_ρ[k]|² ~ (1/N)|φ̂-window|²), so the
single-vector IPR is computable exactly; the interesting object is the IPR of the *compressed operator's own
eigenvectors* (W_T's eigenvectors), which is prime-side-measurable and distinguishes crystal-like (localized)
from GUE-like (delocalized) spectra.

### C4.1 Eigenvector IPR of W_T as a spectral-distance diagnostic — NEW (diagnostic; extends [P1.3])
**Idea:** the crystal's eigenvectors are delta-localized (IPR ~ O(1)); GUE bulk eigenvectors have IPR ~ 3/N
(REASONABLY BELIEVED standard). The measured IPR of W_T's eigenvectors at T = 200–700 tells us whether the
real spectrum is *spectrally* near the crystal (IPR ~ O(1) on some modes) or GUE-like (IPR ~ c/N on all
modes). If delocalized, reality is far from the extremal law and the 0.6818 ceiling is "far from tight in the
realized world" — the cleanest slack measurement of P1.
**Analogy:** participation ratio ↔ localization order parameter; crystal (localized) vs GUE (delocalized)
phases.
**Needs:** W_T spectra (exists, [AF]/[CD-V1]). **Feasibility:** Low (measure). **Label:** NEW (diagnostic).
**Cheapest probe:** [AF] code: IPR of each eigenvector of W_T at T = 200–600; compare with 3/N and O(1) — 1 h.

### C4.2 The fourth-moment measurement: 13/4 vs 10/3 vs 3.2272 — NEW (diagnostic + loose-end resolution)
**Idea:** the *measured* fourth moment of the real zero configuration (tools/empirical_m3.py already computes
m₄ of the Gram matrix; tools/m4_check.py computes the determinantal-diagram m₄(1) vs the paper's 13/4)
discriminates the candidates: extremal world m₄ = 10/3 (mark-only diagonal), paper/GUE-claimed m₄(1) = 13/4
(including 4-point correlation terms), 256-law m₄ = 3.2272. Where reality's m₄ lands (a) **resolves the
UNRESOLVED provenance flag of [AN §6]** (13/4 vs 10/3 = the off-diagonal S₄ part), (b) prices the HL*(4,λ)
conjectural input [AM §4], (c) says which world reality is closest to spectrally.
**Analogy:** 4th moment of the spectral density ↔ the localization/curvature statistic; GUE sum rule ↔ the
13/4 target.
**Needs:** run the two existing scripts; interpret. **Feasibility:** Low (compute, scripts exist). **Label:**
NEW (diagnostic; resolves an [AN]-flagged loose end). **Cheapest probe:** run tools/m4_check.py and the m₄
part of tools/empirical_m3.py on the cached zeros — < 1 h.

### C4.3 Energy-resolved IPR: is there a "mobility edge" inside the spectrum of W_T? — NEW (diagnostic; merges C4.1 and Pool 6)
**Idea:** plot IPR(λ) against the eigenvalue λ of W_T. A sharp jump at some λ_c (two-phase spectrum: localized
below, delocalized above) would be a mobility-edge signature; a smooth GUE-like curve (IPR ~ c/N everywhere)
means single-phase. This is the *resolution* of the Anderson-type question (Pool 6) at the level of the
compressed operator.
**Analogy:** mobility edge ↔ an IPR(λ) jump; the localized fraction ↔ the fraction of modes with IPR ~ O(1).
**Needs:** same spectra as C4.1. **Feasibility:** Low. **Label:** NEW (diagnostic). **Cheapest probe:** fold
into C4.1 — 1 h.

### C4.4 The fourth moment as an *input*: HL*(4,λ) is conjectural — honest status
**Idea:** tr Â⁴ as a certificate input needs the 4-point correlation, which is NOT unconditionally evaluated
(kλ < 2 covers the 3rd moment only; the 4th is the HL*(4,λ) conjecture — [AM §4, CD-V3]). The *measured* tr
Â⁴ at λ = 1/2 (finite T, prime-side matrix) is a diagnostic that prices the conjecture's *numerical* value
before any analytic work (the same move [TB] made for m₃: empirical m₃ ≈ 4.8 vs the PROVEN m₃(1/2) = 5).
**Label:** NEW (diagnostic only; the input is KNOWN-OPEN/conjectural). **Cheapest probe:** fold into C4.2
(empirical_m3.py at λ = 1/2) — 30 min.

### C4.5 Participation ratio of the off-diagonal block (the "bond-order matrix") — NEW (diagnostic; folds into C2.2)
**Idea:** PR of the off-diagonal block of W_T measures how many grid cells the off-diagonal coupling touches —
large (delocalized coupling, GUE-like) vs concentrated (crystal-like pairs). Cheap, diagnostic only.
**Label:** NEW (diagnostic). **Cheapest probe:** fold into C2.2 — 30 min.

**Pool-4 honest verdict:** IPR-type statistics are *diagnostics* (they measure the real spectral distance from
the crystal and price the HL* inputs), not provable certificate inputs — but C4.2 is uniquely valuable because
it resolves a flagged UNRESOLVED ([AN §6]) and discriminates the candidate worlds with existing scripts.

---

## Pool 5 — Vibrational spectroscopy / Wilson GF method: the derivative tower as a secular problem

The GF method (Wilson–Decius–Cross): the vibrational frequencies are the roots of the secular equation
|GF − λI| = 0 with G the inverse-mass matrix and F the force-constant matrix; the *traces* tr((GF)^k) are
determined by the mass and force-constant matrices alone ("sum rules") — coordinate-free content
(REASONABLY BELIEVED, standard). The derivative tower ξ′/ξ, ξ″/ξ′, … are the log-derivative (Green's
function / Stieltjes-transform) ratios of the zero measure — the "secular" objects of a "molecular chain"
whose "masses" are the multiplicities. P5's open question: do the level-j certificates give *joint*
constraints the single-level ceiling laws do not see? ([CD-A4] killed the naive *pairwise* interlacing LP:
interlacing gives only a lower bound; the *joint* structures below are different objects.)

### C5.1 The GF sum rules: the derivative-tower moments are *determined* by the level-0 data — NEW (P5)
**Idea:** the moments of the ξ^(j)-zero set are NOT free parameters — they are determined by ζ's zeros through
the explicit formulas for ξ^(j)/ξ^(j−1) (mechanical, [CD-V9]). The GF lesson (traces of the secular problem
are coordinate-free sum rules) says: the level-j certificates are *joint constraints on the same
configuration* — any world must satisfy ALL of them simultaneously. This is strictly stronger than the
pairwise-interlacing LP killed in [CD-A4] (which used only counting data) because it uses the *moments* of the
derivative-zero sets, which the single-level ceiling analysis of the 256-law does not constrain. Concretely:
compute the two moments of the ξ′-zero set empirically (data EXISTS: tools/data/xiprime_on_line_1_1000.txt)
and analytically (from the ξ′/ξ explicit formula — machinery in tools/check_xiprime.py and the Lean XiPrime
files); compare the empirical value with the level-0-derived prediction. If the ξ′-two-moment constant implied
by the paper's ξ′ theorem (0.85838/0.86864) is incompatible with the level-0 data + explicit formula, there is
a *joint* constraint the ceiling world must satisfy.
**Analogy:** GF sum rules ↔ the moments of the derivative-zero sets as derived (not free) quantities.
**Needs:** (i) the ξ′/ξ explicit formula (exists in Lean/tools); (ii) the empirical moments from the existing
data.
**Feasibility:** Low (empirical part; analytic part Med). **Label:** NEW. **Cheapest probe:** m₁, m₂ of the
xiprime_on_line data (10 min) vs the level-0 moments; and the [CD-V9] formula check.

### C5.2 The derivative tower as a Gauss/Ritz tower: joint interlacing of ξ, ξ′, ξ″ — NEW (structure; P5)
**Idea:** for a real-rooted polynomial p, the zeros of p′ interlace those of p (Rolle — [CD-A4]'s dead end),
but the *joint* structure of the whole tower is the **Gauss-quadrature tower** of the zero-distribution
measure: the zeros of ξ^(j) are the Gauss nodes of a related (shifted) measure, and successive-level nodes
interlace in the Ritz sense (the eigenvalues of successive principal submatrices of ONE Jacobi matrix). This
is a *matricial* constraint on ALL levels at once — strictly stronger than pairwise interlacing. Empirically
checkable: do the real zero sets of ξ, ξ′, ξ″ (data for ξ, ξ′ exists; ξ″ computable from the G(t)-pattern
code in tools/check_xiprime.py) form a Ritz tower — i.e., is there ONE Jacobi matrix whose principal-submatrix
spectra match all levels? If YES, a hidden Jacobi structure exists (candidate joint certificate); if NO, the
secular/Ritz picture is refuted (clean documented negative).
**Analogy:** Ritz values of principal submatrices ↔ the derivative tower; Gauss-node interlacing ↔ joint
Rolle.
**Needs:** ξ″ zeros (compute from the explicit formula); a small Jacobi-reconstruction solve.
**Feasibility:** Med (2–3 h). **Label:** NEW (structure) — the *joint* version of [CD-A4] (documented
difference). **Cheapest probe:** numerical interlacing/consistency check with the two existing datasets +
computed ξ″ — 2–3 h.

### C5.3 Newton-identities / secular-polynomial certificate at finite T — NEW (P6 / [CD-V20] synergy)
**Idea:** the full characteristic polynomial of the finite-rank W_T is prime-side-computable (Newton's
identities from the finite-T traces tr Â^k, k = 1..N); the rank–trace bound is the degree-2 Newton statement;
higher degrees give a *per-T* LP whose value curve vs T is the empirical target for the effective theorem
([CD-V20], P9.1). The blocker is the error terms of the *asymptotic* moments (the bandwidth wall), not the
matrix computation — reframing P6 as "bound the finite-T traces' approach to their asymptotics."
**Analogy:** Newton's identities ↔ traces ↔ secular coefficients (classical, PROVEN-class).
**Needs:** [AF]'s W_T; tr Â^k for k = 3..6 at T = 200–600; the per-T LP value.
**Feasibility:** Low–Med (compute). **Label:** NEW (framing + P6 synergy). **Cheapest probe:** tr Â^k,
k = 3..6, from the [AF] matrix; the per-T LP value vs 0.6725 and its 1/log T trend — 1–2 h.

### C5.4 The GF product structure: W_T = B^t Diag(ν) B as a "GF factorization" — NEW (framing; the coordinate-free reading)
**Idea:** W_T = B^t·Diag(ν)·B with ν = µ + λ_T + π_T (the prime-side measure; [CD-V1]) — a GF-type product
structure. The GF lesson: the *spectrum* of the product depends on coordinates, but the *traces* are
coordinate-free sum rules — for us, tr and ‖·‖² are fixed by the explicit formula (that IS the certificate),
while the *eigenvectors* (and any eigenvector statistic like IPR) are coordinate/compression-dependent. The
honest reading: the certificate is the coordinate-free part of a GF-type problem; the missing input is
coordinate-dependent (beyond-bandwidth-1). Framing only, but it explains why [P5.3]/C4.1 diagnostics measure
*compression-dependent* objects.
**Analogy:** GF = G·F product ↔ W_T = B^t D B; coordinate-free traces ↔ the two moments.
**Needs:** none (documentation). **Label:** NEW (framing). **Cheapest probe:** none.

### C5.5 Empirical level counts: the ξ′-on-line count ratio — NEW (diagnostic)
**Idea:** the existing data (1009 ξ′-roots for the first 1000 ζ-zeros, including 9 small-t roots below γ₁)
gives the *empirical* ratio N₀(ξ′, T)/N(T) — a direct measurement of how the tower's on-line content grows,
to compare with the FGL/paper constants' implications (ξ′ constant 0.85838 > 2/3 — but note the honest
[CD-A4] caveat: this does NOT imply ≥ 85.8% for ζ). The count ratio + the small-t extra roots are cheap,
honest data for P5.
**Label:** NEW (diagnostic). **Cheapest probe:** count the ξ′-roots in [0,T] vs ζ-roots from the existing
files — 10 min.

**Pool-5 honest verdict:** the GF method's genuine contribution is the *joint* structure of the derivative
tower — C5.1 (moments as derived quantities) and C5.2 (the Ritz/Gauss tower) are the first *joint* (as
opposed to pairwise [CD-A4]) P5 constraints in the catalog, both checkable on existing data. C5.3 ties the
tower's secular reading to P6.

---

## Pool 6 — Disordered systems / Anderson localization: the on-line/off-line question as a mobility-edge problem

Anderson localization: disorder localizes eigenstates (IPR ~ O(1)); a mobility edge separates localized from
delocalized phases; the spectral statistics change phase (Poisson ↔ Wigner–Dyson); the localized fraction is
the order parameter (REASONABLY BELIEVED, standard). The transfer to "on-line vs off-line": the off-line
pairs are the "defect/localized" structure the method cannot price; reality is (empirically) fully on-line
(all 1000 first zeros simple [AM]) — i.e., reality sits deep in the "delocalized phase." The honest content:
the mobility-edge picture says the only input that moves the wall is a *phase-exclusion* statement
(repulsion/rigidity — P1.4, KNOWN-OPEN) — but it supplies two cheap diagnostics (the localized-fraction
scaling and the energy-resolved IPR).

### C6.1 The localized-fraction scaling: n₋(W_T)/N vs T — NEW (diagnostic; extends [P1.3])
**Idea:** the negative-eigenvalue content of W_T is the "localized fraction" (off-line pairs inject (1,1)-
planes; the worlds have n₋ = 0). At every finite T, W_T has tiny negative eigenvalues (near-rank-deficiency
[AF]); the *count density* n₋/N and its T-trend is the mobility-edge diagnostic: if n₋/N decays (1/log T-
class?), reality is on the "no off-line pairs" side and the negatives are finite-T artifacts; if it saturates,
reality has genuine off-line content the method is missing. This extends [P1.3] (which measured the edge
*density*) with the *scaling* and the explicit "off-line rate" readout.
**Analogy:** localized fraction ↔ negative-eigenvalue density; mobility-edge scaling ↔ the n₋/N(T) trend.
**Needs:** W_T spectra (exists). **Feasibility:** Low. **Label:** NEW (extends P1.3). **Cheapest probe:**
count negative eigenvalues of W_T at T = 200…700; fit n₋/N vs T — 1 h.

### C6.2 Energy-resolved IPR / mobility-edge detection — NEW (merged with C4.3)
**Idea:** IPR(λ) of W_T's eigenvectors as a function of eigenvalue: a two-phase spectrum (localized modes at
some energies) vs single-phase GUE-like. The crystal's prediction: modes at eigenvalue 2 are "localized" (the
double-mark atoms) — reality's IPR(2)-neighborhood vs the bulk is the test.
**Analogy:** mobility edge ↔ an IPR(λ) jump inside the compressed spectrum.
**Needs:** same as C4.1/C4.3. **Feasibility:** Low. **Label:** NEW (diagnostic). **Cheapest probe:** fold
into C4.1 — 1 h.

### C6.3 Spectral-statistics phase test: spacing ratios of W_T's eigenvalues — NEW (extends [P5.3])
**Idea:** Anderson-locality's cleanest phase diagnostic: level-spacing statistics (Poisson = localized =
crystal-like; Wigner–Dyson = delocalized = GUE-like). [P5.3] proposed the compression-ensemble spacing
statistic; the NEW bit is the *crystal prediction*: the 256-law's spacing distribution (δ-like, lattice
statistics) vs the measured spacing ratio of W_T — a direct two-phase test of the real spectrum.
**Analogy:** Poisson vs Wigner–Dyson ↔ crystal vs GUE phase; spacing ratio ↔ phase order parameter.
**Needs:** W_T spectra (exists). **Feasibility:** Low. **Label:** NEW (extends P5.3). **Cheapest probe:**
spacing-ratio statistic of the [AF] spectra — 1 h.

### C6.4 Thouless / self-averaging prior for the family route — KNOWN-OPEN (references [CD-V12], [P4.4])
**Idea:** Anderson physics: self-averaging quantities (the conductance) concentrate; the physics prior that
the family-averaged certificate self-averages (per-character concentration) is [P4.4]/[P10.5]'s variance
target. No new math; reference. **Label:** KNOWN-OPEN (framing; reference). **Cheapest probe:** [P4.4]'s
variance probe.

### C6.5 The bandwidth-1 wall AS the measurement channel's mobility edge — KNOWN-OPEN (framing; [P2.2] reference)
**Idea:** the λ ≤ 1 wall is where the certificate's "measurement channel" localizes: below X = T the
off-diagonal prime sums are MV-controlled (rigid/delocalized channel), above they are HL-strength
(chaotic/localized channel) — [CD-A1/A5, P2.2]. The mobility-edge reading restates the wall without adding a
route. **Label:** KNOWN-OPEN (framing). **Cheapest probe:** none.

### C6.6 Fluctuation/rigidity phase separation (Selberg CLT vs the crystal) — KNOWN-OPEN (references [CD-V13]; likely-negative)
**Idea:** the crystal has O(1) count fluctuations; ζ's are Gaussian of size √(log log T) (Selberg CLT). Any
provable fluctuation input separates the phases — but the leading variance is fixed by small-α F data the law
already matches, and the distribution *shape* has no known mechanism to enter a per-T certificate
([CD-V13]'s kill criterion). Reference; no new fragment. **Label:** KNOWN-OPEN (likely-negative; reference).
**Cheapest probe:** none.

**Pool-6 honest verdict:** the Anderson/mobility-edge pool contributes two cheap diagnostics (C6.1, C6.3)
that measure reality's "phase" (delocalized vs crystal-like) at the level of the compressed operator, and
confirms — via the localization picture — that the wall is a channel-localization phenomenon ([P2.2], C6.5).
No new provable input: proving the zeros are "delocalized" IS the repulsion/rigidity open problem (P1.4).

---

## TOP 10 (EV × feasibility × cheap-probe), ranked

1. **C4.2 — Fourth-moment measurement (13/4 vs 10/3 vs 3.2272).** The cleanest discriminator between the
   extremal world, the 256-law, and the GUE/HL* target; resolves the [AN §6]-flagged UNRESOLVED m₄
   provenance; prices the HL*(4,λ) input; scripts exist (tools/m4_check.py, empirical_m3.py). Probe < 1 h.
2. **C5.2 — Derivative tower as Gauss/Ritz tower (joint interlacing).** The first *joint* (not pairwise
   [CD-A4]) P5 constraint; checkable on existing ξ′ data; a positive (hidden Jacobi structure) or a clean
   documented negative. Probe 2–3 h.
3. **C5.1 — GF sum rules: derivative-tower moments as derived quantities.** The P5 joint-moment program;
   empirical part < 1 h on existing data; analytic part mechanical ([CD-V9]). Probe 10 min (empirical).
4. **C1.2 — Isospectral/switching classification of the two-moment degeneracy class.** Directly answers
   "which worlds are spectrally identical" ([AM §0]); any switching-breaking provable input moves the wall.
   Probe 1–2 h (small numerics).
5. **C4.1/C4.3/C6.2 — Eigenvector IPR and energy-resolved IPR of W_T.** The cleanest measurement of the real
   spectral distance from the crystal (P1 slack); single probe. 1 h.
6. **C3.1 — Garrod–Percus / G-condition sweep extension.** Closes the Coleman gap in [QI] honestly; expected
   documented negative (like the sweep); reuse tools/qi_sweep.py. 1 h.
7. **C1.1/C3.2 — Principal representations of the 256-law's own (1, 1.3182) moment problem.** Pins the
   "pure-state" reading of the sharp worlds; extends [AN §2]; reuse tools/nevanlinna_check.py. 30 min.
8. **C2.4 — Occupancy-defect (finite-T non-integrality) statistic.** A new P6 error decomposition; the defect
   decay vs the [AF] 1/log T curve. 1 h.
9. **C6.1 — Localized-fraction scaling (n₋/N vs T).** The off-line-rate readout; extends [P1.3]; addresses
   "how far is reality from the off-line side." 1 h.
10. **C5.3 — Newton-identities / per-T secular LP.** The empirical target for the effective theorem
    ([CD-V20], P9.1); tr Â^k at finite T and the per-T LP value curve. 1–2 h.

**Strategic reading:** C4.2 is the standout — it is the cheapest vector with *direct* bearing on P1/P2
(separating the candidate worlds and resolving a flagged loose end), and it uses only existing scripts. The
P5 cluster (C5.1, C5.2) is the catalog's only genuinely new *structural* direction (joint, matricial
interlacing vs the dead pairwise LP). C1.2 and C3.1 attack the degeneracy/representability structure directly
(one expected-negative sweep-completion, one new classification). The diagnostics (C4.1, C2.4, C6.1, C5.3)
all change what we believe about the method's real slack before any expensive funding. As in the physics
catalog, the persistent wall — beyond-bandwidth-1 pair correlation, third/higher moments, repulsion —
remains the only route to constants ≥ 0.70, and the chemistry picture (C3.5, C6.5) explains why: those are
*2-body* inputs, and the 1-body (occupancy/integrality) class is provably exhausted.

---

## WILD section (deliberately absurd premises; honestly evaluated; each labeled)

### CW-1. "The zeros are the eigenvalues of a giant Hückel matrix of the prime graph; RH is the absence of defect states above mark 1" — CONJECTURED (vocabulary; no new input)
**For:** the moments of the tight-binding DOS count closed walks; our prime-side moments (ΣΛ(n)²/n-type
diagonal sums) are "closed-walk counts" of the prime cascade — a genuine reading of the explicit formula as a
walk count.
**Against:** no such Hamiltonian is known (Hilbert–Pólya); the "defect states" are the marks > 1, and their
exclusion is exactly RH. Vocabulary only.
**Honest fragment worth keeping:** the closed-walk *reading* of the two moments (m₁, m₂ as walk counts of the
prime graph) — a 1-page interpretation note; no theorem.

### CW-2. "The 0.6818 law is a charge-density wave (CDW) of the zero lattice; the missing input is its elastic (formation) energy" — CONJECTURED (labels the KNOWN-OPEN repulsion input)
**For:** the law is a periodic, defect-laden lattice (a CDW); a CDW costs elastic energy; proving the zeros'
CDW formation energy is positive = repulsion (P1.4).
**Against:** the "formation energy" is exactly the missing repulsion/rigidity input; the only *computed*
"defect energy" is the LP dual (dual −1 at the validity constraint — [LD]) — already in hand, and it is the
certificate's shadow price, not a new input.
**Honest verdict:** the [LD] dual IS the "CDW chemical potential"; nothing new beyond C1.6/P1.6. Do not fund.

### CW-3. "The zeros are fermions; the generalized Pauli constraints are the missing input — and they exclude the worlds, not reality" — CONJECTURED (identification; input KNOWN-OPEN)
**For:** if the zeros are free fermions (sine-kernel — [W-P2]'s identification), the 1-RDM is the sine kernel
and the marks are *determined* — trivially satisfying all generalized Pauli constraints. Reality (all simple)
satisfies every GPC; the *extremal worlds* (marks 2) violate any GPC that caps occupancies at 1 — i.e., a
GPC-type input would exclude exactly the worlds the certificate needs to exclude.
**Against:** the fermionic identification is conjectural (it IS RH + pair-correlation); no provable GPC exists
for the marks without the full Hilbert–Pólya structure (C2.3, C3.2's honest caveat).
**Honest verdict:** the *form* (a linear inequality the worlds violate but reality satisfies) is precisely the
shape of the missing constraint — worth one page, nothing more.

### CW-4. "The derivative tower is the vibrational spectrum of a ladder molecule; RH = dynamical stability (all frequencies real)" — CONJECTURED (equivalent-formulation)
**For:** ξ real-rooted ⟺ all "vibrational frequencies" (zeros of ξ, ξ′, …) real — dynamical stability; the GF
secular determinant's roots are the zeros of ξ^(j).
**Against:** real-rootedness of ξ IS RH (Hermite–Biehler, classical); the "stability matrix" is W_T renamed;
the finite check is [CD-V16]'s Hermite–Biehler shadow. Equivalent-formulation wall ([CD-W4]).
**Honest verdict:** no new fragment; the *empirical* GF stability matrix (the on-line part of W_T's
positivity) is already measured (near-rank-deficiency, [AF]).

### CW-5. "The finite-T deficit is the electronic-temperature smearing of the marks: Δ(T) ~ k_B T_eff is the 'thermal' departure from the crystal" — CONJECTURED (framing; content = P6)
**For:** the [AF] Δ(T) > 0, ~1/log T deficit is a "temperature"-dependent departure of the marks from the
integral world (C2.4's defect); a "Fermi-smearing" fit gives a physics prior for the P6 error shape.
**Against:** the deficit is dominated by the off-diagonal pair sum ([AF] — PROVEN analysis), not by an
electronic-temperature mechanism; the fit is an analogy.
**Honest verdict:** the C2.4 defect statistic is the checkable version; run it, keep the smearing language out
of any theorem.

---

## Label inventory

- **NEW** (invented here, untested): C1.1 (quadrature bit), C1.2, C1.5, C2.1, C2.2, C2.3, C2.4, C3.1, C3.2,
  C3.3 (fragment), C3.4, C3.5, C4.1, C4.2, C4.3, C4.4, C4.5, C5.1, C5.2, C5.3, C5.4, C5.5, C6.1, C6.2,
  C6.3, CW-1 … CW-5 (conjectured by construction).
- **KNOWN-DEAD / KNOWN-INCORPORATED** (documented to prevent re-derivation): C1.4 (alternant symmetry —
  incorporated in Lemma 3.1), C1.6 (CMS/CF — folds into [AN §3]), C3.6 (self-consistency — equivalent
  formulation), C2.5 (Mulliken per-cell — folds into C2.2), C6.6 (Selberg-CLT fluctuation — references
  [CD-V13]'s kill criterion).
- **KNOWN-OPEN** (core open / already flagged; new framing only): C1.3 (band edge = λmax; [P4.3]), C2.3 /
  C3.2 / CW-3 (GPC/N-representability inputs — need a structural hypothesis), C3.3 (KS/equilibrium measure;
  [P5.1, P3.3]), C6.4 (self-averaging; [P4.4, P10.5]), C6.5 (channel mobility edge; [P2.2]).
- **TESTED-OPEN**: C1.1/C3.2 (extends [AN §2]'s computed principal representations; the (1, 1.3182) check is
  the open bit); C5.2 (structure claimed, numerical test pending).
- **Cheapest-probe discipline:** every vector above has a < 1 h probe (existing tools: finitet, qi_sweep,
  nevanlinna_check, m4_check, empirical_m3, xiprime data) or is a documentation/framing item. Nothing here
  requires new heavy compute to *start*.

**Honest closing note:** the chemistry/condensed-matter angle's two strongest NEW contributions are (i) C4.2
— the fourth-moment measurement that discriminates the candidate worlds and resolves the [AN]-flagged m₄
provenance, and (ii) the P5 cluster C5.1/C5.2 — the first *joint* derivative-tower constraints (GF sum rules
and the Gauss/Ritz-tower interlacing), both checkable on data that already exists in tools/. The rest of the
catalog is dominated by diagnostics (they change what we believe about the method's real slack) and
form-identifications (C2.1, C2.3, C3.5: the missing constraint is a *2-body* input; the 1-body occupancy
class is provably exhausted — consistent with [AN, LD, AM]). The persistent wall — beyond-bandwidth-1 pair
correlation, higher moments, repulsion — is unchanged; the chemistry angle sharpens *why* (the certificate is
a Coleman-level occupancy bound; only 2-body inputs move it) and offers cheap, honest measurements of the
slack that these inputs would have to explain.

---

## 11. Code-backed verification (Round 1 probes) — every number from code run in this session

**Protocol:** all numbers below were produced by scripts run in this session
(`uv run --quiet --with numpy python tools/chem_probe.py`, `uv run --quiet --with numpy python tools/m4_check.py`,
extended R-scan inline). Data: `tools/data/zeros_1_1000.txt` (1000 LMFDB zeros), `tools/data/xiprime_on_line_1_1000.txt`
(1009 ξ′-on-line roots). Labels: CHECKED NUMERICALLY = printed by the cited script in this run; PROVEN = from the
cited notes/Lean. Files: `tools/chem_probe.py` (new, this session), `tools/m4_check.py` (pre-existing).

### F1 (C4.2) — flat-window moments of the real configuration, N = 1000 (CHECKED NUMERICALLY)
λ = 1: m₂ = 1.2841, m₃ = 1.8368, m₄ = 2.8198 (all 1000 zeros); interior (idx 51–950): m₂ = 1.2861, m₃ = 1.8426,
m₄ = 2.8334. Theory targets: m₂ → 4/3, m₃(1) = 2 (PROVEN [TB]), m₄(1) = 13/4 (paper claim). Finite-height deficit
grows with moment order: m₂ ~3.6%, m₃ ~8%, m₄ ~13% below the asymptotic targets. Consistent with [AF]'s measured
windowed m₂ ≈ 1.283–1.291 (qi_sweep TEST A bound/N = 0.709–0.717 ⟹ m₂ = 2 − bound/N).

### F2 (C4.2) — λ = 1/2 (CHECKED NUMERICALLY)
m₂ = 2.1219, m₃ = 4.7291, m₄ = 10.9476 (all 1000); interior m₃ = 4.7369 vs PROVEN m₃(1/2) = 5 [TB] (deficit 5.3%,
matching [TB]'s reported empirical ≈ 4.8).

### F3 (C4.2) — λ = 2/3 (CHECKED NUMERICALLY)
interior m₃ = 3.0367 vs PROVEN m₃(2/3) = 13/4 = 3.25 [TB] (deficit 6.6%). Note: 13/4 = m₃(2/3) (PROVEN) is a
*different* quantity from the paper's claimed m₄(1) = 13/4; the coincidence of values is flagged below.

### F4 (C4.2, the headline negative) — the natural 4th-moment diagram does NOT reproduce 13/4 (CHECKED NUMERICALLY)
`tools/m4_check.py` (determinantal diagram, rho4 formula verified against np.linalg.det — checks pass) gives a
converged (R ≥ 160 plateau) value **m₄(1) ≈ 4.64** (A₄ → +0.972; run at R = 10, 20, 40, 80, 160, 320 in this
session), **not 13/4 = 3.25**. The paper's claimed m₄(1) = 13/4 is therefore NOT reproduced by the natural
sine-kernel diagram computation. Neither 13/4 nor the diagram value equals the extremal-world mark-only value
m₄ = 10/3 [AN]. The [AN §6] "UNRESOLVED provenance" flag for 13/4 is upgraded to: **numerically contradicted by
the natural computation** — either the paper's 13/4 refers to a different normalization/quantity, or the diagram
(or the paper's combinatorics) is wrong. Adversarial re-check of both sides is the next step; do not cite either
value as settled. (Honest caveat: the m4_check diagram is a third-party script not yet adversarially validated.)

### F5 (C5.5) — ξ′-on-line count data (CHECKED NUMERICALLY)
1009 ξ′-roots for the first 1000 ζ-zeros, including 10 small-t roots below γ₁ (ordinates 0.0944, 0.2215, 0.3140,
0.4850, 0.5357, 0.6448, 0.7247, 0.8159, 0.8714, 11.1975 — matches the list in `tools/check_xiprime.py`). In the
window [100, 900): 539 ξ′-zeros on the line vs 540 ζ-zeros → ratio 0.9981. The ξ′-zero density equals the ζ-zero
density (Rolle-consistent); the extra roots are all below γ₁.

### F6 (C5.1 empirical) — ξ′-zero-set moments (CHECKED NUMERICALLY)
Flat-window second/third moments of the ξ′-zero ordinates (N′ = 989 after trimming small-t roots and edges):
m₂ = 1.1109, m₃ = 1.3191 — both *below* the ζ-configuration values (m₂ ≈ 1.286, m₃ ≈ 1.84), ratio
m₂(ξ′)/m₂(ζ) = 0.8332. The ξ′ zeros are measurably more rigid (smaller two-moment footprint) than ζ's zeros —
qualitatively consistent with the paper's ξ′ constants (0.85838/0.86864 > 0.6725). **Qualitative consistency
check only**: the ξ′ certificate uses its own functional (different kernel), so 2 − m₂(ξ′, flat) is NOT the ξ′
constant; no derivation is claimed.

### F7 (C1.1/C3.2) — the 256-law is the unique grid-constrained solution of its own moment problem (CHECKED NUMERICALLY)
Law masses (empty, simple, double) = (0.159086, 0.681829, 0.159086), moments (m₀, m₁, m₂) = (1, 1, 1.318171) =
(1, 1, 2 − p₀). The grid-constrained problem (atoms ⊆ {0,1,2}, these three moments) has the **unique** solution
(a, b, c) = (0.159086, 0.681829, 0.159086) — the law itself (match = True to 1e-12). The two 2-atom Hamburger
principal representations of (1, 1, 1.318171) are P⁻ = {0.435933, 1.564067} (masses ½, ½) and
P⁺ = {0, 1.318171} (masses 0.241373, 0.758627); both verify (m₁, m₂) to 1e-8. The law (3 atoms on {0,1,2}) is
**not** a 2-atom Hamburger principal representation but **is** the unique grid-constrained ("pure-state-on-the-grid")
member — mirroring [AN §3]'s result for (1, 4/3). Consequence (consistent with [AN]): a "pure-state/principal-
representation-type" constraint does NOT exclude the law; the grid-extremality is already what the certificate
reads. C3.2's expected-negative is confirmed.

### F8 (C6.1) — negative-eigenvalue content of W_T: zero at all tested T (CHECKED NUMERICALLY)
n₋(W_T)/N = 0 at T = 200, 300, 400, 500, 600, 700 (N = 123…569), under both a relative 1e-9 and an absolute
1e-12 threshold. The near-rank-deficiency negative eigenvalues are numerical artifacts below 1e-12 (min eig
3.4e-15 … −1.5e-15). The real configuration carries **no resolvable off-line (negative) content** at these
heights — the "localized fraction" is 0, consistent with the all-simple empirical world [AM].

### F9 (C4.1) — eigenvector IPR of W_T: NOT GUE-like (CHECKED NUMERICALLY)
meanIPR·N of W_T's normalized eigenvectors grows 25.6 → 97.8 as T goes 200 → 700 (N: 123 → 569); GUE bulk
predicts ≈ 3. IPRmax = 0.63–0.87 (some eigenvectors are nearly single-component). Energy-resolved at T = 400:
meanIPR·N ranges from ≈ 17.6 (bulk, eig ≈ 0.8–0.9) to ≈ 132 (eig ≈ 1.3–1.4); spectral edges (both low and high)
are more localized. The compressed operator's eigenbasis is far from RMT-delocalized with a systematic
localization profile (Gabor/frame-boundary dominated). Diagnostic: eigenvector-level statistics of W_T are NOT
the place to look for RMT agreement; the delocalization question is settled by the operator's *deterministic
frame structure*, not by random-matrix universality.

### F10 (C2.4) — finite-T non-integrality of the spectrum (CHECKED NUMERICALLY)
Mean distance of the normalized spectrum from the integral marks {1,2}: dev1_2/N ≈ 0.355–0.362, essentially
T-independent over 200–700. The finite-T spectrum is substantially non-integral (the marks are only asymptotic)
— this is the finite-T slack [AF] already documents; the "occupancy defect" is large and flat in this T-range.

### What was NOT run (honest scope note)
- C5.2 (Ritz/Gauss tower, joint interlacing): needs ξ″-zero computation via the ξ″/ξ explicit formula — 2–3 h, next.
- C1.2 (isospectral/switching classification): needs the small-LP numerics — 1–2 h, next.
- C3.1 (Garrod–Percus/G-condition sweep extension): needs an extension of tools/qi_sweep.py — 1 h, next.
- C6.3 (spacing-ratio phase test): needs the W_T eigenvalue spacing statistics — 1 h, next.
- C4.4 (tr Â⁴ at λ = 1/2 as HL* pricing): folds into F2/F4 data — see F4's negative.

### One-line bottom line
The cheapest probes are run: the m₄ = 13/4 provenance is **numerically contradicted** (F4 — the natural diagram
gives ≈ 4.64), the ξ′-tower data is rigid-consistent (F5/F6), the 256-law is grid-extremal as predicted
(F7 — consistent with [AN]'s negative), and reality shows zero off-line content with a non-RMT eigenbasis
(F8/F9). All four P5/P6 diagnostics change what we believe about the method's slack; no constant moved.
