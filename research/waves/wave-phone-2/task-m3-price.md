# Task: m3-price — the price of the m₃ = 5±ε separation (does the new class climb?)

**Agent:** EXECUTOR (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** monetize the m₃-separation discovery (superlaw-s3.md: super-law marked-windowed m₃ = 7.98 vs real zeros PROVEN 5; 256-law family position ≈ 8, pinned ≥ 5.4419). The separation EXCLUDES the super-law AND (numerically) the 256-law from the m₃ = 5±ε certificate class. The class's extremal configuration is unknown — **compute its p₁: the price of the separation.** If the m₃-pinned class optimum > p₀, the class climbs toward 70%; if ≤ p₀, we have the exact price (a documented value, not a hunch).

**Read first (STOP after):**
1. research/waves/wave-phone-2/results/superlaw-s3.md — the separation numbers (m₃(1/2): 7.98 corrected vs 5 proven; pinned bottom 5.4419; mark-moment inflation formula m₃^marked = D·(Em3/Em) + 3·Em2·A2 + Em²·A3 with D = 4−3p₀ = 1.954514, Em2/Em = 1.3182, Em3/Em = 1.9545, A2(1/2) = 7/6, A3(1/2) = 1/2 ⟹ 8.148; scripts superlaw_s3_v2.py).
2. research/notes/attack-pricing-sheet.md §3 — the m₃ ≥ 2 identity (m₂ = 2−p₁, m₃ = 4−3p₁, the −1/3 price, why the one-sided pin caps the SIMPLE cert at 2/3). **NOTE: that analysis is for the UNMARKED simple certificate reading a one-sided m₃ ≥ 2; the new read is MARKED m₃ = 5±ε (two-sided pin) on a class already stripped of super-laws — different object.**
3. research/notes/attack-law-s3.md — the marked S₃ = D + pair + T decomposition, pinned bottoms 5.4419/3.9825.
4. If rgl/64-LP machinery exists (grep tools/ and research/notes/attack-lpdual.md for "rgl", "marked-config LP", "N = 64"), reuse it; else write a self-contained ~80-line marked-config LP (positions on a grid, marks ∈ {1,2}, constraints: mean density, in-band F rows, marked-windowed m₃ = 5±ε, maximize p₁).

**The work (numerics = verification, never the product):**
1. **SET UP the marked-m₃ constraint:** for a marked config on N points, marked m₃(1/2) = tr((MG)³)/Σm with G = sinc(π(x_i−x_j)/2) (window λ=1/2), M = diag(marks). Write the constraint "marked m₃(1/2) = 5 ± ε" exactly as the LP can read it (a quadratic/cubic constraint in the marks — decide if the LP must be relaxed/linearized; if the exact constraint is nonlinear, do the honest thing: solve the LP family over a discretized ε-sweep or use the identity structure).
2. **COMPUTE the optimum:** p₁(m₃ = 5±ε) at N=64 (and N=256 if machinery exists) vs p₀(N). Report: does the pin raise, lower, or leave p₁? Give the ε-sensitivity (ε ∈ {0.1, 0.44, 1, 2.98}).
3. **THE ε-BUDGET:** the real zeros' marked m₃ = 5 is an ASYMPTOTIC (Rudnick–Sarnak); an unconditional certificate needs 5±ε with ε from explicit error terms. State what ε is needed for the class to exclude the super-law (7.98) and the 256-law (≈8) and whether the separation margins (2.98 and ~3) give room.
4. **VERDICT:** price of the separation = p₁(m₃-pinned) − p₀(N). If positive: the m₃ class is a funded climb (quantify how much of the 0.6818 → 0.70 gap it closes). If ≤ 0: documented exact price, and the honest statement of where the m₃ class caps.

**HARD CAPS:** write research/waves/wave-phone-2/results/m3-price.md by your 12th tool use; finish by 18th; < 160K tokens. Crash-proof: append after every computation. Check scipy exists (python3 -c "import scipy") before relying on it; mpmath/numpy are present. bash calls < 90 s (nohup+poll for long LP solves). Do NOT launch subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/m3-price.md — the p₁(m₃-pinned) number(s), the ε-budget statement, the verdict.
**Report (< 100 words):** the pinned-optimum vs p₀, the ε needed, the verdict. End: RESULT: <status> — <one line>.
