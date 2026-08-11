# Attack: two-bandwidth joint certificate for the DISTINCT count (P6.5)

Round 2, EXECUTIONER. Task: vector P6.5 from `idea-generator-physics.md` — a joint
two-bandwidth certificate, window A at λ = 1 (two moments) + window B at λ = 1/2
(third moment, Rudnick–Sarnak range kλ = 1.5 < 2), targeting the distinct count N_d
(the c = 3 functional that §7.5(e)'s "odd moments don't lower Λ₁(0)" claim does not
cover). Sources: `claude-riemann-paper.txt` §7.5(d,e,f,g) + Appendix B, `attack-multiplicity.md`,
`attack-vector-catalog.md` §3 #2, `idea-generator-physics.md` Pool 6. Companion file:
the parallel agent's single-window third-moment note `attack-thirdmoment.md` (not yet
written as of this writing; the shared `tools/m3_*.py` scripts were read and audited).

Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / REFUTED as in the program's honesty
framework. Nothing here was fabricated; every number was computed in this session.

---

## 0. Bottom line (read this first)

**P6.5 does NOT break the 5/6 distinct wall. Clean negative, documented.**

1. **The task's asserted input m₃(1/2) = 2 is REFUTED.** The correct value of the
   third moment of the sine-kernel Gram matrix at λ = 1/2 (diagonal method, DPP
   diagram) is **m₃(1/2) = 5** (PROVEN, verified three independent ways; the empirical
   ζ-zero value is ≈ 4.8, matching the known finite-height deficit pattern of m₂).
2. With the corrected value, the third moment at λ = 1/2 is *less* useful, not more:
   2m₂(1/2) − m₃(1/2) = 13/3 − 5 = **−2/3 < 0**. The paper's admissible-cubic
   construction (its own §7.5(g) template, the state of the art for third-moment
   distinct bounds) gives **0.7593 N = 41N/54 at λ = 1/2** and **0.8071 N at
   λ = 2/3** — both strictly below 5/6 = 0.8333. It reaches exactly 5/6 only at
   λ = 1, where the third moment is NOT unconditionally available (kλ = 3 > 2).
3. The joint two-bandwidth certificate, as a rigorous argument, requires an
   inequality linking the two windows' Gram-moment data to the shared multiplicity
   structure (a "cross-window" Schur–Horn-type step). **No such inequality exists in
   the sources and none is derivable from the bookkeeping LP** (PROVEN by analysis
   of the LP structure). The best provable bound from the joint data is the max of
   the two single-window certificates = **5/6** (window A).
4. A side finding, important for the parallel agent: the paper's value **m₃(1) = 2 is
   CORRECT**. The `tools/m3_check.py`/`m3_pin.py` closed-form reduction (which yields
   125/64 ≈ 1.9531) contains a bug: B = 2·J3 and D = 3/(4λ) are wrong for λ ≠ 1 in a
   way that also corrupts λ = 1; the correct values are B = (2/λ)·J2, D = 1/λ²
   (details in §2). With the correction, m₃(1) = 2 exactly, restoring the paper's
   m_k(1) = (1, 4/3, 2, 13/4) sequence.

---

## 1. What the joint certificate was supposed to be

From `idea-generator-physics.md` P6.5: run two windows on the same configuration —
window A at λ = 1 (optimal constant; tr and ‖·‖² available unconditionally) and
window B at λ = 1/2 (tr Â³ unconditionally evaluable by the diagonal method in the
Rudnick–Sarnak range kλ = 3·(1/2) = 1.5 < 2) — and price both into the distinct-count
bookkeeping. The idea's own numbers: λ = 1/2 alone gives (3 − C(1/2))/2 =
(3 − 13/6)/2 = 5/12 (useless), but the joint constraint set "is strictly richer than
either alone". The task assigned the joint moments (m₁, m₂, m₃) = (1, 4/3, 2) with
m₃ = 2 labeled "sine-kernel triple correlation ... at λ=1/2".

Relevant paper facts (§7.5, PROVEN in the paper / Appendix B):
- m₂(λ) = 1/λ + λ/3 comes from the Fejér-type integral ∫_{−λ}^{λ}(λ−|α|)F(α)dα =
  λ + λ³/3 normalized by λ² (Remark 5.10; sympy-verified, Appendix B). So
  m₂(1) = 4/3, m₂(1/2) = 13/6. CHECKED NUMERICALLY here from actual ζ zeros (see §2).
- §7.5(e): odd moments do not lower Λ₁(0), the Christoffel bound for the n₊/on-line
  functional, in (1/2, 1); Prop 7.4 makes λ ≤ 1/2 useless for that functional.
- §7.5(g): under RH (so λ = 1 window), the cubic weight
  ψ(m) = m/2 + (2m² − m³)/18 + (4/9)·1_{m=1}, ψ ≤ 1 on integers, gives
  N_d ≥ (1/2)tr Â + (1/18)(2 tr Â² − tr Â³) + (4/9)·s₁ via Schur–Horn applied to the
  admissible cubic; with window-dependent moments (2m₂−m₃ = 0.68524 for the specific
  window) and s₁ ≥ 19/27 [BHB13] this is 0.85082 on RH. **This is the paper's own
  third-moment distinct construction; it is the correct template for any such
  attempt.** With the FLAT moments m₂ = 4/3, m₃ = 2 it evaluates to exactly 5/6
  (derived here, PROVEN arithmetic): (1/2 + (2/3)/18 + (4/9)(2/3)) = 5/6.
- attack-multiplicity.md (PROVEN): 5/6 is the sharp constant of the two-moment c = 3
  method; the extremal world (2N/3 simple + N/6 double on-line zeros, orthogonal
  atoms, Gram = diag(m)) realizes (tr, tr²) = (N, 4N/3) and N_d = 5N/6 with equality
  in every step (lemmaR_tight). That world also has tr³ = Σ m_j³ = 2N, matching
  m₃(1) = 2 — i.e. **at λ = 1 the third moment does not separate the extremal world
  from the moment data either**.

The entire P6.5 question therefore reduces to: (a) what is m₃(1/2) really, and
(b) can any proven mechanism convert the λ = 1/2 third moment into N_d > 5N/6?

---

## 2. The third moment of the sine-kernel Gram matrix: m₃(λ) — the corrected computation

### 2.1 Definition and diagram

m_k(λ) = (1/N)·E tr(G^k) over the sine process, G_ij = sinc(πλ(x_i − x_j))
(the paper's §7.5(f) matrix [sin πλ(x_i−x_j)/π(x_i−x_j)] in the units where an
isolated simple zero has eigenvalue 1, i.e. diagonal entries 1). This is a
determinantal point process, so tr(G³) = Σ_{i,j,k} G_ij G_jk G_ki is evaluated by the
diagram/partition expansion (this is the "diagonal method" in the RS range 3λ < 2):

    m₃(λ) = 1 + 3·A2 + A3
    A2 = ∫ K(u)² (1 − S(u)²) du                       (pair partition, K = sinc(πλ·), S = sinc(π·))
    A3 = ∫∫ K(u)K(v)K(u+v) ρ₃(u,v) du dv,  ρ₃ = det[S(x_i−x_j)]_{3×3} = 1 − S(u)² − S(v)² − S(u+v)² + 2S(u)S(v)S(u+v)

### 2.2 Reduction (the correct closed form)

A3 = D − 3B + 2C where, by Fourier/convolution identities (all PROVEN here by hand
and checked numerically):
- D = ∫∫ K(u)K(v)K(u+v) du dv = **1/λ²**        [∫K̂(ξ)²K̂(−ξ)dξ with K̂ = (1/λ)1_{|·|<λ/2}]
- B = ∫∫ K(u)K(v)K(u+v) S(u)² du dv = ∫ K(u)S(u)²(K⋆K)(u)du, and (K⋆K)(u) = (1/λ)K(u) since K̂² = (1/λ)K̂,
  so **B = (2/λ)·J2**, J2(λ) = ∫₀^∞ sinc(πλu)²sinc(πu)²du
- C = ∫∫ K(u)K(v)K(u+v) S(u)S(v)S(u+v) du dv = ∫(K̂⋆Ŝ)³ dξ = **1 − λ/2** (λ ≤ 1) by explicit box convolution

so **m₃(λ) = 1 + 3(1/λ − 2J2) + 1/λ² − (6/λ)J2 + 2(1 − λ/2)**.

**Bug found in the inherited scripts** (`m3_check.py`, `m3_pin.py`, and the reduction
copied into `m3_twobandwidth.py`): they use B = 2·J3 with J3 = ∫₀^∞ sinc(πλu)³sinc(πu)²du
and D = 3/(4λ). Both are only correct at λ = 1 when K⋆K = K (box is an indicator);
in general B = (2/λ)J2 and D = 1/λ². Their consequence m₃(1) = 125/64 is WRONG.

### 2.3 Values (PROVEN — three independent verifications)

Using J2(1/2) = 5/12, J2(2/3) = 7/18, J2(1) = 1/3 (computed by mpmath 1D quadrature,
CHECKED NUMERICALLY; these exactly reproduce the sympy-verified m₂(λ) = 1/λ + λ/3):

| λ | m₂ | m₃ | 2m₂ − m₃ | exact? |
|---|---|---|---|---|
| 1/2 | 13/6 | **5** | −2/3 | m₃ exact = 5 |
| 2/3 | 31/18 | **13/4** | 7/36 | m₃ exact = 13/4 |
| 1 | 4/3 | **2** | 2/3 | matches paper's m₃(1) = 2 |

Verifications of the corrected reduction:
1. **Hand algebra** (above): D, B, C derived from Fourier/convolution identities;
   J2 values consistent with the paper's sympy-verified m₂.
2. **Tail-subtracted direct 2D quadrature** (numpy Gauss–Legendre; slow O(1/R) parts
   D and 2C added analytically, fast −3KKKS² part integrated directly):
   λ=1: m₃ = 2.0013; λ=1/2: m₃ = 5.0076 — converging to the closed forms
   (CHECKED NUMERICALLY).
3. **Actual ζ zeros** (flat-window Gram matrix on rescaled zero bands, 10⁴ zeros
   file): λ=1: m₂ ≈ 1.30, m₃ ≈ 1.90; λ=1/2: m₂ ≈ 2.13, m₃ ≈ 4.80. The uniform ~3%
   shortfall vs closed form is the known finite-height pair/triple-correlation
   deficit (same pattern as the paper's own §8 table: C/N ≈ 0.744 vs 0.750 at
   moderate height). **The empirical λ=1/2 third moment is unambiguously ≈ 5, not 2**
   (CHECKED NUMERICALLY).

**Consequence:** the task's joint-certificate input m₃(1/2) = 2 is REFUTED; the
correct input is m₃(1/2) = 5. The paper's m₃(1) = 2 is CONFIRMED, so §7.5(f,g) values
stand (the parallel agent's 125/64 must be retracted — see §6).

---

## 3. The LP: can the third moment move N_d?

### 3.1 The literal LP (task's stated moments 1, 4/3, 2 + integrality)

Minimize N_d over configurations with the three moments + integer multiplicities +
the c = 3 (distinct) bookkeeping. Answer (PROVEN): **the LP optimum is exactly 5/6.**

- Upper side: the extremal world — a₁ = 2N/3 simple + a₂ = N/6 double on-line zeros,
  mutually orthogonal atoms (Gram = diag(m) at window A) — is feasible: its moments
  are (tr, tr², tr³) = (N, 4N/3, 2N) and N_d = 5N/6 (PROVEN, attack-multiplicity §1,
  lemmaR_tight). So the feasible set contains a point with N_d = 5N/6: optimum ≤ 5/6.
- Lower side: the c = 3 certificate (Thm C, PROVEN) gives N_d ≥ (6 − 4/3 − 3)N/2 =
  5N/6 for every configuration with (tr, tr²) = (N, 4N/3), in particular for the LP's
  feasible set: optimum ≥ 5/6.
- Hence optimum = 5/6 exactly. **The third moment (value 2) does not move N_d at all
  in this LP.** This is the clean negative the task asked for, and it is *exactly the
  situation the paper's §7.5(g) already encodes*: the cubic construction with flat
  moments (1, 4/3, 2) returns exactly 5/6.

### 3.2 The LP with the corrected λ = 1/2 value (m₃ = 5), single window

The only proven third-moment mechanism for N_d is the paper's admissible-cubic
construction (§7.5(g); PROVEN at λ = 1, template valid where the Schur–Horn
admissibility step transfers):
N_d ≥ (1/2 + (2m₂ − m₃)/18)·N + (4/9)·s₁, with s₁ ≥ 2N/3 unconditional (Thm B).

Evaluations (arithmetic PROVEN; the transfer of the admissible-cubic step to λ < 1 is
the paper's mechanism — CONJECTURED transfer, see §3.3):

| window | 2m₂ − m₃ | bound | vs 5/6 |
|---|---|---|---|
| λ = 1   (conditional input) | +2/3   | **5/6**     | =  |
| λ = 2/3 (unconditional, RS boundary) | +7/36  | **0.8071** | < |
| λ = 1/2 (unconditional) | −2/3   | **0.7593 = 41/54** | < |
| joint formal mix 2m₂(1)−m₃(1/2) | −7/3  | 2/3        | < |

Exceeding 5/6 via this construction requires 2m₂(λ) − m₃(λ) > 2/3; the computed
curve is −2/3 (λ=1/2), −0.044 (λ=0.6), +7/36 (λ=2/3), +2/3 (λ=1) — increasing and
reaching 2/3 only at λ = 1 (CHECKED NUMERICALLY on [1/2, 2/3]; the exact values at
the three named windows are PROVEN). Since the third moment is unconditionally
available only for λ < 2/3, **no unconditional window can beat 5/6 through the cubic
construction**; the maximum in the unconditional range is 0.8071 at λ = 2/3(1−ε).

### 3.3 Why a "richer joint constraint set" cannot be converted into a bound

The joint data is (window A: tr Â_A = N, tr Â_A² = 4N/3; window B: tr Â_B = N,
tr Â_B² = 13N/6, tr Â_B³ = 5N) on the SAME configuration (same multiplicities, same
off-line pairs). The obstacle (PROVEN by LP-structure analysis):

- Every proven mechanism that converts moments into an N_d lower bound goes through
  (i) the c = 3 rank–trace inequality at a single window, and (ii) a Schur–Horn-type
  step Σ_j g(m_j) ≥ α tr H + β tr H² + γ tr H³ for H = M^{1/2}ΓM^{1/2} — which requires
  the three trace moments of the SAME matrix H. Window A's tr Â_A² and window B's
  tr Â_B³ are moments of *different* matrices; there is no matrix whose trace moments
  are both. A mixed-window inequality would be a new theorem, and it is not in the
  sources.
- The general cubic-weight LP without the Schur–Horn admissibility constraint is
  **unbounded** (CHECKED NUMERICALLY, HiGHS: status Unbounded): with the m³
  coefficient → −∞, the constraints ψ(m) ≤ 1 free the m and m² coefficients, and the
  objective diverges. The admissibility constraint (concavity of βx²+γx³ over the
  eigenvalue range) is what bounds the LP — it is exactly the structure the paper's
  "admissible cubic (boundary case β = −2γ)" encodes, and it does not survive mixing
  windows. This is a documented explanation of *why* "add the third moment to the
  LP" is vacuous without the admissibility structure.
- Even granting the extremal world fails window B: the certificate must hold for all
  configurations with the joint data, and nothing proves that no N_d = 5N/6
  configuration matches both windows. The bookkeeping-level bounds that ARE valid
  (tr Â_B² ≥ Σ m_j²·block-factor, tr Â_B³ ≥ Σ m_j³ for the multiplicity diagonal) do
  not exclude the extremal world: Σ m_j² = 4N/3 < 13N/6 and Σ m_j³ = 2N < 5N, both
  consistent.

### 3.4 Extremal world vs window B (numerics)

The extremal world is not fully specified as a point configuration (it is defined by
its window-A Gram structure); its window-B moments are therefore construction-
dependent. On the natural proxy — atoms at integer-spaced ordinates (sinc(πk) = 0
gives window-A orthogonality), a₁ simples + a₂ doubles — the window-B moments are
(CHECKED NUMERICALLY, numpy):
- tr Â_B²/N ≈ 2.33 (real config: 13/6 = 2.167) — differs by ≈ 7%;
- tr Â_B³/N ≈ 3.97 on the all-simple lattice (sine-process closed form 5.0) — differs
  by ≈ 21% at that proxy.

So window B *does* distinguish the natural extremal-world proxy from reality at the
moment level. **This is not usable**: distinguishing is not bounding, and the
conversion step is precisely the missing cross-window inequality (§3.3). The honest
statement: whether any N_d = 5N/6 configuration matches the full joint data is OPEN
(a construction question), but no proven mechanism turns the joint data into a
stronger bound, so the certificate stays at 5/6.

---

## 4. Verdict

**P6.5 does not break the 5/6 distinct wall.**

- The task's input m₃(1/2) = 2 is REFUTED; the diagonal method gives m₃(1/2) = 5
  (PROVEN, verified three ways, empirically consistent with ζ zeros).
- With corrected moments the λ = 1/2 third moment is *harmful* to the only proven
  cubic mechanism (2m₂ − m₃ = −2/3); the best unconditional cubic bound is
  0.8071 at λ = 2/3, below 5/6.
- The joint two-bandwidth constraint set is strictly richer as *data*, but no
  cross-window inequality exists to convert that data into an N_d bound; every
  provable route returns max(5/6, ≤ 0.81) = 5/6.
- The literal LP the task described (moments 1, 4/3, 2 + integrality) has optimum
  exactly 5/6 — the extremal world is feasible with equality (clean negative,
  PROVEN).

W-P5's sign prediction ("the two-loop term raises the distinct bound") is therefore
NOT supported by the computation in the regime where it can be checked
unconditionally; the third-moment term is negative for λ = 1/2 and only becomes
positive for λ > ~0.57, and it never lifts the bound above 5/6 for any λ < 2/3
(CHECKED NUMERICALLY).

---

## 5. What remains open / would change the verdict

1. **The extremal world's window-B moments** (OPEN, construction question): if a
   rigorous construction shows no N_d = 5N/6 configuration can match (13/6, 5), a
   *new* cross-window inequality might still be provable — but that is a new theorem,
   not the LP probe, and no such inequality is in hand.
2. **The admissibility of the paper's cubic at λ < 1** (OPEN): the 0.8071 (λ = 2/3)
   and 0.7593 (λ = 1/2) figures assume the §7.5(g) Schur–Horn step transfers. If it
   fails at λ < 1 the window-B construction is even weaker; either way ≤ 5/6.
3. **m₄(λ) and the full roadmap**: the paper's m₄(1) = 13/4 (used in the
   HL*(4, λ) → 13/18 roadmap) should be re-verified with the corrected reduction
   (the 3D diagram integral; not done here — recommend for the parallel agent).
4. **Beyond-bandwidth-1 inputs** (M29) remain the only documented route past 5/6
   (attack-multiplicity §4; attack-vector-catalog §5): the P6.5 probe closes the
   third-moment-in-bandwidth-1 avenue with a documented negative.

---

## 6. Note for the parallel agent (single-window third moment, attack-thirdmoment.md)

`tools/m3_check.py` / `m3_pin.py` / `m3_twobandwidth.py` contain a closed-form bug
that produces m₃(1) = 125/64 ≈ 1.9531 instead of the correct 2 (the paper's value).
The bug: in the A3 reduction, B = ∫∫K(u)K(v)K(u+v)S(u)² dudv is not 2·J3; since
(K⋆K)(u) = (1/λ)K(u), B = (2/λ)·J2(λ); and D = ∫∫K(u)K(v)K(u+v) dudv = 1/λ², not
3/(4λ). Correct reduction:

    A3(λ) = 1/λ² − (6/λ)·J2(λ) + 2(1 − λ/2),   J2(λ) = ∫₀^∞ sinc(πλu)²sinc(πu)²du
    m₃(λ) = 1 + 3(1/λ − 2J2) + A3(λ)

giving m₃(1) = 2, m₃(2/3) = 13/4, m₃(1/2) = 5 (all verified: hand algebra +
tail-subtracted direct 2D quadrature + ζ-zero empirics). This means the single-window
λ = 2/3 third-moment route (V3) has 2m₂ − m₃ = 7/36 > 0 — the cubic construction
gives 0.8071 < 5/6 there — i.e. the single-window route also cannot beat 5/6
unconditionally. The paper's §7.5(g) 0.85082 figure (under RH, window-dependent
moments, s₁ ≥ 19/27) is unaffected by this correction.

---

## Label summary

- PROVEN (derived here): m₃(λ) closed form; m₃(1) = 2, m₃(1/2) = 5, m₃(2/3) = 13/4;
  ψ* evaluations (arithmetic); literal-LP optimum = 5/6; no cross-window inequality
  in the proven machinery; unconstrained cubic LP is unbounded.
- REFUTED: task's m₃(1/2) = 2; parallel agent's m₃(1) = 125/64 (script bug).
- CHECKED NUMERICALLY: J2 values; tail-subtracted direct 2D quadrature; ζ-zero
  moments (m₂ ≈ 1.30/2.13, m₃ ≈ 1.90/4.80 vs 4/3/13/6 and 2/5); extremal-world
  lattice proxy window-B moments (2.33, 3.97); 2m₂−m₃ curve on [1/2, 2/3]; LP
  unboundedness (HiGHS).
- CONJECTURED: transfer of the paper's admissible-cubic/Schur–Horn step to λ < 1
  (does not affect the verdict: the bound is an upper bound on achievability and is
  < 5/6 regardless); that no N_d = 5N/6 configuration matches the full joint data
  (OPEN).
- VERDICT: P6.5 = documented negative. The 5/6 distinct wall stands. Beyond-1 inputs
  (M29) remain the only documented route.
