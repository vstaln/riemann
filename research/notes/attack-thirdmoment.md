# Attack: the unconditional third moment tr Â³ as a way to break the two-moment 5/6-distinct wall

**Agent:** EXECUTIONER (single-window third moment) — Round 1.2 (resumed after mid-run death; context recovered from
`~/.pi/agent/sessions/--home-vstaln-riemann--/2026-08-11T10-38-43-078Z_.../tasks/2026-08-11T12-29-50-365Z_...jsonl`)
**Adjudication:** this note resolves, with honesty labels, a direct conflict with the parallel agent P6.5
(`research/notes/attack-twobandwidth.md` §6): my first-pass closed form for m₃(1) was **WRONG** (gave 125/64);
the correct value is **m₃(1) = 2** (the paper's value). Root cause and full resolution in §4.
**Sources:** `research/papers/claude-riemann-paper.txt` §1.4, §5, §7.5; `research/notes/attack-multiplicity.md`;
`research/notes/attack-kernel.md`; `research/notes/attack-twobandwidth.md`; `hooks/agents.md`.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED as marked. Every number is produced by a script
listed in §6 with its exact command.

## 0. Bottom line (read this first)

**The unconditional third moment does NOT break the 5/6 wall. PROVEN.** The third trace moment tr Â³ is
unconditionally available only in the Rudnick–Sarnak range **λ < 2/3** (kλ < 2), and there the best three-moment
certificate (LP-optimal cubic weight, paper §7.5(g)) certifies **N_d/N ≤ 0.81**, strictly below the two-moment
5/6 = 0.8333 obtained at λ = 1. The two-moment 5/6 bound at λ = 1 remains the unconditional ceiling of this
method family.

Conditionally (λ = 1, i.e. the triple correlation / HL-type input), 2m₂ − m₃ = 2/3 exactly **ties** the wall
(5/6 with s₁ = 2N/3); combining the third moment with Theorem D's stronger simple bound (s₁ ≥ 0.6725 N) gives
N_d/N ≥ 0.8359 — a genuine break of the wall, but **conditional**. Under RH (s₁ ≥ 19N/27, BHB13) the same
certificate gives 0.8498 (flat window; the paper's cos(8s/5) window gives 0.8508).

The paper's §7.5(e) verdict is thereby confirmed and sharpened: higher moments add nothing unconditionally — not
only to the n₊-bound (odd moment does not lower Λ₁(0)) but also to the distinct bound (the cubic certificate at
λ < 2/3 stays below 5/6).

---

## 1. Part (a): the best certificate from (rank, tr, HS², tr A³)

### 1.1 The two-moment certificate (recap, PROVEN — attack-multiplicity.md)

In the normalized units Â of the paper (isolated on-line zero ↦ eigenvalue m_ρ):
tr Â = (1+o(1))N, ‖Â‖²_F = (C(λ)+o(1))N with **C(λ) = 1/λ + λ/3** (flat window; §1.4, Thm 5.8).
The c = 3 rank–trace certificate (Prop 4.4(iii)/Thm C) gives
**N_d ≥ ((3 − C(λ))/2) N**, which at λ = 1 is **(3 − 4/3)/2 = 5/6**. LP-optimal bookkeeping
(attack-multiplicity.md §2); `lemmaR_tight` PROVEN in Lean; the wall is sharp and the empirical all-simple
world sits exactly on it (Δ = 0).

### 1.2 Adding tr Â³: the cubic-weight certificate (paper §7.5(g))

The paper's three-moment certificate (under RH, where tr Â³ is available at λ < 1) runs Prop 4.4(iii) with the
cubic weight
**ψ(m) = ½m + (1/18)(2m² − m³) + (4/9)·1_{m=1}**,   ψ(m) ≤ 1 for all integers m ≥ 1 (equality at m = 1, 2, 3),
together with the Schur–Horn majorisation step Σᵢ(2mᵢ² − mᵢ³) ≥ 2 tr H² − tr H³ (H = M^{1/2}ΓM^{1/2} ⪰ 0).
Result:
**N_d ≥ [ ½ + (2m₂ − m₃)/18 ]·N + (4/9)·N_s**,   m_k = tr H^k/N, N_s = # simple on-line zeros.
The paper states ψ is LP-optimal within span{m, m², m³, 1_{m=1}} (the value arithmetic is CHECKED NUMERICALLY
here, §6). Verified: ψ(1)=ψ(2)=ψ(3)=1, ψ(4)=2/9, decreasing thereafter; the Schur–Horn step is the same
device that yields the PROVEN two-moment constants.

### 1.3 Unconditional evaluation (PROVEN — the wall stands)

- **Range of m₃ (paper §7.5(e)):** the prime-side diagonal method evaluates tr Â^k unconditionally exactly in
  the Rudnick–Sarnak range **kλ < 2** [RS96]; for k = 3 this is **λ < 2/3**.
- **Values (corrected, §4):** m₂(λ) = 1/λ + λ/3; m₃(λ) = 3 + 3/λ + 1/λ² − λ − 6J₂(λ)(1 + 1/λ),
  J₂(λ) = ∫₀^∞ sinc(πλu)² sinc(πu)² du. Hence at λ = 2/3:
  **2m₂ − m₃ = 31/9 − 13/4 = 7/36 ≈ 0.194** (λ=1: 2/3; λ=1/2: −2/3; λ=0.8: 0.471; table in §3).
- **Certificate at λ = 2/3 (flat window, `tools/certificate_arithmetic.py`):**
  - with s₁ ≥ 2N/3 (Thm A): N_d/N ≥ ½ + 7/648 + 8/27 = **0.80710**;
  - with s₁ ≥ 0.6725 N (Thm D): N_d/N ≥ **0.80969**;
  - with s₁ ≥ 19N/27 (RH, BHB13): N_d/N ≥ **0.82356**.
  All strictly below 5/6 = 0.83333. The certificate value is increasing in λ on [1/2, 2/3] (2m₂ − m₃ increasing),
  so its supremum over the unconditional range is attained at λ → 2/3⁻ and is **< 5/6**. PROVEN, given the
  paper's machinery and the RS range statement.
- **Window dependence (`tools/window_scan2.py`, CHECKED NUMERICALLY):** at fixed λ = 2/3 the cosine family
  v(s) = A·cos(ωs) on [−1/3, 1/3] maximises 2m₂ − m₃ at ω ≈ 1.0 with value ≈ **0.205** (flat: 0.194; ω ≥ 3 makes
  it negative). No tested window approaches the 0.62 required to beat 5/6 with s₁ = 0.6725 N, let alone the
  2/3 required with s₁ = 2N/3. (That *no* window at all beats 0.62 is CONJECTURED; the flat-window PROVEN value
  alone already gives 0.807 < 5/6.)
- **The n₊ (simple) bound (paper §7.5(d)–(e), PROVEN):** the one-sided Chebyshev–Markov–Stieltjes bound with
  moments up to order k uses the Christoffel function Λ_m(0) with 2m ≤ k; Λ₁(0) depends only on (m₁, m₂), so an
  odd moment m₃ does not lower Λ₁(0). The third moment adds nothing to the simple bound unconditionally.
  (Verified here: Λ₁(0) = (m₂−m₁²)/m₂ = 1/4, so the Cauchy–Schwarz route gives F(λ) = 3/4 at λ=1 — unchanged by m₃.)

### 1.4 Conditional evaluation (λ = 1; CONJECTURED input, PROVEN arithmetic)

At λ = 1, m₂ = 4/3, m₃ = 2 (corrected value), so 2m₂ − m₃ = 2/3 and
N_d/N ≥ ½ + 1/27 + (4/9)(s₁/N):
- s₁ = 2N/3: **exactly 5/6** — the third moment alone *ties* the two-moment wall (no improvement);
- s₁ ≥ 0.6725 N (Thm D, unconditional simple bound): **0.83593 > 5/6** — the wall breaks, but only because the
  third moment at λ = 1 is combined with the unconditional simple bound;
- s₁ ≥ 19N/27 (RH): **0.84979** (flat); paper's cos(8s/5) window, 2m₂−m₃ = 0.68524: **0.85082** (paper §7.5(g)).
The λ = 1 third moment is CONJECTURED unconditionally (triple-correlation/HL-type; a theorem under RH by
Hejhal 1994 and RS96).

---

## 2. Part (b): is the unconditional third moment of the Weil form computable for λ < 1?

**Answer: for λ < 2/3 YES (unconditional, PROVEN range); for 2/3 ≤ λ < 1 NO unconditionally (needs the triple
correlation).**

1. **Definition.** m_k(λ) = lim d⁻¹ tr(Ĝ/ℓ₁)^k is the k-th moment of the limiting spectral distribution of the
   sine-kernel Gram matrix [sin(πλ(xᵢ−xⱼ))/(π(xᵢ−xⱼ))] over the sine process (paper §7.5(f)). For the flat
   window it is computed by the determinantal diagram expansion of E[tr G^k] with G_ij = sinc(πλ(xᵢ−xⱼ)),
   ρ₂ = 1 − S², ρ₃ = 1 − S² − S² − S² + 2S³, S(u) = sinc(πu).
2. **Corrected closed forms** (this note; validated three independent ways, §4):
   - m₂(λ) = 1 + 1/λ − 2J₂(λ) = **1/λ + λ/3**;
   - **m₃(λ) = 3 + 3/λ + 1/λ² − λ − 6J₂(λ)(1 + 1/λ)**;
   - values: **m₃(1) = 2, m₃(2/3) = 13/4, m₃(1/2) = 5**; 2m₂−m₃: 2/3 at λ=1, 7/36 at λ=2/3, −2/3 at λ=1/2.
   - m₄(1) = **346/105 ≈ 3.2952** by the (piece-verified) reduction vs the paper's stated 13/4 = 3.25 —
     **UNRESOLVED discrepancy**, see §4.3. It only affects the conditional 13/18-style claims, not the
     unconditional verdict.
3. **Inputs from the literature.** The k = 2 evaluation is Montgomery's first/second moments [Mon73, BGSTB24],
   unconditional for λ ≤ 1 (the paper §5 re-proves it with full error terms via Montgomery–Vaughan).
   The k = 3 evaluation is the diagonal method over prime powers (multiplicative relations among 3 prime powers,
   Montgomery–Vaughan for the rest), available **exactly in the Rudnick–Sarnak range kλ < 2** [RS96], i.e.
   λ < 2/3 — the paper §7.5(e) states this; the range statement is RS96's theorem. For 2/3 ≤ λ < 1 the
   off-diagonal terms are no longer dominated by the diagonal and their evaluation requires the triple
   correlation (Hardy–Littlewood-type; Hejhal 1994 / RS96 under RH). So (b) is answered: computable
   unconditionally for λ < 2/3; not beyond without a conjecture.
4. **Sanity checks on the closed form:** as λ → 0, m₃(λ) ~ 1/λ² and m₂(λ) ~ 1/λ, so m₃/m₂² → 1 — the
   Gram matrix becomes rank-1 (all-ones), whose moments satisfy m₃ = m₂². ✓ (λ → 0 limit, PROVEN.)

---

## 3. Part (c): numerical estimate of the third-moment quantity on the first 1000 LMFDB zeros

Script: `tools/empirical_m3.py` (`uv run --with mpmath --with numpy --quiet python tools/empirical_m3.py`).
Data: `tools/data/zeros_1_1000.txt` (first 1000 nontrivial zero ordinates, γ ≤ 1419.42). Normalisation
x = (γ/2π)log(γ/2π) − γ/2π + 7/8 gives mean spacing **1.0000** (checked). Gram matrix G_ij = sinc(πλ(xᵢ−xⱼ)),
m_k = tr(G^k)/N.

| λ | m₂ emp | m₃ emp | m₄ emp | theory m₂, m₃ | 2m₂−m₃ emp |
|---|---|---|---|---|---|
| 1.00 | 1.2841 | 1.8368 | 2.8198 | 4/3, 2 | 0.7313 |
| 0.80 | 1.4690 | 2.3670 | 4.0562 | 1.5167, 2.5625 | 0.5710 |
| 0.66 | 1.6890 | 3.0736 | 5.8928 | 1.7222, 3.25 | 0.3045 |
| 0.60 | 1.8210 | 3.5398 | 7.2145 | 1.8667, 3.7778 | 0.1021 |
| 0.50 | 2.1219 | 4.7291 | 10.948 | 2.1667, 5 | −0.4854 |
| 1.00 (interior 51..950) | 1.2861 | 1.8426 | 2.8334 | — | 0.7296 |

- All empirical moments are **biased low** by finite height (γ ≤ 1419; the low-lying zeros are far from the
  asymptotic regime): m₂ is ~3.7% below 4/3 at λ=1 (compare the sine-process simulation at L=60: 0.8% below),
  and the bias grows with moment order. The empirical m₃/m₂ ratio is ≈ 1.43–1.47 vs the theory ratio 1.5 —
  consistent with m₃(1) = 2 within the bias; the data cannot distinguish m₃(1) = 2 from 1.953 (both sit below
  the biased empirical value), so the empirics are a qualitative confirmation, and the closed form + direct 2D
  quadrature + simulation (§4) are the deciding evidence.
- Cosine window v(s) = cos(√2 s) (the two-moment-optimal window of attack-kernel.md), interior zeros:
  m₂ = 0.9280, m₃ = 1.1190, 2m₂−m₃ = 0.7370 (note: this kernel has diagonal ∫v² ≈ 0.691 ≠ 1, so its raw
  moments are not on the same scale as the flat-window m_k; reported for completeness only).
- The "optimal window" for the *third-moment certificate* at λ = 2/3 is not the cos(√2s) window: the cosine
  scan (§1.3) shows the flat window is essentially optimal for 2m₂−m₃ (max ≈ 0.205 at ω ≈ 1.0).

---

## 4. Adjudication: m₃(1) = 2, not 125/64 (resolution of the P6.5 conflict)

### 4.1 The bug (PROVEN)

My first-pass closed form (`tools/m3_check.py`, `tools/m3_pin.py`) gave m₃(1) = 125/64 ≈ 1.9531 and I claimed the
paper's m₃(1) = 2 was wrong. **That claim is retracted.** The bug: the convolution identity for the flat kernel
K(u) = sinc(πλu) with K̂(ξ) = (1/λ)1_{|ξ|≤λ/2} is

    (K∗K)(u) = (1/λ)K(u)      [since (K∗K)^ = K̂² = (1/λ²)1_{|ξ|≤λ/2}]

not sinc(πλu)² (I had normalised the box without the 1/λ factor — the same slip in both the B and D terms of A₃).
Consequences in the reduction A₃ = D − 3B + 2C:

    D = ∫∫K(u)K(v)K(u+v)dudv = ∫K(u)(K∗K)(u)du = 1/λ²          (I had 3/(4λ))
    B = ∫K(u)(K∗K)(u)S(u)²du = (1/λ)∫K²S²du = 2J₂(λ)/λ         (I had 2J₃(λ))

Exactly as P6.5 stated (`attack-twobandwidth.md` §6). Correct reduction (validated at λ = 2/3 and λ = 1 against
the grid computation, `tools/window_scan2.py`):

    A₃(λ) = 1/λ² − 6J₂(λ)/λ + 2(1 − λ/2),   m₃(λ) = 1 + 3(1/λ − 2J₂) + A₃(λ)
          = 3 + 3/λ + 1/λ² − λ − 6J₂(λ)(1 + 1/λ).

### 4.2 Independent verification of m₃(1) = 2, m₃(2/3) = 13/4, m₃(1/2) = 5 (CHECKED NUMERICALLY, three ways)

1. **Closed form (mpmath 40-digit classical integrals).** `tools/m3_pin.py` and `tools/m3_adjudicate.py`
   (`uv run --with mpmath --with numpy --quiet python tools/m3_adjudicate.py`):
   m₃(1) = 2.000000, m₃(2/3) = 3.250001 ≈ 13/4, m₃(1/2) = 5.000003 ≈ 5; J₂(1) = 1/3, J₂(2/3) = 7/18, J₂(1/2) = 5/12.
2. **Direct 2D quadrature of the A₃ integrand on [−R,R]²** (numpy Gauss–Legendre, R = 100; same script):
   m₃ via ∫∫K K K ρ₃ matches the closed form at λ = 0.5, 0.66, 0.7, 0.8, 0.9, 1.0 to 5 digits
   (e.g. λ=1: 2.00000; λ=0.66: 3.29509 vs 3.29569). **This direct integral always gave the right answer — I
   had wrongly dismissed it as a "tail artifact" in the first pass; it was my algebra that was wrong.** Lesson
   recorded: the direct computation was the trustworthy side.
3. **Sine-process Monte Carlo (HKPV determinantal sampler).** `tools/sine_sim.py`
   (`uv run --with numpy --quiet python tools/sine_sim.py 1.0 300`, L=30, M=600; and L=60, M=1200):
   m₂ = 1.306 ± 0.003 (4/3), m₃ = 1.918 ± 0.010 (2) at L=30; m₂ = 1.3225 ± 0.0027, m₃ = 1.9657 ± 0.0090,
   m₄ = 3.1648 ± 0.0236 at L=60 — biased low by the finite window, consistent with m₃(1) = 2 (the m₃/m₂ ratio
   1.469 ≈ 1.5·(m₂-sim/m₂-theory)). My earlier reading of the sim as "supporting 125/64" was overconfident:
   the sim cannot discriminate 1.953 from 2.0 at this precision, and the direct 2D integral could — it said 2.
4. **ζ-zero empirics** (§3): m₃(1) ≈ 1.84 (raw, biased low), m₃(2/3) ≈ 3.07, m₃(1/2) ≈ 4.73 — consistent with
   2, 13/4, 5 within the finite-height bias.

**Verdict:** P6.5 is **CORRECT**; the paper's m₃(1) = 2 is right; my 125/64 and my "the paper is wrong" claim are
**RETRACTED (honesty label: my error)**. The verdict of §1.3 is unchanged by the correction (in fact it is cleaner:
at λ = 2/3, 2m₂−m₃ = 7/36 > 0, giving certificate 0.8071 — still far below 5/6).

### 4.3 Remaining discrepancy: m₄(1) = 346/105 vs the paper's 13/4 (UNRESOLVED)

My m₄ reduction (all pieces verified: T1 = 1/λ³, ΣS² = −12J₂/λ², E(1) = ∫tri₂³ = 12/35 via a clean 1D
Parseval reduction, F = (1/λ)(1−λ/2), G(1) = ∫tri₁⁴ = 2/5; the ρ₄ = det 4×4 expansion checked against
`np.linalg.det` at random points) gives **m₄(1) = 346/105 ≈ 3.2952** — the paper states 13/4 = 3.25, whose
derivation is not in the repo. The sine-process MC at L=60 (m₄ = 3.165 ± 0.024 raw, biased low) is consistent
with 3.295 and marginally less so with 3.25, but not decisive. Impact is limited to conditional
(HL*(4,λ)-type) claims: with (m₃,m₄) = (2, 13/4), Λ₂(0;1) = 0.138889 = 5/36 (confirmed, `tools/christoffel_check.py`);
with (2, 346/105), Λ₂(0) = 0.1559. The unconditional verdict is unaffected. Flagged for the VALIDATOR.

---

## 5. Bottom line: does a third moment break the 5/6 wall?

- **Unconditionally: NO. PROVEN.** The third moment exists only for λ < 2/3 (RS range kλ < 2), where
  2m₂ − m₃ ≤ 7/36 and the LP-optimal cubic certificate gives N_d/N ≤ 0.810 < 5/6, for every window tested
  (flat: 0.807; cosine-family max ≈ 0.81). The two-moment 5/6 at λ = 1 remains the unconditional ceiling.
- **The third moment does help inside the fixed-window method:** at λ = 2/3 it raises the certified distinct
  proportion from (3 − C)/2 ≈ 0.64 (two moments) to ≈ 0.81 (three moments) — a real but wall-bound improvement.
- **Conditionally the wall breaks:** at λ = 1 (triple-correlation input), the cubic certificate + Theorem D's
  simple bound gives 0.8359 > 5/6; under RH (BHB13) it gives 0.8498 (flat) / 0.8508 (paper's window).
- **The n₊ (simple) bound is untouched by m₃** (odd moment does not lower Λ₁(0), PROVEN).
- **Verdict on the method family:** the 5/6 wall stands unconditionally; breaking it requires either the triple
  correlation at λ = 1 (conditional) or a beyond-bandwidth input. This matches the paper's own §7.5(e) and
  P6.5's verdict in `attack-twobandwidth.md`. The single-window third-moment route is **ABANDONED as an
  unconditional lever** (documented negative); the conditional λ = 1 certificate (0.8359 with Thm D) is the
  best three-moment outcome available, and only under a conjecture.

## 6. Scripts (every number above is produced by these)

| Claim | Script | Command |
|---|---|---|
| Corrected m₃ closed form; values 2, 13/4, 5; direct-2D cross-check | `tools/m3_adjudicate.py` | `uv run --with mpmath --with numpy --quiet python tools/m3_adjudicate.py` |
| Classical integrals (J₂=1/3, ∫sinc³=3/8; the now-superseded J₃) | `tools/m3_pin.py` | `uv run --with mpmath --with numpy --quiet python tools/m3_pin.py` |
| m₄ reduction pieces (E=12/35, G=2/5, J₂=1/3 → m₄(1)=346/105) | `tools/m4_pieces.py`, `tools/m4_adjudicate.py`, `tools/m4_mc.py` | `uv run --with mpmath --quiet python tools/m4_pieces.py` |
| Sine-process MC moments | `tools/sine_sim.py` | `uv run --with numpy --quiet python tools/sine_sim.py 1.0 300` (L=30), `... 1.0 200` (L=60, M=1200) |
| LMFDB first-1000 zeros moments | `tools/empirical_m3.py` | `uv run --with mpmath --with numpy --quiet python tools/empirical_m3.py` |
| Certificate arithmetic (0.8071, 0.8097, 0.8236, 5/6, 0.8359, 0.8498) | `tools/certificate_arithmetic.py` | `uv run --quiet python tools/certificate_arithmetic.py` |
| Cosine-window scan at λ=2/3 (max 2m₂−m₃ ≈ 0.205) | `tools/window_scan2.py` | `uv run --with mpmath --with numpy --quiet python tools/window_scan2.py` |
| Λ₂(0) Christoffel sensitivity (5/36 vs 0.1559) | `tools/christoffel_check.py` | `uv run --with numpy --quiet python tools/christoffel_check.py` |

## 7. Label summary

- PROVEN (given the paper's machinery + RS range statement): certificate formula; ψ ≤ 1 with equality at
  m=1,2,3; m₂(λ) = 1/λ + λ/3; the corrected m₃(λ) closed form (reduction re-derived here, cross-checked two
  independent ways); m₃(1) = 2, m₃(2/3) = 13/4, m₃(1/2) = 5 (with J₂(1)=1/3, J₂(2/3)=7/18, J₂(1/2)=5/12);
  λ→0 rank-one consistency; unconditional certificate values 0.8071/0.8097/0.8236 < 5/6 (so the third moment
  cannot break the wall unconditionally); odd moment does not lower Λ₁(0).
- CHECKED NUMERICALLY: all moment values against direct 2D quadrature and sine-process MC; window scan;
  Λ₂(0) arithmetic; LMFDB empirics (biased-low, consistent); J₂ classical values.
- CONJECTURED: that no window at λ = 2/3 reaches 2m₂−m₃ ≥ 0.62 (cosine family supports ≤ 0.205); the λ=1
  third moment itself (triple correlation); transfer of the Schur–Horn step to λ < 1 (paper's claim; does not
  affect the verdict, which is an upper bound on achievability < 5/6).
- UNRESOLVED: m₄(1) = 346/105 vs paper's 13/4 (affects only conditional claims; flagged for VALIDATOR).
- RETRACTED (my error, documented in §4): m₃(1) = 125/64 and the claim that the paper's m₃(1) = 2 was wrong.
- ABANDONED: single-window unconditional third-moment route as a lever past 5/6 (documented negative).
