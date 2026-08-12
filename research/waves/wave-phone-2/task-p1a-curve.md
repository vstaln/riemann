# Task: p1A-curve — the exact conditional roadmap (extended-row LP, public data only)

**Agent:** EXECUTOR (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** compute the exact p₁(A) curve from the marked-config LP with BEYOND-1 rows — the sharpened form of the paper's Remark roadmap (0.70@1.04, 0.80@1.26, 0.90@1.70, conjectural/conditional). The f1curve wall says rows up to A = 511/256 ≈ 1.9961 are legal LP data; the exact curve needs NO private family (idea 4 of ceiling-ideas.md). Output: p₁(A) at A ∈ {1.0, 1.03, 1.26, 1.70, 1.99} at N=64, compared with the M2 model p₁(A) = 1 − (1−p₀)/A².

**Read first (STOP after):**
1. ~/riemann/research/notes/attack-f1curve.md — the bandwidth-2 wall (A ≤ 511/256 feasible, ≥ 2 infeasible), the M2 curve p₁(A) = 1−(1−p₀)/A², the first-period Parseval identity, the p₁ = 2−383.5/256 = 0.50195 floor.
2. ~/riemann/research/notes/attack-lpdual.md + tools/lpdual/ — the marked-config LP machinery (N=64 or N=256); law_data.json has exact near-CUE masses s_mid[i] = (i+1)/65536, p₀ = 0.6818286874638315, E(1) = −2.5431315104e-06, D1 = 0.8239531607. **Marks are PRIVATE — you do not need them: the LP's optimum as a function of A is the curve.**
3. ~/riemann/research/notes/attack-pricing-sheet.md §5–6 — the beyond-1 price dv*/dA = 0.6363/A³ (M2 model).

**The work (numerics = verification, never the product):**
1. **Set up the extended-row LP** at N=64 (reuse tools/regen_law/lp_smallN.py's VALID gen_family s_c = N−2d — NOT common.py's buggy gen_family_vec) with rows j/N for j up to 2N (A = j/N ≤ 2). The rows are the certified F rows on [0, A]; the certificate's test function r now has support [0, A].
2. **Compute p₁(A)** at A ∈ {1.0, 1.03, 1.26, 1.70, 1.99} (watch the wall at 1.996 — report behavior AT the wall). Compare with the M2 model 1 − (1−p₀)/A² and with p₀(64).
3. **The roadmap:** state the exact conditional statement: under Montgomery's pair-correlation conjecture (F ≡ 1 on [0,A]), certified simple-on-line fraction = p₁(A) + 1/(6N²). Give the A needed for 0.70, 0.75, 0.80 (interpolate the curve).
4. **VERDICT:** does the extended-row curve match M2 within 1.1% (as f1curve §4 saw)? Is the 0.70@1.04 roadmap confirmed on public data?

**HARD CAPS:** write ~/riemann/research/waves/wave-phone-2/results/p1a-curve.md by your 12th tool use; finish by 18th; < 150K tokens. Crash-proof: append after every computation; bash < 90 s (nohup+poll long LP solves). scipy/HiGHS check first (python3 -c "import scipy"). No subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/p1a-curve.md — the p₁(A) table, the roadmap A-values, the M2 agreement verdict.
**Report (< 100 words):** the p₁(A) numbers, A needed for 0.70, M2 agreement. End: RESULT: <status> — <one line>.
