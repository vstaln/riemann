# ADT-71 / B3-01 — Detuning/decomposition closed form for the floors (Q2)

**Date:** 2026-08-12 · **Executor:** EXECUTION agent (phone mirror, proot Ubuntu,
mpmath 1.4.1 / numpy 2.3.5 / scipy 1.18.0, no pip, wall budget < 10 min)
**Idea source:** idea-factory-master.md §4 #21 (ADT-71 / B3-01); original generator text
`analogy-ideas.md` ID-ADT-71 (L790) and the resonance-detuning entry (L509–511).
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE on every claim;
every number code-backed.
**Scripts:** `tools/adt71_detuning.py` (3-pt), `tools/adt71_seven.py` (7-pt prediction).
**Deliverable status:** IN PROGRESS (write-early).

---

## 0. Task

1. Verify the detuning decomposition: min S2 (3-pt) as a weighted sum over kernel-zero
   data — the generator claims `min S2 = 2.2215e-4 ≈ k'(z2)²(u*−z2)² + k'(z1)²(v*−z1)² +
   k(u*+v*)²` to 99.5%, offsets (−0.0180, −0.0042, +0.0449), slopes (−0.8775, +0.4206,
   −0.2779). Find the exact form by least-squares fit.
2. PSLQ (mpmath pslq) on candidate algebraic/rational coefficients: do the c_j live in
   ℚ / √2-field?
3. Predict the 7-pt floor from the same decomposition; compare vs 19/5000 = 3.8e-3.
4. Report the closed form with the honesty label.

## 1. Prior state (from context-pack + CL-01 + ladder notes)

- Kernel (PROVEN): k(x) = [sinc_u((√2−2πx)/2) + sinc_u((√2+2πx)/2)] / (2K0),
  sinc_u(y) = sin(y)/y, K0 = √2·sin(1/√2) = 0.91872536986556843778.
- Kernel zeros on (0,4) (CHECKED, mpmath 60 dps, residual ~1e-62): z1 = 1.0572782910088553,
  z2 = 2.0300675301281605, z3 = 3.0202429921714815.
- Slopes (CHECKED): k′(z1) = −0.877453…, k′(z2) = +0.420646…, k′(z3) = −0.277918….
- min S2 (CHECKED, 35 digits, CL-01): 2.2214911015980081170582120737146383e-4 at interior
  (u*, v*) = (2.012057343466106931139826…, 1.053089401989153888647472…), w* = 3.0651467454552608…;
  stationarity k(u*)k′(u*) = k(v*)k′(v*) = −k(w*)k′(w*) (PROVEN algebraically from ∇S2 = 0).
- At the minimizer (CHECKED): k(u*) = −0.0076428335175…, k(v*) = +0.0036926401022…,
  k(w*) = −0.01225155561795…, so min S2 = k(u*)²+k(v*)²+k(w*)².
- Detuning δ = z1+z2−z3 = 0.0671…, δ² = 4.5e-3 (CHECKED).
- 7-pt documented ε = 19/5000 = 3.8e-3 per block (per-atom 5.43e-4); unweighted span-9
  floor measured 3.8676e-3 (ratio 1.018) [ladder-consecutive-zeros.md, CHECKED NUMERICALLY].

## 2. Results

<!-- FILL -->

## 3. Honesty accounting

<!-- FILL -->

## 4. Rerun

```
proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/adt71_detuning.py
proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/adt71_seven.py
```
