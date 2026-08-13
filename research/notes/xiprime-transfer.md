# Stress-test: the "ξ′ transfer" idea

**Status: FINAL**
**Agent: research/adventurer (stress-test of prior fragmentary finding)**
**s4h skill applied: s4h-investigation-counter-hypothesis**

## Verdict (answer-first)

**VACUOUS as "new input" / EQUIVALENT TO KNOWN RESULT — and partly misread.**

The prior agent's "ξ′ transfer" finding is **misread on two counts** and does not survive
adversarial review:

1. `Transfer.lean` does **NOT** formalize "how ξ′ zeros relate to ζ zeros via the argument
   principle". It proves **XiTraceTransfer** — the transfer of the *trace and Frobenius norm*
   between two Gram matrices (zero-side `Ĝ¹` vs prime-side `M̂ᵀ`) that is the algebraic engine of
   the 67.25% lower-bound machinery [XF′ Lemma 5.1 + 6.1]. It is matrix/trace transfer, not
   zero transfer.
2. `ZeroCount.lean` **does** formalize the ξ′↔ζ link, and it is a **counting** statement:
   Riemann–von Mangoldt for ξ′ zeros, `N_{ξ′}(T,2T) = (T/2π)·ℓ₁(T) + O(log T)`, i.e.
   `N_{ξ′} = N + O(log T)` [XF′ (F3); classical: Conrey 1983 §2]. This is an
   **argument-principle count**, not a pointwise "on-line zero ⇒ on-line zero" transfer.

## 1. The claim under test, and what the tools compute

- **Claim (prior fragment):** on-line zeros of ξ′(s) transfer to on-line zeros of ζ(s).
- **`tools/check_xiprime.py`** (Python + mpmath, dps=25): computes
  `G(t) := i·ξ′(1/2+it)` = Ξ′(t), the derivative of the real Xi function Ξ(t)=ξ(1/2+it), via
  `ξ′/ξ = 1/s + 1/(s−1) − (1/2)log π + (1/2)ψ(s/2) + ζ′/ζ(s)`.
  It (a) evaluates G at claimed small-t roots, (b) scans (0.01, 14.1347) for sign changes of G,
  (c) samples gap roots from `tools/data/xiprime_on_line_1_1000.txt` (999 gap roots + 10 small-t).
- **`Transfer.lean`**: XiTraceTransfer (see header comment: "the target is
  Zeta23.XiPrime.XiTraceTransfer"; `|tr Ĝ¹ − tr M̂ᵀ| ≤ δ·N(T,2T)` and `‖Ĝ¹‖_F² ≤ (1+δ)‖M̂ᵀ‖_F² + δ·N`).
  PROVEN (Lean), but about Gram matrices, NOT about zeros.
- **`ZeroCount.lean`**: `xiDeriv_riemannVonMangoldt` — RvM main + local count for ξ′ zeros.
  PROVEN (Lean); pure counting via the argument principle folded by ξ′(1−s̄) = −conj ξ′(s).

## 2. The Speiser subtlety (real and decisive)

- Speiser's theorem concerns **ζ′**, NOT ξ′: RH ⟺ ζ′ has no zeros in 0 < Re s < 1/2. PROVEN (classical).
- ξ′ ≠ ζ′. With ξ(s) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s), the ξ′ zeros come from the full
  log-derivative bracket, so **ξ′ zeros ≠ ζ′ zeros** and **ξ′ zeros ≠ ζ zeros**.
  PROVEN (elementary product rule).
- **On-line ζ zeros are NOT ξ′ zeros** (for simple zeros): at a ζ zero s₀ on the line, ξ(s₀)=0 and
  ξ′/ξ has a simple pole (from ζ′/ζ), so ξ′ = ξ·(ξ′/ξ) → const ≠ 0. Equivalently Ξ(t) vanishes at
  t=γ but Ξ′ = G does not. **CHECKED NUMERICALLY** (this note, §4): G(γ₁) ≈ −0.0014 ≠ 0 while
  ζ(1/2+iγ₁) ≈ 0.
- The actual relation is **interleaving + counting**: the zeros of ξ′ on the line are the *gap*
  zeros (critical points of Ξ(t)), one in each gap between consecutive ζ zeros (Rolle/Gauss–Lucas
  for the real Ξ), and the *count* matches: N_{ξ′} = N + O(log T). CONJECTURED for the
  pointwise interleaving (classical, unverified here); PROVEN (Lean) for the count.

## 3. Verdict (specific reasons)

- **There is no pointwise transfer.** An on-line ξ′ zero does NOT transfer to an on-line ζ zero;
  on the contrary the ξ′ zeros sit *between* the ζ zeros, and the ζ zeros are precisely where ξ′
  does not vanish. The claim as stated is **FALSE** (not just subtle).
- **The only ξ′↔ζ link is the argument-principle COUNT** N_{ξ′} = N + O(log T) (ZeroCount.lean,
  Conrey 1983). That is a **KNOWN RESULT**, already an input to the 67.25% machinery (it makes the
  ξ′ configuration an admissible `ZeroConfig`), not a new transfer.
- **`Transfer.lean`'s "transfer" is unrelated to zeros**: it transfers a matrix *trace* from the
  zero-side Gram matrix to the prime-side Gram matrix. Reading it as "zero transfer" is a
  category error.
- Therefore the "ξ′ transfer" idea is **VACUOUS as a new input** and **EQUIVALENT TO A KNOWN
  RESULT** where it is true (the count). No new mechanism, no pointwise statement, no improvement.

### Counter-hypothesis (best alternative explanation of the apparent "signal")
The prior agent conflated two unrelated "transfers" (XiTraceTransfer — matrix trace — and
ξ′-zero counting) and mislabeled the function in Speiser's theorem (ζ′ vs ξ′). The apparent
"ξ′ transfer" signal is fully explained by the classical zero-count identity
N_{ξ′}(T,2T) = N(T,2T) + O(log T); no novel phenomenon is present.

## 4. Numerical evidence (commands)

```
# independent probe (mpmath, dps=20) — G = i·ξ′(1/2+it) = Ξ′(t):
uv run --with mpmath python -c "..."
  t=14.1347251417346937904572519835625  G=-0.0013827191   zeta(1/2+it)=(8.2e-22 - 5.1e-21j)   <- ζ zero, G≠0
  t=11.197465                            G=-0.01283814     zeta(1/2+it)=(1.3615 - 0.5549j)     <- gap point, ζ≠0
```
Interpretation: at γ₁ (a ζ on-line zero) G is nonzero ⇒ ξ′ does not vanish at ζ zeros. At a
claimed gap point ζ is nonzero. This is CONSISTENT with interleaving (ξ′ zeros in gaps), and
CONTRADICTS a pointwise transfer. **CHECKED NUMERICALLY** (inline mpmath probe; dps=20, not
interval-rigorous — see caveat below).

`tools/check_xiprime.py` itself **did not complete** under `uv run --with mpmath` within a 120–180s
timeout (exit 124, no output) — its step-0.01 scan + 90-iteration bisection at dps=25 is slow.
**INCONCLUSIVE** on its exact claimed root list; its *purpose* (G real, gap roots) is not disputed.

## Labels
- "Transfer.lean proves XiTraceTransfer (matrix trace/Frobenius transfer), not zero transfer":
  PROVEN (read the file header + theorem statements directly).
- "ZeroCount.lean proves RvM for ξ′ zeros: N_{ξ′} = N + O(log T)":
  PROVEN (read the file; Lean theorem `xiDeriv_riemannVonMangoldt`).
- "Speiser's theorem concerns ζ′, not ξ′": PROVEN (classical literature; also consistent with the
  Lean tree's use of ξ′ as a ZeroConfig whose zeros are counted, never equated with ζ zeros).
- "ξ′ zeros ≠ ζ zeros; on-line ξ′ zeros interleave between ζ zeros": CONJECTURED (classical,
  Gauss–Lucas/Rolle for real Ξ) — NOT independently re-derived here.
- "G(γ₁) ≠ 0 while ζ(1/2+iγ₁) ≈ 0": CHECKED NUMERICALLY (inline mpmath probe, dps=20,
  non-rigorous floating point).
- "The ξ′ transfer idea is VACUOUS / EQUIVALENT TO KNOWN RESULT": PROVEN given the above
  (no pointwise transfer exists; the only true link is the classical count).

## Caveat / honesty
The inline numeric probe uses mpmath floating point at dps=20, NOT the interval-rigorous `rug`/`arb`
path the hooks require for a *certified* claim. It is enough to *refute* a pointwise transfer
(G ≠ 0 at a ζ zero is a robust sign, far from any O(1) error), but a certified version would
confirm via Arb ball arithmetic. Marked CHECKED NUMERICALLY, not PROVEN.

## Context for next agent
- The 67.25% machinery already consumes ξ′ only as a `ZeroConfig` whose zero *count* is
  RvM-admissible (N_{ξ′}=N+O(logT)); there is no ξ′-to-ζ zero transfer to exploit further.
- If pursuing ξ′ further, the only un-used direction is the *gap* structure (interleaving), which
  is a known consequence of RH and appears already exploited by the "simple/distinct zeros"
  (N⁰ˢ, N_d) statements, not a new lever.
- Do not re-open "ξ′ transfer" as a novel input; it is closed: VACUOUS / KNOWN.
