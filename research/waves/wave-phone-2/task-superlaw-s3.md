# TASK: Super-law + S₃ rigidity probe (top-ranked idea from the ceiling ideator)

## Mission
The swarm's #1 idea: the phase-randomized super-block construction (union of scaled GUE blocks) already matches mean density, in-band form factor F≡1 on [0,1], Selberg-CLT fluctuations, and variance — with simple fraction exactly p₀ = 0.68182868746. Because its blocks are GUE, its triple correlation S₃ should equal the sine-kernel value at λ<2/3 essentially for free (inter-block contributions vanish). If so, pinning S₃ does NOT move the ceiling — "0.6818 impassable by proven inputs" becomes a theorem without the private 256-family. Probe it numerically.

## Context — read first, do NOT re-derive
- `research/waves/wave-phone-local/results/ceiling-ideas.md` idea #1 (the super-law/S₃ rigidity construction and its failure modes)
- `research/notes/attack-selberg-clt.md` §3 — the super-block construction; the probe code `s_probe.py` lives in `research/notes/attack-selberg-clt/`
- `research/notes/regenerate-256law.md` — the marked-config machinery + the private-data wall (sha256 cc3de991…)
- Sine-kernel triple correlation (Rudnick–Sarnak / Hejhal, kλ<2/3):
  R₃(α,β) = 1 − sinc²(πα) − sinc²(πβ) − sinc²(π(α−β)) + 2·sinc(πα)·sinc(πβ)·sinc(π(α−β)), sinc(x)=sin(πx)/(πx)

## Environment
Phone Python: `proot-distro login ubuntu -- python3` (mpmath 1.4.1, numpy 2.3.5). Keep blocks small enough to finish < 20 min.

## The work (CHECKED NUMERICALLY, script + command cited)
1. Reconstruct the phase-randomized super-block law per attack-selberg-clt.md §3 (scaled GUE blocks; tune the simple fraction to p₀ = 0.68182868746; mark fraction 1 vs 2 per the construction). Verify it reproduces: mean density, in-band F on [0,1] within tolerance, simple fraction p₀.
2. Compute the law's S₃ at 2–3 points in the Rudnick–Sarnak range (λ<2/3; AVOID the diagonal β=α where R₃≡0) and compare to the sine-kernel value. Report measured vs predicted + deviation.
3. Adversarial: quantify the law's S₃ deviation at the precision the certificate needs (near-CUE rows are certified to ~3·10⁻⁴⁰; the super-law is finite — how big is its S₃ deviation, and does it matter?).
4. (If time permits) add an S₃ row to the N=64 marked-config LP (rgl machinery in regenerate-256law.md) and check the optimum stays at p₀(64).

## Deliverable
`research/waves/wave-phone-2/results/superlaw-s3.md` — construction, 4 verification numbers, S₃ comparison table, verdict (does the super-law match S₃ = sine-kernel? does pinning S₃ move the ceiling?).

## Ponytail (hooks/agents.md §PONYTAIL)
Smallest probe that decides. REUSE s_probe.py and the existing super-block code — do not rewrite it. One runnable self-check. Numbers first, ≤3 lines of prose.
