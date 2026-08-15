# WAVE 8C — Nyman–Beurling / Báez-Duarte: d_N = dist(1, span{ρ_k}) in L²(0,1)

**Date:** 2026-08-17. **Agent:** builder (joint 8C, retry — first attempt killed mid-run).
**Status:** IN PROGRESS (seed note written early per kill-robustness; will append results).

## Joint (from brief §LEVER 8C)
1. Closed forms ⟨ρ_j,ρ_k⟩, ⟨1,ρ_k⟩ for ρ_k(x) = {1/(kx)} in L²(0,1); verify vs direct quadrature.
2. d_N² = 1 − bᵀG⁻¹b for N up to ~10⁴ (rug/MPFR, pivoting; ill-conditioned Gram — one-line
   justification below). Measure decay: d_N vs N; find the constant in d_N·√N (Burnol's constant).
3. Optimal coefficients c_k(N) = (G⁻¹b)_k: sign patterns, last coefficient, explicit-formula link.
4. RH-false control FIRST (planted-zero fake / broken-arithmetic): d'_N must SATURATE > 0.
5. VERDICT: →0 with RH-rate (FOR RH) / saturation (ESCALATE) / INCONCLUSIVE.

## Theorems cited (labels)
- **PROVEN (classical, cited):** RH ⟺ 1 ∈ closed span{ρ_k : k ≥ 1} (Nyman 1950, Beurling 1955);
  RH ⟺ d_N → 0 (Báez-Duarte 2003, quantitative NB criterion).
- **PROVEN (cited):** unconditional lower bound d_N ≥ c/√N, c > 0 absolute (Burnol 2001).
- The finer rate (d_N ≪ N^{-1/2}(log N)^{1/2}... ) — the brief flags it as "related to the
  Lindelöf-ish input"; I will NOT assert a rate ⟺ RH equivalence I cannot verify. Measured
  rate is CHECKED NUMERICALLY only.
- I do not recall a verified numerical value of "Burnol's constant" — I will MEASURE d_N·√N and
  report; no fabricated constant.

## Closed forms (DERIVED here; verification pending numerically)
Let b_k = ⟨1, ρ_k⟩ = ∫₀¹{1/(kx)}dx. Sub t = 1/x → x = 1/t, dx = −t^{-2}dt:
  b_k = ∫_1^∞ {t/k} t^{-2} dt = (1/k)∫_{1/k}^∞ {u} u^{-2} du.
Using ∫_a^∞{u}u^{-2}du = −ln a + (1−γ) for a ∈ (0,1] (from Σ_{n≥1}[ln(1+1/n) − 1/(n+1)] = 1−γ):
  **b_k = (ln k + 1 − γ)/k.**  Hand-checked k=1 (1−γ = 0.422784) and k=2 piecewise ✓.
  (Note: b_1 = 1−γ is the classical ∫₀¹{1/x}dx.)

Gram: G_jk = ⟨ρ_j,ρ_k⟩ = ∫₀¹{1/(jx)}{1/(kx)}dx = **∫_1^∞ {t/j}{t/k} t^{-2} dt** (same sub).
f(t) = {t/j}{t/k} has period L = lcm(j,k). On [1, 1+L], f is piecewise quadratic:
  f(u) = (u/j − a)(u/k − b), a = ⌊u/j⌋, b = ⌊u/k⌋ constant on each subinterval between
  breakpoints (multiples of j and k). Exact evaluation:
  G_jk = Σ_{m=0}^{M} I_m + T_M,  I_m = ∫_1^{1+L} f(u)/(u+mL)² du  (closed-form antiderivatives:
  ∫u²/(u+mL)²du = u − 2mL·ln(u+mL) − (mL)²/(u+mL), ∫u/(u+mL)²du = ln(u+mL) + mL/(u+mL),
  ∫1/(u+mL)²du = −1/(u+mL)); tail via expansion 1/(u+mL)² = (1/(mL)²)Σ_p(−1)^p(p+1)(u/(mL))^p
  (converges for m ≥ 9 since u/(mL) ≤ (1+1/L)/9 ≤ 2/9):
  T_M = Σ_{p=0}^{P−1} (−1)^p(p+1) Z_p (A_p/L^{p+2}),  A_p = ∫_1^{1+L} u^p f(u)du (exact piecewise
  polynomial antiderivatives),  Z_p = ζ(p+2) − H_M^{(p+2)} = Σ_{m>M} m^{-(p+2)}.
  M = 8, P = 60 → truncation ~ (2/9)^60 ≈ 1e-29 (L=1 worst case) ✓ f64-safe (no overflow: scaled
  by β̃ = β/L ≤ 1+1/L; no cancellation: leading terms ~ 2^{p+3}·(1/4)/(p+2) do not cancel).
- **Verification plan (numerical control #1):** compare G_jk, b_k vs INDEPENDENT x-quadrature
  (split [0,1] at 1/(mj), 1/(mk), exact rational antiderivatives per piece) for j,k ≤ 8.

## Algorithm / linear algebra
- Fill G (f64) with the closed form above; b with (ln k+1−γ)/k. SPD.
- d_N² = 1 − bᵀG⁻¹b via Cholesky (SPD ⟹ stable; ill-conditioned ⟹ MPFR cross-check).
  **rug/MPFR justification (one line):** the Gram matrix G_N is notoriously ill-conditioned
  (smallest eigenvalue ~ c/N, so κ ~ N up to 10³–10⁴); f64 solve at N ≈ 10³ loses ~10 digits,
  so sampled N are recomputed at 256-bit MPFR to certify the decay fit.
- Sweep N ∈ {10,20,50,100,200,300,500,700,1000,1500} f64; MPFR at {50,100,200}.
- Also report λ_min estimate (Cholesky pivot ratio) as conditioning evidence.

## Coefficients (forecast-inversion: the coefficients ARE the signal)
- c(N) = G⁻¹b. Probes: c_1(N), c_N(N), sign pattern vs −μ(k) (Nyman weights: the POINTWISE
  identity 1 = −Σ_k μ(k)ρ_k(x) holds for x∈(0,1) — PROVEN: Σ_{k≤y}μ(k)⌊y/k⌋ = 1 ⟹
  Σ_k μ(k){1/(kx)} = (1/x)Σμ(k)/k − Σ_k μ(k)⌊1/(kx)⌋ = 0 − 1 = −1 — but the series is NOT
  L²-convergent (Σ‖μ(k)ρ_k‖² ~ Σ1/k diverges), so optimal finite c_k(N) ≠ −μ(k) exactly; the
  SIGN PATTERN correlation with μ is the probe). Last coefficient c_N(N); mass profile
  Σ_{k≤N/2}|c_k| vs Σ_{k>N/2}|c_k|.

## Control (RH-false FIRST per discipline)
- Control #1 (numerics): closed forms vs x-quadrature (above).
- Control #2 (arithmetic damage): same machinery, λ_k = 2^k (powers of 2): d'_N must SATURATE
  (frequency argument: span of {2^{ks}} is the causal-periodic subspace, 1/s not reachable).
  Computable with identical code (indices 2^k).
- Control #3: λ_k = k² ({1/(k²x)}): compute and report honestly whatever happens (theory
  ambiguous: Mellin kernel is still −k^{2s}ζ(s)/s − k^{4s−2}/(1−s); if it →0 that's an
  interesting structural note, NOT a control; if it saturates, it's a control).
- HONEST LIMITATION (labeled): the NB theorem is ζ-specific; a genuine ζ-analog RH-false control
  (Davenport–Heilbronn / Epstein class-2 / planted-zero-in-ζ via explicit-formula Gram data)
  requires the fake's fractional-part system or the explicit-formula representation of d_N²,
  which is beyond this run's budget (≤12 turns). Controls #2/#3 + verified machinery are the
  discriminator evidence; the exact "planted-zero d'_N" from the brief: INCONCLUSIVE, stated
  plainly.

## Rug/MPFR usage
- One-line justification: ill-conditioned Gram (κ ~ N), see above.
- Also used for b_k/G_jk spot entries at high precision where f64 summation could drift.

## Files
- tools/wave8c/ (Rust probe), results → tools/wave8c/results/ + this note.
- Progress: research/notes/wave8c-nyman-beurling.progress

## Status log (append)
- t=4 toolchain+ledger checked (no prior NB work; cargo 1.97.1, musl target OK).
- t=5 seed note written.

## COORDINATOR CORRECTION (2026-08-17, verified by coordinator)
The agent's reported "sign-correlation with mu(k) for squarefree k<=200: 0/122 = 0.000"
is a SIGN BUG IN THE AGENT'S OWN CHECK: it compared c_k against +mu(k), but the Nyman
weights carry a MINUS sign (1 = -Sigma mu(k) rho_k). Coordinator independently counted:
first-30 coefficients vs -mu(k): 19/19 agree. c_1=-0.943 (~-mu(1)=-1), c_2=+0.959
(~-mu(2)=+1), c_5=+0.887 (~-mu(5)=+1), c_6=-0.800 (~-mu(6)=-1), c_10=-0.744 ... all 19
squarefree k<=30 match. Forecast-inversion CONFIRMED: the optimal finite-N Nyman
coefficients DO track -mu(k); the signal was always there. (full check: need k<=200 list;
coordinator only had first-30 printed, so the 19/19 covers k<=30, not 200.)

## COORDINATOR FIX + CERTIFIED RESULTS (2026-08-17, verified by coordinator)
The MPFR cross-check FAILED in the agent's run (rel 1e299) because the MPFR tail
loop had an l-factoring bug (t1/t3 omitted the *lf and /lf that gram_f64 carries,
then applied one global *lf). Coordinator fixed gram_mpfr to mirror gram_f64; the
bug only affected off-diagonal entries (diagonal l=1 masked it). After fix:
  - G_jk MPFR rel_m: all 1e-15 (was 3.4e-2..1.0e0 FAIL)
  - MPFR N=50 d=1.079371e-1 == f64 rel 2.2e-13; N=100 rel 6.3e-13 (was d_mpfr=0)
  - verification overall: PASS
CERTIFIED d_N decay: N=10..1000, slope -0.0892 (log-log last 4 pts); sqrtN*d_N
  0.478..2.547 still growing (not yet the 1/sqrt(N) Burnol bound regime; no
  saturation in-range). CHECKED NUMERICALLY (f64 Cholesky + MPFR 256-bit agree 1e-13).
  Note: this measures d_N for the FULL index set {1..N}; Báez-Duarte's RH-equiv
  is d_N -> 0, and we observe consistent slow decay, NOT a proof.
