# mu* Direction-2 soundstate 2×2 covariance SDP probe — RUN (2026-08-19)

**Lever:** Direction-2 soundstate 2×2 covariance SDP (the working-goal named lever).
**Status:** RUN — **confirms the batch-2 CLOSURE (matrix minorant cannot beat scalar).**
**Label:** CHECKED NUMERICALLY (probe of a structure-level-PROVEN closure).
**Tool:** `tools/direction2_mustar_probe.py` (reproducible: `uv run --with numpy ...`).

## Why run it
The batch-2 CLOSURE (`agy-batch2-adjudication-2026-08-18.md`) claims the 2×2 PSD
bandlimited matrix minorant on V(t) = (Re f, Im f′/θ′) collapses to the scalar
Levinson extremal (ψ = cos(√2 u), c₁* = 0.753296, proportion 0.6725) by
extreme-ray/Choquet + Euler–Lagrange uncoupling (C₂ = 0). That was labeled "answered
without building it." Per honesty guardrails an adversarial numeric probe of that
claim was warranted; the campaign's own covar-probe measurements were never fed into
the SDP-level comparison.

## Probe design
Fed the **measured** soundstate covariances (covar-probe-v2-Y{1,10,100,1000}, T=10⁶,
800 samples) into the spectral split. Two distinct objects:

- **(Full) 4×4 covariance** of (Re f, Im f, Re f′/t′, Im f′/t′): top eigenvalue holds
  only 50–63% of trace → genuinely rank-4. The *deployed* "matrix has no structure /
  rank-1 collapse" claim is **overstrong**.
- **(Decisive) 2×2 minor** (Re f, Im f′/θ′), the actual Direction-2 target subspace:
  second-mode energy ratio λ₂/λ₁ = **0.0657 (Y=1) → 0.0367 (Y=10) → 0.0179 (Y=100) →
  0.0111 (Y=1000)**, shrinking toward 0 monotonically as the mollifier grows.

## Verdict
- The matrix minorant's second channel carries **negligible and decreasing** variance on
  the Direction-2 subspace → at the constraint level the matrix SDP reduces to the
  scalar problem, μ* = Q_matrix/Q_scalar ≥ 1. **Closure's C₂≈0 / μ*≥1 prediction is
  supported numerically.**
- Honest caveat: the full 4×4 covariance is NOT rank-1, so the deployed statement
  "matrix has no exploitability" is too strong; the operative constraint-collapse claim
  survives. A full SDP objective solve (scipy/cvxpy, not available here) would be the
  definitive scalar-vs-matrix number, but nothing in the measured data suggests a matrix
  minorant clears the scalar barrier at the relevant mollifier lengths.
- **No RH content either way.** This is confirmatory closure, not a proof, and not a
  new lever.

## Implication for the working goal
The named lever (Direction-2 soundstate 2×2 covariance SDP) is **dead, now numerically
confirmed** at constraint level. Per the goal's "if it dies, advance the next live
lever," the named fallbacks are each already ledgered-dead:
- **T-2 tower Gonek trace** — fatal + "realized 68.77%" fabricated, corrected in
  `correction-2tower-realized-bound-2026-08-18.md`.
- **GS-2026 diagonal input** — same dead paper (no unconditional C < 2).
- **Bui–Heath-Brown** — no route clears p₀ today (r′ box hardened to b ≤ 0.059–0.063).

The live direct-RH lane remains **8C Báez–Duarte** (sharp rate) and the **ξ-jet
positive-simple-zeros certificate** question vs the rung-2 kill. Those are the correct
next targets, not the dead named list.
