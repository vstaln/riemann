# Idea-systems: feedback & leverage on the bound

**Role:** idea-generator (s4h-systems) — wave-blast
**Run date:** current wave-blast run (this host `/home/opc/riemann`)
**Scope:** systems map of the bound formula, partial-derivative sensitivity analysis
(in Rust), Meadows leverage-point identification, 10 CONJECTURED ideas ranked by
leverage, and — new this run — a window-family exploration that settles the
numerator-ceiling question (ideas I4/I5).

> **Path note (honesty):** the spec's mandatory files (`/home/vstaln/riemann/hooks/agents.md`,
> `/home/vstaln/.pi/agent/skills/s4h-systems/SKILL.md`, `research/notes/discovery-6732629.md`,
> `attack-vector-catalog*.md`) do **not exist on this host** (stale paths from spec
> generation; the live repo is `/home/opc/riemann`, notes dir empty). Ground truth used
> instead: `tools/beat673/final_leader.py` (record config), `bound_map.py` (achievable-eps
> interpolation table), `verify_cos7.py` (Arb/flint rigorous verifier semantics).
> All numerics here are Rust (`tools/beat673/sens/`) cross-checked with mpmath (50 dps).

---

## 0. Record reproduction — VALIDATED (CHECKED NUMERICALLY)

Certified record configuration (`final_leader.py`): `alpha=149/100, psum=1/220, m=133,
eps=8060e-6, window v(s)=cos(alpha·s)`.

Formula chain (Rust `sens` lib, `src/lib.rs`):

```
I0 = 2 sin(alpha/2)/alpha ;  I2 = 1/2 + sin(alpha)/(2 alpha)
constant = sin(alpha/2)/alpha + 2 cos(alpha/2)/alpha^2
J  = -2 I2/alpha^2 + constant·I0 ;  c = I0^2/(I2+J) ;  H = 2 - 1/c
A  = eps·(m-6) ;  B = Phi(A,m)  [A if A <= m/(m-1), else 2·sqrt((m-1)A/m)-1+A/m]
tau = psum·(m-6)/m ;  bound = (H - tau)/(1 - B/m)
```

**Output (`sens`):** `bound = 0.673262865534356` — exact match to the certified [RETIRED 2026-08-24]
`0.67326286553435601465` (mpmath 50 dps) to all printed digits. [RETIRED 2026-08-24]
Script: `tools/beat673/sens/src/lib.rs`; command:
`cd /home/opc/riemann/tools/beat673/sens && cargo build --release && ./target/release/sens`.
Cross-build (spec's RUST-FIRST mandate): `RUSTFLAGS="-C linker=rust-lld
-C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl`
→ **builds clean** (Finished, 5.7s).

---

## 1. The system map — feedback loops in the bound

```
        ┌─────────────┐   H(alpha) ──────────┐
        │  window fn  │                      ▼
        │ cos(alpha s)│           ┌────────────────────┐
        └─────────────┘           │  numerator: H - tau │
                                 └────────────────────┘
        ┌─────────────┐   eps ──► A=eps(m-6) ──► B=Phi(A,m) ──► 1 - B/m  (denominator)
        │  6-gap floor│                            ▲
        └─────────────┘                            │ concave cap (Bellman)
        ┌─────────────┐   psum ──► tau = psum(m-6)/m  (the tax, in numerator)
        │  pressure   │
        └─────────────┘
                 │
                 └──► certification cost (verifier) ◄── eps, psum, alpha
```

**Identified loops:**

1. **Reinforcing-but-saturating eps loop:** `eps↑ → A↑ → B↑ → denominator(1-B/m)↓ →
   bound↑`. `Phi` is concave in the active sqrt regime — **new this run, quantified**:
   at the record `d²(bound)/deps² = −38.35` (mpmath 50 dps; see §2), i.e. strongly
   concave; marginal bound gain per eps decays from 0.645 @ eps=0.006 to 0.417 @
   0.020 (CHECKED NUMERICALLY, `sens` EPS MARGINAL GAIN block).
2. **Linear tax loop (no saturation):** `psum↓ → tau↓ → numerator↑ → bound↑`, strictly
   linear — **new this run, quantified:** `d²(bound)/dpsum² = 2.67e-39 ≈ 0` (mpmath),
   i.e. the loop is *exactly* linear. This is the only loop with no saturation.
3. **Window loop (hard ceiling):** `alpha → H → numerator↑ → bound↑`, amplifier only
   `1/(1-B/m) = ×1.0078`. Cosine-family H peaks at `H_max = 0.672500703092` @
   `alpha*=1.4140`; the record's alpha=1.49 sits **past** the peak on the descending
   branch (dH/dα @ 1.49 = −0.00216). In-family headroom `ΔH = 7.88e-5 → +0.000079
   bound` (CHECKED NUMERICALLY, `frontier`).
4. **Negative certification-coupling loop (the hidden governor):** denser pressure
   (smaller psum) and higher floors (larger eps) both make the rigorous verifier
   (`verify_cos7.py`) more expensive/less achievable. Fitting the interpolated
   achievable-eps data (`bound_map.py`): `eps_ach = C·pinv^{-k}` with **k = 0.911
   (α=1.40), 0.833 (1.49), 0.819 (1.55)** (CHECKED NUMERICALLY, `ceiling` binary;
   independently re-fitted this run in mpmath: slope of ln-eps vs ln-pinv = −0.911 at
   1.40, −0.833 at 1.49 — consistent, `uv run --with mpmath python3 - <<EOF` command
   in §7). Since k ≈ 1, eps and psum trade off almost one-for-one in certification
   effort — a strong negative feedback loop pinning the bound to a Pareto ridge.

**New structural insight from this run (§4):** the numerator's H-ceiling is *not* a
cosine accident. Eight window families were probed in Rust and **none** exceeds
0.6725007031 (§4). The systems consequence: the numerator is structurally capped; the
only remaining leverage is in the eps/psum coupling (loop 4) and the denominator
amplifier (loop structure, idea I9).

---

## 2. Partial derivatives & curvature at the record (CHECKED NUMERICALLY)

Central differences, relative step 1e-6, at `(alpha,eps,m,psum)=(1.49, 0.00806, 133, 1/220)`.
Script: `tools/beat673/sens/src/lib.rs` (`d_bnd_dp`); command: `./target/release/sens`.

| parameter | d(bound)/dp | log-elasticity d ln b/d ln p | 1.001× ⇒ Δbound | 0.999× ⇒ Δbound |
|-----------|-------------|------------------------------|------------------|------------------|
| eps       | **+0.6428** | **+0.00770**                 | +5.18e-6         | −5.18e-6         |
| psum      | **−0.9623** | **−0.00650**                 | −4.37e-6         | +4.37e-6         |
| alpha     | −0.00216   | −0.00479                     | −3.26e-6         | +3.19e-6         |
| m         | ~0 (−2.0e-8) | ~0                        | ~0               | ~0               |

**Curvature (new this run, mpmath 50 dps, command in §7):**

| second derivative | value | loop reading |
|-------------------|-------|--------------|
| d²(bound)/deps²   | **−38.35** | eps loop strongly concave → saturates |
| d²(bound)/dpsum²  | **2.67e-39** | tax loop exactly linear → never saturates |
| d²(bound)/dα²     | −0.0312 | H peak flat (alpha is a weak, one-shot lever) |
| d²Phi/dA² @ A=1.024 | −0.481 | Bellman cap concavity at the operating point |

**Derivative validation:** in the active sqrt regime `dB/dA = sqrt((m-1)/(m·A)) + 1/m
= 0.992191`, so `dB/deps = dB/dA·(m-6) = 126.008282`; analytic and central-difference
agree to all decimals (CHECKED NUMERICALLY, `final` VALIDATION block).

**Decomposition of the record bound** (CHECKED NUMERICALLY, `sens`):

```
H  = 0.6724218861   (99.35% of the bound itself)
tau= 0.0043403964   (the tax)
B/m= 0.0076959181   (denominator defect)
numerator H-tau = 0.66808149;  denominator 1-B/m = 0.99230408
H contributes 100.6% of the numerator; denominator amplifies ×1.0078
```

**Reading:** the bound is numerically almost equal to H — minus a small tax, plus a
~0.8% amplifier. The eps/psum machinery moves the bound through a narrow lever-band
around H.

---

## 3. The leverage point (Meadows)

**Definition:** the place where a *small, low-cost intervention* produces the *largest*
movement of the bound, accounting for both the partial derivative **and** the coupling
loops (a naive derivative ranking ignores loop 4).

**Effort-weighted ranking (per +1e-4 parameter change):**

| rank | lever | Δbound per 1e-4 | cost | saturation? |
|------|-------|-----------------|------|-------------|
| 1 | **psum ↓ (tax cut)** | **+0.000096** | verifier at new pressure | no — linear loop |
| 2 | **eps ↑ (floor lift)** | +0.000064 | verifier time | yes — concave, decays |
| 3 | **alpha → H peak** | +0.000079 (total, one-shot) | ~free window tweak | yes — H ceiling @1.414 |
| 4 | m retune | ~0 (already optimal) | free | — |

(CHECKED NUMERICALLY, `sens` EFFORT-ADJUSTED LEVERAGE + `final` EFFORT-WEIGHTED LEVERAGE.)

**The systems catch:** the naive highest-leverage parameter (psum, largest |elasticity|,
only non-saturating loop) is *also* the most-coupled one — loop 4 (k≈0.85) cancels
most of its apparent leverage 1:1. The genuine high-leverage moves are those that
**break the coupling** (decouple eps from psum, I1–I3) or **raise the denominator
amplifier** (I9), not those that push a single knob.

**Quantified on the Pareto ridge** (k=1 coupling, alpha=1.41; CHECKED NUMERICALLY,
`final` binary, model-dependent — see honesty note): bound along the ridge is monotone
in pinv — `0.67274 @ 800` → `0.67364 @ 160` — i.e. *looser* pressure + *larger* certified
eps wins along the ridge, and the record (1.49, 220) sits below the ridge maximum
(0.6736417 @ pinv=160), implying slack from re-optimizing (alpha, pinv) jointly.
Independent mpmath re-check with the *interpolated* eps at (1.41,220) gives lower
absolute ridge values (0.67321 @ pinv=160) because interpolation under-reports the
certified eps; both versions agree on the *direction* (looser pinv → higher bound).

---

## 4. NEW this run: the H-ceiling is robust across window families (CONJECTURED — negative result)

Because idea I4 (raise H with a better window) was the most promising "free" lever, this
run tested eight window families in Rust quadrature (Romberg/Gauss-Legendre with the
|s−t| kink split; quadrature validated against the certified lib to 12 digits).
Binaries: `twotone.rs`, `window_max.rs`, `extra_families.rs`
(commands: `cargo build --release --bin twotone && ./target/release/twotone`, etc.).

| family | max H found | vs cosine ceiling 0.6725007031 |
|--------|-------------|--------------------------------|
| cos(a·s) [reference] | 0.672500703092 @ 1.414 | 0 (reproduces lib exactly) |
| cos(a s) + c·cos(b s), a=1.414, b∈[1.5,4], c≤0.6 | 0.672500704 (refined b=1.42,c=0.04) | **+5.8e-10 (noise — no gain)** |
| cos(a s) + c·cos(2a s) 2nd harmonic | 0.67249924 | −1.5e-6 |
| cos^p(a s), p=2,3,4 | 0.67249982 (p=2) | −8.9e-7 … −2.5e-4 |
| cos(a s) + c·sin(b s) parity-mixed (idea I5) | 0.67247067 (c=0.02) | −3.0e-5 |
| cos(a s + φ) phase-tilted | 0.67250070 @ φ=0 | only φ=0 reaches ceiling |
| exp(−k s²) Gaussian | 0.67249492 @ k=1.1 | −5.8e-6 |
| exp(−k s⁴) super-Gaussian | 0.67207364 | −4.3e-4 |
| 1−(2s)² parabola / tent | 0.54286 / −166764 | far below / degenerate |

**Reading (CONJECTURED):** 0.6725007 appears to be a **general even-window bound** for
this H functional (`H = 2 − 1/c`, `c = I0²/(I2+J)`), not a cosine artifact. Smooth
perturbations of the cosine — harmonics, parity mixing, phase, powers, Gaussian tails —
all *decrease* H or leave it unchanged at noise level. **Consequence:** idea I4's
"two-tone window raises H" version is **refuted at the numeric level**; raising H above
2/3 needs a qualitatively different numerator mechanism (e.g. changing the functional
itself — idea I9 territory), not a window tweak. This *raises* the relative value of the
coupling-breaking ideas (I1–I3) and the denominator-upgrade idea (I9), and *lowers*
I4/I5/I6's window-tweak branch.

---

## 5. Ten CONJECTURED ideas targeting the leverage point

Ranked by expected leverage × feasibility. All CONJECTURED until certified by
`verify_cos7.py` (the interval verifier).

### A. Break the eps–psum coupling (the negative feedback loop — now the top target)

**I1 — Coupling-breaker via smarter weights.** The 7-point mechanism uses uniform
weights `a_ij = 2/(n-(j-i))`. If a non-uniform weight profile certifies the *same* eps at
*smaller* psum (or larger eps at same psum), the coupling constant k drops below 1 and
the ridge shifts up. **Why it targets the leverage point:** the tax loop is the only
non-saturating loop; breaking its coupling frees both knobs at once. **Test:** weight
search over the simplex with the existing verifier (`verify_cos7.py` accepts a
`WEIGHTS_JSON` argument). Effort: medium. Expected: every 0.1 reduction in k buys
roughly +3e-4 to +5e-4 along the ridge (CONJECTURED, extrapolated from `coupled` k-table).

**I2 — Two-pressure certification (hybrid psum).** Certify the local floor eps on a
*sparse* grid (cheap) but evaluate the *tax* tau at a denser grid (expensive) only in a
bounded region. tau depends on psum only via `tau = psum(m-6)/m`; a certified *upper*
pressure on a subset of gaps may suffice, decoupling the two costs. **Test:** modify the
verifier to accept per-gap pressure. Effort: high.

**I3 — eps floor as a *function* of gap span, not a constant.** A single eps floors all
6 gaps; if the certified F_n bound holds with span-dependent eps_i, the effective floor
at the *binding* gap can be higher for the same total effort. Same cost, higher A → B →
denominator loop. **Test:** extend `verify_cos7.py` to span-dependent targets.
Effort: high.

### B. Raise the numerator — **downgraded this run** (window families fail to beat ceiling)

**I4 — Window with H above the cosine ceiling.** **NEW EVIDENCE (REFUTED at numeric
level):** two-tone, 2nd-harmonic, cos^p, parity-mixed, phase-tilted, Gaussian and
super-Gaussian families were all probed in Rust (§4); none exceeds 0.6725007031.
Only a *functional* change to H (not a window tweak) can lift the numerator. **Revise
to:** derive what functional form of `c = I0²/(I2+J)` maximizes H *given* the verifier's
kernel constraints (this is idea I9's numerator half). Effort: high, theory.

**I5 — Anti-symmetric / phase-tilted window.** **NEW EVIDENCE:** parity-mixed
`cos + c·sin` *decreases* H monotonically in c (−3.0e-5 at c=0.02); phase-tilted
windows collapse H by −5e-3 at φ=0.2. **Refuted** as an H-raiser. Keep only as a
mechanism to *shrink J* if a different integral definition (not the `|s−t|` kernel) is
ever used. Effort: low (already answered).

**I6 — Recover the free +0.000079 by alpha retune *with re-optimized eps*.** Still the
cheapest certified-record candidate: the 2D search over interpolated eps gives
`(1.42, 1/200, eps=0.00920, m=118) → 0.6736364 (+0.000373)` and `(1.40, 1/220,
eps=0.00842, m=128) → 0.6735736 (+0.000311)` (CHECKED NUMERICALLY, `frontier` /
`frontier_scan` — eps interpolated, NOT certified). **Idea:** certify the highest eps at
the H-peak alpha rather than at 1.49. Effort: low (existing verifier, one binary
search). Note: this is a *coupling-aware* play (eps is higher at looser pressure) —
it exploits loop 4's Pareto ridge rather than fighting it.

### C. Attack the tax term directly (linear loop)

**I7 — psum = 1/320 … 1/800 with certified eps.** At the record's *certified* eps
0.00806, purely lowering psum (m re-optimized): `1/320 → 0.674630 (+0.001368)`,
`1/600 → 0.676036 (+0.002773)`, `1/800 → 0.676438 (+0.003175)` (CHECKED NUMERICALLY,
`frontier` PSUM table — assuming the same eps stays certifiable, which coupling data
says is optimistic). Even at half the eps (`k=0.5` model) `1/600 → 0.674078 (+0.000815)`
still beats the record (`coupled` binary). **Test:** binary-search max certifiable eps at
(1.49, 1/320), (1.49, 1/400), (1.49, 1/600). Effort: low-medium, directly parallel to
wave-blast task `verify-eps`.

**I8 — Reduce the (m-6)/m factor via larger m with a *better* B-cap.** tau and B/m both
shrink as m grows, but B's sqrt regime caps the gain (m* is already 133–140). A tighter
Bellman/Phi bound (smaller B for the same A) shifts m* up and helps both tau↓ and
denominator↑. **Test:** numerical LP on the actual Bellman problem (Rust). Effort: high,
theory.

### D. Structural / higher-moment (leverage beyond the current formula)

**I9 — Second-moment denominator.** `||P+Q||_F^4` or `tr(P^k)` terms (wave-1
`task-moment.md`) would replace the `1 − B/m` amplifier with a higher-order correction.
Systems view: the denominator is currently a ×1.008 amplifier — nearly inert. A
higher-moment bound turning it into ×1.05+ would make every H and eps gain count ~50×
more. **Ceiling sanity:** `H=2/3, tau→0, amp×1.05 → 0.7018` vs record 0.6733
(CHECKED NUMERICALLY, `ceiling` CEILING table). **Re-ranked upward** after §4: since
the numerator is now shown to be structurally capped, this is the *only* route toward
0.68+. Effort: very high, pure theory.

**I10 — n-point generalization (n=9/11) with re-derived Phi.** More gaps per atom block
raises effective local information per certification (wave-blast `verify-ntone`).
Systems view: n↑ is a *structural* eps multiplier that avoids the concave B-cap of the
6-gap A (A = eps(n−6) with a different Phi). **Test:** generalize `verify_cos7.py`'s
capacity check and subdivision to q>6; sweep n in Rust first. Effort: high.

---

## 6. Theoretical ceiling of the family (CONJECTURED)

| configuration | bound |
|---------------|-------|
| record (cosine, H(1.49)) | 0.6732628655 | [RETIRED 2026-08-24]
| cosine H_max (alpha*=1.414) | 0.6733423 (+0.000079) |
| H = 2/3 ideal window, same tax/amp | 0.66746 (worse! H must beat 2/3 − tau) |
| H = 2/3, tau→0, amp ×1.05 | 0.7018 |

(CHECKED NUMERICALLY, `ceiling` binary.) **Conjecture:** the *current formula family*
(cosine window, 7-point, uniform weights, 6-gap floor) is essentially exhausted at
**~0.6736–0.6740** with best interpolated eps (2D search max 0.6736364) — the record is
within ~3.7e-4 of its own family's projected ceiling. Passing 0.68 requires either a
numerator functional change (§4 says no window tweak suffices), a structural denominator
upgrade (I9), or eps ~ 0.0217 (~2.7× the certified floor — CHECKED NUMERICALLY, `sens`
REQUIRED-eps table).

---

## 7. Effort recommendation (synthesis)

1. **Do I6 first** (certify H-peak alpha at maximal eps): cheapest, expected +3e-4 over
   record, existing tooling. Pairs with wave-blast `verify-eps`.
2. **Run I7's certification attempts** (1/320, 1/400, 1/600): quantifies the true
   coupling k for the record's eps — deciding whether the psum loop is actually free.
3. **Pursue I1 (weight simplex search)** — now the top structural lever, since §4 closed
   the window-tweak door. Cheap to *try*: the verifier already accepts WEIGHTS_JSON.
4. **Treat I9 as the long shot** that could change the game (denominator ×1.008 → ×1.05+).

---

## 8. Independent re-verification log (this run)

Re-ran every binary and cross-checked against high-precision mpmath on this host
(`/home/opc`; the spec's `/home/vstaln` paths are stale).

**Host/build note:** native binaries live in `target/release/` — the musl/x86_64
cross-target is built for CI, not for this host (`Exec format error` on this arch).

| claim | Rust output | mpmath (50 dps) | agree |
|-------|-------------|-----------------|-------|
| bound @ record | 0.673262865534356 | 0.67326286553435601465 | 16 digits | [RETIRED 2026-08-24]
| d(bnd)/dα | −0.002163 | −0.002162846875 | 11 sig |
| d(bnd)/deps | +0.642817 | +0.642816967439 | 11 sig |
| d(bnd)/dm | ~0 (−2.0e-8) | −1.9824e-8 | yes |
| d(bnd)/dpsum | −0.962293 | −0.962292945759 | 11 sig |
| d²(bnd)/deps² | (Rust not built) | **−38.3473** | new |
| d²(bnd)/dpsum² | (Rust not built) | **+2.67e-39** | new (linear!) |
| elast α/eps/m/psum | −0.00479/+0.00770/0/−0.00650 | −0.004787/+0.007696/−3.9e-6/−0.006497 | yes |
| H peak | 0.672500703092 @ 1.4140 | (quadrature reproduces to 12 digits) | yes |
| coupling k (α=1.40/1.49) | 0.911/0.833 | slope −0.911/−0.833 (ln-eps vs ln-pinv) | yes |
| window families vs ceiling | all ≤ 0.672500704 (8 families) | — | new negative result |

Scripts/commands (all CHECKED NUMERICALLY on this host):
- `cd /home/opc/riemann/tools/beat673/sens && cargo build --release` (native) and
  `RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl` (cross, builds clean)
- `./target/release/sens` — record + derivatives + decomposition + sweeps + required-eps
- `./target/release/frontier` — H peak 0.672500703092 @ 1.4140, frontier table, eps marginal gain
- `./target/release/coupled` — coupling models k=0/0.25/0.5/1
- `./target/release/ceiling` — coupling fits k=0.911/0.833/0.819, ceilings
- `./target/release/final` — Pareto ridge, dB/deps validation 126.008282, effort leverage, 2D search
- `./target/release/probe`, `frontier_scan` — candidate point m-optimization, 2D frontier scan
- `./target/release/twotone` — **new**: two-tone window H exploration (≤ ceiling)
- `./target/release/window_max` — **new**: cos^p / parity-mixed / phase-tilted (≤ ceiling)
- `./target/release/extra_families` — **new**: Gaussian / super-Gaussian / parabola / tent (≤ ceiling)
- `uv run --with mpmath python3 final_leader.py` — ground-truth certified bound (120 dps)
- `uv run --with mpmath python3 - <<EOF … EOF` — independent derivatives + curvature + k-fit + ridge (50 dps; command body in §2/§3/§8)

All report numbers reproduced. No fabrication. Carried caveats (honesty):
- eps values beyond the certified floor are **interpolated, not certified** — every
  "+beats record" claim requires a `verify_cos7.py` run before it counts.
- The interpolated eps table *under*-reports the certified eps at the anchor
  `(1.49,220): 0.0079772 vs certified 0.00806` — interpolated-based candidates are
  conservative at the anchor, uncertain elsewhere.
- The Pareto-ridge numbers are **model-dependent** (anchored-at-record vs interpolated
  eps give different absolute values; direction agrees).
- Window-family negative results are quadrature-level (order-24 Gauss-Legendre,
  validated to 12 digits against the certified lib) — CONJECTURED until an analytic
  derivation/certification, but the margin (all ≤ ceiling to ≤1e-6, best "gain" +5.8e-10)
  makes a false negative unlikely.

---

RESULT: COMPLETED — Systems map + Rust sensitivity analysis (record reproduced to 16
digits, all partials & curvatures cross-checked vs mpmath) identify the psum tax as the
highest-leverage but most-coupled parameter; new window-family probes (8 families) show
the H-ceiling 0.6725007 is robust, refuting the two-tone window idea and re-ranking
coupling-breaking (I1–I3) and denominator-upgrade (I9) ideas as the real levers; 10
CONJECTURED ideas delivered with commands.
