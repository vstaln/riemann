# Bui–Heath-Brown: the precise RH-dependencies of the 19/27 simple-zero theorem

**Agent:** architect (atomic research deliverable). **Date:** 2026-08-14.
**Scope:** literature only, no compute. Extract EXACTLY what RH supplies in Bui–Heath-Brown
(arXiv:1302.5018, "On simple zeros of the Riemann zeta-function") and assess which of those
hypotheses a box condition or a zero-density estimate could replace — the "partial
unconditionalization" question.

**Sources read this session:** arXiv:1302.5018 full text (PDF, export.arxiv.org); arXiv:2306.04799
abstract (BGSTB); `structural-thread-newinput-2026-08-14.md`. CGG 1998 content is `[secondary]`
via the 1302.5018 text.

---

## 0. One-line answer

**RH supplies EXACTLY ONE thing to Bui–Heath-Brown — the identification S₂ = Σ_{0<γ≤T} |B′(ρ)|² —
and the paper says so verbatim: *"Assuming RH we have S₂ = Σ_{0<γ≤T}|B′(ρ)|². Note that this is
the only place we need RH."* Everything else (the moment evaluation, all error terms, and the
GLH-removal that is the paper's headline) is already unconditional.** The single RH-input is a
qualitative, all-or-nothing statement (every zero satisfies 1−ρ = ρ̄, i.e. lies on Re s = 1/2),
which is exactly the kind of statement a box condition or zero-density estimate can quantitatively
approximate. This *contradicts* the working hypothesis in the structural-thread note that removing
RH from BHB is "strictly harder than the box estimate": the arithmetic core is already
unconditional, and the RH-removal reduces to the SAME box/density question applied to one explicit
weighted sum over off-line zeros.

---

## 1. The discrete mollified moment setup (one paragraph)

Let B(s) = Σ_{k≤y} b(k)/k^s, b(k) = μ(k)·P(log(y/k)/log y), be the Levinson–Conrey mollifier
(y = T^θ, 0 < θ < 1/2, P real with P(0)=0, P(1)=1). Since ρ is simple iff ζ′(ρ) ≠ 0, Cauchy's
inequality gives N*(T) ≥ |Σ_{0<γ≤T} B′(ρ)|² / Σ_{0<γ≤T} |B′(ρ)|² (eq. (1)); here and below sums run
over all zeros ρ = β+iγ with 0 < γ ≤ T. The **first and second mollified moments of the derivative**
are S₁ = Σ_{0<γ≤T} B′(ρ) and S₂ = Σ_{0<γ≤T} B′(ρ)B′(1−ρ), i.e. the second moment is taken at the
*reflected point* 1−ρ. Both are evaluated by the residue theorem on a symmetric rectangle: the
pole of ζ at s = 1 gives the main terms, the functional equation pairs the two vertical sides, and
the horizontal segments give error terms. The evaluation produces S₁, S₂ in terms of main terms
M_ν = Σ_{k≤y} Σ_{m≤kT/2π} a_ν(m) b(k)/k · e(−m/k) (ν = 1, 2), where a₁(n) are the Dirichlet
coefficients of ζ′/ζ(s) and a₂(n) the coefficients of (ζ′/ζ)²(s)B(s) — the "discrete" character of
the moments comes from these coefficient convolutions. This is the mollified ζ′/ζ (equivalently ζ′)
moment machinery: the arithmetic lives entirely in M_ν.

---

## 2. Hypothesis-by-hypothesis table

| Step of the proof | What input it uses | RH? / GLH? / box? / density? | Substitute by zero-density or box? |
|---|---|---|---|
| **A. Cauchy reduction**, eq. (1): N*(T) ≥ S₁² / Σ\|B′(ρ)\|² | denominator must equal S₂, i.e. B′(ρ)B′(1−ρ) = \|B′(ρ)\|² for every zero, i.e. **1−ρ = ρ̄** | **RH — the ONLY RH use** (qualitative: all zeros on the line) | **YES (in principle).** Write Σ\|B′(ρ)\|² = S₂ + E with E = Σ_{0<γ≤T} B′(ρ)·[B′(ρ̄) − B′(1−ρ)]. E = 0 under RH; a box condition makes ρ̄ ≈ 1−ρ (E small); a density estimate bounds the number/weight of off-line ρ (E bounded). See §4. |
| **B. Lemma 1**: asymptotics of S₁, S₂ | residue theorem + functional equation + convexity bound on horizontal segments (ζ ≪ t^{(1−σ)/2+ε}) | **none — unconditional** | n/a |
| **C. Main terms**, M_{ν,1}, q = 1 (eqs. (7),(8)) | residue of ζ′/ζ at the pole s = 1 | **none — unconditional** | n/a |
| **D. M_{ν,2}, 1 < q ≤ Λ** (eq. (9)) | Siegel's theorem on exceptional real zeros of L-functions | **none — unconditional, but ineffective** (constant c(A) not effective) | n/a |
| **E. M_{ν,3}, Λ < q ≤ y** (Lemma 2) | Heath-Brown's generalized Vaughan identity (Lemma 3) + hybrid large sieve (Montgomery Thm 7.1) | **GLH REMOVED here** (CGG needed a 6th-moment/GLH bound of Dirichlet L-functions; BHB replace it). Unconditional. | n/a |
| **F. Optimization**: P(x) = −θx² + (1+θ)x, θ → 1/2− | calculus; S₁ ∼ (19/24)TL²/2π, S₂ ∼ (57/64)TL³/2π | **none — unconditional** | n/a |
| **G. Corollary** κ_d ≥ 0.84665 | Montgomery's 2N* ≤ Σ(m−2)(m−3)/m observation + Cheer–Goldston Σ m(ρ) ≤ 1.3275 N(T) | **none — unconditional** | n/a |

**Net:** the published theorem uses RH only in Step A. GLH is fully removed (Step E). The only
zero-location input in the entire paper is the Step-A identification 1−ρ = ρ̄.

---

## 3. Verdict: minimal hypothesis set for a positive simple fraction > 0.6818

The minimal hypothesis set is:

> { functional equation, convexity bound, Siegel's theorem, hybrid large sieve + generalized
> Vaughan identity (all **unconditional**, already in the paper) } **plus ONE replaceable input:**
> a bound on the off-line correction **E = Σ_{0<γ≤T} B′(ρ)·[B′(ρ̄) − B′(1−ρ)]**, equivalently a
> bound on the off-line part of Σ_{0<γ≤T}|B′(ρ)|².

RH is the special case E = 0. The Cauchy bound degrades smoothly:

**N*(T) ≥ S₁² / (S₂ + E) ≈ (19/27)·N(T)·(1 − E/S₂)**,

so the simple fraction is ≥ 19/27 × (1 − E/S₂). To clear 0.6818 requires
**E/S₂ < 1 − 0.6818·(27/19) ≈ 0.0311** (a 3.1% slack). Both substitute types are viable in
principle:

- **Box condition** (e.g. BGSTB's |β − 1/2| < 1/(2 log T)): makes ρ̄ − (1−ρ) = 2(β − 1/2) small,
  giving E ≪ Δ·Σ|B′(ρ)||B″(ρ)| + …, i.e. E is a first-order perturbation in the box width Δ.
- **Zero-density estimate** (e.g. Guth–Maynard 2024): bounds Σ_{β≠1/2} |B′(ρ)|² by an integral of
  N(σ,T) against |B′|², controlling E without locating individual zeros.

**Honest bottom line (INCONCLUSIVE at the 3.1% threshold):** the *shape* of the substitution is
clear and the arithmetic core is already unconditional, but the off-line weighted moment
Σ_{β≠1/2}|B′(ρ)|² (or |B′B″|) is itself a discrete-moment problem not obviously easier than the
original, and no unconditional/box/density bound on E appears in the literature read this session.
BGSTB's 0.617 result is a PROVEN instance of the same substitution *at the pair-correlation level*
(Montgomery's 2/3), confirming the mechanism is real — but 0.617 < 0.6818, and transferring the
substitution to the BHB discrete-moment level is exactly the open problem.

---

## 4. Labels

| Claim | Label |
|---|---|
| ≥ 19/27 of zeros simple, assuming RH (BHB 2013) | **PROVEN** (published) |
| RH is used in exactly one place: S₂ = Σ\|B′(ρ)\|² | **PROVEN** (verbatim in paper) |
| GLH removed via Heath-Brown's generalized Vaughan identity | **PROVEN** (paper's headline) |
| Lemma 1 + Lemma 2 (all moment/error estimates) unconditional | **PROVEN** (paper states "all the analysis is unconditional") |
| Box or density estimate can substitute for the single RH-use (E = o(S₂)) | **CONJECTURED** (mechanism clear; quantitative bound on E not in literature read) |
| Clearing 0.6818 needs E/S₂ < 3.11% | **PROVEN** (arithmetic: 1 − 0.6818·27/19 = 0.0311) |
| The box/density route reaches the 3.11% slack | **INCONCLUSIVE (blocker:** no bound on the off-line weighted moment Σ_{β≠1/2}\|B′(ρ)\|² is known) |

---

## 5. Next concrete lemma

**Lemma N (candidate — the "partial unconditionalization" lemma):**
Prove that under a box condition |β − 1/2| ≤ Δ(T) (or a Guth–Maynard-type zero-density estimate
N(σ,T) ≤ T^{1−c(σ−1/2)}), the off-line correction satisfies
**E = Σ_{0<γ≤T} B′(ρ)·[B′(ρ̄) − B′(1−ρ)] = O(Δ·T L³ + (density tail))**, by (i) Taylor-expanding
B′(ρ̄) − B′(1−ρ) at 1/2+iγ, and (ii) reducing Σ|B′(ρ)||B″(ρ)| to the S₂-type moments already
computed in Lemma 1. This would make the resulting simple fraction an **explicit function of Δ or
of the density exponent**, κ* ≥ 19/27 − O(Δ) (or the density analogue), turning "partial
unconditionalization" into a single quantitative statement. First check: whether the |B′B″|
moment is O(S₂) purely from the residue machinery (no new hypothesis) — if yes, the box width
needed to clear 0.6818 is a concrete number, and the whole question reduces to a known-type
box/density estimate.

---

## Constraints / framing (s4h logic-constraint-mapping, compressed)

- p₁ in the certificate = simple fraction over **all** nontrivial zeros (on + off line); 19/27 is
  the only known RH-conditional shape clearing the 0.6818 in-class ceiling. So the RH-dependence
  of BHB is the structural lever.
- Hard constraint discovered: the RH-use is a **single qualitative identification**, not a diffuse
  dependence — this is what makes "partial unconditionalization" a well-posed single-target problem.
- Hidden constraint surfaced: even with the box/density substitution, the *denominator* is the
  binding term; the numerator S₁ is already unconditional. The leverage point is exclusively E.
- Assumptions (tagged): `[verified]` RH appears only at S₂ = Σ|B′(ρ)|² (paper text);
  `[verified]` GLH was already removed (paper text); `[inferred]` the box/density substitution for
  E has not been carried out in the literature (no such bound found in the sources read this
  session — this is an absence-of-evidence statement, not a proof of impossibility).
