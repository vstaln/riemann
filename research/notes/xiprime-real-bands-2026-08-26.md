# ξ′ real-band certification — N_k on actual zeta data, heights γ₁..γ₆

Author: builder subagent, 2026-08-26. Mission: first REAL-ξ′ certification run.
Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED.
Runtime: `uv run --with mpmath python3 research/scripts/xiprime_real_bands.py`.
Related notes: `speiser-probe-2026-08-25.md` (method machinery), `speiser-negativity-program.md`
(proves Re(ζ′/ζ)<0 in 0<σ<1/2).

## 0. Contract (mission spec, treated as hypothesis under test)

Speiser equivalence: **RH ⟺ ξ′(s) has NO zeros in the strip 0 < Re(s) < 1/2.**
Certification statistic: N_k := (1/2πi) ∮ ξ″/ξ′ ds over the rectangle
**[0.25, 0.49] × [γk − 8, γk + 8]** for k = 1..6, where γk = Im of the k-th nontrivial
zeta zero. **RH predicts N_k = 0 for ALL k.** Any N_k ≥ 1 would be a seismic event
(a ξ′-zero strictly left of ½ near actual zeta height) — triple-check before believing.

## 1. Method — argument principle, bounded height, real data

f = ξ (the completed zeta function, entire, real on ℝ, ξ(s)=ξ(1−s)).
f′/f = l₁ = 1/s + 1/(s−1) − ½ln π + ½ψ(s/2) + ζ′/ζ  (no planting: R = 1),
f″/f′ = l₁ + l₁′/l₁,  l₁′ = −1/s² − 1/(s−1)² + ¼ψ′(s/2) + (ζ″ζ − ζ′²)/ζ².

N_k counts zeros of ξ′ strictly left of ½ near height γk (f′ = ξ′ is entire; its zeros
are exactly the poles of ξ″/ξ′; the rectangle Re ≤ 0.49 < ½ contains no zeta zeros, so no
pole of l₁ inside). Machine settings per mission: mpmath **dps = 15**, dense grid
**n = 2000 pts/side** on each of the 4 sides (8000 pts/band, phase unwrap).

Per-band outputs:
- **N_k** = round of winding number of ξ′(boundary) (primary, robust — sample-winding of
  ξ′ along the contour, the reliable method per speiser-probe; min|ξ′| on contour recorded
  to flag near-contour zeros/poles),
- **negativity margin** = min over the 2000 left-edge samples (Re = 0.25) of Re(ξ′/ξ)
  (should be < 0 under RH, per the paired-Hadamard sign lemma),
- **wall-clock** per band.

Triple-check protocol (armed only if any N_k ≥ 1):
(a) independent mp.quad of ξ″/ξ′ over the same rectangle (tanh-sinh, maxdegree=8),
(b) halved window [0.25,0.49] × [γk ± 4], n = 2000/side — same count expected if the
zero is real and inside, different if the count is a boundary/numerics artefact.
Also: winding machinery self-check per band (winding of s − c inside = 1, shifted = 0).

## 2. Results — [appended on completion]

## 3. Verdict — [appended on completion]
