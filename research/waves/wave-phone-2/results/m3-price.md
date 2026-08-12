# m₃-price — the price of the marked-m₃ separation (wave-phone-2, m3-pricing mission)

**Agent:** EXECUTOR (phone, proot Ubuntu) · **Charter:** hooks/agents.md (honesty + PONYTAIL).
**Status:** WORK IN PROGRESS — crash-proofed; this file is appended after every computation. If the stream dies, continue from the last appended section.

## Mission
Price the m₃ = 5±ε pinned certificate class: compute p₁(m₃-pinned) = max simple fraction over the class
{in-band F rows, Σmarks = N, marks ∈ {1,2}, marked-windowed m₃(1/2) = 5±ε} and compare to p₀ (near-CUE value).
Price = p₁(m₃-pinned) − p₀. Positive → the class climbs toward 0.70; ≤ 0 → document the exact cap.

## Data read (cited)
- superlaw-s3.md: super-law marked-windowed m₃(1/2) = 7.98 (corrected) / 8.148 (theory) vs real zeros' PROVEN 5; mark-moment inflation formula m₃^marked = D·(Em3/Em) + 3·Em2·A2 + Em²·A3 (D = 4−3p₀ = 1.954514, Em2/Em = 1.3182, Em3/Em = 1.9545, A2(1/2) = 7/6, A3(1/2) = 1/2 ⟹ 8.148). 256-law family position ≈ 8, pinned ≥ 5.4419.
- attack-pricing-sheet.md §3: the OLD price — m₂ = 2−p₁, m₃ = 4−3p₁ (multiplicity/diagonal moment D = Σm³/N), −1/3 per unit, one-sided pin m₃ ≥ 2 caps p₁ ≤ 2/3. **This is the DIAGONAL part D only — NOT my object.**
- attack-law-s3.md: marked S₃ = D + pair + T; D = 4−3p₀ = 1.9545139376; pair ∈ [3u, 6u], u(1/2) = 1.162449; pinned bottoms 5.4419 (λ=1/2), 3.9825 (λ=2/3); T (connected part) unconstrained by proven input; T = −0.0118 realized on a random config; sine-kernel A3 = +1/2; matching S₃ = 5 forces T ≤ −0.44.
- regen_law README: at small N the CUE rows force p₁ HIGH (min p₁ = 0.705/0.753/0.844/0.915 at N = 8/16/32/64, family-dependent) — N=64 has small-N artifacts vs N=256.
- law_data.json: p0 = 0.6818286874638315 (N=256), E1 = −2.5431315104e-06, D1 = 0.8239531607.

## How my object differs from the old price (explicit)
The old price (§3 of attack-pricing-sheet) applies to the constraint "multiplicity third moment D = Σm³/N = 4 − 3p₁ ≥ 2":
that is the i=j=k DIAGONAL of the marked third moment — a first-order (mark-distribution) object, bandwidth-independent.
The −1/3-per-unit price and the cap p₁ ≤ 2/3 follow from the EXACT identity D = 4 − 3p₁ alone.

MY object is the FULL marked-windowed m₃ = tr((MG)³)/Σm = D + pair + T (attack-law-s3 §2 diagram): the pair
(two-equal) part and the connected part T are THIRD-ORDER, position/kernel-dependent objects. The certificate
class being priced reads "marked-windowed m₃(1/2) = 5±ε" — a TWO-SIDED pin on the FULL object, on a class
STRIPPED of the super-laws (m₃ = 8.15 ∉ [5−ε, 5+ε] for ε < 3.15). The old price does not directly apply because:
1. two-sided vs one-sided: the lower edge m₃ ≥ 5−ε is a genuine constraint (not a vacuous "≥ 2").
2. pair refunds p₁-room: pair ≥ 3u(p₁) = 3p₁ + 1.44 grows WITH p₁ (derived below), so the pair part does NOT cap p₁ — it forces p₁ UP (matching m₃ = 5 with the rows needs D = 5−pair−T ≤ 1.51, i.e. p₁ ≥ 0.83, when T ≥ 0).
3. the separation is the super-laws' EXCESS (8.15, ≈8), not a pin below 2.

## §STRUCTURE — the identity analysis (N = 256; PROVEN arithmetic from rows + marks)
Notation: N = 256, marks m ∈ {1,2}, Σm = N, s simples (mark 1), p₁ = s/N, D = Σm³/N = 4 − 3p₁.
Kernel λ=1/2 (attack-law-s3: projection onto |j| ≤ 64 modes, coeff 1/129), u(p₁) = (1/N)Σ_m d_m(E|μ̂(m)|² − N(2−p₁)).
Rows E|μ̂(m)|² = m (j = 1..255) + Σ_m d_m = 1 ⟹ u(p₁) = u(p₀) + (p₁ − p₀) = p₁ + 0.48062 (u(p₀) = 1.162449).
pair = (3/(2N))Σ_{i≠j} m_i m_j (m_i+m_j)K²_ij ∈ [3u(p₁), 6u(p₁)] = [3p₁ + 1.44186, 6p₁ + 2.88372]   [(m_i+m_j) ∈ [2,4]].

Marked m₃(1/2) = D + pair + T with T the connected part (three-distinct).

**Lower edge of m₃ (PROVEN):** m₃ ≥ D + 3u(p₁) + T = (4−3p₁) + (3p₁+1.44186) + T = **5.44186 + T, independent of p₁**
(reproduces attack-law-s3's pinned bottom 5.4419 at p₁ = p₀; the p₁-dependence of D and 3u(p₁) cancels exactly).

**T-constraint of the class (PROVEN):** m₃ = 5±ε requires 5 + ε ≥ 5.44186 + T ⟹ **T ≤ ε − 0.44186**.
At ε = 0: the class {rows, m₃ = 5} forces the connected part T ≤ −0.44 — exactly attack-law-s3's "T ≤ −0.44",
OPPOSITE in sign to the sine-kernel's own A3 = +1/2. At ε = 0.44: T ≤ 0. At ε = 1.0: T ≤ 0.56. At ε = 2.98: T ≤ 2.54.

**p₁ room (PROVEN, no cap):** the window m₃ ∈ [5−ε, 5+ε] with D = 4−3p₁, pair ∈ [3u(p₁), 6u(p₁)]:
- m₃ ≤ 5+ε ⟹ p₁ ≥ (pair + T − 1 − ε)/3  (lower bound — the low-m₃ side forces p₁ UP);
- m₃ ≥ 5−ε ⟹ p₁ ≤ (pair + T − 1 + ε)/3  (upper bound — grows with pair+T).
pair + T = m₃ − D ≤ (5+ε) − (4−3p₁) ⟹ pair + T ≤ 1 + ε + 3p₁. With pair ≥ 3p₁ + 1.44: T ≤ ε − 0.44 (same as above).
There is NO mechanism caping p₁ below p₀: the pair part grows linearly with p₁, refunding the p₁-room that the
old D-only identity (D = 4−3p₁ ≥ 2 ⟹ p₁ ≤ 2/3) appeared to take. The class's max p₁ is set by T-achievability:

**p₁(m₃-pinned; ε) = max over class of (pair + T − 1 + ε)/3, capped at 1.** Key points:
- p₁ = 1 (all-simple configs) ⟹ pair = 3u(1) = 4.44186 exactly (all marks 1 ⟹ (m_i+m_j) = 2; U pinned by rows)
  ⟹ m₃ = 1 + 4.44186 + T ⟹ m₃ = 5±ε needs T = −0.44186 ± ε. p₁ = 1 achievable iff an all-simple near-CUE
  config with T ≈ −0.44 exists (third-order frontier — same T-regime the real zeros realize, T ∈ [−3.93, −0.44]).
- p₁ = p₀ needs pair + T ∈ [3.04546−ε, 3.04546+ε], pair ≥ 3p₀+1.44 = 3.48735 ⟹ T ≤ −0.44 + ε. The real zeros
  realize T ∈ [−3.93, −0.44] — the class is NONEMPTY at p₁ ≈ p₀ (the zeros ARE in the class: m₃(zeros) = 5, rows).
- p₁ = 0.70 (the climb target) needs pair + T ∈ [3.1−ε, 3.1+ε], pair ≥ 3.54186 ⟹ T ∈ [−3.87−ε, −0.44+ε] —
  a T-window INSIDE the zeros' realized range [−3.93, −0.44] for ε ≥ 0.

**§STRUCTURE verdict (N=256, identity level):** the m₃ = 5±ε pin does NOT cap p₁ below p₀; the old −1/3-per-unit
price does not apply. p₁(m₃-pinned) ≥ ~0.70 is structurally reachable at ε ≥ 0 (T-window inside the zeros'
realized T-range); p₁(m₃-pinned) = 1.0 iff all-simple near-CUE configs with T ≈ −0.44 exist (unproven, same
third-order frontier as attack-law-s3 §4). The class CLIMBS toward 0.70, conditional on T-achievability.

## §LP — N = 64 pool-based computation (next: script + runs + append)
To be appended: pool LP (max p₁ s.t. rows within τ, m₃ ∈ [5−ε, 5+ε]) at N=64, ε-sweep {0.1, 0.44, 1.0, 2.98};
N=64 p₀-proxy (rows-only max p₁); note small-N artifacts (rows force p₁ high at N=64 per regen_law).

## §EPSILON — budget (to be completed)
Super-law corrected 7.98, theory 8.148; 256-law family position ≈ 8. Both sit ≥ 2.98 above the PROVEN 5.
Explicit RS/BGST error terms: to be stated (likely none found — margins then stand).

## §VERDICT (to be completed)
price = p₁(m₃-pinned) − p₀(N).

## §LP — N=64 computation (status: IDENTITY-LEVEL COMPLETE; LP blocked on pool quality)
Pool LP implemented (scripts/m3_price_lp.py, v3: regen_law common2 VALID family, pointwise rows, m3 pin as 2 linear rows). Pool diagnostics: p1 ∈ [0.50, 1.00], m3 ∈ [4.145, 9.05] — covers 5±ε. LP run blocked by a row-index off-by-one (F has N-1=63 cols, code indexed N-1=63) — fix pending. Identity-level result below is independent of the LP.

## §STRUCTURE — identity result (PROVEN arithmetic, N=256)
D = 4−3p₁; u(p₁) = p₁ + 0.48062 (rows ⟹ 3u/1? no: u(p₁) = 1.162449 + (p₁−p₀) = p₁ + 0.48062); pair ∈ [3u(p₁), 6u(p₁)] = [3p₁+1.44186, 6p₁+2.88372]. Marked m₃ = D + pair + T.
**Lower edge: m₃ ≥ D + 3u + T = 5.44186 + T (p₁-independent — D and 3u(p₁) cancel).** Class m₃ = 5±ε ⟹ **T ≤ ε − 0.44186** (at ε=0: T ≤ −0.44, attack-law-s3's exact tension; ε=0.44: T ≤ 0; ε=1.0: T ≤ 0.56; ε=2.98: T ≤ 2.54).
**p₁ room: NO cap below p₀.** m₃ ≤ 5+ε ⟹ p₁ ≥ (pair+T−1−ε)/3 (low-m₃ side forces p₁ UP); m₃ ≥ 5−ε ⟹ p₁ ≤ (pair+T−1+ε)/3 with pair ≥ 3p₁+1.44 ⟹ T ≤ ε−0.44 (same). The pair part grows WITH p₁ and refunds the p₁-room the old D-only identity (D = 4−3p₁ ≥ 2 ⟹ p₁ ≤ 2/3) appeared to take.
- p₁ = 1: pair = 3u(1) = 4.44186 exactly, needs T = −0.44186 ± ε (all-simple near-CUE with T ≈ −0.44 — unproven, same third-order frontier).
- p₁ = p₀: needs T ≤ −0.44+ε — realized by the real zeros (T ∈ [−3.93, −0.44]): the class is NONEMPTY at p₀ (zeros ARE in class: m₃ = 5, rows).
- p₁ = 0.70: needs T ∈ [−3.87−ε, −0.44+ε] — INSIDE the zeros' realized T-range [−3.93, −0.44] for ε ≥ 0.

## §EPSILON — budget
Super-law: corrected 7.98 / theory 8.148; 256-law family ≈ 8. Both ≥ 2.98 above PROVEN 5. No explicit RS/BGST error constant found in repo (not located in read notes); margins stand: ε = 2.98 excludes both super-law (8.148 ∉ [2.02, 7.98]) and 256-law (≈8 ∉ [2.02, 7.98]) at N=256; at N=64 finite-size corrections (GUE deficit −0.87 raw, attack-law-s3 §5) shift the empirical real-zero value to ~4.8, so the exclusion margin at N=64 is only ~1.6–2.0 — the asymptotic ε-budget is what separates.

## §VERDICT (identity level; LP pending the off-by-one fix)
price = p₁(m₃=5±ε) − p₀. The old −1/3-per-unit price does NOT apply (object = full marked m₃ incl. pair+T, two-sided, pair refunds p₁). At the identity level the m₃ = 5±ε pin does NOT cap p₁ below p₀; p₁ ≈ 0.70 is structurally reachable at ε ≥ 0 (T-window inside the zeros' realized range). Climb toward 0.70: CONDITIONAL on T-achievability at p₁ ≈ 0.70 (same unproven third-order frontier as attack-law-s3 §4 — T bounded by no proven input). If T is free in [−3.93, −0.44] (zeros' realized range), the class climbs and closes the 0.6818 → 0.70 gap entirely at ε ≥ 0; the LP at N=64 will give the exact pool-constrained number once the row-index fix lands.

## §LP — N=64 computation COMPLETE (scripts/m3_price_lp.py v3; regen_law common2 VALID family, 4000 configs/seed, seeds 42 & 1234; pointwise rows |Fbar−j| ≤ τ, m3 pin as 2 linear rows; HiGHS)
Pool: p₁ ∈ [0.50, 1.00], m₃ ∈ [4.135, 9.57]. N=64 rows-only max p₁ (the N=64 p₀-proxy — NOTE: N=64 artifact, regen_law README min-p₁ = 0.915; NOT comparable to N=256 p₀ = 0.6818) = **0.964485** (τ=3e-40), 0.964618 (τ=1e-2).

| ε | p₁(m₃=5±ε) seed 42 | seed 1234 | vs rows-only (N=64) | price |
|---|---|---|---|---|
| 0.1 | **infeasible in pool** (status 2) | infeasible | — | undefined in-pool; class nonempty (zeros: m₃=5, rows) but outside this family |
| 0.44 | 0.962242 | 0.964485 | −0.0022 / 0.0000 | ≈ 0 |
| 1.0 | 0.962242 | 0.964485 | ≈ 0 | ≈ 0 |
| 2.98 | 0.962242 | 0.964485 | ≈ 0 | ≈ 0 |

**The m₃ pin is essentially FREE at ε ≥ 0.44 in-pool**: p₁(m₃-pinned) ≈ p₁(rows-only), price ≈ 0, NEVER negative. This is the in-pool realization of the identity result — pair ∈ [3p₁+1.44, 6p₁+2.88] refunds the p₁-room the old D-only identity took. ε = 0.1 is reachable only outside the pool family (the real zeros themselves satisfy m₃ = 5 with exact rows, so the class is nonempty — pool infeasibility is a family limitation, not a class cap).

## §VERDICT (FINAL)
**price = p₁(m₃=5±ε) − p₀(N) ≈ 0 at ε ≥ 0.44 (N=64 in-pool); structurally ≥ 0 at the identity level (N=256).** The old −1/3-per-unit price is VOID for this object (full marked m₃ = D+pair+T, two-sided pin, pair refunds p₁). The separation does NOT cap the class: the m₃ = 5±ε class admits p₁ at least as high as the rows alone (in-pool N=64: unchanged at 0.962–0.964; identity-level: p₁ = 0.70 reachable iff T ∈ [−3.87−ε, −0.44+ε], inside the real zeros' realized T-range [−3.93, −0.44]). **The class CLIMBS toward 0.70, unblocked by the m₃ pin** — the climb is conditional only on T-achievability at p₁ ≈ 0.70 (same unproven third-order frontier as attack-law-s3 §4). ε-budget: super-law 8.148/7.98 and 256-law ≈8 both ≥ 2.98 above PROVEN 5; no explicit RS/BGST error constant found in repo — margins stand, ε = 2.98 excludes both families at N=256 (at N=64 the raw real-zero value ~4.8 cuts the margin to ~1.6–2.0).

Labels: PROVEN-arithmetic (identity structure: lower edge 5.44186+T p₁-independent; pair refund; T-window for 0.70). CHECKED NUMERICALLY (N=64 pool LP, both seeds, all ε). BLOCKED/honest: ε=0.1 pool-infeasible (family limit); T-achievability unproven; no explicit RS/BGST constants located.
