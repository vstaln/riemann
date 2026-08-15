# Adversarial D_4 review — hostile blind referee verdict (2026-08-15)

CLAIM under attack: sign(D_n)=(-1)^{n(n+1)/2} for n=1..8 on real b_k; planted control
(gamma_2 -> 0.35+/-21.1i) breaks at D_4 while Turan T_k>0 pass; "D_4-alternation is
strictly sharper than Turan positivity as an RH discriminator".
Referee method: independent recomputation, mpmath 250-300 digit (not the probe's f64).

1. ALGEBRA (PROVEN, literature + hand-checks): RH => F(z)=b_0*Prod(1+z/gamma^2),
   alpha_j=1/gamma_j^2>0 => (b_k/b_0)=e_k(alpha) is PF_infty (Aissen-Schoenberg-Whitney
   1952) => Hankel matrix sign-regular with signature (-1)^{r(r-1)/2} (Karlin, Total
   Positivity II ch.8). Hand-verified on (1+z)(1+2z), (1+z)(1+2z)(1+3z),
   (1+z)^2(1+2z)(1+3z) at n=1..4. Necessity (RH => alternation) is SOUND; a real-case
   signature failure would be an RH disproof. 20 random positive-alpha models: 0 violations.

2. REAL CASE (CHECKED NUMERICALLY, 300-digit mpmath from Phi quadrature, independent):
   D_n signs -,-,+,+,-,-,+,+ = exactly (-1)^{n(n+1)/2} for n=1..8; log10|D| = -4.2..-186.5,
   matches the probe. f64 signs agree with 300-digit on identical inputs at all n<=8,
   and survive rel-1e-15 input perturbation (20 runs, 0 flips). The stieltjes-agent
   "f64 Hankel signs unreliable at n>=7" concern does NOT materialize on THIS data
   (no license beyond it).

3. PLANTED CONTROL gamma_2->0.35+/-21.1i (CHECKED NUMERICALLY, 250-digit): D_4 = -1
   (expected +), |D_4| ~ 1e-50.5; T_1..T_15 > 0. The D_4 break is REAL (survives
   250-digit arithmetic; f64 agrees). This specific fact is VERIFIED.

4. DESTRUCTIVE TEST — REFUTED (250-digit; all models in the note's own e_k class, all
   RH-false by the note's own criterion "F zeros not all real negative", all Turan-pass):
   - gamma_2 -> 50+/-21.1i (beta > gamma_h): FULL D_1..D_8 alternation + Turan pass.
   - gamma_15 -> 0.35+/-65.11i (small beta, high height): FULL alternation + Turan pass.
   - gamma_1 -> 0.35+/-14.13i: D_4 OK (only D_2 breaks). Two pairs (0.35,0.35): D_4 OK.
   - beta sweep at gamma_2: D_4 breaks only in a beta-window (0<beta<~gamma_h); "which n
     breaks" wanders (beta=5: D_3 breaks, D_4 OK; beta=21: D_5 breaks, D_4 OK; beta>=25:
     nothing breaks). The D_4 break is a parameter-specific near-zero crossing, not a
     property of off-line zeros in general.

5. VERDICT: numerical core CERTIFIED (facts 2, 3). The general claim "D_4 strictly
   sharper than Turan as an RH discriminator" is REFUTED: RH-false, Turan-passing models
   with full D_1..D_8 alternation exist, so the alternation check has false negatives and
   neither detector strictly dominates the other. Certified limit (precise): "the
   alternating Hankel signature is a proven necessary RH condition that fires on the
   specific control gamma_2->0.35+/-21.1i at f64 and at 250-digit precision while Turan
   passes" — and nothing more. Any real-case D_n failure would still be an RH disproof
   (that part of the note is sound; holding of alternation is only consistency, as the
   note itself says).

6. LIMITS: n<=8 only; f64 signs verified only on this data set. Marginal signs near a
   D_n zero crossing can be ill-conditioned — for any new control, confirm the sign in
   high precision before trusting it. No claim about n>8 or about other controls.

Evidence: tools/referee_d4_check.py, tools/referee_d4_sweep.py (throwaway, /tmp),
this review's outputs reproduced above.
