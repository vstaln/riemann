# REDISTRIBUTION-FAMILY OPEN PROBLEM — what was searched, what was fixed, and the single most promising unsearched move

**Date:** 2026-08-13 (round 4+). **Agent:** RESEARCH (architect). **Status:** ARGUMENT + OPEN-PROBLEM MAP.
This note is a mathematical argument, not a computation. No new numbers were produced; every number cited is from FINAL-RECORD-2026-08-13.md, coboundary-redistribution-explore.md, coboundary-reopt-corrected.md, attack-ceiling.md, or tools/verify_coboundary_floor.py as quoted.

**Method note (s4h-creativity-lateral-thinking applied).**
- Dominant idea: *the coboundary lever is a 10-parameter linear correction (l,c) on a fixed 6-gap window, and since the LP over (l,c) did not beat tawan, the redistribution lever is near-exhausted.*
- Load-bearing assumptions this framing rests on: (A1) the redistribution must be LINEAR in the gaps; (A2) the window has exactly 6 gaps; (A3) the redistribution must be SEPARABLE (cell-wise, no coupling between adjacent gaps); (A4) psum is a fixed lattice (1/320); (A5) the terminal/large-gap structure (one-body cap at g≈21, per-cell terminal bound) is fixed. Each assumption is a stepping-off point; (A1)+(A3) together are the strongest candidate for a genuine lateral move because the telescoping property that makes a coboundary a valid redistribution does NOT require linearity or separability.

---

## (a) Precise characterization of the searched family (PROVEN from the notes)

The certificate redistributes the multiplicity sum Σmᵢ² between adjacent windows by adding a coboundary to the 6-gap functional density:

```
F_B(g1..g6) = F_0(g1..g6) + U(g2..g6) − U(g1..g5),        (coboundary-redistribution-explore §2)
U(g1..g5)   = (54g1 −123g2 +123g4 −54g5)/1920000
            + (5971/300000)(w(g1)+w(g2)−w(g4)−w(g5)),    (tawan's U, decoded to 10+ digits)
```

**Free parameters that WERE searched:**
1. **α (cosine-window parameter).** Swept 1.47 → 1.49 → √2 → boundary α* ∈ (1.4638, 1.464), with tawan's (l,c) held fixed. The record sits at the eps-feasibility boundary: lowest α still certifying eps=0.0062, maximizing H(α). H(1.464)=0.672467425578. [PROVEN: FINAL-RECORD table; α-transfer table §3 of explore note]
2. **eps (certified floor target).** 620/1e5 certifies; 630/1e5 FAILS terminal-cell. eps=0.0062 is PROVEN the ceiling for the current coefficient set. [PROVEN]
3. **m (level/knot count in the bound).** m=171 optimal at the record; m=183 (tawan), m=176 (√2). [PROVEN]
4. **The 10 coefficients (l₁..l₅, c₁..c₅)** — in the LP attempt only: `F_B` is linear in (l,c), so max-min over a config set is a linear program. Both LP attempts (small-gap-only; full-adverse incl. huge gaps at every position) were interval-certified WORSE than tawan (floor 0.006126 vs tawan 0.006467; the LP "over-rotates" at the c-bound ±0.06 and loses support at huge-gap configs, dipping to 0.0048). [PROVEN worse at certification; CONJECTURED near-optimal in family — the LP's adverse config set was NOT exhausted, per explore §7 INCONCLUSIVE]

**Structural choices that were FIXED (not searched):**
- **Block/window size k=6** (the coboundary is a 5-term telescoping difference on a 6-gap window). No k≠6 variant.
- **Base density F_0** — the 6-gap uniform functional density is never reshaped; only the perturbation U moves.
- **Weight shape for the |s−s′| term: w(i,j) = 2/(7−(j−i))** (the "uniform 7-pt" weights). Fixed.
- **Form of U: linear and separable in (gᵢ, w(gᵢ))**. This is the deepest fixed choice — see (b).
- **psum lattice = 1/320** (Σpᵢ = 1/320; τ = (1/320)(m−6)/m enters the numerator NEGATIVELY). Held at tawan's value; never re-optimized jointly with (l,c).
- **Cap scheme**: cap_scheme='coboundary', one-body pruning exploring gaps up to g≈21, per-terminal-cell enclosure. Fixed.
- **Window family**: cosine(αx) only. (This is separately PROVEN window-optimal within bandwidth 1 for the density H — Theorem D 0.6725 — but the *joint* (window × eps × U) feasibility boundary is what binds here, and only the cosine family was swept.)

The bound chain (PROVEN, exact): bound = (H(α) − τ)/(1 − B/m), τ = (1/320)(m−6)/m, giving 0.6734808616745137 @ α=1.464, eps=0.0062, m=171, 1,096,556 nodes (3 identical runs).

**What the eps ceiling is actually set by (PROVEN/CONJECTURED):**
- The true (float) crystal floor is ~0.0063–0.0066 — ABOVE the certified 0.0062. Margin at α=1.464 is only ~1–3e-4. [CHECKED NUMERICALLY, non-rigorous float]
- 630/1e5 fails at a TERMINAL CELL — i.e., the certified ceiling is set by large-gap / terminal-cell enclosure tightness, not by the crystals. [PROVEN: verifier output]
- The LP's failure mode was the two-large-gap / huge-gap configs: "the LP family is not closed under two-large-gap configs" (FINAL-RECORD honesty ledger). [PROVEN at certification]

---

## (b) ≥3 structural variations NOT searched, with analysis

### V1. NONLINEAR and/or COUPLED coboundary U (drops assumptions A1+A3)

**The move.** Replace U(g₁..g₅) = Σ(lᵢgᵢ + cᵢw(gᵢ)) with a U that is (i) nonlinear in g — e.g. U = Σ h(gᵢ) for a convex/saturating h, or (ii) couples adjacent cells — e.g. U = Σ φ(gᵢ, gᵢ₊₁) or a term in |gᵢ − gᵢ₊₁| or gᵢgᵢ₊₁. Keep the coboundary *shape*: F_B = F₀ + U(g₂..g₆) − U(g₁..g₅).

**Why it is valid (PROVEN, structural).** The telescoping identity that makes a coboundary invisible on periodic sequences — Σ over a long run of windows of [U(g₂..g₆) − U(g₁..g₅)] telescopes to boundary terms — holds for **any** function U of a 5-gap window. Linearity and separability were choices of the search, not requirements of the certificate. A coupled term gᵢgᵢ₊₁ or |gᵢ−gᵢ₊₁| still telescopes identically. So V1 stays **inside the certificate class**; it is a redistribution-family member, just not a linear one.

**Why it could plausibly lower the floor below 0.0062 / raise the bound (CONJECTURED).**
- The binding failure of the linear LP was documented: pressure concentrated on one gap (p₃ ≈ 88%), c saturated at ±0.06, and huge-gap or two-large-gap configs then lost support (dip to 0.0048). A **convex, saturating h** can concentrate redistribution mass where the crystals live (small gaps ~1.05–1.99) while keeping F_B → +∞ as any single gap → ∞ — the qualitative property tawan has and the LP lost. That directly targets the terminal-cell constraint that stops 630/1e5.
- A **coupled term φ(gᵢ,gᵢ₊₁)** can sense the alternating structure of the period-2/3 crystals (1.05,1.98,1.05,1.98,… and 1.996,1.051,1.996,…) that a separable U cannot distinguish from a generic point — i.e., it can penalize the exact minimizer shape. Since the certified eps sits only 1–3e-4 above the crystal floor at α=1.464, even a small lift of the crystal floor converts into a higher certifiable eps.
- **Why it cannot be dismissed by symmetry (PROVEN reasoning).** No symmetry of the certificate maps a nonlinear U to a linear one; the searched family is the linear subspace, and the nonlinear extension is a strictly larger set. The LP's failure is not evidence about the nonlinear closure — the LP was restricted to linear (l,c) by construction.

**Belief a computation would change.** We currently believe eps=0.0062 is "exact" and near the redistribution ceiling. V1's test: does there exist a telescoping (nonlinear) U with interval-certified floor ≥ 0.0063 at the same (α, psum, m), i.e., is the 630-terminal-cell failure an artifact of *linearity* rather than of the coboundary concept? Expected direction: yes; a saturating-convex h should raise the terminal-cell floor while preserving the large-gap growth.

### V2. Block/window size k ≠ 6 (drops assumption A2)

**The move.** Use a k-gap window (k=5, 7, 8) with coboundary U(g₂..gₖ) − U(g₁..gₖ₋₁), re-solving the weight lattice that comes with it.

**Why it could help (CONJECTURED).** The certified ceiling is set by terminal cells with huge gaps. In a block certificate, a single huge gap is diluted over k−1 normal gaps; larger k dilutes the per-block dip of the worst-case "huge gap at one position" configuration, which can raise the terminal-cell floor. Also the crystal geometry of the k-window differs, potentially lifting the period-2/3 floor.

**Why it might NOT help (CONJECTURED).** k is tied to the weight lattice: w(i,j)=2/(7−(j−i)) is a 7-point combinatorial weight (the multiplicity-sum decomposition Σmᵢ² over 7 consecutive points). Changing k likely changes the base F₀ and the whole rank–trace setup, i.e., it exits the *redistribution-family* lever and re-enters certificate-design. It is the bolder, higher-risk move. Not provably reducible to the searched family (no symmetry maps k=6 to k≠6), but the burden of proof is that the 6-gap choice was not arbitrary.

### V3. Joint psum-lattice search (drops assumption A4)

**The move.** Re-optimize (psum, l, c) jointly — currently psum=1/320 is frozen at tawan's value while (l,c) were optimized (incompletely) at that psum.

**Why it could help (CONJECTURED).** τ = psum·(m−6)/m enters the bound numerator NEGATIVELY, so psum trades off against eps: smaller psum raises the bound directly (smaller τ) but shrinks the redistribution budget (lower crystal/terminal floor); larger psum does the reverse. The current point is a balance only for *tawan's coefficients*; the joint optimum (psum*, l*, c*) is uncomputed. If floor(psum) grows sub-linearly near the operating point, a smaller psum at a re-tuned (l,c) wins outright.
**Why it might NOT help (CONJECTURED).** The record's α was already chosen at the eps-feasibility boundary, which implicitly prices in psum; the (psum, α) plane was never swept, so there is no evidence the current psum is suboptimal — but also none that it is optimal. This is the cheap move (one additional scalar in an existing LP-style search).

### V4. Different weight shape w for the |s−s′| term (variant of A5)

**The move.** Replace w(i,j)=2/(7−(j−i)) with another positive weight profile, re-solving (l,c) for it.

**Analysis — likely NOT a free lever (CONJECTURED, with reason).** These weights look like the combinatorial coefficients of the multiplicity decomposition (how Σmᵢ² splits over a 7-point block, i.e., the trace structure of the quadratic form). If they are pinned by the algebra (Sylvester / rank–trace), varying them leaves the certificate class rather than varying within the redistribution family — the same status as V2's risk. Unless the notes' derivation shows w free, this is the weakest candidate; flag for a 30-minute check of where 2/(7−(j−i)) comes from in the underlying theorem before funding it.

### V5. (Negative result, kept for honesty) "Asymmetric coefficients"

**Already in the searched family (PROVEN).** The LP maximized over all (l₁..l₅, c₁..c₅) with NO symmetry constraint; the family is already fully asymmetric (and tawan's own profile is antisymmetric (54,−123,0,123,−54)). Asymmetry per se therefore cannot be the unsearched lever — any asymmetric linear solution is inside the family the LP explored. What is genuinely open is not asymmetry but (i) the LP's adverse-config closure (two-large-gap configs) and (ii) nonlinearity (V1).

---

## (c) VERDICT — the single most promising next move

**V1: a nonlinear, saturating (and eventually coupled) coboundary U, starting as U = Σ[lᵢgᵢ + cᵢw(gᵢ)] + δ·Σ h(gᵢ) with h convex-saturating, on the SAME 6-gap window, same (α, psum, m).**

- It is the only variation that provably stays inside the certificate class while leaving the searched subspace (telescoping is structural, not linear — PROVEN).
- It attacks the exact documented failure mode: the linear LP lost huge-gap / two-large-gap support (dip to 0.0048) by over-concentrating pressure; tawan's coefficients keep F_B growing as any gap → ∞ and therefore sit at the 620/630 terminal-cell boundary. A saturating-convex h inherits tawan's growth property while freeing the crystal-floor degree of freedom that linear c-bounds blocked.
- The crystal floor sits only ~1–3e-4 above the certified eps at α=1.464, so even a marginal lift of the crystal floor converts directly into a higher certifiable eps and a higher bound (H fixed, τ fixed, B/m fixed ⇒ bound is monotone in eps at fixed m).

**Expected direction of change, stated concretely (per METHOD FIRST):** the parameter is the shape of h (convexity/curvature and the small-gap concentration scale); the expected direction is that the certified floor rises from 0.0062 toward the float crystal floor ~0.0064–0.0065, and the 630/1e5 terminal-cell failure disappears.

**The belief the computation would test:** *the redistribution lever is linear-exhausted but not concept-exhausted.* Concretely: "no telescoping redistribution, linear or not, certifies eps > 0.0062 at α=1.464, psum=1/320" (currently CONJECTURED, resting only on the linear LP evidence). A float probe of min F_B over crystals + one/two-huge-gap configs for a few saturating h shapes, then — only if the float floor clears ~0.0063 with margin — an interval certification, would either refute the conjecture (new family member, new record) or confirm it (the lever is genuinely exhausted and the next move is V2/V3 or the 0.6818 in-class program).

**Method-first budget note:** I did NOT run this probe. It would only change the belief above; and per the hooks, the interval-verified negative on the linear family is already documented. The argument that V1 is the right next lever stands on the documented failure modes alone.

---

## (d) Labels

- PROVEN: the searched-family characterization (α, eps, m searched; k=6, F₀, w, psum=1/320, cap scheme, cosine family, linear-separable U fixed); eps=0.0062 exact for tawan's coefficients (620 certifies / 630 terminal-cell fail); telescoping validity of ANY U-coboundary (structural identity); asymmetry already in-family; V1 stays in the certificate class.
- CHECKED NUMERICALLY (cited scripts): crystal floors ~0.0063–0.0066 (float, non-rigorous, /tmp/crystal_floor.py); LP fails certification at 0.006126 vs tawan 0.006467 (/tmp/reoptimize_full.py, /tmp/certify_lp.py); bound arithmetic (exact mpmath).
- CONJECTURED: V1 raises the certified floor (mechanism argument only); V2/V3 help; V4's weights are algebra-pinned (need 30-min derivation check); the redistribution concept is not exhausted.
- INCONCLUSIVE (from explore §7, inherited): whether any linear (l,c) at fixed α beats tawan — the LP adverse-config set was not exhausted (two-large-gap closure missing). This is the reason V1 is argued from failure modes rather than from family-optimality.

**Assumptions:** [verified] all numbers quoted from the cited notes/scripts; [inferred] w(i,j) originates in the multiplicity decomposition (marked V4, cheap to check); [inferred] the terminal-cell failure at 630 is an enclosure-tightness effect of large-gap configs (consistent with the documented LP huge-gap dip and the "not closed under two-large-gap configs" ledger line).

**Next step:** fund V1 as a float probe (belief stated in (c)); if it clears, port to the interval verifier in Rust per the language policy. V3 (joint psum) is the cheap parallel track.
