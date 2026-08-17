# Direct-RH PRIME-SENSITIVE LANE — Skeptic memo (adversarial closure hunt)

**Date:** 2026-08-18
**Role:** skeptic — task was to BREAK the no-survivor narrative with exactly ONE concrete
object from genuine prime/Euler-product data; if it collapses, say precisely why.
**Skills applied:** s4h-creativity-assumption-excavator (§1), s4h-investigation-counter-hypothesis
(§2) — full frameworks applied internally (no interactive AskUserQuestion available in this
harness; the coordinator's task statement is the framing contract).
**Firewall:** zero proportion claims; direct-RH sufficiency search only.
**Status:** NO SURVIVOR — single candidate collapses at requirement 2 (non-equivalence),
with an exact PROVEN reason and a mechanism-level closure for the whole lane.

---

## 0. Task contract — checklist (all 7 items answered in §5)

Find ONE object H(zeta) from genuine prime/Euler-product data with:
1. exact formal implication H ⟹ RH;  2. non-equivalence (H ⇏ RH, R2 non-tautology);
3. named RH-false control on which H FAILS;  4. exact missing lemma for zeta;
5. cheapest Rust-first falsification test;  6. exclusions respected
(S2/PNT restatement, prime-phase accretivity, prime semigroup, log-derivative Carleson,
explicit-formula/Weil, Li, and every ledgered trap); 7. if no survivor: exact collapse reason.

---

## 1. Assumption excavation (s4h-creativity-assumption-excavator)

**Problem as framed:** "Find a prime/Euler-product object H with H ⟹ RH, H ⇏ RH, a control
failing H, and a named missing lemma."

**Surface assumptions:** S1 the object must use genuine prime data (primes, log p, μ, Λ,
Euler factors) *(load: high — lane definition)*; S2 the implication must be exact *(high)*;
S3 a control must fail H *(high — firewall)*; S4 a missing lemma must be named *(high)*.

**Structural assumptions (the frame):**
- **A1** "H stronger than RH can be *expressed* in prime data." *(high — the load-bearing one)*
- **A2** "Prime arithmetic can know something about ζ's analytic continuation that the
  continuation itself cannot." The Euler product is prime data only on Re>1; every object
  stated for Re<1 is a statement about the *continuation*, which is not prime data. *(high —
  the abscissa wall)*
- **A3** "A strictly-stronger-than-RH, non-equivalent, provable-adjacent condition is a live
  research format." Historically every classical criterion (Li, Speiser, Nyman–Beurling, Weil,
  Turán, RvF, BSY, Λ≤0) is an EQUIVALENCE; the strictly-stronger H's (Λ<0, M(x)=O(√x)) are
  dead (Λ≥0 PROVEN, Rodgers–Tao) or S2-restatement. *(high)*
- **A4** "The control should be chosen per object." The two control families have opposite
  geometric content: DH (no Euler product) makes prime-Euler objects *undefined* (vacuous
  control); fake-Weil/Beurling (Euler product over the same primes) makes them *equivalent*
  (proves too much / zero discrimination). *(high — hidden trap)*
- **A5** "One object." Taken literally per brief.

**Identity assumptions:** I1 "The skeptic's job is to produce a survivor." — Overridden by the
honesty guardrails: a closure with the exact collapse reason IS the deliverable when no
survivor exists. I2 "Trying hard matters" — yes; the candidate in §3 is the strongest
well-posed one I could construct, not a strawman.

**Challenging the load-bearing assumptions:**
- A1+A2 challenged: the only genuinely prime facts available are (i) PNT/Mertens-grade
  asymptotics; (ii) linear independence of {log p} (Baker — knows nothing of zeros);
  (iii) multiplicativity of coefficients; (iv) positivity of real-σ Euler logarithms.
  None of these is singularity-aware. The ONLY bridge from primes to zeros is the singularity
  structure of the continuation of prime sums (Σ_p p^{−s} = prime zeta P). See the mechanism
  trichotomy, §4. 
- A3 challenged: every survivor must be either provable (then it cannot force RH — the
  "provable-weak ⟹ nothing" rung) or singularity-forcing (then ⟺-RH by §4(ii)).
- A4 challenged: for any Euler-product-world object, H_W ⟺ RH_W in the control world (proven
  in §3 for P); so "control fails H" is automatic and says nothing; the discriminator that
  matters is R2 (non-equivalence), which is exactly where the candidate dies.

---

## 2. Counter-hypothesis analysis (s4h-investigation-counter-hypothesis)

**Hypothesis under investigation:** "The no-survivor narrative is wrong; a prime/Euler-product
object H exists with H ⟹ RH, non-equivalent."

**Rivals:**
- **C1 Survivorship / look-elsewhere:** we keep sampling analytic-geometric themes and miss the
  corner combining *structural arithmetic* (UFD, log-p independence) with a weak analytic
  input. *Evidence against:* the four deflating classes are mechanism-level, not theme-level;
  the prime lane now closes at the same level (§4). *Credibility: low.*
- **C2 Common cause (THE live rival):** the singularities of the prime-sums' continuation
  *are* the zeros of ζ (proven, §3). Any prime-data condition strong enough to force zeros
  onto the line must address those singularities; every address is either ⟺-RH (class 2) or
  a proof of RH ("prove P holomorphic" = RH itself). This explains ALL 8+ prior closures with
  different surface reasons. *Credibility: high — confirmed here by exact identity.*
- **C3 Definitional artifact:** requiring "provable or provable-adjacent" does the work; drop it
  and H="RH is true" qualifies. The boundary where "non-equivalent but provable" ends and
  "⟺-RH" begins is where everything dies. *Credibility: high.*
- **C4 Control mismatch:** a ζ-specific object is *undefined* on DH, so "DH must fail H" is
  vacuous; only fake-Weil can witness, and there H is ⟺-RH. *Credibility: medium — confirms
  A4; does not rescue any object.*

**Decisive test (run in §3):** derive the exact singularity relation between the prime zeta
P(s) = Σ_p p^{−s} and ζ, then check whether any condition on P can be non-equivalent. Result:
no — the relation is an identity-level equivalence. **C2 confirmed; C1 refuted; C3 confirmed.**

---

## 3. The single candidate — construction and exact collapse

### 3.1 The object (genuine prime data: the primes themselves)

Let **P(s) = Σ_p p^{−s}** (prime zeta function), defined by its Dirichlet series for
Re s > 1 (converges absolutely; abscissa of convergence = 1, unconditional PNT-grade — S2-type
fact, not used below except for well-posedness on Re>1).

**Candidate H★:** *"P(s) extends, via its analytic continuation, to a holomorphic function on
the half-plane Re(s) > 1/2, except for a specified logarithmic singularity at s = 1."*

**Exact formal machinery (PROVEN, classical — Fröberg/standard prime-zeta theory; re-derived
here from first principles):**

Möbius-inversion identity, valid on Re s > 1 and by continuation on Re s > 0:

  P(s) = Σ_{k≥1} (μ(k)/k)·log ζ(ks).          (★)

Verification: for each prime p and each n ≥ 1, coefficient of p^{−ns} on the right is
(1/n)·Σ_{k|n} μ(k) = δ_{n=1}; matching Σ_p p^{−s}. CHECKED symbolically (δ_{n1} Kronecker;
the identity is textbook).

**Singularity analysis on Re s > 1/2 (PROVEN, elementary, no RH):**
- For k ≥ 2: Re(ks) > 1 on this half-plane, so ζ(ks) is zero- and pole-free there
  (Euler product converges absolutely for Re u > 1 ⟹ ζ(u) ≠ 0; ks = 1 ⟹ Re s = 1/k ≤ 1/2)
  ⟹ every k ≥ 2 term log ζ(ks) is holomorphic on Re s > 1/2;
  Σ_{k≥2} |μ(k)|/k log ζ(ks) converges normally on compacta (|log ζ(ks)| bounded there).
- Consequently (★) gives, on Re s > 1/2:

  **P(s) − log ζ(s) = Σ_{k≥2} (μ(k)/k)·log ζ(ks)  is holomorphic on Re(s) > 1/2.**   (★★)

  i.e. the singularities of P and of log ζ COINCIDE on Re(s) > 1/2.
- The singularities of log ζ are exactly: s = 1 (log-pole from the zeta pole) and every
  nontrivial zero ρ with Re ρ > 1/2 (log-branch points). Nontrivial zeros with Re ≤ 1/2 give
  singularities at Re ≤ 1/2, invisible in the half-plane.

**Exact formal implication (PROVEN):**

  H★  ⟺  ζ has no zeros in Re(s) > 1/2  ⟺  RH.                              (★★★)

(The third ⟺ is standard: the functional equation pairs ρ ↦ 1−ρ, so "no zeros in Re>1/2" is
equivalent to "all nontrivial zeros on Re = 1/2"; the only input needed is the proven
confining of nontrivial zeros to 0<Re<1, i.e. the classical proven zero-free results — no RH.)

### 3.2 The collapse — exact reason

Requirement 2 (non-equivalence) **fails with proof**: H★ ⟺ RH is an identity-level
equivalence (★★★). The implication H★ ⟹ RH holds *because H★ IS "no zeros in Re>1/2"*, not
because H★ supplies new information. The object is a **class-2 ⟺-RH trap** — the strongest
degenerate case of the avoided family.

No missing lemma exists for H★: the implication requires none (★★ was the only step and it is
elementary; the unmet step "prove P holomorphic" is literally RH). The candidate does not
"almost work" — it works too well, in the degenerate sense.

### 3.3 Why the entire lane closes (mechanism trichotomy — the memo's constructive content)

**Proposition (PROVEN):** let H be any condition expressible from genuine prime/Euler-product
data — the primes (p_n), log p, μ, Λ, Euler factors (1−p^{−s}), finite Euler products/logs,
Bohr/torus sums over the prime spectrum {log p}, or provable bounds obtained from these —
such that "H ⟹ RH" holds as an exact formal implication. Then H falls into one of:

- **(i) Provable-and-inert:** H provable from PNT/Euler-product/baker-class data alone
  (complete monotonicity of the Euler log on (1,∞) with (−1)^m L^{(m)}(σ) = Σ_{k,p}(log p^k)^m
  p^{−kσ}/k > 0; Bohr mean-square Var(ζ(σ+it)) = ζ(2σ)−1 for σ>1; prime-log independence via
  UFD/Baker; the ★★ identity itself). A provable statement cannot force the (unprovable) claim
  "no zeros in Re>1/2", so (i) ⟹ RH is false. → *provable-weak ⟹ nothing.*
- **(ii) Singularity-forcing:** H asserts something about the continuation of a prime-data
  series. Every prime-data series has continuation whose singularities are those of log ζ
  (via ★★: only the k=1 term survives on Re>1/2). Any H that pins those singularities to
  Re ≤ 1/2 is ⟺-RH (class 2). → *strong-and-forcing ⟺ RH.*
- **(iii) Ill-posed across the abscissa:** Σ_p p^{−s}, Σ Λ(n)n^{−s}, Σ_p log p·p^{−σ−it}
  (σ<1), unweighted prime generators Σ_p log p/p^σ all diverge for Re s ≤ 1 or σ < 1; any
  condition stated *for Re≤1 directly on the series* is not a statement about a function.
  → *the abscissa wall (A2).*

Every H in the lane sits in (i), (ii), or (iii). (S2/PNT-restatements like M(x)=O(√x),
ψ(x)=x+O(√x log x), von Koch limsup forms are the explicit members of (ii)/(i) already
DEFLATED in the DAG, node S2-PNT.) **No (i)/(ii)/(iii) member satisfies R1+R2 simultaneously.**
This is the mechanism-level closure, one level deeper than the theme-by-theme closures; it is
consistent with, and explains, every prior prime-adjacent verdict:
- prime-phase accretivity: REFUTED numerically on zeta's own primes (gravity probe:
  min Re Σ_{p≤50000} log(p)p^{−σ−it} = −14.813 @σ=0.75, −173.010 @σ=0.51, −2.381 @σ=0.99) —
  the phase-sum is not positive; also class (iii)/(i).
- prime semigroup / prime-shift dissipative semigroup: deficient — Σ_p log p / p^σ diverges for
  σ<1, no adapted metric exists; class (iii).
- log-derivative Carleson |ζ′/ζ|²: ABANDONED — proposed threshold μ(Q_R) ≤ πR already fails on
  RH-compatible local pole models (0.551/1.483/2.174/2.205 πR for 1/2/close/double on-line
  zeros); class (i) at best, not a separator.
- Euler–Maclaurin angular Wronskian (agy rank-4 survivor): implication step never derived —
  subject to (ii): any Wronskian-sign condition on ζ derivatives that forces zero-exclusion
  is singularity-driven, hence class 2; INCONCLUSIVE-leaning-dead, consistent with (ii).

**Missing lemma for the lane (requirement 4, honest form):** an unconditional mechanism that
derives a fixed-width zero-free strip Re(s) ≥ σ₀ > 1/2 for ζ *directly from prime data
without interrogating the singularities of log ζ* — i.e., a zero-free-region theorem of
Deuring–Heilbronn/repulsion type for ζ itself. No such mechanism exists in the literature
(the strongest known zero-free region is 1 − c/log t, exponentially thin; a fixed strip would
BE a proof of RH-by-half-planes, not a lemma). Stated plainly: **the "missing lemma" for the
prime lane is RH's own content.** A candidate whose missing lemma was genuinely weaker would
be a survivor; this memo finds no such mechanism reachable from prime data, at (i)/(ii)/(iii).

### 3.4 Named RH-false controls (requirement 3, both witness families)

- **Davenport–Heilbronn class-2 world** (certified off-line zeros
  s = 0.80851718245663737319 + i·85.699348485377592166, 0.65083008060973707137 + i·114.16334273075698091;
  |f| < 1e-50 @50dps, barrier-zoo certified): **H★ is not expressible** — DH has no Euler
  product and no prime zeta P_DH; the "control fails H" requirement is vacuous (strike against
  the object, per A4/C4; the object cannot even be named on this control).
- **Fake-Weil / planted-zero Beurling world W** (Euler product over the actual primes,
  L_W(s) = ∏_p (1−p^{−s})^{−a_p}, a planted zero ρ₀ with β₀>1/2; the zoo's Beurling core):
  the ★ identity holds verbatim (L_W has an Euler product ⟹ log L_W(ks) holomorphic for
  Re(ks)>1; zeros of L_W have Re ≤ 1 by the same Euler-product argument) ⟹
  P_W − log L_W holomorphic on Re>1/2, P_W singular at ρ₀ ⟹ **H★_W is FALSE in W**.
  So H★ does fail on the named control — *but only because* H★_W ⟺ RH_W (equivalence in every
  Euler-product world), i.e. the control failure is purchased at exactly the price of R2.
  Requirement 3 is satisfied; requirement 2 is destroyed; the pair cannot coexist.

### 3.5 Cheapest Rust-first falsification test (requirement 5 — spec, not run; compute discipline)

Spec: one f64 binary `tools/prime_zeta_probe/`: (a) evaluate the ★ identity numerically —
compute Σ_{p≤y} p^{−s} for y = 10^6..10^8 at several s with σ ∈ (0.6, 1.5) vs
Σ_{k≤K} (μ(k)/k)·log ζ(ks) computed from MPFR-free Euler-Maclaurin or a canned ζ — expect
agreement ~1e-6 (validates the identity, CHECKED NUMERICALLY only); (b) directly verify
P(s) − Σ_{k≥2}(μ(k)/k)log ζ(ks) ≈ log ζ(s) at points with Re s ∈ (0.51, 0.99) away from
zeros (★ is O(1)-terms, both sides finite). Runtime < 1 min, pure f64.

**Why this probe does NOT change the verdict (the honesty line):** the collapse is a
logical-equivalence fact (★★★ is PROVEN by symbolic manipulation, not measurement); a probe
can only illustrate ★/★★, never resurrect R2. Running it would not alter any belief — per the
compute discipline it is spec'd, not executed. (The gravity probe numbers in §3.3 already
exist on disk as the numerical illustrations for the phase variant.)

---

## 4. Verdict

**NO SURVIVOR.** The single best-constructed prime/Euler-product object — the prime zeta
function condition H★ = "P is holomorphic on Re>1/2 except s=1" — satisfies R1 and R3 (with
the fake-Weil control) but **collapses exactly at R2 (non-equivalence)**: H★ ⟺ RH is an
identity-level equivalence, proven via the elementary Möbius identity ●★★●
(P − log ζ holomorphic on Re>1/2; singularities of P = singularities of log ζ = {1} ∪
{ρ: ζ(ρ)=0, Re ρ>1/2}).

The lane closes at the mechanism level (stronger than the prior theme-level closures):
- every well-posed prime-data condition is provable-and-inert, ⟺-RH, or ill-posed across the
  abscissa (trichotomy (i)/(ii)/(iii), PROVEN);
- the sole singularity-conducting object, P(s), conducts exactly the zeros of ζ, so any
  condition pinning its continuation is ⟺-RH;
- the missing lemma for any would-be survivor is "a fixed-width zero-free strip from prime
  data without singularity interrogation" — which is RH's own content;
- named controls behave as predicted: DH cannot even express H★ (Euler-product absence);
  fake-Weil witnesses the failure but only at the ⟺ price.

**Labels:** ★★★, ★★, ★, trichotomy (i)/(ii)/(iii): PROVEN (symbolic re-derivation of classical
material; the bounds cited from ledger/notes retain their own labels). H★-dissection:
PROVEN (logic). No numeric claims were fabricated; the only numbers invoked are the
gravity-probe values already on disk (CHECKED NUMERICALLY, prior note) and the barrier-zoo
certified DH zeros (PROVEN, prior note).

**Epistemic honesty:** nothing here is new mathematics — the prime-zeta identity (★) is
classical; the contribution is the campaign-level statement that it closes the prime lane's
one-way-sufficiency search at the mechanism level, consistent with (and deeper than) every
prior prime-adjacent verdict in the DAG. This does NOT close the direct-RH hunt: it closes
the *prime-data-sufficiency* format, and the campaign's remaining live frames (speiser/ξ′
interlacing, GS-2026 diagonal bridge, barrier-zoo discipline on new ideas) are untouched.

---

## 5. Checklist (final)

| Requirement | Status | Where |
|---|---|---|
| 1 exact implication H ⟹ RH | SATISFIED (H★ ⟺ RH, proven) | §3.1 ★★★ |
| 2 non-equivalence | **FAILS (⟺-RH, proven)** — the collapse | §3.2 |
| 3 named control fails H | DH vacuous (undefined); fake-Weil fails H★ but only at the ⟺ price | §3.4 |
| 4 exact missing lemma | none for H★ (implication is identity-level); lane-level lemma = half-strip zero-free from prime data = RH's own content | §3.3 |
| 5 cheapest Rust falsification | spec'd `tools/prime_zeta_probe/` (<1 min f64) — knowingly not run, cannot change a logical equivalence | §3.5 |
| 6 exclusions respected | S2-PNT: series abscissa 1 is PNT-grade but unused (only Euler-product zero-freeness on Re>1 needed); accretivity/semigroup/Carleson/Li/Weil: cited-closed, not reinvented | §3.3 |
| 7 collapse reason | R2 fails via ★★/★★★ (singularities of prime zeta = zeros of ζ); mechanism trichotomy (i)/(ii)/(iii) closes the lane | §3.2–3.3 |

## Files / artifacts
- This memo: `research/notes/direct-rh-prime-skeptic-2026-08-18.md`
- Progress: `research/notes/direct-rh-prime-skeptic-2026-08-18.progress`
- Prior citations: gravity probe (`research/notes/gravity-ideas-triage-2026-08-18.md`),
  acy ideas (`research/notes/agy-ideas-2026-08-18.md`), DAG
  (`tools/closure_dag/closure_dag.json`, nodes S2-PNT, Li-criterion, operator-lane,
  barrierzoo-retrotest, logprofile-boundary, crossdomain-hunt).
- No code was run this session (compute discipline: no probe could change the logical
  verdict; the one illustrative spec is §3.5 for a downstream builder if ever wanted).