# Task: INDEPENDENT VERIFIER — break or confirm the 0.6732628655 record [RETIRED 2026-08-24]

You are an ADVERSARIAL VERIFIER in the Riemann swarm, running from a fresh, independent context.
Your job is to TRY TO BREAK the certified claim below — not to reproduce it by copying code.
If you cannot break it, you confirm it with your own independent implementation.

## The claim under attack (from the swarm's record, 2026-08-12)
The certified lower bound liminf_{T→∞} N₀ˢ(T,2T)/N(T,2T) ≥ **0.673262865534356014645368000853343519319712248** [RETIRED 2026-08-24]
was obtained with:
- Window: cosine kernel v(s) = cos(α·s) on [−1/2, 1/2], α = 1.49
- Pressure: p = 1/1320 per gap, total psum = 6/1320 = 1/220
- Block size: m = 133
- Certified local floor: F ≥ 0.00806 (claim: 0.008065–0.00807 FAIL, boundary is sharp)
- H(α=1.49) = 0.6724218860964 (analytic J formula == kink-split quadrature to 1.7×10⁻⁴¹)
- Bound formula: bound = (H − τ)/(1 − B/m), τ = psum·(m−6)/m, B = Φ_m(ε(m−6)) = 2√((m−1)A/m) − 1 + A/m, A = ε(m−6), ε = the certified floor F.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — the honesty guardrails bind you. Every number you report must come from a script you ran.
2. Read ~/riemann/research/notes/discovery-6732629.md (if present) ONLY for the specification, NOT to copy any verifier code.
3. DO NOT read or copy any existing verify_cos7.py / cert_floor_*.py implementation. The point is independence: your implementation must be built from the math spec below, from scratch.

## What to do
1. **Independent re-implementation of the floor certificate.** Implement a rigorous interval-arithmetic checker (Arb via python-flint if available, else mpmath with strict directed rounding, else Rust) for the claim: for the cosine window with α = 1.49 and per-gap pressure p = 1/1320, the minimum of the 6-gap functional F over the certification domain satisfies F ≥ 0.00806. Certify with a finite grid + rigorous second-derivative bounds (or an equivalent rigorous scheme YOU design). Decide: does ε = 0.00806 certify? Do ε = 0.008065, 0.00807 fail?
2. **Independent H-window computation.** Compute H(1.49) with your own quadrature, handling the |s−t| kink by splitting the integration domain. Compare to 0.6724218860964.
3. **Re-derive the final bound** from (H − τ)/(1 − B/m) with your own arithmetic (high precision, ≥ 60 digits).
4. **Attack the logic**: are there holes in the deduction chain itself (the (1,1)-block Sylvester argument, the rank–trace step, the pressure accounting)? List any step you could not independently justify.

## Deliverable
Write ~/riemann/research/waves/wave-phone-local/results/verify-record.md containing:
- Verdict: **PROVEN** (with your independent numbers) or **BROKEN** (with the exact discrepancy) or **INCONCLUSIVE** (with the blocker)
- Every number with the exact script path + command + output
- The list of deduction steps you could NOT independently justify (if any)

Print at end: RESULT: <PROVEN|BROKEN|INCONCLUSIVE> — <one-line summary>
