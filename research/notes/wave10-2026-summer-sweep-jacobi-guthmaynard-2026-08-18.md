# Wave-10: Feb–Aug 2026 literature sweep — Jacobi pencils (Jin 2608.08714) + Guth–Maynard zero-density note (2607.04632)

**Date:** 2026-08-18 (night continuation, quiet-hours lifted). **Status:** CLOSED — two genuinely new items adjudicated, both NOT-A-LEVER, both registered in closure-DAG.

**Purpose:** wave-22 (wave-9) swept literature through the GS papers (Feb 2026). The Feb–Aug 2026
window was unexplored. This sweep found exactly two items relevant to our two surviving openings
(GJT-completion; GS-2026 diagonal bridge) plus non-lever sideline items.

---

## 1. Jin, "Jacobi Endpoint Pencils and Sharp Interlacing for Centered Binomial Samples" (2608.08714, 9 Aug 2026)

**Looks like the GJT toolkit.** For real even/odd entire H of order ≤ 1, with centered binomial sample
B_{2n+1}[H](z) = Σ_j C(2n+1,j) H(j−(2n+1)/2) z^j, removing the forced endpoint zero and writing
x = z + z⁻¹ gives quotient C_n(x). Theorem 1.1: if Z(F) ⊆ S_√(15/28) (|Re u| ≤ √(15/28) ≈ 0.7319),
then C⁻_{F,n} ⪯ C⁻_{F,n+1} (weak Obreschkoff / interlacing) for all n ≥ 0. Odd case: strip S_1.

**Verdict: NOT-A-LEVER. Two independent structural reasons (both verified from the arXiv text):**

(a) **The strip condition is AUTOMATIC, hence consistency-only.** For the Riemann case F(u) = Ξ(1/2+u),
zeros of F sit at u = ρ − 1/2, Re u = β − 1/2 with 0 < β < 1 by the functional equation, so
|Re u| < 1/2 < √(15/28) ≈ 0.7319 *no matter what* — whether RH holds or not. The hypothesis says
nothing about where zeros are within the strip; it is satisfied in every RH-false world (barrier-zoo
worlds included). A theorem whose hypothesis is RH-independent cannot separate RH from its negation.

(b) **Object identity fails — the sample family is NOT the GJT family.** GJT/RH criterion
(our frontier note, `frontier-smalln0-slice-2026-08-18.md`): RH ⟺ all Jensen polynomials
J^{d,n}(X) = Σ_j C(d,j) γ(n+j) X^j hyperbolic, where γ(n) = n! M_n/(2n)! is the **moment-coefficient
sequence** (M_n = 2∫₀^∞ Φ(u) u^{2n} du). Jin's B_d[H] uses **point evaluations H(j−d/2)** at
half-integers. These are different objects: point values of Ξ at half-integers are not its moment
coefficients (they'd coincide only if Ξ were a very special function; for ξ they are structurally
different). Jin's theorem's real content is interlacing/divided-difference structure for the
**point-value sample polynomials** — which yields signed resultants and inequalities among completed
L-function **special values** (the paper's stated applications), not zero-location statements.
Indeed the paper's target is Dedekind zeta *derivatives* and newform critical-value blocks, not RH.

**Method note (banked as new knowledge, not a lever):** the paper proves the interlacing theorem via
Jacobi spectral multipliers, Bernstein variation diminution, and total nonnegativity of finite Jacobi
matrices attached to zero orbits. That toolkit is adjacent to but distinct from the closed
moment-TP/binomial-moment strands (it does NOT assume the moment sequence is a moment/TP-2
sequence). If a future idea needs "interlacing of point-value samples of Ξ", this is the reference.
But it cannot enter the RH criterion because the moment sequence γ(n) = n!M_n/(2n)! is itself
PROVEN non-moment (Hankel det2 < 0), and this theorem does not apply to the moment coefficients.

## 2. Turnage-Butterbaugh, "A decades-long breakthrough in zero-density estimates and primes in short intervals" (2607.04632, 6 Jul 2026)

**Expository** account of Guth–Maynard 2024: first improvement over Ingham for a key location in the
critical strip in 80+ years; primes in short intervals.

**Verdict: NOT-A-LEVER.** The GS-2026 diagonal-bridge gap is: prove any unconditional diagonal bound
Σ_{γ=γ′}1 ≤ (C+o(1))N, C<2, equivalently control the off-line symmetric-diagonal terms
Σ_{β≠1/2} m_ρ. Those need counting zeros with β in the *near-line* region (1/2, 1/2+ε). Zero-density
theorems (Ingham; Guth–Maynard) all have exponent → 1 as σ → 1/2⁺: 3(1−σ)/(2−σ) → 1 (Ingham),
and GM's is likewise trivial at σ = 1/2⁺. The near-line zeros are exactly the S(T)-type obstruction
(gaps to the line behave like S(T)-contributions). So GM improves primes-in-short-intervals and
zero-density away from 1/2 but supplies **no** input to the diagonal bound, and it leaves the F-on-[0,1]
bandwidth-one record class unchanged. Consistent with the DAG's `gs-2026-diagonal-bridge` node.

## 3. Sideline items in the sweep (no adjudication needed)

- 2607.14515 "Beyond RH bounds: pair correlation → least prime in AP / smallest non-residue": pair-correlation results for **primes**, not zero proportions; no bearing on record or RH side.
- 2604.05733 "Small gaps between consecutive zeros" (resonance-correlation method): small-gap scale, not proportion-on-line; below our axes.
- 2605.20224 "Truncated Weil form" (Connes–van Suijlekom): operator route, already closed (Weil–Deligne structurally impossible; HB degeneracy).
- 2606.07312 (zeta-RMT via hyperfunctions), 2603.26507 (random zeta integral means), 2605.09282 (low-lying zeros for L-functions on the line, family-level): consistency-antecedent or foreign-family material only.

---

## Closure statement

**Both new items CLOSED as levers.** DAG updated: 24 nodes / 22 edges. No new funded probe — the
two surviving openings remain exactly as before:
- GJT-completion small-n ⟺ RH (Jin's strip theorem does not reach the moment-coefficient family);
- GS-2026 unconditional diagonal bound C<2 (GM zero-density cannot control near-line zeros).

The Feb–Aug 2026 window is now fully adjudicated. Files: `research/papers/jacobi-pencils-2608.08714.txt`,
`guth-maynard-2607.04632.txt` (downloaded, pdftotext), this note, closure-DAG nodes
`jacobi-pencils-2608`, `guth-maynard-zerodensity`.