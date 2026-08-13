# Task: n-point generalization — the structural lever to break 0.6734 (EXECUTOR — top priority)

You are an EXECUTOR agent in the Riemann swarm. This is the highest-value structural task: the
rank-trace family is maxed at ~0.6734 (theorist-ceiling.md, PROVEN). The one untested lever that
CHANGES THE STRUCTURE is the n-point generalization: more than 7 points (more gaps) in the local
functional.

## MANDATORY first steps
1. Read /home/vstaln/riemann/hooks/agents.md — persistence hook: NEVER give up; failures are documented results.
2. Read /home/vstaln/.pi/agent/skills/s4h-constraint/SKILL.md and s4h-investigation/SKILL.md.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md and /home/vstaln/riemann/research/waves/wave-local/results/theorist-ceiling.md (the ceiling analysis: family max ~0.6734212, eps is binding).

## THE CONTEXT
- Record: bound 0.6732628655343560, alpha=1.49, psum=1/220, m=133, eps=0.00806, n=7 (6 gaps).
- The n-point generalized deduction (from trmdy's proof, research/ladder-f-family/threshold.py):
  F_n(g) = p·sum g_i + sum_{i<j} a_ij·w(y_j-y_i) >= eps (all g >= 0), uniform weights a_ij = 2/(n-(j-i)),
  span capacities exactly 2.
  Block of m consecutive simple zeros, q = n-1 gaps: A = eps·(m-q), R = A if A<=1 else 2·sqrt(A)-1,
  eta = R/A, B_p = q·p = (n-1)·p, bound = (m·H - eta·B_p·(m-1))/(m - R).
- The theorist says: eps is the binding constraint (H and m are exhausted). If n-point can certify a
  HIGHER eps at the same psum, the bound rises.

## YOUR TASK (RUST-FIRST)
1. Read research/ladder-f-family/threshold.py fully — understand the n-point bound formula exactly.
2. Build a Rust tool (new dir /home/vstaln/riemann/tools/npoint-sweep/) that implements:
   - The n-point bound(n, eps, m, alpha, p) for n in {7, 8, 9, 11, 13, 15}
   - The required eps to beat 0.6732628655343560 for each (n, m, alpha, psum)
   - The constrained ceiling: with eps = kappa(p)·p (kappa ~ 10.7 from the F6 minimizer, CONJECTURED
     to hold for n-point too), what's the max bound over (n, m, alpha, psum)?
3. Report: for which n does the bound meaningfully exceed 0.67342? What eps would be needed?
4. CRITICAL: the n-point eps floor F_n's infimum is NOT the same as the 7-point F6 infimum. If the
   n-point infimum is LOWER per point (more constraints to satisfy), the gain is illusory. Estimate
   the n-point infimum for n=9, 11 numerically (quick float grid search in Rust) to check whether
   eps at n=9+ is still achievable at psum ~ 1/220.

## Deliverable
Write /home/vstaln/riemann/research/waves/wave-local/results/exec-npoint.md:
- The n-point bound formula (exact, from threshold.py)
- The Rust tool location + how to build/run
- The table: for each n, max bound over (m, alpha, psum) with eps achievable, and the eps needed
- The n-point infimum estimates (CHECKED NUMERICALLY — cite script+command)
- Conclusion: is n-point a real path past 0.6734? (honest — if the infimum drops, say so)
Print at end: RESULT: <status> — <one-line summary>
This is the structural question the whole swarm needs answered: can MORE POINTS in the local
functional certify a higher eps and break the family ceiling? Be rigorous and honest.