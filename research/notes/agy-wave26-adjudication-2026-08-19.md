# agy wave-26 adjudication — one-way discriminators, probes RUN (2026-08-19)

**Source:** agy one-shot (`tools/agy_run.sh`, prompt /tmp/agy-wave26-prompt.txt, output
/tmp/agy-wave26.out) on lane #5 hard-mode: genuinely-new one-way discriminators by
computation, with waves 24-25 kills blocklisted. Three candidates. **No survivor; C1
decisively REFUTED; meta-finding: agy's predicted numeric gaps are fabricated.**

## Candidates & probes

1. **C1 — Bohr–Toeplitz resolvent defect.** M_{m,n}(σ,T) = (mn)^{−σ}·(1/2ΔT)∫|ζ(σ+it)|²·(m/n)^{it}dt,
   δ_K = λ_min/λ_max, claimed δ_15 ≥ 0.015·15^{−2σ} and a **2.25e4× suppression** on DH at
   (0.8085, 86.845).
   **REFUTED — CHECKED NUMERICALLY.** Probed (K=10, 48-pt GL, vectorized |ζ|²): at
   (0.8085,86.845) δ_zeta=**1.75e-7**, δ_DH=**4.99e-7**, gap **0.4×** (not 2.25e4×); at
   (0.75,86.845) 1.9e-7 vs 6.0e-7 gap 0.3×; (0.8085,50) 2.5e-7 vs 3.1e-7 gap 0.8×;
   (0.70,20) 6.3e-7 vs 8.1e-7 gap 0.8×. Both worlds tiny and nearly identical; real zeta
   often SMALLER than control. agy's predicted δ_zeta≈0.0412 was wrong by ~2.4e5×; the
   10⁴× separation does not exist.
2. **C2 — Dirichlet scattering commutator.** Ω_N = ‖[G_N,Λ_N]‖²_F/(‖G_N‖²_F·(logN)²) ≤ 1.25/N.
   Zeta side: Ω_10 = 0.084/0.035/0.087 at (0.69,3.82)/(0.75,20)/(0.8085,86.845), all ≤ 0.125
   threshold. BUT: (a) the T=3.82 window [−1.18,8.82] passes near the s=σ pole at t=0 → the
   0.084 is pole-contaminated, meaningless; (b) the claimed Epstein-class-2 ~20× elevation
   (Ω=0.387) was NOT reproducible — the theta-Mellin control eval times out in budget.
   **INCONCLUSIVE on control; zeta-side numbers pole-contaminated at the decisive point.**
   agy's predicted numbers (0.0194 / 0.3871) were never computed by agy.
3. **C3 — prime-fiber orthogonal defect.** Φ_K = (1/K)Σ(J(p_k;σ,T) − Re Σ p_k^{−m(σ+iT)}/m)² < 5e-4,
   claimed 4,570× DH gap at (0.8085,86.845). **NOT probed** (C1's failure + C2's
   non-reproducibility make agy's 4570× prediction unverifiable in budget); predicted
   numbers uncomputed by agy.

## Meta-finding (the real result of this wave)

**agy's quantitative predictions in wave-26 are systematically fabricated — every predicted
"separation gap" was asserted without computation, and the one that was testable (C1's
2.25e4×) measured 0.4× — wrong by 5+ orders of magnitude and in the wrong direction.**
This matches the wave-23 pattern (C2 "0.106 = 0.5·0.212" numerology; Q_3 "0.200" CUE
constant wrong). The honest conclusion: agy generates plausible-sounding discriminators with
confidently-fabricated control numbers; every candidate must be run before any belief change,
and the predicted gaps specifically must be ignored as untrustworthy.

## Net

- Wave 26: **no survivor** (C1 REFUTED, C2 INCONCLUSIVE, C3 unprobed).
- The "average |ζ|² / log|ζ| over short t-windows, look for defect vs Euler expectation"
  family is now partially tested: the Bohr–Toeplitz instance fires identically on DH.
- Firewall intact; nothing RH-implying survives; all claims labeled; every probed number
  ground in the actual run.

## Files
- prompt: /tmp/agy-wave26-prompt.txt; output: /tmp/agy-wave26.out;
  probes: /tmp/w26_c1.py, /tmp/w26_c2.py (zeta-side) + inline Epstein attempts.
