# Riemann Program

A persistent multi-agent research program attacking the **Riemann hypothesis** — and alongside it, any
rigorous, novel mathematics about ζ and its zeros.

**Operating context:** this project studies and extends the 2026 result *"More than two thirds of the zeros
of the Riemann zeta function lie on the critical line"* (Claude; Anthropic), which proved unconditionally
that ≥ 2/3 of the nontrivial zeros lie on the critical line (≥ 5/6 distinct), with optimized constant
0.6725 — improving the prior record of 41.6%.

**Charter:** `hooks/agents.md` — never-give-up search, honesty guardrails (every claim labeled
PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED; nothing counts as progress until adversarial
validators fail to break it; a wrong confident result is worse than no result), multi-agent research
protocol, and a mandatory code-backed-verification protocol (every number must come from a saved, cited
script).

## Layout

- `PLAN.md` — the plan and round structure
- `hooks/agents.md` — the persistent agent charter (binds every model, every session)
- `research/papers/` — primary sources (PDF + text)
- `research/lean-zeta-23/` — the Lean 4 formalization of the underlying result
  (upstream: https://github.com/anthropics/zeta-23-lean)
- `research/notes/` — the living research record: proof maps, verification reports, attack logs,
  idea catalogs (12+ cross-domain generators), and every documented negative
- `tools/` — numerical toolkit (Rust + Python/mpmath), each with cited run commands

## Open problems under attack

- (P1) close the in-class gap 0.6725 → 0.6818 (second-moment gap Δm₂ = 0.0093)
- (P2) break the two-moment 5/6 distinct wall (third/fourth moments, Rudnick–Sarnak range)
- (P3) form factor / pair correlation beyond α = 1 (both mean and variance functionals: documented dead
  as unconditional inputs)
- (P4) family transport (Dirichlet characters, GL(2) families)
- (P5) the derivative tower (ξ′, ξ″, …) certificates
- (P6) finite-T error terms (C∞ vs hard-cutoff kernel)

## Headline findings so far

- **In-class ceiling 0.6818… is tight** (LP dual; optimal certificate r(x) = 1 − x attains
  p₀ + 1/(6·256²) = 0.68183123; Lean-verified modulo one numerically-checked enclosure)
- **The beyond-α=1 wall is closed from every direction** (mean pair sums, variance, matrix inequalities,
  distributional/CLT inputs, the CvS theorem import, even RH itself does not move the ceiling)
- **The 2/3 deficit is arithmetic** — pair-correlation content, not method-inherent (Ihara-zeta sandbox on
  provably-RH-true objects: the certificate is a rigidity meter, not an RH-meter)
- **The 5/6 distinct wall is robust to the third moment** (identical on both worlds; the separation is a
  fourth-moment phenomenon)
- 12 cross-domain idea catalogs (physics, chemistry, control, crystallography/astronomy, music/linguistics,
  games, human systems, earth sciences, biology, ML/ecology, TCS, history-of-mathematics) + the
  history lesson: tight class limits break by *new objects*, never by sharper inequalities in the class

## Honest status

No proof of RH exists here or is claimed. The search is cumulative: every negative is a documented
finding with a script behind it. See `research/notes/` for the full record.
