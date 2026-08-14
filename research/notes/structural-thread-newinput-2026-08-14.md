# Structural Thread: Candidate UNCONDITIONAL inputs to break the 0.6818 wall

**Agent:** research (structural thread). **Date:** 2026-08-14.
**Scope:** literature survey only (no compute — zero-counting and scripts explicitly out of scope per charter).
**Tool note:** the `web_search` tool was down (auth failure) this session; all citations below were verified
directly against the arXiv export API (abstracts read this session) unless marked `[CITATION = secondary]`.

---

## 0. Verdict up front (the honest answer)

**No known unconditional theorem certifies p₁ > 0.6818. The wall is a genuine theorem-level gap, not a
certificate gap.** The fully unconditional state of the art for the *simple fraction of all nontrivial zeros*
is **~0.4075** (PRZZ20, "simple **and on the line**", which is a valid lower bound on the all-zeros simple
fraction). The only theorems that clear 0.6818 — **19/27 ≈ 0.7037** (Bui–Heath-Brown) and **≈0.6792**
(Chirre–Gonçalves–de Laat SDP) — are **conditional on RH**. The strongest result of the *right type* (simple
fraction of ALL zeros, off-line included) is **0.617, but conditional on a box hypothesis**
(|β − 1/2| < 1/(2 log T)) that is itself unproven. This confirms, from the current literature, the verdict in
`structural-final-verdict.md`: the only lever is a new unconditional simple-fraction theorem, and none exists.

That said, the 2024–2026 literature contains **two live threads** that are the closest things to
unconditionalizable inputs, detailed below. Neither is a theorem yet; both are concrete, checkable targets.

---

## 1. The exact object (why the certificate needs ALL-zeros simplicity)

p₁ in the certificate is the simple fraction over **all nontrivial zeros** (on and off the line). Therefore:

- On-line proportion results (Levinson 1/3 → Conrey 40% → Feng 41.28% → PRZZ 41.72%) bound only how many zeros
  sit on the line; they do **not** bound simplicity of off-line zeros.
- PRZZ's **40.75% simple-and-on-line** is a valid unconditional lower bound on the all-zeros simple fraction
  (each of those zeros is simple, period). **PROVEN (unconditional)** — arXiv:1802.10521 "More than five-twelfths
  of the zeros of ζ are on the critical line"; the 40.75% / 41.72% split is `[CITATION = secondary]` (BGST
  2501.14545 §1, as recorded in `multiplicity-theorem-route.md`).
- The only results bounding the **all-zeros** simple fraction are: **0.617 under a box hypothesis** (BGSTB,
  arXiv:2306.04799, abstract verified this session), **≈0.679 under RH** (CGdL via SDP), **19/27 under RH**
  (Bui–Heath-Brown, arXiv:1302.5018, abstract verified this session). All conditional.

**Honesty label:** every "unconditional" bound above is either ~0.41 (far below 0.6818) or conditional. No
unconditional input exceeds p₀ = 0.6818. **CONFIRMED, 2026-08-14.**

---

## 2. Ranked candidate inputs (what they would give / why provable / references)

### Candidate 1 (MOST PROMISING): The Goldston–Suriajaya "general estimate replaces RH" framework
**Status: PROVEN framework; required input UNPROVEN.**

- **What it is:** Montgomery's 1973 pair-correlation theorem (RH-conditional) has been re-proven so that the
  hypothesis is a *general estimate on a double sum over zeros*, or a *narrow-box condition* on zero locations,
  instead of RH. arXiv:2511.20059 "Zeta Zeros on the Critical Line" (Nov 2025) and arXiv:2603.28104 "Zeta Zeros
  in a Narrow Vertical Box" (Mar 2026), both Goldston–Suriajaya (abstracts verified this session). Preceded by
  BGSTB arXiv:2306.04799 "An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta
  Function" (2023), whose abstract states: an **unconditional** form of Montgomery's theorem, applied to prove
  **≥ 61.7% simple** under the box |β − 1/2| < 1/(2 log T) for T^{3/8} < γ ≤ T.
- **What it would give:** a proven unconditional (or much-weaker-hypothesis) estimate of this type IS the
  certificate input: the pair-correlation machinery then bounds Σ_ρ(m_ρ − 1) (equivalently the simple fraction)
  at strength controlled by the estimate, feeding v = p₁ + |E(1)| directly. The BGSTB box result already
  reaches 0.617; a strengthened unconditional form (or any box/double-sum estimate certified for a positive
  proportion of zeros, or on average) would raise p₁ toward and conceivably past 0.6818.
- **Why it might be provable:** the remaining gap is a *single, explicitly-stated, average-type estimate* (a
  double sum over zeros, or the box condition) — not RH itself. BGSTB already proved the unconditional core of
  Montgomery's theorem; the box condition is exactly the shape of what zero-density / mean-value methods
  control. This is the one line where "remove RH from a known simple-fraction theorem" has been reduced to a
  concrete checkable statement.
- **References:** arXiv:2306.04799 (BGSTB); arXiv:2511.20059; arXiv:2603.28104 (Goldston–Suriajaya);
  arXiv:2501.14545 (BGST, companion "Pair Correlation of Zeros of the Riemann Zeta Function I").
- **Honest caveat:** 0.617 < 0.6818, and the box hypothesis itself is unproven. This is the *closest route*,
  not a theorem.

### Candidate 2: The Bui–Heath-Brown / CGG discrete-moment mechanism (the only known shape that clears the wall)
**Status: PROVEN, but only conditional on RH/GLH.**

- **What it is:** arXiv:1302.5018 "On simple zeros of the Riemann zeta-function": **at least 19/27 ≈ 0.7037 of
  the zeros are simple, assuming RH**, removing the Generalised Lindelöf Hypothesis previously needed by
  Conrey–Ghosh–Gonek (Proc. LMS 76 (1998) 497–522) — abstract verified this session. The method is **discrete
  mollified moments of ζ′ at zeros** — a mechanism *different* from pair correlation.
- **What it would give:** 19/27 > 0.6818 — this mechanism, if ever made unconditional (even partially), clears
  the wall outright. It is the *shape* any winning unconditional theorem must mimic.
- **Why it might be provable:** the CGG conjecture (proportion of simple zeros = 1; see §3) is the target; the
  discrete-moment machinery needs on-line control of ζ and ζ′ averages. If a Guth–Maynard-type zero-density
  input could supply the needed moment control without RH (see Candidate 4), a partial unconditional
  simple-fraction bound would follow. **INCONCLUSIVE whether any such unconditional input is known** — no such
  theorem found this session.
- **References:** arXiv:1302.5018; CGG Proc. LMS 76 (1998) 497–522 (via the 1302.5018 abstract — original not
  opened, `[CITATION = secondary]`).
- **Honest caveat:** removing RH from this argument appears strictly harder than the Candidate 1 box estimate.

### Candidate 3: SDP pair-correlation bounds on multiplicity sums (the exact object, made unconditional)
**Status: PROVEN machinery (RH-conditional); unconditional version missing the same input as Candidate 1.**

- **What it is:** arXiv:1810.08843 "Pair Correlation Estimates for the Zeros of the Zeta Function via
  Semidefinite Programming" (Chirre–Gonçalves–de Laat): SDP optimizes Montgomery's form factor and improves
  bounds on the proportion of **distinct** zeros, small gaps, **and sums involving multiplicities of zeros**
  (abstract verified this session). This is a theorem of exactly the type requested: bounds on Σ_ρ(m_ρ − 1)
  / multiplicity-weighted sums from pair correlation. Under RH it yields the ≈0.6792 simple fraction
  (`[CITATION = secondary]` via BGSTB/BGST abstracts).
- **What it would give:** the same SDP machinery is now runnable on the **unconditional** Montgomery theorem
  (BGSTB); the only missing ingredient is the same box/double-sum estimate as Candidate 1. Any unconditional
  strengthening of BGSTB's input transfers, via the SDP, directly into multiplicity-sum bounds — i.e., into p₁.
- **Why it might be provable:** the SDP is a solved optimization layer; the frontier is the input estimate.
  Identical missing piece to Candidate 1, so ranked behind it only because it adds nothing beyond the SDP layer.
- **References:** arXiv:1810.08843 (CGdL, 2020); arXiv:2306.04799 (BGSTB) as the unconditional base.

### Candidate 4: Guth–Maynard zero-density (2024) and the 2026 survey
**Status: PROVEN (Guth–Maynard result); USEFULNESS for simple-fraction INCONCLUSIVE.**

- **What it is:** the 2024 Guth–Maynard new zero-density theorem (announced 2024), summarized in the 2026
  survey "A decades-long breakthrough in zero-density estimates and primes in short intervals" by
  Turnage-Butterbaugh (arXiv:2607.04632, abstract verified this session: "In 2024, Larry Guth and James Maynard
  announced a new zero-density theorem which, for a key location in the critical strip, strengthens pr…").
- **What it would give:** (a) directly, better N(σ, T) estimates could extend the Feng mollifier length θ past
  6/11, improving the **on-line / simple-on-line** proportions (Wall A of `multiplicity-theorem-route.md`) — but
  the Levinson route's ceiling is ~0.41–0.45, still far below 0.6818; (b) potentially, the average-type control
  needed by Candidate 1's double-sum/box estimate (a "positive proportion of zeros in the box" style statement
  fed into BGSTB's unconditional machinery). **INCONCLUSIVE** whether anyone has produced such an application —
  not found in this session's searches.
- **Why it might be provable:** zero-density estimates near σ = 1/2 are precisely the tool for box-type
  statements; the survey's framing suggests applications are actively being pursued.
- **References:** arXiv:2607.04632 (survey); Guth–Maynard (2024, announced; survey cites it).
- **Honest caveat:** even full success on the Levinson route does not clear 0.6818; value is as an input to
  Candidates 1/2.

### Candidate 5: Qualitative/quantitative simple-zero results for other L-functions
**Status: PROVEN, but vanishing proportions; ABANDONED for the 0.6818 wall (reason: strength).**

- arXiv:1802.01764 (Booker–Cho–Kim): every cuspidal GL₂ L-function has **infinitely many** simple zeros
  (PROVEN). arXiv:2109.15311 (de Faveri 2021): Ω(T^δ) simple zeros, δ < 2/27 (PROVEN, quantitative but tiny
  exponent). arXiv:2410.11605 (Banks 2024): a Linnik–Sprindzuk variant for simple zeros of Dirichlet L-functions
  under a new hypothesis RH_sim^†[χ] (PROVEN as conditional statements). arXiv:2410.2433 (Bui 2014, *unpublished
  note*): three-piece mollifier sketch to "slightly improve" simple-zero percentages on the line.
- **What they would give:** nothing directly for p₁ > 0.6818 — exponents are vanishing. Listed for
  completeness: the simple-zeros landscape is active, and Banks' hypothesis class (RH_sim^†) is a novel
  decomposition worth watching.
- **Verdict: ABANDONED** as an input to the 0.6818 wall (provable strength far below the threshold), retained
  only as landscape.

---

## 3. Conjectures vs proven (what the task asked to separate)

| Claim | Status | Source |
|---|---|---|
| Proportion of simple zeros of ζ tends to 1 (CGG) | **CONJECTURED** | CGG Proc. LMS 76 (1998) 497–522, via Bui–Heath-Brown abstract `[secondary]` |
| ≥ 19/27 simple assuming RH (removes GLH) | **PROVEN (conditional on RH)** | arXiv:1302.5018 (Bui–Heath-Brown 2013), abstract read |
| ≥ 2/3 simple assuming RH (Montgomery) | **PROVEN (conditional on RH)** | arXiv:2511.20059/2306.04799 abstracts |
| ≈ 67.9% simple assuming RH (SDP refinement) | **PROVEN (conditional on RH)** | arXiv:2306.04799 abstract; CGdL arXiv:1810.08843 `[secondary]` for 67.92% |
| ≥ 61.7% simple under box \|β−1/2\| < 1/(2 log T) | **PROVEN (conditional on box)** | arXiv:2306.04799 abstract |
| Unconditional Montgomery pair-correlation theorem | **PROVEN (unconditional)** | arXiv:2306.04799 abstract |
| RH replaceable by a general double-sum estimate (GS) | **PROVEN (framework)** | arXiv:2511.20059, 2603.28104 abstracts |
| > 5/12 of zeros on the critical line (PRZZ) | **PROVEN (unconditional)** | arXiv:1802.10521 title/abstract |
| 40.75% simple-and-on-line / 41.72% on-line | **PROVEN (unconditional)** | arXiv:1802.10521, split `[secondary]` via BGST 2501.14545 §1 |
| Gonek conjecture: Σ_{γ≤T} 1/\|ζ′(ρ)\|² ~ (6/π³)T log T | **CONJECTURED**; lower bound of half the value proven **conditional on RH + simplicity** | arXiv:1106.1160 (Milinovich–Ng 2011) abstract |
| Guth–Maynard zero-density (2024) | **PROVEN (unconditional theorem)** | arXiv:2607.04632 survey abstract |

---

## 4. Which single candidate is most promising

**Candidate 1 (Goldston–Suriajaya / BGSTB general-estimate framework).** Reasons:

1. It is the **only** line that has already reduced "RH" to a *single explicit estimate* (a double sum over
   zeros, or the box condition) — and its authors have already proven an **unconditional** Montgomery theorem
   (BGSTB). The hypothesis class has been moved from RH to a quantitatively checkable statement.
2. It is **recent and active** (2023, 2025, 2026 preprints) — this is where the field is moving, not a stale
   record.
3. Its input is a **well-defined research target**: any unconditional certification of the double-sum estimate
   (even for a positive proportion of zeros, or on average) plugs directly into the pair-correlation machinery
   and moves p₁ — the certificate's shadow-price-1 lever.

The honest caveat stands: today it yields 0.617 under a box hypothesis that is itself unproven; it is the
*closest route*, and the **only** route whose missing piece is a concrete estimate rather than RH itself.

---

## 5. Bottom line

- **CONFIRMED (2026-08-14): no unconditional theorem in the surveyed literature certifies p₁ > 0.6818.**
  Best unconditional: ~0.4075 (PRZZ20). Best all-zeros simple fraction: 0.617 (box-conditional, BGSTB) and
  19/27 / 0.679 (RH-conditional). The 0.6818 wall is a theorem-level gap.
- **The live threads to fund/watch:** (a) Goldston–Suriajaya general-estimate framework — the most promising
  route, missing one explicit estimate; (b) Guth–Maynard zero-density as a potential supplier of that estimate
  (or of a longer mollifier for the 0.4075 route); (c) the CGG/Bui–Heath-Brown discrete-moment mechanism as the
  shape of the winning theorem (19/27 clears the wall, conditionally).
- **Not funded:** Candidate 5 (vanishing proportions); re-optimization of the certificate class (Lean-proven
  exhausted, per `structural-final-verdict.md`).

*No computation was performed in this session (literature-only task); every number above carries a source or a
CONJECTURED label per the honesty charter.*
