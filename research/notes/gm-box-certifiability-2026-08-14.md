# Can a Guth–Maynard-type zero-density estimate certify the box |β−1/2| < b/log T?

**Agent:** architect (structural thread). **Date:** 2026-08-14.
**Scope:** closed-form derivation only (charter: NO compute). Sources: `hooks/agents.md`; `gs-general-estimate-2026-08-14.md`; s4h-constraint + s4h-investigation skills.

**One-line answer:** No. The "scale mismatch" wall survives — and is sharpened from a *log* gap to a **log-log** gap: the best box any known zero-density estimate (ZDE) certifies is width **3 log log T / log T**, whereas the BGSTB box needs width **1/(2 log T)** (i.e. b = 1/2). Guth–Maynard is a *fixed-σ* (Shape-1) estimate and is provably blind to every shrinking box. A ZDE can only see the box if it is valid **at the moving boundary** σ = 1/2 + b/log T *and* carries ≤ log^1 T of polylog slack; the classical uniform estimate (Ingham) carries log^5 T and is therefore vacuous for proportions.

---

## 1. Notation and the counting tautology

Write L = log T. Zeros ρ = β + iγ, 0 < γ ≤ T. Total count (von Mangoldt):

N(T) := N(1/2, T) = (T/2π)·L + O(T). **(PROVEN, standard)**

For σ ∈ [1/2, 1]: N(σ, T) := #{ρ : β ≥ σ, 0 < γ ≤ T}.

**Box exterior** (what we must kill):

Zeros with |β − 1/2| ≥ b/L split into the right side {β ≥ 1/2 + b/L} and the left side {β ≤ 1/2 − b/L}. By the functional equation ξ(s) = ξ(1−s̄) each off-line zero β + iγ pairs with 1−β + iγ at the same height, so the two counts are equal. Hence, with σ_b := 1/2 + b/L,

**exterior count = 2·N(σ_b, T),**  **(PROVEN: pure counting + functional equation)**

and the proportion outside the box is

P_out(b) := 2·N(σ_b, T) / N(T) ≤ 4π · N(σ_b, T) / (T L) · (1 + o(1)).  **(PROVEN)**

Therefore:

> **The box condition "a proportion 1 − o(1) of zeros lies in |β − 1/2| < b/L" is the single statement N(σ_b, T) = o(T L).** A positive proportion inside is N(σ_b, T) ≤ (1−η) N(T) for some η > 0. **(PROVEN — this is a tautology; the entire problem is to bound N(σ_b, T) at the moving point σ_b.)**

---

## 2. The two shapes of a zero-density estimate (the structural fork)

A ZDE has the form  N(σ,T) ≪ T^{f(σ)} log^k T  valid on some σ-range, where f is the exponent and k the polylog power.

**Shape 1 — constant-slope exponent:** f(σ) = a·(1−σ), a fixed constant (finite). Then f(σ) → 0 as σ → 1/2. Since the truth is N(1/2,T) ~ (T/2π)L, any such estimate is **necessarily valid only for σ ≥ σ_0 > 1/2** (for some σ_0 = σ_0(a)); below σ_0 it is false. The density hypothesis (a = 2) and the "a = 3/2" Ingham-type corollary are Shape 1. **(PROVEN: f(σ)→0 forces σ_0 > 1/2.)**

**Shape 2 — exponent that tends to 1 at the line:** f(σ) = A(σ)(1−σ) with A(σ) → ∞ as σ → 1/2, arranged so f(σ) → 1. Ingham's A(σ) = 3/(2−σ) has A(1/2) = 2, so f(1/2) = 1, and the estimate can be valid **uniformly in σ ∈ [1/2, 1]** (it reads N(1/2,T) ≪ T log^5 T, consistent with N(T)). **(PROVEN for the form; uniformity of the classical statement flagged [inferred] below.)**

The entire verdict turns on this fork: **only Shape-2 can even speak at σ_b; Shape-1 is deaf.**

---

## 3. Shape-1 estimates are provably blind to every shrinking box

**Proposition (scale blindness).** Let N(σ,T) ≪ T^{a(1−σ)} log^k T be valid for σ ≥ σ_0 > 1/2 (any finite a, any k). Then for every **fixed** b > 0 (in particular b = 1/2) it certifies **no positive proportion** in the box |β − 1/2| < b/L.

*Proof (by a valid model).* For large T, σ_b = 1/2 + b/L < σ_0 (since b/L → 0). Consider the hypothetical zero configuration in which **all** zeros have β = 1/2 + σ_0/2 (fixed, strictly between 1/2 and σ_0; symmetry is satisfiable by pairing). Then N(σ,T) = 0 for every σ ≥ σ_0, which satisfies the estimate trivially; yet N(σ_b,T) = N(T) ~ (T/2π)L, so P_out(b) = 1, P_in(b) = 0. The estimate cannot rule this out. ∎ **(PROVEN)**

**Corollary.** Guth–Maynard (2024) is a Shape-1 estimate — a bound N(σ,T) ≪ T^{a(1−σ)+ε} (with a ≤ 2, and a = 2 the density hypothesis) on a range σ ≥ σ_GM with σ_GM > 1/2 — hence it is **provably incapable of certifying any positive proportion in any shrinking box**, for any value of its exponent or threshold. Lowering σ_GM from Bourgain's 25/32 to some σ_0 > 1/2 does **nothing** for the box: the box boundary sits strictly below every such σ_0. **(PROVEN given Shape 1; GM's exact (a, σ_GM) is [inferred] — but the verdict is independent of them.)**

Note also the task's hint is exactly right and harmless: the density hypothesis N(σ,T) = o(T^{2(1−σ)}) **is** false at σ = 1/2 (it would give N(1/2,T) = o(T), contradicting N(T) ~ (T/2π)L) — but the falsity is a *fixed-σ* statement and is irrelevant to the box, which needs a count at the **moving** point σ_b.

---

## 4. Shape-2 estimates: the P(b) curve

Suppose a ZDE is valid **at** σ_b, with exponent f(σ_b) = 1 − c·b/L + o(1/L) for some c > 0, and polylog power k:

N(σ_b, T) ≪ T^{1 − cb/L} · log^k T = T · e^{−cb} · log^k T.  **(the step T^{−cb/L} = e^{−cb} is exact; PROVEN)**

Then, by §1,

> **P_out(b) ≤ 4π · e^{−cb} · log^{k−1} T · (1 + o(1)).**  **(PROVEN)**

This is the **P(b) curve**. Its three regimes, by log-power k:

| k (polylog power) | P_out(b) as T → ∞ | Box certified |
|---|---|---|
| k = 0 | 4π e^{−cb}/L → 0 | **any fixed b > 0: proportion 1 − o(1) inside** |
| k = 1 | 4π e^{−cb} = const | positive proportion **iff b > log(4π)/c** |
| k ≥ 2 | 4π e^{−cb} log^{k−1} T → ∞ | **nothing (vacuous for every b)** |

**(PROVEN.)** The decisive quantity is **not** the exponent value c but the **log-factor slack k**. A ZDE with a clean log (k = 0) at the moving boundary gives the full box for every fixed b; one with log^2 or worse gives nothing; log^1 is the marginal case needing a large b.

**The constants.** For the density hypothesis c = 2 (f = 2(1−σ) = 1 − 2b/L exactly). For Ingham, A(σ) = 3/(2−σ):

f(σ_b) = 3(1−σ_b)/(2−σ_b) = (3/2 − 3b/L)/(3/2 − b/L) = 1 − (4/3)·b/L + O(1/L^2),  **(PROVEN, series expansion)**

so **c = 4/3** and, classically, **k = 5**.

- **Ingham (c = 4/3, k = 5):** P_out(b) ≤ 4π e^{−4b/3} log^4 T → ∞ for every fixed b. To get P_out → 0 one needs e^{−4b/3} = o(log^{−4} T), i.e. **b > 3 log log T + o(log log T)**. So the best box Ingham certifies is half-width
  **3 log log T / log T** — a log-log factor short of the required 1/(2 log T). **(PROVEN given the uniform Ingham form.)**
- **DH with a single log (k = 1, c = 2):** positive proportion iff b > log(4π)/2 ≈ 1.26; at b = 1/2 it gives P_out ≤ 4π e^{−1} ≈ 4.62 > 1 (vacuous). **(PROVEN.)**
- **DH in o-form (k = 0):** N(σ_b,T) = o(T e^{−2b}) = o(T), so P_out → 0 for every fixed b. **(PROVEN — this is the only "box-certifying" statement in the family, and it is the density hypothesis at the RH scale, not at a fixed σ.)**

---

## 5. Verdict: which exponents certify which boxes

| Estimate (shape, params) | Valid range | Best box width b/log T it certifies | b = 1/2? |
|---|---|---|---|
| Any Shape-1, incl. GM, DH-at-fixed-σ (a ≤ 2, σ ≥ σ_0 > 1/2) | σ ≥ σ_0 | **none** (only fixed-width b ≳ (σ_0−1/2)L, i.e. the classical "almost-all zeros in a fixed strip") | **NO** |
| Ingham (Shape 2, c = 4/3, k = 5) | 1/2 ≤ σ ≤ 1 [inferred uniform] | b = 3 log log T (almost-all) | **NO** |
| DH-at-moving-boundary, log-form (c = 2, k = 1) | at σ_b | b > 1.26 (positive proportion only) | **NO** (4.62 > 1) |
| DH-at-moving-boundary, o-form (c = 2, k = 0) | at σ_b | **any fixed b (1 − o(1))** | YES |

**Bottom line:** no known ZDE — classical Ingham, the density hypothesis in any fixed-σ form, or Guth–Maynard — certifies a positive proportion in the box at b = 1/2 (or any fixed b). The required input is:

> **N(1/2 + 1/(2 log T), T) = o(T log T)** — equivalently a ZDE valid at the moving boundary σ_b = 1/2 + 1/(2 log T) with exponent ≤ 1 − c/L and polylog power **k < 1** (i.e. strictly less than a single log T of slack), or directly o(T^{2(1−σ)}) at σ_b.

In the cleanest form: the needed exponent at σ_b is 1 − c/log T (c > 0) **with no log^1 or worse factor**. The classical Ingham estimate misses on the log power (k = 5), not on the exponent constant. **(PROVEN.)**

---

## 6. Hardness test (s4h-constraint): did the "scale mismatch" wall survive?

**Yes — and it is a *log-log* wall, sharper than the note stated.**

- The note's claim "GM cannot supply the box" is **CONFIRMED and upgraded from INCONCLUSIVE to PROVEN** for the *shape*: any fixed-σ ZDE is consistent with all zeros off-line within σ_0 of the line (the model in §3), so it certifies no shrinking box. This no longer depends on GM's exact range.
- The note said the gap is "the 1/log T scale"; in fact the **gap is a log-log factor**: the classical (Shape-2, uniform) Ingham estimate already reaches width 3 log log T / log T, and the required width is 1/(2 log T). So the missing saving is exactly a factor ~6 log log T, controlled by the log^5 → log^{<1} slack in the estimate.
- **What is genuinely hard vs. assumed:** the *hard* part is "no ZDE reaches σ = 1/2 + O(1/log T) with k < 1" — a theorem-level statement about the zero-detection method (Littlewood's lemma + moment estimates all operate at a fixed distance from the line). The *soft/assumption* part in the prior note was "GM's range is bounded from 1/2", which is now irrelevant to the verdict.

**Counter-hypothesis (best case for GM) — evaluated and rejected.** The best case for GM would be: "GM's *method* (large-value estimates for Dirichlet polynomials), pushed to σ = 1/2 + b/log T, gives a Shape-2 estimate with k < 1." Two obstacles: (i) GM's published corollary is Shape-1 (fixed σ_0), not a boundary estimate; (ii) no moment/large-value method is known to give a *power-of-log* saving (k < 1) at σ = 1/2 + O(1/L) — the standard zero-detection argument loses a fixed power of log T to the Littlewood–Jensen route, which is exactly the k = 5. **CONJECTURED (obstacle ii; I have not read GM — flagged), but the Shape-1 blindness (i) is PROVEN and already decisive.**

---

## 7. Labels

| Claim | Label |
|---|---|
| Exterior count = 2 N(σ_b,T); box ⟺ N(σ_b,T) = o(T log T) | PROVEN |
| Shape-1 ZDE valid only for σ ≥ σ_0 > 1/2 | PROVEN |
| Shape-1 ZDE certifies no shrinking box (model in §3) | PROVEN |
| GM is Shape-1 ⟹ GM cannot certify the box | PROVEN (conditional on Shape-1; exact GM params [inferred], irrelevant) |
| P(b) curve: P_out ≤ 4π e^{−cb} log^{k−1} T | PROVEN |
| Ingham c = 4/3; exponent at σ_b = 1 − (4b/3)/L | PROVEN (series) |
| Ingham's log power k = 5, uniform in σ ∈ [1/2,1] | [inferred] standard Ingham form (Montgomery, *Topics*, ch. 12); re-verify before citing |
| Ingham ⟹ box width 3 log log T / log T (almost-all) | PROVEN (given the uniform form) |
| DH-at-fixed-σ false at σ = 1/2 | PROVEN |
| b = 1/2 needs a moving-boundary ZDE with k < 1 | PROVEN |
| No known ZDE provides k < 1 at the boundary | CONJECTURED (literature state, not re-verified) |
| GM's *method* cannot reach the boundary with k < 1 | CONJECTURED ([inferred] from method structure; GM not read) |
| "GM supplies the box" | **ABANDONED** (Shape-1 scale blindness, §3) |

---

## 8. Next lemma to attack

**Boundary-density-hypothesis classification.** Establish where the needed input sits in the hypothesis web:

> **Lemma (target).** N(1/2 + b/log T, T) = o(T log T) for fixed b > 0 is (a) implied by RH; (b) **not** implied by any fixed-σ ZDE (proven here, §3); (c) open whether it is implied by — or equivalent to — a known hypothesis such as S(T) = o(log T) (the BGSTB Lemma-7 error term) or a pair-correlation input.

The point: §5 shows the 61.7% machine (BGSTB) reduces cleanly to the single count N(σ_b, T) = o(T log T). Classifying that count against S(T)/Selberg-type (log|ζ|) statements would tell us whether the "correct-scale" route the note identified (log|ζ| methods, not zero-density) can supply it — which is the next concrete move.

---

## 9. Assumptions

- `[verified]` von Mangoldt N(T) = (T/2π) log T + O(T); functional-equation symmetry β ↔ 1−β.
- `[verified]` f(σ_b) expansions (§4), constant c = 4/3 (Ingham) and c = 2 (DH); factor 4π in P_out.
- `[inferred]` Ingham's estimate is uniform in σ ∈ [1/2,1] with log^5 — the verdict for b = 1/2 is robust even if only the fixed-σ form holds (then it is Shape-1-blind anyway).
- `[inferred]` GM's zero-density corollary has Shape-1 form N(σ,T) ≪ T^{a(1−σ)+ε}, σ ≥ σ_GM > 1/2 (announced application: primes in short intervals). The box verdict does not depend on the exact (a, σ_GM).
- No computation performed: the only load-bearing numbers (c = 4/3, c = 2, log(4π) ≈ 2.531, threshold b ≈ 1.26, b = 3 log log T) are hand algebra; a numerical check would not change any belief, so per the compute discipline it is skipped.
