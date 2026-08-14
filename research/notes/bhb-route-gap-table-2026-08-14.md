# Route-gap table: BHB partial unconditionalization (M1)

**Agent:** builder (atomic research deliverable). **Date:** 2026-08-14.
**Scope:** closed-form + literature only (no compute). This is the M1 artifact of
`bhb-unconditionalization-plan-2026-08-14.md`.
**Sources read:** hooks/agents.md (charter); bhb-unconditionalization-plan-2026-08-14.md (M1 spec);
bhb-rh-role-2026-08-14.md; bhb-lemmaN-firstcheck-2026-08-14.md; gm-box-certifiability-2026-08-14.md;
s4h-resource-bottleneck-analysis + s4h-epistemology (read & applied).

---

## 0. One-line answer

Every substitute input for the single target `E/S₂ < 3.11%` is unproven, and **two of the three
"routes" collapse to the same gap**: the box and the density route both require one
moving-boundary zero-location input at `b ≈ 0.05` (`|β−1/2| < 0.05/L` ⟺
`N(1/2 + 0.05/L, T) = o(T log T)`), which is the **binding bottleneck** and the only one whose gap
is PROVEN (Shape-1 blindness is a theorem; Ingham's log-power `k = 5 → k < 1` is a theorem-level
log gap). The ζ″-moment is a genuine second open problem but is *bypassable* (the density route
avoids Taylor), so it is a route-selector, not the system constraint. Recommended next: dispatch
**M2 and M3 in parallel**, with M3 carrying the pre-registered belief that Route D reduces to the
same `k < 1` moving-boundary count.

---

## 1. The route-gap table

| Substitute input | Strongest known (unconditional) | Needed for 3.11% slack | Gap | Source | Label |
|---|---|---|---|---|---|
| **Box b** | BGSTB `b = 1/2` gate (`|β−1/2| < 1/(2 log T)`), ⇒ 61.7% of zeros **on the line** — but at the *pair-correlation* level (Montgomery 2/3), **not** the `E`-small discrete-moment level BHB needs | `b ≈ 0.05` (optimistic, ζ″-free): `Δ(T) = b/L`, `b = 0.0311/(2√r)`, `r ≈ 0.0777` | ~10× width (`1/2 → 0.05`) **plus** a level transfer (proportion/pair-correlation → uniform/molified `F = Bζ′`); no unconditional box at any `b < 1` at the BHB level | bhb-lemmaN-firstcheck §5; bhb-rh-role §3 | PROVEN (arithmetic) / INCONCLUSIVE (existence of any `b<1` BHB-level box) |
| **Density exponent** | Guth–Maynard (2024), Shape-1 fixed-σ: `N(σ,T) ≪ T^{a(1−σ)+ε}`, `σ ≥ σ₀ > 1/2`, `a ≤ 2` | Moving-boundary (Shape-2) density hypothesis at `b ≈ 0.05`: `N(1/2 + b/L, T) = o(T log T)`, i.e. exponent `1 − c/L` with polylog power **`k < 1`** (marginal `k = 1` certifies only `b > log(4π)/c ≈ 1.26`) | **Scale-gap lemma: fixed-σ (Shape-1) is provably blind to every shrinking box**; best known moving-boundary (Ingham, `c = 4/3`, `k = 5`) reaches only `b ~ 3 log log T` — a log-power gap `k = 5 → k < 1` | gm-box-certifiability §3–§5 | PROVEN (Shape-1 blindness; Ingham gap) / [inferred] (GM params; Ingham uniformity) |
| **ζ″-moment** | **Nothing.** `Σ_{0<γ≤T}|B(ρ)|²|ζ″(ρ)|²` has no unconditional bound in BHB Lemma 1 (a ζ′-moment theorem) or the literature read; the pending `bhb-zeta2-moment` note is not yet written | `M = O(L²·S₂)` with an explicit `r′` constant (`Σ|Bζ″|² ≪ r′·L²·S₂`) | The whole question — weighted discrete **second moment of ζ″** (double pole at `s=1`, no horizontal-segment analysis in the paper); not implied by `S₁, S₂` | bhb-lemmaN-firstcheck §4(b) | INCONCLUSIVE (absence-of-evidence; flagged as blocker, not impossibility) |
| **S(T)** | `S(T) = O(log T)` unconditional (Littlewood, classical) | A bound strong enough to certify `N(1/2 + 0.05/L, T) = o(T log T)` (the `k<1` count); natural candidate `S(T) = o(log T)` *with a rate that transfers* | The **transfer** `S(T)`-bound → moving-boundary count is itself unproven; `S(T) = O(log T)` is PROVEN, `S(T) = o(log T)` is OPEN (RH gives `O(log T/log log T)`), and whether *any* S(T) bound alone yields `k < 1` is OPEN | Littlewood (classical); gm-box §8 | PROVEN (known bound) / OPEN (needed + transfer) |

### Cell-by-cell notes

**Box b.** The needed value is PROVEN arithmetic: `b = 0.0311/(2√r)` with `r = 99/1274 ≈ 0.0777`
gives `b ≈ 0.049` (net constant 57/64) to `0.056` (diagonal), i.e. **`b ≈ 0.05`** — about 10×
narrower than BGSTB's `b = 1/2`. Two honest caveats: (i) BGSTB's `1/(2 log T)` box is a
*proportion-on-the-line* statement (61.7% of zeros **on the line**, not "simple" — "simple" is the
BHB-level object), and it certifies a proportion, not the *uniform* box the Taylor+Cauchy–Schwarz
bound uses; (ii) it lives at the pair-correlation level and does not bound the `E`-small
discrete-moment sum BHB needs. **No unconditional box theorem at any `b < 1` at the BHB level is
known** (absence-of-evidence; flagged, not proved impossible).

**Density exponent.** The decisive quantity is the **polylog power `k`**, not the exponent value
(gm-box §4): `k = 0` ⇒ full box for every fixed `b`; `k = 1` ⇒ positive proportion iff
`b > log(4π)/c` (≈ 1.26 at `c = 2`); `k ≥ 2` ⇒ vacuous. The needed `b ≈ 0.05` therefore needs
**`k < 1`** at the moving boundary `σ_b = 1/2 + 0.05/L`. The scale-gap lemma (gm-box §3) proves
**any fixed-σ Shape-1 ZDE — Guth–Maynard included — certifies no shrinking box at all**, and the
best known Shape-2 estimate (Ingham, `c = 4/3`, `k = 5`) certifies only `b ~ 3 log log T`, a
log-log factor short. The task's "(1.6)-type" does not match any repo number (`c = 4/3` Ingham,
`c = 2` DH); flagged `[unresolved]` — the verdict does not depend on it.

**ζ″-moment.** This is `Σ|B(ρ)|²|ζ″(ρ)|²`, the "bad part" of `Σ|F′|² = Σ|B′ζ′ + Bζ″|²` in
Lemma N's Cauchy–Schwarz step. BHB Lemma 1 evaluates ζ′-type moments only; the ζ″ integrand has a
double pole at `s = 1` and no error analysis in the paper. `r′` is the ζ″-analogue of `r ≈ 0.0777`;
its very existence is unproven.

**S(T).** Added per the task. `S(T) = O(log T)` (Littlewood) is the unconditional record. The
needed input is *not* literally `S(T) = o(T log T)` (trivially true) — the repo's target
(gm-box §8) is the classification: is `N(1/2 + b/L, T) = o(T log T)` implied by `S(T) = o(log T)`
(or a pair-correlation input)? **Open.** So the S(T) row inherits the *same* moving-boundary gap
as the box/density rows, viewed through an unproven transfer.

---

## 2. Bottleneck verdict (s4h-resource-bottleneck-analysis)

**Process map:** substitute inputs → bound `E` → `E/S₂ < 3.11%` → 19/27 partial-unconditionalization.

**Throughput per stage** (which input is unproven, and how much):

| Input | Unproven? | Gap status | Queues behind it |
|---|---|---|---|
| Box `b ≈ 0.05` | yes | PROVEN (10× + level transfer) | Route A (Taylor) |
| Density exponent (moving-boundary, `k<1`) | yes | PROVEN (Shape-1 blind; Ingham `k=5`) | Route D (no Taylor) |
| ζ″-moment `O(L²S₂)` | yes | OPEN (full) | Route A only |
| S(T) `o(log T)`-with-transfer | yes | OPEN (transfer unproven) | — |

**Current bottleneck: the moving-boundary zero-location input at `b ≈ 0.05`**
(`|β−1/2| < 0.05/L` ⟺ `N(1/2 + 0.05/L, T) = o(T log T)`, `k < 1`).

Why it is the constraint, not the ζ″-moment:
1. **Every live route needs it.** Route A needs its box half; Route D needs the *identical*
   count `N(σ_b, T) = o(T log T)` — gm-box §1 PROVES the box condition **is** that count. The
   "three routes" are really two routes over **one** binding input (A: box + ζ″; D: box-only).
2. **It is the only gap that is PROVEN closed for known methods.** Shape-1 (fixed-σ) blindness is
   a theorem; Ingham's `k = 5` is a documented log-power gap. The ζ″-gap is OPEN (worse in
   absolute ignorance) but **bypassable** via Route D.
3. **Theory-of-Constraints reading:** improving the ζ″-moment (Route C / M4) is
   *non-bottleneck optimization* — it cannot move `E/S₂` unless the box is also solved, and the
   box can be attacked directly (Route D) without ζ″. Work queued behind the box (Routes A, C, D)
   all waits on `k < 1`; nothing waits on ζ″ that cannot reroute.

---

## 3. M2/M3 dispatch recommendation (per plan gating)

- **M1's decision gate** ("kill routes where needed ≫ known with no technique bridging"): the
  *box half* of Route A and the whole of Route D already show **needed ≫ known**, with the gap
  PROVEN for the density form. **But do not kill them here** — M1's job is to quantify, and M2/M3
  are the cheap two-way-door probes that produce the *technique-bridging* verdicts.
- **Dispatch M2 (functional-equation ζ″-elimination) and M3 (density exponent gap) in parallel**
  (plan §4.2; independent, no shared state).
- **M3 must be pre-registered:** its live/gap question is *not* "is the GM exponent large enough"
  (it cannot be — Shape-1 blindness, PROVEN) but "does the **weighted** off-line integral
  `∫ N(σ,T) d|F|² ≪ 0.0311·S₂` reduce to the `k < 1` moving-boundary count, or is a weaker
  Shape-1 estimate sufficient at the *weighted* level?" — expected verdict GAP, expected one
  `<1m` probe only if the integral lacks closed form.
- **M4 (ζ″-moment theorem) and M5 (box attainment) stay gated** behind M2/M3 per plan §4.3.
  Given the bottleneck verdict, M5 is the higher-value Type-1 door *if* it can be re-aimed from
  "attain `b ≈ 0.05`" to "classify the `k < 1` moving-boundary count" — see next note.

---

## 4. Labels & assumptions

| Claim | Label |
|---|---|
| Target `E/S₂ < 0.0311` to clear 0.6818 | PROVEN (arithmetic) |
| Needed box `b ≈ 0.05` (`= 0.0311/(2√r)`, `r ≈ 0.0777`) | PROVEN (form) / rough (value), conditional on ζ″ |
| BGSTB box is `b = 1/2` (`1/(2 log T)`), 61.7% **on the line** | PROVEN (published); pair-correlation level |
| No unconditional box at any `b < 1` at the BHB discrete-moment level | INCONCLUSIVE (absence-of-evidence) |
| Box condition ⟺ `N(σ_b, T) = o(T log T)` | PROVEN (gm-box §1) |
| Fixed-σ (Shape-1) ZDE certifies no shrinking box (GM included) | PROVEN (gm-box §3) |
| Needed density input: moving-boundary, `k < 1`, at `b ≈ 0.05` | PROVEN (gm-box §4) |
| Ingham `c = 4/3`, `k = 5`; certifies only `b ~ 3 log log T` | PROVEN given uniform form; uniformity [inferred] |
| `Σ|Bζ″|² ≪ L²·S₂` | INCONCLUSIVE (open problem; the blocker) |
| `S(T) = O(log T)` | PROVEN (Littlewood, classical) |
| `S(T) = o(log T)` ⇒ `N(σ_b,T) = o(T log T)` | OPEN (transfer unproven; gm-box §8) |

**Assumptions (tagged):** `[verified]` all PROVEN labels above trace to the cited repo notes
(which derive from arXiv:1302.5018 text and closed-form algebra); `[inferred]` Guth–Maynard's
exact `(a, σ₀)` and arXiv id are **not** pinned this session — gm-box flags GM unread; M3's source
read must pin them (`[CITATION NEEDED]` if cited outside the repo before then). `[flagged]` the
task prompt's "BGSTB b=1 gate" and "61.7% simple": repo-canonical is **b = 1/2** and
**61.7% on the line** (plan §1/§3-verification; bhb-rh-role §3; gm-box §1); the M1 verification
criterion requires the `b = 1/2` cell, so this note uses `b = 1/2` and flags "b=1" / "simple" for
reviewer reconciliation. `[unresolved]` "(1.6)-type" density exponent — matches no repo number
(`c = 4/3`, `c = 2`); verdict unaffected.

No computation performed — every load-bearing number is hand algebra (`b ≈ 0.05`, `r ≈ 0.0777`,
`log(4π) ≈ 2.531`, `k = 5`), and a numerical check would not change any belief (compute
discipline, hooks §METHOD FIRST).

---

## 5. Handoff

- **Binding bottleneck:** the moving-boundary zero-location input at `b ≈ 0.05`
  (`N(1/2+0.05/L, T) = o(T log T)`, polylog power `k < 1`) — required by both the box and density
  routes, PROVEN beyond known methods; the ζ″-moment is a bypassable secondary gap.
- **Recommended next milestone:** M2 and M3 in parallel (M3 pre-registered to test the
  weighted-integral reduction to the `k < 1` count); M4/M5 stay gated.
- **Note path:** `/home/vstaln/riemann/research/notes/bhb-route-gap-table-2026-08-14.md`
