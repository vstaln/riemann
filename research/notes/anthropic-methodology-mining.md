# Mining Anthropic's RH package — transferable techniques for the 7-point/coboundary machinery

**Date:** 2026-08-13 (overnight EXPLORER round).
**Method:** s4h-historical-lesson-extraction applied non-interactively to the local corpus
(`research/papers/anthropic-informal-note.txt`, `claude-riemann-paper.txt`, `claude-appendix.txt`,
`claude-transcripts.txt`, `research/lean-zeta-23/README.md` + `Zeta23/`). Case → surface events →
underlying principle → transfer, per `hooks/agents.md`.
**Honesty labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE per
`hooks/agents.md`. No fabrication: every claim is cited to a specific line/§ of the local files or to a
numbered note in our own program. Where a transfer is my assessment rather than a fact of the corpus, it
is labelled CONJECTURED and the reasoning is shown.

---

## 0. What we already know about our own machinery (context for every transfer below)

Our program = the 7-point (uniform) stability refinement of the rank–trace inequality, exactly the
mechanism the external groups ainta/trmdy/tawanerguo used to move Theorem D's 0.67250 → 0.6730–0.6732
(`discovery-gram-stability-673.md`). Corrected certified bound **0.6730690** at (α=1.49, psum=1/220,
eps=0.007759, m=137), **CERTIFIED** twice with the fixed verifier (`retraction-673-invalid.md`,
`synthesis-combine-2026-08-13.md` §1). Proven walls (all in `research/notes/`):

| wall | value | label | where |
|---|---|---|---|
| window ceiling (Montgomery functional Q) | 0.6725007 | PROVEN (Lean `Functional.lean`, `attack-kernel.md`; numerically re-confirmed) | every window family ≤ this |
| class ceiling (bandwidth-one certificate) | 0.6818287 (+ 2.55·10⁻⁶·(|r′(1)|+∫\|r″\|)) | PROVEN (Lean `PairCeiling.ceiling_law256`, modulo one numerically-checked enclosure EnclOK) | `attack-ceiling.md`, `close-inclass-gap.md` |
| n-point per-point floor F_n/n | falls with n | PROVEN (interval) | `exec-npoint.md` |
| third moment (unconditional) | does not break 5/6 | PROVEN | `attack-thirdmoment.md` |

The in-class optimum 0.68183123 is **attained** (LP, `attack-lpdual.md`, `close-inclass-gap.md`): the
0.6725 → 0.6818 gap is a certificate-optimality gap, not a data gap, and the only datum that moves v is
the certified simple-point fraction p₁ itself (shadow price exactly 1), which requires
beyond-bandwidth-1 pair-correlation information.

---

## 1. The complete method chain of the Anthropic package, with the slack located

**Chain** (reconstructed from `claude-riemann-paper.txt` §1.4, §7.1, §7.5; `claude-appendix.txt` §1,
§6.3; `claude-transcripts.txt` pages 37–48 of the E2-pairs run):

1. **Weil form + Gabor compression.** `W(f,g) = Σ_ρ m_ρ ĥf(γ_ρ) ĥg(γ̄_ρ)` is the Hermitian Weil form
   (`claude-appendix.txt` §1.1 "The form and its two sides"); positivity of W on all of C²_c(ℝ) ≡ RH
   (`paper` §1.4, citing Wei52/Bom00/Yos92). Restrict to V = span of `d ≈ λN` Gabor test functions
   `f_k(u) = φ(u)e^{−iτ_k u}` at critical sampling density; Ĝ = W|_V (`paper` §2). **This is the one
   degree of freedom in the method**: the family V, i.e. the window φ² (§7.1).
2. **Zero side: inertia + rank.** Ĝ = P + Q with P ⪰ 0 rank ≤ s (distinct on-line points, each one
   rank-one nonnegative form) and Q carrying the off-line pairs as signature-(1,1) blocks, so
   n₊(Q) ≤ p (# distinct off-line pairs) by Sylvester's law of inertia (pull-back does not increase the
   positive index) (`paper` §1.4 (Z), Lemma 3.1; `appendix` §1.1). Count bookkeeping
   `N ≥ n_on^dist + 2 n_pair^dist` (Riemann–von Mangoldt counts a pair twice).
3. **Prime side: two traces.** tr Ĝ = N(1+o(1)), ‖Ĝ‖²_F = tr Ĝ² = (1/λ + λ/3)N — Montgomery's first
   and second moments, evaluated unconditionally from primes (BGSTB24 Thm 1 / paper Thm 5.8) (`paper`
   §1.4 (P), §5). This is the **only pair-correlation input**, and it is an L² (mean-square) datum.
4. **Linear algebra: rank–trace inequality.** Lemma 3.2 (`paper` (3.1), informal note Lemma 3.4):
   for Hermitian P ⪰ 0, rank P ≤ r, Q with ≤ b positive eigenvalues,
   `‖P+Q‖²_F ≥ c·trP − c²/4·r + 2c·trQ − c²·b`; at c=2:
   `r ≥ 2 trP + 4 trQ − 4b − ‖P+Q‖²_F`.
   Proof via von Neumann's trace inequality + `x² ≥ 2x − 1 = (x−1)² ≥ 0` (the matrix analogue of the
   integrality step `m² ≥ 2m−1`; c=2 applied to the (m−1)² level). The next level `(λ−u)(λ−2u) ≥ 0`
   ⇔ `λ² ≥ 3uλ − 2u²` would give 5/6 but is **robustly false** for interacting zeros (eigenvalues smear
   off the integer lattice; `appendix` §6.3; `transcripts` Note 2 "near-miss").
5. **Assemble.** `s ≥ 4N − 2N − (1/λ+λ/3)N = H(λ)N`; at λ=1, H = 2/3 (Thm A). Regrouping simple zeros
   onto the rank side and multiple on-line points + pairs onto the index side gives `3s₁ + 4s₂ + 4p ≥
   4tr − ‖·‖²_F` (the m² ≥ 3m−2 analogue) → Thm B (simple, 2/3), Thm C (distinct, 5/6).
6. **Optimization over the window.** Thm D: with v*(s) = cos(√2s) the Rayleigh quotient
   `c_λ(v) = λ(∫v)²/(∫v² + λ²∬|s−s′|v(s)v(s′)dsds′)` is maximized; `2 − 1/c*₁ = 3/2 − (1/√2)cot(1/√2) =
   0.672500703679…`. **Proven the limit of the method**: [CCLM17, Cor. 14] (one-delta extremal problem) —
   "no window does better" (`paper` §7.1, end; `attack-kernel.md` re-derived the variational problem
   independently: the minimizer of Q(v) is the cosine, global over L²[−1/2,1/2], PROVEN).

**Where the slack is.** The inequality (3.1) itself is **tight** given its inputs (equality case:
P = c/2·Π₁, Q = c·Π₂ with orthogonal projections; `paper` after (3.1); `appendix` §6.3 "the linear-algebra
minima matching it with equality"). The chain's lossiness therefore lives in three places, and only one
of them is genuinely ours to attack:

- **(a) the two-moment data are the only input** — the certificate reads tr and tr² only; every
  eigenvalue distribution with those two moments and the (rank, n₊) bookkeeping is admissible. This is
  what our 7-point stability term `tr Ψ(M)` attacks: it adds a **function of the Gram matrix** (not of
  the spectrum alone) to the inequality — `‖P+Q‖²_F ≥ 4tr − 3r − 4b + tr Ψ(M)`, Ψ(t) = (t−1)² on [0,2],
  2t−3 beyond (`discovery-gram-stability-673.md`). **The Gram structure is extra information the
  paper's two-moment certificate does not use.** (PROVEN as an exact algebraic identity in the external
  repos; `discovery-gram-stability-673.md` Q2 — whether the 256-law's Gram satisfies the stronger bound,
  i.e. whether tr Ψ(M) pushes the class ceiling — was left OPEN in our ledger.)
- **(b) the window** — capped (0.6725007, PROVEN), not a lever.
- **(c) the certificate shape** — in-class optimum 0.68183123 attained by an explicit r (LP, PROVEN up
  to τ-terms); the gap 0.6725 → 0.6818 is closed in-class, not for real zeros; moving the real constant
  needs beyond-bandwidth-1 data (CONJECTURED/unavailable). (`close-inclass-gap.md` §0, `attack-lpdual.md`.)

**Verdict on slack:** the paper's own slack is (a) — it uses exactly two moments of the compressed
form and nothing about the Gram structure; that is the mechanism our program already exploits, and it is
the same mechanism the paper itself identifies as the entire gap ("the entire problem of reaching 2/3 is
to prove the spectral integrality inequality unconditionally… something of the shape `n_θ₊(R) ≥
2trR/u − trR²/u²`", `appendix` §1 / `transcripts` Note 2). CONJECTURED transfer: our `tr Ψ(M)` term is
the closest existing implementation of exactly that spectral-integrality recovery, at the
(m−1)²≥0 level.

---

## 2. Transferable techniques, ranked by applicability to our machinery

| # | technique | where in corpus | tried in our program? | assessment |
|---|---|---|---|---|
| T1 | **7-point / block stability refinement** (`‖P+Q‖²_F ≥ 4tr − 3r − 4b + tr Ψ(M)`, Ψ=(t−1)²) | external repos, mechanism documented in `discovery-gram-stability-673.md` | **YES — this is our bound 0.6730690** | PROVEN. The single largest lever moved 0.67250 → 0.67307 in our machinery. |
| T2 | **Coboundary (Bellman) redistribution** — tawanerguo's block-size m=183 weighted 7-pt block inequality | external repo tawanerguo (our ledger) | **YES — partially** (coboundary machinery present; bound 0.6730690) | PROVEN in our machinery; the joint (T1+T2) optimum α=1.49, psum=1/220, m=137 is where we stand. |
| T3 | **(1,1) block structure of off-line pairs + Sylvester inertia** | paper §1.4(Z), appendix §1, §6.3 | **YES — core of the method** (we inherit it via the rank–trace machinery) | PROVEN as the bookkeeping `n₊(Q) ≤ p`, `N ≥ n_on + 2n_pair`. Nothing new to transfer; but see T8. |
| T4 | **von Neumann trace inequality coupling P with the negative part of Q** (the proof engine of (3.1)) | paper Lemma 3.2, appendix §6.3 "negative spectrum and rank jointly" | **YES — implicitly** (our inequality is (3.1)+stability; the proof is the same coupling) | PROVEN. The paper's own discovery was that negative spectrum ALONE is useless against tight pairs, but negative spectrum + rank jointly work — that coupling is (3.1). No new lever. |
| T5 | **Integrality steps m² ≥ 2m−1, m² ≥ 3m−2 as matrix inequalities** | paper §3 after (3.1), §7.5(c); appendix §1, §6.3; transcripts Note 2 | **YES for level (m−1)²** (= our tr Ψ(M) positivity); **the (m−1)(m−2) level is ABANDONED** (robustly false: eigenvalues of interacting simple zeros fill (0,2); `appendix` §6.3) | PROVEN. The (m−1)(m−2) level is NOT transferable — the paper and we independently killed it. Do not resurrect. |
| T6 | **Distinct-zeros 5/6 machinery** (Thm C: N_d ≥ 5/6; the same method's distinct count) | paper Thm C, §7.5(b) sharpness config; `transfer-stability-online.md` | **INCONCLUSIVE in our ledger** — the c=3 distinct-zeros route was nominated but not executed; `attack-thirdmoment.md` shows the third-moment route can't beat 5/6, but the *two-moment* 5/6 distinct bound itself is a live target | **CONJECTURED highest-value un-tried transfer.** Our stability term is provably positive on the same kernel for distinct atoms (`transfer-stability-online.md`: ε_A ≥ ε_D numerically, 4000 configs, 0 violations). A distinct-zeros refinement `5/6 + δ` (δ ≈ +1.9e-5 at 3-pt, +3.3e-4 at 7-pt, HYPOTHETICAL linear-response extrapolation) is not blocked by any wall we have proven. |
| T7 | **ξ′ derivative transport** (rank–trace device on ξ′: 0.85838 simple on-line; quartic window 0.86864) | paper Remark 7.3; Lean README §"The zeros of ξ′" (`Zeta23/XiPrime/`) | **NO** — not tried in our program | PROVEN result (Lean, 6 statements, sorry-free). Transferable *in principle*: the same machinery applies to ξ′ with a different two-trace pair. But: (i) the Farmer–Gonek–Lee comparanda show the ξ′-constants are near their conditional ceiling already (85.84% unconditional vs 88.25% conditional); (ii) **it does not move the ζ-bound** — it is a different function. CONJECTURED: only useful as a stress-test of our machinery (does our stability term transfer to the ξ′ Gram?), not as a ζ-bound mover. |
| T8 | **Two-trace structure: tr and tr² as the only certified inputs, sharpness configuration** (2/3N orthogonal simples + 1/6N doubles realizes tr=N, ‖·‖²_F=4N/3, N_d=5/6N) | paper §7.5(b); appendix §6.3 | **partially** — the sharpness config is documented in our ledger (`transfer-stability-online.md` §3) but never used as an *adversarial* probe of our 7-pt floor | CONJECTURED: the sharpness config is the natural probe for our coboundary floor — do our 7-point constraints break the config? (If the floor F ≥ 0.007759 survives the sharpness config, that's evidence the stability term is not the binding slack.) |
| T9 | **Power-complementary (Princen–Bradley) orthogonal Gabor variant** | paper Remark 7.1(i) | **NO** | PROVEN in the paper to give the same limits (λ₀ = λL₀/L). Not a lever: it only renormalizes. ABANDONED. |
| T10 | **Orthonormalization route** | paper Remark 7.1(ii) | **NO** | The paper explicitly does NOT use it: uncontrolled Rayleigh quotients on small-eigenvalue directions (Lindelöf-strength needed). Same obstruction would hit us. ABANDONED. |
| T11 | **Higher moments (tr R³, tr R⁴)** | paper §7.5(d)–(f); appendix §6.3; `attack-thirdmoment.md` | **ABANDONED in our ledger** (attack-thirdmoment.md: unconditional third moment does not break 5/6, PROVEN) | PROVEN dead both in the corpus and in our program. The corpus adds a sharper reason: odd moments cannot lower an eigenvalue-count lower bound without a Lindelöf-strength λmax bound; even k=4 needs λ<1/2 where dim kills it. Do not revisit. |
| T12 | **The window is not a lever** (H = 0.6725007, Montgomery–Taylor, CCLM17 optimality) | paper §7.1; `attack-kernel.md` (PROVEN); `synthesis-combine` Conflict 1 (units error) | **ABANDONED** | PROVEN dead. Our α=1.49 is inside the same class (it trades H for a better ε-floor; H(1.49) = 0.6724219). |
| T13 | **LP-dual / adversarial certificate probing** | our `attack-lpdual.md`, `close-inclass-gap.md` | **YES** (in-class optimum attained, ceiling tight) | PROVEN. The remaining open Q2 (does tr Ψ(M) push the class ceiling?) is the natural continuation — see §4. |

---

## 3. The single most promising technique — combined with coboundary redistribution

**The technique: the stability term `tr Ψ(M)` pushed to the DISTINCT-zeros (Theorem C) count, i.e. a
"5/6 + δ" refinement — combined with our existing coboundary (Bellman) redistribution.**

**Why this one.** Three independent reasons, each grounded:

1. **It is not blocked by any proven wall.** The walls we have are: window (0.6725, PROVEN), class
   ceiling for *simple* zeros in the bandwidth-one certificate class (0.6818, PROVEN in Lean), n-point
   floor (F_n/n falls, PROVEN), third moment (PROVEN dead). The distinct-zeros count is **not** among
   them: the class ceiling `ceiling_law256` bounds the certified proportion of **simple** zeros
   (`attack-ceiling.md`; `close-inclass-gap.md` §0: "the law's p₀ = 0.68183 is the certified simple-point
   fraction"). The 5/6 distinct statement is a **different functional** (`N_d ≥ s₁ + s₂ + 2p ≥ s₁ + s₂ +
   p`, paper §1.4 after (L)), and our stability term's positivity for distinct atoms was numerically
   confirmed (ε_C = ε_D = 4.45e-4, `transfer-stability-online.md` §1: "multiplicity scaling can only
   increase tr Ψ" — but note: the distinct-atom Gram is NOT multiplicity-scaled, so the transfer rests on
   the *same-kernel-ε* argument, which is numerical, not proven). **CONJECTURED — the transfer is
   method-level CHECKED NUMERICALLY, constant-level chain-dependent.**
2. **The corpus itself identifies the distinct count as the honest target.** `appendix` §1: "the
   honest target is: distinct zeros on the line ≥ cN with c matching what RH plus Montgomery's
   pair-correlation argument gives for simple zeros, namely c = 2/3"; and the sharpness config
   (2/3N simples + 1/6N doubles → N_d = 5/6N, `paper` §7.5(b)) is the *same* extremal that realizes
   tr=N, ‖·‖²_F=4N/3. Our 7-pt stability term was designed to break exactly this config's orthogonality
   assumption (the atom inner products are k(γ−γ′) ≠ 0, `discovery-gram-stability-673.md` "THE KEY
   INSIGHT").
3. **It combines naturally with coboundary redistribution.** The coboundary machinery (tawanerguo, our
   T2) reshuffles the *per-gap* 7-point constraint into a block-averaged bound; the stability term is a
   *different* channel of the same Gram data (Ψ of eigenvalues of M, i.e. of the 7-point sub-Grams).
   Nothing in either construction consumes the other's input. **CONJECTURED**: a distinct-zeros
   refinement at the 3-point level (ε_C = 4.45e-4) would give `5/6 + δ` with δ ≈ +1.9e-5, and at the
   7-point level δ ≈ +3.3e-4 — the latter would take the distinct-zeros constant from 0.8333 to
   ≈ 0.83366, i.e. beyond every distinct-zeros bound we have on record (unconditional records: 0.6603
   [Wu15] per paper §1.4; the paper's own 5/6). **HYPOTHETICAL** — linear-response extrapolation from
   D's chain algebra, explicitly labeled in `transfer-stability-online.md` §1.

**Honest CONJECTURED assessment of combining it with coboundary redistribution:**

- **What is solid (PROVEN / CHECKED NUMERICALLY):** the stability identity is an exact algebraic
  identity for any atom scheme (`transfer-stability-online.md` §1); the positivity ε_C = ε_D = 4.45e-4
  is numerically verified; the distinct-zeros constant 5/6 is not covered by the bandwidth-one simple-
  zeros ceiling; the coboundary machinery is orthogonal (it acts on the 7-point floor, not on the
  count functional).
- **What is genuinely uncertain (CONJECTURED / INCONCLUSIVE):** (i) C's chain algebra is not in our
  possession — the constant-level response of the distinct count to the stability term is
  extrapolated, not derived; (ii) whether the *same-kernel-ε* argument survives at λ = 1 with the
  paper's actual window (our numerics used the α=1.49 kernel of our certificate, which is *not* the
  paper's cos(√2·s) window — the kernels differ, so the ε-transfer is kernel-dependent); (iii) whether
  the coboundary block-averaging interacts with the distinct-atom Gram in a way that *reduces* the
  achievable ε (the 7-point floor was certified for simple-atom configurations; distinct configurations
  include multiple on-line points whose atoms are multiplicity-scaled — the floor's adversary family
  may differ).
- **Cost of trying:** low. The tools exist (`tools/verify_coboundary_floor.py`, `tools/online_kernel_check.py`);
  the only new code is a distinct-count variant of the certificate. This is a one-evening experiment,
  and its failure mode is informative (it would pin the distinct-transfer to the chain algebra, i.e.
  close Q1 of `discovery-gram-stability-673.md` for good).

---

## 4. What our program has NOT yet tried (and the honest status of each)

| item | status in our ledger | verdict |
|---|---|---|
| (1,1) block structure / Sylvester inertia | inherited as bookkeeping (T3) | nothing new to transfer; the paper and we use the same `n₊(Q) ≤ p` |
| Sylvester inertia as a *standalone* lever | `attack-argprinciple.md`, `attack-jensen-ometer.md` (our own) | ABANDONED; appendix §6.3 proves negative-spectrum-alone is useless against tight pairs |
| von Neumann trace inequality step | implicit in our (3.1) machinery | PROVEN tight given its inputs; slack is elsewhere (the Gram structure, §1(a)) |
| integrality m²≥2m−1, m²≥3m−2 | level (m−1)² = our tr Ψ(M) (T5); level (m−1)(m−2) ABANDONED (robustly false, both in corpus and independently in our attack-multiplicity work) | do not resurrect (m−1)(m−2) |
| distinct-zeros 5/6 machinery (T6) | **NOT executed** — nominated in `transfer-stability-online.md` Q1, left INCONCLUSIVE | **the live transfer, §3** |
| ξ′ derivative transport (T7) | NOT tried | PROVEN result in corpus; transferable only as a machinery stress-test, not a ζ-bound mover |
| two-trace structure + sharpness config (T8) | documented, never used as adversarial probe | cheap, informative; probe our 7-pt floor with the 2/3N+1/6N config |
| orthogonal Gabor / Princen–Bradley (T9), orthonormalization (T10) | NOT tried | ABANDONED — the paper proves they give the same limits / are blocked by Lindelöf-type obstructions |
| higher moments (T11) | ABANDONED (attack-thirdmoment.md, PROVEN) | confirmed dead by the corpus with a sharper reason |
| beyond-bandwidth-1 data (α>1, HL/RMT) | CONJECTURED/unavailable | the only datum that moves the simple-zeros constant (shadow price 1, `attack-lpdual.md`); no unconditional route exists |

**Open questions carried forward (each is a one-liner in our ledger):**
- Q2 of `discovery-gram-stability-673.md`: does `tr Ψ(M)` push the *class ceiling* (0.6818) itself? The
  ceiling was proven for the certificate class reading only (rank, tr, HS², n₊); the stability term adds
  a Gram constraint the 256-law may or may not satisfy. This is the single most direct test of whether
  T1's mechanism interacts with the ceiling, and it is **not** covered by `attack-lpdual.md` (which
  optimized inside the old certificate class).
- The LP-dual adversarial test of the ceiling with the stability constraint added (nominated in
  `synthesis-combine-2026-08-13.md` §3, never executed).

---

## 5. The "2/3 by a simpler argument" — does it generalize?

**What it is.** Theorem A's 2/3 needs no Montgomery–Taylor optimization: with the flat-top window,
`H(λ) = 2 − 1/λ − λ/3`, and at λ=1 that is exactly 2/3 (`paper` §1.4, Theorem A at λ=1; `close-inclass-
gap.md` §1: "The flat-top version (Theorem B) gives H(λ) = 2 − 1/λ − λ/3, i.e. 2/3 at λ = 1"). The
"simpler argument" is the same chain with the un-optimized window; the 0.6725 comes only from the
Montgomery–Taylor optimization (Thm D). So the statement "2/3 by a simpler argument" = "the flat-top
window already reaches 2/3; the cos(√2·s) window buys the extra 0.0025".

**Does it generalize?** Two readings:

1. *Method-level:* yes — the flat-top H(λ) formula is a special case of the same two-trace chain, and
   our external groups' bounds (0.6730–0.6732) already exceed 2/3 by exactly the mechanism (stability
   term + coboundary) that the paper does not have. **PROVEN** (our bound 0.6730690 > 2/3, CERTIFIED).
2. *Constant-level:* the "simpler" 2/3 is NOT improvable by the flat-top window alone (H(λ) capped at
   2/3 at λ=1); the extra 0.0025 requires the optimized window, and the further 0.0006 (0.6725 →
   0.67307) requires the stability term. Each level needs its own ingredient; there is no free lunch
   from "simpler". **PROVEN** (window ceiling, stability bound).

So: the generalization that matters is not "simpler window", it is "**the paper's chain has exactly two
certified moments and nothing about Gram structure — every external improvement (ours included) comes
from adding Gram-structure constraints, and the distinct-zeros functional is the next place the same
ingredient is unspent**". That is the thesis of §3.

---

## 6. Honesty labels (consolidated)

| claim | label |
|---|---|
| Chain map (§1): Weil form → Gabor compression → inertia/rank → two traces → rank–trace → assembly → window optimization | PROVEN (from the cited paper/appendix/transcript sections, all read in full) |
| (3.1) tight given its inputs; equality case = orthogonal projections | PROVEN (paper §3; appendix §6.3) |
| Slack lives in (a) Gram structure (only two moments used), (b) window (capped), (c) certificate shape (in-class optimum attained) | PROVEN for (b),(c) (Lean/LP); CONJECTURED for (a) being *the* recoverable slack — supported by the corpus's own "the entire problem of reaching 2/3 is to prove the spectral integrality inequality" (appendix §1) |
| tr Ψ(M) stability term = matrix (m−1)² level; (m−1)(m−2) level robustly false | PROVEN (exact identity in external repos; false-level documented in appendix §6.3 AND independently in our attack-multiplicity work) |
| Distinct-zeros transfer: ε_C = ε_D = 4.45e-4; multiplicity scaling increases tr Ψ | CHECKED NUMERICALLY (tools/online_kernel_check.py, 4000 configs, 0 violations) — method level only |
| Distinct-zeros constant-level transfer (5/6 → 5/6 + δ, δ≈1.9e-5 / 3.3e-4) | HYPOTHETICAL (linear-response extrapolation, chain algebra not in our possession) — explicitly NOT claimed as a bound |
| 5/6 distinct is not covered by the 0.6818 simple-zeros ceiling | PROVEN (ceiling's certified quantity is the simple-point fraction; close-inclass-gap.md §0) |
| Higher moments add nothing unconditionally | PROVEN (our attack-thirdmoment.md AND corpus §7.5(e), appendix §6.3) |
| ξ′ constants (0.85838/0.86864 simple, 0.92919/0.93432 distinct) | PROVEN (paper Remark 7.3; Lean XiPrime theorems sorry-free per README) — but NOT a ζ-bound mover |
| Flat-top H(λ) = 2 − 1/λ − λ/3; "2/3 by simpler argument" = flat-top window | PROVEN (paper Thm A/B; close-inclass-gap.md §1) |
| Our 0.6730690 > 2/3 by the stability+coboundary mechanism the paper lacks | PROVEN (retraction-673-invalid.md; synthesis-combine §1) |
| Q2 (does tr Ψ(M) push the class ceiling?) still OPEN; LP-dual with stability constraint not executed | INCONCLUSIVE — carried forward |

---

## 7. Bottom line (for the round report)

**Top transferable technique: run our stability term `tr Ψ(M)` against the DISTINCT-zeros (Theorem C)
functional — a "5/6 + δ" refinement — keeping the coboundary redistribution as the block-averaging
layer.** It is the only technique in the Anthropic package that (i) we have not yet executed, (ii) is
not blocked by any wall we have PROVEN (window 0.6725, class ceiling 0.6818 for *simple* zeros, n-point
floor, third moment), and (iii) has positive numerical evidence at the method level (ε_C = ε_D =
4.45e-4, `transfer-stability-online.md`). The constant-level payoff is HYPOTHETICAL (δ ≈ +1.9e-5 to
+3.3e-4), the wall-free status is PROVEN, and the experiment is cheap (existing verifiers, one new
distinct-count certificate variant). Secondary recommendation: use the paper's sharpness config
(2/3N simples + 1/6N doubles) as an adversarial probe of our 7-pt coboundary floor — it is the same
config the stability term was designed to break, and nobody has run it against our floor.
