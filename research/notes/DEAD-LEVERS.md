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

## 2026-08-21 wave-rh4b(C) — Speiser/DH zero CERTIFIED (Lane D)
- speiser_dh_certify (jensen_probe bin): Hurwitz-Euler-Maclaurin engine (no truncation wall),
  analytic f′, certified per-point bound = 4×last-Bernoulli-term×(2M+|ln x_a|+1).
- DH f′ winding = 1 on circle |s−(0.42+85.70i)|=0.15, min|f′|=1.049, max err 3.19e-11
  (ratio 3e-11) → zero CERTIFIED inside circle [CHECKED NUMERICALLY-RIGOROUS; location PROVEN
  given printed bounds]. TRUE ζ′ control winds 0 on same circle.
- FE for this normalization: f(s)=W(s)f(1−s), W(s)=(5/π)^{1/2−s}Γ(1−s/2)/Γ((s+1)/2), λ=1
  (c=tan(arg ε/2), ε=τ(χ₄)/(i√5)); verified 5e-15 in 40-digit mpmath. Task-proposed
  X=5^{s−1/2}π^{2s−1/2}Γ((3/2−s)/2)/Γ((s+1/2)/2) REJECTED (fails both directions, res 0.33–2.1).
- Status: lever UPGRADED from indication-only (wave-rh4 A: remainder 0.80 >> |f′|) to certified.
  Do NOT re-run truncated variants (same-lever rule). Next: rigor transfer / interval arithmetic
  if a proof-grade claim is ever needed; Speiser-transfer-for-DH stays CONJECTURED.

## 2026-08-21 night — wave RH-4b results
- CERTIFIED [CHECKED NUMERICALLY-RIGOROUS]: DH f′ left-strip zero at 0.42+85.70i inside r=0.15
  (Euler-Maclaurin engine, per-point bound 3.2e−11 vs min|f′|=1.049, winding 1; ζ′ control winding 0).
  Correct DH functional equation derived: f(s)=W(s)f(1−s), W(s)=(5/π)^{1/2−s}Γ(1−s/2)/Γ((s+1)/2)
  (task-proposed X REJECTED numerically). Commit 791f7ac.
- λ_n real world clean through n=100000 (J=100k zeros); plant fires n=5155, permanently negative n≥99994. Commit e0395b4.
- LEDGERED CONJECTURE (lane E, agy): Uniform Hadamard Deficit Conjecture (UHDC) — for t≥14,
  0<σ<1/2, dist(s,{ρ})≥1/log t: Re(ζ′/ζ)(s)>0. Honest label: proving it unconditionally is
  RH-hard; value is as an interval-arithmetic-verifiable refinement target.
- INCONCLUSIVE: sound eps=0.00700 cert at grid 8000 / 60M nodes (node-limit). Sound record stays
  eps=0.00695 → 0.6735117054871194.

## 2026-08-21 wave-rh5(E) — UHDC interval scan
- REFUTED [CHECKED NUMERICALLY]: the ledgered Uniform Hadamard Deficit Conjecture as stated,
  `Re(zeta'/zeta)(sigma+it)>0` away from zeros, fails at all 207210 included grid points for
  sigma=0.05..0.45 and t=14..70000 step 2 after excluding distance <3/log(t). First failure:
  0.05+16i, value -0.6281573984651 +/-4.06e-10, zero distance 1.918789; minimum -33.3593.
- Rust EM probe: `tools/jensen_probe/src/bin/uhdc_scan.rs`; runtime ~40s. N=64/128 cross-check
  at first failure agrees to 8.10e-14 within combined quotient bounds 1.80e-9. Independent 40-digit
  mpmath recheck INCONCLUSIVE (module unavailable). Do not repeat the same grid/sign convention;
  a reversed sign or completed-zeta background formulation is a distinct future conjecture.

## 2026-08-21 wave-rh5(D) — zeta' left-strip certification extended
- EXTENDED (same lever, not new): Hurwitz-EM argument-principle certification of the zeta'
  left strip now covers [0.001,0.49] x [5000,12000] — all 28 bands wind 0, max arg gap
  <=1.64<2.8, err/min<=7.1e-5, spot-doubling worst ratio 7.1e-3; DH control circle wound 1.
  Contiguous with wave-8B [10,5000] => zero-free [10,12000] GIVEN printed bounds
  [CHECKED NUMERICALLY-RIGOROUS]. Bin speiser_zeta_strip.rs (probe mode available). Commit wave-rh5(D).
- DO NOT re-run [10,5000] with this engine (same-lever rule). Do NOT build rectangles with
  right edge at sigma=0.5: zeta' provably has zeros ON the line (Hardy+Rolle); any prior
  "sigma<=0.5" winding claim should be audited for silent false-PASS. Open lanes: sliver
  (0.49,1/2) needs a line-zero-dodging contour or completed-zeta reformulation; beyond 12000,
  widen cells first (gap headroom observed: 1.64 used of 2.8 allowed).

## 2026-08-22 — wave RH-5 results
- EXTENDED [CHECKED NUMERICALLY-RIGOROUS]: ζ′ zero-free on σ∈[0.001,0.49] × t∈[10,12000]
  (contiguous, 28 bands wound 0, err/min ≤7.1e−5, DH control winding=1 passed first).
  Design note: right edge must be <1/2 — ζ′ HAS zeros ON the line (Rolle between critical zeros);
  any prior "σ≤0.5" winding claim should be audited. Commits 9a837c7.
- KILLED [CHECKED NUMERICALLY]: UHDC as stated (>0 direction). Re(ζ′/ζ) is NEGATIVE at every
  included grid point through t=70000 (207k points; first violation 0.05+16i at −0.628;
  min −33.36 at 0.45+22016i). Sign was backwards: under RH one expects Re(ζ′/ζ)<0 throughout
  0<σ<1/2 — which is precisely the Speiser content. Corrected working conjecture:
  **Re(ζ′/ζ)(s) < 0 for all 0<σ<1/2, t≥10 away from poles** — certified on the scanned region.
  mpmath cross-recheck INCONCLUSIVE (unavailable); N=64/128 quotient check agreed to 8e−14.
  Commit 01aef8f.

## 2026-08-22 DATA QUARANTINE IMPACT ASSESSMENT
Corruption boundary row ~21000 (γ≈20100):
- SURVIVES: wave-rh5(D) ζ′ strip cert T=12000 (EM-based, zero-free pipeline); decomposition (D)
  verification at t=16 (clean region); all waves consuming only γ≲20000 zeros.
- FLAGGED FOR RE-RUN: λ_n "clean through n=1e5" (engine consumed corrupted rows; control fire
  n=5155 likely robust—driven by low zeros+plant—but real-world curve must be recomputed);
  UHDC scan exclusions beyond t=20000 (values themselves were correct EM evaluations; the
  >0-direction kill stands via sign theory + clean-region subset).
- ROOT CAUSE: RS-g0 scanner step-0.1 grid missed close pairs above t≈20000; file remains sorted,
  so consumers fail silently. Fix: tools/data/zeros_verified_32k.txt (mpmath zetazero, dps=25)
  regenerating; CONVENTIONS.md quarantines old file above γ≈20100.
- UHDC RE-RUN on trusted range only (t≤17200, commit-restricted bin): STILL FAILS — 47079
  violations, first 0.05+16i at −0.6281573984651 (independently confirmed mpmath-40 earlier).
  Kill no longer depends on corrupted rows.

## 2026-08-22 wave-rh5c(F) — λ_n clean-data rescan (rows 1..19000, γ≤17255)
- Bin tools/jensen_probe/src/bin/li_lambda_clean.rs; full-file "clean through 1e5" claim
  SUPERSEDED by certified-range version. [PROVEN] truncation direction: λ_true(n) ≥ λ_clean(n)
  (sin²≥0), so nonnegativity of the clean scan certifies λ_n ≥ 0 on n∈[1,30000].
- Result: min 0.023013 at n=1; all_nonnegative through n=30000. Plant control (β₀=0.85)
  fires n=5065 (< expected ~5155, explained by omitted positive mass in clean curve).
- Cross-check vs stored li_lambda_1e5.out at n=1000 closes to ~4e-6 after subtracting the
  recomputed corrupted-row contribution (60.1382…) and kernel-bound add (22.0477…).
- Lever status: negative-sign hunt on trusted data through n=30000 is DEAD (no sign found;
  lower bound certified). Absolute magnitudes remain far below true λ_n (modelled tail ~200×
  clean value at n=30000) — re-run with zeros_verified_32k.txt when it lands for magnitudes.

## wave-rh5c(F) — λ_n upgrade post-quarantine [efa8f6f]
UPGRADED [was CHECKED NUMERICALLY w/ corrupted data → now lower-bound certificate]:
λ_n^clean(n) = Σ_{j≤19000 verified} 4sin²(nθ_j) ≥ 0 for ALL n∈[1,30000], min = 0.023 at n=1.
Since sin²≥0, true λ_n ≥ λ_n^clean ⇒ **true λ_n > 0 on [1,30000]** (Li criterion partial,
modulo the 19000 zero values — each audited vs zetazero to ≤7e-5). Negative-sign hunt on
trusted data through n=30000: DEAD. Plant control fires n=5065 (earlier than 5155 because
clean curve omits ~82 units positive mass — mechanistically consistent). Cross-check with
old engine closes to 4e-6. Magnitude re-run pending zeros_verified_32k.txt regen (~10h).
