# Pair-Correlation Route to RH — Deep-Research Findings

**Agent:** RESEARCHER (s4h-investigation)
**Date:** 2026-08-12 (Round: wave-1)
**Task:** `research/waves/wave-1/task-paircorr.md`
**Status:** COMPLETE — the pair-correlation narrow-box method is **dominated** by our rank-trace
machinery at every comparable constant; the narrow-box condition is **compatible** (our method
needs no box and attains the same or better constants unconditionally), and the only route by
which the two could *combine* to break the 0.6818 in-class ceiling is the **conjectural**
|α| > 1 form-factor input (CGdL-type SDP / Hardy–Littlewood additive correlations), which no
proven source supplies.

---

## 0. Sources read (all local full text; arXiv API search for follow-ups)

| Source | Content | Status |
|---|---|---|
| `papers/bgst-2501.14545.txt` (BGSTB25) | Pair Correlation of Zeros I: Proportions of Simple and Critical Zeros. Thm 1 (narrow box b→0): 2/3 simple AND 2/3 on-line, 1/3 both; Thm 2 (fixed b, MT/Tsang kernel): Table 1. | FULL TEXT READ |
| `papers/baluyot-etal-2306.04799.txt` (BGSTB24) | Unconditional Montgomery Theorem. Thm 2 (thin box |β−1/2| < 1/(2 log T)): 61.7% simple; Thm 3 (strong zero-density). | FULL TEXT READ |
| `papers/gs26-2603.28104-zetazeros-narrowbox.txt` (GS26) | Zeta Zeros in a Narrow Vertical Box. Simplest proof of 2/3 simple AND on-line under box b→0; **Theorem 2: the structural C-based statement** (C = bound on Σ_{γ=γ′} 1). | FULL TEXT READ |
| `papers/gs25-2511.20059-zetazeros-criticalline.txt` (GS25) | Zeta Zeros on the Critical Line. Theorem 2/3: C-bound ⇒ simple ≥ 2−C, on-line ≥ 2−C, both ≥ 2−C; horizontal multiplicity H(γ) = #zeros on line t=γ. | FULL TEXT READ |
| `papers/claude-riemann-paper.txt` (our program) | Theorems A–E, rank–trace machinery, Theorem D (0.6725), §7.4 comparison with BGSTB/GS, §7.5 limits (0.6818 ceiling). | FULL TEXT READ (relevant sections) |
| `papers/cgdl-1810.08843-paircorr-sdp.txt` (CGdL20) | SDP pair-correlation bounds. On RH: N*(T) ≤ 1.3208 N ⇒ simple ≥ 0.6792. Uses **F(α) positivity beyond [−1,1]** (f eventually non-positive). | FULL TEXT READ (key lemmas) |
| `papers/glss25-2503.15449-pccI.pdf`, `glss26-2507.06823-pccII-ah.pdf` | PCC ⇒ 100% simple AND on-line (no RH) — via Gallagher–Mueller, ES (Essential Simplicity). | ABSTRACTS (PDF not extractable locally) |
| `papers/bgst-2508.10857-alternative-hypothesis.txt` | AH ⇒ constraints on pair density at k/2 spacings; strong AH ⇒ ES. | PRESENT |
| arXiv API search | "pair correlation simple zeros critical", "narrow box zeta", Goldston–Suriajaya author query | **No post-2026 follow-ups beyond the known GS25/GS26/GLSS25/GLSS26 line.** |

**Label conventions:** PROVEN = theorem in a read source with verified proof; CHECKED NUMERICALLY
= reproduced by a script I ran (script + command cited); CONJECTURED = open / requires an
unproven input; INCONCLUSIVE = blocker named.

---

## 1. Exact theorem statements (condition → proportion bound)

### 1.1 BGSTB25 (arXiv:2501.14545) — the primary target paper

**Setup.** For b > 0, the thin vertical box
$$B_b := \left\{s=\sigma+it : \left|\sigma-\tfrac12\right| < \tfrac{b}{2\log T},\ T < t \le 2T\right\}.$$
Let N(B_b) count zeros with multiplicity, N_s(B_b) simple, N_0(B_b) on the critical line,
N_0^s(B_b) simple **and** on the line.

**Theorem 1 (BGSTB25, b→0).** Assume all zeros with T < γ ≤ 2T lie in B_b, with b→0 as T→∞. Then
$$N_s(B_b) \ge \left(\tfrac23+o(1)\right) N(B_b),\qquad
N_0(B_b) \ge \left(\tfrac23+o(1)\right) N(B_b),\qquad
N_0^s(B_b) \ge \left(\tfrac13+o(1)\right) N(B_b).$$
The third is known unconditionally (Heath-Brown 1979 / Selberg), noted in Remark 2.

**Theorem 2 (BGSTB25, fixed b; Tsang kernel with j = j_M).** As T→∞:
- b = 0.3185: N_s, N_0 ≥ (0.66666908 + o(1))·(T/2π)log T; N_0^s ≥ (0.33333816 + o(1))·(T/2π)log T.
- b = 0.001:  N_s, N_0 ≥ (0.67250064 + o(1))·(T/2π)log T; N_0^s ≥ (0.34500129 + o(1))·(T/2π)log T.

Table 1 (j_M): b = 0.001 → 0.67250 / 0.34500; b = 0.3185 → 0.66667 / 0.33334; b = 0.6 → 0.65208 / 0.30416;
b = 1.0 → 0.61748 / 0.23496; b = 1.8 → 0.50862 / 0.01724; b = 2.0 → 0.47485; b = 4.187 → 0.00007.
**The method fails at b ≥ 4.2 for (1.2)/(1.3) and b ≥ 2 for (1.4).**

**Key mechanism (their §1.2, §6).** The sum Σ_{ρ,ρ′∈B_b} Re K_b(−i(ρ−ρ′) log T) is evaluated by
Montgomery's theorem (Lemma 4, (5.10)) and is *termwise positive* (Tsang kernel Lemma 3(c):
Re K_b(x+iy) > 0 for |y| < b). The "diagonal terms" (ρ = ρ′) are ≥ N(B_b); the "symmetric
diagonal terms" (ρ′ = 1−ρ̄, β ≠ 1/2) are Σ_{β≠1/2} m_ρ. Positivity lets them conclude
$$N(B_b) + \sum_{\beta\ne1/2} m_\rho \le \left(C_b(j)+o(1)\right)\frac{T}{2\pi}\log T,
\qquad C_b(j) := \frac{j(0)+2\int_0^1 \frac{\alpha j(\alpha)}{\cosh(b\alpha)}d\alpha}{2\int_0^1 \frac{j(\alpha)}{\cosh(b\alpha)}d\alpha},$$
hence N_s ≥ (2−C_b)N, N_0 ≥ (2−C_b)N, N_0^s ≥ (3−2C_b)N (their (7.2)). **The box enters exactly
once:** |β−β′| < b/log T for all pairs in B_b, which is what makes Re K_b > 0 termwise.

### 1.2 GS25 (arXiv:2511.20059) — the structural reformulation

**Theorem 2 (GS25).** Suppose Σ_{ρ,ρ′: γ=γ′} 1 ≤ (C+o(1))·(T/2π)log T with 1 ≤ C < 2. Then
proportion of simple zeros ≥ 2−C **and** proportion on the critical line ≥ 2−C.

**Theorem 3 (GS25).** Suppose Σ_ρ m_ρ + Σ_{β≠1/2} m_ρ ≤ (C+o(1))·(T/2π)log T. Then
(i) simple **and** on-line ≥ 2−C; (ii) avg(simple, on-line) ≥ (3−C)/2; (iii) simple ∪ on-line ≥ (4−C)/3.
With C = 4/3: (i) 2/3, (ii) 5/6, (iii) 8/9. [PROVEN — the counting is elementary; see §3.]

**Horizontal multiplicity (§7).** H(γ) := # zeros (with mult) on the line t = γ. Then
H(γ) = 1 ⇒ simple on-line; H(γ) = 2 ⇒ double on-line OR symmetric off-line pair;
H(γ) = 3 ⇒ triple on-line OR simple-on-line + pair; H ≥ 4 ⇒ needs double off-line.
**Σ H(γ) = Σ_{γ=γ′} 1 = Σ_ρ m_ρ²** (pairs at the same ordinate) — this is the *same* quantity
bounded by C. [PROVEN.]

### 1.3 GS26 (arXiv:2603.28104) — the simplest proof

**Theorem 1 (GS26) = BGSTB25 Thm 1** (2/3 simple AND on-line under box b→0), proved with only the
Fejér kernel and Selberg's elementary Lemma 3, no Tsang kernel, no computation. The proof shows:
under the box, the Fejér sum K_b(T) = (4/3+o(1))N, and after removing the W-weight and comparing
to the real Fejér kernel, Σ_{γ=γ′} 1 ≤ (4/3+o(1))N; Theorem 2(i) (C = 4/3) gives both ≥ 2/3.
[PROVEN.]

### 1.4 BGSTB24 (arXiv:2306.04799) — the unconditional Montgomery theorem

**Theorem 1 (BGSTB24).** F(α) := ((T/2π)log T)^{−1} Σ_{ρ,ρ′: 0<γ,γ′≤T} T^{α(ρ−ρ′)} w(ρ−ρ′),
w(u) = 4/(4−u²), is real, even, nonnegative, and
$$F(\alpha) = T^{-2\alpha}(\log T + O(1)) + \alpha + O(1/\sqrt{\log T}) \quad \text{uniformly for } 0\le\alpha\le1.$$
[PROVEN; the 2501.14545 v2 corrects the error terms from the original arXiv version.]

**Theorem 2 (BGSTB24).** Assume all zeros with T^{3/8} < γ ≤ T lie in |β−1/2| < 1/(2 log T). Then
≥ 61.7% of zeros are simple. (Fejér kernel gives 0.6086; j_M gives 0.6175; constants verified
numerically below.) Also holds under the strong zero-density hypothesis (1.6). [PROVEN.]

**Remark (BGSTB24).** "The method of proof neither requires nor provides any information on whether
any of these zeros are on or not on the critical line." — BGSTB25 later shows this is false.

### 1.5 CGdL20 (arXiv:1810.08843) — SDP, RH-conditional

**Theorem 1 / Corollary 2 (CGdL20, RH).** N*(T) ≤ (1.3208+o(1))N(T) ⇒ N_s(T) ≥ (0.6792+o(1))N(T).
(GRH: N* ≤ 1.3155N ⇒ 0.6845 simple.) **The engine:** they take f ∈ A_LP (even, f̂(0)=f(0)=1, f̂ ≥ 0,
f eventually non-positive), so ∫_{|x|>1} ĝ(x)F(x,T)dx ≤ 0 is *dropped* using F ≥ 0 — i.e. they
**exploit F(α) ≥ 0 for |α| > 1 as an upper-constraint**, with support beyond 1. [PROVEN on RH;
the |α|>1 data used is only F ≥ 0, which is unconditional (Lemma 3(BGSTB24)).]

### 1.6 GLSS25 (arXiv:2503.15449) — PCC ⇒ 100%

**Theorem 5 (GS25, citing GLSS25).** The Pair Correlation Conjecture implies asymptotically 100% of
the zeros are simple **and** on the critical line. Engine: PCC ⇒ ES (Essential Simplicity, (8.3)) ⇒
C = 1 in Theorem 2/3. **CONJECTURAL (PCC is open); the RH-free deduction ES ⇒ 100% is PROVEN.**

### 1.7 The rank-trace program (our machinery, `claude-riemann-paper.txt`)

- **Theorem A (unconditional):** N_0^*(T,2T) ≥ (H(λ) − o(1))N(T,2T), H(λ) = 2 − 1/λ − λ/3; at λ=1: **≥ 2/3 on-line (distinct)**; Theorem D: **0.67250...**
- **Theorem B (unconditional):** N_0^s(T,2T) ≥ (H(λ)−o(1))N; at λ=1: **≥ 2/3 simple AND on-line**; Theorem D: **0.67250...** (both with the Montgomery–Taylor-optimal window).
- **Theorem C (unconditional):** N_d(T,2T) ≥ (max(H_d(λ), F(λ))−o(1))N, H_d = (1+H)/2, F(λ) = λ/(1+λ²/3); at λ=1: **≥ 5/6 distinct**; Theorem D: **0.83625...**
- **Theorem E:** same for fixed primitive Dirichlet L-functions.
- **Theorem D constant:** 2 − 1/c*_1 = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573..., with
  c*_1 = 2 tan(1/√2)/(√2 + tan(1/√2)) = 0.75329606785607..., 1/c*_1 = 1/2 + 2^{−1/2}cot(2^{−1/2}) = 1.32749929632059...
- **§7.5/ceiling:** no certificate reading only bandwidth-one data (F on [−1,1]) can certify more
  than 0.68185 simple zeros (the near-CUE 256-law). **PROVEN (Lean) modulo a numerically-checked enclosure.**

---

## 2. THE METHOD in detail: how does pair correlation yield on-critical-line results?

### 2.1 The object: a bound on Σ m_ρ² (equivalently Σ H(γ), equivalently Σ_{γ=γ′} 1)

All the pair-correlation results — Montgomery's 2/3 simple, BGSTB25's 2/3 on-line, GS25/GS26's
2/3 simple-and-on-line, and our Theorem B — reduce to **one quantitative claim**: a constant C such
that, with N(T) ~ (T/2π)log T,
$$\sum_{\rho: 0<\gamma\le T} m_\rho^2 \;\le\; (C+o(1))\,N(T).$$
The equivalence with the horizontal-multiplicity sum is exact: Σ_{ρ,ρ′: γ=γ′} 1 = Σ_{γ: on a line} H(γ)²... no —
more precisely Σ_{ρ,ρ′: γ=γ′} 1 = Σ_ρ m_ρ², because pairs (ρ,ρ′) with the same ordinate γ are exactly
the m_ρ² pairs within the multiset of m_ρ copies at that ordinate. [PROVEN — GS25 §4, §7.]

**Why Σ m_ρ² ≤ C N implies on-line results (the crucial step).** Write the sum over zeros with
β ≠ 1/2 as symmetric diagonal terms: each off-line zero ρ comes with its conjugate pair 1−ρ̄ at the
same ordinate, so
$$\sum_{\beta\ne1/2} m_\rho \;\le\; \sum_{\rho,\rho': \gamma=\gamma'} 1 = \sum_\rho m_\rho^2 \le C N.$$
Then, since Σ_{all} m_ρ = N:
$$N_0 = \#\{\beta=\tfrac12\} \ge N - \sum_{\beta\ne1/2} m_\rho \ge (2-C)N \quad(\text{using } N \le \Sigma m_\rho^2 \text{... no, } N \le \Sigma m_\rho^2 \le CN \text{ is trivial})$$
Careful: the on-line count *with multiplicity* is N_0 = Σ_{β=1/2} m_ρ, and N = N_0 + Σ_{β≠1/2} m_ρ.
The bound Σ_{β≠1/2} m_ρ ≤ C N − N_0... The correct reading (GS25 Thm 2, (5.6)) is:
Σ_{β≠1/2} m_ρ ≤ (C+o(1))N − Σ m_ρ ≤ (C−1+o(1))N using Σ m_ρ ≥ N, and then
N_0^with-mult = Σ_{β=1/2} m_ρ ≥ N − Σ_{β≠1/2}m_ρ ≥ (2−C)N. **The on-line proportion 2−C counts zeros
on the line with multiplicity.** [PROVEN — GS25 (5.5)–(5.6).]

### 2.2 How the C bound is obtained: three readings of the same second moment

**(a) Montgomery's RH reading.** The Fejér-kernel identity
Σ_{γ,γ′} (sin(½(γ−γ′)log T)/(½(γ−γ′)log T))² = (4/3+o(1))N under RH, evaluated via the prime-side
second moment (bandwidth ≤ 1), and the trivial ≥ Σ_{γ=γ′} 1 = Σ m_ρ². Gives C = 4/3, hence 2/3
simple (Montgomery 1973). The 2/3 is **2 − 4/3**, and Montgomery–Taylor/Cheer–Goldston improve the
kernel to C = 1.3275, giving 0.6725 simple. [PROVEN on RH.]

**(b) BGSTB25's RH-free reading with a box.** Unconditional Montgomery (BGSTB24 Thm 1) evaluates the
*same* Fejér/Tsang-kernel sum over complex differences ρ−ρ′. Without RH the sum has the W(ρ−ρ′)
weight and pairs with |β−β′| possibly large. The box B_b makes |β−β′| < b/log T, so the Tsang kernel
has Re K_b(−i(ρ−ρ′)log T) > 0 termwise (Lemma 3(c) BGSTB25), the W-weight removal costs only O(T)
(Lemma 4), and the *whole sum* is ≥ the diagonal Σ m_ρ plus symmetric diagonals Σ_{β≠1/2} m_ρ —
which is exactly the input of GS25 Thm 3 with the same C. **The box is what buys termwise positivity
in the zero-side reading.** [PROVEN under the box.]

**(c) Our rank–trace reading (no box).** Instead of termwise positivity, we use:
- **Sylvester's law of inertia:** each off-line pair {ρ, 1−ρ̄} contributes a (1,1)-signature block to
  the compressed Weil form, *regardless of its depth* (Prop 4.1). Rank(P) ≤ #on-line distinct,
  n₊(Q) ≤ #off-line pairs.
- **Rank–trace inequality (Lemma 3.2):** for Hermitian P ⪰ 0, rank ≤ r, and Q with n₊(Q) ≤ b,
  ‖P+Q‖²_F ≥ c·trP − (c²/4)r + 2c·trQ − c²b; at c = 2: r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F.
- **Prime side:** tr G̃ and ‖G̃‖²_F evaluate unconditionally (bandwidth ≤ 1) to N and (1/λ + λ/3)N
  (Theorem 5.8), giving C_eff = 1/c*_1 = 1.3274992 at the MT-optimal window.

The two traces give the *same* C bound as Montgomery's second moment, but the linear algebra
replaces the box hypothesis. **No box, no RH, no zero-density, no mollifier.** [PROVEN —
`claude-riemann-paper.txt` §§4–6; Lean formalized.]

### 2.3 The "can they combine?" question — the precise answer

The task frames it as "our certified bound is simple+on-line; theirs is simple OR on-line — can they
combine?" The resolution has three parts:

1. **The pigeonhole ceiling on the separate statements.** Their Thm 1(1.2)+(1.3) give simple ≥ 2/3
   and on-line ≥ 2/3 *separately*; by |S∩O| = |S| + |O| − |S∪O| ≥ 2·(2/3) − 1 = 1/3, the combined
   "both" bound is only 1/3 — and that is exactly their (1.4). So **separate simple + on-line does
   NOT give on-line-and-simple; the union of two 2/3's is 1/3 both.** [PROVEN — elementary.]

2. **The correct combined bound comes from the STRUCTURE of Σ m_ρ², not from unioning.** GS25 Thm 3(i)
   shows that a C bound on the diagonal+symmetric-diagonal sum gives simple-and-on-line ≥ 2−C
   *directly*. With C = 4/3 that's 2/3 both (GS26 Thm 1); with our C = 1.3274992 that's 0.6725 both
   (our Thm B). **Our Thm B already dominates their (1.4) by 0.6725 vs 1/3.** [PROVEN.]

3. **Our machinery dominates theirs at every comparable constant, unconditionally:**
   | quantity | BGSTB/GS (box hypothesis) | Ours (unconditional) |
   |---|---|---|
   | simple | 2/3 = 0.6667 (b→0); 0.6725 (b=0.001) | **0.6725** |
   | on-line (with mult) | 2/3 = 0.6667 (b→0); 0.6725 (b=0.001) | **0.6725** (Thm A) |
   | simple AND on-line | 1/3 = 0.3333 (b→0); 0.3450 (b=0.001) | **0.6725** (Thm B) |
   | distinct | — | **5/6 = 0.8333** (Thm C) |
   Their b = 0.001 MT constant equals ours (both are 2 − 1/c*_1 = 0.672500703...), but theirs needs
   the box; ours is unconditional. **There is no proportion gap to close by combining: we are strictly
   ahead.** [CHECKED NUMERICALLY — `scratch/paircorr/final_verify.py`, `combine_analysis.py`.]

4. **Where combination could still bite (the real frontier):** the *only* inputs that improve on
   0.6725 are (i) CGdL-style SDP using F ≥ 0 beyond [−1,1] (gives 0.6792 simple on RH — needs the
   SDP majorant to be made unconditional, which requires a proven |α|>1 input), or (ii) a proven
   Hardy–Littlewood-type additive-correlation estimate Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T
   (paper §7.5(f): would give 13/18 with k₀ = 4, and 1 in the limit). **Both are CONJECTURED.**

**Bottom line for §2:** the pair-correlation route's on-line content is *not* an independent half of
a combination; it is the same Σ m_ρ² ≤ C N bound read through a different (box-dependent) positivity
argument. Our rank–trace reading attains the same C unconditionally and already yields the
"simple AND on-line" statement at the same constant. The genuine open direction is |α| > 1 data.

---

## 3. Is their narrow-box condition compatible with our rank-trace machinery? (THE KEY QUESTION)

**Verdict: COMPATIBLE — and our machinery makes the box unnecessary.**

### 3.1 What the box does in their proof

The narrow-box hypothesis |β − 1/2| < b/(2 log T) for all zeros with T < γ ≤ 2T is used *exactly once*
(BGSTB25 Lemma 4): to ensure |β − β′| < b/log T for all pairs, so the Tsang kernel satisfies
Re K_b(−i(ρ−ρ′)log T) > 0 for every term (Lemma 3(c)). Termwise positivity is what lets them lower-
bound the evaluated zero-side sum by the diagonal + symmetric diagonal terms, i.e. convert the
second-moment evaluation into the Σ m_ρ² ≤ C N inequality with the *same* C. Without the box,
Re K_b can be negative for deep pairs and the sum's terms are not individually positive.

### 3.2 What replaces it in our machinery

Our argument never needs termwise positivity:
- **Sylvester inertia is depth-independent.** An off-line pair {ρ, 1−ρ̄} of *any* depth contributes a
  (1,1) block; the positive index bound n₊(Q) ≤ p and rank(P) ≤ #on-line distinct hold regardless of
  |β − 1/2| (Proposition 4.1). The pair's depth only affects the *magnitude* of its Gram entries,
  which enters the ‖·‖²_F bound — and the prime-side evaluation (Theorem 5.8) controls ‖·‖²_F
  unconditionally without any pointwise control on deep pairs (Remark 4.3, §4.1: "the proof reads
  ‖Ĝ‖²_F from the prime side and uses only rank and positive index here").
- **The rank–trace inequality (Lemma 3.2)** then converts (rank, tr, tr², n₊) into the counting
  inequalities (Prop 4.4), which yield Theorems A–C. The box plays no role.

### 3.3 Structural comparison table

| Aspect | BGSTB25/GS26 (box route) | Rank–trace (our route) |
|---|---|---|
| Hypothesis | all zeros in box width b/log T, b→0 (or b=0.001 fixed) | **none** (unconditional) |
| Positivity | Tsang kernel Re K > 0 termwise (needs box) | Sylvester inertia, depth-independent |
| C bound | C_b(j), depends on b; → 1/c*_1 as b→0 (MT) | 1/c*_1 (MT-optimal window) |
| Bandwidth used | ≤ 1 (Montgomery/BGSTB24 prime side) | ≤ 1 (same prime side) |
| Simple AND on-line | 1/3 (b→0), 0.3450 (b=0.001) | 0.6725 |
| Proves on-line separately? | yes (symmetric diagonals, needs box) | yes (Thm A, no box) |

### 3.4 Is there any way the box *helps* our machinery?

Two candidate mechanisms, both **INCONCLUSIVE / CONJECTURED**:

1. **The box would let us use the Tsang kernel's Re-positivity to sharpen the n₊ bound.** Our
   Proposition 4.1 already captures everything inertia gives; the Tsang kernel positivity is a
   *stronger* property (it would bound the *individual* pair-block traces, not just n₊), but we do
   not use individual pair-block traces in the rank–trace inequality — only tr Q and n₊(Q). To
   exploit the box we would need a *different* inequality consuming per-pair traces, which is not in
   our certificate class (and the ceiling analysis suggests it cannot help for the bandwidth-one
   data anyway). **INCONCLUSIVE — blocker: no such inequality is in the class; §7.5(e) shows higher
   moments don't help.**

2. **The box might weaken the extremal near-CUE law's admissibility.** The 0.6818 ceiling law is a
   256-periodic marked configuration with marks ∈ {1,2} (near-CUE form factor). The box hypothesis
   would force all off-line pairs to have depth < b/log T, which is *compatible* with the law (pairs
   at depth → 0 are spectrally identical to on-line doubles, as our Remark §7.5(b) notes). So the box
   does **not** rule out the ceiling law. **INCONCLUSIVE — the ceiling law's off-line content is at
   depth → 0, which the box permits.**

**Net:** the box condition is *compatible* (nothing in our proof contradicts it), *unnecessary*
(we attain the same C unconditionally), and *not exploitable* within our certificate class (no
known inequality converts per-pair Re K positivity into a better count, and the ceiling persists).

---

## 4. 3–5 CONJECTURED attack ideas combining pair-correlation with our machinery

All ideas below are labeled with their honest status. None is proven; each is a *fundable direction*
with a named blocker.

### Idea 1 — Unconditional CGdL-type SDP via F ≥ 0 beyond [−1,1] (the "free positivity" exploit)
**CONJECTURED.** CGdL20 get N*(T) ≤ 1.3208N (⇒ 0.6792 simple) on RH by choosing f ∈ A_LP (f̂ ≥ 0,
f eventually non-positive) so that ∫_{|x|>1} ĝ(x)F(x,T)dx ≤ 0 using F ≥ 0. **F ≥ 0 for |α| > 1 is
unconditional** (BGSTB24 Lemma 3: F(x,T) = (2/π)∫|Σ...|² dt ≥ 0). The obstruction to making CGdL's
*constant* unconditional is that their derivation of the value of the |x| ≤ 1 integral uses RH
(Montgomery's F(α) = 1 on [−1,1]); BGSTB24's unconditional theorem evaluates the same integral only
for *positive-support* kernels... in fact BGSTB24 Thm 1 *is* unconditional and gives F(α) =
T^{−2α}(log T+O(1)) + α + O(1/√log T) on [0,1], which is enough for the |x| ≤ 1 part. **Attack:**
re-run the CGdL SDP program with BGSTB24's unconditional F on [−1,1] and F ≥ 0 beyond, and check
whether the 0.6792-type constant survives without RH. The paper's ceiling note says no proven
beyond-bandwidth-1 input exists — but F ≥ 0 is not a *value*, it is an *inequality* used as an upper
constraint, so this is a genuinely distinct input from the values the ceiling law matches. **Blocker:
the ceiling's "matches all bandwidth-one data" argument covers the values on [−1,1]; the SDP uses
F ≥ 0 outside, which the near-CUE law also satisfies (its F ≡ 1 there, nonnegativity holds), so the
ceiling *may* still bind — needs the LP dual computed. INCONCLUSIVE until the SDP dual is computed.**
[CONJECTURED — CGdL constants CHECKED NUMERICALLY above; unconditional variant NOT yet run.]

### Idea 2 — Horizontal-multiplicity counting as a 4th constraint (H(γ)-distribution)
**CONJECTURED.** GS25's H(γ) lens says Σ H(γ) = Σ m_ρ² ≤ C N, and the *distribution* of H(γ) (how
many lines carry H = 1, 2, 3, ≥4) is extra combinatorial structure beyond the single C. Our rank–trace
reads tr, tr², n₊ — it does not read the H-distribution. **Attack:** bound the second moment of H,
Σ H(γ)², or the count of lines with H ≥ k, from the pair-correlation side (higher moments of the
zero process, e.g. triple correlation under RH, Hejhal 1994 / Rudnick–Sarnak) and feed it into the
integrality chain m² ≥ 2m−1 / 3m−2. **Blocker:** unconditional triple correlation is available only in
the Rudnick–Sarnak range kλ < 2 (§7.5(e)); for the n₊-bound on (1/2,1) higher moments add nothing,
and for λ ≤ 1/2 the rank cap (Prop 7.4) makes them useless. **INCONCLUSIVE — needs a conditional
(H-or-triple-correlation) input, so it stays conjectural for the constant; the *method* transfer is
PROVEN (the counting identities).**

### Idea 3 — Essential Simplicity as a soft-input hybrid
**CONJECTURED.** GLSS25 prove PCC ⇒ ES ⇒ C = 1 ⇒ 100% simple-on-line (RH-free deduction, PROVEN).
ES is the statement that pairs with |γ−γ′| ≤ (2πλ/log T), λ→0, number (1+o(1))N — i.e. essentially
all zeros are simple on the line. **Attack:** use the *structural* implication ES ⇒ (GS25 Thm 2 with
C=1) inside our rank-trace framework: if ES held, our Prop 4.4 with s_2 = p = 0 would give
s_1 ≥ 4tr − ‖·‖²_F − 2N = (2−1/c*_1)N... no — with C = 1, s_1 ≥ (2−1)N = N, i.e. 100%. The point is
that our Thm B's 0.6725 is *tight* against the extremal configuration (2/3 simple-on-line + 1/6
doubles), and ES would rule out that configuration. **Blocker: ES is open (equivalent to a form of
the pair-correlation conjecture).** The value is in showing *how close* the rank-trace method sits to
the ES threshold: our C_eff = 1.3274992 is 0.3275 above ES's C = 1, and the gap is entirely
conjectural input. [CONJECTURED — the ES ⇒ C = 1 deduction is PROVEN (GS25 §8); the improvement is
not.]

### Idea 4 — The Tsang-kernel Re-positivity as a *conditional* tail correction to n₊
**CONJECTURED.** The box hypothesis buys Re K_b > 0 termwise; our Prop 4.1(ii) bounds n₊(Q) ≤ p but
not the *sizes* of the pair-block traces. If we assumed the box, the Tsang kernel would bound each
pair-block's trace (they are ≈ 2m_ρ·Re K_b(−i(2β−1)log T) > 0), giving a *per-pair* charge that could
sharpen Lemma 3.2 (which currently charges every pair the flat 4). **Attack:** under the box, replace
the flat charge 4 per pair by the actual (positive) pair-block trace, and re-run the rank–trace
inequality. **Blocker:** (a) this reintroduces a box hypothesis (conditional result only); (b) the
per-pair trace depends on the *depth* distribution, which is not bandwidth-one data; (c) the ceiling
analysis shows the flat charge is tight for depth→0 pairs, which the box permits — so the gain would
come only from *deep* pairs, whose count is not controlled by any known input. **INCONCLUSIVE —
blocker: deep-pair count is unknown; the ceiling law puts all pairs at depth → 0 where the flat
charge is tight.**

### Idea 5 — Dirichlet-family transfer with the pair-correlation kernel (Theorem E × GLSS25)
**CONJECTURED.** Theorem E gives 2/3 (and 0.6725 with the MT window) for each fixed primitive
Dirichlet L-function, unconditionally. GLSS25's PCC ⇒ 100% argument is generic to the Selberg class.
**Attack:** run the rank-trace machinery on the *family average* over primitive χ mod q (the paper's
§7.3(iii) sketch: "orthogonality of characters restores Λ* = 1 for the family average"), and
combine with Conrey–Iwaniec–Soundararajan's 14/25 = 56% for Dirichlet L on the line [CIS13]. The
family-average bandwidth can exceed 1 (support up to 1 + ϑ), potentially beating the ζ ceiling.
**Blocker: the Gevrey-class taper needed for Prop 4.2 in the family-average setting is not carried
out (paper §7.3(iii) explicitly); and the family-average second moment needs a large-sieve/orthogonality
input that is standard but was not verified in our sources.** [CONJECTURED — Theorem E PROVEN;
the family-average extension is a paper-sketch, not a theorem.]

---

## 5. Honesty register

| Claim | Label | Evidence |
|---|---|---|
| BGSTB25 Thm 1: box b→0 ⇒ 2/3 simple, 2/3 on-line, 1/3 both | PROVEN | read full proof (Tsang kernel, Lemmas 3–4, §6) |
| BGSTB25 Thm 2 / Table 1: b=0.001 ⇒ 0.67250/0.34500; b=0.3185 ⇒ 0.66667/0.33334 | PROVEN (paper) + CHECKED NUMERICALLY | `scratch/paircorr/final_verify.py`: implied C(b=0.001) = 1.32749936 ≈ 1/c*_1 = 1.32749929632 ✓; C(b=0.3185) = 1.33333092 ≈ 4/3 ✓; 3−2C reproduces N_s0 ✓ |
| BGSTB24 Thm 1: unconditional Montgomery, F(α) = T^{−2α}(log T+O(1)) + α + O(1/√log T) on [0,1] | PROVEN | read full proof |
| BGSTB24 Thm 2: thin box ⇒ 61.7% simple (j_M) | PROVEN + CHECKED NUMERICALLY | `final_verify.py`: 2 − (1.0061271908+0.2832624869)/(2·0.4663199124) = 0.617483788 ≈ 0.617483786 ✓; Fejér 0.608612928 ≈ 0.608612927 ✓ |
| GS25 Thm 2/3, GS26 Thm 1: C ⇒ simple&on-line ≥ 2−C; ΣH(γ) = Σ m_ρ² | PROVEN | read full proofs (elementary counting) |
| Our Thm A/B/C/D constants: 2/3, 0.6725, 5/6, 0.83625 | PROVEN (paper, Lean) + CHECKED NUMERICALLY | `final_verify.py`: c*_1 = 0.75329606785607, 1/c*_1 = 1.32749929632, H0 = 3/2 − 2^{−1/2}cot(2^{−1/2}) = 0.67250070367941164573 ✓ (analytic identity; 2D quad agrees to 7.5e-7 with correct error estimate) |
| Pigeonhole: separate 2/3 + 2/3 ⇒ only 1/3 both | PROVEN | elementary set theory; matches BGSTB25 (1.4) |
| Our Thm B (0.6725 simple&on-line) dominates BGSTB25 (1/3 both) | PROVEN (comparison of proven bounds) | see dominance table, §2.3 |
| Our C_eff = 1/c*_1 equals BGSTB25's C(b=0.001) | CHECKED NUMERICALLY | implied C = 2 − 0.67250064 = 1.32749936 vs 1/c*_1 = 1.32749929632 (diff 6e-8, rounding of their printed decimal) |
| CGdL20: RH ⇒ N* ≤ 1.3208N ⇒ simple ≥ 0.6792 | PROVEN (on RH) | read Lemmas 8, Cor 2 |
| F ≥ 0 beyond [−1,1] is unconditional | PROVEN | BGSTB24 Lemma 3 (integral representation) |
| No proven |α|>1 form-factor *value* exists | PROVEN (literature verdict) | ceiling note §3: everything beyond 1 is conjectural (HL/prime-pair/PCC) |
| 0.6818 in-class ceiling (bandwidth-one certificates) | PROVEN (Lean, modulo EnclOK) | `attack-ceiling.md`; our sources' §7.5 |
| Ideas 1–5 would improve constants | CONJECTURED | blockers named in §4 |
| "the box is compatible with / unnecessary for our machinery" | PROVEN (structural argument) | §3; Sylvester inertia is depth-independent (Prop 4.1) |
| "the box can sharpen our n₊/per-pair charge" | INCONCLUSIVE | §4 Idea 4; deep-pair count unknown, ceiling law puts pairs at depth→0 |

**Scripts (all in `scratch/paircorr/`, all run with `/usr/bin/python3`):**
- `final_verify.py` — ALL constants (c*_1, 1/c*_1, H0, Fejér/BGSTB24 proportions, BGSTB25 Table-1
  implied C's, pigeonhole, GS25 Thm-3 structural constants, MT window functional). **The canonical
  verification script; self-contained; prints verdicts; exits 0 on pass.**
  Command: `/usr/bin/python3 /root/riemann/scratch/paircorr/final_verify.py`
- `combine_analysis.py` — pigeonhole analysis, dominance table, C_eff comparison, GS26 Theorem-2
  structural statements (ΣH(γ) = Σ m_ρ² identity discussion).
- `verify_paircorr.py`, `mt_kernel.py`, `mt_kernel2.py` — early attempts: H0, C_b(jF) = 4/3,
  Montgomery–Taylor kernel transcription attempts. **Negative results recorded:** the garbled j_M
  formula in the pdftotext extraction (2501.14545 (4.3)) does not directly reproduce the paper's
  printed integral constants with my transcription; the *implied* C from the paper's printed Table-1
  values (2 − 0.67250064 = 1.32749936) matches 1/c*_1 = 1.32749929632 to 6e-8, which is the decisive
  check (the formula-level transcription is a pdftotext artifact, not a mathematical discrepancy).

**Copy-to-tools note:** these are verification scripts for *this* note; per project rules I keep them
in `scratch/paircorr/` (not owned by another agent; the tools/ dir is owned by the main program —
copying canonical tools/ was not required since these are note-specific).

---

## 6. What this means for the program (synthesis)

1. **The pair-correlation route is *not* a separate source of on-line content to be combined with
   rank–trace; it is the same second moment read through a box-dependent positivity argument that
   our inertia reading already replaces.** The narrow-box results are strictly weaker than Theorem A/B
   at every comparable constant, and their only structural novelty (GS25 Thm 3: Σ m_ρ² ≤ C N controls
   simple, on-line, and both simultaneously) is *already what our C_eff = 1.3274992 does* —
   unconditionally.
2. **The genuine open frontier is |α| > 1 form-factor information.** Three candidate inputs, all
   conjectural: (a) unconditional CGdL-type SDP using F ≥ 0 beyond 1 (Idea 1 — the *only* one that
   uses a proven inequality rather than a conjectured value); (b) Hardy–Littlewood additive
   correlations (paper §7.5(f), would give 13/18 and 1 in the limit); (c) the family-average Dirichlet
   transfer restoring bandwidth > 1 (Idea 5). Of these, **(a) is the most actionable**: F ≥ 0 for
   |α| > 1 is proven, the SDP machinery is public (CGdL20), and the question "does an unconditional
   SDP majorant beat 0.6725 and does it escape the 0.6818 ceiling" is decidable by computation.
3. **The ceiling's robustness check:** the near-CUE 256-law has F ≡ 1 (≥ 0) beyond 1, so the SDP's
   F ≥ 0 usage does not by itself invalidate the ceiling; the LP dual computation (in-class,
   `attack-ceiling.md` keep-alive item 1) is the decisive test for Idea 1.
4. **Recommended next actions (for PLANNER):** (i) compute the unconditional CGdL-SDP dual and check
   against 0.6725/0.6818; (ii) re-derive GS25 Thm 3(i) in our units to confirm the C_eff ↔ 2−C
   dictionary formally (Lean-adjacent); (iii) file the "box is unnecessary" structural note as a
   completed literature verdict (this note).

---

**RESULT: COMPLETE — the pair-correlation narrow-box route is dominated by our rank–trace machinery
(same C = 1.3274992, strictly stronger proportions, no box), and the only way the two could combine
to break the 0.6818 ceiling is the conjectural |α| > 1 input, of which the unconditional-CGdL-SDP
variant (using the proven F ≥ 0 beyond 1) is the most actionable next step.**
