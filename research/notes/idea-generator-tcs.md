# Idea Generator: Theoretical Computer Science attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (TCS angle). Round 3.
**Purpose:** feed the EXECUTIONER agents. This pool (algorithms / complexity / sketching / property
testing / coding / mechanism design) was **largely unmined** — the ML-eco catalog covered ML spectral
methods, not algorithms/complexity. Every vector is concrete enough to attack, and every numeric claim
is produced by code (probe: `research/notes/idea-generator-tcs-probe.py`, command in §0.3).
**Honesty protocol:** no new theorems are asserted here. Facts are labeled **PROVEN** (Lean / paper /
cited attack note), **CHECKED NUMERICALLY** (our own tools), or **CONJECTURED by construction** (every
invented vector carries a kill criterion). Nothing from the TCS literature is cited from memory as a
theorem without the "standard in the field — verify before citing" caveat.
**Cross-references:** crossdomain = `idea-generator-crossdomain.md` [CD-V#]/[CD-W#]/[CD-A#]; physics =
`idea-generator-physics.md` [P#.#]; ml-eco = `idea-generator-ml-eco.md` [M#]/[E#]/[G#]/[S#]/[B#].
Wall state: attack-lpdual [ALP], attack-qi-sweep [QS], attack-twobandwidth [TB], attack-m29 [M29],
attack-gm-variance [GM], attack-mvconstant [MVC], attack-nevanlinna [NV], attack-finitet [AF],
attack-ceiling [AC], attack-kernel [AK], attack-multiplicity [AM].

---

## 0. The state these vectors must respect (all PROVEN / CHECKED NUMERICALLY — do not re-derive)

1. **The method and its constants.** Two-moment certificate: `tr W_T = N`, `‖W_T‖²_HS = 1.327499…·N`,
   rank–trace (Lemma 3.2) gives `s₁ ≥ 0.67250·N` (Theorem D); 2/3 flat, 5/6 distinct, 0.83625 distinct
   (optimal window). [AK], [AM]
2. **The in-class gap is CLOSED.** The bandwidth-one ceiling `0.681828687…` is PROVEN in Lean [AC]; the
   class-optimal certificate `0.68183123 = p₀ + |E(1)|` is exact and the ceiling is TIGHT [ALP]. **No
   bandwidth-one datum moves the real-zeros constant; the shadow price of p₁ is exactly 1** [ALP §3–4].
3. **No matrix inequality beats rank–trace on (1,1)-blocks.** The strongest candidate (Cauchy–Schwarz on
   Q₊, `(trQ₊−2b)²/b`) provably dominates Lemma 3.2 term-by-term yet vanishes at the sharp
   configurations — no uniform gain [QS]. (QI sweep closed; the CS refinement's gain is exactly the
   conditional quantity a repulsion input would unlock.)
4. **Beyond-1 form factor is PROVEN DEAD** (mean side): the Montgomery–Vaughan bound is 3.6·10³–3.7·10⁴×
   too weak at T = 10⁴–10⁶; every other proven bound is equal or worse; only conjectural
   Hardy–Littlewood / pair-correlation *values* would clear the tolerance [M29]. **Dead from the variance
   side too**: no unconditional variance statement reaches α > 1 with content (Selberg global; Fujii
   U ≤ 1 in-band; the β > 1 asymptotic is *equivalent to the pair-correlation conjecture*), and a
   variance statement is orthogonal to the mean-based certificate ("variance" = 0 hits in the paper)
   [GM].
5. **The third moment is cheap talk for the distinct wall.** m₃(1/2) = 5 (corrected; the task's 2 was
   REFUTED), `2m₂ − m₃ = −2/3` at λ = 1/2, best unconditional cubic bound 0.8071 at λ = 2/3 < 5/6; the
   literal LP optimum is exactly 5/6; no cross-window inequality converts joint two-bandwidth data into
   an N_d bound [TB].
6. **Other closed doors.** MV-constant sharpening has zero effect on 0.6725 (the MV step is
   window-independent and enters only an o(1) error) [MVC]. The Nevanlinna reframe of P1 is a
   documented negative (integrality is exactly what *permits* p₁ > 2/3; closing the gap needs
   m₂ ≥ 1.3275 on near-CUE integer-marked configs = beyond-1 arithmetic) [NV].
7. **The open problems this catalog can touch.** (P5) derivative tower — ξ′ constants PROVEN
   (0.858/0.868), ξ″/ξ‴ mechanical extension open [CD-V9]; (P6) finite-T effective theorem — Δ(T) ~
   1/log T measured, effective E(T) open [AF], [CD-V20]; (P7-diagnostics) the method's real slack —
   the diagnostics agenda [M1–S4]; and the *input* questions (P1–P3) — all currently documented shut
   except repulsion-type inputs (KNOWN-OPEN, [CD-V17]) and the **unconditional fourth moment in the
   Rudnick–Sarnak range, which this file opens as a new, provable-input arithmetic question** (§Pool 1,
   TCS-P1-4, probe run).
8. `attack-hankel-test.md` does **not** exist in `research/notes/` (checked); the closest prior work is
   the Nevanlinna/Hankel analysis [NV] and the physics Hankel-diagnostic [CD-W3] (not executed).

### 0.3 The code-backed probe (this session)

Script: `research/notes/idea-generator-tcs-probe.py` (final; run from `/tmp/tcs_probe.py`).
Command: `cd /home/vstaln/riemann && uv run --with numpy python /tmp/tcs_probe.py`
Data: `tools/data/zeros_computed_10000.txt` (10⁴ zeros, γ ∈ [14.135, 9879.037]).
Output (all **CHECKED NUMERICALLY**):

**(A) Empirical Gram-matrix moments, flat window (local mean-spacing rescale):**

| band | λ | m₁ | m₂ (exp) | m₃ (exp) | **m₄** | 2m₃−m₄ |
|---|---|---|---|---|---|---|
| 9000–9880 (n=1024) | 1 | 1.0000 | 1.3029 (4/3) | 1.8972 (2) | **2.9750** | +0.8193 |
| 9000–9880 | 1/2 | 1.0000 | 2.1341 (13/6) | 4.8020 (5) | **11.2599** | **−1.6558** |
| 5000–7000 (n=2183) | 1 | 1.0000 | 1.3013 | 1.8929 | **2.9659** | +0.8198 |
| 5000–7000 | 1/2 | 1.0000 | 2.1349 | 4.8017 | **11.2471** | **−1.6437** |
| 2000–4000 (n=1957) | 1 | 1.0000 | 1.2969 | 1.8762 | **2.9203** | +0.8320 |
| 2000–4000 | 1/2 | 1.0000 | 2.1346 | 4.7992 | **11.2348** | **−1.6363** |

Reading: m₄(1/2) ≈ **11.25** (first estimate anywhere; uniform across bands). The finite-height deficit
grows with moment order (m₂ −2.3%, m₃ −5%, m₄ ≈ −8.5% vs closed forms at λ = 1), so the closed-form
m₄(1/2) is plausibly ≈ 12.2–12.5, and **2m₃ − m₄ is robustly ≈ −1.6 to −2.3 < 0 at λ = 1/2** — i.e. the
quartic's marginal term is *negative* in the unconditional range (compare the cubic's `2m₂ − m₃` = +2/3
at λ = 1, +7/36 at λ = 2/3, −2/3 at λ = 1/2 [TB]). At λ = 1 (RH-conditional) the empirical combination is
**+0.82** (closed form `2·2 − 13/4 = +0.75` if m₄(1) = 13/4 stands) — positive, larger than the cubic's
2/3.

**(B) Sample complexity of the count-variance test (real zeros vs 256-law):**
V_zeros(one-spacing window) = 0.315 (measured, [GM] §5), V_crystal = O(1/L) ≈ 0; resolving the gap at
95% confidence needs **M ≈ 18 independent windows** → **a few hundred zeros suffice to separate the two
worlds by variance**. The obstruction to using this is *not* sample count — it is that the certificate
class reads means only (per-T), never fluctuation statistics [GM §4].

---

## Pool 1 — Spectral algorithms: sparsification, Laplacian solvers, polynomial filters

### TCS-P1-1 Spectral sparsification of W_T — does it preserve the certificate? — KNOWN-DEAD (derived here)
**Idea:** Spielman–Teng-style: replace the dense W_T by a sparse W̃ with (1−ε)W_T ⪯ W̃ ⪯ (1+ε)W_T and
check whether the inertia/rank–trace certificate survives.
**Analogy:** spectral approximation of quadratic forms ↔ the dense Weil-form compression.
**Why it dies (derived here):** (i) spectral approximation preserves *Rayleigh quotients*, not *inertia*
— small perturbations can flip signs of near-null eigenvalues, and W_T is numerically near-rank-deficient
(exactly where inertia is unstable [AF §3]); (ii) the certificate's value is a function of the *exact*
two moments (atoms 1 and 2 of the extremal law saturate it — [QS] TEST E), and an ε-perturbed W̃ moves
the value by ε·N against an in-class gap of 1.4% — any ε ≥ 10⁻³ kills it; (iii) the premise is empty: W_T
is a *symbol* (analytically evaluable moments), not a data matrix — there is no computational cost to
sparsify away. **Verdict:** no new input; the *question* "does a random-sampled W̃ preserve n₊ at finite T"
is a diagnostic at best (overlaps [M3]/[S4]'s inertia-stability budget).
**Cheapest probe:** none needed (framing argument); record in the attack log.

### TCS-P1-2 Laplacian linear-system solvers / resolvent — KNOWN-OPEN (covered by [P1.1])
**Idea:** the kernel operator (I + T) with |u−v| has an explicit differential inverse (Sturm–Liouville,
2nd derivative + BCs — [AK]'s particle-in-a-box); the finite-rank compression's resolvent
tr(W_T − zI)^{-1} is the Stieltjes transform of the eigenvalue law.
**Why nothing new:** [P1.1] already established that the resolvent at bandwidth one is *determined* by the
moment sequence (continued fraction) — the resolvent route reduces to the moment problem; the cosine
window being the ground state of the kernel's variational problem is already PROVEN [AK]. Laplacian-solver
technology is about *fast solves*, a computational question this program does not have (everything is
exact/analytic).
**Verdict:** KNOWN-OPEN as a *route*, no new provable fragment; do not fund beyond [P1.1]'s probe.
**Cheapest probe:** [P1.1]'s resolvent probe (W_T at T=200–600, grid of complex z).

### TCS-P1-3 The certificate class is a degree-2 SoS / Lasserre relaxation; 0.6818 is its integrality gap — NEW (framing, explanatory)
**Idea:** The certificate reads only two moments + integrality of marks: that is precisely a
degree-2 (psd-moment) relaxation of the integer-constrained configuration problem, and the extremal
256-law is the *integrality gap* witness: the LP/relaxation optimum (0.6818 certified simple fraction)
vs the integer truth (1.0) has gap 0.318. In TCS terms: **the ceiling theorem is the integrality-gap
analysis of the degree-2 relaxation of an integer program.**
**Why it explains the twobandwidth failure:** [TB] §3.3 found the third-moment LP is *unbounded without an
admissibility constraint*, and the admissibility condition (concavity of βx²+γx³ over the eigenvalue
range) is exactly the SoS/psd condition that a higher-degree Lasserre round would impose — the "admissible
cubic" of §7.5(g) IS a degree-3 SoS valid inequality. So the third-moment route died for a *named* reason
in the SoS hierarchy: valid inequalities beyond degree 2 need the psd/admissibility structure, and the
structure only yields value where the moments are (conjecturally) available.
**Needs:** none (re-reads [TB]'s LP analysis through the SoS lens).
**Feasibility:** immediate (documentation). Value: unifies [QS], [TB], [ALP] under one framework and
predicts that *every* higher-moment attack faces the same admissibility wall — only *new arithmetic
inputs* (not new inequalities) can move the constant. **Cheapest probe:** none (documentation).

### TCS-P1-4 Chebyshev / Markov–Chebyshev polynomial-filter route: the UNCONDITIONAL fourth moment m₄(λ) at λ < 1/2 — NEW (probe RUN; the one genuinely new proven-input arithmetic question in this file)
**Idea:** In polynomial-filter / Markov–Chebyshev theory, the degree-d optimal count bound for eigenvalues
in an interval given d moments is the Markov–Chebyshev extremal polynomial; the certificate value
`2tr − ‖·‖²` is exactly the degree-2 instance. The paper's own Remark (one-sided Chebyshev, line 2316)
flags a **4th-moment** bound as the natural next input, and its HL*(4,λ) → 13/18 roadmap [AM §7.5(f)] is
the *conjectural* version. **The new fact this file opens: by the Rudnick–Sarnak diagonal method, the
fourth moment is *unconditionally evaluable* for λ < 1/2 (kλ < 2, the same range that made m₃
unconditional at λ < 2/3 [TB]) — m₄(λ) at λ < 1/2 is a PROVEN-INPUT arithmetic object, never computed in
any prior note.** Value: (a) closes the question "does any higher-moment RS-range input help the distinct
wall" definitively; (b) delivers the m₄(1) = 13/4 re-verification with the corrected reduction (flagged
open in [TB] §5.3).
**Probe result (RUN, §0.3):** empirical m₄(1/2) ≈ 11.25 (first estimate), and the quartic-feasibility
combination `2m₃ − m₄ ≈ −1.6…−2.3 < 0` at λ = 1/2 — **the quartic's marginal term is strongly negative in
the unconditional range, so the admissible-quartic distinct construction CANNOT beat the cubic
(which already fails to beat 5/6 at every λ < 2/3 [TB])**. The RS-range higher-moment route for the
distinct wall is therefore a *probable documented negative* (modulo the exact 3D closed form, whose sign
is already robustly pinned by the data). At λ = 1 (RH-conditional) the combination is +0.75 (closed form
if m₄(1) = 13/4) — positive, so a quartic *under RH* would improve on the cubic's flat-moment 5/6; but
that regime is already priced by the paper's §7.5(g) 0.85082 (with s₁ ≥ 19/27).
**What it needs:** the exact closed form m₄(λ) (3D diagram integral over the 4-point Slater determinant —
the same machinery as the verified m₃ computation [TB §2], one order higher), then the admissible-quartic
N_d bound evaluation.
**Feasibility:** Med (the empirical sign check was <1h and is done; the exact 3D integral is a real but
mechanical computation). **Cheapest probe (DONE):** empirical m₄ from the 10⁴-zeros cache (§0.3).
**Kill:** if the closed form confirms 2m₃−m₄ < 0 for all λ < 1/2 (expected), the RS-range quartic route is
a clean negative — document; the m₄(1) = 13/4 verification is still a deliverable.

### TCS-P1-5 Polynomial-filter *counting* interpretation of the certificate — NEW (framing, folds into P1-4)
**Idea:** the rank–trace certificate `rank(W_on) ≥ 2tr − ‖·‖²` is a polynomial-filter count bound of degree
2 on the eigenvalue law (Chebyshev-type majorant on [θ, ∞)); the LP-dual certificate r ≈ 1−x [ALP] is the
optimal *majorant function* — the same object as Cohn–Elkies/Delsarte majorants (see Pool 5). The
identification predicts: the next term in the hierarchy is the degree-4 Markov–Chebyshev bound = P1-4.
**Needs:** none (documentation). **Feasibility:** immediate. **Cheapest probe:** none.

### TCS-P1-6 Eigenvalue-free inertia (LDLᵀ / rank-revealing) as certificate hygiene — KNOWN-DEAD as input; hygiene overlaps [M3]/[S4]
**Idea:** compute n₊(W_T) by exact/integer-preserving LDLᵀ rather than dense diagonalization.
**Verdict:** a numerics-hygiene point already covered by [M3] (inertia-stability/tail budget) and [S4]
(thresholding); no mathematical input. Do not re-fund. **Cheapest probe:** none.

---

## Pool 2 — Sketching / streaming: AMS moments, count-sketch, heavy hitters

### TCS-P2-1 AMS moment-estimation view of the m₂/m₃/m₄ *measurements* — NEW (diagnostic, P7)
**Idea:** Alon–Matias–Szegedy: higher stream moments are estimable but with worse relative variance, and
odd moments are structurally harder than even ones. Our m₁, m₂, m₃, m₄ of the zero configuration ARE
stream moments of the "zero stream"; the certificate uses m₁, m₂; the twobandwidth program *measured*
m₃ (empirical 4.80 vs closed form 5.0 [TB]) and now m₄ (§0.3, 11.25 vs ~12.3 extrapolated). The AMS
insight maps onto a **reliability statement**: the finite-height deficit grows with moment order (measured
here: m₂ −2.3%, m₃ −5%, m₄ −8.5% at λ = 1) — i.e. higher-moment *measurements* are systematically biased
at fixed height, so any diagnostic that prices higher moments must carry the order-dependent deficit as an
error bar. This is the quantitative form of "why the third/fourth moment data is weak evidence" for
P7-diagnostics.
**Needs:** the measured deficit curve (already in §0.3); a short note formalizing the order-dependent
error bar for the m₃/m₄ empirics used elsewhere.
**Feasibility:** Low (mostly done; a write-up + one variance-over-bands computation).
**Cheapest probe (<1h):** extend §0.3's script: report the *spread* of m₄ across the three bands (already
tight: 11.235–11.260) and the deficit trend with k — the honest error bar for every higher-moment claim.

### TCS-P2-2 Count-sketch / Johnson–Lindenstrauss for the spectral norm — KNOWN-DEAD (derived here)
**Idea:** estimate ‖W_T‖² by random projection.
**Why it dies:** ‖·‖² is *evaluated analytically* from the prime side (the paper's Prop 5.6); a sketch
would estimate a number we already compute exactly, and an estimate is not a proof — the certificate needs
a *bound*. No new input. **Cheapest probe:** none.

### TCS-P2-3 Heavy hitters / resolution limit of the sketch — KNOWN-DEAD (covered by [P6.2]/[P6.3])
**Idea:** off-line pairs at shallow depth are "heavy hitters below the sketch's resolution"; the λ ≤ 1 wall
is a resolution (uncertainty) bound of the two-moment sketch.
**Verdict:** this is physics P6.2 (compressed-sensing undersampling = the dimension cap) and P6.3
(local uncertainty = [CD-A3]) already — reframing only, no new input. **Cheapest probe:** none.

### TCS-P2-4 The certificate as a 2-dimensional linear sketch; the M-row curve as its measurement complexity — NEW (framing; numbers from [ALP])
**Idea:** the certificate reads exactly two linear measurements (tr, ‖·‖²) of the infinite zero
configuration; streaming theory asks: what is the minimum sketch that *distinguishes* two streams? The
row-sweep in [ALP] §3 (LP-B′) is precisely this curve: a certificate valid against the first M cells of
the near-CUE law pins v(M): M=1 → 0.890, M=64 → 0.862, M=128 → 0.794, M=192 → 0.718, M=240 → 0.684,
M=255 → 0.68183. **The quantitative statement: pinning the certificate to 0.70 requires ≈ 192 in-band
measurements of the law's mass profile; pinning to the ceiling requires all 255 — and none of these are
available as proven *arithmetic* inputs (they are configuration data the certificate never sees).** This
is the streaming-theory face of the M29 wall: the sketch's information content is in-band and finite, and
it is *already exhausted*.
**Needs:** none (re-reads [ALP]'s LP-B′ table). **Feasibility:** immediate (documentation).
**Cheapest probe:** none.

### TCS-P2-5 Turnstile / tug-of-war: even moments robust, odd moments hard — NEW (framing; matches §7.5(e))
**Idea:** in streaming, the AMS/tug-of-war estimators for *even* moments have small-variance unbiased
estimators, while *odd* moments need different machinery and are less stable. The paper's §7.5(e)
"odd moments don't lower Λ₁(0)" is the analytic twin: the certificate's on-line functional is even-only.
**Needs:** none. **Feasibility:** immediate (documentation). Value: stops re-derivation of "odd-moment
inputs" for the on-line functional (already proven useless [TB §0, §7.5(e)]); the *distinct* functional
is the only odd-moment target and it is dead at λ < 2/3 [TB]. **Cheapest probe:** none.

---

## Pool 3 — Property testing / distribution testing

### TCS-P3-1 Sample complexity of separating the real zeros from the 256-law — NEW (probe RUN)
**Idea:** the certificate-vs-extremal-law question IS a property test: distinguish the real zero process
from the 256-periodic crystal. The distinguishing statistic is the *count variance* over windows (0 for
the crystal at scale ≫ 256, ≈ 0.31 for the zeros at one-spacing windows, measured [GM §5]). The new
quantitative statement (RUN, §0.3): **resolving the gap at 95% confidence needs M ≈ 18 independent
windows — a few hundred zeros suffice.** The two worlds are *easily* separable in principle; the
obstruction is **not sample count but certificate-feasibility**: the certificate class reads means only,
per-T, and provably cannot read fluctuation statistics (orthogonality, [GM §4]; "variance" = 0 hits in
the paper). This sharpens P7-diagnostics: the method's slack is real in the statistical sense, and the
*mean-based class* is the bottleneck — consistent with the sandbox expectation (G1).
**Needs:** none beyond the [GM] data and the arithmetic in §0.3.
**Feasibility:** Low (done). **Cheapest probe (DONE):** §0.3(B).
**Kill criterion:** none needed — it is a completed measurement; the framing conclusion (class, not
samples) is the deliverable.

### TCS-P3-2 The certificate is a *distribution-free* tester; the 256-law is its adversarial hard instance — NEW (framing)
**Idea:** property-testing distinguishes *distribution-free* testers (guarantee for all inputs) from
*known-distribution* testers (easier). The certificate is distribution-free: it must hold for *every*
configuration consistent with the two moments. The 256-law is exactly the worst-case instance that
distribution-freeness forces (like the standard lower-bound instances in property testing). The lesson:
**distribution-free guarantees are limited by adversarial instances even when all *samples* (empirical
zeros) look perfect — the empirical near-perfectness of the 10¹³ verified zeros cannot be exploited by a
distribution-free certificate.** This is the property-testing face of [ALP]'s "no missing constraint".
**Needs:** none (documentation). **Feasibility:** immediate. **Cheapest probe:** none.

### TCS-P3-3 Average-case vs pointwise: Montgomery's theorem is an *averaged* tester; the certificate needs pointwise — NEW (framing)
**Idea:** B24's F(α) ≈ 1 on [0,1] is an average over T (with smoothing); the certificate converts it into a
per-T bound up to o(1) — a *derandomization of the average* (the o(1) is the cost). The wall is exactly
the gap between averaged and pointwise *second* moments (absorbed by o(1)) and between averaged and
pointwise *higher* moments (the entire M29 obstruction). Property-testing's "average to worst-case" gap is
the same phenomenon: the certificate's hardness is pointwise validity.
**Needs:** none (documentation). **Feasibility:** immediate. **Cheapest probe:** none.

### TCS-P3-4 Identity testing of the zero process against the sine-kernel process — KNOWN-DEAD as certificate input (orthogonality, [GM])
**Idea:** identity-test the zero process against GUE's sine-kernel process with few samples.
**Verdict:** the distinguishing statistic is the pair correlation / count variance — a fluctuation object
[GM §4]; any use inside a certificate is blocked by orthogonality (means-only). The *empirical* identity
test (does the real data match the sine kernel) is [VER] §4's F(α) measurement and [GM] §5's variance
measurement — already done. **Cheapest probe:** none (already measured).

### TCS-P3-5 Tolerant testing: the empirical *distance to the crystal* — NEW (diagnostic)
**Idea:** tolerant testing measures how far a distribution is from a family, not just "equals or not". The
empirical *distance* between the real zero process and the nearest 256-periodic marked law — e.g. the
ℓ₂ mismatch of the 2-point statistics over in-band scales, or the count-variance deficit — is a measurable
"closeness to crystal" diagnostic. If the real world is far (expected: variance 0.31 vs 0; spacing
statistics GUE-like [E3/M5]-style), the crystal is a *purely adversarial* construct, not a plausible model
of reality — strengthening the P7 narrative ("the method's deficit is a proof artifact"). It cannot enter
a certificate (orthogonality), but it changes what we believe about the slack.
**Needs:** the 2-point statistic over dyadic in-band scales (exists in [VER]/[G3] tooling); the crystal's
statistic (computable from the 256-law in [AC]'s Lean data).
**Feasibility:** Low. **Cheapest probe (<1h):** reuse [G3]'s dyadic-box count variance and compare with
the crystal's O(1/L) prediction vs the zeros' (1/π²)log L/L — one plot, existing machinery.

---

## Pool 4 — Complexity theory: natural proofs, derandomization, explicit constructions

### TCS-P4-1 The 0.6818 ceiling is a **natural-proofs-style barrier, and it is PROVEN** — NEW (framing; the strongest vector in this file)
**Idea (task's explicit question):** Razborov–Rudich: a proof technique that is *natural* (applies to all
inputs in a large class) + *useful* (would prove the target) must fail, because it would yield a
pseudorandom-function distinguisher. Map to our setting — the correspondence is exact, item by item:
- *Proof class* = certificates reading (mean density, F on [0,1], integrality) — precisely characterized;
- *Natural* = the certificate holds for every configuration in the class (distribution-free, [P3-2]);
- *Useful* = it would certify ≥ 0.6818 simple zeros for the real configuration;
- *Adversary* = the 256-periodic near-CUE law: **matches every datum the class reads** (mean 1, F ≡ 1 on
  [0,1] up to 10⁻⁴⁰, integer marks, spectral atoms {0,1,2} with 2/3:1/6:1/6) yet has only 68.18% simple
  zeros — a "pseudorandom object" for the bandwidth-one test class;
- *Barrier theorem* = the ceiling (PROVEN in Lean [AC], tight [ALP]).
**The notable point:** RR barriers are *conditional* (they need PRG-existence); our barrier is **a
theorem** — the 0.6818 ceiling is a provable natural-proofs-type impossibility for the certificate class.
The RR escape routes map 1:1 onto our roadmap: RR is circumvented by *non-natural / non-constructive*
inputs (algebraic methods); ours is circumvented only by *non-class inputs* — beyond-bandwidth-1 values
(M29), higher correlations (dead at λ < 1/2 per P1-4 probe), repulsion (KNOWN-OPEN), i.e. exactly the
documented exits. **This reframes the search: "find a non-natural input" rather than "find a better
certificate inside the class" — and explains WHY every in-class attack (QS, TB, MVC, NV) died.**
**Needs:** a one-page writeup; no new code (the pieces are Lean-proven + numerically verified).
**Feasibility:** immediate. **Cheapest probe:** none (documentation); the "barrier part" is PROVEN (Lean),
the "analogy" is CONJECTURED (framing) — labeled accordingly.

### TCS-P4-2 The 256-law as an *explicit construction*; does the barrier scale? — NEW (framing; overlaps [P4.1])
**Idea:** TCS prizes explicit, efficiently-checkable hard instances (expanders, PRGs). The 256-law is an
explicit, rationally-specified adversary for the certificate class. The explicit-construction question is
the *scalability* of the barrier: does a near-CUE marked law exist at N = 512, 1024, 2048 with the same
defect structure (physics [P4.1]'s thermodynamic-limit LP)? If the simple fraction converges to < 0.6818,
the ceiling *improves* (a real finding); if it stays ≥ 0.6818, the barrier is confirmed as scale-invariant
(like an expander family). Same probe as [P4.1] — one probe, two framings.
**Needs:** the exact-rational LP at N = 512 (exists in [AC]/[ALP] machinery).
**Feasibility:** Low–Med. **Cheapest probe (<1h):** LP at N = 512; compare the simple fraction with
p₀ = 0.681828687.

### TCS-P4-3 Derandomization: RH would BE the explicit derandomization of the pair-correlation average — NEW (framing)
**Idea:** the averaged Montgomery data (F ≡ 1 on [0,1]) is the "randomized" statement; a configuration
achieving it *pointwise* (the real zeros, if RH + PCC) is the "derandomized" one. Derandomization theory's
lesson — the gap between randomized and deterministic is bridged by explicit constructions (PRGs) — maps
onto: the zeros themselves would be the PRG for the bandwidth-one test class; and the ceiling says *no
certificate-class proof can distinguish* the real zeros from the 256-law PRG. Consistent with P4-1;
no new input. **Cheapest probe:** none.

### TCS-P4-4 Algebrization / relativization — KNOWN-DEAD (subsumed by P4-1)
**Idea:** relativization (proofs that work for any oracle) and algebrization (the algebraic escape).
**Verdict:** the certificate class is "relativized" to the moment data (it works for any configuration with
those moments) — the relativization barrier = the ceiling; the algebrization escape = non-class arithmetic
inputs. Same conclusion as P4-1 with no additional content; keep only as a pointer. **Cheapest probe:**
none.

### TCS-P4-5 Hardness-of-approximation / integrality-gap reading — NEW (framing; overlaps [P4.2])
**Idea:** the configuration LP (minimize the non-simple fraction subject to in-band data) has optimum
1 − p₀ = 0.31817 [ALP]; the certificate attains it. This is a textbook integrality-gap story: the LP
relaxation of a combinatorial (integer-marked) problem is *exactly solvable* (LP is poly-time) and its gap
to the integer truth (0%) is 31.8% — and the gap is *proven irreducible* by the certificate class. The
UGC-style lesson: hardness-of-approximation results are about *constraint* classes; ours says the
constraint class (two moments) is exactly what the adversary satisfies.
**Needs:** none (documentation). **Cheapest probe:** none.

---

## Pool 5 — Coding theory: Delsarte LP bounds, list decoding, lattices, expander codes

### TCS-P5-1 The certificate is the **Delsarte/Plotkin machinery**; the 256-law is the extremal code — NEW (framing, identification)
**Idea (task's "minimum distance = a spectral/rank statement"):** the certificate `rank ≥ 2tr − ‖·‖²` is a
Plotkin-type bound: the minimum "distance" (on-line content) is bounded from below by the two lowest
statistics of the weight distribution. The Delsarte LP bound (kissing numbers, sphere packing, error-
correcting codes) is the *same* LP-majorant family: majorant functions, positivity, contact-set
optimality. The 256-law is the Delsarte-optimal "code" (its mass profile saturates the LP). **The
identification confirms two things already established:** (i) the in-class closure (0.6725 → 0.6818) is
the correct, complete realization of the Delsarte/Cohn–Elkies-style program for this problem ([ALP]'s
certificate IS the Cohn–Elkies auxiliary function; [P5.1]/[P7.6] said the same from the physics side);
(ii) beating it requires *new packing constraints* (new arithmetic inputs), exactly as in Delsarte theory
where adding constraints (higher-order correlations) tightens the bound.
**Needs:** none (documentation). **Feasibility:** immediate. **Cheapest probe:** none.

### TCS-P5-2 List decoding / Johnson bound = lemmaR_tight — KNOWN-DEAD (framing)
**Idea:** list-decoding's Johnson bound bounds the list size from the average distance; the certificate's
`lemmaR_tight` (the diag(1,…,1,2,…,2) sharp configuration [QS]) is the Johnson-tight case.
**Verdict:** the analogy is exact but adds no theorem: Johnson-type bounds are tight for extremal codes,
which is precisely why the certificate cannot improve within its data. **Cheapest probe:** none.

### TCS-P5-3 Lattice cryptography: the Gaussian heuristic and the random-vs-structured lesson — NEW (framing; points at repulsion)
**Idea (task's "SVP/CVP as eigenvalue-adjacent"):** the Gaussian heuristic λ₁ ≈ √(n/2πe)·det^{1/n} is a
*mean-field* (low-moment) estimate of the shortest vector, and it fails precisely on *structured*
(algebraic) lattices — the same failure mode as the certificate on the 256-law. Lattice cryptography's
operational lesson: worst-case bounds over all lattices are either trivial (like Minkowski's theorem) or
hard; the interesting statements are either (a) worst-case (our ceiling, PROVEN) or (b) under a structured
assumption (our beyond-1 inputs, CONJECTURED). The one genuine pointer: the "shortest vector" of the zero
configuration is the *minimal gap* = repulsion, which remains the KNOWN-OPEN input that would break the
ceiling ([CD-V17], [P1.4]). No new input; the analogy's value is strategic clarity.
**Cheapest probe:** none (documentation).

### TCS-P5-4 Expander codes — KNOWN-DEAD (covered by [G3])
**Idea:** expander codes get minimum distance from the spectral gap; the expander-mixing lemma bounds
discrepancy.
**Verdict:** the zeros' "expansion" is the small-α form factor (F(0) = 0 = rigidity), and the
mixing/discrepancy statement is [G3]'s count-variance diagnostic — already catalogued, diagnostic only.
**Cheapest probe:** none (see [G3]).

### TCS-P5-5 Weight-enumerator / MacWilliams view of the two moments — NEW (framing)
**Idea:** the code's weight enumerator's first two derivatives at x = 1 are the mean and second moment —
exactly (tr, ‖·‖²); the certificate is a weight-enumerator bound. MacWilliams duality would say: the dual
"code" (the prime side!) has its own enumerator whose low moments are *also* evaluable — the two sides of
the explicit formula are a MacWilliams pair. Honest check: the prime-side low moments (ΣΛ², ΣΛ⁴) are
indeed what the paper evaluates (the D/O₁ bookkeeping), so the duality is already consumed by the method —
no new input. **Cheapest probe:** none.

### TCS-P5-6 Is the extremal law's mass profile {1/6, 2/3, 1/6} on {0,1,2} a known combinatorial object (two-distance set / code weight enumerator)? — NEW (curiosity; overlaps physics W-G1)
**Idea:** three-valued spectra with fixed masses are the objects of two-distance-set / strongly-regular /
Delsarte classification; if the (1/6, 2/3, 1/6) profile is realizable as a two-distance set, the crystal
has a known combinatorial home (a structural *explanation*); if not, it is a free construct and even less
forced. Diagnostic/knowledge value only (the LP is already solved [ALP] — no input changes).
**Feasibility:** Low. **Cheapest probe (<1h):** the two-distance-set existence criteria applied to masses
(2/3, 1/6) — a literature-scoped check + one small linear-algebra test.

---

## Pool 6 — Algorithmic game theory / mechanism design

### TCS-P6-1 VCG / duality: shadow price 1 is the market price of the missing datum — NEW (framing; numbers from [ALP])
**Idea (task's explicit prompt):** LP duals ARE prices; the shadow price of p₁ = 1 [ALP §3] is a
market-clearing statement: **one additional unit of certified simple fraction is worth exactly one unit of
certificate value — the missing datum's price is 1:1, and the other constraint prices are the duals
(validity row −1, box at r(0) −2.54·10⁻⁶ [ALP §4]).** Mechanism-design framing: the certificate is a
*truthful mechanism* (sound for every reported configuration, so no configuration has an incentive to
misreport); the 256-law is the truthful-revelation worst case; the ceiling is the mechanism's revenue
bound. The row-sweep curve v(M) [ALP §3] is the "price menu" of in-band information: M=1 → 0.890 down to
M=255 → 0.68183, with the middle rows (j ≈ 64–192) the most valuable individually (drop-row shadow prices
1.5–2·10⁻³ each [ALP §4]) — a ranking of the *information content* of each in-band cell that the
certificate can never buy (they are configuration data, not arithmetic inputs).
**Needs:** none (re-reads [ALP]'s dual table). **Feasibility:** immediate (documentation).
**Cheapest probe:** none.

### TCS-P6-2 "The bottleneck is arithmetic, not computation" — NEW (strategic; the highest-leverage reframing in this file)
**Idea:** computational hardness of equilibrium (Nash PPAD-hard, etc.) is irrelevant here: the certificate
optimization is an **LP (poly-time, solved exactly)** [ALP]; the configuration side is an LP; the
"hardness" lives entirely in the *input evaluations* (arithmetic: the moments). A clean strategic
statement: **every optimization in this program is easy; the rate-limiting step is mathematics (proven
vs conjectural prime-side evaluations), not compute.** Consequence: do not fund "more computation" or
"better algorithms" vectors (TCS-P1-1, TCS-P2-2 die here); fund arithmetic inputs and measurements that
change belief (the diagnostic agenda [M1–S4], P1-4's closed-form m₄).
**Feasibility:** immediate (documentation). **Cheapest probe:** none.

### TCS-P6-3 Hardness of equilibrium — KNOWN-DEAD (subsumed by P6-2)
**Idea:** Nash equilibrium is PPAD-hard, equilibrium computation is hard.
**Verdict:** our equilibrium problems are LPs (poly-time); there is no computational hardness to exploit
or avoid. Folded into P6-2. **Cheapest probe:** none.

### TCS-P6-4 Incentive-compatibility reading of the certificate — NEW (framing; content is [ALP])
**Idea:** the certificate is strategy-proof: a configuration "reporting" the two moments cannot improve its
certified value by lying, because the certificate holds for all reports with those moments. The
revelation principle's lesson — the mechanism's power is bounded by what reports can distinguish — is
exactly [ALP]'s "no missing constraint inside bandwidth one": the report language (two moments) cannot
distinguish the real zeros from the 256-law, so the mechanism is limited by its *language*, not its
incentives. **Cheapest probe:** none.

### TCS-P6-5 No-regret / online row-revelation — KNOWN-DEAD (framing only)
**Idea:** the row-sweep as an online information-revelation game; regret = 0.6818 vs 1.
**Verdict:** decorative; the regret curve is [ALP]'s LP-B′ table with no new content. **Cheapest probe:**
none.

---

## TOP 10 (expected value × feasibility × cheap-probe)

1. **TCS-P1-4 — Unconditional 4th moment m₄(λ) at λ < 1/2 (RS range) + admissible-quartic distinct bound.**
   The only genuinely new *proven-input arithmetic* question in the TCS angle, and the natural next term of
   the paper's own one-sided-Chebyshev/HL*(4,λ) roadmap with RS-range provenance. **Probe RUN (negative-
   leaning):** m₄(1/2) ≈ 11.25, 2m₃−m₄ ≈ −1.6…−2.3 < 0 → the quartic cannot beat the cubic in the
   unconditional range; the exact 3D closed form (a) closes the RS-range quartic route with a documented
   negative, (b) delivers the m₄(1) = 13/4 re-verification flagged open in [TB] §5.3. Probe done; fund the
   closed form if a quartic under RH (2m₃−m₄ = +0.75 > 2/3) is wanted. Med.
2. **TCS-P4-1 — Natural-proofs/RR-barrier identification of the 0.6818 ceiling.** The strongest strategic
   vector: the ceiling is a *proven* natural-proofs-style impossibility for the certificate class (RR
   barriers are conditional; ours is a theorem), and the RR escape map (= non-class inputs) IS our
   documented roadmap. Kills re-derivation of all in-class attacks at the framing stage. Immediate.
3. **TCS-P3-1 — Sample complexity of separating zeros from the 256-law.** Probe RUN: ~18 independent
   windows, i.e. a few hundred zeros — the worlds are statistically easy to separate; the obstruction is
   class-feasibility (means-only, per-T), not sample count. A clean quantitative P7-diagnostics statement.
   Done.
4. **TCS-P1-3 — SoS/Lasserre integrality-gap identification.** Explains *why* the third-moment LP is
   unbounded without admissibility ([TB] §3.3): the admissible cubic IS a degree-3 SoS valid inequality.
   Unifies [QS]/[TB]/[ALP]; predicts every higher-moment attack faces the same wall. Immediate.
5. **TCS-P2-1 — AMS estimator-variance of the moment measurements.** The measured order-dependent
   finite-height deficit (m₂ −2.3%, m₃ −5%, m₄ −8.5%) is the honest error bar for every higher-moment
   diagnostic; formalize once. Low.
6. **TCS-P6-2 — "The bottleneck is arithmetic, not computation."** Strategic: all optimizations here are
   poly-time LPs; funding goes to arithmetic inputs and belief-changing measurements, not algorithms.
   Immediate.
7. **TCS-P3-5 — Tolerant testing: empirical distance to the crystal.** One plot (dyadic count-variance vs
   the crystal's O(1/L)) on existing machinery; strengthens the "the deficit is a proof artifact, not a
   model of reality" narrative. Low.
8. **TCS-P4-2 — Scalability of the barrier (LP at N = 512).** Same probe as physics [P4.1]: does the
   explicit 256-law adversary scale to an explicit family (like expanders)? If the simple fraction drops,
   the ceiling improves — a real finding. Low–Med.
9. **TCS-P2-4 — The M-row curve as measurement complexity.** Documentation of [ALP]'s LP-B′ under the
   streaming framing: pinning 0.70 needs ≈ 192 in-band measurements; all are configuration data, not
   arithmetic — the sketch is exhausted. Immediate.
10. **TCS-P5-6 — Two-distance-set realizability of {1/6, 2/3, 1/6}.** A 1-hour literature/linear-algebra
    curiosity: if realizable, the crystal is a known combinatorial object. Low.

**Strategic reading.** The TCS angle's two substantive NEW contributions are (i) **TCS-P1-4** — the
unconditional fourth moment in the RS range, the one proven-input arithmetic question the prior catalogs
missed (empirically negative for the distinct wall, but it *closes* the higher-moment hierarchy and
delivers the m₄(1) verification), and (ii) **TCS-P4-1** — the recognition that the 0.6818 ceiling is a
*provable* natural-proofs-style barrier, which converts the program's wall from "a hard upper bound" into
"an impossibility theorem for a precisely-defined proof class, whose only exits are non-class inputs" —
exactly the roadmap M29/GM/TB already established. Everything else is framing (Delsarte, VCG, streaming,
property testing) that confirms the existing closure results from new directions and stops re-derivation.
The persistent open inputs remain: beyond-bandwidth-1 values (conjectural), repulsion (KNOWN-OPEN), and
the derivative-tower/new-target paths ([CD-V9], [CD-V12]) — none of which this catalog reopens, and none
of which it finds a new proven-input route to.

---

## WILD section (deliberately absurd premises; honestly evaluated; each labeled)

### W-TCS1. "RH is a derandomization: the real zeros ARE an explicit PRG for the bandwidth-one test class" — CONJECTURED (framing; consistent with the barrier)
**For:** the averaged Montgomery data is the "randomized" statement; RH + PCC would make the real zeros
achieve it pointwise — an explicit derandomization; the 256-law is the "PRG" the certificate class cannot
distinguish from the real zeros; the barrier says no certificate-class proof can break the equivalence.
**Against:** this is the pair-correlation conjecture by another name; the "PRG" claim adds no provable
input. **Honest fragment:** TCS-P4-1's barrier identification, which is the theorem-backed part.

### W-TCS2. "The 0.6818 ceiling is the first PROVEN natural-proofs barrier outside circuit complexity" — PROVEN (the barrier) / CONJECTURED (the "first" claim)
**For:** the structural match to RR is exact, and unlike RR (which needs unproven PRG assumptions) our
barrier is a Lean theorem [AC]/[ALP] — a provable impossibility for a precisely-defined certificate class.
**Against:** I cannot verify the "first" literature claim (no citation held); RR concerns *proof systems*
for circuit lower bounds while our class is a narrower certificate family — the analogy is structural, not
identity. **Honest fragment:** the provable-barrier statement (label it as such, drop the "first").

### W-TCS3. "Spectral sparsification of the Weil form yields a sparse graph whose expansion IS RH" — CONJECTURED (likely-false)
**For:** expander mixing = small-α form factor = rigidity; a sparse graph with expansion 0 would encode
F(0) = 0.
**Against:** expansion ≈ the spectral gap ≈ F(0) = 0 is *already consumed* by the two-moment certificate
(the mean density and rigidity are in-band data); sparsification does not preserve inertia (TCS-P1-1).
The "graph whose expansion is RH" is Hilbert–Pólya renamed. **Verdict:** KNOWN-DEAD-likely; the
measurement fragment is [G3]'s discrepancy diagnostic.

### W-TCS4. "The certificate is a property tester whose power is exactly 0.6818" — CONJECTURED (content = the ceiling)
**For:** the certificate IS a distribution-free tester of "simple fraction ≥ v"; its power (the largest
certifiable v) is 0.6818.
**Against:** this is the ceiling theorem in tester language; no new content. **Honest fragment:**
TCS-P3-1/P3-2's sample-complexity and distribution-freeness statements.

### W-TCS5. "The zeros form a lattice; RH ⟺ the Gaussian heuristic holds for it" — CONJECTURED (speculative; content = repulsion)
**For:** the Gaussian heuristic (a two-moment estimate) fails on structured lattices — exactly like the
certificate on the 256-law; the zeros' "shortest vector" is the minimal gap.
**Against:** the Gaussian heuristic is a heuristic, not a theorem; the minimal-gap statement IS the
repulsion problem (KNOWN-OPEN, [CD-V17]) — no new input; the "⟺" is unverifiable. **Honest fragment:**
TCS-P5-3's strategic lesson only.

### W-TCS6. "RH is the statement that the SoS hierarchy never closes the certificate's integrality gap" — CONJECTURED (consistent with the probe)
**For:** TCS-P1-3 + TCS-P1-4: the degree-2 gap is 0.318; the degree-3 (cubic) round fails unconditionally
at λ < 2/3 [TB]; the degree-4 round fails unconditionally at λ < 1/2 (probe: 2m₃−m₄ < 0); the pattern
predicts every *unconditional* higher round fails in the RS range — the hierarchy closes only under RH
(conjectural inputs).
**Against:** "never" is an extrapolation from three rounds; the RS-range condition kλ < 2 forces
λ → 0 as k → ∞, where the base constants degrade — so the *unconditional* hierarchy is likely *provably*
empty, which is the documented negative in a new dress. **Honest fragment:** TCS-P1-3 + TCS-P1-4's
computations.

---

## Label inventory

- **NEW** (invented here; conjectured by construction, each with a kill criterion): TCS-P1-3 (SoS
  framing), TCS-P1-4 (unconditional m₄; **probe RUN** — empirical m₄(1/2) ≈ 11.25, 2m₃−m₄ < 0,
  CHECKED NUMERICALLY, script cited in §0.3), TCS-P1-5, TCS-P2-1 (diagnostic), TCS-P2-4, TCS-P2-5,
  TCS-P3-1 (**probe RUN** — sample complexity ≈ 18 windows, CHECKED NUMERICALLY), TCS-P3-2, TCS-P3-3,
  TCS-P3-5, TCS-P4-1 (barrier identification; barrier part PROVEN (Lean [AC]/[ALP]), analogy
  CONJECTURED), TCS-P4-2 (overlaps [P4.1]), TCS-P4-3, TCS-P4-5, TCS-P5-1 (identification), TCS-P5-3,
  TCS-P5-5, TCS-P5-6 (curiosity), TCS-P6-1, TCS-P6-2 (strategic), TCS-P6-4, and the WILD fragments
  W-TCS1…W-TCS6 (conjectured by construction).
- **KNOWN-DEAD** (derived here or cited, documented so executioners don't re-derive): TCS-P1-1 (spectral
  sparsification: inertia is not a spectral-approximation invariant; the certificate needs exact atoms;
  the matrix is analytically evaluable), TCS-P2-2 (count-sketch/JL: estimation ≠ proof; ‖·‖² is
  analytic), TCS-P2-3 (heavy hitters/resolution = [P6.2]/[P6.3]), TCS-P1-6 (hygiene; overlaps [M3]/[S4]),
  TCS-P3-4 (identity testing; orthogonality [GM §4]), TCS-P4-4 (algebrization ⊂ P4-1), TCS-P5-2 (Johnson
  = lemmaR_tight), TCS-P5-4 (expander codes = [G3]), TCS-P6-3 (hardness ⊂ P6-2), TCS-P6-5 (no-regret,
  decorative), and the non-measurement halves of W-TCS3/W-TCS4/W-TCS5.
- **KNOWN-OPEN** (core open, new framing only): TCS-P1-2 (resolvent route, [P1.1]); the repulsion pointer
  in TCS-P5-3 ([CD-V17]); the "first provable barrier" literature claim in W-TCS2 (not verifiable from
  held sources).
- **TESTED-OPEN**: TCS-P1-4 and TCS-P3-1 are probe-run states (numbers CHECKED NUMERICALLY, conclusions
  conditional on the closed form / on the measured variance); TCS-P2-1's deficit curve is measured
  (§0.3) and its use as an error bar is the open formalism.
- **Cheapest-probe discipline:** every vector has a <1h probe on existing machinery
  (`tools/data/zeros_computed_10000.txt`, `tools/lpdual/`, the [AC]/[ALP] LP code, the [GM]/[G3]
  variance tooling) or is a pure documentation/framing deliverable. Nothing here needs heavy compute to
  start.

**Honest closing note.** The TCS angle's two substantive NEW contributions are (i) **TCS-P1-4**, the
unconditional fourth moment in the Rudnick–Sarnak range — a real, never-computed, provable-input
arithmetic question whose empirical probe (m₄(1/2) ≈ 11.25; 2m₃−m₄ < 0) makes the RS-range quartic route
a probable documented negative while still delivering the m₄(1) = 13/4 verification, and (ii) **TCS-P4-1**,
the identification of the 0.6818 ceiling as a *provable* natural-proofs-style barrier for the certificate
class — the cleanest available explanation of why every in-class attack (matrix inequalities, third
moments, MV constants, Nevanlinna) died, and why the only exits are non-class arithmetic inputs
(beyond-bandwidth-1 values, repulsion) or new targets (derivative tower, families). Everything else in
this catalog is framing that re-confirms the closed doors (Delsarte, VCG, streaming, property testing,
hardness) or diagnostics that refine the P7 slack story (sample complexity, distance-to-crystal, moment
measurement error bars). No vector here claims to settle RH; the deliverable is a ranked probe set whose
negatives are documented results.
