# TASK: BOX WORKER (oracle-old) — independent adversarial verification of the m₃-separation claim

## Mission (brain directive — funded line: m₃-separation)
Independently re-derive the numbers behind the m₃-separation claim. If the phone's super-law probe
shows the super-law's marked-windowed m₃ ≥ 5.44 vs the real zeros' PROVEN 5, that is a big claim —
it needs an INDEPENDENT implementation (different code path, different machine) before it counts.
You write your OWN code; do NOT copy the phone's probe.

## Context (read; the phone-side probe is in flight — you are the independent check)
- `research/notes/attack-law-s3.md` — marked S₃ = D + pair + T; D = 4 − 3p₀ = 1.9545139376
  (position-free); pair ∈ [3u, 6u], u(1/2) = 1.162449; pinned bottoms **5.4419 (λ=1/2)**, 3.9825 (λ=2/3)
  for ANY marked config with p₀ and near-CUE rows; matching sine-kernel forces connected part T ≤ −0.44.
- `research/notes/attack-twobandwidth.md` §2 — sine-kernel marked m₃: m₃(1/2) = 5, m₃(2/3) = 13/4 (PROVEN).
- `research/notes/attack-selberg-clt.md` §3 — the p₀-family construction (GUE super-blocks, per-block phases).

## Part 1 — REAL zeros: empirical windowed marked m₃ at λ=1/2 (CHECKED NUMERICALLY)
- First N = 3000 real zeros via mpmath zetazero (or python-flint if present). Unfold:
  x_n = N(γ_n) = (γ/2π)log(γ/2π) − γ/2π + 7/8 (mean spacing 1).
- Windowed marked m₃(λ): integrated marked triple correlation over the window W = [−λ,λ]²:
  m₃(λ) = (1/(#base)) Σ_i Σ_{j,k distinct ≠ i, x_j−x_i, x_k−x_i ∈ W} 1  (your own estimator; state it).
- Compare to the PROVEN 5 at λ=1/2. Report measured ± error (block bootstrap).

## Part 2 — SUPER-LAW: its windowed marked m₃ at λ=1/2
- Construct phase-randomized GUE super-blocks (numpy; eigen of GUE matrices), each block rescaled
  to mean spacing 1 **WITHIN the block** (per-block normalization — the phone found a known bug where
  global normalization gave mean spacing ~500 and counts → 0; do NOT repeat it; verify your block
  spacing empirically before trusting any count).
- Marks: fraction p₀ = 0.68182868746 of points mark-1 (simple), the rest mark-2 (double), arranged
  per the p₀-family (uniform random marks ok for the probe; state what you did).
- Windowed marked m₃ at λ=1/2 with YOUR estimator. Compare to 5 (real zeros) and to the pinned
  bottom 5.4419 (attack-law-s3).

## VERDICT (the adversarial output)
Does an independent implementation confirm: (a) real zeros' m₃(1/2) ≈ 5, (b) super-law's marked
m₃(1/2) ≥ 5.44 (separated) or ≈ 5 (not separated)? Report the numbers; flag any discrepancy with
the phone's numbers when they land (the phone pulls your note).

## Deliverable
`research/waves/wave-phone-2/results/box-m3verify.md` (+ your script saved alongside). Labels:
PROVEN / CHECKED NUMERICALLY / INCONCLUSIVE. Keep total < 35 min. Crash-proof: write the file EARLY,
append per part; bash < 90 s.
