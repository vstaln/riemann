# AH lattice vs continuum pressure floors (Q3 feed) — AH-LATTICE researcher run

**Role:** AH-LATTICE researcher. **Date:** 2026-08-12 (phone mirror). **Status:** COMPLETE.

## 0. What this note is

Question: under the **Alternative Hypothesis** (Baluyot–Goldston–Suriajaya–Turnage-
Butterbaugh, arXiv 2508.10857) — consecutive simple-zero gaps are multiples of 1/2 of
the mean spacing, i.e. normalized gaps lie on the lattice {1/2, 1, 3/2, 2, ...} — do the
Gram-stability epsilon floors (min pressure over the gap simplex, span ≤ S_II(n) =
(5n+1)/4) survive, and how do **lattice-valued floors** compare with the **continuum
minima** (and the documented certified floors 221e-6 @ n=3, 19/5000 @ n=7)?

Script: `tools/ah_lattice_check.py` (extended this session to n=13, 15). JSON:
`scratch/ah_lattice_res.json`. Independent verifier: `tools/ah_lattice_verify_indep.py`.
Prior ladder numbers: `research/notes/ladder-consecutive-zeros.md`; adversarial kernel
check: `research/notes/verify-gram-stability.md`.

## 1. Setup

- Kernel k(x) = K(x)/K0, K(x) = sinc((√2−2πx)/2) + sinc((√2+2πx)/2) (unnormalized
  sinc(x)=sin(x)/x convention), K0 = 2·sinc(√2/2); normalization cancels in k. Float code
  uses np.sinc(a/π) (normalized convention) — equivalent, checked against the mpmath
  unnormalized closed form and an mpmath **quad**-kernel brute force (ratio 1.000000,
  see §7). Zeros on (0,4): 1.0573, 2.0301, 3.0202 (CHECKED NUMERICALLY, matches
  verify-gram-stability to all printed digits).
- Functionals over gaps g_1..g_{n-1} (n atoms), span Σ g_i ≤ S_II(n) = (5n+1)/4:
  - U (unweighted): F = Σ_{i<j} k(g_j−g_i)²
  - W (weighted c_s = 2/(n−s)): Fw = Σ_{s=1}^{n-1} c_s · Σ_{pairs at separation s} k²
- Lattice model (AH): g_i ∈ (1/2)·Z_{≥1}. Lattice floors computed by EXACT finite
  enumeration (vectorized compositions + DFS cross-check, assert-agree for n ≤ 9; DFS
  exact for n = 11, 13, 15, corroborated by a reduced-lattice enumeration over m ≥ 2
  units, i.e. gaps ≥ 1, which matches — all exact minimizers use gaps ≥ 1).
- Continuum floors re-derived independently (mixed Dirichlet/gamma + interior sampling +
  multistart SLSQP; seeds include documented ladder argmins + lattice argmin
  (informative only, local)). => continuum values are **upper-bound estimates** of the
  true minima (they can only sit at or above the true min).

Labels: lattice values EXACT (finite enumeration) on the stated AH model; AH itself
CONJECTURED. Continuum values CHECKED NUMERICALLY (estimates from above, not certified).
Deterministic: fixed seed 20260812; re-run reproduces the JSON bit-for-bit (see §7).

## 2. Results (verified run; script ↔ JSON bit-for-bit, mpmath re-eval ratio 1.000000)

| n | S_II | lattU | contU | docU | ratioU | lattW | contW | docW | ratioW |
|---|------|-------|-------|------|--------|-------|-------|------|--------|
| 3 | 4.00 | 3.391844e-4 | 2.221491e-4 | 2.221491e-4 | 1.5268 | 3.492736e-4 | 3.352009e-4 | 3.3520e-4 | 1.0420 |
| 7 | 9.00 | 9.204224e-3 | 3.867575e-3 | 3.8676e-3 | 2.3798 | 3.084206e-3 | 1.353657e-3 | 1.3537e-3 | 2.2784 |
| 9 | 11.50| 1.515568e-2 | 4.070343e-3 | 4.2931e-3 | 3.7234 | 3.809764e-3 | 1.322266e-3 | 1.3223e-3 | 2.8812 |
| 11| 14.00| 1.825363e-2 | 7.247887e-3 | 7.2479e-3 | 2.5185 | 3.666518e-3 | 1.928311e-3 | 1.9344e-3 | 1.9014 |
| 13| 16.50| 2.432124e-2 | 8.524546e-3 | 8.5245e-3 | 2.8531 | 4.071411e-3 | 1.725089e-3 | 1.7251e-3 | 2.3601 |
| 15| 19.00| 2.741944e-2 | 1.234314e-2 | 1.2343e-2 | 2.2214 | 3.931389e-3 | 2.168825e-3 | 2.2588e-3 | 1.8127 |

- docU/docW are ladder_probe2's estimates-from-above (fewer samples). This script's
  contU/contW may come in BELOW doc (n=9 U: 4.0703e-3 < 4.2931e-3; n=15 W: 2.1688e-3 <
  2.2588e-3): an improvement of the estimate, NOT a contradiction — both are upper
  bounds on the true min. CHECKED NUMERICALLY.
- Verified continuum anchors reproduce prior independent values: n=3 contU =
  2.221491e-4 (mpmath Newton true min), n=3 contW = 3.352009e-4, n=7 contW =
  1.353657e-3 (Q4/ladder agreement). CHECK.
- Lattice argmins (exact): n=3 (2,2); n=7 (1,2,2,1,2,1); n=9 (1,2,1,2,1,2,1,1);
  n=11 (1,2,1,2,1,2,1,2,1,1); n=13 (1,1,2,1,2,1,1,2,1,2,1,1); n=15 U
  (1,1,2,1,2,1,1,2,1,2,1,2,1,1) / W (1,1,2,1,2,1,2,1,2,1,1,2,1,1); all in gaps ≥ 1
  (units ≥ 2), i.e. **no half-unit gaps at any exact minimizer**. The n=13 span is
  16.0 < 16.5 (cap not saturated); n=15 U spans 19.0 = cap.

## 3. Continuum vs documented (honesty)

- contU/contW are upper-bound estimates (sampling + SLSQP, not certified); they can only
  overestimate the true continuum min. All 12 ratios (lattice/continuum) ∈ [1.042, 3.723]
  — none < 1; a ratio < 1 would indicate an under-converged continuum estimate or a
  violated subset relation (see §5), neither of which occurs.
- The only case where this run's continuum estimate beats the documented one (n=9 U,
  n=15 W) is an estimate improvement; the true minima are unchanged.

## 4. n=3 adjudication (lattice 3.3918e-4 is GENUINE and EXACT — not an artifact, not under-converged)

- Lattice (u,v) ∈ {0.5,1,1.5,2,...}², u+v ≤ 4: 28 points total. EXACT enumeration
  (vectorized + DFS, agree) and an **independent mpmath brute force with a quad-based
  kernel** both give min F = 3.391843988523e-4 at (2,2) = 2·k(2)² + k(4)². The float-code
  value 3.39184398852528e-4 agrees with mpmath to ratio 0.9999999999999865. CHECKED
  NUMERICALLY (two independent methods, exact on the stated finite set).
- Continuum global min 2.221491e-4 at (2.012057, 1.053089) — NOT on the lattice
  (2.012 ∉ 0.5·Z). (2,2) IS a genuine local min of the continuum S2 (ladder_probe2's
  SLSQP landed there).
- So: the 3.3918e-4 is the EXACT global min on the AH lattice AND a non-global local
  min in the continuum. The "artifact" declaration in the ladder note referred to
  ladder_probe2 mistaking (2,2) for the continuum floor; in the lattice reading the
  number is exact. Both statements are true; they concern different problems. RESOLVED.
- tr Ψ(M3) at (2,2): eig(M) = (0.980201, 1.003176, 1.016622), all in [0,2]; tr Ψ = 2·S2
  = 6.783688e-4 (identity CHECKED, matches verify-gram-stability D1); margin vs the
  certified 221e-6 floor = 3.07×.

## 5. Interpretation (lattice ≥ continuum always; AH costs nothing, buys margin)

- Lattice simplex ⊆ continuum simplex (same span cap; lattice points are a subset)
  ⇒ min over lattice ≥ min over continuum, ALWAYS. PROVEN by subset argument; the 12
  numeric ratios confirm it. No lattice floor exceeds the continuum floor "by accident"
  — it is a theorem; the ratios quantify the gap (1.04×–3.72×).
- The documented certified floors 221e-6 (n=3) and 19/5000 (n=7) are lower bounds on the
  CONTINUUM min; hence also lower bounds on the lattice min, with MORE margin (n=3:
  3.07×, n=7 lattice U: 2.42×). Under AH the binding floor is the LARGER lattice one, so
  the Gram-stability constant is STRONGER under AH, never broken.
- Plug-in constants at lattice floors (A7,B7 coefficients, CONJECTURED for n > 7):
  n=3 U → 67.2546%, n=7 U → 67.3737%, n=9 U → 67.4549%, n=11 U → 67.4975%, n=13 U →
  67.5818%, n=15 U → 67.6252% (W-plug-in plateaus 67.25–67.30%). The plug-in is monotone
  increasing in ε on the certified branch (b·H0 > a, ladder note §5), so every lattice
  floor → a constant ≥ the continuum one. AH is CONJECTURED (expected false for ζ); the
  check shows the refinement is robust to the extremal-configuration restriction.

## 6. Scripts / commands / scratch

- `tools/ah_lattice_check.py` (extended to n=13, 15 this session; otherwise unchanged
  logic). Run:
  `proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/ah_lattice_check.py`
  (wall 460 s on the extended run; note the proot cwd is /root, use the absolute path).
- `tools/ah_lattice_verify_indep.py` — mpmath 50 dps: n=3 brute force (quad kernel) +
  closed-form re-evaluation of all lattice argmins. Run with the absolute path.
- Scratch: `scratch/ah_lattice_res.json` (current, n=3..15),
  `scratch/ah_lattice_res.json.orig` (original n=3..11), `scratch/ah_lattice_res.json.pre13`
  (pre-extension backup, == .orig content), `scratch/ah_lattice_rerun.txt`,
  `scratch/ah_lattice_rerun2.txt` (extended run log), `scratch/ah_lattice_indep_out.txt`.

## 7. Verification log (this session)

- **Script ↔ JSON:** full re-run (fixed seed 20260812, wall 460 s) reproduced the
  pre-extension JSON **bit-for-bit for n=3,7,9,11 (0 diffs across all 32 numeric keys)**;
  n=13, 15 appended. The script matches the JSON; the numbers are deterministic.
  PROVEN (same machine, same seed, two independent full runs agree exactly).
- **Independent mpmath re-evaluation** (50 dps, closed-form kernel) of all 12 lattice
  argmins (n=3,7,9,11,13,15 × U,W): ratio json/mpmath = 1.000000, all OK.
- **n=3 quad-kernel brute force** (mpmath quad of the defining integral, no closed form):
  28 lattice points, min 3.391843988523e-4 at (2,2); float-code ratio 0.9999999999999865.
- **Lattice ≤9 assert-agree:** vectorized-enum vs DFS agree exactly for n=3,7,9 (both
  functionals); n=11,13,15 reduced-enum (gaps ≥ 1) equals full-DFS (no 1/2-gap minimizer).
- **All 12 ratios ≥ 1** (min 1.042, max 3.723): lattice ≥ continuum confirmed numerically.
- Labels recap: lattice floors EXACT on the stated AH model (finite set, two independent
  methods); continuum floors CHECKED NUMERICALLY (upper-bound estimates); the AH
  hypothesis itself and the n>7 plug-in coefficients CONJECTURED; subset inequality
  PROVEN (set-theoretic, independent of any numerics).
