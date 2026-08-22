# wave-rh7 Lane G — eta metrology harness (builder G)

STATUS: DONE. Bin: `tools/eta_metrology/src/bin/eta_probe.rs` (158 lines), crate
`tools/eta_metrology/` (Cargo.toml mirrors jensen_probe). Build+run <15s.

## What was built
- Reused EM machinery from speiser_dh_certify verbatim (Hurwitz zeta + s-derivative,
  N=60, M=10, x4 next-term bound + roundoff term).
- η_k(s) = (1−k^{1−s})ζ(s); η_k′ = ln k·k^{1−s}·ζ + (1−k^{1−s})·ζ′.
- Box σ∈[0.3,1.2], t∈[10,60]; circles r=0.1; k=2 and k=4; 20 random non-zero points each;
  wrong-center controls.

## SPEC CORRECTION [CHECKED — argument principle + empirical]
The spec's "winding of η_2′ on circle r=0.1 must be 1" is mathematically FALSE for simple
zeros: winding of f counts zeros of f inside, but zeros of f′ sit generically displaced
(η′ = g′ζ+gζ′ ≠ 0 at a factor-zero s0 since g′(s0)ζ(s0)≠0). First run confirmed: wind(η′)=0
at EVERY expected zero. Correct metrology is wind(η_k) itself = EXACT zero count inside the
contour. Both columns reported honestly below. This correction matters for the Speiser lane:
certify zeros via wind(f), not wind(f′).

## Results (verbatim, abridged rows all PASS)
```
eta_metrology engine=hurwitz_em N=60 M=10 r=0.1
--- k=2 expected_zeros=18 (re1=5 zeta=13) ---
row00 center=(1.00000,18.12944) wind_eta=1 wind_etap=0 min|eta|=1.182e-1 err/min=0.000 PASS
row01 center=(1.00000,27.19416) wind_eta=1 wind_etap=0 min|eta|=1.246e-1 err/min=0.000 PASS
row02 center=(1.00000,36.25888) wind_eta=1 wind_etap=0 min|eta|=1.066e-1 err/min=0.000 PASS
row03 center=(1.00000,45.32360) wind_eta=1 wind_etap=0 min|eta|=1.462e-1 err/min=0.000 PASS
row04 center=(1.00000,54.38832) wind_eta=1 wind_etap=0 min|eta|=1.145e-1 err/min=0.000 PASS
row05..row17 (13 ζ-zeros on Re=1/2: 14.13473...59.34704) wind_eta=1 wind_etap=0 err/min=0.000 PASS (13/13)
controls k=2 near_off0.05 wind=1 (GEOMETRY-FORCED 1: zero still inside r=0.1 circle) | off0.15 wind=0 err/min=0.000 PASS
k=2 subtotal: 18/18 zero-rows PASS, 20/20 random-zero PASS
--- k=4 expected_zeros=24 (re1=11 zeta=13) ---
row00 center=(1.00000,13.59708) wind_eta=1 ... PASS   (extra odd-multiple heights found)
row01..row10 re1 zeros incl SHARED heights 18.12944/27.19416/36.25888/45.32360/54.38832 counted ONCE
row11..row23 (13 ζ-zeros) wind_eta=1 PASS
controls k=4 near_off0.05 wind=1 (GEOMETRY-FORCED) | off0.15 wind=0 PASS
k=4 subtotal: 24/24 zero-rows PASS, 20/20 random-zero PASS
METROLOGY VERDICT: PASS — eta_2 and eta_4 zero sets found EXACTLY via wind(eta)=count
(no double-count, no miss); controls clean [CHECKED NUMERICALLY]
```
Full log: /tmp/eta_out.txt pattern above; every row printed with min|η| and err/min.

## Adversarial outcomes
- k=4 finds 11 Re=1 zeros (odd multiples πm/ln2 included); the five shared k=2 heights are
  certified individually once each — no double-count, no miss.
- Wrong center offset 0.05 with r=0.1 gives wind=1 GEOMETRICALLY FORCED (zero at distance
  0.0707 < 0.1 remains enclosed) — this is correct engine behavior, not a failure; documented.
- True adversarial control: offset 0.15 → wind=0, err/min≈1e-12. PASSES.
- 40 random points (both k): all wind=0 (one point per k skipped only if within r+0.02 of an
  expected zero).

## Labels
- All windings, zero counts, error bounds: CHECKED NUMERICALLY (f64; EM truncation bound ×4
  plus explicit roundoff term; err/min ≤ ~1e-12 everywhere ⇒ certificates robust).
- Exactness of expected zero lists: PROVEN classical (factor zeros 2πim/log k; Odlyzko ζ table
  to 8 decimals, nearest listed pair >0.9 apart ≫ 0.2 diameter).
- Speiser-lane pipeline validation: this harness validates the WINDING ENGINE mechanics
  (contour sum, branch handling, count attribution) on ground truth; it does NOT certify any
  specific DH/Speiser claim. CONJECTURED that the same engine transfers unchanged.

## Verdict
METROLOGY VERDICT: PASS [CHECKED NUMERICALLY].
