# Idea Generator: additive combinatorics / quasirandomness / analytic number theory attack catalog

**Agent:** IDEA GENERATOR (additive-combinatorics angle). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Every vector is
labeled **NEW** (invented here, not in prior catalogs) / **KNOWN-DEAD** (killed in earlier rounds; cite) /
**KNOWN-OPEN** (a known open problem or a route already flagged; cite) / **TESTED-OPEN** (numerically
tested by our tools, still open). Literature claims are asserted only where the source is held in
`research/papers/` or is a standard theorem; anything reported without a held source is marked
"reported — verify before use".
**Overlap discipline:** crossdomain catalog = `idea-generator-crossdomain.md` [CD-V#]/[CD-A#]/[CD-W#];
physics catalog = `idea-generator-physics.md` [P#.#]; attack notes = attack-multiplicity [AM],
attack-ceiling [AC], attack-lpdual [LPd], attack-twobandwidth [TB], attack-m29 [M29], attack-kernel [AK].
**Every number in this file comes from code run for this session** (uv run --quiet python), saved in
`research/notes/probes-additive/` (probe_additive_a.py, probe_additive_a2.py, probe_b3.py, probe_b5.py,
probe_b6.py), or from the cited notes' own computed tables.

---

## 0. The honest map of where we stand (what the additive-combinatorics toolbox can and cannot contribute)

Our three open problems, with the state of the art the new catalog must respect:

- **(P2) break the 5/6 distinct wall by an unconditional third moment.** This route is now **CLOSED as a
  documented negative**, with two independent layers:
  1. [TB] (executioner, Round 2): the correct third moments are m₃(1/2) = **5**, m₃(2/3) = **13/4**,
     m₃(1) = **2** (the task's m₃(1/2) = 2 was REFUTED); the only proven third-moment mechanism for
     N_d (the paper's admissible-cubic construction, §7.5(g)) gives 0.7593 at λ = 1/2 and 0.8071 at
     λ = 2/3 — both < 5/6 — and the joint two-bandwidth certificate has no cross-window inequality.
  2. **NEW, verified here (probe_additive_a.py):** even at λ = 1, where m₃ = 2, the third moment cannot
     move N_d, because the extremal crystal **saturates it**: the multiplicity multiset
     {1 × 2N/3, 2 × N/6} has moments (m₁, m₂, m₃) = (1, 4/3, 2) — identical to the GUE values — and
     the min-N_d LP under (m₁, m₂, m₃) + integrality has optimum **exactly 5/6** (the crystal is
     feasible and optimal; CHECKED NUMERICALLY, HiGHS). The [AM] inequality Σm(m−1) ≥ 2Σ(m−1) makes
     this a proof: every (1, 4/3)-configuration has N_d ≥ 5N/6, equality only for the crystal, which
     has m₃ = 2.
  The Gowers-ladder explanation (Pool 1, G1-ADD) is the *structural reason*: the third moment is a
  **U²-level (three-term) statistic**, governed by two-point Fourier information that the crystal already
  matches (F ≡ 1 on [0,1]); the first rung with separating power is the 4th moment (U³-level) — and even
  that is degenerate in-class at λ = 1 (see below).
- **(P3) form factor beyond α = 1.** [M29] closed "a proven sliver beyond 1": the Montgomery–Vaughan
  bound exceeds the in-class tolerance by 3.6·10³–3.7·10⁴×, every other proven bound is equal or worse,
  and only Hardy–Littlewood/PCC *values* (CONJECTURED) would clear it. The new catalog adds the
  *structural* diagnosis (Pool 2): the off-diagonal is a **pretentious twisted two-point correlation**
  (the twist n^{iT} points toward ζ(1+iT)), which is exactly the class of multiplicative-function
  correlations the Matomäki–Radziwiłł/Tao machinery does not control; and the Chowla-ladder calibration
  (Q1-ADD) places the needed input on the first *unproven* rung.
- **(P1) the missing in-class constraint.** [LPd] closed it in-class: the LP optimum
  0.68183123 = p₀ + |E(1)| is attained; nothing inside bandwidth 1 moves the value except the certified
  simple fraction p₁ itself (shadow price 1), which needs beyond-1 data. The additive-combinatorics lens
  therefore says: the missing input *is* arithmetic, and the only candidate sources are the unproven rungs
  of the prime-pseudorandomness ladder (Pools 2, 5, 6).

**New verified fact relevant to the paper's §7.5(f) roadmap (probe_additive_a2.py):** within the
certificate's admissible class (integer multiplicities, λ = 1 operator), the fourth moment is **forced**:
given (m₁, m₂, m₃) = (1, 4/3, 2), min m₄ = max m₄ = **10/3** (LP, HiGHS) — every in-class configuration
has m₄ = 10/3, so (i) the λ = 1 fourth moment carries **no separating power** (all admissible worlds are
m₄-degenerate), and (ii) the paper's moment sequence (1, 4/3, 2, 13/4) is **not jointly realizable** by
any single integer-multiplicity configuration (the m₄ = 13/4 constraint is LP-infeasible; m₄ ≥ 13/4 is
automatic since min m₄ = 10/3 > 13/4). This is a caveat on the per-configuration reading of the
HL*(4,λ) → 13/18 roadmap: those are sine-process *expectations*, not per-configuration in-class moments;
a per-window λ < 1 reading (where the moments differ and RS applies) is the consistent one. The only
*separating* higher-order input is therefore **m₄(λ) at λ < 1/2** (RS range 4λ < 2, unconditional) — the
target of vector G2-ADD.

---

## Pool 1 — Gowers uniformity norms (U^k) and higher-order Fourier analysis

The theory of "pseudorandom vs structured" via Gowers norms: (k+1)-term correlation statistics are
controlled by the U^k norm; inverse theorems (Green–Tao U³; Green–Tao–Ziegler U^{s+1}) say large U^k
⟺ correlation with a (k−1)-step nilsequence; Green–Tao's transference moves such statements from
ℤ/Nℤ to the primes. Mapping: our moments m_k(λ) = tr Â^k/N are k-point correlations of the zero
configuration; the compressed operator's spectrum is the "Fourier side".

### G1-ADD — "The third moment is the wrong rung: a U²-level statistic cannot separate the crystal" — NEW (verified content; the headline)
**Idea:** Gowers' control |Λ₃(f)| ≤ ‖f‖_{U²} says three-point (3-term) statistics are governed by
two-point Fourier information. The 256-crystal matches all bandwidth-1 two-point data (F ≡ 1 on [0,1],
PROVEN [AC]), hence its three-point moment matches GUE — and it does: m₃(crystal) = 2 = m₃(GUE)
(probe_additive_a.py; the multiset {1×2N/3, 2×N/6} gives Σm³/N = 2). The min-N_d LP under
(m₁, m₂, m₃) is exactly 5/6 (crystal feasible and optimal) — the third moment is doubly non-discriminating
(every inequality m₃ = 2 is saturated by the crystal). This *proves* the [CD-V3]/[P6.5] "likely negative"
and explains the [TB] negative structurally.
**Analogy:** Gowers norm ladder ↔ the moment ladder: m₂ is U¹-level (Fourier/form factor), m₃ is U²-level
(3-term), m₄ is U³-level (4-term); U^k pseudorandomness is what (k+1)-term statistics detect.
**Needs:** nothing further (the LP is saved; a one-page writeup converts it into the documented negative).
**Feasibility:** done (verified this session). **Probe:** probe_additive_a.py (already run).

### G2-ADD — "The only separating higher-order input: m₄(λ) at λ < 1/2 via an admissible-quartic construction" — NEW (P2-adjacent; the concrete open target)
**Idea:** The first rung with separating power is the 4th moment — but at λ = 1 it is in-class-degenerate
(m₄ ≡ 10/3 given (1, 4/3, 2), probe_additive_a2.py) and not unconditional (4λ = 4 > 2, HL* needed). At
**λ < 1/2 the 4th moment IS unconditional** (RS range 4λ < 2) and the crystal's λ < 1/2-compressed
moments differ from GUE's (the natural extremal-world proxy gives window-B moments 2.33 and 3.97 vs GUE
13/6 and 5, [TB] §3.4, CHECKED). The mechanism to convert m₄ into an N_d bound is the paper's
admissible-*cubic* (§7.5(g)) generalized to an **admissible quartic** (Schur–Horn with a degree-4 weight
ψ ≤ 1 on integers) — a new step the paper does not have (its quartic content is the §7.5(f) Christoffel
bound, conjectural at λ < 1).
**Analogy:** Gowers inverse U³ ⟺ the "quartic detects 2-step nilsequences" rung; the crystal is the
degree-1 (lattice) structure that the quartic excludes.
**Needs:** (i) m₄(λ) at λ = 1/4, 1/3, 1/2−ε via the corrected 3D determinantal diagram (executioner's
open item #3 in [TB]; note the existing m4_check.py has a wrong '1'-term — the analytic value is I₁ =
∫∫∫K(u)K(v)K(w)K(u+v+w) = 2/3, derived here and Irwin–Hall-verified in probe_b3.py, not 1); (ii) the
admissible-quartic Schur–Horn step for the distinct functional; (iii) the min-N_d quartic LP.
**Feasibility:** Med. **Probe:** compute m₄(λ) at λ = 1/2− via the corrected 3D diagram (tail-subtracted,
fast parts per variable) — a day; compare with GUE targets and with the crystal's λ = 1/2-compressed
moments (TB §3.4 proxy).

### G3-ADD — "Transference/majorant: why the Green–Tao transference cannot be lifted to the zeros" — KNOWN-DEAD-as-input (framing)
**Idea:** Green–Tao's transference requires the majorant (here: the GUE model measure) to be
pseudorandom at the relevant level; the zeros' model is matched only on bandwidth 1 (beyond 1: no
control, [M29]) — the transference hypotheses fail exactly at the wall. Any transference-style
"pseudorandom ⟹ correlations match" statement for the zeros is blocked at the same λ = 1 boundary.
**Analogy:** GT transference on ℤ/Nℤ ↔ zero-configuration mod the GUE model; the majorant's
pseudorandomness at *all* scales is what we provably lack.
**Needs:** none (records why the GT machinery cannot be the mechanism). **Feasibility:** immediate.
**Probe:** none (documentation).

### G4-ADD — "The Gowers hierarchy as a roadmap-pricing tool (each rung's separating power)" — NEW (roadmap)
**Idea:** Price the moment ladder's separating power exactly as Gowers prices correlation rungs:
m₁ (U⁰/mean; PROVEN, rigid), m₂ (U¹/Fourier; PROVEN at λ ≤ 1, but crystal-matching), m₃ (U²; PROVEN at
λ < 2/3, non-separating — G1), m₄ (U³; only at λ < 1/2, separating in principle — G2), all moments
(HL*, conjectural; → 1, paper §7.5(f)). The hierarchy shows P2's "third moment" formulation was never
going to work and that the 4th-moment-at-λ<1/2 route is the *unique* unconditional higher-order input.
**Analogy:** the U^k → (k+1)-AP control is the additive-combinatorics analogue of the paper's moment
ladder 2/3 → ? → 13/18 → 1.
**Needs:** none. **Feasibility:** immediate (documentation). **Probe:** none.

### G5-ADD — "Averaged U^k / the logarithmically averaged variant of the certificate (a.e.-route)" — NEW (overlaps [P9.1])
**Idea:** Tao's logarithmically averaged framework (PROVEN for the two-point Liouville case) works at the
"average over scales" level; the analogous averaging *over T* of the certificate value is
diagonal-dominated (see ES3-ADD) — the natural "averaged" target type. Feasibility of the *margin*
depends on the measured T-variance (probe).
**Analogy:** log-averaging in Tao's Chowla work ↔ T-averaging the certificate.
**Needs:** the T-variance of ‖W‖²/N (same probe as ES3-ADD). **Feasibility:** Low-Med.
**Probe:** fold into ES3-ADD.

---

## Pool 2 — Quasirandomness / Fourier uniformity of the primes

The "phase-cancelled off-diagonal" of [M29] is a quasirandomness question: does Σ_{n≠m} a_n a_m
(n/m)^{2iT}·kernel cancel? The primes-pseudorandomness program (Green–Tao, Matomäki–Radziwiłł, Tao)
is the relevant toolbox.

### Q1-ADD — "The off-diagonal is a pretentious twisted two-point correlation: why cancellation fails" — NEW (structural diagnosis of [M29])
**Idea:** The off-diagonal Σ Λ(n)Λ(m)(n/m)^{iT}-weighted sums are the two-point correlation of Λ twisted
by the character n^{iT} — the *pretentious* direction (toward ζ(1+iT), the point where Λ's Dirichlet
series lives). The MR/Tao machinery controls non-pretentious multiplicative functions and their additive
shifts (log-averaged Chowla, PROVEN); pretentious twists have large mean — and indeed the measured
pair sums sit at the main-term scale (S_pair(δ=1)/D = 0.04–0.41, [M29] CHECKED). The failure is
structural, not a missing technique: the twist is the one case the pseudorandomness theorems explicitly
exclude.
**Analogy:** pretentious vs non-pretentious in multiplicative-function theory ↔ the (n/m)^{iT}-twisted vs
untwisted pair correlation; "pretentious functions have large mean" is the reason the certificate's
beyond-1 input is provably out of reach of the Chowla-style machinery.
**Needs:** none (explains [M29]; closes "is there an MR/Tao-style unconditional two-point at our scales" —
no). **Feasibility:** immediate. **Probe:** none (the [M29] table is the evidence).

### Q2-ADD — "Log-averaged Chowla (Tao, PROVEN) vs the multiplicative-log pair: the gap, and whether a transfer exists" — NEW (KNOWN-OPEN; literature probe)
**Idea:** Tao's log-averaged two-point Chowla Σλ(n)λ(n+h)/n → 0 (PROVEN) is *additive-shift*; our pair
window is *multiplicative-log* (|log n − log m| ≤ δ). A "multiplicative log-averaged two-point"
statement — e.g. Σ_{|log n−log m|≤δ} Λ(n)Λ(m)(n/m)^{iT}·g, log-averaged in T — is not in the held
sources, and the MR technique (short-interval averages in the additive shift) does not obviously adapt to
the log-shift (the n^{iT} twist is pretentious — Q1). Whether *any* published work treats
log-averaged *multiplicative-shift* or *twisted* two-point correlations is the honest first check.
**Analogy:** Chowla ladder ↔ the certificate-input ladder (Q3-ADD).
**Needs:** a targeted literature search. **Feasibility:** Low (probe). **Probe:** <1h search
(arXiv: log-averaged Chowla, multiplicative shift, twisted two-point correlations of Λ; any 2020+ result
would update [M29]'s boundary).

### Q3-ADD — "The Green–Tao nilsequence orthogonality as the 'primes have no structure' engine (Chowla-ladder calibration)" — NEW (roadmap/mechanism)
**Idea:** Calibrate the proven rungs of prime pseudorandomness against the certificate inputs:
1-point nilsequence orthogonality (Green–Tao, PROVEN) ↔ mean density (PROVEN); log-averaged 2-point
Chowla (Tao, PROVEN) ↔ the *log-averaged* two-point structure; 2-point un-averaged (Chowla, CONJECTURED)
↔ form factor beyond 1 ([M29]); 3-point (CONJECTURED) ↔ three-point beyond λ = 2/3 ([TB]). The
certificate needs exactly the first unproven rungs. This is the only known *mechanism* for "why should
the zeros be GUE-like" (the primes' pseudorandomness via the explicit formula) — worth a literature probe
for any partial bridge (e.g., twisted-nilsequence orthogonality).
**Analogy:** the Chowla ladder is the arithmetic shadow of the zero-correlation ladder.
**Needs:** a literature probe (twisted nilsequence orthogonality; character-twisted Chowla). **Feasibility:**
Low (probe); High as a theorem. **Probe:** <1h search.

### Q4-ADD — "F(α) ≥ 0 is the only unconditional beyond-1 content (the SDP majorant boundary)" — KNOWN (recorded boundary)
**Idea:** B24 gives F ≥ 0 everywhere (PROVEN) and the formula only to α = 1; the CGdL20 SDP uses F ≥ 0
outside [−1,1] as a majorant but needs RH for F ≡ 1 on [−1,1] ([CD-V11]). The unconditional F ≥ 0 alone
re-derives ≤ 0.6818 ([LPd]). The quasirandomness input's boundary is exactly here.
**Analogy:** Fourier uniformity (F ≥ 0 is a positive-definiteness statement) is the *one-sided* content;
values are the missing two-sided content.
**Needs:** none. **Feasibility:** immediate. **Probe:** none (documented in [CD-V11]/[LPd]).

### Q5-ADD — "Empirical beyond-1 form factor on real zeros: the quasirandomness measurement" — NEW (diagnostic, overlaps [CD-V6])
**Idea:** Measure F(α) for α ∈ (1, 3] from real zeros (Rust, cached 10⁴-zero data). If it hugs 1, reality
is quasirandom beyond 1 (consistent with HL) — a prior for the roadmap, not a proof; if it deviates, the
conjectural input the roadmap needs is in tension with data (a caution). The *fluctuations* at α > 1 also
calibrate the B24 error term.
**Analogy:** empirical spectral form factor ↔ the RMT plateau check in quantum chaos.
**Needs:** Rust pair-correlation + form-factor code (extends [CD-V6]'s probe). **Feasibility:** Low.
**Probe:** hours (Rust).

---

## Pool 3 — Szemerédi-type structure theorems

Structure vs pseudorandomness dichotomies: Szemerédi regularity, arithmetic removal (Green), and the
fact that dense sets contain structure — the "structured side" of our extremal laws.

### SZ1-ADD — "The ceiling law is the counterexample to naive removal/regularity inside the certificate class" — KNOWN-DEAD-as-input
**Idea:** Removal/regularity says "structure is detectable (at some scale)". The 256-crystal is maximally
structured (a 256-periodic lattice with marks) yet *undetectable* at bandwidth 1 (F ≡ 1 on [0,1],
PROVEN [AC]) — so no removal-type statement reading only bandwidth-1 data can force "typical" (all-simple)
configurations. The ceiling theorem [AC] IS this counterexample; the removal framework adds vocabulary,
not input.
**Analogy:** arithmetic removal (structure ⟹ detectable at all scales) ↔ the certificate's bandwidth-1
blindness to the crystal.
**Needs:** none. **Feasibility:** immediate. **Probe:** none (records the ceiling theorem as the
removal-counterexample).

### SZ2-ADD — "Regularity decomposition of the zero measure: 'structured = nilsequence, and nilsequences are prime-orthogonal'" — NEW (direction; the one structural mechanism with real content)
**Idea:** Green's arithmetic regularity decomposes any function into structured + uniform + small
(PROVEN as a theorem). Apply to the zero-side fluctuation: the structured part, if nontrivial, is a
bounded-complexity nilsequence; Green–Tao's Möbius orthogonality to nilsequences (PROVEN) says the primes
do not correlate with such structure; if the explicit formula *transmits* that orthogonality to the zero
configuration (the zeros are generated by the primes), the structured part of the zeros would vanish —
an honest mechanism for "the zeros are as unstructured as the primes", i.e. the *reason* GUE-ness is
expected. The obstacle is exactly the pretentious twist (Q1): orthogonality is an *averaged* statement,
the explicit formula is pointwise-in-test-function, and the connecting averages carry n^{iT}. Whether
*any* twisted version of Möbius-nilsequence orthogonality is proven is the cheap first question.
**Analogy:** Green–Tao "the Möbius function is strongly orthogonal to nilsequences" ↔ "the zero
configuration is orthogonal to periodic/nilstructure at bandwidth 1".
**Needs:** (i) a literature probe for twisted/pretentious nilsequence orthogonality; (ii) a formulation
of the explicit-formula transmission step. **Feasibility:** Low (probe) → High (theorem).
**Probe:** <1h search (Green–Tao nilsequence orthogonality; Matomäki–Radziwiłł–Tao averages; any twisted
version).

### SZ3-ADD — "Szemerédi's theorem direction is wrong for us (existence of structure, not exclusion)" — KNOWN-DEAD
**Idea:** Szemerédi-type results assert *presence* of structure (APs, patterns) in dense sets; the
certificate needs *exclusion* of the crystal. GUE-random sets contain all finite patterns at the random
density, so pattern-existence results are consistent with everything we believe; they give no constraint
on N_d. Recording to prevent re-derivation.
**Analogy:** density increment (structure in dense sets) is the opposite of the certificate's
decrement-based bookkeeping.
**Needs:** none. **Feasibility:** immediate. **Probe:** none.

### SZ4-ADD — "Removal-lemma constants as a pricing tool for a hypothetical beyond-1 input" — KNOWN (redundant with [CD-V5])
**Idea:** If a beyond-1 input F(α) = 1 (α > 1) were ever proven, the structure-detectability dichotomy
would force N_d → N at a rate; the paper's Rem 1.1 (0.70@1.04, 0.80@1.26, 0.90@1.70) already prices this
([CD-V5]). The removal machinery adds no new constant. 
**Needs:** none. **Feasibility:** immediate. **Probe:** none (folded into [CD-V5]).

### SZ5-ADD — "Two-point rigidity amplification: a beyond-1 input would force the full GUE structure" — NEW (formulation; KNOWN-OPEN as a theorem)
**Idea:** Among determinantal point processes, the two-point function determines the process (a DPP is
determined by its kernel) — so IF a beyond-1 input (F ≡ 1 at all scales) were ever proven, and IF the
zero configuration were known to be a DPP (it is not — no DPP structure is proven), the higher
correlations would follow. Among *general* point processes, the pair correlation does NOT determine the
process (standard counterexamples — reported), so no rigidity amplification is available without a DPP
input. The honest NEW content: a literature probe for "point processes with sine-kernel pair correlation:
are they the sine process?" — any proven rigidity (e.g., under an additional repulsion or integrability
assumption) would *amplify* a two-point input into the three-point input P2 needs, converting the
conjectural beyond-1 datum into the separating R₃ datum at no extra cost.
**Analogy:** rigidity of the sine process (DPP rigidity / determinantal rigidity) ↔ the certificate's
need for R₃ structure beyond the moment.
**Needs:** a literature probe (sine-kernel rigidity for non-DPP point processes; characterizations of the
sine process). **Feasibility:** Low (probe); the amplification is conditional on the conjectural input.
**Probe:** <1h search (sine process characterization; pair-correlation rigidity).

---

## Pool 4 — Selberg sieve / parity problem

What the sieve cannot see: the parity problem (the sieve cannot distinguish even/odd numbers of prime
factors) is the documented structural reason lower/main-term statements about prime pairs resist
unconditional treatment. Our beyond-1 wall is of this type.

### SI1-ADD — "The beyond-1 wall is parity-type: the certificate needs a sieve-invisible value" — KNOWN-DEAD-as-input (calibration of A1/A5)
**Idea:** The needed beyond-1 input is the *value* (HL main-term constant) of the Λ-pair correlation.
The Selberg sieve gives upper bounds of the right order (2δX²-class — the [CD-A5] death) but cannot
produce the value: the correlation's main term is parity-sensitive, exactly what sieve lower-bound
technology provably cannot see. The wall is not a missing technique but a structural limit of the
sieve toolkit, matching [M29]'s conclusion (the sieve row of its §4 table is the quantitative death).
**Analogy:** the parity problem (why the twin-prime conjecture resists the sieve) ↔ the certificate's
need for the pair-correlation value at X ≫ T.
**Needs:** none. **Feasibility:** immediate. **Probe:** none (records A1/A5 + [M29] as the parity wall).

### SI2-ADD — "Bombieri/GM escape routes: what IS proven on average, and where the additive window hits its range limit" — NEW (precise wall location)
**Idea:** The proven content on average over the shift: the first moment of the pair correlation
Σ_{h≤H}Σ_{n≤X}Λ(n)Λ(n+h) (main term computable by PNT-type/divisor counting) and the Goldston–Montgomery
second moment of ψ(x+H)−ψ(x)−H — both PROVEN in the α ≤ 1 regime (they are the engine of [B24]);
the GM variance asymptotic is CONJECTURED in the full range (GM's own conjecture; reported — verify).
The certificate's window (multiplicative log-window at X = T^{1+ε}, additive H ~ X/log T) lies beyond
every proven range (H ≫ X^{1/2}-class) — the precise additive-combinatorics location of the λ = 1 wall
([M29]). The genuinely useful content: the *h-windowed* (additive) reformulation of the pair sum is
provably averaged, the *log-windowed* (multiplicative) one is not — the certificate's window shape is
what pushes it past the proven range.
**Analogy:** Bombieri's asymptotic sieve (averaging over shifts defeats the parity problem for *averages*)
↔ the certificate's need for the non-averaged, windowed value.
**Needs:** a careful writeup of the window-shape distinction (additive vs log window) and the GM range;
a literature check that no theorem evaluates the log-windowed pair sum at X ≫ T (expected: [M29]).
**Feasibility:** Low (documentation + probe). **Probe:** <1h: verify the GM variance's proven range
against [B24]'s usage; confirm the log-window case has no theorem.

### SI3-ADD — "Parity-insensitive statistics: the variance is the only accessible beyond-1 object" — NEW (framing; overlaps ES3-ADD)
**Idea:** Because the pair-correlation *value* is parity-protected, the only sieve-accessible beyond-1
object is the *variance* (parity-insensitive): the GM second moment. The certificate is a mean-type
bound, so a variance input cannot enter the rank-trace directly ([AM] already prices the two-moment
class) — but a *T-averaged* (variance-in-T) statement is the honest realization (ES3-ADD): "the
off-diagonal is diagonal-dominated for most T".
**Analogy:** sieve's variance-type successes (GM, MR) vs its parity-blocked values.
**Needs:** none beyond ES3-ADD. **Feasibility:** Low. **Probe:** fold into ES3-ADD.

### SI4-ADD — "Maier-type irregularities: a caution, not an obstruction" — NEW (diagnostic)
**Idea:** Maier's theorem (proven irregularities of the primes in very short intervals of length
(log x)^A) operates at scales far below our window (H ~ X/log T ≫ (log X)^A) — no obstruction at our
scale, but a standing warning that "primes are smooth in short windows" is false at very small scales,
so any certificate assumption of prime-smoothness must be checked at its own scale (it is not smooth at
ours either — that is [M29]).
**Analogy:** Maier's matrix method ↔ a caution on Cramér-model assumptions.
**Needs:** none. **Feasibility:** immediate. **Probe:** none (documentation).

### SI5-ADD — "Level of distribution / Bombieri–Vinogradov: the sieve's proven input is averaged, the certificate's is not" — KNOWN-DEAD-as-input (calibration of SI2)
**Idea:** The sieve's strongest proven inputs (Bombieri–Vinogradov, the level-of-distribution bounds that
power GPY) are *averages over moduli/levels*; the certificate's beyond-1 need is a *per-window value*.
The gap between proven averages and needed pointwise/windowed values is the same averaging obstruction
as SI2 — the sieve literature's entire toolkit (higher-order Λ₂ weights, BV-type level bounds, Selberg
sieves) converts averages into almost-prime statements, never into prime-pair *values* at fixed windows;
the parity wall is exactly this. Recording to close the "higher-order sieve weights" avenue.
**Analogy:** BV/level-of-distribution (average over q) ↔ the certificate's per-T-window form-factor value.
**Needs:** none. **Feasibility:** immediate. **Probe:** none (documentation; A1/A5 + [M29] + SI2).

---

## Pool 5 — Moments of L-functions / shifted moments

The shifted-moment literature (Conrey–Gonek, Chandee, CFKRS, Harper–Soundararajan, Motohashi) is the
arithmetic source of higher-moment main terms — the arithmetic shadows of the zero correlations.

### LM1-ADD — "The 6th moment of ζ as an unconditional 3-fold additive-correlation input (recent progress)" — NEW (literature-verification; potentially the biggest prize)
**Idea:** The shifted-moment ladder: 2nd moment of |ζ(1/2+it)| (PROVEN, classical), 4th (PROVEN, Ingham
1926; exact spectral form, Motohashi), 6th (CFKRS CONJECTURED; a recent asymptotic is reported —
Heap–Lindqvist 2024, "The sixth moment of the Riemann zeta function" — **verify before use; source not
in our library**). A proven 6th-moment asymptotic = a proven 3-fold additive-correlation main term, the
arithmetic shadow of the three-point zero correlation *beyond* RS's λ < 2/3. Honest caveat: it is a
t-averaged statement, and the certificate needs per-window inputs (the same averaging obstruction as
[P9.1]); but the *off-diagonal estimate inside the proof* may be a new unconditional additive-correlation
bound usable at our window scale.
**Analogy:** the k-th moment of |ζ|² ↔ the k-fold divisor/additive correlations ↔ the k-point zero
correlations (through the explicit formula); CFKRS is the conjectural completion of the ladder whose
bottom rungs are proven.
**Needs:** (i) obtain and read the Heap–Lindqvist paper (or confirm/deny the theorem's existence and
range); (ii) extract any unconditional additive-correlation estimate at our scales (|h| ~ X/log T at
X = T^{1+ε}). **Feasibility:** Low (probe) → Med. **Probe:** <1h arXiv check + abstract/section read.

### LM2-ADD — "Motohashi's exact 4th-moment formula: the only exact identity to mine for a beyond-1 channel" — NEW (KNOWN-OPEN as transfer)
**Idea:** Motohashi's formula gives ∫|ζ(1/2+it)|⁴ w(t)dt as an *exact* spectral expression (Maass-form
side + Kloosterman sums), i.e. the additive divisor correlation is exactly expressible — the only exact
identity of this type. Its direct transfer to the zeros' two-point form factor beyond 1 runs through a
different explicit-formula channel (divisor vs Λ correlations), so no direct input is known; but the
*technique* (spectral decomposition of the off-diagonal) is the only route to *exact* beyond-1-type
statements, and a targeted probe ("Motohashi + pair correlation beyond 1", "spectral methods for F(α)")
is cheap.
**Analogy:** the Kuznetsov/Motohashi spectral decomposition is the exact version of what quasirandomness
heuristics approximate for the off-diagonal.
**Needs:** a literature probe; a formulation of any exact identity whose prime side matches the
certificate's Λ-pair window. **Feasibility:** Low (probe). **Probe:** <1h search (Motohashi formula
extensions; spectral evaluations of Montgomery's F(α) beyond α = 1).

### LM3-ADD — "Short-shift moments: the off-diagonal lives exactly where nothing is proven" — KNOWN-OPEN (calibration)
**Idea:** The certificate's per-window need corresponds to shifted moments at shifts ~ 1/log T (the
short-shift regime where the off-diagonal matters). Unconditional state: 2nd shifted moment classical;
4th shifted at short shifts only bounds of the right order (Soundararajan-type, PROVEN — upper bounds,
not asymptotics); 3rd (6th) at short shifts CONJECTURED. The paper's §7.5(g) 0.85082 (RH, window-dependent
moments) is the conditional ceiling of this route.
**Analogy:** short-shift moments ↔ the zeros' window scale (shifts 1/log T are the pair-correlation
scale).
**Needs:** none (calibration). **Feasibility:** immediate. **Probe:** none.

### LM4-ADD — "Mollified/amplified second moments: the F(α)-extraction technique — re-check that [M29]'s boundary still holds" — NEW (literature re-check)
**Idea:** The standard technique for pair-correlation data beyond α = 1 is the second moment of ζ with a
mollifier/amplifier; the sharpest unconditional form is [B24] (stops at α = 1) and the conditional forms
(CGdL20 0.6792 under RH) need RH ([CD-V11]). A 2023+ probe for "unconditional amplified second moment
α > 1" is the honest check that [M29]'s boundary has not moved.
**Analogy:** amplification in the second-moment method ↔ the certificate's need for F(α) values, α > 1.
**Needs:** a literature probe. **Feasibility:** Low. **Probe:** <1h arXiv search (amplified/mollified
second moment of ζ; form factor beyond α = 1, 2023–2026).

### LM5-ADD — "The moment-ladder calibration table" — NEW (documentation)
**Idea:** Map the ζ-moment ladder (2nd/4th/6th ↔ PROVEN/PROVEN/open-recent) and the shifted-moment
sub-ladder (short-shift 2nd/4th/6th ↔ PROVEN/bounds-only/CONJECTURED) onto the certificate inputs
(mean density / form factor ≤ 1 / three-point beyond λ = 2/3). The table is the roadmap: each
certificate input is a specific rung, and the first unproven rung needed is the short-shift 4th or the
6th at our window scale.
**Analogy:** CFKRS's moment conjecture is the "all-rungs" statement; the certificate needs single rungs.
**Needs:** none. **Feasibility:** immediate. **Probe:** none.

---

## Pool 6 — Exponential sums / Vinogradov

Mean values of exponential sums over primes (Vinogradov, the large sieve, Weyl sums) and the
Matomäki–Radziwiłł short-interval results. The λ = 1.04 sum of [M29] is the concrete object.

### ES1-ADD — "Logarithmic phases have no cancellation: Vinogradov is structurally inapplicable" — KNOWN-DEAD-as-input (framing of [M29])
**Idea:** The phase n^{iT} is slowly varying (|d/dn·n^{iT}| ~ T/n ~ 1 at n ~ T) — a *logarithmic* phase,
not a polynomial phase e(αn^k). The entire Vinogradov/Weyl mean-value machinery is built for polynomial
phases; for logarithmic phases the mean value of Σ a_n n^{iT} is at the diagonal scale (a geometric-type
sum). This is *why* the diagonal dominates at λ ≤ 1 and why no exponential-sum mean-value theorem exists
at our scales — the Vinogradov row of [M29] §4 is the quantitative death.
**Analogy:** Weyl sums (polynomial phase, cancellation) vs n^{iT}-sums (logarithmic phase, no
cancellation) — the difference is the derivative scale.
**Needs:** none. **Feasibility:** immediate. **Probe:** none.

### ES2-ADD — "Montgomery's mean-square = the large sieve over the height variable (the proven quasirandomness content)" — KNOWN (framing)
**Idea:** The T-averaged second moment of the off-diagonal IS the diagonal (PROVEN — Montgomery's
mean-square; the source of F ≥ 0 and the α ≤ 1 formula in [B24]). This is a large-sieve inequality in
disguise: the certificate's inputs are exactly the large-sieve-optimal content of the prime
correlations, and the large sieve over T gives nothing beyond α = 1 (the off-diagonal's T-average is the
diagonal only while the near-diagonal dominates).
**Analogy:** large sieve (average over characters) ↔ Montgomery's mean-square (average over T).
**Needs:** none. **Feasibility:** immediate. **Probe:** none.

### ES3-ADD — "The almost-everywhere certificate: a new target type (off-diagonal ≪ diagonal for most T)" — NEW (target type; overlaps [P9.1]/[P9.2])
**Idea:** Since the T-variance of the off-diagonal is diagonal-dominated (Montgomery-type second moment,
PROVEN at α ≤ 1), Chebyshev gives: for most T in a dyadic range, the off-diagonal is ≤ (1+ε)·(diagonal
· √(variance/diagonal²)) — i.e. the certificate value is ≥ 0.6725 − margin(T) for all T outside a
quantifiable exceptional set. The honest catch: the *margin* is set by the measured variance — [M29]'s
S_pair/D ~ 0.04–0.41 suggests the a.e. margin is of order 0.1–0.4, likely vacuous at the constant level
(0.6725 vs 0.6818 is 1.4%) — but the *target type* (measure-theoretic 67.25%, "for all T outside a set
of density zero") is new, the variance is computable, and even a weaker-but-genuine "≥ 2/3 a.e."
statement would be a new theorem.
**Analogy:** a.s./Borel–Cantelli certificates in analytic number theory ↔ per-T certificate validity for
most T.
**Needs:** (i) the T-variance of ‖W‖²/N (measure, from the [AF]/[CD-V1] machinery); (ii) a second-moment
bound over T-windows; (iii) the a.e. statement. **Feasibility:** Med (probe cheap).
**Probe:** Rust: compute var(‖W‖²/N) over adjacent T-windows at fixed scale — hours; compare with the
diagonal prediction (P9.1's probe).

### ES4-ADD — "The λ = 2/3 boundary: the third moment's off-diagonal reaches the main-term scale exactly there" — KNOWN-OPEN (precision location, from [TB])
**Idea:** The RS third-moment evaluation at λ < 2/3 is the statement that the 3-fold off-diagonal prime
sums are diagonal-dominated; at λ = 2/3 (boundary) the combination 2m₂ − m₃ = 7/36 > 0 enters — the
cubic construction's best *unconditional* value is 0.8071 < 5/6 ([TB], PROVEN). The exponential-sum
structure at the boundary is the concrete obstruction: the λ = 2/3 three-fold prime sums are the
"Vinogradov-type" question reduced to its actual form (log-phase, pretentious twist — Q1/ES1), and any
improvement there is new input.
**Analogy:** the RS boundary kλ = 2 is where the diagonal-method's off-diagonal stops being negligible —
the additive-combinatorics "diagonal wins" threshold.
**Needs:** none (locates the wall; the twobandwidth negative is the evidence). **Feasibility:** immediate.
**Probe:** none.

---

### ES5-ADD — "Direct diagnostics of the twisted pair sum P(T): distribution, variance, sign-change structure" — NEW (raw-data diagnostic; TESTED-OPEN)
**Idea:** [M29]'s phase-cancelled proxy |P(T)| ≈ 0.26–1.43×budget oscillates and grows with ε; a direct
numerical study of P(T) over adjacent T-windows (its mean, variance, sign-change rate, and whether its
T-average is diagonal-dominated) is the fundamental measurement behind both the a.e.-certificate
(ES3-ADD) and the quasirandomness question (Q1-ADD): it measures whether the off-diagonal has any
*systematic* cancellation (which would be unprovable HL content) or is a genuine fluctuation about a
nonzero mean (parity/prententious-type — expected).
**Analogy:** fluctuation diagnostics of oscillatory sums ↔ separating "true cancellation" from
"fluctuation about a mean" in the [M29] data.
**Needs:** the /tmp/prime-pairs Rust machinery ([M29]) extended to a T-sweep. **Feasibility:** Low
(compute). **Probe:** Rust: P(T) over ~10² T-windows at T = 10⁴–10⁵, λ = 1.04; report mean, std,
sign-change rate — hours.


## TOP 10 (EV × feasibility × cheap-probe)

1. **LM1-ADD — 6th-moment literature verification (Heap–Lindqvist 2024, verify).** A proven 6th-moment
   asymptotic would be the first unconditional 3-fold additive-correlation main term — the single biggest
   possible new input for the three-point route. Probe: <1h (arXiv check).
2. **LM4-ADD — amplified-second-moment re-check (2023+).** Re-verifies that [M29]'s α = 1 boundary
   hasn't moved; if it has, the P3 picture changes. Probe: <1h.
3. **Q2-ADD — log-averaged/multiplicative-log transfer check.** Determines whether any Tao/MR-style
   theorem reaches the certificate's window structure. Probe: <1h.
4. **G2-ADD — m₄(λ) at λ < 1/2 via the corrected 3D diagram** (executioner's open item #3 in [TB]).
   The unique unconditional higher-order input with separating power; the corrected '1'-term I₁ = 2/3
   (verified here) fixes the existing script's bug. Probe: a day.
5. **SZ2-ADD / Q3-ADD — twisted nilsequence orthogonality probe.** The only mechanism candidate for
   "primes ⟹ zeros pseudorandom"; a literature probe for any twisted/pretentious version. Probe: <1h.
6. **ES3-ADD — a.e.-certificate T-variance probe.** Measures whether the almost-everywhere 67.25% has a
   positive margin; a genuinely new target type even if the margin is small. Probe: hours (Rust).
7. **Q5-ADD — empirical beyond-1 form factor on real zeros.** The quasirandomness measurement; changes
   what we believe about the roadmap's conjectural input. Probe: hours (Rust).
8. **SI2-ADD — GM-range and window-shape precision writeup.** Pins the additive-vs-log window distinction
   as the reason the proven-average content doesn't reach the certificate; documentation + one check.
   Probe: <1h.
9. **LM2-ADD — Motohashi/spectral probe for a beyond-1 channel.** The only exact-identity route; cheap
   literature probe. Probe: <1h.
10. **G4-ADD — Gowers-ladder pricing table.** Documentation; frames why the third moment was doomed and
    where the unique separating rung sits. Probe: none (writeup).

**Strategic reading:** G1-ADD (the third-moment negative, verified here) and [TB] together close the P2
"third moment" formulation completely and explain it structurally; the only *unconditional* higher-order
avenue left is m₄ at λ < 1/2 (G2-ADD, fed by the open m₄(λ) evaluation). The P3 avenue is closed by [M29]
except for (a) literature-currency re-checks (LM1, LM4, Q2) and (b) the new *target type* (ES3, a.e.-in-T).
The P1 in-class question is closed by [LPd]; the additive toolbox's role is to identify which *arithmetic*
input could raise p₁ — and every candidate (6th moment, amplified second moment, twisted Chowla,
nilsequence orthogonality) sits on an unproven rung, honestly labeled.

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

### W-ADD1 — "Prove the transference: the zeros are U^k-pseudorandom because the primes are" — CONJECTURED (direction; no known technique)
**For:** the explicit formula makes the zeros a functional of the primes; Green–Tao-style transference
is the only known mechanism for "pseudorandom inputs ⟹ pseudorandom outputs"; a character-twisted
transference would be a *proof structure* for "why GUE".
**Against:** the twist n^{iT} (pretentious, Q1) is exactly the case the transference theorems exclude;
the output (zero correlations) is a *spectral* object with no known averaging identity at our scales;
every known attempt reduces to re-deriving the explicit formula.
**Honest verdict:** the mechanism sketch is right but the tool does not exist; the only fundable fragment
is SZ2-ADD/Q3-ADD's literature probe for twisted orthogonality.

### W-ADD2 — "RH ⟺ the structured part of the zero measure vanishes (a regularity-lemma formulation)" — CONJECTURED (equivalent-formulation risk)
**For:** the regularity decomposition is a proven dichotomy; if the structured part vanished, the
bandwidth-1 pseudorandomness would extend to all scales and the crystal would be excluded.
**Against:** the vanishing of the structured part is exactly RH-strength (the crystal is only excluded at
all scales by the full pair-correlation conjecture); the "finite shadow" (W_T's spectrum vs the
crystal's) is measurable but cannot enter a per-T certificate ([CD-V1]/P4.3 probes are the honest
diagnostics).
**Honest verdict:** reformulation, no free lunch ([CD-W4]'s lesson); keep only the diagnostics.

### W-ADD3 — "Logarithmically averaged certificate: a Tao-style log-average over T might be provable where pointwise fails" — CONJECTURED (target type; the content is ES3-ADD)
**For:** log-averaging defeats slow drifts in every known application (Tao's Chowla); the T-average of
the off-diagonal is diagonal-dominated (ES2), so a log-averaged-in-T certificate has a provable mean.
**Against:** the certificate value is a *liminf* object — the exceptional set of T where it dips matters
and the log-average doesn't control it; the margin (measured variance, [M29]-scale) is likely too small
to lift above 2/3.
**Honest verdict:** the a.e. statement (ES3-ADD) is the honest realization; worth one variance probe.

### W-ADD4 — "Build the certificate on the parity-insensitive variance (GM) instead of the mean" — CONJECTURED (likely-false as input)
**For:** the variance is the one sieve-accessible beyond-1 object; a variance-based certificate might
dodge the parity wall.
**Against:** the rank–trace method is a mean-type inequality — variance inputs don't enter it ([AM]
prices the two-moment class; `lemmaR_tight` is tight); the variance enters only through the T-averaging
(ES3-ADD), not as a per-T constraint.
**Honest verdict:** closed; the variance is a T-averaging tool, not a certificate input.

---

## Label inventory

- **NEW** (invented here, untested or verified-this-session): G1-ADD (verified: the third-moment negative
  + Gowers-rung explanation), G2-ADD (m₄ at λ < 1/2 route), G4-ADD, G5-ADD, Q1-ADD (pretentious-twist
  diagnosis of [M29]), Q2-ADD, Q3-ADD, Q5-ADD, SZ2-ADD, SZ5-ADD (two-point rigidity amplification),
  SI2-ADD, SI3-ADD, SI4-ADD, SI5-ADD (level-of-distribution calibration), LM1-ADD, LM2-ADD, LM4-ADD,
  LM5-ADD, ES3-ADD (a.e.-certificate), ES5-ADD (twisted-sum diagnostics), W-ADD1…W-ADD4 (conjectured
  by construction).
- **KNOWN-DEAD** (killed earlier; re-confirmed/reframed here): G3-ADD (transference fails at the wall),
  SZ1-ADD (the ceiling law is the removal-counterexample), SZ3-ADD (wrong direction), SI1-ADD (parity
  wall; A1/A5 + [M29]), SI5-ADD (level-of-distribution averaging gap), ES1-ADD (logarithmic phases;
  [M29]), ES2-ADD (large-sieve boundary; known).
- **KNOWN-OPEN** (core is open; new framing only): Q2-ADD (multiplicative-log transfer — literature
  probe), LM3-ADD (short-shift moments), ES4-ADD (λ = 2/3 boundary), LM2-ADD (Motohashi transfer),
  SZ5-ADD's rigidity question (no known sine-process characterization among general point processes),
  G2-ADD's m₄(λ < 1/2) evaluation (executioner's open item).
- **TESTED-OPEN**: ES5-ADD's P(T) diagnostics (measurement pending, [M29] data exists).
- **TESTED-OPEN**: G1-ADD's LP and crystal moments (CHECKED NUMERICALLY, probes a/a2), m₃ values
  (re-verified first-hand, probe b6: 5.004, 3.252, 2.001 converging to 5, 13/4, 2), the m₄-degeneracy
  (probe a2), I₁ = 2/3 (probe b3, Irwin–Hall-verified).
- **Facts cited from the program's verified notes (not re-derived here):** the 5/6 wall and
  `lemmaR_tight` [AM]; the ceiling 0.68183123 [LPd]; m₃(1/2)=5, m₃(2/3)=13/4, m₃(1)=2 [TB] (corroborated
  first-hand in probe b6); the beyond-1 negative [M29]; F ≡ 1 on [0,1] for the 256-law [AC].
- **Reported — verify before use:** the 6th-moment asymptotic (Heap–Lindqvist 2024, LM1); the GM
  variance's full-range status (GM's conjecture, SI2).

## Honesty footer

- Probes: `research/notes/probes-additive/{probe_additive_a,a2,b3,b5,b6}.py`, all run with
  `uv run --quiet --with numpy --with scipy python`; outputs recorded in this file. The finite-GUE
  empirical route (probe_b3.py) was infeasible at scale in this environment (unoptimized BLAS: 26 s for a
  300×300 complex eigvalsh) and its small-sample ballpark carried finite corrections too large to
  discriminate m₄(1) = 13/4 from the buggy 4.5 — so m₄(1) = 13/4 remains UNVERIFIED by our tools
  (executioner's open item #3 in [TB]), and the corrected 3D-diagram computation is flagged as the next
  probe (G2-ADD).
- No claim in this file is a new theorem; the deliverable is a mined catalog with verified negatives,
  honest labels, and ranked probes. The persistent walls — beyond-1 two-point data, higher-order
  correlations with separating power, and any structural input excluding the crystal — are now
  *explained* by the additive-combinatorics toolbox (Gowers rungs, pretentious twists, parity) rather
  than merely asserted.
