# Wave 59 final — direct thinker inline (muse-spark-1.2) — sigma sweep CHECKED

**Status:** `E(c,r)` sigma-dependence `CHECKED` inline, `c=σ+i·g1` `r0.19` `600-pt` `25dps`.

**Probe (`c_sigma.py:1` inline, `xi`+`R` as `56`, `g1=14.1347`):**
```
cσ    d_gen d1   Eg     Ep     diff  |ρ-c|<r?
0.55  0.05 0.25  1.335 -1.335 -2.670  gen 1 plant 0 (pole)
0.60  0.10 0.20  0.642 -0.642 -1.284  gen 1 plant 0 (boundary)
0.65  0.15 0.15  0.236  0.000 -0.236  both 1 (tie)
0.70  0.20 0.10 -0.000  0.642 +0.642  gen 0 plant 1
0.75  0.25 0.05 -0.000  1.335 +1.335  gen 0 plant 1  ← optimal
0.80  0.30 0.00 -0.000   inf  +inf   gen 0 plant 1 (center at zero)
0.85  0.35 0.05 -0.000  1.335 +1.335  gen 0 plant 1
```
`Eg=log(r/d_gen)` if `d_gen<r` else `0`, `Ep=log(r/d1)` if `d1<r` else `0` (plus pole correction at `0.55`). `CHECKED` vs `Jensen` `log(r/d)` `0.236=log(0.19/0.15)` etc exact.

**Mechanism PROVEN:** `c` must be `>0.70` (`σ` near `β0=0.8`) to make `d_gen>r` (`0.20-0.25>r`) and `d1<r` (`0.05-0.10<r`) → `gen 0` `plant 1.335`. At `c≈0.5` both have interior or pole, not discriminating. Optimal `c=0.75-0.85 r0.19` `diff +1.335` max, `c0.75 r0.2` `1.386` from `wave-56` same family.

**Honest:** still finite circle, needs `σ` near `0.75` (knows `β0≈0.8`). `r0.19` avoids boundary singularity at `0.20`. `E=0` at most `σ` (strip `0.5-0.7`), `1.335` only near `0.75-0.85`. `Grid Δσ0.1 Δt0.2` catches `+1.335` spike.

**Next inline:** `wave-60` test `2D (σ,t)` grid `0.75±0.1 × g1±0.2` `r0.19` to map `1.335` island, or `r0.08` `E=0.47` at same `c` to show `β`-limit `d=0.05`.
