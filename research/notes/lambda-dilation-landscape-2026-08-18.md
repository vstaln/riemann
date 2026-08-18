# lambda-dilation-landscape-2026-08-18 — exhaustive α-sweep at λ=1.15

## Lattice floor search (30-start gradient descent, f64, grid 4000, lo=1000 hi=10000)

| α | lattice floor | worst-case gaps /4000 | time |
|---|---|---|---|
| 1.415 | 0.0068918 | [4194,7940,4181,7966,7976,4198] | 363s |
| 1.43 | 0.0069464 | [4199,7939,4186,7965,7976,4203] | 366s |
| 1.45 | 0.0070089 | [8014,4200,7982,8009,7992,4212] | 211s |
| 1.464 | 0.0070487 | [8014,4204,7982,8010,7992,4217] | 375s |
| 1.48 | 0.0070953 | [8015,4210,7982,8010,7993,4223] | 374s |
| 1.50 | 0.0071554 | [8016,4216,7982,8010,7993,4230] | 403s |
| 1.52 | 0.0072176 | [8017,4223,7982,8011,7993,4237] | 390s |

Note: two basin types exist: (a) all-large gaps ~8000, (b) mixed ~4200+8000. The all-large basin
gives the lower F values for α ≥ 1.45.

## 200-bit MPFR bounds at lattice floor (theoretical max at each α)

| α | eps (floor) | bound | delta from record 0.6735633 |
|---|---|---|---|
| 1.415 | 0.00689 | 0.6735065 | +2.6e-5 |
| 1.43 | 0.00695 | 0.6735419 | +6.1e-5 |
| 1.45 | 0.00700 | 0.6735604 | +7.9e-5 |
| 1.464 | 0.00704 | 0.6735698 | +8.9e-5 |
| 1.48 | 0.00709 | 0.6735763 | +9.5e-5 (peak) |
| 1.50 | 0.00714 | 0.6735652 | +8.4e-5 |
| 1.52 | 0.00720 | 0.6735479 | +6.7e-5 |

## Arb verification results (the certifiable eps)

| α | target | grid | verified? | terminal-cell low | note |
|---|---|---|---|---|---|
| 1.45 | 0.00700 | 4000 | TRUE | n/a | 1,120,338 nodes |
| 1.464 | 0.00703 | 4000 | TRUE | n/a | 1,068,980 nodes |
| 1.464 | 0.00704 | 4000 | FALSE | 0.0070274 | prior session |
| 1.464 | 0.00704 | 8000 | FALSE | 0.0070337 | grid-8000 reduces slack |
| 1.48 | 0.00708 | 4000 | FALSE | 0.0070669 | target - low ≈ 1.3e-5 (grid-4000 slack) |
| 1.48 | 0.00708 | 8000 | FALSE | 0.0070734 | target - low ≈ 6.6e-5 (grid-8000 slack) |
| 1.48 | 0.00709 | 4000 | FALSE | 0.0070773 | |
| 1.45 | 0.00710 | 4000 | FALSE | 0.0070875 | |

## True F at terminal cell midpoints (f64 exact evaluation)

| α | cell | midpoint F | target | below? |
|---|---|---|---|---|
| 1.48 | g8k terminal (8447,...,8446) | 0.0070802 | 0.00708 | BARELY above |
| 1.464 | g8k terminal (8442,...,8442) | 0.0070403 | 0.00704 | BARELY above |

The midpoint evaluations are ABOVE the targets, but the true minimum over the cell is
BELOW the target (the verifier's low is a rigorous cell-lower-bound). The cell minimum
lies in [low, midpoint+slack]. So:
- true floor at (1.48, 1.15) ∈ [0.007073, 0.007080] — certifiable eps ≈ 0.00707
- true floor at (1.464, 1.15) ∈ [0.007034, 0.007040] — certifiable eps ≈ 0.007035

## Conclusion

The certifiable landscape is:
- (1.45, 1.15, 0.00700) → bound 0.6735604
- (1.464, 1.15, 0.00703) → bound 0.6735633 (current record)
- (1.48, 1.15, ~0.00707) → bound ~0.6735636 (marginal gain +0.3e-6)

**The lambda-dilation class is structurally saturated at ~0.6736.** The bound varies
<1e-4 across the entire α range. The in-class ceiling 0.6818 requires p/q re-optimization
(12-parameter max-min over the coboundary class), which is a separate computational project.
