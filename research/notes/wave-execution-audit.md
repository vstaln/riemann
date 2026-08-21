# Wave Execution Audit — Are we DOING compute or BURNING TOKENS?

**Date:** 2026-05-11
**Status:** REFINED v1 — 6 reads (swarm.py, jensen_probe/main.rs, jensen_probe/Cargo.toml, alien_probes bins, wave-159/158 executor+verdicts)
**Labels:** PROVEN = code read + output on disk; CHECKED NUMERICALLY = numbers from cargo run logs; CONJECTURED = inferred

## Verdict: DOING STUFF — with ~50% alias-stub leakage (mislabeled, not fake)

Executor **does** shell out to Rust and does **real** <1min compute. Not a token-burn loop. Leakage is at the *label* layer: 11 `jensen_probe` [[bin]] entries in `tools/jensen_probe/Cargo.toml` all point to the **same** `src/main.rs`. Bins named `li_feedback_gain`, `turan_debranges_jensen`, `li_jensen_laplace`, `li_debranges_turan`, etc. compute **only Jensen E** and append the warning `Li/Turan probe: this binary currently only reports honest Jensen E` — yet prompt whitelists them as DIRECT-RH Li/Turan discriminants and verifiers count them as VERIFIED.

Alien probes (`kolmogorov_prime`, `diffraction_logp`, `coulomb_energy`, `persistence_zero`) are **separate real binaries** (`tools/alien_probes/src/bin/*.rs`), not aliases — they do distinct N-body compute.

## Evidence Table

| # | Check | File / Function | Real or Stub? | Evidence (PROVEN) |
|---|---|---|---|---|
| 1 | Executor shells out | `tools/swarm_langgraph/swarm.py: make_executor` L~380, `_run_rust` L~720, `_binary_exists` L~680 | **Real** | `if rust_cmd and _binary_exists(rust_cmd): out = _run_rust(rust_cmd, timeout=cfg["rust_timeout"])` → `subprocess.run(["bash","-lc",cmd], timeout)` with 124/timeout kill. Else emits `NO BINARY (...) Label INCONCLUSIVE` which verifier kills. Not a CONJECTURED emit when binary exists. |
| 2 | Manifest injection | `swarm.py: _binary_exists`, `_run_rust` | **Real (fixed)** | Scans `tools/**/Cargo.toml` for `name="<bin>"` or `[[bin]] name`; rewrites `cargo run` → `cargo run --manifest-path <found>` if missing. Fixes old wave-79 bug where `command -v cargo` always True → exit 101. Checked in code. |
| 3 | jensen_probe computes honest E | `tools/jensen_probe/src/main.rs` lines 1–220 | **Real** | Loads `tools/data/zeros_rust_100k.txt` (100k zeros), computes `E(c,r)=sum log(r/|rho-c|)` per center T, handles planted `(beta0,t0)` with `remove_nearest`, prints `E_RH`, `E_false`, `gap`, `Re_distance_RH`, `in_disc` flags. Example `wave-159` log: `E_RH=0.182322 E_false=1.098612 gap=0.916291` with `Finished in 0.02s`. Not LLM text. |
| 4 | li/turan bins are aliases | `tools/jensen_probe/Cargo.toml` + `src/main.rs` tail L~170 | **Alias / Stub** | Cargo.toml: 11 `[[bin]]` all `path="src/main.rs"` (`jensen_probe`, `nyman_jensen_hybrid`, `li_feedback_gain`, `turan_debranges_jensen`, `li_jensen_laplace`, `li_debranges_turan`, …). Tail: `if bin.contains("li_")\|\|bin.contains("turan") { println!("Li/Turan probe: this binary currently only reports honest Jensen E; Li lambda_n / Turan Delta require separate zero-sum (not yet implemented)") }`. Whitelist advertises them as Li/Turan but they are Jensen E. |
| 5 | Alien probes real | `tools/alien_probes/src/bin/kolmogorov_prime.rs`, `diffraction_logp.rs`, `coulomb_energy.rs`, `persistence_zero.rs` + `Cargo.toml` | **Real** | Separate package `alien_probes` with 4 distinct mains: `sieve + lz76`, `S(k)=|Σ exp(i k log p)|^2`, `Σ log|rho_i-rho_j|` Coulomb, `persistence_zero` H1 hole_gain. `wave-158` executor-0: `alien diffraction_logp N=...` and `alien coulomb_energy/persistence_zero` produce distinct outputs, not Jensen E. |
| 6 | Prompt routing | `swarm.py: GEN_ANGLES` + whitelist L~240 | Mixed | Whitelist lists 14 DIRECT-RH jensen-family + 4 alien; template `cargo run --bin jensen_probe -- --c-re 0.75 --r 0.30 --planted-beta 0.80 --centers 14.1347,...` is correct and used verbatim in waves. |
| 7 | Verifier anti-inflation | `swarm.py: make_verifier` L~450 | **Real but blind to alias** | Kills `label CONJECTURED/INCONCLUSIVE → INCONCLUSIVE` pre-LLM and demotes `INCONCLUSIVE+VERIFIED→INCONCLUSIVE`. This prevents wave-78 false VERIFIED. But alias bins arrive as `CHECKED NUMERICALLY` (exit 0) + Jensen numbers, so verifier treats them as Jensen hybrids and VERIFIEDs them (e.g. `wave-159 g2-0 VERIFIED: log(0.2/0.10)=0.693147` for `li_feedback_gain`). |

## Recent Waves: Are rust_cmd outputs real?

**YES — numbers are real Jensen E, not stub message `this binary currently only reports honest Jensen E` alone.** The stub message is *appended* after real numbers.

- **wave-159:** `results/executor-0.md` 4 claims, `executor-1.md` 4 claims (8 total, 0 INCONCLUSIVE claims). Each shows `exit 0`, `Finished in 0.02s`, and lines like `T=14.1347 E_RH=0.182322 E_false=1.098612 gap=0.916291` (CHECKED NUMERICALLY). Two of four per file carry trailing `Li/Turan probe: this binary currently only reports honest Jensen E` (`li_feedback_gain`, `turan_debranges_jensen`, `li_jensen_laplace`, `li_debranges_turan`) — 4/8 = **50% alias outputs**. `verdicts.md`: 4 VERIFIED, 0 REFUTED, 0 INCONCLUSIVE. One VERIFIED (`g2-0 li_feedback_gain`) is alias counted as Jensen.
- **wave-158:** 8 claims (4+4), 8 VERIFIED, 0 REFUTED, 0 INCONCLUSIVE. `grep "only reports honest Jensen" executor-*.md` → 3 hits per file = 6/8 = **75% alias outputs** in grep count (head sample shows 1/4 per file clearly, remainder in truncated tail — CONJECTURED split). Includes real alien `persistence_zero` (`M=5000 VAR=0.239629 hole_gain=0.0128`) and real `jensen_weil_hybrid`/`nyman_jensen_hybrid`. Mixed real + alias.
- **wave-157:** 4 VERIFIED, 0 REFUTED/INCONCLUSIVE; 1/∼4 alias hits (25%).
- **wave-156:** 7 VERIFIED, 0 REFUTED/INCONCLUSIVE; 2+2=4 alias hits across executors (~50%).

Pattern: **Executor runs <0.1s Rust every time** (`Finished ... in 0.01–0.02s`), prints `DONE c_re=... E_RH(t0)=... E_false(t0)=... gap=... overall_ok=true`. When `li_/turan_` requested, same numbers + warning line. No wave in last 4 produced a pure stub with no numbers.

## Count Summary (last 4 waves)

| Wave | VERIFIED | REFUTED | INCONCLUSIVE | Executor claims | Alias-stub hits (`only reports honest Jensen`) | Stub ratio |
|---|---|---|---|---|---|---|
| 159 | 4 | 0 | 0 | 8 (4+4) | 4 (2+2) | 50% |
| 158 | 8 | 0 | 0 | 8 (4+4) | 6 (3+3) | 75% |
| 157 | 4 | 0 | 0 | ~4 | 1 (1+0) | ~25% |
| 156 | 7 | 0 | 0 | ~8 | 4 (2+2) | ~50% |
| **Avg** | — | — | — | — | — | **~50% alias leakage** |

No INCONCLUSIVE/REFUTED waves in this window — gate `_binary_exists` never fires (all bins exist as aliases), so verifier is the only filter and it lets alias Jensen through as hybrid.

## Is executor running <1min Rust or LLM text?

**Running <1min Rust (PROVEN).** Logs prove `cargo run --manifest-path tools/jensen_probe/Cargo.toml --bin X` completes in 0.01–0.02s dev profile, reads 100k zeros, computes E. Alien bins similarly <5s (`N≤800k` caps). No LLM-generated numbers — E values are deterministic (`log(r/d0)` etc.) and `in_disc_RH`/`in_disc_plant` flags match geometry (`Re_distance_RH=|0.5-c_re|`).

**Not burning tokens on stubs:** CPU burn is Jensen E every time; token burn is prompt + verifier LLM (~4–8 calls/wave). The waste is *reasoning* on mislabeled Li/Turan — synthesis may claim Li evidence when only Jensen was measured.

## One Fix

**Executor honest labeling (1 line, cheapest lever).** In `swarm.py: make_executor`, after `_run_rust`, downgrade alias outputs: if stdout contains `only reports honest Jensen E`, set `label = "INCONCLUSIVE"` or at least annotate `CHECKED NUMERICALLY (Jensen E only, not Li/Turan)` and include `ALIAS-STUB` tag; alternatively make `src/main.rs` li/turan bins exit 124. And shrink whitelist prompt: keep DIRECT-RH as `jensen_probe, jensen_weil_hybrid, nyman_jensen_hybrid, beurling_jensen_dist, arch_hessian_detrend, jensen_hessian_gamma, jensen_curvature_subtract, beurling_jensen_dist` as honest Jensen hybrids; move `li_feedback_gain, turan_debranges_jensen, li_jensen_laplace, li_debranges_turan` to a separate `REQUIRES zeta-rs` section or implement their real discriminants before whitelisting. This stops 50% VERIFIED inflation at the source without touching verifier or gate.

---
*Teams: executor trace via `_run_rust`+Cargo.toml, alias detection via Cargo.toml 11→1 mapping + tail println, wave counts via `results/executor-*.md`+`verdicts.md` grep. All numbers above copy-pasted from disk logs.*
