# Adversarial Re-verification: marked-windowed m₃ separation (superlaw-s3)

**Date:** 2026-08-17. **Author:** main loop (independent implementation).
**Status:** SEPARATION REPRODUCED (CHECKED NUMERICALLY, fresh code); two honesty
corrections required before the new certificate class is claimed.

## What was re-verified and why

The `superlaw-s3` note (wave-phone-2) claims a **new certificate class opens**: any
certificate whose validity hypothesis reads "marked-windowed m₃ = 5 ± ε" (ε < 2) excludes
the entire super-law (256-law-sibling) adversary family, because that family's marked m₃ ≈ 8
≫ the real zeros' ≈ 5. The ledger flagged: **"box independent re-verification DID NOT run."**
This note is that missing independent re-verification — fresh script, fresh seed, fresh
block size, own GUE sampler, real-zeros leg on LMFDB data.

**Script:** `research/notes/adversarial-m3-reverify-2026-08-17.py` (written 2026-08-17,
independent of wave-phone-2 implementations; GUE sampler n=300 K=40 seed=99; wave used
n=500 K=60 seed=42). **Command:** `uv run --quiet --with numpy python3
research/notes/adversarial-m3-reverify-2026-08-17.py`

## Numbers (all from the script above)

| quantity | independent run | wave-phone-2 claim | verdict |
|---|---|---|---|
| super-law marked m₃(1/2) raw | 7.054 ± 0.041 | 7.108 | ✓ |
| super-law marked m₃(1/2) bias-corr | **7.935 ± 0.041** | 7.978 | ✓ reproduced (~0.5%) |
| super-law marked m₃(2/3) raw | 4.858 ± 0.033 | 4.866 | ✓ |
| super-law marked m₃(2/3) bias-corr | **5.348 ± 0.033** | 5.359 | ✓ reproduced |
| pure-GUE finite-n deficit (1/2) | −0.881 | −0.870 | ✓ |
| pure-GUE finite-n deficit (2/3) | −0.489 | −0.492 | ✓ |
| real zeros m₃(1/2) (52,800 LMFDB, windowed 2000) | 5.373 ± 0.378 (SE 0.075) | ≈5 sine | ✓ within window noise |
| real zeros m₃(2/3) | 3.466 ± 0.244 | 3.25 | ✓ within window noise |
| simple fraction of constructed super-law | 0.67897 | p₀ = 0.68183 | ✓ construction valid |

**Verdict line (script-printed):** `SEPARATION REPRODUCED: YES` — at both λ, real zeros ≈
sine value (within 10%) and super-law separated from real zeros by > 5σ.

## Honesty corrections (REQUIRED before the new class is claimed)

1. **CONDITIONALITY of "m₃ = 5 PROVEN".** The superlaw-s3 note labels real-zero m₃ = 5 as
   "PROVEN (Rudnick–Sarnak λ<2/3)". But `attack-ceiling.md` §7.5(e) (repo's own record)
   states: *"Under RH the triple correlation is a theorem (Hejhal 1994; RS96) but only in
   kλ < 2."* So:
   - The sine-kernel **value** m₃(1/2) = 5, m₃(2/3) = 13/4 is an unconditional closed form
     (GUE limit). PROVEN.
   - The **real zeros attaining it** is PROVEN only **conditional on RH** as a theorem;
     **empirically** ≈5±0.5 (finite-window noise; wave's first-1000 measurement 4.802,
     mine 5.373 across heights — both within ±0.5 of 5).
   - Consequence for the certificate: the m₃ read must be treated as a **numerical
     enclosure input** (like EnclOK rows), i.e., "marked-windowed m₃ of the real zeros =
     5 ± ε_real with a rigorous enclosure bound", NOT as an unconditional theorem.
   - Gap analysis for ε: separation gap ≈ 2.9 (super-law 7.9 vs real 5.0); window noise
     ≈ 0.5; so ε = 1.0 is safely below the gap and above the noise. A rigorous m₃-enclosure
     with ε_real < 1.0 is the required certificate input.
2. **THEORY-FORMULA DISCREPANCY adjudicated.** The note's marked-m₃ theory value is 8.148;
   my first-principles derivation (marks-only, no density rescale) gives 7.69. Direct
   measurement (7.94 bias-corrected) confirms the note's convention: the super-law
   construction rescales points to mass-density 1 (x → x·Em, Em = 1.189), which shifts the
   effective kernel λ → λ·Em, inflating m₃. My 7.69 used the non-rescaled convention and
   is therefore a different quantity, not a contradiction. **Adjudicated:** the measured
   7.94 sits within ~2.5% of the note's 8.148 theory; the separation verdict is robust to
   either convention (both ≫ 5).

## What this buys (next lever, NOT yet done)

The separation says: configs with marked m₃ ≈ 5 and p₁ near p₀ = 0.6818 do not exist in the
near-CUE marked family — the pinned bottom (D + 3u = 5.4419/3.9825, attack-law-s3) already
shows any near-CUE marked law with p₁ = p₀ has marked m₃ ≥ 5.44 ≫ 5. Therefore a
certificate that reads **marked m₃ = 5 ± ε** (ε < 0.44) excludes every p₀-level adversary,
and its in-class ceiling may lie strictly above 0.6818.

**The concrete next step (open lever):** formulate the marked-m₃ read inside the existing
LP-dual certificate (the same machinery behind `lpdual-realconfig-check` / the Lean 256-law
ceiling), add the m₃ = 5 ± ε constraint with a rigorous ε, and compute the new in-class
ceiling. If it exceeds 0.6818 + |E(1)|, that is a genuine unconditional improvement over
the current certified 0.673481. This requires: (a) a rigorous marked-m₃ enclosure for the
real zeros (finite window + explicit error terms — the EnclOK-style treatment), (b) the LP
with the m₃ constraint (a third-moment constraint on the marked measure).

## Labels

- **CHECKED NUMERICALLY** — separation reproduced, all table numbers (script + command
  cited above).
- **PROVEN (unconditional)** — sine-kernel closed forms m₃(1/2) = 5, m₃(2/3) = 13/4
  (GUE limit values; attack-twobandwidth §2 re-verified in repo).
- **PROVEN (conditional on RH)** — real zeros' triple correlation = GUE (Hejhal 1994; RS96,
  kλ<2), per `attack-ceiling.md` §7.5(e).
- **CONJECTURED** — that a marked-m₃-reading certificate's in-class ceiling exceeds 0.6818
  (needs the LP computation above).
- **CORRECTION FILED** — superlaw-s3 note's "PROVEN (Rudnick–Sarnak)" label overstated
  unconditionality; see §"Honesty corrections".

## Files

- This note: `research/notes/adversarial-m3-reverify-2026-08-17.md`
- Script: `research/notes/adversarial-m3-reverify-2026-08-17.py`
- Source data: `tools/argprinciple/data/lmfdb_zeros_*.txt` (52,800 zeros)
- Predecessor: `research/waves/wave-phone-2/results/superlaw-s3.md`
