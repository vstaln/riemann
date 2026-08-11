# Attack: H4.3 — the 256-law's triple correlation S₃ vs the PROVEN sine-kernel value

**Agent:** EXECUTIONER (investigation + constraint-hardness-testing + epistemology)
**Vector:** H4.3 from `research/notes/idea-generator-history.md` (§4 Pool 4, TOP-10 #1) — the Frey-curve move:
if the 256-law's triple correlation S₃ ≠ the PROVEN sine-kernel value, the law is EXCLUDED at the first
provable higher order, re-opening the certificate class with a third-moment validity constraint (V3/V4).
**Date:** Round 2
**Sources read:** `idea-generator-history.md` (H4.3, meta-verdict), `attack-twobandwidth.md` (corrected
sine-kernel moments m₃(1/2)=5, m₃(2/3)=13/4), `attack-nevanlinna.md` (m₃(law)=1.9545, integrality identity,
second-moment gap), `validation-enclok.md` (EnclOK = the only non-Lean link; certificate absent),
`attack-ceiling.md` (§1–4: what S(j) is, the ceiling, the FUND inputs), `attack-kh-triple.md` (the K–H
triple bound; admissible unmarked m₃ range [−1.56, 10.77] at λ=1/2 — "nothing useful excluded"),
`research/lean-zeta-23/Zeta23/PairCeiling/{Defs,NearCUE,LawN256,NumericCert}.lean` (read-only).
**Compute:** `tools/attack_law_s3.py` (new, self-contained) — `uv run --quiet --with mpmath --with numpy python tools/attack_law_s3.py`.
Output archived: `/tmp/attack_law_s3_final.txt`. Every number below is produced by that script (or cited with
its own script/command), per the code-backed-verification protocol.

---

## 0. Verdict up front (honest)

**NOT-EXCLUDED — BLOCKED-ON-DATA for the exact S₃, with one genuinely new, code-backed structural finding.**

1. **The law's exact S₃ cannot be computed in this session: BLOCKED-ON-DATA.** The marked configuration
   (weights w_c, positions x_{c,i}, marks m_{c,i}) exists only in the authors' private certificate
   `cert_N256_blk_b128m.json` (sha256 `cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8`).
   `research/notes/regenerate-256law.md` does **not** exist (checked — the regeneration agent's output never
   landed); `tools/regen_law/` and `tools/lpdual/law_data.json` contain only LP probe scripts and the
   *form-factor masses* s_j = S(j)/256 — not the configuration. No fabrication: the law's configuration is
   not in this repo, on the web, or in the Lean repo (validation-enclok §5's exhaustive search stands).
2. **What the pair rows + p₀ DO pin (PROVEN, new):** the diagonal (multiplicity) part of the law's S₃ is
   **D = 4 − 3p₀ = 1.9545139376** (position-free, exact from p₀), and the pair (two-equal) part is bounded
   **3u ≤ pair ≤ 6u** with u computed exactly from the recorded near-CUE rows + p₀: **u = 1.1624 (λ=1/2),
   0.6760 (λ=2/3)**. Hence for *every* near-CUE marked law with the law's rows:
   **S₃ ≥ D + 3u = 5.4419 (λ=1/2) > 5** and **S₃ ≥ 3.9825 (λ=2/3) > 13/4**, **plus the connected part T**.
   The pinned diagonal+pair parts **alone exceed the PROVEN sine-kernel values** (by +0.44 and +0.73).
3. **The sine-kernel value is therefore NOT provably outside the range** — the connected part T is a
   genuine third-order datum, **unconstrained by any proven input**, and configurations with T < 0 exist
   (exhibited). Matching S₃ = 5 forces **T ≤ −0.44** (λ=1/2), opposite in sign to the sine kernel's own
   connected part A3 = **+1/2**. This is a *structural tension* — the "the law saturates all higher moments"
   expectation is now suspicious at the pair level — but **not a proof of exclusion**.
4. **Epistemic status:** PROVEN — sine-kernel values 5, 13/4 (re-verified); D pinned; pair-part bounds
   [3u, 6u] (given EnclOK rows); T free (demonstrated). BLOCKED — the exact S₃(law). CONJECTURED — that T
   for a near-CUE marked law differs from the sine-kernel's +1/2 (this is exactly the missing third-order
   input; nothing proves it either way).
5. **Next step if BLOCKED (exact):** get `cert_N256_blk_b128m.json` from the authors (verify sha256), then
   run `marked_s3(w, xs, ms, λ)` — the function is written, validated, and waits for the data. OR complete
   the regeneration: re-solve the law's defining exact-rational LP (H6.2's "regenerate-256law machinery";
   `tools/regen_law/` has probes) and compute S₃ from the re-derived configuration.

---

## 1. Data-status statement (the blocker, precisely)

**What S₃(law) needs.** The law is a finitely supported probability distribution over 256-periodic marked
configurations (`LawN256.lean` header): weights w_c ≥ 0, Σ w_c = 1; positions x_{c,i} ∈ [0, 256) (rational,
off-grid); marks m_{c,i} ∈ {1, 2}, Σ_i m_{c,i} = 256. The marked third moment is

    S₃(law; λ) = Σ_c w_c · (1/256) Σ_{i,j,k} m_{c,i} m_{c,j} m_{c,k} K_λ(x_{c,i}−x_{c,j}) K_λ(x_{c,j}−x_{c,k}) K_λ(x_{c,k}−x_{c,i})

with K_λ the λ-window kernel. **Every term needs (w_c, x_{c,i}, m_{c,i}).** Only two data about the law are
in the repo:
- p₀ = 10909258999421303588095230195816054408197/16000000000000000000000000000000000000000 =
  0.6818286874638… (exact simple-point fraction, `LawN256.lean` header);
- the 256 enclosures lo_j ≤ 2^140·S(j) ≤ hi_j (`LawN256.encl`), which pin the *pair rows*:
  **E|μ̂(j)|² = 256·S(j) = j for j = 1..255** to within 2^-132 (verified, see §3).

**Checks performed this session (all negative):**
- `research/notes/regenerate-256law.md`: **does not exist** (`ls` — absent).
- `tools/lpdual/law_data.json`: contains K, s_mid/s_lo/s_hi = S(j)/256 enclosures — the *form factor*, not
  the configuration. `tools/regen_law/` (cert_allconfigs*, lp_pairs256, lp_doubles*, …): LP probe scripts
  only; no saved configuration. `scratch/`, `tmp/`: unrelated.
- The certificate file itself: absent (validation-enclok §5's exhaustive search — Lean repo full history,
  workspace, web — stands).

**Minimal data needed (exact blocker):** the 256-law's weight/position/mark arrays (or any file from which
S₃ is recomputable — e.g., the certificate JSON, or the LP's solution). Given those, the verdict is a
one-liner: `S3 = marked_s3(w, xs, ms, λ)`; **LAW-EXCLUDED iff S3 ≠ 5 (λ=1/2) or ≠ 13/4 (λ=2/3)** (per H4.3's
criterion; subject to the certificate design question in §6).

---

## 2. The S₃ formula (as code — ready for the data)

For a marked configuration with atoms (x_i, m_i) and window kernel K_λ (K(0) = 1), the diagram over the
marked atoms (i,j,k) is exact:

    tr((K·diag(m))³) = D + pair + T,   per mark (÷256):
      D    = (1/256) Σ m_i³                        (i=j=k — the multiplicity diagonal)
      pair = (1/256)[ Σ_{i≠k} m_i² m_k K_ik²  +  Σ_{i≠j} m_i m_j (m_i+m_j) K_ij² ]
           = (3/(2·256)) Σ_{i≠j} m_i m_j (m_i+m_j) K_ij²          (two-equal)
      T    = (1/256) Σ_{i,j,k distinct} m_i m_j m_k K_ij K_jk K_ki  (three-distinct, connected)

    S₃(law; λ) = Σ_c w_c (D_c + pair_c + T_c)/256 .

Implemented as `marked_s3(w, xs, ms, lam)` in `tools/attack_law_s3.py`; validated on a random
configuration: `D + pair + T == tr((KD)³)/256` to machine precision (D4; the diagram counting for the
marked case is the subtle part — the three two-equal cases sum to (3/2)Σ m_i m_j (m_i+m_j)K², **not** 3×;
an earlier factor-2 error was caught by the D2/D4 identities and corrected).

The periodic window kernel: finite-rank projection onto modes |j| ≤ M, M = ⌊128λ⌋, coefficient 1/B per
mode, B = 2M+1, so K(0) = 1. (The periodization of the continuum sinc is not well-defined as a function —
Poisson summation fails for the 1/u tail; the projection kernel is the canonical periodic analog. Rank
choice is a documented O(1/N) ambiguity, handled in §4 by a sensitivity sweep.)

---

## 3. What the pair rows + p₀ pin (PROVEN, code-backed)

**Setup.** The marked measure of each configuration has μ̂(j) = Σ_i m_i e^{2πi j x_i/256}. The recorded rows
give E|μ̂(j)|² = 256·S(j) = j for j = 1..255 (verified below), |μ̂(0)|² = 65536 deterministically (Σ m = 256),
and E Σ m_i² = 512 − 256 p₀ = 256(2 − p₀) from the marks (s + 2d = 256, s = simple count; the integrality
identity of attack-nevanlinna §3).

**Verification of the rows** (exact integer arithmetic, `tools/attack_law_s3.py` §A2):
| row data | value | source |
|---|---|---|
| enclosures parsed | 256 (width-1 boxes) | LawN256.lean → script |
| \|lo_j − j·2^132\| ≤ 1, j=1..255 | True (124 below / 131 at) | script (matches validation-enclok) |
| max \|256·S(j) − j\| over boxes | 256/2^140 = 2^-132 = 1.837e-40 < τ = 3e-40 | script (integer-exact; margin 1.63) |
| S(256) (closed band) | 211.432009142 (D(1)-consistent 0.82395) | script (matches validation-enclok) |

**The three pinned quantities** (`attack_law_s3.py` §C; mpmath 60-digit where relevant):

    D  = 4 − 3 p₀ = 1.9545139376          (position-free; the "multiplicity diagonal")
    E Σ m_i²    = 256(2 − p₀) = 337.4519
    u(λ) = (1/256) Σ_m d_m ( E|μ̂(m)|² − 256(2−p₀) )        [d = circular convolution of kernel coeffs]

    λ = 1/2:  u = 1.162449   ⟹   pair ∈ [3.4873, 6.9747]   ⟹   D + pair ∈ [5.4419, 8.9292]
    λ = 2/3:  u = 0.675981   ⟹   pair ∈ [2.0279, 4.0559]   ⟹   D + pair ∈ [3.9825, 6.0104]

The pair-part bound uses (m_i+m_j) ∈ [2,4] for marks ∈ {1,2}; the *lower* bound 3u uses only (m_i+m_j) ≥ 2,
so it holds for every near-CUE marked law. The identity U = EΣ_{i≠j} m_i m_j K_ij² = Σ_m d_m(E|μ̂(m)|² − EΣm²)
is exact per configuration and was verified to 4.6e-12 on random configurations (D2); the 3u ≤ pair ≤ 6u
bound was verified on 8 random configurations (D3).

**Consequence (the new finding):** with E|μ̂(m)|² = m (the Montgomery F ≡ 1 datum, which is what the
certificate reads and what is PROVEN for the real zeros on [0,1]),

    S₃(law; 1/2) ≥ D + 3u + T = 5.4419 + T,        S₃(law; 2/3) ≥ 3.9825 + T,

so **D + pair alone exceeds the sine-kernel values 5 and 13/4**. Matching the sine kernel forces
**T ≤ −0.44 (λ=1/2)**, i.e. a *negative* connected part — while the real zeros' connected part is
**A3 = +1/2 (λ=1/2)**, +1/12 (λ=2/3) (PROVEN, §5). The law cannot be sine-kernel at third order unless its
three-distinct correlation is opposite in sign to the zeros'.

---

## 4. Range analysis (task item c): is 5 / 13/4 inside or outside?

**The range of S₃ over near-CUE marked laws is not pinned, and the sine-kernel value is NOT provably
outside.** The decomposition gives S₃ = D + pair + T with D pinned, pair ∈ [3u, 6u] pinned, and **T
unconstrained by any proven input**:

- T is a third-order (three-distinct) datum; the near-CUE rows constrain only second-order data
  (E|μ̂|² = m). No proven statement bounds the 3-point correlation of near-CUE marked laws — a bound would
  be exactly the missing beyond-two-moment input (attack-ceiling §4's FUND list; §7.5(e)).
- T < 0 is realizable: the sanity configuration in D4 has T = −0.0118 < 0 (and T < 0 needs only some
  triples with negative K_ij K_jk K_ki, which the sinc's negative lobes provide).
- The pinned bottom exceeds the sine value at both windows, and this is **robust to the kernel-rank
  ambiguity**: for λ=1/2, D + 3u ∈ [5.26, 5.63] as M ranges over {62,…,66}; for λ=2/3, D + 3u ∈ [3.88, 4.09]
  as M ranges over {83,…,87} (sweep, in-session). The +0.44/+0.73 gaps are O(1), far above the O(1/N)
  kernel ambiguity.

**Conclusion for (c):** the sine-kernel value 5 (resp. 13/4) is compatible only with T ≤ −0.44 (resp.
≤ −0.73); T is not constrained by the pair rows; hence **5 and 13/4 are inside the achievable range —
not provably outside**. No exclusion follows from the pair rows + p₀ + marks alone. (This converges with
attack-kh-triple's unmarked analysis — admissible m₃ range [−1.56, 10.77] at λ=1/2, "nothing useful
excluded" — and sharpens it: the marked diagonal+pair bottom is now pinned *above* the sine value.)

**What WOULD complete the exclusion (either direction):** a proven bound on T for near-CUE marked laws —
e.g. T ≥ 0 would exclude the law outright (S₃ ≥ 5.44 > 5); T ≤ −0.44 would confirm the law violates the
sine kernel by excess. Neither is available: T ≥ 0 is refuted in general (D4), and no proven third-order
input exists. This is the honest frontier: the exact S₃(law) and any T-bound are the same missing datum.

---

## 5. The PROVEN sine-kernel reference values (task item a) — re-verified

Closed form (attack-twobandwidth §2, PROVEN): m₃(λ) = 1 + 3(1/λ − 2J2) + 1/λ² − (6/λ)J2 + 2(1 − λ/2),
J2(λ) = ∫₀^∞ sinc(πλu)² sinc(πu)² du. mpmath quadrature (60 digits), `attack_law_s3.py` §A:

| λ | J2 | m₃ closed | m₃ direct diagram (box, ±2%) | ref |
|---|---|---|---|---|
| 1/2 | 0.41666667 | **4.999999911** | 5.038 | **5** |
| 2/3 | 0.38888889 | **3.249999945** | 3.269 | **13/4** |
| 1 | 0.33333333 | **2.000000009** | 2.006 | **2** |

Diagram decomposition (PROVEN parts): A2 = 1/λ − 2J2 ∈ {7/6, 13/18, 1/3}; connected A3 = m₃ − 1 − 3A2 ∈
{**1/2, 1/12, 0**} at λ ∈ {1/2, 2/3, 1}. (A3(1) = 0 exactly — the λ=1 third moment is two-point data;
matches attack-kh-triple byproduct (ii).)

Empirical cross-check on real zeros (`zeros_computed_10000.txt`, band [9000, 9880], N = 1024, §A3):
**m₂(1/2) = 2.1341, m₃(1/2) = 4.8020** — matching the PROVEN 5 to the known ~3% finite-height deficit
pattern (same as attack-twobandwidth's 4.80; the real zeros ARE sine-kernel at third order empirically).

**Context of "m₃(law) = 1.9545 < 2" (task item 1):** attack-nevanlinna's m₃(law) = p₁ + 8(1−p₁)/2 = 1.9545
is the *multiplicity* third moment Σm³/256 = 4 − 3p₀ — **exactly the diagonal part D of the law's S₃**
(bandwidth-independent: it is the i=j=k term). It is a first-order (mark-distribution) object, not a
triple-correlation object (object discipline, attack-kh-triple §3). In H4.3's language: D = 1.9545 is the
pinned diagonal of S₃; the would-be separator "m₃ ≥ 2" (attack-nevanlinna §4) is exactly "D ≥ 2", which is
false for the law (1.9545 < 2) and unprovable as a general input (§7.5(e)). The new content here is that the
*pair part* (not D) already pushes the law's S₃ above the sine value.

---

## 6. Verdict and labels

**VERDICT: NOT-EXCLUDED (by pair rows + p₀); exact S₃(law) BLOCKED-ON-DATA.**

- **Law's exact S₃:** BLOCKED-ON-DATA. Blocker: the marked configuration (w_c, x_{c,i}, m_{c,i}) exists only
  in the authors' private `cert_N256_blk_b128m.json` (sha256 cc3de991…); `regenerate-256law.md` absent; no
  re-derived configuration in the repo. **Exact next step:** obtain the certificate (authors) and run
  `marked_s3(w, xs, ms, λ)` for λ ∈ {1/2, 2/3} (code ready); or complete the regeneration (re-solve the
  law's exact-rational LP — `tools/regen_law/` probes exist; H6.2's machinery) and compute S₃ from the
  re-derived configuration. **LAW-EXCLUDED iff S₃ ≠ 5 / 13/4** (with the caveat below).
- **New structural finding (PROVEN given EnclOK rows):** D + pair ≥ 5.4419 (λ=1/2) and ≥ 3.9825 (λ=2/3)
  for every near-CUE marked law with the law's rows and p₀ — both **strictly above** the proven sine-kernel
  values; the law can match the sine kernel only via a negative connected part T ≤ −0.44 (resp. ≤ −0.73),
  opposite in sign to the zeros' own A3 = +1/2. The "law saturates all higher moments" expectation is now
  structurally suspicious at the pair level — a genuine new datum for the V3/V4 third-moment certificate LP.
- **Caveat on the comparison target:** the certificate's third-moment validity functional is not yet fixed
  (it is the V3/V4 LP-design question). The marked S₃ vs 5 comparison assumes the constraint is "marked
  third moment = proven real-zero value"; if the functional drops the marks (unmarked position set), the
  object changes and this analysis's D-part does not apply. The formula in §2 covers both (marks = 1
  reduces to the unmarked case).

**Labels.** PROVEN (re-derived/verified this session): sine-kernel m₃(1/2) = 5, m₃(2/3) = 13/4, m₃(1) = 2
(mpmath closed form, 7–9 digits; diagram cross-check ±2%); A2, A3 values (A3(1/2) = 1/2 etc.); D = 4 − 3p₀
= 1.9545139376 (exact arithmetic on p₀); EΣm² = 256(2−p₀); pair bounds 3u ≤ pair ≤ 6u with u(1/2) =
1.162449, u(2/3) = 0.675981 (from the recorded rows); pinned bottoms 5.4419 / 3.9825; enclosure rows
(|256·S(j) − j| ≤ 2^-132, 124/131 split); D2/D3/D4 identities (machine precision). CHECKED NUMERICALLY:
kernel-rank robustness (bottoms ∈ [5.26, 5.63] / [3.88, 4.09]); empirical m₃(1/2) = 4.8020 on the 10⁴-zero
file; T = −0.0118 < 0 realized on a random configuration. BLOCKED-ON-DATA: S₃(law) exactly. CONJECTURED:
the law's T ≠ +1/2 (nothing proves it either way — this is the honest frontier, identical to the missing
beyond-two-moment input).

*Persistence note: a documented negative-with-tension, not a stop. H4.3's decisive computation (the law's
S₃) is a one-liner once the configuration is in hand; the pair-level tension found here is a new, funded
datum for the V3/V4 third-moment LP. The search continues.*
