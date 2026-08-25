# Two-tone window lead REFUTED (documented negative)

**Date:** 2026-08-12. **Status:** ABANDONED (with rigorous reason).
**Labels:** all eps bounds PROVEN (interval-certified by the extended verifier);
the resulting conclusion is PROVEN.

## The lead that was refuted
`exec-two-tone.md` (from the two-tone Rust sweep) found window v(s)=cos(1.407s)+0.005·cos(2.53s),
psum=1/300, m=135 giving H=0.672500703285 and a *nominal* bound 0.6745091758911242
(+1.25e-3 over the certified record 0.6732628655343560). [RETIRED 2026-08-24]
**But** that bound assumed eps=0.00806 was achievable at psum=1/300 (label: CONJECTURED).

## The rigorous check (verifier extended to two-tone windows)
The verifier tools/beat673/verify_cos7.py was extended to two-tone windows
(closed-form kernel K(x) = sum of sinc terms; copy at tools/beat673/verify_twotone7.py).
At the winning config (A=1.407, B=2.53, c=0.005, psum=1/300 → per-gap p=1/1800):

| target eps | verifier lower bound at terminal | verdict |
|---|---|---|
| 0.006145 | 0.0061318 | FAIL |
| 0.006140 | 0.0061273 | FAIL |
| 0.006130 | 0.0061164 | FAIL |
| 0.006120 | 0.0061060 | FAIL |
| 0.006110 | 0.0060968 | FAIL |

**Max certifiable eps ≈ 0.00607**, well below the required 0.0061357 to beat the record,
and far below the CONJECTURED 0.00806.

## Why it fails (the mechanism)
Lower pressure psum=1/300 cannot support a high local floor F ≥ eps. The eps floor grows with
pressure, but the bound's tax τ = psum·(m−6)/m grows with pressure too — the previous record's
psum=1/220 was chosen at the sweet spot. The two-tone window's higher H (0.67250 vs 0.67242)
is more than eaten by the lower achievable eps at the lower pressure.

## What this teaches (transferable)
1. **A higher H-window alone cannot beat the record** — the eps floor is the binding constraint,
   and it couples to pressure. Any new window must be verified at the SAME psum as the record
   (or its eps achievability proven), or the nominal gain is illusory.
2. The **n-point generalization** (more gaps, higher n) remains the untested lever that could
   genuinely raise eps — it changes the local functional structure, not just H.
3. The single-cosine at alpha=1.49, psum=1/220, eps=0.00806 is confirmed **at the certified
   boundary** (eps-max runs: 8067/1e6 fails, 8060/1e6 verifies) — the record is tight.

## Where the code lives
- Two-tone verifier: tools/beat673/verify_twotone7.py (extension of verify_cos7.py)
- Two-tone H sweep (Rust): /tmp/two-tone/ and tools/two-tone-sweep/
- eps-max boundary runs: /home/vstaln/riemann/research/waves/wave-local/results/exec-eps-max-runs.log

## Verdict
The 0.6745091759 lead is NOT real (REFUTED). The certified record 0.6732628655343560 stands. [RETIRED 2026-08-24]
Next best moves: (a) n-point generalization, (b) eps-max at nearby (alpha, psum) — already shown
tight — (c) structurally new inequalities (higher moments, per the theorist track).
