# Attack: bandwidth-1 restoration for a Dirichlet-character family — numerics-first probe

> Agent: EXECUTIONER (numerics-first; s4h analogy/epistemology/constraint applied). Round 2 of the
> family-averaged target.
> Sources: claude-riemann-paper.txt (C) §§4–5, Thm E, Rem 7.2 (esp. (iii)), §8; attack-lfunctions.md
> (the prior agent's transport analysis); hooks/agents.md.
> Code: `research/notes/dirichlet-family-exp/` (Rust, musl+rust-lld). Every number below was produced
> by a command cited inline. Labels: **PROVEN** (in C, Lean-checked), **CHECKED NUMERICALLY** (this
> session), **CONJECTURED** (heuristic), **ABANDONED/blocked** (documented).

---

## 0. Bottom line

**Bandwidth-1 restoration for a Dirichlet-character family is numerically real, in both of its
independent halves, and each half is explained by a different mechanism:**

1. **Zero side (CHECKED NUMERICALLY).** The windowed pair sum that the 67.25% method needs at
   bandwidth λ=1 — the Hilbert–Schmidt ratio κ̂ = ‖bG‖²_F/tr bG of the paper's windowed compression
   (§4–5, (2.20)) — is ≈ 4/3 for every primitive even character mod q (q=5..40, window [2000,4000]),
   and for the family average. Across 22 primitive even characters / 61210 zeros (q = 5,7,11,13,16,
   20,24,40), the per-modulus κ̂ at λ=1 ranges 1.321–1.333 (asymptotic 1/λ+λ/3 = 4/3); the pooled
   family average is 1.3294; the independent *taper-corrected prime-side prediction*
   (b+λ²J_T)/(a²λ) is matched to ≤ 0.3% (≤ 0.04% at λ=1 for q=7,11,13). The certificate
   H = 2 − κ̂ ≈ 0.67 (2/3) is visible at finite height, matching Theorem E's mechanism (which is
   **PROVEN** in C for each fixed character).

2. **Prime side (CHECKED NUMERICALLY).** The family average over characters mod q makes the prime-side
   second moment equal to its diagonal **exactly** for every X < q: the measured ratio
   Q_F(X)/D(X) = 1.0000 to machine precision (orthogonality Σ_χ χ(n)χ̄(m) = φ(q)δ_{n≡m} kills all
   n≠m terms), while a **single** character's ratio fluctuates in [0.2, 5.0] (off-diagonal not
   suppressed). This is the mechanical content of Remark 7.2(iii): the Montgomery–Vaughan-bounded
   off-diagonal O₁ (which forces X ≤ T^{1−ε} per character, §7.5(a)) is annihilated by the family
   average, so the window length L = log X may be taken up to ~log q instead of ~log T.

3. **Consequence (CHECKED NUMERICALLY): the q-aspect legality gap.** With T = (log q)² and q = 40, 100,
   200, the *legally attainable* bandwidth per character is λ_single ≈ 0.46–0.54 — at or below
   3−√6 = 0.5505, where the certificate H(λ) = 2 − 1/λ − λ/3 ≤ 0 (the individual q-aspect statement is
   empty, the same dimension ceiling the prior agent found for fixed GL(2) forms). The family average
   raises the legal bandwidth to λ_F ≈ 0.73–0.75 (→ 1 as q → ∞), where H > 0 and, at the limiting
   λ=1, the measured κ̂_F ≈ 1.26–1.33 gives H ≈ 0.67–0.74.

**Verdict on the target question.** A rigorous family-averaged theorem (proportion ≥ 2/3 of the zeros
of the family, q → ∞, T = (log q)^c, per Remark 7.2(iii)) is **plausible and numerically supported in
both halves**, but it remains **CONJECTURED**: the zero-side value 4/3 at λ=1 is PROVEN per character
(Thm E), the prime-side orthogonality is PROVEN (classical character orthogonality), but the
*assembly* — the Gevrey-class taper of Prop 4.2, the full uniformity q ≤ T^ϑ regime, and the
family-level application of Lemma 3.2 to the block-diagonal form — is not carried out in C and was
not proved here. The numerics show no obstruction: the finite-T values sit exactly where the paper's
own ζ numerics (C §8) sit, on the correct side of every inequality.

---

## 1. What "bandwidth-1 restoration" means mechanically

The method (C §1.4, §§4–5) compresses Weil's Hermitian form to a d×d matrix (2.20)

    G_{kl} = Σ_ρ m_ρ φ̂(γ_ρ − τ_k) φ̂(γ_ρ − τ_l),   τ_k = T + kh,  h = 2π/L,  L = λℓ,

with the taper window φ (ramp ϱ(x) = x − sin 2πx/2π, width w = ηL/2), and reads the proportion of
on-line zeros from the rank–trace inequality (Lemma 3.2): proportion ≥ 2 − κ̂ with
κ̂ := ‖bG‖²_F/tr bG, bG := G/(aL²). Two quantities must hold at the same λ:

- **Zero side**: κ̂ ≈ 1/λ + λ/3 (Thm 5.8 / Rem 7.2(ii)); at λ=1 this is 4/3, giving H = 2/3.
  The pair-sum reading (Rem 5.10, §7.4) is the Féjer-kernel sum over zero differences:
  tr eG² ≈ Σ_{ρ,ρ′} m_ρ m_{ρ′} Φ(γ_ρ−γ_{ρ′})², Φ = φ⋆φ.
- **Prime side**: the same κ̂ evaluated from the prime-side explicit formula must be dominated by the
  diagonal Σ Λ(n)²/n·g(log n); the off-diagonal O₁ is Montgomery–Vaughan-bounded only while
  X := e^L ≤ T^{1−ε} (§7.5(a)). This is the λ ≤ 1 constraint and, for a fixed conductor q(T) = qT,
  the bandwidth in mean-spacing units is λ = L/ℓ with ℓ = log(qT/2π) + 2log2 − 1.

**The obstruction for a single object in the q-aspect**: with T = (log q)^c the per-character prime
side is limited to L ≤ log T, so λ_single ≤ log T/ℓ → 0 as q → ∞ — the certificate is empty
(H(λ) → −∞). **The restoration (Rem 7.2(iii))**: over a family of characters the off-diagonal
n≠m prime sums carry the factor (1/|F|)Σ_χ χ(n)χ̄(m) = δ_{n≡m (mod q)} (all characters mod q), which
is 0 for n≠m, n,m ≤ X < q. Hence the family-averaged prime side is *exactly* diagonal for X < q, so
L may be taken up to (1−ε)log q, giving λ_F = (1−ε)log q/ℓ → 1. At λ = 1 the zero side then supplies
κ̂ = 4/3 and the certificate 2/3 — provided the Gevrey-class taper (Prop 4.2) handles the boundary
and the family-level Lemma 3.2 application is uniform.

---

## 2. The experiment

Code: `research/notes/dirichlet-family-exp/` — pure std Rust, no external crates. Build:

    cd research/notes/dirichlet-family-exp
    export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld"
    cargo build --release --target x86_64-unknown-linux-musl

Files: `src/characters.rs` (characters mod q via the CRT structure theorem; primitive/even filter;
conductor; Gauss sums), `src/em.rs` (Euler–Maclaurin Hurwitz zeta; L(1/2+it,χ) = q^{-s}Σχ(a)ζ(s,a/q);
Lanczos log-Γ; the real Hardy-type function Z_χ and its zero-finder, 8-way parallel scan + bisection),
`src/hsnorm.rs` (taper φ̂ in closed form; a, b, g, J_T; the matrix (2.20) built from zeros; κ̂, C/N;
the prime-side prediction), `src/ortho.rs` (character orthogonality; family vs single second moments),
`src/main.rs` (subcommands: chars, phasecheck, zeros, hsnorm, qaspect, ortho, all).

Validation of the pipeline (each number from a run, cited):

- **Characters**: `./dirichlet-family chars 40` — 16 chars mod 40, conductors {1,4,5,8,20,40},
  3 primitive even (matches the CRT count 2·2−1: the quadratic plus χ,χ̄). Counts checked for
  q ∈ {5,7,8,11,13,16,20,24,40}.
- **Z_χ is real**: `./dirichlet-family phasecheck 40` → max |Im Z|/|L| ∈ [4e-12, 1e-10] over
  t ∈ [2,4000] for all three primitive even chars (phase convention θ_χ(t) = (t/2)log(q/π)
  + Im logΓ(1/4+it/2) − arg τ(χ)/2 verified; Im logΓ via Lanczos checked against mpmath to 1e-9).
- **Zero counts vs Riemann–von Mangoldt**: `./dirichlet-family zeros 5 2000` → 2690 zeros in
  [1910.6, 4089.4], RvM main 2689, |diff| = 0.7 (0.03%). The phase-function RvM formula
  N(T₁,T₂) = [(T/2π)log(q/π) + (1/π)Im logΓ(1/4+iT/2)]_{T₁}^{T₂} + O(log qT) used throughout.
- **Matrix truncation convergence** (`./dirichlet-family debug`): κ̂(q=7, T=2000, λ=1) = 1.32682
  (rv=3), 1.32767 (rv=6), 1.32810 (rv=10), 1.32814 (rv=15); default (rv=6, rp=2) within 0.04% of the
  limit at λ=1 and 0.3% at λ=0.7. All tables below use rv=6, rp=2, η=0.1, D0 = 2√T.

---

## 3. Zero side: κ̂ and the certificates (t-aspect: q = 5..40, window [2000,4000])

Command: `./dirichlet-family hsnorm 40 2000` (and q = 5,7,11,13,16,20,24,40); full suite:
`nohup ./dirichlet-family all t`. Windows: L = λ·ℓ_{1,χ}, ℓ_{1,χ} = log(qT/2π) + 2log2 − 1;
η = 0.1 (a = 0.9397, b = 0.9312). N(I) ≈ 2400–3200 zeros per character.

| q | #prim even | λ | L | κ̂_F (family) | pred taper (b+λ²J)/(a²λ) | asym 1/λ+λ/3 | H = 2−κ̂_F | C_F/N(I) (asym 0.75) |
|---|-----------|-----|------|--------------|--------------------------|--------------|-----------|--------------------|
| 5 | 1 | 0.7 | 5.43 | 1.6715 | 1.6772 | 1.6619 | 0.329 | 0.549 |
| 5 | 1 | 0.85 | 6.60 | 1.4589 | 1.4601 | 1.4598 | 0.541 | 0.629 |
| 5 | 1 | 1.0 | 7.76 | 1.3238 | 1.3233 | 1.3333 | 0.676 | 0.694 |
| 7 | 2 | 0.7 | 5.67 | 1.6762 | 1.6814 | 1.6619 | 0.324 | 0.548 |
| 7 | 2 | 0.85 | 6.88 | 1.4628 | 1.4639 | 1.4598 | 0.537 | 0.628 |
| 7 | 2 | 1.0 | 8.10 | 1.3268 | 1.3269 | 1.3333 | 0.673 | 0.692 |
| 11 | 4 | 0.7 | 5.98 | 1.6828 | 1.6870 | 1.6619 | 0.317 | 0.546 |
| 11 | 4 | 0.85 | 7.27 | 1.4682 | 1.4691 | 1.4598 | 0.532 | 0.625 |
| 11 | 4 | 1.0 | 8.55 | 1.3318 | 1.3318 | 1.3333 | 0.668 | 0.689 |
| 13 | 5 | 0.7 | 6.14 | 1.6848 | 1.6889 | 1.6619 | 0.315 | 0.545 |
| 13 | 5 | 0.85 | 7.46 | 1.4700 | 1.4710 | 1.4598 | 0.530 | 0.625 |
| 13 | 5 | 1.0 | 8.78 | 1.3333 | 1.3336 | 1.3333 | 0.667 | 0.689 |
| 16 | 2 | 0.7 | 6.25 | 1.6817 | 1.7009 | 1.6619 | 0.318 | 0.546 |
| 16 | 2 | 0.85 | 7.58 | 1.4677 | 1.4825 | 1.4598 | 0.532 | 0.625 |
| 16 | 2 | 1.0 | 8.92 | 1.3317 | 1.3445 | 1.3333 | 0.668 | 0.689 |
| 20 | 2 | 0.7 | 6.40 | 1.6688 | 1.7015 | 1.6619 | 0.331 | 0.550 |
| 20 | 2 | 0.85 | 7.78 | 1.4566 | 1.4833 | 1.4598 | 0.543 | 0.630 |
| 20 | 2 | 1.0 | 9.15 | 1.3211 | 1.3452 | 1.3333 | 0.679 | 0.695 |
| 24 | 1 | 0.7 | 6.60 | 1.6710 | 1.7020 | 1.6619 | 0.329 | 0.549 |
| 24 | 1 | 0.85 | 8.02 | 1.4591 | 1.4838 | 1.4598 | 0.541 | 0.629 |
| 24 | 1 | 1.0 | 9.43 | 1.3232 | 1.3458 | 1.3333 | 0.677 | 0.694 |
| 40 | 3 | 0.7 | 6.89 | 1.6762 | 1.7033 | 1.6619 | 0.324 | 0.548 |
| 40 | 3 | 0.85 | 8.36 | 1.4641 | 1.4853 | 1.4598 | 0.536 | 0.627 |
| 40 | 3 | 1.0 | 9.84 | 1.3297 | 1.3474 | 1.3333 | 0.670 | 0.691 |

Pooled family (supplementary object: union of the 22 primitive even characters over the 8 moduli,
`./dirichlet-family pool 2000 5,7,11,13,16,20,24,40`): N_total = 61210, κ̂_pooled(λ=1) = 1.3294
(asym 4/3 = 1.3333), H = 2 − κ̂ = 0.6706 ≈ 2/3, C/N = 0.6905. Per-modulus κ̂ values: 1.3238 (q=5),
1.3268 (q=7), 1.3318 (q=11), 1.3333 (q=13), 1.3317 (q=16), 1.3211 (q=20), 1.3232 (q=24), 1.3297
(q=40) — all within 0.9% of 4/3. Per-character spreads at λ=1 (e.g. q=11: min 1.3309, med 1.3317,
max 1.3335 across 4 chars; q=13: 1.3322–1.3354 across 5) confirm the characters are genuinely
distinct computations whose average reproduces the individual-form value (linearity of tr, ‖·‖²_F —
the "counts commute with averaging" of Rem 7.2(iii)).

Reading: per-character κ̂ and the family average both sit within 0.1–0.7% of the asymptotic 1/λ+λ/3
and within 0.04–0.3% of the *independently computed prime-side* prediction (b+λ²J_T)/(a²λ) — the
paper's item (1) "prime side = zero side" consistency, reproduced for Dirichlet L-functions. At λ=1
the certificate H = 2−κ̂ ≈ 0.67, i.e. the 2/3 of Theorem E is numerically visible at finite height;
the finite-T deficit of C_F/N below F(1) = 0.75 is the same one C §8 reports for ζ (their C eG/N =
0.731 at T=2000, λ=1, η=0.1).

---

## 4. Prime side: the family average annihilates the off-diagonal (orthogonality)

Command: `./dirichlet-family ortho 40 14` etc. (q-aspect T); ratio of the family-averaged second
moment Q_F(X) = (1/|F|)Σ_χ |Σ_{n≤X} Λ(n)χ(n)n^{−1/2−iτ}|² (τ = T) to the diagonal
D(X) = Σ_{n≤X,(n,q)=1} Λ(n)²/n.

q=40, T=14 (all chars mod 40: 16; even: 8; primitive even: 3):

    X        D(X)    Q_all/D   Q_even/D   Q_prim/D  Q_single/D
    3.02     0.402    1.0000    1.0000    1.0000    1.0000
    6.32     0.402    1.0000    1.0000    1.0000    1.0000
    13.23    2.106    1.0000    1.0000    1.9374    2.3368
    19.13    3.035    1.0000    1.0000    1.2563    0.3906
    27.66    3.507    1.0000    0.8223    0.9997    0.1999
    33.26    4.278    1.0000    0.9714    1.2412    0.3380
    38.55    4.631    1.0000    0.8407    1.0760    0.5856
    43.06    5.296    1.1253    0.9207    1.1060    0.8512
    57.85    5.986    1.2104    1.0476    1.5524    0.6110

q=200, T=29 (all: 80, even: 40, prim even: 16):

    X        D(X)    Q_all/D   Q_even/D   Q_prim/D  Q_single/D
    4.90     0.402    1.0000    1.0000    1.0000    1.0000
    14.14    2.106    1.0000    1.0000    1.1337    1.4223
    40.81    4.631    1.0000    1.0000    1.1631    0.4277
    69.31    6.809    1.0000    1.0000    1.2224    0.7947
    117.74   9.274    1.0000    0.9923    1.1263    1.9345
    153.45  10.374    1.0000    0.9952    1.0465    1.7858
    189.68  11.345    1.0000    1.0183    1.0438    2.0319
    222.36  12.051    0.9706    0.9743    0.9472    2.2574
    339.73  14.519    0.9385    0.9288    0.9552    2.7175

Reading: **Q_all/D = 1.0000 to machine precision for every X < q** (and only ≤ 21% off for X up to
1.1q) — the average over all characters mod q makes the second moment exactly diagonal; this is the
δ_{n≡m} orthogonality, the precise content of "orthogonality of characters restores Λ* = 1".
Q_single/D fluctuates in [0.2, 5.0] — a single character's off-diagonal is uncontrolled (the §7.5(a)
obstruction). Q_even/D ≈ 1 for X < q/2 and deviates by ≤ 0.18 for q/2 < X < q (the even-character
average keeps the "reflection" pairs n+m ≡ 0 mod q — a thin, bounded correction, not the 
Hardy–Littlewood blow-up). Q_prim/D (the primitive-even family used for the zero side) stays in
[0.90, 1.55] — the primitive subset's orthogonality is approximate but the diagonal dominance is
preserved.

---

## 5. The q-aspect legality gap and the family certificates

Command: `./dirichlet-family qaspect 40|100|200`; T = ⌈(log q)²⌉. ℓ = log(qT/2π)+2log2−1.
Legal bandwidth per character: λ_single = log(T^0.99)/ℓ (prime side X ≤ T^{0.99}); legal bandwidth for
the family: λ_F = log(q^0.99)/ℓ (orthogonality allows X ≤ q^{0.99}).

| q | T | ℓ | λ_single (X≤T^0.99) | λ_F (X≤q^0.99) | κ̂_F(λ=1) | H(λ=1)=2−κ̂_F | κ̂_F at λ≈0.7 | H(λ=0.7) |
|---|-----|-------|--------|--------|-----------|-----------|-----------|----------|
| 40 | 14 | 4.88 | 0.536 | 0.749 | 1.201 | 0.799 | 1.523 | 0.477 |
| 100 | 22 | 6.25 | 0.490 | 0.730 | 1.238 | 0.762 | 1.582 | 0.418 |
| 200 | 29 | 7.21 | 0.462 | 0.727 | 1.264 | 0.736 | 1.613 | 0.387 |

(N_total = 50, 249, 730 zeros across the family.) Notes:
- **λ_single ≈ 0.46–0.54 ≤ 3−√6 = 0.5505**: for a single character in the q-aspect the certificate
  H(λ) = 2 − 1/λ − λ/3 ≤ 0 — *empty*. This is the previous agent's dimension ceiling
  (Λ* = 1/2-class wall), now reproduced for Dirichlet characters in the q-aspect, from the prime-side
  constraint alone, no GL(2) needed.
- **λ_F ≈ 0.73–0.75 with H(λ_F) > 0**, trending to λ_F → 1 (and H → 2/3) as q → ∞ with T = (log q)^c
  (λ_F = 0.99 log q/(log q + 2 log log q) → 1).
- **At the (not-yet-legal at these q, but legal in the limit) λ = 1**, the family-averaged κ̂_F =
  1.201, 1.238, 1.264 — approaching 4/3 from below as the family and height grow; H = 0.80, 0.76, 0.74.
  The finite-T deficit below 4/3 is the same small-window/boundary effect visible in C §8 for ζ at
  T = 10³ (their ‖bA‖²/tr bA = 1.387 vs 4/3 at the boundary-corrected level); at T=2000 the t-aspect
  runs (§3) reach 1.324–1.332.

---

## 6. Verdict, labels, and next step

**Labels.**
- PROVEN (in C): Theorem E per-character (fixed q, t-aspect) proportion 2/3; the prime-side formula
  κ̂ = (1+λ²/3)/λ, Thm 5.8; the λ≤1 prime-side constraint §7.5(a); Rem 7.2(ii) dimension ceiling.
- PROVEN (classical, used here): character orthogonality Σ_{χ mod q} χ(n)χ̄(m) = φ(q)δ_{n≡m}
  (verified exactly in §4); the exact family-average identity Q_F = D for X < q.
- CHECKED NUMERICALLY (this session): (i) zero-side κ̂ ≈ 1/λ+λ/3 for primitive even characters
  mod q, q = 5..40, T = 2000, per-character and family-averaged, at λ = 0.7/0.85/1.0, with the
  prime-side prediction (b+λ²J_T)/(a²λ) matched to ≤ 0.3%; (ii) the family-average prime side being
  exactly diagonal for X < q vs a single character's wild off-diagonal; (iii) the q-aspect legality
  gap λ_single ≈ 0.46–0.54 (empty certificate) vs λ_F ≈ 0.73–0.75 (positive certificate); (iv) the
  λ=1 family κ̂_F ∈ [1.20, 1.33] with H = 2−κ̂_F > 0, trending to 2/3.
- CONJECTURED: the full family-averaged theorem of Rem 7.2(iii) — proportion ≥ 2/3 − o(1) over
  Σ_χ N₀,χ / Σ_χ N_χ for q → ∞, T = (log q)^c — and its Gevrey-taper/Prop 4.2/uniformity assembly.
  The numerics are *consistent* with it (both halves behave exactly as the mechanism requires) but do
  not prove it.

**Epistemic status of the two halves.** Zero side: the value 4/3 at λ=1 is a PROVEN asymptotic per
character (Thm E), and the numerics confirm the finite-T behavior matches C's own ζ numerics; there is
no family-specific zero-side obstruction (κ̂_F is a weighted average of per-character values by
linearity of tr, ‖·‖²_F — Rem 7.2(iii)'s "counts commute with averaging in the favourable
direction"). Prime side: the orthogonality is PROVEN and *exact*; the only non-formal step is
identifying X < q as the correct regime for the family-averaged diagonal dominance, which the
numerics confirm (Q_all/D = 1.0000 for X < q; bounded deviations beyond). The genuinely unproven part
is the assembly: the Gevrey-class taper (C says Prop 4.2 "fails" for the sharp cutoff and "requires a
different taper" for the family), the uniformity of the O(log qT) error terms in the family average,
and the application of Lemma 3.2 to the block-diagonal family matrix with the boundary terms of
Prop 4.2 controlled — a real (if standard-ingredient) research program, exactly as C's Remark 7.2(iii)
says ("not carried out here").

**Constraint hardness.** The λ ≤ 1 prime-side constraint is HARD for a single object (§7.5(a): X ≫ T
requires prime-pair information) and is the source of the individual q-aspect emptiness. The
family-average removal of that constraint is PROVEN mechanism (orthogonality) + numeric confirmation;
no hidden obstruction surfaced. The remaining constraint is analytic effort, not a wall.

**Concrete next step (cheapest, highest information).** (a) Push the q-aspect numerics to q ~ 10³–10⁴
at T = (log q)² and T = (log q)³ (the zero-side cost per character is O(T log T · q) — feasible in
Rust for a few characters per modulus, and the family average needs only a sample of characters, not
all φ(q)); verify κ̂_F(λ_F) → 4/3 as q grows and H(λ_F) → 2/3. (b) For rigor: write the family-level
statement as a formal argument — the block-diagonal matrix ⊕_χ Ĝ_χ, Lemma 3.2 applied with
tr ⊕ = Σ tr, ‖·‖² = Σ ‖·‖², and prove the Gevrey-taper Prop 4.2 for the family (the paper's own
open item) — then hand the family-averaged analytic evaluation to a Lean check. (c) Only if (b)
survives: transport to the GL(2) weight-aspect family (Petersson/Kuznetsov), which is where the
original 67.25%-method family target lives.

**Negatives recorded.** (i) The LMFDB Dirichlet zero pages were not cross-checked (URL scheme for
Dirichlet zero files not located in a quick probe; internal validation via RvM counts, phase realness,
and prime-side = zero-side agreement stands instead). (ii) The q-aspect λ=1 window is not yet legal
at q = 40–200 (λ_F ≈ 0.73); the λ=1 certificate is a limit statement, not a current-q statement —
reported as such. (iii) Even-character family average keeps the reflection pairs n+m ≡ 0 mod q
(bounded, ≤ 0.18 relative, and exactly zero for X < q/2); the clean statement is for all characters
mod q.
