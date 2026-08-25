# ROLE 5 — THEORIST: which finite-T term, if controlled better, most helps the constant?

**Executed by:** orchestrator (inline) — Agent tool unavailable; THEORIST role executed inline.
Labels per `hooks/agents.md`. Lever sensitivities from `results/verifier-finitet-flip.py`
(CHECKED NUMERICALLY, mpmath 80 digits); finite-T measurements from
`results/executor-finitet-probe.py` (CHECKED NUMERICALLY).

## 1. Where the constant comes from (the lever map)

The record 0.6732628655 = (H − τ)/(1 − B/m) is assembled from three levers: [RETIRED 2026-08-24]

| lever | value | role | T-sensitivity |
|---|---|---|---|
| **H(α)** | 0.6724218860964 | window value (main term) | T-free, verified to 1.7e-41 |
| **τ** | psum·(m−6)/m = 4.34e-4 | tax on block size | T-free, exact rational |
| **B/m** | Φ_m(ε(m−6))/m = 0.007696 | block/floor penalty | T-free, certified via ε |

**Control statement (theorist's ranking, from sensitivities):**
- d(bound)/dH = 1.0078 — the window value is the dominant lever. But H is already *optimized*
  (α=1.49, verified to 1.7e-41, and attack-kernel.md PROVES the cosine is the global minimizer
  of the window functional). **There is no headroom in H** — it is at its proven optimum.
- d(bound)/d(B/m) = 0.6785 — the block penalty is the *second* lever, and it is the one with
  **certification margin**: B/m = 0.007696 sits 1.3% above the flip threshold 0.007593.
- τ is small (4.3e-4) and exact.

**Consequence:** the constant is not going to move by re-optimizing H (proven ceiling) or τ
(exact). The only levers with real headroom are **(i) the block functional's finite-T error
o_χ(1)** (P6's object — it multiplies the whole bound through H's derivation) and **(ii) ε, the
certified floor** (a finer certification or a better F functional raises the achievable ε, which
raises the bound via B/m — the discovery note's own mechanism: ε↑ ⇒ B/m↓ ⇒ bound↑).

## 2. Ranking the finite-T terms by "what controlling it would buy"

**Term 1 — the o_{χ;T→∞}(1) HS² smoothing error (Lemma 3.3).** The paper's chain:
`‖W‖²_HS = (1/2 + (1/√2)cot(1/√2) + o_χ;T→∞(1))·Nall(T)`. This is THE finite-T term of P6. It
enters *additively* in the rank–trace bound and is the only unquantified piece. Controlling it
**upward** (proving the overshoot) would certify the record's margin rigorously; controlling it
**downward** would not hurt (bound is a lower bound — an error in either direction away from 0
is safe as long as its *sign contribution to the inequality* is understood). Measured magnitude
at T≤5000: Δ = +0.04…+0.07 — three orders above the record margin, safe direction.
**Buy: rigorous closure of P6's (B) side; converts CONJECTURED robustness to PROVEN.**

**Term 2 — the pair-sum deficit (HS2 below its window constant Q(v) ≈ 1.333).** This is the
*finite-T zero statistics* effect (attack-finitet-cinf CONJECTURED): at T=5000, HS2/N = 1.302
still 2.3% below Q(cos²·1)≈1.333. Because bound = 2·trW − HS2, **a smaller deficit (HS2 closer
to its limit) RAISES the bound** — this is the only finite-T term whose better control *helps
the constant directly*, not just certifies it. If the deficit were provably ≥ 0 and decaying,
the T→∞ limit would approach from the same safe side. But: the deficit is kernel-independent
(all five kernels tested show it), so controlling it means controlling zero pair correlation —
essentially a deep result (Montgomery/GUE), NOT an achievable bound. **Buy: direct constant
improvement, but only via a deep pair-correlation statement — LOW achievability, HIGH value.**

**Term 3 — the k-sum/Poisson-completion truncation (Claim 2.1).** Provably killed by C∞
smoothing (super-algebraic, ≤3.9e-19 — attack-finitet-cinf §3), at the cost of a worse window
constant Q. **Buy: none for the record** (already negligible in the C∞ picture; the hard-cutoff
O(1/K) version is dominated by the C∞ one).

**Term 4 — the O(T^δ log T) RvM window-count error, δ=10⁻¹⁰.** Negligible (O(10⁻¹⁰) in the
proportion). **Buy: none.**

## 3. The theorist's verdict

1. **The term that most helps the constant if controlled better: Term 2 (the HS2 pair-sum
   deficit)** — it is the *only* term whose sign is currently *against* the constant's full
   value (the bound sits below its T→∞ ideal by the deficit), and its reduction directly raises
   bound/N. But it is CONJECTURED zero statistics (kernel-independent), so controlling it is a
   deep pair-correlation problem — not an achievable finite-T bound.
2. **The term whose control most *certifies* the record: Term 1 (o_χ(1))** — provable via the
   paper's C∞ construction + super-algebraic decay (integration by parts), closing P6 rigorously.
   This is the highest *achievable* value: it converts the current CONJECTURED robustness into a
   PROVEN one with the tools already in the repo.
3. **The lever with the best cost/benefit: ε (the certified floor F ≥ 0.00806)** — the discovery
   note already showed ε is the sharp boundary (0.00806 certifies, 0.008065 fails). Any
   improvement in the F functional (better interval verifier, better block geometry) raises the
   bound directly through B/m with margin 1.0e-4 to the next record. **This is not a finite-T
   term** — it is the practical next move for the constant, orthogonal to P6.

## 4. Ranked next moves (theorist's input to synthesis)

1. **Prove the o_χ(1) bound** (Term 1) for the block functional via the paper's C∞ φ_T +
   super-algebraic φ̂ decay — closes P6 rigorously, converts CONJECTURED → PROVEN robustness.
   Impact: HIGH, Achievability: HIGH (tools exist).
2. **Probe the refined block functional at finite T** (bound=(H−τ)/(1−B/m) with real zeros,
   not the idealized functional) — the single biggest unknown in the current picture; could
   change the sign/structure of Δ. Impact: HIGH, Achievability: MEDIUM (needs block machinery
   coded against zero data).
3. **Attack ε / the F-floor functional** (raise the certified floor; sharper interval verifier
   or better block geometry) — directly raises the constant via B/m; margin 1.0e-4 to next
   record. Impact: MEDIUM-HIGH, Achievability: MEDIUM.
4. (Long shot) Model/control the HS2 pair-sum deficit (Term 2) via Montgomery–GUE numerology
   with T ≫ 10⁵ data (LMFDB block starts to 1e7 are cached in tools/data) — value HIGH, but
   achievability LOW (deep pair-correlation). Fund only if 1–3 stall.

RESULT: CONJECTURED — the finite-T term whose better control most helps the constant is the HS2
pair-sum deficit (Term 2, direct but deep/zero-statistics); the term whose control most
certifies it is the o_χ(1) smoothing error (Term 1, provable with existing tools = P6 closure);
the practical constant lever is ε/B/m (margin 1.0e-4).
