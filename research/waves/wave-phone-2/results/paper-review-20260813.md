# Paper review pass — working state (interruption-proof)

Date: 2026-08-13. Paper: `paper-main.tex` (6 pages), author Vstalin Grady.
This file is the SINGLE SOURCE OF TRUTH for the review/publish phase. Restore from here if a session dies.

## Status at this file's last write
- [x] Citations verified programmatically (CrossRef + arXiv), all 7 real, DOIs added. Commit 187d934.
- [x] Reviewer 3 (clarity/venue) COMPLETE — full output below.
- [x] Claim-verification agent COMPLETE — findings below (3 real issues + 1 unverifiable).
- [ ] Reviewer 1 (soundness) — running, agent ID 6600c438-45cf-4cf.
- [ ] Reviewer 2 (novelty/positioning) — running, agent ID a1010323-a3bc-47d.
- [ ] Meta-review synthesis + apply fixes + recompile + arXiv prep.

## Agent IDs (current run)
- Verifier: 47a1b25c-a906-4df (completed)
- Reviewer 1 (soundness): 6600c438-45cf-4cf
- Reviewer 2 (novelty): a1010323-a3bc-47d
- Reviewer 3 (clarity): 7e2e8a9b-34f0-418 (completed, output captured below — was NOT lost)

## ISSUES FOUND SO FAR (must fix before publish)

### A. Theorem 1 script mismatch (verifier, adversarial flag)
`scripts/attack_bound_check.py` does NOT literally print 0.6732660791400006829.
- Its hardcoded headline uses eps=8060, psum=1/220 → 0.6732628655 (OLD record).
- Its sweep uses float 0.008065 → 0.6732660791400006824, diverges at digit 19 (...829 vs ...824).
- Paper's value reproduced only by exact-rational 8065/1e6, matches ledger.md to 37 digits.
- **Number is CORRECT, but cited script does not literally produce it. FIX: update script to compute eps=8065e-6 exact-rational and print it.**

### B. Parameter label inconsistency (verifier)
Paper says (α,P,m)=(1.49, 1/1320, 133) and "psum 1/1320", but τ formula needs psum=1/220 (=6/1320).
- P (mollifier length) and psum (pair-weight sum) are CONFLATED in the paper.
- With psum=1/1320 the bound is 0.6769, not the record.
- **FIX: distinguish P from psum in the paper text. psum=1/220, P=1/1320.**

### C. Theorem 3 rounding (verifier)
"C ≤ 1.3277" gives 0.83615, not 0.83621. Stated 0.83621 needs C ≤ 1.327579.
- **FIX: state C ≤ 1.32758 (or give the exact C value 1.3275781) so 0.83621 follows.**

### D. Unverifiable numbers (verifier)
min-gap 0.0188 and small-gap exponent 3.06 have NO saved output anywhere.
- 10M/21M zero data lives on the LAPTOP (/home/vstaln/ff21m/), not on phone.
- ledger.md:130 records a DIFFERENT 924k-run exponent 3.81±0.18.
- **FIX: either regenerate these numbers with a saved script, or drop them from the paper.**
- NOTE: the stats table values (m3, T-mean, T-min, ρ1) match `make_figures.py` comments verbatim, so those are fine.

## Reviewer 3 (clarity/venue) — FULL OUTPUT
```json
{
  "summary": "This 6-page preprint reports a certified lower bound κ ≥ 0.6732660791 inside a self-defined \"certificate class\" of bandwidth one, a machine-checked ceiling κ ≤ 0.6818312306 for that class, and a \"proved\" simple-zeros bound 0.83621, plus numerical probes of Li's criterion and zero statistics to height 10^7. As written it is a results summary, not a paper. The actual certificate — polynomial F, verifier, derivation — is deferred to a never-named \"companion repository.\" The central Section 2 formula is rendered with scrambled tokens, several symbols are undefined or collide, and the \"proved\" theorems rest on unstated constants (C ≤ 1.3277) or an unconstructed witness. For math.NT this would not survive a first pass without major revision; the epistemic honesty is the one real virtue.",
  "strengths": [
    "Honest three-way labeling (proved / machine-checked / numerically certified / empirical) is genuinely unusual and valuable.",
    "The structural-ceiling framing — the class certifies 0.6733 yet cannot exceed 0.6818, so improvement requires a class change — is a potentially interesting conceptual contribution if the witness is valid.",
    "The remark that a distinct-zeros bound cannot by itself lift s1 past 2/3 shows awareness of the sharpness obstruction."
  ],
  "weaknesses": [
    "Headline result is not reproducible. The certificate (polynomial F, verifier, full derivation) is in a companion repository that is never named or linked.",
    "Finite-grid certification is not a proof. 'Checked in interval arithmetic on a finite grid' certifies a continuum only with a covering/Lipschitz/branch-and-bound argument, which is absent.",
    "Section 2 formula under-specified: κ ≥ (H(α)−τ)/(1−B/m) — the exponent c in τ = p_sum/m^c is never defined, Φ_m is named but not given, factor 127 in B = Φ_m(ε·127) unexplained.",
    "The 'Proved' theorems are asserted, not proved. Theorem 3 hinges on C ≤ 1.3277 with no derivation; Theorem 2's witness and the 1/(6·256²) defect are stated, not constructed.",
    "Undefined table symbols: Section 6 table reports T-mean, T-min, ρ1, m3 before T, ρ1, G, K2 are defined; ρ1 is never defined anywhere.",
    "Figures never referenced in body text; captions depend on undefined symbols (T, m3, ρ1).",
    "Notation collisions: c is the exponent in m^c but also 'c = 3' in Section 4; ρ1 in Li criterion is 1/ρ (extraction artifact).",
    "Sections 5 and 6 are disconnected empirical appendices with unclear relevance."
  ],
  "questions": [
    "Where is the companion repository? Provide URL and hash, and the certificate polynomial F.",
    "What is c in τ = p_sum/m^c, and what is Φ_m concretely?",
    "How is C ≤ 1.3277 established, and where is the proof of Theorem 3?",
    "What are T and ρ1 precisely, and is the floor T ≥ 1/3 a theorem or an observation?",
    "Does the Theorem 2 witness satisfy every class constraint, and how is 'machine-checked' verified independently?"
  ],
  "missing_references": [
    "The companion repository (URL/DOI)",
    "Montgomery (pair correlation) — the form-factor input",
    "Bombieri–Lagarias (the substitution used in Section 5)",
    "LMFDB (zero validation)",
    "A source for the GUE form-factor third moment / unfolded matrix G",
    "A source for the Stieltjes-constants computation"
  ],
  "soundness": 2,
  "presentation": 2,
  "contribution": 2,
  "overall": 3,
  "confidence": 4
}
```

## Verifier — FULL FINDINGS (verbatim summary)
Thm 1: PARTIAL — matches ledger to 37 digits but cited script doesn't emit it (uses old eps=8060 / float 0.008065).
Thm 2: MATCH (0.68183123059534187426) and p0 MATCH (0.68182868746383147426).
Thm 3: MATCH w/ tension — "C ≤ 1.3277" gives 0.83615, not 0.83621 (needs C ≤ 1.327579).
λ1 = 0.023095708966121033814: MATCH (li_probe.py cross-check line).
λ1..λ12 positive: MATCH (all 12 positive; first negative at n=92).
m3 / T-mean / T-min / ρ1: MATCH-to-comment (make_figures.py verbatim).
Full-set 4.73090±0.00023, 330,209 blocks: MATCH-to-comment (21133383/64=330209.1).
5/12≈0.4167: MATCH.
min gap 0.0188 + exponent 3.06: UNVERIFIABLE (no saved output; data on laptop).

## FIX PLAN (apply after Reviewer 1 & 2 return)
1. Fix attack_bound_check.py to compute eps=8065e-6 exact-rational and print headline (so script literally emits the paper's number).
2. Disambiguate P vs psum in paper text (psum=1/220 = 6/1320; P=1/1320).
3. Fix Theorem 3 constant: state C ≤ 1.32758 (or exact 1.3275781) so 0.83621 follows.
4. Regenerate-or-drop min-gap 0.0188 and exponent 3.06.
5. Define table symbols before use (T, ρ1) and reference figures in text.
6. Add missing refs: Montgomery pair correlation, Bombieri–Lagarias, LMFDB, GUE form factor source.
7. Name/link the companion repository (the riemann git repo) in the paper.
8. Recompile, re-verify, copy to Downloads, commit.

## Files
- Paper tex: /root/riemann/research/waves/wave-phone-2/results/paper-main.tex
- Plain text: /data/data/com.termux/files/home/.tmp/paper-main.txt
- Verifier script: /root/riemann/research/waves/wave-phone-2/scripts/attack_bound_check.py
- Li probe: /root/riemann/tools/li_probe.py
- Figures script: /root/riemann/tools/make_figures.py
- This file: /root/riemann/research/waves/wave-phone-2/results/paper-review-20260813.md
