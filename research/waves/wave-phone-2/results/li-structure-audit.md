# Li criterion — structural audit (2026-08-14)

**Continuation:** completes the partial structure analysis of a previous agent run
(items 1–3 below, all verified — see §V). Reads: `li-literature-audit.md` (primary
context, cited as [AUDIT]), `li-probe.md`, `method-frontier-synthesis.md`,
`equivalent-forms-survey.md`, `li_criterion_proof.md`. Primary sources read directly:
Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I",
Rend. Lincei 11 (2000) 183–233 [B00]; Suzuki, "Li coefficients as norms of functions
in a model space", arXiv:2301.05779 [S23]; Griffin–Ono–Rolen–Zagier, arXiv:1902.07321
[GORZ19]; Griffin–Ono–Rolen–Thorner–Tripp–Wagner, arXiv:1910.01227 [GORTTW20];
Holland, "A new hyperbolicity wedge…", arXiv:2608.08682 [H26]; O'Sullivan,
arXiv:2007.13582 [O20]; Xiao, arXiv:2006.13103 [X20]; Lagarias, "Li coefficients for
automorphic L-functions" [L99].
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.
Every number below is produced by a saved script (`li-structure-verify-weil.py`,
`li-structure-verify-jensen.py`, `li-structure-hankel.log` (wave-phone-2/results/)) or cited to a source.
No file other than this memo and the ledger was modified.

---

## 0. The partial analysis (from the interrupted run) — verified

The previous run's three claims are all CONFIRMED, two with new numerical checks:

1. **λ_n = Σ_γ 2(1 − cos nθ_γ), θ_γ = π − 2 arctan(2γ)** — PROVEN (algebra; each
   conjugate zero pair {ρ, ρ̄}, ρ = 1/2+iγ, contributes 2 − (1−1/ρ)^n − (1−1/ρ̄)^n =
   2 − 2Re(1−1/ρ)^n = 2(1−cos nθ_γ) = 4sin²(nθ_γ/2) ≥ 0 under RH). CHECKED
   NUMERICALLY: θ_γ = π − 2 arctan(2γ) matches arg(1−1/ρ) to 1e-61 (first 100 zeros);
   the zero-sum Σ_γ 2(1−cos nθ_γ) over the first N zeros converges to the probe λ_n
   from below at the predicted Σ1/γ² tail rate (n=1: 0.022553 at N=1500 vs probe
   0.02309571, tail bound ≤ 3.2e-4; §V).
2. **{c_n = Σ_γ cos(nθ_γ)} is Toeplitz-positive-definite under RH; {2−2cos(nθ)} is
   NOT** — PROVEN with the standard caveat: the c_n individually diverge (Σ_γ 1 = ∞),
   so the correct statement is that the quadratic form Σ_{j,k} a_j ā_k Σ_γ e^{i(j−k)θ_γ}
   = Σ_γ |Σ_j a_j e^{ijθ_γ}|² ≥ 0 is positive term-by-term (i.e. the measure
   Σ_γ δ_{θ_γ} on the circle is positive and {c_n} are its regularized Fourier
   coefficients — a THEOREM under RH, Bochner–Herglotz). CHECKED NUMERICALLY:
   the per-zero form equals |Σa_j e^{ijθ_γ}|² to 12 digits (§V). And det[[2−2cos0,
   2−2cosθ],[2−2cosθ, 2−2cos0]] = −(2−2cosθ)² < 0 for θ ∉ 2πℤ — CHECKED
   NUMERICALLY (−0.8453 at θ=1) — so {2−2cos(nθ)} is not of positive type, consistent
   with λ_n = 2(c_0 − c_n) being a **renormalized Toeplitz difference**, not a moment
   (Hankel) sequence.
3. **"{λ_n} Hankel-PSD ⟺ λ_n ≥ 0" is FALSE** — endorsed and sharpened below (§VI.1);
   the correction in `method-frontier-synthesis.md` (2026-08-14) is correct.

---

## A. The Bombieri–Lagarias Weil form

**The form (PROVEN, [B00] §3, [S23] (1.3)–(1.4), [BL99]).**
2λ_n = W(g_n ∗ x⁻¹g_n(x⁻¹)) with multiplicative convolution on ℝ_{>0} and
W(f) = Σ_ρ ∫₀^∞ f(x) x^{ρ−1} dx (ρ over all nontrivial zeros, the pairing of the
Guinand–Weil explicit formula). The test function (Bombieri's explicit form, [B00] p.192;
[S23] (1.4)) is

    g_n(x) = Σ_{j=1}^n C(n,j) (log x)^{j−1}/(j−1)!  for 0 < x < 1,
           = n/2                                   for x = 1,
           = 0                                     for x > 1.

**Mellin transform (PROVEN, and verified numerically):** ĝ_n(s) = ∫₀^∞ g_n(x)x^{s−1}dx
= Σ_{j=1}^n C(n,j)(−1)^{j−1} s^{−j} = **1 − (1 − 1/s)^n** — the same function that
appears in Li's definition. CHECKED NUMERICALLY by direct Mellin integration for
n = 1,4,8 at two complex s: agreement to 1e-34…1e-49 (§V).

**The "square-root" algebra (PROVEN, [B00] p.192):** (1−1/s)(1−1/(1−s)) = 1, hence
[1−(1−1/s)^n]·[1−(1−1/(1−s))^n] = [1−(1−1/s)^n] + [1−(1−1/(1−s))^n], so the composed
function f_n := g_n ∗ x⁻¹g_n(x⁻¹) has Mellin transform ĥ_n(s) = ĝ_n(s)ĝ_n(1−s) and
W(f_n) = Σ_ρ ĝ_n(ρ)ĝ_n(1−ρ) = 2λ_n. Under RH, 1−ρ = ρ̄ so each pair contributes
|ĝ_n(ρ)|² = |1−(1−1/ρ)^n|² ≥ 0 — the B–L form becomes a **sum of squares**
λ_n = Σ_{upper half} |1−(1−1/ρ_γ)^n|², the genuine square structure behind the sin²
form. CHECKED NUMERICALLY: the factorization is exact to 1e-60; the pairing
(1/2)Σ_ρ ĝ_n(ρ)ĝ_n(1−ρ) over the first N zeros converges to the probe λ_n from below
at the tail rate and equals the zero-sum partial sum at every N (as the square
identity predicts under RH), §V.

**Where f_n sits relative to the known Weil-positivity classes (the honest core of §A).**
The classes on which W ≥ 0 is known UNCONDITIONALLY are bandlimited classes:
- Yoshida 1992 / Bombieri [B00] §12: W is positive definite for test functions with
  Fourier support in [−t, t], verified for t = (log 2)/2 — i.e. bandwidth ≤ log 2 ≈ 0.69
  in the additive coordinate (PROVEN). This is the same "bandwidth-1" family the
  program's two-moment/Levinson machinery lives in (ceiling 0.6818).
- Bombieri's Theorem 1 [B00]: RH ⟺ Σ_ρ g̃(ρ)g̃(1−ρ) > 0 for **all** g ∈ C₀^∞(0,∞)
  (PROVEN — but this is the full class, i.e. it *is* RH, not a partial result).

The Li test functions lie strictly OUTSIDE both:
(i) **g_n is not smooth with compact support** — Bombieri: "Since g_n is not a smooth
function with compact support, we cannot apply the Explicit Formula directly" ([B00]
p.192); one needs the truncation g_{n,ε} and a limit ε→0 (eq. (3.4)). g_n is unbounded
at 0 (log-polynomial), discontinuous at x = 1 (jump n → n/2 → 0).
(ii) **The composed f_n has a full-spectrum Mellin transform**: on the critical line
|ĥ_n(1/2+it)| = |ĝ_n(1/2+it)ĝ_n(1/2−it)| ~ n²/t² as t→∞ — CHECKED NUMERICALLY
(n²/t² decay to 5 significant digits at t = 500, §V). No bandlimited-positivity theorem
applies; f_n is not compactly supported in any variable.
**Conclusion (honest statement of why Li's criterion is open):** the countable explicit
family {f_n} sits strictly outside every class where Weil positivity W ≥ 0 is known
unconditionally; W(f_n) ≥ 0 for all n is exactly λ_n ≥ 0 for all n, i.e. exactly RH.
There is no known theorem covering full-spectrum test functions whose Mellin transforms
are the rational functions [1−(1−1/s)^n][1−(1−1/(1−s))^n].

---

## B. Suzuki's L²-norm criterion (arXiv:2301.05779) [S23]

**Setup (PROVEN, unconditional).** With η_k the Laurent coefficients
−ζ′/ζ(s+1) = 1/s − Σ_{k≥0} η_k s^k and E(z) = ξ(1/2−iz) + ξ′(1/2−iz), define H_n(s)
([S23] (1.6)); Prop. 2.1 gives the clean form H_n(s) = ξ(s)·M_n(s)/(ξ(s)+ξ′(s)) with
M_n(s) = Σ_ρ m_ρ [1−(1−1/ρ)^n]/(s−ρ) (ρ with multiplicity m_ρ). Then
G_n(z) := H_n(1/2 − iz) is bounded, real-analytic and in L²(ℝ) unconditionally
(Prop. 2.2; H_n ≪ |s|⁻¹ log|s|).

**The criterion (PROVEN, [S23] Thm 1.1).** RH ⟺ λ_n = (1/2π)‖G_n‖²_{L²(ℝ)} for all
n ≥ 1. "Equality for all n ⟹ RH" is trivial (then λ_n ≥ 0, Li). The nontrivial
direction (RH ⟹ equality) runs through the model space K(Θ) for the meromorphic inner
function Θ(z) = E(z̄)/E(z): under RH, E lies in the Hermite–Biehler class, Θ is inner,
and the {F_γ} of (3.4) are an orthonormal basis of K(Θ) (Prop. 3.2); G_n = T(g_n) with
basis coefficients √(πm_γ)·[1−(1−1/ρ)^n], giving ‖G_n‖² = π Σ_γ m_γ |1−(1−1/ρ_γ)^n|²
= 2πλ_n. K(Θ) ≅ de Branges space H(E) (Lagarias), whose multiplication operator has
the ξ-zeros as eigenvalues.

**What this gives us.**
- A genuinely Hilbert-space formulation: λ_n ≥ 0 is the norm of a concrete function.
- A second, independent finite witness: the equality at index n is a finite computation
  of two real numbers (λ_n from Stieltjes constants; ‖G_n‖² by direct integration).
  Suzuki records the referee's observation: "it could be verified by a finite
  computation if the equality does not hold" — i.e. this is a *disproof* family.
- The hard direction is open: Suzuki (§4.1) — the integrals
  ∫_ℝ F_{μ₁}F_{μ₂}dz = ∫_{Re s=1/2} ξ(s)ξ(1−s)/[(s−ρ₁)(ξ+ξ′)(1−s−ρ₂)(ξ−ξ′)] ds
  are intractable without RH ("new and fundamental ideas are needed"); what happens to
  ‖G_n‖² when RH fails is not understood (only Bombieri's negative-eigenvalue theory
  for the Weil functional gives hints, [B00] §8–11).
- **Numerical status (CHECKED NUMERICALLY, shape-level):** the direct integral
  (1/2π)∫_{−100}^{100}|G_n(t)|²dt with 200 zeros gives ≈ 0.34·λ_n for n = 1 and n = 2
  (same fraction both n) — consistent with the identity modulo a heavy 1/(t log²t) tail
  that carries ≈ 2/3 of the L² mass; a high-precision verification needs R ≳ 10⁴–10⁶
  or a Parseval/explicit-formula evaluation (deferred). The B–L pairing (§A) is the
  high-precision channel instead.

**What would have to be proven.** Equality λ_n = (1/2π)‖G_n‖² for all n (⟺ RH), or any
unconditional two-sided estimate on ‖G_n‖² − 2πλ_n. Suzuki: "new and fundamental ideas
are needed".

---

## C. sin² / Chebyshev representations

- **sin² form (PROVEN, [BL99], [V22] (16); [AUDIT] §5):** under RH,
  λ_n = Σ_pairs 4sin²(nθ_γ/2), θ_γ = π − 2 arctan(2γ) (§0.1, verified to 1e-61). This
  is the kernel form λ_n = ∫ 4sin²(nθ/2) dν(θ) with ν = Σ_γ δ_{θ_γ} ≥ 0 under RH.
  The kernels 4sin²(nθ/2) = 2(1−cos nθ) are the squares of the Fejér kernel's building
  blocks (F_N(θ) = sin²(Nθ/2)/(N sin²(θ/2))); λ_n is a "cumulative Fejér-type" sum.
- **Chebyshev form (PROVEN under RH, [X20]):** λ_n = Σ_ρ (1 − T_n(x_ρ)) with
  x_ρ = 1 − 1/(2ρ(1−ρ)) ∈ (0,1). CHECKED NUMERICALLY: x_ρ = cos θ_ρ **exactly** and
  1 − T_n(x_ρ) = 1 − cos(nθ_ρ) to 1e-60 (§V) — the two representations are the same.
- **Total-positivity structure (CONJECTURED as a program direction; folklore facts):**
  the node system {T_n} is a classical total-positivity (Chebyshev/Markov) system, and
  the kernels 1−T_n(x) are strictly positive on x ∈ (−1,1); so under RH λ_n is a
  positive linear functional of the positive measure ν on the Chebyshev nodes.
  BUT this is NOT a moment (power-moment) representation: the measure lives on the
  interval with Chebyshev moments, and the sequence {λ_n} is a Toeplitz-type object
  (renormalized cosine differences, §0.2), not a Hamburger moment sequence (verified
  negative Hankel minors, §V). Total positivity of the *kernel family* does not make
  {λ_n} a moment sequence; it is the *node system* that carries the TP structure.
- **No published moment theorem for {λ_n}** ([AUDIT] §5 — arXiv/Crossref audit 2013–26):
  INCONCLUSIVE but well-swept; the search space is genuinely open.


---

## D. Finite certificates — per route

Threshold facts that apply to ALL routes (PROVEN, [V22] (17),(23), [AUDIT] §4): a
hypothetical off-line zero rho_0 at height T with |1/2-Re rho_0| = t imprints a term
(1+delta_0)^n, delta_0 = (1-2Re rho_0)/|rho_0|^2 ~ 2t/T^2, into lambda_n (via
[1-(1-1/rho_0)^n]); it can compete with the RH-true background n*log n only for
**n >= T^2/t >= 2T^2 >= 10^25** (T >= 10^13, the current verification height).
Finitely many n < 10^25 cannot distinguish RH from any world whose first off-line
zero is above sqrt(n) — for every route.

**D1. Li positivity, lambda_n >= 0 (routes A/C).**
(i) REFUTATION check: a certified lambda_n < 0 at any single n. Sharpest index for a
hypothetical zero at (T, t): n* ~ T^2/t (with log corrections) — PROVEN unreachable
(n* >= 10^25). (ii) PROVE: lambda_n >= 0 for all n — that IS RH; nothing weaker is
known (lambda_1, lambda_2 > 0 unconditionally, BPY — the only unconditional cases).
(iii) NUMERICS: lambda_n to n = 10^3-10^4 via the Johansson pipeline [AUDIT]
(n = 10^5 certified record); positive throughout — consistency with RH only (cannot
be otherwise below 10^25).

**D2. B-L Weil pairing, (1/2) sum_rho ghat_n(rho) ghat_n(1-rho) = lambda_n (route A).**
(i) REFUTATION: the pairing computed from the first N zeros differs from lambda_n by
the tail — no sign information below n* (same threshold). The pairing is an identity,
not a certificate; its value here is structural (square-root factorization, §A) and as
a cross-check. (ii) PROVE: W(f_n) >= 0 for all n. (iii) NUMERICS: pairing partial sums
converge to lambda_n at rate (log gamma_N)/gamma_N — verified (CHECKED NUMERICALLY,
§V); the equality of pairing and zero-sum at every N confirms the RH-conditional
square identity on-line.

**D3. Suzuki equality, lambda_n = (1/2pi)||G_n||^2 (route B).**
(i) REFUTATION: certified inequality at ANY n — two independent witnesses; the
sharpest disproof family available (referee's remark, §B). Threshold: still n* >= 10^25
for a zero-driven violation, BUT the equality check is *quantitative* (two numbers,
all digits) rather than sign-only. (ii) PROVE: equality for all n (iff RH).
(iii) NUMERICS: direct L^2 integral vs lambda_n — shape-consistent (0.34*lambda_n at
R=100 for n = 1,2, §B); a certified high-precision evaluation of ||G_n||^2 - 2*pi*lambda_n
at n = 1..~30 is a doable next task (needs R >= 10^4-10^6 quadrature or the Parseval
route; on a laptop).

**D4. Jensen hyperbolicity, J^{d,n} hyperbolic for all d,n (route E).**
(i) REFUTATION: non-hyperbolicity of J^{d,n} for any pair with d <= T^2 implies an
off-line zero below height T (PROVEN, [GORTTW20] Thm 1.2 contrapositive; T = 3.06*10^10
implies d <= 9.36*10^20 all n, PROVEN). Numerically GORZ's remark: Jensen polynomials
are "quite inefficient at detecting zeros that violate RH" — a zero at height T only
shows up at d ~ T^2, same family as D1. (ii) PROVE: hyperbolicity for all d,n
(iff RH, Polya 1927). (iii) NUMERICS: J^{d,n} hyperbolic for all checked (d <= 10,
various n) — CHECKED NUMERICALLY (§V), consistent with the PROVEN d <= 8; root-finding
at larger d is ill-conditioned (gamma-coefficients span >20 orders of magnitude at
d ~ 10) and needs high-precision solvers — a real, bounded next task.

**Sharpest certificate in the finite regime (CONJECTURED ranking):** D3 (Suzuki
equality) is the only route whose refutation witness is quantitative rather than
sign-only, and D1 (lambda_n sign) is the only route with a certified-probe pipeline
already in hand (Johansson n = 10^5). D4 has the most PROVEN partial results but the
weakest refutation power.

---

## E. Jensen connection (GORZ 2019) [GORZ19], [GORTTW20], [O20], [H26]

**Definitions (PROVEN).** Theta(z) = xi(1/2+z) = sum_{j>=0} gamma(j)/j! * z^{2j},
gamma(j) = j! * xi^{(2j)}(1/2)/(2j)!; J^{d,n}(X) = sum_{j=0}^d C(d,j) gamma(n+j) X^j.
Polya 1927: RH iff all J^{d,n} hyperbolic (all real roots).

**Known hyperbolicity (all PROVEN, literature):**
- d <= 3, all n: CNV 1986 / DL 2009; d <= 8, all n: GORZ19 (Thm 1.1);
- d <= 2*10^17, all n: Chasse 2011 (via Borcea-Branden / Obreschkoff);
- large-n (n to infinity, fixed d): Hermite modelling — GORTTW20 Thm 1.1: hyperbolic
  for n >= c*e^{d/2} (effective);
- new wedge: H26: n^3 log^2(n+2) >= K*d^5 implies hyperbolic (d <= n^{3/5});
- RH_m(T) implies hyperbolic for d <= T^2, n >= m (GORTTW20 Thm 1.2); with Platt's RH
  up to 3.06*10^10: d <= 9.36*10^20, n >= 0 (PROVEN, Cor 1.3).

**The sharp band d ~ sqrt(n) (CONJECTURED/folklore — NOT a theorem).** The crossover
d ~ sqrt(n) is where the Hermite-model band (d <= 2 log n) meets the low-lying-zero
band (d <= n^{3/5}); at d ~ sqrt(n) the Hermite model degenerates and the zeros of
J^{d,n} begin to feel the actual xi-zeros. No PROVEN result reaches the band, and —
critically — Polya's criterion requires hyperbolicity for ALL (d, n); there is NO
propagation theorem making band-hyperbolicity equivalent to all (d, n). Claiming
"d ~ sqrt(n) carries RH" is folklore, not mathematics; [AUDIT] must not treat it as
a theorem.

**The structural correction (PROVEN + CHECKED NUMERICALLY).** The Hadamard product for
Theta(z) = sum gamma(j)/j! * z^{2j} shows hyperbolicity of ALL J^{d,n} iff
{gamma(j)/j!} is a **Polya frequency (PF) sequence** — i.e. ALL Toeplitz minors of
{gamma(j)/j!} are >= 0 (Toeplitz total positivity). It is NOT a Hankel (moment) PSD
statement. CHECKED NUMERICALLY (§V): Toeplitz minors of {gamma(j)/j!} (sizes 2-4,
shifts 0 and 2) are all POSITIVE (0.247, 5.68e-9, 0.123, ...) while the 2x2 and 3x3
**Hankel** minors are NEGATIVE (-7.06e-5, -1.47e-13). This is the mirror image of the
lambda_n correction (§0.3, §VI.1): on BOTH sides of the Li/Jensen duality the correct
positivity object is Toeplitz, never Hankel.

**Relation to Li (CONJECTURED, structural).** The lambda_n-side sum-of-squares
lambda_n = sum |1-(1-1/rho)^n|^2 and the Jensen PF condition are two faces of the
same "all zeros on the line" statement: Li tests the zeros through the circle map
rho -> theta_gamma (Toeplitz in n), Jensen tests them through the Taylor coefficients
of xi (Toeplitz in j). A proof tool that establishes either total-positivity statement
would, by Polya/Li, prove RH; none exists. GORZ's inefficiency remark (§D4) applies.


---

## V. Verification log (all numbers from saved scripts)

Scripts: `li-structure-verify-weil.py`, `li-structure-verify-jensen.py`, `li-structure-hankel.log`
(proot container /tmp; 60 dps mpmath; zeta zeros via mpmath.zetazero; probes via the
Stieltjes-constant pipeline of li-probe.md, which this audit re-validated).

- A: probe lambda_1..lambda_12 = 0.023095708966121033814, 0.092345735228046670386,
  0.20763892055432474828, ..., 3.2632553206246434403 (lambda_12; matches MaSlanka's
  3.26325532062). lambda_1 closed form 1 + gamma/2 - (1/2)log(4*pi): diff 0.0.
- B: theta_gamma = pi - 2 atan(2 gamma) vs arg(1-1/rho): diff <= 3.4e-61 (zeros 1-100).
  4 sin^2(n theta/2) vs 2(1-cos n theta): 6.3e-62. x_rho = 1-1/(2 rho (1-rho)) =
  cos(theta_rho): diff 0.0. 1 - T_n(x_rho) vs 1 - cos(n theta): 1.6e-60.
- C: det [[2-2cos0, 2-2cost],[2-2cost, 2-2cos0]] = -0.8452878799605974868 at theta=1
  (= -(2-2cos 1)^2). Per-zero QF = |sum a_j e^{ij theta}|^2 to 12 digits.
- D: (1-1/s)(1-1/(1-s)) - 1 = O(1e-62). Factorization identity exact to 6e-61 (n=3,7).
  Mellin integral vs closed form 1-(1-1/s)^n: diffs 1e-34..1e-49 (n = 1,4,8; two s).
  |hhat_n(1/2+it)| ~ n^2/t^2: t=1: 2.15; t=5: 0.914; t=20: 0.0621; t=100: 2.50e-3;
  t=500: 1.000e-4 (n=5; n^2/t^2 = 25/t^2).
- E (Weil pairing): (1/2) sum_{N} ghat(rho)ghat(1-rho) -> probe lambda_n from below:
  n=1: 0.021035 (N=200), 0.021947 (500), 0.022376 (1000), 0.022553 (1500) -> probe
  0.02309571 (tail bound <= 3.2e-4; n=10: 2.2251 at N=1500 vs 2.2793 probe). Pairing
  partial sums EQUAL zero-sum partial sums at every N (RH-conditional square identity
  on-line). Zero-sum lambda_n: same numbers (identity).
- F (Suzuki): (1/2pi) int_-100^100 |G_n|^2 dt ~ 0.00795 (n=1), 0.0318 (n=2) =
  0.344 x lambda_n both — shape-consistent modulo the heavy tail. H_n zero-sum
  convergence: |N=150 - N=200| = 3.8e-4 (n=1) at s = 1.4+0.6i.
- Jensen/PF: gamma(0) = xi(1/2) = 0.497120778188314; gamma(1..9) = 1.1486e-2,
  2.4690e-4, 4.9941e-6, 9.5813e-8, ... (all positive, ratio ~ 0.02). J^{d,n} hyperbolic
  for d = 2..10 (checked shifts 0..3; max |Im root| = 0.0; polyroots non-convergence at
  d >= 10 with shifts — conditioning, not signal). Toeplitz minors of {gamma(j)/j!}
  ALL positive (size 2: 0.24713, 5.680e-9; size 3: 0.12285, 1.470e-13; size 4:
  0.061073, 2.585e-18); Hankel minors NEGATIVE (size 2: -7.0557e-5; size 3:
  -1.4705e-13; size 4: +1.4489e-27 — sign change at size 4 is a near-cancellation of
  tiny quantities; the sequence is not a moment sequence). Log-concavity of
  {gamma(j)/j!} (d=2 case): c_{j+1}^2 - c_j c_{j+2} = +7.056e-5, +5.680e-9, ... all
  positive.
- Hankel of {lambda_n}: leading minors 2x2: -3.732e-3, 3x3: -9.852e-5, 4x4: -1.611e-11
  — NEGATIVE; {lambda_n} is NOT a Hamburger moment sequence (CHECKED NUMERICALLY).

---

## VI. Corrections to project notes (applied ONLY to this memo; other files untouched)

1. **method-frontier-synthesis.md** — "Hankel PSD iff lambda_n >= 0" (and the Li-promise
   entry) is FALSE, as previously corrected (2026-08-14). This memo adds the
   definitive witness: the Hankel matrix of the actual {lambda_n} has NEGATIVE leading
   minors (2x2: -3.73e-3; 3x3: -9.85e-5; 4x4: -1.61e-11; CHECKED NUMERICALLY, §V) —
   the claim is not merely unproven, it is false for the true lambda_n. The correct
   object is the regularized TOEPLITZ cosine form (§0.2). The 0.6818 ceiling is
   untouched: it lives in the bandlimited/moment-constrained class; the Li family is
   outside it (§A), so the ceiling does NOT constrain Li certificates — but no other
   bound replaces it either.
2. **equivalent-forms-survey.md** — the entries asserting (a) "lambda_n >= 0 iff
   {lambda_n} is a Stieltjes/moment sequence iff an explicit Hankel matrix (in Stieltjes
   constants) is PSD", and (b) "Jensen polynomials all-hyperbolic iff a Hankel matrix
   of xi-coefficients is PSD" are WRONG on the Hankel side: (a) fails by the negative
   minors just cited; (b) fails by the negative Hankel minors of {gamma(j)/j!}
   (-7.06e-5 at size 2; CHECKED NUMERICALLY, §V) while the correct (Toeplitz/PF)
   minors are positive. The surveys should be read as: Li/Jensen are TOEPLITZ-type
   positivity criteria, never Hankel.
3. **li-probe.md** — numerics are sound (lambda_1..lambda_12 and the closed form match
   this audit exactly: lambda_12 = 3.2632553206246434403, CHECKED NUMERICALLY).
   Terminology fix: "moment-positivity certificate class" is loose — lambda_n is not a
   moment sequence; the phrase should read "Toeplitz/cosine-kernel positivity
   certificate class".
4. **li_criterion_proof.md** — the "Zero-by-Zero Manifest Positivity" and "Off-Line
   Zero Exponential Destruction" analyses are correct and consistent with this audit
   (the destruction threshold n >= T^2/t matches [V22]; PROVEN). No change needed.
5. **sharp-band claim in [AUDIT] / frontier synthesis** — "d ~ sqrt(n) carries RH"
   is folklore, not a theorem (§E); no propagation result exists. Flagged for removal
   from any results summary as a PROVEN statement.

---

## VII. Ranked candidate certificates (the next moves)

Ranked by (value of a proof) x (strength of finite witness) x (numerical feasibility).

**R1. Suzuki equality family, lambda_n = (1/2pi)||G_n||^2 (route B) — first.**
- Refutation check: certified inequality at one n (two independent witnesses, all
  digits — the only quantitative disproof family in the audit).
- Infinite statement: equality for all n (that IS RH).
- Numerical evidence: shape-consistent at n = 1,2 (0.34 factor at R=100, heavy
  t^-1 log^-2 t tail). Next: certified ||G_n||^2 - 2*pi*lambda_n for n = 1..30 via
  R >= 10^4-10^6 quadrature or Parseval; on the laptop verifier. Difficulty of proof:
  RH itself (Suzuki: "new and fundamental ideas are needed").

**R2. Li positivity with certified probes (route A/C) — second.**
- Refutation: lambda_n < 0 (unreachable below n ~ 10^25, but the probe pipeline to
  n = 10^4-10^5 is already built and certified).
- Infinite statement: lambda_n >= 0 for all n (that IS RH).
- Numerical evidence: strong and cheap (Johansson pipeline, n = 10^5 record); positive
  throughout. New content from this audit: the B-L square-root factorization and the
  full-spectrum boundary statement (§A) — the honest reason this family is outside
  every known unconditional class.
- Difficulty of proof: RH itself.

**R3. Jensen hyperbolicity via PF/Obreschkoff (route E) — third.**
- Most PROVEN partial results (d <= 8, d <= 2*10^17, n >= c e^{d/2}, Holland wedge).
- Refutation: weakest (GORZ inefficiency remark; threshold d ~ T^2).
- Numerical next step: certified hyperbolicity at d = 20..100, n ~ 10^2-10^4, using
  high-precision root-finding (mpmath polyroots is ill-conditioned past d ~ 10) —
  extends the PROVEN d <= 8 by two orders as a consistency statement only.
- The PF reformulation ({gamma(j)/j!} Toeplitz-total-positive iff RH) is the cleanest
  total-positivity object found in this audit; a total-positivity proof technique
  (e.g., Karlin-type) aimed at this sequence is the only route with any theory.

**R4. Hankel-inertia diagnostics — ABANDONED as a certificate (keep as diagnostic).**
The audit shows {lambda_n} and {gamma(j)/j!} are NOT moment sequences; Hankel inertia
is expected negative and carries no RH signal. Replaced by the Toeplitz forms (§0.2,
§E). The regularized cosine quadratic form sum_{j,k} a_j a_k c_{j-k} >= 0 under RH is
the correct finite certificate on the lambda side; its finite-rank verification needs
the divergent c_0 regularized by the pairing — worth one focused session, then parked.

**Relationship to the 0.6818 ceiling (PROVEN):** all four routes are certificate-CLASS
changes. The ceiling is specific to the two-moment / bandwidth-1 / Levinson class; the
Li and Jensen families sit outside it (full-spectrum f_n, §A; PF sequence, §E) and
carry no ceiling of their own — their "ceiling" is RH itself. A certificate of the
Li/Jensen class, if it ever exists, would not be a proportion bound but the proof.

---

## VIII. Sources

[B00] E. Bombieri, Remarks on Weil's quadratic functional in the theory of prime
numbers, I, Rend. Lincei Mat. Appl. 11 (2000) 183-233.
[S23] M. Suzuki, Li coefficients as norms of functions in a model space, arXiv:2301.05779.
[GORZ19] Griffin-Ono-Rolen-Zagier, Jensen polynomials for the Riemann zeta function
and other sequences, arXiv:1902.07321.
[GORTTW20] Griffin-Ono-Rolen-Thorner-Tripp-Wagner, Jensen polynomials for the Riemann
zeta function and other sequences: towards a proof, arXiv:1910.01227.
[H26] Holland, A new hyperbolicity wedge for Jensen polynomials, arXiv:2608.08682.
[O20] O'Sullivan, Properties of the incomplete gamma function / Jensen polynomials,
arXiv:2007.13582.
[X20] Xiao, unpublished notes on Chebyshev representations of Li coefficients,
arXiv:2006.13103 (per [AUDIT]).
[V22] Voros, the off-line-zero threshold analysis (per [AUDIT] §4, [V22] (17),(23)).
[BL99] Bombieri-Lagarias, Du J. Number Theory 77 (1999) 274-287.
[L99] Lagarias, Li coefficients for automorphic L-functions, Ann. Inst. Fourier 2005
(announced 1999).
[AUDIT] li-literature-audit.md (this wave's literature audit).
