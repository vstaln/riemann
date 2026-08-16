# Herglotz / positive-real probe — H(t)=Xi'(t)/Xi(t) (wave-20 g4-2)

STATUS: COMPLETE. DATE: 2026-08-18. TOOL: tools/herglotz_probe (Rust, reuses wave8d
em.rs certified ζ,ζ' via Euler–Maclaurin, n=600; Stirling Γ/ψ copied from lk_zeta.rs).
Output: research/notes/herglotz-probe-2026-08-18.out (full tables).

## Verdict (headline)
**RH-CONSISTENT — no violation found; and the probe EXPOSES A SIGN ERROR in the
g4-2 harvest idea as stated.** H(t)=Xi'/Xi does NOT map the UHP to itself for
all-real zeros — it maps the UHP to the LOWER half-plane (anti-Herglotz). The
correct statement is:

  **RH ⟺ −H(t) = −Xi'(t)/Xi(t) is Herglotz (Im(−H) ≥ 0 in ℑt>0) ⟺ Im H ≤ 0 in ℑt>0.**

The probe measured Im H(x+iy) < 0 at every sampled point with y>0 (margins 1e3–1e11
above certified error for y ≤ 2), including Im H(γ_j + iy) ≈ −1/y at the zeros — the
exact anti-Herglotz pole signature predicted by the all-real-zero product form
H(t) = Σ_j 2t/(t²−γ_j²). This is consistency, not evidence: a finite grid can only
ever find a violation; the equivalence itself remains PROVEN and ⟺RH (ledger class:
equivalent-to-RH). No new attackable identity emerged from the Φ-integral form
(CONJECTURED/INCONCLUSIVE).

## The trap — corrected math
For all-real zeros, H(t) = d/dt log Xi = Σ_j [1/(t−γ_j) + 1/(t+γ_j)] and
Im[1/((x−ρ)+iy)] = −y/((x−ρ)²+y²) < 0. So H is anti-Herglotz; the Herglotz object
is −H = Σ_j [1/(γ_j−t) + 1/(γ_j+t)]. Equivalently, with A(s)=d/ds log ξ(s) and
H(t)=i·A(1/2+it): Im H(t+iy) = Re A((0.5−y)+ix); all-real zeros give
Re A(s) = Σ_j (Re s − ½)/|s−s_j|² ≤ 0 for Re s < 1/2 (zeros s_j = ½±iγ_j).
"Proving −H Herglotz" IS proving RH — a reformulation, not a route.

## Key secondary finding — inherited polygamma sign slip in wave8d/lk_zeta.rs
The m=0 (ψ) Stirling branch in tools/wave8d/src/bin/lk_zeta.rs ADDS the Bernoulli
series (ψ = ln w − 1/(2w) + Σ B_{2k}/(2k w^{2k}) in code) while its comment and the
standard formula require SUBTRACTING. Effect (verified): with the code-as-written,
ψ(0.25) = −4.2273508 vs the exact value −4.227453534 (error 1.03e-4 → gate1 leak
|H(0)| = 5.1e-5). After the one-character fix (subtract), ψ(0.25) = −4.227453533 ✓
and ψ(1) = −0.577215665 ✓. Consequences:
- This probe: fixed; all gates clean (below).
- wave8d wave8d-lk-zeta-direct route-B L_k values: L_k depends on u' = −Im A_1 which
  carries ½·δψ. At t=56.5 (δ=0.054 from γ₁₂), u-derivatives are pole-dominated
  (u₁≈18, u₂≈−342, u₃≈1.3e4) and the Bell cancellation B_2≈B_3≈0 makes L_3 ∝ −B_2·B_4
  shift by O(1) under a 3e-5 δu₁ — the reported L_3(56.5)=+8.9e-32 (mpmath-matched)
  cannot survive it. Route-A CD values at those points (8.85→8.22→4.44e-32 as
  h→h/4) drift by 2× across h: roundoff-noise floor, i.e. INCONCLUSIVE, not POSITIVE.
  **Follow-up: re-run lk_zeta route B with the corrected ψ and re-adjudicate the
  7 flagged points.** (The m≥1 ψ^(m) branch is correct; only m=0 is affected.)

## Sanity gates (all PASSED, after ψ fix)
- psi(0.25) = −4.227453533 (exact −4.227453534); psi(1) = −0.577215665 (exact −γ).
- gate1 |H(0)| = |A(0.5)| = 7.1e-15 (was 5.1e-5 with the bug) — Xi even ⟹ H(0)=0. ✓
- gate2 max |Im H(t)| for real t ∈ [0,120] = 4.96e-13 — H real on the real axis. ✓
- gate3 residue (t−γ_j)H(t) → 1+O(γ_approx_err) at γ₁..γ₄ (Im parts ~1e-11; the
  1.4e-3–4.2e-3 residuals are exactly the 7-decimal γ approximation: γ₁ off by
  1.4e-7 → δ·(t−γ_true)/… ≈ 1.4e-3). Validates ζ AND ζ' at the zeros. ✓
- gate4 H(9.7) analytic Im = 1.8e-14 (H real on axis ✓); FD log-Xi cross-check
  agrees to ~3e-6 in Re (FD at ε=1e-5 is roundoff-limited; weak check, not decisive).
- Phi(u) > 0 on u ∈ [−0.6, 2.0] (min +1.02e-69 at u=2.0; positive, monotone decay)
  — CHECKED NUMERICALLY (consistent with the known theorem Φ>0).

## Grid probe — Im H(x+iy) (Herglotz-for-−H requires ≤ 0; measured all < 0)
y | min Im H (at x) | certified ζ err there | row max err | Im H(x=γ₁)
0.1 | −10.0243 (48.00≈γ₉) | 2.1e-11 | 2.7e-11 | −10.0067 (predicted −1/y −neighbors ≈ −10.007 ✓)
0.5 | −2.2419 (48.00)     | 2.0e-10 | 2.5e-10 | −2.0337 (predicted ≈ −2.034 ✓)
1.0 | −1.5276 (60.00)     | 4.5e-9  | 4.5e-9  | −1.0671 (predicted ≈ −1.067 ✓)
2.0 | −1.3086 (60.00)     | 1.7e-6  | 1.7e-6  | −0.6312 (predicted ≈ −0.631 ✓)
5.0 | −20.61 (2.00)       | 1.2e1*  | 1.8e2*  | −0.4606 (*certified bound inflated by
     worst-case rounding at σ=0.5−5=−4.5; actual error is double-precision ~1e-12 —
     sign decision by huge margin, but certified-rigorous only for y ≤ 2)
Midpoint checks (y=0.1, x=17.58 between γ₁,γ₂): measured Im H ≈ −0.022 matches the
pole-expansion prediction −Σ y/((x−γ_j)²+y²) − Σ y/((x+γ_j)²+y²) to ~10% (x=18 row:
−0.0241). The anti-Herglotz pole structure is quantitatively reproduced.

## Structural analysis — any new attackable identity? (CONJECTURED: NO)
Two exact rewrites (from Xi = R − iI, R,I real):
  Im H(x+iy) = (R'I − I'R)/(R²+I²) = (d/dx) arg Xi(x+iy).
So the Herglotz condition on −H is: arg Xi(x+iy) is non-decreasing in x for each
y>0. For all-real zeros this is manifest: arg Xi = Σ_j [arctan(y/(x−γ_j)) +
arctan(y/(x+γ_j))], each term increasing in x. From the Φ integral,
Xi(x+iy) = 2∫Φ(u)[cos(xu)cosh(yu) − i sin(xu)sinh(yu)]du, and no positivity of a
single integral can bound arg's x-derivative (a cos-transform of a positive density
can have complex zeros, e.g. 2sin(t)/t — Schoenberg's theorem needs PF kernels, not
positivity; Φ is positive but not a Pólya-frequency density). The ratio/arg structure
kills every direct Φ-positivity line. Same wall as all other ⟺RH reformulations.
No new attackable identity found. The only non-circular value of this lever is the
disproof filter (which the probe exercised) and the sign correction above.

## Ledger line
- herglotz-probe-2026-08-18: g4-2 (H=Xi'/Xi Herglotz) — PROVEN equivalence, ⟺RH
  (deflating class: equivalent-to-RH). Probe: Im H < 0 everywhere at y>0 with
  margins ≥1e3 (y≤2 certified) — RH-CONSISTENT; NOT a disproof. **g4-2 as stated is
  WRONG SIGN: H is anti-Herglotz; −H is the Herglotz object.** No new attackable
  identity from Φ-integral (CONJECTURED no). Secondary: lk_zeta.rs m=0 polygamma
  sign slip (ψ(0.25) off 1.03e-4) — wave8d route-B L_k at the 1e-32 level SUSPECT;
  re-run with fix (follow-up).
