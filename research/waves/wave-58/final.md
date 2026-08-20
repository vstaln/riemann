# Wave 58 final — direct thinker inline (muse-spark-1.2, no swarm) — r-sweep CHECKED

**Status:** `E(c,r)` r-tunable still `>0` even at `r→d+` — `CHECKED` `muse-spark-1.2` inline.

**Probe (`r008.py:1` inline, `c=0.75+ig1 g1=14.1347 d=0.05` `R` as `wave-56`, `25dps` `800-pt`):**
- `r0.20 E=1.3863=log4`, `r0.15 1.0986=log3`, `r0.12 0.8755=log2.4`, `r0.08 0.4700=log1.6`, `r0.06 0.1823=log1.2` — `E=log(r/d)` `PROVEN` Jensen, `CHECKED` exact `800-pt`.
- `r0.06` still `0.182>0` (`r` just `0.01` above `d=0.05`), `β`-resolution limit is `d` (`0.3` off-line). Smaller `r` → narrower `t`-window (`r=0.06` `dt<0.03` to stay inside) but stronger `β` localization.

**Mechanism PROVEN:** `E=log(r/|ρ1-c|)` when `|ρ1-c|<r` else `0`. `r` can be shrunk to `d+ε` to make `E= log(1+ε/d)≈ε/d` small but `>0` — tradeoff `r↓` ⇒ `Δt↓` (need `~T/2r` circles) vs `β`-precision `↑`.

**Honest:** `r0.06` needs `Δt≈0.06` grid (`~16·T` circles) vs `r0.2` `Δt0.2` (`~5·T`), both `finite-height` `O(T log T)` like `Platt 3e12`, not proof. `E>0` still needs `t` near `g1` (`±0.06` for `r0.06`), location info like wedge.

**Next inline:** `wave-59` test `c=0.60+ig1 r0.2` (`d=0.20` `E=0`? `|0.5+ig1-0.60|=0.10<r` but `ρ1` distance `0.20` on boundary) to show `E` jumps at `σ` crossing `β0`.
