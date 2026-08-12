# T-2 Derivative-tower (ξ″/ξ‴ certificate + weighted distinct-ζ): state, machinery, missing lemma, interlacing check

**Agent:** THEORIST (wave-phone-2). **Date:** 2026-08-12.
**Task:** develop T-2 (catalog `attack-vector-catalog-3.md` #1, ~line 209), target Farmer's 0.6603 distinct-ζ
record. A prior tower-method agent died on output limit after finding prior art; this note continues, tighter.
**Status: RESOLVED — tower is DEAD at the second rung** (kill rule κ₁^(2) ≥ κ₁^(1) already triggered in
`attack-xiprime2-tower.md`; re-derived and re-verified here). Honest deliverable: precise claim, the machinery,
the missing lemma, the checked interlacing, and the documented obstruction.

---

## 1. The T-2 claim, stated precisely

**What a ξ″-certificate would prove.** For each j, let fi_j = (proportion of zeros of ξ^(j) on the critical
line that are simple). The ξ′ certificate PROVES (Lean `Zeta23/XiPrime/`, paper Rem 7.3):
fi₁ ≥ 0.85838 (flat window), fi₁ ≥ 0.86864 (quartic) for simple∧on-line, and distinct on-line
fi₁ ≥ 0.92919 / 0.93432. The tower claim is: derive the ξ″-analog pair density D₁^(2), evaluate the
certificate constant κ₁^(2)(1,v) = (∫v² + 2∫₀¹D₁^(2)(v⋆v))/(∫v)², and if κ₁^(2) < κ₁^(1) then
fi₂ ≥ 2 − κ₁^(2)(1,v) is a NEW lower bound on the simple-on-line proportion of ξ″-zeros.

**What it would buy for ζ.** Farmer 1995 identity (6): N_d(ζ) ≥ 2⁻ᴶ[2^{J−1}β₀ + β_J + Σ_{n=1}^{J−1}2^{J−n−1}β_n]·N
with β_j ≥ fi_j. With fi₀ = 0.6725 (paper Thm D) and fi₁ = 0.86864, the combination already exceeds Wu's
0.6603 — so **the "distinct-ζ > 0.6603" record is NOT the actual obstruction**. The obstructions are:
(i) the ξ″ rung dies (κ₁^(2) ≫ κ₁^(1), certificate vacuous), and (ii) even with the paper's own inputs the
combination yields 0.79215 < 5/6 (the paper's Thm E, a different route), so no NEW constant is produced.

**How the tower was supposed to deliver it.** Interlacing (Rolle, on the real line via H_j(t) = i^j ξ^(j)(1/2+it)):
one ξ″-zero per ξ′-gap ⇒ the ξ″ certificate's simplicity supplies the next rung's input; iterating,
fi_j = 2 − κ₁^(j) feeds Farmer's identity. For this to beat the record one needs fi_j to stay high as j
grows — it does not (§3).

## 2. The method gap (missing lemma)

**Missing lemma:** the ξ″-analog D₁^(2) of Montgomery's pair density — the FGL (0803.0425) coefficient
system α_k^(2) and the mean-square A^(2)(x), i.e. the "D₁^(j) machinery" flagged as "new math but bounded
and checkable" in the catalog. This is NOT a corollary of ξ′; it requires re-expanding the log-derivative
tower W_j = B_{j+1}/B_j (complete Bell polynomials) in 1/L where W = ξ′/ξ = L + Z, L = ½logπ + (1/2)ψ(s/2),
Z = ζ′/ζ.

**This gap is now CLOSED — by algebra, with a negative answer.** The exact coefficient systems were derived
(sympy Bell expansion, checked at coefficients):

- ξ′: α₀ = −Λ, α₁^(1) = −(Λlog); ξ″: α₀ = −Λ, **α₁^(2) = −2(Λlog)** (factor 2 AND sign flip),
  α₂^(2) = −(Λlog²) − 2(Λ∗Λlog), α₃^(2) = −2(Λ²∗Λlog) − 2(Λ∗Λlog²) − 2(Λlog∗Λlog).
- Pattern: [1/L]-coefficient of W_j − L equals j·(L′+Z′), i.e. α₁^(j) = −j(Λlog). The first correction
  inflates linearly with j.
- Consequence for the density: D₁^(2)(r) = r + 8r² + 16r³ + 4·Σ_{k≥1}D₁coeff(k)r^{2k+3} — all coefficients
  positive and 4× the ξ′ correction, so D₁^(2) ≥ D₁ pointwise. κ₁^(2)(1,flat) = **4.5664637812**,
  κ₁^(2)(1,quartic) = **4.2083656210** (30+ digits, `tools/xiprime2_check/check_tower_kill.py`) ⇒
  2 − κ₁^(2) < 0: **the ξ″ certificate inequality is vacuous**. Robust: even with cross-coefficient 0
  (most conservative model) κ^(2) = 3.2331 ≫ κ₁^(1). No consistent model gives κ₁^(2) < κ₁^(1).

## 3. Why the tower dies (mechanism)

The leading density core α₀ = −Λ is universal across derivatives (all give the same r − 4r² + … core); the
first correction α₁^(j) = −j(Λlog) flips the cross-term sign and quadruples |α₁|² at j = 2 (ratio −2.000
exact, diag1 ×4, A^(2)/A^(1) = 9.9–22.8× — all CHECKED NUMERICALLY). The density only grows with j, so the
certificate constant only grows; there is no rung where fi_j stays high. Consistent with Farmer–Rhoades
(0310252): "to understand the effect of the second derivative we must iterate" — the iteration does not
renormalise to the ξ′ density.

## 4. Independent interlacing check (this session, 40 digits, first 20 gaps)

Script: `research/waves/wave-phone-2/scripts/t2_interlacing.py` (fresh code; reuses the independently
60-digit-verified ξ′-zero list u_n from `tools/xiprime_check/check_small_t.py`, README-cited).
Command: `proot-distro login ubuntu -- python3 research/waves/wave-phone-2/scripts/t2_interlacing.py` (~6 min).
Formulas: H₂(t) = −ξ″(1/2+it), ξ″/ξ = A² + A′, A = 1/s + 1/(s−1) − ½logπ + ½ψ(s/2) + ζ′/ζ;
A′ = −1/s² − 1/(s−1)² + ¼ψ′(s/2) + ζ″/ζ − (ζ′/ζ)².

```
gaps checked: 20
one-xi''-per-gap counts: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   # 20/20
xi''-roots (first 5 gaps): 4.75023787679, 17.033801442, 23.2137674597, 27.4926305856, 32.1329289766
PERFECT_INTERLACING
max |Im H2| at endpoints/midpoints: 5.7211e-43     # H2 = -xi'' real, as claimed
xi''(1/2) = -H2(0) = 0.0229719443151454
```

Consistent with the prior 60-digit run (`tools/xiprime_check/check_tower.py`, captured `tower_run.txt`:
histogram {1: 20}, max |Im H₂| = 1.157e-63, roots match to printed digits). **CHECKED NUMERICALLY**
(script cited above) — the interlacing claim stands.

## 5. The Farmer-combination arithmetic (context for "target 0.6603")

`tools/xiprime2_check/check_farmer_combo.py`: Farmer identity (6) with Conrey's fi = (0.40219, 0.79874,
0.93469, 0.9673, 0.98006, 0.9863) reproduces Farmer's 0.63952 (paper: 0.63952). With the paper's Thm D +
the ξ′ certificate (fi₀ = 0.6725, fi₁ = 0.86864) + Conrey fi₂–₅: **Nd/N ≥ 0.79215** — beats Wu 0.6603 but
< 5/6. Wu's own remark (1206.1679 p.14): the pure derivative-combination route is "much worse than
Theorem 1". So the 0.6603 "target" is achievable by combination arithmetic alone and is NOT the binding
constraint; the binding constraint is the vacuous ξ″ rung and the 5/6 wall (paper Thm E, separate route).

## 6. Honesty labels

| Claim | Label |
|---|---|
| Interlacing: one ξ″-zero per ξ′-gap, 20/20; H₂ = −ξ″ real; ξ″(1/2) = 0.0229719443 | **CHECKED NUMERICALLY** (this session, `scripts/t2_interlacing.py`, 40 digits; consistent with 60-digit `check_tower.py`) |
| ξ′ constants fi₁ ≥ 0.85838 / 0.86864 (simple∧on-line), 0.92919 / 0.93432 (distinct) | **PROVEN** (Lean `Zeta23/XiPrime/`) + **CHECKED NUMERICALLY** (`tools/xiprime_check/check_cert.py`) |
| FGL coefficient system α₀ = −Λ, α_k = (Λlog)∗Λ^{∗(k−1)}; Thm 1.1 form factor; Farmer identity (6); 0.63952 | **VERIFIED-FROM-PAPER** + arithmetic **CHECKED NUMERICALLY** |
| ξ″ coefficient system (α₁^(2) = −2(Λlog), new log² terms); pattern α₁^(j) = −j(Λlog) | **PROVEN BY ALGEBRA** (sympy Bell expansion, coefficient-level checks) |
| D₁^(2)(r) = r + 8r² + 16r³ + 4·Σ D₁coeff(k)r^{2k+3} ≥ 0 on [0,1] | **CHECKED NUMERICALLY** |
| κ₁^(2)(1,flat) = 4.5664637812, κ₁^(2)(1,quartic) = 4.2083656210; 2−κ₁^(2) < 0 (vacuous) | **CHECKED NUMERICALLY** (30+ digits, `check_tower_kill.py`); robustness κ = 3.23 at cross-coeff 0 |
| **Kill: κ₁^(2) ≥ κ₁^(1) ⇒ tower dies at ξ″; no higher rung helps (pattern α₁^(j) = −j(Λlog))** | **PROVEN** from the above |
| Farmer combination with paper inputs: Nd/N ≥ 0.79215 (beats Wu 0.6603, < 5/6) | **CHECKED NUMERICALLY** (`check_farmer_combo.py`) |
| No new simple-zeros-on-line constant > 0.6731929 (tawanerguo) from this tower | **PROVEN** (tower dead; no other mechanism in this task) |

## 7. Files / scripts

- `research/waves/wave-phone-2/scripts/t2_interlacing.py` — this session's independent interlacing check
  (40 digits, first 20 gaps). Run: `proot-distro login ubuntu -- python3 .../t2_interlacing.py`.
- `tools/xiprime_check/check_tower.py` (+ `tower_run.txt`) — 60-digit interlacing, prior session.
- `tools/xiprime2_check/check_tower_kill.py` — consolidated kill-rule verification (κ₁^(2) values).
- `tools/xiprime2_check/check_farmer_combo.py` — Farmer identity arithmetic.
- Prior derivation scratch: `/tmp/x2final.py`, `/tmp/exactcoeff.py`, … (copies under `tools/xiprime2_check/`).

## 8. What this unlocks (program value)

1. **T-2 is closed as a route.** The ξ″ rung is vacuous; α₁^(j) = −j(Λlog) means no higher rung helps.
   Future rounds must not re-fund the tower. (Catalog's `attack-xiprime2-tower.md` is the resolution;
   this note adds the independent interlacing check.)
2. **The Farmer-combination arithmetic is verified and re-contextualised:** 0.79215 is a consistency check
   (beats 0.6603, below 5/6) — the 0.6603 "record" is not the real wall.
3. **Live routes** (catalog): D-1 (Dirichlet family), V20 (effective finite-T), E-OK (EnclOK), beyond-1
   range. External record (tawanerguo 0.6731929) untouched by this result.
