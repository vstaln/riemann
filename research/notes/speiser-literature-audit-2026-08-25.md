# Speiser-family literature audit: ξ′-crossing mechanism — what is already known

**Date:** 2026-08-25 · **Agent:** adventurer (knowledge audit, read-only, no compute)
**Subject:** our finding — an FE-consistent off-line ζ-zero (plant at β=0.9) forces an ξ′ zero to cross
into 0<σ<1/2 (N=1 localized at Re≈0.4526); single-factor plants proven inert via paired-Hadamard identity.
**Verdict (stdout): PARTIALLY_KNOWN** — see §"Verdict".

Labels: PROVEN (classical/verified locally) / RECALLED (from training, primary source not verified in this
session — honest caveat) / NOT FOUND (absent from local corpus and not recalled) / INCONCLUSIVE.

---

## 1. Local corpus: what this project already holds

| File | Content relevant to us | Status |
|---|---|---|
| `research/notes/speiser-negativity-program.md` | Full ζ′-lane: decomposition (D) of ζ′/ζ via paired Hadamard terms; RH ⟹ Re(ζ′/ζ)<0 in 0<σ<1/2 PROVEN termwise; the converse ("deep-left kernels never dominate the always-negative partners") analyzed as **RH-equivalent and RH-hard** — the loop closes at t-dependence. Footnote: the ζ′ road already knows the pair-splitting sign structure we use for ξ′. | PROVEN (direction); converse INCONCLUSIVE (open) |
| `research/notes/xiprime-transfer.md` | Prior stress-test of "ξ′ transfer": concluded (i) there is NO pointwise transfer ξ′-zero→ζ-zero (on-line ζ zeros are where ξ′ does NOT vanish; ξ′ zeros interleave in gaps); (ii) the only exact ξ′↔ζ link is the count N_{ξ′}=N+O(log T) — classical (Conrey 1983 §2, `ZeroCount.lean` `xiDeriv_riemannVonMangoldt`). | PROVEN / CONJECTURED (interleaving) |
| `research/notes/wave8b-speiser-2026-08-17.md`, `DEAD-LEVERS.md` (line 190) | ζ′-left-strip certificate history (T=12000-scale). Speiser direction only. | — |
| `research/notes/literature-sweep-simplezeros.md` (line 35) | Grigutis–Turčinskas: pointwise lower bound for Re(ξ′/ξ) > 0 in ½+1/√log t < σ < 1 — modern positivity input on the RIGHT side near the line. | RECALLED-by-sweep |
| `research/notes/unmined-machinery-sweep-2026-08-24.md` (line 91) | Suggests using an FE-consistent ξ′ functional to cross-check pressure schemes. Idea-level only, no theorem. | — |
| `zeta-density-one-reproduction` repo (`paper-zh.tex` §1382 interpolation map) | The density-one program treats off-line zeros **via their FE mirror pairs** in band-limited forms (off-line signal ∝ N_off, δ>0 zeros enter through the mirror), and explicitly walls itself off from pointwise/λ→∞ data. Contextually relevant: FE-mirror-pair structure is already a working concept here; ξ′ crossings are not. | PROVEN (within their theorem) |

**Key local fact:** no local note states or proves "off-line ζ-zero ⟹ ξ′ zero left of ½", nor any crossing
count. The closest local objects are (a) the ζ′ negativity program, which is a log-derivative-sign lane, and
(b) the N_{ξ′}=N+O(logT) count, which is global and says nothing about crossings.

---

## 2. What the literature knows (from training; primary citations not re-verified this session)

### 2.1 PROVEN / classical — the equivalence family

1. **Speiser (1934):** RH ⟺ ζ′(s) has no zeros in 0 < Re s < 1/2. Classical theorem, about **ζ′, not ξ′**.
   (Direction RH ⟹ is trivial termwise; the converse is a real argument-principle theorem.)
   → Already superseded locally by `speiser-negativity-program.md` (direction + RH-hardness analysis).
2. **RH ⟹ all zeros of ξ′ lie on Re = 1/2:** classical, even cleaner than ζ′: ξ′/ξ(s) = Σ_{γ>0}[1/(s−ρ)+1/(s−1+ρ̄)]
   has NO Archimedean background (unlike ζ′/ζ), every pair-term has Re ∝ (2σ−1)·(positive), so Re(ξ′/ξ) has
   strict sign off the line under RH; no pole/zero off the line. This is "the equivalence direction" the
   mission asks about — definitely known. [RECALLED as standard; follows Speiser-family reasoning, in the
   ξ′/Ξ literature and Conrey 1983 context.]
3. **ξ′ zero count:** N_{ξ′}(T,2T) = N(T,2T) + O(log T) (argument principle, Riemann–von Mangoldt fold via
   ξ′(1−s̄)=−conj ξ′(s)). Classical; formalized locally in `ZeroCount.lean`. **Conrey (1983, J. Number Theory
   16, "Zeros of derivatives of Riemann's xi-function on the critical line"):** positive proportion of ξ′ zeros
   on the line; also proved derivative-zero results along this line. [RECALLED; locally the count is PROVEN.]
4. **Symmetry:** ξ′(s) = −ξ′(1−s) ⟹ off-line ξ′ zeros come in mirror pairs about σ=½; so "a ξ′ zero with
   Re>½ exists" ⟺ "a ξ′ zero with Re<½ exists". Any off-line ξ′ zero is automatically a left-half crossing.

### 2.2 The KEY question — is "ζ has an off-line zero ⟹ ξ′ has a zero in 0<σ<1/2" a known theorem?

Honest answer: **not verifiable as a pinned theorem from this session's sources; recalled as Speiser-family
folklore.** Specifically:

- I recall the ξ′-version of Speiser ("RH ⟺ all zeros of ξ′ have Re s = ½") being stated in expositions of
  Speiser-type equivalences — the ξ′/Ξ derivative literature (incl. Conrey 1983 surroundings), and folklore
  around Ξ′(t) gap zeros. But I cannot, from memory, name a primary source with a full proof of the
  converse (ζ off-line ⟹ ξ′ left-of-½) distinct from Speiser's own ζ′ argument. **Label: RECALLED, unverified.
  RECOMMEND: verify against Conrey 1983 intro / a survey of Speiser equivalents (e.g., Ivić's "The theory of
  Hardy's Z-function" chapters; the Borwein et al. "Riemann Hypothesis" problem book) before we claim the
  direction.**
- Modern quantitative side I recall: results on zeros of ζ′ (and higher derivatives) in the left half-strip
  counting off-line zeros — e.g., work bounding the number of ζ′-zeros in Re<½ in terms of off-line ζ zeros
  (I associate this with the ζ′ literature post-Speiser; maybe due to... [cannot pin]). NOT found locally.
- **Nothing recalled** (and nothing local) on *planted-zero perturbation counting*: "one FE-consistent off-line
  zero at β=0.9 forces exactly N=1 crossing localized at Re≈0.4526"; "single-factor plants are inert because of
  a paired-Hadamard identity". That is the mechanistic content of our finding, and it is **NOT FOUND** in the
  literature I recall.

### 2.3 Contrasts the mission asked about

- **Davenport–Heilbronn (1936) counterexample:** correct contrast — the D–H function has a zeta-type start and
  zeros far off the line, but its functional equation is **not** of the self-dual ξ-type (no ζ-completed
  ξ(s)=ξ(1−s) structure with the matching Γ factor), so no paired-Hadamard/ξ′ mechanism transfers to it.
  Consistent with our machinery being *completed-zeta-specific*. [RECALLED, classical]
- **Berlinger-type equivalences:** the mission presumably means **Beurling**-type criteria (Beurling's
  L²/fractional-integral criterion; Balazard–Saias–Yor integral criterion) and the **Li criterion** (λ_n ≥ 0),
  plus the Weil-positivity family. None of these is a ξ′-crossing-count equivalence; they are alternative
  spectra of RH-equivalence formulations. (If "Berlinger" is meant as a person, I am not aware of a Berlinger RH
  equivalence — flag as likely typo for Beurling.) **Li–Yang on zeros of ξ′:** I recall work by X.-J. Li and
  collaborators on ξ′ zeros (recall includes the Li-positivity program, not a ξ′-crossing theorem). Label
  RECALLED, unverified, likely orthogonal.
- **Levinson / Levinson–Montgomery / Spira / Skewes:** Levinson's positivity of ζ′-zeros on the line and
  Levinson–Montgomery simple-zeros-on-line are about zeros *on* the line; Spira did computational studies of ζ′
  zeros; Skewes is about π(x)−Li(x) sign changes — none is a left-of-½ ξ′ crossing statement. All orthogonal to
  the crossing mechanism. [RECALLED, standard]

---

## 3. What is plausibly new in OUR observation

1. **The crossing-count object itself:** planting a *single consistent* off-line zero (β=0.9 with its FE
   mirror at 0.1) and observing an *actual* ξ′ zero (not a sign change of Re ξ′/ξ, which is generically
   insufficient) cross into 0<σ<1/2, **counted** (N=1) and **localized** (Re≈0.4526). The literature (as far
   as recalled) knows the qualitative equivalence family and the global count — it does not know local
   crossing statistics under planted perturbations. **PLAUSIBLY NEW (mechanistic).**
2. **Paired-Hadamard inertia:** the observation that a single-factor (unpaired) plant is inert — i.e., the
   mirror-pair structure (ρ, 1−ρ̄) is what creates the crossing force — is a clean structural lemma that I do
   not recall in the literature and is not in the local corpus. It reframes the Speiser-family statements as a
   *deformation theorem*: consistent (mirror-complete) perturbations of the zero set move ξ′ zeros off the
   line; inconsistent ones do not. **PLAUSIBLY NEW.**
3. **Link to an RH-proof strategy:** the mechanism connects to the local Speiser-negativity program (the same
   pair-splitting sign structure; the negativity program's "hole" is exactly the converse of the mission's
   crossing claim, stated for ζ′/ζ rather than ξ′), and to the density-one program's FE-mirror-pair treatment
   of off-line zeros (`paper-zh.tex` §1382). A rigorous global form of the crossing count would give a new
   quantitative Speiser-family statement ("if N_off(σ₀,t) ≥ 1 at height t then an ξ′-crossing exists at height
   ≈t with count ≥ 1"), the kind of per-height converse that `speiser-negativity-program.md` identifies as the
   missing RH-difficulty ingredient. **This is the single most valuable unexplored direction**: per-height,
   non-averaged, off-line ⟹ crossing. But nothing here is new to *RH itself* unless the converse is proved
   (currently only numerically demonstrated at one plant).

---

## 4. Verdict

**PARTIALLY_KNOWN.** Evidence, one line: the qualitative pair (RH ⟹ ξ′ zeros on Re=½ is classical;
"off-line ⟹ ξ′-crossing" is recalled as Speiser-family folklore though unpinned) is known, but no local note
or recalled literature contains the planted-zero crossing *count* (N=1, Re≈0.4526, paired-Hadamard
single-factor inertia) — that is plausibly new as a mechanism, and it is the right per-height tool shape the
ζ′-negativity lane identifies as missing for an elementary RH attack.

**Action items before any novelty claim:**
1. Verify the ξ′-version of Speiser's equivalence in a citable primary source (start: Conrey 1983 intro; Ivić's
   Z-function monograph; Borwein et al. problem book). If it is a full theorem, the *direction* is a
   re-discovery and only the counting/inertia is new. If it is folklore-only, our numerical demonstration is a
   first explicit instance.
2. Do not let the numeric N=1 be quoted as a theorem; mark it CHECKED NUMERICALLY (planted FE-consistent
   model, one regime β=0.9).
3. Probe the boundary of the mechanism (β→½⁺, β→0, multiple interacting pairs, extreme height skew) — the
   literature gives no guidance there either, which is itself evidence of what ISN'T known.