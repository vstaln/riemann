# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR — FOCUS: distinct-zeros wall, 4th moment)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Spawn YOUR OWN subagents, have them research,
and SYNTHESIZE their results into ONE deliverable.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — persistence hook binds you AND all your subagents; honesty labels
   mandatory (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE).
2. Read ~/riemann/research/notes/attack-ihara-sandbox.md, paper-sixthmoment.md, attack-xiprime2-tower.md
   (skim), and the README's "5/6 distinct wall" findings.

## CONTEXT (verified)
- Known: ≥ 5/6 of nontrivial zeta zeros are DISTINCT (Weil-form compression; integrality steps
  m² ≥ 2m−1, m² ≥ 3m−2).
- Program finding: the 5/6 distinct wall is ROBUST to the third moment — identical on the provably-RH-true
  world and the generic world; the separation is a FOURTH-MOMENT phenomenon.
- Ihara-zeta sandbox exists in tools/ihara-sandbox (Rust) but may be Rust-only; you can build a Python
  analogue (small graphs, adjacency/Ihara-type operators, spectra provably on the line).

## YOUR FOCUS: does a FOURTH-MOMENT inequality break the 5/6 distinct wall?
Subagents: (a) derive the m⁴ / tr(P⁴) analogue of the integrality steps (CONJECTURED deduction);
(b) numerically probe on RH-true vs generic worlds: distinct-zero fraction, 3rd-vs-4th moment defects,
does the 4th-moment defect separate the worlds? (CHECKED NUMERICALLY, script+output); (c) if it
separates — quantify how far the distinct bound moves; if not — document the negative precisely.

## SPAWN 4–6 SUBAGENTS IN PARALLEL
1. THEORIST (s4h-systems): the 4th-moment integrality deduction sketch
2. EXECUTOR (s4h-constraint): the two-world numerical probe (Python; small graphs ≤ 1000 vertices)
3. IDEA-GEN (s4h-analogy): 3rd/4th moment structures in RMT and coding theory that produce separation
4. VERIFIER (s4h-investigation): adversarial check on the probe — does the separation survive
   independent re-implementation? (fresh code, different formulation)
5. THEORIST (s4h-cognition or s4h-constraint): what is the theoretical limit of moment-based
   separation for the distinct fraction?

Each subagent: read ~/riemann/hooks/agents.md first; write to
~/riemann/research/waves/wave-orch-phone/results/{subagent-name}.md; print RESULT: <status> — <one line>.

## ENVIRONMENT (cloud box or phone — adapt)
Repo at ~/riemann. Python: python3 (+ numpy/mpmath if installable). Rust only if cargo exists. Small compute.

## THEN SYNTHESIZE
Write ~/riemann/research/waves/wave-orch-phone/results/orch-distinct-synthesis.md:
- The 4th-moment deduction (CONJECTURED), the two-world numbers (CHECKED NUMERICALLY),
- Verdict: does the 4th moment break 5/6? How far? Or is the negative precise?
- 3 concrete next moves ranked by impact

Print at end: RESULT: <status> — <one-line summary>
