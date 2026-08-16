# Wave 9, Lever 9B — Classification: Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh, "Short mollifiers of the Riemann zeta-function" (arXiv:2508.11108v1)

**Agent:** LEVER 9B (read-only architect). **Date:** 2026-08-18.
**Labels:** PROVEN (repo) / PROVEN (literature) / CHECKED NUMERICALLY (in-paper, not re-run here) / CONJECTURED / INCONCLUSIVE.

---

## VERDICT (up front)

**DUPLICATE-TRAP — no new lever. The variational Q family is NOT a sufficient-condition family for LP/RH; the Bettin–Gonek "θ=∞ ⟹ RH" statement is a named instance of the campaign's existing moment/coefficient-margin trap class; the Siegel-f smooth-approximation claim is the same argument-principle content as the CLOSED xi'-transport strand.**

- RH-side content: **DUPLICATE-TRAP** (proposes registering "levinson-theta-infinity" as a named member of the existing moment/explicit-formula trap class, for ledger indexing — NOT a new trap class).
- Zero-detector claim (Siegel f): **DUPLICATE** of the closed argument-principle strand.
- No barrier-zoo probe funded (nothing live to test); minimal prescription recorded for completeness.

---

## What the paper actually is (verified in text — PROVEN, read)

- **Theorem 1** (p. 5): there exists θ₀ > 0 such that for θ ∈ (0, θ₀) there is Q = Q_θ ∈ C¹[0,1] with Q(0)=1, Q(y)+Q(1−y)=1 such that the Levinson proportion κ := 1 − (1/R)·log c(P,Q,R) satisfies κ > 2θ/3 > 0. This is a **proportion-of-zeros theorem** for the critical line, extended to modular L-functions (Bernard 2.97% → 6.32%, §1.2).
- **The content is a moment computation.** The whole machine is the mollified second moment (12)–(15):
  c(P,Q,R) = 1 + (1/θ)∫∫(w(y)P′(x) + θw′(y)P(x))² dx dy, w(y)=e^{Ry}Q(y); κ from (14). The variational problem (Problem 1, eqs 21–28) minimizes the functional K*_R(S), a **quadratic form in S and S′ with weight e^t** (30). The Euler–Lagrange equation (31)–(36) is solved explicitly in ₂F₁ hypergeometric functions (§3.1–3.2); Theorem 1 closes on **finite numerical inequalities** (0.5898e^R bound, (55)–(57): ∫₀^R e^{−t}S_R(t)dt ≥ 0.248, S′_R(0) ≥ −0.39006, C₁(R) ~ 0.674…). [CHECKED NUMERICALLY in-paper via Mathematica; NOT independently re-run by this agent — read-only dispatch, no numerics funded.]
- **The FE enters only as the symmetry constraint** (18)/(24): Q(y)+Q(1−y)=1 from the functional equation (Conrey 1989, condition (3)). Everything else is generic variational machinery.
- **Bettin–Gonek citation** (verified, Introduction p. 2): "Farmer [Far93] proposed the 'θ=∞' conjecture… He showed that this would imply 100% of the zeros of ζ(s) lie on σ=1/2. More recently, Bettin and Gonek [BG17] proved that 'θ=∞' in fact implies the Riemann Hypothesis." [PROVEN-literature; BG17 theorem not internally re-derived — cited only, as the paper cites it.]
- **Siegel section + Proposition 1** (pp. 3–4, §4): Q∞(y) = step function (11); f(s) = ∫_L e^{iπw²}/(e^{iπw}−e^{−iπw}) w^{−s} dw (6); h(s)ζ(s) = 2Re h(s)f(s) on Re s=1/2 (7); Siegel: N₀(T) > 2·#{zeros of f in σ<1/2} (8). Paper's Proposition 1: Q_θ → Q∞ pointwise as θ→0+ (proved via the shared e^{(√5−1)t/2} asymptotics of all components, §4). [PROVEN-literature + paper's own proof.]

---

## (a) NEW-FAMILY CHECK — does the variational Q family escape the closed levers?

**NO. Classify: classical reformulation / counting method; NOT a sufficient-condition family; no escape from the closed levers. Label: PROVEN (structure read; argument in this note).**

Structural chain (each step in the text):

1. **It is a counting (proportion) theorem, never a zero-location theorem.** The output is κ > 2θ/3 > 0: a positive *proportion* of zeros on the line for each fixed θ. At no fixed θ does the method make any assertion about zeros off the line, about 100%, or about LP. The campaign firewall applies verbatim: **a proportion-on-the-line theorem is ZERO evidence about RH in either direction.** The paper even strengthens this: Selberg's method already gives positive proportion for ANY θ (paper's own Intro, p. 1) — so the paper's headline (positive proportion for any θ via Levinson) is *not even new information about ζ's line-zeros at the qualitative level*; it's a numerical-constant improvement inside a closed counting paradigm.
2. **The sufficient-condition role is empty.** The family places no sufficient condition on the Taylor coefficients or zeros of Ξ. It computes κ from c(P,Q,R) — an S1-margin / moment-functional type object (a quadratic form on a weight e^{Ry}Q(y)). The lever classes it could conceivably touch — S1-margin (constant-margin coefficient criteria, PROVEN dead at Newton boundary), log-profile (deficit-2: consistency-only, PROVEN dead in both DH and Epstein worlds, barrier-zoo retro-test), moment-transfer (PROVEN exhausted) — are all **moment/coefficient-content levers, and this family adds no new constraint on that content**: the FE enters only as evenness-type symmetry (18) ⇔ the classical condition (3), which the cross-domain hunt already re-derived as "any even real-entire function satisfies the FE on the line" (crossdomain-hunt §5: FE-on-the-line = evenness; FE-based content is consistency-only).
3. **Deflation test (campaign method, 4 classes):** the paper's claim lands in (i) "known theorem restated" — Levinson's method with a better Q (Conrey 1989 already established the framework (3)–(5); the novelty is the explicit variational optimizer, a finite numerical check class object) — and is at best a *finite numerical check* (the κ bound closes on finitely many computed constants). It is NOT RH-equivalent content at any fixed θ, and it does NOT state a condition that would force LP. Both frames land it in the do-not-repeat ledger classes.
4. **The only RH-adjacent claim is the θ→∞ limit, which is the trap (see (b)), not an escape.**

**Verdict (a): NOT a new family. No new lever. Nothing here escapes S1/log-profile/barrier-zoo closures.**

---

## (b) REFORMULATION CHECK — the Bettin–Gonek "θ=∞ ⟹ RH" statement

**Classify: DUPLICATE of the campaign's existing moment/explicit-formula/coefficient-margin trap class. Register the name "levinson-theta-infinity" as an indexed member of that class for ledger disambiguation (NOT a new trap class). Label: PROVEN (literature) that the implication holds; classification = PROVEN (structure read).**

- **What "θ=∞" is:** in Farmer's formulation it is the statement that the *admissible range* of the mollifier length θ extends to infinity — i.e., the mollified-second-moment asymptotic (12) with c(P,Q,R) as in (15) holds for **arbitrarily long mollifiers** y = T^θ. Farmer: θ=∞ ⟹ 100% on the line; Bettin–Gonek: θ=∞ ⟹ RH. [PROVEN-literature, as cited in the paper.]
- **The key structural question — algebraically explicit condition on ζ, or hidden moment/FE content? — answer: HIDDEN MOMENT CONTENT.** The hypothesis "(12) for all θ>0" is a **conjectural moment asymptotic** whose hard part is the off-diagonal/arithmetic structure of a genuinely long mollified second moment — the very content the campaign's moment levers (S1, moment-transfer, GJT) PROVEN exhausted. Nothing in the θ→∞ limit is expressible directly as a coefficient condition on Ξ; the condition lives in an asymptotic formula that (i) is not known to hold, and (ii) whose failure is exactly what a zero off the line produces via the zero-detection inequality (14) (κ = 1 − (1/R)log c; a zero at β>1/2 forces the corresponding R-scale moment to be too large — the classical Lehman/Levinson mechanism). Hence **the hypothesis is at-least-as-hard-as-RH and RH-equivalent in content: proving "θ=∞" IS the barrier, and Bettin–Gonek only shows the implication direction that carries no usable input.**
- **Trap-taxonomy placement:** it is not GJT-completion (no small-n/complement decomposition), not HB (no operator degeneracy), not Weil positivity in explicit-formula form, but it **is** the potential-theory/explicit-formula-moment class: a moment/mean-value statement that provably subsumes RH (Farmer's 100% ⟸ θ=∞ is the counting version; BG17 the RH version) — i.e., ⟺-class content absorbed in a conjectural input. Closest existing entries: coefficient-margin (a margin on a moment functional) and moment-transfer (moment ⟺ RH). **It is a duplicate, under a new name.**
- **One-way input? NO.** A one-way input would be a condition Ξ *provably satisfies* that forces zeros onto the line. "θ=∞" is not proven for ζ (it subsumes RH); it is a conjecture whose content is RH's own. No input is earned.

**Verdict (b): DUPLICATE-TRAP — register "levinson-theta-infinity" = named member of the moment/coefficient-margin trap class; do not treat as a candidate.**

---

## (c) SIEGEL-f CHECK — does the optimized Q ⟶ Q∞ approximation give a new zero-detector?

**NO — DUPLICATE of the closed ξ'/argument-principle strand. Label: PROVEN (structure read).**

- The object on both sides is the **same argument-principle counting**: (i) Siegel (8): N₀(T) > 2·#{zeros of f in σ<1/2}, detected by arg(hf) ≡ π/2 mod π on the line (7); (ii) Levinson: zeros of ζ on the line detected by arg of Q(−1/L·d/ds)ζ (paper §1.3: "Levinson's method detects zeros … by identifying when arg(hζ′)(1/2+it)≡π/2 occurs"). The paper's Proposition 1 is a **formal asymptotic identity** (saddle point, O(T^{−1/4})) showing the variational Q_θ converges pointwise to the Siegel step kernel Q∞ (11) as θ→0+ — i.e., the mollified-derivative combination *tends to* the classical Riemann–Siegel kernel. That is a **nice smooth-approximation fact (in-paper proof, PROVEN-literature context), but not a new zero-detection mechanism:** both representations are "line-argument of an FE-even entire function built from a smoothing kernel," the identical content class the campaign closed in xi'-transport.
- The zeta-specific load in Siegel's method is the **moment** (9) (∫|f(σ+it)|²dt ∼ C_σ T^{1/2−σ}) used to bound the RHS of (8) — again a moment/arithmetic computation; and the zeros of f that feed (8) would have to be located by argument principle — circular. Nothing in the smooth-approximation family separates RH content: any even real-entire function has SOME such kernel; the zeta-specific information is exhausted at the moment level (closed levers). The paper's own Question (6) (zeros of Q_R(−1/L d/ds)ζ drift left as R→∞) is line-zero-distribution folklore, not an RH handle.

**Verdict (c): same argument-principle content as the CLOSED xi'-transport strand. No new zero-detector representation. Do not reopen.**

---

## (d) BARRIER-ZOO PRESCRIPTION (for the record; not run — the task says prescribe only, and (a) leaves no live candidate)

If ANY future proposal claims the Q-family (or its θ→∞ limit, or the Siegel-approximation) is a **sufficient condition for LP/RH**, the minimal barrier-zoo test (`tools/barrier_zoo_rs dhprofile` / `epstein` machinery) is:

1. **Build the world's Levinson-Moment analogue:** recompute (21)–(35) with the DH/Epstein Φ's Taylor coefficients (c_{2k} already tabulated in barrierzoo-retrotest-2026-08-18) replacing Ξ's, keeping the same FE-symmetry constraint (18) (it holds verbatim in both worlds — self-duality). The variational minimizer S_R is unchanged (Euler–Lagrange (31) uses only the symmetry + weight e^t — world-independent); the only input that changes is the constant c(P,Q,R) → c_world(P,Q,R).
2. **Check the analog of κ > 2θ/3 > 0** in the DH/Epstein worlds. **Predicted outcome: it holds — the family is consistency-only.** Reason: the variational machinery is FE-generic (positivity of the moment quadratic form + symmetric weight), exactly the property the retro-test already established for the campaign's own identities (all-positive coefficients, deficit-2 profile, Hankel-TP all hold in both RH-false worlds). A "positive proportion on the line" analog in an RH-false world is not even a contradiction — DH is known to have infinitely many line zeros (PROVEN-literature) and the proportion bound is a counting statement, so the test would pass trivially, confirming the family proves no RH-type statement.
3. **If the claim instead concerns (b)** (θ=∞ ⟹ one-way input): the test is the reverse — verify that the world's analogue of (12) for all θ **fails** in DH/Epstein (it must: β>1/2 zeros destroy large-θ moment asymptotics — the Lehman mechanism); that failure is the proof the "θ=∞" hypothesis carries the RH content, not an input to it. (Do not run; this is the structural argument, PROVEN at the mechanism level from (14).)
4. **Conclusion of the prescription:** the Q-family, the θ=∞ reformulation, and the Siegel approximation all reduce to either (i) FE-generic moment positivity (consistency-only in DH/Epstein by construction — the "proves too much" verdict applies if anyone claims sufficiency) or (ii) RH-content-in-disguise (θ=∞). No probe funded.

---

## One-line structural reason

**The Levinson/Q machinery reduces to positivity of a second-moment quadratic form whose only zeta input is the functional-equation symmetry — so the Q-family is a counting/proportion method (firewall: zero evidence about RH), its θ→∞ limit hides the same moment content the campaign PROVEN exhausted, and the Siegel approximation is the same argument-principle detector in a smoother kernel.**

## Ledger-ready line (append to research/notes/ledger.md)

- **wave9-9B-short-mollifier-2026-08-18** — arXiv:2508.11108 (Conrey–Farmer–Kwan–Lin–Turnage-Butterbaugh, "Short mollifiers of ζ"): classified DUPLICATE-TRAP / NOT-A-NEW-FAMILY. (a) Variational Q-family = Levinson counting method (κ>2θ/3 proportion for any θ>0); proportion ≠ RH (firewall); FE enters only as even-type symmetry (18); no sufficient condition on zeros; escapes no closed lever (S1/log-profile/barrier-zoo untouched). (b) Bettin–Gonek "θ=∞ ⟹ RH" = conjectural long-mollifier moment asymptotic subsuming RH; hidden moment content, not algebraically explicit; DUPLICATE of moment/coefficient-margin trap class (register "levinson-theta-infinity" as indexed member). (c) Proposition 1 (Q_θ → Siegel step function Q∞) = smooth approximation of classical Riemann–Siegel kernel; same argument-principle content as CLOSED xi'-transport; no new zero detector. (d) Barrier-zoo prescription recorded: Q-family is FE-generic ⟹ consistency-only in DH/Epstein by construction; no probe funded. Read-only; no fabrication; BG17 theorem cited as the paper cites it (PROVEN-literature), not re-derived.

## Closure-DAG registration (for the coordinator)

- **No new lever.** Proposal: (i) add trap member tag **levinson-theta-infinity** under the existing moment/coefficient-margin trap node (duplicate, for search/indexing only); (ii) close DAG edge "short-mollifier family → LP/RH" as **not-a-sufficient-condition (counting method)**, with the firewall annotation proportion ≠ RH; (iii) leave closed the ξ'/argument-principle strand (Siegel-f approximation does not reopen it).

## Honesty appendix

- Paper's Theorem 1 numerical constants (0.5898, 0.674…, κ ≥ 2θ/3 etc.): CHECKED NUMERICALLY **in-paper** (Mathematica appendices); NOT re-verified by this agent (read-only dispatch; no numerics funded; Rust-only-if-needed). All structural/classification claims in this note are PROVEN relative to the texts read (paper extract, crossdomain-hunt-2026-08-18, barrierzoo-retrotest-2026-08-18).
- Bettin–Gonek's theorem statement is taken from the paper's own citation (Intro p. 2), not from BG17 directly — marked PROVEN-literature-as-cited.
- No claim here asserts RH true/false, and nothing in the paper is a disproof signal. Documented negative; persistence hook honored: the classification IS the deliverable.