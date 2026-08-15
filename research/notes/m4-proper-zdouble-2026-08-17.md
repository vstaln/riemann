# M4-proper: mechanical re-derivation of BHB Lemma 1 with ζ′ → ζ″ (the r′ pin)

**Agent:** builder (IDEA/ATTEMPT probe, background). **Date:** 2026-08-17.
**Model:** opencode-go/deepseek-v4-flash. **Task:** pin r′ in the box form E/S₂ ≤ 8b²(r+r′)
by re-deriving the ζ″-analogue of BHB Lemma 1 (arXiv:1302.5018). **Method:** closed-form
residue algebra + one Rust probe. **Sources:** bhb-m6-synthesis-2026-08-14.md,
bhb-adversarial-validator-af-2026-08-17.md, bhb-zeta2-moment-2026-08-14.md,
bhb-lemmaN-firstcheck-2026-08-14.md (all read this session).

## 0. Verdict (one line each)

- **r′ ≥ 0: PROVEN** (positivity: M = Σ|Bζ″(ρ)|² ≥ 0 pointwise and M ~ (T/2π)ℒ⁵·c(M) ⟹ c(M) ≥ 0, c(S₂) = 57/64 > 0).
- **r′ = 3/5: REFUTED, twice.** (i) anchor dead: the un-mollified ζ″-moment is **ℒ⁶-scale, not ℒ⁵**; (ii) the 1/(2k+1) pattern is false (k=1 gives Gonek's 1/12, not 1/3).
- **r′ VALUE: NOT PINNED by this route.** The pin needs the ℳ₂,₁^ζ″-evaluation — a (log n)⁴-weighted character-sum computation not in 1302.5018 and not closed-form-accessible from its quoted constants.
- **Forecast outcome (b) (r′ ≤ 0 breaks the quadratic form): IMPOSSIBLE** (PROVEN by positivity). Forecast outcome (a) (lever closed): CONFIRMED.
- **Box ceiling b_pair ≤ 0.2237 (ζ″-free): STANDS, PROVEN.** b ≈ 0.0758 (r′ = 3/5): DEAD. The box route cannot reach below 0.2237 without a paper-length computation or a new moment input.

## 1. Setup and the exact route (PROVEN)

BHB Lemma 1 (verbatim, 1302.5018): S₂ := Σ_{0<γ≤T} Bζ′(ρ)·Bζ′(1−ρ) = (T/2π)L³(½ + 3ϑ∫P²) − 2Re(ℳ₂) + error,
ℳ_ν = Σ_{k≤y}Σ_{m≤kT/2π} a_ν(m)b(k)/k·e(−m/k), ζ′/ζ·ζ′²·B = Σa₂(n)/n^s. Contour form:
**S₂ = (1/2πi)∮_𝒞 B(s)ζ′(s)·B(1−s)ζ′(1−s)·(ζ′/ζ)(s)ds** — residues at zeros (simple pole of ζ′/ζ), s = 1.

**M4-proper substitution ζ′ → ζ″** (under RH, 1−ρ = ρ̄):
**M := Σ|Bζ″(ρ)|² = (1/2πi)∮_𝒞 B(s)ζ″(s)·B(1−s)ζ″(1−s)·(ζ′/ζ)(s)ds.** At each zero the pole is still the simple pole of ζ′/ζ; ζ″ contributes no pole at (simple) zeros. [PROVEN — zeta2-note §2, re-verified]

## 2. The three bracket terms and the pole orders at s = 1 (PROVEN, closed-form)

Functional equation, differentiated twice (validator (i), signs +2L, +L² verified): **ζ″(1−s) = χ(1−s)[ζ″(s) + 2Lζ′(s) + L²ζ(s)] + O(1/t·ζ-terms)**, L = log(t/2π).

M-integrand = B(s)B(1−s)χ(1−s)·(ζ′/ζ)(s)·ζ″(s)·[ζ″ + 2Lζ′ + L²ζ] = three bracket terms. Laurent orders at s=1 (ζ: order 1; ζ′: 2; ζ″: 3):

| term | pole order at s=1 | ℒ-power (order^{−1}) |
|---|---|---|
| T₁ = (ζ′/ζ)·ζ″² | 1+3+3 = 7 | ℒ⁶ |
| T₂ = 2L·(ζ′/ζ)·ζ″ζ′ | 1+3+2 = 6, ×L | ℒ⁶ |
| T₃ = L²·(ζ′/ζ)·ζ″ζ = L²ζ″ζ′ | 3+2 = 5, ×L² | ℒ⁶ |

**Un-mollified ζ″ second moment is (T/2π)-ℒ⁶-scale** — direct transfer of the Gonek pole-count (ζ′: order-5 pole → ℒ⁴ ✓ matches Gonek's PROVEN ℒ⁴/12). The old "c(M) = (1/5)(1+MF), un-mollified (T/2π)L⁵/5" is refuted at the power level: ℒ⁶ ≠ ℒ⁵.

## 3. The B=1 (un-mollified) constant via Perron residue (PROVEN + CHECKED NUMERICALLY)

Laurent data at s = 1: (ζ′/ζ)(s) = −1/(s−1) + γ₀ + O(s−1); ζ″(s) = 2/(s−1)³ + 2γ₂ + O(s−1) (γₙ Stieltjes). Hence
**(ζ′/ζ)(s)ζ″(s)² = −4/(s−1)⁷ + 4γ₀/(s−1)⁶ − 8γ₂/(s−1)⁴ + O((s−1)⁻³)**.

Perron: Σ_{m≤X}ã₂⁰(m) = (1/2πi)∫(ζ′/ζ)(s)ζ″(s)²·X^s/s ds ~ Res at s=1 = X·[−4·Σ_{j=0}^{6}(−1)^{6−j}L^j/j! + 4γ₀·Σ_{j=0}^{5}(−1)^{5−j}L^j/j! + O(L³)],
leading term **−4·L⁶/720·X = −X·ℒ⁶/180**. Same method on ζ′: (ζ′/ζ)ζ′² = −1/(s−1)⁵ + γ₀/(s−1)⁴ + … ⟹ −X·ℒ⁴/24 (reproduces the validator's −(T/2π)ℒ⁴/24 ✓). So the B=1 ℳ₂-analogue ~ −(T/2π)ℒ⁶/180, and the B=1 un-mollified ζ″-moment ~ (T/2π)(d·ℒ⁵ + ℒ⁶/90) with leading (T/2π)ℒ⁶/90. **CHECKED NUMERICALLY (§8): probe gives S(X)/(−X·L⁶/180) = 0.4450, 0.4657, 0.4850 at X = 5·10⁴, 10⁵, 2·10⁵ — increasing toward 1 from below, the same convergence pattern as the ζ′-analog control (0.5560, 0.5761, 0.5945, which reproduces the validator's E-ii numbers 0.556…0.595 exactly, validating the code).**

## 4. The mollified constant c(M): structure PROVEN, value NOT PINNED

The ℒ⁶-parts of the ℳ₂-analogue are ∝ B(1) (q=1-piece pole structure, same mechanism as the ζ′ case where ℒ⁴ ∝ B(1), validator E-ii) and vanish for the mollifier (B(1) = 0). What remains:
**c(M) = [ζ″-diagonal ℒ⁵-coefficient] − 2·[ℒ⁵-coefficient of ℳ₂,₁^ζ″]**, with the ℳ₂,₁^ζ″-term being the (log n)⁴-weighted version of the paper's (1/12 − ϑ/2∫P + 3ϑ/2∫P² − ϑ²/2(∫P)² − 1/24ϑ∫P′²).

Neither the diagonal nor the ℳ₂,₁^ζ″-coefficient is quoted in 1302.5018; both require the full character-sum machinery (paper eqs. (5)–(8)) with (log n)⁴-weights — a paper-length computation, NOT a "harmless log-weight" transfer (the q=1 pieces are main-term-scale; validator E-iv). **Hence r′ = c(M)/c(S₂) is NOT pinned by this route.** [Structure: PROVEN transfer. Value: NOT PINNED.]

## 5. The r′ verdict and consequences (PROVEN)

- **r′ ≥ 0 PROVEN by positivity** (M ≥ 0 pointwise, M ~ (T/2π)ℒ⁵·c(M), c(S₂) = 57/64 > 0). This kills forecast outcome (b) outright: the quadratic form cannot be broken by a negative r′, and no world is forced to b ≤ 0 (r′ ≥ 0 is world-independent — it holds for ANY real-coefficient function with the ρ↔1−ρ̄ pairing).
- r′ = 3/5 is dead (both anchors). b_pair ≤ 0.2237 stands PROVEN. b ≈ 0.0758 (pair) is unsupported.
- **The empty direction's DUAL (E2):** the box form is a certificate *decreaser* — the pair identity gives N* ≤ S₁²/S₂ with NO r′ at all, and the box can only ever shrink b; r′ ≥ 0 means the ceiling 0.2237 is the best the quadratic form can certify without a genuinely new computation/input. The r′-lever is closed as unproductive; the binding input remains the k<1 moving-boundary count (M1), not r′.

## 6. The control (DH + fake-Weil) and firewall

Mechanical re-derivation against the RH-false zoo: the route's ONLY conclusion is r′ ≥ 0 (positivity of a sum of squares). It therefore **cannot force b ≤ 0 in any world** — no "proves too much" failure exists: the mechanism is a large-T asymptotic of ζ's *own* moments, and a world with planted off-line zeros at fixed height (DH σ = 0.8085, 0.6508; fake-Weil) is not a counterexample class for a large-T statement. DH/fake-Weil have structurally different moments (no ζ-type order-7 pole at s = 1; finite zero sets for Weil), so the route says nothing about them — the honest firewall position. Control runs (both PASS, §8): model_dh certified the off-line zeros σ = 0.808517182, 0.650830081 (|f| < 1e-9, matched 2/2; 6 off-line zeros total) — RH false in that world; model_weil confirmed all roots off the unit circle. The box ceiling 0.2237 is compatible with them: their off-line zeros (|β−1/2| = 0.15–0.31 in *their* units) violate the box hypothesis itself, so the box-form bound never applies there — no contradiction is even formulable, which is the point.

## 7. Labels

| Claim | Label |
|---|---|
| M contour integrand Bζ″·B(1−s)ζ″(1−s)·(ζ′/ζ); simple residue at zeros | PROVEN |
| ζ″(1−s) = χ(1−s)[ζ″+2Lζ′+L²ζ] + O(1/t) | PROVEN (validator (i), both signs) |
| Three bracket terms; pole orders 7,6,5 at s=1; un-mollified ζ″-moment ℒ⁶-scale | PROVEN (pole-count transfer from Gonek ℒ⁴) |
| Σ_{m≤X}ã₂⁰(m) ~ −X·ℒ⁶/180 (B=1 ζ″-moment ℒ⁶/90) | PROVEN (residue algebra) + CHECKED NUMERICALLY (probe, §8) |
| c(M) = diagonal − 2·ℳ₂,₁^ζ″; value requires (log n)⁴ character-sum computation | PROVEN (structure) / NOT PINNED (value) |
| r′ ≥ 0 | PROVEN (positivity) |
| r′ = 3/5 | REFUTED (anchor dead: ℒ⁶ vs ℒ⁵; 1/(2k+1) false) |
| b_pair ≤ 0.2237 ceiling stands; outcome (b) impossible | PROVEN |
| Firewall: route cannot force b ≤ 0 in DH/fake-Weil; says nothing about them | PROVEN (positivity + structural difference) |

## 8. Scripts + commands (all Rust, all run this session)

Probe `tools/m4_proper_probe/src/main.rs` (bin `m4_proper_probe`): Λ-sieve + Dirichlet-convolution partial sums. Run: `tools/m4_proper_probe/target/x86_64-unknown-linux-musl/release/m4_proper_probe`.

```
X=  50000  S1= -15873638.4  -X L^4/24= -28551715.6  ratio1=0.5560   S= -198317437.3  -X L^6/180= -445664116.9  ratio=0.4450
X= 100000  S1= -42172434.7  -X L^4/24= -73203446.8  ratio1=0.5761   S= -602455300.4  -X L^6/180= -1293724054.4  ratio=0.4657
X= 200000  S1= -109979024.6  -X L^4/24= -184979054.6  ratio1=0.5945   S= -1782087366.7  -X L^6/180= -3674626416.3  ratio=0.4850
```

ratio1 reproduces validator E-ii (0.556, 0.576, 0.587, 0.595) — code validated. ratio → 1 from below confirms −X·L⁶/180 (ζ″-analog of Gonek's −X·L⁴/24).

Control: `tools/barrier_zoo_rs/target/x86_64-unknown-linux-musl/release/barrier_zoo_rs dh` and `... weil` — both PASS (see §6).

No Python used. Note is the deliverable; probe binary + source saved alongside.
