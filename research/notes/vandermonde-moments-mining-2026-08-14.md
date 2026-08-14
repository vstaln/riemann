# Vandermonde Moments Mining — Reconnaissance Note

Date: 2026-08-14
Agent: adventurer (reconnaissance, literature mining)
Scope: mine two Baluyot papers for a NEW moment input usable in the certificate's P2 lever
(distinct zeros 5/6 wall, fourth-moment phenomenon). Target: anything that pushes past the
structural 0.6818 ceiling (`research/notes/structural-final-verdict.md`) — a genuinely new
moment STRUCTURE, ideally unconditional.

Sources read (pdftotext extraction into `$SCRATCHPAD/bc-2206.04821.txt`, `bc-2501.12529.txt`):
- Baluyot–Conrey, "Moments of zeta and correlations of divisor-sums: stratification and
  Vandermonde integrals", arXiv:2206.04821v2 (2022).
- Baluyot–Čech, "Multiple Dirichlet series predictions for moments of L-functions: unitary,
  symplectic and orthogonal examples", arXiv:2501.12529v1 (2025).

---

## Paper (a) — Baluyot–Conrey 2206.04821 (Vandermonde stratification)

### Main objects
- Shifted moments of ζ:  (1/T)∫ ζ(1/2+α+it)·ζ(1/2+β−it) dt over finite multisets A, B of
  shifts α, β ≪ 1/log T (p.2, §1).
- Their Dirichlet-polynomial approximations M_{A,B}(T,X) (eq. 1.1), with coefficients
  τ_A(m) = coefficients of ∏_{α∈A} ζ(s+α) (eq. 1.2) — i.e. **weighted divisor-sums**.
- The stratification S_ℓ (eq. 1.5): sum over rational directions M_j/N_j with
  M_1···M_ℓ = N_1···N_ℓ and the delta-method constraints m_j N_j − n_j M_j = h_j.
  This is the "Vandermonde" layer: it stratifies the divisor-sum variety (Wooley/Manin
  arithmetic-stratification reading, p.5).

### Theorems (typed, with hypotheses)
All MOMENT statements are conjectural. The rigorous content is local/combinatorial.

- **Conjecture 1.1** (p.3): if α, β ≪ 1/log T, then M_{A,B}(T,X) ~ Σ_{ℓ=0}^{min(|A|,|B|)} S_ℓ.
  → CONJECTURED (heuristic).
- **Conjecture 1.2** (pp.3–4, eq. 1.6): S_ℓ equals a "Vandermonde integral" — a (2ℓ)-fold
  residue integral over |z_j|=|w_j|=ε of
      ∏ χ(1/2+ξ−z_j+it)χ(1/2+η−w_j−it)
      × ∏ ζ(1+α+β+ξ+η) ∏ ζ(1+α+z_j) ∏ ζ(1+β+w_j)
      × ∏ (1/ζ)(1+α+ξ+η−w_j) ∏ (1/ζ)(1+β+ξ+η−z_j)
      × ∏_{i≠j}(1/ζ)(1−z_i+z_j)(1/ζ)(1−w_i+w_j)
      × ∏ ζ(1+z_i+w_j−ξ−η)ζ(1−z_i−w_j+ξ+η)
      × A(A,B,Z,W,ξ+η)  (Euler product, abs. convergent on the contour).
  → CONJECTURED (heuristic). The "Vandermonde" is the ∏_{i≠j} reciprocal-ζ factor — a
  **determinantal/repulsion structure over the shift variables**.
- **Conjecture 1.3** (p.5): S_ℓ ~ sum of the ℓ-swap terms of the CFKRS recipe (1.3).
  → CONJECTURED (heuristic).
- **Theorem 4.4** (p.19): the LOCAL Euler-product identity. Given a prime p, partitions
  A = A_1∪···∪A_ℓ, B = B_1∪···∪B_ℓ, and shifts ξ,η with Re(ξ)=Re(η)=2ε, the p-adic sum
      Σ_{M_1+···+M_ℓ=N_1+···+N_ℓ, min{M_j,N_j}=0} ∏ p^{N_j(−1/2+ξ−z_j)+M_j(−1/2+η−w_j)}
        × Σ_{d,q≥0}(−1)^q p^{min{q+d,N_j}(1+z_j)+min{q+d,M_j}(1+w_j)−q(2+z_j+w_j)−d(1+ξ+η)}
        × G_{A_j}(1+z_j, p^{q+d−min{q+d,N_j}}) G_{B_j}(1+w_j, p^{q+d−min{q+d,M_j}})
      equals an explicit finite Euler product (displayed p.19) in terms of
      I_{A_{ξ+η}∪W,(Z−)_{ξ+η}} and I_{B∪Z−ξ−η, W−}.
  → **PROVEN** (unconditional). This is a rigorous evaluation of the local (p-adic) factor of
  the divisor-sum stratification — an algebraic/combinatorial identity, NOT a moment theorem.
- Supporting rigorous lemmas: Lemma 3.1 (gamma-function integral), Lemma 4.1, Lemma 4.2
  (generalization of CK's Lemma 2), Lemma 4.3 (local factor recoupling). All PROVEN local
  identities.

### Verdict for paper (a)
PROVEN: only the local Euler-factor identities (Thm 4.4 + Lemmas 4.1–4.3, 3.1).
CONJECTURED: everything about the actual moment (Conj 1.1–1.3), which reproduce the CFKRS
recipe / Keating–Snaith RMT prediction. The paper is explicit (p.1, §1) that it provides
HEURISTIC evidence, and that the Rodgers–Soundararajan random-matrix analog of the
Vandermonde integral is PROVEN on U(N) (p.4), while the ζ-side is conjectural.

---

## Paper (b) — Baluyot–Čech 2501.12529 (MDS predictions)

### Main objects
- Shifted moments of FOUR L-function families (p.2, §1):
  (1) L(s,χ), χ even primitive Dirichlet chars, conductor ≤ Q → ∞ (unitary);
  (2) L(s,χ_d), quadratic Dirichlet (symplectic);
  (3) L(s, f⊗χ_d), quadratic twists of a fixed Hecke eigencuspform (orthogonal);
  (4) L(s, E_d), quadratic twists of an elliptic curve E/Q of non-square conductor.
- Tool: **multiple Dirichlet series (MDS)** heuristic (Diaconu–Goldfeld–Hoffstein), compared
  term-by-term against the CFKRS recipe.

### Theorems (typed)
- **Conjecture 2.2, 3.1, 4.1, 5.1, 5.2** (all "CFKRS [9]"): recipe predictions for the shifted
  moments of families (1)–(4). → CONJECTURED.
- **Conjecture 2.6, 3.3, 4.3**: the MDS has meromorphic continuation + polynomial boundedness
  on a prescribed region, with specified poles/residues. → CONJECTURED.
- **Proposition 2.4, 3.2, 4.2, 5.4**: the MDS is absolutely convergent in a region Re(w) > c.
  → **PROVEN** (unconditional, standard).
- **Proposition 2.8, 3.4, 4.4** (e.g. "Conjecture 2.6 implies Conjecture 2.2 with a
  power-saving error term"): conditional reductions. → **PROVEN as implications**; the
  antecedent is unproved.
- Key content result (abstract + §1): for families (1)–(3) the MDS prediction agrees exactly
  with the CFKRS recipe, term-by-term (one-to-one correspondence of residues ↔ swap terms).
  For (4) the recipe REQUIRES A MODIFICATION (root number ↔ coefficients correlation).
  → CONJECTURED overall; the (4) discrepancy is a genuine structural observation about
  elliptic-curve twists, not about ζ.

### Verdict for paper (b)
PROVEN: convergence propositions (2.4/3.2/4.2/5.4) and conditional implications
(2.8/3.4/4.4). CONJECTURED: all moment asymptotics. No unconditional moment theorem.
No content about the Riemann zeta function itself (it is explicitly about other families).

---

## Transfer table

| New moment statement | Certificate lever it could feed | Unconditional? | Expected strength |
|---|---|---|---|
| Vandermonde-integral form of S_ℓ (Conj 1.2, paper a) — determinantal ∏_{i≠j}(1/ζ)(1−z_i+z_j) structure | P2 fourth-moment / "distinct zeros" weighting: the ∏_{i≠j} factor is a literal *distinct-pair repulsion*, structurally analogous to distinct-zero forcing | NO (CONJECTURED for ζ; PROVEN only on U(N) by Rodgers–Soundararajan) | New STRUCTURE, zero proven strength on ζ-side |
| Local Euler-factor identity (Thm 4.4, paper a) | Rigorous algebraic backbone for any divisor-sum/stratification attack on the fourth moment | YES (PROVEN) | Real but local: a p-adic identity, not a moment bound |
| Recipe ⟺ MDS term-by-term agreement (paper b, families 1–3) | Confirms m3/m4 predictions are robust across heuristics — no new input, just cross-validation | NO (all conjectural) | Zero new strength |
| Modified recipe for elliptic-curve twists (paper b, family 4) | P3/other-family levers only; not ζ; not P2 | NO | Zero for RH certificate |
| MDS meromorphic-continuation conjectures (Conj 2.6/3.3/4.3) | A route to PROVING m3/m4 if the continuation were established — but it is exactly the open step | NO (the continuation is the conjecture) | Zero now; the reduction (Prop 2.8/3.4/4.4) is PROVEN and would be the vehicle |

## Verdict

**Is there a usable NEW input here?**

- **Unconditional new moment input: NONE.** Both papers prove no moment theorem. Every
  moment asymptotic is CONJECTURED and reproduces existing CFKRS-recipe / Keating–Snaith
  RMT predictions. This is CONJECTURED across the board for the ζ moment statements.
- **The one genuinely new STRUCTURE** is the **Vandermonde/determinantal representation of
  the ℓ-swap terms** (Conj 1.2, paper a). Its ∏_{i≠j}(1/ζ)(1−z_i+z_j) factor is a
  distinct-pair repulsion term over the swap variables — the closest thing in these papers to
  the "distinct zeros 5/6" flavor the P2 lever needs. But on the ζ-side it is CONJECTURED
  (INCONCLUSIVE as an input); only the U(N) characteristic-polynomial analog is PROVEN
  (Rodgers–Soundararajan). So it is a possible new ATTACK STRUCTURE, not a new theorem.
- **PROVEN content present** (both papers): local Euler-product identities (Thm 4.4, paper a)
  and MDS convergence/conditional-reduction propositions (paper b). These are real but are
  either local (p-adic) or conditional (antecedent unproved) — neither moves the 0.6818 ceiling.
- No paper addresses distinct zeros, the 5/6 wall, Levinson, or the critical line directly
  (verified: greps for "distinct/simple zero/5/6/fourth moment/Levinson" return nothing
  relevant).

**Bottom line:** All-moment content is conjectural / random-matrix-matching. The only
unconditional findings are local identities that could *serve* a future proof but are not
themselves new moment bounds.

## Context for next agent (architect / builder)

1. The transfer candidate worth an architect look: **promote the ∏_{i≠j}(1/ζ)(1−z_i+z_j)
   Vandermonde factor (Conj 1.2) from a heuristic to a real constraint.** If the determinantal
   structure can be shown to force distinct-pair behavior in a Weil-quadratic-form / inertia
   certificate (the 3/2 − (1/√2)cot(1/√2) machine), it would be a genuinely new P2 input. But
   note honestly: the paper gives the structure as a CONJECTURE, so the work is to find a
   PROVEN avatar of the same determinantal object, not to cite Conj 1.2 as a theorem.
2. Do NOT treat Thm 4.4 (paper a) as a moment theorem — it is a local Euler-factor identity;
   useful only as an algebraic tool inside a divisor-sum proof.
3. Paper (b) is out of scope for the RH certificate (it is about other L-function families),
   except for one meta-point: its conditional reductions (Prop 2.8/3.4/4.4) show the *shape*
   of what a "meromorphic continuation ⇒ moment formula" argument looks like — a template
   only, no ζ content.

## Assumptions
- `[verified]` Both papers' moment statements are conjectural (Conj 1.1–1.3, 2.2/2.6, 3.1/3.3,
  4.1/4.3, 5.1/5.2) and reproduce CFKRS/Keating–Snaith predictions — read directly from the
  abstracts and theorem statements.
- `[verified]` Thm 4.4 (paper a) and Props 2.4/2.8/3.2/3.4/4.2/4.4/5.4 (paper b) are the only
  proven statements — read directly.
- `[verified]` Neither paper mentions distinct zeros / 5/6 / Levinson / fourth-moment-as-lever
  — grep over both full-text extractions returned no relevant hits.
- `[inferred]` The ∏_{i≠j}(1/ζ)(1−z_i+z_j) factor is "the" Vandermonde/determinantal structure
  — the paper itself calls the integral "Vandermonde" and the U(N) analog carries a literal
  ∆̃_ℓ(Z)∆̃_ℓ(W) = ∏(1−e^{γ−γ̂}) Vandermonde-type product (p.4); I did not verify the full
  residue evaluation (Conj 1.2 ⇒ Conj 1.3) line-by-line.
- `[inferred]` "Fourth-moment phenomenon" of P2 corresponds to the k=2 moment M_2(T) =
  ∫|ζ(1/2+it)|^4 dt, which is the highest PROVEN moment (known only for k=1,2 per paper a p.2);
  the papers' shifted-moment machinery specializes to it but proves nothing about it.

## Concrete next step
Architect: assess whether the **determinantal ∏_{i≠j}(1/ζ)(1−z_i+z_j) factor** (paper a,
Conj 1.2) has a PROVEN, RH-free avatar (e.g. via the Rodgers–Soundararajan U(N) formula or
a Selberg/inertia rewriting) that could enter the P2 certificate as a fourth-moment
repulsion constraint. If no proven avatar exists, close this lever with a documented
"CONJECTURED structure only, no unconditional input" note — do not spend builder compute on it.
