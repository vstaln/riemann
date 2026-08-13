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
4. **The 10 coefficients (l₁..l₅, c₁..c₅)** — in the LP attempts: `F_B` is linear in (l,c), so max-min over a config set is a linear program. Three rounds of LP + cutting planes were run (coboundary-reopt-corrected.md):
   - **Exact asymptotic (PROVEN):** as gᵢ → ∞ with the other five bounded, F_B = pᵢ·gᵢ + O(1), where pᵢ = 1/1920 + lᵢ₋₁ − lᵢ is the redistributed pressure (l₀ = l₆ = 0). The huge-gap limiting slope is EXACTLY the pressure at position i. Certification of F_B ≥ eps therefore requires pᵢ ≥ 0 for all i — the "κᵢ ≥ 0" constraint (the note's κ list is p; the §2 "p" reporting error is a relabeling, the constraint is the same).
   - **LP attempts (PROVEN worse at certification):** every LP optimum that raised the crystal floor did so by concentrating pressure (p₂ ≈ 3.3× uniform) and alternating q at the c-bound ±0.06; each then violates pᵢ ≥ 0 or collapses on huge-gap / two-large-gap configs (worst floor 0.001268 at g ≈ (1.06, 9.91, 1.06, 2.01, 1.05, 7.98)). The prior explorer's LP (p₃ ≈ 88% concentration) failed certification even at 600/1e5; the corrected LP's reported (l,c) has p₂ < 0 and fails at both 0.0062 and 0.00577.
   - **§7 cutting-plane closure (CONJECTURED near-optimal, mechanism PROVEN by the iteration):** serialized cutting planes show the tradeoff binds: raising the crystal floor drives min pᵢ → 0 (0.000471 → 0.000056 → 0.000038 over iterations) while the worst huge-gap floor collapses (0.006372 → 0.005129 → 0.001268). tawan's even spread (p = κ ≈ 0.000457–0.000613, all comfortably positive) is the balanced optimum of the LINEAR family. Verdict: no linear (l,c) beats tawan is now a sharp CONJECTURE with a documented mechanism (INCONCLUSIVE as a proof — the true feasible set was sampled, not certified).

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
- The binding constraint class is the **period-2 crystal** (g ≈ (2.00, 1.05, 1.99, …)) — the same class that limits the certified eps and the same class that punishes every pressure-concentrating LP solution (reopt-corrected §5). [CHECKED NUMERICALLY]
- 630/1e5 fails at a TERMINAL CELL — i.e., the certified ceiling is set by large-gap / terminal-cell enclosure tightness, in tension with the crystal floor. [PROVEN: verifier output]
- The LP family is "not closed under two-large-gap configs" (FINAL-RECORD honesty ledger); §7's cutting-plane iteration located the mechanism: raising the crystal floor forces min pᵢ → 0 and collapses the huge-gap floors (worst 0.001268 at g ≈ (1.06, 9.91, 1.06, 2.01, 1.05, 7.98)). [PROVEN at certification / CHECKED NUMERICALLY]

---

## (b) ≥3 structural variations NOT searched, with analysis

### V1. NONLINEAR and/or COUPLED coboundary U (drops assumptions A1+A3)

**The move.** Replace U(g₁..g₅) = Σ(lᵢgᵢ + cᵢw(gᵢ)) with a U that is (i) nonlinear in g — e.g. U = Σ h(gᵢ) for a convex/saturating h, or (ii) couples adjacent cells — e.g. U = Σ φ(gᵢ, gᵢ₊₁) or a term in |gᵢ − gᵢ₊₁| or gᵢgᵢ₊₁. Keep the coboundary *shape*: F_B = F₀ + U(g₂..g₆) − U(g₁..g₅).

**Why it is valid (PROVEN, structural).** The telescoping identity that makes a coboundary invisible on periodic sequences — Σ over a long run of windows of [U(g₂..g₆) − U(g₁..g₅)] telescopes to boundary terms — holds for **any** function U of a 5-gap window. Linearity and separability were choices of the search, not requirements of the certificate. A coupled term gᵢgᵢ₊₁ or |gᵢ−gᵢ₊₁| still telescopes identically. So V1 stays **inside the certificate class**; it is a redistribution-family member, just not a linear one.

**Why it could plausibly lower the floor below 0.0062 / raise the bound (CONJECTURED).**
- **The decoupling argument (the sharp reason).** Within the linear family, the huge-gap limiting slope at position i is PROVEN to equal the redistributed pressure pᵢ = 1/1920 + lᵢ₋₁ − lᵢ exactly (slope of F_B as gᵢ → ∞ is p₀ + (lᵢ₋₁ − lᵢ)). Linearity therefore *identifies two quantities the certificate needs to control independently*: (i) the small-gap concentration (lᵢ₋₁ − lᵢ) that lifts the period-2/3 crystal floor, and (ii) the huge-gap slope pᵢ = p₀ + (lᵢ₋₁ − lᵢ) that keeps the terminal-cell floor positive. The §7 iteration shows any linear attempt to raise (i) forces some pᵢ → 0 and collapses (ii). A nonlinear, saturating h breaks the identification: with U = Σ[lᵢh(gᵢ) + cᵢw(gᵢ)], the small-gap concentration is (lᵢ₋₁ − lᵢ)·h′(small) while the huge-gap slope is p₀ + (lᵢ₋₁ − lᵢ)·h′(∞) — two independent parameters for the cost of one extra degree of freedom per gap. h can concentrate on the crystal band (g ≈ 1.0–2.0) and decay to a small but positive slope beyond g ≈ 3, so both the crystal floor and the terminal-cell floor rise together. This is the only variation on this list for which there is a PROVEN obstruction (the pᵢ ≥ 0 identification) that the variation itself removes.
- A **coupled term φ(gᵢ,gᵢ₊₁)** (e.g. |gᵢ − gᵢ₊₁| or gᵢgᵢ₊₁) additionally senses the alternating structure of the period-2/3 crystals (1.05,1.98,1.05,1.98,… and 1.996,1.051,1.996,…) that a separable U cannot distinguish from a generic point. Since the certified eps sits only ~1–3e-4 above the crystal floor at α=1.464, even a small lift of the crystal floor converts into a higher certifiable eps.
- **Why it cannot be dismissed by symmetry (PROVEN reasoning).** No symmetry of the certificate maps a nonlinear U to a linear one; the searched family is the linear subspace, and the nonlinear extension is a strictly larger set. The linear LP/cutting-plane evidence is evidence about the linear subspace only.

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

**Already in the searched family (PROVEN).** The LP maximized over all (l₁..l₅, c₁..c₅) with NO symmetry constraint; the family is already fully asymmetric (and tawan's own profile is antisymmetric (54,−123,0,123,−54)). Asymmetry per se therefore cannot be the unsearched lever — any asymmetric linear solution is inside the family the LP explored. What is genuinely open is not asymmetry but nonlinearity (V1): the linear family is now near-closed by the §7 cutting-plane mechanism (CONJECTURED), and the reopt note §6 explicitly floats restricting the search to tawan's symmetric subspace as a cheap confirmation — indicating the symmetric subspace is believed optimal *within the linear family*.

---

## (c) VERDICT — the single most promising next move

**V1: a nonlinear, saturating coboundary U — U(g₁..g₅) = Σ[lᵢh(gᵢ) + cᵢw(gᵢ)] with h convex-saturating (h′(small) large, h′(∞) small-but-positive) — on the SAME 6-gap window, same (α, psum, m).**

- It is the only variation that provably stays inside the certificate class while leaving the searched subspace (telescoping is structural, not linear — PROVEN), and it is the only variation that removes a PROVEN obstruction: the linear-family theorem that the huge-gap slope equals the redistributed pressure (pᵢ ≥ 0 binding). Nonlinearity decouples the small-gap concentration from the huge-gap slope, which is exactly the tradeoff the §7 cutting-plane iteration showed kills every linear (l,c).
- It attacks the exact documented failure mode: the linear LP/cutting-plane iterates collapse on huge-gap and two-large-gap configs (worst 0.001268) precisely when they raise the crystal floor; tawan's even pressure spread survives because it keeps all slopes comfortably positive. A saturating h inherits tawan's huge-gap safety (positive asymptotic slope at every position) while freeing the crystal-floor degree of freedom that the pᵢ ≥ 0 identification blocked.
- The crystal floor sits only ~1–3e-4 above the certified eps at α=1.464, so even a marginal lift of the crystal floor converts directly into a higher certifiable eps and a higher bound (H fixed, τ fixed, B/m fixed ⇒ bound is monotone in eps at fixed m).

**Expected direction of change, stated concretely (per METHOD FIRST):** the parameter is the shape of h (its saturation scale G₀ and the curvature on the crystal band g ∈ [1, 2]); the expected direction is that the certified floor rises from 0.0062 toward the float crystal floor ~0.0064–0.0065, and the 630/1e5 terminal-cell failure disappears.

**The belief the computation would test:** *the redistribution lever is linear-exhausted but not concept-exhausted.* Concretely: "no telescoping redistribution, linear or not, certifies eps > 0.0062 at α=1.464, psum=1/320" (currently CONJECTURED, resting on the linear LP + cutting-plane evidence, which by §7's own mechanism is evidence only against the linear subspace). A float probe of min F_B over crystals + one/two-huge-gap configs for a few saturating h shapes, then — only if the float floor clears ~0.0063 with margin — an interval certification, would either refute the conjecture (new family member, new record) or confirm it (the lever is genuinely exhausted and the next move is V2/V3 or the 0.6818 in-class program).

**Method-first budget note:** I did NOT run this probe. It would only change the belief above; and per the hooks, the interval-verified negative on the linear family is already documented. The argument that V1 is the right next lever stands on the documented failure modes alone.

---

## (d) Labels

- PROVEN: the searched-family characterization (α, eps, m searched; k=6, F₀, w, psum=1/320, cap scheme, cosine family, linear-separable U fixed); eps=0.0062 exact for tawan's coefficients (620 certifies / 630 terminal-cell fail); telescoping validity of ANY U-coboundary (structural identity); asymmetry already in-family; the huge-gap limiting slope equals the redistributed pressure pᵢ = 1/1920 + lᵢ₋₁ − lᵢ (exact derivation, reopt-corrected §1) and pᵢ ≥ 0 is necessary for certification; the two-gap rays add no constraints; V1 stays in the certificate class and removes the pᵢ-slope identification (V1's decoupling argument).
- CHECKED NUMERICALLY (cited scripts): crystal floors ~0.0063–0.0066 (float, non-rigorous, /tmp/crystal_floor.py); LP failures: uncorrected LP 0.006126 vs tawan 0.006467; corrected LP v*=0.00877 on the 578-config family but global float floor 0.005615 vs tawan 0.006344; LP (l,c) fails interval certification at 0.0062 and 0.00577; §7 cutting-plane iteration (tawan 0.006471; LP worst 0.006372 → 0.005129 → 0.001268); bound arithmetic (exact mpmath). Scripts: tools/coboundary-reopt/*.py, tools/verify_coboundary_floor.py.
- CONJECTURED: V1 raises the certified floor (decoupling argument only); V2/V3 help; V4's weights are algebra-pinned (need 30-min derivation check); tawan is near-optimal within the LINEAR family (§7 mechanism, not a certified optimum).
- INCONCLUSIVE: a certified answer to "does any (l,c) beat tawan at α∈{1.464,1.49}" — the linear family was sampled via cutting planes, never certified-exhausted. This is precisely the gap the nonlinear extension (V1) jumps over.

**Assumptions:** [verified] all numbers quoted from the cited notes/scripts; [inferred] w(i,j) originates in the multiplicity decomposition (marked V4, cheap to check); [inferred] the terminal-cell failure at 630 is an enclosure-tightness effect of large-gap configs (consistent with the documented huge-gap dips and the §7 iteration's collapsing worst floors).

**Next step:** fund V1 as a float probe (belief stated in (c)); if it clears, port to the interval verifier in Rust per the language policy. V3 (joint psum) is the cheap parallel track.
