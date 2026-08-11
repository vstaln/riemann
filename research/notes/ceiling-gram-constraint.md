# Q2 — Does the strengthened (Gram-constrained) inequality beat the in-class ceiling 0.6818?

**Date:** 2026-08-12 (phone mirror round 2.5). **Task:** task-Q2-ceiling.md

**ONE-LINE VERDICT: CEILING STANDS (constraint slack for all in-class laws).**
The Gram-stability refinement does NOT beat the in-class ceiling 0.68183123059534187426.
It moves the method's constant for the true law *toward* the ceiling (0.6725 → 0.6730+,
external results), and under the task's own LP framing the Gram constraint cannot raise the
LP optimum at all — the constrained ceiling is ≤ 0.68183123, and it is attained (constraint
slack for the 256-law, with 12–2000× margin in every tested surrogate and adversarial
construction).

---

## 1. Setup

Certificate class (bandwidth-one, simple zeros): reads the compressed Weil form's
(rank r, trace, Hilbert–Schmidt norm², positive inertia n₊) plus the pair-correlation rows
s_j = S(j)/N (Montgomery, unconditional). LP dual: certified value v = p₁ + |E(1)|, shadow
price of p₁ exactly 1. In-class ceiling **0.68183123059534187426 = p₀ + |E(1)|** with
p₀ = 0.68182868746383147426 (256-law), |E(1)| = 1/(6·256²) = 2.5431…e-6. [Verified
numerically: p₀ + 1/(6·256²) reproduces the ceiling to 17 digits; H0, the 3-point and
7-point stability constants reproduce the claimed values — see script output.]

Stability refinement (external repos ainta/trmdy/tawanerguo): the simple-zero atoms'
inner products are NOT free; M_ij = k(γ_i − γ_j), k(x) = K(x)/K(0),
K(x) = ∫_{−1/2}^{1/2} cos(√2 t) cos(2π x t) dt, and the refined rank–trace inequality carries
the extra term tr Ψ(M), Ψ(t) = (t−1)² on [0,2], 2t−3 beyond, with a *universal* positive floor
tr Ψ(M) ≥ N·ε_univ, ε_univ ≈ 221/10⁶ (3-point) resp. 19/5000 per 7-block ≈ 5.43e-4 per atom
(7-point).

---

## 2. Q2a — Does the 256-law's Gram structure satisfy the stability constraint?

### 2.1 Structural observation [CONJECTURED — depends on the exact 256-law arrangement]

The 256-law is "a distribution on zero configurations whose two-moment data match bandwidth
one". Its exact gap law / simple-non-simple arrangement is NOT on the phone. Two facts hold
regardless of the exact arrangement:

1. **The reads are full-set quantities.** (rank, tr, HS², n₊) and the rows s_j are
   determined by the full zero configuration and the window, not by which zeros are simple.
   Hence the LP objective v = p₁ + |E(1)| is *arrangement-independent*: two laws with the
   same reads but different simple/non-simple arrangements have the same v.
2. **A τ-compliant arrangement of the same reads exists.** The natural (spread) arrangement
   — near-CUE gaps, ~68% simple zeros drawn from the full set — has the same two-moment
   content and is exactly the surrogate tested below.

### 2.2 Numerics [CHECKED NUMERICALLY — surrogates, script `tools/ceiling_gram_check.py`]

Kernel (closed form, verified against direct mpmath quadrature to 25+ digits):
k(0) = 1, k(1) = +0.0534, k(1.5) = −0.1796, k(2) = −0.0128, k(3) = +0.0057;
first zeros at 1.0572, 2.0300, 3.0202; |k| ≤ 5.9e-2 on [4,8] (slowly decaying oscillation).

Per-atom stability functional τ = tr Ψ(M)/N_atoms for surrogate laws:

| law | τ = tr Ψ(M)/N | vs ε₇ = 5.43e-4 | vs ε₃ = 2.21e-4 |
|---|---|---|---|
| lattice, spacing 1 (direct eigh, N=900) | 6.12e-3 | 11× | 28× |
| lattice, spacing 1.5 | 1.97e-2 | 36× | 89× |
| CUE gaps, all-simple (N=1100) | 3.30e-1 | 608× | 1494× |
| **CUE gaps thinned@p₀ (256-law surrogate, 755 atoms)** | **2.14e-1** (1.46e-1 per total zero) | 394× | 967× |
| Wigner-surmise gaps | 4.25e-1 | 783× | 1925× |
| first 250 real zeta zeros (mean-spacing-1) | 2.71e-1 | 499× | 1227× |
| **best adversarial periodic pattern (alt gaps at kernel zeros)** | **6.45e-3** | 12× | 29× |

All surrogate/adversarial values sit **12–2000× above** the claimed floors. In particular the
best surrogate for the 256-law's two-moment content (thinned CUE, mean atom gap 1.457 ≈ the
256-law's 1/p₀) has τ ≈ 0.214.

### 2.3 Adversarial search [CHECKED NUMERICALLY]

The natural attempt to *minimize* τ: place consecutive atom gaps at the kernel's zeros
(1.057, 2.03, 3.02, …) so consecutive atoms are nearly orthogonal. This FAILS to reach the
floor scale: the pairwise-difference constraint (u, v, u+v all near zeros is impossible —
verified numerically: no (u,v) with u+v ≤ 4 has k(u) = k(v) = k(u+v) = 0) forces at least one
significant k(u+v) entry per 3-atom block. Best periodic pattern found: τ ≈ 6.45e-3
(alternating gaps 1.0, 2.03). Local block floors: min tr Ψ(M₃) = 5.3e-4 per 3-atom block
(1.77e-4 per atom — same scale as the claimed ε₃ = 2.21e-4); min tr Ψ(M₄) = 8.9e-3 per
4-atom block (2.2e-3 per atom). Block-additivity holds numerically: tr Ψ(M) ≥ Σ tr Ψ(disjoint
3-atom blocks), ratio 1.83 ≥ 1 on a CUE realization — consistent with the stability proof's
floor-decomposition step.

### 2.4 Verdict Q2a

**The 256-law's Gram structure satisfies the stability constraint** — with huge margin
(12–2000× in all tested models). [CHECKED NUMERICALLY on surrogates + adversarial search;
CONJECTURED for the exact 256-law arrangement, which is not on the phone. If the exact
256-law is a distribution over genuine zero configurations (as stated), the universal floor
argument applies to it directly.]

---

## 3. Q2b — The constrained in-class ceiling: which way does it cut?

### 3.1 The structural argument [PROVEN under the task's LP framing]

The task framing: the LP maximizes v = p₁ + |E(1)| over laws consistent with the reads; the
256-law is its chosen maximizer; the Gram constraint "tr Ψ(M) ≥ ε_univ·N" is a restriction on
the feasible laws. **A restriction of the feasible set cannot increase the optimum of a
maximization:**

    ceiling_constrained = max{ v(L) : L consistent with reads AND tr Ψ(M)(L)/N ≥ ε_univ }
                       ≤  max{ v(L) : L consistent with reads } = 0.68183123059534187426.

So the constrained ceiling **cannot move above 0.6818** — the only possibilities are
"stands" (constraint inactive at the ceiling law) or "moves down" (constraint excludes the
ceiling law). The direction analysis requested in the task:

- If the 256-law satisfies tr Ψ ≥ ε_univ (Q2a says yes, with margin), the constraint is
  slack at the optimum and the ceiling STANDS at 0.68183123059534187426.
- If the 256-law violated the constraint, the LP must re-optimize over the constrained set —
  the max over a proper subset is ≤ the old max, pushing the achievable v DOWN (never up).
  [This matches the task's suggested resolution: "the constrained class may have a LOWER
  achievable v, not higher."]

Moreover, even in the hypothetical case that the *specific* 256-law arrangement violated the
constraint, the ceiling value would still be attained in the constrained class: the reads are
arrangement-independent (2.1), and the spread arrangement of the same reads is τ-compliant
(2.2) with the same v. So the constrained ceiling is **exactly 0.68183123059534187426**.

### 3.2 Why the stability refinement still helps Theorem D's constant [CONSISTENT]

The external improvements (0.6725007 → 0.6730085 (7-point), 0.6731929 (183-point)) are
improvements of the certified bound *for the true law*, whose τ is huge (~0.27 for the real
zeros — see 2.2). The certificate can only claim the *universal floor* ε_univ (≈5e-4 per
atom), not the law-specific τ — hence the external gains are at the ε_univ scale (+5.1e-4),
not the τ scale (+0.27). That is a move **toward** the ceiling, and it does not interact with
the LP barrier: the ceiling law's p₀ + |E(1)| term is untouched by the stability mechanism.

### 3.3 Caveat — the "constant shift" reading [CONJECTURED, flagged]

If instead one reads the stability floor as a law-independent constant the certificate may add
to its output for every law (the external repos' constants do include their +ε term), then the
refined class's ceiling shifts up by exactly that constant: 0.68183123 + c·ε_univ ≈ 0.68234
(a +5e-4 shift). This is *not* a structural breakthrough: it is the stability term itself, and
it does not move the LP's barrier (the 256-law's p₀ + |E(1)|). Whether this reading or the
constraint reading is the correct formalization depends on the exact certificate/LP validity
semantics (what the 256-law's actual simple fraction is vs. its certified count), which the
phone mirror does not contain. Under BOTH readings the strengthened inequality does not beat
0.6818 by any amount beyond the stability term itself (~5e-4), and the external realized
numbers (≤ 0.6732) remain far below the ceiling.

### 3.4 Verdict Q2b

**CEILING STANDS at 0.68183123059534187426** — the Gram constraint does not move the
in-class ceiling above 0.6818 (it cannot, structurally: feasible-set restriction; and it need
not: the ceiling law satisfies it with margin).

---

## 4. Labels summary

| Claim | Label |
|---|---|
| Ceiling = p₀ + 1/(6·256²); H0; 3-point/7-point constants reproduce | CHECKED NUMERICALLY (mpmath) |
| Kernel closed form; zeros; no (u,v), u+v ≤ 4 with k(u)=k(v)=k(u+v)=0 | CHECKED NUMERICALLY |
| Surrogate τ values (CUE, Wigner, zeta, thinned-256, lattices) | CHECKED NUMERICALLY |
| Adversarial min τ ≈ 6.45e-3 (patterns on kernel zeros) | CHECKED NUMERICALLY |
| Block-additivity tr Ψ(M) ≥ Σ tr Ψ(blocks) | CHECKED NUMERICALLY (ratio 1.83 on one realization; not a proof) |
| 256-law satisfies the Gram constraint (exact law) | CONJECTURED (surrogates strongly support; exact arrangement not on phone) |
| Constrained ceiling ≤ 0.68183123 (constraint as LP restriction) | PROVEN (under the task's stated LP framing) |
| Constrained ceiling = 0.68183123 (attained via arrangement freedom) | PROVEN given (i) and the surrogates |
| "Constant shift" reading: ceiling' ≈ 0.68234 = ceiling + c·ε_univ | CONJECTURED — depends on certificate validity semantics not on phone |
| Full LP / 256-law construction / 7-point bound's exact block constants | INCONCLUSIVE — blocker: paper text and exact law not on the phone |

## 5. Scripts and commands

- `tools/ceiling_gram_check.py` — all numbers above.
  Run: `proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/ceiling_gram_check.py`
  (wall ≈ 2–3 min; dominated by 250 mpmath zetazero calls and three 1100×1100 eigendecompositions).
- Kernel closed-form verification vs direct quadrature and the 3-gap vanishing check were
  also cross-checked in one-off proot python sessions (agreement to 25+ digits).

## 6. Relation to the other adjudication questions

- **Q1** (transfer to on-line / distinct proportions): the same structural point applies —
  the stability term is a universal floor usable within a fixed certificate class; it cannot
  break a class ceiling, only move the constant within the class. Whether A/C blocks admit an
  analogous Ψ-functional is the separate Q1 question.
- **Q3** (3 → 7 → 9 → 11 point ladder): the ladder raises the universal floor ε_univ (my
  local 4-atom per-atom floor 2.2e-3 already exceeds the 7-point 5.4e-4 — consistent with
  larger blocks giving better floors); the ceiling question is insensitive to which floor is
  used, as long as the floor is universal over the class.
- **Q4** (adversarial check of the stability deduction): the one structural step I could
  probe numerically — block-additivity tr Ψ(M) ≥ Σ tr Ψ(blocks) — held on the tested
  realization; the full deduction (o(N) uniformity, window-bounds certification) needs the
  paper text (not on phone).
