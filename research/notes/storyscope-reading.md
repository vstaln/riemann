# StoryScope: what the paper actually found

A reading of Russell, Rajendhran, Pham, Iyyer, and Wieting, *StoryScope: Investigating
idiosyncrasies in AI fiction*, arXiv:2604.03136 (v6, 10 Aug 2026).

Everything below is taken from the paper itself (abstract page + full HTML). No numbers
are invented. Where the paper reports a number, it is quoted; where it reports a
mechanism, it is paraphrased.

---

## The question

Most AI-text detectors look at surface style: word choice, sentence rhythm, the em-dash
problem, words like "delve" and "tapestry". Those cues work, but they are fleeting.
The paper's authors point out that GPT-5.4 already cut em-dash usage sharply, and that
fine-tuning an LLM to mimic human style drops detection on creative writing from 97% to
3% (Chakrabarty et al. 2026). If the surface is this easy to change, detection built on
the surface will not last.

So the paper asks a different question: can a story be identified as human or AI from
**discourse-level narrative choices** alone — plot structure, character agency,
temporal ordering, information revelation — with style stripped out entirely?

The framing matters. Changing narrative structure is not a post-hoc edit; it is a
rewrite. A detector built on narrative features should survive the edits that kill
style-based detectors.

## The method

**Corpus.** 10,272 human-written short stories from Books3. Each human story was
reverse-engineered into a writing prompt (Gemini 2.5 Flash inferred the premise), and
five LLMs — Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2, Claude Sonnet 4.6, GPT-5.4 — each
wrote a story from the same prompt. Six sources total, 61,608 stories, mean 4,753 words
each. Source identities were anonymized in all LLM-facing prompts.

**Pipeline.** Three stages:

1. **Structured templates.** Each story is converted by GPT-5.1 into a structured
   template organized along ten narrative dimensions from the NarraBench taxonomy:
   Agent, Social Network, Event, Plot, Structure, Setting, Time, Revelation,
   Perspective, Style. Prose becomes fields: character names and motivations, causal
   chains, key events, temporal order. The template is the intermediate representation
   that forces later stages to reason about narrative content rather than prose.

2. **Cross-source comparison.** A held-out discovery pool of 600 stories (100 prompts,
   all six versions) is presented in template form to GPT-5.1 with high reasoning
   effort, which produces structured comparative analyses: per-source dimension notes,
   cross-source divergences, and recurring patterns. This compresses ~2.7M tokens of
   raw text into ~686K tokens of comparison.

3. **Feature discovery.** From the comparative analyses, the pipeline induces 408
   candidate features, each phrased as a question with typed answers (categorical,
   ordinal, scale, binary, multi-select). These are deduplicated by embedding clustering
   (F2LLM-4B embeddings, single linkage at cosine 0.85), yielding **304 features**.
   A style-dependence audit (GPT-5.4 rating each feature high/medium/low style
   dependence) excludes 47 style-linked features, leaving **257 strict narrative
   features** for the main experiments.

**Classifier.** XGBoost, chosen over linear models and random forests. Features are
one-hot or integer-encoded. Split: 7,383 train / 1,405 val / 1,384 test prompts,
tuned on validation, retrained on train+val, reported on test (8,301 stories).

**Reliability.** The production extractor (Gemini 3 Flash) was checked with a
repeated-measures design: Krippendorff's α = 0.90 across five runs, mean pairwise
Cohen's κ = 0.89. A human validation over 12 stories (240 story-feature items per
annotator) gave human-vs-model Cohen's κ = 0.84 on average, versus human-vs-human 0.74 —
the extractor agrees with humans at least as well as humans agree with each other.

## The numbers

**Binary human-vs-AI detection (macro-F1):**

| Method | Features | F1 | AUPRC |
|---|---|---|---|
| Narrative (strict, no style) | 257 | **93.2** | .959 |
| Core only | 30 | 84.8 | .828 |
| Core + fingerprint | 101 | 91.1 | .934 |
| Narrative + Style | 304 | 96.0 | .982 |
| Style only | 39 | 85.8 | .867 |
| ModernBERT (raw text) | — | 99.9 | 1.00 |
| Stylometric + XGB | 144 | 99.8 | .999 |
| TF-IDF + XGB | 5,000 | 99.7 | .999 |
| Binoculars (zero-shot) | — | 55.9 | .404 |

Narrative features alone get 93.2% — 2.8 points below narrative+style, retaining over
97% of the full model's performance. A compact 30-feature core keeps 84.8%. The
ModernBERT baseline on raw text is near-perfect, which is expected; the point is that
narrative structure alone, with no style at all, is already strongly discriminative.

**Six-way authorship attribution (macro-F1):**

| Method | F1 |
|---|---|
| Narrative | **68.4** |
| Core only | 46.5 |
| Core + fingerprint | 63.4 |
| Narrative + Style | 77.3 |
| Style only | 60.4 |

Narrative beats style-only by 8.0 points (CI 6.7–9.2). Attribution is much harder than
detection — the AI models overlap heavily with each other.

**Robustness to editing.** 278 Gemini stories were run through LAMP (a span-level
rewriter that removes seven categories of AI artifacts like cliché and purple prose,
using Gemini itself as the rewriter). The narrative classifier still detects the edited
stories at **93.9% macro-F1** (AUPRC .988), versus 95.5% on the originals: a 1.6-point
drop. Editing prose does not change the structural choices the classifier reads.

## What separates human from AI, in narrative terms

From the core-feature analysis (Section 4.1). These are the differences with the
largest, most stable human-vs-AI gaps.

**AI over-explains its themes.** AI stories are roughly 20% more explicit and moralizing
on a 1–5 scale. Narrators state the theme explicitly 77% of the time versus 52% for
humans — a grieving character's arc ends with the narrator spelling out the lesson.
AI dialogue serves philosophical debate 59% vs 34%. Allusions are vague (72% vs 50%)
rather than specific. The pattern is over-determination: the meaning is said, not
inferred.

**Human authors subvert linearity.** AI stories have tighter causal chains, more
protagonist-driven resolutions (69% vs 46%), far fewer subplots (79% "no subplots" vs
57%). AI resolutions favor internal acceptance (47% vs 27%); humans tolerate ambiguity.
Humans use time jumps, flashbacks, flash-forwards, nonlinear structure to delay
revelation. A human mystery opens at the funeral and spirals backward; AI tells it from
first clue to grand reveal.

**AI over-writes the body and senses.** AI conveys emotion through physical sensation
81% vs 38%, smell imagery 82% vs 57%, and uses setting as inner-state mirror. Humans
name feelings: explicit emotion labels 29% vs 8%. Where a human writes "she felt
afraid", AI writes a tightening chest, cold sweat, dimming lamplight.

**Human authors engage the outside world.** Humans reference specific texts and authors
at nearly double the AI rate (47% vs 24%), balance explicit and implicit references
(37% vs 16%), break the fourth wall more (67% vs 39%), and address the reader directly
(28% vs 7%). AI writes as though no one is watching; human writing treats the reader as
a co-participant.

**AI has less diverse narrative features overall.** Humans span more locations, carry
more dialogue, integrate more subplots (42% vs 21%), and give protagonists moral
ambivalence more often (59% vs 38%).

## The per-model fingerprints

The five AI models are separable by their own quirks. These are the standout features
(not an exhaustive list):

- **Claude keeps it cool.** The most distinctive profile. Restraint: event intensity
  escalates less than any other source, most uniform narrative voice. Reverent toward
  literary tradition — honoring and extending conventions rather than subverting them
  (62% vs 39–56% across others). Favors epilogues, avoids dream sequences, prefers
  quiet endings over "avalanche" endings.
- **GPT likes to gossip.** Social storytelling: gossip and rumor as plot mechanism (64%
  vs 44–55%), stories framed as reflection on events years or decades ago, ensemble
  social networks at human levels. Subverts expectations more than other AI (41% vs
  27–36%), leaves reconciliations ambiguous.
- **DeepSeek front-loads.** Puts crucial context early that other sources save.
- **Gemini, tidiest and bleakest.** Tidiest endings, extended denouements, bleakest
  settings (88% tagged bleak and oppressive).
- **Kimi is the generic center.** Fewest fingerprints, lowest attribution F1, no
  distinctive narrative choices.

**AI convergence.** The five AI sources cluster in a shared region of narrative space,
well separated from humans. Human-vs-AI centroid distance is 1.6× the AI-vs-AI
distance; even the closest human-AI pair is farther than the most distant AI-AI pair.
The six most-confused attribution pairs are all AI-vs-AI; the largest confusion (Gemini
↔ DeepSeek, 222 and 207 stories) dwarfs the most common human misclassification (Human
→ Kimi, 46).

**Human narratives are rarer.** Per-story rarity is mean Euclidean distance to 25
nearest neighbors. Human stories have higher mean rarity percentile (0.71 vs 0.49,
Cohen's d = 0.83). 24.7% of human stories fall in the top-10% rarest corpus-wide versus
7.1% of AI stories; 3.0% vs 0.6% in the top 1%. At the prompt level, the human version
is the rarest of the six 57.8% of the time (chance would be 16.7%). Human stories are
also more dispersed: 22% larger radius about the human centroid, 1.13× larger median
10-NN radius.

## What it means

The durable claim is not "we can detect AI with 93% F1" — raw-text detectors do 99.9%.
It is that **narrative structure itself carries the signal, independent of style**, and
that this signal survives the edits that defeat style detectors. Changing the narrative
choices means rewriting the story, which most people will not do. So narrative features
are a more durable basis for authorship analysis than style, and the rarity measure
gives a concrete, measurable proxy for originality.

There is a flip side the paper mostly leaves implicit: the same feature space is a
recipe list for making AI fiction *less* detectable. Over-explain less, break the
causal chain, add subplots, name real books, address the reader, let endings dangle,
give the protagonist a moral mess. The paper's own finding — humans are rarer and more
dispersed — is also a target: the detection gap will shrink as models are pushed toward
the human region of narrative space, and the features will have to keep moving.

## Method caveats worth keeping in mind

- The corpus is Books3 short stories, mean 4,753 words. The pipeline needs long texts
  to extract fine-grained features; how well it transfers to flash fiction, poetry, or
  non-fiction is untested in the paper.
- Human stories are one per prompt; AI stories are five per prompt from the same
  inferred prompt. The human stories also *generated* the prompts, so the human side is
  the reference the prompt is built from — this is the design, but it means the
  human/AI comparison is human-original vs AI-mirror, not human-vs-AI on equal footing.
- All feature extraction uses LLMs (GPT-5.1 for templates, GPT-5.4 for the style audit,
  Gemini 3 Flash for production features). The extractor's agreement with human
  annotators (κ = 0.84) is good but not perfect, and the feature space is therefore
  partly an LLM's view of narrative.
- The paper uses Books3, which is copyright-problematic as a dataset; the authors state
  academic use only. The AI disclosure notes Claude Code and Codex were used to write
  and polish the paper itself.
