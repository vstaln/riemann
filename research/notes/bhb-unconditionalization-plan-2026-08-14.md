# Phased attack plan: BHB 19/27 partial-unconditionalization (the Lemma N lever)

**Agent:** planner (atomic deliverable). **Date:** 2026-08-14.
**Task:** Produce the phased plan for the top surviving structural lever — replacing BHB's single RH-use.
**Sources:** hooks/agents.md; bhb-rh-role-2026-08-14.md; bhb-lemmaN-firstcheck-2026-08-14.md;
s4h-strategy-terrain; s4h-decision-reversibility-analysis (read & applied).
**Note:** this plan is the deliverable; it is written read-only (no compute) and is handed to
`reviewer` per the maker/checker split.

---

## 0. One-line answer

The lever is a **single** replacement target: BHB's one RH-use `S₂ = Σ|F(ρ)|²` (with `F = Bζ′`,
*not* `B′`). Partial unconditionalization = bounding `E = Σ F(ρ)[F(ρ̄) − F(1−ρ)]` so that
`E/S₂ < 3.11%`. The terrain has **three independent routes**, two of which are cheap to probe and
one of which is an expensive one-way door. Plan: (1) gap-table scan → (2) two cheap closed-form
probes in parallel (functional-equation ζ″-elimination; density-exponent gap) → (3) only then fund
the expensive commitments, each gated on a cheap probe's outcome.

---

## 1. The single target (restated, [verified] from the two source notes)

- BHB's only RH-use: `1−ρ = ρ̄` for every zero, giving `S₂ = Σ_{0<γ≤T}|F(ρ)|²`, `F = Bζ′`.
  [verified: paper text, bhb-rh-role §0/§2]
- Everything else in BHB (Lemma 1 moments, error terms, GLH-removal) is unconditional. [verified]
- Off-line correction: `E = Σ F(ρ)[F(ρ̄) − F(1−ρ)]`; RH ⇔ E = 0; `N*(T) ≥ S₁²/(S₂+E)`.
- **Slack:** clear 0.6818 ⇔ `E/S₂ < 1 − 0.6818·(27/19) = 0.0311` (3.11%). [verified: PROVEN arithmetic]
- Taylor reduction: `F(ρ̄)−F(1−ρ) = 2(β−1/2)F′(1/2+iγ) + O((β−1/2)³)`, `F′ = B′ζ′ + Bζ″`.
  [verified: PROVEN, lemmaN-firstcheck §3]
- **Blocker:** `Σ|F′|²` splits into good part `Σ|B′ζ′|² = L²·r·S₂`, `r ≈ 0.0777` (diagonal),
  and **bad part `Σ|B(ρ)|²|ζ″(ρ)|²`** — a new weighted discrete second moment of ζ″ that BHB's
  Lemma 1 (a ζ′-moment theorem) does not provide. [verified: lemmaN-firstcheck §4]
- **Optimistic box:** if the bad part were `O(L²·S₂)`, then `E/S₂ ≤ 2Δ√r·L`, so
  `Δ(T) = b/L` with `b ≈ 0.05` clears 3.11% — a **~10× stronger box** than BGSTB's `b = 1/2`.
  [verified: PROVEN form / conditional value, lemmaN-firstcheck §5]

---

## 2. Terrain map (s4h-strategy-terrain, applied)

**Favorable ground (cheap, we hold it):** the arithmetic is already unconditional and the slack
number (3.11%) and box width (b≈0.05) are already PROVEN. The leverage point is exactly one sum `E`.
We are not fighting the whole proof — only the off-line correction.

**Contested ground (cheap to probe, even match):**
- **Route A (box):** Taylor + Cauchy–Schwarz, needs (i) ζ″-moment resolved AND (ii) a b≈0.05 box.
- **Route B (functional equation):** rewrite `E` via `ζ′(1−ρ) = −χ(1−ρ)ζ′(ρ)` at zeros to try to
  avoid differentiating `F` (i.e. avoid ζ″ entirely). Pure algebra; may eliminate the ζ″ blocker.

**Dangerous ground (expensive one-way door):**
- **Route C (prove a new ζ″-moment theorem):** `Σ|B(ρ)|²|ζ″(ρ)|² ≪ L²·S₂` unconditionally. This is
  an open-type problem not in BHB Lemma 1 and not in the literature read. Committing here is a
  Type-1 decision — only after the cheap probes show it is the *only* live route.
- **Route D (density, Guth–Maynard):** bound `E` directly via `N(σ,T)` without Taylor — avoids ζ″
  but requires the density exponent to be strong enough; the exponent gap is unquantified.

**High ground:** RH itself (`E = 0`). The only paths to a *known-type* weaker input are A/B (box)
and D (density); C is a novel theorem that would itself be the research contribution.

---

## 3. Milestones (cheapest-first, highest-information earliest)

> Budget legend: **[CF]** = closed-form / literature only (no compute); **[PROBE<1m]** = f64 scalar
> probe, must name the belief it changes; **[VERIFIER]** = one bounded interval run, recorded eps;
> **[PROOF]** = human effort, no compute unless a <1m probe changes a belief.

---

### M1 — Route-gap table (Type 2, two-way door). Budget: [CF] only.

**Goal:** For every route, extract the strongest KNOWN unconditional input and the exact gap to the
3.11% slack, so no further milestone is funded against a dead gap.

**The one artifact:** a **route-gap table** with rows (Box b, Density exponent, ζ″-moment) and
columns {strongest known / status (unconditional or conditional, and for what proportion of zeros) /
needed to clear 3.11% / gap / source citation}. Every "known" cell cites an arXiv id + verbatim
statement; every "needed" cell re-derives from the PROVEN 3.11% arithmetic above.

**Verification:** validator checks (a) each "known" number traces to a source (no unlabeled claim),
(b) each "needed" number re-derives from `E/S₂ < 0.0311`, (c) the BGSTB `b=1/2` and needed
`b≈0.05` cells reproduce the already-PROVEN values. Any cell without a citation ⇒ milestone fails.

**Dependencies:** none (uses the two source notes + literature). **Rollback:** pure note; fully
reversible — if sources disagree, downgrade the cell to INCONCLUSIVE and cite both. No code, no
compute, nothing to undo.

**Decision gate (the one this milestone exists for):** kill any route whose gap table shows
"needed ≫ known with no known technique bridging it". Routes surviving M1 proceed to M2/M3.

---

### M2 — Functional-equation ζ″-elimination check (Type 2). Budget: [CF] only.

**Goal:** Determine whether the ζ″-blocker can be *bypassed* rather than *bounded*.

**The one artifact:** a **proof sketch or refutation** of the claim "at zeros, the FE identity
`ζ′(1−ρ) = −χ(1−ρ)ζ′(ρ)` lets us express `F(ρ̄) − F(1−ρ)` (or the full `E`) in terms of `F` and
`ζ′`-moments already controlled by BHB Lemma 1 — i.e. without ever differentiating `F` to get `Bζ″`."
If ζ″ is unavoidable, the artifact is the **exact step** where the substitution fails and why
(e.g. the Taylor at `1/2+iγ` forces the second derivative regardless of the FE rewriting).

**Verification:** validator re-derives the FE identity (differentiate `ζ(s)=χ(s)ζ(1−s)` at `s=ρ`
where `ζ(ρ)=ζ(1−ρ)=0`) and checks that every step of the sketch/refutation is labeled and that the
claimed elimination actually removes `Bζ″` (not just relabels it).

**Dependencies:** M1 (so we know the box route's other half, b≈0.05, is even in play). **Rollback:**
pure algebra note; fully reversible. No compute.

**Gate:** success ⇒ ζ″-blocker is neutralized and Lemma N reduces to *only* the box question (M5);
refutation ⇒ the box route needs Route C (ζ″-moment theorem) — do **not** commit yet; see M3 first.

---

### M3 — Density-route exponent gap (Type 2). Budget: [CF], one [PROBE<1m] only if the integral is
not closed-form.

**Goal:** Quantify whether the Guth–Maynard zero-density route can bound `E` directly (no Taylor, no
ζ″) strongly enough for 3.11%.

**The one artifact:** a **density gap statement**: the needed `N(σ,T)` exponent `a(σ)` such that
`∫ N(σ,T) d|F|² ≪ 0.0311·S₂`, compared (verbatim, cited) to the best known Guth–Maynard exponent.
Output is a single number pair {needed exponent, known exponent} plus a one-line verdict
(known ≥ needed ⇒ route LIVE; known < needed ⇒ route GAP).

**Verification:** validator re-runs the closed-form integral (or the cited script/command) and
re-checks the known exponent against the source. A <1m probe is permitted ONLY if the integral has
no closed form; it must state the belief it changes ("which exponent is live") in one line first.

**Dependencies:** M1 (which gives the known exponent verbatim; do not assume a value). Independent
of M2 — **M2 and M3 can run in parallel** (two executioner tasks, no shared state).

**Rollback:** reversible; a wrong exponent is corrected by re-citing the source. **Gate:** GAP ⇒
Route D is killed (density cannot reach 3.11% with known tools) and the lever survives only via
Routes A/C; LIVE ⇒ Route D becomes the preferred honest route and M4/M5 are deprioritized.

---

### M4 — ζ″-moment theorem attempt (Type 1, one-way door). Budget: [PROOF]; no compute unless a
[PROBE<1m] changes a belief. **GATED: fund only if M2 refutes ζ″-elimination AND M3 kills Route D.**

**Goal:** Prove `Σ_{0<γ≤T}|B(ρ)|²|ζ″(ρ)|² ≪ L²·S₂` unconditionally (or reduce it to a known moment),
closing Lemma N's Cauchy–Schwarz step.

**The one artifact:** either (a) a **proof sketch / reduction** of the ζ″-moment to a known theorem
(with every hypothesis named), or (b) a **documented refutation/blocker** naming the exact residue
obstacle (e.g. the double pole of ζ″ at s=1 and the horizontal-segment error analysis missing from
BHB Lemma 1).

**Verification:** adversarial — validator tries to break the claimed bound (counterexample, hidden
hypothesis, or a step that silently uses RH/GLH). Success criteria fixed BEFORE starting: the bound
must be `≪ L²·S₂` with all inputs unconditional and labeled. A bound conditional on anything ≥ RH
strength is a FAILURE (it would not be a "partial" unconditionalization).

**Dependencies:** M2=refute, M3=GAP. **Rollback (one-way):** this is the expensive commitment; the
rollback is the pre-declared **effort cap** — if no sketch/reduction survives `reviewer` inside one
round, record the blocker and return. Partial results (a reduction even without a closed proof) are
themselves deliverables.

---

### M5 — Box-attainment reduction (Type 1). Budget: [CF] + literature; [PROOF] only if a reduction
is found. **GATED: fund only if M2 succeeds (ζ″ eliminated) OR M4 succeeds (ζ″ bounded).**

**Goal:** The box route still needs `|β−1/2| ≤ 0.05/log T` (b≈0.05, ~10× BGSTB's b=1/2). Determine
whether this box is *attainable unconditionally* — as a known result, a corollary of a density bound,
or a zero-free-region input — or is itself as hard as RH.

**The one artifact:** a **reduction chain** `{needed box b≈0.05} ← {known density/ZFR input}` with
every implication labeled, OR a **refutation** that no known input gives b≈0.05 (with the exact gap:
what density exponent would suffice and why it exceeds known).

**Verification:** validator checks each arrow of the chain is a valid implication and that the final
input is genuinely unconditional (no hidden RH/GLH). A chain that secretly needs RH is a FAILURE.

**Dependencies:** M2-success or M4-success. **Rollback (one-way):** capped the same way as M4 —
one round, then record the gap. **Gate:** unattainable ⇒ **the box route is killed** (but the lever
may survive via Route D if M3 was LIVE).

---

### M6 — Synthesis write-up (Type 2). Budget: [CF] writing only.

**Goal:** Merge surviving pieces into one labeled statement.

**The one artifact:** a note that states the final status of the lever — either a **new theorem**
"19/27 − O(·) of zeros simple, conditional only on {box/density} weaker than RH", or an
**ABANDONED/inconclusive verdict** with the exact blocker and what it leaves open.

**Verification:** every claim labeled PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED /
ABANDONED(reason); no unlabeled gap. **Dependencies:** all prior milestones. **Rollback:** none
needed (synthesis).

---

## 4. Ordering rationale (cheapest-first, highest-information earliest)

1. **M1 first** — pure literature + closed-form, zero compute, and it decides *which routes are
   even alive* before a single expensive step. Highest information-per-cost available.
2. **M2 and M3 second, in parallel** — both are closed-form (or one <1m probe), both are Type-2
   (fully reversible), and each independently gates one expensive commitment: M2 gates M4/M5
   (box route), M3 gates Route D (density route). They share no state, so they parallelize.
3. **M4 and M5 only after their cheap gate passes** — these are the one-way doors (a novel
   ζ″-moment theorem; a box-attainment reduction). s4h-decision-reversibility: do not spend
   Type-1 effort on a decision a Type-2 probe can already kill.
4. **M6 always runs** — the search never stops; a closed lever is a documented result.

This order guarantees: no verifier run, no branch-and-bound, and no theorem attempt is ever
launched against a gap the cheap probes could have closed first.

---

## 5. Kill criteria (what negative result closes the lever, and what it leaves open)

- **Route-level kills (narrow the lever, do not end the search):**
  - **M3 GAP** ⇒ Route D (density) is dead: known `N(σ,T)` cannot reach 3.11% at this level.
  - **M5 refutation** ⇒ the box route is dead: b≈0.05 is not attainable unconditionally.
- **Lever kill (the conjunction that closes partial-unconditionalization):**
  **M2 refutes ζ″-elimination AND M4 fails to bound `Σ|Bζ″|²` AND M3 shows the density route has a
  gap.** Then every known-type substitute for BHB's single RH-use fails at the 3.11% threshold, and
  the lever is labeled **ABANDONED(reason: ζ″-moment is a new open problem; box b≈0.05 and the
  needed density exponent both exceed known results)**.
- **What it leaves open instead:** (a) the zero-density / simple-zero program as a *standalone*
  target (not a BHB substitute); (b) a genuinely new input structure — per hooks/agents.md, pushing
  past the 0.6818 in-class ceiling *requires* a new input structure or theorem regardless; (c) the
  certified-record thread (0.673481 → 0.6818 in-class ladder) continues as the non-structural track.
- **Positive closure:** if M2 (or M4) + M5 both succeed, the deliverable is a theorem
  "≥ 19/27 − O(b) of zeros simple, conditional only on a b≈0.05 box" (or the density analogue) —
  a real partial-unconditionalization result.

---

## 6. Budget discipline summary

| Milestone | Budget | Belief the (rare) compute would change |
|---|---|---|
| M1 | [CF] only | — (no compute) |
| M2 | [CF] only | — (no compute) |
| M3 | [CF] + ≤1 [PROBE<1m] | "is the density exponent live for 3.11%?" |
| M4 | [PROOF]; ≤1 [PROBE<1m] | "does a candidate ζ″-moment identity survive numerically?" |
| M5 | [CF] + literature; [PROOF] if a reduction exists | — (literature) |
| M6 | [CF] writing | — |

No milestone launches a verifier run, a sweep, or a branch-and-bound. A milestone that would need
>~20 min of compute to reach its next decision point is stopped and re-planned first (hooks
compute discipline). Any numeric claim that *does* arise is produced by code, Rust-first, and the
script + command is cited in the note (hooks language policy).

---

## 7. Labels & assumptions

| Claim | Label |
|---|---|
| RH used once in BHB: `S₂ = Σ|F(ρ)|²`, F = Bζ′ (not B′) | PROVEN (paper text; both source notes) |
| Slack `E/S₂ < 0.0311` to clear 0.6818 | PROVEN (arithmetic) |
| `Σ|B′ζ′|² = L²·r·S₂`, r ≈ 0.0777 | PROVEN (transfer; M₂^Q constant pending) |
| `Σ|Bζ″|² ≪ L²·S₂` | INCONCLUSIVE (the blocker; Route C/M4) |
| Optimistic box `Δ = b/L`, b ≈ 0.05 | PROVEN (form) / rough (value), conditional on ζ″ |
| Route ordering is cheapest-first | PROVEN (design decision, not a math claim) |

**Assumptions (tagged):** `[verified]` the two source notes' PROVEN labels are correct (they were
derived from arXiv:1302.5018 text); `[verified]` BGSTB box b=1/2 (cited in bhb-rh-role note);
`[inferred]` the Guth–Maynard density exponent and its exact gap are unknown until M1/M3 read the
source — M3 must not assume a value; `[inferred]` the ζ″-moment has no unconditional bound in the
literature (absence-of-evidence, flagged as blocker not impossibility).

---

## 8. Handoff

- **Next step:** hand this plan to `reviewer` (maker/checker split); after approval, dispatch
  **M1 → executioner** (a literature/gap-table task, read-only), then M2 and M3 as two parallel
  executioner tasks.
- **First executable step (single, atomic):** M1 — build the route-gap table (Box b, Density
  exponent, ζ″-moment) from literature + the two source notes; no compute.
- **Reversibility:** M1–M3 are Type-2 (two-way); M4/M5 are Type-1 (one-way) and are gated.
