# Marked-m₃-reading certificate: LP formulation + bounded probe (2026-08-17)

**Status: COMPLETE.** **Verdict: NO — the computation does NOT establish an in-class ceiling above 0.6818.** The m₃ read (ε < 0.44) robustly destroys the old ceiling's adversary mechanism (the p₀-level near-CUE marked laws are excluded: measured m₃ ≈ 6.9–7.3 ≫ 5.44), but the restricted admissible class is not characterized: its min-p₁ member is undetermined, and the certificate cannot certify above it. The decisive missing input is a bound on the connected part T of near-CUE marked laws (identical to attack-law-s3 §5's frontier).
**Author:** builder (L4 certificate-builder).
**Task:** test whether a certificate that READS marked-windowed m₃ = 5 ± ε (ε < 0.44) has an
in-class ceiling strictly above the PROVEN wall 0.6818.

---

## 1. SPEC — the marked-m₃-reading certificate (LP formulation)

### 1.1 The certificate being extended (from tangent-lp-decisive / lpdual-realconfig-check)

The in-class certificate is an LP-dual (coboundary) certificate over near-CUE marked laws:

- **Decision variables:** the certificate's read parameters (l, c) = (law-level / coefficient
  perturbations) plus per-box dual variables κᵢ ≥ 0, qᵢ ≥ 0 (soundness rows). Concretely in
  `tools/adv_lp_loop_v3.py`: variables (l, c) with |c| ≤ 0.06, constraints
  `tangent_lower(l, c) ≥ eps` on each adverse box.
- **What the certificate reads (validity hypothesis H):** pair-correlation rows
  E|μ̂(j)|² = 256·S(j) = j for j = 1..255 (the Montgomery F ≡ 1 datum, PROVEN for the real
  zeros on [0,1]) + the simple-fraction parameter p₁.
- **Ceiling (PROVEN structural):** v*(p₁) = p₁ + |E(1)|, |E(1)| = 1/(6·256²) = 2.5431e-6,
  shadow price of p₁ = 1; ceiling = 0.68183123 attained at p₁ = p₀ = 0.6818287 (the 256-law's
  simple fraction). The 256-law sits at the LP feasibility boundary: the LP with pair-row
  reads is feasible up to p₁ = p₀, infeasible above (the record 0.673481 is the certified
  frontier; 0.6818 is not reachable by optimization, only by a new unconditional input).

### 1.2 The new read: marked m₃ = 5 ± ε

The marked-windowed third moment of a marked configuration class (from attack-law-s3 §2):

    S₃(law; λ) = Σ_c w_c (1/256) Σ_{i,j,k} m_i m_j m_k K_λ(x_i−x_j) K_λ(x_j−x_k) K_λ(x_k−x_i)

with the diagram decomposition per configuration: S₃ = D + pair + T,
  D = (1/256)Σ m_i³ = 4 − 3p₁ (multiplicity diagonal, position-free, exact),
  pair ∈ [3u, 6u], u(λ) = (1/256) Σ_m d_m (E|μ̂(m)|² − 256(2−p₁))  (two-equal),
  T = connected three-distinct part (free, unconstrained by any proven input).

**Pinned bottoms (PROVEN given pair rows + p₁):**
  λ=1/2: S₃ ≥ D + 3u + T = 5.4419 + T   (at p₁ = p₀)
  λ=2/3: S₃ ≥ 3.9825 + T               (at p₁ = p₀)

**Real zeros (empirical, windowed):** marked m₃ ≈ 5.0 (λ=1/2: 5.373 ± 0.378 on 52,800 LMFDB
zeros, windowed 2000; sine value 5 PROVEN unconditional as a GUE closed form). Separation
from the super-law adversary family ≈ 2.9 (super-law marked m₃ ≈ 7.9 bias-corrected vs real
≈ 5), reproduced independently (adversarial-m3-reverify-2026-08-17).

**The certificate reads m₃ = 5 ± ε as a validity constraint:** a law L is admissible for the
certificate only if its marked m₃ satisfies |S₃(L) − 5| ≤ ε. The real zeros satisfy this
(empirically, within window noise); every near-CUE marked law at p₁ = p₀ satisfies
S₃ ≥ 5.4419 + T — so for T ≥ −0.44 − ... (see below) the p₀-level adversaries are EXCLUDED.

### 1.3 What the m₃ constraint does in the LP

The certificate's proven lower bound is v*(p₁) = p₁ + |E(1)| with shadow price 1 on p₁. The
feasibility boundary p₁ ≤ p₀ is set by the 256-law: the law is a feasible point of the
pair-row constraints at p₁ = p₀, and no certified law exists above p₀ in-class.

Adding the m₃ read does NOT by itself change v*(p₁) = p₁ + |E(1)| (that functional is fixed).
The question is whether it moves the **max feasible p₁**: with the m₃ constraint active, the
admissible class is

    Class(p₁; ε) = { near-CUE marked laws with pair rows E|μ̂|² = m,
                     simple fraction p₁, |marked S₃(λ=1/2) − 5| ≤ ε }

If Class(p₀; ε) = ∅ (the 256-law and its siblings are all excluded because their m₃ ≥ 5.4419
> 5 + ε), then the boundary p₁ = p₀ no longer blocks; the question becomes the max p₁ for
which Class(p₁; ε) ≠ ∅, which sets the new ceiling v = p₁_max + |E(1)|.

**The key subtlety (to be checked in the probe):** the LP feasibility boundary is NOT simply
"does a law with those properties exist" — it is a duality condition. The probe below takes
the reductionist approach: compute the max p₁ such that a law in the reduced family with
marked m₃ ∈ [5−ε, 5+ε] exists, and report how that compares to p₀ = 0.68183. This is a
necessary condition for the ceiling to move (existence of an admissible class), not a full
duality certificate. Explicit caveat will be labeled.

### 1.4 What belief the computation changes

If the probe shows the max admissible p₁ (with m₃ ∈ [5−ε, 5+ε]) is strictly ABOVE p₀ =
0.68183, then the m₃ read opens the possibility of an in-class ceiling above 0.6818 —
upgrading the CONJECTURE to a FUNDED conjecture (and the exact LP, with the m₃ constraint
as a row, would be the next decisive computation). If the probe shows max p₁ ≤ p₀, the
ceiling does not move within the reduced family (negative result, reported straight).

---

## 2. Code + command (FILLED)

- **Script:** `research/notes/marked-m3-certificate-LP-2026-08-17.py` (self-contained numpy;
  canonical machinery read: `tools/lpdual_realconfig_check.py`; conventions from
  `research/notes/adversarial-m3-reverify-2026-08-17.py`).
- **Main command:**
  ```
  cd /home/vstaln/riemann && uv run --quiet --with numpy python3 research/notes/marked-m3-certificate-LP-2026-08-17.py
  ```
  wall 81 s (GUE block sampling dominates; within the <5 min budget).
- **Robustness snippet** (3 seeds × p₁ targets + no-rescale reference), 60 s, §6.

## 3. Results table (FILLED — all from §2 commands)

### 3A. Exact pin — D(p₁) + 3u(p₁) vs p₁ (flat ENSEMBLE rows, projection kernel, m=0 mass 65536)

| λ | D+3u at p₁ ∈ {0.50, 0.60, p₀, 0.75, 0.90, 1.00} | spread | p₁-independent? |
|---|---|---|---|
| 1/2 | 5.4419 ×6 (identical) | 8.9e-16 | **True** |
| 2/3 | 3.9825 ×6 (identical) | 1.1e-15 | **True** |

(m0=0-flat variant gives −0.51: the m=0 mass term |μ̂(0)|² = 65536 is essential to the pin.)

### 3B. Real zeros (LMFDB, 52,800, all marks 1 → p₁=1 measurement convention, B=2000 windows)

| λ | windowed marked m₃ | sine | PIN bottom | gap to PIN (needs T ≈) |
|---|---|---|---|---|
| 1/2 | 5.373 ± 0.378 | 5.0 | 5.4419 | −0.069 |
| 2/3 | 3.466 ± 0.244 | 3.25 | 3.9825 | −0.516 |

(Matches the independent re-verification exactly: 5.373 ± 0.378 / 3.466 ± 0.244.) The real
zeros sit BELOW the pinned bottom (T ≈ −0.07 at λ=1/2, opposite in sign to the sine kernel's
A3 = +1/2) — within window noise (SE 0.378), no contradiction established; tension flagged.

### 3C. Synthetic near-CUE marked family: marked m₃ vs p₁ (GUE n=200 K=20, marks {1,2}, mass-density-1 rescale)

| target p₁ | realized p₁ | m₃(1/2) | m₃(2/3) |
|---|---|---|---|
| 0.60 | 0.585 ± 0.047 | 7.331 ± 0.066 | 5.122 ± 0.050 |
| p₀ | 0.684 ± 0.040 | 6.984 ± 0.079 | 4.780 ± 0.057 |
| 0.75 | 0.738 ± 0.040 | 6.674 ± 0.048 | 4.529 ± 0.034 |
| 0.90 | 0.910 ± 0.020 | 5.967 ± 0.052 | 3.905 ± 0.040 |
| 1.00 | 1.000 ± 0.000 | 5.550 ± 0.023 | 3.544 ± 0.017 |

**Trend:** m₃(1/2) decreases monotonically toward the sine value as p₁ → 1, but stays ABOVE
the ε=0.44 window [4.56, 5.44] at every p₁ (min over family = 5.550 at p₁ = 1.0, margin +0.11).
**No synthetic near-CUE marked law at ANY p₁ ∈ [0.585, 1.0] is admissible for ε ≤ 0.44.**
Robustness (§5): 3 seeds, all-simple end 5.550–5.622, p₀ end 6.88–6.96.

### 3D. Edge cases (task list)

| case | value | result |
|---|---|---|
| ε = 0.44 boundary | 5+0.44 = 5.44 < 5.4419 = PIN | boundary itself below the pinned bottom |
| ε = 0 | admissible laws need T ≤ 5 − 5.4419 = −0.4419 | needs strongly negative connected part |
| p₁ = p₀ | m₃(1/2) ≈ 6.9–7.3 (3 seeds); 256-law ≈ 7.9 (reverify) | robustly excluded (margin ≥ 1.4) |
| all-simple p₁ = 1 | 5.550–5.622 (mass-density-1); 4.073–4.127 (point-density) | **convention-dependent**: excluded at ε=0.44 in mass-density-1 (margin 0.11–0.18), admissible in point-density |


---

## 4. VERDICT (FILLED — honest)

**Ceiling > 0.6818? NO — not established.**

1. **What the computation shows (positive, CHECKED NUMERICALLY):** the m₃ read with ε < 0.44
   excludes the ENTIRE near-CUE marked family at p₁ ≤ p₀ — measured m₃(1/2) ≈ 6.9–7.3 at
   p₁ ≈ p₀ (3 seeds), pinned bottom 5.4419 p₁-independent (exact, §3A), 256-law's own ≈ 7.9
   (reverify). The old ceiling's adversary mechanism (a flat-row law at p₁ = p₀) is destroyed.
   This sharpens the separation: not just "the p₀ law is excluded" but "no near-CUE marked law
   at any p₁ ≤ p₀ reaches m₃ = 5 ± 0.44".
2. **What it does NOT show:** that the new in-class ceiling exceeds 0.6818. The restricted
   class {flat rows + m₃ ∈ [5−ε, 5+ε]} is NOT empty (the real zeros, m₃ = 5.373 ± 0.378, are
   in it), but its **min-p₁ member is not characterized**: within the sampled family m₃
   approaches the sine value only as p₁ → 1 (all-simple), so the restricted class appears to
   live at high p₁ — which would RAISE the ceiling — but this is CONJECTURED. A certificate
   cannot certify p₁ ≈ 1 without proving the zeros' multiplicity structure (the target
   itself); the empirical all-simple low range is not a theorem.
3. **The decisive missing input** (identical to attack-law-s3 §6): a **provable bound on the
   connected part T** of near-CUE marked laws, or on min p₁ over {flat rows + m₃ ∈ [5−ε, 5+ε]},
   or a rigorous marked-m₃ enclosure for the real zeros **with true multiplicities** (this
   probe's real-zero leg uses the all-marks-1 convention, i.e. p₁ = 1 measurement convention —
   not the certificate's p₁). None is available; the ceiling question is **INCONCLUSIVE at the
   LP level**, and the claimed improvement is **CONJECTURED, not supported** by this
   computation.

## 5. Robustness snippet (3 seeds × p₁ targets; no-rescale reference)

Command:
```
cd /home/vstaln/riemann && uv run --quiet --with numpy python3 -c "<inline snippet: GUE n=200 K=20, marks {1,2}, mass-density-1 rescale, m3(1/2) per p1 target>"
```
Output:
```
seed  7: | p1~0.68: 6.905+/-0.046 | p1~0.91: 6.030+/-0.044 | p1~0.94: 5.790+/-0.041 | p1~1.00: 5.550+/-0.023
seed 42: | p1~0.68: 6.884+/-0.063 | p1~0.89: 6.040+/-0.063 | p1~0.95: 5.778+/-0.032 | p1~1.00: 5.551+/-0.027
seed 99: | p1~0.69: 6.958+/-0.076 | p1~0.89: 6.148+/-0.046 | p1~0.96: 5.834+/-0.040 | p1~1.00: 5.622+/-0.030
```
No-rescale all-simple reference (pure-GUE point-density convention): m₃(1/2) = 4.073–4.127
(3 seeds) — the convention sensitivity at the p₁ = 1 end; also reproduces the reverify's
pure-GUE finite-n deficit (−0.881 ⇒ 4.119 at n=300 seed 99).

## 6. Honesty labels (FILLED)

- **PROVEN (exact, this probe):** p₁-independence of the diagonal+pair bottom D(p₁)+3u(p₁) =
  5.4419 (λ=1/2) / 3.9825 (λ=2/3), spread ≤ 1.1e-15 (§3A); the m=0 mass |μ̂(0)|² = 65536 is
  required for the pin.
- **CHECKED NUMERICALLY (this probe):** real-zeros windowed m₃ = 5.373 ± 0.378 (1/2), 3.466 ±
  0.244 (2/3) — matches the re-verification exactly; synthetic family m₃-vs-p₁ (§3C) and its
  exclusion of the ε=0.44 window at every p₁ (3-seed robustness); edge cases (§3D).
- **CONJECTURED (not established):** that the m₃-reading certificate's in-class ceiling
  exceeds 0.6818 — the probe's headline negative; the restricted class's min-p₁ lives at high
  p₁ (the family reaches m₃ ≈ 5 only as p₁ → 1), which would raise the ceiling IF a theorem
  certified it.
- **TENSION FLAGGED (no contradiction established):** real-zeros m₃ = 5.373 sits 0.069 BELOW
  the pinned bottom 5.4419 (requires T ≈ −0.07, opposite in sign to the sine kernel's
  A3 = +1/2) — within window noise (SE 0.378). Also: the all-simple end's admissibility is
  convention-dependent (mass-density-1: 5.55 excluded; point-density: 4.07 admissible) — the
  exclusion of the p₁ ≤ p₀ end is robust to this; the p₁ ≈ 1 end is not.
- **INCONCLUSIVE:** the LP-level ceiling for the m₃-reading certificate (requires the missing
  third-order input of attack-law-s3 §6; also requires a multiplicity-carrying marked-m₃
  enclosure for the real zeros, not the all-marks-1 convention).

## 7. Files

- This note: `research/notes/marked-m3-certificate-LP-2026-08-17.md`
- Probe: `research/notes/marked-m3-certificate-LP-2026-08-17.py`
- Predecessors: `adversarial-m3-reverify-2026-08-17.md` (separation re-verified),
  `attack-law-s3.md` (pin D+3u, marked S₃ diagram), `lpdual-realconfig-check.md`,
  `tangent-lp-decisive-2026-08-14.md` (LP ceiling, path closure).
