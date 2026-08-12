# Task: bump-price — decompose and price the α≈1.1 empirical beyond-1 bump

**Agent:** EXECUTOR (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** the program's one real unexplained empirical deviation: ≥ 11σ at α ∈ [1.0, 1.3] in the periodogram under both naive and LS estimators (attack-ls-estimator.md, attack-hot-hand.md). Decompose it (τ-bins, prime-power support, height dependence), then price the observed F(α) ≈ 1.5-level bump under the M3/M2 models: what would it be worth if certified, and can it be traced to a prime-arithmetic origin (a candidate for a real provable sliver)?

**Read first (STOP after):**
1. ~/riemann/research/notes/attack-ls-estimator.md — the ≥11σ deviation, the LS estimator.
2. ~/riemann/research/notes/attack-hot-hand.md — the naive-trend and α=1 spike verdicts (the surviving residue is the [1.0,1.3] bump).
3. ~/riemann/research/notes/attack-pricing-sheet.md §5–6 + .py — the beyond-1 price models: M2 range model p₁(A) = 1−(1−p₀)/A² (dv*/dA = 0.6363/A³), M3 free-mass model (8.5e-4 per unit δ at ε = 0.02), the pointwise price (δ ≈ 21 needed per the sheet's own lesson).
4. The periodogram code: find it (grep -rn "periodogram\|naive\|LS estimat" ~/riemann/research/notes/*.md ~/riemann/tools/ 2>/dev/null | head) — reuse whatever exists; else write your own ~60-line periodogram (the explicit formula: F(α) ≈ (1/T)Σ_{p^e ≤ T} (log p)^e p^{-e/2} ... the standard normalized pair-correlation periodogram).

**The work (numerics = verification, never the product):**
1. **DECOMPOSE:** reproduce the bump with the periodogram code at the existing height(s); then mask the explicit-formula terms by prime-power support (τ-bins: which prime powers p^e with p^e ≤ T contribute to which α-band?) and by height windows (T = 3·10³, 10⁴, 3·10⁴ — use the cached zeros if present; else 10³). Report where the bump's mass lives.
2. **PRICE IT:** feed the observed F(α) ≈ 1.5 on [1.0,1.3] into the M3/M2 models: exact statement — "if F ≡ 1+δ on [1,1.3] were certified, the beyond-1 certificate buys Δ = …" (use the M2 range price p₁(1.3) − p₁(1) and the M3 pointwise price). Give the certified-value gain for the observed bump and the margin to 70% (does 1.3 buy more than 1.04's 0.70?).
3. **ORIGIN CHECK:** is the bump consistent with a prime-power/arithmetic source (e.g., squares p² or cubes p³ contributions — the explicit formula has e ≥ 2 terms that ARE beyond-1 and NOT conjectural)? If the bump's shape matches the square-prime contribution, that is a candidate for a REAL, PROVABLE sliver of beyond-1 structure (the e≥2 terms are rigorous). This is the potentially big finding: **the prime-square terms give a rigorous F(α) ≥ 1 + δ on a beyond-1 band — an unconditional beyond-1 read.**
4. **VERDICT:** bump = real/artifact; price = Δ; rigorous sliver = YES/NO with the δ and band if yes.

**HARD CAPS:** write ~/riemann/research/waves/wave-phone-2/results/bump-price.md by your 12th tool use; finish by 18th; < 160K tokens. Crash-proof: append after every computation; bash < 90 s. mpmath/numpy present; scipy check first. No subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/bump-price.md — the decomposition, the price Δ, the prime-square sliver verdict.
**Report (< 100 words):** bump source, Δ if certified, whether the e≥2 explicit-formula terms give a rigorous beyond-1 δ. End: RESULT: <status> — <one line>.
