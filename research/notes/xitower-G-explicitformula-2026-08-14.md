# Xitower G: explicit formula for G = Σ 1/|ξ′(ρ)|² — and why it is NOT the Gonek sum

**Agent:** BUILDER (atomic next step of `xitower-certificate-design-2026-08-14.md` §7).
**Date:** 2026-08-14. **Scope:** closed-form derivation only; no compute beyond trivial arithmetic.
**Primary source fetched this session:** Milinovich–Ng, "A note on a conjecture of Gonek",
arXiv:1106.1160v1, *full text read* (journal: Funct. Approx. Comment. Math. 46 (2012) 177–187,
DOI 10.7169/facm/2012.46.2.3). PDF cached in session scratchpad `mn2011.pdf`/`mn2011.txt`.
**Reads applied:** `hooks/agents.md`; `xitower-certificate-design-2026-08-14.md`;
`structural-thread-newinput-2026-08-14.md`; `s4h-investigation-source-trace`; `s4h-probability-expected-value-calculation`.

---

## 0. Verdict up front

**Three independent findings, each decisive:**

1. **Normalization bug.** G as *literally* written — Σ 1/|ξ′(ρ)|² — is **not** the Gonek sum.
   |ξ′(ρ)| = (π/2)^{1/4} γ^{7/4} e^{−πγ/4} |ζ′(ρ)| (1+O(1/γ)), so
   1/|ξ′(ρ)|² = (2/π)^{1/2} γ^{−7/2} **e^{πγ/2}** |ζ′(ρ)|⁻². The exponential e^{πγ/2} makes
   G_ξ ≫ e^{πT/2} T^{−O(1)} and concentrates all Cauchy mass on the top zero. **PROVEN**
   (Stirling; elementary). The certificate weight must be renormalized to **ζ′**, not ξ′.

2. **The Gonek conjecture is mis-stated in both prior notes.** The correct conjecture (Milinovich–Ng
   (1.1), verbatim from the paper) is **Σ_{0<γ≤T} 1/|ζ′(ρ)|² ~ (3/π³)T** — *no* log T and *no* 6.
   The notes' "(6/π³)T log T" is wrong on both counts. Milinovich–Ng prove the **half-value**
   lower bound **Σ ≥ (3/(2π³) − ε)T**, conditional on **RH + simplicity**. [The "half the
   conjectured value" phrase is only internally consistent with the (3/π³)T conjecture, since the
   theorem is (3/2π³)T — with no log T.]

3. **The Cauchy route the certificate relies on is vanishing regardless of hypotheses.**
   rank Q ≥ G²/H (Cauchy–Schwarz on weights w_ρ = 1/|ζ′(ρ)|²) gives, under the full Gonek
   conjecture (G ~ (3/π³)T) *and* Ng's k=2 conjecture (H = Σ1/|ζ′(ρ)|⁴ ~ C₂ T log T):
   **N_s ≥ G²/H ~ (9/(π⁶C₂))·T/log T** — a **zero asymptotic proportion** (N_s ~ (T/2π)log T).
   Cauchy is saturated only by *equal* weights, which the zero derivatives do not have. So the
   G²/H mechanism **cannot certify any positive simple fraction**, even if G were proven
   unconditionally at full Gonek strength. **The conditional nature of Milinovich–Ng is the
   smaller problem; the vanishing Cauchy bound is the fatal one.**

---

## 1. The normalization: ξ′ vs ζ′ (fixing "up to gamma factors")

The design note treats |ξ′(ρ)|⁻² and |ζ′(ρ)|⁻² as interchangeable "up to gamma factors". They are
not — the gamma factor carries an **exponential**.

ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s). At a simple zero ρ = ½+iγ only the ζ′ term survives:

> ξ′(ρ) = ½ ρ(ρ−1) π^{−ρ/2} Γ(ρ/2) ζ′(ρ).

Magnitudes (γ ≥ 1):

- |ρ(ρ−1)| = |ρ||ρ−1| = γ² + ¼, so ½|ρ(ρ−1)| = ½(γ²+¼).
- |π^{−ρ/2}| = π^{−1/4} (Re ρ = ½).
- |Γ(¼+iγ/2)| = √(2π)·(γ/2)^{−1/4}·e^{−πγ/4}·(1+O(1/γ))  (Stirling).

Product: **|ξ′(ρ)| = (π/2)^{1/4} γ^{7/4} e^{−πγ/4} |ζ′(ρ)| (1+O(1/γ))**.  [PROVEN, elementary]

Hence

> **1/|ξ′(ρ)|² = (2/π)^{1/2} γ^{−7/2} e^{πγ/2} · 1/|ζ′(ρ)|² · (1+O(1/γ)).**  [PROVEN]

**Consequences.**

- G_ξ := Σ_{0<γ≤T} 1/|ξ′(ρ)|² has a single top term ≫ e^{πT/2} T^{−O(1)} (using only the trivial
  polynomial bound |ζ′(ρ)| ≪ T^{O(1)}), so **G_ξ ≫ e^{πT/2} T^{−O(1)}** — exponentially large.
- For the Cauchy ratio: weights w_ρ = 1/|ξ′(ρ)|² range over dynamic range e^{πT/2}, so
  G_ξ²/H_ξ ≈ (top term)²/(top term)² = O(1). The Cauchy bound N_s ≥ G_ξ²/H_ξ is **O(1)** —
  no information at all. [PROVEN]

**Fix.** The only normalization that recovers a finite moment structure (and the Gonek machinery)
is the **ζ′ normalization**, G_ζ := Σ_{0<γ≤T} 1/|ζ′(ρ)|² — equivalently the "flat"/unit-density
derivative ζ′(ρ)·(γ^{...} Γ-factors removed). All statements below concern G_ζ. The certificate
Q = Σ|ξ′(ρ)|⁻² q_ρ q_ρᵀ as written in the design note must be **rescaled to Σ|ζ′(ρ)|⁻² q_ρ q_ρᵀ**
(or the q_ρ blocks absorbed into a γ^{7/4}e^{−πγ/4} renormalization); otherwise tr Q is not a
trace in the Gonek sense and rank Q is not bounded below usefully. **[assumption → corrected]**

---

## 2. What is proven for G_ζ (primary source, full text)

**Conjecture (Gonek, via [5,7,8]; HKO random-matrix heuristic [10]).** Assume RH + simplicity.
Then Σ_{0<γ≤T} 1/|ζ′(ρ)|² ~ **(3/π³)T**. [CONJECTURED; primary source (1.1)]

**Theorem (Milinovich–Ng 2011).** Assume RH and that all zeros are simple. Then for every fixed
ε>0, for T sufficiently large,

> **Σ_{0<γ≤T} 1/|ζ′(ρ)|² ≥ (3/(2π³) − ε) T.**  [PROVEN, conditional on RH + simplicity; (1.3)]

i.e. **exactly half** the conjectured value. (Gonek [5] had earlier obtained ≥ CT for *some*
C>0, unpublished/weaker constant; Milinovich–Ng push C up to any C < 3/(2π³).)

**Method (traced from the full text).** It does **not** use Guinand–Weil or Landau–Gonek. It uses
the residue theorem + Montgomery–Vaughan/Tsang mean values. Define the Möbius Dirichlet polynomial
M_ξ(s) = Σ_{n≤ξ} μ(n) n^{−s}, ξ = T^ϑ, 0<ϑ<1 fixed. Under RH, M_ξ(ρ) = M_ξ(1−ρ) is **real**
(1−ρ = ρ̄ and μ real). Cauchy then gives (their (2.2)):

> Σ_{0<γ≤T} 1/|ζ′(ρ)|² ≥ M₁²/M₂,
> M₁ = Σ_{0<γ≤T} M_ξ(1−ρ)/ζ′(ρ),   M₂ = Σ_{0<γ≤T} |M_ξ(ρ)|².

**Key integrals** (their §3–4; rectangle [c+i, c+iT, 1−c+iT, 1−c+i], c = 1+1/log T; residue of
1/ζ at a simple zero ρ is 1/ζ′(ρ)):

- M₁ = (1/2πi)(I₁+I₂+I₃+I₄), with **I₁ = ∫_{c+i}^{c+iT} M_ξ(1−s)/ζ(s) ds** the main term.
  By Tsang's mean-value lemma (their (3.1); Montgomery–Vaughan case bₙ=aₙ):
  ∫_0^T (Σ aₙn^{−it})(Σ bₙn^{it}) dt = T Σ aₙbₙ + O((Σ n|aₙ|²)^{1/2}(Σ n|bₙ|²)^{1/2}),
  one gets I₁ = (3/π³)T log ξ + O(√ξ log T + T). With a standard RH choice of T (their (3.2),
  |ζ(σ+iτₙ)|⁻¹ ≪ exp(A log τₙ/log log τₙ)), the horizontal/left legs are error. Net:
  **M₁ = (3ϑ/π³)T log T + O(T)**. [RH + simplicity]
- M₂ = (1/2πi)(J₁+J₂+J₃+J₄), with **J_j = ∫ M_ξ(s)M_ξ(1−s)(ζ′/ζ)(s) ds** over the same legs.
  Using ζ(s)=χ(s)ζ(1−s) and its log-derivative **ζ′/ζ(1−c−it) = −χ′/χ(1−c−it) + ζ′/ζ(c+it)**,
  plus **χ′/χ(1−c−it) = log(t/2π)(1+O(t^{−1}))** (Stirling) — this is the
  ξ′(s)/ξ(s)=ξ′(1−s)/ξ(1−s) structure the task gestured at — they get J₃ = K + J₁ + O(ξ log T)
  with **K = (1/2π)∫_1^T log(t/2π) M_ξ(c+it)M_ξ(1−c−it)dt = (3/π³)T log(T/2π) log ξ + O(T log T)**,
  and **J₁ = −(3/2π³)T (log ξ)² + O(T log T)**. Net:
  **M₂ = (3/π³)(ϑ+ϑ²)T log²T + O(T log T)**. [RH only]
- Combine: G_ζ ≥ M₁²/M₂ = (3/π³)·ϑ/(1+ϑ)·T, and **ϑ→1⁻** gives (3/2π³−ε)T. ∎

The log T in M₂ comes from χ′/χ (functional-equation log-derivative), *not* from a log in the
conjecture. The conjecture's constant 3/π³ and the theorem's 3/(2π³) both multiply **T alone**.

---

## 3. What the certificate needs vs what is proven

The design note's inequality (§1) is **rank Q ≥ G²/H**, i.e. N_s ≥ G²/H (Cauchy–Schwarz on the
weights, with N_s the simple count). With the corrected normalization:

- **G = G_ζ = Σ 1/|ζ′(ρ)|².** Needed: a **lower bound of order T**.
  - Proven: **≥ (3/(2π³)−ε)T** — **conditional on RH + simplicity** (Milinovich–Ng). [PROVEN conditional]
  - Unconditional: **no order-T lower bound is known**; the sum must even be restricted to simple
    zeros (a multiple zero contributes |ζ′(ρ)|⁻² = ∞). [honest state of the art]
- **H = Σ 1/|ζ′(ρ)|⁴.** Needed for the denominator. The paper's (1.4) with k=2 conjectures
  only a *lower bound* **H ≥ C₂ T log T**; the standard Gonek-type asymptotic conjecture
  (k=2 case of the (k−1)² rule) is **H ~ C₂ T log T**. Either way (≥ or ~) the ratio G²/H is
  O(T/log T) — vanishing. [CONJECTURED; no unconditional order is known]

**Precision the certificate actually needs.** Insert the conjectured orders: N_s ≥ G²/H ~
(9/π⁶C₂)·T/log T. Meanwhile N_s ~ N ~ (T/2π)log T. The Cauchy bound is a **vanishing proportion**
— ratio ≈ const/log²T → 0. To clear the 0.6818 wall the certificate needs N_s ≥ c·N for a
*positive constant* c; **the G²/H mechanism cannot deliver that under any hypotheses**, because
Cauchy–Schwarz is saturated exactly when all weights w_ρ are equal, and the actual weights
1/|ζ′(ρ)|² are genuinely spread (indeed conjecturally of typical size ≍ (log T)^{−1} with an
Ω(T^{2/3−ε})-type tail, cf. the paper's discussion before (1.4)). [PROVEN for the inequality;
CONJECTURED orders for the asymptotic evaluation; the *structural* inability is PROVEN — no
Cauchy bound of the form G²/H with G,H as above reaches a positive proportion of N_s ~ T log T.]

---

## 4. Cauchy lower-bound alternative (task point 4) — evaluated

The task's suggested alternative is exactly the Milinovich–Ng structure: Cauchy on a linear
functional. Two distinct things must not be conflated:

1. **Cauchy as a bound on the weight sum G itself** (what Milinovich–Ng do): G ≥ M₁²/M₂. This
   is **effective** and yields the correct order T — but it bounds the *weight sum*, **not the
   simple count** N_s. [PROVEN conditional; strength = half the conjecture]

2. **Cauchy as a bound on the simple count** (what the certificate needs): N_s ≥ G²/H. This is
   the relevant inequality for rank Q, and it is **vanishing** (≈ T/log T vs N_s ~ T log T), even
   at full Gonek + Ng-k=2 strength. [PROVEN structural]

So the "Cauchy alternative" does **not** rescue the certificate: it produces a lower bound on
G (conditional), and any subsequent Cauchy/Sylvester extraction N_s ≥ G²/H loses a log²T and
gives a zero proportion. A positive-proportion simple bound needs a **mollified linear functional
/ higher-moment mechanism**, not the quadratic G²/H Cauchy — which is precisely why the known
positive-proportion results (0.4075 unconditional PRZZ; 0.617 box-conditional BGSTB; 19/27 and
0.679 RH-conditional) all use mollifiers/discrete moments rather than a Cauchy ratio.

---

## 5. Honest status: does the conditional nature kill the xi-tower route?

**Yes — but the conditional input is not even the main killer.** Ordered by severity:

1. **(Fatal, unconditional in form) The extraction mechanism is vanishing.** rank Q ≥ G²/H gives
   at most O(T/log T) simple zeros — a zero proportion — under the *full* Gonek conjecture. It
   cannot reach a positive simple fraction, so it can never certify p₁-type content, let alone
   break 0.6818. [PROVEN structural]

2. **(Fatal for the "unconditional input" goal) The weight G is RH+simplicity-conditional.**
   The only order-T lower bound on G_ζ is Milinovich–Ng, conditional on RH + simplicity. Using it
   makes the certificate conditional on the very hypothesis (RH) it is meant to attack — defeating
   the purpose stated in `xitower-certificate-design-2026-08-14.md` §4. And even then, its known
   *conditional* competitors (Bui–Heath-Brown 19/27 ≈ 0.7037; CGdL ≈ 0.679) already clear 0.6818
   without needing G. So the tower contributes nothing that isn't already dominated by known
   conditional results. [honest]

3. **(Also fatal) The ξ′ normalization is wrong.** As literally written, tr Q = G_ξ is
   exponentially large and concentrated; even the Cauchy ratio collapses to O(1). §1. [PROVEN]

**What would rescue the route (stated for the record):**
- Replace the quadratic Cauchy extraction G²/H by a **mollified linear-functional / discrete
  moment** bound on the simple count — i.e., abandon "rank Q ≥ G²/H" as the engine and instead
  use G (or 1/ζ′(ρ)-weighted linear forms) inside a Bui–Heath-Brown/CGG-type argument. That is
  exactly the known simple-zero machinery, and its *unconditional* state of the art is 0.4075
  (far below 0.6818), per `structural-thread-newinput-2026-08-14.md`.
- Or prove an **unconditional** order-T lower bound on G_ζ (over simple zeros). None is known;
  the Milinovich–Ng argument needs RH at two places (M_ξ(ρ)=M_ξ(1−ρ) reality; the ζ⁻¹ bound on
  the horizontal line) and simplicity for the residue 1/ζ′(ρ) to be well-defined. Removing both
  is the open problem. [INCONCLUSIVE whether possible]
- **Verdict: the xi-tower G-route, as specified (rank Q ≥ G²/H with ξ′-weights), is ABANDONED**
  as an input to the 0.6818 wall — on *three* independent grounds (normalization, vanishing
  Cauchy strength, conditional weight). The multiplicity-bit observation (ξ′(ρ)=0 ⇔ multiple) in
  the parent note remains valid PROVEN structure; what is dead is the *specific* trace
  G = Σ|ξ′(ρ)|⁻² as a usable magnitude.

---

## 6. Labels

| Claim | Status |
|---|---|
| |ξ′(ρ)| = (π/2)^{1/4} γ^{7/4} e^{−πγ/4} |ζ′(ρ)| (1+O(1/γ)) | PROVEN (Stirling) |
| G_ξ ≫ e^{πT/2}T^{−O(1)}; G_ξ²/H_ξ = O(1) | PROVEN (trivial polynomial bound on ζ′) |
| Gonek conjecture: Σ 1/|ζ′(ρ)|² ~ (3/π³)T | CONJECTURED (Milinovich–Ng (1.1); HKO [10]) |
| Σ 1/|ζ′(ρ)|² ≥ (3/(2π³)−ε)T | PROVEN conditional on RH+simplicity (Milinovich–Ng (1.3)) |
| Milinovich–Ng key integrals (M₁, M₂ as in §2) | PROVEN (paper §3–4, full text read) |
| N_s ≥ G²/H (Cauchy) | PROVEN (Cauchy–Schwarz) |
| N_s ≥ G²/H ~ (9/π⁶C₂)T/log T (vanishing proportion) | CONJECTURED orders (Gonek k=1 + Ng k=2) for the asymptotics; the vanishing nature is structural PROVEN |
| Certificate weight must be ζ′, not ξ′ | PROVEN (§1) |
| Notes' "(6/π³)T log T" is wrong; correct is (3/π³)T | PROVEN (primary source, this session) |

**Correction flags for two existing notes:** `xitower-certificate-design-2026-08-14.md` §4 and
`structural-thread-newinput-2026-08-14.md` §3 both record the Gonek conjecture as
"(6/π³)T log T"; the correct statement is **(3/π³)T** (Milinovich–Ng (1.1)), with the conditional
half-bound **(3/(2π³)−ε)T** (their (1.3)). Recommend a follow-up edit of those two rows.

---

## 7. Next step

**Not** to certify G (it is conditional and, worse, unusable via Cauchy). The actionable next step
is to re-check the parent design's other lever: can the multiplicity-bit ξ′(ρ)=0 be injected into a
**mollified linear-functional** simple-zero argument (Bui–Heath-Brown/CGG shape) rather than the
quadratic G²/H Cauchy — i.e. does the tower add any *new* input to the 19/27 mechanism, or is it
strictly subsumed by it? If subsumed, the xi-tower is closed as a lever (ABANDONED, with this note
as the reason).

*Provenance: the only "computation" this session was fetching arXiv:1106.1160 (API + PDF, cached in
scratchpad). All numbers above are closed-form (Stirling, Cauchy, elementary constants).*
