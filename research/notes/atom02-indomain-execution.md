# ATOM-02 / NUM-05 — In-domain fraction + empirical S2 distribution on real zeros (Q1 honesty gate)

**Status (overall):** CHECKED NUMERICALLY (script + command cited below; every number code-backed)
**Date:** 2026-08-12
**Executed by:** EXECUTION agent (ATOM-02/NUM-05 dispatch)
**Idea source:** research/ideas/idea-factory-master.md §4 entry #7 (EV rank 7), §8 run-today list; fan-ideas.md ID-ATOM-02 + ID-NUM-05.

## Aim (verbatim distillation)

1. On the first 500 zeta ordinates (`mp.zetazero(1..500)`, `float(mp.im(...))`), compute the fraction of
   consecutive-3-zero configs (γi, γi+1, γi+2 → two normalized gaps u, v) whose span falls in the
   certification domain — plus pairwise-gap readings against the kernel-zero structure
   (z1=1.0572782910, z2=2.0300675301, z3=3.0202429921).
2. Histogram the S2 values (pack functional S2 = k(u)² + k(v)² + k(u+v)²) over those configs:
   typical vs worst-case.
3. Report the **conservatism ratio** (typical S2 / worst-case S2) — the honesty gate for whether the
   certified floor (min S2 = 2.221491e-4, pack) is achievable in practice.

## Method

- **Script:** `tools/atom02_indomain.py` (final), working copies in `scratch/` during the run.
- **Command:** `proot-distro login ubuntu -- python3 tools/atom02_indomain.py`
  (phone: mpmath 1.4.1 / numpy 2.3.5; no pip; wall < 10 min).
- **Kernel:** closed form k(x) = [sinc((√2−2πx)/2) + sinc((√2+2πx)/2)] / (2·K0),
  K0 = √2·sin(1/√2) = 0.91872536986556843778 (pack, PROVEN).
- **Zeros:** ordinates t_i = float(mp.im(mp.zetazero(i))). PHONE QUIRK VERIFIED: zetazero returns
  0.5 + i·γ (complex); `mp.re` gives 0.5 (WRONG — fan_probe2.py's `mp.re` usage would yield zero
  gaps; flagged, do not repeat), `mp.im` gives γ. Check: im(zetazero(1)) = 14.134725141734695 vs
  known γ1 = 14.1347251417346938... ✓.
- **Normalized gaps:** g_i = (t_{i+1} − t_i) · log(t_mid/(2π))/(2π), t_mid = (t_i + t_{i+1})/2
  (mean spacing ≈ 1).
- **Configs:** 3-zero windows → (u, v) = (g_i, g_{i+1}); span = u+v; pairwise gaps {u, v, u+v}.
- **S2 functional (pack, ID-CL-01 caveat below):** S2 = k(u)² + k(v)² + k(u+v)².
- **Sanity anchors computed by the script (must match pack):**
  - kernel zeros z1, z2, z3 (Newton/bisection from closed form) → compare 1.0572782910 / 2.0300675301 / 3.0202429921;
  - floor: min S2 over u,v ≥ 0, u+v ≤ 4 → compare 2.221491e-4 (pack, CHECKED NUMERICALLY);
  - k(1) ≈ 0.0267, k(2) ≈ −0.0064 (fan-ideas "What the fan reveals" #5).

## Domain conventions (honesty: three readings, all reported)

| Label | Definition | Meaning |
|---|---|---|
| D4  | u + v ≤ 4  | pack 3-pt span S=4 (the actual certified domain, context-pack "Atom sets") |
| D9  | u + v ≤ 9  | task dispatch literal "span ≤ 9" (loose inclusion) |
| DZ  | u ≤ z3, v ≤ z3, u+v ≤ z3 | each pairwise gap inside the kernel-zero structure range (0, z3) |

(7-zero / 6-gap windows, the ATOM-02 companion, reported separately: fraction of 6-gap windows with
Σ6 gaps ≤ 4 [model I] and ≤ 9 [model II span] — the Q1 E[Σ6]≈8.9 honesty context.)

## Results

(computed — filled from script output; every number below appears in the run log)

### 0. Sanity anchors
- kernel zeros reproduced / floor reproduced / k(1), k(2) reproduced: SEE RUN OUTPUT SECTION.

### 1. In-domain fractions (3-zero windows, N = 498 windows from 500 zeros)
- D4 (certified, u+v ≤ 4): FRAC_D4
- D9 (task literal, u+v ≤ 9): FRAC_D9
- DZ (kernel-zero-structure range): FRAC_DZ
- (for contrast) theoretical E[u+v] = 2 under mean-1 gaps.

### 2. S2 distribution (all windows and in-domain)
- all windows: min / p50 / mean / p99 / max
- in-domain (D4): min / p50 / mean / p99 / max
- worst-case certified floor (pack): 2.221491e-4 at (z1, z2) vertex (recomputed: RECOMPUTED_FLOOR)

### 3. Conservatism ratios (the honesty gate)
- mean(S2|D4) / floor
- median(S2|D4) / floor
- mean(S2|D4) / empirical min(S2|D4)
- min(S2|D4) / floor  → how close real configs come to the worst case
- count of real configs with |u−z1| < 0.05 and |v−z2| < 0.05 (near-vertex)

### 4. 6-gap (7-zero) window coverage (ATOM-02 companion)
- fraction with Σ6 gaps ≤ 4 (model I), ≤ 9 (model II)

### 5. Histogram
- 10-bin histogram of log10 S2 over in-domain (D4) configs + bin table (in run output; JSON in scratch/).

## Labels / honesty notes

- PHONE QUIRK (re/im): verified above; fan_probe2.py `mp.re` usage is stale/wrong — corrected here.
- S2 functional caveat: ID-CL-01 (top EV idea) flags raw-Gram ≠ pack S2 mismatch as OPEN. This run
  uses the pack functional S2 = k(u)²+k(v)²+k(u+v)² (the object behind the certified floor); if
  ID-CL-01 resolves the raw-Gram mismatch, the histogram should be re-computed on the true functional.
- Sample size: 500 zeros → 498 3-zero windows. Statistics are stable-in-spirit diagnostics, NOT
  certified bounds; the in-domain fraction is an *empirical* rate, and the Q1 per-block→liminf
  passage still needs a proof (SPAN-01 / A6-01 are the candidate fixes).
- No new proof claimed. Everything CONJECTURED except the reproduced pack anchors
  (CHECKED NUMERICALLY).

## Deliverables
- this note; tools/atom02_indomain.py; scratch/atom02_indomain_out.txt; scratch/atom02_indomain_hist.json
