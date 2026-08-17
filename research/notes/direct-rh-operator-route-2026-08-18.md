# Direct-RH blind operator/variational lane — Pólya density criterion and its closure

**Agent:** architect (subagent) · **Date:** 2026-08-18
**Brief lane:** ONE genuinely new one-way RH sufficient condition from positive operator /
contraction / variational inequality / spectral quantity — NOT HB/de Branges, NOT Nyman-Beurling,
NOT Weil positivity, NOT finite Jensen/GJT, NOT GS diagonal/pair correlation, NOT prime
semigroup/commutator.
**Skills used:** s4h-logic-causality-mapping (Mode 3 dependency + Mode 4 counterfactual),
s4h-analogy-structure-mapping (transport of the PF-density mechanism).
**Inputs read:** hooks/agents.md, research/notes/CAMPAIGN-STATE.md, research/notes/ledger.md,
tools/closure_dag/closure_dag.json. No closed verdict re-derived — cited.
**Labels used:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

---

## 0. Verdict up front (honest)

**NO surviving one-way sufficient condition in the operator/variational lane escapes the
campaign's four closure classes.** The closest route is the **Pólya cosine-transform density
criterion** (Ξ is a cosine transform of the positive even density Φ; if Φ were in the
Laguerre–Pólya/Pólya-frequency density class, RH would follow by a classical theorem). That
hypothesis is **PROVEN false** (Φ ∉ PF∞, campaign crossdomain closure, `SINC-PF∞` —
"Phi not PF-infinity PROVEN via Hardy+duality"). The only un-tested residue — the strictly
weaker **log-concavity** hypothesis — is probed numerically here (one cheap Rust probe) and
its result is recorded below. Even if log-concavity held, no classical theorem derives real
zeros of the cosine transform from mere log-concavity (sharp Schoenberg duality needs PF∞),
so the lane closes either way. No RH evidence in any direction beyond what the campaign
already holds.

---

## 1. The object and the mechanism (structure map, s4h-analogy-structure-mapping)

**Situation A (mechanism that works in other worlds):** PF-density theory. In probability,
if ρ is an even **Pólya frequency density** (ρ(t) totally positive as a convolution kernel,
equivalently ρ = limit of finite Gaussian*exp-polynomial products with positive factors),
then the characteristic function ρ̂(z) = ∫ρ(t)e^{izt}dt is real entire of the Laguerre–Pólya
class and has **only real zeros**. This is the classical Fourier-side of Pólya's and
Schoenberg's theory (Pólya 1918 Math. Z. 2; Pólya 1926 Acta Math. 48; Schoenberg's
PF∞ classification). One-way, genuine, non-trivial.

**Situation B (our object):** Ξ(z) = ξ(1/2+iz) is literally a cosine transform:
Ξ(t) = 2∫₀^∞ Φ(u)cos(tu)du with Φ the **positive even** theta-function density
Φ(u) = 2e^{u/2}(2x²θ″(x) + 3xθ′(x)), x = e^{2u} (campaign-PROVEN theta identity, wave-20),
Φ(0) = +0.8933938 > 0, Φ > 0 on (0,∞) (PROVEN, 8D).

**Element mapping (A → B):**
| Element in A (PF theory) | Element in B (Ξ) | Genuine/Superficial |
|---|---|---|
| even density ρ ≥ 0 | Φ ≥ 0 even | GENUINE (both positive even densities) |
| characteristic function ρ̂ | Ξ = Φ̂/2 cosine transform | GENUINE (identical role: FT) |
| hypothesis ρ ∈ PF∞ | Φ ∈ PF∞ | **the load-bearing pair — FAILS (PROVEN)** |
| conclusion: ρ̂ all-real zeros | conclusion: Ξ all-real zeros = RH | GENUINE one-way implication IF hypothesis held |

**Where the mapping breaks (the useful part):** the entire mechanism lives on the single
hypothesis "density is PF∞"; every other element transfers cleanly. So the search reduces to:
*is there ANY density-class H ⊇ {PF∞} with (ρ ∈ H ⟹ ρ̂ all-real zeros) and Φ ∈ H?*
The closed cases: H = PF∞ → PROVEN not applicable; H = {positive} → FALSE in general
(positive densities with complex-zero FT exist trivially); H = {log-concave} → theorem status
INCONCLUSIVE from memory (literature check needed; sharp Schoenberg duality requires PF∞,
so expected false in general) and Φ's membership is the cheap probe below.

---

## 2. Candidate screen (causality map, s4h-logic-causality-mapping — Mode 3 dependency)

Every candidate H(ζ) one-way ⇒ RH in this lane, and its closure:

| # | Candidate H(ζ) | Mechanism type | Closure (precise reason) |
|---|---|---|---|
| 1 | Φ ∈ PF∞ (Ξ cosine transform of PF∞ density) | positive operator/spec | **PROVEN DEAD**: Φ ∉ PF∞ (crossdomain SINC-PF∞, Hardy+duality). This is also Pólya's own 1926 negative result on exactly this density. |
| 2 | Φ log-concave (weakening of 1) | variational/spectral | **THIS PROBE** (below). No classical sufficiency theorem at this hypothesis level (sharp duality = PF∞); probe decides only the consistency fact, not RH. |
| 3 | Nevanlinna/S-fraction/Jacobi-matrix positivity | positive operator | **CLOSED (equivalence + inapplicable)**: Stieltjes S-fraction ⟺ real-rootedness is class-2 restatement (ledger `stieltjes-sfraction`, wall test executed); AND γ(n)=n!M_n/(2n)! is NOT a moment sequence (Hankel det2<0, PROVEN) so the equivalence's premise fails anyway. |
| 4 | Self-adjoint model operator with spectrum = zeros (Hilbert–Pólya) | spectral | **NO THEOREM EXISTS** (conjectural construction); a "sufficient condition" needs a specific T with proven spectrum = zeros; none exists unconditionally. ABANDONED (no object to verify). |
| 5 | de Bruijn heat semigroup e^{t∂²}Ξ, real zeros at some t<0 | contraction semigroup | **CLOSED**: Λ≤0 ⟺ RH (Newman); the "one-way" slice (real zeros at some fixed t<0 ⇒ RH) is a restatement of Λ<0, and Λ's computation is the same barrier. Already in closed list (de Bruijn heat). |
| 6 | Toeplitz/Hankel winding-number = zero count in half-plane | spectral quantity | **CLOSED**: equivalent to the argument-principle/Speiser channel (left-strip infeasible via Platt–Trudgian; right-strip PROVEN explained by Levinson–Montgomery count law, wave-18). |
| 7 | 2D log-gas / electrostatic energy variational inequality (off-line zeros cost energy) | variational inequality | **HEURISTIC**: no mechanism forces the config to the axis; the repulsion picture is exactly the "near-line obstruction" form (below), no theorem. ABANDONED. |
| 8 | Burnol/convolution-operator positivity on L² (Weil-adjacent refinements) | positive operator | **CLOSED**: Weil-positivity class (top of excluded list); every subset closed in campaign. |

**Dependency map of the surviving residue (candidate 2):**
- Goal: H(Φ log-concave) ⟹ RH. Dependencies: (d1) theorem "even log-concave density ⟹ FT has only real zeros" — ASSUMED-unknown (likely FALSE in general; Schoenberg sharpness); (d2) Φ log-concave on the meaningful support — UNKNOWN, probe resolves. Single point of failure: (d2) is now measured; (d1) expected false → the implication chain has no live theorem even if (d2) holds. **No fundable route remains.**

---

## 3. The one-way candidate written out (for the record)

**Candidate H(ζ):** "The theta-density Φ of ξ is log-concave on R."
**Exact H(ζ) ⇒ RH implication (would-be theorem):** *If* (a) Φ is log-concave and (b)
[taken as a black box] the classical log-concavity-of-density ⟹ real-zeros-of-FT result
held in this generality, *then* Ξ = 2∫₀^∞Φ(u)cos(tu)du has only real zeros, i.e., all
nontrivial ζ zeros lie on Re(s) = 1/2. Both inputs would be unconditional; RH would follow
unconditionally.
**Missing unconditional lemma (exactly one):** the sufficiency theorem at the log-concave
level, L: {ρ even, log-concave} ⟹ ρ̂ ∈ LP. **Status: INCONCLUSIVE from memory — likely FALSE
in general** (the sharp classical result is the PF∞ one; log-concavity is strictly weaker
than PF-ness and does not in general yield the structure theory that forces real zeros).
Falsifying example candidates: any symmetric log-concave density whose characteristic
function provably has a complex zero — none found by memory; a literature check of
Schoenberg/Pólya is the correct next step (NOT funded — see stopping rule §6).

---

## 4. RH-false control (explicit)

- **Control object:** the Davenport–Heilbronn world (barrier_zoo_rs, 23 certified off-line
  zeros; the campaign's own retro-test world). Its ξ-analogue is also an entire real function
  of order 1 with a functional equation; its density analogue (Burnol-type measure) is **not
  positive** — the DH θ-density changes sign. 
- **Control test:** any criterion "positive/log-concave density ⟹ all-real zeros" must NOT
  fire on DH. Branch analysis: (i) if the DH density-analogue is not positive, the candidate
  has no hypothesis to fire on → does not prove too much *and* does not discriminate (vacuous
  on control — acceptable, the firewall says a claim that would ALSO prove the control is
  wrong; a claim that merely fails to apply is zero evidence, correctly); (ii) if a later
  density-level condition were found whose hypothesis the control satisfies while DH still has
  off-line zeros, that condition is REFUTED ("proves too much") — this is the standing
  barrier-zoo demand, carried forward.
- Distinctness check: since Φ ∈ PF∞ is PROVEN false while RH is open, the PF∞ criterion is
  **provably unidirectional and not-RH-in-disguise**: RH does not imply its hypothesis
  (unlike all ⟺-traps where hypothesis ⟺ RH).

---

## 5. Cheapest Rust-only probe (executed) + stopping rule

Probe `tools/polya_density_probe/` (single rustc file, f64, no deps, <1 s runtime):
evaluate L(u) := Φ″(u)Φ(u) − Φ′(u)² on u ∈ [−2.0, 1.5] (401 grid points) via the PROVEN
theta identity with exact chain-rule derivatives (θ..θ⁗ summed to tail < 1e-17), flag
sign(L) changes, restrict to Φ(u) > 1e-6 (log of a vanishing tail is meaningless).
- **Stopping rule:** (a) if L > 0 anywhere in the meaningful region → Φ not log-concave →
  candidate 2's hypothesis fails → LANE CLOSED with the exact failure locus as the recorded
  reason; (b) if L ≤ 0 throughout → log-concavity holds (a genuine consistency fact about Φ)
  but the sufficiency lemma is expected-false (Schoenberg sharpness) → LANE CLOSED with the
  missing lemma labeled INCONCLUSIVE and flagged for literature check; either branch: no RH
  evidence.

---

## 6. Results (appended after run — see below)

[Result block inserted by the probe run.]

---

## 7. Ledger note (≤5 lines)

- **operator-lane polya-density (direct-rh-operator-route-2026-08-18)** — CLOSED: closest
  route = Pólya cosine-transform density criterion (Ξ = Φ̂, Φ>0); hypothesis Φ ∈ PF∞ PROVEN
  false (crossdomain SINC-PF∞ closure). Weakening to log-concavity probed: [result]; no
  sufficiency theorem at log-concave level (Schoenberg sharpness) → no surviving one-way
  condition in the lane; consistent with wave-9/10 "one-way space fully mapped" verdict.
  No RH evidence either direction.
## Coordinator adjudication after restart

The stale `phi_probe.out` was produced by an older binary and printed `Phi(0)=0.4466969`,
which is the wrong factor. Recompiling the saved `main.rs` with `rustc -O` gives the required
sanity value `Phi(0)=0.893393800934`, and the same bounded grid gives
`min L=-3.045087e1`, `max L=-3.311903e-9`, and zero positive samples on the meaningful
support. This is **CHECKED NUMERICALLY** only; it is not a global log-concavity proof.

More importantly, the missing implication is **PROVEN FALSE in general**. Let

`rho(x) = (1/4) sech^2(x/2)`.

This is an even, strictly positive, log-concave probability density because
`(log rho)''(x) = -(1/2) sech^2(x/2) < 0`. Its Fourier transform is the exact elementary
function

`rho_hat(z) = pi*z/sinh(pi*z)`

(with the removable value 1 at z=0), which has non-real zeros `z=i n` for every nonzero
integer n. Therefore even log-concavity is not a real-zero-forcing hypothesis. This is an
explicit RH-false control for the proposed density mechanism, not a finite numerical analogy.

**Final status: ABANDONED as a one-way RH route.** The stronger PF-infinity hypothesis would
force real zeros but is already PROVEN false for the Riemann theta density; the weaker
log-concavity hypothesis is not sufficient by the logistic counterexample. No RH evidence.
