# HANDOFF — isthisaislop: on-device AI-slop detector (MODEL ONLY)

**Written:** 2026-08-18 · **Author:** coordinator session · **Expires:** 2026-09-18
(after expiry: run `scripts/preflight.sh`, re-read `LEDGER.md`, re-derive status from `git log`; do
not trust the STATUS block below on faith)

**Scope:** the detection model and its data/eval pipeline. **No UI, no app, no store listing.**
Deliverable is a quantized model file + tokenizer + threshold/calibration file + model card + eval report.

---

## STATUS (one screen, always current — update in the same commit as the work)

| | |
|---|---|
| Phase | 0 — not started |
| Trained model | none |
| Frozen eval set | not built |
| Numbers we can quote | none |
| Blockers | (B1) generator API key for fresh-corpus build, (B2) target phone spec for latency budget |

## NEXT 3 ACTIONS

All commands run from `isthisaislop/` (the package root), after a one-time
`cd isthisaislop && pip install -e .`. **The `slop` package does not exist yet** — action 1 creates
it, so these are the acceptance commands for Phase 0, not commands that run today. Paths below are
relative to `isthisaislop/`; from the repo root they will not resolve.

1. Scaffold the package (`pyproject.toml`, `slop/`, `config/human_sources.yaml`), then
   `python -m slop.data.build_human --config config/human_sources.yaml --out data/human`
   → `data/human/*.parquet` + `data/manifest.json`
2. `python -m slop.features.extract --in data/human --out data/features/human.parquet`
   → interpretable feature table (CPU, no GPU)
3. `python -m slop.eval.harness --baseline lexicon-lr --report reports/baseline_lr.md`
   → first honest numbers on every eval slice

Nothing may be reported as a result until command 3 runs and prints per-slice TPR@1%FPR.

## STOP CONDITIONS (hard)

- Any number quoted without a logged run (commit hash + seed + command) is deleted, not "cited".
- No claim of accuracy without the FPR it was measured at, and the slice it was measured on.
- If the shipped student model cannot beat the interpretable-feature baseline (action 3) on the
  unseen-generator slice, we ship the baseline instead. A 50 KB logistic regression that explains
  itself beats a 40 MB transformer that doesn't.

---

## 1. What we are actually building (and the trap in the name)

The user-facing question is "is this AI slop?". That is **two different questions**, and conflating
them is how zerogpt-class products end up confidently wrong:

- **P(machine)** — provenance. Was this text produced by an LLM? Supervised, corpus-dependent,
  degrades hard when the generator or domain changes.
- **P(slop)** — style. Is this low-information, cliché-dense, template-shaped writing? Measurable
  from the text alone (overrepresented n-grams vs a human baseline, "not just X, but Y" density,
  lexical diversity, sentence-length uniformity, hedging chains, em-dash rate, tricolon rate).

They are correlated but not the same. Human marketing copy is slop written by a human. A carefully
edited LLM paragraph is machine-written and not slop. So:

**Decision D1 (locked): two heads, two numbers, one optional headline.** The model emits
`p_machine` (calibrated), `slop_score` (0–100, feature-derived, deterministic), and a headline
verdict computed by a stated rule over both. Never a single unexplained "87% AI".

**Decision D2 (locked): the model may refuse.** Under ~50 words there is not enough signal for a
provenance claim; the model returns `INSUFFICIENT_EVIDENCE` and shows only style flags. Short-text
unreliability is the single most common source of false accusations in existing detectors.

**Decision D3 (locked): explanations are evidence, not narration.** Three layers, all auditable:
per-sentence `p_machine` from the same encoder over sliding windows; deterministic pattern hits with
counts; and matched slop n-grams shown with their **measured** overrepresentation ratio against our
own human baseline ("`a testament to` occurs 41× more often in our AI corpus than our human corpus").
Explicitly forbidden: an LLM writing a post-hoc rationalization, and attention weights presented as
reasons. Saliency, if shown at all, is labeled "where the classifier looked".

## 2. Architecture

```
text
 └─ normalize (NFKC, strip zero-width, homoglyph fold, whitespace collapse)   ← kills 4 of RAID's
 ├─ feature extractor (pure Python, ~50 KB of tables)  → slop_score + reasons     mechanical attacks
 └─ encoder student (INT8 ONNX, ≤40 MB target)         → p_machine (doc + per-sentence)
                                                       → calibration (temperature + per-length bins)
```

**Backbone plan.** Train a teacher we can afford, distill into a phone-sized student.
- Teacher: RoBERTa-base or DeBERTa-v3-base (see §6 for the T4 precision constraint), 512 tokens.
- Student: MiniLM-L6-H384-class encoder (~22 M params, 30 k vocab). Vocab size matters more than
  depth for file size — a 128 k-vocab model spends ~100 M params on embeddings alone, which is the
  difference between a 40 MB and a 300 MB artifact.
- Runtime: ONNX Runtime Mobile, INT8 dynamic quantization. ORT is the pragmatic choice because the
  same artifact runs on Android, iOS and desktop for the eval harness; ExecuTorch is the fallback if
  ORT's mobile latency disappoints. No LLM ships in v1.

**Decision D4 (the robustness bet): distill the zero-shot signal instead of shipping it.**
Metric-based detectors (Fast-DetectGPT-style conditional probability curvature, Binoculars-style
cross-perplexity) generalize to unseen generators and rare domains far better than supervised
encoders, but need an LM forward pass at inference — 600 MB+ and battery we don't want to spend.
So we compute the curvature signal **once, at training time**, with a small frozen scorer LM over
the whole corpus, and train the student with an auxiliary regression head onto that signal
(alongside the binary label and the teacher's logits). The student learns the shape of the signal
without carrying the LM.
This is a **testable bet, not an assumption**: the ablation is "student with vs. without curvature
distillation, measured on held-out generator families". If the delta is not clearly positive, drop
the term and say so in the ledger. (CONJECTURED until measured.)

**Deferred to v2, explicitly:** an on-device "deep scan" that runs a 0.6 B scorer for a
curvature-based second opinion on demand. Sized but not built.

## 3. Data

The whole project lives or dies here, not in the architecture.

**Human text.** Provenance rule: prefer text that *cannot* be LLM-authored — dated before
2022-11-30. Wikipedia 2021 dump, Project Gutenberg, pre-2022 Reddit, pre-2022 arXiv abstracts,
Stack Exchange dumps, student-essay corpora, pre-2020 news. Text dated after that is kept in a
separate `modern_human` pool with its own era tag: people now write like LLMs, and a detector that
flags them is our problem, not theirs. `modern_human` is used for FPR measurement always, and for
training only as an explicit ablation.

**AI text.** Three tiers:
1. *Legacy public corpora* for volume and cheap coverage: MAGE, RAID-train, M4GT, HC3, DAIGT-v2.
   Their generators are GPT-3.5/Llama-2 era — they teach the easy cases and nothing about 2026 models.
2. *Fresh generations* (the expensive, differentiating part). ~20 current model families × 8 domains
   × 3 decoding settings × 4 prompt styles, including adversarial prompts ("write like a human",
   "no em dashes, vary sentence length, be specific"). This is API-bound, not GPU-bound. **Blocker B1:**
   needs a generation key; the Command Code provider documented in `handoff/HANDOFF.md` covers ~45
   models and is the obvious source. Key by reference only — env var, never in a file.
3. *Attacks*: paraphrase/humanizer passes over tier-1 and tier-2 text, plus RAID's mechanical suite
   (homoglyph, whitespace, zero-width, misspelling). The mechanical ones are the normalizer's job;
   include them anyway to prove the normalizer works.

**Hybrid text** (human prefix + machine continuation, machine draft + human edit, sentence-level
interleaving) is generated synthetically from the pairs above. This is what gives us per-sentence
supervision for the highlighting story, and it is the realistic case: almost nothing in the wild is
100% either.

**Splits.** Split by generator family AND domain AND source document, not randomly. Random splits
measure memorization and produce the 99.9% numbers that fall apart in the app. MinHash dedupe across
splits. One **frozen holdout** never touched by model selection, plus a "future generator" set built
after the training freeze.

**Licensing (open item O1).** The shipped weights must be trainable-and-redistributable. Research
corpora with unclear terms are eval-only until audited. Safe fallback if the audit is messy: train
the shipped model on our own generations + permissive/public-domain human text, and use the public
corpora purely as an external test set.

## 4. Evaluation — the part that makes this not slop itself

Primary metric: **TPR at 1% FPR, per slice.** Accuracy and bare AUROC are banned from headlines
because a detector that is 95% accurate overall can still be a machine for falsely accusing one
group. Also report AUROC, ECE (calibration), and refusal rate.

Mandatory slices, every run: unseen generator family · unseen domain · **non-native-English human
writing** · human creative writing (published prior-art evaluations found no system clearing 0.8
accuracy on novel human text and 0.8 recall simultaneously — assume this is our ceiling too until
measured) · short text (<100 words) · hybrid/edited · paraphrased-humanized · code-adjacent prose.

Baselines that must be beaten, in order: (a) always-human; (b) interpretable-feature logistic
regression; (c) a public off-the-shelf ModernBERT-class detector; (d) Fast-DetectGPT with a small
scorer. Beating (b) is the go/no-go gate for the whole neural approach (see STOP CONDITIONS).

Every artifact carries a model card with: training corpus composition, per-slice numbers at fixed
FPR, calibration curve, refusal policy, known failure modes, and an explicit "this is not evidence
of misconduct" statement. Claims are labeled **MEASURED / ESTIMATE / CONJECTURED / ABANDONED** per
the repo's honesty rules, and every MEASURED number names its run id.

## 5. Phases, gates, and definition of done

| Phase | Work | Compute | DoD gate |
|---|---|---|---|
| 0 | Corpus spec, human harvest, dedupe, splits, feature extractor, eval harness, baselines (a)+(b) | CPU only | Harness prints all slices; LR baseline numbers in `LEDGER.md` |
| 1 | Teacher fine-tune, calibration, full slice eval | T4, ~4–8 GPU-h (ESTIMATE) | Beats baseline (b) on unseen-generator slice at 1% FPR |
| 2 | Curvature feature extraction, distillation, span head, hard-negative mining, ablations | T4, ~10–25 GPU-h (ESTIMATE) | Each added loss term justified by its own ablation, or removed |
| 3 | Student distill → INT8 ONNX → on-phone latency/size measurement | CPU + phone | ≤40 MB, ≤300 ms per 512-token window on target phone, ≤1 AUROC point lost to quantization |
| 4 | Attack hardening, threshold policy, freeze v1, model card | CPU | Frozen holdout run once; report published; no unlabeled claims |

## 6. Hardware: a Colab T4 is enough through Phase 3

MEASURED facts that shape the plan:
- FlashAttention-2 does not support Turing; the upstream README points T4 users at a separate
  partial-support fork. So no FA2 on Colab's T4.
- Turing has no bfloat16. fp16 + loss scaling is the only mixed-precision option.
- DeBERTa-v3's disentangled attention has a long, documented history of fp16/bf16 overflow and NaN
  gradients (mDeBERTa needed fp32; the failure is still being reported in 2026).
- ModernBERT's speed advantage assumes FA2, and NaN-logit reports exist for its FA path.

Consequences (locked): **v0/v1 backbone is RoBERTa-base** — the boring, fp16-safe choice on a T4.
DeBERTa-v3 only in fp32 or with a stability preflight. ModernBERT is deferred to a machine with
bf16 + FA2, and is not on the critical path. Cap Phase 1 at ≤512 tokens, ≤150 M params, ≤1 M samples.
Session discipline mirrors this repo's kill-robustness protocol: checkpoint to Drive every ~500
steps, resume idempotently, stage shards to local disk before training (Drive I/O will otherwise
dominate).

Rough T4 arithmetic (ESTIMATE, verify with one measured step): ~0.26 TFLOP per fwd+bwd sample for a
base encoder at 512 tokens; at a realistic ~20 TFLOPS that is ~75 samples/s → ~2 h per epoch over
500 k samples. Curvature extraction with a 0.6 B scorer over 500 k samples is forward-only,
~4 h (ESTIMATE). Both fit inside Colab sessions if checkpointed.

**When better hardware actually pays for itself:** a 4–8 B LoRA teacher, curvature extraction beyond
~1 M samples, ModernBERT (bf16 + FA2), or several ablations in parallel. An L4 24 GB or a single
A100 40 GB removes the fp16 tightrope and cuts wall-clock roughly 3–6× (ESTIMATE) — worth renting a
few hours in Phase 2, not before. **Open item O2:** does the Void laptop have a usable NVIDIA GPU?
If yes it may beat Colab for long unattended runs.

## 7. Repo layout

```
isthisaislop/
  HANDOFF.md            this file (status + next actions + decisions)
  LEDGER.md             one entry per claim: label, number, run id, command, artifact path
  config/               corpus sources, generation matrix, training configs
  slop/data/            harvest, generate, attack, dedupe, split
  slop/features/        deterministic slop features + n-gram tables
  slop/train/           teacher, distill, calibrate
  slop/eval/            harness, slices, baselines, attack suite
  scripts/preflight.sh  checks env/keys/GPU and exits nonzero with what's broken
  artifacts/            exported ONNX + tokenizer + thresholds + model card
  reports/              per-run eval reports (immutable, dated)
```

## 8. Handoff contract (why this document is shaped like this)

Rules inherited by every future revision of this file, learned from reviewing the RH handoff:

1. **Status, next actions and stop conditions live in the first screen.** A resuming agent must not
   read 170 lines to learn what to run.
2. **Every fact is classed.** MEASURED (with command + artifact + date), ESTIMATE, CONJECTURED, or
   STALE-BY (date/condition). Statements about "your current session" are not facts.
3. **The document points at live state; it does not duplicate it.** Status tables rot; `LEDGER.md`
   and `git log` are the source of truth, and this file names them.
4. **Environment claims become executable.** Anything that could break is checked by
   `scripts/preflight.sh`, not asserted in prose. A handoff that can be run cannot rot silently.
5. **Secrets by reference only** — env var names and file locations, never a field shaped like a key.
6. **Dead ends are recorded** with an ABANDONED label and a reason, because rediscovering them is
   the most expensive thing a new session can do.
7. **Numbers carry their reproduction.** Script, args, expected output line. Otherwise they are
   folklore and get moved to a folklore list.
8. **An expiry date and a re-derivation procedure**, so a reader in three months knows the doc is a
   historical artifact rather than a current briefing.
