# Wave RH-4 builder B — Li spectral scan through n=100000

## Verdict

**CHECKED NUMERICALLY:** the bounded f64 spectral scan found no negative displayed-model value for `1 <= n <= 100000`. This is not a proof that the exact Li coefficients are nonnegative on this interval, not a global positivity claim, and not an RH proof. The tail is modeled asymptotically rather than certified.

**CHECKED NUMERICALLY (RH-false control):** the same `beta0=0.85`, `gamma0=14.13472514` functional-equation quadruplet first makes the modeled coefficient negative at `n=5155`, reproducing the known control fire. It later returns nonnegative, with last nonnegative `n=99993`; therefore the finite scan's permanently-negative suffix begins at `n=99994`. "Permanently" here means only through `n=100000`.

## Data and method

Code: `tools/jensen_probe/src/li_lambda_1e5.rs`, registered as Cargo bin `li_lambda_1e5`.

The loader skips every line whose first non-whitespace character is not a digit and uses all `J=100000` parsed ordinates. The actual supplied cutoff is `gamma_J=74980.922970159532`, not approximately 500000. The scan is O(NJ), threaded over zero blocks, and uses the validated engine's complex phasor recurrence for `4 sin^2(n theta_j)` with `theta_j=atan(1/(2 gamma_j))`.

The displayed real-world values include the old engine's Riemann-von Mangoldt density tail model. **CONJECTURED:** integrating `dN(t) ~= log(t/2pi) dt/(2pi)` gives
`sum_{gamma>T} 4/(4gamma^2+1) ~= (log(T/2pi)+1)/(2pi T) = 2.204774418822e-5` at this cutoff. With `|sin(n theta)| <= n|sin theta|`, the resulting crude scale is at most `n^2` times this estimate, or `220477.441882` at `n=100000`. There are infinitely many omitted zeros; an exact finite omitted count is unavailable. This large resolution limit prevents interval-certifying signs from this f64 computation.

## Build and run

```text
cd tools/jensen_probe
cargo build --release --bin li_lambda_1e5
timeout 60s target/release/li_lambda_1e5
```

```text
li_lambda_1e5 n_max=100000 J=100000 gamma_cutoff=74980.922970159532
data note: the supplied file ends near 74980.9, not 500000; all loaded zeros were used
real global_min n=1 lambda=0.023095647958
real first_negative=NONE
real anchor n=1000 lambda=2325.992266418907
real anchor n=5000 lambda=15637.637097125576
real anchor n=5155 lambda=16201.760806417515
real anchor n=5156 lambda=16205.216942565874
real anchor n=10000 lambda=34731.566529233714
real anchor n=100000 lambda=472190.551505977812
plant beta=0.85 gamma=14.13472514 |z_growing|=1.001750106741
plant first_negative=5155
plant anchor n=5155 lambda=-153.354778987810
plant anchor n=5156 lambda=-247.914947738172
plant anchor n=100000 lambda=-8181549018571031689123217936246309967809622594851957472057341138320266100736.000000000000
plant permanently_negative_suffix_through_scan=99994 (finite-range statement only)
omitted_zero_count=INFINITE (the data set is finite; exact ordinates beyond cutoff are not loaded)
[CONJECTURED] Riemann-von Mangoldt-density estimate sum_{gamma>T} 4/(4gamma^2+1) ~= 2.204774418822e-5
[CONJECTURED] using |sin(n theta)| <= n|sin(theta)| gives omitted on-line tail magnitude <= n^2 times that estimate; at n=100000: 220477.441882164858
CHECKED NUMERICALLY: finite f64 scan only; no claim that lambda_n >= 0 globally and no RH proof.
elapsed_seconds=14.528
```

## Legacy-engine cross-validation

Command:

```text
timeout 60s target/release/li_lambda_spectral --n-max 10000 --zeros-n 100000
```

Old-engine anchors:

```text
 1000  lam=   2325.992266  lit=-  plant_delta=             -  lam_planted=             -
 5000  lam=  15637.637097  lit=-  plant_delta=             -  lam_planted=             -
10000  lam=  34731.566529  lit=-  plant_delta=             -  lam_planted=             -
```

New vs old (new printed to 12 decimals, old to 6):

| n | new | old | status |
|---:|---:|---:|:---|
| 1000 | 2325.992266418907 | 2325.992266 | CHECKED NUMERICALLY: agrees at 6 decimals |
| 5000 | 15637.637097125576 | 15637.637097 | CHECKED NUMERICALLY: agrees at 6 decimals |
| 10000 | 34731.566529233714 | 34731.566529 | CHECKED NUMERICALLY: agrees at 6 decimals |

## Interpretation

- **CHECKED NUMERICALLY:** global modeled minimum is `lambda_1=0.023095647958`; no modeled negative occurs through `100000`.
- **CHECKED NUMERICALLY:** control fire remains exactly `n=5155` under the extended data/model.
- **INCONCLUSIVE:** the computation cannot certify exact finite-range positivity because its omitted tail treatment is asymptotic and the crude `n=100000` resolution scale is about `2.20e5`.
- **CONJECTURED:** the density-integral expression is an informative tail scale, not a rigorous bound unless supplied with explicit zero-counting error control.
