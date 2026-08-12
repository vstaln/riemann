# SYNTHESIS — combining existing research (s4h) into a ranked set of untried combinations

**Date:** 2026-08-13 (overnight). **Method:** s4h master orchestration — intake → cross-check
→ combine → rank → execute. This document does NOT generate new research; it merges the
existing corpus (10 cloud idea catalogs + local attack notes + the retraction) and extracts the
*combinations* of existing pieces that have not yet been tried. **Labels:** PROVEN / CHECKED
NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE per hooks/agents.md.

---

## 0. The corpus (what exists, de-duplicated)

**Certified/structural facts (all committed, post-retraction):**
- Corrected bound **0.6730690** at (α=1.49, psum=1/220, eps=0.007759, m=137) — CERTIFIED twice
  with the fixed verifier (retraction-673-invalid.md). Beats ainta, below trmdy/tawanerguo.
- Window ceiling **H = 0.6725007** — the global max of the Montgomery functional Q (attack-kernel.md,
  PROVEN in Lean; re-confirmed numerically this synthesis — see synthesis-crosscheck note).
- Class ceiling **0.6818** (attack-ceiling.md, PROVEN in Lean modulo EnclOK).
- n-point: F_n/n falls with n — DEAD (exec-npoint.md). Two-tone: H max = classic constant — DEAD.
- Third moment: unconditional version does NOT break 5/6 (attack-thirdmoment.md, PROVEN); conditional λ=1 gives 0.8359.

**Idea catalogs (the research to combine):**
- `idea-constraint.md` — 4 constraints (E ε-floor, W window, B block, G gap-structure); 15 inversions.
- `idea-systems.md` — feedback loops, partial-derivative leverage, 10 ideas (I1–I10).
- `idea-lateral.md`, `idea-analogy.md`, `idea-network.md`, `idea-probability.md`,
  `idea-historical.md`, `idea-provocation.md`, `idea-random.md`, `idea-analogy-x1.md`.
- Local: attack-kernel/ceiling/multiplicity/mollifier/lfunctions/finitet/thirdmoment,
  ladder-consecutive-zeros, ah-lattice-trpsi, adt69-crystal, discovery-gram-stability.

---

## 1. Cross-check resolution (the contradictions found and settled)

A synthesis must first resolve cross-source conflicts. Two were found:

### Conflict 1 — the window frequency (SETTLED, see synthesis-crosscheck-2026-08-13.md)
`idea-constraint.md`'s **#1 idea "W-1"** claims changing α from √2 to 1.0 raises H from 0.6725
to **0.8579 (+27.5pp)**. This is a **units error**: it substitutes √2→α inside the scalar formula
`3/2 − (1/α)cot(1/α)`, which only holds AT α=√2. The true Montgomery functional Q for cos(λu)
has its global max 0.6725007 exactly at λ=√2 (verified to 30 digits). **The window is NOT a lever.**

### Conflict 2 — the "record" eps (SETTLED by the retraction)
Multiple catalogs reproduce "0.6732629" as the certified record. That record is RETRACTED
(kernel double-normalization). The corrected certified floor at psum=1/220 is eps=0.007759
(not 0.00806), giving 0.6730690. All catalogs' "interpolated eps beats record" claims are moot.

**Net effect:** removing these two phantoms (W-1's +27.5pp, and the buggy record) leaves a
*smaller but honest* lever set.

---

## 2. The combined leverage map (what all catalogs agree on)

Across idea-systems (partial derivatives), idea-constraint (hardness audit), and the retraction
arithmetic, the bound `(H − τ)/(1 − B/m)` has exactly these live knobs:

| knob | derivative | status | catalog consensus |
|---|---|---|---|
| H (window) | +1.0 | **capped at 0.6725007** (PROVEN) | DEAD — every window family ≤ ceiling (systems §4) |
| eps (floor) | +0.64, concave | **0.007759 certified** at psum=1/220 | the binding quantity; crystal family saturates it |
| psum (tax) | −0.96, linear | coupled to eps via k≈0.83 | highest leverage but coupled (negative feedback loop 4) |
| m (block) | ~0 | already optimal (m*=137) | retune buys nothing |
| denominator B/m | amplifier ×1.0078 | nearly inert | I9 is the only route to make it bite |

**The single cross-catalog convergence:** the ε-floor is saturated by a specific **crystal
adversary family** — alternating gaps at the kernel zeros z1≈1.057, z2≈2.030, z3≈3.020
(idea-constraint §1.4 "crystal", adt69-crystal, ah-lattice-trpsi, ladder-consecutive-zeros).
Every catalog that examined the floor found the SAME minimizer shape. This is the adversary the
method must break.

---

## 3. THE untried combinations (ranked by leverage × feasibility × tooling-readiness)

These are *combinations of existing pieces*, not new research. Each is rated by whether the
existing verifier (`tools/beat673/verify_cos7.py`) can run it tonight.

### C1 — Non-uniform weights to break the crystal (combines I1 + crystal + capacity structure)
**Rank: #1. Tooling: READY (WEIGHTS_JSON supported).**
The 7-point mechanism uses **uniform** weights `a_ij = 2/(n−(j−i))` — each span r gets total
weight exactly 2 (the capacity bound `Σ_i a_{i,i+r} ≤ 2` is saturated). But the crystal adversary
is an *alternating* configuration that is worst for the *uniform* weighting. A non-uniform weight
profile — concentrating weight on the spans where the crystal is weakest (i.e. where k² is large)
while de-weighting the spans where the crystal pins the floor — could certify a **strictly higher
eps at the same pressure**, breaking the eps–psum coupling (the systems catalog's I1, its #1
structural lever after §4 closed the window door). **No one has run a weight search.** The
verifier already accepts arbitrary weights and enforces the capacity constraint.
- **Mechanism (why it can help):** the floor F = p·Σg + Σ a_ij k²(g_j − g_i). The crystal sets
  k² to its smallest attainable values on the spans it occupies. If we *re-weight* away from the
  crystal's occupied spans and toward spans where the crystal cannot be small, the minimum
  over configurations rises.
- **Test:** binary-search max certifiable eps over a simplex of weight profiles, α=1.49, psum=1/220.
- **Expected:** CONJECTURED — even +5e-5 on eps would move the bound above trmdy (need eps≥0.00787).

### C2 — Read-constrained τ-floor (combines E-1 + crystal family + GUE-flat rows)
**Rank: #2. Tooling: needs a read-feasibility filter (new, small).**
The crystal family saturates the floor *only because it is an unconstrained adversarial gap law*.
But its pair-correlation function is spiky at the kernel zeros — it does NOT match ζ's observed
GUE-flat rows (s_j ≈ 1, the form factor). If the certificate class may read the form factor on
[0,1] (it may — bandwidth one), then the crystal is read-INFEASIBLE and the certified ε jumps
above the crystal floor. This is idea-constraint's flagship E-1 (CI-74) + the G-cluster's
"periodic laws are exactly the read-infeasible crystals" cross-link (G-5). **Never executed.**
- **Test:** minimize F over configurations whose form factor is GUE-flat (|S(j) − j| ≤ δ, the
  NearCUE condition) — a constrained LP that excludes the crystal.
- **Expected:** CONJECTURED — if the crystal is excluded, the floor could rise 10–100× (toward
  the law's τ≈0.27), which would break the class ceiling. But need to check the certificate
  class *may* actually read the form factor at this granularity.

### C3 — Certify eps at the H-peak (combines I6 + retraction-corrected floor)
**Rank: #3. Tooling: READY (binary search at α=√2).**
The record is at α=1.49 (H=0.6724219) because eps is higher there. But the H-peak is at α=√2
(H=0.6725007, +7.9e-5). The corrected-kernel eps at α=√2 is lower, but the trade-off was never
re-optimized with the FIXED verifier. **Test:** binary-search max eps at α=√2, psum=1/220 (and a
few nearby α), recompute the bound. Even a modest eps there beats the α=1.49 record's H.
- **Expected:** CONJECTURED — the corrected floor at α=√2 is ~0.0075 (vs 0.007759 at 1.49);
  bound (H=0.6725007, eps=0.0075, m*) ≈ 0.67312, a real certified gain over 0.6730690.

### C4 — Second-moment denominator (I9) — the only route to 0.68+
**Rank: #4 (highest ceiling, highest effort). Tooling: NOT ready (pure theory).**
The denominator `1 − B/m` is a ×1.008 amplifier — nearly inert. A higher-moment (‖·‖⁴_F or tr P³)
bound would replace it with a larger amplifier, making every H and eps gain count ~50× more
(systems §5 I9). This is the paper's §7.5(e) territory, PROVEN to add nothing for the *odd*
moments at λ<2/3, but the *denominator* reading is different from the *n₊-bound* reading the
paper dismissed. **Long shot, not tonight.**

---

## 4. What I am executing now

C1 (weight search) is the only untried combination with tooling ready tonight and a real chance
to move the corrected bound. I will:
1. Establish the corrected uniform-weight baseline (eps=0.007759 at psum=1/220 — already certified).
2. Search a simplex of non-uniform weight profiles for a higher certifiable eps at the same pressure.
3. If any profile certifies eps ≥ 0.00787, recompute the bound — that beats trmdy.

C3 (H-peak α) is a cheap parallel binary search and will run if the machine has headroom.

---

## 5. Honesty footer

- All "PROVEN / DEAD" statements trace to the cited committed notes; nothing re-derived here.
- The rankings and "expected" outcomes are CONJECTURED (synthesizer judgment).
- The two contradictions resolved (§1) are the synthesis's own verified findings — the window
  is not a lever (re-proven) and the record is corrected (retraction).
- No new proof is claimed; every numeric claim below will be a `verify_cos7.py` certification
  or an honest FAILED terminal bound.

## 6. Execution results (overnight)

### C3 — H-peak α (√2) — RESULT: NEGATIVE (CHECKED NUMERICALLY)
Binary search at α=√2, psum=1/220, fixed verifier, grid 4000:
- eps certified: **0.00745** (7450/1e6 True; 7460/1e6 False, terminal lower 0.00744)
- bound = (H=0.6725007, eps=0.00745, m=142) = **0.672955** < current 0.6730690
- The α=1.49 point's higher floor (0.007759) outweighs the H-peak's +7.9e-5 H gain.
**Conclusion: the record configuration (α=1.49) is a genuine optimum; α=√2 does not beat it.**

### C3b — H-peak with required-eps threshold — CONFIRMED
The required eps at α=√2 to match 0.6730690 is 0.007636; the certified floor there is only
0.00745 < 0.007636. The gap is real (not a grid artifact: terminal lowers cluster at 0.00744).

### C1 — weight search — IN PROGRESS (see below)
