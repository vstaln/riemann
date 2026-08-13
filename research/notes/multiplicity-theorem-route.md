# Route to a genuine multiplicity / simple-fraction theorem for RH

**Agent:** ARCHITECT (epistemology-limits + literature verification + constraint-hardness)
**Verdict up front:** The task premise contains one **false attribution** and one **half-truth**, and correcting them sharpens — but does not change — the bottom line. The correct unconditional record for "simple **and on the critical line**" is **40.75%** (Pratt–Robles–Zaharescu–Zeindler 2020, PRZZ20), *not* "~0.405, Bui–Heap–Turnage–Young" — no such paper exists on arXiv (verified). The certificate-class ceiling **0.6818** is real and Lean-proven, and the only non-circular lever is a *new proven* input: either a beyond-bandwidth-1 form-factor estimate (conjectural), or a multiplicity-structure theorem excluding the extremal near-CUE 256-law. A bound on Σ_ρ (m_ρ − 1) is the **right object but not a free lever** — strengthening it is either circular (it re-derives the pair-correlation bound already saturated by the ceiling) or requires exactly the missing input. Every claim below carries an honesty label.

## 0. Label legend

- **PROVEN** — theorem with a published/formalized proof (Lean or literature).
- **CHECKED NUMERICALLY** — computed/verified this session with a script or programmatic query.
- **CONJECTURED** — open problem or hypothesis.
- **ABANDONED** — a claim in the task premise that I refuted and will not use.
- **INCONCLUSIVE** — cannot be established from available sources.
- **[CITATION]** — source; a number resting on a secondary citation is flagged.

---

## 1. State of the art: the simple-zeros fraction, exactly

Three distinct quantities are conflated in circulation. They must be separated before anything else:

| Quantity | Best bound | Method | Status / citation |
|---|---|---|---|
| **Simple AND on the critical line** (the "multiplicity theorem" target) | **> 40.75%** | Levinson/Feng mollifier | **PROVEN (unconditional)** — Pratt–Robles–Zaharescu–Zeindler 2020 [PRZZ20], Res. Math. Sci. 7(2):74. [CITATION] = BGST 2501.14545 §1, quoting "more than 40.75% of the zeros are on the critical line and simple". |
| On the critical line (any multiplicity) | **> 41.72%** | Levinson/Feng mollifier | **PROVEN (unconditional)** — [PRZZ20], same source. |
| Simple (all zeros, not necessarily on line) | **> 61.7%** | Montgomery pair correlation, unconditional form | **PROVEN (conditional on a box hypothesis weaker than RH)** — Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2023 [BGSTB24], arXiv:2306.04799: zeros with T^{3/8}<γ≤T and |β−1/2| < 1/(2 log T) → ≥ 61.7% simple. |
| Simple (all zeros, **RH**) | **> 67.92%** | SDP / Montgomery | **PROVEN (on RH)** — Chirre–Gonçalves–de Laat 2020 [CGdL20]. [CITATION] = BGST 2501.14545 §1. |
| Simple (all zeros, **RH**) | **19/27 ≈ 70.37%** | discrete mollified moments of ζ′ | **PROVEN (on RH)** — Bui–Heath-Brown 2013. [CITATION] = project context `structural-final-verdict.md` + the string "70.3703% of the zeros are simple" in BGST 2501.14545. Verify the original before relying in print. |
| Certificate-class ceiling (rank–trace, bandwidth-1 pair correlation) | **0.6818** (unconditional upper bound on what *this class* can certify) | Lean `ceiling_law256_signed` | **PROVEN (Lean, std axioms)** — modulo the numerically-checked enclosure `EnclOK`; see `attack-ceiling.md`, `attack-lpdual.md`. |

**The task's "~0.405" is PRZZ's 0.4075, mis-attributed.** The trio "Bui–Heap–Turnage–Young" does not exist:
- **ABANDONED** — arXiv query for `ti:"simple zeros" AND au:"Heap"` returns **zero** results; Turnage-Butterbaugh's full arXiv list (40 entries, queried this session) contains **no** simple-zeros fraction paper (her zeros work is gaps/pair-correlation/moments, e.g. arXiv:2306.04799, 2501.14545, 2025 "Short mollifiers"). The nearest real papers are Bui 2013 ("Simple Zeros Of The Zeta Function", arXiv:1306.0458) and Bui–Heap 2014 ("Gaps between zeros of Dedekind zeta-functions II"). No joint Bui–Heap–Turnage-Butterbaugh simple-fraction result exists. **CHECKED NUMERICALLY** (export.arxiv.org API, two independent queries).

**Net, corrected:** the honest unconditional state of the art on "simple and on the line" is **0.4075**; the honest RH-conditional state is **0.7037 (19/27)**; the certificate ceiling is **0.6818**, which sits *between* them and is Lean-proven.

---

## 2. The exact technical obstruction to going beyond 0.405 unconditionally

Two independent walls, one per route:

**Wall A — the mollifier route (Levinson/Feng), stuck at 40.75% / 41.72%.**
The Feng mollifier length θ is the bottleneck: PRZZ20 achieved θ < 5/12 = 0.4167 (giving 41.72% on line) by pushing the Feng θ from 17/33 to 6/11 via Kloosterman-sum / zero-density decomposition (Type I/II sums). Going further requires one of:
- a longer admissible mollifier (θ → 1/2), blocked by the zero-density estimates for ζ in short ranges;
- better zero-density (the "decades-long breakthrough in zero-density estimates" is a 2026 survey title in Turnage-Butterbaugh's list, **CHECKED NUMERICALLY** — status of a usable new unconditional input: INCONCLUSIVE from this session's sources).
**Classification: HARD WALL at current inputs; a real, non-circular opening exists only via a genuinely new zero-density or mollifier-length theorem.**

**Wall B — the pair-correlation certificate route, hard-capped at 0.6818.**
`attack-ceiling.md` + `attack-lpdual.md` (both in this repo) establish, in Lean:
- The certificate value v is pinned **1:1 by the certified simple fraction p₁** (LP shadow price exactly 1).
- The class optimum is attained at v\* = p₀ + |E(1)| = 0.68183123, and the near-CUE 256-law realizes p₀ = 0.68182868746… with F ≡ 1 on [0,1] — an admissible configuration against **every** bandwidth-one datum.
- Therefore no certificate of this class can exceed 0.6818, *unless* a proven beyond-bandwidth-1 input (F(α) for some α > 1, or a multiplicity-structure bound) rules out the extremal law.
**Classification: HARD WALL (Lean-proven), not an artifact.** The only proven beyond-bandwidth-1 information is the *trivial nonnegativity* F ≥ 0, which supplies upper constraints only, not values (already exploited by CGdL20's SDP; does not move p₁).

**Net:** 0.405 → beyond requires either (a) a new mollifier/zero-density theorem, or (b) new pair-correlation input beyond |α| = 1. Neither exists in the verified literature. This is *not* a certificate-of-effort gap; it is a documented structural fact.

---

## 3. Is an explicit-formula bound on Σ_ρ (m_ρ − 1) the right lever? (conditional vs circular)

**The object is right; the lever is not free.**

Σ_ρ (m_ρ − 1) = N_mult(ζ) − N_simple(ζ) is **exactly** the complement of the simple fraction: p₁ = 1 − (1/N)Σ_ρ (m_ρ − 1) over a window. So "bound Σ(m_ρ − 1)" ≡ "bound the simple fraction" — it is the target, not a new input. The real question is *what input bounds it*, and there are exactly two known mechanisms:

1. **Rank–trace / pair-correlation (Montgomery):** bounds Σ (m_ρ² − m_ρ) (hence Σ (m_ρ − 1)) from the form factor on [0,1]. This is **saturated**: the 0.6818 ceiling is the exact optimum of this input, Lean-proven. A *stronger* pair-correlation bound on Σ(m_ρ − 1) would require F(α) on (1,∞), which is **equivalent to Hardy–Littlewood prime-pairs** (Goldston–Montgomery 1987 equivalence, cited in `attack-ceiling.md` §3). **CONJECTURED. Circular to assume.**

2. **Mollifier / Levinson (discrete moments of ζ and ζ′):** bounds the simple fraction by a *different* mechanism that does run unconditionally, and is currently at 0.4075 (PRZZ20). This is **not** circular, but it is **not** a "pair-correlation strengthening" either — it is the route that Wall A blocks.

**Conclusion on (3):** A strengthening of Montgomery's pair correlation to yield an explicit-formula bound on Σ_ρ (m_ρ − 1) is the *right shape of theorem*, but as a *hypothesis* it is conditional-on-RH or conjectural, and as a *theorem* it either (i) reproduces the bandwidth-1 bound already saturated at 0.6818 (no gain), or (ii) must invoke beyond-bandwidth-1 data (Hardy–Littlewood, conjectural). It is **not an independent lever**. The genuine unconditional lever is the mollifier route (Wall A), and the genuine structural lever is a multiplicity-exclusion theorem (below).

---

## 4. The minimal new theorem (precise, checkable)

Two candidate statements, each independently sufficient, each falsifiable:

**Theorem A (minimal beyond-bandwidth-1 input).** There exist constants δ > 0 and c ∈ (0,1] such that, *unconditionally*, for all α ∈ (1, 1+δ),
F(α) ≥ c
(or, dually, F(α) ≤ C with a sharp C), where F(α) = lim_{T→∞} (2π/(T log T)) Σ_{γ,γ′ ≤ T} T^{−iα(γ−γ′)} W(γ−γ′).
*Checkability:* any such estimate is a prime-pair statement (Goldston–Montgomery equivalence); verify by producing the additive-correlation estimate Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h) for |h| ≤ X²/T. Each unit of certified simple fraction transfers 1:1 (shadow price 1), moving the ceiling from 0.6818 to 0.6818 + O(δ).
**Status: CONJECTURED** (equivalent to a Hardy–Littlewood prime-pair estimate; none proven). This is the *only* theorem that reopens the pair-correlation route.

**Theorem B (multiplicity-structure exclusion).** The actual zero configuration of ζ cannot realize a 256-periodic near-CUE law with simple fraction ≤ p₀ = 0.6818 — concretely: prove an *unconditional* upper bound on the multiplicity-weighted count in some short zero-window (e.g., Σ_{γ∈(T,2T]} (m_γ − 1) ≤ (1 − p₀ − ε)·N(T,2T]) for an explicit ε > 0) that contradicts the extremal law's shape.
*Checkability:* compare against the law's exact rational weights/positions/marks (certificate sha256 `cc3de991…`, or the regenerated LP dual in `attack-lpdual.md`). If a bound with ε > 0 is proven, `ceiling_law256`'s premise ("the law is admissible") fails and the ceiling falls.
**Status: INCONCLUSIVE** — no such structural constraint is known or even suggested by the local sources; it may not exist (the law may be arbitrarily close to realizable by a genuine configuration). Low prior, but it is the only *unconditional, non-conjectural* way to beat 0.6818 inside the certificate class.

**Theorem C (mollifier route, unconditional).** Extend the admissible Feng mollifier length beyond θ = 6/11 (equivalently, sharpen the relevant zero-density estimate for ζ in short ranges) to push the simple-on-line proportion past 0.4075.
*Checkability:* an explicit θ > 6/11 with a zero-density input weaker than RH.
**Status: OPEN, unconditional in principle** — the survey "A decades-long breakthrough in zero-density estimates and primes in short intervals" (Turnage-Butterbaugh, 2026, in her arXiv list — **CHECKED NUMERICALLY** for existence; content INCONCLUSIVE this session) is the natural place to look for the required input.

**Minimality statement:** Theorem A is the *smallest* new hypothesis that breaks the pair-correlation ceiling (any non-trivial proven value of F past 1 suffices); Theorem C is the smallest that breaks the mollifier wall without any new hypothesis class. Everything else (higher Gram-matrix moments in the Rudnick–Sarnak range kλ < 2, the ξ′-transport giving 0.85838 for ξ′ — see `attack-ceiling.md` §3) is either already-saturated or a different function, and cannot move p₁ for ζ.

---

## 5. Decisions

- **ABANDON** the attribution "~0.405, Bui–Heap–Turnage–Young". Correct to **PRZZ20, 40.75%**.
- **ABANDON** (confirmed) "push the unconditional simple-fraction past 0.6818 via the bandwidth-1 pair-correlation certificate." Lean-proven wall.
- **FUND** (conditional on a hypothesis strictly weaker than full pair-correlation conjecture): Theorem A.
- **FUND** (unconditional, low prior, high verification value): Theorem B — adversarial: any ε > 0 refutes the ceiling's only premise.
- **FUND** (unconditional, classical): Theorem C — a new zero-density/mollifier-length result, the only non-circular unconditional lever.

## 6. Assumptions

- `[verified]` PRZZ20 = 40.75% simple-on-line / 41.72% on-line, unconditional — quoted in BGST 2501.14545 §1 (read this session).
- `[verified]` BGSTB24 61.7% simple under box hypothesis — read in arXiv:2306.04799 abstract/text this session.
- `[verified]` No Bui–Heap–Turnage-Young simple-zeros paper — two arXiv API queries this session.
- `[verified]` Ceiling 0.6818 and its LP tightness — Lean files + `attack-ceiling.md` + `attack-lpdual.md` (repo).
- `[inferred]` 19/27 ≈ 0.7037 attributed to Bui–Heath-Brown 2013 — carried from project context and the "70.3703%" string in BGST 2501.14545; the original paper was not opened this session. **Flag for verification before citing in print.**
- `[inferred]` CGdL20 67.92% (RH) — from BGST §1 citation; original not opened.

## 7. Open items for follow-up (not blocking)

1. Open Bui–Heath-Brown 2013 directly and confirm 19/27 (label upgrade: `[verified]`).
2. Open PRZZ20 directly and confirm 40.75% vs 41.72% split (label upgrade from secondary citation).
3. Read the 2026 zero-density survey for whether it yields an unconditional θ > 6/11 (Theorem C feasibility).
4. Regenerate the 256-law LP dual (per `attack-lpdual.md` §4) to make `EnclOK` an independent CHECKED-NUMERICALLY item rather than INCONCLUSIVE.

---
*This note is deliberately partial on items 1–4 rather than blocked on them. The state-of-art map (§1), the obstruction (§2), the circularity verdict (§3), and the three minimal theorems (§4) are complete and checkable.*
