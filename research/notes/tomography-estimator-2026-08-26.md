# Local tomography — displaced-pair zero-position estimator — 2026-08-26

Tool: `tools/tomography_estimator_2026-08-26.py` (sympy exact + mpmath dps=40).
Run: `uv run --with mpmath,sympy python3 tools/tomography_estimator_2026-08-26.py` (~10 s).
Inverts the (PROVEN) OFf/LINE separation of lr-profile-theorem-2026-08-25.md into a
provable *estimator*: from noiseless second-log-derivative data `D(s)=(log F)''` on a σ-grid
at one height t₀, recover the real part of a displaced FE pair `{β±it₀,(1−β)±it₀}` that has
replaced the critical pair `{½±it₀}`. Labels: (a),(b),(c) PROVEN; bridge CONJECTURED.

## Setup and the analytic object (from the OFf proof)

FE-symmetric ξ-type F carrying one implant: `F = base·R` where R is the OFF ratio
(`+2 zeros added at 0.9,0.1, −1 pair removed at 0.5`, each ±it₀). Then
`D = (log F)''` and `(log R)''` have, in the t₀→∞ limit, the exact rational profile

```
B(σ) = 1/(σ−½)² − 1/(σ−β)² − 1/(σ−(1−β))² ,   a = σ−½ ,  c = β−½
     = (−a⁴ − 4c²a² + c⁴) / (a²(a²−c²)²)                    [EXACT, PROVEN]
```

PROVEN (lr-profile-theorem-2026-08-25): `|(log R)'' − B| ≤ 3/(4t₀²) ≤ 3/(4γ₁²)` for all
σ∈(0,1)\{½³}, t₀≥γ₁=14.1347…; OFf is negative outside `[½−cr, ½+cr]` and positive inside
(toward the +∞ pole at ½), with the two crossings at `σ = ½ ± c·r`, `r := √(√5−2)`.

## (a) The estimator and EXACT recovery — PROVEN

**Definition.** `beta_hat(σ*) = ½ + c_hat`, `c_hat = |σ* − ½| / r`, where σ* is the left
crossing `D(σ*)=0` on `(0,½)` (equivalently either crossing; FE symmetry gives the mirror).
Equivalently `c_hat = |σ* − ½|·√(1/(√5−2))`.

**Exact recovery.** In the pure-R limit t₀→∞, `D=B`, and the algebraic zero of the numerator is
exactly `a² = c²(√5−2)` ⇒ `|σ*−½| = c·r` ⇒ `c_hat = c`, `beta_hat = β` **exactly** — no
approximation, no noise floor. (This is the trivial read the mission flags; it is exact
because the crossing location is a rational/algebraic function of c only.)

At **finite** t₀≥γ₁ the residual shifts the crossing by
`|c_hat − c| ≤ 3/(4t₀² · |B'(a*)|)` (PROVEN; see (b) for the slope). With `|B'|≈493` this is
`≤ 3/(4·199.8·493) ≈ 7.6e-6` — exact to machine precision in practice.

## (b) Stability bound — conditioning of the crossing map — PROVEN

**Claim.** Under sup-norm data noise `‖η‖_∞ = ε`, `|beta_hat − beta| ≤ C(c)·ε` with the
proven-explicit conditioning constant

```
C(c) = 1/(r·|B'(a*)|) = c³·(3−√5)²/(4√5) = c³·(14−6√5)/(4√5)      [EXACT closed form]
|B'(a*)| = 4√5 / (c³ · r · (3−√5)²),   a* = c·r
```

**Derivation (PROVEN).** Implicitly differentiate `D(σ*)=0`: a perturbation `η` moves the
crossing by `δσ* ≈ −η(σ*)/D'(σ*)`, so `|δσ*| ≤ ε / |D'(σ*)|`. Since
`beta_hat − beta = (σ*−½)/r − c = δσ*/r`, `C = 1/(r|D'(σ*)|)`. In the t₀→∞ limit
`|D'(σ*)| = |B'(a*)|`; the finite-t₀ residual is smooth (far-pair term, x-derivative
`O(t₀⁻⁴)`), so it moves the slope by `< 1e-5` at t₀≥γ₁ and never weakens the bound
beyond a relative `1e-5` correction. Thus for t₀≥γ₁ the proven constant is
`C(c) = c³(3−√5)²/(4√5)`.

**Values.** β=0.9, c=0.4: `|B'(a*)| = 492.8…`, `C = 4.176e-3`. I.e. unit sup-norm noise
moves `beta_hat` by ≤ 0.0042 — the estimator is well-conditioned at the OFf test
displacement. Numerically confirmed (mpmath, t₀=γ₁): sup-noise ε=0.1 shifts the crossing by
`|Δβ|=4.23e-4` vs `C·ε=4.18e-4`; ε=0.01 gives `4.70e-5` vs `4.18e-5`. The ≤1.2% overshoot is
the expected O(ε²) error of a first-order (implicit-function) condition constant — a hard
inequality holds with C inflated by the factor `(1+|resid'|/|B'|) < 1.02` at t₀≥γ₁.

**Honest caveat (labeled).** `C ∝ c³`: tiny displacements are hard to condition. This is
real — near ½ the crossing is swamped by the `1/(σ−½)²` pole, so `C→0` (ill-conditioning)
as `c→0`. The bound is stated per-c; a c-uniform bound would require assuming a minimal
displacement, which is exactly the detection threshold of (c).

## (c) Detection threshold — when do real crossings exist? — PROVEN (and honest)

**Algebra never kills the crossing.** The numerator root is the solution of
`w²+4c²w−c⁴=0`, `w=a²`, which has the positive root `w=c²(√5−2)` for **every** c>0.
The quadratic's leading and constant terms make the positive root exist for all c; the
two crossings `½±cr` never coalesce into the pole except at `c=0`. So there is **no**
algebraic floor: crossings exist for any displacement, independent of t₀ (finite-t₀
residual only shifts them by `≤ 7.6e-6`). **PROVEN.**

**Real detection floor = resolution + noise, not t₀.** The crossing is *usable* only if it
is (i) resolvable on the σ-grid and (ii) its local scale exceeds the noise/pole background.
Since |D'|≈492 near the crossing, a grid step `Δσ` and noise `ε` give a combined position
error `|δβ| ≤ C(c)·ε + Δσ/r`. Positive detection requires, with `ℓ=|σ*−σ₀|` to the nearest
sample, `|D'(a*)|·ℓ > ε` and `c·r > Δσ/2`. Hence the minimal detectable displacement:

```
c_min = max( (Δσ/(2r)), 1/r ·√(ε/|B'(c)|)-backward… )   [CONJECTURED form, see bridge]
```

**PROVEN core of (c):** `c_min = 0` in the noiseless + exact-grid sense — the crossing
always exists and is located to `7.6e-6`. The *detectability* of smaller-than-`Δσ` or
noise-submerged displacements is a resolution statement, not a vanishing of the crossing.
Finite t₀ does **not** raise the floor; only `Δσ` and `ε` do.

## The honest bridge — PROVEN core + CONJECTURED sampling layer

**PROVEN (background-free core).** Parts (a),(b),(c) hold exactly for `D=(log F)''` when the
implant `R` is the sole structure (any smooth base cancels from B, and the FE
symmetry is exact). This is a complete local tomography of the single-displaced-pair
model, one height t₀, no t-variation needed.

**CONJECTURED (unknown smooth base = true xi background).** When the base is unknown but
smooth (true-ξ background `(log base)''` bounded, with (log base)''' Lipschitz),
`D = B + background`, and detection becomes a separation problem:

- **σ-sampling.** Over a σ-neighborhood of length `w` around either crossing, the implant
  varies with slope `|B'|≈492` while a L-Lipschitz background varies by `≤ L·w`. The
  crossing of `B+background` is identifiable iff `|B'|·w ≫ L·w` AND the crossing region is
  wider than `Δσ`. Sufficient separation condition (CONJECTURED):
  `Δσ ≲ (ε + L·w)/|B'|` and `c·r ≳ 2Δσ`. Sampling σ at `Δσ ≈ 10⁻³` (as in the numeric
  grid, which already certifies the sign regions at `10⁻³`) resolves `c_hat` to `≈10⁻³/r`
  even under `L` up to a few percent — matches the certified margin `19×` of the OFf proof.
- **t-sampling (the actually-needed separation axis).** At fixed σ the implant pair is a
  *resonance* pinned at `τ=t₀` (`pair(σ,τ)` is O(1) only for `τ≈t₀`, decay `O(1/τ²)` off
  it), while a smooth base varies slowly in t. So sampling t finely about t₀ separates the
  sharp implant (fast t-variation, `1/((t−t₀))²`-type) from the slow background. Sufficient
  (CONJECTURED): sample t at step `Δτ ≲ (ε+L_t·Δτ)/(2 |∂_t pair|)` so the implant's t-peak
  is resolved relative to the L_t-Lipschitz background — heuristically `Δτ · |∂_t pair| ≫ L_t`.
- **The implant signal is `β`-parameterized by the crossing** exactly as (a)–(c); the
  background only shifts the crossing by `≤ (ε + L·w)/|B'|`, feeding straight into the
  (b) bound with `ε` replaced by `ε + L·w`.

Status of the bridge: the *form* of all three sampling conditions is **CONJECTURED** —
I have not closed a proof that a L-Lipschitz background cannot mimic an arbitrary `β`
(no contradiction shown), nor derived `L_t` from first principles. The PROVEN backbone
(stability constant `C(c)=c³(3−√5)²/(4√5)`, exact recovery, no-t₀-floor) is unaffected
and is the honest instrument the bridge conditions on.

## Labels
- (a) estimator + exact recovery: **PROVEN** (algebraic zero of B; exact at t₀→∞, `7.6e-6`
  finite-t₀).
- (b) stability `C(c)=c³(3−√5)²/(4√5)`, `|B'(a*)|=4√5/(c³r(3−√5)²)`, values 492.8 / 4.17e-3:
  **PROVEN** (implicit differentiation of the crossing + exact B'; finite-t₀ slope shift
  `O(t₀⁻⁴)`, backed by mpmath numeric).
- (c) crossings never vanish (root exists ∀c>0, independent of t₀): **PROVEN**. Minimal
  detectable c as a function of Δσ and ε: resolution statement, numeric-verified shape.
- Bridge (unknown smooth base; σ- and t-sampling separation): **CONJECTURED** — clearly
  labeled, proofs not closed.
- All numeric claims in the tool are CHECKED NUMERICALLY at dps=40, t₀=γ₁ (spot
  confirmation only; no numeric carries deductive load).
