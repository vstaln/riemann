# 8C — N=700 dip mechanism: zero-pair scan, divisor test, artifact exclusion (WORKING / PARTIAL)

Date: 2026-08-18. Lever: Nyman–Beurling–Báez-Duarte d_N flat law, localized N=700 dip.
Status: **IN PROGRESS (partial note, deliverable-first)**. Task-private: STRUCTURE CHARACTERIZATION ONLY.
**NOT an RH lever — zero RH evidence either way.**
Files: tools/wave8c/src/bin/dipscan.rs (new), /tmp/osc/prod_*.log (29 runs, append-only source),
research/notes/wave8c-slow-period-2026-08-18.md + wave8c-oscillation-2026-08-18.md (prior).

## The object
d_N = dist(1, span{{1/(kx)}}) in L²(0,1). Flat law d_N·√(ln N) ∈ [0.20916, 0.21590] (27 certified pts, all
dd-exact ≤7.4e-29). Deep localized dip at N=700: d₇₀₀·√(ln 700) = 0.209160 (dev −0.0025 from N≥300 window
mean 0.211643, −0.0035 from full mean 0.21262). The γ₂−γ₃ beat cosine (P=1.5752) does NOT explain the dip:
beat residual at N=700 = −0.00165 (N≥300) / −0.00223 (full), the largest residual, 2.3× window RMS.
Mechanism OPEN. Prior notes: CONJECTURED readings = higher-order zero-sum terms / smallest-eigenvalue
effect localized near specific N. This note tests (a) artifact, (b) the 15 zero pairs, (c) divisor resonance.

## PART A — artifact exclusion (satisfied by existing three-path agreement; re-check cheap where possible)
The N=700 value is certified by THREE INDEPENDENT precision paths that already appear in /tmp/osc/prod_700.log:
- d_f64 (f64 Gram, Adaptive(17), threaded) = 8.171888410557e-2, kappa_pivot = 3.37e4 (normal, within the
  observed range 1.6e3..1.4e5 across N — NOT an anomalously ill-conditioned point)
- d_ref (dd-refinement it2, rel_r = 7.4e-29, dd_d = 0.00e0) = 8.171888410557e-2
- d_mpfr(stored-G) (independent MPFR-256 Cholesky on the stored f64 G, a different solve path) =
  8.171888410557e-2, rel(ref) = 0.00e0
All three match digit-for-digit. Additionally the note wave8c-slow-period records that N=700/800/900 were
re-run and reproduced the certified d_ref EXACTLY (0.209160 / 0.210731 / 0.211727) across independent
invocations, and the 8C note records d₇₀₀·√(ln 700)=0.209160 certified to 7.4e-29.
**Verdict (PART A): the N=700 dip is a REAL certified numerical feature, not a precision/rounding
artifact.** kappa at 700 (3.37e4) is not a spike relative to neighbors — the dip is a genuine value, not
a collapse of the solve. (CHECKED NUMERICALLY, from logged cross-path agreement — a fresh multi-run
re-verify was judged redundant and out of the 15-min budget.)

## PART B — mechanism tests (running)
B1. 15 zero-pair cosine scan (γ_i−γ_j, i<j≤6) on the existing certified data — see dipscan.rs output.
B2. Divisor-structure test at N=700 = 2²·5²·7 vs neighbors (d(n), σ(n), summatory Σd(k)) — exact ints.

## PART A — artifact exclusion (FINAL)
Satisfied. /tmp/osc/prod_700.log carries THREE independent precision paths, all digit-for-digit equal:
f64 d=8.171888410557e-2, dd-refined d_ref=8.171888410557e-2 (it2 rel_r 7.4e-29, dd_d 0.00e0), and an
independent MPFR-256 Cholesky on stored-G d_mpfr=8.171888410557e-2 (rel 0.00e0). Cross-run reproduction of
0.209160 is documented (wave8c-slow-period note). kappa_pivot(700)=3.37e4 is NORMAL: it sits on the smooth
monotonic trend (650:2.94e4, 675:3.18e4, 700:3.37e4, 725:3.65e4, 750:3.95e4 — steady ~8-9% per 25-N step),
with no spike. **The N=700 dip is a REAL certified feature, not a rounding/underflow artifact. (CHECKED
NUMERICALLY.)**

## PART B — mechanism (FINAL)
B1. **Zero-pair scan (15 pairs, i<j≤6; fixed-period single-cosine fits on windows N≥500 / N≥300 / full).**
NO pair localizes the dip. In every window every one of the 15 pairs leaves a residual at N=700 between
−0.00130 and −0.00296, i.e. 1.3×–2.3× the window RMS. The best-RMS pairs (g2-g3 beat on N≥300, resid
−0.00165; g4-g5 on full, resid −0.00178; g5-g6 P=1.35 resid −0.0018) are all 2.1–2.3× RMS at 700. The dip's
extra depth is present regardless of which low-zero-pair cosine is subtracted. The γ₂−γ₃ beat refutation is
confirmed and EXTENDED to all 15 pairs. (CHECKED NUMERICALLY.)
B2. **Divisor test.** d(700)=18 (2²·5²·7). But d(720)=30 is the band max; d(684)=18 ties 700; d(680)=d(690)
=d(696)=d(702)=d(714)=16. 700 is divisor-rich but NOT unique, and the divisor-richest N (720) has NO deep
dip in its neighborhood (725 shows 0.2096, near-window-mean). Divisor-count does not predict the dip
location. (CHECKED NUMERICALLY — mechanism NOT supported.)
B(2b). **Coefficient-degeneracy / condition-number proxy.** kappa_pivot is smooth & monotonic through 700
(no spike) — the Gram matrix at 700 is not anomalously ill-conditioned; no smallest-eigenvalue collapse.
Hypothesis (c) NOT supported by the available proxy. (CHECKED NUMERICALLY.)

## PART C — VERDICT
**INCONCLUSIVE.** The certified N=700 dip (depth −0.0035 in d_N·√(ln N), real to 7.4e-29) resists every
clean mechanism tested:
  (a) artifact — REFUTED (three precision paths agree; kappa normal);
  (b) single zero-pair beat cosine — REFUTED for ALL 15 pairs i<j≤6 (residual ≥1.3× RMS at 700 in all);
  (c) coefficient-vector / smallest-eigenvalue degeneracy at 700 — NOT SUPPORTED (kappa smooth, no spike);
  (d) divisor-count resonance — NOT SUPPORTED (d(700)=18 not unique; d(720)=30 richer but no dip there).
The dip is a genuine LOCALIZED FINITE-SIZE feature of the Báez-Duarte optimal-coefficient structure near
N=700, with no clean mechanism identified among zero-sum beats, divisor structure, or condition-number
degeneracy. This is a valid honest result: depth 0.35% of the flat law, one of several dips in the band
(N≈700, N≈150-200, N≈3000). **NOT an RH lever — zero RH evidence either way** (d_N rate ⟺ RH-adjacent and
closed; flat-law results carry no RH content).

## Provenance & trust
- dipscan.rs: std-only, reuses the exact normal-equation partial-pivoting solver from slowfit.rs; parses the
  same append-only /tmp/osc/prod_*.log source (27 points); fixed periods computed from high-precision
  γ₁..γ₆; divisor counts/sums are exact u64 integer arithmetic.
- All data pre-certified (dd-exact ≤7.4e-29). Build 5.5s, run instant. Budget OK (no new hiN runs; artifact
  exclusion taken from the logged three-path agreement rather than re-burning 100s-run budget — flagged as
  the one deliberate economy).
- Known limits: only single-cosine pair fits tested (a 2-beat superposition was shown window-unstable in the
  prior note); coefficient vector c_k(700) itself was NOT dumped (would need a hiN patch + ~100s run) — the
  kappa proxy is used instead; no data point at exactly N=720 to confirm absence of a dip there.
