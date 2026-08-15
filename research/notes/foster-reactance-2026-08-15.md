# Foster reactance transfer (g1-1): F = d/ds log Xi as LC immittance

Date: 2026-08-15. Status: ANALYZED + CHECKED NUMERICALLY — the analogy is EXACTLY
equivalent to RH (deflating class 2: equivalent-to-RH restatement), no new proof
route; finite C-fraction check built and PASSES (all coefficients positive to a_40
at 200-digit precision). Ledger: fresh lever, no prior verdict.

## 1. Setup and the exact lemma

Xi(s) = xi(1/2+s) = Σ_k b_k s^{2k}, b_k = xi^{(2k)}(1/2)/(2k)! > 0 (repo's gamma(k)/k!).
F(s) := d/ds log Xi(s). F is odd, real-on-real, meromorphic; poles = zeros of Xi
(multiplicity m = residue m). Zeros pair ±s_k; Hadamard (genus 1, automatic from
pairing): Xi(s) = Xi(0)·Π_k (1 − s²/s_k²), Σ 1/|s_k|² < ∞, so
F(s) = Σ_k 2s/(s² − s_k²) (absolutely convergent on compacta).

**Lemma (PROVEN, two-line argument):** RH ⟺ Re F(s) ≥ 0 for all Re s > 0.
(⇒) each term 2s/(s²+ω²), ω real, has Re = 2σ(σ²+τ²+ω²)/|s²+ω²|² ≥ 0 iff σ ≥ 0.
(⇐) if a zero has α = Re s_k > 0, then at s = s_k − ε (0<ε<α): Re F ≈ Re[m/(s−s_k)]
= −m/ε < 0 with Re s > 0. Contradiction. Zeros on Re s = 0 ⟺ RH.

**Corollary (PROVEN, classical Stieltjes/Foster theory):** RH ⟺ F has the Foster
partial fraction Σ c_k 2s/(s²+ω_k²), c_k ≥ 0, ω_k ∈ R ⟺ g(z) := F(s)/(2s) = Σ_k 1/(z+γ_k²)
is Stieltjes ⟺ with g(z) = Σ_n (−1)^n m_n z^n, m_n = Σ_k γ_k^{−2n−2}, the sequence {m_n}
satisfies det[m_{i+j}] > 0 and det[m_{i+j+1}] > 0 for ALL n ⟺ all coefficients of the
regular C-fraction of g are positive (Stieltjes' S-fraction theorem). The m_n are
COMPUTABLE from b_k: g = N/D, N(z) = Σ_{k≥1} k b_k z^{k−1}, D(z) = Σ b_k z^k
(check: g(0) = b_1/b_0 = F'(0)/2 ✓, m_0 = b_1/b_0 = Σ1/γ² ✓).

## 2. Where the analogy breaks (boundary test — the real deliverable)

Foster's theorem converts a GIVEN immittance into realizability. Here the poles ARE
the unknown — they are the zeros of Xi, i.e. exactly RH's content. The finite data
b_0..b_N determine only the first N Taylor coefficients of F at 0. Two proven facts
kill the "finite proof" idea:

(a) The reactance condition is an EXACT equivalence (Lemma): a restatement of zero
location, not a simplification. The Foster transfer buys nothing by itself.

(b) **No uniform control (PROVEN sketch):** CF coefficients are continuous functions
of the pole data s_k, and at all-imaginary data they are all strictly positive; an
off-line zero pair at distance α>0 perturbs them continuously, so for every fixed N
there is α>0 with the first N coefficients still positive while RH fails. Violation
index → ∞ as α → 0. No a priori bound ties "first N positive" to "no zeros with
|Re ρ − 1/2| > δ". A finite check (any fixed N) can never rule out near-line zeros.

So: TRUE but EQUIVALENT reformulation; the C-fraction positivity is the same infinite
staircase as total positivity of {b_k} (PF-sequences) and Hermite–Poulain J_{n,d}
all-rooted — pairwise equivalent, all PROVEN classical. Residue that could be
non-tautological (CONJECTURED, not attempted): a DIRECT proof that g = N/D is
Stieltjes from the explicit integral form of b_k (Φ > 0), bypassing the zeros.

## 3. The check (Rust, f64, <1s compute; input prep ~1 min at 400 digits)

Rust: tools/foster_check/ (b.txt = b_0..b_42 from repo explicit-formula tower,
dps=400 — cross-validated vs dps=1200 to 1e-244; moments from b_k match verified-zero
power sums to ~1e-5, residual = m_0 analytic-tail approximation). Algorithm: scaled
w = z/ρ, ρ = 199.79 ≈ γ_1² (positivity of CF coefficients invariant under z→ρz,
PROVEN: Hankel determinants scale by ρ^{n(n+1)}); series division Ñ/D̃ → moments
m̂_n = m_n·ρ^{n+1}; regular C-fraction a_i = 1/cur[0], cur ← (1/cur − a_i)/w.
VERDICT: PASS — a_1..a_18 all > 0 (f64), a_1..a_40 all > 0 at 200 digits (mpmath,
same algorithm: first non-positive = NONE). Consistent with RH. A FAIL (some a_i ≤ 0)
would be a disproof of RH; not seen.

Two corrections to the plan as designed:
(i) b_k do NOT underflow f64: b_k = b_0·e_k(1/γ²), elementary-symmetric sums, decay
like e^{−c√k} (b_60 ≈ 1.7e−200). The moments m_n = Σγ^{−2n−2} DO (m_n ~ γ_1^{−2n},
underflow at n ≳ 130) — the ρ-scaling handles that.
(ii) f64 alone is NOT stable for the direct CF recursion past a_18 (a_19..a_40 come
out negative in f64 — PRECISION COLLAPSE from the series' singularity at |w|=1:
reciprocal coefficients grow per level; confirmed by the 200-digit run, which is all
positive, as the positive-measure theorem guarantees). Documented as a numerical
caution: direct CF recursion needs high precision or a stable algorithm (qd).
Also: the naive Edwards-Φ quadrature M_k = 2∫Φu^{2k}du disagrees with xi^{(2k)}(1/2)
by a k-DEPENDENT factor (1.50, 3.10, 4.67, 6.32, 8.06, 9.88 for k=0..5) — the
task-convention M_k ≠ xi^{(2k)}(1/2); ABANDONED in favor of the repo's validated
explicit-formula tower. Also: a_even grows ~ linearly (14, 26, 39, 48, ...) — real
behavior for sparse-atom Stieltjes measures, NOT divergence to ±∞; the "a_n → a/4"
limit claim only holds for continuum measures and was DROPPED.

## 4. Forecast + inversion

Forecast was PASS; confirmed (a_1..a_40 positive, 200 digits). Likely-wrong spots I
checked: (i) the support condition in the Stieltjes criterion — unconditional
(compact support [γ_1²/ρ, ∞), positive atoms), sound; (ii) the a_n → a/4 limit —
WRONG for sparse measures, dropped; (iii) my first Φ-quadrature — wrong normalization,
caught by validation vs repo constants (b_0 = xi(1/2), m_0, m_1, m_2); (iv) f64
stability of the CF recursion — FAILS past a_18, caught by 200-digit cross-check.

## 5. Bottom line

The Foster reactance transfer is a genuine, PROVEN equivalent of RH (positive-real
Xi'/Xi ⟺ zeros on the line) but it is a RESTATEMENT, not a route: proving Re F ≥ 0 or
positivity of the C-fraction coefficients is exactly the RH staircase. The finite
check passes and re-derives the validated Turán/Laguerre controls (ledger: cite, do
not relitigate). No new theorem, no ABANDONED line — classified: equivalent-to-RH
restatement with a working finite-check tool for future re-use. Next lever if wanted:
the CONJECTURED residue (direct Stieltjes representation of N/D from Φ's integral
form) is the only non-tautological direction, and it is a hard analytic problem.
