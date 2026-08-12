# Li criterion probe — v3 validated (2026-08-13)

**Tool:** `tools/li_probe.py` (mpmath, formal power-series log of (s-1)ζ(s) via
Stieltjes constants, Bombieri–Lagarias substitution u = x/(1-x), closed-form
polygamma coefficients — no zeta(1) evaluation).

## Result
- λ₁ = 0.023095708966121033814… **matches the closed form** 1 + γ/2 − (1/2)log(4π)
  to all 20 digits — the pipeline is CORRECT (CHECKED NUMERICALLY).
- λ₁..λ₁₂ all positive and growing: 0.0231, 0.0923, 0.2076, 0.3688, 0.5755, 0.8276,
  1.1245, 1.4658, 1.8509, 2.2793, 2.7504, 3.2633 — consistent with RH
  (λ_n ~ (n/2)(log n + γ − 1 − log 2π) > 0).
- **Precision wall (known Keiper–Li ill-conditioning):** beyond n≈40 the values
  diverge exponentially (10²⁷ at n=148) — the series-log substitution amplifies the
  dps-limited Stieltjes constants. Deep-n positivity needs hundreds of dps + a
  stabilized recurrence (Keiper's own, or the λ_n ↔ Stieltjes Hankel form directly).

## Meaning
Li's criterion (λ_n ≥ 0 ⟺ RH) is a **moment-positivity certificate class orthogonal
to Levinson's zeros-counting**, with NO a-priori 0.6818 ceiling. The probe confirms
the numerics are feasible and trivially parallel (each λ_n independent given the
Stieltjes constants); the deep-n computation needs ~300–500 dps (python-flint's
arb / ball arithmetic on the laptop) and a stabilized recurrence. This is the
program's adopted new method (see method-frontier-synthesis.md).

## Honesty
CHECKED NUMERICALLY: λ₁ matches closed form (20 digits); λ₁..λ₁₂ positive.
CONJECTURED (standard): λ_n ≥ 0 for all n under RH; deep-n positivity is the probe.
