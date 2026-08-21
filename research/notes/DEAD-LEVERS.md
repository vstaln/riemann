## ⚠️ 2026-08-21 CERTIFICATION BUG (READ FIRST)

The formerly-claimed record **0.6735633479946228 (eps=0.00703) is RETIRED — invalid certificate**.
`tangent_lower` in verify_coboundary_floor.py certified convexity from entrywise lower bounds of w''
(LDL on M ≻ 0), which does NOT imply the true Hessian is PD. Exact counterexample at RECORD params:
g=(8082,8069,11965,8040,4227,4244)/4000 gives F_B=0.00689927 < 0.00703 (confirmed float + arb + mpmath 40-digit).
Sound verifier (fixed, Gershgorin certificate): eps=0.00689 verified=true → honest record
**N₀(T)/N(T) ≥ 0.6734729658**. The "joint max-min breakthrough to 0.6751273" was an artifact of the same bug — DEAD.
Details: research/notes/cert-bug-2026-08-21.md. Do NOT cite 0.00703 / 0.6735633 / 0.6751 anywhere.

---

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
- Real Li lambda_n COMPUTED twice (binomial li_lambda_real + spectral li_lambda_spectral, cross-validated 6dp: lam1=0.023096 lam2=0.092346). CORRECT Li variable z=1-1/rho (audit b8: 1-1/(rho-1) was a sign error that produced a FALSE fire at n=2576 — retracted). Planted quadruplet: growing base |z3|=|rho_p/(1-rho_p)|=1.001750 for beta0=0.85; local dip at n=87-91 (real), CONTROL FIRES at n=5155 (CHECKED NUMERICALLY, 2.1s scan to n=8000). Real world positive through n=8000.
- NB defect rate: RH slope -0.208 vs planted -0.30 separates at N<=200 but PRE-ASYMPTOTIC; residue lemma C(beta0,gamma0)=1/[(2b-1)(b^2+g^2)|zeta'|^2] CONJECTURED unverified.
- Weil bridge: ONE phi family proves nothing; prime-error budget DERIVED 2026-08-21 (q1: R(X) <= (sqrt(pi)C*sigma/2)e^{sigma^2/4}*[(V^2/(2s^2)-1)/(V/(2s^2)-1/2)]*exp(-(V-sigma^2)^2/(4sigma^2)), V=log X, C=1.000028 Dusart) — needs independent verification + implementation (weil_prime_sum tool committed cf83374, unverified). Family-richness equivalence statement still open.

## RULE
Any new idea must state which of these it avoids and why its missing analytic input (Lipschitz bound / error budget / asymptotic regime) is provable where the above failed.

## 2026-08-21 battery adjudication (agy b1-b8)
- KILLED [PROVEN]: Beurling defect residue lemma d_N^2(beta0)>=C/N^{2(1-beta0)} — the "zeta(rho0)=0 kills zeta*P_N" residue justification does not apply (b3).
- UPGRADED to CHECKED NUMERICALLY: Weil-truncated-inside-Jensen with prime-error budget |R|<0.01 for X>=808 (independently rechecked: bound sum 0.002753 at X=808; oscillatory R(100)=+0.005595 vs claimed 0.006123) (b1). Single test function = single scalar inequality only; RH-below-T needs dense Galerkin family (Bombieri 2000 Thm 10).
- LIVE: lambda_n spectral phases to n=1e5 via O(N) phasor recurrence, variable z=1-1/rho (b4); finite Galerkin Q_N negative-eigenvalue test.
- CHECKED NUMERICALLY (wave RH-4B): the spectral Li scan used all J=100000 supplied zeros (cutoff gamma=74980.923, not 500000), found no negative lambda_n through n=100000, and the beta0=0.85 quadruplet fired at n=5155 then stayed negative only from n=99994 through this finite scan. This finite f64 result is not an RH proof; do not repeat it without extending data/rigor.
- CONFIRMED DEAD: de Branges HB obstruction (b7); two-case covering stays conditional (b2).

## 2026-08-21 wave-rh4(A) — Speiser/DH control (Lane D, ranking.md)
- Ran speiser_dh_control (jensen_probe bin): DH f' scan σ∈[0.05,0.5], t∈[10,120], Nmax=2000.
  Strongest |f'| min at 0.42+85.70i, |f'|=0.0968 — matches canonical Voronin DH zero height ~85.7i;
  the proposal's claimed 14.12 saddle did NOT appear (confirms ranking.md's UNVERIFIED flag).
- Winding: DH f'=1 on circle r=0.15 [CHECKED NUMERICALLY]; truncated ζ'-analog control=0 —
  discriminator NOT broken; RH-false control fires.
- NOT CERTIFIED: Dirichlet remainder bound 0.80 >> 10%|f'| at Nmax=2000 (ratio 8.3). Task's literal
  bound Σ|r|ln n n^{-0.05} DIVERGES. Verdict FAIL-on-certification; winding-1 is indication only.
- Status: Speiser-transfer-for-DH stays CONJECTURED. Lever remains LIVE pending certified re-run
  (functional-equation eval or N>=1e6 + interval arithmetic). Do not re-run as-is (same-lever rule).
