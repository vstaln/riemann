# m₃-min-frontier — certificate value over the m₃ = 5±ε class (T-frontier)

**Agent:** EXECUTOR (phone, proot Ubuntu) · **Charter:** hooks/agents.md (honesty + PONYTAIL).
**Mission file:** task-m3-min-frontier.md. **Status:** WORK IN PROGRESS — crash-proofed; appended after every computation.

## §VERDICT — EARLY (identity + zeros-read level; LP pending)

**THE T-RANGE [−3.93, −0.44] IN m3-PRICE IS NOT REALIZED BY THE ZEROS — IT IS THE IDENTITY-DERIVED WINDOW FOR MARKED p₁ = 0.70 CONFIGS, AND IT HAS THE WRONG SIGN FOR THE REAL ZEROS' CONNECTED PART.**

1. **Real zeros' connected part T = m₃ − D − pair, computed directly (this session, `scripts/m3_min_frontier.py`):**
   - N=64 blocks: T ∈ **[+0.272, +0.427]**, mean +0.367 (156 blocks, zeros 1–10000, theta/π unfolding, sinc kernel λ=1/2)
   - N=256 blocks: T ∈ **[+0.333, +0.401]**, mean +0.385 (39 blocks)
   - Trend: T → **A3(1/2) = +1/2 (PROVEN)** as N grows; m₃ → 5 (mean 4.64/4.75 at N=64/256, finite-height deficit). **CHECKED NUMERICALLY.**
   - The zeros' T is POSITIVE. The identity lower edge m₃ ≥ 5.4419 + T is then **m₃ ≥ 5.78–5.84 for the real zeros**, consistent with... **no**: the zeros' m₃ = 4.64–4.75 < 5.44+T because the marked-pair lower bound 3u is an *identity for marked laws* — the unmarked zeros have pair = 3·A2 = 3·(7/6) = 3.5 with D = 1, giving m₃ = 1 + 3.5 + T = 4.5 + T = 5 ⟹ T = +1/2 exactly (PROVEN A3). **The marked pair-refund (m_i+m_j ≥ 2 → pair ≥ 3u(p₁)) does NOT apply to the unmarked zeros.**
2. **The [−3.93, −0.44] number:** identity-derived — T = m₃ − D − pair with m₃ = 5, D = 4−3p₁, pair ∈ [3u(p₁), 6u(p₁)]: T = 5 − (4−3p₁) − pair ∈ [5−(4−3p₁)−6u, 5−(4−3p₁)−3u] = [1+3p₁−6(p₁+0.48062), 1+3p₁−3(p₁+0.48062)] = [−1.88372−3p₁, −0.44186]. At p₁ = p₀ ≈ 0.682: [−3.93, −0.44]. **PROVEN arithmetic (m3-price §STRUCTURE).** It is the T the MARKED configs need to reach m₃ = 5 — opposite in sign to the zeros' own connected part.
3. **Min-side consequence at the identity level:** the marked class {m₃ ∈ 5±ε, T ∈ realized} with T-realized ≈ [+0.33, +0.43] (zeros) gives m₃ = D + pair + T ≥ 5.4419 + T ≥ 5.77 — **outside [5−ε, 5+ε] for every ε ≤ 2.77**. A marked config at m₃ = 5 with T in the zeros' positive range is IMPOSSIBLE unless pair is at its lower edge 3u(p₁) = 3p₁ + 1.44186 AND... D + 3u = 5.44186 already exceeds 5; T ≥ +0.33 pushes m₃ ≥ 5.77. **At the identity level: min-p₁ over {marks, m₃ = 5±ε, T-realized} = the class is EMPTY for ε ≤ 2.77 if T is required to equal the zeros' positive T.** The m₃ = 5 pin and the zeros' T are contradictory for marked configs — a marked config can match m₃ = 5 only with T ≤ −0.44 (negative), never with the zeros' T.
4. **What the LP must decide:** with the REALIZED T-range [T_min, T_max] = [0.272, 0.427] (N=64) as a *constraint*, is any pool config in {rows, marks, m₃ ∈ 5±ε, T ∈ [0.272, 0.427]}? If none: min-p₁ = ∞ (class empty in-pool); the certificate question is void at the pool level, and the honest statement is: the m₃ = 5±ε class with T constrained to the zeros' range is EMPTY for all ε ≤ 2.77 (identity-level, pending LP). If the class is nonempty at some ε, min-p₁ is the number and the adversary is the lowest-p₁ config.

**Verdict (identity level, N=256, PROVEN arithmetic):** the certificate value v(ε) = min p₁ over {rows, marks, m₃ ∈ 5±ε, T ∈ zeros-realized} is **UNREACHABLE — the class is empty for ε ≤ 2.77** because (a) marked m₃ ≥ D + 3u(p₁) + T = 5.44186 + T and (b) T = +1/2 (PROVEN A3) for the real zeros' unmarked connected part, and no marked config in the m₃ = 5±ε window can have T in [+0.27, +0.43]. The "door" (certificate 0.70) is CLOSED at this hinge by a sign contradiction: the marked m₃ = 5 pin needs T ≤ −0.44, the zeros realize T = +1/2. Pending: (a) the LP class-count confirms emptiness in the N=64 pool; (b) the subtlety that the zeros' T is the UNMARKED connected part while the class's T is the MARKED one — the marked T is not observable from zeros and could differ. If marked-T is free (as attack-law-s3 §4 holds — no proven input bounds marked T), the pin's T-window [−1.88−3p₁, −0.44] is the operative one, and min-p₁ over {m₃ = 5±ε, T ∈ that window} = 0.70 reachable — but that is the OLD claim, and the "realized T-range" then means nothing (it is identity-derived, not zeros-realized).

## §STEP 1 — realized T of the real zeros (COMPLETE, CHECKED NUMERICALLY)

Script: `scripts/m3_min_frontier.py` (self-contained, reads zeros_computed_10000.txt). T = m₃ − D − pair with D = 1, pair = (3/N)Σ_{i≠j}K², sinc kernel λ=1/2, theta/π unfolding, consecutive N-blocks.

| N | blocks | m₃ range | m₃ mean | T range | T mean |
|---|---|---|---|---|---|
| 64 | 156 | 4.458–4.803 | 4.640 | **+0.272–+0.427** | +0.367 |
| 256 | 39 | 4.647–4.793 | 4.750 | **+0.333–+0.401** | +0.385 |

- m₃ → 5 with N (finite-height deficit pattern, matches attack-twobandwidth's 4.80 @ N=1024).
- T → +1/2 = PROVEN A3(1/2) (attack-law-s3 §5). The zeros' connected part is POSITIVE.
- Contrast with m3-price's claimed realized range [−3.93, −0.44]: that is the identity-derived MARKED-T window for p₁ ≈ p₀ (PROVEN arithmetic in m3-price §STRUCTURE: T = m₃ − D − pair ∈ [1+3p₁−6u, 1+3p₁−3u] = [−1.88372−3p₁, −0.44186]; at p₁ = 0.682: [−3.93, −0.44]).

## §STEP 2 — min-p₁ LP with T-realized (NEXT: run + append)

## §STEP 2 — min-p₁ LP COMPLETE (CHECKED NUMERICALLY)

Script `scripts/m3_min_lp.py`: per-config T = m₃ − D − pair computed exactly (D4 identity verified to 0.0 err on ALL-1 and mixed configs). Pool marked-T ∈ [−7.51, −2.59] (seeds 42/1234), ALL NEGATIVE — disjoint from the zeros' unmarked T ∈ [+0.27, +0.43].

**Class {rows, marks, m₃ ∈ 5±ε, T ∈ zeros-realized [0.272, 0.427]}: EMPTY for every ε ∈ {0.1, 0.44, 1.0, 2.98}, both seeds, both zero-windows [0.272,0.427] and [0.333,0.401].**

Why: marked m₃ = D + pair + T with D = 4−3p₁, pair ≥ 3u = 3p₁+1.44186 ⟹ m₃ ≥ 5.44186 + T (p₁-independent). With T = zeros' +1/2: m₃ ≥ 5.94, outside 5±ε for every ε ≤ 2.98. The zeros' m₃ = 5 needs T = +1/2 with pair = 3·A2 = 3.5 (UNMARKED, marks all 1, D = 1) — the zeros realize the UNMARKED connected part; a MARKED config in the pool never does (T ≤ −2.6 always).

## §STEP 3 — adversary identity (PROVEN arithmetic; LP per-config)

m₃ ∈ 5±ε, D = 4−3p₁, pair ∈ [3p₁+1.44186, 6p₁+2.88372] ⟹ **marked-T window: T ∈ [−1.88372 − 3p₁ − ε, −0.44186 + ε]** (from m₃ ≤ 5+ε with pair ≥ 3u: T ≤ ε−0.44; from m₃ ≥ 5−ε with pair ≤ 6u: T ≥ −1.88−3p₁−ε). The window is nonempty for every p₁ ≥ 0, so the m₃-pin imposes **NO lower bound on p₁** at the identity level: low-p₁ (high D) configs stay in-class by taking T in the marked window (T = m₃ − D − pair, negative). Binding adversary: **p₁ = 0.50 (pool floor), m₃ ∈ 5±ε, T ≈ −2.6…−3.5 in-pool** — a low-p₁/high-D config whose negative marked-T compensates; NOT excludable by the zeros (their T = +1/2 is the unmarked connected part; marked T is unconstrained by proven input, attack-law-s3 §4). k=4 moment: no data read (pool has no marked k=4 constraint); not needed — the pin alone already fails to bound p₁.

## §VERDICT (FINAL)

**v(ε) = min p₁ over the class = 0.50 (pool floor) at every ε ∈ {0.1, 0.44, 1.0, 2.98} — the certificate 0.70 is NOT reachable.** The m₃ = 5±ε pin is free on BOTH sides: on the max side (m3-price) because the pair refunds p₁-room (pair grows with p₁); on the MIN side because the marked-T window [−1.88−3p₁−ε, −0.44+ε] is nonempty for all p₁, letting low-p₁ configs compensate with negative marked-T. The "[−3.93, −0.44] realized T-range" in m3-price is NOT zeros-realized — it is the identity-derived marked-T window at p₁ ≈ p₀ (T = m₃−D−pair); the zeros' actual connected part is **+1/2 (PROVEN A3), measured +0.27…+0.43 (N=64) / +0.33…+0.40 (N=256)**. With T required in the zeros' range the marked class is EMPTY (m₃ ≥ 5.44+T ≥ 5.7 > 5+ε); with T free in the identity window the class contains p₁ = 0.50. Door: CLOSED on the min side — no ε gives v ≥ 0.70; a sharper read would need a PROVEN bound on the MARKED connected part T (same missing third-order input as attack-law-s3 §4).

Labels: PROVEN arithmetic (marked-T window; m₃-pin ⇒ no p₁ lower bound; zeros' unmarked A3 = +1/2). CHECKED NUMERICALLY (zeros T ranges; D4 identity err 0.0; LP class empty under zeros-T, both seeds; pool T ∈ [−7.5,−2.6]). INCONCLUSIVE-as-wall: marked T unconstrained by proven input.
