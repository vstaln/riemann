# Attack: the ξ′ derivative method — mechanism, small-t density cross-check, constants, tower

**Agent:** EXECUTIONER (recovery + independent verification), Round 1.
**Date:** 2026-08-11.
**Question (per brief):** recover the previous agent's findings on "iterate the ξ′ derivative method"
(0.85838 / 0.86864 simple-and-on-line, 0.92919 / 0.93432 distinct — paper Remark 7.3, Lean
`Zeta23/XiPrime/`), resolve its "suspicious density of small-t roots" with an independent 60-digit
cross-check, and write up (a) mechanism ξ′- vs ζ-method, (b) the small-t check, (c) numerical
reproducibility of the constants, (d) the derivative-tower idea, (e) bottom line with labels.

**Status:** RESOLVED. All numeric claims below are backed by code that was run (scripts saved in
`tools/xiprime_check/`; exact commands in §7). No honest-guardrail issue found in the Lean/paper
constants; the previous agent's small-t roots were its own numerical artifacts, and the density
question is closed: **no hole in the window method for ξ′.**

---

## 1. What was recovered from the previous agent (transcript + files)

Previous agent's session: `~/.pi/agent/sessions/--home-vstaln-riemann--/2026-08-11T10-38-43-078Z_019ff067-3386-7b05-8c9b-be611039467c/tasks/2026-08-11T11-21-42-066Z_019ff08e-8db2-78c0-b245-6cc972ee3edd.jsonl`. Recovered:

- **Code:** `tools/zeta-rs/src/xiprime.rs` (f64 Rust; H(t) = Z(t)·(P′/P)(t) + Z′(t), zeros of H = on-line ξ′-zeros); `tools/check_xiprime.py` (mpmath, mp.dps=25, the i·ξ′·[log-derivative] formula). Output file `tools/data/xiprime_on_line_1_1000.txt` (1009 entries: 10 claimed small-t roots + 999 gap roots).
- **Findings:** 999/999 zeta-gaps contain exactly one on-line ξ′-zero; 999/999 gaps contain exactly one stationary point of Hardy's Z (separate claim); **10 H-zeros below γ₁** (t ≈ 0.094, 0.221, …, 0.871, 11.197) — flagged by the agent itself as "suspicious density", which is where it stopped (its `check_xiprime.py` then crashed on `mp.dps`; the first recovery attempt never ran).
- **The paper/Lean mechanism** (read from `research/lean-zeta-23/Zeta23/XiPrime/`): the ξ′ two-trace certificate has the same shape as ζ's, with the *pair density* **D₁** replacing ζ's |s−s′| kernel (Defs.lean: `kappaXi(λ,v) = 1/cWin D1 λ v`, `cWin = λ(∫v)²/(∫v² + λ·𝒥_D₁(λ;v))`, `𝒥_D₁(λ;v) = 2∫₀¹ D₁(λr)(v⋆v)(r) dr`; Certificate/AtOne.lean: proportions `2 − κ₁(λ,v)` (simple∧on-line) and `3/2 − κ₁(λ,v)/2` (distinct)). Constants are PROVEN in Lean (`certFlat_sharp`, `certQuartic_sharp`: 0.858383 / 0.929191 / 0.868640 / 0.934320 at some λ ∈ [1/2,1)).

---

## 2. (b) The small-t root density check — CHECKED NUMERICALLY (60 digits, mpmath)

### 2.1 Setup and self-verification

H(t) := i·ξ′(1/2+it) is **real** for real t (ξ(1/2+it) is real and even in t, so d/dt ξ(1/2+it) = i·ξ′(1/2+it) is real), and H(t) = 0 ⟺ ξ′(1/2+it) = 0. Computed two independent ways (60 digits):

1. **Direct:** H(t) = Re[i·ξ(s)·A(s)], A(s) = 1/s + 1/(s−1) − ½log π + ½ψ(s/2) + ζ′/ζ(s) (exact log-derivative; ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)).
2. **Z-form (no spurious poles):** H(t) = −(Z(t)·(P′/P)(t) + Z′(t)), Z = e^{iθ}ζ(1/2+it), θ = Im log Γ(¼+it/2) − (t/2)log π, P′/P = 2t/(t²+¼) − ½Im ψ(¼+it/2).

They agree up to the positive factor P(t) = (t²+¼)/2·π^{−1/4}|Γ(¼+it/2)| (H_direct = P·H_zform), hence share zeros; signs match at every probe (t = 0.5, 10, 16, 50, 500). Also `mp.diff` on ξ gives the identical value. Max |Im H| on the line ~ 10⁻⁶³ — H is real to working precision.

### 2.2 The true small-t structure (60 digits)

- **No zeros of ξ′ on the line in (0, γ₁):** sign scans of H over (0.0001, γ₁−0.5) at step 0.1 (0 changes) and (0.0001, 3.0) at step 0.005 (0 changes); H(0.001) = −2.30·10⁻⁵, H(5) = −6.65·10⁻², H(13.9) = −1.79·10⁻³ — H < 0 throughout (0, γ₁).
- **Zeros: t = 0** (ξ′(1/2) = 0 by the functional equation, since ξ(s)=ξ(1−s) forces ξ′ to vanish at 1/2) **and exactly one in each zeta-zero gap** (γ_n, γ_{n+1}), n = 1, …, 999.
- First 20 gap roots (60 digits), all simple (sign-changing):

  | gap | t | gap | t |
  |---|---|---|---|
  | 1 | 15.5857085898293423445957292355 | 11 | 53.9687288597224334661117413328 |
  | 2 | 22.0979772804009020982460583653 | 12 | 57.2629341113391025140841206942 |
  | 3 | 26.2722473569356243750711540382 | 13 | 59.9306989737258423521851881633 |
  | 4 | 31.2317958710097855089118960065 | 14 | 62.1099057508713071858658957278 |
  | 5 | 34.1933102690113808807215179314 | 15 | 65.7583193064237373440898606707 |
  | 6 | 38.4982407637544907213571745169 | 16 | 67.9264537710552439462471054791 |
  | 7 | 41.7367295224193331427350981285 | 17 | 70.4184071425949099814148995090 |
  | 8 | 44.5417036073809966272692376173 | 18 | 73.0605435210706675476179764859 |
  | 9 | 48.6225326852778658468161729295 | 19 | 76.2254379706120628126703379202 |
  | 10 | 50.8390048228159697828179099569 | 20 | 77.9978720250931747998206833418 |

- Gap histogram over the first 50 gaps: {1 : 50} (exactly one per gap); far-out samples at gaps 100, 200, …, 999: {1 : 10}, e.g. gap 200 → 397.076308115727967, gap 999 → 1418.99574690661016. Fine scans confirm: gap 1 has its single root at 15.58570858982934 (step 0.01); the (γ₉, γ₁₁) region has exactly two roots at 48.6225… and 50.8390… (γ₉=48.005, γ₁₀=49.774, γ₁₁=52.970 from the LMFDB file).
- **Count consistency:** on-line ξ′-zeros with 0 < t ≤ γ₁₀₀₀ = 999 = N_ζ(γ₁₀₀₀) − 1 (the t=0 zero is not in (0,T] for T>0). Riemann–von Mangoldt for ξ′ (Lean `xiDeriv_riemannVonMangoldt`) has the ζ main term (T/2π)ℓ₁(T) ≈ 999.5 at T = 1419.42 — the −1 is inside the O(log T) error. **The density is exactly what the interlacing structure predicts; it is consistent with the 0.85838 certificate; there is NO hole.**

### 2.3 The previous agent's ten "small-t roots" are artifacts — root cause pinned

Direct 60-digit evaluation of H at all ten claimed roots gives **H ≠ 0 by large margins** (e.g. H(0.094361507680) = −2.17·10⁻³, H(11.197465161854) = −1.28·10⁻²; a genuine zero would give |H| < 10⁻³⁰). Its gap-1 root 16.152219566157 is also false (true: 15.58570858982934; H(16.152) = +1.8·10⁻⁴ ≠ 0). All its gap-2+ roots are correct to ≤ 4·10⁻⁶ (f64 noise; see §2.4).

Root cause, found by re-running its f64 pipeline against mpmath values (table below): **two bugs confined to t < 20**, both in its own code:

1. **Sign bug in its ψ(¼+it/2) recursion** (`psi_im` in `tools/zeta-rs/src/xiprime.rs`): it computes ψ(z) = ψ(z+m) − Σ1/(z+j) but returns `s − corr` where `corr = Σ Im[1/(z+j)]` with the sign that requires `s + corr`. Since Im ψ(z) = Im ψ(z+m) − Σ Im[1/(z+j)] = Im ψ(z+m) + corr, the sign is wrong. Effect: P′/P = 2t/(t²+¼) − ½Imψ is wrong whenever the recursion is used (|z| < 10, i.e. t < 20) — e.g. t=5: their P′/P = +0.920 vs true −0.440 (wrong sign); t=10: +0.200 vs −0.611; t=13: −0.0886 vs −0.651. For t ≥ 20 (no recursion) their P′/P is correct, which is exactly why their gap-2+ roots are right.
2. **Stirling divergence in its θ(t) for |z| ≲ 1** (`theta_small` in `tools/zeta-rs/src/zeta.rs`): the Bernoulli asymptotic for ln Γ(¼+it/2) at |z| = 0.35 (t=0.5) has terms growing like k=6 term ≈ −1323; their Z(t) = e^{iθ}ζ(1/2+it) is corrupted near t=0 (Z(0.5) = −0.477 vs true −1.065), and the h=1e-4 central-difference Z′ amplifies any residual θ error by 1/(2h) = 5000.

Their Z(t) itself is accurate for t ≥ 2 (matches mpmath to ≲ 10⁻⁴ everywhere checked, e.g. Z(10), Z(13), Z(100) to 10⁻⁹…10⁻⁵); the artifacts come entirely from (1) and (2). Verbatim comparison (their pipeline vs 60-digit mpmath; H computed both as Z·(P′/P)+Z′):

| t | their Z | true Z | their P′/P | true P′/P | their Z′ | true Z′ | their H | true H (Z-units) |
|---|---|---|---|---|---|---|---|---|
| 0.5 | −0.4769 | −1.06535 | +3.1206 | +0.8538 | +2592.9 | +0.9343 | +2591.4 | −0.0246 |
| 5.0 | −0.7389 | −0.73886 | +0.9203 | −0.4399 | −0.1467 | −0.1467 | −0.8267 | −0.1783 |
| 10.0 | −1.5492 | −1.54919 | +0.1998 | −0.6110 | −0.0305 | −0.0305 | −0.3400 | −0.9160 |
| 13.0 | −0.7911 | −0.79115 | −0.0886 | −0.6510 | +0.5839 | +0.5839 | +0.6540 | −1.0989 |
| 15.5857 | +1.2115 | +1.21150 | −0.3015 | −0.6733 | +0.8157 | +0.8157 | +0.4504 | −6·10⁻⁶ (zero) |
| 16.1522 | +1.6477 | +1.64771 | −0.4326 | −0.6772 | +0.7127 | +0.7127 | +1.2·10⁻⁵ (spurious) | +0.403 |
| 20.0 | +1.1478 | +1.14784 | −0.6980 | −0.6980 | −1.0390 | −1.0390 | −1.840 | +1.840 |
| 22.0 | −0.9839 | −0.98392 | −0.7059 | −0.7059 | −0.8045 | −0.8045 | −0.110 | +0.110 |

(Their Z′ column matches true Z′ because Z is accurate; the H mismatch is driven entirely by the wrong P′/P for t < 20. Signs of H are convention-dependent up to the outer minus; zeros are what matter.)

### 2.4 Agreement of the remaining data

Their file entries 12–1009 (gap roots 2–999) vs the 60-digit values: |diff| ≤ 4.2·10⁻⁶ (e.g. gap 2: 2.9·10⁻¹⁰, gap 5: 5.6·10⁻⁸, gap 7: 4.2·10⁻⁶), consistent with their Z′(t) central-difference noise (~10⁻⁶) shifting roots by |H′|⁻¹·noise ≈ 0.3⁻¹·10⁻⁶. Entry 11 (their gap-1 root) is wrong by 0.567. The one-per-gap *count* survives: their full f64 scan also reports 1 per gap for all 999 gaps (gap-1 count correct by luck, position wrong), and the 60-digit scans confirm the count for gaps 1–50 plus ten sampled far gaps.

---

## 3. (a) Mechanism: ξ′-method vs ζ-method

Both are rank–trace two-trace certificates; the difference is the *trace functional* (which density sits in the second trace):

- **ζ-method** (paper §7.1, Lean `Zeta23/ThmD`): the window functional is c_λ(v) = λ(∫v)²/(∫v² + λ²∬_{[−½,½]²}|s−s′|v(s)v(s′) ds ds′); the HS-norm constant is 1/c₁(v₀) = Q(v₀) = ½ + (1/√2)cot(1/√2) = 1.3274993…, proportion = 2 − Q = 0.67250… (PROVEN optimal for that functional — attack-kernel.md).
- **ξ′-method** (Remark 7.3, Lean `XiPrime/Defs.lean`): c_λ^(1)(v; D₁) = λ(∫v)²/(∫v² + λ·𝒥_{D₁}(λ;v)) with 𝒥_{D₁}(λ;v) = 2∫₀¹ D₁(λr)(v⋆v)(r) dr and the **pair density**
  **D₁(r) = r − 4r² + Σ_{k≥0} D1coeff(k)·r^{2k+3},  D1coeff(k) = 2·4^{k+1}·k!/(2k+2)!**
  (D1coeff 0 = 4, 1 = 4/3, 2 = 16/45, 9 = 1024/3273645375; ratio D1coeff(k+1)/D1coeff(k) = 2(k+1)/((k+2)(2k+3)) — all verified numerically). κ₁(λ,v) = 1/c_λ^(1)(v;D₁); at λ=1, **κ₁(1,v) = (∫v² + 2∫₀¹ D₁(r)(v⋆v)(r) dr)/(∫v)²**. Proportions: simple∧on-line ≥ 2 − κ₁(λ,v), distinct ≥ 3/2 − κ₁(λ,v)/2. This D₁ is Farmer–Gonek's F₁ for ξ′ (minus its T^{−2α}log T term; Defs.lean), i.e. the ξ′-analog of Montgomery's pair density — that is why the flat constant 0.85838 equals the FGL RH-conditional constant made unconditional (attack-kernel.md).
- **Why the constants are higher for ξ′ than ζ:** the D₁-based kernel is "smaller" than the |s−s′| kernel on [0,1]² in the relevant norm, giving a smaller κ₁ (1.1416 vs 1.3275), hence proportions 2 − κ₁ = 0.858 vs 0.6725. (Heuristic statement; the exact reason lives in the coefficient/diagonal-law machinery — CONJECTURED at the level of intuition, PROVEN as a statement by Lean.)
- **The ζ-optimal cosine is NOT optimal for ξ′ — CONJECTURED in attack-kernel.md, now CHECKED NUMERICALLY:** κ₁(1, vCos(√2·)) = 1.1321111348009480644 → 2−κ₁ = 0.86788886519905193555, which is *worse* than the quartic window's κ₁ = 1.1313594848334966975 → 0.86864051516650330245 (and better than flat 1.1416159452907819718 → 0.85838405470921802815). So for the ξ′ functional the numerically-optimized quartic beats both the flat box and the cosine; the cosine is suboptimal for ξ′ (different functional ⟹ different optimizer). This is the concrete content of the CONJECTURED mechanism in attack-kernel.md §4, and it does **not** transfer to ζ (0.6718 < 0.6725, PROVEN in attack-kernel.md).

---

## 4. (c) Are 0.85838 / 0.86864 and 0.92919 / 0.93432 numerically reproducible? — YES (CHECKED NUMERICALLY, 50 digits)

Direct evaluation of κ₁(1,v) from the D₁ series (mp.quad; D₁ summed to k ≤ 60; autocorrelations v⋆v integrated exactly via mp.quad on [−½, ½−r]):

| window | κ₁(1,v) | 2 − κ₁ | 3/2 − κ₁/2 | certified interval | holds? |
|---|---|---|---|---|---|
| flat (v≡1) | 1.1416159452907819718 | 0.85838405470921802815 | 0.92919202735460901408 | [100905635384/88388425125, + 1024/2990212875] | ✓ in interval |
| quartic (1 − (7/100)(2s)² − (51/200)(2s)⁴) | 1.1313594848334966975 | 0.86864051516650330245 | 0.93432025758325165123 | [kap9Quartic, + ε₉·(2777/3000)²] | ✓ in interval |
| cos(√2 s) | 1.1321111348009480644 | 0.86788886519905193555 | 0.93394443259952596778 | — (mechanism test) | — |

Every certified lower bound holds with the correct margin:
- flat: 2 − κ₁ = 0.8583840547 ≥ 0.85838371 ✓ (published 5-digit: > 0.85838 ✓); 1.5 − κ₁/2 = 0.9291920274 ≥ 0.92919185 ✓ (> 0.92919 ✓).
- quartic: 0.8686405152 ≥ 0.86864017 ✓ (> 0.86864 ✓); 0.9343202576 ≥ 0.93432008 ✓ (> 0.93432 ✓).

Also verified: D₁ ≥ 0 on [0,1] (grid min = 0.0 at r = 0 and r = ½, consistent with D₁ = r(1−2r)² + nonneg series); D₁(0.37) = 0.0346055444 vs truncation-1 0.025012 (tail 0.00959); ε₉ = 3.4245·10⁻⁷ < 3.43·10⁻⁷. The Lean constants are exact rationals (κ₉) sandwiched by the D₁-truncation/tail — the numerics sit inside the certified intervals, confirming the certificate machinery is faithful to its own definitions.

---

## 5. (d) The derivative tower (ξ″, ξ‴, …) — Farmer-style certificate: CONJECTURED, interlacing CHECKED NUMERICALLY

- **Interlacing (CHECKED NUMERICALLY, 60 digits):** H₂(t) := −ξ″(1/2+it) is real (ξ″ is real on the line); its zeros interlace the ξ′-zeros exactly as expected: **one ξ″-zero in every interval between consecutive ξ′-zeros, including (0, u₁)**, where u₁ = 15.5857… is the first ξ′-zero. Verified over the first 20 intervals (histogram {1 : 20}); all detected zeros sign-changing. First few: 4.750237876793571908645817 (in (0,u₁)), 17.03380144196064931975966, 23.21376745968233030597151, 27.49263058560298204532293, 32.13292897662641905981081. (|H₂′| at roots is exponentially small — |ξ″| itself is ~ e^{−πt/4}·poly — so "simple" here means sign-changing, which is the content that matters for interlacing.) By induction the same holds for ξ^(j) whenever the previous derivative's zeros are on the line and simple.
- **Why it could give a NEW certificate (Farmer 1995; the paper's own history):** Farmer proved N^d(ζ) > 0.6395·N(ζ) by combining simple-zero proportions for the derivatives ξ^(j); Wu pushed to 0.6603. The two-trace machinery now supplies, for each ξ^(j), a bound of the form proportion-simple∧on-line ≥ 2 − κ₁^(j)(v) provided the D₁-type density (diagonal law) and the coefficient machinery extend to ξ^(j). The coefficients for ξ′ are C(N; Λ⋆), Λ⋆ = l/2 + iπ/4 (Lean `Coeff.lean`); the extension to ξ^(j) is a genuine re-derivation (different Λ⋆/coefficient shifts), **not a corollary — CONJECTURED**. If it holds with constants comparable to ξ′'s (κ₁^(j) ≈ 1.13–1.14), a Farmer-style weighted combination would convert per-derivative simple-zero proportions into a bound on distinct zeros of ζ, the natural target being the gap 0.6603 → higher (and the paper's own distinct-ξ′ 0.92919 is about ξ′, not ζ).
- **Honest caveats:** (i) the weights in Farmer's combination need the actual interlacing counts per derivative, not just proportions; (ii) the D₁^(j) densities for j ≥ 2 are not in the repo and would need derivation + certification (the current ε₉-style tail argument is D₁-specific); (iii) each derivative adds O(1)-per-gap zeros only if the previous derivative's zeros are all on-line-and-simple, which is exactly what the certificate supplies — so the tower is self-reinforcing but the base (ξ′) is unconditional (PROVEN in Lean). Net: a plausible, concrete next attack (the ξ″ certificate constant first), **CONJECTURED**, not a theorem.

---

## 6. (e) Bottom line (with labels)

1. **Small-t density question: RESOLVED — numeric artifact, no hole. (CHECKED NUMERICALLY at 60 digits, two independent formulations.)** True on-line ξ′-zeros: t = 0, plus exactly one in each zeta-zero gap (γ_n, γ_{n+1}); none in (0, γ₁). Gap-1 root = 15.5857085898293423445957292355 (NOT 16.152). Total on-line in (0, γ₁₀₀₀] = 999 = N_ζ(γ₁₀₀₀) − 1, consistent with RvM for ξ′ and with the 0.85838 certificate structure. The previous agent's 10 "small-t roots" (its own transcript flagged them) are artifacts of its f64 pipeline: a sign bug in its ψ recursion (P′/P wrong for all t < 20) and θ-Stirling divergence at |z| ≲ 1 (Z corrupted near t = 0; Z′ noise ×5000). Its Z(t) itself is accurate; its gap-2+ roots are correct to ≤ 4.2·10⁻⁶.
2. **The window method for ξ′ stands. (PROVEN as a statement by Lean; the specific constants CHECKED NUMERICALLY here.)** The proportion claims (≥ 0.85838 flat, ≥ 0.86864 quartic; distinct ≥ 0.92919 / 0.93432) count zeros in (T, 2T] as T → ∞; small-t behavior is irrelevant to them, and the small-t structure is in any case the clean interlacing one.
3. **Constants reproducible. (CHECKED NUMERICALLY, 50 digits.)** κ₁(1,flat) = 1.1416159452907819718, κ₁(1,quartic) = 1.1313594848334966975, both inside their certified rational intervals; all four published decimals 0.85838371 / 0.92919185 / 0.86864017 / 0.93432008 hold with the correct side/margins. The five-digit interface numbers 0.85838, 0.92919, 0.86864, 0.93432 are strict.
4. **Mechanism: different trace functional. (CONJECTURED in attack-kernel.md; the cosine-suboptimality part now CHECKED NUMERICALLY.)** For ξ′ the second trace uses the density D₁(r) = r − 4r² + Σ 2·4^{k+1}k!/(2k+2)!·r^{2k+3} in place of ζ's |s−s′| kernel; κ₁(cos(√2·)) = 1.132111 > κ₁(quartic) = 1.131359 > κ₁(flat) = 1.141616 gives 0.86789 < 0.86864 > 0.85838 — the ζ-optimal cosine is beaten by the quartic for ξ′ (different optimizer), and the quartic never transfers to ζ (PROVEN, attack-kernel.md).
5. **Derivative tower: plausible next attack, CONJECTURED.** ξ″ interlacing verified numerically (one ξ″-zero per ξ′-gap, 20/20 intervals). A Farmer-style combination over ξ^(j) certificates is a concrete route toward distinct-ζ bounds (0.6603 → ?), contingent on extending the D₁/diagonal-law machinery to ξ^(j) — new math, not a corollary.
6. **Meta (epistemic):** the recovered claim "0.85838/0.92919 proven per Remark 7.3 and Lean" is consistent with everything measured; the only broken artifact in the chain was the previous agent's own f64 small-t scan, which it correctly distrusted. No fabricated/weakened validator encountered. The search continues on the tower and on the PairCeiling gap (0.6725 → 0.68185, attack-kernel.md §5).

---

## 7. Exact commands for every number above

- Small-t structure, H cross-check, claimed-root evaluation, gap roots (60 digits):
  `cd tools/xiprime_check && uv run --quiet --with mpmath python check_small_t.py 20`  (→ `small_t_run.txt`; the 50-gap histogram {1:50} is from the same script with argument 50, ~11 min).
- Certificate constants (50 digits): `uv run --quiet --with mpmath python check_cert.py`  (→ `cert_run.txt`).
- Tower interlacing (60 digits): `uv run --quiet --with mpmath python check_tower.py`  (→ `tower_run.txt`).
- Consistency/debug (60 digits): `uv run --quiet --with mpmath python check_consistency.py`.
- Optional full-count (25 digits, slow): `uv run --quiet --with mpmath python check_count.py`.
- Previous agent's pipeline (reproduces the artifacts): `cd tools/zeta-rs && cargo build --release --target x86_64-unknown-linux-musl && ZETA_DATA=../data ./target/x86_64-unknown-linux-musl/release/xiprime`; its ψ/θ bugs reproduced standalone via `rustc --target x86_64-unknown-linux-musl -C linker=rust-lld` (scripts in this repo's git history / transcript; the numeric comparison table in §2.3 was produced by evaluating both pipelines at the listed t values).

All mpmath runs use `uv run --quiet --with mpmath` (mpmath 1.4.1), 60 digits (50 for check_cert.py), zeta and its first two derivatives, digamma/trigamma, Γ, and mp.quad for the certificate integrals.
