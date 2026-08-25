# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR — FOCUS: break the 0.6818 ceiling)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Spawn YOUR OWN subagents, have them research,
and SYNTHESIZE their results into ONE deliverable.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — persistence hook binds you AND all your subagents; honesty labels
   mandatory (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE).
2. Read ~/riemann/research/notes/discovery-6732629.md, attack-ceiling.md, ceiling-gram-constraint.md,
   and skim attack-vector-catalog-3.md — so you do NOT re-try the exhausted (α, psum) family or the
   documented beyond-α=1 dead ends (mean pair sums, variance, matrix inequalities, CLT inputs).

## CONTEXT (verified)
- Certified record 0.6732628655; the (α, psum) family is EXHAUSTED (true minimum of F proven: [RETIRED 2026-08-24]
  0.00806 certifies, 0.008065 fails).
- In-class ceiling 0.68183123 (LP-dual certificate r(x)=1−x; the rank–trace/Weil-compression class
  cannot exceed it).
- The program's history lesson: tight class limits break by NEW OBJECTS, never by sharper inequalities
  in the class.

## YOUR FOCUS: find NEW OBJECTS / NEW INPUTS that can move the proportion bound past 0.6818
Subagents hunt: new kernels beyond the cosine family (with better Fourier structure), new quadratic
forms/compression schemes, higher moment hierarchies (SOS/tensor lifts), new inputs from neighboring
theorems (Selberg trace, automorphic families, L-function moments, spectral theory of completed ξ),
function-field/non-Archimedean analogues (Ihara/Beurling zetas), or entirely different frameworks
(direct zero-counting functionals). A rigorous proof that the ceiling is IMPASSABLE is also a win.

## SPAWN 4–6 SUBAGENTS IN PARALLEL
1. IDEA-GEN (s4h-creativity): 10–15 CONJECTURED new-object ideas
2. IDEA-GEN (s4h-analogy): history/episode transports (Delsarte, E8/Leech, modularity, PNT)
3. IDEA-GEN (s4h-probability or network): statistical/spectral formulations that escape the class
4. EXECUTOR (s4h-constraint): numerically probe the MOST promising 2–3 candidate new objects —
   does the resulting bound move at all? CHECKED NUMERICALLY with script+output
5. THEORIST (s4h-systems): leverage analysis — which single assumption in the deduction chain, if
   replaced, would crack the class open?

Each subagent: read ~/riemann/hooks/agents.md first; write to
~/riemann/research/waves/wave-orch-phone/results/{subagent-name}.md; print RESULT: <status> — <one line>.

## ENVIRONMENT (cloud box or phone — adapt)
Repo at ~/riemann. Python: python3 (Rust only if cargo exists). Small probes fine; keep compute modest.
Do NOT edit canonical tools/ — copy to /tmp or a new dir.

## THEN SYNTHESIZE
Write ~/riemann/research/waves/wave-orch-phone/results/orch-ceiling-synthesis.md:
- Top 5 new-object candidates ranked by plausibility×novelty×impact
- Any numerical evidence the ceiling moves (exact numbers, CHECKED NUMERICALLY)
- Verdict: is the 0.6818 ceiling breakable by any candidate on the list, or does the evidence
  suggest impassability? (CONJECTURED)
- The single most promising next move

Print at end: RESULT: <status> — <one-line summary>
