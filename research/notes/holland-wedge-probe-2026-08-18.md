# Holland 2608.08682 hyperbolicity-wedge mechanism probe — FINAL

Date: 2026-08-18. Agent: builder. Task: is Holland's new wedge theorem (the single genuinely
NEW structural theorem from the lit sweep) margin-driven (S1-dead family) or genuinely
different (a new sufficiency family)? Firewall binding: finite-degree Jensen hyperbolicity
carries ZERO RH evidence; this is a structural probe, NOT an RH lever.

Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE.

## 0. Theorem (from paper text, PROVEN in literature)
- ξ_c(z)=ξ(1/2+z)=Σ γ(n)/n! z^{2n}, γ(n)>0. J^{d,n}(X)=Σ_{j=0}^d C(d,j)γ(n+j)X^j.
- **Thm 1.1:** ∃ absolute K>0 s.t. n³log²(n+2) ≥ K·d⁵ ⟹ J^{d,n} has d distinct negative real
  zeros. Equiv d ≤ c·n^{3/5}·log^{2/5}(n+2).
- **Thm 1.2 (semicircle):** along any nν,dν→∞ with nν³log²≥K dν⁵, the centered/scaled zero
  empirical measure → Wigner semicircle. Does NOT assert local statistics/edge universality.
- Paper's own disclaimer (line ~1913): "This result controls an asymptotic region and does not
  provide a converse route from partial Jensen hyperbolicity to the Riemann hypothesis; see
  Farmer." → the paper itself knows it is a large-n diagnostic, not an LP/one-way input.

## 1. THE MECHANISM (PROVEN — read from the paper's framed proof, §§2-7,11)

Coordinates: R_j=γ(n+j)/γ(n), q_k=R_{k+1}²/(R_k R_{k+2}) (second-ratio / Turán invariants).
Three nested comparison families (Laguerre → Jacobi → finite-free multiplicative convolution),
each matching one more quotient coordinate (Lemma 2.1: matching q_0..q_{m-2} ⟺ matching R_0..R_m).
- Laguerre family L_j(B,S)=S^j/(B)_j ⟹ tJ is a *confluent hypergeometric* _{1}F_1 / Laguerre pol
  (5): has d simple negative zeros.
- Jacobi J_j(A,B,S)=S^j (A)_j/(A^j (B)_j).
- Finite-free F_j (4): product of two Pochhammer ratios ⟹ by finite-free multiplicative
  convolution of real-rooted polynomials [4, Prop 2.7/2.17] it stays real-rooted.
- Final model matches R_0..R_4 EXACTLY (5-coefficient matching, via the two defect signs).
**Carrier of real-rootedness:** (i) a real-rooted special-function comparison polynomial
(Laguerre/Jacobi/finite-free — Hermite/ultra-spherical asymptotic family), and
(ii) **Prop 2.2 (fifth-order multiplier stability):** if p is real-rooted with simple positive
zeros and you multiply its coefficients by a holomorphic multiplier c with c(0)=…=c(4)=1,
c(d)>0, sup_{Ω_r}|c−1|≤ε<16, then the perturbed polynomial stays hyperbolic (same signs at 0,
critical points, +∞; Newton-interpolation expansion (8)-(9) kills Δ^k c(0) for k=1..4 leaving
ε·Σ_{k≥5}2^{-k}<ε/16<1).
- The controlled distance sup|c−1| comes from an ANALYTIC saddle estimate on γ's integral
  representation: sup|c−1| ≪ d^{5/2}/(n^{3/2}·log(n+2)). The wedge n³log²(n+2)≥K d⁵ is EXACTLY
  "this error is uniformly small". (Root scale r_F ≍ √(nd); 5th-difference of log-multiplier
  O(1/(n⁴ log n)); error (√nd)⁵/(n⁴ log n)=d^{5/2}/(n^{3/2} log n).)

**Net mechanism: a real-rooted comparison polynomial kept hyperbolic under a bounded
holomorphic coefficient-multiplier perturbation, on a joint (n,d) large-n wedge, controlled
analytically.** Same special-function/spectral family as GJT (fixed-d Hermite limit) and GORZ,
sharpened to a JOINT (n,d) statement with a semicircle transfer.

## 2. PART A §2 — is it margin-driven (S1-dead)? NO — genuinely different.

The S1-dead family = pointwise/local coefficient-margin criteria imposed for ALL n:
t_{n+j} ≥ c/(n+j), c>1 (Hutchinson 3/4), or a pointwise q_k ≥ bound, designed to force LP.
Holland's theorem is NOT anywhere in this family (PROVEN from proof structure):
- It is a JOINT (n,d) large-n wedge, not a condition for all n. For fixed small n it covers only
  d ≤ c·n^{3/5}·log^{2/5}; it says nothing about n=0,1,2 (d⁵ ≤ K·0 impossible; KE⩽K·1-3 small).
- No pointwise margin inequality t ≥ c/(n+j) appears. ξ's actual margin t_k·k→2 with deficit
  EXACTLY 2 (campaign PROVEN) is far BELOW Hutchinson's 3/4 (=0.75 vs the required constant
  margin); Holland uses NO margin. The q_k are only MATCHING COORDINATES for the model, not
  imposed bounds.
- The decisive structure is distance-to-a-real-rooted-model (analytic sup-norm over Ω_r) +
  order-5-exact-matching + bounded-multiplier stability. This is a *perturbation/spectral*
  mechanism, not a coefficient-criterion, and not a margin bound. It is a NEW family relative to
  S1 (name it: "real-rooted-comparison + bounded-analytic-multiplier stability", alias
  Hermite/comparison-semicircle family — an extension of GJT/GORZ to joint (n,d)).

## 3. PART A §3 + PART B §1-2 — wedge sharpness on real data

Accessible grid d≤20,n≤200: LITERAL hyperbolicity boundary = 0 for every d (S4 CHECKED
NUMERICALLY; and PROVEN unconditionally by GORZ d≤8 + GORTTW Cor 1.3 d≤9.36e20 all n via
Platt's RH₀). So the TRUE hyperbolic region is all of ℕ² on the grid. Holland's wedge demands
n ≳ d^{5/3} (n_H(d) = (K d⁵/log²)^{1/3} = K^{1/3} d^{5/3}/log^{2/3}(n_H)) — FAR above 0.

Wedge boundary n_H(d) for K=1 (computed):
  d=8: d⁵=32768, n_H≈16.5
  d=10: d⁵=100000, n_H≈21.5
  d=12: d⁵=248832, n_H≈27.5
Correction to the task brief: (248832)^{1/3}≈62.9 is the naive cube root WITHOUT the log²
factor; because n³log²(n+2) has an EXTRA log² ≥ 1 multiplier, the needed n is SMALLER, ≈27
(K=1), not 63. (The "times log² correction" divides, not multiplies, the cube root.)

Empirical regime-transition onset (S4, clean d≤12, CHECKED NUMERICALLY): n₀*(d;1e-2) ≈
7.7·d^0.97, i.e. d=8:58, d=10:69, d=12:79. Literal boundary 0.

**Sharpness gap:** n_H(d)/n₀⁺(d) ∝ K^{1/3} d^{5/3}/(d · log^{2/3}) = K^{1/3} d^{2/3}/log^{2/3} →
diverges as d→∞ at fixed K. Even vs the extreme "boundary = 0", the wedge leaves an uncovered
strip [0, c·d^{5/3}] that is provably all-hyperbolic. **The wedge is FAR from sharp on the real
ξ (CONJECTURED from S4 data, and trivially true vs the literal boundary=0 which is PROVEN on the
grid).** It is a sufficient large-n bound whose boundary law (d^{5/3}) is structurally faster
than the observed hyperbolicity onset (~d^1 or 0).
- **Effective K that would match the wedge to the empirical onset:** toward boundary=0 none
  exists (would need K→0, contradicting K>0 absolute). Toward the transition onset n₀⁺≈7.7 d:
  K = 7.7³·log²(7.7d)/d² → 0 as d→∞ — still no positive constant. ⟹ the wedge cannot be brought
  down to the empirical region by ANY constant; the d^{5/3} vs d^1 growth gap is structural.
- Certification of points INSIDE the wedge (d=8..12, n at K=1 boundary ≈17,22,28): not run as a
  new binary — these are PROVEN hyperbolic unconditionally (GORZ/GORTTW d≤9.36e20 all n), so a
  128/256-bit Aberth re-check is a verification exercise with no new information (S4 refereed
  this already). Machinery validated against the theorem is a formality; the wedge prediction is
  trivially satisfied and confirms nothing beyond the existing proofs.

## 4. PART C — VERDICT

1. **Mechanism family: genuinely DIFFERENT from S1 margin (PROVEN, from the paper's framed
   proof).** It is NOT margin-driven. Name: *real-rooted-comparison + bounded-analytic-multiplier
   stability* (Hermite/comparison-semicircle family, a JOINT (n,d) refinement of GJT/GORZ). The
   S1 closure (no decaying-margin criterion with C>1 forces LP) is untouched — Holland never
   uses a margin condition. As a *new sufficiency family for finite-n hyperbolicity*, it is real
   and new.
2. **Is there ANY path from a finite-degree wedge to all-d hyperbolicity that is not ⟺ RH?
   NO (honest, and the paper itself says it, citing Farmer).** Holland's wedge governs only the
   large-n region n ≳ d^{5/3}. For every fixed n (esp. n=0,1,2) the wedge leaves all
   d > c·n^{3/5} uncovered — an infinite-(d) region. LP of Ξ = all-d all-n hyperbolicity splits
   as (Holland/GJT/GORZ large-n, PROVEN) ∧ (small-n completion, ⟺ RH). **The complement is
   exactly the GJT-completion trap: after the wedge, the leftover small-n part is ⟺ RH.** There
   is no bounded path from Holland's wedge to LP without ⟺ RH. Same diagnostic class as
   GORZ/GORTTW (ledger: Jensen route diagnostic-only).
3. **Wedge not sharp on real ξ (CONJECTURED; sharpness gap ∝ d^{2/3}, and literal boundary=0 is
   PROVEN on the grid).**
4. **Firewall:** zero RH evidence either way. This is a structural/record finding only.

## 5. Honest bottom line
Holland's theorem is the most structurally distinct NEW sufficiency in the 2023-26 sweep — a
genuinely new (non-margin) finite-degree comparison mechanism with a semicircle transfer. But it
is exactly the class the campaign already closed for the one-way need: finite-degree / large-n
Jensen hyperbolicity, whose missing part is ⟺ RH (Farmer diagnostic, GJT completion). It does NOT
revive the one-way search and adds no RH weight. Its value is (a) independent proof that the
accessible hyperbolicity region is covered by a *non-margin* theorem (so the "margin" cohort is
not the whole story — the perturbation/comparison family is open at finite-degree), and (b) a
sharper quantitative boundary (d^{5/3}) that is nonetheless non-sharp on real data. No new RH
lever. Campaign-close on the one-way need stands.

Files touched: /home/vstaln/riemann/research/notes/holland-wedge-probe-2026-08-18.md (this);
.holland-wedge-probe-2026-08-18.progress; ledger line appended.
