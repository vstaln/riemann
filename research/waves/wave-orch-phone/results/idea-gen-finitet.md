# ROLE 3 — IDEA-GEN: how classical analytic-number-theory bounds handle finite-T errors (s4h-analogy)

**Executed by:** orchestrator (inline) — Agent tool unavailable; IDEA-GEN role executed inline
from literature knowledge + the paper's own error chain. Labels per `hooks/agents.md`.
Statements about standard results are literature (CONJECTURED-as-translated unless the repo
paper states them); the paper's own error terms are quoted from
`research/papers/anthropic-informal-note.txt` (PROVEN structure there).

## 1. The paper's own finite-T error chain (from the informal note, lines 10–80)

```
#on[T,2T) + O(T^δ log T)   [RvM/window-count error, δ=10⁻¹⁰]
   ≥ 2 trW + ... − ‖W‖²_HS − O(T^δ log T)
   = (3/2 − (1/√2)cot(1/√2) + o_{χ;T→∞}(1))·Nall(T)
Nall(T) = (T/2π)log(2T/π) − T/2π + O(log T)
```

**Two distinct dropped finite-T terms:**
- **(A) O(T^δ log T), δ=10⁻¹⁰**: the Riemann–von Mangoldt window-count error. In the final
  proportion it is O(δ) = O(10⁻¹⁰) — utterly negligible. This is the classical RvM error term
  that Selberg/Levinson also carry; nothing special.
- **(B) o_{χ;T→∞}(1)**: the C∞-χ-smoothing error — the exact object of open problem P6. The
  paper does not quantify it; the program probes it numerically (attack-finitet*.md). **It is
  the only finite-T term with unknown sign/magnitude in the paper's argument.**

## 2. How classical techniques handle finite-T (analogy catalog)

1. **Selberg / Levinson (1974)**: Levinson's ≥1/3 uses a mollifier of length ≤ T^{θ}, θ<1/2.
   Finite-T error budget: the RvM O(log T), the Littlewood-lemma error O(T log T)/N(T) ~ O(1),
   and the mollifier-average error which is *asymptotically zero by design* — Levinson proves the
   mollified second moment splits with error O(T^{1/2+θ+ε}) that vanishes on division by N(T).
   **Lesson: the mollifier exists precisely to make the finite-T error a provable o(1), not a
   numerically-probed one.** The program's m=133 block plays the mollifier role, but its
   B/m = Φ_m(ε(m−6))/m error is a *window-certified constant* (provable), not a probed o(1).
2. **Levinson–Conrey mollifiers**: Conrey's 40% pushes θ → 1/2−ε; the finite-T errors scale as
   T^{θ−1/2}·log-power, vanishing. The trade is: longer mollifier → better main term, worse
   error term. The program's block size m=133 was *numerically optimized* (optimal for
   (α,psum)), i.e. the same trade, settled empirically.
3. **Zero-density theorems (Selberg–Huxley N(σ,T))**: standard bounds allow O(T^{c}) errors
   because the *count* is being bounded, not the proportion; the proportion then inherits
   O(T^{c−1}) → 0. The program's liminf proportion is structurally cleaner: it needs only
   o(1), and the certified constants (H, ε→B) are T-free.
4. **Montgomery pair correlation (1973)**: at finite T the pair-correlation function is
   conjectured to approach its limit with error ~O(log T)/T (or loglog T/log T in some
   regimes). This matches the program's measured HS2 deficit (~2–4%, decaying ~1/log T,
   CONJECTURED zero statistics — attack-finitet-cinf §7). **Classical numerology says the
   deficit should shrink, not flip — consistent with all measurements.**
5. **Explicit formulas (Riemann–von Mangoldt, Guinand–Weil)**: any *rigorous* finite-T bound
   on the pair-sum deficit would need a usable error term in the explicit formula for
   Σ_{ρ}φ̂(γ−α_k)φ̂(γ′−α_k) at height T. This is where the program's numerical probes could
   become a proof: bound the Poisson-completion remainder (Claim 2.1) with an explicit
   O(T^{1/2} log²T)-type term via the explicit formula, instead of assuming it vanishes.

## 3. Analogical transfer — what would classical method say about the record?

1. **The record's formula bound=(H−τ)/(1−B/m) is already in "classical shape":** all finite-T
   dependence has been pushed into (a) the liminf's o(1) and (b) certified T-free constants.
   No classical argument keeps a numerically-probed error in the final statement; neither does
   this one. The only unquantified piece is (B) the o_χ error — P6.
2. **The o_χ error in classical practice would be bounded, not probed**: Selberg/Levinson prove
   their smoothing error is o(1) via integration by parts + decay of φ̂. The C∞-smoothed φ_T has
   super-algebraic φ̂ decay (PROVEN numerically: k-truncation error ≤3.9e-19,
   attack-finitet-cinf §3) — the machinery for a rigorous o(1) bound exists; it has simply not
   been written down for the *record's* block functional.
3. **Pair-correlation deficit (HS2 gap)**: classical numerology (Montgomery, and the
   GUE-conjecture literature) treats the finite-T deficit as positive/fluctuating, not a
   systematic negative. This is *supportive evidence* for the record's robustness, but it is
   CONJECTURED, not proof.
4. **Mollifier-length tradeoff is the natural knob**: if a finite-T refinement ever *did*
   threaten the record (it doesn't at T≤5000), the classical response is to shorten the block
   m or reduce ε — exactly the trade τ(m) vs B/m the discovery note already optimized.

## 4. Concrete transferable ideas (each CONJECTURED unless script-backed)

1. **Write the rigorous o_χ(1) bound** for the record's block functional using the paper's C∞
   construction + super-algebraic decay (integration by parts; the paper's own setup).
   Impact: closes P6's (B) side rigorously; HIGH.
2. **Explicit-formula bound on the Poisson-completion remainder** (Claim 2.1 for the *block*,
   not the idealized kernel) via Guinand–Weil at height T — the numerically-observed O(1/K)→
   super-algebraic speedup becomes a proof; MEDIUM-HIGH.
3. **Extend the numerical probe to the refined functional** (bound=(H−τ)/(1−B/m) evaluated at
   finite T with real zeros) — currently only the *idealized* functional is probed; the
   refinement could change the sign/structure of Δ; MEDIUM (needs the block machinery coded).
4. **Montgomery-pair-correlation-aware deficit model**: fit the HS2 deficit against the
   classical 1−sinc²/λ² kernels at T up to 10⁵ (needs γ ≫ 10⁷ data, or the LMFDB block starts
   file present in tools/data) to distinguish "approaching 0" from "nonzero level"; LOW-MEDIUM
   (data-limited).

RESULT: INCONCLUSIVE — classical analogy (Selberg/Levinson/mollifiers/pair-correlation) says
finite-T errors should vanish or overshoot (safe), the paper's own chain has exactly two dropped
terms (O(T^δ log T), δ=1e-10, negligible; and the o_χ(1) smoothing error = P6, unquantified);
the transferable fix is to prove the o_χ(1) bound via super-algebraic decay — HIGH impact.
