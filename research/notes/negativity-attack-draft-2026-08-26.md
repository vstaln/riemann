# Assembled attack: deformation tool → ζ′-negativity program (draft 2026-08-26)

**Author:** adventurer subagent (read-only synthesis; no compute this session).
**Inputs:** `speiser-negativity-program.md` (program + named missing ingredient),
`lr-profile-theorem-2026-08-25.md` (PROVEN deformation theorem), `speiser-probe-2026-08-25.md`
(crossing mechanism, CHECKED NUMERICALLY), `speiser-literature-audit-2026-08-25.md`
(PARTIALLY_KNOWN verdict), `xiprime-transfer.md` (caution: no pointwise ξ′↔ζ transfer).
**Status:** CANDIDATE ATTACK LINE — the deformation/crossing machinery is exactly the tool-shape
the negativity program declares missing; the honest gap is a single named conjecture (FV, §4).

---

## 1. The ζ′-negativity program's exact blocking statement

The program's target is **(W): Re(ζ′/ζ)(s) < 0 for all 0<σ<1/2, t≥10** (certified on 207210 pts;
(W) ⟺ RH via Speiser, with the RH⟹(W) direction PROVEN termwise in the note).

Its exact decomposition (D) is PROVEN and numerically verified to 1e-8:

    ζ′/ζ(s) = B(s) + Σ_{γ>0} P_ρ(s),   P_ρ(s) = (2s−1)/((s−ρ)(s−1+ρ̄))
    B(s) = −1/s − 1/(s−1) + ½log π − ½ψ(s/2)   (Re B ≈ −½log(t/2π) → −∞)

with the sign structure: **Re P_ρ = (σ−β)/|s−ρ|² + (σ+β−1)/|s−1+ρ̄|²**, where the partner term
(σ+β−1)/|·|² is ALWAYS negative for σ<1/2. **Positivity of Re(ζ′/ζ) can come ONLY from a zero
with β<σ at nearby height t.**

The program's named missing ingredient (verbatim one-sentence form, §2 of the program):

> a per-height (non-averaged) upper bound showing that zeros with β<σ cannot push
> Σ_{β<σ}(σ−β)/((σ−β)²+(t−γ)²) above −Re B near height t — no current zero-density method
> operates pointwise in t for any σ<1/2.

And its structural verdict: the hole is **RH-hard by closed loop** — bounding how close to σ=0 a
zero can sit at each height *is* RH. Any successful attack must inject an ingredient NOT
equivalent to RH. The deformation theorem + crossing mechanism (§2–3) is that ingredient's
candidate shape: a per-height, non-averaged, t-uniform observable that provably type-separates
off-line from on-line configurations in closed form.

## 2. The deformation tool — what is PROVEN

From `lr-profile-theorem-2026-08-25.md` (all closed-form, all t₀ ≥ γ₁, margins ≥ 19×):

- **Observable:** L_R(s) = (log R)″ = −Σ_P 1/(s−p)² + Σ_M 1/(s−m)² (second log-derivative of a
  planted factor; base cancels out of every comparison).
- **(LINE) PROVEN:** for an on-line implant, Re L_LINE(σ+it₀) ≥ 2.6134 > 0 everywhere on
  (0,1)\{½} — zero σ-crossings, sign-stable, uniform in t₀.
- **(OFF) PROVEN:** for a mirror-complete off-line pair at β (with FE mirror 1−β), Re L_OFF has
  EXACTLY two σ-crossings at |σ−½| = (β−½)·√(√5−2) ≈ 0.19435 (β=0.9) and is negative at both
  extremes (σ→0 and σ→1); positive in the middle.
- **(TYPE_SEPARATION) PROVEN:** any one of (a) sign at a common σ (σ=0.3: −2.7765 vs +27.9586),
  (b) σ-zero-count (2 vs 0), (c) monotonicity class separates OFF from LINE. Upgraded from
  turan-probe's CHECKED NUMERICALLY to PROVEN.

From `speiser-probe-2026-08-25.md` (crossing mechanism):

- **Single-factor inertia PROVEN (paired-Hadamard identity):** a lone off-line plant without its FE
  mirror cannot push an ξ′ zero across Re=½ (N=0, PROVEN + CHECKED NUMERICALLY).
- **FE-consistent plant CHECKED NUMERICALLY:** planting (0.9±it₀, 0.1±it₀) forces exactly N=1
  ξ′-zero into Re<½, localized at Re≈0.4526, Im≈t₀. On-line plants: N=0. The mirror zero at 1−β
  contributes Re 1/(s−(1−β)+it₀) = (σ−(1−β))/|·|² > 0 for σ>1−β — this is what opens the real
  part to positivity. Mechanism is completed-zeta-FE-specific (Davenport–Heilbronn contrast,
  audit §2.3).
- **Caution from `xiprime-transfer.md` (PROVEN):** the crossing object is an *ξ′ zero*, NOT a ζ
  zero (G(γ₁) ≈ −0.0014 ≠ 0 at the ζ zero); the only exact ξ′↔ζ link is the global count
  N_{ξ′} = N + O(log T). So the chain must route through ξ′ (see §3), never claim ζ-zero transfer.

## 3. The assembled chain (each step labeled)

**Goal:** (W) Re(ζ′/ζ)<0 in 0<σ<1/2 ⟺ RH.

1. **(W) ⟺ L** — decomposition (D) exact + Prop B reduction. [PROVEN; speiser-negativity §1,§3a]
2. **L ⟺ per-height deep-left-zero exclusion** at radius ~(σ−β)^{1/2}/√(log t) — the dangerous
   kernels only come from zeros within a small window |t−γ| ≲ R(t) < 8 (for t ≥ γ₁, any fixed
   δ = 8 exceeds R(t)). [PROVEN reduction; speiser-negativity §2]
3. **Per-height exclusion ⟸ contrapositive of FV** (see §4): N(t₀)=0 in a height-window ⟹ no
   off-line ζ-zero at that height. This is precisely the pointwise-in-t statement no zero-density
   method supplies. [MISSING — this is the bridge, named FV below]
4. **FV ⟸ crossing mechanism + shape certificate:** an FE-consistent off-line pair at (β, γ₀)
   opens Re(ξ′/ξ) to positivity in (1−β, ½) near height γ₀ (PROVEN sign analysis), forcing ξ′
   zeros left of ½ (CHECKED NUMERICALLY: N=1 at Re≈0.4526 for β=0.9, γ₀=γ₁, window ±8); the
   deformation theorem certifies the OFF profile-shape in closed form for ALL t₀ ≥ γ₁ (PROVEN),
   so the discrimination is t-uniform, not averaged. [mechanism: PROVEN sign + CHECKED count;
   general-β/γ₀ proof: MISSING]
5. **N = 0 is computable/provable per band:** certified argument-principle machinery already exists
   (wave8b certleft: certified arc control, Taylor drift, threshold π/2) and the probe's winding
   method counts N robustly. [method PROVEN in wave8b for ζ′; ξ′ band-certification: NOT YET RUN]
6. **ξ′ route is legitimate:** ξ′/ξ has NO Archimedean background (unlike ζ′/ζ) — every pair term
   has Re ∝ (2σ−1)·(positive) under RH — so ξ′-left-of-½ crossings are the cleanest witness of
   off-line ζ-zeros. [PROVEN classical; literature audit §2.1]

**The honest reading:** steps 1–2 + 6 are PROVEN; step 4's production side is CHECKED NUMERICALLY
(one regime) with a PROVEN t-uniform shape certificate; step 5's machinery is PROVEN but not yet
pointed at ξ′. The chain's *only* unproven node is step 3 = FV, and it has the right shape the
program demands: per-height, non-averaged, zero-density-free. The attack reduces the program's
missing ingredient (an uncomputable estimate about ζ-zeros) to a computable, provable-per-band
observable (ξ′-crossing count) plus one named conjecture.

**Counts:** PROVEN 5 (steps 1, 2, 6, mechanism-sign part of 4, machinery of 5) · CHECKED 1
(crossing count N=1 at β=0.9/γ₁, plus all prior numerics) · MISSING 2 (step 3 = FV as a theorem;
step 4's general-β/γ₀ proof). (The ξ′-Speiser converse pinned to a primary source is also
outstanding but not load-bearing: the contrapositive direction we need IS FV itself.)

## 4. The honest gap — named conjecture

**Discriminability → constraint-on-reality.** What is PROVEN is that *planted* configurations
type-separate. To constrain the *real* ζ we need the observable applied to the real function to
be provably inert — and the minimal theorem with that force is:

> **Conjecture FV (Off-line Visibility / ξ′-Crossing Production):** if ζ has an off-line zero
> ρ₀ = β + iγ₀ with 0 < β < ½ (mirror 1−β at the same height, forced by the functional
> equation), then for the actual ξ, #{ ξ′-zeros in Re<½, |Im−γ₀| ≤ 8 } ≥ 1.

Contrapositive (the step-3 bridge): **N(t₀) = 0 in a height-window ⟹ no off-line ζ-zero at that
height** — exactly the per-height deep-left-zero exclusion Lemma L needs, and the window δ=8 is
generous (the required exclusion radius is only R(t) ~ (σ−β)^{1/2}/√(log t) < 8).

**Weakest sufficient form:** it suffices to prove FV for a *single mirror-complete pair* at
arbitrary (β, γ₀) — the deformation theorem already certifies the pair's profile-shape in closed
form for all t₀ ≥ γ₁ (uniform, margin ≥ 19×), and the probe demonstrates the count at one regime.
If even the single-pair statement resists, a weaker usable form suffices: total-count visibility,
¬RH ⟹ ∃ height with N ≥ 1 (localization dropped) — but localization is what the machinery
naturally gives, so the single-pair localized form is the honest target.

**Honest caveats (why this is a candidate, not a proof):** (i) the probe is one regime (β=0.9,
γ₀=γ₁, δ=8) — FV's parameter range is untested; (ii) the "base cannot swamp the pair signal" side
— whether the absolute (log ξ)″ profile (as opposed to the differenced L_R) is a usable
discriminant — is unquantified and may be false pointwise near on-line zero heights (Re(log ξ)″
has negative dips at (σ−½)² > (t−γ)² under RH), so the usable real observable is the *crossing
count N*, not the raw profile; (iii) FV at the hard edge β→½⁺ is unknown; (iv) the ξ′-Speiser
converse should be pinned to Conrey 1983 / Ivić before any novelty claim (audit action item 1).

## 5. Next 3 steps (<1h each) — test the weakest link (FV / the real observable)

1. **Real (log ξ)″ profile at γ₁** — reuse `speiser_probe.py` §1's exact l₁′ formula
   (=(log ξ)″) to compute the real profile on σ∈[0.01,0.99] at t₀=γ₁ and 2–3 higher heights;
   check whether the real profile's zero-count/extreme-signs are LINE-typed or OFF-typed. Tests
   the "base-swamping" caveat (ii): whether the absolute profile carries usable signal at all.
   (~30 min; pure extension of existing code.)
2. **FV parameter sweep** — extend the probe to β ∈ {0.55, 0.7, 0.9, 0.99} × γ₀ ∈ {γ₁, γ₂, γ₃},
   window δ=8, plus the β→½⁺ edge; does N=1 persist, and where does the pushed zero land?
   Tests FV's production side across regimes. (~45 min; reuses winding harness.)
3. **Certified N=0 for real ξ′ in one band** — point the wave8b certleft machinery (certified arc
   control + Taylor drift, already PROVEN for ζ′) at ξ′ to certify N=0 in [0.001,0.499]×[t₀±8]
   at one height, converting the method's CHECKED status into PROVEN for a finite band. Tests
   step 5's claim that the computable side is provable. (~45 min; port of existing certifier.)

**Failure logic (honest):** if step 2 shows N=0 for some β>½ regime, FV is false as stated and the
pair-sign mechanism has a gap to find — documented result, not a stop. If step 1 shows the real
profile is OFF-typed at some height, that is direct numerical evidence of an off-line zero (a
witness, not a proof). The search continues either way.

---
Labels: PROVEN (steps 1,2,6; inertia lemma; deformation theorem; N-count identity) /
CHECKED NUMERICALLY (crossing N=1 at β=0.9,γ₁; decomposition to 1e-8; (W) on 207210 pts) /
MISSING (FV theorem, general-β crossing proof, ξ′-Speiser primary-source pin).
