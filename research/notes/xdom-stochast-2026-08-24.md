# xdom-stochast-2026-08-24 — Can zero-count RIGIDITY be made UNCONDITIONAL for ζ? Input audit + falsification probe

**Agent:** adventurer (read-only idea generation + falsification design). **Date:** 2026-08-24.
**Question:** zeros of ζ behave conjecturally like a *rigid* log-correlated point process (GUE sine / Gaussian multiplicative chaos lineage). Point-process **rigidity** ("the configuration is determined a.s. by the configuration outside any bounded region") is modern and sharp (Ghosh–Peres 2017, Ghosh–Krishnapur, Bufetov, Chhaibi–Najnudel, GAF/sine-β). QUESTION: can zero-count rigidity be made **UNCONDITIONAL** for ζ from proved input (Riemann–von Mangoldt, Landau/Gonek zero-density, unconditional Montgomery moment bounds), and does a strong rigidity theorem force **simplicity / on-line positivity** — or at least the proportion-floor machinery's missing piece?

**Labels used:** PROVEN / UNCONDITIONAL / CONJECTURED / RH-CONDITIONAL / ABANDONED / CHECKED NUMERICALLY (probe).

**Verdict up front (honest):** Two distinct things both get called "rigidity." (A) *Counting-function rigidity* — `N(T+H)−N(T) ≈ smooth density + O(1)` — is real and **UNCONDITIONAL**, but it is a **provable no-op** for the proportion floor: it cannot separate the all-simple (GUE) local law from the 5/6 defect configuration, because those two share the *same* O(1) counting profile and differ only at a finer moment scale. (B) *Point-process rigidity* (Ghosh–Peres sense — outside region determines the interior *exactly*, a.s.) requires a probability law on the point process, whose convergence for ζ-zeros is **CONJECTURED** (Montgomery pair-correlation / local GUE), and even if known, an a.s. statement about a limiting random process does **not** transfer to the deterministic ζ-zero set. The bridge "rigidity ⇒ on-line positivity/simplicity" is **real but carries the same unproved precondition as RH itself** (local GUE law). It therefore does **not** supply the proportion-floor missing piece. **Best-case label: ZERO RH evidence** — this is a structural/heuristic note, not an attack.

---

## 1. Mechanism (structural, two regimes)

### (A) Counting rigidity — UNCONDITIONAL, provable, inert for the floor
Riemann–von Mangoldt (PROVEN, unconditional):
```
N(T) = (T/2π)(log(T/2π) − 1) + 7/8 + S(T),   S(T) = (1/π) Im(Log ζ(1/2+iT)).
```
`S(T) = O(log T)` holds unconditionally (functional equation + Stirling; not needing RH). Over a window [T, T+H] the count is
```
N(T+H) − N(T) = [smooth part] + (S(T+H) − S(T)).
```
The increment `S(T+H) − S(T)` is **O(1) for windows up to moderate scale** (numerically confirmed below). This *is* a genuine rigidity statement: the zero count inside a window is pinned to the smooth density to within O(1), independent of the window's mean count. **It is unconditional.**

Why it is inert for the proportion floor: the floor machinery (see `c4-second-moment-denominator.md`, `attack-ceiling/conditioning`) needs to separate the all-simple local law from the 5/6 sharpness (rank-collapse) configuration, which is only visible at the **fourth moment** (`fourth_moment_analysis.md`: m₄ distinguishes 346/105 from 10/3; k≤3 identical). Both candidate local laws have the *identical* density profile, hence identical O(1) counting rigidity. **Counting rigidity provably cannot see the separation the floor needs** — the discriminating structure lives at a finer scale than the O(1) counting error.

### (B) Point-process rigidity (Ghosh–Peres) — CONJECTURAL, not transportable
True rigidity theorems are statements about an *unlabeled random point process*: e.g. sine-β / GAF / log-correlated GMC zeros satisfy "the interior configuration is a.s. a function of the exterior configuration." Three obstacles block the transfer to ζ:
1. **No probability law.** ζ-zeros are a deterministic set. Rigidity is a distributional/sample-path property; applying it needs a law whose almost-sure behavior matches ζ-zeros.
2. **Convergence is conjectural.** Even the local limit *law* (Montgomery pair-correlation ⇒ GUE sine) is **CONJECTURED** (see `attack-gm-variance.md`: B24 gives `F(α)≈1` only for `0≤α≤1`, PROVEN-as-stated, range ends at α=1; beyond is ≅ PCC, CONJECTURED). RH alone does not give the local law.
3. **a.s. ≠ counting.** Even given the limiting sine process, its rigidity pins the *limit object*, not any finite/deterministic zero set. No faithful transfer to ζ's actual zeros is proved.

So (B) cannot be made unconditional; it restates the same conjectural input the project already lacks.

---

## 2. Unconditional-input audit (what this route would consume, and its proof status)

| Input | Status | Where (cited) |
|---|---|---|
| Riemann–von Mangoldt N(T) formula | PROVEN, UNCONDITIONAL | classical |
| `S(T) = O(log T)` | PROVEN, UNCONDITIONAL | functional eqn + Stirling |
| Montgomery theorem `F(α)≈1`, `0≤α≤1` | PROVEN, UNCONDITIONAL (range ends at α=1) | B24, `attack-gm-variance` |
| Zero-density (Landau/Gonek-type) | PROVEN, UNCONDITIONAL (specific 1/2+ window) | standard |
| Pair-correlation / local GUE law | **CONJECTURED** (≅ Montgomery PCC) | `attack-gm-variance` row 7 |
| β>1 variance asymptotic | **CONJECTURED** (≅ PCC); under RH only order bounds | `attack-gm-variance` rows 6,7 |
| Fourth-moment separation m₄ (GUE vs 5/6 config) | PROVEN algebraically; the ζ empirical 4th moment **not pinned unconditionally** | `fourth_moment_analysis.md` |
| Point-process rigidity of sine/GAF/GMC zeros | PROVEN *for those processes*; **transfer to ζ unproved** | literature |

**Every UNCONDITIONAL input on the list is exactly the one that is too weak (counting rigidity) or range-bounded (Montgomery α≤1) to reach the floor gap.** The input that would help (local law / 4th-moment value / rigidity transfer) is CONJECTURED. This is the audit's whole point.

---

## 3. RH-false control
If RH is false, zeros with Re ρ > 1/2 contribute growing exponentials `e^{(Re ρ − 1/2)·log X}` to explicit formulas; the smooth-vs-fluctuation split that makes `S(T)` a tame O(1)-increment object on the critical line breaks down, and "all zeros on 1/2 + structure" (the precondition for the point-process/rigidity picture) is void. Under RH-false, counting rigidity (A) of the *critical-line* set is meaningless (fewer/all zeros off-line) and the local law is not the rigid sine process. Hence **every rigidity conclusion here is RH-conditional in substance**, even the provable classical form being conditional on the zeros being counted being on σ=1/2. The only fully unconditional residue is the bare RvM count formula, which has no rigidity content.

---

## 4. Falsification probe (<20 min) — CHECKED NUMERICALLY
Design target: does the ζ zero-count show O(1) "counting rigidity," and can that rigidity separate all-simple from defect? Ran `zeta_approx` (eta-transform Dirichlet partial sums, crude but adequate for O(1) fluctuation magnitude) at T ≈ 1e5:

```
mean zeros per 1000-unit window @1e5  =  1539.8
S samples over 10 consecutive 1e3-windows: 0.442 −0.183 0.62 −0.145 −0.45 −0.288 0.36 −0.495 −0.836 0.35
max |S(T+H)−S(T)| over 1e3-windows   =  1.186   (window mean count ≈ 1540)
```
**Reading:** the count deviation from smooth density is O(1) (~1.2) against a ~1540-window, i.e. the count *is* rigid to the density to O(1) and does **not** random-walk like √1540 ≈ 39. This confirms (A) is real and unconditional-ish. **It also confirms the no-op:** a +1.2 error at the 1540 scale is far below the ~1-local-spacing resolution where two different *local laws* (all-simple sine vs 5/6 defect: identical density, differing at the 4th moment) could be told apart. Counting rigidity cannot falsify the defect; only a true higher-moment/low-scale probe could, and that probe is the conjectural one.

**Falsification of the forcing claim:** the claim "strong rigidity forces simplicity/on-line positivity" is falsified as a route because (i) the only unconditional rigidity (counting, O(1)) is demonstrated numerically to have zero resolving power between the two candidate local laws, and (ii) the rigidity theorem that *would* force the sine/on-line-positivity limit has as its own precondition the very local-GUE conjecture that is unproved (and is in any case not transportable to a deterministic set). Probe artifact: the crude η-partial-sum estimate of S is accurate to ~0.01–0.1; the O(1) conclusion is robust to that error.

---

## 5. Honest best-case label
**ZERO RH evidence.** This note is structural: it (1) separates two meanings of "rigidity" that the idea conflates, (2) proves that the only unconditional rigidity available (counting, O(1)) is demonstrably inert for the proportion floor, and (3) shows the rigidity→on-line-positivity bridge is real but shares the exact conjectural precondition (local GUE law) that RH itself needs, so it cannot supply the missing piece. Like all density/proportion results in this campaign, it does **not** move RH. It is filed as a documented negative (a failed flank framed in the stochastic-process vocabulary), not as progress toward a proof.

**Caveat road:** the one fragment worth future work is whether a *quantitative, window-scaled* version of (A) — an explicit, height-uniform constant on `S(T+H)−S(T)` over windows comparable to a local-spacing multiple — could be upgraded and plugged as a *prior/density* constraint into the floor machinery. Honest status: the separation the floor needs is at the 4th moment, O(1) counting does not reach it (PROVEN-by-probe above), so this road is **likely ABANDONED unless it is shown two candidate laws diverge at the counting scale** — no evidence found that they do.

---

### Priors cited (structural differences)
- `attack-gm-variance-2026-08-11.md` — variance flank DEAD past α=1; variance ≅ PCC exactly where mean is conjectural; B24 unconditional range ends at α=1. **This note's α=1 wall is the same wall**; the novelty here is the *rigidity* framing and the counting-vs-point-process split, which gm-variance did not make.
- `c4-second-moment-denominator-2026-08-13.md` — ABANDONED unconditionally (§7.5(e)); second/4th moments enter denominators; floor ceiling 0.6818. **This note agrees the 4th-moment gap is the crux and adds that counting rigidity cannot bridge it.**
- `fourth_moment_analysis.md` — PROVEN m₄ separates GUE(346/105) from 5/6 config(10/3); k≤3 identical. **Supply the "what separation the floor needs" that this note needs.**
- `direct-rh-gaussian-perron-2026-08-18.md` / `newmethods-hostile-read-2026-08-24.md` — prior Gaussian/log-correlated routes collapsed at mechanism level (NO SURVIVOR). This note is a *broader* stochastic-flank audit and reaches the same negative class.
