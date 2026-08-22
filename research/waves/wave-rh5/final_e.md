# Wave RH-5E — Uniform Hadamard Deficit scan

## Verdict

**UHDC as stated is refuted on the requested grid [CHECKED NUMERICALLY].** Every one of the 207,210 included points has `Re(zeta'/zeta)<0` beyond the propagated Euler–Maclaurin error bound. The first is `s=0.05+16i`, value `-0.6281573984651 +/- 4.06e-10`, distance `1.918789` from the nearest supplied zero. The most negative value is `-33.35930407273 +/- 5.00e-5` at `0.45+22016i`, distance `0.778642` from the nearest supplied zero.

This is a finite f64 Euler–Maclaurin scan, not an RH result. A requested independent 40-digit mpmath recheck could not run because `mpmath` is not installed; the binary reports `MANUAL RECHECK REQUIRED`. The internal N=64 versus N=128 cross-check at the first violating point differs by `8.10e-14`, below the combined quotient bound `1.80e-9`. Thus the numerical refutation is **CHECKED NUMERICALLY**, while an independent arbitrary-precision recheck is **INCONCLUSIVE (missing mpmath)**.

## Method

Probe: `tools/jensen_probe/src/bin/uhdc_scan.rs` (220 lines). It loads `tools/data/zeros_rust_100k.txt`, scans sigma `0.05,0.10,...,0.45` and t `14..70000` by 2, and excludes points within `3/log(t)` of the nearest supplied critical-line zero. It evaluates zeta and zeta-prime by Euler–Maclaurin with 24 Bernoulli corrections, a periodic-Bernoulli integral remainder bound and a conservative floating-point accumulation allowance; quotient uncertainty is propagated as

`|delta(zeta'/zeta)| <= e_zeta'/(|zeta|-e_zeta) + |zeta'| e_zeta/(|zeta|(|zeta|-e_zeta))`.

Command:

```sh
cargo build --release --manifest-path tools/jensen_probe/Cargo.toml --bin uhdc_scan
./tools/jensen_probe/target/release/uhdc_scan
```

Bounded runtime was about 40 seconds.

## Output

```text
uhdc_scan EM_M=24 selfcheck_zeta2_abs=4.441e-16 bound=5.620e-12 cross_N64_N128=8.101e-14 combined_bound=1.802e-9
grid sigma=0.05..0.45 step=.05 t=14..70000 step=2 included=207210 excluded=107736
minimum Re(zeta'/zeta)=-3.335930407273e1 +/- 4.999e-5 at s=0.45+22016.0i nearest_zero=22016.777035398292 distance=0.778642
centered=Re(zeta'/zeta)-0.5log(t/2pi): min=-37.440128 max=-0.953284 mean=-11.885891 first_third_mean=-10.282548 last_third_mean=-13.065963
hist[ 0] [-37.440128,-33.791444) = 4
hist[ 1] [-33.791444,-30.142759) = 1
hist[ 2] [-30.142759,-26.494075) = 1
hist[ 3] [-26.494075,-22.845390) = 6
hist[ 4] [-22.845390,-19.196706) = 9
hist[ 5] [-19.196706,-15.548022) = 1243
hist[ 6] [-15.548022,-11.899337) = 113410
hist[ 7] [-11.899337,-8.250653) = 82918
hist[ 8] [-8.250653,-4.601968) = 8915
hist[ 9] [-4.601968,-0.953284) = 703
violations=207210 uncertain=0
first_violation s=0.05+16.0i value=-6.281573984651e-1 bound=4.057e-10 distance=1.918789 mpmath40=MANUAL RECHECK REQUIRED
VERDICT: FAIL — UHDC refuted on scanned grid [CHECKED NUMERICALLY]
```

The centered statistic is not near zero and drifts more negative: first-third mean `-10.2825`, last-third mean `-13.0660`. This is consistent with the conjecture having the sign/background convention reversed, but that diagnosis is **CONJECTURED**, not established by this scan.
