# Li-coefficient falsification harness — baseline result

Date: 2026-08-25
Lever: 4 (classical equivalences with RH-false controls), rung 1 (Li coefficients as a falsification harness)
Status: **PROVEN (Δ-arithmetic) / CHECKED NUMERICALLY (λ_n(true), three independent methods) / CONJECTURED (n\* estimate)**

## ONE-LINE VERDICT

**NO_FLAG within n ≤ 60 for every implant tested** (off-line β=0.9 and both on-line controls).
The first 60 Li coefficients **cannot distinguish** the true ζ from the FE-symmetric planted model
that carries an off-line zero; the plant is only detected at **n\* ≈ 4.4×10³** (by the reflected partner zero),
not anywhere near n ≤ 60.

| implant (t0 = zetazero(1..12), n = 1..60) | min λ_n(planted) | first negative n | verdict |
|---|---|---|---|
| OFFLINE β=0.9 (P = {0.9,0.1}±it0) | +0.023409445 (n=1) | none | **NO_FLAG** |
| ONLINE shift t0 → t0+0.3 | +0.022890325 (n=1) | none | NO_FLAG (control) |
| ONLINE swap t0 → zetazero(2) | +0.020358262 (n=1) | none | NO_FLAG (control) |

Conventions `bl` (B–L exact per-zero) and `std` (standard Li form) give **identical** verdicts and identical Δλ_n.

## Question

Does λ_n > 0 actually FLAG a single planted off-line zero (FE-symmetric model) within n ≤ 60, and at what n?

## Model & exactness (reused from `tools/jensen_honest_probe.py`)

Planted model: `zeta_planted = zeta_true * R`, `R(s) = ∏_{ρ∈P}(1−s/ρ)/∏_{ρ∈M}(1−s/ρ)` with
`M = {1/2±it0}`, `P = {β±it0, (1−β)±it0}` for β≠1/2 (FE + conjugation closed orbit), `P = {1/2±itp}` for β=1/2.
`R(1−s) = R(s)` exactly (both sets FE-closed) ⇒ exactly ξ-symmetric.

Exactness trick (Bombieri–Lagarias): `log ξ(1/(1−x)) = Σ_{n≥1} λ_n x^n/n`. The per-zero contribution to λ_n is
`h_n(ρ) = 1 − (ρ/(ρ−1))^n`, so

    Δλ_n = Σ_{ρ∈P} h_n(ρ) − Σ_{ρ∈M} h_n(ρ)        (EXACT — unchanged zeros telescope out)
    λ_n(planted) = λ_n(true) + Δλ_n

computed from the moved zeros alone at dps=30; no ξ evaluation in the Δ. **PROVEN** (algebra + the B–L identity).

λ_n(true), n=1..60, comes from the validated series in `tools/li_probe.py` (Stieltjes constants + B–L substitution),
cross-validated three independent ways **(all agree)**:

| n | series | derivative-formula (mp.diff) | zero-sum (20,000 zeros) |
|---|---|---|---|
| 1 | 0.023095708966 | 0.023095708966 | 0.0230167 (tail ~8e-5) |
| 2 | 0.092345735228 | 0.092345735228 | 0.0920296 (tail ~3e-4) |
| 3 | 0.207638920554 | 0.207638920554 | 0.2069275 (tail ~7e-4) |
| 5 | 0.575542714461 | 0.575542714461 | 0.5735666 (tail ~2e-3) |

+ λ₁ checked against the exact closed form `1 + γ/2 − log(4π)/2` to 6.96e-32.
min λ_n(true) over n = 1..60 is λ₁ = 0.0230957 > 0 (the implied-positivity baseline).

## Convention findings (important; corrects the mission's f_n)

The mission-specified `f_n(ρ) = 1 − (1 − 1/(ρ−1))^n` is **NOT** the Li per-zero sequence.
Exact B–L per-zero is `h_n(ρ) = 1 − (ρ/(ρ−1))^n = 1 − (1 + 1/(ρ−1))^n`; the mission's f_n equals h_n(2−ρ)
(= 1 − (1 + 1/(1−ρ))^n). In the mission convention the **true ζ already has λ₁ = Σ_ρ 1/(ρ−1) = −λ₁ = −0.0230957 < 0**
(verified: closed form and the 2000-zero sum = −0.02265). So f_n is not a positivity sequence; using it as prescribed
yields a **false-positive "flag" at n = 1 that also fires on the true ζ** — it tells us nothing about RH.

I computed it anyway (artifact block):
`mission λ₁(the true ζ) = −0.0230957 < 0`; `mission Δλ₁(offline) = −0.00497507`; `mission λ₁(planted) = −0.02807 < 0`.
This is a **FALSE-POSITIVE artifact**, not an RH-flag — flagged as such.

The two valid conventions give identical results: `std: g_n = 1 − (1 − 1/ρ)^n` and `bl: h_n = 1 − (ρ/(ρ−1))^n`
produce the same Δλ_n and the same λ_n(planted) at every n (both are valid per-zero splits of the same λ_n).

Also: **λ₁ = 0.0230957…, not 0.0923**. The 0.0923 in the prompt is λ₂ (n=2). Sign convention verified via the
closed form (positive, as required by the RH direction).

## Results (detail, t0 = zetazero(1) = 14.1347, bl convention)

| n | λ_n(true) | Δλ_n(offline) | λ_n(offline planted) | Δλ_n(shift) | Δλ_n(swap) |
|---|---|---|---|---|---|
| 1  | 0.0230957  | +0.0049751  | 0.0280708  | −0.0002054  | −0.0027374 |
| 2  | 0.0923457  | +0.0198757  | 0.1122214  | −0.0008195  | −0.0109299 |
| 5  | 0.5755427  | +0.1231514  | 0.6986941  | −0.0050346  | −0.0674464 |
| 10 | 2.2793394  | +0.4775350  | 2.7568744  | −0.0189178  | −0.2576442 |
| 20 | 8.7692769  | +1.6834490  | 10.452726  | −0.0578826  | −0.8498203 |
| 60 | 57.781650  | +2.9296908  | 60.711341  | +0.1534632  | +1.0131252 |

Key observation: **Δλ_n(offline) > 0 for every n ≤ 60** — the off-line β=0.9 implant *raises* λ_n throughout,
so λ_n(planted) = λ_n(true) + Δλ_n stays strictly positive. The plant is invisible at n ≤ 60.
The on-line controls also stay positive (they only lower λ_n slightly, well within the positive margin).

Cross-model consistency: Δλ₁(offline) = +0.00497507 equals the Δ = 0.004975 documented in
`jensen_honest_probe.py`'s corr_factor docstring (sum 1/ρ_p − sum 1/ρ_m). The two probes agree on the same plant.

## At what n does it actually flag? (CONJECTURED)

By Li's theorem the FE-symmetric planted model has an off-line zero ⇒ **∃n: λ_n(planted) < 0** (PROVEN existence).
The flag is driven by the reflected partner zero `1−β+it0 = 0.1+it0`, whose per-zero factor
`|ρ/(ρ−1)| = 1.00135` grows like (1.00135)^n and overtakes λ_n(true) ≈ (n/2)log n.
Using the exact Δλ_n and a two-term fit λ_n(true) ≈ (n/2)log n + (−1.0879)n
(rel. err ≤ 0.9% at n = 30..60, anchored to exact values), the first negative appears at **n\* ≈ 4.4×10³**.
**CONJECTURED**: λ_n(true) is extrapolated by the fit beyond n=60; the flag's existence is PROVEN, only n\* is estimated.

## Honest framing (mission item 4)

This run tests the **sensitivity** of the Li-coefficient equivalence to a *local single-zero* violation,
**not RH itself**. Findings: finite truncations of Li's criterion (n ≤ 60) carry essentially no power against a
single off-line implant — they cannot separate true ζ from the planted model, and the numerical margin between
true, off-line-planted, and on-line-control λ_n is small. RH ⟺ λ_n ≥ 0 ∀n is a global criterion; the sensitivity
to an off-line zero at height t0 only switches on around n ~ (horizontal zero scale), here n\* ≈ 4.4×10³.
This is a documented, honest baseline: **the first rung of the Li-coefficient falsification harness does not flag
at n ≤ 60**, and the corrected per-zero convention (not the prompt's f_n) is the one that carries Li's theorem.

## Files / run
- Tool: `tools/li_coefficient_harness.py` — `uv run --with mpmath python3 tools/li_coefficient_harness.py` (~2.5 min).
- Reuses: model from `tools/jensen_honest_probe.py`, λ_n(true) series core from `tools/li_probe.py`.
- Input: `tools/data/zeros_verified_32k.txt` (−3 root: first 2000 + 20000 zeros for cross-checks).

## Next steps
- Sweep β ∈ {0.6, 0.7, 0.8, 0.95, 0.99}: the flag n\* should shrink as the reflected partner (1−β) approaches 0;
  this maps the sensitivity curve of the Li criterion.
- Compute exact λ_n(planted) past n=60 with an exact (non-asymptotic) method to firm up n\* from CONJECTURED to CHECKED.
