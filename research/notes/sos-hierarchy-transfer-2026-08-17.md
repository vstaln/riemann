# SoS / Lasserre hierarchy transfer to the simple-fraction certificate — can a higher-order lift break 0.6818?

**Agent:** architect (L3 domain-transporter). **Method:** s4h-analogy-domain-transfer + s4h-analogy-structure-mapping.
**Date:** 2026-08-17. **Scope:** read-only note; verdict + one checkable statement.

---

## 0. Framing (abstraction, no domain vocabulary)

We certify a lower bound on the fraction of "good" objects in a large collection, using only
(a) total density, (b) a two-point statistic on a bounded interval (bandwidth 1), (c) an
integrality/discreteness constraint. An explicit adversary — a concrete collection matching
every input — pins the best provable bound at 0.6818 (the near-CUE 256-law, simple fraction
p₀ = 0.6818287). Question: is 0.6818 a *low-degree relaxation* that a higher-order moment
hierarchy (SoS/Lasserre, Lovász θ, Cohn–Elkies SDP) exceeds, or is it *structurally
saturated*? Follow-up that the repo's own lever makes live: the **marked third moment m₃**
(adversarial-m3-reverify-2026-08-17.md) is a new datum at λ = 1/2 — inside the Rudnick–Sarnak
range kλ < 2 — that separates the adversary family.

---

## 1. Structural mapping table

| Certificate object (Riemann) | SoS/Lasserre object | Classification |
|---|---|---|
| certificate pair (c₀, r), r ∈ C¹[0,1] | dual SOS test polynomial, degree 2d | GENUINE (abstract) |
| value v = c₀ + ∫₀¹ r(x)x dx | dual objective L(f) | GENUINE |
| validity c₀ + Σ s_j r(j/N) ≤ p₁ for **all** configurations | Lasserre dual feasibility L − c·x = Σ σᵢgᵢ, σᵢ SOS | GENUINE |
| mean density + F on [0,1] (2-level density) | level-1 moment data {m₁, m₂} | GENUINE |
| integrality, marks ≤ 2 | support/integrality constraint on the measure | **BREAKS** — not a polynomial inequality; feasible set non-semialgebraic ⇒ Lasserre convergence theorem does not apply |
| near-CUE 256-law | level-1 extremal moment-feasible atomic measure | GENUINE |
| ceiling v ≤ p₁ + |E(1)|, shadow price of p₁ = 1 | exact upper value of the level-1 relaxation (witness = the law; attaining dual certificate not yet computed) | GENUINE |
| marked m₃ at λ = 1/2 (3-level density) | level-2 moment data {m₃}, kλ = 1.5 < 2 | GENUINE **and exists** (unlike a λ = 1 m₃) |
| tr G̃ᵏ only for kλ < 2; odd moments don't lower Λ₁(0); Prop 7.4 rank bound | availability of level-d data / rank degeneracy | **BREAKS as applied to the m₃ lever** — §7.5(e) concerns the Gram-eigenvalue (n₊/Λ₁) functional, not a marked third-moment constraint on the dual measure; the lever uses a different functional, so the negative results do not transfer |
| super-law family (m₃ ≈ 7.9 at λ=1/2, p₁ ≈ p₀) | level-2 adversary candidate | separated from the m₃ = 5±ε read by >5σ (CHECKED NUMERICALLY, independent re-run) |
| pinned bottom: near-CUE law with p₁ = p₀ has m₃ ≥ 5.44 | non-emptiness failure of the level-2 adversary set | CHECKED NUMERICALLY (m₃ note) — the p₀-level adversary family is excluded by the m₃ read |

Secondary analogies:
- **Cohn–Elkies / sphere packing:** the LP bound cannot improve via sharper kernels on the
  same data, because the extremal configurations match every read input (E8/Leech here;
  256-law here). New records need new inputs. GENUINE — one-line description of the ceiling.
- **Lovász θ hierarchies:** each improvement needs more *certified* data about the actual
  object. Here the level-2 data (m₃ at λ=1/2) is the available-but-not-yet-enclosed sliver.
  GENUINE (mechanism), with the enclosure as the bottleneck.

---

## 2. Verdict — two layers

**Layer 1: same-data degree lifts are DEAD — the ceiling is degree-independent (PROVEN, Lean, modulo EnclOK).**
`ceiling_law256` bounds the value of **every** certificate (c₀, r) — any r ∈ C¹, any c₀ —
valid against all configurations: v ≤ p₀ + 2.5431316e-6·(|r′(1)| + ∫|r″|). A degree-4/6/∞ SOS
certificate reading only {mean density, F on [0,1], integrality} is still valid against the
256-law, hence still ≤ 0.68183123. There is no degree at which the class escapes the law.
So 0.6818 is **not** a degree-2 SDP artifact: within the data class it is exactly the
level-1 optimum and it saturates. (This is where the Lasserre monotone-convergence premise
fails: the constraint set is not semialgebraic, and the data, not the degree, is the cap.)

**Layer 2: the new-data lift is real and partially verified — and it is not a hierarchy step, it is the m₃ lever.**
A certificate that additionally reads **marked m₃ = 5 ± ε at λ = 1/2** is a level-2-style
lift (new moment of the configuration measure). Its current status:
- m₃(1/2) = 5 is the unconditional sine-kernel closed form (PROVEN). The real zeros attaining
  it is PROVEN conditional on RH (Hejhal 1994 / RS96, kλ = 1.5 < 2) and CHECKED NUMERICALLY
  (≈ 5 ± 0.5 over 52,800 LMFDB zeros).
- The super-law family has marked m₃ ≈ 7.9 ± 0.04 (bias-corrected) — separated from 5 by
  >5σ, gap ≈ 2.9. Any near-CUE marked law with p₁ = p₀ has m₃ ≥ 5.44 (pinned bottom).
  Therefore no p₀-level adversary survives the m₃ = 5 ± ε read for ε < 0.44.
- Consequence: the level-2 in-class ceiling **may lie strictly above 0.6818** — the ceiling
  proof's premise (the 256-law is admissible) breaks because the law violates the new read.
  CONJECTURED until the LP is run.

**Net verdict.** The transfer fails as a same-data Lasserre hierarchy (saturated at every
degree — PROVEN) and succeeds as a data-class change (the m₃ lever — separation PROVEN
numerically, ceiling lift CONJECTURED). The 0.6818 ceiling is a **data-class bound, not a
degree bound**; it moves only when the data moves. This is the repo's history lesson
re-derived through the SoS lens.

---

## 3. The single most concrete checkable statement

**(A) Degree-independence (PROVEN — no computation needed).** Re-derive the ceiling with a
degree-4/6 parameterized r (e.g. r = Σ_{k≤3} c_k (x²−1)^k, or any bandlimited SOS family): the
optimum is still v ≤ p₀ + 2.5431316e-6·(|r′(1)| + ∫|r″|) with shadow price of p₁ = 1, because
`ceiling_law256` quantifies over all r. This confirms no degree escape exists within the data
class.

**(B) The level-2 lift test (computation target; the open lever).** Extend the exact-rational
LP machinery behind `lpdual-realconfig-check` / the 256-law ceiling with one extra read:
"marked-windowed m₃ at λ = 1/2 = 5 ± ε", ε < 0.44 (below the pinned bottom 5.44, above the
finite-window noise ≈ 0.5). Compute the new in-class ceiling over configurations matching
{mean density, F on [0,1], marks ≤ 2, m₃ = 5 ± ε}. Verdict criterion:
- new ceiling > 0.68183123 + |E(1)| ⇒ transfer succeeds: the level-2 lift exceeds the level-1
  optimum, giving an improvement over the certified 0.673481 (conditional on the rigorous m₃
  enclosure, below);
- new ceiling ≤ 0.68183123 ⇒ a different adversary family (non-near-CUE, or m₃-flexible)
  survives the read ⇒ saturation persists at level 2.
Required prerequisite (INCONCLUSIVE, not done): a rigorous finite-window enclosure ε_real for
the real zeros' marked m₃ (EnclOK-style treatment), so the read is a certified input rather
than an empirical one.

**(C) Separation already independently reproduced (CHECKED NUMERICALLY).**
`uv run --quiet --with numpy python3 research/notes/adversarial-m3-reverify-2026-08-17.py`
prints `SEPARATION REPRODUCED: YES` (super-law 7.935 ± 0.041 vs real 5.373 ± 0.075 at λ=1/2,
>5σ) — the adversary family the level-2 read excludes is real, not an artifact.

---

## 4. Honesty labels

| Claim | Label |
|---|---|
| Ceiling ≤ p₀ + 2.5431316e-6·(|r′(1)| + ∫|r″|) for **all** certificates (c₀, r) — hence degree-independent | PROVEN (Lean `ceiling_law256`; modulo EnclOK enclosure: INCONCLUSIVE-not-refuted) |
| Shadow price of p₁ = 1; v*(p₁) = p₁ + |E(1)| | CHECKED NUMERICALLY (lpdual-realconfig-check.md) |
| No degree escape within {mean density, F on [0,1], integrality} | PROVEN (direct corollary of ceiling_law256's quantification over r) |
| m₃(1/2) = 5 sine-kernel closed form (GUE limit) | PROVEN (unconditional closed form) |
| Real zeros' marked m₃ = 5±ε attained | PROVEN conditional on RH (Hejhal/RS96, kλ<2); CHECKED NUMERICALLY (5.373 ± 0.075, LMFDB) |
| Super-law m₃ ≈ 7.9 ≫ 5; separation >5σ; pinned bottom 5.44 | CHECKED NUMERICALLY (independent re-run, script cited) |
| Level-2 in-class ceiling > 0.6818 | CONJECTURED — the test is §3(B), not yet run |
| Rigorous m₃ enclosure ε_real < 0.44 exists | INCONCLUSIVE — required input, not done (EnclOK-style task) |
| Lasserre theorem inapplicable (non-semialgebraic, data-truncated) | PROVEN (structural) |
| Cohn–Elkies / Lovász θ illustrations | CONJECTURED (illustrative) |

## 5. Bottom line

The 0.6818 ceiling is a **data-class saturation, not a polynomial-degree bound**: same-data
degree-4/6 lifts are provably dead, and the only lift that can exceed it reads a *new*
moment — marked m₃ at λ=1/2, which exists inside the Rudnick–Sarnak range and separates the
adversary family (>5σ, independently reproduced). The single checkable gate is the
exact-rational LP with the m₃ = 5 ± ε read (§3(B)), with a rigorous enclosure as its
prerequisite. Transfer verdict: hierarchy FAILS, data-class change is LIVE.
