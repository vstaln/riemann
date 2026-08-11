# Round 1 — Multi-Agent Attack Brief (persistent)

> Written by the orchestrator. Every agent in Round 1 must read this + hooks/agents.md
> before working. Round status tracked in research/notes/round-1-log.md.

## The problem we are attacking

The Riemann hypothesis. We have in hand a verified new-record result: **≥ 67.25% of zeros of ζ lie on the critical line** (Anthropic, 2026; Lean-formalized in research/lean-zeta-23). The operative goal of THIS round: attack the extension points — push constants, relax hypotheses, transport the technique — and adversarially validate everything.

## Honesty guardrails (bind on every agent)

1. Never fabricate a proof, lemma, or numerical result. No exception.
2. Every claim labeled: **PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED**.
3. Nothing counts as progress until adversarial validators fail to break it.
4. Never weaken a validator to make a result pass.
5. A wrong, confident result is worse than no result.
6. Keep trying: a failure is a documented result. Only honesty guardrails can stop a line of work.

## The method (67.25% argument, skeleton — for orientation only; the proof map is being built by another agent)

Weil/Guinand explicit formula → restrict to a finite-dimensional space via vectors
v_ρ[k] = φ̂_T(γ_ρ − T − (T/N)k) built from a test function φ_T ≈ ψ(x·T/N), ψ(u) = cos(√2u)·1_{|u|≤1/2}
→ compressed form W_T = (T/(N∫φ²))·Σ ord_ρ·v_ρ·v_ρᵀ (real symmetric; on-line zeros give positive squares, off-line pairs give hyperbolic (1,1) planes) → Sylvester inertia + rank–trace inequality (Lemma 3.4: rank A ≥ 2trA + 4trB − 4n₊(B) − ‖A+B‖²_HS) → analytic computation: tr W_T = (1+o(1))·N(T); ‖W_T‖²_HS = (1/2 + (1/√2)cot(1/√2) + o(1))·N(T) via Montgomery–Vaughan off-diagonal control + the variational identity for ψ → **3/2 − (1/√2)cot(1/√2) ≈ 0.67250…**, and 2/3 via the simpler argument; ≥ 5/6 distinct; ≥ 2/3 simple; Dirichlet L-function analogues (Theorems A–E).

Key constants: c₁* = √2·tanϑ/(1+ϑ·tanϑ), ϑ=1/√2; 2 − 1/c₁* = 0.6725007036794116…

## s4h skill methods to APPLY (summarized; the full skill library is at ~/.claude/skills/s4h-*)

- **epistemology** (epistemic status): inventory every claim you make; label KNOW (PROVEN) / BELIEVE (CHECKED NUMERICALLY) / ASSUME (CONJECTURED) / HOPE (CONJECTURED) / UNKNOWN. Trace which confident claims rest on shakier foundations.
- **investigation** (claim decomposition, counter-hypothesis, triangulation): decompose big claims into testable pieces; for each, actively try to DISPROVE it; verify numerically by ≥2 independent methods when feasible.
- **logic** (argument validation, consistency): find holes; state the weakest link explicitly.
- **constraint** (hardness-testing, rule-inversion, scope-reduction): classify constraints as hard/soft/assumption. Test whether the "bandwidth-one ceiling" is a real barrier. Invert "we can't do X" into "what would X require".
- **creativity + analogy** (domain-transfer, structure-mapping, provocation): map the structure of this problem onto other domains — function fields (RH PROVED there by Weil/Deligne: what structure imports?), random matrix theory, other L-functions, spectral theory, orthogonal polynomials, statistical mechanics, Landau–Siegel zeros, mollifier methods (Levinson/Conrey/Feng), moment methods. What solved-problems have the same shape?
- **strategy** (terrain, force economy, victory, kill criteria): map the terrain; decide which angle to fund; state explicit kill criteria (when you'd abandon an angle); victory = a verified, adversarial-validated result, however small.

## Sources

- research/papers/anthropic-informal-note.txt — the terse full proof (read this first; it is the ground truth skeleton)
- research/papers/claude-riemann-paper.txt — the paper
- research/papers/claude-appendix.txt — technical appendix
- research/papers/baluyot-etal-2306.04799.txt, bgst-2501.14545.txt — arXiv inputs (read fully; they're small)
- research/lean-zeta-23/README.md — Lean theorem map (read it, not the .lean files)
- research/notes/proof-map.md, literature-map.md — being produced by parallel agents; check if present

## Compute discipline (this machine is compute-poor)

- CPU-bound work → **Rust** (toolchain: ~/.cargo/bin, stable 1.97.1). Python/mpmath is far too slow.
- Data: LMFDB zeros cached at tools/data/zeros_1_1000.txt (verified, 34 digits). index.db at ~/Downloads/index.db (SQLite: zero counts N(t) for heights 14…1e11 — great for Riemann–von Mangoldt checks). Rust Riemann–Siegel (Euler–Maclaurin ζ) can compute any additional zeros locally.
- Network fetches: LMFDB REST https://www.lmfdb.org/zeros/zeta/list?N=<start>&limit=<count> — chunk ≤1000, delay ≥0.4s, or get captcha'd.
- Run a computation only if it changes what we believe. Cache everything.

## Deliverables

Each agent writes research/notes/<your-file>.md and reports back: 8–12 lines — what you tried, what you found (with labels), the single most promising next step.
