# Task: EMPIRICAL S₃ PROBE — triple correlation of real zeros vs sine-kernel, and candidate-family S₃

You are an EXECUTOR agent in the Riemann swarm, running locally on this phone. Real research, honesty charter.

## Context (verified from program notes)
- The 256-law (a constructed near-CUE 256-periodic configuration, p₀ = 0.68182868746…) matches ALL bandwidth-one data. Its own triple correlation S₃ is the "Frey-curve move": the real zeros' S₃ at λ < 2/3 is PROVEN equal to the sine-kernel value (Rudnick–Sarnak / Hejhal). If the law's S₃ ≠ sine-kernel, the law is excluded at the first provable higher order, opening a new third-moment certificate class.
- The 256-law's exact data is PRIVATE (cert_N256_blk_b128m.json) and NOT recoverable from the constraints (six candidate families tested, all infeasible for the exact CUE spectrum — see ~/riemann/research/notes/regenerate-256law.md).
- Therefore we do the closest achievable probes: (A) empirically verify the REAL zeros' triple correlation against the sine-kernel value; (B) compute S₃ for the reconstructed candidate 256-families and compare to sine-kernel.

## MANDATORY first steps
1. Read ~/riemann/hooks/agents.md — honesty charter (labels; every number from a script you ran).
2. Read ~/riemann/research/notes/regenerate-256law.md (the family space + LP structure) and skim attack-ceiling.md §1 (the law's definitions).

## THE WORK — all CHECKED NUMERICALLY (script + command + output)

### A. Empirical triple correlation of real zeros (mpmath)
- Compute the first N zeros γ₁,…,γ_N of ζ via mpmath.zetazero (N = 2000–5000 — phone compute, keep it modest; mpmath zetazero for 5000 zeros is a few minutes).
- Empirical triple correlation R₃(α, β) = (1/N) Σ_{i≠j≠k} δ-normalized counts of (γ_j − γ_i, γ_k − γ_i) in windows, for (α, β) in the Rudnick–Sarnak range with λ = max(|α|,|β|,|α−β|) < 2/3. Use smoothing (Gaussian or rectangle bins of width δ) and the standard normalization (mean spacing 2π/log T).
- Compare to the sine-kernel triple correlation value (Rudnick–Sarnak: K₃ formula — use the known result: for the CUE/sine process, R₃(α,β) = 1 − sinc²(πα) − sinc²(πβ) − sinc²(π(α−β)) + 2 sinc(πα)sinc(πβ)sinc(π(α−β)) in the normalized units — state which normalization you use and cite your formula source).
- Report: measured vs predicted at 3–5 (α, β) points, with error bars (bootstrap or subsample).

### B. Candidate-family S₃
- From regenerate-256law.md, reconstruct the candidate families (jittered lattices, antipodal-pairs+specials, lattice+doubles, random marked configs, grid configs).
- For each family, build a 256-periodic marked configuration with Σ marks = 256, compute its form factor S(j) for j = 1..256 and its triple correlation S₃ (the periodic analogue: S₃(j₁,j₂) from the marks).
- Compare each family's S₃ to the sine-kernel value at 2–3 points. Verdict per family: does S₃ match sine-kernel (consistent with near-CUE) or differ (excluded at third order)?
- ALSO: report each family's two-moment deviation |256·S(j) − j| (the near-CUE measure) so we see how close each family got.

## ENVIRONMENT
- Phone: Python via `proot-distro login ubuntu -- python3 file.py` or Termux python3; `proot-distro login ubuntu -- pip install mpmath numpy` allowed (mpmath likely present). NO Rust. Keep N small enough to finish in < 20 min.

## DELIVERABLE
Write ~/riemann/research/waves/wave-phone-local/results/s3-probe.md:
- Part A numbers (CHECKED NUMERICALLY): measured vs sine-kernel at each (α,β), with errors
- Part B numbers (CHECKED NUMERICALLY): per-family two-moment deviation + S₃ comparison, verdicts
- Bottom line: (i) does the real data confirm the proven sine-kernel S₃? (ii) which (if any) candidate family reproduces near-CUE at second order AND separates at third?

Print at end: RESULT: <status> — <one-line summary>
