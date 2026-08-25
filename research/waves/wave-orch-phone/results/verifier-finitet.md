# ROLE 4 — VERIFIER: adversarial analysis — can dropped finite-T terms flip 0.6732628655? [RETIRED 2026-08-24]

**Executed by:** orchestrator (inline) — Agent tool unavailable; VERIFIER role executed inline.
Labels per `hooks/agents.md`. All arithmetic CHECKED NUMERICALLY by
`results/verifier-finitet-flip.py` (`proot-distro login ubuntu -- python3 verifier-finitet-flip.py`,
mpmath 80 digits). Finite-T measurements from `results/executor-finitet-probe.py` (CHECKED NUMERICALLY).

## 1. The certificate is T-free (PROVEN, by inspection + arithmetic)

```
bound = (H − τ)/(1 − B/m) = 0.673262865534356…   (reproduced to 4.8e-14 by script) [RETIRED 2026-08-24]
  H(1.49) = 0.6724218860964     (window value, verified to 1.7e-41)
  τ = psum·(m−6)/m, psum=1/220, m=133            (exact rational)
  B = Φ_m(ε(m−6)), ε ← certified floor F ≥ 0.00806 (Arb interval verifier)
```
**No T-dependent quantity appears in the formula.** The finite-T content lives only in the
*derivation* of the machinery (Claim 2.1 Poisson completion, Lemmas 3.2/3.3), i.e. in what
"liminf_{T→∞}" forgets. This is the correct structure for a liminf statement: any finite-T dip
at accessible T does NOT refute it — only a finite-T error that survives as T→∞ with the wrong
sign would.

## 2. Margins and sensitivities (CHECKED NUMERICALLY, mpmath 80 digits)

| quantity | value | margin |
|---|---|---|
| bound vs tawanerguo (0.67319291…) | +6.995e-5 | **6.995e-5** |
| bound vs Theorem D (0.67250070…) | +7.622e-4 | 7.62e-4 |
| bound vs its own H (0.67242189…) | +8.410e-4 | 8.41e-4 |
| d(bound)/dH | 1.0078 | — |
| d(bound)/d(B/m) | 0.6785 | — |

Flip thresholds (to drop below tawanerguo): **H error ≤ −6.9e-5**, OR **B/m ≥ 0.007593**
(current B/m = 0.007696 — a margin of only **1.03e-4**, ~1.3% relative). B/m is the sensitive
lever, not H.

## 3. Adversarial verdict — can the dropped terms flip the record?

1. **Measured finite-T errors are POSITIVE (overshoot) at every T ≤ 5000** (executor probe,
   both windows): Δ = +0.040…+0.066 for α=1.49, +0.025…+0.051 for √2, decaying slowly.
   Magnitude 0.04–0.07 is **three orders of magnitude larger** than the 6.995e-5 record margin —
   but in the SAFE direction. A flip requires the dropped terms to be negative at T→∞ with
   |·| ≥ 7e-5 (record) or ≥ 1.0e-4 (B/m lever). **No negative-sign evidence exists in any
   probe** (this run, T≤5000; prior notes, T≤600).
2. **The B/m lever is the real attack surface**: ε is certified at the sharp boundary
   (0.00806 certifies; 0.008065–0.00807 fail — discovery-6732629.md). If a finite-T refinement
   forced ε down by ~1.3% (B/m from 0.007696 to 0.007593), the record falls to tawanerguo
   level. The certified floor is Arb-interval-rigorous, so this is not a numerics risk — but it
   means the *record's* lead is thin against B/m perturbations, not against finite-T effects.
3. **What would refute the certificate** (adversarial checklist): (a) a sign change of the
   derivation error at large T (needs T ≫ 10⁵ data, γ ≫ 10⁷ — out of reach); (b) a flaw in the
   interval verifier (out of scope here; verify_cos7.py is the agent's own implementation, not
   Lean — discovery note flags this); (c) the H value (verified to 1.7e-41 — safe); (d) the
   liminf ↔ certified-floor link (the floor is a T-free window property — safe).
4. **Verdict: CONJECTURED (robust).** All evidence — every measured T, both kernels — has the
   dropped terms positive (safe). The residual risk is (i) the asymptote level of Δ is
   INCONCLUSIVE (fits give 1/log²T intercept +0.01…+0.03, 1/logT intercept −0.016…0), and
   (ii) the probes use the *idealized* functional, not the block-refined one — a refined-
   functional probe at larger T is the outstanding check.

## 4. Hard-cutoff vs C∞ for the kernel question (from attack-kernel.md, PROVEN)

Cosine is the **global minimizer** of the window functional Q(v) over all L² windows on
[−1/2,1/2] (Lean-formalized; attack-kernel.md §2). Every C∞-smoothed variant has strictly worse
Q: 1.415 (ε=0.1), 2.20 (ε=0.5), 3.86 (ε=T/N) — and at accessible T the smoothed bound is
vacuous/negative (attack-finitet-cinf.md). **So a hard-cutoff kernel does not "beat" the cosine
at the window level — the cosine already is the optimum.** The only P6 opening left is a
different kernel × block-mollifier combination optimizing the *block* functional (bound=(H−τ)/(1−B/m)),
which has not been probed at finite T (open).

RESULT: CONJECTURED — 0.6732628655 is robust to finite-T (dropped terms positive/safe at all [RETIRED 2026-08-24]
T≤5000, flip needs ≥6.995e-5 negative error at T→∞, none seen); the sensitive lever is B/m
(margin 1.0e-4), and the block-functional finite-T probe is the outstanding check.
