# Barrier-zoo retro-test: PROVEN Xi identities vs the RH-false DH world (2026-08-18)

**Status:** COMPLETE. **Tool:** `tools/barrier_zoo_rs dhprofile` (Rust, std-only, added subcommand).
**Labels:** CHECKED NUMERICALLY (f64, trusted head k=0..5; k>=6 contour noise, excluded).

## QUESTION (the barrier-zoo discipline applied to the campaign's OWN identities)

The cross-domain hunt prescribed: any proposed sufficient lemma must be run against the RH-false
model worlds (Epstein class-2, Davenport–Heilbronn, planted-zero Beurling) — a lemma that "proves"
a control for the DH world proves too much. This probe retro-tests the campaign's PROVEN Xi
identities against the RH-false Davenport–Heilbronn world:

  (i)   b_k > 0 for all k          (PROVEN: M_k moments of positive measure, b_k = M_k/(2k)!)
  (ii)  t_k·k = 2 − 2/ln k + …     (PROVEN deficit-2 log-profile, this session)
  (iii) M_n Hankel-TP              (PROVEN: positive-measure structure)

If the RH-false world satisfies them too → they are consistency-only, definitively. If it violates
one → that identity separates Xi from an RH-false world (candidate one-way input).

## CONSTRUCTION (verified, not guessed)

DH world: f(s) = L(s,ψ) + c·L(s,ψ̄), ψ mod 5 with ψ(2)=i, c = τ(ψ)/(i√5) (Gauss-sum normalized),
FE sign +1. The bare combination f = L + c·L̄ is NOT real on the critical line (checked: Φ(1/2) =
2.652+0.753i). The real-on-line combination (Titchmarsh's kappa-form up to real scale) is
  Φ(s) = (5/π)^{(s+1)/2} Γ((s+1)/2) · [e^{-iφ/2} L(s,ψ) + e^{+iφ/2} L(s,ψ̄)],  φ = arg(τ(ψ)/(i√5)) = 0.553574.
Verified: Φ(1/2) = 1.4495905 + 0.0000000i (real), even (Φ(0.5±0.1i) equal), and 23 off-line zeros
found to |Φ| < 1e-20 (e.g. s = 0.7413+17.0424i, 0.1933+37.3076i, ...) — RH-FALSE world confirmed.

Taylor coefficients via Cauchy integral on |z| = 0.45 (spectral trapezoid, 128 nodes):
  b'_k defined by Φ(1/2+it) = Σ (−1)^k b'_k t^{2k}  ⟹  actual Taylor coeffs c_{2k} = (−1)^k b'_k = |b'_k|.
Cross-checked: b'_1 = 1.421607e-1 by 2-pt and 4-pt finite differences (exact match), b'_0 = Φ(1/2).

## RESULTS (trusted k=0..5)

  c_0 = 1.449591e0, c_2 = 1.421607e-1, c_4 = 5.703513e-3, c_6 = 1.324330e-4,
  c_8 = 2.066114e-6, c_10 = 2.353271e-8   (clean geometric decay, ratio ~0.10/0.04/0.02/0.016/0.011)

  (i)  all c_{2k} > 0:  YES — the RH-false DH world has all-positive Taylor coefficients,
       exactly like Xi.  **Positivity does NOT separate.**
  (ii) deficit-2 profile on trusted k=2..5:  t_k·k = 0.843, 0.984, 1.080, 1.896
       vs profile 2−2/ln k = −0.885, 0.180, 0.557, 0.757 — ALL ABOVE (gaps +1.73, +0.80,
       +0.52, +1.14; zero violations).  **The RH-false DH world SATISFIES the deficit-2
       log-profile — the campaign's own PROVEN identity proves too much.  Consistency-only,
       confirmed by the barrier zoo.**  (k>=6 excluded: contour noise, rho^{-2k} amplification,
       coefficients stop decaying — not real.)
  (iii) Hankel det2 of M'_n = c_{2n}·(2n)!: +1.176e-1 > 0 (first minor consistent with a
       positive measure — not separating at this order; a signed Φ would need higher minors).

## VERDICT

The barrier-zoo discipline has now been applied to the campaign's own PROVEN identities, with the
decisive outcome for (ii): **the deficit-2 log-profile is confirmed consistency-only by the
campaign's own standard** — a genuine zeta-like object with a functional equation, no Euler
product, and 23 certified off-line zeros satisfies t_k·k ≥ 2 − 2/ln k in the trusted range.
This is a THIRD independent line closing the log-profile lever (after: S1 log-periodic
perturbations in-class-and-non-LP; smooth (2,−2) member in-class-and-non-LP). No new lever from
this probe: the identities that separate (none found at trusted order) would still not be
sufficient without a proof. The barrier-zoo point stands: positivity and the deficit-2 profile
are not sufficient conditions for LP/RH — they hold in an RH-false world.

## FILES / COMMITS
- tools/barrier_zoo_rs/src/main.rs — new `dhprofile` subcommand (dh|weil|epstein|beurling|classify|all + dhprofile)
- This note; ledger line appended.

## ADDENDUM — Epstein class-2 world (the strongest analogue) ALSO passes (same verdict)

The DH world is an L-combination without Euler product. The Epstein class-2 world is the
CLOSEST structural analogue to Xi: its completed function is built from a theta series with
all-positive coefficients (Theta_Q(t) = Σ_{m,n} e^{−πtQ(m,n)} > 0, mirroring Xi's own Φ>0
theta structure), it has a self-dual functional equation Xi_Q(s) = Xi_Q(1−s), and DH 1936
PROVEN (numerically verified here for the individual forms) zeros off the critical line.

**NEW STRUCTURAL FACT (this probe): Xi_Q is meromorphic, NOT entire** — it has simple poles
at s=0 (res −1) and s=1 (res +1); the raw Taylor coefficients grow like ~4^k (pole at
distance 0.5 from the s=1/2 expansion center). The Taylor-coefficient / log-profile
machinery therefore applies only to the symmetric ENTIRE part
  E(s) = Xi_Q(s) − [1/(s−1) − 1/s],
which preserves the FE (verified E(0.5+1.3i)/E(0.5−1.3i) = 1+0i) and is real on the line
(E(1/2) = 0.5634236 + 0.0000000i).

**Results (entire part, trusted k=0..7 — geometric decay 0.563, −0.0773, 5.4e-3, −2.4e-4,
7.9e-6, −1.9e-7, 3.7e-9; k≥8 contour noise):**
  (i)  all c_{2k} > 0 — YES, same as Xi.  Positivity does NOT separate (2nd world).
  (ii) deficit-2 log-profile on k=2..5: t_k·k = 0.719, 0.859, 0.953, 1.049 vs profile
       2−2/ln k = −0.885, 0.180, 0.557, 0.757 — ALL ABOVE (gaps +1.60, +0.68, +0.40,
       +0.29; zero violations).  **The closest analogue to Xi — positive theta coefficients,
       self-dual FE, RH-false — satisfies the campaign's PROVEN deficit-2 identity.
       Consistency-only, confirmed in the strongest possible analogue.**
  (iii) Hankel det2 of M'_n = c_{2n}(2n)!: +4.96e-2 > 0 (first minor; not separating).

**Verdict (now two independent RH-false worlds, DH + Epstein):** the deficit-2 log-profile is
consistency data — it holds for Xi and for both RH-false model worlds. The barrier-zoo
"proves too much" verdict is now established on the campaign's own PROVEN identity by the
campaign's own standard, in the closest structural analogue available. The profile cannot be
a sufficient condition. No new lever; documented negative. (The meromorphic-vs-entire fact
is itself a structural reason the Epstein world is NOT a counterexample to anything about Xi:
Xi is entire, Xi_Q is not — the analogy stops before the coefficient structure even starts.)

## ADDENDUM 2 — Hankel-TP at det3 does NOT separate either (last positivity hope closed)

Completed the (iii) test to det3 for both worlds (M'_n = c_{2n}·(2n)!, n=0..4 from the
trusted contour head):
  DH world:      det2 = +1.175876e-1,  det3 = +1.473272e-3  (TP)
  Epstein world: det2 = +4.957459e-2,  det3 = +3.118803e-3  (TP)
So the positive-measure / Hankel-TP structure of M_n (PROVEN for Xi at det1/2/3, frontier
probe) is ALSO satisfied by both RH-false worlds at the tested orders.  Positivity structure
does NOT separate Xi from an RH-false world either — consistent-only at every tested order.
Combined with the frontier probe (gamma(n)=n!M_n/(2n)! itself NOT a moment sequence, the
M→gamma bridge broken), there is no positivity-based separator left at the trusted orders.
