# TASK: Laptop discovery line — the exact law of min p₁(N) (near-CUE marked-config certificates)

## Mission (brain directive: NEW DISCOVERY, method-driven, no brute force)
The class-ceiling question was left open: **"is the ceiling an N=256 phenomenon?"** (MB2.4).
Extend the existing small-N computation to N=128 and 256 (both data budgets), with multi-seed
stability, and FIT the exact law of min p₁(N). A closed form (or a precise crossing of the
0.6725 Theorem-B line) is a NEW RESULT. Numerics are the verification; the research is the law.

## Context — read first, do NOT re-derive
- `research/notes/regenerate-256law.md` — the full LP construction (pointwise rows Σ w_c f_c(j)=j;
  cumulative budget |D(1)|≤d1, |E(1)|≤1/(6N²)+τ/(2N)); known values: pointwise min p₁ = 0.705/0.753/
  0.844/0.915 (N=8/16/32/64, upper bounds over the random family, VALID configs); cumulative min p₁ =
  0.669–0.687 (N=8, seed/family-dependent!), 0.732/0.782/0.835/0.883/0.914 (N=16/32/64/128/256);
  E(1) = −1/(6N²) PROVEN-BY-ARGUMENT; grid lower bound p₁ ≥ 3/2 − d₁ = 0.67604683.
- `tools/regen_law/final_numbers.py` — the EXISTING report script: extend it (it already loops N
  for both budgets — extend the N range and add a fit).
- `tools/regen_law/lp_smallN.py` — VALID config family generator (s_c = N − 2d) + solve_lp.
- `tools/regen_law/check_cum8.py` — the seed-stability pattern (cumulative min p₁ at N=8 depends on
  family size/seed — this is a KEY sensitivity: report it, don't hide it).
- `tools/regen_law/common.py` — vectorized spectra. NOTE: common.py's gen_family_vec is the KNOWN
  BUGGY generator (Σ marks = N+d); use lp_smallN.py's gen_family (valid) or fix common.py.

## Environment
Laptop is the compute worker (no pi there): `proot-distro login ubuntu -- bash -lc 'ssh pc-jump
"su vstaln -c \"cd /home/vstaln/riemann/tools/regen_law && python3 <script>\""'` (laptop has scipy/
HiGHS). Phone python (mpmath/numpy, scipy unknown — check `proot-distro login ubuntu -- python3 -c
"import scipy"`) only for light work.

## The work (CHECKED NUMERICALLY, script + command cited)
1. **Extend the curves**: run BOTH budgets at N ∈ {8,16,32,64,128,256} with VALID configs, 3+ seeds
   (seed ∈ {42,1234,2024} or similar) — tabulate min p₁(N) per seed (family-size sensitivity is part
   of the result). Pointwise rows at large N will likely be INFEASIBLE over the random family — that
   IS a result (the exact-CUE spectrum is not in the random family); report the largest feasible N.
2. **The fit (THE DISCOVERY)**: fit min p₁(N) for the cumulative curve. Candidates: 1 − c/√N,
   1 − c/N^a (a free), 1 − c·log(N)/N, c₀ + c₁/N^a. Report the best fit with residuals at all N.
   Check: does the cumulative curve cross the Theorem-B line 0.6725, and at what N? (Known: N=8 dips
   to 0.669–0.687 BELOW it.) Is the crossing monotone/unique?
3. **Adversarial**: re-verify E(1) = −1/(6N²) numerically at N=128, 256 (closed form Σⱼ(j/N)(1−j/N));
   re-check the N=8 cumulative dip with the seed-sweep (is 0.669 real or a family artifact?).
4. Write the discovery note: the law, the crossing, the N=256-phenomenon verdict, honest labels.

## Deliverable
`research/waves/wave-phone-2/results/laptop-family.md` — the table (both budgets × N × seeds), the
fitted law with residuals, the crossing analysis, labels. Save the extended script alongside.

## Ponytail + crash-proof (hooks/agents.md)
Extend final_numbers.py (don't rewrite); save the script; write the deliverable EARLY and append per
result; bash calls < 90 s; numbers first. Honest labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED.
