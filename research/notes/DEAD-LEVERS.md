# DEAD LEVERS — standing digest for agy/swarm prompts (append to every ideation prompt)
# Source: 133+ wave audit + hooks/agents.md death list + 2026-08-21 session. Keep <2KB.

## PROVEN DEAD / CLASSICAL-CLOSED (never re-propose)
- Total-positivity / Polya-Laguerre / log-concavity of xi; d_N floors ALONE; winding & argument-principle zero-counts; explicit-formula residue extraction ALONE; zero-search; Herglotz family; midpoint resolvent floors; critical-point counts.
- angle_kernel: REFUTED (+0.13 at lambda=0.60). cert-floor-rs: 0.67319 < 0.6818 fails. finitet-cinf: TIMEOUT.

## MEASURED NULLS (133 waves, 0 global survivors — all VERIFIED were synthetic planted-local checks)
- Alien 4-probes diffuse, no bound: kolmogorov C drops only ~70% of predicted; diffraction +20% proxy matches plant AND noise; coulomb Delta_H/N ~ 1e-5; persistence hole 0.0029-0.0128.
- Jensen disc is LOCAL: gap>0 iff |T-t0|<sqrt(r^2-d0^2)=0.2828; vanishes T>=30. Sweet spot c=0.75 r=0.30: E_RH=0.182322, plant beta0=0.85 -> E_false=1.098612 gap 0.916291.
- VACUOUS configs (do not reuse): c=0.75 r=0.20 (disc misses line, E_RH=0 tautology); inverted c=0.60 r=0.30.

## CONDITIONAL-ONLY (2026-08-21 — the open analytic inputs are the frontier)
- **LIPSCHITZ L=0.19 REFUTED (2026-08-21, agy+independent grid check)**: true L = 5*sqrt(11)/9 = 1.8426 (9.7x larger; 0.19 was peak amplitude log(1.2) mislabeled as slope). Unconditional L is IMPOSSIBLE (off-line zero near sigma=0.75 gives log singularity |E'|~1/(2d)->inf). Corrected covering cert still fires: 0.182322 + 1.8426*0.125 = 0.4126 < planted worst-case 0.6281 (margin 0.215, was 0.19). BUT conditional-on-computation version COLLAPSES to classical zero-counting (certifying 'only the 29 on-line zeros in [0,100]' already proves the window) — salvage path: two-case detection (far-from-line: finite L(d) grid catch; near-line: log spike at nearest grid point), NOT yet formalized.
- Covering/island chain (44 discs t=14..100): fires numerically, but see L refutation above; detection floor beta0>~0.55; finite window only.
- Real Li lambda_n COMPUTED (li_lambda_real, lit-validated 6dp: lam1=0.023096 lam2=0.092346); plant beta0=0.85 flips sign at n=90, dips grow |z|^n, |z|=1.0032; predicted crossing n~3300 (CONJECTURED) — f64 dies at n>=250. FIX DESIGNED (q3, spectral phase engine): on-line 1-1/rho=e^(2i*theta), theta=arctan(1/(2*gamma)), lambda_n=sum_j 4sin^2(n*theta_j)+tail — phasor recurrence, ~85ms to n=4000, NO cancellation. NOT yet implemented.
- NB defect rate: RH slope -0.208 vs planted -0.30 separates at N<=200 but PRE-ASYMPTOTIC; residue lemma C(beta0,gamma0)=1/[(2b-1)(b^2+g^2)|zeta'|^2] CONJECTURED unverified.
- Weil bridge: ONE phi family proves nothing; prime-error budget DERIVED 2026-08-21 (q1: R(X) <= (sqrt(pi)C*sigma/2)e^{sigma^2/4}*[(V^2/(2s^2)-1)/(V/(2s^2)-1/2)]*exp(-(V-sigma^2)^2/(4sigma^2)), V=log X, C=1.000028 Dusart) — needs independent verification + implementation (weil_prime_sum tool committed cf83374, unverified). Family-richness equivalence statement still open.

## RULE
Any new idea must state which of these it avoids and why its missing analytic input (Lipschitz bound / error budget / asymptotic regime) is provable where the above failed.
