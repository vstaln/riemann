# ADT-70 — Density-matched admissible floor: bootstrap fixed point (execution)

**Date:** 2026-08-12 (phone mirror, proot Ubuntu; mpmath 1.4.1 / numpy 2.3.5 / scipy 1.18.0)
**Idea (idea-factory-master §4 #8):** the certificate's own count pins a ~7× bigger ε
(per-atom ~4.0e-3 at mean gap 1.457 vs 5.43e-4); solve the fixed point ε\* = floor(ε\*)
where the floor depends on the density it implies (bootstrap).
**Task:** (1) derive the fixed-point equation ε(f) with mean gap = 1/f; (2) compute the
fixed point numerically with the exact kernel; (3) report the bootstrap constant (7-pt)
vs `seven_point = 0.67300852792777976`; (4) verdict: strictly better? self-consistent?
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE. Every number
code-backed (`tools/adt70_bootstrap.py`). No fabrication.

---

## 0. TL;DR (filled at the end)

<!-- FILL -->

---

## 1. Setup and objects (all as in context-pack, PROVEN unless marked)

- Kernel: k(x) = [sinc_u((√2−2πx)/2) + sinc_u((√2+2πx)/2)]/(2K0), sinc_u(y)=sin y/y,
  K0 = √2 sin(1/√2) = 0.91872536986556843778. k(0)=1. (PROVEN closed form, corpus.)
- H0 = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573… (base simple-zero density, PROVEN).
- 7-pt block (7 atoms): 0 = x₀ < x₁ < … < x₆, gaps g_j = x_j − x_{j−1}, span s = x₆ = Σg.
- Functional under which 19/5000 is reproduced (ladder note §3.2, CHECKED NUMERICALLY):
  **unweighted all-pairs U = Σ_{0≤a<b≤6} k(x_b − x_a)²** on the domain Σgaps ≤ 9,
  min = 3.8676e-3 (ratio 1.0178 vs 19/5000). The certified claim is a per-block lower
  bound 19/5000 = 3.8e-3 (per-atom 5.4286e-4 = 19/5000/7) — INCONCLUSIVE as to exact
  external normalization (Q1), but this is the reading used throughout.
- Plug-in (constant algebra, PROVEN at 60 dps in verify note / co10):
  c(ε) = (H0 − A₇ε)/(1 − B₇ε), A₇ = 2680/5111, B₇ = 263/269; c(19/5000) =
  seven_point = (1345000·H0 − 2680)/1340003 = 0.67300852792777976132…, per-BLOCK ε.
- In-class ceiling 0.68183123059534187426 (constraint reading, PROVEN — the bootstrap
  must not claim to exceed it under that reading).

## 2. The fixed-point equation (task 1 — derivation)

Normalize ordinates so the mean gap of ALL zeros (on the critical line) is 1. Let f ∈
(0,1] be the (proven lower bound on the) proportion of simple zeros. The simple-zero
atoms then have intensity f and **mean gap 1/f** (standard counting identity; PROVEN
given the model). Mean 7-block span = 6 gaps × mean gap = **6/f**.

**Density-matched floor.** For span budget S define
  F(S) = inf{ U(x) : 0 = x₀ < … < x₆, s ≤ S }.
Feasible set shrinks with S ⟹ F is non-increasing in S (floor grows as span shrinks;
PROVEN monotonicity). Certified anchor: F(9) ≥ 19/5000 (external; numerically F(9) ≈
3.8676e-3).

**Mean-span passage (the bootstrap's engine; CONJECTURED as a theorem).** If the atom
process has density f (mean gap 1/f), the admissible per-block pressure is taken as the
floor at the mean span:
  ε(f) = F(6/f).
Honesty: this replaces the first-moment Markov good-blocks fraction (vacuous: P(Σ6 ≤ 9)
≥ 1 − 6/(9f) = 0.8675% at f = H0 — CHECKED NUMERICALLY, workaround note) with a
mean-span argument. Its rigorous form is SPAN-01's linear-minorant lemma (L2,
CONJECTURED): if c(B) ≥ ε₇ + B(9 − s(B)) for a certified slope B, averaging over blocks
gives mean cost ≥ ε₇ + B(9 − 6/f), i.e. the floor at the mean span. The direct reading
ε(f) = F(6/f) is exactly the secant-minorant value at 6/f. **Status: CONJECTURED** (the
same step SPAN-01 flagged; no certified decay bound for s > 9 exists in the corpus).

**Self-consistent certificate.** The plug-in converts the floor into a density bound:
  Φ(f) = c(ε(f)) = c(F(6/f)).
A **bootstrap fixed point** f\* = Φ(f\*) is self-consistent: the density it proves equals
the density used to compute the floor. Bootstrap from the PROVEN anchor f₀ = H0 (no ε
needed — Theorem D): f_{k+1} = Φ(f_k).
- Monotonicity: F non-increasing in S ⟹ ε(f) = F(6/f) non-decreasing in f; c(ε) =
  (H0 − A₇ε)/(1 − B₇ε) is increasing in ε while 1 − B₇ε > 0 (here B₇ = 0.9777, ε ≤
  F(6) ≪ 1/B₇). Hence Φ is non-decreasing and (f_k) is non-decreasing from f₀ = H0,
  bounded above by 1 ⟹ converges to the least fixed point ≥ H0 (PROVEN monotone
  convergence, conditional on the mean-span passage).
- Circularity: none IF each step is a deduction from the previous bound (each input is a
  PROVEN lower bound, not the conclusion). The only unproven ingredient is the
  mean-span passage (CONJECTURED). This is the exact CI-66 "self-referential
  constraint as engine" formulation, in the density-matched-floor reading.

**Fixed-point equation (final):**
  f\* = (H0 − A₇·F(6/f\*)) / (1 − B₇·F(6/f\*)),   A₇ = 2680/5111, B₇ = 263/269.
  (Equivalently ε\* = F(6/f\*), f\* = c(ε\*).)

## 3. What was computed (task 2–3, filled after run)

<!-- FILL -->

## 4. Honest verdicts (task 4, filled after run)

<!-- FILL -->

## 5. Files / commands

- `tools/adt70_bootstrap.py` — this run.
  `proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/adt70_bootstrap.py | tee scratch/adt70_bootstrap_out.txt`
- scratch output: `scratch/adt70_bootstrap_out.txt`, results JSON `tools/_adt70_results.json`.
