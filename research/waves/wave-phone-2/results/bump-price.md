# bump-price.md (phone-2 wave, EXECUTOR, v2) — decompose & price the α∈[1.0,1.3] bump

**Status: INCONCLUSIVE (turn limit hit before computation ran).** Script written and
environment verified; the run itself did not execute. This is a blocker report per
hooks/agents.md — NOT a fabricated result.

## What was done (all verifiable)

1. **Read** hooks/agents.md, attack-ls-estimator.md, attack-hot-hand.md,
   attack-pricing-sheet.md (§5–6) — full context loaded.
2. **Environment resolved:** this phone runs Termux (no uv, no numpy on host python3.14);
   `~/riemann` is a symlink into the proot Ubuntu rootfs
   (`proot-distro login ubuntu -- python3 ...`), where numpy 2.3.5 + scipy 1.18.0 exist and
   the canonical zeros `tools/data/zeros_computed_10000.txt` (10 000 ordinates) + cached
   `zeros_1_1000.txt` are present.
3. **Script written:** `results/bump_price2.py` (self-contained, appends to
   `bump_price2.log`), covering the full task: reproduce F̂ on [1.0,1.3] at N=1e3/3e3/1e4,
   adjudicate the notes' conflict (LS-note F̂(1.00)=1.378 vs hot-hand 245.84 on the same
   data — resolved by direct computation), compute the RIGOROUS e≥2 prime-power diagonal
   plane-wave sum D(α)=Σ (log p)^e/(p^{e/2} L)·cos(2πα·e·log p/L) (Guinand explicit
   formula; absolutely convergent, unconditional), correlate F̂−1 with D on the band,
   and price under M2 (p₁(1.3)=1−(1−p₀)/1.3², dv*/dA=0.6363/A³) and M3 (8.49e-4/unit δ at
   ε=0.02).

## Key facts established during setup (CHECKED, environment-level)

- The 10k zeros file exists (10000 ordinates, `tools/data/zeros_computed_10000.txt`).
- Run command (verified numpy/scipy present): `proot-distro login ubuntu -- bash -c
  'cd /root/riemann && python3 research/waves/wave-phone-2/results/bump_price2.py'`
  (~seconds at N=1e4 for periodograms; τ-bin loop not needed for the plane-wave D).

## What remains (blocker, 1 step)

Run the script, read `bump_price2.log`, then fill in the verdict sections below. Expected
math (from the read notes, PROVEN there, not recomputed here): M2 Δ = p₁(1.3)−p₀ =
0.8098−0.6818 = **+0.1280** (lands above 0.80, far above 0.70); the e≥2 diagonal terms are
measure-zero point spikes in α (heights ~ (log p)²/(pL)·N/(4π²L²) ~ 1e-3–1e-2), so D(α)
cannot be ≥1+δ on a positive-width band — the "rigorous sliver" fails at the level check
unless F̂−1 correlates with D's local spikes (test in script).

## Honesty footer

Nothing in this note reports a computation that did not run. The only numbers quoted are
from the read notes (labeled there CHECKED NUMERICALLY / PROVEN) or environment checks.
Labels: INCONCLUSIVE (blocker: turn limit before run). Next agent: run the command above.

## VERDICT (computation completed, phone proot, bump_price2.py — all numbers from the run log)

**RESOLVED — the α∈[1.0,1.3] "bump" is the isolated α=1 arithmetic spike, NOT a beyond-1 band effect. No certified price. The rigorous beyond-1 sliver FAILS at the level check.**

1. **DECOMPOSE / adjudicate the notes conflict:** F̂(1.00) = **245.8** at N=10000 (hot-hand's 245.84 was right; attack-ls-estimator's 1.378 was a mis-scaled estimator). Anchors N=10000: [1.00: 245.84, 1.05: 1.358, 1.10: 0.402, 1.25: 1.292, 1.30: 1.924]. Excluding α=1: fine-grid band (1.005,1.3] mean(F) = 1.056 (N=10000) / 1.168 (N=1000), band-mean z = **+0.43 / +0.92** (n_eff 59/30, sigma 0.130/0.183) — **sub-significant**. The ≥11σ claims in the source notes measured the single-point α=1 spike (F−1 ≈ 244σ at that α), not a band excess.
2. **RIGOROUS e≥2 prime-power diagonal (Guinand explicit formula, unconditional):** D(α) = Σ (log p)^e/(p^{e/2}L)·cos(2πα·e·log p/L): at N=1000: 28 terms, on-band 12, |D| ≤ 0.0333, mean −0.028; at N=10000: 51 terms, on-band 23, |D| ≤ 0.0255, mean −0.023. Heights ~1e-3–1e-2 — measure-zero point spikes. **corr(F̂−1, D) = −0.098 (N=1000) / −0.029 (N=10000) — no shape match.** D cannot deliver F ≥ 1+δ on a positive-width band (needs δ ~ O(1); D ≤ 0.03). **The "candidate unconditional beyond-1 read" is dead at the level check.**
3. **PRICE:** M2 Δ = p₁(1.3) − p₁(1) = 0.81173 − 0.68183 = **+0.1299** — but ONLY if F ≥ 1+δ is certified ON THE BAND; band read is z = +0.43 → **no certified band F ≥ 1+δ, no M2 price**. M3 pointwise: dp₁/dδ = 8.49e-4 (1+0.02) … 1.24e-3 (1+0.5); 0.70 needs δ = 14.6–21.4 units — unrealistic (realistic O(1)) → pointwise gain ~8.5e-4, negligible.

## Honesty footer
All numbers above are from `results/bump_price2.log` (script `results/bump_price2.py`, run on the phone proot 2026-08-12; zeros = tools/data/zeros_computed_10000.txt). Labels: CHECKED NUMERICALLY (all). The M2 band-price reasoning is from attack-pricing-sheet §5 (PROVEN there as the pricing mechanism). Verdict completes v1's blocker report (v1 died before the run; the v2 agent died at the final write — the run log was complete; the verdict sections were appended by the orchestrator from the log).

RESULT: RESOLVED-NEGATIVE — bump = isolated α=1 spike (hot-hand right, LS 1.378 mis-scaled); band excess z ≤ 0.92 sub-significant; rigorous e≥2 terms |D| ≤ 0.033 no correlation; beyond-1 band price NOT certifiable; M3 pointwise negligible. Door: closed on this evidence.
