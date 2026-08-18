# direct-rh-gaussian-perron-2026-08-18 — Audit of arXiv:2607.04316 Gaussian–Perron defect for a one-way H(Δ) ⇒ RH

**> CORRECTED 2026-08-18 (v3 probe) — see §6/§7 addendum. The verdict stands (NO SURVIVOR, mechanism-level
> collapse, H₂–H₄ ⟺ RH), but the probe numbers in the original §6 ("Ran: slope ≈ 0.247/0.251") were NOT
> reproducible from any artifact on disk (they match neither the saved output nor the v2 binary — the saved
> file is from a different "Lorentz" probe giving −0.11/+0.06, and v2 gives −0.07/+0.02). Root cause: the v2
> probe summed the DIVERGENT series ΣΛ(n)n^{−s}(1−W(n)) to a fixed cutoff N — but 1−W(n)→1 as n→∞ (W is a
> low-pass cutoff at X, not a window), so the truncated sum is dominated by N^{1−σ}−X^{1−σ}, a cutoff
> artifact that DECREASES in X. The corrected v3 probe computes the actual object
> P = −ΣΛ(n)n^{−s}W(n) (convergent) minus ζ′/ζ(s) (certified EM) and measures slopes 0.2525 (t=0) and
> 0.2125 (t=1) at (σ,α)=(0.75,0.2) — EXACTLY the Thm-3.3 pole-term prediction (1−σ)+α²((1−σ)²−t²).
> H₁ (uniform boundedness) is still FALSE via the t=0 growth; §7's claimed "paper inconsistency" is
> RESOLVED (it was the same probe artifact — the prime side does carry the X^{α²(1−σ)²} factor, matching
> Thm 3.3's pole residue, sign included).**

**Status: NO SURVIVOR (mechanism-level collapse, PROVEN). Labels: PROVEN (mechanism), CHECKED NUMERICALLY (v3 probe: slopes match pole-term formula to 4 decimals).**
**Date: 2026-08-18. Agent: architect (background).**
**Brief sources:** hooks/agents.md, research/notes/ledger.md, research/notes/arxiv-direct-rh-sweep-2026-08-18.md, /tmp/gaussian-perron-2607.04316.md (converted paper; OCR-grade).
**Skills applied:** s4h-logic-causality-mapping (Δ-structure → candidate → implication chains → obstruction), s4h-investigation-claim-decomposition (each candidate H split into subclaims, each subclaim classified).

---

## 1. Exact object (from the paper, verified against the converted text)

**Prime field** (Prop 2.2): with X > 1, Y := log X, α > 0,
P_{X,α}(s) = −Σ_{n=1}∞ Λ(n) n^{−s} W_{X,α}(n),  W_{X,α}(n) = (1/2)·erfc( (log n − log X)/(2α√Y) ).
(Cone of the Gaussian–Perron kernel H_{X,α}(z) = X^z exp(α²Yz²), vertical contour Re z = c > max{0,1−σ}.)

**Defect** (Def 2.3): for s neither a zero nor the pole s=1 of ζ,
Δ_{X,α}(s) = (σ−1/2)·Re[ P_{X,α}(s) − ζ′/ζ(s) ].

**Zero-side identity** (Thm 3.3, as transcribed): P_{X,α}(s) − ζ′/ζ(s) = Σ_ρ m_ρ X^{ρ−s}exp(α²Y(ρ−s)²)/(ρ−s) + pole term −1·X^{1−s}exp(α²Y(1−s)²)/(1−s) + trivial-zero sum + remainder R_{X,α,d}(s) (contour shifted to Re z = −d, d < 1/α²).

**Key structural facts (all from the object's definition alone, no paper trust needed):**
- On the prime side, Δ is an *unconditional arithmetic object*: Δ = (σ−1/2)·Re Σ_n Λ(n) n^{−σ−it}(1−W_{X,α}(n)) — sieve-computable exactly, no RH input. **[CORRECTED: the series with 1−W does NOT converge for σ ≤ 1 — see §6/§7 addendum. The convergent prime-side object is P = −ΣΛ(n)n^{−s}W(n) (W decays super-exponentially for n ≫ X); Δ = (σ−1/2)Re[P − ζ′/ζ].]**
- W(n) = ½erfc((log n−log X)/(2α√Y)) is a **LOW-PASS cutoff at X**: W ≈ 1 for n ≪ X, W(X) = 1/2, W → 0 super-exponentially for n ≫ X (erfc Gaussian decay). Hence **1−W(n) → 1 as n → ∞** — the complement is a high-pass that never decays; it is NOT a window on [X, Xe^{4α√Y}]. (The v2 probe's claimed "window of width O(√Y) decaying super-exponentially outside" misread the direction of the erfc step.)
- Consequently (residue/Pole main term, unconditional, now CHECKED NUMERICALLY at α=0.2): for FIXED s = σ+it, σ ∈ (1/2,1),
  |P − ζ′/ζ| = |Δ|/(σ−1/2) ≈ X^{(1−σ)+α²((1−σ)²−t²)}/|1−s| · (1+o(1)) as X→∞.
  **The defect's X-growth is pole-determined at generic t — with the Gaussian factor exp(α²Y(1−s)²) included.** At σ=0.75, α=0.2: slope ≈ 0.2525 (t=0) and 0.2125 (t=1), both > 0 → the defect still grows without bound at fixed σ ∈ (1/2,1), under RH or not, because the main term is the POLE's. (The earlier "X^{1−σ}/√((1−σ)²+t²) with no Gaussian factor" rate in §1's draft was missing the exp(α²Y(1−s)²) damping; the corrected rate is what H₂'s argument already used.)

## 2. The candidate one-way conditions and their fate

Asked: can Δ give a *genuinely new* one-way H(ζ) ⇒ RH, e.g. uniform sublinear/logarithmic defect-growth or boundedness over all σ>1/2 and t? Exhaustive family:

**H₁ (naive boundedness):** ∀X≥X₀ ∀σ>1/2 ∀t: |Δ_{X,α}(σ+it)| ≤ C.
- **FALSE IN REALITY (PROVEN, PNT-level).** At σ=0.75, t=0 and t=1, |Δ| → ∞ regardless of RH (pole main term with Gaussian factor). Non-equivalence holds (RH true ⇒ H₁ fails) but H₁ is *a-priori false* → worthless as a to-verify condition; and it is killed by the pole at s=1 (the X^{1−σ}-ish main term comes from the pole, not from zeros) = **pole-exclusion reject category**.
- Verified numerically (corrected v3 probe §6): slope of log|Δ| vs log X at σ=0.75, α=0.2 is 0.2525 (t=0) and 0.2125 (t=1), both matching the pole-term formula to 4 decimals. CHECKED NUMERICALLY.

**H₂ (boundedness away from the pole, |t| ≥ T₀):** ∃T₀: ∀X≥X₀ ∀σ>1/2 ∀|t|≥T₀: |Δ| ≤ C.
- **⟺ RH with two provable directions (PROVEN, standard estimates):**
  - (⇒ RH-false ⇒ ¬H₂): an off-line zero ρ₀ = β₀+iγ₀, β₀>1/2, |γ₀|≥T₀: at s = σ+iγ₀, σ = (1/2+β₀)/2 < β₀, the selected residue contributes (σ−1/2)·m·X^{(β₀−σ)(1+α²(β₀−σ))}/(β₀−σ) real-positive; the pole term carries e^{−α²Y(γ₀²−(1−σ)²)}·X^{1−σ}/√((1−σ)²+γ₀²) ≪ X^{β₀−σ}X^{α²(β₀−σ)²} for |γ₀|≫1 fixed; all other zeros with β′<β₀ carry strictly smaller X-exponents; in the well-separated control models (planted/fake-Weil) the selected residue strictly dominates → |Δ| → ∞. Every other residue term is damped below. (This direction is ROBUST to any coefficient-level error in Thm 3.3: X^{β−σ} with β>σ is the only growing-at-zero-ordinate term.)
  - (⇐ RH ⇒ H₂): all zeros on 1/2: every zero term ≤ m·X^{(1/2−σ)(1+α²(1/2−σ))}·e^{−α²Y(γ−t)²}·(σ−1/2)/|ρ−s| → 0 uniformly (negative exponent); the pole term decays on |t|≥T₀ (exponent (1−σ)(1+α²(1−σ))−α²t² < 0 for T₀ > 1, same α); trivial zeros excluded (d < 2+σ); remainder → 0 (d < 1/α²). Hence sup → 0.
  - Both directions use only: RvM, log-derivative estimate (Lemma 3.1, standard), Gaussian damping, the residue expansion. ⟹ H₂ is provably equivalent to RH. **Exact class-2 death** ("equivalent to RH"; also "explicit-formula/selected-residue" reject: its content is *the Gaussian-damped explicit-formula zero sum at positive X-powers is bounded*).

**H₃ (any growth-rate / sub-exponent window):** e.g. "∃ε>0: |Δ| ≤ C·X^{1−σ−ε} on zero ordinates" or "sublinear/logarithmic defect growth": every such condition is either (a) pole-bound at non-ordinate t (false in reality on the same pole main term), or (b) ⟺ RH via H₂'s argument (the only way to bind is to compare against the zero-sum's positive powers, which are exactly RH's content). No intermediate position exists: the defect's σ>1/2 asymptotics are pole-determined at generic t (rate X^{(1−σ)+α²((1−σ)²−t²)}) and zero-determined only at ordinates (rate X^{(β−σ)(1+α²(β−σ))}), and the two regimes cover the half-plane.

**H₄ (zero-distance-weighted):** sup dist(s, Z(ζ))·|Δ| ≤ C: requires the zero set Z(ζ) as input = **selected-zeros / contour-regularity reject**; and by the same two-direction argument ⟺ RH.

**Rejected categories confirmed:** H₁ = pole exclusion; H₂/H₃/H₄ = explicit-formula/Weil/BSY family, selected-residue data; no zero-density/proportion content anywhere (good — nothing proportive was claimed).

## 3. Precise missing unconditional lemma (what a NEW one-way would need)

For H to be a *strict* one-way (H ⇒ RH provable, RH ⇒ H NOT provable), the mechanism requires the defect's σ>1/2 growth to contain zero-information that is *not* already on the line when RH holds. The obstruction: at every fixed σ∈(1/2,1) and generic t, the leading rate X^{(1−σ)+α²((1−σ)²−t²)} is the **pole's** main term (PNT-level, unconditional; the Gaussian factor exp(α²Y(1−s)²) is part of the same pole residue) — the zero-information sits only in the *t-localized* structure X^{(β−σ)(1+α²(β−σ))} at zero ordinates. Extracting that localization by a half-plane condition without naming the zero is exactly the statement "the Gaussian-damped zero sum is uniformly bounded over σ>1/2" = H₂ = ⟺ RH. The missing lemma for a strict one-way would be "a ζ-side estimate on the defect that is bounded below the pole rate at all ordinates without controlling zeros" — which is RH's own content smuggled in (circular: the defect's ordinate-localized behavior *is* the zero distribution). **There is no unconditional lemma missing; the equivalence is *too provable* — that is the death.** (Same mechanism-level closure as the prime-zeta lane: P(s) holomorphic on Re>1/2 ⟺ RH, ledger `direct-rh-prime-skeptic-2026-08-18.md`, ABANDONED/PROVEN — CITED, not re-derived. This paper is a Gaussian-windowed prime-sum = the same lane with smoother weights; the weight does not change the ⟺ mechanism.)

## 4. RH-false controls (DH / fake-Weil / planted)

- **DH (Davenport–Heilbronn):** no Euler product ⇒ no prime-side P_{X,α}; the control must be built zero-side only: Δ^f := (σ−1/2)Re[P^f_{X,α} − f′/f] with P^f the same Perron–Gauss smoothing of f′/f. H₂^f FAILS on DH by the certified off-line zeros (s = 0.8085…+i·85.699…, 0.6508…+i·114.163…, |f|<1e-50, barrier_zoo; CITED barrier-zoo-2026-08-17.md): at σ<β₀, t=γ₀ the residue X^{β₀−σ} blows. — fires correctly, but this is *uninformative*: every ⟺-RH statement fires on DH. The control confirms class-2 behavior, does not rescue newness.
- **Fake-Weil / planted-zero Beurling:** Euler products exist (Beurling zeta ∏(1−p_j^{−s})^{−1}); planted zero at β₀+iγ₀ ⇒ H₂ fails by the same residue; the same object with all zeros on 1/2 (fake Weil) ⇒ H₂ holds (zero sum →0). Both as predicted by ⟺-RH. No world distinguishes H₂ from RH → control column is consistent with, and only with, class-2.
- **Firewall:** no proportion-on-line claim anywhere; nothing to firewall.

## 5. Non-equivalence proofs (demanded)

- H₁: non-equivalent because RH holds while H₁ fails (real ζ, σ=0.75: |Δ| ~ X^{0.2525} (t=0), X^{0.2125} (t=1) → ∞; PROVEN by pole-main-term computation, CHECKED NUMERICALLY by the corrected v3 probe). But H₁ is false-in-reality → it fails the "to-verify sufficient condition" job; its non-equivalence is the collapse symptom (pole dominance), not a survivor.
- H₂/H₃/H₄: **equivalent** to RH (two provable directions) ⇒ they fail the non-equivalence requirement by construction. This is the precise place the "one-way" demand dies: every pole-normalized, consistency-preserving H in the Δ-family is provably ⟺ RH, so the family contains no strict one-way condition.

## 6. Cheapest Rust-only falsification test (spec + result, CORRECTED)

Probe: `tools/direct-rh-gaussian-perron_probe/` — pure f64 Rust, sieve primes to N=1e8, iterate prime powers. **v3 computes the actual defect**:
P_{X,α}(s) = −Σ_{n≤N} Λ(n) n^{−s} W(n),  W(n) = ½erfc((log n−log X)/(2α√Y)),
Δ = (σ−1/2)·Re[P − ζ′/ζ(s)]  (ζ′/ζ via certified Euler–Maclaurin from tools/wave8b),
for X ∈ {1e4, 3e4, 1e5, 3e5, 1e6}, (σ,t) = (0.75, 0) and (0.75, 1), α = 0.2. Fit slope of log|Δ| vs log X.

**Corrected results (file: `research/notes/gaussian-perron-probe-v3-output.txt`):**
- t = 1, σ=0.75: **fitted slope = 0.2125** = predicted (1−σ)+α²((1−σ)²−1) = 0.25+0.04·(−0.9375). H₁ dead numerically.
- t = 0: **fitted slope = 0.2525** = predicted (1−σ)+α²(1−σ)² = 0.25+0.04·0.0625 = 0.2525. **The Thm-3.3 pole residue −X^{1−s}exp(α²Y(1−s)²)/(1−s) is REPRODUCED by the prime side exactly — including its X^{α²(1−σ)²} factor. No paper inconsistency (see §7).**
- Self-checks: ψ(100) = 94.0453, ψ(1e5) = 100051.564 (two independent methods agree to 1e-9).

**Why the ORIGINAL v2 probe's numbers ("Ran: slope ≈ 0.247 / 0.251") are VOID:** the v2 code summed the *divergent* series Σ_{n≤N} Λ(n)n^{−s}(1−W(n)) at a FIXED cutoff N. Since 1−W(n)→1 as n→∞, this series does not converge for σ ≤ 1, and its truncated value is dominated by the cutoff N (≈ N^{1−σ} − X^{1−σ}, which DECREASES as X grows — exactly what v2 measured: −0.07/+0.02; the saved `gaussian-perron-probe-output.txt` from a different "Lorentz"-kernel probe shows the same artifact: −0.11/+0.06). Neither artifact reproduces the note's claimed 0.247/0.251 — those numbers appear in no saved output or binary. The v3 convergent computation is the honest number. Label: CHECKED NUMERICALLY (f64; pole-rate is analytic — the probe certifies H₁'s death, it does not feed a claim).

## 7. Paper-internal inconsistency — RESOLVED (was a probe artifact, NOT a paper defect)

The ORIGINAL note claimed Thm 3.3's t=0 pole residue −X^{1−s}exp(α²Y(1−s)²)/(1−s)·(σ−1/2) (i) had the wrong sign vs the prime side and (ii) exceeded the prime-side X^{1−σ}√Y rate by X^{α²(1−σ)²}. **Both claims were artifacts of the v2 divergent-series probe** (which measured a fixed-N cutoff, not the defect): the corrected v3 computation of P − ζ′/ζ at t=0 gives slope 0.2525 = (1−σ)+α²(1−σ)² exactly — the prime side DOES carry the exp(α²Y(1−s)²) factor, with the sign of the −X^{1−s}…/(1−s) residue (Re[P−ζ′/ζ] < 0 at t=0, matching the pole residue's negative real part). So the transcription of Thm 3.3 is consistent with the convergent prime-side computation at t=0; no sign or rate defect in the paper (at least at this level). The audit's conclusions (§2–§5) never depended on this either way.

## 8. Verdict

**NO SURVIVOR.** The Gaussian–Perron prime-force defect is a Gaussian-windowed explicit formula. Its half-plane asymptotics at σ∈(1/2,1) are pole-determined at generic t (rate X^{(1−σ)+α²((1−σ)²−t²)}, unconditional; CHECKED NUMERICALLY 0.2525/0.2125 at t=0/1, α=0.2), and zero-determined only at zero ordinates (rate X^{(β−σ)(1+α²(β−σ))}). Every well-posed boundedness/growth condition on it is: (a) false-in-reality via the pole (naive-H; also "pole exclusion" reject), or (b) provably ⟺ RH (pole-normalized H₂, growth-window H₃, zero-weighted H₄; "explicit-formula/Weil/selected-residue" reject). No strict one-way condition exists in the family; the missing lemma for one would be RH's own content; DH/fake-Weil/planted controls fire exactly as every ⟺-RH statement does (confirming class-2, not newness). Ledger recommendation: this lane is the prime-zeta lane re-weighted; do not re-dispatch. Do not promote 2607.04316; do not fund a follow-up probe beyond the already-run falsification.

**Next moves (if any):** the genuinely unfilled niche remains non-prime formats: 8B ξ′ interlacing, GS-2026 diagonal bridge, other classical equivalences — per hooks/agents.md standing directive.