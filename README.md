# Riemann Program

> ## 🏆 Current certified record (2026-08-23)
>
> **N₀(T)/N(T) ≥ 0.6735471309049393** — the proven proportion of nontrivial zeros of ζ(s) that are
> simple and lie on the critical line (κ* = liminf N₀ˢ/N). This **exceeds the 0.6725 constant of the
> 2026 Anthropic/Claude result** ("More than two thirds…", Montgomery–Taylor window) by +1.05×10⁻³.
>
> Certificate: eps = 0.0079 block-inequality floor, verified by Arb interval-arithmetic branch-and-bound
> with Gershgorin convexity certificates (27,679,928 nodes, sound prune paths only).
> Parameters: α = 1.4263026187858052, λ = 1.351623997475116, raw_p/raw_q in
> `research/papers/main.tex` §5. Paper: **`research/papers/main.pdf`** (17 pp, compiled from `main.tex`).
>
> Also certified this week: ζ′ zero-free on σ∈[0.001,0.49] for t∈[10,175,000] (Speiser lane) ·
> Li λₙ > 0 for n ≤ 10⁶ · Robin σ(n) bound clean through n = 10⁶⁰.
> RH itself remains open; every claim carries printed error budgets and planted-zero false controls.


A persistent multi-agent research program attacking the **Riemann hypothesis** — and alongside it, any
rigorous, novel mathematics about ζ and its zeros.

> **Transparency note.** This repository is a *work in progress*, not a finished paper. It documents a
> research process: a team of parallel AI agents (dispatched and orchestrated by **DeepSeek V4 Pro running
> on Command Code**, with the agent roles ported from the pi coding agent setup), set the task of independently
> reproducing, verifying, and extending the 2026
> Anthropic result below — the way one would test a new model against a known hard benchmark. Nothing here
> is a claimed proof of the Riemann hypothesis, and no claim here should be read as a peer-reviewed result.
> Every note is honest about its status (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED /
> INCONCLUSIVE), and the whole record — including the failures, the dead ends, and the walls — is public on
> purpose. The underlying result being tested is the LLM-produced paper by Claude (Anthropic); the test
> harness is DeepSeek V4 Pro on Command Code.

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
