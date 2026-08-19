# agy wave-24 batch — adjudication with probes RUN (2026-08-19)

**Source:** fresh agy one-shot (`agy --print`, prompt `/tmp/agy-wave24-prompt.txt`, output
`/tmp/agy-wave24-output.txt`) on the corrected frontier (r′ T=6000 resolved, δ(N) flat law,
μ* Direction-2 dead, ξ-jet lane, Weil new families, one-way discriminants lane #5).
Four candidates produced. **Result: NO survivor; probes settle 2 of 4.**

## Candidate-by-candidate

1. **C1 — normalized curvature ratio at zeros** `Q_n = Re[ζ″(1/2+iγ_n)/(L·ζ′(1/2+iγ_n))]`,
   claim all Q_n ≥ 1−√r∞ > 0. **INCONCLUSIVE-AS-SPECIFIED (probe broken).** The candidate's
   own cheapest probe (`mp.zeta(s,2)`, the 2nd derivative at γ≈14..35) is catastrophically
   unstable: returns Q ∈ ±10²⁹ with spurious sign flips, because Euler–Maclaurin 2nd
   derivatives of ζ at these heights are not reliable at dps=30. No clean signal can be
   read; the lever as stated is not implementable as a discriminant. Do not re-propose
   without a certified derivative method.
2. **C2 — 4th-order Turán/jet determinant** `Φ(t) = L₁J₂ − (1/12)(E′E″−EE′″)² > 0`.
   **STRUCTURALLY DEAD.** Lives in lane #3 (ξ-jet positive certificate), which the campaign
   has **PROVEN** closed: rung-2 kill (κ₁^(2)=4.57 ≫ κ₁^(1)=1.14, certificate vacuous) and
   G²/H Cauchy fatality (even full Gonek+Ng gives zero asymptotic proportion). Also a higher
   sibling of wave-23 agy-L3 (same Turán family), already REFUTED numerically. Do not fund.
3. **C3 — Báez–Duarte energy center-of-mass** `V(N) = (1/d_N²)·Σ_{k≤N} k·a_k*²`,
   claim V(N)/(N·log N) ≤ C with **C ≈ 0.182 flat**. **REFUTED — CHECKED NUMERICALLY.**
   Probed on the certified k=1..N basis (my a* reproduces wave8c d_N exactly:
   0.1510/0.1268/0.1192 at N=10/20/30, so the coefficients are right):
   **V/(N·log N) = 19.2 → 25.8 → 30.5 (N=10/20/30)** — a factor ~150 above the claimed 0.182
   and *rising*, not flat. C3's quantitative claim is false as stated. (Whether some other
   weighted coefficient-energy separates RH from a planted-zero world is not settled by this;
   but this specific object/constant is dead.)
4. **C4 — Mellin–Möbius Hankel singularity radius** `R(K)=[det H_K/det H_{K−1}]^(−1/2K)`,
   claim R(K) > 1.45 → r_c = 2−sup Re ρ = 1.5. **RESTATEMENT (dead).** The radius of
   convergence of 1/ζ at s=2 is exactly 2 − (distance to nearest numerator singularity),
   i.e. 2 − sup Re(1/ζ pole) = 2 − sup Re(ζ zero). "r_c = 3/2 iff RH" is the pole-location
   statement (RH restated), the closed prime-zeta/pole-interrogation family. The Hankel
   estimator is just a numerical radius-of-convergence estimator; it can't separate worlds by
   computation. Do not fund.

## Net

- All 4 candidates dead: C4 restatement, C2 structural, C3 numerically REFUTED, C1 probe-broken.
- Consistent with the established pattern: agy batches produce candidates but no surviving
  one-way RH lever. The two "new" objects (C1, C3) failed on their own proposed probes.
- **RH-false controls** (planted-zero Beurling / DH) were demanded by the task brief for every
  candidate but were not reached because each candidate died at statement or probe level
  before a control run was meaningful.
- **Firewall:** nothing RH-implying survives; exploration continues.

## Files
- prompt: /tmp/agy-wave24-prompt.txt; output: /tmp/agy-wave24-output.txt; probe: /tmp/w24_probe.py
