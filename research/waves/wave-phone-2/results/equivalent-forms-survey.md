# Equivalent Forms of RH — Honest Classified Survey

**Agent:** equivalent-forms-survey. **Frame:** reasoning from standard literature only, no compute, no ssh.
**Reads:** attack-record.md, ledger.md (program language: certificates, law, moments m₃, E(1), marked-T, ceiling 0.6818 law-specific).
**Taxonomy used below:** part (c) splits into two kinds of "equivalent":
- **(c2) disguise** — logically ⟺ RH *and* a mere rephrasing (same objects, same proof wall). No new idea can live here.
- **(c1) structurally distinct** — logically ⟺ RH but with genuinely different objects/positivity structure, so a *new method* could be hosted (proving it is still proving RH; there is no shortcut — only a different door).
- **Lindelöf** is the only item that is *not* equivalent (strictly weaker).

Labels per program charter: PROVEN / CHECKED NUMERICALLY / CONJECTURED / SPECULATIVE.
Promise: HIGH = real independent surface; MEDIUM; LOW = RH-in-disguise.

---

## 1. De Bruijn–Newman constant Λ — [Λ ≤ 0 ⟺ RH]
(a) Let H_t(z) be the heat-flow of ξ (Fourier/heat convolution of the ξ-kernel). Λ = inf{ t : H_t has only real zeros }. RH ⟺ Λ ≤ 0; Newman gave Λ ≥ 0, so RH ⟺ Λ = 0.
(b) Zeros of H_t move monotonically in t and at large t converge to (horizontal shifts of) the critical-line zeros; t=0 recovers ξ. Real-at-t=0 = all ξ-zeros on the line.
(c) **disguise (c2).** Λ ≤ 0 is literally RH; there is no strictly weaker intermediate. Rodgers–Tao proved Λ ≥ 0 unconditionally — a real theorem, but the wrong side (it is a lower bound; RH needs the upper bound). No route to Λ ≤ 0 short of RH exists by definition.
(d) **Numerical: yes, cheap and parallel.** Λ is a min over (t, z)-zeros; each zero is independent root-finding ("turtle"/mollifier method, Polymath 15). Current best Λ ≤ 0.22 (Polymath 15, 2020); prior Λ < 0.5 (Ki–Kim–Lee). Pushing to 0.19, 0.17… is routine distributed work.
(e) Not cracked because a finite bound can never reach 0 without new structure; the gap 0.22 → 0 is exactly RH and the numerics have no structural lever.
**Label:** PROVEN (equivalences, Λ ≥ 0); CHECKED NUMERICALLY (Λ ≤ 0.22). **Promise: LOW** (proof route), MEDIUM (numerical headline only).

## 2. Nyman–Beurling criterion — [closure of fractional-part span]
(a) RH ⟺ χ_{(0,1]} lies in the L²(0,1)-closure of the span of ρ_θ(x) = {θ/x} − θ·{1/x}, θ ∈ (0,1].
(b) Approximating χ by combinations of ρ_θ is dual to approximating 1 by Dirichlet polynomials in 1/ζ(s); the distance² equals a sum over zeros Σ_ρ |1/(ρ(ρ−1))|-type, so closure ⟺ 1/ζ pole-free in Re(s) > 1/2 ⟺ RH (Báez-Duarte; Balazard–Saias–Yor).
(c) **structurally distinct (c1).** A Hilbert-space approximation / determinantal problem, reducible to exact finite linear algebra (distance d_N to the span of the first N functions; RH ⟺ d_N → 0). Different objects, different positivity than Levinson.
(d) **Numerical: yes, excellent.** d_N is exactly computable in rational/interval arithmetic for large N; parallelize over N. Analytic: only the same d_N → 0 wall.
(e) Not cracked because d_N → 0 is equivalent to RH; best unconditional bounds sit at c/log-ish scale and never approach 0.
**Label:** PROVEN (equivalence); CHECKED NUMERICALLY (d_N values). **Promise: MEDIUM.**

## 3. Riesz criterion — [growth of the Riesz function]
(a) RH ⟺ R(x) = Σ_{n≥1} (−1)^{n+1} x^n / ((n−1)! ζ(2n)) = O(x^{1/4+ε}).
(b) Mellin transform of R is essentially 1/(ζ(2s)Γ(s)); its growth order reads off the rightmost pole, i.e. the first zero off the line. Textbook.
(c) **disguise (c2).** Growth = RH verbatim; no new structure, only a different way to state the same zero.
(d) Numerical: feasible (oscillatory series, huge cancellation) but it is only a *test* of RH, never a lever.
(e) Not cracked because O(x^{1/4+ε}) is RH itself.
**Label:** PROVEN (equivalence). **Promise: LOW.**

## 4. Li's criterion — [positivity of Keiper–Li coefficients λ_n]
(a) RH ⟺ λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] ≥ 0 for all n ≥ 1. The λ_n are exactly computable from Stieltjes constants (λ_n = (1/(n−1)!) dⁿ/dsⁿ[s^{n−1} log ξ(s)]_{s=1}).
(b) Writing ρ = 1/2 + iγ, the term 1 − 1/ρ has modulus < 1 iff Re(ρ) = 1/2; positivity of a moment-like sum of powers for all n forces every |1 − 1/ρ| ≤ 1, i.e. all Re(ρ) = 1/2.
(c) **structurally distinct (c1), and the closest to the program's existing machinery.** λ_n ≥ 0 ⟺ {λ_n} is a Stieltjes/moment sequence ⟺ a certain explicit Hankel matrix (in Stieltjes constants) is positive semidefinite. That is a *moment-positivity certificate*, the same species as the program's law / m₃ / E(1) / marked-T reads — but a **different certificate class from Levinson's zeros-counting**, hence NOT subject to the 0.6818 (law-specific) ceiling. Under RH λ_n ~ (n/2) log n (positive, growing); if RH fails, λ_n eventually turns negative with exponential amplitude oscillating at the off-line height — an extremely sharp probe.
(d) **Numerical: yes.** Compute Stieltjes constants to high precision (parallel), form λ_n to n ~ 10⁴–10⁵, check positivity and Hankel inertia (interval/rational). Symbolic: hunt a positive-definite representation of the Hankel form (Christoffel–Darboux / continuous "law" whose moments are λ_n) — a genuine new-idea door.
(e) Not cracked because positivity of the full infinite Hankel matrix is equivalent to RH; finite inertia checks cannot close the tail.
**Label:** PROVEN (equivalence, λ_n ↔ Stieltjes); CHECKED NUMERICALLY (Maślanka/others). **Promise: HIGH.**

## 5. Robin / Lagarias elementary inequality — [σ(n) bound]
(a) Robin: RH ⟺ σ(n) < e^γ n log log n for all n > 5040. Lagarias (elementary form): RH ⟺ σ(n) ≤ H_n + exp(H_n)·log H_n for all n ≥ 1, equality iff n = 1.
(b) The maximal order of σ(n)/(n log log n) is governed by whether the PNT error term has its worst oscillation forced by an off-line zero; Robin's constant e^γ is precisely the RH-optimal constant. Equivalence is a real theorem (Robin, Lagarias) but goes through the standard zero machinery.
(c) **disguise (c2).** Elementary-looking, yet proving the inequality for all n is exactly as hard as RH; there is no independent mechanism in it.
(d) Numerical: fully parallel counterexample search over n (trivial per-n cost); but a proof route does not exist.
(e) Not cracked because it is RH; finite verification to 10^k never closes the infinite gap.
**Label:** PROVEN (equivalences). **Promise: LOW.**

## 6. Weil's explicit formula / positivity of the Weil distribution
(a) RH ⟺ for every even test function h with compactly supported Fourier transform ĥ and ĥ ≥ 0 (positive type), Σ_γ h(γ) ≥ 0 — i.e. the "Weil distribution" Σ_γ δ_γ (minus the known archimedean/primes term) is a positive functional.
(b) The explicit formula expresses Σ_γ h(γ) as (prime sum) + (correction); positivity for all admissible h is equivalent, by Beurling–Selberg majorant duality, to the spectral measure being non-negative ⟺ no off-line zeros.
(c) **structurally distinct (c1) — but this is the program's EXISTING home.** Levinson–Conrey *is* a finite-family application of Weil positivity (chosen h, moments, weights). So it is a HIGH surface but not a *novel* one for this program; the 0.6818 ceiling is exactly the gap between the program's restricted class of h and the full class.
(d) Numerical/symbolic: the program already operates here (law, weights 2/(7−r), m₃, E(1)). Novelty would have to come from a *wider function class* than the certificate family currently in use.
(e) Not cracked because full positivity over all h is RH; every finite family faces its own ceiling.
**Label:** PROVEN (equivalence). **Promise: HIGH surface, but already occupied — not the "new" door.**

## 7. Mertens / zeta-positivity — [M(x) = O(x^{1/2+ε})]
(a) RH ⟺ M(x) = Σ_{n≤x} μ(n) = O(x^{1/2+ε}) for all ε > 0. (The stronger "Mertens hypothesis" |M(x)| ≤ √x is FALSE — Odlyzko–te Riele 1985 — but the weakened O-form is equivalent to RH.)
(b) 1/ζ(s) = Σ μ(n)/n^s; M(x) = O(x^{1/2+ε}) ⟺ no pole of 1/ζ in Re(s) > 1/2 + ε via Perron. Faithful translation, nothing more.
(c) **disguise (c2).** M(x) is a *test* of RH, not a route; and the natural sharp bound was already disproved, so even the "expected" numerics are dead ends.
(d) Numerical: μ is sieve-computable to 10²⁰+ (Kotnik–van de Lune et al.), parallel; but it only ever *checks* RH.
(e) Not cracked because it is RH; and the naive bound's failure (Odlyzko–te Riele) removes the one numerically-reachable hope.
**Label:** PROVEN (equivalence); CHECKED NUMERICALLY (Mertens-hypothesis refutation). **Promise: LOW.**

## 8. Lindelöf-vs-RH hierarchy — [the genuinely *weaker* surface]
(a) LH: ζ(1/2+it) = O(t^ε). RH ⟹ LH, strictly (LH constrains size on the line, not location). Full ladder: LH ← density hypothesis N(σ,T) = O(T^{2(1−σ)+ε}) ← zero-density estimates ← subconvexity μ(σ) (current μ(1/2) ≤ 13/84, Bourgain 2017) ← the 2k-th moments of |ζ(1/2+it)| (2nd, 4th known; higher open; Keating–Snaith RMT conjecture).
(b) Not equivalent to RH — this is the point. It is a *strictly easier*, winnable hierarchy that shares technique with RH.
(c) **genuinely independent (and NOT equivalent).** The moments problem / subconvexity is a real attack surface with active, incremental progress. It does not imply RH and does not directly yield zeros-on-line proportion.
(d) **Numerical: excellent and parallel** (compute moments to high height, test Keating–Snaith; subconvexity is analytic). A distributed program could produce genuinely publishable results (empirical moments at new heights) even though it will not touch RH.
(e) Not cracked because it is *hard in its own right* (moments 2k for k ≥ 3 are wide open); progress is real but slow.
**Label:** PROVEN (implications); CHECKED NUMERICALLY (moments ≤ 4, 13/84). **Promise: HIGH as an intermediate surface; LOW as a route *to RH*.**

---

## 9. Jensen polynomials — [hyperbolicity, Griffin–Ono–Rolen–Zagier 2019]
(a) RH ⟺ for every d ≥ 1 and n ≥ 1, the Jensen polynomial J^{d,n}(X) built from the Taylor coefficients of ξ(1/2 + ix) (equivalently the "γ(n)" coefficients) has all real roots (is hyperbolic).
(b) The coefficients γ(n) are moments of a measure whose support sits on the line iff RH; Jensen-polynomial hyperbolicity for all (d,n) is exactly the total-positivity/moment condition for that measure (this is the *new* bridge: Hermite-polynomial universality in the limit).
(c) **structurally distinct (c1), and the freshest surface.** Finite-dimensional, exactly computable, and only ~6 years old — far from exhausted. Proven for d fixed with n → ∞ (d = o(n^{1/2})); the *sharp* range d ≍ n^{1/2} is the open boundary that carries RH.
(d) **Numerical: excellent and trivial to parallel** — each J^{d,n} is an explicit polynomial; root-count/hyperbolicity is per-(d,n) independent. Symbolic: an Obreschkoff / derivative-interlacing or monotonicity argument could push the proven range toward the sharp threshold — a plausible home for a genuinely new idea.
(e) Not cracked because hyperbolicity for ALL (d,n) (including the sharp d ≍ √n band) is equivalent to RH; the 2019 universality results stop at d = o(√n).
**Label:** PROVEN (equivalence, d = o(√n) universality); CHECKED NUMERICALLY (partial ranges). **Promise: HIGH.**

## 10. Hilbert–Pólya spectral interpretation — [operator whose spectrum = zeros]
(a) RH ⟺ there exists a self-adjoint operator H on a Hilbert space whose eigenvalues are {1/2 ± iγ} (the non-trivial zeros). Conjectured, not constructed; Berry–Keating xp + px is the canonical near-miss (missing boundary condition); Connes' adelic spectral framework is the deep modern form.
(b) If such an H existed, RH is automatic (spectrum of self-adjoint operator is real). But no H is known — so this is a conjecture *about* a proof route, not a usable equivalent statement.
(c) **SPECULATIVE — not a precise theorem surface.** It cannot host a distributed computation because the object does not exist yet. It matters only as a *target*: the program's GUE/CUE, E(1) = −1/(6N²), and law structure are exactly the spectral language, so a *constructed* operator (or trace formula) would be the ultimate certificate-class change.
(d) No numerical content until someone constructs a candidate operator; then eigenvalue computation becomes the test.
(e) Not cracked because nobody has found the operator; the self-adjointness + correct spectrum combination is the entire difficulty.
**Label:** SPECULATIVE. **Promise: HIGH ceiling, but not currently attackable.**

---

## VERDICT (5 lines)

1. **Attack Li's criterion as Hankel-matrix/moment positivity** — it is a moment-positivity certificate class orthogonal to Levinson's zeros-counting, it speaks the program's native language (law, m₃, E(1), marked-T), and its finite approximations have **no a priori 0.6818 ceiling**; the open door is a positive-definite representation of the λ_n Hankel form (the program's own "law" is the prototype).
2. **Probe Jensen-polynomial hyperbolicity** — a 2019, finite-dimensional, exactly-computable reformulation; the sharp d ≍ n^{1/2} band is numerically probeable in parallel and may admit a rigid Obreschkoff/interlacing proof — the most "unworked" surface on the list.
3. Both are RH-equivalent (no shortcut), but that is the correct target: the program needs a **certificate class whose ceiling is not 0.6818**, and both Li (moment) and Jensen (hyperbolicity) provide one.
4. Numerics are embarrassingly parallel for both (Stieltjes→λ_n→Hankel inertia; per-(d,n) root counts); symbolic effort concentrates on the positivity/interlacing lemma each needs.
5. Reject for novelty: Λ (finite-bound-only), Robin/Mertens/Riesz (pure disguise), Weil-positivity (already the program's occupied home), Hilbert–Pólya (no object to compute with yet).
