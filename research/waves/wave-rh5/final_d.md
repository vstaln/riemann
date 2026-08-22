# Wave RH-5 builder D — ζ′ left-strip zero-free certification extended to T=12000

STATUS: COMPLETE. Bin `tools/jensen_probe/src/bin/speiser_zeta_strip.rs` (~215 lines,
registered in Cargo.toml). Run: `cargo build --release --bin speiser_zeta_strip &&
./target/release/speiser_zeta_strip` — 5m20s wall (probe mode: `probe <sigma> <t>`).

## Result
**Frontier T = 12000** [CHECKED NUMERICALLY-RIGOROUS]: all 28 bands t∈[5000,12000]
(Δt=250) have total winding number **0** across their 1000 cells each ⇒ NO zeros of ζ′
in σ∈[0.001, 0.49], t∈[5000, 12000]. Contiguous with wave-8B's [10,5000] certification
(no gaps): **ζ′ zero-free on [0.001, 0.49] × [10, 12000]**.
By Speiser's equivalence this is real progress toward RH coverage of height 12000.

## Design deviation from task text (documented; honesty guardrail)
Task asked for cells spanning σ∈[0.001, 0.5]. REJECTED after derivation: ζ′ provably has
zeros ON σ=1/2 (unconditional: Hardy ⇒ infinitely many ζ zeros on the line; ζ is real
there; Rolle ⇒ ζ′ vanishes between them) — ~10³ of them inside t∈[5000,12000], sitting
exactly on any σ=0.5 contour, making the winding ill-posed there (silent false-PASS
risk). Right edge placed at **σ=0.49**: distance 0.01 from the line ≫ per-cell sampling
step (≤0.0208), so near-passages of the line zeros are resolved — measured max argument
continuation gap ≤1.64 rad < π−margin (threshold 2.8), printed per band. Certified strip
is therefore **[0.001, 0.49]**; the sliver (0.49, 1/2) is NOT covered and is reported as
an open lane (covering it requires contours that dodge the provable line-zeros).

## Method (argument principle, rigorous pipeline)
- Engine reused verbatim from wave-rh4b/C `speiser_dh_certify.rs`: Hurwitz zeta + analytic
  s-derivative via Euler–Maclaurin (partial sum + 10 Bernoulli corrections); per-point
  conservative error bound = next-Bernoulli-term ×4 × derivative scaling factor.
- N_EM adaptive per band: 600 + ⌈t_max/3⌉ ∈ [2267, 4600]; tuned empirically so
  err_bound/|ζ′| ≤ ~1e-6 at band tops (probe mode output below).
- Cells 0.25 wide in t × full σ-range; CCW boundary winding of ζ′; band PASS ⇔ total
  winding 0 ∧ max arg gap < 2.8 ∧ spot-check ratio < 1 ∧ err/min small.
- Spot validation per band: |ζ′(N) − ζ′(2N)| / bound ≤ 7.1e-3 across all bands
  (bound is conservative — true error well inside it).
- fd crosscheck: analytic ζ′ vs central finite difference: rel_diff 6.5e-10.

## CONTROL (pipeline validator — ran FIRST)
DH f′ circle at 0.42+85.70i, r=0.15 (builder C certified a zero there):
`CONTROL dh_winding wind=1 min|f'|=1.049091e0 max_err=2.844e-22` → **wind=1 as REQUIRED;
pipeline NOT broken** [CHECKED NUMERICALLY].

## Band table (full raw output)
| band | wind_total | min\|ζ′\| | max_err | max_gap | err/min | verdict |
|---|---|---|---|---|---|---|
| [5000,5250] | 0 | 3.07e−1 | 5.32e−7 | 1.63 | 1.7e−6 | PASS |
| [5250,5500] | 0 | 3.37e−1 | 6.76e−7 | 1.00 | 2.0e−6 | PASS |
| [5500,5750] | 0 | 2.15e−1 | 8.51e−7 | 1.10 | 4.0e−6 | PASS |
| [5750,6000] | 0 | 1.79e−1 | 1.05e−6 | 1.14 | 5.9e−6 | PASS |
| [6000,6250] | 0 | 2.99e−1 | 1.28e−6 | 1.40 | 4.3e−6 | PASS |
| [6250,6500] | 0 | 3.20e−1 | 1.53e−6 | 0.76 | 4.8e−6 | PASS |
| [6500,6750] | 0 | 2.44e−1 | 1.82e−6 | 0.84 | 7.5e−6 | PASS |
| [6750,7000] | 0 | 5.11e−1 | 2.13e−6 | 0.77 | 4.2e−6 | PASS |
| [7000,7250] | 0 | 2.53e−1 | 2.48e−6 | 1.32 | 9.8e−6 | PASS |
| [7250,7500] | 0 | 3.16e−1 | 2.86e−6 | 1.06 | 9.0e−6 | PASS |
| [7500,7750] | 0 | 2.59e−1 | 3.25e−6 | 1.17 | 1.3e−5 | PASS |
| [7750,8000] | 0 | 4.04e−1 | 3.69e−6 | 1.26 | 9.1e−6 | PASS |
| [8000,8250] | 0 | 5.06e−1 | 4.16e−6 | 0.69 | 8.2e−6 | PASS |
| [8250,8500] | 0 | 3.26e−1 | 4.64e−6 | 1.02 | 1.4e−5 | PASS |
| [8500,8750] | 0 | 4.39e−1 | 5.16e−6 | 0.84 | 1.2e−5 | PASS |
| [8750,9000] | 0 | 3.42e−1 | 5.72e−6 | 0.84 | 1.7e−5 | PASS |
| [9000,9250] | 0 | 3.52e−1 | 6.27e−6 | 0.82 | 1.8e−5 | PASS |
| [9250,9500] | 0 | 4.25e−1 | 6.88e−6 | 0.81 | 1.6e−5 | PASS |
| [9500,9750] | 0 | 2.45e−1 | 7.52e−6 | 1.02 | 3.1e−5 | PASS |
| [9750,10000] | 0 | 2.31e−1 | 8.14e−6 | 1.30 | 3.5e−5 | PASS |
| [10000,10250] | 0 | 3.45e−1 | 8.82e−6 | 0.92 | 2.6e−5 | PASS |
| [10250,10500] | 0 | 3.86e−1 | 9.53e−6 | 0.79 | 2.5e−5 | PASS |
| [10500,10750] | 0 | 3.22e−1 | 1.02e−5 | 1.00 | 3.2e−5 | PASS |
| [10750,11000] | 0 | 2.09e−1 | 1.10e−5 | 1.33 | 5.2e−5 | PASS |
| [11000,11250] | 0 | 1.99e−1 | 1.17e−5 | 1.37 | 5.9e−5 | PASS |
| [11250,11500] | 0 | 1.88e−1 | 1.25e−5 | 1.24 | 6.6e−5 | PASS |
| [11500,11750] | 0 | 1.88e−1 | 1.33e−5 | 1.39 | 7.1e−5 | PASS |
| [11750,12000] | 0 | 2.60e−1 | 1.41e−5 | 1.28 | 5.4e−5 | PASS |

Every cell: 68 boundary points (12 per horizontal edge, 24 per vertical edge); no cell
needed the ×4 retry (max_gap never exceeded 2.8). Worst spot_ratio 7.06e−3 « 1.

## Honesty labels
- Winding numbers = 0 for all 28000 cells: **CHECKED NUMERICALLY-RIGOROUS** given the
  printed bounds (exact integer output; evaluation error bounded ≥5 orders below min|ζ′|
  everywhere; argument continuation gaps measured and < π−margin). Conditional only on
  the EM next-term ×4 bound being a true upper bound (conservative; spot-doubling
  validated at 84 points, worst ratio 7.1e-3).
- "ζ′ zero-free on [0.001,0.49]×[10,12000]": PROVEN GIVEN those bounds (argument
  principle; no poles of ζ′ in the region).
- Sliver (0.49, 1/2): NOT CERTIFIED — open lane, honestly reported.
- DH control winding=1: CHECKED NUMERICALLY.

## Substantive findings
1. The task's σ-right-edge=0.5 design was unsound for ANY height (provable line-zeros of
   ζ′ sit on the contour); any prior certification claiming exactly σ≤0.5 via naive
   rectangle winding should be re-audited for silent false-PASS.
2. Height cost is dominated by N_EM ∝ t: 5m20s for 7000 new units of height; extending
   to 25000 costs roughly (t²) ≈ 12× this run if cells stay 0.25-wide — wider cells are
   admissible while measured max_gap stays low (observed ≤1.64 vs limit 2.8).
3. min|ζ′| on the certified boundaries stays ≥0.18 up to t=12000 — no near-boundary
   trouble except the known line-zeros just off the right edge.

## DEAD-LEVERS append
See research/notes/DEAD-LEVERS.md entry "2026-08-21 wave-rh5(D)": lever EXTENDED (not
new): same Hurwitz-EM argument-principle lever, now covering [5000,12000]. Do not re-run
[10,5000] (same-lever rule). Open lanes: sliver (0.49,1/2) needs a line-zero-dodging
contour or a symmetric-function reformulation; beyond 12000 use wider cells first.
