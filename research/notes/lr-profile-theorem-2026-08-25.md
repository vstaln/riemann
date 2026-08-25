# L_R sigma-profile type-separation theorem — closed form — 2026-08-25

Tool: `tools/lr_profile_theorem_2026-08-25.py` (sympy exact + mpmath dps=40).
Run: `uv run --with mpmath,sympy python3 tools/lr_profile_theorem_2026-08-25.py` (~20 s).
Reinterprets turan-probe-2026-08-25.md (VERDICT: TYPE_SEPARATES, numeric-only) into an
elementary rational-function theorem, all inequalities PROVEN in closed form.

## Convention (matches verified probes)
`L_R(s) = (log R)'' = -Sum_{p in P} 1/(s-p)^2 + Sum_{m in M} 1/(s-m)^2` for
`zeta_planted = zeta_true * R` (zeros added at P, removed at M). This is the sign used by
turan-probe-2026-08-25 and zigzag-proof-attempt-2026-08-25 (validated to 1.3e-51; reproduces
FALSE = −2.77653 at σ=0.3). The mission text's sign (Σ_P − Σ_M) is the negative of this;
every structural claim here is invariant under global sign flip, so convention is immaterial.

**Exact pair contribution** (conjugate pair {a+iτ, a−iτ}, real part at s=σ+it₀):
```
pair(a,τ) = (x²−y₁²)/(x²+y₁²)² + (x²−y₂²)/(x²+y₂²)²,   x=σ−a, y₁=t₀−τ, y₂=t₀+τ
```
For τ=t₀ the near point gives 1/(σ−a)² and the far point gives an O(t₀⁻²) term.

Off the mission's shorthand: the stated "2·Re[1/(x+iy)²] per pair" is exactly 2× this when
the near point dominates (τ=t₀); signs are unaffected. We use the exact form above.

## THEOREM (PROVEN, closed form; β=0.9 ⇒ c=β−½=2/5, δ=0.3, t₀ ≥ γ₁ ≈ 14.1347)

**(LINE) positivity is uniform and sign-stable.**
For *every* δ>0 and every σ∈(0,1)\{½}:
```
Re L_LINE(σ+it₀) =  δ²(3u²+δ²) / (u²(u²+δ²)²)  +  Δ(u;t₀,δ),   u=σ−½        [EXACT]
main part ≥ δ²(¾+δ²) / (¼·(¼+δ²)²)  (monotone decreasing in u²∈(0,¼]; PROVEN,
  d/dw log main = −(δ⁴+3δ²w+6w²)/(w(δ²+w)(δ²+3w)) < 0 for all w>0, δ>0)
|Δ| ≤ 1/(4t₀²) + 1/(2t₀+δ)²  ≤  1/(2t₀²)
```
For δ=0.3, t₀≥γ₁: `Re L_LINE ≥ 2.615917 − 0.002503 = 2.6134 > 0`. So LINE never changes
sign on (0,1) — zero σ-crossings, strictly positive, with a +∞ pole at σ=½ (removed zero).

**(OFF) two exact zero-crossings, negative at both extremes.**
Writing B(σ) = 1/(σ−½)² − 1/(σ−β)² − 1/(σ−(1−β))² (the t₀→∞ part), a=σ−½:
```
B = (−a⁴ − 4c²a² + c⁴) / (a²(a²−c²)²),   c = β−½                    [EXACT factorization]
numerator zero  ⇔  a² = c²(√5 − 2)   ⇔  |σ−½| = c·√(√5−2) ≈ 0.19435 (β=0.9)
```
The residual far-term error satisfies |L_OFF − B| ≤ 3/(4t₀²) ≤ 0.003754 (t₀ ≥ γ₁).
B is strictly increasing on (1−β, ½−c√(√5−2)) (B′ ≥ 2/c³ − 2/((1+√(√5−2))c)³ > 0, PROVEN)
and symmetric about ½ (B(1−σ)=B(σ)). Hence with exact rational boundary values
```
B(0.3055) = −0.075248…  < −0.003754 = 3/(4γ₁²)   and   B(0.3058) = +0.072614…  > +0.003754
```
(margin ≥ 19×), we get for every t₀ ≥ γ₁:
```
Re L_OFF(σ+it₀) < 0   on  (0, 0.3055] ∪ [0.6945, 1)      (also on (0,1−β),(β,1) exactly:
                          B ≤ −97.2 on (0,1−β), B → −∞ at the β,1−β poles)
Re L_OFF(σ+it₀) > 0   on  [0.3058, 0.6942] \ {½}          (+∞ pole at σ=½)
```
Asymptotically (t₀→∞) the crossing is exactly at σ = ½ ± c√(√5−2) = 0.30565 / 0.69435.

**Corollary (TYPE_SEPARATION, PROVEN).** At the common point σ=0.3:
`sign Re L_OFF = −1 ≠ +1 = sign Re L_LINE` (computed −2.7765 vs +27.9586). Moreover the
σ-profiles on (0,1) have *different zero counts* (OFF: 2 crossings; LINE: 0) and different
extreme-σ behaviour (OFF → −∞ toward the β,1−β poles and large negative at σ→0,1; LINE stays
≥ 2.6134 everywhere). Any one of (a) sign at a common σ, (b) σ-zero-count, (c) monotonicity
class separates the two implant types in closed form — the probe's numeric verdict is now a
theorem.

## Verification (all printed by the tool)
- sympy: exact factorization `−a⁴−4a²c²+c⁴`; zero `a²=c²(√5−2)`; monotonicity bound
  `2/c³(1−1/(1+r)³) > 0`, r=√(√5−2); B(0.3055), B(0.3058) exact rationals with stated
  margin vs 3/(4γ₁²); LINE main-part log-derivative `−(δ⁴+3δ²w+6w²)/(w(δ²+w)(δ²+3w)) < 0`.
- mpmath dps=40 at t₀=γ₁: grid 1/1000..999/1000 (poles excluded): OFF negative on
  [0.001,0.999]-clipped ends, positive inside [0.306, 0.694]; LINE zeroneg on the whole grid.
- spot: L_OFF(0.3) = −2.776528…, L_LINE(0.3) = +27.958554…, L_OFF(0.45) = +386.8997,
  L_OFF(0.95) = −396.44, L_LINE(0.05) = +3.6233.

## Labels
- THEOREM (LINE positivity, OFF sign structure, separation corollary): **PROVEN** — every
  inequality is an exact rational/algebraic identity with certified margins; no numerics
  carry any deductive load (they are spot-confirmation only).
- Asymptotic crossing location ½ ± c√(√5−2): PROVEN (t₀→∞ limit of B; finite-t₀ shift is
  bounded by the stated error term, |shift| ≤ 0.003754/|B′| ≈ 7.6e-6).
- General β∈(½,1) version: PROVEN structurally (crossing |σ−½| = (β−½)√(√5−2), LINE bound
  independent of β, OFF monotonicity B′ ≥ (2/c³)(1−1/(1+r)³)) for t₀ ≥ γ₁ with the same
  margin argument; the explicit numeric intervals above are stated for β=0.9.

## Relationship to prior notes
- Consistent with zigzag-proof-attempt-2026-08-25.md: REFUTED was the *flip of the total*
  (log ξ_planted)″ at σ=0.3,0.5 vs base — a different claim. The L_R *profile itself* is
  exactly what separates OFF from LINE here; base cancels out of every comparison.
- turan-probe-2026-08-25.md VERDICT TYPE_SEPARATES is upgraded from CHECKED NUMERICALLY to
  PROVEN. (Its LINE column used a truncated sum; the exact added-pair term raises e.g. the
  σ=0.3 value from 25.01 to 27.96 — sign and structure unchanged.)
- The removable singularity at σ=½ is type-invariant (both types carry it), carries no type
  information; separation lives entirely in the off-critical σ-signature, as conjectured.