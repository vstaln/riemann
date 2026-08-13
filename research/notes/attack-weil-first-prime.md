# Attack: first-prime survival for Weil positivity (the RH-horizontal line)

**Date:** 2026-08-13. **s4h:** constraint-hardness (is the first-prime a wall or a finite calculation?) + epistemology (labels) + strategy (do not re-grind the exhausted coboundary class).
**Redirect:** the previous session closed the in-class `(psum, l, c)` search (`handoff-psum-lc-frontier.md`). METHOD FIRST + `attack-cvs-import.md` §9.4: if the program funds the RH-horizontal line, the first tasks are Suzuki Thm 1.4 for larger `a`, and the limit formulas. This note does (a).
**Code:** `tools/weil_first_prime/probe.py`, `lower_bound.py`, `diagnose_neg.py`, `dirichlet_matrix.py`, `multiplier.py`, `dirichlet_ft.py`, `screw_kernel.py`, `dirichlet_vs_prime.py`, `remainder_bound.py`, `rpp_closed.py`, `poincare_even.py`, `l_fourier.py`. Every number below is from those scripts (or the one-off N-convergence command in §6). `uv` was not on PATH; ran with system `python3` + numpy 2.4.4.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

---

## 0. Verdict up front

Weil positivity on every finite interval is equivalent to RH. Positivity is already proved on the *prime-free* interval `a < (log 2)/2`. Continuity of `λ_a` does **not** by itself cross the first prime (the infimum could hit `0` at the endpoint). Yoshida’s finite calculation at `t = (log 2)/2` supplies the strict inequality at the threshold, hence some `δ`-neighborhood past it; that `δ` is not explicit. The crude bound that treats the prime-2 term as size `√2 log 2 ≈ 0.980` **cannot** produce an explicit `δ` (it is 600× the Ritz gap at `a = (log 2)/2`). The actual prime-2 matrix element is an *overlap* of size `O(10^{-2})`, not `O(1)`. In the 4–8 mode even Dirichlet subspace the Rayleigh quotient stays positive through the whole first-prime window — but Rayleigh–Ritz is an **upper** bound, and past `a₂` the value is a `10^{-5}` remainder after `O(1)` cancellation, so this does **not** prove `λ_a > 0` for `a > (log 2)/2`.

**What is new (this continuation):** the Poincaré overlap lemma is now **PROVEN** (elementary Hardy on endpoint strips). The saturating two-bump family is *not* a negative direction (`T/G(0) ≥ 0.386` through `a₃`). The pointwise Fourier multiplier of `T` is **negative even where positivity is known**, so a 1D infimum of `M_a(ξ)` cannot prove the lemma. Gershgorin / diagonal Schur on the Dirichlet matrix **fail** (off-diagonals `4–6×` the ground gap; positivity is a coherent cancellation). Frequency-side Ritz in the even Dirichlet subspace stays positive through the whole first-prime window, but the gap collapses from `1.5×10^{-3}` at `a₂` to `6×10^{-8}` at `a₃`. Prime-by-prime matrix certification will not reach RH; a uniform-in-`a` argument is required.

**What is new (§21):** `r''(t)` is closed-form; Taylor is `−7/8 t² − t³/288 − 3t⁴/128`; Suzuki (4.5) matches `T` to `3×10^{-5}`; (4.6) matches `L` to `4×10^{-6}`; dropping `ρ` **fails** at `a₂` (`ν_{\mathrm{Ritz}}=1.348<1.355`); `ρ''≤−(3/10)t²` on `(0,20]` saves the J-ground state at `a₂` (`LB=+2.4×10^{-4}`) and dies near `a₃` on the cosine. Even mean-zero **`μ₂ ≥ 1.641`** (nested HS, conservative `n=81×1.05`) **clears `threshold(a₂)=1.355`**. Complement at `a=a₂` has `R≥0.182`. Ground ray and primes past `a₂` remain. 67% record unchanged. RH not proved.

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
- CHECKED NUMERICALLY (`python3 tools/weil_first_prime/lower_bound.py`, `diagnose_neg.py`, `dirichlet_matrix.py`, `multiplier.py`, `dirichlet_ft.py`, `screw_kernel.py`, `dirichlet_vs_prime.py`): §§10–14, §§17–19.
- CONJECTURED: the Lemma in §5; Bombieri (iii) uniqueness in the infinite on-line class; Suzuki limit formula (1.12); explicit O(t⁴) constant in `r(t)`.
- PROVEN (elementary Taylor of Suzuki (2.2)): `r(t)=−(7/8)t²+O(t⁴)` for `0<t<log 2`.
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

Next lever: Suzuki’s positivity-improving argument in §5 — what dies at `a₂`. Reading at source (Suzuki 2606.09096 §5.2): small-`a` positivity uses a Beurling–Deny Dirichlet form whose jumping kernel `|x−y|^{-1}` is positive on `(-1,1)²`, hence irreducible, hence the semigroup is positivity-improving and the ground state is simple and even. The prime-2 term `−√2 log 2 · G(log 2)` is an *attractive* coupling of the two endpoint strips (for even `v`, a Hankel form `∫_0^{2ε} u(s) u(2ε−s) ds`). Attractive kernels are not Dirichlet-form jumping measures. Label: PROVEN that Suzuki’s §5 machine as written does not apply past `a₂`. The replacement is **not** “add prime to `L_a`”: §17–§18 show `L_a` is O(1) while `T` is the cancelled remainder of Suzuki (4.5). Next: certify `r(t)=−(7/8)t²+O(t⁴)` in (2.2) and control the `−a⟨r''(a·)w,w⟩` term plus the scaled Hankel.

---

## 17. Screw `g(t)` parse (CHECKED NUMERICALLY)

Command: `python3 tools/weil_first_prime/screw_kernel.py`.

Suzuki (1.3) implemented via the Gradshteyn expansion of the Lerch piece in §2.2 (not a truncated Lerch series — that series is unusable as `z=e^{-2|t|}→1`). Self-checks:

| check | value | want |
|---|---|---|
| `g(0)` | `0` | `0` |
| evenness | odd part `0` | `0` |
| `ζ(0,1/4)` via Bernoulli | `0.25` | `1/4` (Suzuki) |
| `A_emp(t=10^{-3})` | `0.70667136` | `A=0.70754637` (rel `1.24×10^{-3}`, the `O(t)` in `r(t)/|t|`) |
| `r(t)/t²` as `t→0` | `−0.87500039` at `t=10^{-4}` | **PROVEN** `−7/8` (Taylor of (2.2): polar contributes `−t²`, `n=2` Hurwitz `ζ(0,1/4)=1/4` contributes `+t²/8`; DSV4F independently re-derived the same three lines; script prints `r/t²`) |

Nyström of the compact kernel `K(t,u)=g(t-u)-g(t)-g(u)` on mean-zero `L²(-a,a)`: `n_neg=0` through `a₃` on grids up to `n=81`. **This does not prove `λ_a>0`.** `G` is compact, spectrum accumulates at `0`, so `min_nz→0` under refinement even when the operator is positive. `Q_W(v)=⟨G Dv, Dv⟩`; the useful operator is `D*GD`, i.e. `T` again. **ABANDONED** as a better lower-bound encoding.

---

## 18. `L_a` does not absorb prime 2 (CHECKED NUMERICALLY)

Command: `python3 tools/weil_first_prime/dirichlet_vs_prime.py`.

Suzuki (2.3) jumping form `L_a` vs prime-2 vs `T`, even families, `G(0)=‖v‖²`:

| family | `ε` | `L_a/G0` | prime/`G0` | `T/G0` |
|---|---|---|---|---|
| cosine | 0.01 | 1.397 | −7.1e-5 | 0.00328 |
| cosine | 0.10 | 1.172 | −0.034 | 0.00794 |
| cosine | 0.202 | 0.967 | −0.140 | 0.00045 |
| two-bump | 0.01 | 5.199 | −0.243 | 2.612 |
| two-bump | 0.202 | 1.950 | −0.245 | 0.385 |

`L_a + prime` stays positive on both families. That does **not** prove `λ_a>0`: `L_a` is O(1) while `T` is the O(10^{-3}) remainder after Suzuki’s other terms cancel `L_a`. Prime 2 is negligible against `L_a` and large against `T` (at `ε=0.202`, `|prime|/T ≈ 310` on the cosine). DSV4F (thinking disabled) suggested absorbing Hankel into `L_a`; the table kills that as an RH route. Two-bump stays Gårding-safe (`T/G0≥0.385`).

---

## 19. The identity that *does* split the cancellation (Suzuki (4.5), PROVEN at source)

Scale `w(t)=v(at)` onto `[-1,1]`. Then `T(v)/‖v‖²_{(-a,a)} = R(a,w)` with

```
R(a,w) = −log a − (2A+1) + L(w)/‖w‖²
         + (1/a) Σ_{n≤e^{2a}} (Λ(n)/√n) · (Hankel of w at lag (log n)/a)
         − (a/‖w‖²) ∬ r''(a(x−y)) w(x) w(y) dx dy.
```

Here `A=(1/2)(log(2π)+γ−1)`, `L` is (4.4) on the *fixed* interval `[-1,1]` (independent of `a`), and `r` is the C² remainder in (2.2). For `a<a₂` the prime sum is empty. As `a→0` the last term is `O(a)` and `−log a → +∞`: that is Thm 1.4.

CHECKED on the even cosine (`w(t)=cos(π t/2)`), `L(w)/‖w‖² = 0.365642` (independent of `a`), and

```
T − [log(1/a) − (2A+1) + L]  ≈  2.86 a
```

for `a∈[0.10, 0.45]` (coefficient `2.84, 2.85, 2.86`). Matching the rank-one approximation `−a r''(0)(∫w)²/‖w‖²` with `r''(0)=−7/4` and `∫w=4/π` gives `a·(7/4)·16/π² ≈ 2.837 a`. The O(10^{-3}) gap at `a₂` is this three-way cancellation (`L`, `log(1/a)−(2A+1)`, and the `r''` rank-one) to relative error `~10^{-3}`. Primes then hit that remainder.

**Lemma (t² remainder) — PROVEN, elementary.** For `t>0` (archimedean `r`, primes stripped),
`r(t) := g_{\mathrm{arch}}(t) − (1/2)t log t − A t` satisfies
`r(t) = −(7/8) t² − (1/288) t³ − (3/128) t⁴ + O(t^5)`.
Proof: `r=r_0+r_1` as in Suzuki p.11; polar `r_0=−t²−t⁴/48+O(t^6)`; Hurwitz `ζ(0,1/4)=1/4` ⇒ `+t²/8`; `ζ(−1,1/4)=1/96` (`B_2(1/4)=−1/48`) ⇒ `−t³/288`; `ζ(−2,1/4)=−1/64` ⇒ `−t⁴/384`; net `t⁴` is `−1/48−1/384=−3/128`. The expansion in `|t|` is even as a function of `t` but has odd powers of `|t|` for `t>0`. CHECKED: `rpp_closed.py`.

Then the last line of (4.5) is `(7/4)a (∫w)² + ρ`-term, and the `ρ`-term is *not* a crude `O(a³)‖w‖²` of size `~0.04` (that wall is the same as `‖ρ''‖_∞`). Sign-definite control is §21.

Cheap model: OpenCode Go `deepseek-v4-flash` with `thinking.disabled` (otherwise the whole `max_tokens` budget is hidden reasoning and `content` is empty). Key is not in the repo. DSV4F drafts were not trusted for numbers: one draft called `L_a=0.967` “below zero”; that error is discarded.

---

## 21. Closed-form `r''`, sign of `ρ''`, even-sector Poincaré (this round)

**RH is not proved.** Certified simple-on-line proportion unchanged. No coboundary grind.

### 21.1 `r''(t)` — PROVEN (Suzuki generating function + chain rule)

For `t>0`,
```
r''(t) = −2 cosh(t/2) + e^{t/2}/(2 sinh t) − 1/(2t),     r''(0+) = −7/4.
```
`r_0''(t)=−2 cosh(t/2)` (chain rule; the factor `1/2` is load-bearing — missing it gives the false `−15/4`). `r_1''` is Suzuki p.11. CHECKED vs 5-point stencil of `r_of_t`: `|closed−stencil|<4×10^{-5}` on `[10^{-4}, 2a_3]` (`rpp_closed.py`).

### 21.2 Taylor — PROVEN elementary; the fake `t⁴` mismatch was `t³`

Command: `python3 tools/weil_first_prime/rpp_closed.py`.

| coeff | exact | source |
|---|---|---|
| `t²` | `−7/8` | polar `−1` + Hurwitz `n=2` `+1/8` |
| `t³` | `−1/288` | `ζ(−1,1/4)=1/96` |
| `t⁴` | `−3/128` | polar `−1/48` + Hurwitz `n=4` `−1/384` |

`(r+7/8 t²)/t⁴` at `t=10^{-3}` is `−3.495` (not `−3/128`): that is `c_3/t + c_4 + O(t)`, with `c_3=−1/288`. After subtracting `c_3 t³`, the quotient is `−0.023437` at `t=10^{-2}` (`−3/128=−0.02343750`).

### 21.3 `(4.5)` pieces sum to `T` — CHECKED NUMERICALLY

Command: `python3 tools/weil_first_prime/remainder_bound.py` (n=401, ~4 min). Even cosine: `T−sum ≈ 3.1×10^{-5}` at every listed `a∈[0.10, 0.45]`. First odd sine: `T−sum ≈ 1.0×10^{-4}`. Crude `‖ρ''‖_∞` lower bound is **negative at `a₂`** (`−0.577` vs `T=0.00268`) — ABANDONED, same wall as crude `|G|\le G(0)`.

Odd sine: rank-one vanishes; `L/‖w‖²=1.518799`; prime Hankel is **positive** (opposite-sign bumps). The first-prime obstruction is in the **even nonnegative** sector.

### 21.4 Dropping `ρ` cannot cross `a₂` — CHECKED NUMERICALLY

`threshold(a)=(2A+1)+log a`. Need `L/‖w‖² + (7/4)a(∫w)²/‖w‖² + ρ + prime ≥ threshold`.

Command: `python3 tools/weil_first_prime/poincare_even.py`.

| | value |
|---|---|
| `threshold(a₂)` | `1.35543263` |
| cosine `L+rank1−th` | `−0.006570` |
| `ν_Ritz` of `J=L+(7/4)a₂(∫)²` on 5 even Dirichlet modes | `1.34822781 < threshold` |
| J-ground (almost cosine: `c_0=0.99963`), `min w=0` | `J−th=−0.007205` |

**Lemma (checked).** The joint form `J_a` without `ρ` is already below threshold at `a₂` on the approximate ground state. Any proof that drops `ρ` cannot cross `a₂`.

### 21.5 Sign of `ρ''` and a usable lower bound for `w≥0`

`ρ''(t):=r''(t)+7/4`. Command: `python3 tools/weil_first_prime/l_fourier.py`.

- `ρ''(t)<0` on `(0,20]` (max in the scan is `O(10^{-5})` at the left endpoint; no zero). CONJECTURED for all `t>0` (DSV4F proof attempt truncated at `max_tokens`; not used).
- `min_{t∈(0,20]} (−ρ''(t)/t²) = 0.300259` at `t=1.501`. Hence **CHECKED:** `ρ''(t) ≤ −(3/10) t²` on `(0,20]` (margin `2.6×10^{-4}`). On the first-prime window `(0,2a₃]`, `c_*=0.302417`.

**Lemma (PROVEN given the sign bound).** If `w≥0` and `ρ''(s)≤−c s²` on `[0,2a]`, then
`ρ`-term `≥ c a³ ∬(x−y)² w(x)w(y) / ‖w‖²`. For even `w`, `∬(x−y)² ww = 2(∫w)(∫ x² w)`.

On the cosine at `a₂`: `ρ_lo=0.00773 > 0.00657`, `LB=+0.00116`. On the J-ground state: `ρ_lo=0.00744`, `LB=+0.00024>0`. The `ρ` lower bound *saves those two functions* at `a₂`. Near `a₃` (`a=0.5483`) the same cosine bound fails (`LB=−0.00253`, prime `−0.140`). So this `c t²` remainder is **not** a ticket through the whole first-prime window, even on test functions.

`LB(w)>0` is a lower bound of `R(w)` on that `w`, **not** of `inf R`. Ritz of `J` is an **upper** bound of `inf J`. Neither proves `λ_a>0`.

### 21.6 `L` split; cosine is not the `L`-minimizer

| family | `L/‖w‖²` | jump | pot | `(∫w)²/‖w‖²` |
|---|---|---|---|---|
| cosine | 0.365645 | 0.284499 | 0.081147 | 1.621122 |
| plateau η=0.05 | 0.293602 | 0.038942 | 0.254661 | 1.966641 |
| tent | 0.447048 | 0.386304 | 0.060744 | 1.499981 |
| mean-zero even | 1.967044 | 1.819418 | 0.147627 | 0 |
| sine (odd) | 1.518799 | 1.330688 | 0.188110 | 0 |
| two-bump | 2.637891 | 2.079673 | 0.558218 | 0.378713 |

`μ_Ritz(L)=[0.26552, 1.96706, 2.555, …]` at `M=5`, `n=201` (upper bounds). Command `python3 tools/weil_first_prime/mu_ritz.py`: `μ₂` is stable under `M=3→7` (`1.9809, 1.9671, 1.9607`) and under `n=81→201` (`1.96715→1.96706`). `μ₁` still drops (`0.285→0.257`). Plateau has smaller `L` than cosine (almost-constant). Two-bump is Gårding-safe. Mean-zero even / odd: rank-one vanishes; through mid-window they stay positive (`log-c+L` or primes help). At `a₃−10^{-3}` mean-zero even `LB=+0.00482` (prime `−0.148` vs `log-c+L=+0.153`). `threshold(a₃)=1.81599338`; `μ_{2,\mathrm{Ritz}}≈1.961` sits `0.145` above it — the same size as the prime hit, so a *lower* bound on `μ₂` is tight if it is to reach `a₃`.

### 21.7 Suzuki (4.6) — CHECKED NUMERICALLY

`L(w)=(1/2π)∫(log|ξ|+γ)|ŵ(ξ)|² dξ` with `ŵ(ξ)=∫_{-1}^1 w(t)e^{-iξt}dt`. Uniform `ξ`-grid is a trap (log weight). Split log-grid near 0 + linear tail, closed `ŵ` of the cosine: `Plancherel=1.000001`, `L_ft−L_jump=−4×10^{-6}`. Average `log|ξ|=−0.21158`.

Crude Paley–Wiener envelope `|ŵ|≤√(2/3)|ξ|‖w‖` on `{ŵ(0)=0}`, dropping the positive tail `|ξ|>e^{-γ}`: `L/‖w‖² ≥ −0.00417`. **ABANDONED** as a `μ₂` bound (vacuous vs `threshold(a₂)=1.355`).

**Even mean-zero envelope that keeps the tail — PROVEN elementary, constant CHECKED.**
For even mean-zero `w` supported in `[-1,1]`: `|cos(ξt)−1|≤ξ²t²/2` ⇒ `|ŵ(ξ)|≤(ξ²/2)∫ t²|w|≤(ξ²/2)√(2/5)‖w‖`, so `|ŵ|²≤ξ⁴/10 ‖w‖²`. Hence the Plancherel mass in `|ξ|<Ω` is `≤ Ω⁵/(50π)`. The log-weight on `|ξ|<e^{-γ}` contributes `≥ −7.09×10^{-5}`. Therefore
```
μ₂ ≥ max_{Ω>1} (1 − Ω⁵/(50π))(log Ω + γ) − 7.09e-5 = 1.02797
```
at `Ω=1.865` (`l_fourier.py`). Hard frequency cutoff with this `ξ²` envelope is **0.327 short** of `threshold(a₂)`.

**Nested concentration (this round) — CHECKED NUMERICALLY.** Command: `python3 tools/weil_first_prime/mu2_envelope.py`.

Low-frequency mass in `|ξ|<ω` is `⟨Q_ω w,w⟩` with kernel `sin(ω(x−y))/(π(x−y))`. On even mean-zero, `‖Q^{emz}_ω‖_{HS}` is a valid operator-norm cap (PROVEN: `‖·‖_{HS}≥‖·‖_{op}`). Nyström trapezoid of that HS, `n=81→321` at `Ω=2.4`: `0.125775 → 0.125675` (decreases; coarser grid is conservative). HS, max-eig, and trace agree to `10^{-4}` (the compression is essentially rank one).

Hard cutoff using `α(Ω)=HS_emz(Ω)` peaks at `μ₂≥1.270` (`Ω=2.4`) — **cannot** reach `1.355` even with exact `λ_max`, because it treats mass in `(0,Ω)` as log-weight 0.

Nested constraint `F(ω)≤α(ω)` for all `ω`, greedy fill, integration by parts:
```
μ₂ ≥ log Ω + γ − ∫_0^Ω α(ω)/ω dω + NEG.
```
Conservative pass (`n=81` HS × 1.05):

| `Ω` | `α_cons` | nested `μ₂` |
|---|---|---|
| 2.2 | 0.0938 | 1.3429 |
| 2.4 | 0.1321 | 1.4202 |
| 3.2 | 0.3570 | **1.6414** |
| 6.0 | 1.0000 | 1.8159 (saturates; HS cap hits 1) |

**`μ₂ ≥ 1.6414 > threshold(a₂)=1.3554`** (margin `0.286`). Does **not** clear `threshold(a₃)=1.816`. Label: CHECKED NUMERICALLY (quadrature of HS, not `rug` interval). The inequality `λ_max ≤ HS` and the Stieltjes lower bound are PROVEN given `α`; the number `α(ω)` is the quadrature.

**Even mean-zero sector at `a=a₂` (prime 2 not yet overlapping).** `R ≥ μ₂ − threshold + ρ`-term. Crude `|ρ|≤ a₂ · |ρ''(log 2)| · 2` with `|ρ''(log 2)|=0.14986` (`rpp_closed.py`) gives `|ρ|≤0.1039`, hence `R ≥ 0.182 > 0`. CHECKED. This is **not** `λ_a>0`: the even ground ray (nonzero mean) still needs the rank-one + `ρ_lo` argument of §21.5, and past `a₂` the prime Hankel is open.

Does **not** raise the 67% simple-on-line record. Does **not** prove RH.

### 21.8 What would prove a local `δ`, and what would prove RH

- **Local `δ` (not RH):** even mean-zero complement at `a=a₂` is now CHECKED (`μ₂≥1.641>1.355`, crude `ρ` leaves `R≥0.182`). The ground ray (nonzero mean) still needs rank-one + `ρ_lo`. Primes past `a₂` still eat overlap. `threshold(a₃)` is not cleared. Interval/`rug` certification of the HS quadrature is the remaining analytic hygiene, not a matrix grind over `a`.
- **RH:** still uniform-in-`a`. Primes accumulate; the `c t²` remainder plus rank-one is a local cancellation, not a Gårding inequality that survives `a→∞`. Suzuki Cor 1.6 (`W(a,θ;z)→ξ/ξ'`) is the spectral encoding; it assumes the form stays positive to define the spaces. Do not claim a path we do not have.

---

## 22. Commands (continuation)

```
python3 tools/weil_first_prime/remainder_bound.py   # (4.5) vs T; ~4 min
python3 tools/weil_first_prime/rpp_closed.py        # r'' closed form + Taylor
python3 tools/weil_first_prime/poincare_even.py     # L split, J vs threshold, ρ_lo
python3 tools/weil_first_prime/l_fourier.py         # (4.6), J-ground, global c*
python3 tools/weil_first_prime/mu_ritz.py           # μ1, μ2 Ritz stability
python3 tools/weil_first_prime/mu2_envelope.py      # nested HS μ₂ vs threshold
```

(`uv` not on PATH; system `python3` + numpy 2.4.4. Exploratory `f64`, not `rug`/`arb`. Python used because each script is closed-form / 1D quadrature, not a search.)

