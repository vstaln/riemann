# ADT-69 — Crystal ansatz for Q1: periodic-crystal energy vs ladder floors

**Date:** 2026-08-12 · **Executioner:** phone mirror (proot Ubuntu, mpmath 1.4.1 / numpy 2.3.5 / scipy 1.18.0)
**Labels used:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE. Every number code-backed
(`tools/adt69_crystal.py`, scratch output `scratch/adt69_crystal_out.txt`).

## 0. Task (idea-factory #4, ADT-69)

A periodic atom configuration ("crystal") on the mean-gap lattice (mean simple-zero gap
L = 1/H0 ≈ 1.487) with the exact kernel k gives a lattice energy per atom.
Generator sub-claims (to verify):
1. **2-periodic crystal reproduces the ladder to 0.3%.**
2. **3-periodic crystal is ~13% BELOW 19/5000** (→ would rule out the unweighted
   per-block reading of the 7-pt floor).
3. Decide **which normalization** the crystal matches (per-atom 5.43e-4 vs per-block
   3.8e-3).
4. Verdict: does the ansatz sharpen Q1 ("which normalization")?

## 1. Definitions (all as in context-pack)

- Kernel (PROVEN form): k(x) = [sinc_u((√2−2πx)/2) + sinc_u((√2+2πx)/2)] / (2K0),
  sinc_u(y) = sin(y)/y, K0 = √2·sin(1/√2) = 0.91872536986556843778. k(0) = 1.
  numpy form: k(x) = [np.sinc(√2/(2π)−x) + np.sinc(√2/(2π)+x)]/(2K0).
- Mean gap L = 1/H0, H0 = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573 → L ≈ 1.48699.
- n-periodic crystal: n atoms per cell, cell size P = nL, positions x_0=0 < ... < x_{n−1},
  gaps g_i = x_i − x_{i−1} (g_1 = x_1, etc.), Σg_i = P, all g_i ≥ 0.
- **Crystal energy per atom (periodized Madelung-type):**
  E_per_atom(g) = (1/n) Σ_{i,j∈cell} Σ_{m∈ℤ} k²(x_j − x_i + mP), excluding (i=j, m=0).
  (Ordered-pair convention; for the uniform 1-periodic crystal this reduces to
  E_1 = 2Σ_{m≥1} k²(mL).)
- **Block energy (no periodization; the ladder-type functional)** U(g) = Σ_{i<j} k²(x_j−x_i),
  per atom U/n. Ladder floors are minima of U under span constraints (Σg ≤ S_n).
- Ladder per-atom floors (from ladder-consecutive-zeros.md, CHECKED NUMERICALLY there):
  n=3: 2.2215e-4/3 = 7.405e-5 · n=7: 3.8676e-3/7 = 5.525e-4 · n=9: 4.2931e-3/9 = 4.770e-4
  n=11: 7.2479e-3/11 = 6.589e-4 · n=13: 8.5245e-3/13 = 6.557e-4 · n=15: 1.2343e-2/15 = 8.229e-4
- 19/5000 = 3.8e-3 **per-block** (7-pt documented ε) ; per-atom = 3.8e-3/7 = 5.42857e-4.

## 2. Verification plan

A. Kernel table (k at L, 2L, 3L, kernel zeros z1,z2,z3) — mpmath 50 dps sanity.
B. 1-periodic uniform energy E_1 = 2Σ_{m≥1}k²(mL) (tail-controlled).
C. 2-periodic: E_2(δ) for δ = cell gap #1 (gaps δ, 2L−δ), minimize over δ ∈ [0,L].
D. 3-periodic: E_3(g1,g2,g3), Σg = 3L, minimize over simplex.
E. Block (non-periodized) energies at the SAME span (Σg = nL) for direct ladder comparison.
F. Comparison table + normalization verdict + tail-error accounting.
G. Sensitivity: also run L' = 1.457 (ADT-70's alternate mean-gap estimate) as a robustness
   cross-check on the sub-claim percentages.

## 3. Results (filled as computed)

<!-- FILL -->

## 4. Honesty accounting

- Tail truncation error in the m-sum: measured by comparing M vs 2M on the minimizers (report).
- All minima: global grid + local refine (Nelder-Mead / L-BFGS-B); SLSQP avoided per
  context-pack artifact warning.
- The "13% below 19/5000" and "0.3%" sub-claims: reported as ratio vs exact numbers.

## 5. Rerun

```
proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/adt69_crystal.py | tee scratch/adt69_crystal_out.txt
```
