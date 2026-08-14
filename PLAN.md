# Riemann Program — Plan

## Situation (verified)

- RH (all nontrivial zeros on Re(s)=1/2) is open since 1859. Millennium Prize.
- Anthropic's unreleased research model, given "take a real stab at RH", did NOT solve it but proved a new record: ≥ 67.25% (and ≥ 2/3 by a simpler argument) of nontrivial zeros lie on the critical line; ≥ 5/6 are distinct; previous record 41.6%. Verified by Conrey & Goldston; Lean-formalized (anthropics/zeta-23-lean).
- Method: finite compression of Weil's Hermitian form; Sylvester's law of inertia ((1,1) blocks for off-line pairs {ρ, 1−ρ̄}); rank–trace inequality via von Neumann's trace inequality; integrality steps m² ≥ 2m−1, m² ≥ 3m−2; Montgomery's prime-side pair-correlation second moment (unconditional, bandwidth ≤ 1). Analytic inputs: BGSTB24 (arXiv:2306.04799), Goldston–Suriajaya (arXiv:2501.14545), Bombieri (2000).
- Anthropic: "We don't expect that the techniques Claude used will lead to proving the Riemann hypothesis."

## Our goal

Long-term: prove RH. Operative near-term targets (each a genuine research result):
1. Reproduce & understand the 67.25% argument (proof map) — done when we can re-derive 3/2 − (1/√2)cot(1/√2) from the method.
2. Verify numerically everything we can (zero data, moment computations, signature/rank checks on the compressed Weil form).
3. Attack the extension points: improve constants (67.25% → ?), relax hypotheses, transport to related problems (L-functions, simple zeros, moments, distinct zeros).
4. Anything rigorous that survives adversarial validation gets written up; Lean-check where feasible.

## Pipeline (per user request; adapted to this harness)

Round structure: PLANNERS (decompose) → EXECUTIONERS (attack components) → VALIDATORS (adversarial, try to break) → JUDGES (score) → SYNTHESIZER (merge) → CRITIQUE LOOP (repeat). Numerical checks against known zeros are mandatory for any claim. Hooks: hooks/agents.md (persistent charter).

## Workspace

- research/papers/*.pdf/.txt — primary sources
- research/lean-zeta-23/ — Lean formalization
- research/notes/ — proof map, literature map, verification reports, attack log
- tools/ — numerical toolkit (Rust-first; legacy Python + mpmath where already certified)
- hooks/agents.md — persistent agent hooks

## Honest constraints

- This harness runs a handful of real agents per round (not 60), with bounded budgets. Many rounds over the session.
- Proofs require correctness, not just volume. Every output is judged by adversarial validators; fabricated results are the #1 failure mode and are forbidden.
- We will not claim success we don't have. Progress = verified results, recorded honestly.
