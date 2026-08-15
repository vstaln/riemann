# Fix: broken math cores in tools/barrier_zoo_rs (rung-0 RH-false zoo)

Date: 2026-08-17. Agent: builder (deepseek-v4-flash, background).
Edits: ONLY `tools/barrier_zoo_rs/src/main.rs` (8 root-cause edits + 2 array-size/compile fixes).
Python in tools/barrier_zoo/ used for formulas only; fresh Rust written.
Build: `cargo build --release --target x86_64-unknown-linux-musl` (clean, 1 warning pre-existing).

## Root causes (all found by reading code + hand-derivation, then fixed)

| # | symptom (before) | root cause | fix |
|---|---|---|---|
| 1 | Gamma(2)=1.505, Gamma(5)=32.40 | Lanczos `t = z+g`; must be `z+g+1/2` (t = s+g−1/2 = s+6.5) | `t = z + (g+0.5)` |
| 2 | eps = −13.877+66.587i (\|eps\|=68) | `C::exp` angle put in **re** slot: `C::new(2πa/5,0).exp()` = e^{2πa/5} real, not e^{i2πa/5} | `C::new(0.0, 2πa/5).exp()` |
| 3 | FE ratios \|·\|≈0.525=5^{−0.4} | `l_dirichlet` multiplied by 5^{+s}; correct is q^{−s}=5^{−s} (Python `L_dirichlet` = q^-s·Σχ(a)ζ(s,a/q)) | `cpow_pos(5.0, s.scale(-1.0))` |
| 4 | DH search finds 0 off-line zeros | grid ds=0.05,dt=0.5,rel=0.3 **provably** cannot resolve zeros at t=85.7/114.16: near a simple zero \|f\|≈\|f'\|·d, local-min ratio d_min/d_nb ≈ 0.74–0.99 > 0.3 regardless of \|f'\| | fine grid ds=0.01, dt=0.05, rel=0.9 (ratios 0.19/0.83) |
| 5 | epstein modularity rel 0.59–0.91; continuation off 3e3–1e6 | `theta_q` excluded origin (`v>0` test) → returned Θ−1, but the Poisson identity and the I(s) integrand need FULL Θ (integrand already subtracts 1.0, so it got Θ−2) | `v >= 0.0` (origin term exp(0)=1) |
| 6 | Dedekind false | same theta_q bug (5) AND the inline `l_chi20` had the same 20^{+s} vs 20^{−s} bug as (3) | `cpow_pos(20.0, s.scale(-1.0))` |
| 7 | \|Z(s0)\|=0.89 at planted zero | Z used `2^{+s}`; task formula is `Z(s)=ζ(s)(1+c·2^{−s})` (2^{−s0}=−1/c at s0=½+δ+iπ/ln2) | `cpow_pos(2.0, s.scale(-1.0))` |
| 8 | classifier 7/10 (not 9/10 as briefed) | (a) tautology pattern missing "trivial, on the critical line, or off"; (b) **regex-engine bug**: `(s)` in pattern parsed as regex-group, the literal `)` consumed, so "re(s)=1/2" text never matched (item 9 → unknown); (c) no unit-circle RH-conclusion pattern (item 7 → unknown) | +2 tautology patterns; escape parens `re\\(s\\)` in 2 RH patterns; +"all roots on the unit circle" |
| 9 | weil genuine roots \|x\|=2.85 | same `C::exp` bug as (2) | `C::new(0.0, 2πk/6).exp()` (freebie; not in acceptance) |

## BEFORE vs AFTER (same binary, `all` subcommand)

| check | before | after |
|---|---|---|
| Gamma(2), Gamma(5) | 1.5054, 32.3955 | **1.0000000000, 24.0000000000** |
| eps(psi) | −13.877+66.587i, \|·\|=68.0 | **0.850651+0.525731i, \|·\|=1.000000** |
| FE sign +1 / −1 | false / false | **true / true** (ratios 1.000000±0 / −1.000000±0 at t=0.3,1.7,5.1,12.7) |
| \|f_plus\| at certified zeros | 6.415e2, 2.320e2 | **3.144e-14, 3.263e-14** |
| DH off-line zero search | 0 | **6 off-line** (4 in f_plus: 0.8085/85.699, 0.1915/85.699, 0.3492/114.163, 0.6508/114.163; 2 in f_minus at t=77.35); **certified matched 2/2** |
| epstein modularity rel | 0.59 / 0.78 / 0.91 | **1.3e-15 / 2.2e-16 / 2.2e-13** |
| direct-sum anchors | rel 3.3e3, 1.1e6 | **1.3e-7, 3.1e-10** |
| Dedekind identity | false | **true** (rel 5.6e-11, 6.6e-11, 7.3e-10) |
| epstein FE (self-dual) | false | **true** |
| \|Z(s0)\|, second planted | 8.898e-1, 5.139e-1 | **2.334e-16, 1.520e-16** |
| classifier | 7/10 | **10/10** |

## Final binary output block (real run, acceptance lines)

```
  zeta(2,1) = 1.644934066848 vs pi^2/6 = 1.644934066848  (rel 1.3e-16)   [unchanged, pass]
  |zeta(0.5+14.134725i)| = 9.093e-15                                    [unchanged, pass]
  Gamma(2) = 1.0000000000 (expect 1) ;  Gamma(5) = 24.0000000000 (expect 24)
  eps(psi) = 0.850651 + i*0.525731   (|eps| = 1.000000)
  FE sign +1 (c=+eps): true ;  FE sign -1 (c=-eps): true
  s = 0.808517182 + i*85.699348485   |f_plus| = 3.144e-14
  s = 0.650830081 + i*114.163342731   |f_plus| = 3.263e-14
[f_plus] zeros located: 55, off-line: 4   [f_minus] zeros located: 32, off-line: 2
  certified zeros matched by search: 2/2
  modularity rel diff 1.3e-15 / 2.2e-16 / 2.2e-13  (< 1e-3)
  direct sum zeta(2;Q1)=2.502421907  continuation=2.502422241  rel 1.3e-7
  direct sum zeta(3;Q2)=0.421838542  continuation=0.421838542  rel 3.1e-10
  Dedekind identity: true ;  functional equation check: true
  |Z(s0)| = 2.334e-16 ;  |Z(0.3+2.7i)| = 0.646933 ;  |Z(s0+i*2pi/log2)| = 1.520e-16
  classifier agreement: 10/10
```

## Labels
- **core (Gamma/hurwitz): PROVEN** — Γ(2)=1, Γ(5)=24 exact; zeta self-tests untouched & passing.
- **model_dh: PROVEN** — FE +1/−1 exact, |f_plus|<1e-9 at both certified zeros (3e-14), search finds 6 off-line zeros, certified 2/2.
- **model_epstein: PROVEN for acceptance (modularity < 1e-3, Dedekind true, FE true, direct-sum anchors 1e-7)**. NOTE/INCOMPLETE: its off-line-zero search (t_hi=40, dt=0.5, rel 0.3) still finds 0 — the SAME grid-resolution limitation as DH had pre-fix, and a fine grid is ~1000× too slow because each zeta_epstein eval is an O(50k)-term Simpson theta integral. The pre-existing VERDICT text ("numerically verified here") therefore overclaims for the zero search; the DH-1936 off-line zeros for disc −20 remain undemonstrated in the Rust port. Follow-up: fast I(s) evaluator + fine grid (as done for DH).
- **model_beurling: PROVEN** — |Z(s0)|=2.3e-16 < 1e-6 at planted zero, second planted zero 1.5e-16, generic point nonzero.
- **classifier: PROVEN 10/10** — note: actual pre-fix state was 7/10 (brief said 9/10); item 9 failed from a regex-engine paren-as-group bug, item 7 from a missing unit-circle RH pattern; both fixed plus the item-5 tautology.

## Handouts
- Runtime of `all` dominated by the DH fine grid (~252k pts × 8 hurwitz × 2 searches) and the epstein theta grid; ~10–30 s on this box. `barrier_zoo_rs [dh|weil|epstein|beurling|classify|all]` unchanged.
- No new dependencies; zero external crates preserved.
