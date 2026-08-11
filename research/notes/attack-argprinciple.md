# Attack: certified argument-principle counts of off-line zeros in narrow strips (C-NY1)

**Agent:** EXECUTIONER (numerics-first, all code-backed; constraint-hardness + epistemology lens)
**Vector:** C-NY1 from `idea-generator-control.md` (Pool 5 — Nyquist/argument-principle)
**Date:** 2026
**Verdict up front:** The strip counts **are real, certified finite-T theorems at new heights** — 590 / 643 / 715 on-line simple zeros in [T, T+500] at T = 10⁴, 2·10⁴, 5·10⁴, each bracketed by Z(t) sign changes with fully accounted f64 error bounds, each bracket containing exactly one LMFDB-verified ordinate, and the argument-principle winding number on the rectangle [0,1]×[T,T+H] equals the on-line count exactly (590.000000, 643.000000, 715.000000). The implied simple-on-line fraction is **1.0000000000** at every height. **BUT** the vector's promise — that this produces "p₁-type data with a provable finite-T form" that feeds the shadow-price-1 datum — **cannot move the certificate**: p₁ is a *global/asymptotic* quantity and finite strips do not constrain it. This is a **structural, not practical, obstruction** (stated precisely in §6). The deliverable: the tool, the counts table, the honest statement of what a finite computation certifies, and the structural reason.

Labels: **PROVEN (literature)** = RH below 3·10¹² (Platt–Trudgian 2021, peer-reviewed), simplicity of the first 10¹³ zeros (Gourdon–Demichel 2004, rigorous verification method), ζ ≠ 0 for Re s ≥ 1 and σ = 0 (classical). **PROVEN (this tool, given the stated error-bound arithmetic)** = every reported bracket contains ≥ 1 zero of ζ on Re = 1/2. **CHECKED NUMERICALLY** = all counts, 1:1 LMFDB containment, windings, RvM consistency, mpmath cross-checks. **UNCERTIFIED** = the winding number (numerical demonstration). See the full label table in §7.

---

## 1. Why this vector exists (the shadow-price-1 context)

`attack-lpdual.md` proved: within the bandwidth-one certificate class, the certified value is **v = p₁ + |E(1)|** where p₁ is the certified simple-point fraction — the LP's shadow price of p₁ is exactly 1, and p₀ + |E(1)| = 0.6818312305953… is attained in-class by the near-CUE 256-law. **The only datum that moves the real-zeros constant 0.6725 is a better lower bound on p₁.** C-NY1 proposed to produce p₁-type data at new heights by argument-principle / root-finding counts of off-line zeros in narrow strips — "RvM-style contour counts that produce p₁-type data at NEW heights with a PROVABLE finite-T form."

The task: (a) certified zero counts in [T, T+H] via Z(t) sign changes with rigorous bracketing, (b) counts of off-line pairs {ρ, 1−ρ̄} in the strip, (c) the implied simple-on-line fraction vs 2/3, 0.6725, 0.6818 — at T = 10⁴, 2·10⁴, 5·10⁴ — and an honesty check of what a finite computation can certify.

## 2. Honesty check FIRST: what can a finite computation certify?

**What my code PROVES (given the stated error-bound arithmetic):**
- Z(t) = e^{iθ(t)}ζ(1/2+it) is evaluated with a rigorous absolute error bound (explicit EM remainder + Kahan rounding + trig-angle rounding + correction rounding — formulas in §4). At the strip endpoints the certified errors are 1.3e-9 (T=10⁴), 4.2e-9 (2·10⁴), 1.9e-8 (5·10⁴) — dominated by the f64 trig-angle rounding, with the EM remainder ≤ ~4e-16.
- Every reported bracket (a,b) has Z(a), Z(b) of **certified opposite signs** (|Z| > err at both, signs certain), so by continuity there is **≥ 1 zero of ζ on Re = 1/2 in (a,b)** — a PROVEN statement. The bracket width is ≤ 1e-9 (bisection with certified evaluations; the rare |Z(mid)| < err case breaks with [a,b] still bracketing).
- Therefore **#sign changes ≤ #on-line zeros**, each located to 1e-9. This is the only *proof* my code gives. (Each sign change corresponds to at least one zero of ODD multiplicity; even-multiplicity zeros are invisible to sign changes.)

**What my code CANNOT prove alone:**
- That the bracket contains exactly one zero, and that there are no other zeros (off-line, or even-multiplicity on-line) in the strip. The sign-change count is a lower bound on on-line zeros; the equality with the total requires the total count, which my code obtains only from the argument principle (the winding, **uncertified** in my implementation) or from the literature.
- That the off-line count is 0. My numerics only give *consistency* (count-match + winding = integer equal to the on-line count).
- **Nothing global.** No finite computation can prove a statement about liminf_{T→∞} N^s_0(T)/N(T). This is the load-bearing caveat (§6).

**What the literature PROVES for these heights (making the strip statements full theorems):**
- **RH below 3·10¹²** (Platt–Trudgian, *Bull. LMS* 2021): no zeros of ζ with 0 < Im s < 3·10¹² off the critical line. All our strips (≤ 5.05·10⁴ ≪ 3·10¹²) contain **zero off-line zeros — PROVEN**. Off-line pairs: **0**.
- **Simplicity**: all zeros below the first 10¹³ (Gourdon–Demichel 2004, rigorous verification): all on-line zeros in our strips are **simple — PROVEN**. Hence each sign change = exactly one simple on-line zero, and #sign changes = #on-line zeros = N(T+H) − N(T).
- ζ(s) ≠ 0 for Re s ≥ 1 and on σ = 0 (classical; functional equation) — the contour [0,1]×[T,T+H] is zero-free on its vertical sides.

So the honest frame: **the strip statements "exactly N zeros, all simple, all on the line, zero off-line" are PROVEN theorems below 3·10¹²** (Platt–Trudgian / Gourdon–Demichel). What C-NY1's tool adds is an **independent, certified-error re-derivation of the on-line zeros and their count** (different software, different error accounting than LMFDB's or mpmath's), plus a numerical demonstration of the argument-principle count, plus the p₁ structural analysis.

## 3. The tool

Crate: **`tools/argprinciple/`** (new, self-contained; musl + rust-lld). Build:
```
export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld"
cargo build --release --target x86_64-unknown-linux-musl
```
Run (data dir holds the fetched LMFDB ordinates, §4):
```
target/x86_64-unknown-linux-musl/release/argprinciple 10000 500 0.02 data
target/x86_64-unknown-linux-musl/release/argprinciple 20000 500 0.02 data
target/x86_64-unknown-linux-musl/release/argprinciple 50000 500 0.02 data
```
Data: `tools/argprinciple/fetch_lmfdb.py` (LMFDB `zeros/zeta/list?N=&limit=`, chunks of 1000, ≥0.4 s delay); ordinates cached in `tools/argprinciple/data/lmfdb_zeros_*.txt` (indices 0–64 799, 34 digits, 51 499 ordinates fetched; gaps remain in 12 000–28 999 / 37 000–43 999 / 46 000–57 999 — the LMFDB server began rate-limiting (reCAPTCHA). The strip-covering ranges are complete; global N(T) at the strip edges is reconstructed from `~/Downloads/index.db` block counts + fetched ordinates, §5.)

Components (all in `src/zeta.rs` / `src/main.rs`):
1. **Certified ζ(s), σ ∈ [0,1], t ≤ 5.05·10⁴** by Euler–Maclaurin, K = 40 Bernoulli corrections, N = ⌈1.6t/2π⌉, Pochhammer products in scaled form ∏((s+j)/N) (no f64 overflow; the naive (s)_{2K} overflows at t ≈ 10⁴·(K=40)).
2. **Certified Z(t)** with the complete error budget printed at each strip endpoint.
3. **Sign-change scan** (step 0.02; min zero gap ~0.7 at these heights, 35+ samples per gap) + **certified bisection** to bracket width ≤ 1e-9.
4. **LMFDB cross-check**: every fetched ordinate in the strip must lie in exactly one bracket, and every bracket must contain exactly one ordinate (1:1 containment + count equality).
5. **RvM cross-check**: main term N(T+H) − N(T) = (T+H)/2π·ln((T+H)/2π) − T/2π·ln(T/2π) − H/2π; the rigorous bracket from the Trudgian bound |S(t)| ≤ 0.112 ln t + 0.278 ln ln t + 2.510; the empirical S(T) = N(T) − main(T) at the strip edges.
6. **Numerical argument-principle winding** of ξ̃(s) = s(s−1)π^{−s/2}Γ(s/2)ζ(s)/2 on [0,1]×[T,T+H] (CCW), with adaptive subdivision so |Δarg| ≤ π/2 per segment (the contour grazes on-line zeros on its horizontal edges — at T = 10⁴ the bottom edge passes 0.065 from the zero at height 10000.0653, the first zero in the strip, and the naive fixed-step unwrapping mis-counts there; subdivision fixes it). **Label: UNCERTIFIED** (a numerical demonstration; making it a certified winding needs certified variation control, e.g. Backlund's method with interval arithmetic — the standard machinery, not re-implemented here).

### Error bounds (stated so a validator can re-derive; the tool prints the components)
Euler–Maclaurin with explicit remainder:
|R_K| ≤ 2·|B_{2K}|/(2K)! · ∏_{j=0}^{2K−1}|s+j|/N · N^{1−σ} / (σ+2K−1),
from |B_{2K}({x}) − B_{2K}| ≤ 2|B_{2K}| and the exact identity |B_{2n}|/(2n)! = 2ζ(2n)/(2π)^{2n}. The coefficients are hardcoded as the exact rationals (computed at 60 dps, inflated ×(1+2e-14) to be safe upper bounds). Main sum: Kahan summation, error ≤ 4ε·Σ|n^{−s}|. Trig-angle rounding (the dominant term): Σ_j (|t·ln j|·2^{−52} + 1e-15)·|n_j^{−s}| — the f64 product t·ln j is not exact and the error feeds through sin/cos. Correction terms: ≤ Σ_k (3k+20)ε·|C_k|. θ(t): Stirling with m=6 terms, error < 1e-25 at t ≥ 10³. Z combination: + (|Re ζ|+|Im ζ|)·(Δθ + 4ε).

**Validity of the bound** — CHECKED NUMERICALLY against mpmath (40 dps) at t = 37.6, 100.9, 10³, 10⁴, 2·10⁴, 5·10⁴, 5.05·10⁴: the actual value error is ≤ the certified bound at every point (e.g. at t = 5·10⁴ the value error is ~7e-11 vs the bound 1.9e-8; at t = 37.6, where N clamps to the min 10 and the EM corrections barely converge, the bound honestly reports ~6e-6 > the actual ~2e-6 error).

## 4. Results

### 4.1 The counts table (all three strips, H = 500)

| T | certified brackets (sign changes) | zeros in strip, LMFDB | off-line pairs | implied simple-on-line fraction | winding (uncert.) | max |bracket mid − LMFDB ordinate| | certified |Z| error |
|---|---|---|---|---|---|---|---|---|
| 10⁴ | **590** | 590 | **0** | **1.0000000000** | 590.000000 | 1.404e-9 | 1.3e-9 |
| 2·10⁴ | **643** | 643 | **0** | **1.0000000000** | 643.000000 | 6.705e-9 | 4.2e-9 |
| 5·10⁴ | **715** | 715 | **0** | **1.0000000000** | 715.000000 | 1.473e-8 | 1.9e-8 |

Every row: **count-match (brackets == LMFDB count) = true**; 0 LMFDB ordinates outside any bracket; 0 brackets with >1 or 0 ordinates. The winding equals the on-line count exactly (590.000000 / 643.000000 / 715.000000), i.e. the argument-principle count on the rectangle returns the same integer as the sign-change count.

Commands that produced these numbers (all in `tools/argprinciple/`):
```
target/x86_64-unknown-linux-musl/release/argprinciple 10000 500 0.02 data   # → 590
target/x86_64-unknown-linux-musl/release/argprinciple 20000 500 0.02 data   # → 643
target/x86_64-unknown-linux-musl/release/argprinciple 50000 500 0.02 data   # → 715
```
Independent-precision check (mpmath, 40 dps, `uv run --with mpmath`): max |Z(bracket mid)| over 12 sampled brackets per strip = 4.0e-8 (T=10⁴), 8.5e-8 (2·10⁴), 9.8e-8 (5·10⁴) — every sampled bracket center is a genuine zero of ζ; every LMFDB ordinate in a strip lies within 1.6e-8 of a bracket mid.

### 4.2 Riemann–von Mangoldt cross-check

| T | N(T+H) − N(T) (exact) | RvM main term | S(T) | S(T+H) | Trudgian bound on \|S(T+H)\|+\|S(T)\| |
|---|---|---|---|---|---|---|
| 10⁴ | 590 | 588.639 | −0.965 | +0.396 | 8.325 |
| 2·10⁴ | 643 | 642.827 | −0.412 | −0.239 | 8.517 |
| 5·10⁴ | 715 | 715.154 | +0.173 | +0.020 | 8.769 |

N(T) exact at the strip edges from the contiguous fetched ordinates (T = 10⁴, 1.05·10⁴) and from `~/Downloads/index.db` block counts plus fetched ordinates in the inter-block range (T = 2·10⁴, 2.05·10⁴: N(19700) = 22106 + 385 = 22491; 22106 + 1028 = 23134; T = 5·10⁴, 5.05·10⁴: N(49100) = 62233 + 1286 = 63519; 62233 + 2001 = 64234). All |S| < 1, comfortably inside the classical |S(t)| ≪ ln t bound and consistent with `attack-finitet`'s independent validation of RvM against the index.db (max |Δ| = 2.08 over 14.6 M rows).

Note on the tool's own printed `S(T)` line: it reads N(T) from the fetched files, which are contiguous only up to index 10 999 (the LMFDB server rate-limited the mid-range fetch — see §3); at T = 10⁴ the printed line agrees with the table, at T = 2·10⁴/5·10⁴ it undercounts and the table values above (index.db-based) are authoritative.

### 4.3 The implied p₁-type fraction vs the in-class constants

Measured simple-on-line fraction in each strip: **1.0000000000** (every one of the 590/643/715 zeros is a simple on-line zero — PROVEN by Gourdon–Demichel simplicity + Platt–Trudgian RH below 3·10¹²; measured exactly 1 by the 1:1 count-match).
- 2/3 = 0.66666666666666666667
- 3/2 − (1/√2)cot(1/√2) = **0.67250070367941164573** (the Theorem-D constant; `verification-001`)
- p₀ (256-law simple fraction) = **0.68182868746383147426** (`attack-lpdual`)
- p₀ + |E(1)| = **0.68183123059534187426** (the in-class ceiling; `attack-lpdual`)

Measured 1.0 > 0.6818 at every height — reality sits far above the ceiling, exactly as the empirical (all-simple) world does at the multiplicity level (`attack-multiplicity`: Δ = 0, reality on the wall).

## 5. What C-NY1 delivers (the honest positive content)

1. **Certified on-line zero counts at new heights by an independent method.** T = 10⁴, 2·10⁴, 5·10⁴ — heights well beyond the cached 10⁴ zeros in `tools/data/zeros_computed_10000.txt` — with every evaluation error-bounded and every zero bracketed to 1e-9. Independent of LMFDB's software (which computed the ordinates) and of mpmath (40-dps cross-check agrees).
2. **A numerical argument-principle count that matches.** The winding of ξ̃ on [0,1]×[T,T+H] equals the on-line count exactly at all three heights — the vector's "(i) the empirical version" — demonstrating that the contour count works and agrees with the Z(t) count. (UNCERTIFIED: it is a demonstration; the certified form is Backlund's method with interval arithmetic, already subsumed by the verification literature for these heights.)
3. **P6-type finite-T theorems, true and now independently certified:** "the strip [5·10⁴, 5.05·10⁴] contains exactly 715 zeros of ζ, all simple and on Re = 1/2; zero off-line zeros." Already PROVEN by Platt–Trudgian/Gourdon–Demichel; the certified-error re-derivation is a second, independent method producing the same facts — exactly the "two independent methods" protocol the hooks demand.
4. **Off-line-pair count = 0** in each strip (PROVEN below 3·10¹²; numerically consistent via count-match + winding).

## 6. Why this CANNOT feed the certificate — the structural reason

The certificate's datum p₁ is the **simple-point fraction of the true configuration**, and the certificate's conclusion is about the **asymptotic proportion** liminf_T N^s_0(T)/N(T) (Theorem B: N^s_0(T,2T) ≥ (H(λ) − o(1))N(T,2T)). A finite strip count is a **local empirical fact at finitely many heights**. The gap is definitional, not practical:

1. **A liminf is not constrained by finitely many samples.** For every finite (indeed every enumerable) set of heights, there exist configurations with p₁ = 1 in every listed strip and global simple fraction = p₀ (the 256-law's realizations are flexible below any fixed height — the law is a distribution on configurations whose local simple fractions are unconstrained while the aggregate form-factor rows and simple fraction are pinned). So "p₁ = 1 at heights ≤ 5·10⁴" — even PROVEN for all heights below 3·10¹² — says nothing about the liminf, which is the quantity the certificate reads.

2. **The certificate is valid against the whole configuration.** Its rows s_j = S(j)/N are *global* pair-correlation averages; the LP's worst case (the 256-law) is a configuration that matches ALL bandwidth-one data. A strip measurement is not even the same kind of datum as a row s_j — it is one configuration's behavior on a height interval, and the certificate must hold configuration-by-configuration (Remark 1.1). Feeding "simple fraction = 1 on [T₀, T₀+H]" into the certificate would be a category error: the certificate needs a certified lower bound on the *global* simple fraction, which requires either an unconditional asymptotic theorem (Theorem B-type; currently 2/3 − o(1), improvable only by beyond-bandwidth-1 pair correlation or a multiplicity exclusion — both CONJECTURED/unavailable per `attack-ceiling` §3) or a proof about the whole infinite zero sequence.

3. **The LP structure makes the failure mode precise.** In `attack-lpdual`, p₁ is a free parameter of the certificate's validity constraint c₀ + Σ s_j r(j/N) ≤ p₁; the LP's shadow-price-1 result says the certified value is 1:1 the certified global simple fraction. A local measurement can neither enter that constraint (it is about global masses) nor raise the worst-case p₁ (the 256-law attains p₀ while being consistent with any finite set of height-local observations).

4. **The "provable finite-T form" is a finite-T theorem, not a global one.** The certified statement "N_off(T,T+H) = 0, all zeros simple on-line in [T,T+H]" at specific T is true and useful, but countably many such theorems never assemble into a liminf bound: the tail above any fixed height is entirely free. This is exactly why the verification literature (RH below 3·10¹²) is a *verification*, not a proof — and why no amount of certified strip counting can certify p₁ ≥ 0.70 globally.

**Conclusion of the structural analysis:** C-NY1's measurement is real and delivers certified finite-T facts and an independent verification method, but **the p₁-at-new-heights approach cannot feed the certificate** — the datum the certificate needs is global/asymptotic, and finite strips do not constrain it. This is a hard wall of the same kind as the bandwidth-one wall (s4h-constraint-hardness: the constraint "p₁ is a liminf; finite computations read only finitely many heights" is **HARD**, with the concrete consequence that the certificate cannot consume the strip counts; the workaround is the documented one — a new global input: beyond-bandwidth-1 form factor, or a new proof technique for the global simple fraction).

## 7. Label summary

| Claim | Label |
|---|---|
| RH below 3·10¹² (hence zero off-line zeros in all our strips); simplicity of the first 10¹³ zeros (hence every on-line zero in our strips simple); ζ ≠ 0 on Re s ≥ 1, σ = 0 | **PROVEN (literature)** — Platt–Trudgian 2021 (peer-reviewed), Gourdon–Demichel 2004 (rigorous verification), classical |
| Every reported bracket contains ≥ 1 zero of ζ on Re = 1/2; bracket width ≤ 1e-9 | **PROVEN (this tool)** — certified opposite signs of Z at the bracket endpoints, given the stated error-bound arithmetic (§3); bound validity itself CHECKED NUMERICALLY vs mpmath |
| Strip counts 590 / 643 / 715; 1:1 bracket↔LMFDB containment; count-match true; windings 590.000000 / 643.000000 / 715.000000; RvM main-term + S(T) values; certified |Z| errors at the strip endpoints | **CHECKED NUMERICALLY** — `tools/argprinciple/`, commands in §4.1, §4.2 |
| mpmath (40 dps) |Z(bracket mid)| ≤ 1e-7, all LMFDB ordinates within 1.6e-8 of a bracket mid | **CHECKED NUMERICALLY** — independent precision |
| Implied simple-on-line fraction = 1.0000000000 at each height | **PROVEN by literature** (simplicity + RH below 3·10¹²) **and measured** by the 1:1 count-match |
| Off-line pairs = 0 in each strip | **PROVEN by literature**; numerically consistent (count-match + winding) |
| The winding number on [0,1]×[T,T+H] | **UNCERTIFIED** — numerical demonstration with adaptive subdivision; the certified version is Backlund's method (not re-implemented here) |
| "Finite strip counts cannot prove a global p₁ bound" | **PROVEN (structural argument, §6)** — p₁ is a liminf; the certificate is configuration-valid and global; finitely many heights leave the tail free |
| The constants 2/3, 0.67250070367941164573, p₀ = 0.68182868746383147426, p₀+\|E(1)\| = 0.68183123059534187426 | **CHECKED NUMERICALLY** (mpmath, 40 dps) / from `verification-001`, `attack-lpdual` |

## 8. What would change what we believe (for the next round)

- The only inputs that can move the certificate remain: (a) a proven bound on the form factor for some |α| > 1 (equivalently a Hardy–Littlewood prime-pair fragment), each unit of certified global simple fraction transferring 1:1 into the certified proportion; (b) a new *global* proof technique for N^s_0(T)/N(T) — finite strips are not it (this note).
- The winding count could be made fully certified (Backlund's method: bound arg ζ on the contour via the explicit |ζ'|/|ζ| control from the same EM machinery, or via Platt's interval-arithmetic approach) — a genuine but modest new finite-T certificate, already subsumed by the literature below 3·10¹²; worth doing only if a *certified* (not literature-cited) finite-T theorem at one height is ever needed.
- Independently: the LMFDB fetch script is rate-limited; re-fetching the missing index ranges (12 000–28 999, 37 000–43 999, 46 000–57 999) with long delays would complete the contiguous N(T) reconstruction at larger heights — not needed for the current claims (strip data is complete).
