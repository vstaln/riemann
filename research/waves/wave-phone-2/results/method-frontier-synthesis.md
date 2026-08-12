# SYNTHESIS — the method frontier (2026-08-12)

Three research agents (SOTA audit, ceiling-breaker, equivalent-forms survey) landed.
Converged answer to "we need a better method, not more compute": **the in-class
Levinson certificate is exhausted at 0.6818; the better method is a NEW certificate
class that has no 0.6818 ceiling.** Two candidates, both RH-equivalent (no shortcut —
proving either fully IS RH — but both are genuinely different doors with real
incremental surface):

## 1. Li's criterion → Hankel-matrix / moment positivity  [PROMISE: HIGH]
- RH ⟺ λ_n = Σ_ρ [1 − (1−1/ρ)^n] ≥ 0 for all n ≥ 1, where λ_n = (1/(n−1)!) dⁿ/dsⁿ[s^{n−1} log ξ(s)]_{s=1}
  are exactly computable from the Stieltjes constants.
- λ_n ≥ 0 ⟺ {λ_n} is a moment sequence ⟺ a Hankel matrix (in Stieltjes constants) is PSD.
- **This is a moment-positivity certificate class orthogonal to Levinson's zeros-counting** —
  it speaks the program's native language (law / m₃ / E(1) / marked-T) but has NO a priori
  0.6818 ceiling. Under RH λ_n ~ (n/2) log n (positive, growing); if RH fails, λ_n turns
  negative with exponential amplitude oscillating at the off-line height — an extremely sharp probe.
- Concrete next step: compute Stieltjes constants → λ_n to n ~ 10⁴–10⁵ (parallel), check
  positivity + Hankel inertia (interval arithmetic); hunt a positive-definite representation
  of the Hankel form (the program's own "law" is the prototype).

## 2. Jensen-polynomial hyperbolicity  [PROMISE: HIGH, freshest surface]
- RH ⟺ every Jensen polynomial J^{d,n} from the ξ-coefficients is hyperbolic (all-real roots),
  Griffin–Ono–Rolen–Zagier 2019. Proven for d = o(√n); the SHARP band d ≍ √n carries RH.
- Finite-dimensional, exactly computable, embarrassingly parallel; may admit an
  Obreschkoff / derivative-interlacing rigidity proof.

## Rejected for novelty (honest)
- Λ (de Bruijn–Newman): only finite numerical bounds; Λ≤0 IS RH, no intermediate.
- Robin / Mertens / Riesz: pure RH-in-disguise tests.
- Weil-positivity: already the program's occupied home (the 0.6818 ceiling is its finite-family gap).
- Hilbert–Pólya: no object exists to compute with yet.
- Higher moments m→∞: RS wall (kλ<2) — a genuine barrier, not a limitable gain.

## Where our 0.6733 actually sits (honesty)
- Published UNCONDITIONAL record: 5/12 ≈ 0.4167 (Pratt–Robles–Zaharescu–Zeindler 2020).
  Our 0.6732660791 is far above it, BUT it is a different, stronger certificate-defined
  "simple-on-line" statistic — CHECKED NUMERICALLY, not a classical hand-proved κ record.
- It beats the formalized Thm D (0.6725) but sits below the PROVEN in-class ceiling 0.6818312306.
- The 2/3→68% wall is a certificate-class ceiling, NOT a number-theory wall.

## The decision
Adopt **Li's criterion (moment-positivity certificate)** as the primary new method.
It is the only door with (a) no a-priori ceiling, (b) program-native language, (c) exactly
parallelizable numerics, (d) a concrete symbolic lemma to hunt (positive-definite Hankel
representation). Jensen hyperbolicity is the parallel second track.

## Tags
PROVEN: equivalences (Li, Jensen, Robin, Mertens, Λ, Nyman–Beurling); RS wall kλ<2;
ceiling 0.6818312306; ξ′ 0.85838/0.92919 (Lean); Λ≥0 (Rodgers–Tao); Mertens-hypothesis
refutation (Odlyzko–te Riele). CHECKED NUMERICALLY: our 0.6733 (Arb g4000 eps=8065);
Λ≤0.22 (Polymath 15); moments ≤4; 13/84 (Bourgain). REPORTED-UNVERIFIED: any 2020–2026
κ > 0.4167 claim. CONJECTURED: λ_n positivity as a finitely-attackable certificate.
