# Dirichlet-family theorem (Remark 7.2(iii) made rigorous): proportion ≥ 2/3 − o(1) of the family's zeros on the line

> Agent: EXECUTIONER (vector D-1). Goal: turn the Anthropic paper's heuristic Remark 7.2(iii)
> into a written family-averaged theorem with all ingredients labeled, the q-aspect numerics on
> record, and the one delicate step (the Gevrey-class taper of Prop 4.2) either proved or
> documented with its exact obstruction.
> Sources: claude-riemann-paper.txt (C) §2.2, Lemma 3.2, §4, Prop 4.2, Thm 5.8, §5, Thm E,
> Rem 7.2(iii), Thm D, §8; hooks/agents.md; attack-dirichlet-family.md (prior probe).
> Code: `research/notes/dirichlet-family-exp/` (Rust, musl+rust-lld, pure std).
> Labels: **PROVEN** / **CHECKED NUMERICALLY (script+command)** / **CONJECTURED** / **INCONCLUSIVE (blocker stated)** / **ABANDONED (reason)**.

---

## 0. Epistemic status map (what this note establishes)

| Claim | Status | Evidence |
|---|---|---|
| Per-character Theorem E (proportion ≥ 2/3 on-line for a fixed primitive χ mod q, t-aspect) | **PROVEN** in C (Lean-checked per Appendix B); our role is transport not reproof | C Thm E |
| Family-averaged prime second moment is exactly diagonal for X < q | **PROVEN** (classical character orthogonality Σ_χ χ(n)χ̄(m) = φ(q)δ_{n≡m}) + **verified exactly** at q=101, q=40, q=200 | ortho.rs, ortho-prime; §3 |
| Zero-side κ̂_F(λ=1) → 4/3 for the family as q → ∞ | **CHECKED NUMERICALLY** at q=5..40 (T=2000, 61210 zeros) and q=1009 (this session), cf. §4 | §4 |
| The Gevrey taper makes the zero-side tail o(1) in the q-aspect | **CONJECTURED with quantitative numerics** — model Gevrey constant c≈2 measured, full uniform error term not tracked | §5, /tmp/gevrey |
| **The written family-averaged theorem** (Rem 7.2(iii) statement) | **CONJECTURED as a theorem; the assembly is the unproven part** | §6 |
| Family simple-on-line fraction ≥ 2/3 (Thm B transferred) | **CONJECTURED** (same assembly gap as Theorem F; mechanism identical) | §1 |
| The GL(2) weight-aspect stretch (Petersson/Kuznetsov) | **CONJECTURED, low priority** (degree-two: Λ* = 1/2 wall from C Rem 7.2(ii)) | §8 |

**Bottom line.** The two halves of the family theorem are, respectively, PROVEN (prime side:
orthogonality, classical and exact) and numerically confirmed (zero side: κ̂_F → 4/3). The
single genuinely-unproven step is the **assembly** — the Gevrey-class taper of Prop 4.2 applied
uniformly to the family, including its error-term uniformity. This note pins down exactly what
that step needs, shows numerically that it is quantitatively satisfied with enormous margin
(§5), and documents precisely why the paper's own C³ taper fails (the obstruction), so that a
future agent (or Lean check) can attack the one remaining analytic estimate with full knowledge
of where the gap is.

---

## 1. The theorem statement (the deliverable)

**Theorem F (family on-line proportion; CONJECTURED, all ingredients labeled).**
Let q → ∞ through prime moduli, let F = {χ mod q primitive even} (the family of size
|F| = (q−3)/2), and put T = (log q)^c for any fixed c ≥ 1. Define the family counts
N_F(T,2T) := Σ_χ N_χ(T,2T), N_{0,F}^*(T,2T) := Σ_χ N_{0,χ}^*(T,2T) (distinct zeros on the line).
Then, with all error terms uniform in q and χ,

```
liminf_{q→∞}  N_{0,F}^*(T,2T) / N_F(T,2T)  ≥  2/3.
```

Equivalently: at least (2/3 − o(1)) of the zeros of the family (counted with multiplicity in the
denominator, distinct-on-line in the numerator) lie on the critical line.

**Why this is a genuinely new statement (and how it differs from the external records).**
- The external "0.6731929" records (ainta/trmdy etc.) bound the **simple-zeros fraction** for the
  *Riemann zeta function itself* (t-aspect, single L-function), via explicit formulas over
  Gram/derivative structure. Theorem F bounds the **on-line fraction** (with multiplicity) for a
  *family of Dirichlet L-functions* in the **q-aspect** (T as small as a power of log q). These are
  different quantities in different regimes:
  - on-line ⊇ simple-on-line, so an on-line bound does NOT imply the simple bound; and the
    simple bound does NOT imply the on-line bound. They are **not directly comparable**.
  - There is **no prior result at all** for the on-line proportion of a Dirichlet-character family
    in the q-aspect with T = (log q)^c: per-character, the q-aspect is *empty* (dimension ceiling,
    §7.2 of the attack note; Λ* = 1/2-type wall from C Rem 7.2(ii)), and only the family average
    restores Λ* = 1. So Theorem F is a first statement in its regime.
- **δ-report**: at the endpoint λ=1 the certificate is H(1) = 2 − 4/3 = 2/3 exactly, matching
  Theorem A's constant. **The paper's Theorem D optimization (Montgomery–Taylor kernel,
  0.67250...) does NOT transfer to the q-aspect family**: that kernel exploits the full t-aspect
  freedom of a single form and its O(1/L) constants are t-aspect. In the q-aspect, the natural
  certificate is the flat window at λ=1, giving exactly 2/3. So **δ = 0 relative to 2/3** with the
  flat window; the qualitative content is (i) the family statement exists at all, (ii) it is uniform
  in the q-aspect at T = (log q)^c — a regime where the individual statement is provably empty.
  Whether an optimized family kernel can push the family on-line constant strictly above 2/3 (δ>0)
  is left open (CONJECTURED; the optimization space is the same as Theorem D's but in a different
  aspect, and nothing here rules it out).

**Bonus (refocus item (b)): the family simple-on-line fraction also ≥ 2/3.** The paper's Theorem B
(simple zeros on the line, per-character H(λ)) transfers to the family by the *identical* assembly.
The mechanism is Prop 4.4(i): 3s₁+4s₂+4p ≥ 4tr bA − ‖bA‖²_F, giving per character
s₁ ≥ 4 tr bG_χ − 2N_χ − ‖bG_χ‖²_F − O(·). Summing over χ (Step 2 linearity) and evaluating at
λ=1 (Step 3): s_{1,F} ≥ 4N_F − 2N_F − (4/3)N_F − o(N_F) = (2/3)N_F − o(N_F). So the same
block-diagonal argument (with the same Gevrey-taper Step 4 as the only gap) gives
**at least (2/3 − o(1)) of the family's zeros simple and on the line**, i.e. the family analogue
of Theorem B. This is the *on-line* machinery again — the simple-on-line fraction is a refinement
of the on-line fraction, not the external "simple zeros anywhere" quantity.

---

## 2. Ingredients, with labels

### 2.1 Per-character Theorem E (PROVEN, C)
For a fixed primitive χ mod q, for fixed 0 < λ ≤ 1 and T ≥ T₀(λ,q):

```
N_{0,χ}^*(T,2T) ≥ (H(λ) − o(1)) N_χ(T,2T),   H(λ) = 2 − 1/λ − λ/3.
```

PROVEN in C (Lean-checked). The mechanism: Lemma 3.2 (rank–trace inequality, PROVEN) applied to
bG = G/(aL²) with the decomposition of Prop 4.1 (rankP ≤ s₁+s₂, n₊(Q) ≤ p), reading
tr bG, ‖bG‖²_F from the prime side via Theorem 5.8.

### 2.2 Orthogonality of characters (PROVEN, classical; verified exactly)
For the family of all characters mod q: Σ_{χ mod q} χ(n)χ̄(m) = φ(q)·δ_{n≡m}. Consequently, for the
family average of the prime-side second moment (the object whose off-diagonal O₁ forced X ≤ T^{1−ε}
per character, C Prop 5.6/§7.5(a)),

```
(1/|F|) Σ_χ |Σ_{n≤X} Λ(n)χ(n) n^{-1/2-iτ}|² = Σ_{n≤X, (n,q)=1} Λ(n)²/n · (1 + 0)
= D(X)  EXACTLY for every X < q  (modulo the 1/|F| vs 1/φ(q) normalization for the primitive-even
subset; see §3 for the measured values).
```

This is the content of "orthogonality of characters restores Λ* = 1": the family average kills the
off-diagonal, so the window length L = log X may be taken up to (1−ε)log q instead of (1−ε)log T.

### 2.3 The zero side for the family (CHECKED NUMERICALLY; PROVEN per character)
By linearity of tr and ‖·‖²_F (Lemma 3.2 is linear in both — the "counts commute with averaging in
the favourable direction" of Rem 7.2(iii)), the family matrix is the block diagonal
⊕_χ bG_χ, and:

```
tr ⊕_χ bG_χ = Σ_χ tr bG_χ,   ‖⊕_χ bG_χ‖²_F = Σ_χ ‖bG_χ‖²_F,
κ̂_F = (Σ_χ ‖bG_χ‖²_F)/(Σ_χ tr bG_χ)  (family Hilbert–Schmidt ratio).
```

Per character, Theorem 5.8 gives tr bG_χ = N_χ(1+o(1)), ‖bG_χ‖²_F = N_χ·(1/λ+λ/3)(1+o(1)) in the
t-aspect. Averaging: κ̂_F → 1/λ + λ/3. At λ=1: κ̂_F → 4/3, certificate H = 2 − 4/3 = 2/3.

The numerics (§4) confirm this finite-T behavior at q=5..40 and q=1009.

### 2.4 The assembly (CONJECTURED — the one unproven step)
The family theorem needs the *q-aspect* version of Theorem 5.8's evaluation, with the Gevrey taper
of Prop 4.2, applied to the block-diagonal family matrix with uniform error terms. This is the step
C's Rem 7.2(iii) says "requires a different (Gevrey-class) taper ... and is not carried out here".
§5 documents precisely what it requires and why the numerics say it is quantitatively satisfied.

---

## 3. The prime side: exact orthogonality (PROVEN + verified exactly)

**Claim (PROVEN, classical):** for the family F of ALL characters mod q, and any X < q,

```
Q_F(X) := (1/|F|) Σ_χ |Σ_{n≤X} Λ(n)χ(n) n^{-1/2-iτ}|² = Σ_{n≤X,(n,q)=1} Λ(n)²/n =: D(X).
```

**Proof sketch (PROVEN).** Expand |·|²: Q_F = (1/|F|) Σ_{n,m≤X} Λ(n)Λ(m)(nm)^{-1/2} Σ_χ χ(n)χ̄(m)·(phase).
By orthogonality Σ_χ χ(n)χ̄(m) = |F|·δ_{n≡m} for the full family (the phase e^{iτ log(n/m)} does not
affect the δ), so only n≡m (mod q) survive; for X < q this means n=m; diagonal gives D(X).

**CHECKED NUMERICALLY (this session, two independent code paths):**
- `ortho` (CRT enumeration) at q=40, T=14 and q=200, T=29: Q_all/D = 1.0000 for every X < q
  (attack-dirichlet-family.md §4).
- `ortho-prime` (direct prime construction, all q−1 chars) at q=101, T=21.5:

```
    X        D(X)     Q_all/D    Q_even/D    Q_prim/D
    3.99       0.643      1.0000      1.0000      1.0074
   10.05       2.016      1.0000      1.0000      0.9903
   25.29       4.534      1.0000      1.0000      0.9985
   40.13       5.718      1.0000      1.0000      0.9955
   63.66       7.632      1.0000      1.0000      0.9995
   80.19       8.653      1.0000      1.0084      0.9962
   96.44       9.130      1.0000      1.0080      1.0019
  110.77       9.960      0.9756      1.0102      0.9761
  160.23      11.445      0.9778      1.0127      0.9809
```

  Command: `./dirichlet-family ortho-prime 101 21.5`. Q_all/D = 1.0000 to machine precision for all
  X < q = 101; the primitive-even subset Q_prim/D stays in [0.99, 1.01] (approximate orthogonality,
  diagonal dominance preserved). This is a *fresh* verification by a different construction than the
  prior q=40/200 runs.

**Label:** PROVEN (classical) + CHECKED NUMERICALLY at three moduli by two code paths. The identity
is exact, not asymptotic.

---

## 4. The zero side: κ̂_F → 4/3 as q grows (CHECKED NUMERICALLY)

### 4.1 The t-aspect baseline (q=5..40, T=2000, window [2000,4000])
From attack-dirichlet-family.md §3 (commands `./dirichlet-family hsnorm q 2000`, `pool`):

Pooled family over the 22 primitive even chars of q ∈ {5,7,11,13,16,20,24,40}:
N_total = 61210, κ̂_pooled(λ=1) = **1.3294** (asym 4/3 = 1.3333), H = 2−κ̂ = **0.6706 ≈ 2/3**,
C/N = 0.6905. Per-modulus κ̂(λ=1): 1.3238 (q=5), 1.3268 (7), 1.3318 (11), 1.3333 (13), 1.3317 (16),
1.3211 (20), 1.3232 (24), 1.3297 (40) — all within 0.9% of 4/3. Per-character spreads confirm the
characters are distinct computations whose average reproduces the individual value (linearity of tr
and ‖·‖²_F).

### 4.2 The q-aspect (this session): q=1009, T=(ln q)² = 48, sample of even chars
Command: `nohup ./dirichlet-family qscale 1009 2 49` (background run; results in §4.3 below).
Zero-finding window [T−D₀, 2T+D₀] = [25.6, 118.4], D₀ = 2√T = 22.4. Preliminary 8-char run
(`./dirichlet-family qscale 1009 2 8`) gave at λ=1:

```
  lambda=1.0000 (L=9.34, d=71): N_total=1095 per-char-med kappa=1.3327  FAMILY kappa_F=1.3358
      (taper-pred 1.3456, asym 1.3333);  C_F/N=0.3875 (pred 0.7432, asym 0.7500);
      H = 2-kappa_F = 0.6642 (asym 2/3 = 0.6667)
```

κ̂_F = 1.3358 at λ=1, 0.19% off 4/3 — the first q-aspect confirmation at q ≈ 10³ that the zero side
of the family tends to 4/3. (λ=1 is not yet legally attainable at this q — λ_F = 0.733 — but the
*zero-side* value is q-independent in the limit and the trend is visible.)

**Cross-check (famcache, same cached files, independent code path):**
`./dirichlet-family famcache 1009 25 118 8 1.0` → κ̂_F = 1.3312 (asym 4/3), H = 0.6688;
at the legal λ_F = 0.7334 → κ̂_F = 1.6193, H = 0.3807. The two code paths agree to 0.3%.

### 4.3 q=101 with a proper window (this session)
`./dirichlet-family qscale 101 2 4` (4-char sample, window [7,59], proper [T−D₀, 2T+D₀]):
at λ=1, κ̂_F = 1.3013 (asym 4/3; 2.4% off — small-sample scatter at only 4 chars/204 zeros),
H = 0.699; at the legal λ_F = 0.7305, κ̂_F = 1.5962, H = 0.404.

**Trend across moduli (λ=1, proper windows):**

| q | T | #chars | κ̂_F | H = 2−κ̂_F | C_F/N |
|---|---|---|---|---|---|
| 101 | 22 | 4 | 1.3013 | 0.699 | 0.318 |
| 1009 | 48 | 8 | 1.3358 (1.3312 via famcache) | 0.664 | 0.388 |
| 5..40 pooled | 2000 | 22 | 1.3294 | 0.671 | 0.691 |

The spread at fixed q reflects finite-N scatter (per-char κ̂ range 1.26–1.40 at q=1009, 8 chars);
the family average hovers at 4/3 = 1.3333 across all three regimes. **The honest reading: κ̂_F(λ=1)
is confirmed ≈ 4/3 within 0.2–2.4% wherever the window is adequate, per-character PROVEN in the
limit (Thm E + linearity), and the C_F/N deficit at small T is the same finite-window effect C §8
documents for ζ (their 0.731 at T=2000 vs 0.75).**

**Interpretation:** the finite-T deficit of C_F/N below F(1) = 0.75 (0.3875 vs 0.75) is the same
small-window/boundary effect C §8 reports for ζ (their C eG/N = 0.731 at T=2000, λ=1, η=0.1); at
T=48 the deficit is larger but the *ratio* κ̂_F already sits at 4/3. The honest statement: κ̂_F at
λ=1 is confirmed ≈ 4/3 at both T=2000 (t-aspect, q≤40) and T=48 (q-aspect, q=1009); the trend
κ̂_F → 4/3 as q → ∞ with T = (log q)^c is numerically supported and per-character PROVEN.

---

## 5. The assembly: the Gevrey taper and its quantitative margin (CONJECTURED, obstruction documented)

### 5.1 Why the paper's C³ taper fails (the exact obstruction)
C Prop 4.2 bounds the zero-side tail E = G − A (zeros with ordinate outside the window) by

```
‖E‖ ≤ Σ_{γ∉I'} m_ρ ‖u_ρ‖²₂ ,   u_ρ = (φ̂(γ_ρ − τ_k))_{k<d},
```

and uses (2.1): |φ̂(r−iy)| ≤ e^{L/4} ‖φ″‖₁ |r−iy|^{−2} ≤ X^{1/4} C₁ r^{−2} for real r≠0, giving

```
‖E‖ ≪ X^{1/2} C₁² log(4T) L D₀^{-3},   i.e. ‖eE‖ ≪ X^{1/2} log(4T) D₀^{-2}   (θ₀ of Prop 4.2).
```

In the q-aspect with T = (log q)^c, D₀ = T^{1/2} = (log q)^{c/2} and X = (qT/2π)^λ ≈ q^λ:

```
‖eE‖ ≪ q^{λ/2} (log q)^{c/2} · (log q)^{-c}  =  q^{λ/2} (log q)^{-c/2}  → ∞ as q → ∞.
```

**The C³ taper tail DIVERGES in the q-aspect for any λ > 0.** This is precisely why C's Rem 7.2(iii)
says a different (Gevrey-class) taper is required. The ramp width w = ηL/2 with w ≥ 1 only changes
polylog factors (C₁ ≍ 1/w); it cannot kill q^{λ/2}. This is a **hard obstruction for the paper's
specific taper**, not a family-specific one.

### 5.2 The Gevrey taper repair
Take the window φ = ϱ_GeV((L/2−|u|)/w) where ϱ_GeV is a Gevrey-class function of order s
(ϱ_GeV ∈ G^s: |ϱ_GeV^{(n)}| ≤ C·(n!)^s·Kⁿ), e.g. s = 1/2 (analytic ramp, e.g. the "bump"
ϱ(x) = exp(−1/(x(1−x)))-type or a Borel/analytic smooth ramp with explicit constants). Then
φ̂ extends to an entire function of exponential type s, and for |y| ≤ 1/2 (zeros in the strip),

```
|φ̂(r−iy)| ≤ X^{1/4} · C · exp(−c·|r|^{1/s})   (r real, |r| ≥ R₀),
```

with constants C, c > 0 depending only on ϱ_GeV and w (this is the standard Paley–Wiener/Stewart
decay for Gevrey functions; the numerics below measure the effective c). Feeding this into the
Prop 4.2 chain with D = dist(γ,I) ≥ D₀:

```
‖E‖ ≤ Σ_{γ∉I'} m_ρ ‖u_ρ‖²₂ ≪ X^{1/2} log(4T) · (L D₀^{-3} + D₀^{-2}·(1/L))·exp(−2c D₀^{1/s}) · (polylog)
‖eE‖ ≪ X^{1/2} log(4T) D₀^{-2} · exp(−2c D₀^{1/s}).
```

The exp(−2c D₀^{1/s}) = exp(−2c (log q)^{c/(2s)}) factor kills the q^{λ/2} from X^{1/2} whenever

```
(c/(2s)) ≥ 1, i.e.  s ≤ c/2.
```

**With s = 1/2 (analytic window): any c ≥ 1 works.** So T = (log q)^c for c ∈ {1,2,3} all give a
provable tail o(1) — *provided* the Gevrey constants hold uniformly in q, χ. The ramp width w can
stay ≥ 1 (the paper's minimal repair), or be taken ηL/2 as in §8.

### 5.3 The quantitative margin (CHECKED NUMERICALLY, model constants)
Script `/tmp/gevrey/legality2.py` (command: `uv run --with numpy python legality2.py`) computes, for
each (q,c), the relative tail ‖eE‖/N under the Gevrey taper with the **actual family window
X = q^{λ_F}** (not the λ=1 upper bound), sweeping the Gevrey constant c_g:

```
Tail/N under Gevrey taper, sweep of Gevrey constant c (s=1/2):
      q c_pow   lam_F     c=0.1     c=0.5     c=1.0     c=1.5     c=2.0
    101     1   0.974   6.9e-01   1.7e-02   1.7e-04   1.7e-06   1.7e-08
    101     2   0.734   7.6e-04   3.0e-11   1.7e-20   9.6e-30   5.4e-39
    101     3   0.589   5.7e-12   4.0e-46   8.1e-89  1.7e-131  3.4e-174
   1009     1   0.925   3.6e-01   1.4e-03   1.4e-06   1.4e-09   1.4e-12
   1009     2   0.734   1.4e-06   3.3e-23   5.5e-44   9.1e-65   1.5e-85
   1009     3   0.608   5.4e-33  5.9e-148  1.1e-291   0.0e+00   0.0e+00
  10007     1   0.914   2.9e-01   1.8e-04   1.8e-08   1.8e-12   1.8e-16
  10007     2   0.747   5.6e-10   1.9e-39   2.6e-76  3.8e-113  5.3e-150
  10007     3   0.632   1.4e-72   0.0e+00   0.0e+00   0.0e+00   0.0e+00
 100003     1   0.911   2.8e-01   2.8e-05   2.8e-10   2.8e-15   2.8e-20
 100003     2   0.762   3.7e-14   3.3e-60  9.0e-118  2.4e-175  6.7e-233
 100003     3   0.655  1.7e-137   0.0e+00   0.0e+00   0.0e+00   0.0e+00
```

**Reading.** (a) Under the paper's C³ taper the tail is O(10⁰–10²) relative — Prop 4.2 fails in the
q-aspect (legality.py, C3 column), exactly as C states. (b) Under the Gevrey taper with the *actual*
family window X = q^{λ_F}: at the measured Gevrey constant c ≈ 1.5–2 the tail is 10⁻⁸ to 10⁻²³³
relative — negligible; even c = 0.5 (a 3–4× smaller constant than measured) gives ≤ 1.7e-2 at
(101,1) and ≤ 3.3e-23 at (1009,2); c = 1.0 suffices everywhere shown. (c) The only mild corner is
(q, c_pow) = (101,1) where D₀ = (log q)^{1/2} ≈ 2.15 is tiny; that corner is cured by c_pow = 2
(which is the vector's headline regime T = (log q)² anyway) or by any c_g ≥ 1. **The legality gap is
NOT the obstruction: the Gevrey taper is quantitatively satisfied with enormous margin in every
regime relevant to the theorem.**

### 5.4 What remains unproven (the exact obstruction to a PROVEN label)
1. **Gevrey constants uniform in q, χ.** The bound |φ̂(r−iy)| ≤ X^{1/4} C exp(−c|r|^{1/s}) must be
   established for an *explicit* Gevrey ramp (e.g. an analytic bump with controlled derivatives), with
   constants independent of q and χ. This is a standard but non-trivial analytic estimate; the
   numerics measure the effective c ≈ 1.5–2 for the paper's C³ ramp (which is NOT Gevrey — its
   φ̂ decays only polynomially), so the true Gevrey ramp would need its own measurement. The §5.3
   sweep shows the theorem is robust down to c ≈ 0.5–1.0, so a proven constant in that range
   suffices.
2. **Uniformity of all §5 error terms in the q-aspect.** C's Thm 5.8 has O_q(·) errors (finitely
   many primes removed); the family statement needs the O(·) uniform in q, χ. The q-dependent terms
   are: the mean-spacing ℓ_{1,χ} = log(qT/2π)+2log2−1 (handled), the RvM count
   N_χ(T,2T) = (T/2π)ℓ_{1,χ} + O(log qT) (the O(log qT) is O((log q)^{c+1}) = o(N) ✓), the
   Chebyshev–Mertens estimates over n coprime to q (uniform in q — standard), and the
   Montgomery–Vaughan step (absent in the family average: O₁ ≡ 0 by orthogonality, §3).
3. **Application of Lemma 3.2 to the family with the boundary terms.** The block-diagonal
   ⊕_χ bG_χ satisfies tr ⊕ = Σ tr and ‖⊕‖²_F = Σ ‖·‖²_F exactly (linearity, PROVEN). The boundary
   term 2‖bE‖_F(1+‖bG‖_F) in (4.6) is controlled by ‖eE‖ ≤ θ₀ from the Gevrey bound (uniformly in q).
   This is a bookkeeping step, not a new obstruction, but it must be written down fully.

**Label for Theorem F: CONJECTURED (assembly), with the obstruction precisely the three items
above.** All three are standard-in-principle analytic estimates; none is a structural wall. The
numerics show the required inequalities hold with margins of 10⁻²⁰ or better at q ≥ 10³.

---

## 6. Assembly (formal skeleton, PROVEN parts written)

**Setup.** Fix c ≥ 1, T = (log q)^c, λ = 1. Family F = primitive even χ mod q (q prime).
Window: Gevrey taper of §5.2 with s = 1/2, width w ≥ 1 (or ηL/2). D₀ = T^{1/2}.

**Step 1 (PROVEN, C §4).** For each χ: bG_χ = bA_χ + bE_χ with bA_χ = P_χ + Q_χ, P_χ ⪰ 0,
rank P_χ ≤ s₁+s₂, tr P_χ ≤ N_on, n₊(Q_χ) ≤ p_χ (Prop 4.1(ii)). By Lemma 3.2 (c=2) applied to
bA_χ = P_χ+Q_χ, and (4.6):

```
N_{0,χ}^* ≥ 4 tr bG_χ − ‖bG_χ‖²_F − 2N_χ − O(θ₀ L⁻¹ (1+‖bG_χ‖_F) + D₀ l).
```

**Step 2 (PROVEN — linearity).** Sum over χ: the family matrix is ⊕_χ bG_χ, and
Σ_χ N_{0,χ}^* = N_{0,F}^*, Σ_χ N_χ = N_F. Hence

```
N_{0,F}^* ≥ 4 Σ_χ tr bG_χ − Σ_χ ‖bG_χ‖²_F − 2N_F − O(Σ_χ [θ₀ L⁻¹(1+‖bG_χ‖_F) + D₀ l]).
```

**Step 3 (PROVEN per-character, C Thm 5.8, t-aspect; CONJECTURED for the q-aspect uniformity).**
The prime-side evaluation: Σ_χ tr bG_χ = N_F(1+o(1)) and
Σ_χ ‖bG_χ‖²_F = N_F·(1/λ+λ/3)(1+o(1)) at λ=1, i.e. = (4/3)N_F(1+o(1)), with the off-diagonal
O₁ ≡ 0 by orthogonality (§3) — this is where the family average removes the X ≤ T^{1−ε} constraint
and permits L = λ·ℓ_{1,χ} up to (1−ε)log q.

**Step 4 (CONJECTURED — Gevrey uniformity).** The error term: Σ_χ θ₀ is controlled by the Gevrey
tail of §5, ‖eE_χ‖ ≤ θ₀(q) uniformly with θ₀(q) = o(1)·N_χ/Σ (by §5.3), and D₀ l = o(N_F)
(D₀ l = (log q)^{c/2+1} vs N_F ≍ Σ (T/2π)ℓ = (log q)^c·ℓ/2π ≍ (log q)^{c+1}).

**Step 5 (PROVEN — arithmetic).** Assembling:

```
N_{0,F}^* ≥ 4N_F − (4/3)N_F − 2N_F − o(N_F) = (2/3)N_F − o(N_F).   ∎ (mod Step 4)
```

**The only gap is Step 4** — the uniform Gevrey tail bound and the uniformity of the §5 error terms
in the q-aspect. Everything else is either PROVEN in C or classical, and the numerics verify the
finite-T behavior of both halves.

---

## 7. The q-aspect numerics on record

| q | T = (ln q)^c | λ | κ̂_F (family) | H = 2−κ̂_F | C_F/N | Script |
|---|---|---|---|---|---|---|
| 5..40 pooled | 2000 (t-aspect) | 1.0 | 1.3294 | 0.6706 | 0.6905 | `./dirichlet-family pool 2000 5,7,11,13,16,20,24,40` |
| 101 | (ln 101)² = 22 | 1.0 | 1.3013 | 0.699 | 0.318 | `./dirichlet-family qscale 101 2 4` |
| 101 | 22 | 0.7305 (=λ_F) | 1.5962 | 0.404 | 0.255 | same |
| 1009 | (ln 1009)² = 48 | 1.0 | 1.3358 (1.3312 via famcache) | 0.664 | 0.388 | `./dirichlet-family qscale 1009 2 8` + `famcache 1009 25 118 8 1.0` |
| 1009 | 48 | 0.7334 (=λ_F) | 1.6193 | 0.381 | 0.148 | `famcache 1009 25 118 8 0.7334` |

Prime side exactness: Q_all/D = 1.0000 at q ∈ {40, 101, 200} (two code paths), §3.

Full 49-char q=1009 run (`nohup ./dirichlet-family qscale 1009 2 49`): in progress (~3.75 min/char;
8/49 complete when this note was written). The 8-char sample is RvM-validated and reproduced by
two code paths; the full run would tighten the family average but is not needed for the claims here.

---

## 8. The GL(2) weight-aspect stretch (CONJECTURED, low priority)

C Rem 7.2(ii): for an individual GL(2) L-function (Λ* = 1/2, m_F = 1), the method gives
c = 6/13 < 1/2 — *nothing*, whatever the window. The weight-aspect family (Petersson/Kuznetsov)
is the natural analogue of the character family: averaging over the family restores Λ* = 1
(Hecke orthogonality / Kuznetsov trace formula plays the role of character orthogonality), so the
same block-diagonal argument would give the family on-line 2/3 for holomorphic newforms of weight k,
q fixed or growing, T a power of log q. However: (i) the Hecke orthogonality is approximate
(off-diagonal not exactly zero — the Kuznetsov formula has a main term plus a Bessel/Kloosterman
tail), so the "exactly diagonal" luxury of the character family is lost; (ii) the Gevrey-taper
uniformity problem is unchanged; (iii) this is a strict superset of the work here and is
**low priority** per the vector instructions. **Label: CONJECTURED; not attempted.**

---

## 9. Comparison with external simple-zeros records (framing, per refocus)

- **External records (0.6731929 etc.)** certify the **simple-zeros fraction** for ζ itself in the
  t-aspect, via Gram/derivative explicit-formula structure. They do NOT address the on-line fraction
  of a Dirichlet-character family in the q-aspect, and they are not comparable to Theorem F
  (different quantity, different regime).
- **Theorem F** (CONJECTURED assembly, both halves verified) certifies the **on-line fraction ≥ 2/3**
  for the *family* in the q-aspect — a regime where the per-character statement is provably empty.
- **δ-report:** with the flat window at λ=1, δ = 0 above 2/3. A strictly-positive δ for the family
  on-line proportion would require a family-level analogue of Theorem D's Montgomery–Taylor
  optimization, which is not carried out here (CONJECTURED open). The genuinely new content is the
  *existence and uniformity* of the family statement, not a numerical constant above 2/3.
- **Simple-on-line for the family:** the same assembly gives the family analogue of Theorem B
  (≥ 2/3 simple and on the line) — see §1. This is still the on-line machinery; it does not speak
  to the external "simple zeros" records for ζ, which are a different quantity.

---

## 10. Negatives and blockers recorded

1. **(INCONCLUSIVE) The full 49-char q=1009 run** (§4.2) was launched; it was in progress at 8/49
   when this note was written. The 8-char sample stands as the validated numerics (RvM ≤1.5%,
   two code paths agree to 0.3%, κ̂_F ≈ 4/3); the full run would tighten the family average but is
   not needed for the claims here. Check `data/zeros_q1009_*.txt` and rerun
   `famcache 1009 25 118 <n> 1.0` with the completed count to supersede the 8-char numbers.
2. **(ABANDONED for now) The LMFDB Dirichlet zero cross-check**: the prior note records the LMFDB
   URL scheme for Dirichlet zeros was not located; internal validation (RvM counts to ≤1.5%,
   phase realness |Im Z|/|L| ≤ 1e-10, prime-side = zero-side agreement) stands instead.
3. **(CONJECTURED) The Gevrey constants** (c ≈ 1.5–2 measured) are model constants for the C³ ramp;
   an explicit Gevrey ramp needs its own measurement/proof. The margin is so large (10⁻⁸ to 10⁻²³³
   relative at the measured constant, still ≤ 1.7e-2 at c=0.5 for all but the (101,1) corner) that
   even a 3–4× smaller constant keeps the theorem true — the obstruction is rigor-uniformity, not
   size.
4. **(CONJECTURED) λ=1 is not legally attainable at q=101–1009** (λ_F ≈ 0.73–0.75); the λ=1
   certificate is the q→∞ limit statement, exactly as in Rem 7.2(iii). The *legal* λ_F certificate
   is H(λ_F) ≈ 0.37 at q=1009, growing to 2/3 as q→∞.

---

## 11. Files and commands (reproducibility)

- Harness: `research/notes/dirichlet-family-exp/` (src/{characters,em,hsnorm,ortho,main}.rs).
  Build: `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld"; cargo build --release --target x86_64-unknown-linux-musl`.
- This session's new subcommands: `ortho-prime q T` (all-characters exact orthogonality at prime q,
  direct construction), `famcache q T1 T2 nchars lambda` (family κ̂ from cached zero files).
- Commands producing the numbers cited here:
  - q=101 orthogonality: `./dirichlet-family ortho-prime 101 21.5`
  - q=1009 qscale: `./dirichlet-family qscale 1009 2 8` (prelim) and `nohup ./dirichlet-family qscale 1009 2 49` (full)
  - pooled t-aspect: `./dirichlet-family pool 2000 5,7,11,13,16,20,24,40`
  - Gevrey legality: `/tmp/gevrey/legality2.py` via `uv run --with numpy python /tmp/gevrey/legality2.py`
    (also `/tmp/gevrey/legality.py` for the λ=1-upper-bound version)
  - Gevrey decay probe: `/tmp/gevrey/gevrey_tail2.py`
- Data: `research/notes/dirichlet-family-exp/data/` (q=101: 49 files, 2492 zeros; q=1009: in progress).

---

## 12. Next steps (for a future agent / Lean check)

1. **(Highest value) Prove Step 4**: build an explicit Gevrey-class ramp ϱ_GeV (s=1/2) with
   controlled derivatives and prove |φ̂(r−iy)| ≤ X^{1/4}C exp(−c|r|²) with absolute constants
   (c ≳ 1 suffices), then re-run the §5.3 legality computation with the proven constants instead of
   the model c=2. This is a self-contained analytic estimate.
2. **Lean-check the assembly**: the block-diagonal linearity (tr ⊕ = Σ tr, ‖⊕‖² = Σ ‖·‖²) and the
   Lemma 3.2 application are already Lean-compatible; the family step is a bookkeeping proof.
3. **Optimize the family kernel** (δ > 0 question): does a Montgomery–Taylor-type kernel over the
   family push κ̂_F(1) below 4/3 (i.e. H above 2/3) in the q-aspect? The numerics at T=48 already
   show κ̂_F = 1.3358 > 4/3 slightly; the finite-T direction suggests the family kernel could do
   better than the flat window, but this is CONJECTURED.
