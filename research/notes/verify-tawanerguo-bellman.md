# VERIFICATION — tawanerguo 67.3192911473% (Bellman coboundary, third external mechanism)

**Date:** 2026-08-12 (round 3). **Status:** INDEPENDENTLY REPRODUCED (all headline numbers
match the repo's own certificates to 60+ digits). **Labels:** numbers CHECKED NUMERICALLY;
the analytic framework (imported asymptotic passage) NOT independently re-derived.

## What it is — a THIRD mechanism (not the stability ladder)

| Source | Bound | Mechanism |
|---|---|---|
| Anthropic Thm D | 0.672500703679 | rank–trace, orthogonal-atom equality case |
| ainta | 0.673008527927 | 7-point stability refinement (tr Ψ(M) ≥ 19/5000) |
| trmdy | 0.673137630699 | trig-polynomial window + weighted 7-point block |
| **tawanerguo-cn** | **0.673192911473142** | **cosine window α=1.47 + Bellman coboundary correction (block m=183)** |

tawanerguo KEEPS the paper's cosine window (H_window = 0.6724587094007293 — BELOW the paper's
H0 = 0.6725007036794116!) and lifts the final bound by a finite-memory coboundary correction:
local target F_B ≥ 577/100000, block size m = 183, pressure tax 59/19520.
gain_over_repo = +0.0001843835 (vs the paper's constant), gain_over_previous = +0.0000911268.

## What I verified (code, all reproduced)

- `tools/evaluate_coboundary_bound.py` (uv + mpmath): bound_lower = 0.6731929114731422,
  bound_upper = 0.67319291147314231 — matches README and certificate/bound-evaluation.txt.
- `tools/compute_joint_bound.py` (uv + mpmath): I0/I2/J/c_window/H_window/block_energy/
  block_defect = 1.021228785292982…/pressure/new_bound all match to 60+ digits.
- Derivative table SHA-256 035946b4368f… matches the repo's local expectation
  (source ZIP unavailable — not byte-identical, per the repo's own audit).
- Certificate trail: 64/64 boxes verified=true, tree identity 1126636−563286 = 563350,
  unresolved_terminal_cells = 0, final bound directed-MPFR.

## The transferable concept — trace-energy envelope (connects to OUR Ψ machinery)

The repo's docs/trace_energy_envelope.md is EXACTLY our stability Ψ: for G PSD m×m unit
diagonal, E = tr(G−I)² = Σ(λᵢ−1)², D = tr Ψ(G), Ψ(t) = (t−1)² on [0,2], 2t−3 beyond.
It proves a sharp branch bound: whenever E + P ≥ A (=1.02129, m=183) and P ≥ 0,
D + P ≥ Φ_m(E) with Φ_m(E) = E on [0, m/(m−1)], 2√((m−1)E/m) − 1 + E/m beyond.
That's the same Ψ as the ainta/trmdy stability discovery — confirming the stability
mechanism is a REAL shared phenomenon, not a single repo's artifact.

## The open route it names (the frontier)

NEXT_FRONTIER.md: "a global spectral-dual/Bellman subaction could reduce block-boundary
pressure loss and possibly improve the constant" — crossing block boundaries m → global.
That is the same question as our ladder-to-ceiling: does the stability/coboundary
correction CONVERGE (to p₀ = 0.6818286874638314? the 0.6818 class ceiling? something
else?) as the ladder grows / blocks merge. Current reconnaissance double precision,
NOT interval certified — not part of any theorem yet.

## Implications for the program's 1%+ goal

- Three INDEPENDENT mechanisms now beat 0.6725: stability (ainta/trmdy), coboundary
  (tawanerguo), and they share the SAME Ψ. The mechanism is real.
- All three are +0.05–0.08pp — NOT 1%+. The external race has not reached the class
  ceiling 0.6818 (which is +0.93pp over 0.6725, +0.62pp over the external best).
- The convergence question (ladder/coboundary limit) is THE live question: if the
  combined mechanism converges to p₀/0.6818, the class ceiling is the attractor and
  only beyond-1 or a new technique moves 1%+; if it overshoots, the ceiling breaks.
