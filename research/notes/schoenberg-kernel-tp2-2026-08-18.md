# Schoenberg shift-kernel TP2 probe — FINAL REPORT (certified mpfr)

Date 2026-08-18. Lever: DISPROOF-CAPABLE-as-briefed check of K(x,y)=Ξ(x−y), Ξ(t)=ξ(1/2+it).
Verdict: **probe is NOT disproof-capable — the brief's premise is FALSE (PROVEN). Data is
RH-CONSISTENT (zero evidential weight). The lever as designed points the WRONG WAY.**

Files: tools/wave8d/src/bin/schoenberg_tp2.rs (f64, exploratory — Stirling-inaccurate near
t=0, keep only as documentation of the f64 pitfall), tools/wave8d/src/bin/schoenberg_tp2_mpfr.rs
(hybrid certified, THE probe), src/bin/schoenberg_tp2_body.inc (lk_zeta_mpfr body, include).
Output: /tmp/schoenberg_final.out (also schoenberg_mpfr.out, schoenberg_tp2.out).

## 1. The premise is FALSE (PROVEN) — this kills the lever
Brief: "Schoenberg (1951): f ∈ LP ⟺ shift kernel K(x,y)=f(x−y) totally positive. Hence a
negative 2×2 minor for K_Ξ ⟹ Ξ ∉ LP ⟹ RH false." The claimed equivalence is FALSE.

Counterexample (EXACT, hand-checked): f(t)=sin(t)/t = Π_{n≥1}(1−t²/(nπ)²) ∈ LP (real zeros,
uniform limit of real-zero polynomials — textbook). Its shift kernel has a negative 2×2 minor:
x=(0, π/4), y=(−5π/4, −π/2) (x₁<x₂, y₁<y₂) gives
det[[f(x₁−y₁),f(x₁−y₂)],[f(x₂−y₁),f(x₂−y₂)]] = det[[−2√2/(5π), 2/π],[−2/(3π), 2√2/π]] = −4/(15π²) ≈ −0.0270 < 0.
Numerically: min minor over grids = −2.28e-1, negative rate 4907/10456 ≈ 47% (both f64 and mpfr runs).

The CORRECT Schoenberg duality is the Fourier-transform one: f ∈ PF∞ ⟺ 1/f̂ ∈ LP (LP of the
transform variable, zeros iα_k imaginary). An even LP function with REAL zeros (the structure
RH gives Ξ) is NOT the FT of a PF function; its shift kernel is generally NOT TP. Negative
shift-kernel minors are the TYPICAL signature of even-LP-with-real-zeros (sin(t)/t: 47%
negative). The brief's chain "RH ⟹ Ξ∈LP ⟹ K_Ξ TP ⟹ minors ≥ 0" breaks at the second link.

## 2. Evaluation machinery (certified)
Hybrid Xi evaluation, RUST ONLY:
- Taylor Ξ(t)=Σ(−1)^k b_k t^{2k} for |t| ≤ 12, b_k = M_k/(2k)!, M_k = 2∫₀³Φ(u)u^{2k}du,
  Φ(u)=2Σ(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}} (Simpson 2¹⁸, n≤40). b₀=0.497120778188282
  (true 0.497120778188314), b₁₀=5.622858e-25 (true 5.62286e-25) ✓. Taylor abs err ≤ ~1e-10 at
  |t|≤12. NOTE: f64 Taylor is INVALID for t ≳ 25 (alternating terms reach ~1e9–1e14 at
  t=30–56, cancellation leaves error O(1) — the cross-check at 30.4/56.4 shows exactly this:
  Taylor +4.9e-3/+2.0e16 vs certified Stirling −3.0e-15/+5.2e-23). This is why |t|>12 uses mpfr.
- mpfr (rug, prec=100) Stirling gamma (term-truncation certified, z^−2 stepping fix) ×
  zeta_em_ders_mpfr(n=600, K=40) for |t| > 12, via xi_complex_mpfr from lk_zeta_mpfr.rs.
- CROSS-CHECK at γ₁: Taylor 1.960219e-10 vs Stirling 1.959793e-10, diff 4.3e-14 ✓. Machinery
  sound. (|Xi(γ_j)| = 1.96e-10 … 5.2e-23 = true values at the truncated γ_j; the f64 Stirling
  path was accidentally accurate there.)
- f64-only Stirling is NOT trustworthy near t=0 (divergent series at |z|≤1.5: Xi(0)=0.5053 in
  the existing lk_zeta f64 binary, 1.6% high; mpfr Stirling Xi(0)=0.4423±0.079, 11% low with
  HONEST certified error) — hence the Taylor fix. Sign-pattern "failures" in the f64 run were
  a stale expectation table (γ₁₃≈59.35, γ₁₄≈60.83 both below t=62.1/66.1), not an eval error.

## 3. Certified TP2 results (mpfr, prec=100, margins = 100× certified err)
Controls (machinery gates): exp(−t²) min +1.66e-11, 0/10000 negatives (≥0 ✓);
1+t²−t⁴/2 (NOT LP) min −1.50e13 (<0 ✓, probe detects non-TP); sin(t)/t (LP, real zeros)
min −2.28e-1, 4907/10456 negatives (premise-refuting signature, as §1).
Target K(x,y)=Ξ(x−y) on [0,60]² (random x₁<x₂,y₁<y₂ grids + near-zero windows at γ₁..γ₁₂):
- 60×60 grid:  min minor = −3.854e-4  (cert err 8.0e-13, margin 4.8e8)   neg 1404/3888 = 36%
- 90×90 grid:  min minor = −3.929e-4  (cert err 8.0e-13, margin 4.9e8)   neg 3131/8388 = 37%
Certified negative 2×2 minors exist with enormous margin. Sign: same qualitative signature as
the provably-LP sin(t)/t control (negative rate 36–47%, magnitude scale follows |Ξ| being
smaller than |sin/t| on the sampled differences). This is exactly the expected behavior of an
RH-consistent even LP function with real zeros.

## 4. VERDICT
**RH-CONSISTENT (negative Xi shift-kernel minors are RH-consistent with ZERO disproof weight).
The probe is NOT disproof-capable: the brief's premise "f ∈ LP ⟹ shift kernel TP2" is PROVEN
FALSE (exact sin(x)/x counterexample −4/(15π²), numerically min −2.28e-1).** No RH disproof
signal; no escalation. The disproof-capable direction for RH remains the CLOSED 2026-08-15
Hankel lever (RH ⟹ T_k = b_k²−b_{k−1}b_{k+1} > 0 and D_n alternation (−1)^{n(n+1)/2}; a failure
there would be a real disproof — cite total-positivity-2026-08-15.md, do not re-derive).

## 5. Ledger line (appended)
schoenberg-kernel-tp2-2026-08-18 | K(x,y)=Ξ(x−y) 2×2 minors | RH-CONSISTENT / premise REFUTED
| label: DISPROOF-CAPABLE-as-briefed but premise FALSE — "f∈LP ⟹ shift kernel TP" disproven by
sin(x)/x (exact −4/(15π²), 47% negative minors); Ξ has certified negatives (min −3.9e-4, margin
5e8) = LP-typical, zero RH weight; correct Schoenberg duality is FT-based (PF∞ ⟺ 1/f̂∈LP);
do not re-run this lever.
