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

---

## Reviewer 1 (soundness) — FULL OUTPUT [agent 6600c438, completed]
```json
{
  "summary": "The paper's central object — a 'bandwidth-one Levinson–Conrey certificate class' — is never defined precisely enough to judge the theorems. The pivotal input, 'a prescribed pair-correlation form factor on [0,1]' (glossed as 'a fixed two-point statistic E(1)'), is either a restriction on the mollifier (unconditional) or the actual two-point statistic of the zeta zeros (conditional on Montgomery's pair correlation). The wording 'two-point statistic' implies the latter, in which case Theorem 1's 'κ ≥ 0.6732660791' is a conditional, certificate-defined statistic dressed in the notation of the unconditional proportion κ, making the comparison to 5/12 misleading. Theorem 3 is labeled 'Proved' but rests on C ≤ 1.3277 with unstated provenance; if C is certified rather than proved, the label is false. Theorem 2's ceiling is a feasibility claim whose witness, machine-checking system, and the derivation of the 1/(6·256²) 'discretization defect' are all missing or asserted.",
  "weaknesses": [
    "Certificate class is hand-waved: the 'pair-correlation form factor on [0,1]' is never defined, so it is impossible to tell whether Theorem 1 is unconditional (mollifier restriction) or conditional (assumes pair correlation of zeros).",
    "Theorem 1 writes 'κ ≥ 0.6732660791' using the same κ as the unconditional proportion; if the class assumes a conjectural input, this is not a bound on κ and 'above 5/12' is an invalid comparison.",
    "Theorem 3 labeled 'Proved' but rests on 'C ≤ 1.3277' whose provenance is never stated.",
    "The ceiling correction 1/(6·256²) is asserted with no derivation (no Lipschitz constant, no grid, no error bound).",
    "Ceiling conflates the witness's 'simple-point fraction p0' with the value of the certified-bound functional; no computation shows the functional ≤ 0.6818312306 at the witness.",
    "The witness configuration and machine-checking system (Coq/Lean/Isabelle?) are never specified.",
    "Distinct-count formula Nd ≥ (3−C)/2·N appears with no derivation.",
    "'The class is closed in every parameter' is a Nelder–Mead proxy search claim, not a proof of closure."
  ],
  "questions": [
    "Is the bandwidth-one form factor a restriction on the mollifier (unconditional) or the actual pair-correlation of zeta zeros (conditional)? This determines the validity of everything.",
    "What system performed the machine-check, and where is the witness configuration?",
    "Is C ≤ 1.3277 proved or numerically certified, and of which norm exactly?",
    "Derive the 1/(6·256²) defect: what grid, what Lipschitz/second-order bound?",
    "Where is the companion repository and its revision hash?"
  ],
  "missing_references": ["Montgomery (1973)", "machine-checking system + proof artifact", "companion repo URL+hash", "source of C ≤ 1.3277 and (3−C)/2 inequality", "published unconditional simple-zeros record"],
  "soundness": 2, "presentation": 2, "contribution": 2, "overall": 3, "confidence": 4
}
```

## Reviewer 2 (novelty/positioning) — FULL OUTPUT [agent a1010323, completed]
```json
{
  "summary": "The paper's central claim — a 0.6733 lower bound that sits 'above every published unconditional constant' — is a category error. The certificate class takes the pair-correlation form factor on [0,1] as an INPUT constraint; that is Montgomery's pair-correlation conjecture, not a proven fact. So 0.6733 is a conditional/empirical statistic and is not comparable to the unconditional 5/12 of PRZZ. Worse, Montgomery (1973) already gives (conditionally on pair correlation) κ ≥ 2/3 ≈ 0.6667, so 0.6733 is a hair above a 1973 conditional benchmark, not a new regime. The 0.83621 simple-zeros theorem is labeled 'Proved' but must inherit the same conjectural C ≤ 1.3277 input; unconditionally it is not credible. The 0.6818 ceiling bounds the author's own relaxed class, which is not shown to faithfully model the real Levinson–Conrey optimization, so 'structural gap' is vacuous for the actual problem. The Li section is a standard, decades-old computation.",
  "weaknesses": [
    "0.6733 is not comparable to 5/12. The class's second constraint is 'a prescribed pair-correlation form factor on [0,1]' — Montgomery's pair-correlation conjecture. Claiming 'above every published unconditional constant' is misleading.",
    "Theorem 3 ('Proved', 0.83621 simple zeros) is mislabeled. A positive proportion of SIMPLE zeros is not known unconditionally. Either conditional (relabel) or an unconditional proof of a major open statement (unbelievable).",
    "Failure to cite Montgomery (1973), who under pair-correlation proved κ ≥ 2/3 (and ≥ 2/3 simple). Against this, 0.6733 and 0.83621 are modest incremental refinements, not records. Positioning silently wrong by choosing 5/12 as baseline.",
    "The 0.6818 ceiling bounds an ad-hoc class NOT shown to be a faithful relaxation of the true Levinson–Conrey feasible set. Unless faithfulness is proved, 'structural gap' says nothing about the real problem.",
    "The 'machine-checked' ceiling carries a hand-asserted 1/(6·256²) correction that is not machine-checked.",
    "The Li section adds nothing: λ1 = 1 + γ/2 − (log 4π)/2 is textbook; λ1..λ12 positivity and n≈90 ill-conditioning computed by Keiper, Coffey, Maslanka decades ago."
  ],
  "questions": [
    "What exactly is the 'form factor E(1)' and where is it PROVEN for ζ(s)? If Montgomery's conjecture, why is Theorem 1 not labeled conditional?",
    "Is the certificate class a faithful relaxation of the actual Levinson–Conrey optimization?",
    "Is Theorem 3 unconditional? If yes, provide the unconditional proof of C ≤ 1.3277; if no, relabel and compare against Montgomery's conditional 2/3.",
    "Where is the companion repository and verifier? Does the ceiling still hold without the hand-added defect correction?",
    "Does 0.83621 follow from the on-line machinery, and what is the exact conditional status of each ingredient?"
  ],
  "missing_references": ["Montgomery (1973) pair correlation", "Montgomery–Odlyzko / Dyson GUE form factor", "Heath-Brown (1979) simple zeros", "Conrey–Ghosh–Gonek simple zeros", "Goldston–Gonek–Montgomery / Hughes–Rudnick", "Rudnick–Sarnak", "Bombieri–Lagarias (1999) Li criterion complements", "Coffey & Maslanka (λn numerics)", "Farmer–Gonek–Hughes"],
  "soundness": 2, "presentation": 2, "contribution": 2, "overall": 3, "confidence": 4
}
```

## CRITICAL DECISIVE QUESTION (all 3 reviewers + verifier converge here)
Is the "pair-correlation form factor on [0,1]" / "two-point statistic E(1)" input to the certificate class:
(a) a PROVEN/unconditional restriction (on the mollifier), or
(b) Montgomery's pair-correlation CONJECTURE (conditional)?
If (b): the paper's positioning collapses — 0.6733 is conditional, and Montgomery 1973 already gives κ ≥ 2/3 ≈ 0.6667 conditionally, so 0.6733 is a hair above a 1973 benchmark, NOT "above 5/12".
This MUST be resolved from the actual math source files before any fix is applied.

---

# META-REVIEW (orchestrator synthesis, 2026-08-13)

## The decisive question — RESOLVED from source
Reviewers asked: is the "pair-correlation form factor on [0,1]" input (a) unconditional or
(b) Montgomery's pair-correlation conjecture (conditional)?

RESOLUTION from repo source (verify_cos7.py, laptop-family.md, ceiling-breaker-proposal.md):
- The certificate reads ONLY {mean density, form factor F on [0,1], multiplicity integrality}.
- E(1) = -1/(6N²) is the CUE/GUE form factor of the certificate's OWN admissible law — a
  closed-form model object (PROVEN-BY-ARGUMENT, laptop-family.md:42), NOT the actual zeros'
  pair correlation.
- The moments m_k(lambda) are PROVEN unconditionally via Rudnick–Sarnak (k*lambda < 2).
- The conjectural input in Levinson-type methods is the Hardy–Littlewood PRIME-pair conjecture
  (HL*), which gates mollifier length beyond theta = 4/7 (the proven fourth-moment barrier,
  Ingham). It is NOT Montgomery's zero-pair conjecture.
- The 0.6733 bound is a "simple-on-line" quantity inside a weighted Levinson integral, certified
  numerically (CHECKED NUMERICALLY), NOT a hand-proven theorem. sota-online-bound-audit.md:26
  already states this honestly.

VERDICT on reviewers' positioning criticism:
- Reviewer 2's claim "Montgomery 1973 gives kappa >= 2/3 conditionally" is FALSE — Montgomery's
  pair-correlation work is about zero SPACING, not proportion-on-line. There is no such theorem.
  Reviewer 2 hallucinated a benchmark.
- Reviewer 2's claim "a positive proportion of simple zeros is not known unconditionally" is
  FALSE — Levinson's method proves > 1/3 simple-on-line unconditionally (that IS the method).
- Reviewer 2's claim that "the form factor = Montgomery's conjecture" is FALSE per the repo
  source (it's the admissible-law form factor).
- BUT the reviewers are RIGHT that the paper must define the class precisely and must not
  overclaim. The paper itself is honest (says "current unconditional record 5/12" and shows it
  "for scale" in Fig 1) — it does NOT say "above every published constant". My own summary to
  the reviewers overclaimed this, not the paper.

## THE REAL ERROR FOUND (all reviewers + verifier missed it; orchestrator caught it)
**0.83621 is a DISTINCT-zeros bound (N_d = s1+s2+2p), NOT a simple-zeros bound.**
- paper-main.tex abstract line: "at least 0.83621 of the zeros are simple" — WRONG.
- paper-main.tex Theorem 3: "At least 0.83621 of the nontrivial zeros of ζ(s) are simple" — WRONG.
- Section 4 correctly says N_d >= (3-C)/2 * N and then warns "a bound on N_d does not by itself
  lift s1 past 2/3". The abstract + Thm 3 CONTRADICT Section 4.
- Ledger.md:126: C = 1.3275781 exactly, (3-C)/2 = 0.83621095. Honest statement: "C <= 1.32758"
  (not 1.3277, which gives 0.83615).
- This is a major honesty fix. 0.83621 distinct is still a real result (beats 5/6 = 0.8333 by
  +0.00288) but it is NOT "0.83621 simple".

## Reviewer score consensus
soundness 2/4, presentation 2/4, contribution 2/4, overall 3/10 — driven mostly by the
under-specified class + the simple/distinct mislabel + provenance gaps.

## FINAL FIX LIST (updated, ordered)
1. [CRITICAL] Fix abstract + Theorem 3: "0.83621 simple" -> "0.83621 distinct on-line"
   (N_d = s1+s2+2p); state C <= 1.32758 (not 1.3277).
2. Fix attack_bound_check.py to compute eps=8065e-6 exact-rational and print the headline
   (script must literally emit 0.6732660791...).
3. Disambiguate P vs psum in paper text: psum = 1/220 (= 6/1320), P = 1/1320 (mollifier length).
4. Define the certificate class precisely in Section 2: what Phi_m is, what c is (c = I0^2/(I2+J)),
   the kernel k_alpha, the 127 = m-6 factor, and the admissible-law form factor E(1) = -1/(6N²).
5. Add missing refs: Montgomery 1973, Rudnick–Sarnak 1996, Bombieri–Lagarias 1999, Heath-Brown 1979,
   Conrey–Ghosh–Gonek 1998, LMFDB, Keating–Snaith 2000 (moment conjecture). Cite Montgomery for
   the form factor correctly (as the admissible-law source, not as a kappa bound).
6. Fix table symbols: define T, rho_1 before the table; reference figures in body text.
7. Name the companion repository (the riemann git repo + commit hash) so the headline is reproducible.
8. min-gap 0.0188 + exponent 3.06: keep ONLY if a saved script produced them; else drop or label
   "computed from the 10M subset" with the script path. Data file lives on laptop.
9. Add an explicit "conditional status" paragraph: what is proven, what is certified, what is
   conjectural (HL* prime-pair / sixth moment), and that 0.6733 is numerically certified, not proved.
10. Recompile, re-verify numbers, copy to Downloads, commit.

## Status
All review agents complete. Meta-review done. Fix list finalized. Next: apply fixes 1-9 to
paper-main.tex + attack_bound_check.py, recompile, verify, commit.

---

# STATUS UPDATE (2026-08-13, fixes applied)

## Fixes APPLIED (paper v2, commit f09c37a + CGG fix)
1. [CRITICAL] Abstract + Theorem 3: "0.83621 simple" -> "0.83621 distinct on the
   critical line" (N_d = s1+s2+2p). Done. Verified in compiled PDF.
2. attack_bound_check.py rewritten: computes eps=8065/1e6 exact-rational, psum=1/220,
   emits bound = 0.67326607914000068290279687189167079692373428880136 — matches paper
   headline to all displayed digits (residual 2.6e-51 = 160dps vs 120dps truncation).
3. psum/P disambiguation: Theorem 1 now states (alpha, psum, P, m) = (1.49, 1/220,
   1/1320, 133); table row fixed to "1/220 optimal (mollifier P=1/1320)".
4. Certificate class defined precisely in Section 2: Phi_m, c = I0^2/(I2+J), the cosine
   kernel k_alpha, the 127 = m-6 factor, E(1) = -1/(6N^2) explicit with "not a
   conjecture about the zeros pair correlation".
5. New refs added + verified: Montgomery 1973 (Proc. Sympos. Pure Math. 24, 181-193),
   Rudnick-Sarnak 1996 (Duke 81, 269-322), Bombieri-Lagarias 1999 (JNT 77, 274-287),
   Heath-Brown 1979 (Bull. LMS 11, 17-18), Keating-Snaith 2000 (CMP 214, 57-89),
   CGG 1986 (Invent. Math. 86, 563-576 — corrected from 1998 via CrossRef).
6. Table symbols defined: T, rho_1, K_2, gamma_i before the table.
7. Companion repository named in text ("the riemann git repository, commit hash at
   publication").
8. Unverifiable min-gap 0.0188 + exponent 3.06 DROPPED (no saved source; data on laptop).
9. New section "What is proven, what is certified" — explicit conditional status.

## Verified clean
- Recompiled: 7 pages, 0 errors, no undefined refs (3x).
- Downloads copies refreshed (md5 d61f859e...).
- arXiv package builds standalone from clean dir (951K, 7 pages, 0 errors).

## Remaining (not blocked, deferred)
- Deep-n Li lambda_n at 300-500 dps (the live mathematical frontier — next step, not
  part of this review pass).
- arXiv actual submission: user must create account / submit; package is ready at
  results/arxiv-pkg.tar.gz + arxiv-README.md.

## Files
- Paper v2: paper-main.tex/.pdf (7 pages)
- Verifier: scripts/attack_bound_check.py (rewritten, emits headline)
- Review file: paper-review-20260813.md (this)
- arXiv: arxiv-README.md + arxiv-pkg.tar.gz
