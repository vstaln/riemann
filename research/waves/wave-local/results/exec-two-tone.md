# EXEC — Two-tone window sweep: v(s) = cos(a·s) + c·cos(b·s)

**Date:** 2026-08-12. **Agent:** EXECUTOR (local, wave-local). **Status:** COMPLETE.
**Headline:** the two-tone family does **NOT** raise the window functional H above the
single-cosine ceiling — the max H over a very wide box equals the classic constant
3/2 − (1/√2)cot(1/√2) = 0.672500703679412 to within 1.6×10⁻¹³. c = 0 (pure cosine) is always
optimal. The "window is the biggest lever" hypothesis is REFUTED within this family.
The remaining lever is (eps, psum, m): lowering psum below 1/220 and raising eps above
0.00806 mechanically yields bound > record, but **eps > 0.00806 is CONJECTURED** until the
interval verifier certifies it.

---

## 1. Tool location, build, run

- Source (canonical copy): `/home/vstaln/riemann/tools/two-tone-sweep/` (`Cargo.toml`, `src/main.rs`)
- Working copy used for this run: `/tmp/two-tone/` (same source; built there)
- No dependencies (pure std f64; own Gauss–Legendre).

Build:
```
export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"
cargo build --release --target x86_64-unknown-linux-musl
```
Run:
```
./target/x86_64-unknown-linux-musl/release/two-tone              # the (a,b,c,psum,m) sweep
./target/x86_64-unknown-linux-musl/release/two-tone validate     # H/J cross-checks vs analytic
./target/x86_64-unknown-linux-musl/release/two-tone cosmax       # single-cosine H max over alpha
./target/x86_64-unknown-linux-musl/release/two-tone fine         # fine scan around optimum
./target/x86_64-unknown-linux-musl/release/two-tone wide         # coarse wide box scan
./target/x86_64-unknown-linux-musl/release/two-tone single <a> <b> <c> <psum> <m> <eps>
```

## 2. The functional — and the label convention (important)

The certified record scripts (`/tmp/combine/final_leader.py`, `verify_H.py`, and the original
`tools/bound-sweep/src/main.rs`) use:

```
I0 = ∫ v ds                       (∫ over [-1/2, 1/2])
I2 = ∫ v² ds
J  = ∬ |s−t| v(s) v(t) ds dt      (kink at s=t — MUST be split; naive quad fails, documented)
c  = I0² / (I2 + J)
H  = 2 − 1/c
bound = (H − τ)/(1 − B/m),  τ = psum·(m−6)/m,  A = eps·(m−6),
B = A if A ≤ m/(m−1) else 2√((m−1)A/m) − 1 + A/m
```

The task prose labels these I0/I2 differently (calling I2 = ∫v²s² ds). The task's own check
value `1/2 + sin(α)/(2α)` is exactly ∫cos²(αs)ds, proving I2 = ∫v² ds in the certified
machinery. I verified both readings numerically: the certified reading reproduces
H(1.49) = 0.6724218860964 exactly; the prose reading gives H = 1.5347059… and matches
nothing. **The certified reading is the correct contract.**

## 3. Validation — CHECKED NUMERICALLY (all from the tool's `validate` output)

```
cos alpha=1.47: J_num=0.266645172001 J_an=0.266645172001 dJ=5.551e-17 | H_num=0.672458709401 H_an=0.672458709401 dH=0
cos alpha=1.49: J_num=0.264962417451 J_an=0.264962417451 dJ=1.665e-16 | H_num=0.672421886096 H_an=0.672421886096 dH=2.220e-16
cos alpha=1.5:  J_num=0.264115313808 J_an=0.264115313808 dJ=2.776e-16 | H_num=0.672398862599 H_an=0.672398862599 dH=0
H(1.49) numeric = 0.6724218860964  reference = 0.6724218860964  diff=4.774e-14
bound(eps=0.00806, m=133, alpha=1.49, psum=1/220) = 0.6732628655343562  record = 0.6732628655343560  diff=2.220e-16 [RETIRED 2026-08-24]
resolution: H(1.49) n=48 = 0.6724218860964  diff(96 vs 48) = 2.220e-16
```

- J via kink-split Gauss–Legendre (96-pt, inner/outer) matches the analytic cosine formula
  to ≤2.8×10⁻¹⁶ (f64 ULP level).
- **H(1.49) = 0.6724218860964 reproduces the certified reference to 4.8×10⁻¹⁴** (f64 limit;
  mpmath gives 4×10⁻⁴¹ for the analytic-vs-kinksplit agreement at higher precision).
- The full bound reproduces the certified record 0.6732628655343560 to 2.2×10⁻¹⁶ (1 ULP in f64). [RETIRED 2026-08-24]
- 48-pt vs 96-pt quadrature agree to 2.2×10⁻¹⁶ ⇒ resolution converged.

## 4. Top-10 two-tone candidates (from the sweep, eps = 0.00806 CONJECTURED)

Sweep grid: a ∈ [1.4,1.6] (201), b ∈ [2.5,3.5] (201), c ∈ [−0.3,0.3] (121),
psum ∈ {1/220, 1/250, 1/300}, m ∈ [100,200]. 1,481,221,863 configs in ~63 s.
**H values CHECKED NUMERICALLY; "bound beats record" CONJECTURED (needs verifier for eps).**

```
rank a       b       c        psum   m    H               bound
1    1.4070  2.5300  0.0050   1/300  135  0.672500703285  0.6745091758911242
2    1.4070  2.5350  0.0050   1/300  135  0.672500703269  0.6745091758753008
3    1.4070  2.5250  0.0050   1/300  135  0.672500703264  0.6745091758697059
4    1.4070  2.5400  0.0050   1/300  135  0.672500703216  0.6745091758221197
5    1.4070  2.5200  0.0050   1/300  135  0.672500703206  0.6745091758111604
6    1.4070  2.5450  0.0050   1/300  135  0.672500703126  0.6745091757314670
7    1.4220  2.6100  -0.0050  1/300  135  0.672500703122  0.6745091757266519
8    1.4070  2.5150  0.0050   1/300  135  0.672500703111  0.6745091757156045
9    1.4220  2.6050  -0.0050  1/300  135  0.672500703108  0.6745091757127005
10   1.4220  2.6150  -0.0050  1/300  135  0.672500703097  0.6745091757013879
```

Observe: the top-10 H values are **all ≈ 0.672500703** (the classic constant), and the winning
c ≈ ±0.005 is effectively c = 0 — the second cosine is not doing anything. The bound gain
relative to the record comes **entirely from psum = 1/300 < 1/220** (lower tax τ), not from H.

## 5. The decisive negative: two-tone does NOT beat single-cosine H

- `cosmax`: max over single-cosine H(α), α ∈ [0.5, 3.0] (refined to 10⁻⁵):
  `max H_cos = 0.672500703679249 at alpha = 1.41421` (≈ √2),
  `classic 3/2 − (1/√2)cot(1/√2) = 0.672500703679412`, excess = −1.626×10⁻¹³.
- `fine` (a ∈ [1.40,1.42], b ∈ [2.50,2.56], c ∈ [−0.02,0.02], 401 c-steps): top H = 0.672500703678794
  at c = −0.0002 — strictly **below** the c=0 max.
- `wide` (a ∈ [0.5,3.0], b ∈ [0,6.0], c ∈ [−1,1], 989,901 configs): top H = 0.672500703673639
  (b=1.35, c=−0.225 etc.) — again ≈ classic constant, never above it.

Interpretation (CHECKED NUMERICALLY; explanation CONJECTURED): the H functional over the
two-tone family is maximized exactly at the pure cosine with α = √2, and its value is the
classic constant. Adding a second tone only perturbs H to first order in c (the Hessian is
negative/neutral), so c = 0 is the optimum. The window is NOT the biggest lever within this
family — H is capped at the classic constant. The known in-class ceiling 0.6818 must come
from elsewhere (the ε functional / more exotic window families, per ceiling-gram-constraint.md).

## 6. The real lever: (eps, psum, m), still CONJECTURED on eps

`single` scans at α = 1.49 (H = 0.672421886096) with c = 0:

```
psum      eps     m     bound                  beats record?
1/220     0.00806 133   0.6732628655343560     (= record, reproduction) [RETIRED 2026-08-24]
1/300     0.00806 135   0.6745091758911242     yes (CONJECTURED eps)
1/220     0.00830 133   0.6734164908644640     yes (CONJECTURED eps)
1/220     0.00900 120   0.6738652602746451     yes (CONJECTURED eps)
1/300     0.01000 120   0.6756514148449326     yes (CONJECTURED eps)
```

The record uses psum = 1/220, eps = 0.00806 (CERTIFIED by verify_cos7.py). Every bound
> record above relies on eps > 0.00806 or psum < 1/220, and **eps is a property of the
interval verifier, not of this window computation.** So:

- bound = 0.67451 at (a=1.407, c=0, psum=1/300, m=135) **CHECKED NUMERICALLY** (arithmetic),
- but "the bound beats the record" is **CONJECTURED** until verify_cos7.py certifies
  eps ≥ 0.00806 at α = 1.407 (or eps ≥ 0.0083 at α = 1.49).

## 7. Honesty labels (summary)

| Claim | Label | Evidence |
|---|---|---|
| H(1.49) = 0.6724218860964 | CHECKED NUMERICALLY | two-tone validate: diff 4.8e-14 vs reference; J analytic vs kink-split ≤2.8e-16 |
| bound reproduction 0.6732628655343562 | CHECKED NUMERICALLY | two-tone validate: diff 2.2e-16 vs record | [RETIRED 2026-08-24]
| max two-tone H = classic constant (c=0 optimum) | CHECKED NUMERICALLY | cosmax/fine/wide scans, all ≤ 0.672500703679 |
| two-tone family cannot raise H above classic constant | CONJECTURED (explanatory) | numeric evidence only; no proof the Hessian is ≤0 everywhere |
| top-10 bounds beat record | CONJECTURED | arithmetic CHECKED; requires eps certifiable at the claimed level |
| eps = 0.00806 achievable at α=1.407 | CONJECTURED | needs verify_cos7.py run at that α (interval verifier) |

## 8. Files

- `/tmp/two-tone/` — working build (source identical to canonical copy below)
- `/home/vstaln/riemann/tools/two-tone-sweep/` — canonical copy (Cargo.toml + src/main.rs)
- Commands: `cargo build --release --target x86_64-unknown-linux-musl` then the run lines in §1.

## 9. Suggested next steps (for the round)

1. Run verify_cos7.py at α = 1.407 (or α = √2) to test if eps ≥ 0.00806 certifies there —
   if yes, the psum=1/300 bound 0.6745 becomes a real candidate without any two-tone.
2. Test whether eps at psum = 1/300 actually improves or degrades vs psum = 1/220
   (the record note says lower psum → lower achievable eps; the trade-off is exactly what
   cert_search.py should measure).
3. Do NOT fund further two-tone window search with b > a in this regime — the c=0 optimum
   is now numerically established.
