# ATTACK RECORD — record 0.673262865534356… (eps-max push + artifact probe) [RETIRED 2026-08-24]

**Session:** wave-phone-2 / executor attack-record. **Start:** 2026-08-12 (after mobile-data loss of prior run).
**Mission:** (1) resolve the eps boundary at grid=4000 (8065 certify/fail?), (2) artifact probe: does a finer grid (6000/8000) move the certified max eps, (3) recompute bound at any improved certified eps, (4) adversarial formula re-check at m=133.
**Deliverable contract:** this file, appended after every result. Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE.

## Seeds from the prior (killed) run + wave-local log
- `exec-eps-max-runs.log` (wave-local): p=1/1320 (psum=1/220, α=149/100): 8063/1e6 True (282s, 1015132 nodes), 8064 True (450s, 1116906), 8066+ all False (8067/8070/8075/8081/8090/8102/8120/8145/8180/8230). p=1/1350 (psum=1/225): max True = 7909/1e6 (197s).
- Prior run (killed): grid=4000 re-verified 8060/1e6 certifies at 942,944 nodes; 8066/1e6 FAILS; 8065 in flight when it died.
- Discovery note: eps=0.00806 certifies, 942,944 nodes, all pruned, max_depth 64, ~300s. Verifier = `/tmp/combine/verify_cos7.py` (Arb via python-flint, 410 lines) on the laptop.

## Running log
(append after every result)

---
## Result 1 — Adversarial formula re-check at m=133 (DONE, CHECKED NUMERICALLY)
Script: `scripts/attack_bound_check.py` (mpmath 160/220 dps) + inline 220-dps re-derivation.
Command: `proot-distro login ubuntu -- bash -lc 'cd ~/riemann/.../scripts && python3 attack_bound_check.py'`
- H(1.49) = 0.67242188609644747281039838018029596113320575516194…
- τ = (1/220)(127/133) = 0.00434039644565960355434039644565960355434… (rational, diff 0)
- A = 0.00806·127 = 1.02362; B = Φ_133(A) = 1.023557109402758221390751244754121476959… (A > 127/126 = 1.00794, so the sqrt branch applies: B = 2√((m−1)A/m) − 1 + A/m)
- bound = (H−τ)/(1−B/m) = 0.6732628655343560146453680008533435193197122483889… [RETIRED 2026-08-24]
- HEADLINE REPRODUCED to all 42 printed digits; residual vs printed value 3.889e-46 = truncation of the note's 120-digit print, not a formula failure.
- Monotone in eps at m=133 confirmed: 0.00806→0.6732628655, 0.008065→0.6732660791, 0.00807→0.6732692918, 0.00808→0.6732757142, 0.0081→0.6732885476, 0.00813→0.6733077692, 0.00816→0.6733269567. [RETIRED 2026-08-24]
- Any certified eps > 0.00806 → bound > 0.6732628655 immediately (per-eps gain ~ +3.2e-4). [RETIRED 2026-08-24]

## Verifier runs (laptop nohup, grid artifact probe) — LAUNCHED, results pending
`/tmp/combine/attack_run.sh` on pc-jump via pc-jump (nohup, crash-proof), log `/tmp/combine/attack_results.txt`:
eps8065_g4000 → eps8065/8066/8068/8070 @g6000 → eps8065/8066/8068 @g8000.
(Command template: `uv run --quiet --with python-flint python3 verify_cos7.py 149 100 1 1320 <T> 1000000 - <GRID>`)

## Verifier relaunch (fixed uv path)
- First nohup attempt failed: `uv` not on non-login PATH (rc=127). Found `/home/vstaln/.local/bin/uv`.
- Another agent (beat673) is running the same verifier from `/home/vstaln/riemann/tools/beat673/verify_cos7.py` (identical to /tmp/combine copy, diff SAME). 8 cores, ~6GB free.
- Relaunched `/tmp/combine/attack_run2.sh` (nohup) — order: 8065@g4000, then 8066/8068/8070@g6000, 8065@g6000, 8066/8068@g8000, 8065@g8000. Log: `/tmp/combine/attack_results2.txt`.

## Result 2 — CERTIFIED NEW RECORD (grid=4000, eps=0.008064) — CHECKED NUMERICALLY
From wave-local log: `cert alpha=149/100 p=1/1320 target=8064/1e6 -> verified=True (450s) nodes=1116906` (grid=4000 verifier, default uniform-span weights). eps=8063/1e6 also True (282s). Prior killed run independently re-confirmed 8060 (942,944 nodes, matching discovery note).
At eps=0.008064, m=133: bound = (H−τ)/(1−B/m) =
**0.67326543649552352207990181282271996377681849486392** (mpmath 120d, script `scripts/attack_bound_check.py` inline; H=0.672421886096447472810398380180295961133205755, A=1.024128, B=1.02406108048356053160742615965953979941209469, τ=(1/220)(127/133)=0.00434039644565960355434039644566).
**GAIN over record = +2.5709611675074345e-6. NEW RECORD: True.** m=133 optimal (m=132: 0.6732653839, m=134: 0.6732653277).
Caveat: eps=0.008064 certification comes from the wave-local log (same verifier, grid=4000); re-certification in-flight in parallel runs is 8065@4000 + finer-grid probes.

## Result 3 — Sweep at OTHER certified eps (CHECKED NUMERICALLY, bound arithmetic only)
- (α=1.47, psum=1/220, eps=0.007985): NO m in 128..139 beats record.
- (α=1.49, psum=1/225, eps=0.007909): m=135,136 beat record (0.6732629498, 0.6732629169) but both < 0.6732654365 leader.
- (α=1.45..1.53 × m=130..140 × psum 1/220/1/225 at certified eps): max = 0.6733277419 at (α=1.45, m=133, psum=1/220, eps=0.008064) — BUT α=1.45's certified eps is NOT established (only α=1.49 certifies 8064; α=1.47 max ~7985). INCONCLUSIVE as certified; would need verifier runs at α=1.45. Flagged, not counted.

## Grid artifact probe — in flight (laptop nohup)
Runs started 16:50:55 (parallel, 6 workers): 8065@g4000, 8066/8068/8070@g6000, 8065@g6000, 8066@g8000. (8068@8000 and 8065@8000 deferred.)

## Result 4 — ARTIFACT PROBE #1: eps=0.008070 at grid=6000 FAILS (CHECKED NUMERICALLY, verifier)
`verify_cos7.py 149 100 1 1320 8070 1000000 - 6000` → verified=False, terminal box
((6316,6316),(11945,11945),(11895,11895),(6280,6280),(11857,11857),(6301,6301)) lower=0.008060649099672502,
max_depth=81, pruned=146518, interval=124317, tangent=21644, elapsed ~3.6 min.
**Finer grid (6000) does NOT raise the certified floor: 0.008070 fails at g6000 with the same ~0.0080606 floor.** The box coordinates are exactly grid-scaled versions of the g4000 failing boxes (coords × 1.5) — same terminal region, grid-refined.
