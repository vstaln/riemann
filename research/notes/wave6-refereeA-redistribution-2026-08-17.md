# Wave 6 — Referee 6A (hostile, blind): the redistribution algebra behind the 0.673481 record

**Date:** 2026-08-17. **Joint:** 6A — re-derive `bound = (H(α) − τ)/(1 − B/m)` from the
rank–trace lemma + coboundary mechanism; attack the division; cross-check the verifier.
**Blind:** read only my brief, FINAL-RECORD-2026-08-13, tools/verify_coboundary_floor.py,
coboundary-redistribution-explore.md, structural-leverage-synthesis.md,
attack-realconstants.md, and the tawanerguo external bound script
(research/external-results/tawanerguo-zeta-simple-zeros/tools/evaluate_coboundary_bound.py).
Labels per hooks/agents.md.

---

## 0. VERDICT

**INCONCLUSIVE — the certificate's *checkable* layers are all VALID; the division's *direction*
is an unproven step that I could neither confirm nor refute, and it is exactly the
single-point-of-failure the brief flagged.**

- Everything that can be checked **numerically or by code inspection is correct**: the
  arithmetic reproduces the record exactly; the verifier is sound and complete for its
  statement; the redistribution coefficients are all positive, decode exactly from the
  telescoping coboundary, and the verifier's pruning is conservative for them; `B < m`
  always (the denominator `1 − B/m = 0.994018` is a fixed positive constant — no
  per-configuration sign flip of the E[T]≥0 kind); m=171 is the true argmax of the formula;
  the formula reproduces ALL FOUR independently-certified records (two coboundary, one
  uniform, tawan's) to the precision of the printed H.
- **The one unproven step:** the derivation of `p·(1 − B/m) ≥ H − τ` — i.e., why the
  certified floor `eps` enters the *denominator* with a *minus* sign at the SAME weight
  `(m−6)/m` as the tax `τ` enters the numerator. I found **no note stating this theorem**,
  and the record's own ledger agrees ("NOT YET: Lean formalization"). The direction is
  assumed in the bound script, not derived. A sign error there (true form
  `p ≥ (H−τ)/(1+B/m)`) would drop the value to **0.665467 — below the ceiling**; a direct
  subtraction gives 0.663470. The value that beats the 0.6725007 ceiling exists **only**
  through this one division by 0.994018.
- **What would close it:** a written lemma "certified floor eps of F_B ⇒
  p·(1 − Phi(eps(m−6),m)/m) ≥ H − psum(m−6)/m" with a proof, or an independent
  re-derivation of the self-consistent term `p·B/m` from the E2-pairs rank–trace lemma.
  Until then the correct label for 0.673481 is **CHECKED NUMERICALLY (consistent
  formula), derivation unproven** — matching the record's own honesty ledger.

---

## 1. The chain, fully explicit (first principles to final value)

### 1.1 Objects (all now identified)

- **H(α)** = 2 − 1/c*(α): the plain rank–trace constant for window α. From the REAL-data
  Lemma 3.2 (PROVEN, attack-realconstants.md §1.1): `s₁ ≥ 4N − 2N − ‖Ĝ‖²_F`, with
  `‖Ĝ‖²_F/N ≤ 1/c*`; hence `p₁ ≥ 2 − 1/c*₁ = 0.6725007` at α=√2 and
  `H(1.464) = 0.672467425578` (consistent with H(1.47)=0.67245871, H(1.49)=0.67242189;
  monotone decreasing on [√2, 1.49] — CHECKED NUMERICALLY). **This is a direct-subtraction
  bound, the window-class ceiling of which is Theorem D (PROVEN, Lean).**
- **The 6-gap functional:** `F_0(g) = Σ p0·g_i + Σ q0·w(g_i) + Σ_{i<j} a_ij·w(y_j−y_i)`,
  uniform p0 = 1/1920, q0 = 1/3, a_ij = 2/(7−(j−i)), w = (k/k0)², k = cosine window α.
- **Coboundary** (decoded, PROVEN in coboundary-redistribution-explore.md §2; I re-derived
  the coefficient sums exactly):
  `U(g1..g5) = (54g1−123g2+123g4−54g5)/1920000 + (5971/300000)(w(g1)+w(g2)−w(g4)−w(g5))`,
  `F_B = F_0 + U(g2..g6) − U(g1..g5)` — **telescoping**: exactly 0 on 6-periodic
  sequences (crystals); shifts mass between gaps only.
- **Redistributed coefficients:** `p_i = p0 + (l_{i−1} − l_i)`, `q_i = q0 + (c_{i−1} − c_i)`
  with l = (54,−123,0,123,−54)/1920000, c = (5971,5971,0,−5971,−5971)/300000,
  giving `p = (946,1177,877,877,1177,946)/1920000` (Σp = 1/320 **exact**), `q =
  (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5)` (Σq = 2.0 **exact**).
  All 12 coefficients > 0. PROVEN (exact rational arithmetic).
- **eps = 0.0062** — the certified floor: verifier PROVES `F_B(g) ≥ eps` for ALL `g_i ≥ 0`
  (620/1e5 passes at 1,096,556 nodes; 630/1e5 fails terminal-cell; 3 identical runs).
- **m = 171**, **psum = Σp_i = 1/320**.
- **τ = psum·(m−6)/m = 11/3648 = 0.003015350877…** ("pressure tax").
- **A = eps·(m−6) = 0.0062·165 = 1.0230**, and the **Bellman cap**
  `B = Phi(A, m) = 2·√((m−1)·A/m) − 1 + A/m = 1.0229282103…` (exact formula read from
  the tawan external script; concave in A since d²B/dA² = −(1/2)√((m−1)/m)·A^(−3/2) < 0).

### 1.2 The chain

```
Lemma 3.2 (rank–trace, PROVEN):        s₁ ≥ 4N − 2N − ‖Ĝ‖²_F        [subtraction form]
plain bound:                            p₁ ≥ 2 − ‖Ĝ‖²_F/N ≥ 2 − 1/c* = H(α)
redistribution (the audited claim):     p₁ ≥ (H(α) − τ)/(1 − B/m)    [division form]
  numerator:  H − τ = 0.672467425578 − 0.003015350877 = 0.669452074701
  denominator: 1 − B/m = 1 − 0.005982036318 = 0.994017963682
  ⇒ p₁ ≥ 0.669452074701/0.994017963682 = 0.6734808616745…           [CHECKED, exact]
```

The **only unproven link** is the last bullet: the lemma statement that the redistributed
floor converts the subtraction bound into the division bound. All links before it are
PROVEN or CHECKED NUMERICALLY (below).

---

## 2. Attack on the move (E[T]≥0 analogues)

### 2.1 Is the denominator direction right? (the crux — INCONCLUSIVE)

Three candidate "true" forms, same data:

| candidate | value | beats 0.6725007? |
|---|---|---|
| `(H−τ)/(1−B/m)` (record) | 0.6734809 | YES (+9.8e-4) |
| `(H−τ)/(1+B/m)` (sign flip) | 0.6654670 | NO |
| `H−τ−B/m` (direct subtraction) | 0.6634700 | NO |

What I can rule out: a *per-configuration* sign flip. `B` is a **fixed number**
(1.022928), not a configuration-dependent quantity, and `B < m` holds for every eps up to
0.1 (CHECKED NUMERICALLY), so `1 − B/m > 0` unconditionally at any plausible operating
point. The residual risk is a *systematic* direction error in the lemma application —
invisible to the verifier (which certifies only `F_B ≥ eps`, not the rank–trace step) and
invisible to cross-record consistency (all four records use the same formula). I found
**no note deriving `p(1−B/m) ≥ H−τ`**, and the record's own ledger marks the
α/redistribution chain as not-yet-formalized. This is a genuine INCONCLUSIVE, not a found
bug.

Supporting (but not conclusive) evidence for the direction:
- The formula reproduces the **corrected uniform record** 0.6730690301666756 (the
  post-retraction value, itself certified with the fixed single-normalization verifier) to
  4e-9 — the formula is *the* mechanism, not a per-scheme fit (CHECKED NUMERICALLY).
- Monotonicities are all sensible: ∂bound/∂eps > 0 (0.648 per 1e-4), ∂bound/∂τ < 0,
  ∂bound/∂H > 0; m=171 is the true argmax over m∈[120,260] (CHECKED NUMERICALLY).
- The formula never exceeds the 256-law class ceiling 0.6818 at any *feasible* point: it
  crosses 0.6818 only at eps ≈ 0.0252, while the certifiable eps is capped by the crystal
  floor at ≈ 0.0063 (CHECKED NUMERICALLY). No claimed value violates the brief's 0.6818
  guard.

Warning sign (minor, out-of-range): at eps → 0, `B → −1` and the formula gives
`(H−τ)/(1+1/m) = 0.66556 < H` — i.e. the formula does **not** degrade to the plain bound
H at zero floor. This is consistent with "the redistribution needs its certified floor to
pay for the looser psum", but it means the formula is an operating-point mechanism, not a
clean interpolation of the plain bound; its behavior is only meaningful where
eps ≥ ~0.0057 (the certified regime). Not a falsification at the record point.

### 2.2 Does the redistribution p,q require a false assumption? (NO — checked)

- All p_i, q_i > 0, all a_ij > 0, w ≥ 0 ⇒ every term of F_B nonnegative; the
  "one-body ≥ target ⇒ F_B ≥ target" pruning logic is valid. PROVEN.
- p,q decode **exactly** from the telescoping coboundary (Σp = 1/320, Σq = 2.0 exact
  rational identities; coboundary-redistribution-explore.md §2 PROVEN to 10+ digits).
- The verifier's pressure cutoff (Σg ≥ 18.6 ⇒ prune) is **conservative** for the
  redistributed scheme: `min_i p_i = 0.00045677 > uniform p = 1/3000`, so any pruned
  configuration satisfies `F_B ≥ 0.00045677·18.6 = 0.008496 > 0.0062` by the linear term
  alone. CHECKED NUMERICALLY. No configuration where the floor fails is hidden by the
  domain reduction.

### 2.3 eps mis-certification? (NO — verifier soundness, §4)

---

## 3. Cross-check: verifier vs algebra — NO divergence found

**Algebra claims:** `F_B = F_0 + U(g2..g6) − U(g1..g5) ≥ eps` for all g ≥ 0.
**Code computes (`box_lower`, cap_scheme='coboundary'):**
`Σ p_i·g_i + Σ q_i·w(g_i) + Σ_{i<j} a_ij·w(y_j−y_i)` with the SAME p,q (as
`pressure_coeffs`, `nearest_coeffs`) and uniform a_ij — exactly the decoded F_B.
PROVEN (read code; sums checked). **No divergence.**

Soundness/completeness of the certification loop (all PROVEN by code inspection):
- `w_lower_on_cell`/`w_second_lower_on_cell`: rigorous Arb (prec 128) interval lower bounds,
  `nextafter`'d down.
- One-body prune: excluded only when the one-body **lower bound** ≥ target; then
  F_B ≥ one_body ≥ target by nonnegativity. Valid.
- Pressure prune: conservative for the redistributed scheme (§2.2).
- Tangent prune: gated on exact-LDL PSD certification of the Hessian (built from w''
  lower bounds); if not certified PD, no prune; for a convex f, `f(x) ≥ f(mid) +
  ∇f(mid)·(x−mid) ≥ f(mid) − Σ|∇f_i|·radius_i` is valid. Valid.
- Terminal cell ⇒ `verified=False`; `max_nodes` exceeded ⇒ `verified=False`. No silent
  acceptance.
- **Domain completeness:** all `g ≥ 0` covered — Σg ≥ 18.6 handled by the pressure
  argument, Σg < 18.6 explored by B&B over surviving component boxes (cells excluded only
  when one-body ≥ target). The certified statement is genuinely `F_B ≥ eps` on the whole
  domain.

**Bound formula vs code:** the bound script `evaluate_coboundary_bound.py` computes
`h = 2 − 1/c` (interval MPFR, 256 bits), `a = eps(m−6)`,
`b = 2·√((m−1)a/m) − 1 + a/m`, `pressure = psum(m−6)/m`, `bound = (h − pressure)/(1 − b/m)`.
My re-implementation reproduces it exactly; the script's own certified_decimal_14 for
tawan is 0.6731929114731... (matches). PROVEN.

---

## 4. The empirical cross-scheme law (all four records, my computation)

| record | H | psum | eps | m | formula bound | claimed bound | resid. |
|---|---|---|---|---|---|---|---|
| tawan 1.47 | 0.67245871 | 1/320 | 0.00577 | 183 | 0.6731929121 | 0.6731929115 | 6e-10 |
| ours 1.49 | 0.67242189 | 1/320 | 0.0062 | 171 | 0.6734350521 | 0.6734350481 | 4e-9 |
| **RECORD 1.464** | 0.672467425578 | 1/320 | 0.0062 | 171 | 0.6734808617 | 0.6734808617 | 2e-13 |
| uniform 1.49 | 0.67242189 | 1/220 | 0.007759 | 137 | 0.6730690341 | 0.6730690302 | 4e-9 |

Residuals are the printed-H precision (12–8 digits); the formula is exact. The SAME
`B = 2√((m−1)A/m) − 1 + A/m` fits uniform AND coboundary schemes — strong evidence it is
the actual mechanism. Empirically `B ≈ A = eps(m−6)` at all operating points. CHECKED
NUMERICALLY (mpmath 40 dps, commands below).

---

## 5. Minimal reproducer

```bash
cd /home/vstaln/riemann
uv run --quiet --with mpmath python3 -c "
from mpmath import mp; mp.dps=40
def bound(H,psum,eps,m):
    A=eps*(m-6); B=2*mp.sqrt((m-1)*A/m)-1+A/m; tau=psum*(m-6)/m
    return (H-tau)/(1-B/m), B, tau
b,B,tau=bound(mp.mpf('0.672467425578'),mp.mpf(1)/320,mp.mpf('0.0062'),171)
print(b)   # 0.6734808616747268... (record: 0.6734808616745137, diff=printed-H precision)
# direction stakes
H=mp.mpf('0.672467425578'); T=tau
print('sign-flip  :',(H-T)/(1+B/m))   # 0.66547 (below ceiling)
print('no-division:',H-T)             # 0.66945 (below ceiling)
"
```

---

## 6. What would change my verdict

- **→ VALID:** a written lemma stating the redistribution bound
  `p·(1 − Phi(eps(m−6),m)/m) ≥ H − psum(m−6)/m` with a derivation from Lemma 3.2 / the
  E2-pairs rank–trace mechanism (the self-consistent `p·B/m` term is the key object), or a
  Lean formalization of the α=1.464 redistribution chain (the record's own "NOT YET" item).
- **→ BROKEN:** any demonstration that the correct relation is `p ≥ (H−τ)/(1+B/m)` or a
  direct subtraction (values 0.665/0.663, below the ceiling), or a configuration/domain
  where the verifier's certification is invalid (I found none), or an eps used in the bound
  that exceeds the certified floor (not the case: eps = 0.0062 = the certified 620/1e5).
- **INCONCLUSIVE (current):** the direction of the division is the blocker — stated
  precisely in §2.1.

## 7. Honest labels

- PROVEN: arithmetic reproduction of all four records (exact formula); Σp=1/320, Σq=2;
  all p_i,q_i > 0; pressure-prune conservativeness (0.008496 > 0.0062); verifier
  soundness+completeness (code inspection); B = 2√((m−1)A/m) − 1 + A/m (read from the
  tawan script and re-derived); B < m for eps ≤ 0.1; m=171 is the formula's argmax;
  formula stays below 0.6818 for all feasible eps (crosses only at eps ≈ 0.025, infeasible);
  no verifier/algebra divergence.
- CHECKED NUMERICALLY (mpmath 40–50 dps, commands in §5 + session transcript): the
  four-record table; direction candidates; H(α) monotonicity; dB/deps = 163.6 at the record
  point; eps=0 behavior (B = −1, bound 0.66556).
- CONJECTURED: the interpretation "certified floor eps drives B, which drives the
  denominator, at the same weight (m−6)/m as the tax" (consistent with
  structural-leverage-synthesis.md's decomposition, but the lemma behind it is unread).
- INCONCLUSIVE (blocker): the direction of the division — whether the certified algebra is
  `p(1−B/m) ≥ H−τ` (record valid) vs a sign-flipped or subtraction form (record invalid,
  value ≤ 0.6695 < ceiling). This is the E[T]≥0-class question for this certificate and is
  NOT resolved by the verifier, which certifies only `F_B ≥ eps`.
