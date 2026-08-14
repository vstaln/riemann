# Li criterion — literature / state-of-the-art audit (2026-08-14)

**Agent task:** research-only audit of (1) records for computing Keiper–Li coefficients λ_n,
(2) algorithms + precision requirements, (3) known positivity results, (4) asymptotics and
thresholds, (5) Hankel/moment structure. Every claim is labeled PROVEN / CHECKED NUMERICALLY /
CONJECTURED / INCONCLUSIVE and cited. Primary sources were read directly where available
(arXiv PDFs extracted with pdftotext); the Keiper paper itself is paywalled behind an AMS
Cloudflare wall — its content is cited via the secondary account in Johansson 2013.

**Normalization warning (applies everywhere below):** the literature uses TWO normalizations.
Keiper's coefficients λ_n^K are the series coefficients of log ξ(x/(x−1)) = −log 2 + Σ λ_n^K x^n;
Li's coefficients are λ_n^L = n·λ_n^K (Voros 2022, 2204.01036, explicitly warns "λ_n^L = n λ_n^K").
All formulas below are flagged K/L where the factor n matters. The project's probe computes
Li's λ_n^L (its λ_12 = 3.2633 matches Maślanka's λ_12 = 3.26325532062, CHECKED NUMERICALLY).

---

## 1. Records for computing Keiper–Li coefficients λ_n

| who | year | max n | precision | rigor | source |
|---|---|---|---|---|---|
| Keiper | 1992 | 7000 | n/a (paper paywalled) | heuristic | [J93], via [J13] §4.2 |
| Maślanka | 2004 | ~3300 | 2000 Stieltjes consts at 800 digits; λ_n accuracy falls linearly in n | heuristic (Mathematica) | [M04] |
| Coffey | 2005 | ~100 (tables) | ~7–8 digits shown | heuristic | [C05] App. D |
| Johansson | 2013 | **100000** | ~0.1n accurate bits at index n (working precision 1.1n+50 bits) | **rigorous (Arb ball arithmetic)** | [J13] Table 2 |
| Misguich | 2017+ | 5·10^5 | n/a | heuristic | [V17] (modified Λ_n sequence, NOT λ_n) |
| (post-2013) | 2014–2026 | — | — | — | no paper exceeds Johansson's n=10^5 for λ_n itself (arXiv audit) |

- **Keiper 1992** (J. B. Keiper, "Power series expansions of Riemann's ξ function", Math. Comp.
  58 (1992) 765–773): introduced the coefficients (his λ_n^K), conjectured
  λ_n^K ≈ (1/2)(log n − log(2π) + γ − 1), and "presented numerical evidence for this conjecture
  by computing λ_n up to n = 7000, showing that the approximation error appears to fluctuate
  increasingly close to zero" — REPORTED by Johansson [J13 §4.2] citing Keiper (the paper itself
  is behind an AMS bot-wall; we could not verify the digit count directly). Keiper also computed
  the Stieltjes constants γ_n to n = 150 by "numerical integration and recurrence relations"
  [J13 §4.3]; this is the algorithm behind Mathematica's StieltjesGamma[n] [M04].
- **Maślanka 2004** (K. Maślanka, "Effective method of computing Li's coefficients and their
  properties", arXiv:math/0402168): computed 2000 γ_n at 800 significant digits each and
  "almost 3300" λ_n; observed the trend + tiny-oscillation decomposition (below). Voros reports
  Maślanka's precision loss as ≈ 0.2 decimal place per step n [V17 §1.2].
- **Coffey 2005** (M. W. Coffey, "Toward verification of the Riemann hypothesis: Application of
  the Li criterion", arXiv:math-ph/0505052): theoretical program (verification reduced to sign
  conjectures on the η_k) plus tabulated λ_k (Appendix D, k to ~100). Also gives the
  exponentially-cancelling series λ_n = S1 + S2 + 1 − n(γ + ln π + 2 ln 2)/2.
- **Johansson 2013** (F. Johansson, "Rigorous high-precision computation of the Hurwitz zeta
  function and its derivatives", arXiv:1309.2877; publ. Numer. Algorithms 69 (2015) 253–270):
  **current record for λ_n**: computed λ_0..λ_100000 with proved error bounds; λ_100000^K =
  4.62580782406902231409416038… (plus ~2900 more accurate digits) vs (1/2)(log n − log 2π + γ − 1)
  ≈ 4.626132. Table 2: n=10^5 took 71051 s wall (~19.7 h, 16 threads), 48700 MiB peak RAM.
  "Empirically, we need a working precision of about n bits to determine λ_n" [J13 §4.2].
- **Voros–Misguich variant**: Voros' discretized Keiper–Li sequence Λ_n (explicit closed form,
  §2) was computed to n = 5·10^5 by G. Misguich [V17 abstract]. This is NOT the original λ_n;
  it is a separate RH-sensitive sequence (asymptotically), so it does not extend the λ_n record.
- **No 2014–2026 record**: arXiv full-text search for "Keiper-Li" (all years, sorted by date)
  returns only Voros (2014, 2016, 2017, 2022), Maślanka (2022), Johansson (2013) — no newer
  λ_n computation beyond n=10^5 exists in the public literature as of this audit (INCONCLUSIVE
  for non-arXiv venues, e.g. possible MSc theses; no journal evidence found).
- Stieltjes-constant records (inputs to λ_n): Kreminski 2003 (γ_n to a few thousand digits for
  all n ≤ 10^4, isolated values to γ_50000 at 1000 digits, Newton–Cotes, heuristic) [K03];
  Johansson 2013 (all γ_n ≤ 10^5 at 125050 bits, rigorous; accuracy from 37640 digits at γ_0 to
  ~10860 digits at γ_100000; γ_100000 = 1.991927306312541095658… × 10^83432; 26 h, 80 GiB) [J13 §4.3];
  Johansson–Blagouchine 2019 (complex integration, rigorous, Math. Comp. 88 (2019) 1829–1850) [JB19];
  Tyagi 2022 (arXiv:2212.07956, saddle-point/DE; reaches γ_10^100 to ~1000 digits but
  **non-rigorous** — "results differ from the exact results only on the last digits" [T22];
  cross-checks γ_10^5 against Johansson's value).

## 2. Algorithms

**2.1 Generating function (anchor).** log ξ(1/(1−x)) = log ξ(x/(x−1)) = −log 2 +
Σ_{n≥1} (λ_n^L/n) x^n = −log 2 + Σ_{n≥1} λ_n^K x^n (Keiper [J93]; Li [L97]; B–L [BL99];
used by Johansson [J13 §4.2]). Also λ_n^L = Σ_ρ [1−(1−1/ρ)^n] (Li [L97]) and
λ_n^L = (1/(n−1)!)·[d^n/ds^n(s^{n−1} log ξ(s))]_{s=1} (Li [L97], eq. (2.1) in [M04]).

**2.2 Keiper's own method (as documented in the secondary literature).** Per Johansson [J13 §4.3],
"Keiper provides a method for computing the Stieltjes constants based on numerical integration
and recurrence relations"; Keiper's algorithm is what Mathematica's StieltjesGamma implements
[M04]. The exact a_k/b_k recurrence is NOT restated in the accessible literature (AMS paywalled);
we could not obtain the paper (INCONCLUSIVE on the literal recurrence). The recurrences that ARE
documented in the open literature are 2.3–2.6 below.

**2.3 Johansson's rigorous pipeline (recommended; [J13 §4.2]).** Evaluate
log ξ(s) = log(−ζ(s)) + log Γ(1+s/2) + log(1−s) − (s/2)log π at s = x ∈ ℝ[[x]], then:
1. series of ζ(s) at s = 0 by Euler–Maclaurin (power sums by binary splitting, Bernoulli
   numbers, rigorous remainder bounds);
2. power-series logarithm (log f = ∫ f′/f);
3. series of log Γ(1+s/2) at s = 1 from γ, ζ(2), ζ(3), …;
4. right-compose by x/(x−1) via the binomial (Euler) transform T[f(x)] = f(x/(x−1)) using
   T[f] = B^{−1}[e^x B[f(−x)]] (Borel transform), numerically stable in ball arithmetic,
   cost M(n) + O(n) coefficient operations.
Horner, Brent–Kung, and binary-splitting composition were tested and are slower/less stable [J13].
Implementation is open source in Arb (python-flint exposes the same library on the laptop).
Precision: ~n bits working for λ_n^K; 1.1n+50 bits yields ~0.1n accurate bits; loss ≈ 1 bit
(≈ 0.3 decimal digit) per step [J13 §4.2, V17 §1.2].

**2.4 Maślanka / B–L decomposition (what the phone probe effectively implements).**
λ_n^L = trend + oscillations with
  trend: from π^{−s/2}Γ(1+s/2) — strictly increasing, computable in closed form;
  oscillations: ~λ_n^L = −Σ_{j=1}^n C(n,j) η_{j−1},
where η_k are the Laurent coefficients of −ζ′(s+1)/ζ(s+1) = 1/s − Σ η_k s^k [M04 (2.4)–(3.12)].
η_k are polynomials in the Stieltjes constants via the power-series-exponentiation recurrence
[M04 (3.8)]:  c_0^{(k)} = γ_0^k,  c_m^{(k)} = (1/(m γ_0)) Σ_{i=0}^{m−1} [km − (k+1)i] γ_{m−i} c_i^{(k)},
then η_n = (n+1) Σ_{k=0}^n (−1)^{k+1} c_{n−k}^{(k+1)}/(k+1) [M04 (3.10)].
Equivalent closed form (B–L Theorem 2 / Suzuki eq. (1.9)):
  λ_n^L = −Σ_{j=1}^n C(n,j) η_{j−1} + 1 − (n/2)(γ_0 + log 4π) − (n/2) Σ_{j=2}^n (−1)^{j−1} C(n,j)(1−2^{−j})ζ(j).
The series-log recurrence actually used in tools/li_probe.py: b_m = a_m − (1/m)Σ_{k<m} k b_k a_{m−k}
with a_m = (−1)^{m−1}γ_{m−1}/(m−1)! — equivalent to the above (same ill-conditioning).
Convention: mpmath/Arb stieltjes(n) = γ_n in ζ(s) = 1/(s−1) + Σ (−1)^k γ_k (s−1)^k/k!;
Maślanka's γ_n^M = (−1)^n γ_n/n! [M04]. Number of polynomial terms grows like the partition
function — write-out impractical past n ≈ 30–50, but numeric evaluation is fine [M04 §4].

**2.5 Voros exact sum / integral.** λ_n^L = −n Σ_{j=1}^n (−1)^j C(n+j−1, 2j−1) Z(j) with
Z(j) = Σ_k x_k^{−j}, x_k = ρ_k(1−ρ_k) > 0 (secondary zeta function at integers) [V04 (6)];
Z(j) > 0 termwise but the alternating signs force "cancellations that increase with n" [V04].
Integral representation λ_n^L = (−1)^n (n i/π) ∮_C [Γ(σ+n)Γ(σ−n)/Γ(2σ+1)] Z(σ) dσ [V04 (7)].
Caveat: needs Z(j) for j ≤ n, which requires its own computation (zeros or recurrences).

**2.6 Voros closed-form variant Λ_n (cheapest, RH-sensitive only asymptotically).**
Λ_n = (−1)^n Σ_{m=1}^n (−1)^m A_{nm} log 2ξ(2m), A_{nm} explicit 2^{−2n}-scaled partial-fraction
coefficients; log 2ξ(2m) from ζ(2m) = Bernoulli values [V17 (36)–(38)]. Precision loss ≈ 2× that
of λ_n (~0.6 dp/step) [V17 §4]; computed to n = 5·10^5 by Misguich [V17]. NOT an iff-positivity
certificate (RH-sensitive in the asymptotic tail only).

**2.7 Stieltjes constants to high precision (for route 2.4).** Records/methods in §1;
ill-conditioning: "we need about n + p bits of precision to determine γ_n with p bits of
accuracy" [J13 §4.3]; rigorous: Arb acb_dirichlet_stieltjes / [J13] / [JB19]; asymptotic sign
formula (Knessl–Coffey) correct except n = 137 (verified the sole exception for n ≤ 10^5 by
Johansson) [J13 §4.3, KC05]; improved rigorous bounds: Pauli–Saidak 2023 (arXiv:2301.11209).

**2.8 Precision requirement (answers "digits ≈ c·n").** Working precision ≈ n bits for λ_n^K
(≈ 0.1n accurate bits at 1.1n+50 working bits) [J13]; loss ≈ 1 bit per step (0.2–0.3 dp/step)
[V17 §1.2]. For Li's λ_n^L (values ~log₂n bits larger): intermediate precision ≈ n + log₂n + p
bits for p accurate bits, i.e. **decimal digits ≈ 0.30 n + log₁₀n + 0.30 p**. So n = 1000,
p = 100 digits ⟹ ~335 decimal digits intermediate; n = 10⁴ ⟹ ~3.0×10³ digits; n = 10⁵ ⟹
~3.0×10⁴ digits (Johansson's regime; his 1.1n+50 bits is a safety margin). The phone plan
(γₖ, k ≤ 1000, at 2500–3000 dps, then λₙ to n ≈ 1000) is comfortably within these
requirements (CHECKED against the literature rule, no new computation performed).

## 3. Known positivity results

- **PROVEN (Li 1997):** RH ⟺ λ_n^L ≥ 0 for all n ≥ 1. X.-J. Li, "The positivity of a sequence
  of numbers and the Riemann hypothesis", J. Number Theory 65 (1997) 325–333 [L97].
- **PROVEN (Bombieri–Lagarias 1999):** generalized criterion; 2λ_n = W(g_n ∗ x^{−1}g_n(x^{−1}))
  where W is the Weil distribution (explicit formula), g_n explicit in (1.4) [BL99, via S23 (1.3)];
  RH ⟺ Weil positivity W(f) ≥ 0 for all test f (Weil's criterion) [BL99].
- **PROVEN (given RH):** λ_n^L = Σ_pairs 4 sin²(nθ_ρ/2) ≥ 0 term-by-term, θ_ρ = arg(1−1/ρ)
  (|1−1/ρ| = 1 on the critical line) [BL99; V22 §2.2.2]; equivalently the Chebyshev form
  λ_n^L = Σ_ρ (1 − T_n(x_ρ)) with x_ρ = 1 − 1/(2ρ(1−ρ)) ∈ (0,1) under RH (Xiao 2020,
  arXiv:2006.13103).
- **PROVEN (unconditional, small n):** λ_1 = 1 + γ/2 − (1/2)log(4π) = 0.0230957089661… > 0
  (B–L Remark, p. 282, [BL99]; confirmed by our probe to 20 digits — CHECKED NUMERICALLY);
  λ_1, λ_2 > 0 for ζ unconditionally via probability-law/cumulant arguments
  (Biane–Pitman–Yor 2001, BAMS 38, 435–465 [BPY01]; restated with proof for
  Q, Q(√−1), Q(√−2) by Plumpton 2024, arXiv:2411.08863).
- **PROVEN (unconditional, generalized family):** Sekatskii's b-shifted generalized Li
  derivatives (1/(n−1)!)·[d^n/dz^n((z+b)^{n−1} log ξ(z))]_{z=1+b} are > 0 for all n ≤ m whenever
  b ≥ c(m) (Theorem 5, arXiv:1404.7276) — positivity for a modified family, NOT for the original
  λ_n. Generalized Li criterion (parameter a < 1/2) ⟺ RH: Sekatskii (arXiv:1304.7895;
  1404.7276), Mazhouda (arXiv:1405.7354), Omar–Mazhouda (J. Number Theory 125 (2007) 50–58).
- **Numerical verification records (all CHECKED NUMERICALLY, none of which proves RH):**
  Keiper n = 7000 [J93 via J13]; Maślanka n ≈ 3300 [M04]; Coffey n ≈ 100 [C05];
  **Johansson n = 100000, rigorous intervals** [J13]; Misguich n = 5·10^5 (Λ_n variant) [V17];
  Dirichlet L-functions: Omar–Ouni–Mazhouda 2015 (arXiv:1507.03431).
- **No unconditional λ_n^L ≥ 0 for any n ≥ 3** — that would be a step toward RH; the only
  unconditional results are λ_1, λ_2 and the generalized families above (INCONCLUSIVE if any
  hidden paper exists, but nothing found in arXiv/Crossref audits).

## 4. Asymptotics & thresholds

- **Keiper's conjecture (16)** [J93, as reported in J13]: λ_n^K ≈ (1/2)(log n − log(2π) + γ − 1),
  i.e. λ_n^L ≈ (n/2)(log n − log(2π) + γ − 1). Verified to n = 10^5: λ_100000^K =
  4.62580782406902231409416038… vs 4.626132 from (16); the error n·(λ_n^K − (16)) oscillates
  with bounded amplitude (Johansson Fig. 1) — CHECKED NUMERICALLY.
- **PROVEN (saddle-point analysis, Voros 2004 [V04]):** RH-true:
  λ_n^L ~ (n/2)(log n − log 2π − 1 + γ) as n → ∞; RH-false:
  λ_n^L ~ Σ_{arg τ_k > 0} [(τ_k + i/2)/(τ_k − i/2)]^n + c.c. — exponentially growing, phase-
  oscillating terms. Constant +7/4 arises from the pole at σ = 0 (next-order correction) [V04 (12)].
  The exact constant (γ − 1 − log 2π)/2 was computed by Voros [V04; M04 (2.7)].
- **Remainders (PROVEN):** λ_n^L = (n/2)(log n + γ − 1 − log 2π) + O(√n log n)
  (Lagarias 2007, "Li coefficients for automorphic L-functions", Ann. Inst. Fourier (Grenoble)
  57 (2007) 1689–1740); strengthened to λ_n^L/n − (1/2)(log n + γ − 1 − log 2π) = y_n with
  {y_n} ∈ ℓ² (Arias de Reyna 2011, "Asymptotics of Keiper-Li coefficients", Funct. Approx.
  Comment. Math. 45 (2011) 7–21) — per [V17 §1.2].
- **If RH fails (PROVEN direction + quantified thresholds):**
  - λ_n^L < 0 must occur for infinitely many/arbitrarily large n in the asymptotic regime
    (contrapositive of Li's criterion + (18) of [V22]) — PROVEN.
  - A violating zero ρ′ = 1/2 + t + iT (t > 0, |T| ≥ T_0) imprints a term z_{ρ′}^{−n},
    z = 1 − 1/ρ, that competes with the RH-true trend only for **n ≳ T²/|t|** ([V22] (23));
    the inequality is a strict necessity by the uncertainty principle ([V22] (17)).
  - Best case (t → 1/2, T = T_0 ≈ 2.4×10^12, the current verification height): **n ≳ 2T_0² ≈ 10^25**
    is needed for λ_n to possibly sense RH violations [V22 §2.3, V17 §1]. "values n ≳ 10^25 needed
    for new tests of RH appear way out of reach" [V22].
  - Zero-free-height ⟹ positivity: Re ρ = 1/2 for all |Im ρ| ≤ T_0 ⟹ λ_n > 0 for n < T_0²
    [V22 §2.2.2, citing [24]]. Oesterlé's heuristic (reported in Biane–Pitman–Yor 2001, p. 441,
    and in [M04]): if the first n zeros lie on the line, Li positivity should hold for about the
    first n² coefficients — same order of magnitude (T² up to logs) — CONJECTURED/heuristic.
  - Quantitative conversion of interval sign data into zero-free regions: Palojärvi 2018
    (arXiv:1807.01506): explicit N_1, N_2 such that Re(τ-Li coefficients) ≥ 0 for all n in
    [N_1, N_2] ⟹ a zero-free region of explicit shape; negative values in an interval ⟹ a zero
    in a corresponding region — PROVEN.
- **Entire-function lens:** Maślanka 2022 (arXiv:2211.08993) constructs an even entire λ(s) with
  λ(n) = λ_n^L; its zeros form complex quadruplets if RH is true and real doublets if RH is false
  (3500+ zeros computed at 14 digits) — CHECKED NUMERICALLY / CONJECTURED structure.

## 5. Hankel / moment structure

**Correction to method-frontier-synthesis.md:** the chain "λ_n ≥ 0 ⟺ {λ_n} moment sequence ⟺
Hankel matrix PSD" is NOT a theorem. Positivity of all entries of a sequence does not imply
moment-ness (e.g. 1 + cos n), and no proof exists for the specific sequence λ_n. The honest
state of the art:

- **PROVEN (classical, general theory):** a real sequence {a_n} is a (Hamburger) moment
  sequence iff every principal minor of the Hankel matrix (a_{i+j}) is ≥ 0. Applied to λ_n, the
  *sufficiency* "Hankel-PSD ⟹ λ_n ≥ 0" is trivial (diagonal entries), but the *necessity*
  "λ_n ≥ 0 ∀n ⟹ Hankel-PSD" is an open question (CONJECTURED, no literature found).
- **PROVEN: λ_n as values of the Weil quadratic form.** 2λ_n^L = W(g_n ∗ x^{−1}g_n(x^{−1}))
  (Bombieri–Lagarias 1999 [BL99], reproduced in Suzuki 2023 (1.3) [S23]). RH ⟺ W ≥ 0 (Weil's
  criterion) [BL99]. So λ_n ≥ 0 is Li's criterion, and under Weil positivity it is automatic —
  but the implication runs through RH, not directly.
- **PROVEN (given RH): explicit positive trigonometric representations** —
  λ_n^L = Σ_pairs 4sin²(nθ_ρ/2) [BL99, V22 (16)]; Chebyshev form λ_n^L = Σ(1 − T_n(x_ρ)),
  x_ρ ∈ (0,1) [X20]. These are positive *sums*, not moment (power) representations.
- **PROVEN: norm representation equivalent to RH (Suzuki 2023, arXiv:2301.05779).**
  RH ⟺ λ_n^L = (1/2π)||G_n||²_{L²(ℝ)} for all n, where G_n are explicit functions built from
  the η_k and (1−2^{−k})ζ(k+1). Under RH, G_n ∈ a model space K(Θ) generated by
  Θ(z) = E(z̄)/E(z) with E(z) = ξ(1/2−iz) + ξ′(1/2−iz), i.e. Lagarias' de Branges space H(E)
  (whose multiplication operator has the ξ-zeros as eigenvalues) [S23]. This is a genuine
  Hilbert-space positivity ("norm of a concrete function") representation, of Weil type —
  the closest published analogue of the program's "law"/moment-positivity language.
- **PROVEN (unconditional):** E(Y^s) = 2ξ(s) for a positive random variable Y (Biane–Pitman–Yor
  2001 [BPY01]); consequently λ_n are "modified cumulants" of log Y (λ_1 = κ_1 − log√|D|,
  λ_2 = 2λ_1 + κ_2 with κ_2 = Var ≥ 0 [P24]) — the source of the unconditional λ_1, λ_2 > 0.
- **Voros 2004 (6):** λ_n^L = −n Σ (−1)^j C(n+j−1, 2j−1) Z(j) with Z(j) = Σ x_k^{−j} > 0 —
  positive *ingredients* with alternating signs (not a moment form) [V04].
- **No published "λ_n = ∫ x^n dμ" moment theorem** exists for the original λ_n (arXiv +
  Crossref audit, 2013–2026). The moment/Hankel-PSD program is a genuinely open research
  direction (CONJECTURED), which is precisely why it is interesting for this project.

---

## Implications for our deep-n probe

1. **What is genuinely new vs re-verification.** Computing λ_n to n ≈ 10^3–10^4 at ~3×10^3 dps
   is NOT a record — Johansson (2013) rigorously reached n = 10^5 with ~10^4 digits on similar
   hardware, and our scale sits ~2 orders below it. The new content of our probe is (a) an
   independent, interval-arithmetic re-verification of positivity with our own toolchain
   (valuable as a cross-check, not as a record), and (b) the structural diagnostics nobody has
   published: Hankel inertia of (λ_{i+j}), moment-representation searches, and generalized-
   parameter (a-shift / expansion point Re x_0 > 1) conditioning experiments (Voros [V22 §3]
   notes expanding at Re x_0 > 1 improves convergence — numerically unexplored territory for
   positivity hunting). The asymptotic/positivity facts (λ_n ~ (n/2)log n; λ_1, λ_2 > 0;
   finite-n positivity is only heuristic evidence — the literature's threshold n ≳ 10^25 for
   sensing RH violations makes any finite-n λ-probe mathematically inconclusive for RH) must be
   reported honestly alongside the numerics.
2. **Which algorithm to implement.** Recommend Johansson's pipeline (§2.3: Euler–Maclaurin ζ-
   series at 0 with rigorous bounds + series log + Borel-transform composition) using Arb via
   python-flint on the laptop — it is the only published method with proved error bounds at
   scale, and the reference implementation is open source. Use the phone's current mpmath
   route (B–L decomposition / series-log, §2.4) with 2500–3000 dps as the independent
   cross-check at n ≤ 1000 (literature precision rule says ~430 dps suffices there). Target:
   certified positivity λ_1..λ_1000 (stretch: 10^4) + Hankel inertia with ball arithmetic.
   A λ_n record attempt (n = 10^5, rigorous) would need ~1.1×10^5 bits working precision,
   ~20 h on 16 threads and ~50 GiB RAM — feasible only on the laptop, and of heuristic value
   only; not recommended as the primary line.
3. **Verdict on the certificate class.** Li's criterion remains the right door (no 0.6818
   ceiling, exact parallelizability, RH-equivalent), but the finite-n positivity numerics are
   evidence, not proof; the mathematically load-bearing pieces are the structural identities
   (§5): B–L Weil-form evaluations, Suzuki's L²-norm criterion, and the (open) moment/Hankel
   question — that is where a genuinely new lemma could live.

---

## References

- [J93] J. B. Keiper, Power series expansions of Riemann's ξ function, Math. Comp. 58 (1992) 765–773. (Paywalled; details via [J13].)
- [L97] X.-J. Li, The positivity of a sequence of numbers and the Riemann hypothesis, J. Number Theory 65 (1997) 325–333.
- [BL99] E. Bombieri, J. C. Lagarias, Complements to Li's criterion for the Riemann hypothesis, J. Number Theory 77 (1999) 274–287.
- [BPY01] P. Biane, J. Pitman, M. Yor, Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions, Bull. AMS 38 (2001) 435–465 (arXiv:math/9912170).
- [M04] K. Maślanka, Effective method of computing Li's coefficients and their properties, arXiv:math/0402168.
- [V04] A. Voros, A sharpening of Li's criterion for the Riemann Hypothesis, arXiv:math/0404213.
- [C05] M. W. Coffey, Toward verification of the Riemann hypothesis: Application of the Li criterion, arXiv:math-ph/0505052.
- [K03] R. Kreminski, Newton–Cotes integration for approximating Stieltjes (generalized Euler) constants, Math. Comp. 72 (2003) 1379–1397.
- [KC05] C. Knessl, M. W. Coffey, An effective asymptotic formula for the Stieltjes constants, Math. Comp. 74 (2005) 1383–1397 (sign rule also in [J13 §4.3]).
- [J13] F. Johansson, Rigorous high-precision computation of the Hurwitz zeta function and its derivatives, arXiv:1309.2877; Numer. Algorithms 69 (2015) 253–270.
- [JB19] F. Johansson, I. Blagouchine, Computing Stieltjes constants using complex integration, Math. Comp. 88 (2019) 1829–1850.
- [X20] H. Xiao, Recurrence relations of Li coefficients, arXiv:2006.13103.
- [P24] G. Plumpton, Probability laws concerning zeta integrals, arXiv:2411.08863.
- [V17] A. Voros, Discretized Keiper/Li approach to the Riemann Hypothesis, arXiv:1703.02844.
- [V22] A. Voros, From asymptotic to closed forms for the Keiper/Li approach to the Riemann Hypothesis, arXiv:2204.01036.
- [S23] M. Suzuki, Li coefficients as norms of functions in a model space, arXiv:2301.05779.
- [T22] S. Tyagi, High precision computation and a new asymptotic formula for the generalized Stieltjes constants, arXiv:2212.07956.
- [PS23] S. Pauli, F. Saidak, A bound for Stieltjes constants, arXiv:2301.11209.
- [Sek14] S. K. Sekatskii, First applications of generalized Li's criterion…, arXiv:1404.7276 (and arXiv:1304.7895).
- [P18] N. Palojärvi, Explicit zero-free regions and a τ-Li-type criterion, arXiv:1807.01506.
- [OOM15] S. Omar, R. Ouni, K. Mazhouda, On the zeros of Dirichlet L-functions, arXiv:1507.03431.
- [M22] K. Maślanka, Analytic extension of Keiper-Li coefficients, arXiv:2211.08993.
- [L07] J. C. Lagarias, Li coefficients for automorphic L-functions, Ann. Inst. Fourier (Grenoble) 57 (2007) 1689–1740.
- [AR11] J. Arias de Reyna, Asymptotics of Keiper-Li coefficients, Funct. Approx. Comment. Math. 45 (2011) 7–21.
