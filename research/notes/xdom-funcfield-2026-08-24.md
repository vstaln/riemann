# Function-field RH vs number-field RH — the SHARP lemma-level gap (2026-08-24)

Status: READ-ONLY idea generation + falsification design. No proof claimed.
Scope: sharpen the ledger's prior Weil–Deligne closure, propose a decidable
shadow, give RH-false control + <20-min probe. Author: adventurer (recon).

---

## 0. What the ledger already closed (cite, then sharpen — do NOT redo)

- **crossdomain-hunt-2026-08-18** (#4 Weil–Deligne): killed at 3 folk-level
  "needs": (a) rational zeta function — ζ/Q is not; (b) algebraic-integer roots —
  ζ's zeros are transcendental; (c) a Frobenius/cohomology functor — none for
  GL(1)/Q. Also closed the Selberg-trace/function-field-analogue line (line 68–69:
  "runs on the same cohomology mechanism as #4"). Verdict: STRUCTURALLY IMPOSSIBLE.
- **wave25-nextmove-weil-negativity (2026-08-19)**: any FIXED finite-basis /
  finite-rank truncation of the Weil (expl.-formula) form has λ_min < 0 **identically
  across RH vs RH-false worlds** (DH character-mod-5 control matches ζ to ±0.1).
  REFUTED the "prime-depth boundary barrier" g0-0. Root finding: negativity is a
  finite-basis discretization artifact, non-separating on BOTH sides.
- **wave-21 g0-1 (Weil–Gram rank)** and **g1-0 (Weil explicit-form arithmetic
  kernel Gram)**: both REFUTED — fire on Beurling/DH/Epstein controls ("prove too
  much"). barrier_zoo (Epstein cls-2, DH, planted-zero Beurling, fake-Weil) is the
  standing RH-false control set (ledger 98, 119).

So the prior closes say "no cohomology, non-separating at fixed rank." That is
TRUE and CHECKED, but it is a *folk* statement. The task: name the single
geometric input with no number-field analogue, at lemma level, so we understand
WHY the finite-rank strikes failed. Below.

---

## 1. The sharp lemma-level gap (the actual missing geometric input)

### 1a. What the function-field proof factually runs on (PROVEN literature)
For C/F_q smooth projective genus g, Weil/Grothendieck give the **rationality**:
    Z_C(T) = P_1(T) / ((1−T)(1−qT)),   P_1(T) = det( 1 − T·Frob | H^1_et(C,Q_l) )
H^1_et(C,Q_l) is a Q_l-vector space of **dimension 2g — finite, and l-independent**
(= rank of the L-function, degree of P_1). Deligne's purity: the eigenvalues
α_1,…,α_{2g} of Frob satisfy |α_i| = √q, i.e. exactly "nontrivial zeros on the
critical line" in the s-normalization Z(q^{−s}).

The **mechanism** is not a random fact about a polynomial: it is a **positivity
theorem on a FINITE-rank self-dual Hermitian space** —
   (i) Poincaré duality ≅ self-duality of the Galois rep on H^1;
   (ii) Weil's form (Castelnuovo–Severi / Weil pairing) is positive;
   (iii) positivity ⟹ Frobenius is a "unitary-times-positive" operator on a
        finite-dim space ⟹ eigenvalues lie on |z|=√q (Weil's original route,
        and the same PSD shape that Deligne's general purity formalizes).
The whole RH is captured by **one PSD check of a rank-2g Hermitian form**.

### 1b. The number-field side (the gap)
ζ(s) = L(s, GL_1/Q). To run the SAME mechanism we would need:
   - a finite-rank Q_l-vector space H with dim H = rank(ζ-radius) = ∞
     (the nontrivial zero set is infinite); and
   - an algebraic spectral realization: the zeros of ζ would be unit-modulus
     eigenvalues of Frob on that H in the s→T normalization.

**Sharp gap, one line:** *In the number-field case there is no finite-rank
self-adjoint operator with algebraic spectrum whose spectral values realize the
nontrivial zeros — the disease is not "no cohomology" (folk) but "infinite rank":
the positivity inequality the mechanism runs on is NONCOMPACT, with no
finite-rank reduction.*

Why "rank = ∞" is the real killer (not just "transcendental roots"):
   - "ζ is not rational" (folk (a)) is the SAME statement as "H would have to be
     infinite-dimensional": Z_C(T) is rational precisely because H^1 is finite-dim
     (2g). Over Q, "2g" would be ∞. 
   - "zeros are transcendental" (folk (b)) is the FOOTPRINT of infinite rank:
     the spectral values of a finite-rank operator over Z̄ are algebraic; an
     infinite-rank spectral set is allowed to be transcendental. So (a)+(b) are
     not independent obstructions — they are consequences of the single rank-∞
     gap.
   - A finite-rank realization WOULD be the object that makes the zeros algebraic
     and a rational char.poly — i.e. its existence is exactly a theorem's worth of
     spectral information about ζ's zeros, not a source of it. Nobody can write it
     down without already knowing the zeros' arithmetic. This is why (a) is "the
     weakest object" (Sec. 3) and why it has never been built.

### 1c. The repo's finite-rank strikes are the EMPIRICAL FOOTPRINT (CHECKED)
wave-25, wave-21 g0-1, g1-0 all truncated the (infinite-rank/noncompact) Weil
form or Gram operator to finite rank/basis and found: (i) λ_min stays negative at
every finite cut; (ii) it does NOT separate RH worlds from RH-false controls.
Label: **CHECKED NUMERICALLY.** These failures are exactly what infinite-rank-
noncompactness predicts: at every finite cut there is a negative direction, and
that direction is common to RH and RH-false worlds because it comes from the
−log·π Archimedean tail, not from zero-location. So Sec-1b's gap is *consistent
with* and *explains* the prior closures rather than re-litigating them.

Conjectural status: that NO finite-rank realizing operator exists (at any rank) is
**CONJECTURED** (it is literally RH-adjacent; one cannot prove non-existence
without essentially the theory of the zeros). Only the finite-cut non-separation
is CHECKED. Labeled honestly.

---

## 2. Why the folk "no Weil conjectures for Q" is the WRONG sharpening (one para)
Saying "there is no cohomology" or "no Weil conjectures" is true but vacuous: it
doesn't say WHICH input is missing, so it can't guide a probe. The sharp version
is *rank*: the function-field RH is a finite-dim PSD statement (rank 2g); every
attempt to port it to Q must confront a noncompact form of infinite rank, and the
ledger's numeric record (all finite cuts non-separating, on controls) is the
resolution of that rank-∞ structure. Any future sufficient lemma must therefore
show either (i) a genuine rank-∞ positivity (⟺-trap risk, Sec-4) or (ii) a
finite-rank object that SEPARATES worlds — which the record says is absent.

---

## 3. (a) Weakest new object that would fill the gap — and why it cannot be built

**Object:** a *finite-rank reflexive* Hermitian operator family {H_d}, rank
d → ∞ as d→∞, with: dim = d, self-adjoint, well-defined algebraic spectrum
Σ(H_d) ⊂ Z̄, and a spectral-convergence theorem Σ(H_d) → {nontrivial zero set of
ζ}  (as d→∞), together with a PSD certificate per finite d.

**Why nobody can build it (honest, CONJECTURED):** PSDness of H_d *would*
separate the RH world from the DH/Beurling controls at finite d — but the ledger
(wave-25, g0-1, g1-0) has CHECKED that every finite-rank realization built so far
fails to separate. For H_d to be the right object it must simultaneously (i) have
algebraic spectrum that converges to ζ's transcendental zeros (forcing d→∞ in a
specific, unknown rate — itself a theorem) and (ii) already know enough about the
zeros at finite d to be separating. That circularity is the construction blocker.
The one structural opening the campaign identifies (GJT-completion / truncated-
moment decomposition) is exactly the attempt to build such H_d; it is hard
(Farmer diagnostic) and not funded-built. So (a) is a restatement of the open
program, correctly: the missing object is an infinite-rank self-adjoint
realization, and its construction is the genuinely-new-math the crossdomain
conclusion demands.

---

## 4. (b) DECIDABLE SHADOW — and its falsification design

### D1 (operational, decidable, <20 min): growing-basis separation of the Weil form
**Statement to test:** prior finite-cut negatives used FIXED bases (wavelet Gram,
Schur). Question: does ANY *basis that grows adaptively with the critical-line
data* (Gabor / entire-function test functions tuned to the known zeros) separate
the RH world from the RH-false controls — i.e. does |λ_min(RH)| → 0 while
|λ_min(control)| stays bounded away from 0, OR do the two families remain
coincident at every d?

- **Evidence value:** non-separation at every growing basis (up to d≈2^10)
  CONFIRMS NUMERICALLY the Sec-1b infinite-rank-noncompact diagnosis — sharpening
  crossdomain #4 from "structurally impossible (argued)" to "numerically
  universal across adaptive finite cuts (checked on 4 controls)". This is the
  sharpest evidence the *kind* of object sought in Sec-3(a) cannot be finite-rank.
- **It does not prove RH** — positive result is consistency evidence, honest.
- **RH-false control:** the barrier_zoo worlds (Epstein cls-2, Davenport–Heilbronn
  = 23 certified off-line zeros, planted-zero Beurling, fake-Weil polynomial), all
  already in repo with certified zeros. DH is the load-bearing one (off-line zeros
  that violate RH while passing most analytic identities — the repo's poison matrix).
- **Falsification (the interesting branch):** if ANY adaptive growing-basis DOES
  separate (λ_min(RH)→0, λ_min(DH)→−c<0, ratio diverging), then Sec-1b is WRONG and
  a genuinely new separating functional exists → that is a NEW LEVER worth funding,
  contradicting the wave-25 "negativity is artifact on both sides" verdict.

### probe spec (<20 min, ~150 lines, Python + existing zoo)
- Reuse the correct-Archimedean-integral machinery in `tools/wave25_schur_weil_probe.py`
  (its X-independence finding is the baseline to beat).
- Inputs: true-ζ zeros (prior validated table), DH 23 off-line certified zeros,
  Epstein-2, planted Beurling world; support cut exp(B) fixed, B∈{1.8,2.5,3.5}.
- Build a GROWING test-function dictionary: d = 2^4,2^5,…,2^10 Gabor/entire
  functions centered on candidate critical-line positions (not a fixed wavelet
  grid — this is the novel part vs wave-25).
- For each d, each world: λ_min(W_d) via working precision 80–120 bits (mpmath/Arb,
  Arb preferred for certified bounds).
- Output: table λ_min(d) per world + separation ratio |λ_min(RH)|/|λ_min(DH)| vs d.
- Verdict rule: ratio → ∞ ⇒ FALSIFIED-the-gap / NEW LEVER; ratio stays ≈1 (wave-25
  plateau: −0.33/−0.67 slices) at all d ⇒ CONFIRMED-non-separating.
- Budget: 4 worlds × 7 d-values × rank ≤1024 eigenvalues ≈ minutes. <20 min total.

### D2 (conceptual shadow, lower priority): genus-2 RH by pure analysis, no cohomology
**Statement:** For genus-2 hyperelliptic curves over F_q (Weil polynomial
det(1−T·Frob|H^1) of degree 4, RH ⟺ its 4 roots on |T|=q^{−1/2}, i.e. explicit
inequalities on c1,c2), prove RH by an **explicit-formula / positivity argument
that never names Frobenius or étale cohomology** — isolating the *transferable
analytic kernel* (a self-dual operator + positivity) from the *algebraic residue*
(the finite-rank Frob). Because genus-2 RH is already PROVEN (Weil), this is not
a new theorem; it is a mechanism-isolation experiment: if the analytic reproof
cleanly separates "finite-rank self-dual positivity" (portable) from
"Frobenius-algebraicity" (not portable), we learn precisely where the number-field
case breaks — operationalizing Sec-1. RH-false control: a formally degree-4
"raw" polynomial that is NOT a Weil polynomial of a curve (fails the Weil
inequalities / Newton polygon) but passes analytic-looking identities — the probe
shows the positivity argument correctly rejects it. Decidable (finite check,
5-min script). Lower priority than D1 because its historical result is known;
its value is purely mechanism-isolation.

---

## 5. Honest bottom line (labels)
- **PROVEN (lit):** rationality/purity give function-field RH via a rank-2g
  finite-dim PSD form; 2g = rank of L-function, l-independent.
- **CHECKED NUMERICALLY (repo):** every finite-rank truncation of the Weil/
  Gram form so far tested is non-separating across RH and RH-false worlds
  (wave-25, wave-21 g0-1, g1-0).
- **CONJECTURED (this note):** the sharp gap is *infinite rank* — no finite-rank
  self-adjoint operator with algebraic spectrum realizes ζ's zeros; folk
  "no cohomology / transcendental roots / not rational" are consequences of one
  rank-∞ obstruction, not three independent ones.
- **DECIDABLE next step:** D1 growing-basis separation on the existing zoo
  (<20 min). A separation would falsify the gap AND hand the campaign a new lever;
  non-separation sharpens the closure to "numerically universal across adaptive
  finite cuts." Either branch is informative. No brand-new machinery needed —
  reuses wave25 probe core + barrier_zoo data.

## Files / sources
- research/notes/crossdomain-hunt-2026-08-18.md (prior #4 closure, lines 28,45-47,68-69)
- research/notes/wave25-nextmove-weil-negativity-2026-08-19.md (finite-rank non-separation, CHECKED)
- research/notes/ledger.md lines 98,119,180,210,951-955,1074,1329-1335 (barrier zoo, prior kills)
- tools/wave25_schur_weil_probe.py (reusable probe core)
