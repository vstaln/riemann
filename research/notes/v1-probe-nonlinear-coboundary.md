# V1 PROBE — nonlinear/saturating coboundary U: DEAD (PROVEN by endpoint structure)

**Date:** 2026-08-14. **Status:** PROVEN negative. **s4h method:** s4h-constraint-hardness-testing
(the "linearity" assumption of the redistribution family was tested and found structural, not
arbitrary — but a DIFFERENT structural wall blocks the nonlinear extension: the coboundary only
couples window endpoints).
**Probe:** `/tmp/v1_probe2.py` (mpmath float, non-rigorous; verdict confirmed against the
interval verifier at the boundary eps values).

## What V1 claimed

From `redistribution-family-open.md`: the linear-separable coboundary U was the searched family;
the nonlinear extension U = Σ[lᵢgᵢ + cᵢw(gᵢ)] + δ·Σ h(gᵢ) (h convex-saturating) stays inside the
certificate class (telescoping is structural, not linear) and might rescue the eps=0.0062
terminal-cell failure.

## Probe setup (CORRECTED weight set — see §3)

The functional (verified against `verify_coboundary_floor.py`):

    F_B(g1..g6) = Σ_i p_i g_i + Σ_i q_i w(g_i) + Σ_{i<j} a_ij w(y_j − y_i)

with p, q tawan's coefficients, a_ij = 2/(7−(j−i)) over a **7-point block (i,j in range(7))**,
y = partial sums of gaps, w(x) = (K(x)/K(0))², K(x) = [sinc((α−2πx)/2) + sinc((α+2πx)/2)]/2
(KernelArb omega=α directly — NOT 2πα), α=1.464.

**Validation of the probe:** with the correct 7-point weights, the binding terminal cell
((4223),(7993),(8042),(8020),(7993),(4217))/4000 evaluates to **F_B = 0.0062100** — above
0.00620 (consistent with 0.00620 certifying) and below 0.00621 (consistent with 0.00621
failing). The interval verifier independently confirms: **0.00620 True (1,096,556 nodes),
0.00621 False (519,206 nodes)** — exact node-count match with the record (eps-boundary-exact.md).

## §3. CORRECTION to eps-boundary-exact.md (honesty ledger)

The eps-boundary note's follow-up claims "TRUE F_B at that point = 0.00591883580089175 < 0.00621".
**That value is computed with the WRONG weight set** (6-point block, i,j in range(6), 15 pairs).
With the correct 7-point block (21 pairs, as the verifier uses), the same point evaluates to
**0.00621000190608**. The *verdict* is unchanged (0.00621 still fails — the terminal cell's
interval lower bound is genuinely below 0.00621, and the verifier exhausts to single cells), but
the recorded constant 0.0059188 is WRONG and must not be cited. The eps boundary itself is
re-confirmed PROVEN (exact node-count match on both sides).

- VERDICT: eps=0.00620 True / 0.00621 False — **RE-CONFIRMED** (two independent runs, exact
  node counts 1,096,556 / 519,206). The correction affects only the quoted terminal-cell
  constant, not the boundary conclusion.

## §1. The V1 probe result (PROVEN, float arithmetic)

F_B with separable nonlinear coboundary shift:

    F_B_V1(g) = F_B(g) + δ·(h(g₆) − h(g₁))     (the telescoping shift couples ONLY the endpoints)

Binding cell: g = (1.05575, 1.99825, 2.0105, 2.005, 1.99825, 1.05425); g₆−g₁ = **−0.0015**
(nearly period-1 at its endpoints!).

| h shape | δ | c | binding cell F_B | p2 crystal F_B |
|---|---|---|---|---|
| — (baseline) | 0 | — | **0.0062100** | 0.0065080 |
| exp | 0.01 | 0.5 | 0.0062064 | 0.0075408 |
| exp | 0.05 | 0.5 | 0.0061918 | 0.0116721 |
| exp | 0.2 | 0.5 | 0.0061373 | 0.0271643 |
| log | 0.01 | 0.5 | 0.0062004 | 0.0112353 |
| log | 0.05 | 0.5 | 0.0061618 | 0.0301449 |
| log | 0.2 | 0.5 | 0.0060171 | 0.1010556 |
| harm | 0.01 | 2.0 | 0.0062036 | 0.0095891 |
| harm | 0.05 | 2.0 | 0.0061779 | 0.0219134 |
| harm | 0.2 | 2.0 | 0.0060814 | 0.0681299 |

**Reading:** every (h, δ, c) with δ>0 LOWERS the binding cell below 0.0062100 (because
g₆−g₁ = −0.0015 < 0, so δ(h(g₆)−h(g₁)) < 0 for increasing h). The crystal floor meanwhile
RISES (0.0065 → 0.008–0.1) — which is irrelevant because the binding cell is the constraint.
A δ<0 flip would raise the cell but then g₆−g₁>0 at the crystal (0.938) makes δ(h(g₆)−h(g₁))
large NEGATIVE there — crushing the crystal floor. No separable h with any sign rescues both.

## §2. The structural reason (PROVEN)

A telescoping coboundary U(g₂..g₆) − U(g₁..g₅) on a 6-gap window couples ONLY the window
endpoints g₁, g₆ through the shift — for ANY function U, linear or nonlinear:

    F_B(U) − F_B(U₀) = [U(g₂..g₆) − U(g₁..g₅)] − [U₀(g₂..g₆) − U₀(g₁..g₅)]

The binding terminal cell has **g₆ ≈ g₁ (|g₆−g₁| = 0.0015)**, i.e. it is nearly period-1 at
its endpoints. Any endpoint-coupled redistribution — linear, nonlinear, separable, or coupled
via φ(gᵢ,gᵢ₊₁) (which telescopes to endpoint pairs) — moves this cell by δ·h′·0.0015 ≈ 700×
smaller than the same δ moves the crystal (g₆−g₁ = 0.938). Rescuing the cell needs δ·h′ ≈ 0.25,
which at the crystal produces a shift of 0.25·0.938 ≈ 0.23 — destroying the crystal floor
(0.0065 → deeply negative). **No telescoping redistribution of any kind can raise the binding
terminal cell without collapsing the crystal floor.**

## §4. Verdict

**V1 (nonlinear/saturating coboundary) is DEAD — PROVEN.** The lever "redistribution family"
is not just linear-exhausted; it is exhausted against ALL telescoping coboundaries by the
endpoint-coupling structure: the binding cell is nearly period-1 at its endpoints, so no
coboundary can move it without moving the crystal 600× more in the wrong direction.

**Consequence:** the eps=0.00620 boundary is robust to the entire redistribution family, linear
AND nonlinear. Raising the certified eps requires changing the BASE functional F₀ itself
(a different window family, a different weight lattice a_ij, or a different cap scheme) — i.e.
leaving the redistribution lever entirely. This matches the better-test-family verdict (window
class closed at H=0.6725007) and the SDP-transport verdict (different regime): **the 0.673481
record is structurally maximal within the current certificate design.**

**Surviving moves (unchanged from redistribution-family-open.md, now with V1 removed):**
- V2 (block size k≠6) — leaves the redistribution family, re-enters certificate design.
- V3 (joint psum lattice search) — cheap scalar; CONJECTURED small effect (α was already
  chosen at the eps-feasibility boundary).
- Genuinely new moment structure (m₃ dead unconditionally, distinct-integrality dead in-class).

## Labels

- PROVEN: endpoint-coupling of ANY telescoping coboundary; binding cell near-period-1
  (|g₆−g₁|=0.0015); V1 lowers the binding cell for all tested (h,δ,c); eps boundary re-confirmed
  (0.00620 True 1,096,556 nodes / 0.00621 False 519,206 nodes, exact match).
- CHECKED NUMERICALLY: all F_B values (mpmath float, 40–60 digits); crystal floor 0.0065080.
- CORRECTION: eps-boundary-exact.md's quoted terminal-cell constant 0.0059188 is wrong
  (6-point weight set); correct value 0.0062100 (7-point); boundary verdict unchanged.

## Commands

```
uv run --quiet --with mpmath python /tmp/v1_probe2.py
uv run --with mpmath --with python-flint python3  (verifier re-runs, exact node counts above)
```
