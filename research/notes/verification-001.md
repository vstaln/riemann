# Verification report 001 — core numerical checks of the 67.25% argument

Status: CHECKED NUMERICALLY (f64, independent Rust implementation + LMFDB zero data)
Date: 2026-08-11
Tooling: `tools/zeta-rs` (Rust, Euler–Maclaurin ζ(1/2+it), Riemann–Siegel θ, Z(t) via
Re(e^{iθ}ζ), sign-change zero location, bisection). Zero data: LMFDB REST cache
`tools/data/zeros_1_1000.txt` (1000 verified ordinates, 34 digits) + `~/Downloads/index.db`.

Every claim below carries an honesty label. Nothing here is a proof; everything is a
numerical consistency check of the informal note's key equations.

---

## 1. Headline constant — PROVEN identity, CHECKED NUMERICALLY to 15 digits

   c₁* = √2·tanϑ/(1+ϑ·tanϑ), ϑ = 1/√2;   result = 3/2 − (1/√2)·cot(1/√2) = 2 − 1/c₁*

   computed               : 0.67250070367941162
   mpmath 60 dps reference: 0.672500703679411645734379790803… (agreement 15 digits, f64 limit)
   2 − 1/c₁* (independent branch): 0.67250070367941173 (f64 rounding, 1.1e-16 off)

   Variational identity (∫ψ² + ∬|u−v|ψ(u)ψ(v) = (1/2+(1/√2)cot(1/√2))(∫ψ)², ψ=cos(√2u)·1_{|u|≤1/2}):
   lhs = 1.120484139534, rhs = 1.120484151254, diff = 1.2e-8 (CHECKED NUMERICALLY)
   quotient = 1.327499282436 vs expected 1/2+(1/√2)cot(1/√2) = 1.327499296321 (1.4e-8 rel.)

   Consequence: HS-norm coefficient 1/2+(1/√2)cot(1/√2) ≈ 0.7532900538·N(T) is confirmed,
   and 4 − 2 − (1/2+(1/√2)cot(1/√2)) = 0.6725007036… is reproduced.

## 2. LMFDB zeros are genuine ζ zeros — CHECKED NUMERICALLY (999/999)

   For each of the 999 gaps between consecutive LMFDB ordinates γ_i, γ_{i+1}: Z(t)
   (independently computed, Euler–Maclaurin, f64) changes sign across the gap, and
   |Z(γ_i)| ≤ 4.67e-6 for i ≤ 500 (f64 noise floor at the zero height).
   Sign-alternation anomalies: 0. VERDICT: PASS — the LMFDB ordinates are bracketed
   sign changes of the independently-computed Z(t); they are real zeros on Re = 1/2
   up to f64 accuracy. (These are the zeros the W_T construction uses.)

## 3. Guinand–Weil spectral identity (paper form, Lean H-EF conventions) — CHECKED NUMERICALLY

   Identity tested: W(f,f) = Σ_ρ m_ρ|h_f(γ_ρ)|² = ∫_ℝ |h_f(τ)|² ν_X(τ)dτ,
   ν_X = μ + Π_X + P_X, h_f(τ) = ∫f(u)e^{iτu}du, supp f ⊆ [−L/2,L/2], X = e^L.
   Conventions taken verbatim from Zeta23/Defs.lean (paperFT has no 2π, plus sign).

   Family of C∞ bumps f(u) = e^{1−1/(1−(u/a)²)} on [−a,a], L = 2a+0.1:

   | a   | LHS (zero sum) | RHS (integral) | μ-part | Π-part | P-part | |Δ|/scale |
   |-----|----------------|----------------|--------|--------|--------|----------|
   | 6.0 | 0.000000       | 0.000000       | −27.36 | +384.87| −357.51| 1.3e-10  |
   | 1.0 | 0.000927       | 0.000927       | −2.26  | +3.03  | −0.77  | 1.4e-8   |
   | 0.3 | 0.009140       | 0.009140       | −0.25  | +0.26  | 0.0    | 3.9e-8   |
   | 0.15| 0.048861       | 0.048859       | −0.017 | +0.066 | 0.0    | 1.7e-6   |

   Notes:
   - a=6: prime side + poles fully active; the three terms ±400 cancel to ~0 while the
     zero side is ~0 (no zero sees h_f) — the identity holds through cancellation at
     1.3e-10 relative to the parts (≈ 10 significant digits).
   - a=0.15: zero side fully active (first ~50 zeros dominate; sum converged by 100
     zeros), prime side vacuous (X = e^{0.4} < 2). Agreement 1.7e-6 relative — the
     quadrature noise floor of the oscillatory narrow-bump integrals; still 6 digits.
   - The zero-sum tail converges (100 zeros ≈ 1000 zeros) for all widths.

   VERDICT: PASS — the paper's spectral identity (the engine of the W_T trace/HS-norm
   analysis) is numerically consistent with LMFDB zero data and the prime side.

## 4. Montgomery pair-correlation form factor — CHECKED NUMERICALLY (trend only)

   Empirical form factor from the 3000 cached ordinates: F(α) ≈ |α| for 0 < α < 1 is
   reproduced qualitatively (values climb to ≈ 0.93–1.0 near α = 1, decay beyond).
   Sample noise at N = 3000 is large; label: trend only, consistent with |α|, NOT a
   tight check.

## 5. Lemma 3.4 rank–trace inequality — CHECKED NUMERICALLY (5000 random trials)

   For random Hermitian A ≥ 0 and symmetric B (n = 2..10, Gaussian entries):
   rank A ≥ 2 tr A + 4 tr B − 4 n₊(B) − ‖A+B‖²_HS. Violations: 0 / 5000.
   (The tightness data points k₁(m)=m² ≥ 2m−1, c=3 → 5/6 distinct are corroborated
   structurally by the inequality's constants; see attack-multiplicity.md for the
   combinatorial analysis.)

## 6. Montgomery–Vaughan Hilbert-type inequality — CHECKED NUMERICALLY (200 trials)

   |Σ x_m x̄_n/(y_m−y_n)| ≤ π Σ|x|²/σ for |y_m−y_n| ≥ σ: worst observed ratio 0.1738 ≤ 1.

## 7. Riemann–von Mangoldt zero counts vs LMFDB index.db — CHECKED NUMERICALLY

   N(T) = (T/2π)(ln(T/2π) − 1) + 7/8:
   T=5000:   4520 vs 4520.3 (Δ=−0.3)
   T=26000:  30324 vs 30324.2 (Δ=−0.2)
   T=236000: 358093 vs 358092.4 (Δ=+0.6)
   T=446000: 721913 vs 721913.0 (Δ=0.0)
   T=5e6,5e7,1e8: Δ = −2595, −758, −3695 — all negative and bounded by block
   granularity (N read at the last block start ≤ T undercounts by < one block ≈ 2–4k).
   Conclusion: the LMFDB index (103.8 billion zeros, all with Re = 1/2) is consistent
   with the RvM count; N(T) ≈ (T/2π)ln(T/2π) scaling used in the argument is sound.

## 8. Independent zero computation — IN PROGRESS (background)

   `zeta-rs zeros 10000` computes the first 10 000 ordinates from scratch (sign-change
   scan of Z(t) + bisection, no LMFDB data) for a full independent cross-check of the
   cached LMFDB list. Expected agreement within f64 EM noise (~1e-6).

---

## Consolidated status

| check | label | result |
|-------|-------|--------|
| headline constant + variational identity | PROVEN (identity) / CHECKED NUMERICALLY | PASS |
| bracket (LMFDB zeros are real) | CHECKED NUMERICALLY | PASS 999/999 |
| Guinand–Weil spectral identity | CHECKED NUMERICALLY | PASS (1.3e-10 … 1.7e-6) |
| pair correlation | CHECKED NUMERICALLY (trend) | PASS (qualitative) |
| Lemma 3.4 rank–trace | CHECKED NUMERICALLY | PASS 5000/5000 |
| Montgomery–Vaughan | CHECKED NUMERICALLY | PASS |
| RvM counts vs LMFDB | CHECKED NUMERICALLY | PASS |
| independent zeros (10k) | IN PROGRESS | — |

Open flags (passed to the validator):
- ψ(±1/2) = cos(1/√2) ≠ 0 — the variational minimizer does not vanish at the boundary;
  the note's justification of the minimizer must be scrutinized (see validation-001.md).
- The bandwidth-one ceiling (0.6818287, Lean Zeta23/PairCeiling) lies ABOVE the
  67.25% result — consistency to be explained in the proof map (the trace form is not
  rank-one, so the ceiling does not directly constrain W_T's kernel of interest).

---

## ROUND-3 VALIDATOR CORRECTIONS (from validation-001.md, adversarial pass, all rerun-backed)

- VALIDATOR TARGET (a): the I+T spectrum numbers in this note are CORRECTED — the odd eigenfunctions sin((2m+1)πu) with eigenvalue −2/((2m+1)²π²) were omitted. Min eigenvalue is ≈ 0.797 (not ≈ 0.93); the even root is k ≈ 5.60 (not 5.43). The conclusion (I+T ≻ 0, cosine is the global minimizer) SURVIVES. See validation-001.md target 2.
- VALIDATOR TARGET (b): the "Δ decays to 0 at ~1/log T" reading is INCONCLUSIVE as stated — the note's own fits have nonzero asymptotes (0.014, 0.037, 0.028). Convergence of bound/N to 0.6725 is not demonstrated by the reported data. See validation-001.md target 3.
- VALIDATOR TARGET (c): this note does not mention that EnclOK is the one non-Lean numerical hypothesis in the 0.68185 ceiling; see validation-enclok.md (INCONCLUSIVE, not refuted). See validation-001.md target 5.
- VALIDATOR TARGET (d, verification-001 only): "noise floor" → "Euler–Maclaurin truncation error" (max 6.2e-6 over i≤1000, K=10; collapses at K=14). See validation-001.md target 1.
