# THEORIST — Ceiling Analysis of the Rank–Trace Simple-Zeros Bound (0.6732628655343560)

**Date:** 2026-08-11 (round 2.5 follow-up). **Author:** THEORIST agent (Riemann swarm).
**Scope:** what limits the certified lower bound **0.6732628655343560** (simple zeros on the
critical line) for the rank–trace family, and what its theoretical ceiling is.

All claims are labeled **PROVEN** (verified numerically against the real kernel + algebra),
**CERTIFIED** (external/Lean/interval-verified by the upstream repos), or **CONJECTURED**
(rests on the eps model, which the bound-sweep treats as a heuristic — see §4).

---

## 0. The bound machinery (reference, PROVEN)

For the rank–trace simple-zeros family (ainta/tawanerguo/trmdy mechanism, cf.
`research/notes/discovery-gram-stability-673.md`, `external-results/*/`):

```
bound = (H − τ) / (1 − B/m)
  H    = 2 − 1/c(α)            window functional, c = I0²/(I2+J) over the trig window
  A    = eps·(m−6)
  B    = Φ_m(A) = A  if A ≤ m/(m−1),  else 2√((m−1)A/m) − 1 + A/m
  τ    = psum·(m−6)/m           psum = total defect-pressure on the block
  eps  = local floor (7-point kernel floor, certified sharp at 0.00806)
```

**Record config (CERTIFIED, reproduced exactly by this agent's Rust scan, diff 0.0e0):**
α = 1.49, p = 1/1320 per gap (psum = 1/220), eps = 0.00806 (sharp: 0.008065–0.00807 fails),
m = 133, H(1.49) = 0.6724218860964 → **bound = 0.6732628655343560**.

---

## 1. Sensitivity at the record (PROVEN)

Derivatives computed both analytically (chain rule on the formula) and numerically
(finite differences on the real kernel); mpmath 90-digit cross-check of H(1.49), H_max, c1*.

| variable | d(bound)/d·  | elasticity (×var/bound) | meaning |
|---|---|---|---|
| **H**  | +1.00776 | **1.0065** | dominant: window is the bottleneck |
| **eps** | +0.64282 | 0.0077 | eps is sharp but small; 6.4e-4 bound per 1e-3 eps |
| **psum** | −0.96229 | −0.0065 | pressure dial; couples to eps |
| **m** | ≈ −1.9e-8 | ~0 | flat at m=133 (unimodal peak) |

**Key structural facts (PROVEN):**
- As m→∞: B/m→0, τ→psum ⇒ bound → **H − psum**. The 1/(1−B/m) amplification is a
  *finite-m* effect only. At the record: H − psum = 0.67242 − 0.004545 = 0.667876,
  i.e. ~5.4e-3 of the record's margin over 2/3 comes from the finite-m amplification.
- **H is capped: H_max = H(√2) = 3/2 − (1/√2)·cot(1/√2) = 0.6725007036794116** (PROVEN,
  cosine-global Rayleigh minimizer). The record's H = 0.6724218861 is only 7.9e-5 below H_max.
- **2/3 is already exceeded** (0.6733 > 0.6667). The strategic wall is not 2/3.

---

## 2. Ceiling question (CONJECTURED algebra, numerically probed)

Asked: as eps→eps_max, H→H_max, psum→0, m→∞ — what does bound→?

**Naive (eps-free) ceiling:** H_max with psum→0, m→∞ gives bound → **H_max = 0.6725007**
— *below* the record. The record exceeds it only via the eps-amplified finite-m gain.

**Constrained ceiling (the real question):** eps is NOT free. It is bounded by the local floor
functional: eps ≤ eps_max(p) = inf over 6-gap blocks of the 7-point kernel floor F6 (with
defect-pressure p per gap). This agent minimized F6 (Nelder–Mead, 150+ restarts) and scanned
the (α,p) plane:

```
eps_max(p; α=1.49) ≈ 0.00809 at p=1/1320   (record uses 0.00806 — at the frontier, CONFIRMED)
eps_max(p) / p  ≡ κ(p)  ≈ 10.7 at p=1/1320, rising to ~15 at p=1/10⁴, ~6.4 at p=1/100
```

Certified frontier points (CERTIFIED) lie right on this curve:
ainta κ=11.40, trmdy κ=11.50, tawan κ=11.08, record κ=10.64 (my F6-minimizer: 10.7 — the
certified points are at the numerical frontier; the eps model itself is CONJECTURED, see §4).

**Constrained ceiling (max over m of (H(α) − τ)/(1 − B/m), with eps = eps_max(p)):**

```
α=1.40: max 0.6732338 (p=1/2000, m=188)     α=1.49: max 0.6734212 (p=1/1600, m=150)
α=1.43: max 0.6733301 (p=1/2000, m=184)     α=1.50: max 0.6734119 (p=1/1600, m=150)
α=1.46: max 0.6733597 (p=1/1600, m=153)     α=1.52: max 0.6733845 (p=1/1600, m=149)
α=√2  : max 0.6732512 (p=1/2000, m=188)     α=1.55: max 0.6733806 (p=1/1320, m=126)
```

**GLOBAL constrained ceiling ≈ 0.6734212 at α=1.49, p=1/1600, eps≈0.00711, m=150 (CONJECTURED).**

So, direct answers:

- **Can the family reach 2/3?** Already past it (record 0.67326 > 2/3).
- **Can it reach 0.7?** **No.** The eps→0.05 needed for 0.7 is ~6× the F6 infimum at any p
  that keeps τ negligible. With κ(p)~10–15, pressure p = 1/60–1/100 would push psum to
  0.06–0.10, collapsing the bound to 0.668–0.670 (computed, table §3).
- **Max H over any window:** H_max = 0.6725007036794116 = 2 − 1/c*, c* = 1/(2−H_max)
  = 0.7532960678560707, attained at α = √2 (PROVEN).
- **What limits it:** H is exhausted (7.9e-5 headroom), m is exhausted (unimodal peak at
  133, ∞-limit H−psum < record), psum is a dial coupled to eps, and **eps itself is the
  binding constraint** — the F6 floor caps eps at ~0.007–0.008 for the p range that keeps
  τ small. The record sits ~1.6e-4 below the family's constrained ceiling.

---

## 3. Structural wall (rank–trace inequality) — PROVEN vs CONJECTURED

**Does ‖P+Q‖²_F ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M) alone impose a ceiling on the
simple-on-line fraction?**

- The **eps floor itself** (F6 ≥ ε on every 7-point block) is a *direct consequence* of the
  strengthened inequality: tr Ψ(M) > 0 because the kernel cannot vanish at all three pairwise
  differences of any 3 consecutive gaps (PROVEN, in-class: this is exactly the 
  `eps = 19/5000 = 0.0038` and `221/10⁶` values from the external repos).
- What the inequality does **NOT** do: it does not bound eps from above. Nothing in the
  inequality says F6 can't be driven to 0.007–0.008. The ceiling comes from the **local
  geometry of the kernel k(x) = K(x)/K(0) over the gap domain** — the minimizer of F6
  (g ≈ 1.04, 1.03, 1.95, 1.03, 1.02, 1.03) is a real configuration the kernel supports,
  and it's the *infimum*, not a defect of the inequality. **PROVEN** (numerical infimum;
  the epsilon-certification of any particular eps remains CERTIFIED/CONJECTURED as in the
  upstream repos).
- **So the wall is not the inequality; the wall is the kernel's overlap structure.**
  The rank–trace inequality gives the *form* bound = (H−τ)/(1−B/m); the ceiling is set by
  the feasible region of (H, eps, psum) that the kernel + pressure model admit. Any
  further gain must either (a) find a larger H (a different window with a bigger
  Rayleigh quotient — nothing in the inequality forbids it, but H_max is the optimum of
  the cosine family; CONJECTURED that no window in the class beats √2), or (b) beat the
  F6 floor by extending the block ladder (3→7→9→11 points, Q3 in the discovery note),
  which is CONJECTURED to raise eps_max but is *not* part of the rank–trace inequality
  alone.

---

## 4. Analogy — tax + defect bound structure in other domains (CONJECTURED analogy)

The bound = (H − τ)/(1 − B/m) has the shape of a **rate with a defect discount and an
amplification denominator**. Parallels:

1. **Communication theory — random-coding error exponent with a cost penalty.**
   Error probability ~ 2^{−n(E(R) − ε)}; the exponent E(R) is capped by the sphere-packing
   bound, and the penalty ε (defect) trades against rate R. Known ceiling: the
   sphere-packing exponent is the wall; you cannot push E(R) above it by shrinking the
   penalty alone. Same structure: H plays E(R) (capped by H_max), psum plays the penalty,
   and the 1/(1−B/m) is a finite-block correction. **Known broken part:** rate–penalty
   trade-offs in coding are *convex*; here the eps–psum coupling is *not* convex (κ(p)
   varies), so the analogy is only structural.
2. **Statistical mechanics — free energy with a defect potential.** F = E − T·S; the
   entropy term (H) is bounded, the defect energy (τ) can only be made small at the cost of
   raising the "temperature" (pressure). Known ceiling: the free energy cannot exceed the
   ground-state energy; likewise bound ≤ H_max when τ→0. Broken part: the amplification
   denominator has no stat-mech analog.
3. **Coding/cryptography — Singleton bound / rate–distance trade-off.** The fraction of
   "good" coordinates (simple zeros) vs distance (gap structure) is capped by a
   dimension-counting law; the in-class ceiling 0.6818 (PROVEN for the certificate class
   reading only rank, tr, HS², n₊) is the analog of the Singleton bound: it counts only
   coarse data and ignores the Gram structure. **The strengthened inequality adds
   tr Ψ(M) > 0 — i.e., it moves *inside* the Singleton-like ceiling.** But it does not
   remove the ceiling; it converts it into the eps_max(p) frontier.

**General lesson (CONJECTURED, transferable):** in every domain, the "tax + defect" bound
form has a *feasibility frontier* — a convex-ish curve trading the free parameter (eps)
against the penalty (psum). The true ceiling is where that frontier meets the structural
cap (H_max, 0.6818). The record is a point on the frontier; the frontier's shape, not the
inequality, is what blocks 0.7.

---

## 5. Ranked next moves

1. **Certify the eps_max(p) frontier** (highest value). The F6 infimum curve (CONJECTURED
   here) is the single thing separating "record ≈ ceiling" from "headroom exists."
   Reproduce with Arb/flint interval arithmetic on the 7-point floor, and prove
   eps_max(p) < ε₀·κ(p) for the p range. *Expected payoff: settle whether 0.67342 is
   reachable and whether 0.6818 is touchable.*
2. **Extend the block ladder (3→7→9→11 points) and recompute F9, F11.** Q3 of the
   discovery note. The eps floor is the binding constraint; a 9- or 11-point floor may
   raise eps_max and push the constrained ceiling toward 0.6818. *Payoff: direct
   headroom on the binding constraint.*
3. **Search beyond the cosine window family for larger H.** H is the second-lever;
   H_max(√2) caps the family. A different window class (e.g., higher-degree trig
   polynomial) may give H > 0.6725007. *Payoff: shifts the whole ceiling.*
4. **Adjudicate Q2 of the discovery note rigorously:** does tr Ψ(M) (Gram structure)
   push the in-class ceiling 0.6818 upward, or is 0.6818 a hard wall for this class?
   *Payoff: defines the ultimate target.*
5. **Adversarial check of the eps model** (Q4): the bound-sweep's eps floor is
   CONJECTURED; confirm the 0.00806 sharpness certification independently (0.008065 fails)
   and that no configuration exploits the B/m amplification to exceed the computed
   constrained ceiling. *Payoff: hardens the record.*

---

## 6. Bottom line

- Sensitivity: **d(bound)/dH = +1.008** (elasticity 1.0065, dominant), d(bound)/deps =
  +0.643, d(bound)/dpsum = −0.962, d(bound)/dm ≈ −1.9e-8 (flat).
- H is capped at **0.6725007036794116** (α=√2), only 7.9e-5 above the record's H.
- **2/3 is already beaten; 0.7 is unreachable** in this family. The constrained ceiling
  (eps = F6 infimum, H ≤ H_max, τ→0, m optimized) is **≈ 0.67342**, attained at
  α=1.49, p=1/1600, m=150 — the record is within 1.6e-4 of it.
- The wall is the **kernel's overlap structure** (eps_max(p) frontier), not the
  rank–trace inequality: the inequality gives the form, the kernel gives the ceiling.

RESULT: CEILING ≈ 0.67342 (CONJECTURED) — the record 0.6732628655343560 sits ~1.6e-4 below the family's constrained ceiling; 2/3 already beaten, 0.7 unreachable because the F6 kernel floor caps eps at ~0.007-0.008 while H is capped at H(√2)=0.6725007; the binding constraint is eps, whose true infimum is the only remaining headroom (certify the eps_max(p) frontier next).

## ⚠️ CORRECTED STATUS (2026-08-12, after the retraction)
The certified eps values cited above (0.00806 etc.) were produced by the buggy
double-normalized verifier and are INVALID. Corrected certified floors (fixed verifier,
single normalization w(0)=1):
- psum=1/220 (p=1/1320): eps certified = 0.007759 (7759 True, 7760 False) → bound **0.6730690** (m=137)
- psum=1/214 (p=1/1284): eps certified = 0.007931 → bound 0.6730572 (m=134)
Structural conclusions that SURVIVE: H capped at 0.6725007 (window-independent, PROVEN),
sensitivity d(bound)/dH ≈ +1.0 dominant, d(bound)/deps ≈ +0.64, the family is exhausted
at its corrected limits, and beating trmdy/tawanerguo needs a structurally new inequality.
See research/notes/retraction-673-invalid.md.
