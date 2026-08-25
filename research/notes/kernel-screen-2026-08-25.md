# Kernel screen — H(v) ranking for the multi-term kernel family

Date: 2026-08-25 · Status: **CHECKED NUMERICALLY (surrogate only, f64)** — no Arb certification.

## What was computed
H(v) = 2 − 1/c₁(v), c₁(v) = (∫v)² / (∫v² + ∫∫|s−s′|·v(s)v(s′)), v(s) = Σⱼ cⱼ cos(ωⱼ s) on
[−1/2, 1/2]. This is the kernel-agnostic definition behind
`tools/direction2_sdp/joint_c21_ft2.bound_from`'s single-cosine closed form
(I0 = ∫v, I2 = ∫v², J = ∫∫|s−s′|vv′). Generalization: I0 exact-analytic
(= K(0) of the kernel family), I2 and J by trapezoid quadrature with the
prefix-sum trick at N = 20000 (converged, N-independent). Self-check against
the single-cosine closed form at a = 1.40 / 1.464 / 1.52: agreement ≤ 8e-10.
Secondary metric: vmin = min v on [−1/2,1/2] (clearance above the trmdy
certification floor 3/4).

## Table (H higher ⇒ higher bound at fixed eps/psum; kernel invariant under scaling)

| rank | kernel | H | vmin | notes |
|---|---|---|---|---|
| 1 | MT sqrt2 (1 term, ω=√2) | **0.67250070** | 0.76024 | equals ANTHROPIC_H0 = 0.672500703679… exactly |
| 2 | cos(a), a=1.42 | 0.67250027 | 0.75836 | peak of the α-family (optimum sits at ≈√2=1.4142) |
| 3 | cos(a), a=1.40 | 0.67249814 | 0.76484 | highest vmin clearance of the top three |
| 4 | cos(a), a=1.44 | 0.67249196 | 0.75181 | |
| 5 | cos(a), a=1.46 | 0.67247265 | 0.74517 | ≈ current chain alpha (1.464) operating point |
| 6 | trmdy 7-term (design.py rationals) | 0.67245704 | 0.75021 | matches trmdy H_cert = 0.67245704141454… |
| 7 | cos(a), a=1.48 | 0.67244181 | 0.73847 | |
| 8 | cos(a), a=1.50 | 0.67239886 | 0.73169 | |
| 9 | cos(a), a=1.52 | 0.67234323 | 0.72484 | |
| 10 | 2-term [1,0.25], ω=(1.40,2.80) | 0.67066595 | 0.80733 | |
| 11 | 2-term [1,0.25], ω=(1.46,2.92) | 0.66960751 | 0.77282 | |
| 12 | 2-term [1,0.25], ω=(1.52,3.04) | 0.66823706 | 0.73753 | |

## Findings
1. **H-max in this family is the pure single cosine at ω ≈ √2** (0.67250070). The
   α-sweep peaks at a ≈ 1.414–1.42; the pipeline's current a ≈ 1.464 sits ~2.8e-5
   below the optimum. Moving α → √2 (or 1.42) is worth ≈ (257·ΔH)/(257−R) ≈ 2.8e-5
   on the final bound, at zero added certification burden (still one term).
2. **Multi-term specs do not help H.** Both 2-term [1,0.25] mixtures (−0.2e-2) and the
   certified trmdy 7-term (0.67245704) land *below* the MT single term. Multi-term
   windows buy certification flexibility (vmin, w″ control), not H. If the chain ever
   needs extra margin in the pair-weight/certificate inequality (†), trmdy's 7-term is
   the only already-certified non-MT option and its H is only 4.4e-5 below MT.
3. vmin is anti-correlated with H in the sweep and is comfortably above 3/4 everywhere;
   not the binding constraint at these alphas.

## Top-3 flagged for real (Arb) certification next
1. **MT sqrt2 single term** — H = 0.67250070, vmin = 0.76024; reproduces the standing
   Anthropic H0 record exactly; one-term cert is the cheapest possible.
2. **cos(a), a = 1.42** — H = 0.67250027; certifies the α-tuned gain (+2.8e-5 vs current
   1.464) while staying inside the existing single-cosine machinery.
3. **cos(a), a = 1.40** — H = 0.67249814; vmin = 0.76484 best-in-class clearance; marginal
   H loss (−2.5e-6) against 1.42 buys the fattest window margin.

Recommended next move: certify H(√2)/H(1.42) with the arb closed form
(trmdy `h0_cert.py` pattern) and re-run the direction2_sdp chain at α = 1.42 to bank the
~2.8e-5 bound gain. Honest caveat: bound gain assumes eps/psum can be held at the current
feasible point; α couples into eps in the joint model.