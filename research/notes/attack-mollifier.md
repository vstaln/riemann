# Attack: fusing the Weil-form method with the Levinson–Conrey–Feng mollifier machinery

Agent: EXECUTIONER (analogy + creativity angle). Date: round 1.
Status: analysis only; no new theorems. Every claim labeled PROVEN (read in a source) /
CHECKED / CONJECTURED / ABANDONED.

Sources used (all read in full or in the cited passages):
- P = research/papers/claude-riemann-paper.txt (the paper, §1.2, §1.4, §1.5, §7.1, §7.4, §7.5, abstract)
- N = research/papers/anthropic-informal-note.txt (the terse proof; Lemmas 3.1–3.4)
- B1 = research/papers/baluyot-etal-2306.04799.txt (BGSTB24, unconditional Montgomery theorem)
- B2 = research/papers/bgst-2501.14545.txt (BGSTB25, pair correlation I)
- A = research/papers/claude-appendix.txt, T = research/papers/claude-transcripts.txt (development record)

No citation in this file points outside these files.

---

## 1. The two methods, one paragraph each (extracted)

**Mollifier line (Levinson–Conrey–Feng–PRZZ).** PROVEN, P §1.2: Selberg (1942) got a
positive proportion; Levinson (1974), "by an entirely new and strikingly direct method based on
mollifying ζ near the line", got κ = 1/3; Heath-Brown (and independently Selberg) observed
Levinson's zeros are simple; Conrey (1989) "refined the mollifier to reach κ > 2/5"; further
refinements by Bui–Conrey–Young (2011), Feng (2012), Pratt–Robles–Zaharescu–Zeindler (2020)
brought the record to κ > 5/12 = 0.4166…, "where it has stood since 2020. Every result in this
line uses Levinson's method." The input object of the simple-zero branch is stated in B2 §1:
Conrey–Ghosh–Gonek (1998) "introduced a method which uses the discrete, mollified moments of
ζ'(ρ)"; on RH (+ an extra hypothesis) that gave 19/27 simple, and Bui–Heath-Brown later got 19/27
on RH alone. The exact mean-square variants used by Conrey/BCY/Feng/PRZZ (lengths of mollifier,
which moments of ζ·M) are NOT itemized in our sources — they live in the cited papers, which we do
not have. The task-frame "mollifier needs moment estimates ∫|ζ(1/2+it)|^{2k} or log-moments" is
consistent with, but stronger than, what our sources state.

**Weil-form line (the 67.25% result).** PROVEN, P §1.4: "The argument does not use Levinson's
method; it makes unconditional the pair-correlation argument of [Mon73]." Take the bilinear map
W(f,g) = Σ_ρ m_ρ f̂(γ_ρ) ĝ(γ_ρ) of the Weil/Guinand explicit formula as a Hermitian form on test
functions; restrict W to a finite-dimensional Gabor family V of d ≈ λN modulated copies of one
window (critical sampling density over [T,2T]); write eG = W|_V. Zero side (P §1.4(Z), N): by the
functional equation each on-line point contributes a rank-one nonnegative form and each off-line
pair {ρ, 1−ρ̄} a block of signature (1,1), so P ⪰ 0 has rank ≤ s and Q has ≤ p positive
eigenvalues (Sylvester inertia). Prime side (P §1.4(P)): tr eG and ‖eG‖²_F are "Montgomery's first
and second moments [Mon73, BGSTB24]", evaluated unconditionally from primes ≤ X = (T/2π)^λ.
Linear algebra (P §1.4(L), N Lemma 3.4): rank A ≥ 2trA + 4trB − 4n₊(B) − ‖A+B‖²_HS (von Neumann
trace inequality; "the matrix analogue of the integrality steps m² ≥ 2m−1 and m² ≥ 3m−2",
abstract). Combining: ≥ 2/3 on the line as distinct points (Theorem A), ≥ 2/3 simple on the line
(Theorem B), ≥ 5/6 distinct (Theorem C); with the optimized window v*(s) = cos(√2 s) the constants
are 2 − 1/c*₁ = 3/2 − (1/√2)cot(1/√2) = 0.67250… (Theorem D; c*₁ = 0.7532960…, P §7.1). "No
termwise positivity, no mollifier, no zero-density estimate, and no zero-free region is used."

## 2. Inputs side by side

| Input | Mollifier line (Levinson–Conrey–Feng–PRZZ) | Weil-form line (67.25%) |
|---|---|---|
| Zero-side device | argument principle on ζ (or ξ) mollified near the line; discrete mollified moments of ζ'(ρ) [B2 §1] | Sylvester inertia + rank–trace on the compressed Weil form: on-line → positive squares, off-line pairs → (1,1) planes [P §1.4, N] |
| Arithmetic estimates | mean squares of ζ (resp. ζ') weighted by a mollifier M(s) = Σ a_n n^{-s} — moment estimates; exact variants not in our sources | tr eG, ‖eG‖²_F from Chebyshev–Mertens sums Σ_{n≤X} Λ(n)², Σ Λ(n)²/n, Σ Λ(n)n^{-1/2}, X = (T/2π)^λ, plus Montgomery–Vaughan for off-diagonals [P Thm-A proof list, N Lemma 3.3] |
| Pair-correlation input | none | Montgomery form factor F(α), |α| ≤ 1, unconditional [B1 Thm 1]; abstract: "exactly Montgomery's prime-side evaluation of the pair-correlation second moment with band-width ≤ 1" |
| Conditionality | unconditional | unconditional |
| Record | 41.6% (2020), stalled [P §1.2] | 67.25% (Theorem D) |
| Wall that stops it | long-mollifier mean squares hit off-diagonal (prime-pair/HL-type) terms | λ > 1 off-diagonal prime sums need prime-pair/HL-type info [P §1.5, §7.5(a)] |

## 3. Structure mapping (analogy)

1. Both methods certify on-line zeros by bounding the rank/positive index of a Hermitian form
   whose entries are computed from the arithmetic (prime) side. PROVEN, P §1.4, N.
2. Both are limited by the SAME dichotomy — diagonal vs off-diagonal of a second moment of a
   length-≤T Dirichlet polynomial. In the Weil-form computation the off-diagonal λ_T·λ_T terms
   are handled by Montgomery–Vaughan–Hilbert (N, Lemma 3.3: "the diagonal terms … contribute to
   the main term, and for the off-diagonal terms we will use Montgomery-Vaughan-Hilbert"); the
   moment is exact at λ = 1 because the extremal configuration realizes it (P §7.5(b): "2/3 N
   mutually orthogonal simple on-line zeros together with 1/6 N on-line doubles realise
   tr = N, ‖·‖²_F = 4/3 N"). P §7.5(a) states the wall verbatim: "for X ≫ T^1 the off-diagonal
   terms O_1 are no longer dominated by the diagonal, and their evaluation would require
   information on prime pairs (the Hardy–Littlewood conjectures, or equivalently Montgomery's
   pair correlation conjecture for α > 1 [Mon73, GM87])".
3. Montgomery's integrality m² ≥ 2m−1 (and m² ≥ 3m−2) under RH = the paper's rank–trace
   inequality made unconditional; the CGG98 (mollifier-moment!) multiplicity device m² ≥ 3m−2
   reappears verbatim as the (P₁, Q′) regrouping of Proposition 4.4 — P §7.5(c): "This is the
   device of [CGG98, (1.2)] made unconditional." PROVEN — this is the ONE documented, real point
   of contact between the two lines, and it is already inside the 67.25% paper.
4. The paper never claims "orthogonal, therefore combinable". What it claims is: new method does
   not use Levinson's method (P §1.4) and the input is disjoint (ζ-moments vs prime-side second
   moment). Orthogonality of inputs is PROVEN; usefulness of combining is NOT addressed anywhere
   in the sources (P, A, T).

## 4. Fusion candidates with obstacles

(a) Mollifier as a better inner product / weight on the Weil-form space. CONJECTURED, no source
   basis. The role of the mollifier in Levinson's method is to make ζ·M small near the line so the
   argument principle counts zeros of the product; the Weil form sums over zeros of ζ itself, and
   M(ρ) is not even controlled at zeros. Obstacle: any weight would have to change tr eG or
   ‖eG‖²_F (the only data the counting inequality reads), and those are saturated at λ ≤ 1 —
   Theorem D is "the limit of the method 'block structure + two traces + primes up to T': no
   window does better" (P §7.1, via [CCLM17, Cor. 14]). Upgrade evidence: an identity expressing
   a mollified mean square as a W-compression with a weight; nothing like it appears in P, A or T.

(b) Rank–trace applied to a mollified determinant (Levinson's quadratic form). CONJECTURED, no
   source basis. Levinson's quadratic form lives in the mollifier COEFFICIENT space (mean square
   over a_n); eG lives in the test-function space. The paper contains no map between these
   spaces, and its Cap proposition caps any such scheme: with test functions supported in
   [−L/2, L/2], L = λl, no argument can certify more than λN on-line points, and the certificate
   is non-positive for λ ≤ 1/2 (P §7.5, Prop 7.4). The transcript's lever analysis of the
   determinant/triple-correlation route (T, "Use the DETERMINANT / higher traces … involves
   triple correlation of primes … NOT unconditional") concerns higher moments of eG, not
   mollifiers, and ends at the same wall.

(c) Feed stronger BGST moments into the Weil-form off-diagonal terms. Partially PROVEN, then
   collapses into Task 4. The off-diagonal of the Weil-form second moment is already at its
   Montgomery–Vaughan floor (N Lemma 3.3: error ≪ T log²T vs main term ≍ T log³T — one log of
   slack, no constant to gain); the main terms are exact; the extremal configuration attains
   4/3 N. At fixed λ ≤ 1 the two-trace scheme is saturated (P §7.1, §7.5(b)). The paper's own
   scan of "what more input would help" (P §7.5(d,e,f)): more moments k ≤ 2m improve the
   Christoffel bound 1 − Λ_m(0), but the prime-side evaluation of tr eG^k is available only in
   the Rudnick–Sarnak range kλ < 2 — at most k = 3 for λ ∈ (1/2,1), and odd moments are useless;
   at λ ≤ 1/2 the dimension cap kills it. Conditional HL*(4,λ) would give 13/18 = 0.7222
   (P §7.5(f)). So the only uncapped direction is λ > 1, i.e. the form factor beyond 1.

## 5. Task 4: does a form-factor estimate beyond bandwidth 1 improve the Weil-form constant?

YES on the need, CONJECTURED on the supply. PROVEN (P §1.5): "the restriction λ≤1 is essential
(for X≫T^l the off-diagonal prime sums would require information on prime pairs of Hardy–
Littlewood strength)"; PROVEN (P §7.5(a)): "reaching 0.70, 0.80, 0.90 by the same route would
require pair-correlation information on Fourier supports out to roughly 1.04, 1.26, 1.70
respectively, beyond what is known." So even F(α) on [1, 1.04] would lift 0.6725 → 0.70, and
F(α) = 1 for all α > 1 (Montgomery's conjecture, equivalently Hardy–Littlewood prime pairs,
per the paper's own equivalence) would take the mechanism to its 100% ceiling — P §7.5(a): the
method's ceiling at bandwidth 1 for simple zeros is 0.68185 ("Theorem B's 2/3 is therefore
within 0.016 of the ceiling of its own method"), and §7.5(f): "HL*(k₀, λ) for all k₀ and all
λ < 1 would give proportion 1 … This is complementary to [GLSS25], where the pair correlation
conjecture with full support … yields 100% simple zeros on the line."

The needed estimate, precisely (all from sources): Montgomery's form factor
F(α) = ((T/2π)log T)^{-1} Σ_{ρ,ρ', T<γ,γ'≤2T} T^{α(ρ−ρ')} W(ρ−ρ') on α ∈ [1, A], A > 1, with
the B2 "Montgomery Theorem (MT)" asymptotics F(x,T) = (T/2πx²)log²T(1+O(1/√logT)) +
(T/2π)log x + O(T√logT) extended beyond x = T (i.e. α = 1); equivalently the additive
convolution Σ_{n,m≤T^{1+ε}} Λ(n)Λ(m)·g(log n)·h(log m) with |log n − log m| small (the
off-diagonal of the length-T^{1+ε} second moment). Known unconditionally: only 0 ≤ α ≤ 1
(B1 Thm 1: F(α) = T^{-2α}(log T + O(1)) + α + O(1/√log T)). Nothing in B1, B2, P, A, T
provides α > 1. No unconditional result in our sources estimates the prime-pair sum.

**The honest catch.** A MOLLIFIER-based estimate does not supply F(α), α > 1. The mollifier
line's inputs are ζ-side moments; its long-mollifier mean squares are blocked by exactly the
same off-diagonal wall (that is why 41.6% has stood since 2020, P §1.2). No paper in our set
derives prime-pair / form-factor-beyond-1 information from a mollifier argument. So the
"highest-value fusion" is real on the NEED side and empty on the SUPPLY side: what would improve
the Weil-form constant is any estimate of the prime-pair additive convolution (equivalently
F beyond 1) — from any method — and the mollifier machinery as documented does not produce it.
The 67.25% paper is already the unconditional completion of the pair-correlation line (B1/B2/GS),
NOT of the Levinson line; the genuinely orthogonal lineage (mollifier) shares the same wall.

## 6. Bottom line

1. Inputs of the two methods are disjoint (ζ·M mean squares vs prime-side pair-correlation
   second moment, bandwidth ≤ 1) — PROVEN. They share one wall: off-diagonal prime-pair
   information beyond length T.
2. The only documented fusion point is already inside the paper: the CGG98 multiplicity
   integrality m² ≥ 3m−2, transplanted as Proposition 4.4's regrouping — P §7.5(c). PROVEN.
3. The two-trace scheme at λ ≤ 1 is saturated (Theorem D "no window does better"; Cap
   Prop 7.4; extremal configuration §7.5(b)) — PROVEN. Weights, inner products, or more
   linear algebra cannot help without new arithmetic input.
4. The Weil-form constant is directly bottlenecked on the form factor beyond bandwidth 1
   (0.70 needs support 1.04) — PROVEN, P §7.5(a). A mollifier-based estimate of F(α), α > 1
   does not exist in the sources and is not derivable from the mollifier machinery — it is
   exactly the open Hardy–Littlewood / pair-correlation-beyond-1 problem. The fusion therefore
   has no lever: both methods are blocked by the same open arithmetic.
5. Candidates (a) and (b) are CONJECTURED with no evidence; candidate (c) reduces to Task 4's
   open estimate.

Most promising next step (concrete, cheap): write the λ = 1.04 version of the informal note's
Lemma 3.3 off-diagonal term — the exact prime-pair sum Σ_{n,m≤T^{1+ε}} Λ(n)Λ(m) g(log n) h(log m)
over |log n − log m| ≤ δ — and check which (if any) known unconditional upper bound (sieve or
Vinogradov–Korobov zero-free-region driven) gives a nontrivial constant in that range. If none
does, the angle is blocked at the same wall and effort should move to the conditional
HL*(4,λ) → 13/18 line (P §7.5(f)), which the sources DO quantify.
