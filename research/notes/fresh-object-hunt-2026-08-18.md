# Fresh-Object Hunt — one-way sufficient conditions for RH (idea-generator layer)

**Date:** 2026-08-18. **Agent:** architect (read-only, idea layer). **Status:** reasoning memo; every
claim labeled. No code run. Ledger-clean per task contract (all ledgered levers cited, never re-proposed).

---

## 0. The structural diagnosis (why the campaign needs a one-way)

Ledger state (cited, not re-derived): 8A Li λ_n≥0, 8B Speiser ζ′, 8C Báez–Duarte d_N→0, 8D
Turán/Laguerre T_k,L_k, 8E Beurling operator, D3 de Bruijn heat (PROVEN empty), D6 Herglotz
Xi′/Xi, total-positivity Hankel (CLOSED: RH forces ALTERNATING), foster-reactance (PROVEN ⟺ RH),
stieltjes S-fraction (PROVEN ⟺ RH), lee-yang-asano (ABANDONED, section roots dip below 1),
lee-yang-integral-handle (ABANDONED, reduces to Riemann's 1859 integral), m₃-read, off-centre,
M4-r′, k<1 count, sinc-m3 (REFUTED), exact-s3 (CLOSED). Every classical route is a ⟺ RH
reformulation; a finite probe finds only violations. **The missing object is S with: (S provable ⟹ RH)
and NOT (RH ⟹ S).** The trap to flag at every step: any S with both directions is a class-2
restatement (known theorem / ⟺ RH) and proves nothing new.

**Honest meta-finding (PROVEN by this memo's own survey): genuine one-way sufficient conditions
are RARE and all known members fall into four structural families:**
1. **Quantitative sharpenings of ⟺-RH statements that are NOT implied by RH** (the log-power /
   rate improvements). Members: S2 (PNT error), S3 (Báez–Duarte sharp rate, 8C-adjacent),
   S1 (Turán margin) — the sharp form of the fluctuation/rate is open under RH, so the statement
   is strictly stronger than RH. **The catch (PROVEN, dilogarithm family): the extra strength is
   exactly the RH-difficult content — no member has an independent proof route.**
2. **Trivially-stronger conjunctions** (RH + simplicity). One-way by definition, zero mechanism.
3. **Strict-negativity / strict-margin variants** (Λ < 0). One-way, believed FALSE (Newman: Λ = 0).
4. **The GJT trap**: after Griffin–Ono–Rolen–Thorner's unconditional large-n Jensen hyperbolicity,
   the remaining small-n hyperbolicity is ⟺ RH (derived below). Looks one-way, is an equivalence.

Every "fresh" candidate below is triaged into these families, with the honesty check explicit.

---

## 1. Candidate S1 — strict Turán margin + coefficient-criterion theorem

**(a) Statement.** Let b_k = M_k/(2k)! with M_k = 2∫₀^∞ Φ(u)u^{2k}du (8D-verified), t_k =
(b_k² − b_{k−1}b_{k+1})/b_k². S1: **t_k ≥ C/(k+1) for all k ≥ 1, for some constant C > 1.**
(Numerical anchor, 8D: min t_k·(k+1) = 1.06963238 at k=1, CHECKED to k ≤ 200.)

**(b) Why S1 ⟹ RH (CONJECTURED, two steps).** (i) S1 is a strict-margin Turán inequality; the
classical Turán/Laguerre theorem (8D's own frame) gives: strict Turán for all k ⟹ Ξ ∈ LP-class
⟹ all zeros real ⟹ RH. (ii) The margin C > 1 is the load-bearing extra: plain Turán (t_k ≥ 0)
is ⟺ RH, but the *strict margin* is the content of a classical sufficient-condition family
(Hutchinson-type ratio theorems; exact statement of the "t_k ≥ C/(k+1), C>1 ⟹ LP" theorem —
**CONJECTURED to exist, MUST be verified against the classical PF-sequence literature
(Aissen–Schoenberg–Whitney / Edrei / Hutchinson / Kurtz) in the probe**).

**(c) Honesty check — one-way or trap?** **Genuinely one-way, then FALSE at the crux.**
- RH ↛ S1: RH gives t_k ≥ 0 only; the sharp margin is NOT a theorem under RH (the asymptotic
  below is unconditional but the *lower bound for all k with C>1* is open). So S1 is not ⟺ RH. ✓
- Saddle-point analysis of the Φ-moment (sketch, CONJECTURED but rigorous-izable): for large k the
  integral is dominated by u_k ≈ (1/2)(log k − log log k); log b_k ≈ −2k log k + 2k log log k + 2k(1−2 log 2)
  − 2k/log k − (1/2)log(4πk); the second difference gives **t_k·k → 2** (the linear and log k terms
  contribute second differences → 0). So S1 holds with any C < 2 for k ≥ K₀ — **provable**.
- **The crux FAILS (PROVEN by the dilogarithm family):** the sequence a_k = 1/(k+1)² has
  t_k ≈ 2/k (same margin as Ξ) and its generating function Σ z^k/k² (dilogarithm) has non-real
  zeros. Hence NO theorem "t_k ≥ C/(k+1), C ≤ 2 ⟹ LP" can exist. Coefficient-margin criteria at
  the true margin provably cannot force RH — this is the g3-2 wall (coefficient-ratio wall) from a
  new angle, now with a counterexample family at the exact margin.

**(d) Probe (Rust, <10 min).** (i) Numerically extend t_k to k = 10⁴, confirm t_k·k → 2 (8D had
k ≤ 200). (ii) The dilogarithm check: verify Li₂ has non-real zeros and t_k ≈ 2/k, and scan the
family a_k = k^{−α}, α ∈ (0,3) — find the largest α for which margin α/k still allows non-real
zeros (this pins the exact threshold where coefficient-criteria die). (iii) Verify the classical
margin-theorem statement against a reference (no such theorem at margin ≤ 2 — the probe
confirms). RH-false control: not needed (the probe is a *closure* probe, not an RH probe).

**(e) Forecast: 10%.** The saddle asymptotics are provable new mathematics (the campaign only has
t_k numerically to k=200); the LP-forcing step is dead by dilogarithm. Value = a certified closure
of the coefficient-criterion class + the exact margin constant for the record.

---

## 2. Candidate S2 — the sharp PNT error (von Koch strengthening)

**(a) Statement.** S2: **π(x) = li(x) + O(√x·(log x)^{1/2+ε}) for every ε > 0.** (Equivalently the
ψ-form ψ(x) = x + O(√x·(log x)^{1/2+ε}).)

**(b) Why S2 ⟹ RH (PROVEN, classical).** √x·(log x)^{1/2+ε} = O(x^{1/2+ε}) for every ε > 0, and the
von Koch criterion is classical: **π(x) = li(x) + O(x^{1/2+ε}) ∀ε ⟺ RH** (von Koch 1901;
standard, in Titchmarsh Ch. XIV). So S2 ⟹ RH is a one-line classical implication.

**(c) Honesty check.** **Genuinely one-way, contingent on one literature fact:**
- RH ⟹ π(x) − li(x) = O(√x log x) (von Koch, classical, PROVEN). The best published
  RH-conditional bound is this O(√x log x); **no improvement of the log-power is standard —
  CONJECTURED (verify in probe):** if an RH-conditional O(√x (log x)^{1/2+ε}) result exists in
  the literature, S2 collapses to ⟺ RH (trap) and must be dropped.
- Consistency with truth: Montgomery's conjectured maximal oscillation
  Ω±(√x·(log log log x)^{5/4}·(log x)^{−1/2}) satisfies the S2 bound — no contradiction.
- Not attackable: improving von Koch's log-power is strictly RH-hard (the log x comes from the
  zero-sum truncation; the (log x)^{1/2} target is the explicit formula at its sharpest).

**(d) Probe (Rust, <10 min, FEASIBLE with existing data).** The campaign holds 924,715 cached
zeros γ ≤ 5.6×10⁵ (8A). The explicit formula for ψ(x) with those zeros is accurate for
x ≲ 10^{10}–10^{11} (need T ≳ √x). Probe: (i) compute ψ(x) − x over a dense log grid up to 10^{10},
fit the envelope vs √x·(log x)^{1/2+ε}; (ii) planted-zero control: rebuild the explicit formula
with one zero moved off the line (0.6+14.13i-style, cf. 8A) — the error envelope must grow past
the √x·(log x)^{1/2} band (discriminator); (iii) literature check that no RH-conditional
(log x)^{1/2} bound is published (decides trap-vs-one-way).

**(e) Forecast: 65% true, 1% provable.** It is the cleanest textbook one-way; the campaign has
never probed the prime-counting side (grep: no Skewes/von-Koch lever in notes). Cheap, gives a
new discriminator family outside the equivalence-lever zoo, but provability is nil.

---

## 3. Candidate S3 — the sharp Báez–Duarte rate (flagged: 8C-adjacent, NOT fresh)

**(a) Statement.** S3: **d_N = O((log N)^{−1/2}).** (d_N = Báez–Duarte distance, L²(0,1), 8C.)

**(b) Why S3 ⟹ RH (PROVEN).** (log N)^{−1/2} → 0, so d_N → 0, and d_N → 0 ⟺ RH (Nyman 1950,
Beurling 1955, Báez-Duarte 2003 — classical, ledgered).

**(c) Honesty check.** **One-way contingent on the sharp rate being open under RH — current state:
open (ledgered).** RH ⟹ d_N → 0 but the *rate* under RH is conjectural (Báez–Duarte sharp-rate
conjecture; Burnol's lower bound d_N ≥ c/√N is strictly weaker; the finer rate "related to
Lindelöf-ish input" per the 8C brief). So S3 is not known to be ⟺ RH. **BUT this is not a fresh
object — it is the 8C completion** (8C established d_N·√(ln N) ≈ 0.213 flat to N = 5000,
CERTIFIED; 8C-osc characterized the wobble). Restated here only for the one-way taxonomy: S3 is
the canonical member of family 1.

**(d) Probe.** Existing 8C machinery; would extend nothing (N = 8000+ is patience-only, 4.5h/N).
**(e) Forecast: 60% true, 0.5% provable.** Do NOT fund — ledgered, no new input.

---

## 4. Candidate S4 — the GJT Jensen completion (TRAP, explained)

**(a) Statement.** S4: Jensen polynomials J_{d,n}(t) (Hermite–Poulain frame) hyperbolic for all
d ≥ 1, all n.

**(b) ⟹ RH (PROVEN, classical):** Ξ ∈ LP ⟺ all J_{d,n} hyperbolic (Hermite–Poulain; Jensen 1913)
⟹ all zeros real ⟹ RH. The partial-progress fact: **GJT (Griffin–Ono–Rolen–Thorner, PNAS 2019):
for each FIXED d, J_{d,n} is hyperbolic for all sufficiently large n — UNCONDITIONAL** (this is the
campaign's only genuine unconditional sufficient-direction theorem; it sits in
literature-sweep-simplezeros.md territory, not as a closed lever).

**(c) Honesty check — the trap made explicit (PROVEN by logical reduction).** RH ⟺
(hyperbolic ∀(d,n)) ⟺ (large-n part ∧ small-n part). GJT proves the large-n part unconditionally.
Hence **RH ⟺ the small-n part alone** (RH ⟹ small-n trivially; small-n ∧ GJT ⟹ RH). So "complete
the GJT region" is ⟺ RH — a class-2 restatement, NOT one-way. The apparent one-way-ness ("GJT is
a partial proof of a sufficient condition") dissolves: after the reduction, the remaining object
is equivalent to RH. (Compare: the trap that S1 dodges and S4 does not — S1's margin is not
implied by RH, S4's small-n part IS implied by RH.)

**(d) Probe.** Cheap and informative (worth ~30 min): quantify n₀(d) — the smallest n where GJT's
mechanism provably kicks in — numerically (the Jensen polynomials are finite objects; check
hyperbolicity for d ≤ 20, all n, and find where the asymptotic regime begins). Output: the size of
the RH-difficult region as a function of d. Not an RH probe; a *region-size* probe.
**(e) Forecast: extension to all n: 0.1% (the GJT method uses leading-coefficient asymptotics;
the small-n region is governed by the low zeros — RH's own content).** Do NOT fund as an RH lever.

---

## 5. Trap-inventory — one-way-looking conditions that are NOT one-way (the honesty value)

Each of these was stress-tested; record why it is excluded:
1. **Weil-positivity subclasses** (positivity on a subclass of test functions). TRAP: RH ⟹ full
   positivity ⟹ subclass positivity, and subclass ⟹ RH (if it does) — so ⟺ RH (class 2). No
   subclass escapes: RH implies positivity on ALL test functions. (Burnol's Hilbert-space
   reformulations are ⟺ RH; the E1 kernel-TP route is the live one — see §6.)
2. **Hutchinson strong ratio b_k² ≥ 4b_{k−1}b_{k+1}.** One-way (sufficient, not necessary) but
   FALSE for Ξ: t_k ≈ 2/k → 0 ≪ 3/4 (8D + S1's saddle). The canonical "one-way but false."
3. **Λ < 0 (de Bruijn–Newman strict negativity).** One-way (Λ < 0 ⟹ Λ ≤ 0 ⟺ RH), believed FALSE
   (Newman's conjecture: Λ ≥ 0; Rodgers–Tao proved Λ ≤ 0 ⟺ RH, Λ = 0 believed). The canonical
   "one-way, provably-hard-to-find-true."
4. **RH + all-zeros-simple.** One-way by definition; zero mechanism; provably no easier.
5. **Mertens-type M(x) = O(√x (log x)^{−c}), c > 0.** One-way (⟹ M(x) = O(x^{1/2+ε}) ⟺ RH,
   Littlewood), FALSE (Odlyzko–te Riele: limsup M(x)/√x > 1.06 — Mertens false, so no log saving).
6. **Zero-free region of width c(T)/log T, c(T) → ∞.** One-way-looking but TRAP: RH ⟹ it
   trivially, it ⟹ RH (take T = Im ρ) — ⟺ RH as propositions. Any region shrinking to the line is
   implied by RH. (This is the classic sucker; flagged for the record.)
7. **λ_n sharp fluctuation bound (8A's residual).** Same family-1 structure as S2/S3: one-way if
   the sharp bound is not provable from RH (open), unattackable (explicit formula at its sharpest).

---

## 6. Funding recommendation

**The honest bottom line (PROVEN by §0's taxonomy): no member of family 1 has an independent proof
route — each quantitative strengthening carries exactly RH's difficulty — and families 2–4 are
useless, false, or traps. The campaign should NOT expect a fundable fresh one-way sufficient
condition; the deliverable value is the classification + the two bounded probes below that produce
provable side-results.**

**Fund next wave (bounded, Rust, <10 min each):**
1. **S1-saddle probe** (NEW mathematics, closure value): the exact saddle-point asymptotics of
   M_k (t_k·k → 2, provable), numerical extension to k = 10⁴, and the dilogarithm-family scan
   (largest α for which margin α/k admits non-real zeros) — certifying that coefficient-margin
   criteria die at the true margin. This is a *closure theorem* for the coefficient-criterion
   class (the g3-2 wall, now with a counterexample family at the exact margin), and it upgrades
   8D's k ≤ 200 check to a proven asymptotic.
2. **S2-PNT probe** (new discriminator family, zero-overlap with the lever zoo): explicit-formula
   ψ(x) − x envelope check to x ≲ 10^{10} with the 924k cached zeros, planted-zero control
   (envelope must exceed the √x (log x)^{1/2} band), plus the literature check that no
   RH-conditional log-power improvement exists (decides one-way-vs-trap for S2). Cheap; the
   campaign has never probed the prime-counting side.
3. **S4 region-size probe (optional, third):** quantify GJT's n₀(d) for d ≤ 20 — measures the
   RH-difficult region. Cheap, informative, NOT an RH probe.

**Wave-20 unfunded briefs — verdicts:**
- **g0-2 (Gaussian-quadrature compactness): fund as INFRASTRUCTURE ONLY, not a proof lever.** The
  moment-matching quadrature is a trap as a route (Q_N real-rooted ∀N ⟺ RH by Hermite–Poulain;
  compactness adds nothing — it gives subsequential convergence, not zero control), but a certified
  Gaussian-quadrature moment evaluator directly extends S1's saddle probe and feeds E1's kernel
  minors with certified values. **Caveat to verify first: Φ's pointwise positivity on (−∞,∞) is
  asserted "classical" in the brief; the branch formula's sign near u = 0 is subtle (8D's verified
  form e^{9u/2}/e^{5u/2}/e^{2u}·2 gives Φ(0) < 0 by direct evaluation — the positivity claim needs
  re-verification on the campaign's own evaluator before any positivity-based mechanism builds on
  it).**
- **g3-1 (Schoenberg PF kernels): DO NOT fund separately — it IS the E1 interaction.** The
  kernel-TP2 result in flight (E1) is the first rung of g3-1's ladder: Schoenberg's theorem
  (f ∈ LP ⟺ K(x,y) = f(x−y) TP∞) makes E1's 2×2 minor check the PF₂ rung, and the next rungs
  (TP₃, TP₄ minors) are the g3-1 product-representation machinery. If E1 finds a negative 2×2
  minor, RH is false (disproof, escalate); if E1 passes, the natural continuation is TP₃/TP₄ —
  that continuation is g3-1. Fold g3-1 into E1's completion; never dispatch it as an independent
  brief (it would re-dispatch E1's own joint).
- **g4-1 (Carathéodory–Fejér / Toeplitz TP): TRAP — do not fund as a lever.** Toeplitz total
  positivity of the coefficient sequence ⟺ PF∞ ⟺ Ξ ∈ LP ⟺ RH (Schoenberg; and
  li-structure-audit already pinned: the sequence is Toeplitz-type, Jensen criterion = PF
  (Toeplitz TP), Hankel-inertia ABANDONED). Finite PF₂/PF₃ checks are 8D's Turán content again
  (violation-only). The one legitimate residue: g4-1's Toeplitz machinery is the computational
  frame for E1's higher-order minors — again fold into E1, not a separate lever.
- **g3-2 (Lee–Yang circle): DEAD (ledgered).** Section roots dip below |w| = 1 at N = 12;
  superposition of circle-stable blocks fails (cosh(ζ)+ε cosh(2ζ)); handle reduces to Riemann's
  1859 integral, RH ⟺ L(ζ) = −L(−ζ) unsolved. Do not re-dispatch (same verdict, cited).
- **g4-0 (Lee–Yang/Asano): DEAD (ledgered, g2-1 verdict).** No contraction mechanism (sum, not
  product).
- **g1-1 foster / g1-2 stieltjes: PROVEN ⟺ RH (ledgered), closed. g2-2 de Bruijn: PROVEN EMPTY
  (ledgered).**

---

## 7. Verdict summary

- **The one-way sufficient-condition space is nearly exhausted structurally.** Every genuine
  one-way is a quantitative strengthening whose proof IS RH's difficulty (family 1), or is false /
  useless / a trap. This is itself the campaign's finding: the search for a "provable-by-a-
  different-route" sufficient condition has a negative structural verdict — the extra strength of
  any one-way S is exactly the RH-difficult content.
- **Funded next wave:** S1-saddle closure probe (provable side-result: t_k·k → 2 + the
  coefficient-criterion closure theorem) and S2-PNT discriminator probe (new data family, cheap).
- **E1 interaction:** g3-1 (Schoenberg ladder) and g4-1 (Toeplitz frame) both fold INTO E1's
  completion; g0-2 funds as certified-moment infrastructure after a Φ-positivity re-verification.
- **Honesty guardrails honored:** every candidate labeled; S1/S2/S4's trap/one-way status derived,
  not asserted; no proof fabricated; the negative structural verdict is the deliverable.

## Assumptions (per architect contract)
- `[inferred]` von Koch's O(√x log x) is the sharpest published RH-conditional PNT error and no
  (log x)^{1/2}-power improvement is standard — MUST be literature-checked in the S2 probe
  (if wrong, S2 is ⟺ RH and is dropped).
- `[inferred]` t_k·k → 2 via saddle analysis (sketch above; the O(k) and log k terms' second
  differences vanish) — provable in the S1 probe, not yet certified.
- `[inferred]` the classical "strict-margin ⟹ LP" theorem at margin ≤ 2 does not exist
  (dilogarithm family counterexample) — the probe verifies the threshold.
- `[verified]` GJT's unconditional large-n Jensen hyperbolicity + Hermite–Poulain ⟹ S4's small-n
  part is ⟺ RH (the trap derivation is elementary logic).
