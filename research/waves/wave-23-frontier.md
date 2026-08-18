# Wave 23 frontier — open direct-RH inputs ONLY (2026-08-18)

**Generator rule (binding):** propose ONLY one-way objects that (a) are not on the
do-not-repeat ledger, (b) attach an RH-false control (Davenport–Heilbronn, planted-zero
Beurling, fake-Weil via tools/barrier_zoo), (c) are checkable by real compute (script +
numeric run), and (d) lead with the input — NOT the fallback. Known ⟺RH equivalences
re-proposed as "success = prove RH" will be rejected by the GATE before compute.

New data since wave 22 (for input generation, all CHECKED NUMERICALLY):

- r′(T) = (Σ|ζ″(ρ)|²)/(L²·Σ|ζ′(ρ)|²) at real zeros: 0.8168/0.8447/0.8623/0.8688/**0.8882**
  at T = 150/300/600/900/3000 (N=2403, 97.3% capture; S₁/law1 → 1.17 continuing down toward 1 —
  validates the pipeline). Limit fit-ladder: 1/L → **0.963** (best MSE 7e-7), 1/L² → 0.910,
  1/L³ → 0.892. 0.87 dead, 0.90 disfavored. T=6000 discriminating run in flight (0.955 vs 0.930).
- λ_min(G_N) of the Báez–Duarte Gram matrix: **0.634·N^(−1.837)** power law (validated port +
  eigsy, 30 digits). Spectral-gap/diagonal-dominance routes to d_N ≤ C/log N are DEAD —
  measured 10⁶× below the 1/log N bar at N=2^16. NOTE: the *sharp rate itself* d_N ~ c/√(log N)
  (c ≈ 0.213 flat to N=5000) is consistent with the ill-conditioning: the rate lives in the
  specific vector v_k = ⟨1,ρ_{1/k}⟩ = (log k + 1 − γ)/k, not in λ_min. Any d_N bound that uses
  only spectral information is provably wrong-shaped.

## OPEN lanes (fundable directions — lead with the INPUT)

1. **S₂-limit r∞ — now ≈ 0.91–0.96 by two independent power-law fits; T=6000 separating.**
   Input: if r∞ ≈ 0.96 (1/L wins), BHB box b ≤ 0.061; if 0.91, b ≤ 0.063. Both make the
   (blocked) moving-boundary count HARDER — so no positive RH route here; the only open value
   is a sharper constraint on the BHB framework. Do not re-propose this as an RH proof.
2. **8C Báez–Duarte sharp-rate structure.** OPEN honest questions, all consistency-level:
   (a) extend the certified d_N·√(log N) ≈ 0.213 flat law beyond N=5000 (MPFR Cholesky OOMs at
   ≥3000; f64 stored-G refinement path exists to ~2000, then adaptive truncation limits);
   (b) explain the shape of d_N²·log N = 1 − vᵀG⁻¹v·log N rising slowly at small N (0.113 →
   0.153 at N=10..30): is the correction O(√log N) or O(1)? This is the honest mathematics
   behind the flat law, and a NEW quantitative object (the finite-N correction law) nobody has
   stated. RH-false control: planted-zero Beurling world must give a DIFFERENT correction law.
3. **The ξ,ξ′ jet structure / positive simple-zeros certificate** (from the tower audit,
   status CORRECTED): given the rung-2 kill (κ₁^(2) ≥ κ₁^(1)) and the G²/H Cauchy fatality,
   can ANY positive (simple, on-line) zeros certificate exist on (ξ,ξ′) / (ξ,ξ′,ξ″) jets?
   The honest open question is structural — propose a real SDP/dual inequality or a proof of
   impossibility. Control: Davenport–Heilbronn must fail any candidate certificate.
4. **Weil positivity / sub-prime densities** — new test functions only; cosine-Gram and
   specific-prime cases are closed. No repackaging of existing test pairs.
5. **Geniunely new one-way objects.** Anything not in the ledger: new arithmetic objects with
   ζ-value constraints, new discriminants that separate the RH world from a planted-zero world
   by COMPUTATION (not by equivalent restatement).

## Closed / do-not-propose (recent majors)

- Gram spectral-gap / diagonal dominance → d_N ≤ C/log N (MEASURED DEAD, gramlam note).
- Speiser winding extensions beyond the PROVEN certleft band; Li-coefficient positivity;
  Rouché-winding of Taylor polynomials; Nyquist–Bode phase bounds; Lee–Yang Ising encodings;
  Wiener–Tauberian restatements (wave-22 g0–g2 verdicts).
- Direction-2 soundstate 2×2 SDP (closed by convexity); T-2 tower Gonek trace
  (G²/H Cauchy fatal); GS-2026 diagonal C<2 (no unconditional input; same paper as GS box);
  Bui–Heath-Brown partial unconditionalization (no route clears p₀);
  GS/BGSTB box (width ceiling 1.3275); r′ = 3/5 (dead at every height).
- The 0.213 proportion record and all λ-dilation saturation numbers: proportion-theorem only,
  NOT RH evidence — never propose as proof input.

## Deliverable format

For each funded probe: one file under research/waves/wave-23/ stating the object, the exact
computation, labels (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE),
and the RH-false control verdict. No claim is progress until the control fails to break it.