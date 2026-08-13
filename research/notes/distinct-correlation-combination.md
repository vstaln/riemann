# Can the paper's correlation-moment distinct combination (0.85082) be made unconditional? — VERDICT: NO; 0.836740 is the unconditional ceiling in both classes

**Date:** 2026-08-14. **Status:** PROVEN (LP algebra + exact arithmetic); the collapse of the
weight is PROVEN, the load-bearing role of the cubic moment is PROVEN (direction of inequalities
+ paper's own §7.5(e)). **s4h method applied:** s4h-logic-argument-validation (the premises of
"m₂ unconditional + N_s = 0.673481 beats 0.836740" are individually sound but the *inference*
fails on a hidden premise — the weight's validity ψ(m) ≤ 1 — see §4).

---

## 0. One-line verdict

**No.** The paper's distinct combination `N_d ≥ ½ + (2m₂−m₃)/18 + (4/9)·N_s/N` (0.85082 under RH,
§7.5(g)) **cannot be made unconditional**, and its unconditional residue is *strictly weaker* than
our certified 0.836740. The load-bearing ingredient of the weight
`ψ(m) = ½m + (2m²−m³)/18 + (4/9)·1_{m=1}` is the **cubic term** (the negative m³ coefficient is
what keeps ψ(m) ≤ 1 for large multiplicities); the cubic moment is exactly the RH-conditional
input. Removing it collapses the weight to `ψ = 1_{m=1}` — the correlation-moment structure is not
an escape hatch from the affine lock, it is the *same* lock wearing an RH costume.

---

## 1. The paper's formula and the normalization of m₂, m₃

Source: `research/external-results/anthropic-zeta23/bundle/564f962e60643842f5fcb4a17c9dbc8f608f1c37.txt`
lines 2780–2799 (§7.5(g) "Distinct zeros under RH"):

```
ψ(m) = ½m + (1/18)(2m² − m³) + (4/9)·1_{m=1},   one checks ψ(m) ≤ 1 for all m ≥ 1 (equality at m = 1, 2, 3)
Schur–Horn (f(x) = −x²/9 + x³/18 convex):  Σ(2m_i² − m_i³) ≥ 2 tr H² − tr H³,  H = M^{1/2}ΓM^{1/2}
N_d ≥ Σψ(m_i) ≥ ½N + (1/18)(2 tr H² − tr H³) + (4/9)N_s
tr H²/N → m₂(1,v),  tr H³/N → m₃(1,v) under RH,  v(s) = cos(8s/5)1_{|s|≤1/2}:  2m₂ − m₃ = 0.68524…
N_s ≥ (19/27 − o(1))N on RH [BHB13]
⟹  N_d/N ≥ ½ + 0.68524/18 + (4/9)(19/27) = 0.85082…
```

**Normalization of the moments (PROVEN, from the paper's own text):** `m_k(λ,v)` is the k-th
moment of the limiting spectral distribution of the sine-kernel Gram matrix
`[sin πλ(xᵢ−xⱼ)/π(xᵢ−xⱼ)]` over the sine process; `m_k(1) = 1, 4/3, 2, 13/4` for k ≤ 4 (§7.5(f)).
So m₂, m₃ are **normalized trace moments of the correlation Gram matrix** (`tr H²/N`, `tr H³/N`),
NOT the raw multiplicity sums `Σmᵢ²/N, Σmᵢ³/N` — the two are connected by Schur–Horn in the
direction `Σ(2mᵢ²−mᵢ³) ≥ 2trH²−trH³`. This distinction is the crux (§3, §4).

---

## 2. The arithmetic (few-line check; script: `research/notes/distinct-correlation-combination-arith.py`)

Command: `cd /home/vstaln/riemann && uv run --quiet --with mpmath --with scipy --with numpy python3 research/notes/distinct-correlation-combination-arith.py`

| quantity | value | label |
|---|---|---|
| paper's RH bound ½ + 0.68524/18 + (4/9)(19/27) | **0.8508260905** | PROVEN (reproduces the paper's 0.85082) |
| correlation alone ½ + ½(2m₂−m₃) (RH) | 0.84262 | PROVEN (paper's own §7.5(g)) |
| naive plug: m₃=0, m₂=4/3, N_s=0.673481 | **0.9474729756** | **INVALID — not a bound** (§3) |
| honest unconditional weight LP, span{m, m², 1_{m=1}} | collapses to **0.673481** (= h) | PROVEN (§4) |
| our certified distinct record (1+h)/2 | **0.8367404308372568** | CHECKED NUMERICALLY (FINAL-RECORD-2026-08-13) |

The one number that matters for the make-or-break question: **the naive unconditional plug reads
0.9475 — but it is a fiction.** It assumes the weight survives dropping m₃, and it assumes
`Σmᵢ²/N ≥ m₂ = 4/3` unconditionally. Both assumptions are false (next two sections).

---

## 3. Why the naive m₃=0 plug (0.9475) is not a bound (PROVEN, arithmetic)

A weight bound `N_d ≥ Σψ(mᵢ)` is valid **only if ψ(m) ≤ 1 for every integer m ≥ 1** (then each
distinct zero contributes at most 1). The paper's cubic weight attains ψ = 1 at m = 1, 2, 3 and
stays ≤ 1 because the **cubic term dominates at large multiplicity**:

```
ψ(1)=1.0, ψ(2)=1.0, ψ(3)=1.0, ψ(4)=0.222, ψ(5)=−1.667, ψ(10)=−39.4        (cubic, valid)
ψ₀(1)=1.056, ψ₀(2)=1.444, ψ₀(3)=2.5, ψ₀(6)=7.0                            (m³ dropped, INVALID)
```

Dropping m³ gives `ψ₀(m) = ½m + m²/9 + (4/9)1_{m=1}` with **ψ₀(2) = 13/9 > 1**: a double zero
would be counted as 13/9 > 1 of a distinct zero, so `N_d ≥ Σψ₀(mᵢ)` is **false**. The 0.9475 is a
numerical artifact of an illegal weight, exactly as a false-premise conclusion is an artifact of
an invalid argument (s4h-logic-argument-validation: the premises are individually true, the
inference fails on the hidden premise "the weight survives").

**Second failure of the naive plug (direction of the moment inequality, PROVEN):** m₂ is the
moment of **tr H²** (the *full* Gram norm, diagonal + off-diagonal), while the weight consumes
`Σmᵢ²` (the *diagonal* part). Since H ⪰ 0 with diagonal mᵢ, `tr H² = Σmᵢ² + Σ_{i≠j} Hᵢⱼ² ≥ Σmᵢ²` —
the unconditional pair-correlation second moment `tr H²/N → m₂` gives an **upper** bound on
`Σmᵢ²`, not a lower one. The only unconditional lower bound on `Σmᵢ²` is the trivial
`Σmᵢ² ≥ N` (mᵢ ≥ 1). This is the same "direction" phenomenon as the eps-floor in the
integrality transplant note (b3): the spectrum controls the full Gram norm, and multiplicity
information (`Σmᵢ²`, `N_dist`) is exactly what it cannot see from below.

---

## 4. The class-escape question — answered (PROVEN)

**Is the correlation-moment structure a different certificate class that escapes the affine lock
(1+H)/2?** It *is* a different class — under RH it reaches 0.85082 > 0.836740, so it genuinely
escapes the in-class ceiling. But the escape hatch is exactly the cubic moment, and the cubic
moment is exactly the RH-conditional input. Unconditionally the class collapses:

**(a) The cubic term is load-bearing (PROVEN, direction of inequalities).** The positive m²
coefficient (+1/9) and m coefficient (+1/2) can coexist with ψ ≤ 1 **only** because the negative
m³ coefficient (−1/18) dominates at large m. For any weight in span{m, m², 1_{m=1}} (cubic
removed), a positive m² coefficient forces ψ(m) → +∞ as m → ∞, so b ≤ 0; a positive m coefficient
a > 0 likewise forces am > 1 for m large, so a = 0. Only `c·1_{m=1}` survives.

**(b) The Schur–Horn combination needs tr H³ from above (PROVEN).** The certified quantity is
`2 tr H² − tr H³`, and a lower bound on it requires an **upper** bound on tr H³. Unconditionally
tr H³ is unavailable at the operative bandwidth: the Rudnick–Sarnak range is kλ < 2 (§7.5(e)),
so k = 3 requires λ < 2/3, and even there the paper proves an odd moment does not lower the
Chebyshev–Markov–Stieltjes bound. `m₂` alone gives `2trH² − trH³ ≥ 2m₂N − UB(trH³) = −∞`.

**(c) The honest unconditional LP over span{m, m², m³, 1_{m=1}} (PROVEN, LP algebra).**
With the only unconditional inputs — `Σmᵢᵏ ≥ N` (trivial), `N_s ≥ hN` — the optimum is
`ψ = 1_{m=1}`, giving `N_d ≥ N_s ≥ hN = 0.673481` in the pure weight framework. The scipy LP over
the finite cap m ≤ 3000 finds a = 1/3001, f = h + (1−h)/3000 = 0.673589, converging to h as the
cap → ∞ — the blowup structure made visible. (Our certified 0.836740 comes from the *stronger*
two-constraint LP on (s₁, s₂, p) — rank–trace + pair bookkeeping — which the per-multiplicity
weight framework does not contain; the weight framework is strictly weaker.)

**(d) Any richer unconditional weight is back inside our class (PROVEN).** Extending the span
with indicators 1_{m=2}, 1_{m=3}, … asks for the proportions of zeros of exact multiplicity k ≥ 2,
whose only unconditional bounds are the bookkeeping `N ≥ s₁ + 2s₂ + 2p + …` — i.e. exactly the
two-constraint LP of the integrality note, whose distinct ceiling is (1+H)/2 = 0.836740
(distinct-integrality-transplant.md §b1).

---

## 5. Verdict + labels

**Verdict: the paper's distinct combination cannot be made unconditional, and 0.836740 is
confirmed as the unconditional distinct ceiling in both classes.** The 0.85082 rests on the
RH-conditional cubic moment m₃, which plays a *double* role — (i) it is the upper bound that makes
`2 tr H² − tr H³` certifiable from below, and (ii) it is the term that keeps the weight ≤ 1 so the
bound is a genuine lower bound on N_d. Remove it (as any unconditional version must) and the
combination collapses to `N_d ≥ N_s ≥ 0.673481` in the weight framework, strictly below our
certified 0.836740; the only structure that reaches 0.836740 is our two-constraint LP, which is
its own ceiling. **distinct > 0.836740 ⟺ H > 0.673481 remains the reduction** — the correlation
moments provide no second independent input unconditionally. No new record is claimed; the
certified 0.673481 / 0.836740 stand unchanged.

| claim | label |
|---|---|
| The paper's formula: N_d ≥ ½ + (2m₂−m₃)/18 + (4/9)N_s/N with 2m₂−m₃ = 0.68524, N_s = 19/27 gives 0.850826 | PROVEN (reproduced by script; paper's own constants) |
| m₂, m₃ are normalized trace moments tr H²/N, tr H³/N of the correlation Gram matrix (m_k(1) = 1, 4/3, 2, 13/4) | PROVEN (paper §7.5(f)) |
| ψ(m) ≤ 1 for all m requires the cubic term; dropping m³ gives ψ₀(2) = 13/9 > 1 | PROVEN (exact arithmetic, script) |
| The m₃=0 plug 0.9475 is not a valid bound | PROVEN (weight invalid; Σψ₀(mᵢ) ≰ N_d) |
| Unconditional pair correlation gives an upper (not lower) bound on Σmᵢ² (tr H² ≥ Σmᵢ², direction) | PROVEN (tr H² = Σmᵢ² + off-diagonal ≥ 0) |
| The combination 2trH²−trH³ needs an upper bound on tr H³; unavailable unconditionally (RS range kλ<2; odd moment adds nothing, §7.5(e)) | PROVEN (paper's own §7.5(e) + direction of inequalities) |
| Unconditional LP over span{m, m², m³, 1_{m=1}} collapses to ψ = 1_{m=1}, giving 0.673481; finite-cap LP 0.673589 → h as cap → ∞ | PROVEN (LP algebra + script) |
| Indicator-extended spans re-enter the (s₁,s₂,p) two-constraint LP, ceiling (1+H)/2 = 0.836740 | PROVEN (distinct-integrality-transplant.md §b1) |
| 0.836740 is the unconditional distinct ceiling in both classes | PROVEN in-class + this note; "all conceivable classes" | CONJECTURED |
| No new record claimed | PROVEN (this note changes no numbers) |

## 6. Files & script

- Script: `research/notes/distinct-correlation-combination-arith.py` (few-line mpmath/scipy
  check, <1 s; reproduced the paper's 0.850826, computed the invalid 0.9475 plug, verified the
  weight values ψ/ψ₀, and ran the collapse LP). Command: `uv run --quiet --with mpmath --with
  scipy --with numpy python3 research/notes/distinct-correlation-combination-arith.py`.
- Sources: paper §7.5(g) lines 2780–2799 and §7.5(e)/(f) lines 2743–2768
  (`564f962e60643842f5fcb4a17c9dbc8f608f1c37.txt`); `FINAL-RECORD-2026-08-13.md` (H =
  0.6734808616745137, distinct = 0.8367404308372568); `distinct-integrality-transplant.md` (the
  affine lock (1+H)/2 and its PROVEN in-class ceiling); `c4-second-moment-denominator.md` (the
  paper's own §7.5(e): higher moments add nothing unconditionally on (1/2,1));
  `records-vs-anthropic-paper.md` (paper's affine corollary H_d = (1+H)/2, constants 0.6725 /
  0.83625). No zero data downloaded; no verifier re-run.
