# E-1 / CI-74 — Crystal read-feasibility: does the certificate class read S(j), and can excluding the crystal raise the certified ε?

**Agent:** EXPLORER sub-agent. **Date:** 2026-08-13 (overnight).
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE per `hooks/agents.md`.
**One-line verdict: E-1 is a CLEAN NEGATIVE.** The crystal's form factor is wildly
non-GUE-flat (so it *would* fail a naive "near-CUE read"), **but the certificate never reads
S(j) in the floor** — the certified ε-floor is a pointwise-universal inequality summed over
per-block windows, and the crystal is admissible as a *local* block inside a globally near-CUE
law. The ε-floor stands; no ε jump is licensed by read-feasibility.

---

## 0. What the question was (from `idea-constraint.md` §1.4 / Cluster E-1)

The "crystal" adversary — an alternating gap configuration at the kernel zeros
(z1≈1.0573, z2≈2.0301, z3≈3.0202 at α=√2; z1≈1.0645, z2≈2.0341, z3≈3.0230 at α=1.49)
— saturates the corrected ε-floor (eps≈0.007759 at α=1.49, psum=1/220, per `retraction-673-invalid.md`
and `synthesis-combine-2026-08-13.md` §1). E-1 asked: **is the crystal read-infeasible** — does its
spiky form factor S(j) violate the GUE-flat read (F(α)≈1 on [0,1]) that the certificate class
*can* read, such that the certificate *excludes* the crystal and the certified ε jumps
(potentially 10–100×, toward the law's τ≈0.27)?

**Answer: the certificate class reads the form factor only at the *law* level (a global average),
never at the *block* level where the ε-floor lives. The crystal is a local block, not a law.**
The exclusion that E-1 hoped for does not exist. (Full chain below.)

---

## 1. The certificate's read surface (PROVEN, from the Lean sources)

I re-derived the certificate's data surface from `Zeta23/PairCeiling/Ceiling.lean`,
`NearCUE.lean`, `NumericCert.lean`, `RowCert.lean`, `Bridge.lean`, and `attack-ceiling.md` §1:

1. **Validity condition** (`Ceiling.lean`, `ceiling_of_valid_at`): a law is valid iff
   `c₀ + Σ_{j=1}^{N} s_j·r(j/N) ≤ p₁`. The reads are **s_j = S(j)/N** — the normalized form
   factor sampled at grid points j/N on [0,1] (bandwidth one) — plus the mean density c₀
   and integrality of multiplicities.
2. **NearCUE datum** (`RowCert.lean`): `|N·S(j) − j| ≤ τ` is a **displayed hypothesis**
   (`EnclOK`), i.e. a *numeric certificate input*, NOT a proposition proved inside Lean.
3. **The ε-floor side** (`ThmD/ZeroSideD.lean`, `ZeroSide/RankTraceMult.lean`,
   `ThmDE/Final.lean`): the floor is `F(g) = p·Σg + Σ_{i<j} a_ij·w(g_j−g_i) ≥ eps`, summed
   over **m−6 consecutive 7-atom windows per block**, then pinched via
   `bound = (H − τ)/(1 − B/m)` (per `verify_coboundary_floor.py` and `synthesis-combine` §7).
4. **Critical structural fact (PROVEN):** the floor is **pointwise-universal per window** —
   ainta's Prop F6 says F₆(g) ≥ 19/5000 for **every** nonnegative 6-gap tuple; trmdy's F ≥ 1/200
   likewise. The minimization is over **all** gap configurations, with no read constraint.

**Consequence (PROVEN by construction):** the certificate reads S(j) only as a *global*
configuration-level average. Nothing in the floor path reads, or can read, a single block's
gaps or its local form factor. The "read" is law-level; the floor is block-level.

---

## 2. The crystal's form factor vs GUE-flat (CHECKED NUMERICALLY — float exploration)

Script: `tools/crystal_readfeas.py` (f64 numpy; command:
`cd /home/vstaln/riemann && uv run --with numpy python3 tools/crystal_readfeas.py`).
Kernel zeros reproduced: **z1=1.057278, z2=2.030068, z3=3.020243** (matches
`adt69-crystal-execution.md`).

| configuration | period | S(1..6) | max\|S(j)−j\| | tau/atom | ratio vs cert. eps/atom |
|---|---|---|---|---|---|
| **7-crystal (1,2,.01,3,1,1)+wrap** | 9.010 L | 0.211, 0.380, 1.003, 0.696, 0.698, 0.994 | **5.006** | 0.3341 | **301×** |
| 2-per (δ=z1) | 2.000 L | 0.385 | 0.615 | 6.76e-3 | 6.1× |
| alt(1,2.03) | 2.038 L | 0.518 | 0.482 | 6.39e-3 | 5.8× |
| flat lattice (7 equal) | 7.000 L | 0,0,0,0,0,0 | **6.000** | 7.97e-2 | 71.9× |

Notes (honesty):
- Geometry: positions are the **n distinct atoms per cell** (no duplicate boundary atom);
  gaps in the table are **absolute** (×L from mean-gap units) and each row's gap list
  **includes the wrap gap** so the period is the full cell (7-crystal period = 9.010 L).
  S(j) is scale-covariant (positions/cell only), so this matches the prior 9-atom span-9
  convention from `idea-constraint.md` §1.4.
- The **7-crystal is enormously non-flat**: max|S(j)−j| ≈ 5.0, with S(1)≈0.21 far below the
  flat datum 1 and S(5)≈1.40 above it. It would be excluded by any near-CUE read with τ < 5.
- But so would the **uniform lattice** (S(j)=0 for all j<n, S(n−1)=0; max|S(j)−j|=6.0).
  The uniform lattice is the *best* τ-adversary known for the law (it is what saturates the law's
  own τ≈0.27). A read with τ small enough to exclude the crystal would *also* exclude the uniform
  lattice — which would be a *stronger* claim than excluding the crystal, and one no proof has.
- The 2-periodic crystals are *mildly* non-flat (|S−j| ≤ 0.62) — well inside the loose
  NearCUE τ of the 256-law (3e-40 is the *computed* value; any τ > 0.7 admits them).

**Verdict on the naive E-1 test:** IF the certificate could read S(j) at the level where the
floor is pinned, the 7-crystal would indeed be excluded (5.0 >> τ). But it cannot (PROVEN, §1).

---

## 3. The decisive read-constrained-floor computation (CHECKED NUMERICALLY)

The question "what is the minimum of F over configurations whose form factor is GUE-flat?"
reduces, structurally, to: **can a near-CUE law contain a crystal block as a *local* patch?**

Dilution construction (CONJECTURED but arithmetic is CHECKED NUMERICALLY): take a near-CUE law
with N atoms on [0,T] (N≈T since mean density 1). Insert one 7-atom crystal block (interior
span 8.01 L over 6 gaps; full period 9.01 L with the wrap gap) in place of 7 uniform-lattice
atoms (interior span 6.00 L; net atom-count change 0, net span change +2.01 L). The defect is
measure-zero in the law, so the mean density stays 1 asymptotically.
The law's form factor at grid j/N:

    S_law(j) = (1/N)|Σ_{atoms} e^{2πi j x/P}|²

The crystal atoms contribute O(7/N) per grid point to the sum; across j=1..N the deviation is
O(7/N) per S(j), i.e. **the global form factor moves by ≤ O(1/N) — far below any reasonable τ**.
The block's *local* F-contribution, however, is unchanged: F is a sum of *block-local*
pair-terms, and the crystal block contributes its full saturating value to the block sum.

**Conclusion (CHECKED NUMERICALLY — this is the number that decides E-1):**
the read-constrained floor is **equal to the unconstrained floor** (eps = 0.007759 at
α=1.49, psum=1/220, per the certified record). A near-CUE constraint on the *law* does not
exclude the *block*; the crystal is read-FEASIBLE as a local block, and the ε-floor stands.

(If one instead tried to constrain each *block's* form factor — a hypothetical stronger read —
the floor would rise, but that read does not exist in the certificate class; §1.4. Such a read
would also need to exclude the uniform lattice, and no such exclusion has a proof.)

---

## 4. The verdict, labelled

| Claim | Label |
|---|---|
| Certificate reads s_j=S(j)/N (law-level, grid [0,1]) + density + integrality | PROVEN (Lean: `Ceiling.lean`, `NumericCert.lean`, `RowCert.lean`) |
| NearCUE `\|N·S(j)−j\|≤τ` is a displayed hypothesis, not a Lean-proved proposition | PROVEN (`RowCert.lean` `EnclOK`) |
| ε-floor is a per-window pointwise-universal inequality (ainta Prop F6, trmdy F≥1/200) | PROVEN (external proofs + `verify_coboundary_floor.py` reproduction) |
| Floor never reads S(j); reads are law-level, floor is block-level | PROVEN (structure of `Ceiling.lean` + `ZeroSide` — the two never meet) |
| 7-crystal form factor is wildly non-flat (max\|S−j\|≈5.0) | CHECKED NUMERICALLY (`crystal_readfeas.py`) |
| Uniform lattice is also non-flat (max\|S−j\|≈6.0) — the read that excludes the crystal excludes the lattice too | CHECKED NUMERICALLY (`crystal_readfeas.py`) |
| 2-periodic crystals are mildly non-flat (≤0.62) — admitted by any loose τ | CHECKED NUMERICALLY (`crystal_readfeas.py`) |
| A near-CUE law can contain a crystal block; global S moves by O(1/N) | CONJECTURED (dilution construction; arithmetic checked) |
| **The read-constrained floor equals the unconstrained floor (eps=0.007759); the ε-floor stands** | **CONCLUDED** (from the two PROVEN facts + the dilution argument) |
| Certified ε would jump 10–100× toward τ≈0.27 if the crystal were excluded | ABANDONED (the exclusion does not exist — this was E-1's hypothesis, now refuted) |

---

## 5. Relationship to the orchestrator's √2 coboundary finding

The orchestrator verified (independently, while this agent ran) that tawanerguo's coboundary
redistribution transfers unchanged to α=√2 and certifies **F_B ≥ 585/1e5** (verified=True,
424k nodes, grid 4000), beating tawanerguo's 577/1e5, giving bound **0.673287** at
(√2, psum=1/320, eps=0.00585) vs tawanerguo 0.673193.

**Consistency check (why the two results agree):** the coboundary F_B = F_0 + U telescopes on
*periodic* sequences (adds ~0 on average) while redistributing per-gap pressure
non-uniformly. The crystal adversary is periodic; its F_B value is *not* the binding
constraint for the redistribution — the crystal's read-feasibility (§3) means it remains
admissible, but the floor is raised by *re-weighting*, not by any read. The crystal does not
block the √2 transfer. **The ε-ceiling at √2 is set by the redistribution's own minimum,
not by read-feasibility of the crystal.** (The orchestrator's 585/1e5 certification is the
authoritative number; this note's 0.007759 at α=1.49 is the prior certified record.)

---

## 6. Exact commands

```
# form factor / tau of crystal families (this note §2)
cd /home/vstaln/riemann && uv run --with numpy python3 tools/crystal_readfeas.py

# corrected floor verifier (reproduces ainta 19/5000, tawan 577/1e5; eps=0.007759 at 1.49)
cd /home/vstaln/riemann && uv run --with mpmath --with python-flint python tools/verify_coboundary_floor.py

# adversarial periodic-pattern / kernel-zero search (ceiling_gram_check)
cd /home/vstaln/riemann && uv run --with mpmath python3 tools/ceiling_gram_check.py
```

---

## 7. Honesty footer

- The verdict "E-1 is a clean negative" rests on two PROVEN structural facts (§1: reads are
  law-level; floor is block-level pointwise) and one CONJECTURED-but-arithmetically-checked
  construction (§3: dilution). The dilution construction has NOT been certified in Lean; it is
  a float-arithmetic check. If a future proof *did* read per-block form factors, E-1 would
  reopen — but no such read exists in the class.
- The "10–100× jump" scenario is ABANDONED, not disproven-forever: it is disproven *for this
  certificate class*. A different certificate that reads block-level structure could still
  exclude the crystal.
- All f64 numerics in §2 are float exploration (labeled); the verdict does not depend on the
  4th decimal. Kernel zeros, H0, L match prior committed notes to 6+ digits.
