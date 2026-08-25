# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR — FOCUS: derivative tower + literature sweep)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Spawn YOUR OWN subagents, have them research,
and SYNTHESIZE their results into ONE deliverable.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — persistence hook binds you AND all your subagents; honesty labels
   mandatory (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE).
2. Read ~/riemann/tasks/task-Q3-ladder.md, task-Q4-validator.md, task-LIT-sweep.md (the open task
   specs), and skim ~/riemann/research/notes/ladder-convergence.md, attack-xiprime2-tower.md,
   literature-sweep-simplezeros.md.

## CONTEXT (verified)
- Program open problems: P5 = the derivative tower (ξ′, ξ″, …) certificates; the "ladder" is the
  program's cumulative-verification structure; the LIT sweep is a literature sweep on simple zeros
  and related quantities.
- The certified record 0.6732628655 stands; the (α, psum) family is exhausted; ceiling 0.6818. [RETIRED 2026-08-24]

## YOUR FOCUS: (a) derivative-tower certificates and (b) the literature sweep
Subagents: (a) THEORIST/EXECUTOR: can derivatives of the completed ξ (ξ′, ξ″) yield certificate
inequalities (signed kernels from ξ′? local extrema of |ξ|? spacing of zeros of ξ′?) — probe
numerically on the first zeros (Python; modest compute) and deduce the mechanism (CONJECTURED +
CHECKED NUMERICALLY); (b) LITERATURE SWEEPER: scan the program's papers dir + notes for any
unexploited results on simple zeros, Levinson–Conrey-type mollifiers, and zero-spacing theorems that
bear on P5; produce a synthesis of the 5 most exploitable external results with exact citations.

## SPAWN 4–6 SUBAGENTS IN PARALLEL
1. THEORIST (s4h-systems): derivative-tower mechanism (ξ′, ξ″ certificates)
2. EXECUTOR (s4h-constraint): numerical probe — zeros of ξ′ vs ξ, spacing statistics, signed-kernel
   candidates (Python; script+output)
3. READER (literature): sweep ~/riemann/research/papers/ + notes for simple-zeros/mollifier results;
   top-5 exploitable with citations
4. IDEA-GEN (s4h-analogy): what do other functions' derivative towers give (e.g., Γ, Bessel, RMT
   characteristic polynomials)?
5. VERIFIER (s4h-investigation): adversarial — break any numerical claim the tower probe makes

Each subagent: read ~/riemann/hooks/agents.md first; write to
~/riemann/research/waves/wave-orch-phone/results/{subagent-name}.md; print RESULT: <status> — <one line>.

## ENVIRONMENT (cloud box or phone — adapt)
Repo at ~/riemann. Python: python3 (+ numpy/mpmath if installable). Rust only if cargo exists.
If zero data is absent, use mpmath to compute the first ~500 zeros (mpmath has zetazero) — fine.

## THEN SYNTHESIZE
Write ~/riemann/research/waves/wave-orch-phone/results/orch-tower-synthesis.md:
- The derivative-tower mechanism (CONJECTURED) + probe numbers (CHECKED NUMERICALLY)
- The top-5 exploitable literature results with citations (labels: which you actually read vs recall)
- Verdict: does the derivative tower give anything new? 
- 3 concrete next moves ranked by impact

Print at end: RESULT: <status> — <one-line summary>
