# Attack: the real-data constants of Theorems A–D — audit, reconciliation, and movability of the 0.6725

**Agent:** EXECUTIONER (constant audit + reconciliation; constraint-hardness + epistemology lens)
**Date:** 2026-08-11
**Task:** re-derive the paper's real-data certificate v = p₁ + |E(1)| for the REAL zeros; audit every constant
(Chebyshev–Mertens sums, MV Hilbert 3π/2, O(1/log T) terms); compute the best real constant obtainable with the
paper's own inputs under (a) the paper's constants and (b) any tightenings; answer whether v(real) exceeds
0.6725 at any λ ∈ (0,1]; reconcile 2/3 vs 0.6725.
**Verdict up front:** **v(real) = 2 − 1/c\*₁ = 0.6725007036794116… (Theorem D, PROVEN) and it is IMMOVABLE with
existing inputs.** (i) p₁(real) is the simple-fraction bound from the second moment alone: 2/3 with the flat-top
window (Thm B, H(1) = 2 − 1/F(1) = 2 − 4/3), upgraded to 2 − 1/c\*₁ = 0.6725 by the window optimisation (Thm D;
the task's "c\*₁ = 1.3275" is **1/c\*₁ = 1.3274993**, with c\*₁ = 0.7532961 the trace-ratio maximum — see §1.2).
(ii) E(1)(real) is NOT a fixed constant (no fixed-N real configuration exists); it is the finite-T error
−O(E′_T), E′_T = w/L + (l²+X)log l/(Tl) + T^{λ/2−1}, size O(log log T/log T) at λ=1, O(1/log T) at λ<1
(CHECKED: ≈ 0.070 at T=10¹⁰, λ=1), with the underlying zero-side near-CUE deviation O(1/√log T) (BGSTB24 Thm 1,
≈ 0.21 at T=10¹⁰ — ~7·10³⁸ × the 256-law's τ = 3·10⁻⁴⁰). (iii) The constant audit finds real slack ONLY in
o(1) error terms (MV 3π/2 vs sharp π / measured ≈ 2.52; Chebyshev–Mertens 3√x vs true ≈ 2√x; δ⁻¹ ≤ 2n vs ~1/n;
end-effect bookkeeping of Lemma 5.4); the leading constants ((log x)²/2, (log x)³/6, 1/6, 2/3, 4/3, c\*₁) are
exact/optimal. Sharpening the slack constants improves the implied constant c(λ) in the finite-T error at most
~2×, NEVER the liminf, and never enough to matter at accessible heights: even with perfect constants the
finite-T error has an irreducible floor ≈ 1/l + log l/(2πl) (taper + bandwidth wall), which clears the
window-gain 0.0058 only at l ≳ 300 (T ≳ 10¹³⁰). **The real lower bound cannot move with existing inputs; only
the finite-T error's implied constant can be shaved.**

---

## 0. Honesty labels

| Claim | Label |
|---|---|
| c\*₁ = 0.75329606785607067722…; 1/c\*₁ = 1.3274992963205883543… = 1/2 + 2^(−1/2)cot(2^(−1/2)); 2 − 1/c\*₁ = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573…; Thm-D distinct constant (1/2)(3 − 1/c\*₁) = 0.83625035183970582287… | **CHECKED NUMERICALLY** (mpmath, 80 digits) — `attack-realconstants.py` §A; consistent with paper (7.4), Thm D, Lean `Functional.lean` HD(1) (PROVEN there) |
| H(1) = 2/3 = 2 − 1/F(1) = 2 − 4/3; F(1) = 3/4; H_d(1) = 5/6; H(λ) = 2 − 1/λ − λ/3 strictly increasing on (0,1], max at λ=1; 2 − 1/c\*_λ nondecreasing in λ, max at λ=1 = 0.6725007 | **CHECKED NUMERICALLY** — `attack-realconstants.py` §B, B2 (grid λ = k/2000, k ≤ 2000); the H-monotonicity and c\* monotonicity are the reason **no λ ∈ (0,1] beats 0.6725** |
| λ₁ = λl/(l+c₀), c₀ = 2 log 2 − 1 = 0.3862943611198906…; H(λ) − H(λ₁) ≤ c₀/(λl) (Proof of Thm A) | **CHECKED NUMERICALLY** — §C (grid l ∈ {10..500}, λ ∈ {1/4,1/2,3/4,1}; max excess −6.4·10⁻⁵ < 0) |
| (5.2) Σ Λ(n)²/n = (log x)²/2 + O(log x); Σ (Λ(n)²/n)(log x − log n) = (log x)³/6 + O((log x)²) — constants 1/2 and 1/6 against actual prime-power data | **CHECKED NUMERICALLY** — §D (sieve to 10⁷: ratios 0.977→0.988 for 1/2-term, 0.952→0.972 for 1/6-term, errors O((log x)²) as claimed; constants 1/2, 1/6 are the exact PNT/Mertens limits, no slack) |
| Lemma 5.1 third line: Σ Λ(n)/√n ≤ 3√x is loose — true PNT asymptotic ≈ 2√x (measured 0.996–0.9995 of 2√x, slack 1.50×) | **CHECKED NUMERICALLY** — §E (sieve); the 3 is a crude universal constant, but the term it bounds (Π_X, O₂, cross terms) is o(main) |
| Σ Λ(n)² ≪ x log x (constant ~1; measured 0.912–0.938) | **CHECKED NUMERICALLY** — §E |
| E′_T (Thm 5.8): λ=1 → 0.0701 at T=10¹⁰, 0.0588 at 10¹², 0.0363 at 10²⁰, 0.0248 at 10³⁰ (≍ log l/l); λ=1/2 → 0.0944 at 10¹⁰ (≍ 1/l); BGSTB24 1/√log T = 0.2084 at T=10¹⁰ | **CHECKED NUMERICALLY** — §F (formula evaluation; the theorem's E′_T definition is PROVEN in the paper) |
| Irreducible finite-T floor ≈ w/L + log l/(2πl) at λ=1 (taper + bandwidth wall); perfect constant bookkeeping ≥ 0.0595 at T=10¹⁰ (vs 0.0701 actual); floor < 0.0058 only for l ≳ 300 (T ≳ 10¹³⁰) | **CHECKED NUMERICALLY** — §F decomposition (run in this round's transcript; formula-level, see §3.3) |
| M[P_X,P_X] main term T L³/6π = (T L/2π)(L²/3) (identity, 1/6 = (1/2)(1/3)); H(λ) = 2 − 1/F(λ); 1/F(λ) = 1/λ + λ/3; ∫₀¹(1−x)x dx = 1/6; law row-sum Σ (j/65536)(1−j/256) = 21845/131072; law E(1) = −1/(6·256²) | **CHECKED NUMERICALLY** — §G, I; law E(1) and row-sum independently **PROVEN** in `close-inclass-gap.md` via `tools/lpdual/verify_exact_cert.py` |
| MV 3π/2 (Lemma 5.2) is loose; sharp universal π; measured norm of the actual log-prime-power Hilbert matrix ≈ 2.5199 at N = 3·10⁴, saturated; sharpening has ZERO effect on 0.6725 | **CHECKED NUMERICALLY / PROVEN** — `attack-mvconstant.md` (parallel agent P7.1; Rust + numpy, dense SVD at N ≤ 10³; NOT re-derived here — used as delivered) |
| Remark 5.9 finite-T taper factor a²(1+λ₁²/3)/(b+λ₁²J_T): model reproduction (smoothstep ramp, w=1, actual primes, exact convolution g = ϕ²⋆ϕ²) gives 0.870 at L=4.4 (paper 0.89) and 0.974 at L=16 (paper 0.975); factor < 1 and → 1 like 1 − O(1/L) | **CHECKED NUMERICALLY (model)** — §H; the exact paper values depend on the unstated ramp ϱ of §2.2, so the 0.89/0.975 are reproduced only at the 2% level (INCONCLUSIVE as exact numbers; the qualitative claim is robust) |
| **The liminf 0.6725 is immovable by ANY constant bookkeeping of the existing inputs** | **PROVEN consequence** — every tightened constant (MV, Chebyshev–Mertens, end effects) sits inside o(1) error terms; the leading constant 2 − 1/c\*₁ is the exact optimum of the window problem (Thm D + [CCLM17, Cor. 14] = one-delta extremal, PROVEN in paper) |

---

## 1. The real-data certificate value v = p₁ + |E(1)| re-derived

### 1.1 What p₁(real) is (two-moment theorem) and what E(1)(real) is

**p₁(real)** — the certified proportion of simple on-line zeros. The paper's inputs (Thm 5.8) are the two
trace moments of the compression Ĝ in the units (4.4):

```
tr Ĝ  = N(T,2T)(1 + O(T^{λ/2−1}))                                  (Prop 5.3)
‖Ĝ‖²_F = tr Ĝ²/(aL)²  ≤  (1/λ₁ + λ₁/3)·N·(1 + O(E′_T))   flat-top   (Proof of Thm A)
        = N·(1/c*_{λ₁} + O(log l/l))                     optimised  (Proof of Thm D)
```

The rank–trace inequality (Lemma 3.2, PROVEN) gives, for simple zeros s₁,

```
s₁ ≥ 4N − 2N − ‖Ĝ‖²_F  =  (2 − 1/F(λ₁) − O(E′_T))N = (H(λ₁) − O(E′_T))N        flat-top
s₁ ≥ 4N − 2N − ‖Ĝ‖²_F  =  (2 − 1/c*_{λ₁} − O(E′_T))N = (0.6725 − O(E′_T))N      optimised (Thm D)
```

with H(λ₁) ≥ H(λ) − 1/(λl) (verified, §C). Hence **p₁(real) = 2/3 at λ=1 (Thm B, flat-top)** and
**p₁(real) = 2 − 1/c\*₁ = 0.6725 (Thm D, optimised window)** — both read ONLY the second moment ‖Ĝ‖²_F, i.e. the
mean-square pair-correlation datum ∫₋_λ^λ (λ−|α|)F(α)dα = λ + λ³/3, which Thm 5.8 (= BGSTB24 Thm 1, PROVEN)
evaluates unconditionally from the prime side.

**E(1)(real)** — the integrated-discrepancy term of the certificate. In the certificate/LP formalism
(`close-inclass-gap.md`, `attack-lpdual.md`) the value is v = p₁ + |E(1)| with E(1) the integrated discrepancy
of a **fixed-N configuration**. For the REAL zeros there is no fixed-N configuration: the proof is a T → ∞
statement, and the analogue of E(1) is the finite-T error in the evaluation,

```
E(1)(real)  ≈  −O(E′_T),   E′_T := w/L + (l²+X)log l/(T l) + T^{λ/2−1}   (Thm 5.8)
    λ=1 :  E′_T ≪ log l/l  =  O(log log T / log T)        [Thm A/B error budget]
    λ<1 :  E′_T ≪ w/L + T^{λ−1} log l  =  O(1/log T)      [Thm A/B error budget]
```

numerically ≈ 0.070 at T=10¹⁰, λ=1; ≈ 0.094 at T=10¹⁰, λ=1/2 (CHECKED, §F). Its **sign is unknown** — the
theorem needs only |error| ≤ c(λ)·E′_T. There is no fixed positive |E(1)| for the real zeros (unlike the 256-law's
E(1) = −1/(6·256²) exactly, PROVEN): the law's tiny discrepancy is a synthetic-configuration property, not a
real-zero fact.

**The BGSTB24 near-CUE error** (the other candidate the task asks about): BGSTB24 Thm 1 (PROVEN,
`baluyot-etal-2306.04799.txt` lines 49–57) states

```
F(α) = T^(−2α)(log T + O(1)) + α + O(1/√log T)   uniformly 0 ≤ α ≤ 1,
```

i.e. the zero-side form factor deviates from exact CUE by O(1/√log T) ≈ 0.2084 at T=10¹⁰ (CHECKED, §F). This is
the *interpretation-level* error; the paper's *evaluation-level* error is E′_T above (the prime-side mean-square
evaluation is exact; the form factor only reads the zero side). Both are o(1); neither can contribute a fixed
gain. The real zero configuration is ~10³⁹ times further from CUE than the 256-law (τ = 3·10⁻⁴⁰) at T=10¹⁰.

**So the honest real-data certificate value is**

```
v(real) = p₁(real) + E(1)(real)  =  2 − 1/c*₁  +  o(1)  =  0.6725007036794116…  (liminf, PROVEN Thm D),
```

where "E(1)(real) = o(1)" is the E′_T error (O(log log T/log T) at λ=1, O(1/log T) at λ<1), NOT the law's
fixed |E(1)| = 1/(6·256²) ≈ 2.54·10⁻⁶ (which would need a fixed-N real configuration with quantified
discrepancy — CONJECTURED/unavailable, see §5).

### 1.2 Reconciliation: where do 2/3 and 0.6725 come from in the REAL proof?

Both constants come from the **same single datum**, the second moment ‖Ĝ‖²_F, evaluated at the same prime-side
input; the difference is only which window ϕ is used:

| window | ‖Ĝ‖²_F / N (limit) | certificate 2 − 1/(that) | value |
|---|---|---|---|
| flat-top (Thm B) | 1/F(λ) = 1/λ + λ/3, F(1) = 3/4 | 2 − 1/F(1) = 2 − 4/3 = H(1) | **2/3** = 0.6666… |
| optimised cosine (Thm D) | 1/c\*₁, c\*₁ = 0.7532961 | 2 − 1/c\*₁ | **0.6725007…** |

c\*₁ is the maximum of the scale-free functional (7.3) over windows (Cauchy–Schwarz on the positive-definite
operator 1+λ²T, maximiser v\*(s) = cos(√2 s)); 1/c\*₁ = 1/2 + 2^(−1/2)cot(2^(−1/2)) = 1.3274993 (the task's
"c\*₁ = 1.3275" — note the constant that equals 1.3275 is **1/c\*₁**, while c\*₁ itself = 0.7533), and
2 − 1/c\*₁ = 3/2 − (1/√2)cot(1/√2) = **0.6725007**. The gain over the flat-top is c\*₁ − F(1) = 0.0033 in the
ratio, i.e. 0.5834 percentage points in the proportion. The paper cites [CCLM17, Cor. 14] (PROVEN) that the
cosine kernel solves the one-delta extremal problem given only F on [−1,1] — so 0.6725 is the exact limit of the
method "block structure + two traces + primes up to T", and **no window does better** (Thm D is the method
ceiling for the liminf). 2/3 is the flat-top sub-optimum; 0.6725 is the window-optimised optimum; both are
"real-data" in the sense of using only the unconditional two moments.

---

## 2. Constant audit table (every real constant, source, numeric check, slack)

All numerics in this table: `research/notes/attack-realconstants.py` (run
`cd /home/vstaln/riemann && uv run --quiet --with mpmath --with numpy python research/notes/attack-realconstants.py`;
36/36 checks pass), except the MV row, which is `attack-mvconstant.md` (parallel agent P7.1 — used, not
re-derived, per the task instruction).

| # | constant | source (paper) | numeric check | optimal as used? |
|---|---|---|---|---|
| 1 | c\*₁ = √2 tan(1/√2)/(1 + (1/√2)tan(1/√2)) = **0.75329606785607067722…** | (7.4), Thm D | 80-digit mpmath (§A) | **OPTIMAL** — window-max of (7.3); [CCLM17 Cor.14] one-delta extremal (PROVEN); Lean HD(1) |
| 2 | 1/c\*₁ = 1/2 + 2^(−1/2)cot(2^(−1/2)) = **1.3274992963205883543…** | Thm D proof | §A | OPTIMAL (same) |
| 3 | **2 − 1/c\*₁ = 3/2 − (1/√2)cot(1/√2) = 0.67250070367941164573…** | Thm D | §A | OPTIMAL — this is the liminf; see §3 |
| 4 | H(λ) = 2 − 1/λ − λ/3; H(1) = **2/3**; strictly increasing on (0,1] | (1.3), Thm A/B | §B (derivative + grid max) | OPTIMAL for the flat-top (H = 2 − 1/F, F from the exact second moment) |
| 5 | F(λ) = λ/(1+λ²/3); F(1) = **3/4**; 1/F(1) = 4/3; H = 2 − 1/F | (1.3), Thm 5.8 (5.13) | §G | OPTIMAL — exact second-moment main term |
| 6 | H_d(1) = **5/6**; Thm-D distinct constant (1/2)(3 − 1/c\*₁) = **0.83625035183970582287…** | (1.3), Thm C/D | §A, §B | OPTIMAL (same inputs) |
| 7 | λ₁ = λl/(l+c₀), c₀ = 2 log 2 − 1 = **0.3862943611198906…**; H(λ)−H(λ₁) ≤ c₀/(λl) < 1/(λl) | Proof of Thm A | §C (grid, max excess −6.4·10⁻⁵) | exact identity; bound used as stated |
| 8 | **Σ Λ(n)²/n = (log x)²/2 + O(log x)** | Lemma 5.1 (5.2) | §D (sieve 10⁵–10⁷: ratio→0.988, error O((log x)²)) | constant **1/2 exact** (PNT/Mertens); only the O(log x) implied constant is shaveable |
| 9 | **Σ (Λ(n)²/n)(log x − log n) = (log x)³/6 + O((log x)²)** | Lemma 5.1 (5.2) | §D (ratio→0.972, error O((log x)²)) | constant **1/6 exact** — the source of the L³/6 main term (= (TL/2π)(L²/3)); **no slack in the leading constant** |
| 10 | **Σ Λ(n)/√n ≤ 3√x** | Lemma 5.1, 3rd line | §E (sum ≈ 0.996–0.9995·2√x; 3√x has 1.50× slack) | **LOOSE (slack 1.5×)** — true ≈ 2√x (PNT); used for Π_X ≤ 6√X/T, O₂, cross terms — all o(main) |
| 11 | Σ Λ(n)² ≪ x log x (const ~1) | Lemma 5.1 | §E (measured 0.912–0.938·x log x) | constant ~1 fine; sharpening ~8% — inside o(1) |
| 12 | **MV Hilbert 3π/2 = 4.7124** | Lemma 5.2 | `attack-mvconstant.md`: sharp universal π; measured ‖∆H∆‖ ≈ **2.5199** for the actual log-prime-power frequencies (saturated at N=3·10⁴), factor 1.87 below 3π/2 | **LOOSE** (paper itself: "any absolute constant would suffice"); enters ONLY O₁ ≪ L²X (off-diagonal), o(main); sharpening changes the certificate value **not at all** |
| 13 | δₙ⁻¹ ≤ 2n (min gap of log-prime-powers) | (5.3) | — | slack: true gap constant ~1 for large n; factor 2 inside O₁'s constant — o(1) |
| 14 | |α±ₙ| ≤ πL (Fourier amplitude bound) | Prop 5.6 (O₁) | universal bound; sharp constant irrelevant — o(1) |
| 15 | E′_T = w/L + (l²+X)log l/(Tl) + T^{λ/2−1}; λ=1: ≪ log l/l; λ<1: ≪ 1/l | Thm 5.8 | §F (0.0701 at T=10¹⁰ λ=1; 0.0944 at λ=1/2) | shape **exact**; implied constant improvable ~2× via rows 10, 12, 13 — see §3.3 |
| 16 | tr eG² error O(L l log l (l²+X)) (end effects L³B²logL, O₁≪L²X, O₂≪XL, cross ≪ l√X, lL√X, LX, LX/T) | Lemma 5.4, Props 5.5–5.7 | §F (decomposition) | bookkeeping bounds; the (l²+X)log l shape is set by the bandwidth wall X=T^λ and the taper — **not** removable by constants |
| 17 | Remark 5.9 taper factor a²(1+λ₁²/3)/(b+λ₁²J_T): paper says 0.89 (L=4.4), 0.975 (L=16) | Remark 5.9, (7.2) | §H: model reproduction **0.870 / 0.974** (smoothstep ramp, w=1, exact convolution g, actual primes) | factor < 1, → 1 like 1 − O(1/L); exact values ramp-dependent (INCONCLUSIVE at the 2% level); a MAIN-term finite-T effect, not improvable by constants |
| 18 | (5.2) second-moment main term M[P_X,P_X] = T L³/6π = (TL/2π)(L²/3); ∫₀¹(1−x)x dx = 1/6; law row-sum 21845/131072; law E(1) = −1/(6·256²) | Prop 5.6, close-inclass-gap.md | §G, §I | 1/6 exact; law E(1) PROVEN separately (`tools/lpdual/verify_exact_cert.py`) |

**Audit summary.** The constants that determine the *leading* real constant are all exact/optimal: 1/2 and 1/6 in
the Chebyshev–Mertens main terms (rows 8–9), F(1) = 3/4 and H(1) = 2/3 (rows 4–5), and c\*₁ (row 1). Every
constant with genuine slack (rows 10, 12, 13, 15-implied) sits inside an **o(main)** error term: Π_X-terms
≪ l√X, off-diagonal O₁ ≪ L²X, O₂ ≪ XL, cross terms, and end effects — each vanishing relative to
TL³/6π + bLTℓ₁²/2π as T → ∞. None of them can change the liminf.

---

## 3. Best real-data constant with the paper's own inputs

### 3.1 (a) Under the paper's constants
p₁(real) = 2 − 1/c\*₁ = **0.6725007036794116** (Thm D, PROVEN); finite-T value = 2 − 1/c\*_{λ₁} − O(E′_T) with
c\*_{λ₁} = c\*₁ + O(1/l). **No λ ∈ (0,1] beats 0.6725**: 2 − 1/c\*_λ is nondecreasing in λ with maximum at λ=1
(CHECKED, §B2), and H(λ) ≤ 2/3 for all λ (CHECKED, §B). The distinct-zeros branch gives 0.83625 (Thm D),
similarly max at λ=1.

### 3.2 (b) Under the tightenings (MV 3π/2 → π/2.52; CM 3√x → 2√x; δ⁻¹ ≤ 2n → ~1/n; sharper Lemma 5.4 bookkeeping)
Every tightening lands in an o(1) error term; the certificate value 2 − 1/c\*₁ is **unchanged to all digits**.
The only visible effect is on the implied constant c(λ) of the finite-T error term (Thm A/B):
c(λ)·log log T/log T (λ=1), c(λ)/log T (λ<1). Quantified (CHECKED, §F decomposition): at T=10¹⁰, λ=1,
E′_T = 0.0701 = 0.0472 (taper w/L, **irreducible**) + 0.0229 (bandwidth wall; MV sharpening 3π/2 → 2.52 buys
≤ 1.87×, i.e. ≤ 0.0123) + 10⁻⁵ (power). Even with **perfect** constants the finite-T error is ≥ 0.0595 at
T=10¹⁰ — still 10× the window-gain 0.0058 over 2/3 and 6× the 0.0093 gap to the law ceiling 0.68183. The error
drops below the 0.0058 window gain only at l ≳ 300, i.e. T ≳ 10¹³⁰. **Tightening constants therefore moves
nothing that matters; it is a constant-factor shave of an already-o(1) term.**

### 3.3 Reconciliation of "2/3 vs 0.6725" and of "0.6725 vs 0.6818"
- **2/3 vs 0.6725 (real proof):** same second-moment input, different window; 2/3 = 2 − 1/F(1) (flat-top,
  F(1) = 3/4), 0.6725 = 2 − 1/c\*₁ (optimised window, c\*₁ = 0.7533 > 3/4). Both are liminf statements with
  o(1) error; 0.6725 is the method's window optimum (PROVEN).
- **0.6725 vs 0.6818 (law vs real):** 0.6818 = p₀ + |E(1)| is the **256-law** certificate value
  (`close-inclass-gap.md`, PROVEN up to τ-terms; p₀ = 0.6818287 is the law's simple fraction, E(1) = −1/(6·256²)).
  It is NOT a certified real-zero constant: it needs the law's exact N=256 configuration and its τ = 3·10⁻⁴⁰
  near-CUE row bounds, while the real zeros have only the mean-square two-moment control with error
  O(1/√log T) ≈ 0.21 ≫ τ (CHECKED, §F). The 0.6725 → 0.6818 gap is closed **in-class** (LP: r = 1−x attains the
  ceiling, `attack-lpdual.md`), **not for real zeros**.

---

## 4. Bottom line: can the real lower bound move with existing inputs?

**The liminf: NO.** v(real) = 2 − 1/c\*₁ = 0.6725007 is the exact optimum of the method given the two trace
moments and the window constraints (Thm D; [CCLM17, Cor. 14], PROVEN). Every constant with slack (MV 3π/2,
Chebyshev–Mertens 3√x, δ⁻¹ ≤ 2n, end-effect bookkeeping) is inside an o(1) error term; sharpening any of them
cannot change a liminf, and numerically the certificate constant is unchanged to all digits under every
tightening in §2/§3.2.

**The finite-T error term: YES, but by at most ~2× and it never matters.** The implied constant c(λ) in
H(λ) − c(λ)·log log T/log T (λ=1) can be shaved ~1.5–2× by combining the MV and Chebyshev–Mertens tightenings,
but the *shape* of the error (log log T/log T at λ=1; 1/log T at λ<1) is fixed by the bandwidth wall X = (T/2π)^λ
and the taper — it is not a bookkeeping artifact. And the irreducible floor (taper + wall) ≥ 0.0595 at T=10¹⁰
(§3.2) is 10× larger than the 0.0058 window-gain over 2/3; the finite-T statement cannot even certify more than
2/3 at any computationally accessible height, with or without tightened constants (Remark 5.9: the finite-T
ratio stays below F(λ) at all accessible heights — confirmed by the 0.87–0.97 taper factor, §H).

**What would move the real lower bound (shadow price 1, per `attack-lpdual.md`):** a beyond-bandwidth-1
pair-correlation datum (F(α) for α > 1 — equivalent to Hardy–Littlewood prime-pair estimates, CONJECTURED) or a
proven multiplicity bound excluding the 256-law shape; each unit of certified real simple fraction transfers 1:1
into the constant. Neither exists in the verified literature (`attack-ceiling.md` §3).

---

## 5. What would change what we believe

- **Would strengthen:** (i) a proven bound on F(α) for some α > 1 or a multiplicity bound — the only input with
  shadow price 1 (CONJECTURED); (ii) a quantified uniform near-CUE row bound for the real zeros at fixed N
  (currently only mean-square O(1/√log T)); (iii) writing the "box lemma" of `close-inclass-gap.md` (removes the
  last 7.8·10⁻⁴³ sliver of the *law* ceiling — does not touch the real constant).
- **Would undermine the "immovable" claim:** any demonstration that Theorem D is not the true window optimum
  given F on [−1,1] — i.e., a violation of [CCLM17, Cor. 14]'s extremal-role statement; or an error in the
  second-moment main term (1/6, 2/3, 4/3 constants), which the numerical checks in §D/§G/§I and the paper's own
  Appendix B (symbolic + zero-side agreement 10⁻⁶–10⁻⁸) do not indicate.
- **Resolved out-of-scope:** the exact 0.89/0.975 numbers of Remark 5.9 require the paper's unstated ramp ϱ
  (reproduced here at the 2% level with a smoothstep ramp; qualitative claim robust). The MV sharp constant for
  the actual frequencies is CONJECTURED ∈ (2.5, π], consistent with the saturated measurement ≈ 2.5199
  (`attack-mvconstant.md`).

**Label for the headline claim:** real-data certificate value v(real) = 2 − 1/c\*₁ + o(1) = **0.6725007036794116**
— PROVEN (Theorem D; window optimality [CCLM17, Cor. 14]); immovable by constant bookkeeping of the same inputs —
PROVEN (all slack constants are o(1); finite-T floor computed); finite-T error improvable by ≤ ~2× (MV + CM
tightenings) — CHECKED NUMERICALLY (this note's script); the 2/3 ↔ 0.6725 reconciliation — CHECKED NUMERICALLY
(§B, §G; both = 2 − 1/ratio of the same second moment).

---

## 6. Scripts and provenance

- **`research/notes/attack-realconstants.py`** (self-contained; also at `scratch/realconst/verify_realconstants.py`):
  every number in §A–§I of this note. Run: `cd /home/vstaln/riemann && uv run --quiet --with mpmath --with numpy python research/notes/attack-realconstants.py`.
  36/36 checks pass. Sections: A (Thm D constants, 80-digit), B/B2 (H, c\*_λ optimality over λ ∈ (0,1]),
  C (λ₁ correction), D (Chebyshev–Mertens 1/2, 1/6 vs sieve data to 10⁷), E (3√x slack vs true 2√x), F (E′_T and
  BGSTB24 error at sample heights + irreducible-floor decomposition), G (main-term identities), H (Remark 5.9
  taper factor reproduction), I (1/6 and law E(1) arithmetic).
- **`attack-mvconstant.md`** (parallel agent P7.1): MV 3π/2 loose, sharp π, measured ≈ 2.5199, zero effect on
  0.6725 — used as delivered, not duplicated.
- **`close-inclass-gap.md`, `attack-lpdual.md`**: law certificate v = p₀ + |E(1)| = 0.68183123 (PROVEN up to
  τ-terms), in-class closure, shadow-price-1 levers — used for §1/§4.
- **Primary sources:** `claude-riemann-paper.txt` (Thm 5.8, Lemma 5.1/5.2, Thm A–D, Remark 5.9, §7.1),
  `baluyot-etal-2306.04799.txt` (Thm 1: F(α) = α + O(1/√log T)).
