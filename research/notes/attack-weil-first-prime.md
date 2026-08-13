# Attack: first-prime survival for Weil positivity (the RH-horizontal line)

**Date:** 2026-08-13. **s4h:** constraint-hardness (is the first-prime a wall or a finite calculation?) + epistemology (labels) + strategy (do not re-grind the exhausted coboundary class).
**Redirect:** the previous session closed the in-class `(psum, l, c)` search (`handoff-psum-lc-frontier.md`). METHOD FIRST + `attack-cvs-import.md` §9.4: if the program funds the RH-horizontal line, the first tasks are Suzuki Thm 1.4 for larger `a`, and the limit formulas. This note does (a).
**Code:** `tools/weil_first_prime/probe.py`, `lower_bound.py`, `diagnose_neg.py`, `dirichlet_matrix.py`, `multiplier.py`, `dirichlet_ft.py`. Every number below is from those scripts (or the one-off N-convergence command in §6). `uv` was not on PATH; ran with system `python3` + numpy 2.4.4.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

---

## 0. Verdict up front

Weil positivity on every finite interval is equivalent to RH. Positivity is already proved on the *prime-free* interval `a < (log 2)/2`. Continuity of `λ_a` does **not** by itself cross the first prime (the infimum could hit `0` at the endpoint). Yoshida’s finite calculation at `t = (log 2)/2` supplies the strict inequality at the threshold, hence some `δ`-neighborhood past it; that `δ` is not explicit. The crude bound that treats the prime-2 term as size `√2 log 2 ≈ 0.980` **cannot** produce an explicit `δ` (it is 600× the Ritz gap at `a = (log 2)/2`). The actual prime-2 matrix element is an *overlap* of size `O(10^{-2})`, not `O(1)`. In the 4–8 mode even Dirichlet subspace the Rayleigh quotient stays positive through the whole first-prime window — but Rayleigh–Ritz is an **upper** bound, and past `a₂` the value is a `10^{-5}` remainder after `O(1)` cancellation, so this does **not** prove `λ_a > 0` for `a > (log 2)/2`.

**What is new (this continuation):** the Poincaré overlap lemma is now **PROVEN** (elementary Hardy on endpoint strips). The saturating two-bump family is *not* a negative direction (`T/G(0) ≥ 0.386` through `a₃`). The pointwise Fourier multiplier of `T` is **negative even where positivity is known**, so a 1D infimum of `M_a(ξ)` cannot prove the lemma. Gershgorin / diagonal Schur on the Dirichlet matrix **fail** (off-diagonals `4–6×` the ground gap; positivity is a coherent cancellation). Frequency-side Ritz in the even Dirichlet subspace stays positive through the whole first-prime window, but the gap collapses from `1.5×10^{-3}` at `a₂` to `6×10^{-8}` at `a₃`. Prime-by-prime matrix certification will not reach RH; a uniform-in-`a` argument is required.

RH is not proved. The certificate-class grind is not resumed.

---

## 1. The RH-equivalent (literature, restated)

Let `Q_W(v) = W(v * ṽ)` be Weil’s quadratic form and

```
λ_a := inf { Q_W(v)/‖v‖_{L²(-a,a)}² : 0 ≠ v ∈ C_c^∞(-a,a) }.
```

| Claim | Label | Source |
|---|---|---|
| RH ⇔ `Q_W(v) ≥ 0` for all `v ∈ C_c^∞(ℝ)` | PROVEN | Weil 1952; Suzuki 2606.09096 §1.1 |
| RH ⇔ `Q_W > 0` on `C_c^∞(-a,a)` for **every** `a > 0` | PROVEN | Yoshida 1992; Suzuki after Thm 1.3 |
| `λ_a` is continuous in `a` (no RH used) | PROVEN | Suzuki Thm 1.3 |
| `λ_a > 0` for all `0 < a < (1/2) log 2` | PROVEN | Suzuki Thm 1.4 (proof: §5, explicitly for `a < (1/2)log 2`); Bombieri Thm 12 (`|supp F| < log 2`); Yoshida Lemma 2 |
| Yoshida verified positivity at the endpoint `t = (log 2)/2` by a finite calculation | PROVEN as stated | Bombieri 2000, p.184 |
| If RH fails then `λ_a < 0` for some finite `a` (continuity + small-`a` positivity) | PROVEN | Suzuki after Thm 1.3 |
| For sufficiently small `a`, `λ_a` is simple and the eigenfunction is even | PROVEN | Suzuki Thm 1.4 |
| `W(a,θ;z)` has only real zeros, unconditionally | PROVEN | Suzuki Thm 1.5 (uses only: finitely many primes at fixed `a`) |
| `e^{φ} W(a,θ;z) → ξ/ξ'(1/2−iz)` as `a→∞` uniformly on compacts ⇒ RH | CONJECTURED | Suzuki Cor 1.6 |

**Normalization in this note.** Suzuki’s `a` is the support of `v`. Primes enter `W(v*ṽ)` when `2a ≥ log n`, i.e. `a ≥ (log n)/2`. So:

- `a₂ := (log 2)/2 ≈ 0.346573590280` — first-prime threshold (Yoshida’s `t`)
- `a₃ := (log 3)/2 ≈ 0.549306144334` — second-prime threshold
- first-prime-only window: `a₂ < a < a₃`, width `(1/2)log(3/2) ≈ 0.202732554054`

**Corollary (PROVEN, given Yoshida’s endpoint check).** Suzuki gives `λ_a > 0` only on the open interval `a < a₂`. Continuity alone does **not** push past `a₂` (the infimum could tend to `0` at the endpoint). What does: Yoshida’s finite calculation that positivity still holds *at* `t = a₂` (Bombieri p.184), hence `λ_{a₂} > 0`, hence by continuity a neighborhood `a < a₂+δ`. First-prime survival for *some* `δ` is therefore in the literature, but the `δ` is not explicit and is not known to reach `a₃`.

---

## 2. Why the crude prime bound dies (PROVEN arithmetic)

For even `G = v*ṽ`, the prime-2 contribution to Bombieri’s `T[G]` is

```
− (Λ(2)/√2) · 2 G(log 2) = − √2 log 2 · G(log 2).
```

`|G(log 2)| ≤ G(0) = ‖v‖²`, so the crude size is

```
√2 log 2 ≈ 0.98025814
```

CHECKED NUMERICALLY (`probe.py` prints `crude |prime2|/G0 ≤ 0.98025814`).

At the threshold, the even-subspace Ritz gap is `≈ 1.58×10^{-3}` (converged, §6). The crude bound is **~620× larger** than that gap. **ABANDONED:** any argument that estimates `|G(log 2)|` by `G(0)` cannot cross `a₂`. This is a hardness of the *estimate*, not of the form.

---

## 3. The overlap mechanism (the only way prime 2 does not immediately win)

`G(log 2) = ∫ v(y) v(y−log 2) dy`. The integrands have overlapping supports of length `2a − log 2 = 2(a−a₂)`. At `a = a₂` the overlap is empty and `G(log 2) = 0` (the autocorrelation vanishes at the edge of its support). For `a = a₂+ε` the overlap has length `2ε`.

Cauchy–Schwarz on the overlap:

```
|G(log 2)| ≤ ‖v‖_{L²(I₁)} ‖v‖_{L²(I₂)} ≤ (overlap bound).
```

CHECKED NUMERICALLY at the mid-window `a = (a₂+a₃)/2 ≈ 0.44794`, ground even mode, `G(0)=1`:

| quantity | value | command |
|---|---|---|
| `G(log 2)` | `7.20033147×10^{-3}` | `python3 tools/weil_first_prime/probe.py` |
| overlap CS bound | `2.53011324×10^{-2}` | same |
| prime-2 term in `T` | `−7.05818356×10^{-3}` | same |
| crude ceiling `√2 log 2` | `0.98025814` | same |

The actual matrix element is **136× smaller** than the crude bound, and the overlap CS bound is only 3.5× the actual value (right shape, not sharp). This is why first-prime survival is not obviously false: prime 2 couples only through a thin edge overlap.

A Poincaré upgrade (PROVEN, §10): `v ∈ H₀¹(-a,a)` vanishes at `±a`, so on a strip of width `2ε` one has `‖v‖_{strip} ≤ √2 ε ‖v'‖_{strip}`. Then `|G(log 2)| ≤ ε² ‖v'‖²`. Dangerous modes are *low* frequency (small `‖v'‖/‖v‖`); those are exactly the modes for which the strip bound is cheapest. High-frequency modes are protected by `Re ψ(1/4+iv/2) ~ log|v|` (Bombieri Thm 12). The saturating (linear-ramp) family has Poincaré ratio `1/3` and `T/G(0) ≥ 0.386` through `a₃` — not a negative direction.

---

## 4. What Rayleigh–Ritz can and cannot say

The probe expands even Dirichlet functions

```
v(x) = Σ_{k=0}^{M−1} c_k cos((k+1/2) π x / a),  v(±a)=0,
```

and computes the lowest generalized eigenvalue of the discretized `T[v*ṽ]`. **Ritz ⇒ `λ_true ≤ λ_Ritz`.** Positive `λ_Ritz` does not prove positivity. Negative `λ_Ritz` would prove a negative direction (a disproof of positivity on that interval, hence — if `a` is large enough to be past all numerical doubt — a disproof of RH). We found no negative direction.

Self-checks in `probe.py` (must pass): `T` linear in `G`; `G(0)=‖v‖²`; primes do not change `T` for `a < a₂`; `λ_Ritz(0.10)>0`.

### 4.1 Inside the proved region (sanity of `T`)

| `a` | primes | `λ_Ritz` (M=8, N=601) | N-convergence (M=4) |
|---|---|---|---|
| 0.10 | off | 0.470546928057 | — |
| 0.20 | off | 0.101693183516 | 0.10733 at N=1601, stable to 0.1% from N=201 |

At `a=0.20 < a₂` the value is `O(10^{-1})` after `O(1)` cancellation and **is grid-converged**. Consistent with Suzuki/Bombieri/Yoshida. Label: CHECKED NUMERICALLY (sanity, not a new theorem).

### 4.2 At and past `a₂`

| `a` | `λ_Ritz` (M=8, N=601) | notes |
|---|---|---|
| `0.95 a₂` | 0.002943398607 | primes on/off agree to `1e-9` (self-check) |
| `a₂` | 0.001520003761 | prime-2 term `2×10^{-32}` (edge vanishing) |
| `(a₂+a₃)/2` | 0.000035438374 | **not N-converged at N=601** |
| `0.98 a₃` | 0.000017619976 | same caveat |
| `a₃` | 0.000016214642 | primes 2 and 3 both live |
| `1.05 a₃` | 0.000016420999 | same caveat |

M-stability at `0.98 a₂`: M=6 gives 0.002004, M=8 gives 0.001941, rel 3.2%.

N-convergence of `λ_Ritz` (M=4), extra command in §6:

| N | `a=0.20` | `a=a₂` | mid-window |
|---|---|---|---|
| 201 | 1.07476e-1 | 1.66091e-3 | 1.21488e-4 |
| 401 | 1.07369e-1 | 1.60236e-3 | 5.30273e-5 |
| 801 | 1.07338e-1 | 1.58356e-3 | 3.44908e-5 |
| 1601 | 1.07329e-1 | 1.57888e-3 | 2.81570e-5 |

At `a₂`, Richardson `2λ_{1601}−λ_{801} ≈ 1.574×10^{-3}` — **converged, positive in the 4-mode even subspace.** Consistent with Yoshida’s endpoint calculation.

At mid-window the value is still dropping (`~1/N`). Richardson estimate `≈ 2.18×10^{-5}`. Still positive *as an upper bound*, which does not prove `λ_true > 0`. Label: INCONCLUSIVE for positivity past `a₂`.

### 4.3 The cancellation (why a lower bound is the whole game)

Component split of `T` on the ground even mode (`G(0)=1`), M=8 N=601:

| `a` | `T` | `2cosh` | `−(log 4π+γ)` | arch. integral | primes |
|---|---|---|---|---|---|
| 0.20 | +1.017e-1 | +0.726 | −3.108 | +2.484 | 0 |
| `a₂` | +1.520e-3 | +1.102 | −3.108 | +2.008 | ~0 |
| mid | +3.544e-5 | +1.224 | −3.108 | +1.891 | **−7.058e-3** |
| `a₃` | +1.621e-5 | +1.328 | −3.108 | +1.802 | **−2.153e-2** |

Past `a₂`, `T` is the difference of two `O(1)` archimedean blocks minus an `O(10^{-2})` prime term, leaving `O(10^{-5})`. Float64 rounding is not the issue (`~1e-15` relative); **quadrature bias is**. A proof must control this difference with a two-sided remainder, i.e. Yoshida’s finite calculation with the prime-2 Dirac included.

---

## 5. The missing lemma (the METHOD)

**Lemma (first-prime finite calculation) — CONJECTURED, the deliverable shape.**
There exist explicit constants `K < ∞` and `c > 0` such that for every `v ∈ H₀¹(-a,a)` with `a ∈ [a₂, a₃)` and `‖v‖₂ = 1`,

```
T[v*ṽ]  ≥  c  >  0.
```

*Why this is finite-dimensional.* Split frequencies at height `K` as in Bombieri Thm 12: the high-frequency piece is positive by `Re(Γ'/Γ(1/4+iv/2)) ≥ log|v| − C` (explicit `C`); the low-frequency piece lives in a Paley–Wiener space of dimension `O(K a)` and is a genuine matrix, now with one extra rank-one update `−√2 log 2 · G(log 2)`. Yoshida already did the `K`-split with **no** primes at `a=a₂`. Adding prime 2 is one explicit functional on that same matrix.

*Kill criterion.* If the low-frequency matrix (interval-certified) has a negative eigenvalue that the high-frequency floor cannot absorb, the lemma is false and `λ_a < 0` for that `a` — which, if the certification is correct, would refute RH. If it stays positive through `[a₂, a₃)`, repeat at prime 3, 5, … . The induction is the RH-horizontal program. It fails if the spectral gap shrinks faster than the accumulating prime updates; §4.3 says the gap is already `10^{-5}` at the first prime, so each step needs a tighter remainder than the last.

*What we did not do (compute discipline).* No interval-arithmetic run, no `K`-sweep, no zero-counting. The float64 Ritz is only a search for a cheap negative direction (none found in 8 even modes). A `rug`/`arb` certificate of the low-frequency matrix is the next cheap-enough computation that would change a belief (positivity in the first-prime window: INCONCLUSIVE → PROVEN or REFUTED).

---

## 6. Commands (every number)

Main probe (self-checks + table + components + M/N spot checks):

```
python3 tools/weil_first_prime/probe.py
```

(`uv` was not installed in this environment; numpy 2.4.4 provided `numpy.trapezoid`.)

N-convergence (M=4, the table in §4.2):

```
python3 - <<'PY'
import sys
sys.path.insert(0, 'tools/weil_first_prime')
from probe import A2, A3, lowest_rayleigh
for a, pr, tag in [(0.20, False, 'a20'), (A2, True, 'a2'), (0.5*(A2+A3), True, 'mid')]:
    print(tag, a, pr)
    for N in (201, 401, 801, 1601):
        print(N, lowest_rayleigh(a, M=4, N=N, primes=pr))
PY
```

Belief these runs change: (1) whether `T` is sane inside the proved region (yes); (2) whether a crude `|G|≤G(0)` bound can cross `a₂` (no); (3) whether an 8-mode even subspace already goes negative in the first-prime window (no, but that does not prove positivity). Expected runtime: a few seconds. No further grid was run.

---

## 7. Bombieri’s trichotomy, sharpened (side lemma)

Bombieri 2000, introduction / Thm 10: if there are **finitely many** off-line zeros, then either (i) RH, or (ii) a negative Rayleigh for the infinite matrix, or (iii) a linear relation

```
Σ_ρ c_ρ / (ρ(1−ρ)) x^{−ρ} + A + B x^{−1}  ≡  0    for  1 ≤ x ≤ M₀
```

with `Σ |c_ρ|² = 1` and at least half the `ℓ²` mass on the off-line zeros.

**Lemma (finite exponential independence) — PROVEN, classical.** If `S ⊂ ℂ` is finite and the exponents are pairwise distinct, then `{x^{−s} : s ∈ S} ∪ {1, x^{−1}}` are linearly independent as functions on any nonempty open subinterval of `(0,∞)`. Proof: `x=e^t` reduces to exponential polynomials; distinct exponents are independent (Wronskian / Laplace).

**Consequence.** Alternative (iii) **cannot hold as a finite sum**. Under the finite-exceptions hypothesis the on-line zeros still contribute an *infinite* almost-periodic sum, so (iii) is not killed. The remaining uniqueness statement is: a Besicovitch / Sobolev almost-periodic function of the Weil-extremal class that vanishes on an interval vanishes identically. That is CONJECTURED (Bombieri himself calls the independence “probably quite difficult”). It is a different lever than first-prime survival; it would rule out *finitely many* exceptions, not RH.

---

## 8. Decisions

- **ABANDON** (this session) further coboundary / `(psum,l,c)` / tangent-LP work. Class exhausted at 0.673481; METHOD FIRST.
- **ABANDON** the crude `|G(log n)| ≤ G(0)` estimate as a tool for crossing any prime threshold.
- **FUND** the first-prime finite calculation (Lemma in §5): explicit `K`-split + one rank-one prime-2 update, interval-certified. That is Suzuki Thm 1.4 for `a` up to `a₃`.
- **TRACK** Bombieri (iii) uniqueness for the infinite on-line sum; not funded until the finite-calculation lever is closed.
- **DO NOT** claim `λ_a > 0` for `a > a₂`. Ritz is the wrong side of the inequality.
- **ABANDON** Gershgorin / diagonal Schur / pointwise `M_a(ξ)>0` as tools to prove first-prime survival (all three fail for documented reasons, including in the *proved* region `a<a₂`).
- **ABANDON** (as an RH route) prime-by-prime interval certification of Dirichlet matrices: the even-subspace gap drops by `~2×10^4` across one prime window (`1.5×10^{-3} → 6×10^{-8}`). The next primes are uncertifiable by this encoding. A one-off explicit `δ` just past `a₂` would still be a theorem, but it is not on the path to RH.
- **FUND** a uniform-in-`a` positivity mechanism (Suzuki Cor 1.6 limit, or a Gårding inequality with an `a`-independent remainder that the primes cannot eat), not a larger matrix at `a₃`.

---

## 9. Honesty footer

- PROVEN (read at source): Weil ⇔ RH; Yoshida localization; Suzuki Thms 1.1–1.5, Cor 1.6; Bombieri Thm 12 and the trichotomy; continuity of `λ_a`.
- PROVEN (elementary, §10): Poincaré overlap `|G(log 2)| ≤ ε² ‖v'‖_{L²(-a,a)}²` for `a=a₂+ε`.
- CHECKED NUMERICALLY (`python3 tools/weil_first_prime/probe.py` and the N-convergence snippet): all tables in §2–§4; self-checks passed.
- CHECKED NUMERICALLY (`python3 tools/weil_first_prime/lower_bound.py`, `diagnose_neg.py`, `dirichlet_matrix.py`, `multiplier.py`, `dirichlet_ft.py`): §§10–14.
- CONJECTURED: the Lemma in §5; Bombieri (iii) uniqueness in the infinite on-line class; Suzuki limit formula (1.12).
- INCONCLUSIVE: sign of `λ_a` on `(a₂, a₃)` (Ritz upper bounds only; remainder not a proof; gap at `a₃` is `10^{-8}`).
- ABANDONED: crude prime bound; in-class certificate grind as an RH route; Gershgorin/Schur decoupling; pointwise multiplier positivity; prime-by-prime matrix grind as an RH route.
- No zeros were computed. No coboundary verifier was rerun.

---

## 10. Poincaré overlap lemma (PROVEN)

**Lemma.** Let `a = (log 2)/2 + ε` with `ε>0`, and `v ∈ H₀¹(-a,a)` (absolutely continuous, `v(±a)=0`). Let `G(τ) = ∫ v(x) v(x-τ) dx`. Then

```
|G(log 2)|  ≤  ε² ‖v'‖_{L²(-a,a)}².
```

**Proof.** The integrand of `G(log 2)` lives on the overlap of `[-a,a]` with `[-a,a]+log 2`, which is `I_R = [a-2ε, a]`; the shifted copy is `I_L = [-a, -a+2ε]`. For `s ∈ [0, 2ε]`,

```
v(a-s) = −∫_0^s v'(a-u) du,
|v(a-s)|² ≤ s ∫_0^s |v'(a-u)|² du ≤ s ‖v'‖_{I_R}².
```

Integrate in `s`: `‖v‖_{I_R}² ≤ ‖v'‖_{I_R}² ∫_0^{2ε} s ds = 2ε² ‖v'‖_{I_R}²`, so `‖v‖_{I_R} ≤ √2 ε ‖v'‖_{I_R}`. The same bound holds on `I_L`. Therefore

```
|G(log 2)| ≤ ‖v‖_{I_R} ‖v‖_{I_L}
           ≤ 2ε² ‖v'‖_{I_R} ‖v'‖_{I_L}
           ≤ ε² (‖v'‖_{I_R}² + ‖v'‖_{I_L}²)
           ≤ ε² ‖v'‖_{L²(-a,a)}².
```

Equality in the strip Hardy bound holds when `v'` is constant on each strip (linear ramps). Equality in AM-GM needs `‖v'‖_{I_R}=‖v'‖_{I_L}`. Equality in Cauchy–Schwarz for `G` needs `v|_{I_R}` proportional to the shifted `v|_{I_L}`; linear ramps are *reversals* of each other, so they do not saturate CS. □

CHECKED NUMERICALLY on the saturating even ramps of width `2ε` (`python3 tools/weil_first_prime/lower_bound.py`): `G(log 2)/G(0) → 1/4` (independent of `ε`), Poincaré ratio `|G|/(ε²‖v'‖²) → 1/3`, max ratio on the sampled grid `0.3355 < 1`. Closed-form check: `G=ε/3`, `G(0)=4ε/3`, `‖v'‖²=1/ε`, ratio `(ε/3)/ε = 1/3`.

**Corollary (size of prime 2).** The prime-2 term in `T` is `−√2 log 2 · G(log 2)`, hence

```
prime-2  ≥  −√2 log 2 · ε² ‖v'‖²  ≈  −0.980258 · ε² ‖v'‖².
```

For the saturating family this is `−0.245 · G(0)`, independent of `ε`. Narrow bumps are *not* a small perturbation of `G(0)`; they are a large high-frequency correction, protected by `Re ψ ~ log|ξ|`.

---

## 11. Saturating two-bump is not a negative direction

Even linear ramps of width `2ε` at `±a`, `a=a₂+ε`. `T` via `probe.T_of_G`. Command: `python3 tools/weil_first_prime/lower_bound.py`.

| `ε` | `G(log 2)/G(0)` | Poincaré ratio | `T/G(0)` (no primes) | `T/G(0)` | prime/`G(0)` |
|---|---|---|---|---|---|
| 0.001 | 0.2505 | 0.3329 | 5.107 | 4.862 | −0.246 |
| 0.010 | 0.2479 | 0.3324 | 2.868 | 2.625 | −0.243 |
| 0.050 | 0.2497 | 0.3332 | 1.436 | 1.191 | −0.245 |
| 0.100 | 0.2502 | 0.3334 | 0.950 | 0.705 | −0.245 |
| 0.202 | 0.2501 | 0.3334 | 0.631 | 0.386 | −0.245 |

Min two-bump Rayleigh in the window: `+0.386` at `ε=a₃-a₂`. **No negative direction.** As `ε→0`, `T/G(0)` grows like `log(1/ε)` (Gårding), beating the constant `−0.245` prime term.

A spurious negative 2×2 generalized eigenvalue in `span{cosine, two-bump}` was `numpy.linalg.eigvalsh` applied to the non-symmetric matrix `B^{-1}H` (`⟨cosine, bump⟩≠0`). Direct Rayleigh on `φ + t·bump` is minimized at `t=0` and stays positive (`python3 tools/weil_first_prime/diagnose_neg.py`). After a Cholesky generalized eigen, `λ_min(2×2) ≥ +4.21×10^{-4}` in the window. Same family below `a₂` (`a=0.20`, primes off) has Rayleigh `≥ 0.129`. `T` is not the source of the scare.

---

## 12. High-frequency `K`-split vs the crude prime bound

`Re ψ(1/4+iξ/2)` via recurrence `ψ(z)=ψ(z+n)−Σ 1/(z+j)` with Stirling seed; self-checked against `ψ(1)=−γ` and `ψ(1/4)=−γ−π/2−3 log 2` (error `< 3×10^{-15}`).

Floor: `log π + √2 log 2 ≈ 2.124988`. First `K` on a `0.1`-grid with `inf_{ξ≥K} Re ψ >` floor: **`K=16.80`**. At that cutoff, even Dirichlet frequencies `(M−1/2)π/a ≥ 16.80` need only `M ≳ 3.4` modes at `a₃`. High modes are crude-prime-safe. The missing lemma is entirely low-frequency.

Bombieri’s printed Thm 12 (`log K − O(1) − 4(a+2/K)a K² log K` with `K=a^{-1}(1+log a^{-1})^{-1}`) is vacuous near `a₂` (the `O(1)` is unspecified and the `K² log K` term already eats `log K`). That is why Yoshida needed a finite calculation, not Thm 12.

---

## 13. Why decoupling fails (Gershgorin, Schur, pointwise multiplier)

### 13.1 Dirichlet matrix, closed-form `G` and frequency-side `M`

Even basis `φ_j(x)=cos(ω_j x)`, `ω_j=(j+1/2)π/a`. Cross-correlation `C_{jk}(τ)` has an elementary antiderivative (`dirichlet_matrix.py`). Equivalently, the even FT is

```
φ̂_j(ξ) = 2 ω_j (−1)^j cos(a ξ) / (ω_j² − ξ²),     φ̂_j(±ω_j) = a,
```

and `H_{jk} = (1/2π) ∫ M_a(ξ) φ̂_j(ξ) φ̂_k(ξ) dξ` (`dirichlet_ft.py`), where `M_a` is Bombieri (12.3) plus the prime-2 multiplier `−√2 log 2 · cos(ξ log 2)`.

Plancherel self-check: `(1/2π)∫ |φ̂_0|² = 0.199992` vs `a=0.20`. Frequency-side `λ` at `a=0.20`, `M=4`: `1.07203×10^{-1}` vs τ-method `1.07327×10^{-1}` (rel `1.2×10^{-3}`). At `a₂`, `M=6`: `1.536×10^{-3}`, matching the converged Ritz `~1.57×10^{-3}`.

Mid-window `|R_{0j}|` (`python3 tools/weil_first_prime/dirichlet_matrix.py`, `M=8`, `nτ=1001`):

| `j` | `R_{jj}` | `|R_{0j}|` | `|R_{0j}|/R_{00}` |
|---|---|---|---|
| 0 | 7.87e-3 | 7.87e-3 | 1.00 |
| 1 | 0.271 | 4.53e-2 | 5.77 |
| 2 | 0.795 | 3.25e-2 | 4.14 |
| 3 | 1.416 | 3.30e-2 | 4.20 |
| 7 | 2.046 | 1.59e-2 | 2.02 |

Naive diagonal Schur `R_{00} − Σ_{j≥1} |R_{0j}|²/R_{jj} = −2.31×10^{-3} < 0`, while the actual min eig of the same matrix is `+4.07×10^{-5}`. **Positivity is a coherent cancellation among coupled modes, not a diagonally dominant gap.** Gershgorin on the ground row is `−0.13`. **ABANDONED** as a proof tool.

### 13.2 Pointwise multiplier (fails even in the proved region)

```
M_a(ξ) = k̂_a(ξ) + Re ψ(1/4+iξ/2) − log π − 1_{2a≥log 2} √2 log 2 · cos(ξ log 2),
k̂_a(ξ) = ∫_{-2a}^{2a} 2 cosh(x/2) cos(ξ x) dx.
```

If `inf_ξ M_a > 0` then `T ≥ (inf M)‖v‖²` because `Ĝ=|v̂|²≥0`. Command: `python3 tools/weil_first_prime/multiplier.py`.

| `a` | primes | `inf M` | at |
|---|---|---|---|
| 0.10 | off | **−4.571** | `ξ=0` |
| 0.20 | off | −3.761 | `ξ=0` |
| `a₂` | on | −3.524 | `ξ=0` |
| mid | on | −2.648 | `ξ=0` |

`inf M < 0` already at `a=0.10`, where Suzuki/Bombieri prove `λ_a>0`. The Paley–Wiener type constraint is load-bearing **even with no primes**. Mid-window `M(ξ)` has a negative well at `ξ=0` (`M=−2.65`) *and* a second well near `ξ=5–10` (`M≈−0.16`). The first Dirichlet frequency `π/(2a)≈3.50` sits on a positive ridge (`M(3)≈+0.27`) between the wells; sinc leakage into the wells is exactly the `10^{-5}` remainder. **ABANDONED:** pointwise `M>0`.

`k̂(0)=8 sinh(a)` closed form, error `0` to `5×10^{-16}`. Fourier-`M` vs `probe.T` at `a=0.20`: rel `2.8×10^{-3}`.

---

## 14. The gap collapses across the first-prime window

Frequency-side Ritz, prime 2 only, `nξ=20001`, `xmax=200`. Command: `python3 tools/weil_first_prime/dirichlet_ft.py`.

| `a` | `ε=a−a₂` | `λ_Ritz` `M=6` | `M=8` |
|---|---|---|---|
| `a₂` | 0 | 1.536e-3 | 1.502e-3 |
| `a₂+0.01` | 0.01 | 1.128e-3 | 1.117e-3 |
| `a₂+0.05` | 0.05 | 2.603e-4 | 2.507e-4 |
| mid | 0.101 | 2.240e-5 | 2.209e-5 |
| `a₂+0.15` | 0.15 | 1.495e-6 | 1.302e-6 |
| `a₃−10^{-3}` | 0.202 | 8.37e-8 | 7.02e-8 |
| `a₃−10^{-4}` | 0.203 | 7.93e-8 | 6.63e-8 |

ξ-grid at mid, `M=4`: `λ` *increases* toward `~2.59×10^{-5}` as `(nξ, xmax)` grow (`2.33e-5 → 2.59e-5`). The `10^{-5}` is not a τ-trapezoid artifact. At `a₃−10^{-3}`, `M=4,6,8,10` gives `1.76e-7, 8.37e-8, 7.02e-8, 6.57e-8` — still positive, still dropping, still an **upper** bound.

Ratio `λ(a₂)/λ(a₃−) ≈ 2×10^4` over a window of width `0.20`. A geometric extrapolation through subsequent primes (thresholds at `(log p)/2`) makes the gap uncertifiable long before the primes are exhausted. **ABANDONED as an RH route:** interval-certifying larger Dirichlet matrices prime by prime.

A modest explicit `δ` with gap `~10^{-3}` (`a ≤ a₂+0.01`) remains a possible *local* theorem (Yoshida with prime 2, `δ` explicit). It does not scale to RH.

---

## 15. What would actually prove RH in this encoding

Weil positivity on every finite interval ⇔ RH. The obstruction is not “we have not computed a large enough matrix.” It is that `λ_a` (even restricted to a few even modes) appears to drop exponentially in `a` once primes are live, while the archimedean multiplier `M_a` is negative on a set of positive measure at every `a` we sampled. Any proof must use the Paley–Wiener type `2a` *structurally* — a Gårding inequality, a positivity-improving semigroup (Suzuki §5, currently only for small `a`), or Suzuki Cor 1.6 (limit of `W(a,θ;z)` toward `ξ/ξ'`).

Next lever: Suzuki’s positivity-improving argument in §5 — what dies at `a₂`. Reading at source (Suzuki 2606.09096 §5.2): small-`a` positivity uses a Beurling–Deny Dirichlet form whose jumping kernel `|x−y|^{-1}` is positive on `(-1,1)²`, hence irreducible, hence the semigroup is positivity-improving and the ground state is simple and even. The prime-2 term `−√2 log 2 · G(log 2)` is an *attractive* coupling of the two endpoint strips (for even `v`, a Hankel form `∫_0^{2ε} u(s) u(2ε−s) ds`). Attractive kernels are not Dirichlet-form jumping measures. Label: PROVEN that Suzuki’s §5 machine as written does not apply past `a₂`; CONJECTURED that some replacement (Dirichlet form plus a compact Hankel perturbation, or a different Markov kernel) can. That replacement is the RH-horizontal method, not a larger matrix.

---

## 16. Commands (continuation)

```
python3 tools/weil_first_prime/lower_bound.py
python3 tools/weil_first_prime/diagnose_neg.py
python3 tools/weil_first_prime/dirichlet_matrix.py
python3 tools/weil_first_prime/multiplier.py
python3 tools/weil_first_prime/dirichlet_ft.py
```

(`uv` not on PATH; system `python3` + numpy 2.4.4. Exploratory `f64`, not `rug`/`arb`. Python used because each script is a few hundred ms of closed-form / 1D quadrature, not a search.)

