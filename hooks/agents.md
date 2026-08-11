# Riemann Program — Persistent Agent Hooks

## Mission

The Riemann hypothesis (RH): every nontrivial zero of ζ(s) lies on Re(s) = 1/2.
This project pursues a proof of RH — and alongside it, any rigorous, novel mathematics about ζ and its zeros. **We never give up on the search for a proof.** The search persists across sessions, attempts, and failures; a failed attack is a documented result, not a reason to stop.

## Operative targets (each is a genuine research result)

1. Reproduce and understand the 67.25% lower-bound argument (Weil quadratic form + Sylvester inertia + rank–trace inequality) well enough to re-derive the constant 3/2 − (1/√2)cot(1/√2).
2. Verify every claim numerically against known zeta-zero data before trusting it.
3. Improve or extend: push constants, relax hypotheses, transport the technique to related problems (L-functions, simple zeros, moments).
4. Write up anything that survives adversarial review; Lean-check where feasible.

## Non-negotiables (honesty guardrails)

1. Never fabricate a proof, lemma, or numerical result. No exception.
2. Every claim is labeled: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED.
3. Nothing counts as progress until adversarial validators fail to break it.
4. Never weaken a validator to make a result pass.
5. A wrong, confident result is worse than no result — it poisons the whole search.

## Method: multi-agent research protocol

Each round: PLANNERS decompose the problem → EXECUTIONERS attack components → VALIDATORS (adversarial) try to break every claim → JUDGES score surviving pieces → SYNTHESIZER merges → CRITIQUE LOOP repeats until no movement. Numerical checks against known zeros are mandatory for any analytic claim.

## Skills: skills-for-humanity (s4h)

Reference: https://github.com/human-avatar/skills-for-humanity (install: npx @human-avatar/skills-for-humanity).
Apply the underlying methods even where plugin commands are unavailable:
- epistemology (evidence weighting, belief updating — what counts as progress)
- investigation (hypothesis generation and testing)
- logic (argument mapping, finding holes)
- constraint (turn RH's structure into constraints)
- creativity + analogy (transfer methods from other problems)
- strategy (which attack to fund; kill criteria)

## Standing research context

- RH: open since 1859 (Millennium Prize).
- Record lower bound on the proportion of zeros on the critical line: 41.6% → 67.25% (Anthropic research model, 2026; verified by Conrey & Goldston; Lean-formalized in anthropics/zeta-23-lean). Anthropic does not expect those techniques to settle RH.
- Clean constant: 3/2 − (1/√2)·cot(1/√2) ≈ 0.6725; simpler argument gives 2/3.
- Prior chain: Levinson (1974) ≥ 1/3 → Conrey (1989) 40% → Bui–Conrey–Young (2011) 41.05% → Feng (2012) 41.28% → ... → 41.6% → 67.25%.
- Key inputs: Bombieri (2000); Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (arXiv:2306.04799, 2501.14545); Montgomery pair correlation (1973).

## Workspace

- /home/vstaln/riemann — root
- research/papers/ — primary sources (.pdf + .txt)
- research/lean-zeta-23/ — Lean formalization
- research/notes/ — proof map, literature map, verification reports, attack log
- tools/ — numerical toolkit (Python + mpmath)
- PLAN.md — the plan; hooks/agents.md — these hooks
