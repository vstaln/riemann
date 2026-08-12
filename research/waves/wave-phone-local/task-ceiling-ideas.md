# Task: NEW-OBJECT IDEATION — break the 0.6818 ceiling

You are an IDEA GENERATOR in the Riemann swarm. Context, verified:
- The certified record is 0.6732628655 (67.3263% of nontrivial zeros on the critical line), α=1.49, psum=1/220, m=133, floor F≥0.00806.
- The (α, psum) family is EXHAUSTED: the leader sits at the true minimum of the F functional (0.00806 certifies, 0.008065 fails). Sharp boundary proven.
- The in-class ceiling is 0.68183123 (LP dual, certificate r(x)=1−x attains p₀ + 1/(6·256²); Lean-verified modulo one numerically-checked enclosure). The whole rank–trace/Weil-compression class CANNOT exceed it.
- The program's history lesson (research/notes/): tight class limits break by NEW OBJECTS, never by sharper inequalities in the class. The beyond-α=1 wall is closed from every direction tried (mean pair sums, variance, matrix inequalities, CLT inputs, even RH itself does not move the ceiling).

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md (charter + honesty labels).
2. Read ~/riemann/research/notes/attack-ceiling.md, ceiling-gram-constraint.md, discovery-6732629.md, and skim attack-vector-catalog-3.md so you DO NOT duplicate already-tried ideas.
3. Skim the s4h skill catalogs if present (analogy, constraint, history-of-mathematics) for cross-domain routes.

## Your task: produce 10–15 CONJECTURED ideas for objects/mechanisms OUTSIDE the exhausted class that could move the proportion-of-zeros-on-line bound past 0.6818 — or, failing that, ideas that provably PROVE the ceiling cannot be passed (a rigidity result is also a contribution).

STRICT FILTER: parameter tweaks of the cosine family, bigger m, better ε — all forbidden. Each idea must introduce a NEW OBJECT or NEW INPUT, e.g.:
- new kernels/weights not in the cosine family (families with different Fourier-decay or sign structure)
- new quadratic forms or new compression schemes of the Weil form (different moment hierarchies, tensor/SOS lifts)
- new inputs from neighboring theorems (Selberg trace, automorphic/L-function families, moments of L-functions, Ratios conjecture-free inputs, spectral theory of the completed ξ)
- non-Archimedean or function-field analogues (Ihara/Beurling zetas) whose provably-RH-true structure leaks a certificate
- transport from other "tight class limit broken by new object" episodes in mathematics history (Delsarte/LP in coding theory, sphere packing 8D/24D, circle method, modularity, Perron–Frobenius…)
- completely different frameworks: no compression at all, direct inequalities on N₀/N via zero-counting functionals

For EACH idea write: (a) the object/input in one paragraph, (b) why it could move the ceiling (mechanism), (c) the most likely way it fails, (d) the cheapest numerical probe to test it in < 2 hours, (e) plausibility×novelty score (1–10 each).

## Deliverable
Write ~/riemann/research/waves/wave-phone-local/results/ceiling-ideas.md — the ranked list (top 5 highlighted), each labeled CONJECTURED, with the cheapest probes.

Print at end: RESULT: <status> — <one-line summary of the top idea>
