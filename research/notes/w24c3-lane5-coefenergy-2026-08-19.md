# w24c3-lane5 — coefficient-energy discriminant V(N): real-world growth law + planted-zero control (2026-08-19)

Status: IN PROGRESS (plan + first findings; results appended below).

## Context (cited, not re-derived)
- RH ⟺ Báez-Duarte d_N → 0, d_N = L²(0,1) distance from 1 to span{ρ_{1/k}: k≤N}, ρ_u(x) = {1/(u x)}. (Campaign contract, ledger; BD criterion.)
- Real world, certified (wave8c): d_N·√(log N) ≈ 0.212 flat to N=5000; δ(N)=d_N²·log N flat 0.0448–0.0525.
- Closed-form Gram engine validated: reproduces certified d_N = 0.151041 / 0.126823 / 0.119192 at N=10/20/30 (tools/wave8c hiN.rs; /tmp/dN_recheck.py, /tmp/w24_probe.py). Basis k=1..N, b_k=(log k+1−γ)/k.
- agy wave-24 C3 claim "V(N)/(N log N) ≤ 0.182 flat" REFUTED (check /tmp/w24_probe.py C3, adjudication note agy-wave24-2026-08-19): V/(N log N) = 19.2 → 25.8 → 30.5 at N=10/20/30, rising, factor ~150 above claim.
- OPEN: actual growth law of V(N) in real world; does a planted-zero world give a genuinely different (divergent / different-exponent) law? V(N) = (1/d_N²)·Σ_{k≤N} k·(a_k*)².

## Plan
1. Reproduce certified d_N at N=10/20/30 on the validated engine in MY probe (sanity gate).
2. Compute V(N), W(N)=Σ k a_k²=(1−... d-scale) for N = 10..60 (k=1..N basis), fit growth law of V(N): check V ~ N^α via log-log regression, V/(N log N) trend, V·d_N²=W growth; report residuals. Expect V/(N log N) still rising (consistent with refutation); determine α.
3. Planted-zero world (β=0.7, 1/2<β<1): building the true planted Beurling Gram is NOT feasible in this budget (generalized-prime inner products are a different object). HONEST control instead:
   - PROVEN (from the BD iff + monotone-convergence argument): planted world ⟹ d_N ↛ 0, d_N ↘ d_∞ ≥ dist(1, closed span) > 0, so the certified real-world law d_N·√(log N) ≈ 0.212 is VIOLATED: planted gives c·√(log N) → ∞ (divergent signature on the same axis). This is the discriminating growth signature.
   - CONJECTURED (Mellin/coefficient-runaway argument, NOT computed — would need planted Gram): with the 1/d_N² denominator saturated at c²>0 in the planted world vs decaying ~C/log N in the real world, V(N)'s growth in the two worlds differs by the exponential-of-(log N) factor structure; coefficient vector fights the pole at s=0.7 of 1/ζ.
   - No fake control: the planted V(N) trajectory was NOT numerically computed; that is stated as CONJECTURED.
4. Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE on every claim.

## First findings
- Engine gate + C3 numbers re-verified in probe run (see below).
- (filled in after run)
## Second findings (final synthesis — parent completed after subagent's context death)

### Real-world coefficient energy (CHECKED NUMERICALLY, two independent runs agree)
- Certified d_N gates PASS at N=10/20/30 (|Δ|≤4e-8), monotone strictly decreasing (≤) all steps.
- Normalized object V(N)=(1/d_N²)·Σ k a_k² (agy's literal C3): **V/(N logN) = 19.2, 26.1, 25.8, 26.4** (N=10/15/20/25) — ~100x above agy's claimed 0.182 and not flat. **REFUTED AS STATED** (parent's independent run agrees: 442/1545/3112 at N=10/20/30).
- Unnormalized U(N)=Σ_{k≤N} k·a_k² (parent's independent run, N=12..56): log-log slope ≈ **1.4 (0.5≤α≤~1.6 noisy)**, U/(N logN) drifts 0.42→0.61, U/N² falls. **No clean law**; U(N) ≈ N^α super-linear sub-quadratic, α not pinned at N≤56 (Gram build cost ~O(N²) at high precision; N=50+ killed by 1800s timeout once, rescued by 8-worker pool).

### Planted-zero control — HONEST, two-part
- **PROVEN (elementary, no computation):** In a planted-zero world (an off-line zero β>1/2), the Báez–Duarte criterion gives d_N ↛ 0, d_N ↘ d_∞ ≥ dist(1, closed span) > 0. Hence the certified real-world signature d_N·√(log N)≈0.212 flat is VIOLATED there (d_N·√(log N) → c·√(log N) → ∞). **This is the known BD-criterion itself, not a new separator** — it re-encodes "RH ⟺ d_N→0", so it has zero new discriminating power beyond the theorem already in the ledger. Heavy flag: a "new" discriminant that equals the stored BD criterion is a restatement, and it is not RH-false-control-verified beyond what BD already gives.
- **CONJECTURED (NOT computed):** with 1/d_N² saturated at c²>0 (planted) vs decaying ~C/log N (real), agy's V(N) growth would differ — but the true planted Gram (generalized-prime inner products) is a different object we did not build. Stated CONJECTURED, no number attached.

## VERDICT (complete)
- agy wave-24 **C3 refuted as stated** (both runs agree): the normalized V/(N logN) ≈ 19–26, not ≤0.182.
- The corrected unnormalized coefficient-energy U(N) is a genuinely-novel object but **no clean law at N≤56** and its planted-control hinges entirely on the already-stored BD-criterion (restatement risk) + an uncomputed CONJECTURED trajectory. **Not fundable as a new one-way RH discriminant.** ABANDONED (consistency-level only; no RH content; nothing proves-too-much).
- Lane #5 remains OPEN for a genuinely NEW object; this C3-line does not close it with anything usable.
- Firewall intact: nothing implying RH survives; all labels honest.

## Files
- probe: research/notes/w24c3-lane5-probe-2026-08-19.py ; run: research/notes/w24c3-lane5-probe-run-2026-08-19.txt
- parent independent: /tmp/w24_probe.py, /tmp/un_growth.py, /tmp/vn_growth.py
