# Task: ANALOGY ENGINE — Delsarte/LP and random-matrix transplants for the zero-proportion problem

You are a THEORIST in the Riemann swarm. Context, verified:
- Certified record 0.6732628655 (67.33% of nontrivial zeros on the critical line), in-class ceiling 0.68183123, family exhausted.
- The program's unified bound model: bound = (H − τ)/(1 − B/m) with H = 2 − 1/c, c = I₀²/(I₂+J) for the cosine window, B = Φ_m(ε(m−6)), τ = psum·(m−6)/m. The ceiling certificate r(x) = 1 − x is an LP-dual object.
- The rank–trace + Sylvester (1,1)-block argument compresses Weil's Hermitian form; Montgomery's second moment is the input on the prime side.
- Your program's prior findings: the beyond-α=1 wall is closed from every direction tried; the 2/3 deficit is arithmetic (pair-correlation content), the certificate is a "rigidity meter".

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md (charter, honesty labels, Rust-first rule).
2. Read ~/riemann/research/notes/discovery-6732629.md, attack-ceiling.md, mine-openai-spherepacking.md, attack-cvs-import.md (skim).
3. Read the s4h-analogy and s4h-creativity-lateral-thinking skills if present.

## Your task
Two deep analogy transplants, worked to the level of a CONCRETE probe:

**A. Delsarte-style LP on the zero-proportion problem.** Delsarte's linear programming bound (coding theory / sphere packing) proves optimality of tight designs by exhibiting a dual witness. The ceiling certificate r(x) = 1 − x is already LP-dual-like. Investigate: what is the FULL LP (or SDP) whose optimum is 0.6818, what are its constraints, and what does the next-higher relaxation (more variables, more constraints) bound? Numerically solve the k-th Delsarte-style relaxations for k = 2,3,4 on the actual functional and report whether the bound sequence converges to 0.6818 or jumps above it (a jump above = a path past the ceiling). Label each number CHECKED NUMERICALLY with script+command.

**B. Random-matrix transplant.** In RMT, the proportion of eigenvalues on the "critical line" analogue is governed by level repulsion (GUE). The pair-correlation content is what makes the deficit arithmetic. Investigate: model the compressed Weil form as a finite random Hermitian operator whose spectral statistics match Montgomery/Odlyzko. Compute (in Rust, or uv python if small) the analogue of the proportion bound for the GUE and for the "generic" ensemble with Poisson statistics. Question: does the RMT analogue predict the 0.673 → 0.6818 gap, and does it suggest which statistic (3rd/4th moment, spacing distribution) carries the information that moves it?

## Deliverable
Write ~/riemann/research/waves/wave-phone-local/results/analogy-lp-rmt.md:
- The Delsarte-relaxation experiment with exact numbers (CHECKED NUMERICALLY, script + command + output),
- The RMT analysis with exact numbers (CHECKED NUMERICALLY),
- Verdict: does either path get past 0.6818? (CONJECTURED where extrapolated),
- 3 concrete next probes ranked by impact.

Print at end: RESULT: <status> — <one-line summary>
