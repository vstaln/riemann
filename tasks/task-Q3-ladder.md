# Task: Q3 — The consecutive-zeros ladder: how far does 3 → 7 → 9 → 11 go?

## Role
EXECUTIONER (numerics-first). Read `research/notes/discovery-gram-stability-673.md`, PLAN.md,
hooks/agents.md first.

## Context (self-contained)
The external stability refinement for SIMPLE zeros of ζ works like this: with the Montgomery–Taylor
overlap kernel k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2t)cos(2πxt)dt, the rank–trace
inequality's equality case would need simple-zero atoms to be mutually orthogonal, which the kernel
forbids. The refined inequality carries an extra positive term tr Ψ(M) ≥ ε > 0, where the positivity
is certified via "pressure" functionals on consecutive gap blocks:

- **3-point:** over (u,v), u,v ≥ 0, u+v ≤ 4 (pairwise differences u, v, u+v of 3 consecutive
  zeros), a certified bound ε₄ ≥ 221/10⁶. Plugging in: constant = (H0 − ε/4)/(1 − ε/2) with
  H0 = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573 → **67.2519767%**.
- **7-point:** over six consecutive gaps (u₁..u₆ ≥ 0, with 21 pairwise differences), a weighted
  six-variable bound ≥ 19/5000 = 0.0038 with coefficients c_s = 2/(7−s), s = number of gaps crossed
  by a pair. Plugging in: constant = (1345000·H0 − 2680)/1340003 → **67.3008528%** (ainta) /
  67.3137630699% (trmdy, different window) / 67.3192911473% (tawanerguo, coboundary, m=183).

**Q3 asks:** how far does the ladder go? 9 consecutive zeros (8 gaps)? 11 (10 gaps)? Is there a
limit as the block size grows, and does it approach something meaningful (e.g. the in-class ceiling
0.6818, or a natural kernel-dependent value)?

## Tasks (numerical; estimates labeled CONJECTURED unless certified)
1. **Reconstruct the pressure functionals.** From the description: for a block of n consecutive
   gaps, the functional is a weighted sum over pairs of kernel values at the pairwise differences,
   minimized over the gap domain (Σgaps ≤ 4 presumably; check both Σ≤4 and Σ≤H for H=4 and the
   natural bound from the kernel support). Get the 3-point and 7-point versions to reproduce the
   documented minima (221/10⁶ and 19/5000) — if you cannot reproduce them, that itself is a
   finding (the coefficients or domain may differ; document what reproduces what).
2. **Extend to 9 and 11 points.** Build the n-point functional (generalize c_s: for n zeros there
   are C(n,2) pairs, s = number of gaps between the pair, coefficient c_s = 2/(n−s) is the natural
   guess from the 7-point pattern — verify against the 3-point and 7-point cases first!). Minimize
   over the gap domain with:
   - dense random sampling (numpy, 1e5–1e6 points, vectorized),
   - then scipy local refinement (L-BFGS-B / differential_evolution on a few hundred starts).
   Report the best minima for n = 3, 7, 9, 11 and the implied constants via the appropriate
   plug-in formula (derive the general formula (H0 − f(ε))/(1 − g(ε)) from the 3-point and 7-point
   cases — match both).
3. **Trend & limit.** Fit the ladder; try n = 13, 15 if cheap. Does εₙ grow, plateau, or decay?
   (Note the kernel k decays slowly; the number of pairs grows like n², so the sum may grow — the
   relevant object is the weighted pressure, check its normalization.) State the conjectured limit
   and its implied constant.
4. **Honesty.** The certified versions used Arb interval arithmetic (python-flint — NOT installed on
   the phone; do not try to install). Your minima are numerical estimates with sampling error:
   label them CHECKED NUMERICALLY (estimate, not certificate). If a minimum is suspiciously close
   to the certified bound, flag it as "certified bound plausibly tight — needs Arb run on laptop".
   Document the exact commands for a certified rerun.

## Deliverables
- `research/notes/ladder-consecutive-zeros.md` — the ladder table (n, min pressure, implied
  constant), trend analysis, labels, and the exact commands for certified reruns.
- `tools/ladder_pressure.py` — vectorized; reproduces 3-point and 7-point before extending; runs
  < 10 min.

## Compute budget
< 10 min wall. n=11 with 1e6 samples over 10 dims is heavy — use smart sampling (concentrate near
the 7-point minimizer region, exploit that minima sit at the domain boundary), or reduce samples
and be honest about the resolution.
