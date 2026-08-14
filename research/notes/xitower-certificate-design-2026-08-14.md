# Xitower certificate DESIGN (P5) — a derivative certificate that carries multiplicity

**Agent:** BUILDER (P5 derivative-tower structure). **Date:** 2026-08-14.
**Status:** STRUCTURE DELIVERED (no record claimed). Companion to `attack-xiprime2-tower.md`
(which KILLED the *pair-density* use of ξ″) and `structural-final-verdict.md` (the 0.6818 ceiling).
**Reads applied:** `hooks/agents.md` charter; `attack-xiprime2-tower.md`; `structural-final-verdict.md`;
`s4h-constraint-rule-inversion`; `s4h-logic-consistency-check`.

---

## 0. Constraint inversion (what the ceiling forces — s4h-constraint-rule-inversion)

**Constraint (precise):** the in-class Weil quadratic certificate on ξ proves p₁ ≤ 0.6818, and
`structural-final-verdict.md` names the missing lever: "an explicit-formula bound on Σ (m_ρ − 1),
with m_ρ the multiplicity" — the ξ-form alone carries no m_ρ term.

**Inverted form (as design requirement):** a new certificate must *make the multiplicity term
appear as a free structural variable*, not merely re-optimize the ξ density.

**Answer to the skill's question ("what object does the derivative tower make available?"):**
the tower makes available the **evaluation of a derivative at each zero, ξ′(ρ)**, which is **zero
iff ρ is a multiple zero** (classically ξ′(ρ)=0 ⇔ multiplicity ≥ 2, and under RH the reciprocal
|ξ′(ρ)|⁻¹ is well defined exactly at the simple zeros). ξ(ρ)=0 is true at *every* zero and carries
no multiplicity bit; ξ′(ρ) carries the bit. That bit is precisely what the ceiling says is missing.

---

## 1. The certificate object (STRUCTURE)

**Objects.** Enumerate (a finite test window) the on-line zeros of ξ by ordinate γ_ρ, counted
**with multiplicity** (N of them). Define the two Hermitian forms on ℂ^N:

- **Weil form W** (the existing ξ-certificate): W = Σ_ρ m_ρ · (Weil-explicit-formula kernel on γ_ρ),
  i.e. rank-one blocks of weight m_ρ per *position*; tr W = N, rank W ≤ N_d (distinct count).
  *This is the form whose inertia gives the 67.25% / 0.6818 machinery.* **[verified = in-class]**

- **Derivative form Q** (the NEW object): the quadratic form in ξ′-evaluations,
  Q = Σ_{ρ simple} |ξ′(ρ)|⁻² · q_ρ q_ρᵀ,  with q_ρ a fixed vector block per ordinate and
  weight **w_ρ = |ξ′(ρ)|⁻²**.
  Equivalently Q = Σ_ρ m_ρ · b_ρ · (single-zero block), where **b_ρ = [ξ′(ρ) ≠ 0] / |ξ′(ρ)|²**
  is 0 at every multiple zero. So Q *drops the rank of every multiple-zero position to zero*.

**Compression pattern (which pairs / off-line blocks).** Exactly as in the ξ-certificate, the
matrix is organized into (i,j) blocks by ordinate; the same (1,1)-block calculus and the same
off-line/zero-density blocks carry over **verbatim**, with the single change that the diagonal
block at position ρ is multiplied by b_ρ. No new block topology is introduced — the compression
is "same frame, multiplicity-weighted diagonal."

**The (1,1)-block Sylvester analogue.** In the ξ-form the (1,1) block has trace p₁ (simple
fraction) and the rank–trace–inertia bound reads rank ≤ (1,1)-entries that are nonzero. In Q the
(1,1)-block trace is

> tr Q = Σ_{ρ simple} 1/|ξ′(ρ)|² =: G,   and   tr Q² = Σ_{ρ simple} 1/|ξ′(ρ)|⁴ =: H,

and Sylvester/Cauchy gives **rank Q ≥ G² / H**, while by construction **rank Q ≤ N_s** (the number
of simple zeros). This is the multiplicity-carrying analogue of the (1,1)-block computation: the
ξ-form bounds N (counted with multiplicity) from below by its trace; Q bounds **N_s** — the simple
count — from below by G²/H, a *negative-moment* (Gonek) quantity.

**Synthesis into a NEW inequality.** Pair the two forms in one PSD block matrix:

```
M = [ W + λ₁·(I − P_offline)        λ₂·(coupling from ξ′ explicit formula) ]
    [ λ₂·(coupling)                 λ₃·Q + (multiplicity-defect block)      ]
```

The diagonal block W already certifies (via inertia) the fraction of on-line zeros; the new
block Q certifies the simple fraction through rank Q ≤ N_s. Together they give a *two-trace*
inequality:

**CONJECTURED (structure, to be certified):**  N_s ≥ G²/H  with G = Σ 1/|ξ′(ρ)|²,
and the multiplicity defect enters as  Σ_ρ (m_ρ − 1) ≥ N − N_s  — a term that is **absent** from
the ξ-certificate's objective but present here as the rank drop of Q.

---

## 2. The KEY new ingredient vs the ξ-certificate

**ξ′(ρ)=0 iff ρ is a multiple zero** [PROVEN, classical: ξ(ρ)=ξ′(ρ)=0 ⇔ multiplicity ≥ 2; under RH
all zeros are on the line so the derivative is taken on the line]. The ξ-certificate's data
ξ(ρ)=0 is identical at every zero; the derivative data splits the zero set into **simple**
(b_ρ > 0) and **multiple** (b_ρ = 0). This split is exactly the multiplicity information
`structural-final-verdict.md` says is missing ("a bound on Σ (m_ρ − 1)").

**What inequality the derivative adds (precise statement):**

- Weil form W: rank W ≤ N_d, tr W = N → gives the *distinct/on-line* proportion.
- Derivative form Q: rank Q ≤ N_s, tr Q = G, tr Q² = H → **rank Q ≥ G²/H** → gives the
  **simple** proportion N_s/N via the negative-moment sum G = Σ 1/|ξ′(ρ)|².

So the tower's contribution is a **second trace inequality whose free variable is N_s**, not a
fourth moment of ξ-evaluations. It does NOT reuse the ξ″ pair-density machinery that
`attack-xiprime2-tower.md` killed — that kill applies to using ξ″ as a *density*, i.e. to the
FGL coefficient system α₁^(j) = j(Λlog). This design uses the **value of ξ′ at zeros**, a
different functional.

**Consistency note (s4h-logic-consistency-check):** the T-2 kill and this design are not in
conflict. T-2 killed "ξ″-pair-density → κ₁^(2) ≥ κ₁^(1) → vacuous"; it never touched "ξ′(ρ)=0
screens multiplicity". The two attack-xiprime notes are attacks on the ξ′-*density*; this is an
attack on the ξ′-*evaluation at zeros*. No requirement in either note blocks it. **[consistency: CLEAN]**

---

## 3. Worked toy computation (typed; one <1min float probe)

Finite-dimensional model: three distinct zeros with multiplicities m = (1,1,2), derivative values
ξ′(ρ) = (2.0, 0.5, 0.0). Script: `toy_tower.py` in the session scratchpad (path below), run via
`uv run --quiet python toy_tower.py`.

| Quantity | Value |
|---|---|
| N = Σ m (zeros with multiplicity, what pair correlation counts) | 4 |
| N_d (distinct) | 3 |
| N_s = # {ξ′(ρ) ≠ 0} | 2 |
| M = # {ξ′(ρ) = 0} = # multiple zeros | 1 |
| multiplicity defect Σ (m_ρ − 1) = N − N_d | 1 |
| rank bound of W: rank W ≤ N_d | 3 |
| rank bound of Q: rank Q ≤ N_s | 2 |
| rank drop = N_d − N_s = M (multiplicity term appears) | 1 |
| N − N_s (multiplicity-weighted drop) | 2 |

**Belief the probe changes:** CONFIRMS the structure — the derivative form's rank upper bound
equals the **simple** count, so the multiplicity term Σ(m_ρ−1) appears as a *rank drop* that the
ξ-form cannot see. (Float check is illustrative, not a theorem: the real weights are 1/|ξ′(ρ)|²
and the real certification needs the Gonek sum G.)

**Infinite-dimensional analogue (typed):** in the real certificate, replace "rank" by
tr/tr²-inertia on the (1,1)-block: rank Q ≥ G²/H with G = Σ_{ρ simple}|ξ′(ρ)|⁻²,
H = Σ_{ρ simple}|ξ′(ρ)|⁻⁴, and N_s ≥ G²/H is the simple-count inequality. The multiplicity
defect Σ(m_ρ−1) = N − N_d is bounded below by N − (size of the largest rank-Q bound), which is
the new input the ceiling demands. **[CONJECTURED — structure; needs the Gonek-sum certification]**

---

## 4. Is the tower input unconditional?

**No.** The input G = Σ_{γ≤T} 1/|ξ′(ρ)|² is a *negative second moment of ξ′ at zeros* —
precisely the **Gonek conjecture** class:

> **Gonek conjecture:** Σ_{γ≤T} 1/|ζ′(ρ)|² ~ (6/π³)·T·log T.

**Status (per `structural-thread-newinput-2026-08-14.md` §3, the Milinovich–Ng cite):**
**CONJECTURED**; Milinovich–Ng 2011 (arXiv:1106.1160) prove **a lower bound of half the conjectured
value, conditional on RH + simplicity of zeros**. The full Gonek sum is **not unconditional**.
[Source read: `structural-thread-newinput-2026-08-14.md`, table row "Gonek conjecture …" — label as
cited there; Milinovich–Ng 1106.1160 abstract verified in that prior session.]

**Consequence for the design:** the derivative certificate's *weight* G is RH+simplicity-conditional
today; the **structure** (rank Q ≤ N_s, the multiplicity split) is unconditional in form but its
trace magnitude is not proven. This is the honest status: the tower supplies the **missing
variable** (N_s), not yet the missing **magnitude** (G ≥ c·T log T unconditionally).

**Labels:** structure [CONJECTURED]; multiplicity split ξ′(ρ)=0 ⇔ multiple [PROVEN, classical];
Gonek magnitude [CONJECTURED]; Milinovich–Ng half-bound [PROVEN conditional on RH+simplicity, per
prior note's cite].

---

## 5. Honesty / edge cases (s4h-logic-consistency-check)

- **Not a record.** This is a certificate STRUCTURE; no p₁ bound is claimed. Any number that would
  follow needs the Gonek sum certified first. **[label: STRUCTURE]**
- **The ξ″-density kill does not reach here.** T-2's α₁^(j)=j(Λlog) inflation concerns ξ″/ξ′
  coefficient *series*, not the *value* ξ′(ρ). Two different functionals; no contradiction.
  **[consistency: CLEAN]**
- **Hidden assumption:** the PSD block matrix M and the coupling block need an explicit formula
  for Σ f(ρ)·(1/ξ′(ρ)) type cross terms to be certified; that explicit formula is not derived here.
  Flag: the coupling λ₂ block is the least-specified part of the structure. **[assumption flagged]**
- **Edge case (all zeros simple):** then Q has full rank N_s = N, G and H are both convergent
  under the Gonek conjecture, and the design reduces to the ξ-certificate — correct, no false
  multiplicity term. **[consistent]**

## 6. Files / commands

- `toy_tower.py` — session scratchpad `/tmp/commandcode-1000/-home-vstaln-riemann/61a49810-b85a-43a0-929b-94527c54ff96/scratchpad/toy_tower.py`; run `uv run --quiet python toy_tower.py`. Output recorded in §3.
- No repository files modified (structure deliverable only).

## 7. One concrete next step

Derive the **explicit formula for the Gonek-weighted trace G = Σ_{ρ simple} 1/|ξ′(ρ)|²** in the
Weil/Guinand kernel form (the analogue of the (1,1)-block trace computation), so that G²/H can be
certified against a test-function pair; this converts the structure into the first candidate
simple-count inequality. **[next step: explicit-formula derivation for G]**
