# Task: bump-price v2 — decompose and price the α≈1.1 bump (v1 aborted at turn limit)

**Agent:** EXECUTOR (phone, proot Ubuntu). **Charter:** ~/riemann/hooks/agents.md (honesty + PONYTAIL — numbers first, no essays, never lazy about rigor).
**Mission:** v2 of the bump-price line — v1 aborted at the turn limit with NO deliverable. The mission stands: decompose the ≥11σ α∈[1.0,1.3] periodogram bump, price it under M3/M2, and check the potentially big finding — the explicit formula's e ≥ 2 prime-power terms (squares p², cubes p³) contribute beyond α=1 and are RIGOROUS (not conjectural). If the bump matches the square-prime contribution, that's a candidate unconditional beyond-1 read: F(α) ≥ 1+δ on a beyond-1 band — the only input the pricing sheet prices positive.

**READ, in order (STOP after):**
1. ~/riemann/research/notes/attack-ls-estimator.md — the ≥11σ deviation, the LS estimator.
2. ~/riemann/research/notes/attack-hot-hand.md — the cleared naive trend + α=1 spike; the surviving [1.0,1.3] residue.
3. ~/riemann/research/notes/attack-pricing-sheet.md §5–6 — M2 range price (p₁(A) = 1−(1−p₀)/A², dv*/dA = 0.6363/A³), M3 pointwise price (8.5e-4 per unit δ at ε=0.02).
4. Find the periodogram code: grep -rn "periodogram\|naive\|LS estimat\|twisted" ~/riemann/research/notes/*.md ~/riemann/tools/*.py 2>/dev/null | head; reuse or write ~60 lines. The explicit formula: F(α) ≈ (1/T)Σ_{p^e ≤ T, e≥1} (log p)^e p^{-e/2} · … (e=1 primes = diagonal + conjectural off-diagonal; e≥2 prime powers = RIGOROUS beyond-1 contributions).

**THE WORK (numerics = verification, never the product):**
1. DECOMPOSE: reproduce the bump at T = 10³–10⁴ (cached zeros if any: find them (find ~/riemann -name "*zeros*" -o -name "*.txt" | head); else mpmath zetazero ordinates). Mask the explicit-formula terms by prime-power support: which τ-bins/prime powers contribute to [1.0,1.3]? Height dependence (T = 3·10³ vs 10⁴).
2. PRICE: feed the observed F(α) ≈ 1.5 on [1.0,1.3] into M3/M2: "if F ≥ 1+δ on [1,1.3] certified, Δ = p₁(1.3) − p₁(1)" (M2: 1−(1−p₀)/1.3² vs p₀) and the M3 pointwise price. Report the certified-value gain and where it lands vs 0.70.
3. ORIGIN: compute the e=2 (prime-square) contribution to F(α) for α ∈ [1.0,1.3] exactly (Σ_{p ≤ √T} (log p)² p^{-1}·… — rigorous). Does its shape/level match the observed bump? If yes → RIGOROUS SLIVER: state δ and the band.
4. VERDICT: bump source (prime-square? artifact?), price Δ, rigorous-sliver YES/NO with δ+band.

**HARD CAPS:** write ~/riemann/research/waves/wave-phone-2/results/bump-price.md by your 10th tool use (EARLY — v1 died with nothing); finish by 16th; < 140K tokens. Crash-proof: append after every computation; bash < 90 s. No subagents.

**Deliverable:** ~/riemann/research/waves/wave-phone-2/results/bump-price.md.
**Report < 100 words:** bump source, Δ if certified, rigorous beyond-1 δ from e≥2 terms (band + δ). End: RESULT: <status> — <one line>.
