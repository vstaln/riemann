# Idea Generator: control theory & dynamical systems attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (control-theory angle). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Control facts (Routh–
Hurwitz, Ostrowski–Schneider, KYP, Glover/Enns, μ-analysis, Carathéodory–Fejér) are standard textbook
material named at that level; anything I cannot verify from the sources we hold is labeled "reported
standard — verify before heavy use". Every *idea* is CONJECTURED by construction and carries a kill
criterion. Labels: **NEW** (invented here) / **KNOWN-DEAD** (killed here or in cited notes) /
**KNOWN-OPEN** (core is open, or already flagged; cite) / **TESTED-OPEN** (numerically tested, still open).
Overlap discipline: crossdomain = [CD-V#]/[CD-W#]/[CD-A#]; physics = [P#.#]/[W-P#]; attack notes =
[AK]=attack-kernel, [AC]=attack-ceiling, [AM]=attack-multiplicity, [AF]=attack-finitet,
[AL]=attack-lpdual, [QS]=attack-qi-sweep, [PF]=paper-finder-001.

---

## 0. The funnel: what control theory can and cannot add (read this first)

**The two negatives the control angle must respect (both verified):**
1. **No matrix inequality beats Lemma 3.2 on the certificate's data budget D = (tr, ‖·‖²_F, block
   structure, trP₁ ≤ s₁, n₊(Q) ≤ b)** — the QI sweep [QS] proved the strongest candidate (Q₊-side
   Cauchy–Schwarz) provably dominates term-by-term yet its gain `(trQ₊−2b)²/b` vanishes at the sharp
   configurations (`lemmaR_tight` / Prop 4.4(b), PROVEN). `r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F` (Lemma 3.2,
   c=2) is not improvable within D.
2. **No missing constraint exists inside bandwidth one** — the LP dual [AL] attains the Lean ceiling
   v\* = p₀ + |E(1)| = 0.68183123; the only datum that moves v is the certified simple fraction p₁
   (shadow price exactly 1), which needs beyond-bandwidth-1 pair correlation or a multiplicity bound
   (both CONJECTURED / unavailable [AC]).

**Consequence (constraint-hardness reading).** The walls "Lemma 3.2 tight on D" and "in-class ceiling
0.6818" are HARD within their input classes. Therefore every control vector must either (a) add **data
outside D** (entrywise/sign structure, certified zero counts, higher moments — the only things that can
move anything), or (b) be a diagnostic/roadmap that changes what we believe (the method's real slack, the
finite-T error structure, the price of conjectural inputs). Control theory's genuinely outside-the-budget
assets, in order of promise:
- **(i) the argument principle / Nyquist counting**: counts zeros from *boundary data* (ξ values on a
  contour = primes + Γ, zero-free) — the direct, provable route to the shadow-price-1 datum p₁;
- **(ii) Toeplitz / Carathéodory–Fejér real-rootedness** (CvS 2025, a held full-text-verified source
  [PF #61], the closest published relative of our method): a proven *finite* mechanism producing
  real-rootedness certificates;
- **(iii) realization theory (Ho–Kalman, McMillan degree)**: canonical rank tests on the moment Hankels —
  the operational form of the third-moment (P2) question;
- **(iv) μ-analysis / D-scaling / stability radius**: identifies the certificate as a robust-margin bound
  and the 256-law as the worst-case real perturbation — confirms [AL] from a second direction;
- **(v) the moment/Christoffel cascade (Routh array, Jensen polynomials)**: the algorithmic form of the
  paper's own Remark (d) — targets P2 at λ < 2/3.

**Control-family check on negative #1.** The control inequality family (Glover/Enns 2Σσ, Perron–
Frobenius/max-row-sum, Ostrowski–Schneider inertia transfer, D-scaled norms) all reduce to functions of
(tr, ‖·‖²_F, rank, n₊) — the same budget D — hence all are bounded by the same tight example; expected
no gain, but the sweep is cheap and closes the class-level question from the control direction (C-MU2).
Entrywise/Perron bounds on W_T's *entries* are NOT valid certificate inputs: the entries carry zero
positions (zero-side data), so any entrywise bound is either window-only (contracts to Cauchy–Schwarz in
the asymptotic normalization, C-BT4/KNOWN-DEAD) or uses zero data (diagnostic only, [P10.4]).

---

## 0.5 Probe run this round (code-backed; mandatory protocol)

**What was probed:** the top "data outside D" candidate, C-LY3's kernel real-rootedness + CF-condition
check, plus the C-PF explicit-numerator verification.

**Code:** `tools/control_probe_kernel.py` (mpmath dps=40 + numpy); **output:**
`tools/control_probe_kernel_out.txt`.
**Command:** `uv run --quiet --with mpmath --with numpy python tools/control_probe_kernel.py`
(Part B rerun appended; the closed-form numerator check appended separately).

**Findings (all CHECKED NUMERICALLY, labels in §Label inventory):**
1. **Φ and Ψ are numerically real-rooted** on [−40,40]×[−20,20]: argument-principle winding 12 (Φ) and
   78 (Ψ), all located roots real, max |Im| = 1.5e-56 (Φ) / 2.0e-55 (Ψ), |f| < 1e-42 at the roots.
   Φ roots: ±7.042241, ±12.950871, ±19.106031, ±25.325100, ±31.569809, ±37.827344 (next ≈ ±44.09).
   Φ(0) = 0.8492279993183042 = ∫ψ²; Ψ(0) = 0.918725; removable-pole value of Ψ = 0.8492… ✓.
2. **Explicit closed form (verified to < 1e-18):** Φ(x) = (1/2)·N(x/2)/((x/2)((x/2)²−2)) with
   N(u) = [(1+cos√2)u²−2]·sin u − √2·sin√2·u·cos u — real-rootedness of Φ ⟺ real-rootedness of this
   explicit sin/cos combination (a Laguerre–Pólya-class statement).
3. **CF mechanism on the finite Toeplitz T[j,k]=Φ(j−k) does NOT fire:** T is PSD (min eig 4.7e-17 …
   −3.2e-16, consistent with the nonnegative symbol cos²(√2u)), but the ground-state eigenvector
   polynomial is NOT real-rooted: max |Im(roots)| = 0.467, 0.838, 1.105 at d = 12, 24, 48 — the CF
   lemma's rank-(n−1) hypothesis is not met and its conclusion fails numerically. The CvS 2025 mechanism
   does not transfer to the finite lattice compression (documented negative).

**Effect on the catalog:** C-LY3 re-labeled TESTED-OPEN (Part A positive, Part B negative); new vector
C-PF (Pool 3) records the Hadamard/Perron–Frobenius structure and the explicit quadratic cross-term
contraction |⟨v_ρ,v_ρ′⟩| ≤ Φ(0)(1−s²/α₁²) — the explicit-constant form of the [P1.4] repulsion input.
Open steps: larger-box real-rootedness check, and the Laguerre–Pólya proof attempt for N(u).

---

## Pool 1 — Routh–Hurwitz stability / root-location

### C-RH1. The Routh array as the operational algorithm for the sharp k-moment certificate — NEW (P2, overlaps [CD-V3]/[P3.4])
**Idea:** The paper's Remark (d) says Lemma 3.3 is the m=1 case of the one-sided Chebyshev–Markov–
Stieltjes bound: with moments up to order 2m, the sharp lower bound for n₊/d is 1 − Λ_m(0) (Λ_m the
Christoffel function). Control theory's Routh–Hurwitz array is the *same* cascade in its classical
operational form: for a real polynomial, "all roots in the half-plane ⟺ positivity of n nested Hurwitz
minors ⟺ positivity of the n continued-fraction (Stieltjes) coefficients of the even/odd ratio" — and the
CF coefficients ARE computable from the moments in O(n²) (the classical Sylvester–Frobenius / Routh
algorithm). The certificate class "best n₊-lower-bound from the first k moments" is *exactly* the
Routh/CMS cascade; the array is a *decision procedure*, not an LP.
**Analogy:** Routh–Hurwitz cascade (polynomial stability from coefficient moments) ↔ CMS/Christoffel
cascade (n₊-count from matrix moments); each minor/CF coefficient = one "row" of the certificate.
**Needs:** (i) the exact statement of the k-moment certificate for the *distinct* (c=3) functional (the
paper's own §7.5(d) "Christoffel bound 1−Λ_m(0)" is the mollifier-side shadow; the matrix-side object is
the n₊(W)-type count); (ii) the available moments at λ < 2/3 (tr, ‖·‖², tr Â³ — unconditional in the
Rudnick–Sarnak range kλ < 2, [CD-V3]); (iii) the Routh-array evaluation of the CF coefficients.
**Feasibility:** Med. Value: a third formulation of P2 (after the LP [P6.5] and the Christoffel test
[P3.4]) with an *algorithm* instead of an LP — and the Routh picture makes the *monotonicity in moment
order* explicit (2 moments → 2/3, 4 moments → 13/18 under HL*(4), [AM]).
**Cheapest probe (<1h):** mpmath: from (m₁,m₂,m₃) = (1, 4/3, 2) build the 3×3 Hankel, run the Routh/
Stieltjes CF algorithm, and check the *distinct* functional's value — identical numbers to [P3.4]'s probe,
but the algorithm (not the LP) is the deliverable; confirms the cascade is the operational route.

### C-RH2. The Jensen-polynomial cascade as the *entire-function* Routh–Hurwitz; degree-2 discriminant is prime-computable — NEW (diagnostic + P2 dictionary)
**Idea:** The correct entire-function analog of the Routh–Hurwitz cascade is the Jensen-polynomial
criterion: RH ⟺ the Jensen polynomials J_{d,n}(ξ) are hyperbolic (all roots real) for every degree d and
shift n (Ki–Kim–Kim–Markham; GORT give *effective* degree-2 hyperbolicity; source: arXiv:1910.01227,
listed VERIFIED-BY-FETCH in [PF #57]). Degree-2 hyperbolicity is a *discriminant ≥ 0* condition in the
Taylor data ξ(t₀), ξ′(t₀), ξ″(t₀) — and ξ and its derivatives at a point are *prime-side computable* (the
explicit formula for ξ′/ξ, the derivative tower [CD-V9]). So the *local* degree-2 Jensen discriminant is a
new, zero-free RH-ometer (analogous role to W_T's inertia in [CD-V1], different object), and the
*dictionary* degree-d Jensen ↔ moment order 2d identifies P2's third-moment input with *degree-3* Jensen
hyperbolicity (an unconditional fragment at λ < 2/3? — the RS range gives 3 moments).
**Analogy:** Routh–Hurwitz minors ↔ Jensen discriminants; hyperbolicity cascade ↔ the CMS moment cascade;
KKKM's "RH ⟺ all Jensen hyperbolic" is the exact infinite analog of "stability ⟺ all Hurwitz minors
positive".
**Needs:** (i) verify the KKKM/GORT statements from 1910.01227 (held as a fetch record only — label
"reported standard — verify before heavy use"); (ii) the explicit formula for ξ′/ξ, ξ″/ξ (mechanical,
[CD-V9] machinery); (iii) the discriminant computation along the line.
**Feasibility:** Low (probe) — Med. Value: (a) a *new* prime-side diagnostic with different error
structure than W_T's moments; (b) a formal dictionary that sharpens P2.
**Cheapest probe (<1h):** Rust/mpmath: from the explicit formula, compute ξ,ξ′,ξ″ at ~10⁴ grid points at
height 10³–10⁴, print the degree-2 Jensen discriminant margin; compare with the W_T-inertia margin from
[CD-V1]/[AF]. Kill: if the discriminant margin is structurally uninformative (always ≫ 0), the diagnostic
is weaker than the W_T one — record.

### C-RH3. Hermite–Biehler interlacing + Rolle for the derivative tower — KNOWN-OPEN (overlaps [CD-A4], [P3.5]; the naive Rolle dead-end is documented)
**Idea:** The real-rootedness of ξ ⟺ Hermite–Biehler interlacing of the even/odd parts; the derivative
tower ξ^(j) has interlacing zeros (Rolle). [CD-A4] killed the *naive* joint (ξ, ξ′) interlacing LP (no
usable upper constraint — a derivative can have arbitrarily more real zeros than the function). The
control restatement does not resurrect it: the "root-locus of the derivative" (as the derivative order j
varies) is a *roadmap*, not a constraint. The only NEW fragment worth keeping: Hermite–Biehler interlacing
is *sign-alternation structure* — the same *kind* of input as C-LY3's sign structure below; probe them
together.
**Analogy:** Hermite–Biehler (interlacing ⟺ real roots) ↔ Nyquist/encirclement (boundary sign changes ⟺
interior roots) — both are "counting via alternation".
**Needs:** nothing new (documentation + fold into C-LY3's probe).
**Feasibility:** Low. Value: prevents re-funding [CD-A4]'s dead interlacing route.
**Cheapest probe:** none (already documented dead in [CD-A4]).

### C-RH4. The partial cascade is strictly weaker: 2 moments can't reach the 4-moment constant — KNOWN-OPEN (documentation, P1/P2 support)
**Idea:** Routh–Hurwitz's cascade is *monotone in the polynomial degree*, not in the constant: checking
more minors certifies the *same* stability. The matrix-side cascade (Lemma 3.3 → CMS, paper Remark (d))
is monotone in the *moment order*: each extra moment pair strictly improves Λ_m(0) (1−Λ₁(0)=2/3 →
1−Λ₂(0)=13/18 under HL*(4,·), [AM]). This is the control-theoretic explanation of why *no* two-moment
certificate can reach 0.6818 (the in-class ceiling [AL] is a *configuration-side* obstruction; the
moment-order wall is *data-side*) — two different reasons the same gap is closed.
**Analogy:** cascade monotonicity in the data order ↔ the moment hierarchy of the certificate (P9.4's
"next order" framing, physics side).
**Needs:** none (documentation; the numbers are [AM]/[AL]-verified).
**Feasibility:** immediate. Value: strategic clarity — funds the *third-moment* route (P2), not a
better two-moment certificate.
**Cheapest probe:** none.

### C-RH5. Schur–Cohn / unit-disk criterion — KNOWN-DEAD
**Idea:** The Schur–Cohn test (roots inside the unit disk from coefficient moments) would be the disk
analog of Routh–Hurwitz.
**Death:** the functional equation pairs ρ ↔ 1−ρ̄ (reflection in the line Re s = 1/2), not the unit circle;
there is no natural disk structure on the zero set to certify. Dead at the framing stage.
**Cheapest probe:** none (recorded).

---

## Pool 2 — Lyapunov theory & inertia theorems

### C-LY1. Ostrowski–Schneider / Lyapunov-inertia reframe of n₊(W) — KNOWN-OPEN (overlaps [CD-W1]/[CD-W5])
**Idea:** The control inertia theorem (Ostrowski–Schneider 1962, standard): for AX + XA* = −Q with
Q ⪰ 0, a Hermitian solution X has inertia *matched* to A (X ≻ 0 ⟺ A Hurwitz, under controllability).
Mapping: if W_T were the solution X of a Lyapunov equation whose dynamics A has the zeros as eigenvalues,
the theorem would give n₊(W_T) = n₊(A) *with equality* — a strictly stronger statement than the rank–
trace bound. The obstacle: no such A exists — the "dynamics with the zeros as eigenvalues" is the
Hilbert–Pólya operator ([CD-W5], [P8.2]), whose construction IS RH. At the infinite level this is an
equivalent reformulation (the W-P1 risk); there is no *finite* shadow because no explicit A is available
for the compressed form either.
**Analogy:** Lyapunov equation + inertia transfer ↔ the Weil form + Sylvester; the missing "A" is the
missing Hilbert–Pólya operator.
**Needs:** a Hilbert–Pólya candidate (none rigorous).
**Feasibility:** Low. Value: a clean statement of *why* the inertia route cannot beat the rank–trace
bound without a new operator — prevents re-derivation.
**Cheapest probe:** none (documented).

### C-LY2. The shift-invariance / Toeplitz Lyapunov (Stein) equation on W_T — KNOWN-DEAD
**Idea:** W_T is the Gram matrix of Gabor vectors v_ρ[k] = Ψ(s_ρ − k) — translates of one window. The
grid-shift S (Sv)[k] = v[k−1] is Toeplitz-generating, and a Toeplitz/Stein equation X = S*XS + B would
carry *new* inertia constraints on W_T from a boundary term B (the discrete Ostrowski–Schneider: B ⪰ 0,
‖S‖ ≤ 1 ⟹ X ⪰ 0).
**Death (derived here):** the shift acts on the *grid index k*, so S*WS is the Gram matrix of the
*shifted configuration* (s_ρ + 1) — W − S*WS is the difference of two Gram matrices at *different zero
configurations*, i.e., zero-side data, not a boundary term; the tight-frame identity (Claim 2.1) is the
only window-data statement and it is already fully consumed by the two-moment evaluation. The Stein
structure adds nothing unconditional.
**Cheapest probe:** none (recorded).

### C-LY3. Carathéodory–Fejér / PSD-Toeplitz real-rootedness (CvS 2025) — TESTED-OPEN (probe run; part A positive, part B negative)
**Idea:** The held source [PF #61, arXiv:2511.23257, full text read] proves: if the quadratic form with
Schwartz kernel D̃(x−y) defines a lower-bounded self-adjoint operator on L²([−L/2,L/2]) with simple,
isolated lowest eigenvalue λ and even eigenfunction ξ, then all zeros of ξ̂ (the FT) lie on the real
line — via a C*-algebraic corollary of **Carathéodory–Fejér 1911**: a rank-(n−1) PSD Toeplitz matrix has
an eigenvector whose polynomial is real-rooted. This is the closest published relative of our method (the
truncated Weil form / Galerkin matrix is the same construction as W_T in the CvS/CCM normalization, per
[PF #59-60]). NEW transfer: (i) state the *finite* CF condition for our W_T (or its interior Toeplitz
part — the frame kernel Φ(τ−τ′) is translation-invariant, Lemma 2.2); (ii) the *consequence* if the
window-side object is real-rooted: an *explicit Hadamard product* and a *sign/interlacing* structure —
genuinely outside the (tr, ‖·‖²) budget D (the QI sweep's negative does not cover sign structure).
**Probe run (CHECKED NUMERICALLY, `tools/control_probe_kernel.py`; output
`tools/control_probe_kernel_out.txt`; `uv run --quiet --with mpmath --with numpy python tools/control_probe_kernel.py`):**
- **Part A — kernel real-rootedness (POSITIVE):** the frame kernel
  Φ(x) = ∫_{−1/2}^{1/2} cos²(√2u)e^{ixu}du = sin(x/2)/x + ½[sin((x+2√2)/2)/(x+2√2) + sin((x−2√2)/2)/(x−2√2)]
  has, in the box [−40,40]×[−20,20], **12 zeros (argument-principle winding count), all real**:
  α₁ ≈ 7.042241, α₂ ≈ 12.950871, α₃ ≈ 19.106031, α₄ ≈ 25.325100, α₅ ≈ 31.569809, α₆ ≈ 37.827344
  (next at ≈ 44.09; max |Im| = 1.5e-56, |f| < 1e-42). The finite-T Gabor kernel
  Ψ(s) = sin(1/√2−πs)/(√2−2πs) + sin(1/√2+πs)/(√2+2πs) has **78 zeros in the box, all real**
  (roots ≈ 1.057, 2.030, 3.020, 4.015, 5.012, 6.010, 7.009, … near-integer; max |Im| = 2.0e-55).
  Φ(0) = 0.8492279993183042 = ∫ψ² ✓; Ψ(0) = 0.918725; pole value of Ψ = Φ(0) ✓.
- **Part B — CF mechanism on the finite Toeplitz T[j,k] = Φ(j−k) (NEGATIVE):** T is PSD (min eig
  4.7e-17 … −3.2e-16, consistent with the nonnegative symbol cos²(√2u)), but the ground-state
  eigenvector polynomial is **NOT real-rooted**: max |Im(roots)| = 0.467, 0.838, 1.105 for d = 12, 24, 48
  (growing with d) — the CF lemma's rank-(n−1) hypothesis is not met and its conclusion fails
  numerically. The CvS/CF mechanism does **not** transfer to the finite lattice compression.
**Consequence (honest):** the *sign-structure* fragment survives only through Part A's real-rootedness,
whose unconditional certificate use is blocked by the same wall as ever (the cross entries ⟨v_ρ,v_ρ′⟩ =
Φ(s_ρ−s_ρ′) have the sign pattern *determined by the zero separations* — zero-data; uniform use needs a
min-separation/repulsion input, [P1.4] KNOWN-OPEN). What Part A *does* give unconditionally is the
explicit Hadamard product Φ(x) = Φ(0)∏(1−x²/αᵢ²) (Φ is of exponential type, genus ≤ 1), hence the
explicit quadratic contraction |⟨v_ρ,v_ρ′⟩| ≤ Φ(0)·(1−s²/α₁²) for |s| < α₁ ≈ 7.04 — the *concrete
repulsion-pricing form* of [P1.4] with explicit constants, and a candidate tool for the error/tail terms
of the off-diagonal prime-side sums ([P7.1]-adjacent). See C-PF (Pool 3).
**Cheapest next probe (<1h):** (a) verify Part A at larger boxes [−100,100]×[−50,50] (any complex root
beyond 40 kills the product formula's global validity — 20 min); (b) check whether real-rootedness of Φ
is *provable* (Φ is a sum of three sincs — Laguerre–Pólya class; a literature/argument check, 30 min).

### C-LY4. Lyapunov-rank / minimal-PSD-decomposition count — KNOWN-DEAD
**Idea:** the certificate's b = n₊(Q) counts positive directions of the off-line part; control/QI
"Lyapunov rank" = minimal number of PSD terms in a decomposition.
**Death:** b is an *upper bound on the cost*; minimality reduces the *representation*, not the cost —
no admissible configuration is over-charged by a non-minimal decomposition. No new inequality on D.
**Cheapest probe:** none (recorded).

### C-LY5. Kreiss / pseudospectrum diagnostic: resolvent norm near the spectral edge — NEW (diagnostic, overlaps [P1.3])
**Idea:** The Kreiss matrix theorem and pseudospectral bounds certify "spectrum location given resolvent
data". For W_T (prime-side, [CD-V1] code): ‖(W_T − zI)⁻¹‖ for z just below the positive edge measures
*spectral clustering* — the control name for [P1.3]'s edge-density diagnostic. Value: a *quantitative*
clustering meter (how close the bottom of the spectrum is to a cluster of small eigenvalues = a
near-(1,1)-plane footprint) computed from primes.
**Analogy:** pseudospectrum ⟺ ε-neighborhoods of the empirical spectrum; Kreiss bound ⟺ resolvent-moment
certificates.
**Needs:** W_T spectra (exists).
**Feasibility:** Low (measure). Value: diagnostic for the "off-line structure hiding at the bottom"
question [P1.3]/[P4.3].
**Cheapest probe (<1h):** extend [CD-V1]/[AF] code: max resolvent norm on a grid of z below the edge at
T = 200–600; compare with the p = 0 model prediction.

---

## Pool 3 — Balanced truncation / model reduction

### C-BT1. Glover/Enns truncation bounds vs Lemma 3.2 on the (1,1)-blocks — TESTED-OPEN (expected negative)
**Idea:** The model-reduction error bounds (Glover 1984, Enns 1984, standard): ‖G − G_k‖_∞ ≤ 2Σ_{i>k}σᵢ
(Hankel singular values), and the trace/HS relatives — a *family* of "rank vs trace vs HS" inequalities
beyond Lemma 3.2. The certificate's Lemma 3.2 is the c=2 member; the question posed in the task ("do any
beat it on (1,1)-blocks?") has the same answer as the QI sweep at the class level: all these bounds are
functions of (tr, ‖·‖²_F, rank, n₊) — the budget D — so `lemmaR_tight` (PROVEN) bounds them all. The
*new* control-specific members worth testing: the "2Σσ" bound and the *max-row-sum / Perron* bounds on the
block structure.
**Analogy:** Hankel singular values ↔ eigenvalues of the Gramian pair; truncation error ↔ the certificate
deficit.
**Needs:** one numeric sweep (extend tools/qi_sweep.py).
**Feasibility:** Low. Value: closes the class-level question from the control direction (independent of
[QS]); expected negative, cheap to settle.
**Cheapest probe (<1h):** `uv run --with numpy python tools/qi_sweep.py` extended with the Glover 2Σσ
bound and the max-row-sum bound on the synthetic (1,1)-block data (TEST B configs); report whether any
beats Lemma 3.2's RHS (expected: no).

### C-BT2. Hankel singular-value *decay* of the zero-moment Hankel ↔ repulsion pricing — NEW (prices [P1.4])
**Idea:** For a Hankel matrix with an *atomic* symbol (the zero measure), the singular values decay at a
rate governed by the *separation* of the atoms (the classical "off-diagonal decay of Hankel operators
with analytic symbol" has no atoms; with atoms the decay is governed by the minimal gap — reported
standard, verify before use). The zeros' moment Hankel (from power sums Σγ^k, [CD-W3]) has atoms at the
zero heights; its σᵢ decay curve is *measurable* from real zeros, and the decay rate is a *pricing* of
the repulsion input: "a minimal gap ε ⟹ decay rate r(ε) ⟹ what the certificate's higher-moment rows are
worth" — the control-theoretic form of [P1.4]'s ceiling(ε) curve.
**Analogy:** Hankel singular-value decay (model reduction) ↔ the value of each moment row (certificate);
atom separation ↔ level repulsion.
**Needs:** (i) the zero-moment Hankel from real zeros (cheap); (ii) the σᵢ computation and decay fit;
(iii) a statement connecting decay to a certificate input (CONJECTURED — the decay is zero-side
diagnostic data, usable only as a pricing roadmap, exactly like [P1.4]).
**Feasibility:** Low (probe). Value: a numeric price curve for the only input (repulsion) that breaks the
ceiling.
**Cheapest probe (<1h):** Rust/mpmath: from the cached 1000 zeros (34 digits) compute Σγ^k, k ≤ 40, build
the 20×20 Hankel, print the σᵢ decay exponent and compare with the prediction from the measured minimal
gap.

### C-PF. Perron–Frobenius / Hadamard-product structure of the Gram matrix (probe-backed) — NEW (repulsion pricing + slack explanation, [P1.4]'s explicit form)
**Idea:** C-LY3 Part A's probe found the frame kernel Φ is *numerically real-rooted* with explicit roots
α₁ ≈ 7.042, α₂ ≈ 12.951, … (max |Im| = 1.5e-56). Since Φ is the Fourier transform of the compactly
supported measure cos²(√2u)du (exponential type, genus ≤ 1), real-rootedness would give the Hadamard
product Φ(x) = Φ(0)·∏ᵢ(1 − x²/αᵢ²), and hence, for the zero-indexed Gram matrix G[ρ,ρ′] = ⟨v_ρ,v_ρ′⟩ =
Φ(s_ρ − s_ρ′) (full-grid frame identity, Lemma 2.2): (i) **entrywise positivity** of G whenever all zero
separations are < α₁ (the typical case — mean spacing 1), so G is a *positive matrix* in the
Perron–Frobenius sense: λmax simple with a strictly positive eigenvector; (ii) the **explicit quadratic
contraction** |G[ρ,ρ′]| ≤ Φ(0)·(1 − s²/α₁²) for |s| < α₁ — a quantitative bound on the off-diagonal
*blocks* (the P–Q interaction term tr(PQ₋) that Lemma 3.2's proof pays for via von Neumann). The honest
status: the *uniform* certificate use is still blocked (the contraction needs the separations, i.e., a
min-gap/repulsion input, [P1.4] KNOWN-OPEN), but (a) the contraction is now *explicit with window-only
constants* — any future repulsion input plugs directly into it; (b) the *measured* finite-T slack
(bound/N = 0.709–0.717, [AF]) is partly *explained* as the entrywise contraction of the real Gram matrix
(a new, code-backed explanation); (c) the real-rootedness itself is a *provable-in-principle* statement
with a concrete attack: Φ(x) = (1/2)·N(x/2)/((x/2)((x/2)² − 2)) with the explicit numerator
N(u) = [(1 + cos√2)u² − 2]·sin u − √2·sin√2·u·cos u (u = x/2) — **CHECKED NUMERICALLY** (matches Φ to
< 1e-18 at the roots), so real-rootedness of Φ ⟺ real-rootedness of this explicit combination of
sin/cos — a Laguerre–Pólya-class statement with a classical toolkit.
**Analogy:** Perron–Frobenius (positive matrices: dominant eigenvector, spectral gap) ↔ the Gram
matrix's structural positivity; Hadamard product ↔ explicit cross-term decay (the model-reduction
"Gramian" picture, balanced-truncation pool).
**Needs:** (i) the larger-box real-rootedness check (C-LY3's next probe); (ii) the Laguerre–Pólya
argument for Φ; (iii) a statement of the entrywise-positivity condition "all separations < α₁" in terms
of a box/min-gap hypothesis (cf. the B25/GS26 narrow-box framework).
**Feasibility:** Low–Med. Value: the concrete, explicit-constant form of the only input ([P1.4]
repulsion) that breaks the ceiling, plus a structural explanation of the measured slack.
**Cheapest probe (<1h):** extend C-LY3's probe: (a) [−100,100]×[−50,50] root check of Φ (no complex
roots ⇒ product formula on the larger window); (b) from the cached zeros, histogram the separations
s_ρ−s_ρ′ against α₁ = 7.04 and report the fraction of pairs with |s| < α₁ (the entrywise-positivity
fraction); (c) verify |G| ≤ Φ(0)(1−s²/α₁²) on real cross inner products (mpmath, [AF] machinery).

### C-BT3. Ho–Kalman / realization-theory rank test for the third moment (P2's cheapest form) — NEW (overlaps [P3.4], [P6.5])
**Idea:** Realization theory (Ho–Kalman, standard): the rank of the block-Hankel of a system's Markov
parameters = the McMillan degree, and the *minimal* realization is unique. The zeros' moment sequence
(m₁,m₂,m₃,m₄) = (1, 4/3, 2, 13/4) ([AM]) has a 3×3 Hankel; the two worlds the two-moment certificate
cannot separate (all-simple vs 2/3-simple + 1/6-double, [AM] PROVEN) give *different* third moments —
their *realization ranks* differ. The NEW claim: the *canonical* rank test (is the 3-moment Hankel of rank
1, 2, or 3, and which principal representation — cf. the Nevanlinna reframe [P8.1]) is the sharpest cheap
decider of whether the third moment can separate the worlds — the concrete linear-algebra core of the
P6.5/Christoffel probes.
**Analogy:** Ho–Kalman rank test ↔ the distinct-wall separation test; McMillan degree ↔ the number of
distinct zero heights.
**Needs:** (i) the 3×3 Hankel from (1, 4/3, 2) and its rank/eigenvalue structure; (ii) the same for the
"double-world" moment sequence (m₃ for the 2/3+1/6 world — the LP in [P6.5] gives it); (iii) the
comparison.
**Feasibility:** Low (probe). Value: decides the P2 question's linear-algebra feasibility in 30 minutes;
feeds [P6.5]'s LP.
**Cheapest probe (<30min):** mpmath: Hankel[(1,4/3,2)], print rank/eigenvalues; Hankel of the double-world
(m₁,m₂,m₃′); if both are PSD and the third-moment difference doesn't change the rank, the "realization"
view says the worlds remain close — a clean negative for the rank-based formulation (the LP [P6.5] remains
the arbiter).

### C-BT4. McMillan-degree/rank identity for the distinct count — NEW (framing)
**Idea:** rank(Hankel of the zero measure) ≤ #distinct zero heights (an elementary rank bound), tying the
distinct-count (c=3) bookkeeping to a Hankel rank — the realization-theoretic name for why the distinct
functional is a *rank-type* object (as opposed to the on-line n₊ which is an *inertia-type* object).
**Analogy:** McMillan degree ↔ distinct-zero count; rank (not inertia) ↔ the 5/6 wall's functional.
**Needs:** none (documentation).
**Feasibility:** immediate. Value: explains *why* P2's third moment enters the distinct functional
(different bookkeeping type) — cross-links [CD-V3]/[AM].
**Cheapest probe:** none.

---

## Pool 4 — Passivity / positive-real functions / KYP

### C-PS1. The finite-T deficit as a Nyquist/sampling-resolution error — NEW (P6 diagnostic, CONJECTURED)
**Idea:** The grid α_k = T + (T/N)k samples the zero distribution at rate N/T = one zero per cell; the
window's Fourier support (~1/l at height T) is exactly the resolution at which the off-diagonal
pair-sum terms are non-negligible — i.e., the certificate's data is *sampled at the Nyquist rate of the
pair-correlation structure*. Control's sampling/Nyquist language gives a *prediction*: the finite-T
deficit Δ(T) = ‖W‖²/N − 1.3275 ([AF], measured ~1/log T) is dominated by the *resolution* (the mean
spacing ~1/log T), not by a kernel artifact (Fisher–Hartwig would give a T-power law, [P5.5]) nor by the
arithmetic pair-correlation error (1/√log T, B24 Thm 1). The measured 1/log T matches the spacing scale
— the control-framed explanation of the [AF] trend, and a *decomposition* of P6's error into
kernel-FH + sampling + arithmetic parts.
**Analogy:** Nyquist sampling / aliasing ↔ grid resolution of the zero distribution; the sampling error
↔ the finite-T deficit.
**Needs:** (i) the [AF] Δ(T) data; (ii) a fit against the 1/log T (spacing) and 1/√log T (arithmetic)
models; (iii) the FH prediction ([P5.5]).
**Feasibility:** Low (analysis of existing data). Value: a testable physical explanation of the measured
deficit — the "which mechanism" decider for P6.
**Cheapest probe (<30min):** fit [AF]'s Δ(T) curve against 1/log T, 1/√log T, and T^−θ; report the best
exponent (reuse the existing [AF] numbers; no new compute).

### C-PS2. Passivity-index RH-ometer (min-eig of W_T, prime-side) — NEW (framing of [P1.3])
**Idea:** For a passive system the "passivity index" is the margin by which the operator exceeds
passivity; for W_T the index is min-eig(W_T) — computed from primes ([CD-V1]). The real W_T is
numerically near-PSD (min eig ≈ −1e-17·λmax, [AF]) — a huge passivity margin, i.e., the prime-side
"RH-ometer" reads "no off-line structure at the edge". Control vocabulary for the [P1.3]/[P4.3]
diagnostic.
**Analogy:** passivity margin ↔ min-eig; lossless system ⟺ RH (all zeros on the line).
**Needs:** none beyond [CD-V1] (documentation + the [P1.3] probe).
**Feasibility:** Low. Value: naming + cross-linking; no new math.
**Cheapest probe:** fold into [P1.3].

### C-PS3. KYP / frequency-sampled passivity certificate — the certificate as a sampled passivity check — NEW (framing; P6-adjacent)
**Idea:** The KYP lemma (standard) equates frequency-domain positive-realness with a state-space LMI —
the *same* frequency ↔ state-space duality the paper's method runs (prime-side moments ↔ zero-side
matrix). The paper's certificate checks the Weil form at *finitely many* test frequencies (the window
grid): a *sampled passivity check*. The control question: is the *sampling error* (checking at N points
instead of all frequencies) a *provable* P6 error term? Honest answer: the paper's Lemma 3.3-type
statements already carry the sampling/truncation errors as o(1); the KYP framing names them but adds no
new provable constant. Keep as documentation (the frequency-sampling reading of C-PS1).
**Analogy:** KYP LMI ⟺ Weil-form positivity; sampled passivity ⟺ the finite window grid.
**Needs:** none (documentation).
**Feasibility:** Low. Value: prevents funding a "KYP gives new certificates" line (the LMI direction is
Theorem D's already-proven window optimality, C-PS4).
**Cheapest probe:** none.

### C-PS4. Convex-hull-of-windows / KYP LMI search vs Theorem D — KNOWN-DEAD
**Idea:** maximize the certificate over a *polytope* of windows (KYP/LMI flavor) rather than the single
cosine.
**Death:** Theorem D + [AK] prove the cosine is the *global* minimizer of the Rayleigh quotient over all
bandwidth-one positive windows — the window direction is closed (PROVEN), exactly as the LP closed the
certificate direction [AL]. No window search can beat 0.6725.
**Cheapest probe:** none (recorded; cite [AK]).

---

## Pool 5 — Root locus / Bode / Nyquist

### C-NY1. Certified argument-principle counts in narrow strips: the direct route to the shadow-price-1 datum — NEW (P1/P6, highest EV)
**Idea:** The LP-dual attack [AL] proved the certified value is pinned 1:1 by the certified simple
fraction p₁ (shadow price exactly 1) — and p₁ is exactly "the zero configuration has ≥ p₁·N on-line
simple zeros". The RvM-style argument principle counts zeros from *boundary data*: the number of zeros of
ξ in a box [1/2−δ, 1/2+δ] × [T, 2T] equals (1/2πi)∮ ξ′/ξ — computable from ξ values on the box =
*primes + Γ, zero-free*. NEW: (i) the *empirical* version — complex root-finding of ζ in narrow strips at
heights 10⁴–10⁵ (Rust, extending the on-line tools [CD-V6]) measures the off-line count p(T;δ) directly —
the *exact* quantity that separates reality from the ceiling law (the law's off-line content is the
doubles/pairs structure Lemma 3.2 cannot price [AM], and the LP cannot move without p₁); (ii) the
*provable* version — at a fixed T, the box count is a *rigorous integer* from ξ evaluations with the
standard RvM-style error control, i.e., a *certified* "no off-line zeros at depth δ in [T,2T]" statement
per height — a *new class* of finite-T theorem (P6) that does not require the 10¹³-verification machinery.
**Analogy:** Nyquist encirclement / argument principle (zeros inside from boundary winding) ↔ the
certificate's need for the off-line count; RvM's N(T) count is the classical instance — the strip
refinement is the new one.
**Needs:** (i) ζ evaluation in the strip (Euler–Maclaurin/Riemann–Siegel, existing machinery, extended
off-line); (ii) the box-contour error control (standard RvM proof, [litmap]); (iii) Rust.
**Feasibility:** Low–Med (probe is hours). Value: the *only* control vector that directly produces the
shadow-price-1 datum at *new* heights; even at heights where RH-below-T already answers p = 0, the
*certified contour* form is a different, independently verifiable method and a P6 finite-T statement.
**Cheapest probe (<1h):** Rust: search for zeros of ζ in [1/2−10/log T, 1/2+10/log T] × [T, 2T] at
T = 10⁴ (grid of Euler–Maclaurin evaluations, Newton refine off-line candidates); print the off-line
count and compare with the on-line count from the cached data. Kill: if p is exactly 0 at all tested
heights (expected — RH-below-T), the *value* is the certified-contour form (P6) and the new-height
measurement, both still worth recording; the vector does not promise a proof.

### C-NY2. Nyquist/encirclement framing of RH + the SFF phase probe — KNOWN-OPEN (framing) + NEW (probe)
**Idea:** RH ⟺ every contour in the strip has the "correct" winding (the argument of ξ counts only
on-line zeros). This is the argument principle, i.e., equivalent to RH by construction ([CD-W4]'s
"reformulation = no free lunch"). The genuinely probe-able fragment: the *phase* of the zero-sum spectral
form factor K(α) = Σ_ρ e^{iαγ}-weighted (the complex SFF, [P2.1]) — its *argument's* winding over α is a
complex object the certificate never reads (intensity-only, [P6.4]); measure whether the argument is
well-behaved (monotone / bounded variation) on real zeros — a diagnostic for P3's beyond-1 region.
**Analogy:** Nyquist plot winding ⟺ argument of the SFF over α; encirclements ⟺ "resonances".
**Needs:** the SFF computation ([P2.1]'s probe).
**Feasibility:** Low (probe). Value: diagnostic for the beyond-1 region [P3]; the framing itself is
equivalent-by-construction.
**Cheapest probe (<1h):** extend [P2.1]: compute arg K(α) for α ∈ [0,8] from real zeros; print the total
variation and winding; compare with the GUE prediction.

### C-NY3. Bode gain–phase (Kramers–Kronig) relation on the Weil sum — KNOWN-DEAD
**Idea:** for a causal/minimum-phase system the phase is the Hilbert transform of the log-gain — a
*dispersion relation* linking the real and imaginary parts, which could give cross-constraints beyond the
magnitude-only certificate.
**Death:** the Weil sum (explicit formula) is *even* in the height variable (ρ ↔ 1−ρ̄ pairing), so its
imaginary part on the real axis is identically zero ([CD-A2]'s Im W ≡ 0, PROVEN) — the dispersion
relation is vacuous on the real axis, and off the axis there is no new provable fragment (the complex
structure is the argument principle, C-NY1/C-NY2).
**Cheapest probe:** none (recorded, cite [CD-A2]).

### C-NY4. Root-locus v(λ): the certificate value as the window bandwidth varies — NEW (diagnostic, overlaps [CD-V5])
**Idea:** In control, the root-locus traces closed-loop poles as a gain varies; here the "locus" is the
certified value v(λ) as the window bandwidth λ varies (the paper's F(λ) branch, Theorem C; the
support-curve roadmap [CD-V5] for 0.70/0.80/0.90 at supports 1.04/1.26/1.70). The control *addition*: the
*margins* — d v/dλ and the "gain margin" (the λ-range over which v ≥ 2/3), i.e., the sensitivity of the
certificate to window mistuning, computable from the LP machinery [AL].
**Analogy:** gain margin / sensitivity ⟺ the certificate's robustness to window choice.
**Needs:** the [AL]/[CD-V5] LP extended over λ.
**Feasibility:** Low (compute). Value: a quantitative sensitivity statement + re-verification of the
support curve.
**Cheapest probe (<1h):** extend the [CD-V5] LP: report v(λ) for λ ∈ {1/2, 2/3, 3/4, 1, 1.04, 1.26, 1.70}
and the derivative at λ = 1.

### C-NY5. Winding of the pair-correlation "loop gain": F(α) as a stability margin — NEW (speculative, WILD-adjacent)
**Idea:** F(α) ≥ 0 (PROVEN, B24), ∫₀¹F = 1 (PROVEN); treat F as an "open-loop gain" whose departure from
1 (the GUE value) is the "loop error". The complex SFF's winding (C-NY2) is the honest version; the
real-valued F has no winding — so this reduces to C-NY2 with the real-F margin reading (how far the
empirical F is from 1 on [0,1] — the [CD-V6] form-factor measurement). Keep as a framing note.
**Analogy:** loop gain ⟺ F; unit-gain loop ⟺ GUE.
**Needs:** the [CD-V6] empirical F.
**Feasibility:** Low. Value: documentation.
**Cheapest probe:** fold into [CD-V6]/C-NY2.

---

## Pool 6 — Structured singular values / μ-analysis

### C-MU1. The certificate as a D-scaled robust margin; the 256-law as the worst-case real perturbation — NEW (confirms [AL] from the control direction)
**Idea:** μ-analysis (Doyle, standard): for block-structured uncertainty, μ(M) is bracketed by scaled
norms inf_D ‖DMD⁻¹‖, and the *real* perturbation theorem guarantees a worst-case real Δ at the margin.
The certificate LP [AL] is *literally* a D-scaling: the certificate r reweights the form-factor rows
s_j (validity c₀ + Σ s_j r(j/N) ≤ p₁), the box |r| ≤ 1 is the normalization, and the residual |E(1)| is
the "stability radius" — the smallest off-line/multiplicity perturbation that moves the certified value.
The real-μ reading: the 256-law is the *worst-case real perturbation* (the extremal configuration), and
the certificate's margin is exactly |E(1)| = 2.54·10⁻⁶ ([AL], CHECKED NUMERICALLY). This re-derives the
LP-dual closure from robustness language: *no structured perturbation within bandwidth one moves the
value beyond |E(1)| — only the datum p₁ (the perturbation's size) does, 1:1.*
**Analogy:** D-scaling ⟺ the certificate's row reweighting r; real-μ worst case ⟺ the 256-law.
**Needs:** none (documentation; the numbers are [AL]-verified).
**Feasibility:** immediate. Value: an independent, control-framed confirmation of the in-class closure and
the shadow-price-1 structure.
**Cheapest probe:** none.

### C-MU2. Control inequality family vs Lemma 3.2 on the (1,1)-blocks — TESTED-OPEN (expected negative)
**Idea:** Sweep the control-specific rank/trace/HS bounds (Glover 2Σσ; max-row-sum/Perron; D-scaled
norms; Ostrowski–Schneider inertia transfer) against the certificate's block structure, on the same
synthetic data as [QS] TEST B/G. Expected verdict (class-level): all read the budget D, so
`lemmaR_tight` (PROVEN) caps them — no uniform gain; the sweep closes the control direction of the
"does any inequality beat Lemma 3.2?" question independently of the QI sweep.
**Analogy:** model-reduction/robustness bounds ⟺ the rank–trace family; tightness at the crystal ⟺
lemmaR_tight.
**Needs:** an extension of tools/qi_sweep.py.
**Feasibility:** Low. Value: a documented negative (or a surprise).
**Cheapest probe (<1h):** `uv run --with numpy python tools/qi_sweep.py` extended with the Glover 2Σσ and
max-row-sum bounds on the TEST B/G configurations; report whether any RHS exceeds Lemma 3.2's (expected:
no).

### C-MU3. Stability radius (Hinrichsen–Pritchard): distance of reality from the sharp crystal — NEW (diagnostic, overlaps [CD-V1])
**Idea:** The stability radius is the distance (in a structured norm) from the real configuration to the
nearest "bad" one. For the certificate: how far does the *real* W_T sit from the sharp
diag(1,…,1,2,…,2) configuration (the extremal of `lemmaR_tight` / Prop 4.4(b))? The [AF]/[CD-V1] numerics
already show large slack on real data (bound/N = 0.709–0.717 > 0.6725); the stability-radius reading turns
this into a *margin* (the norm of the smallest perturbation reaching the crystal) — the control name for
the V1 slack question.
**Analogy:** stability radius ⟺ distance to the worst-case configuration.
**Needs:** the [CD-V1] spectrum + a distance computation.
**Feasibility:** Low (measure). Value: quantifies the method's real slack in robustness units.
**Cheapest probe (<1h):** from the [CD-V1] W_T at T = 200–600, compute the minimal ‖Δ‖_F such that
W_T + Δ has the sharp eigenvalue pattern (smallest perturbation to the crystal); report the margin vs T.

### C-MU4. Real-μ "smallest perturbation moving the certified value by δ" — NEW (confirms the no-missing-constraint result [AL] §5)
**Idea:** The μ-framing of [AL] §5's headline: inside bandwidth one the value moves only with p₁
(1:1); in μ language, the certificate map has a *condition number* 1 with respect to the simple-fraction
datum and ~|E(1)| with respect to everything else. Any "structured perturbation" one can write down from
bandwidth-one data fails to move v — the control-theoretic restatement of "no missing constraint inside
bandwidth one" (PROVEN numerically, [AL]).
**Analogy:** condition number ⟺ shadow price; structured perturbation ⟺ admissible configuration change.
**Needs:** none (documentation).
**Feasibility:** immediate. Value: cross-links [AL] to μ-analysis vocabulary for future
cross-checking.
**Cheapest probe:** none.

---

## TOP 10 (EV × feasibility × cheap-probe), control-specific

1. **C-NY1 — Certified argument-principle / root-finding counts of off-line zeros in narrow strips.**
   The shadow-price-1 datum p₁ at new heights, with a *provable* finite-T form (RvM-style contour counts)
   — the only control vector that directly produces what the LP says moves the certificate. Probe: Rust
   strip search at T = 10⁴ — hours.
2. **C-LY3/C-PF — Kernel real-rootedness + explicit Hadamard/Perron–Frobenius structure (PROBE RUN:**
   Part A positive — Φ and Ψ numerically real-rooted, Φ(0)=0.849228, roots α₁≈7.042, α₂≈12.951, …
   max|Im|<1e-55, explicit numerator N(u)=[(1+cos√2)u²−2]sin u − √2 sin√2·u cos u verified to <1e-18;
   Part B negative — the CF mechanism does not fire on the finite Toeplitz (eigenvector polynomial max
   |Im| = 0.47, 0.84, 1.10 for d=12,24,48)). Live fragments: prove Φ real-rooted (Laguerre–Pólya), the
   quadratic cross-contraction |⟨v_ρ,v_ρ′⟩| ≤ Φ(0)(1−s²/α₁²), and the entrywise-positivity fraction of
   the real Gram matrix — the explicit-constant form of the [P1.4] repulsion input. Probe: larger-box
   root check + separation histogram — <1h.
3. **C-RH2 — Jensen-polynomial dictionary + prime-computable degree-2 discriminant.** A new zero-free
   RH-ometer and the formal P2 dictionary (degree-d Jensen ↔ moment order 2d). Probe: ξ,ξ′,ξ″ from the
   explicit formula; discriminant margin — <1h.
4. **C-BT3 — Ho–Kalman realization rank test on the (1, 4/3, 2) moment Hankel.** The cheapest concrete
   decider of P2's linear-algebra feasibility; feeds [P6.5]. Probe: 3×3 Hankel ranks, both worlds — <30min.
5. **C-PS1 — The 1/log T deficit as a Nyquist/spacing-resolution error (P6 decomposition).** A testable
   physical explanation of the [AF] measurement; separates kernel/sampling/arithmetic error. Probe: fit
   [AF] data — <30min.
6. **C-MU2 — Control-family inequality sweep vs Lemma 3.2 (Glover, Perron, D-scaled).** Closes the
   class-level "does any control bound beat Lemma 3.2?" question independently of [QS]; expected
   negative. Probe: extend qi_sweep.py — <1h.
7. **C-BT2 — Hankel singular-value decay ↔ repulsion pricing.** A numeric price curve for the only input
   ([P1.4] repulsion) that breaks the ceiling; now cross-linked to C-PF's explicit contraction law.
   Probe: 20×20 Hankel from the cached zeros — <1h.
8. **C-NY4 — Root-locus v(λ) with margins.** Quantifies the certificate's sensitivity to window choice;
   re-verifies the [CD-V5] support curve. Probe: extend the LP over λ — <1h.
9. **C-RH1 — Routh-array algorithm for the CMS/Christoffel certificates.** The operational (non-LP) form
   of P2's third-moment route; third formulation of the P2 attack. Probe: Routh/Stieltjes CF on the 3×3
   Hankel — <1h.
10. **C-MU1/C-MU4 — μ/D-scaling identification + worst-case-real-perturbation = 256-law.** The
    control-framed confirmation of [AL]'s in-class closure (documentation; zero new compute; the C-MU2
    sweep is its only numeric companion).

**Strategic reading.** The control angle's two strongest NEW contributions are (i) **C-NY1** — a direct,
zero-free measurement/certification of the shadow-price-1 datum p₁, the exact quantity [AL] identified as
the only thing that moves the certificate; and (ii) **C-LY3/C-PF** — a *probe-backed* finding: the frame
kernel Φ and the finite-T Gabor kernel Ψ are numerically real-rooted (all zeros in the checked box real,
|Im| < 1e-55), giving an explicit Hadamard product, a verified closed-form numerator
N(u) = [(1+cos√2)u²−2]sin u − √2 sin√2·u cos u, and the explicit quadratic contraction of the cross inner
products — the only candidate consuming data *outside* the (tr, ‖·‖², rank, n₊) budget D, whose Part B
(CF mechanism on the finite Toeplitz) is a clean documented negative. The control *family* of inequalities
(Glover, Perron, Ostrowski–Schneider, D-scaling) is expected to confirm the QI-sweep negative at the class
level (C-MU2 — cheap, closes the direction). The rest is diagnostics (P6 decomposition C-PS1, repulsion
pricing C-BT2, stability radius C-MU3) and documentation (C-MU1/C-MU4 re-derive [AL] in robustness
language; C-RH4/C-PS4/C-LY1/C-NY3 record why the Lyapunov/KYP/window directions are closed). The persistent
wall — beyond-bandwidth-1 F, third moments, repulsion, and now the *sign/Hadamard structure* of the window
kernel (C-LY3/C-PF) — remains the only frontier, and the control picture (Nyquist counting, μ margins,
realization rank) says *why*: the certificate is an intensity-only, D-scaled robust margin, and every
escape is a *phase/structural/count* datum (exactly [P6.4]'s phase-retrieval reading, now with control
vocabulary attached).

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

### W-C1. "RH is the statement that the zero system is lossless; the certificate is the maximum-dissipation bound; 67.25% is the dissipation allowed by two moments" — CONJECTURED (likely equivalent-formulation)
**For:** the passivity index of W_T (min-eig, prime-side) is a clean scalar "how far from RH" meter
(C-PS2); the rank–trace deficit is the "dissipation" the two moments permit.
**Against:** by construction — the "system" is W_T renamed; no new inequality emerges (C-PS3/C-PS4 close
the KYP/window directions). Keep the *index* (it is the [P1.3] edge diagnostic under a control name),
discard the proof claim.

### W-C2. "The zeros are the closed-loop poles of a feedback loop whose open-loop gain is the explicit formula; RH ⟺ zero encirclements" — CONJECTURED (argument-principle by construction)
**For:** the Nyquist plot of the prime-side sum's phase over the contour *is* the argument principle
(C-NY1); a feedback reading gives a *why* for the pairing structure (poles of a real system come in
conjugate pairs — the FE's ρ ↔ 1−ρ̄ is the conjugate-pairing of a real-rational system after rotation).
**Against:** the "plant" is the explicit formula renamed; the provable content is RvM's counting (already
used). The useful fragment: the *phase* probe of the SFF argument (C-NY2) — diagnostic only.

### W-C3. "The 1/log T deficit is a finite-horizon Lyapunov transient; the spectral gap of the zero process sets the rate" — CONJECTURED (overlaps [P9.2]; the rate prediction is testable)
**For:** finite-horizon Lyapunov convergence rates are governed by the spectral gap of the dynamics; the
zero process's "gap" is the mean spacing ~1/log T — matching the measured deficit scale (C-PS1).
**Against:** there is no explicit dynamics (C-LY1's obstacle); the fit is to ten data points. The *rate
prediction* is the honest, testable fragment (same as C-PS1's probe).

### W-C4. "The certificate is a balanced-truncation error bound; the zeros' McMillan degree is the rank of the moment Hankel; 2/3 is the approximation error of the two-moment system" — CONJECTURED (renaming risk)
**For:** the Glover 2Σσ bounds are the same CS family as Lemma 3.2 (C-BT1); the Hankel rank = distinct
count (C-BT4).
**Against:** renaming — no new inequality; the honest content is C-BT1's expected-negative sweep and
C-BT2's decay pricing. Keep those; discard the "2/3 = approximation error" slogan.

### W-C5. "The 256-law is the worst-case *real* structured perturbation; control theory's real-μ theorem *proves* a worst-case real perturbation exists" — CONJECTURED at the μ-theorem level; CHECKED NUMERICALLY at the LP level
**For:** the real-μ lower bound (a worst-case real Δ exists at the margin) is the control-theoretic twin
of the LP's attainment of the ceiling ([AL]: the 256-law attains p₀; the certificate attains
p₀ + |E(1)|). The framing is honest and mostly *confirmed* by [AL]'s numerics.
**Against:** the μ theorems apply to finite matrices with a fixed uncertainty block structure; the
certificate's "perturbations" are admissible configurations — the identification is exact at the LP level
(C-MU1) but no *new* theorem is imported. Value: a robustness-language confirmation of the ceiling.

---

## Label inventory

- **NEW** (invented here, untested): C-RH1, C-RH2, C-LY5, C-BT2, C-BT3, C-BT4, C-PF, C-PS1, C-PS2,
  C-NY1, C-NY2 (probe part), C-NY4, C-NY5, C-MU1, C-MU3, C-MU4, W-C1 … W-C5 (conjectured by
  construction).
- **CHECKED NUMERICALLY (probe run this round, `tools/control_probe_kernel.py`, output
  `tools/control_probe_kernel_out.txt`):** kernel real-rootedness of Φ and Ψ on [−40,40]×[−20,20]
  (all zeros real, max |Im| = 1.5e-56 / 2.0e-55; winding counts 12/78 consistent); Φ(0) = 0.849228;
  roots α₁ ≈ 7.042, α₂ ≈ 12.951, …; the closed-form numerator N(u) = [(1+cos√2)u²−2]sin u −
  √2·sin√2·u·cos u matches Φ to < 1e-18; the finite Toeplitz T[j,k]=Φ(j−k) is PSD but its ground-state
  eigenvector polynomial is NOT real-rooted (max |Im| = 0.467, 0.838, 1.105 at d = 12, 24, 48) — the CF
  mechanism does not fire (C-LY3 Part B negative).
- **KNOWN-DEAD** (killed here or in cited notes): C-RH5 (no disk structure), C-LY2 (shift acts on the
  grid, W−S*WS is zero-side data), C-LY4 (minimality doesn't reduce the cost), C-NY3 (Im W ≡ 0 by
  [CD-A2]; dispersion relation vacuous), C-PS4 (Theorem D/[AK] window optimality is PROVEN),
  C-RH3's naive interlacing (killed in [CD-A4]), C-LY3 Part B (CF/rank-(n−1) mechanism does not transfer
  to the finite lattice Toeplitz — documented negative).
- **KNOWN-OPEN** (core is open / already flagged; control framing only): C-LY1 (Ostrowski–Schneider needs
  the Hilbert–Pólya operator), C-RH3 (Hermite–Biehler, reframe of [CD-A4]), C-RH4 (moment-order cascade
  wall, from [AM]/[AC]), C-PS3 (KYP as documentation), C-NY2 (Nyquist framing,
  equivalent-by-construction), C-BT1/C-MU2 (expected negatives to be tested — TESTED-OPEN).
- **TESTED-OPEN**: C-LY3 (Part A positive — real-rootedness of Φ/Ψ numerically on the checked box; the
  *provability* and the larger-window check are open), C-PF (numerically-backed structure; the uniform
  certificate use is blocked by the missing repulsion input [P1.4]), C-BT1, C-MU2 (probe-now, expected
  no-gain), C-PS2/C-MU3 (fold into [P1.3]/[CD-V1] measurements).
- **Cheapest-probe discipline:** every vector has a <1h probe (mpmath/Rust on existing machinery, or an
  extension of tools/qi_sweep.py / the [AL] LP / tools/control_probe_kernel.py). Nothing requires new
  heavy compute to *start*.

**Honest closing note.** The control angle does not resurrect the two documented walls — Lemma 3.2 is
tight within its data budget (the control inequality family is expected to confirm [QS]'s negative,
C-MU2), and the in-class ceiling 0.6818 is tight (the μ/D-scaling reading re-derives [AL]'s closure,
C-MU1). What control theory adds is: (i) a *direct route to the shadow-price-1 datum* (C-NY1: certified
off-line counts from zero-free boundary data — the argument principle, which is exactly our Z(t)
sign-change counting made quantitative on contours), (ii) a *probe-backed structural finding* (C-LY3/
C-PF: the frame kernel Φ and the Gabor kernel Ψ are numerically real-rooted, giving the explicit Hadamard
product, the verified closed-form numerator, and the quadratic cross-contraction |⟨v_ρ,v_ρ′⟩| ≤
Φ(0)(1−s²/α₁²) — the explicit-constant form of the [P1.4] repulsion input; the CF mechanism's transfer
fails (Part B), documented as a negative), and
(iii) operational/algorithmic and diagnostic forms of the already-funded routes (Routh array for the CMS
cascade, Ho–Kalman rank test for the third moment, Nyquist-rate reading of the finite-T deficit, Hankel
decay pricing of repulsion). The persistent wall remains: the certificate reads intensity-only,
D-scaled, two-moment data; every escape is a phase/structural/count datum, and control theory now names
each one.
