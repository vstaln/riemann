# Task: Mini-Orchestrator — run your own subagent swarm (ROLE: ORCHESTRATOR — FOCUS: finite-T error terms)

You are a MINI-ORCHESTRATOR agent in the Riemann swarm. Spawn YOUR OWN subagents, have them research,
and SYNTHESIZE their results into ONE deliverable.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — persistence hook binds you AND all your subagents; honesty labels
   mandatory (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE).
2. Read ~/riemann/research/notes/attack-finitet.md, attack-finitet-cinf.md, discovery-6732629.md
   (skim), and the README's open problem P6.

## CONTEXT (verified)
- The certified record 0.6732628655 uses the C∞ cosine kernel v(s)=cos(1.49·s) on [−1/2,1/2] with [RETIRED 2026-08-24]
  pressure psum=1/220 and block m=133; bound=(H−τ)/(1−B/m), H(1.49)=0.6724218860964.
- Open problem P6: the finite-T error terms differ between C∞ kernels and hard-cutoff kernels.
  The program has notes on finite-T behavior (attack-finitet*, finitet-cinf) — read them to learn
  what's already known and what the open questions are.

## YOUR FOCUS: quantify and tighten the finite-T error terms for the record argument
Subagents: (a) read the existing finite-T notes and extract the exact error-term structure used in
the 0.67326 certificate (what O(·) terms are dropped, what the T-dependence is); (b) numerically
probe the finite-T vs T→∞ gap for the cosine window on moderate T (CHECKED NUMERICALLY: compute the
windowed zero-count functionals for the first 10⁴–10⁶ zeros if data is available, else a model
functional; script+output); (c) determine whether any dropped finite-T term could flip the certified
constant at accessible T (i.e., is the certificate robust?) — and (d) whether a hard-cutoff kernel
with better finite-T control could beat α=1.49 cosine.

## SPAWN 4–6 SUBAGENTS IN PARALLEL
1. READER/THEORIST: extract the exact error-term structure from the finite-T notes
2. EXECUTOR (s4h-constraint): numerical probe of the finite-T gap (Python; modest compute)
3. IDEA-GEN (s4h-analogy): how other analytic-number-theory bounds handle finite-T (e.g., Selberg,
   Levinson–Conrey mollifiers, standard zero-density proofs)
4. VERIFIER (s4h-investigation): adversarial — can you find a T where the dropped terms matter?
5. THEORIST (s4h-systems): which finite-T term, if controlled better, most helps the constant?

Each subagent: read ~/riemann/hooks/agents.md first; write to
~/riemann/research/waves/wave-orch-phone/results/{subagent-name}.md; print RESULT: <status> — <one line>.

## ENVIRONMENT (cloud box or phone — adapt)
Repo at ~/riemann. Python: python3 (+ mpmath/numpy if installable). Rust only if cargo exists.
Zero data may not be present — if not, use a model functional and say so. Small compute.

## THEN SYNTHESIZE
Write ~/riemann/research/waves/wave-orch-phone/results/orch-finitet-synthesis.md:
- The error-term structure extracted from the notes (labeled)
- The finite-T probe numbers (CHECKED NUMERICALLY, script+output)
- Verdict: is the 0.67326 certificate robust to finite-T? Does a hard-cutoff kernel help?
- 3 concrete next moves ranked by impact

Print at end: RESULT: <status> — <one-line summary>
