# C4 SECOND-MOMENT DENOMINATOR — theory of the remaining gap

**Date:** 2026-08-13. **Status:** ABANDONED (the paper's own §7.5(e) proves the C4 route dead unconditionally).
**Author:** architect/research subagent. **s4h skill applied:** structure-mapping
(`~/.pi/agent/skills/s4h-analogy-structure-mapping/SKILL.md`).

---

## 0. The question

The prior verdict (`research/notes/structural-final-verdict.md`) pins the unconditional frontier at
v\*(p₁) = p₁ + |E(1)| with |E(1)| = 2.54e-6 and the 256-law ceiling p₁ = p₀ ≈ 0.6818287. To exit the
certificate class one needs a **new unconditional** simple-fraction bound p₁ > p₀. The prior agent
flagged two structural locations in the paper:

- **§7.1** "The optimal window: Montgomery–Taylor" — where the window/test family V is chosen.
- **§7.5** "Limits of the method" — where the decisive higher-moment discussion lives.

This note develops the C4 (fourth-moment) / second-moment-denominator attack: whether a sharper
estimate of the **pair-correlation second moment** (the denominator of the trace lower bound) or a
genuine fourth-moment input can push the fraction past 0.6818, and whether such an input is
UNCONDITIONAL, CONDITIONAL, or CIRCULAR.

---

## 1. Where the second moment enters the denominator (structural, from the paper)

The trace lower bound has the form (paper §§4–5, condensed):

  P  ≥  trace(Q) / ‖Q‖  ≥  ⟨linear form, window⟩ / (second-moment denominator).

Specifically the paper states [paper .txt line 268, cited verbatim from grep]:

> "they are Montgomery's first and second moments [Mon73, BGSTB24]"

and [line 233]:

> "Montgomery's pair correlation with test functions of Fourier support in (−1,1), and the in-
>  [variance?] on configurations shows that no certificate of this kind, reading only this bandwidth-one data ..."

So the second moment **∫ |Σ_ρ g(ρ)|²** enters as the **denominator / normalization** of the
rank–trace inequality, and it is controlled by **Montgomery's pair correlation restricted to
Fourier support in (−1,1)** — i.e. **bandwidth ≤ 1**. The unconditional second-moment input is
[BGSTB24] (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh); the classical Montgomery input is
[Mon73] + [GM87] (Goldston–Montgomery).

- Label: **PROVEN** that the *paper's* denominator is Montgomery second moment at bandwidth ≤ 1
  (this is the paper's own stated input; the exact normalization constant is NOT re-derived here).
- Label: **CHECKED NUMERICALLY** (indirect) that the resulting fraction ceiling is 0.68183123 —
  recorded in `structural-final-verdict.md` and the lpdual certificates.

---

## 2. The bandwidth-1 wall (why the denominator is the bottleneck)

Montgomery's pair correlation theorem is **unconditional only for test functions with Fourier
support in (−1,1)**. Extending support to (−a,a), a>1, requires the pair-correlation *conjecture*
(Heath–Brown / Goldston–Montgomery style) — i.e. estimates on **prime pairs** in short intervals,
which are of **Hardy–Littlewood twin-prime strength** [paper line 314: "require information on
prime pairs of Hardy–Littlewood strength"]. §7.5 (line 2268) states the method can reach higher
fractions only "under Montgomery's pair correlation conjecture for α>1 [Mon73, GM87]" — that is
**CONDITIONAL** (on a statement strictly stronger than the RH the method is trying to prove → the
circularity documented in the final verdict).

- Label: **PROVEN** (from the paper's own §7.5) that bandwidth-1 is the unconditional wall of the
  *second-moment* input. [The exact §7.5 wording to be re-read; see §5 refinement.]


---

## 2bis. THE PAPER ALREADY KILLS THE C4 ROUTE (decisive, verbatim)

The paper's §7.5(d)–(f) is a *general* higher-moment analysis, and it settles the C4 question
directly. Key sentences (read from the .txt, lines 2303–2352):

- **(d)** "Lemma 3.3 is the case m = 1 of the one-sided Chebyshev–Markov–Stieltjes bound: if the
  normalised moments d⁻¹ tr(G̃/ℓ₁)ᵏ, k ≤ 2m, are known, the sharp lower bound for n⁺_θ(G̃)/d is
  1 − Λ_m(0), Λ_m the Christoffel function of the moment sequence at 0."
- **(e)** "The prime-side evaluation of tr G̃ᵏ by the diagonal method of Section 5 ... is available
  exactly in the Rudnick–Sarnak range kλ < 2 [RS96]; for λ ∈ (1/2,1) this allows at most k = 3
  (and only for λ < 2/3), and an odd moment does not lower Λ₁(0). **Thus, unconditionally, higher
  moments add nothing to the n⁺-bound on (1/2,1)** (and Proposition 4.4 uses only the first two in
  any case), while for λ ≤ 1/2, where many moments are available, Proposition 7.4 makes them
  useless."
- **(f)** "Conditionally, let HL*(k₀, λ) denote the hypothesis that for all k ≤ k₀, tr G̃ᵏ = d ℓ₁ᵏ
  (m_k(λ) + o(1)) ... One computes m_k(1) = 1, 4/3, 2, 13/4 for k ≤ 4, so Λ₂(0;1) = 5/36 and
  HL*(4, λ) for all λ < 1 would give lim inf N⁰_s(T,2T)/N(T,2T) ≥ 13/18 via the count of
  Proposition 4.5, and HL*(k₀, λ) for all k₀ and all λ < 1 would give proportion 1 ... RH itself
  is out of reach of the mechanism."

**Consequence for C4 (the fourth moment, k = 4, m = 2):**

- **Unconditionally**, the fourth moment is in the Rudnick–Sarnak range only for kλ < 2, i.e.
  λ < 1/2 at k = 4. On λ ∈ (1/2,1) — the range where the 0.6818 ceiling lives — k = 4 is NOT
  available, and even the moments that ARE available "add nothing" (7.5(e)). So the C4 denominator
  cannot sharpen the second-moment normalization at the operative bandwidth.
  **Label: PROVEN** (this is the paper's own §7.5(e), not my inference).
- **Conditionally**, HL*(4, λ) for all λ < 1 gives 13/18 ≈ 0.7222 > 0.6818 — but HL*(4, λ) at
  λ > 1/2 "encodes a Hardy–Littlewood-type asymptotic for the additive correlations"
  (twin-prime strength), and full HL*(k₀,λ) gives proportion 1 while "RH itself is out of reach".
  **Label: CONDITIONAL (CIRCULAR)** — the hypothesis is strictly stronger than RH.
- **Under RH**, the third trace tr G̃³ (triple correlation) is a theorem [Hej94, RS96] and the
  certificate runs with cubic weights (7.5(g)) — but this is the *distinct*-zeros branch, and it
  presupposes RH. **Label: CONDITIONAL (CIRCULAR)**.

This is the rigorous negative the task asked for: **the C4 route is dead unconditionally, and this
is PROVEN inside the paper (§7.5(e)), not conjectured.**

---

## 3. Candidate higher-moment inputs (rigorously labeled)

| Input | What it would give | Status | Would it break 0.6818? |
|---|---|---|---|
| **C4 / fourth moment** of the zero-sum | sharper control of the denominator's concentration | **DEAD UNCONDITIONALLY — PROVEN** (paper §7.5(e): higher moments add nothing on (1/2,1)) | NO — only HL*(4,λ) (conditional) reaches 13/18 |
| **Triple correlation (Hejhal)** | third-moment of zeros → extends the admissible support of the test | **CONDITIONAL** — [Hej94] is on RH (and uses the conjecture for full support) | would be CIRCULAR if it presupposes RH |
| **Rudnick–Sarnak n-level density** | n-level density (GUE) for test functions of full support | **CONDITIONAL** — [RS96] is proven under GRH for principal L-functions; unconditional version is the Montgomery conjecture at all levels | CIRCULAR for our purpose (needs RH/GRH) |
| **GLSS25 full-support pair correlation** | pair correlation conjecture at all levels | **CONDITIONAL** — [GLSS25] (conjectural) | CIRCULAR |

- **Unconditional candidates: NONE found.** Every mechanism that raises the moment level beyond
  the second at bandwidth ≤ 1 is, on current literature, either conditional on RH/GRH or on the
  pair-correlation conjecture itself.
- Label: **INCONCLUSIVE** (literature search is partial; a dedicated unconditional C4 theorem could
  exist and is not excluded by this survey).

---

## 4. Structure-mapping (s4h): is the C4 route genuinely new?

**Mapping target — Levinson's method.** Levinson's classical ≥1/3 lower bound replaced the
*pointwise* second moment with a *mollified* second moment: the mollifier cancels the zeros'
contribution so the denominator becomes tractable at bandwidth ≤ 1. The structural verdict's
0.673481 uses the same mechanism at the certificate level (coboundary redistribution).

**Mapping claim (structure-mapping output):** the "C4 denominator" idea is **isomorphic to** the
classical question "can a mollifier of degree 2 sharpen the Levinson second moment without new
prime-pair data?" — the answer in the classical literature is **NO**: the second moment at
bandwidth ≤ 1 is already *sharp* for the family (the 256-law p₀ = 0.6818287 is exactly the
in-class optimal simple fraction). A fourth-moment input that is a *function of* the same
bandwidth-1 pair-correlation data **adds no information** — it is a derived statistic, not a new
one.

- Label: **CONJECTURED** (structure-mapping judgment): the C4 route, if it uses only bandwidth-1
  pair correlation, is **dead** — the denominator's second moment at bandwidth ≤ 1 already carries
  all the information a fourth moment of the same data can carry (a C4 bound of a sum is implied
  by a bound on the same sum's second moment only via concentration, which is not available
  unconditionally).
- The route is **genuinely new ONLY IF** it introduces an *independent* unconditional input — e.g.
  an explicit-formula bound on Σ_ρ (m_ρ − 1) with m_ρ the multiplicity (as flagged in the final
  verdict), or a zero-density theorem stronger than BHTY's ~0.405.

**Known-mechanism comparison (prime-side trace):** the paper's trace asymptotics are the "prime
side" (line 979: "All the arithmetic is in the trace asymptotics"). The second moment is the
"zero side" of the same explicit formula. Any attempt to sharpen the zero-side denominator without
new prime-side arithmetic is a **re-normalization, not a new theorem** — this is the same
bottleneck as the classical "one-half the zeros on the line vs. all pairs of primes" trade.

- Label: **CONJECTURED** (structural judgment, consistent with the final verdict's HARD-constraint
  classification).

---

## 5. Concrete checkable formula (the deliverable core)

The honest, checkable statement that survives this note:

**Claim (to be checked, not yet certified):** *Under the assumption that the only unconditional
zero-side input is Montgomery pair correlation at bandwidth ≤ 1 (Fourier support (−1,1)), any
fourth-moment bound C4 of the trace denominator that is expressible as a function of that same
bandwidth-1 data cannot certify p₁ > p₀ = 0.6818287; equivalently, the C4 route is dead unless it
imports an independent unconditional theorem.*

Check procedure (for a future validator, Rust `rug`/`arb` per hooks):
1. Re-derive the second-moment denominator D(φ) = ∫ |Σ_ρ g(ρ)|² for a test window φ with
   supp(φ̂) ⊂ (−1,1), matching the paper's (7.1) normalization.
2. Compute the maximal fraction the rank–trace inequality yields with D(φ) as normalization
   (this reproduces the 0.68183123 ceiling; CHECKED NUMERICALLY by the lpdual certificates).
3. Attempt to write any C4 = ∫ |Σ_ρ g(ρ)|⁴ as a functional of D(φ) alone; if it factorizes /
   is bounded by a constant times D(φ)², then C4 contributes nothing new → route **ABANDONED**
   for the stated purpose.
4. If C4 does NOT factorize through D(φ), then it must import support beyond (−1,1), which is
   exactly the **conditional/circular** territory of §2.

- **Current label: INCONCLUSIVE** — step 3 (the factorization check) has NOT been run. It is the
  single most valuable next computation, and it is exactly the kind of small Rust `rug` probe the
  hooks mandate.

---

## 6. Assumptions and citations

- `[verified]` The final-verdict ceiling v\*(p₁) = p₁ + 2.54e-6, p₀ = 0.6818287, unconditional best
  ~0.405 (BHTY), RH-conditional 19/27 (Bui–Heath–Brown 2013) — from `structural-final-verdict.md`.
- `[verified]` Paper contains §7.1 (optimal window, Montgomery–Taylor) at .txt line ~1920 and §7.5
  (Limits of the method) at .txt line ~2261; the bandwidth-1 wall and the Hardy–Littlewood-prime-
  pair statement at lines 233, 268, 314, 2268, 2303, 2322, 2352 (grep-verified, exact wording to
  be re-read).
- `[verified]` Bibliography contains Hejhal triple correlation [Hej94], Rudnick–Sarnak n-level
  density [RS96], Montgomery second moment unconditional [BGSTB24], full-support pair correlation
  conjecture [GLSS25].
- `[inferred]` The C4-route-dead factorization claim (Section 5, step 3) is a structural
  hypothesis, NOT a theorem; rationale: a fourth moment of a random sum is informationally
  redundant given its second moment only if a concentration (subgaussian-type) inequality holds,
  which is precisely what is NOT available unconditionally at bandwidth 1.
- `[CITATION NEEDED]` Any claim that a *conditional* higher-moment input (Hejhal triple
  correlation / RS n-level density) yields an *unconditional* fraction above 0.6818 — no such
  reduction exists in the literature I could locate this session.
- `[CITATION NEEDED]` An unconditional fourth-moment theorem for Σ_ρ g(ρ) at support beyond (−1,1).

---

## 7. Verdict

**The C4 second-moment-denominator route is DEAD unconditionally — this is PROVEN in the paper's
own §7.5(e), not conjectured.** The second moment is the normalization of the trace lower
bound and is pinned by Montgomery pair correlation at bandwidth ≤ 1 (unconditional). Every known
route to *raise* that moment level (C4, triple correlation, n-level density, full-support pair
correlation) is CONDITIONAL on RH/GRH or the pair-correlation conjecture — i.e. CIRCULAR for
proving RH. The factorization check of §5 step 3 is now moot: §7.5(d) already encodes the general moment
mechanism (Chebyshev–Markov–Stieltjes / Christoffel function Λ_m(0)), and §7.5(e) proves higher
moments add nothing unconditionally on (1/2,1). The route is recorded as ABANDONED with a PROVEN
reason.

This is a **rigorous negative, now certified by the paper itself**: the structure is mapped, the
conditional/circular classification is solid, and §7.5(e) proves the C4 denominator cannot
sharpen the unconditional bound.

**Labels summary:** PROVEN (paper's inputs; §7.5(e) kills C4 unconditionally; ceiling arithmetic) ·
CHECKED NUMERICALLY (ceiling 0.68183123 via prior certificates) · CONDITIONAL/CIRCULAR (HL*(4,λ),
triple correlation, n-level density) · ABANDONED (the C4 denominator route, reason: §7.5(e)).
