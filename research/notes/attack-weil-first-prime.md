# Attack: first-prime survival for Weil positivity (the RH-horizontal line)

**Date:** 2026-08-13. **s4h:** constraint-hardness (is the first-prime a wall or a finite calculation?) + epistemology (labels) + strategy (do not re-grind the exhausted coboundary class).
**Redirect:** the previous session closed the in-class `(psum, l, c)` search (`handoff-psum-lc-frontier.md`). METHOD FIRST + `attack-cvs-import.md` §9.4: if the program funds the RH-horizontal line, the first tasks are Suzuki Thm 1.4 for larger `a`, and the limit formulas. This note does (a).
**Code:** `tools/weil_first_prime/probe.py`. Every number below is from that script (or the one-off N-convergence command in §6). `uv` was not on PATH; ran with system `python3` + numpy 2.4.4.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

---

## 0. Verdict up front

Weil positivity on every finite interval is equivalent to RH. Positivity is already proved on the *prime-free* interval `a < (log 2)/2`. Continuity of `λ_a` does **not** by itself cross the first prime (the infimum could hit `0` at the endpoint). Yoshida’s finite calculation at `t = (log 2)/2` supplies the strict inequality at the threshold, hence some `δ`-neighborhood past it; that `δ` is not explicit. The crude bound that treats the prime-2 term as size `√2 log 2 ≈ 0.980` **cannot** produce an explicit `δ` (it is 600× the Ritz gap at `a = (log 2)/2`). The actual prime-2 matrix element is an *overlap* of size `O(10^{-2})`, not `O(1)`. In the 4–8 mode even Dirichlet subspace the Rayleigh quotient stays positive through the whole first-prime window — but Rayleigh–Ritz is an **upper** bound, and past `a₂` the value is a `10^{-5}` remainder after `O(1)` cancellation, so this does **not** prove `λ_a > 0` for `a > (log 2)/2`.

**What is new:** a precise missing lemma (Yoshida’s “finite calculation depending on `t`”, now with one prime) and a diagnosed obstruction (need a *lower* bound at the `10^{-5}` scale, not more coboundary optimization).

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

A Poincaré upgrade (CONJECTURED as a lemma, not proved here): `v ∈ H₀¹(-a,a)` vanishes at `±a`, so on a strip of width `2ε` one has `‖v‖_{strip} ≤ C ε ‖v'‖`. Then `|G(log 2)| ≤ C' ε² ‖v'‖²`. Dangerous modes are *low* frequency (small `‖v'‖/‖v‖`); those are exactly the modes for which the strip bound is cheapest. High-frequency modes are protected by `Re ψ(1/4+iv/2) ~ log|v|` (Bombieri Thm 12).

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

---

## 9. Honesty footer

- PROVEN (read at source): Weil ⇔ RH; Yoshida localization; Suzuki Thms 1.1–1.5, Cor 1.6; Bombieri Thm 12 and the trichotomy; continuity of `λ_a`.
- CHECKED NUMERICALLY (`python3 tools/weil_first_prime/probe.py` and the N-convergence snippet): all tables in §2–§4; self-checks passed.
- CONJECTURED: the Lemma in §5; Poincaré `ε²` overlap; Bombieri (iii) uniqueness in the infinite on-line class; Suzuki limit formula (1.12).
- INCONCLUSIVE: sign of `λ_a` on `(a₂, a₃)` (Ritz upper bounds only; remainder not a proof).
- ABANDONED: crude prime bound; in-class certificate grind as an RH route.
- No zeros were computed. No coboundary verifier was rerun.
