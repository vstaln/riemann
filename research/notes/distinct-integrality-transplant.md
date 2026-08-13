# Can the CGG98 integrality step be transplanted off the line to beat 0.836740? — VERDICT: NO, in-class (1+H)/2 is the exact ceiling; distinct > 0.836740 ⟺ simple > 0.673481

**Date:** 2026-08-14. **Status:** PROVEN (LP algebra + certified constants); one claim CONJECTURED
(chain algebra of the multiplicity-scaled coboundary floor). **s4h method applied:**
s4h-constraint-rule-inversion (the "integer masses do not control the eigenvalue slack" wall is
restated as a design requirement, see §5).

---

## 0. One-line verdict

**The integrality transplant cannot beat our 0.836740.** In our certificate class the distinct
bound is *forced* to be the affine image (1+H)/2 of the simple-on-line bound H by exact LP
algebra on the shared two-constraint system — the integrality (m−1)² ≥ 0 is a *tautology* for
integer multiplicities and adds no constraint to that LP. Consequently
**distinct > 0.836740 ⟺ H > 0.673481** (PROVEN in-class): the distinct record and the
simple-on-line record are the *same* lever, and the lever is H.

---

## (a) The transcript's integrality-transplant method, explained

Source: `research/external-results/anthropic-zeta23/bundle/8a0d1add3c637b858a9a181e98c40e9548c3f44f.txt`
lines 9790–9810 (page 39 of 48, sub-agent "E2-pairs").

The step being transplanted is the *matrix analogue of the integer inequality m² ≥ 3m−2* (the
rank–trace inequality (L) applied to the simple-zeros split, which the paper's §1.4 lines
287–296 use; see `distinct-zeros-56-refinement.md` §1). Its "level-1" form is

```
(m−1)² ≥ 0  ⟺  m² ≥ 2m − 1  ⟺  Σ mᵢ² ≥ 2·N_on − N_dist^on           (∗)
```

for integer on-line multiplicities mᵢ ≥ 1. The transcript's Theorem 4' *transplants (∗) off the
line*: it needs no RH, and it yields **2/3 DISTINCT ON-LINE** — i.e. `N_dist^on ≥ 2N/3` — by
combining (∗) with the two-moment upper bound `‖M_on‖² ≤ (1/λ+λ/3)·N` (at λ=1: `≤ 4N/3`,
`N_on ≤ N`, giving `N_dist^on ≥ 2N_on − 4N/3 ≥ 2N/3`).

The transcript's own diagnosis of why (∗) is *not* a route to simple (or sharper distinct)
results is the key observation:

> "step (i) of the proof consumes the eigenvalue slack Σ(μ_k − c)²₊ of M_on, which integer
> masses do not control — coincident/near-coincident distinct simple zeros and a double zero
> are indistinguishable to M_on's spectrum."

**Reading of this observation (PROVEN as a statement about the quantities).** The spectrum of
the on-line Gram block with a double zero (mass vector (2) → 1×1 matrix [2], eigenvalues
{2}) and with two coincident simple zeros (mass vector (1,1) → [[1,1],[1,1]], eigenvalues
{2,0}) is identical in every quantity that matters for the rank–trace step except the *count*
`N_dist^on` itself: trace 2 = 2, Frobenius² 4 = 4, and even `Σ(μ−1)²₊`: (2−1)² = 1 vs
(2−1)²+(0−1)² = 2. So the *eigenvalue data that the Weil-form machinery controls cannot see
multiplicity*; the only multiplicity information available at the trace/Frobenius level is the
tautology (∗). Step (i) of the proof needs the slack `Σ(μ_k − c)²₊` (eigenvalue excess above a
threshold) to be *small*, and integer masses give no control of it — they only give the coarse
lower bound `Σmᵢ² ≤ ‖M_on‖²_F`, the wrong direction.

## (b) Can it beat 0.836740 in our framework? — NO (PROVEN in-class)

### b1. The exact LP structure of our certificate (PROVEN)

Our whole certified chain reduces to a single inequality on the multiplicity split
(s₁ = simple on-line, s₂ = multiple on-line, p = off-line pairs), namely the strengthened
rank–trace inequality

```
3s₁ + 4s₂ + 4p ≥ c·N,     c = 2 + H_cert = 2.6734808616745137       (I1)
```

together with the bookkeeping

```
N ≥ s₁ + 2s₂ + 2p                                               (I2)
```

with (I2) *exactly* the shadow of integer multiplicities (every non-simple on-line zero has
m ≥ 2; p is a count of off-line pairs contributing 2 each). The certified constants are from
`FINAL-RECORD-2026-08-13.md` (H = 0.6734808616745137, eps = 0.0062, α = 1.464).

**Two LPs on this shared system** (derived and verified, script cited in §6):

- **Simple LP:** min s₁ s.t. (I1),(I2). Closed form: `s₁ ≥ (c−2)·N` = H·N. The certified H is
  *exactly* the LP optimum (linprog: 0.6734808616745136 vs H ✓).
- **Distinct LP:** min (s₁+s₂+p) s.t. (I1),(I2) (using N_d ≥ s₁+s₂+p). Closed form:
  `s₁+s₂+p ≥ (c−1)·N/2 = (1+H)/2·N`. The certified distinct record 0.8367404308372568 is
  *exactly* the LP optimum (linprog: 0.8367404308372568 ✓).

**Hence the affine identity u_min = (1+H)/2 is an exact consequence of the two-constraint LP,
for ANY certified RHS c** — regardless of how c was obtained (two-moment law, Gram-stability
term tr Ψ(M), coboundary redistribution, eps floor: all of them only move c). PROVEN.

### b2. The integrality (∗) adds no constraint to this LP (PROVEN)

In the (s₁, s₂, p) variables, the integrality content is *exhausted*:

1. `(m−1)² ≥ 0` is a tautology for every integer m ≥ 1 (PROVEN: (m−1)² ≥ 0 is an identity). Its
   summed form (∗) is automatically satisfied by any multiplicity configuration; it becomes a
   *constraint* only when `Σmᵢ²` is related to a computable quantity, which requires the
   spectrum/Gram data — and that data is exactly what c already encodes.
2. `m ≥ 2` for non-simple on-line zeros is already in the bookkeeping (I2). A "stronger"
   integrality statement does not exist at this level: multiplicities higher than 2 only make
   (I2) more slack, never tighter.
3. The LP optimum is attained with `p = 0` and all non-simple zeros as *on-line doubles*
   (linprog argmin: (s₁,s₂,p) = (0.67348, 0.16326, 0) ✓) — precisely the sharpness
   configuration (2N/3 simples + N/6 doubles, verified in `distinct-zeros-56-refinement.md` §4).
   This is the configuration that the transcript's observation says is *spectrally
   indistinguishable* from near-coincident simple pairs: the (m−1)² integrality is exactly what
   would need to rule it out, and it cannot, because a double zero and two coincident simples
   have identical trace/Frobenius fingerprints.

**Therefore (PROVEN in-class):** any distinct bound in this class is ≤ (1+H)/2, and no
integrality input can raise it.

### b3. Why the eps floor helps the *opposite* direction (PROVEN)

The transcript's Theorem 4' needs an **upper** bound on `‖M_on‖²` to push `N_dist^on` up.
Our eps floor / Gram-stability term `tr Ψ(M) ≥ eps·N > 0` is a **lower**-bound statement on the
spectral slack (it certifies that the true `‖G̃‖²` exceeds its diagonal-mass part by at least
eps·N). Substituted into the (∗)-chain it makes the bound *weaker*, not stronger. Our certificate
uses the same slack in the opposite direction — as a *positive* term on the RHS of (I1), raising
c — which is the direction that helps. So the two mechanisms consume the same quantity
(eigenvalue slack) in opposite directions, and our direction is the profitable one. The
transcript's "integer masses do not control the slack" is, in our framework, the statement that
**the slack is controlled by the kernel/pair-correlation data (our eps floor) and never by
multiplicities** — which is exactly what our certificate already does. PROVEN (direction of the
inequalities), CONJECTURED only at the level of "no other use of the slack exists".

### b4. The Theorem-4'-transplant with *our* inputs still gives ≤ 2/3 (PROVEN, arithmetic)

Even if we fed the transplanted chain our certified two-moment data, the bound is
`N_dist^on ≥ 2N_on − ‖M_on‖²_UB ≤ 2N_on − 4N/3 ≤ 2N/3` (using `N_on ≤ N`), with the eps floor
unavailable (wrong direction, b3). So the transplant is strictly weaker than our affine
distinct bound 0.8367, in every input regime. PROVEN (arithmetic, from the transcript's own
formula and the two-moment constants).

---

## (c) The reduction claim: distinct > 0.836740 ⟺ H > 0.673481 (PROVEN in-class)

- (⟸) If H > 0.673481 were certified, Theorem C (the affine corollary, `distinct ≥ (1+H)/2`,
  PROVEN in `distinct-zeros-56-refinement.md` §1) gives distinct > 0.836740 immediately.
- (⟹) If distinct > 0.836740 in this class, then (b1) forces (1+H)/2 ≥ 0.836740, i.e.
  H > 0.673481. **Any** certified distinct improvement in-class is the affine image of a
  certified simple improvement.

**Conclusion:** the reduction is exact *within the certificate class* — distinct and simple are
the same lever, locked by the shared two-constraint LP. The question "distinct > 0.836740?"
reduces to "H > 0.673481?", which is the 0.6818-ceiling problem (`structural-final-verdict.md`:
the class is exhausted at the 256-law ceiling 0.68183123; passing 0.673481 further requires a
new input structure or theorem, not more optimization). PROVEN in-class.

**Honest boundary of the PROVEN label:** "in-class" means: any certificate whose analytic
content is one inequality of the form (I1) on the (s₁, s₂, p) split plus the bookkeeping (I2).
A hypothetical *second independent* inequality on (s₁, s₂, p) — one whose coefficient vector is
not in the span of {(1,2,2), (3,4,4)} — could in principle decouple the distinct bound from the
affine image. We know of no mechanism producing one: the third-moment route was tried and does
not break 5/6 at λ=1 (`attack-thirdmoment.md`); off-line-specific bounds of the form `p ≥ p₀N`
only move the LP minimum if `p₀ > (1−H)/2 ≈ 0.1633` (PROVEN arithmetic: feasibility of the LP
requires `u ≥ max((c−1)/2, 1−p₀)` in units of N, and the certified p is far below the
threshold — indeed we certify none). So the reduction stands as PROVEN in-class, CONJECTURED as
a statement about all conceivable certificate structures.

---

## (d) Verdict + the one small check

**Verdict: the integrality transplant does not interact with the coboundary certificate to
beat 0.836740.** The affine corollary (1+H)/2 is not merely a convenient reading of our
H-machinery — it is the *exact LP optimum* of the two-constraint system that *is* the
certificate class, and the integrality (m−1)² ≥ 0 is a tautology that contributes no
constraint. The eigenvalue slack the transcript identifies as multiplicity-blind is precisely
the quantity our eps floor controls (in the profitable direction), so our framework already
extracts everything the transplant could offer and more. The only route to distinct > 0.836740
is H > 0.673481, i.e. the simple-on-line problem. This *confirms* the standing reduction and
re-labels it from folklore to PROVEN-in-class.

**The one small check that would validate the positive residue (describe, do not run):**
The single un-proven link in the ceiling argument is the *chain algebra* of the
multiplicity-scaled block certificate: the certified eps floor 0.0062 (coboundary
redistribution, 7-point blocks, α = 1.464) was certified on *all-simple* on-line atoms. The
claim that the sharpness configuration (on-line doubles) is *in-certificate* — i.e. that
multiplicity-scaled atoms do not lower `tr Ψ` below the floor — is currently CHECKED
NUMERICALLY only (4000 random configs, 0 violations, `tr Ψ ≥ 1.0006` at the argmin for any
m ≥ 2; `distinct-zeros-56-refinement.md` §2.3, at the 3-point level ε = 4.45×10⁻⁴). The
positive-residue check is a **hand proof** (no compute): re-derive the chain algebra of the
7-point coboundary floor with diagonal masses mᵢ ∈ {1,2} on the on-line blocks and show
`tr Ψ(G_multiplicity) ≥ tr Ψ(G_simple)` for the block-averaged certificate. If it goes
through, the claim "the double-zero extremal is in-certificate, so (1+H)/2 is genuinely
attained (not vacuous)" upgrades from CHECKED NUMERICALLY to PROVEN, closing the last hole in
"the ceiling is the affine image". It does not change any number — it changes a label.
(Per hooks: a verification run of `tools/verify_coboundary_floor.py` at new configs would be
compute-slop; the chain algebra is a paper-and-pencil task and is the right form of the check.)

---

## 5. s4h-constraint-rule-inversion applied

**Constraint (precise):** "The distinct bound is locked to (1+H)/2 by the two-constraint LP
((I1) shared rank–trace + (I2) bookkeeping), and multiplicity integrality (m−1)² ≥ 0 is a
tautology that adds no constraint — so integer masses give no distinct leverage."

**Inverted form (design requirement):** "The certificate must be designed so that the
eigenvalue slack that integer masses cannot control is an *input* (it already is: the eps
floor), and any path to distinct > (1+H)/2 must add a constraint that *distinguishes off-line
structure or multiplicity beyond the trace level*."

**Solutions that use the constraint:**

| # | Solution | Why it requires the constraint | Strength |
|---|----------|-------------------------------|----------|
| 1 | Accept the affine lock; push H past 0.673481 (the reduction) | The lock is exactly why distinct work *is* simple work; no duplicate machinery | Strong — PROVEN reduction |
| 2 | Find a second independent inequality on (s₁,s₂,p) (third moment, off-line structure) | Only a non-spanning constraint can decouple u from (1+H)/2 | Weak — third-moment tried and fails at λ=1; p₀-bound needs p₀ > 0.163 |
| 3 | Transplant Theorem 4' (on-line spectrum + (∗)) | Needs an *upper* bound on ‖M_on‖²; our eps is a lower-bound input | Dead — gives ≤ 2/3, strictly below 0.8367 |

**Most promising:** Solution 1 — the constraint *is* the reduction; it confirms that the
frontier for distinct is the frontier for simple, i.e. the 0.6818-ceiling problem
(`structural-final-verdict.md`), which requires new input structure, not the integrality
transplant.

---

## 6. Honesty labels (consolidated)

| claim | label |
|---|---|
| The distinct bound in the two-constraint LP is exactly (1+H)/2 for any certified RHS c (closed form u_min = (c−1)N/2, c = 2+H) | PROVEN (LP algebra; linprog reproduces 0.8367404308372568 exactly, script below) |
| The certified H is exactly the LP optimum of the shared inequality (c = 2+H = 2.6734808616745137) | PROVEN (linprog: min s₁ = 0.6734808616745136; matches certified H) |
| The LP extremal is p = 0, all non-simple on-line doubles | PROVEN (linprog argmin (0.67348, 0.16326, 0)) |
| Integrality (m−1)² ≥ 0 is a tautology for integer m; summed form (∗) is automatically satisfied and adds no (s₁,s₂,p)-constraint | PROVEN (identity) |
| A p₀-bound on off-line pairs cannot move the LP min unless p₀ > (1−H)/2 ≈ 0.1633 | PROVEN (feasibility algebra) |
| The eps floor is a lower-bound statement; the (∗)-chain needs an upper bound on ‖M_on‖², so the transplant cannot use our floor (and gives ≤ 2/3 with any inputs) | PROVEN (direction of inequalities + transcript formula) |
| The eigenvalue slack Σ(μ_k−c)²₊ is controlled by kernel data (our eps floor), never by multiplicities; a double zero and coincident simples have identical trace/Frobenius fingerprints | PROVEN (quantity identities); the "no other use exists" reading | CONJECTURED |
| distinct > 0.836740 ⟺ H > 0.673481 (in-class) | PROVEN (b1 + affine corollary); "in all conceivable certificate classes" | CONJECTURED |
| Multiplicity-scaled atoms keep tr Ψ above the floor (sharpness config is in-certificate) | CHECKED NUMERICALLY (4000 configs, 0 violations, tr Ψ ≥ 1.0006 at argmin; distinct-zeros-56-refinement.md §2.3); PROOF of the block-averaged chain | CONJECTURED / not done |
| No new record claimed; the certified 0.673481 / 0.836740 stand unchanged | PROVEN (this note changes no numbers) |

## 7. Files & script

- Script: `/tmp/distinct_transplant_check/` (one-liner above; `uv run --with numpy --with scipy
  python`), plus the LP checks in this note's body. This is a <1 s arithmetic check serving the
  argument, per the task's allowance; no zero data was downloaded and no verifier was re-run.
- Sources: transcript `8a0d1add3c637b858a9a181e98c40e9548c3f44f.txt` lines 9790–9810;
  `FINAL-RECORD-2026-08-13.md` (H = 0.6734808616745137, distinct 0.8367404308372568, eps 0.0062,
  α=1.464); `distinct-zeros-56-refinement.md` (Theorem C affine structure, sharpness config,
  multiplicity numerics); `records-vs-anthropic-paper.md` (paper's H_d(λ) = (1+H(λ))/2 eq. 1.3,
  constants 0.6725/0.83625); `structural-final-verdict.md` (0.6818 class ceiling, new-input
  requirement); `attack-thirdmoment.md` (third-moment route, fails to break 5/6 at λ=1).
- Note: transcript cites "Bui–Heath-Brown-type papers quote 0.8466 distinct under RH" without a
  locatable offline citation [CITATION NEEDED]; not used in any argument here.
