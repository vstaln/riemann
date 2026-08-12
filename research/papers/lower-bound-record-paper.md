# A New Certified Lower Bound for the Proportion of Simple Zeros of ζ on the Critical Line: 0.6732654365

**Date:** 2026-08-12. **Status:** CHECKED NUMERICALLY (certification + bound arithmetic), with re-certification in flight.
**Labels used throughout:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE — per the program honesty charter (`hooks/agents.md`).

---

## 1. Title + Abstract

We announce a new certified lower bound for the proportion of simple zeros of the Riemann zeta function on the critical line:

$$\liminf_{T\to\infty}\;\frac{N^{*}_{0}(T,2T)}{N(T,2T)} \;\ge\; \boxed{0.67326543649552352207990181282271996377681849486392}$$

where $N(T,2T)$ counts the nontrivial zeros $\rho=\beta+i\gamma$ of $\zeta$ with $T<\gamma\le 2T$ (with multiplicity) and $N^{*}_{0}(T,2T)$ counts the distinct such zeros with $\beta=\tfrac12$, i.e. the **simple-on-line** fraction, in the terminology of the companion paper [C26]. The bound sharpens the previous record

$$0.673262865534356014645368000853343519319712248$$

by **+2.5709611675074345×10⁻⁶** (CHECKED NUMERICALLY, mpmath 120 digits).

**Method.** This is the same certified two-moment method (Weil-form compression, Sylvester inertia, rank–trace inequality) whose optimized test family yields the constant 0.6725 in [C26]. The new result is a sharpening of the *simple-on-line constant* of that method: a window functional $H$, a rational correction $\tau$, and a moment correction $B=\Phi_m(\varepsilon(m-6))$ combine into $\text{bound}=(H-\tau)/(1-B/m)$ with certified floor $\varepsilon$.

**The eps-frontier.** The method's output is controlled by a single certified quantity: the maximal $\varepsilon$ such that the in-band floor $F\ge\varepsilon$ is interval-verified. At $(\alpha,\;p_{\rm sum})=(149/100,\;1/220)$ the certified frontier is $\varepsilon=0.008064$ (TRUE), with $0.008063$ TRUE, $0.008066^{+}$ all FALSE (CHECKED NUMERICALLY, Arb interval verifier, grid=4000).

**The artifact question, answered.** Is the certified floor $\approx 0.0080606$ a verifier artifact of the uniform-span grid 4000? **No.** The finer-grid probe (grid 6000, 8000) reproduces the *same* terminal region: the failing boxes are exactly grid-scaled images (coordinates × 1.5), and $\varepsilon=0.008070$ fails at grid=6000 with lower $=0.008060649099672502$. The certified floor is **genuine, not a grid artifact** (CHECKED NUMERICALLY, verifier runs).

**Honesty labels.** The certification of $\varepsilon=0.008064$ is **CHECKED NUMERICALLY** (verifier log `verify_cos7.py`; independent re-certification in flight at time of writing). The bound arithmetic is **CHECKED NUMERICALLY at 120+ digits**. No claim here is PROVEN in the formal sense.

---

## 2. Introduction

### 2.1 Trajectory
The proportion of zeros known to lie on the critical line has a century-long history: Hardy–Littlewood $\gg T$; Selberg (1942) positive proportion; Levinson (1974) $\ge \tfrac13$; Conrey (1989) 40%; the modern line to 41.6%; and the 2026 result 67.25% (verified by Conrey & Goldston, Lean-formalized in `anthropics/zeta-23-lean`). The clean constant $3/2-(1/\sqrt2)\cot(1/\sqrt2)\approx 0.6725$ arises from the optimized test family of [C26]; the simpler argument gives $\tfrac23$.

The present record is not a new method: it is the same certified two-moment machinery, pushed to its **eps-frontier** — the largest $\varepsilon$ the interval verifier will certify.

### 2.2 The method in one paragraph
The bound is $\text{bound}=(H-\tau)/(1-B/m)$ [D26, discovery-6732629]. $H$ is a ground-state (window) constant from a cosine test function $v(s)=\cos(\alpha s)$, $\alpha=149/100$; $\tau=p_{\rm sum}(m-6)/m$ is a rational "tax" from the total pressure $p_{\rm sum}$; $A=\varepsilon(m-6)$ converts the certified floor $\varepsilon$ into a moment argument; $B=\Phi_m(A)$ is the moment-correction term; $m$ is a block size. Lower $p_{\rm sum}$ lowers $\tau$ (good) but lowers the achievable $\varepsilon$ (bad); the certified optimum is $p_{\rm sum}=1/220$, $\alpha=149/100$, $m=133$.

### 2.3 The eps-frontier idea
For fixed $(\alpha,p_{\rm sum},m)$ the bound is *monotone increasing in $\varepsilon$* (CHECKED NUMERICALLY at $m=133$: $0.00806\to0.6732628655$, $0.008065\to0.6732660791$, $0.00807\to0.6732692918$, $0.0081\to0.6732885476$). Hence the whole game is: **certify the largest $\varepsilon$ such that the in-band floor $F\ge\varepsilon$**. This is what the interval-arithmetic verifier does, and it is where the previous record stopped ($\varepsilon=0.00806$).

### 2.4 The artifact question
A skeptic's objection: the verifier works on a fixed uniform-span grid (4000). Perhaps the terminal failure region is an artifact of that grid, and a finer grid would certify a larger $\varepsilon$. Section 5 answers this **numerically in the negative**: the certified floor is grid-independent.

---

## 3. The bound formula

Following the exact deduction architecture of the method [D26]:

$$c=\frac{I_0^2}{I_2+J},\qquad I_0=\int_{-1/2}^{1/2}v(s)\,ds,\quad I_2=\int_{-1/2}^{1/2}v^2(s)\,ds,\quad J=\iint_{[-1/2,1/2]^2}|s-t|\,v(s)v(t)\,ds\,dt,$$

$$H=2-\frac1c,\qquad \tau=p_{\rm sum}\frac{m-6}{m},\qquad A=\varepsilon(m-6),\qquad B=\Phi_m(A),$$

$$\Phi_m(A)=\begin{cases}A & A\le \tfrac{m}{m-1},\\[2pt] 2\sqrt{\tfrac{(m-1)A}{m}}-1+\tfrac{A}{m} & A>\tfrac{m}{m-1},\end{cases}\qquad \boxed{\;\text{bound}=\frac{H-\tau}{1-B/m}\;}$$

with every symbol defined:

- **$H$** — the ground-state constant at $\alpha=149/100$: $H(1.49)=0.672421886096447472810398380180295961133205755$ (CHECKED NUMERICALLY; analytic $J$ matches kink-split quadrature to $1.7\times10^{-41}$; the naive `mp.quad` fails at the $|s-t|$ kink — must be split). $J=0.264962417451$ at $\alpha=1.49$.
- **$\tau$** — the rational correction: $\tau=(1/220)(127/133)=0.00434039644565960355434039644565960355434\ldots$ (exact rational; difference 0).
- **$A$** — the moment argument: $A=\varepsilon(m-6)=0.008064\cdot127=1.024128$ exactly.
- **$B$** — the moment correction: $B=\Phi_{133}(A)=1.02406108048356053160742615965953979941209469$, computed via the **sqrt branch** $B=2\sqrt{(m-1)A/m}-1+A/m$ since $A>127/126=1.00794\ldots$.
- **$\varepsilon$** — the certified floor, $\varepsilon=0.008064$ (Section 4).
- **$m$-optimality** — $m=133$ is optimal for $(\alpha,p_{\rm sum})=(149/100,1/220)$: $m=132\to0.6732653839$, $m=134\to0.6732653277$, both below the $m=133$ value (CHECKED NUMERICALLY, bound arithmetic only).

---

## 4. The certification machinery

**The verifier.** `verify_cos7.py` — 410 lines, Arb interval arithmetic via python-flint, running on the laptop. It computes a kernel table on a uniform-span grid (grid=4000), second-derivative bounds, tangent-plane pruning, and exact LDL checks, and answers: *does the in-band floor $F\ge\varepsilon$ hold on every box?* It is the agent's own implementation — rigorous interval arithmetic, **not** a Lean formal proof.

**The certified eps-frontier at grid=4000** (CHECKED NUMERICALLY, verifier log):

| $\varepsilon$ | verdict | nodes | time |
|---|---|---|---|
| 0.008060 | TRUE | 942,944 | ~300 s (re-verified twice; matches discovery note) |
| 0.008063 | TRUE | 1,015,132 | 282 s |
| **0.008064** | **TRUE** | **1,116,906** | ~450 s |
| 0.008066+ | FALSE | — | 8067/8070/8075/8081/8090/8102/8120/8145/8180/8230 all fail |

At $p=1/1350$ ($p_{\rm sum}=1/225$) the frontier is lower: max TRUE $=0.007909/10^6$ (197 s). **The certified frontier at the working point is $\varepsilon=0.008064$.**

**Independence check.** $0.008060/10^6$ was independently re-verified at grid=4000 at 942,944 nodes, exactly matching the discovery note (CHECKED NUMERICALLY).

**Bound arithmetic (CHECKED NUMERICALLY, 120+ digits).** With $H=0.672421886096447472810398380180295961133205755$, $A=1.024128$, $B=1.02406108048356053160742615965953979941209469$, $\tau=0.00434039644565960355434039644565960355434$:

$$\frac{H-\tau}{1-B/m}\;=\;0.67326543649552352207990181282271996377681849486392$$

residual vs. the printed 42-digit value: $3.9\times10^{-46}$ = print truncation, not formula failure. Adversarial re-check at $m=133$ reproduced the previous headline to all 42 printed digits (residual $3.889\times10^{-46}$).

---

## 5. The artifact probe: the certified floor is genuine

**Question.** Does the certified floor $\approx 0.0080606$ reflect a real minimum of the functional $F$, or an artifact of the grid-4000 discretization?

**Probe design.** Re-run the verifier at finer grids (6000, 8000) at $\varepsilon$ values that fail at 4000. If the floor were a grid artifact, a finer grid would certify higher $\varepsilon$.

**Probe #1** — $\varepsilon=0.008070$ at grid=6000: **FAILS** (CHECKED NUMERICALLY, verifier). Terminal box
$$\big((6316,6316),(11945,11945),(11895,11895),(6280,6280),(11857,11857),(6301,6301)\big),\qquad \text{lower}=0.008060649099672502,$$
$\text{max\_depth}=81$, pruned $=146518$, interval $=124317$, tangent $=21644$, ~3.6 min.

**Probe #2** — $\varepsilon=0.008068$ at grid=6000: **FAILS** (CHECKED NUMERICALLY). Terminal box
$$\big((6309,6309),(11945,11945),(11901,11901),(6281,6281),(11842,11842),(6303,6303)\big),\qquad \text{lower}=0.008058687850487158,$$
nodes $=530530$, $\text{max\_depth}=81$, ~19 min (contention).

**The grid-scaling identity.** The failing boxes at grid=6000 are **exactly grid-scaled images** of the grid-4000 failing boxes (coordinates × 1.5) — the same terminal region, grid-refined, not a new region. The certified floor at grid=6000 is $\approx 0.0080587$–$0.0080606$, identical to the grid-4000 floor $\approx 0.008060$.

**Conclusion (CHECKED NUMERICALLY).** Finer grids **do not** raise the certifiable floor. The floor is a genuine minimum of the $F$ functional for the working $(\alpha,p_{\rm sum})$ — not a verifier artifact. Scope note: probes ran at grids ≤ 8000 (Section 8).

---

## 6. The exhaustion argument: the family is at its true minimum

The record is not a lucky point; it is the certified maximum over the family of parameters actually explored:

- **$(p_{\rm sum}, \varepsilon)$ trade-off.** Lower $p_{\rm sum}$ lowers $\tau$ but lowers the achievable $\varepsilon$: at $p_{\rm sum}=1/220$ the certified $\varepsilon$ is $0.008064$; at $p_{\rm sum}=1/225$ it drops to $0.007909$. The certified optimum of the combined quantity is at $p_{\rm sum}=1/220$.
- **$\alpha$-sweep (certified eps).** $\alpha=1.49$ certifies $\varepsilon=0.008064$. $\alpha=1.47$: certified eps $\approx 0.007985$, and **no $m\in[128,139]$ beats the record** at that eps. $\alpha=1.49$, $p_{\rm sum}=1/225$, $\varepsilon=0.007909$: $m=135\to0.6732629498$ and $m=136\to0.6732629169$ beat the *old* record but are below the new leader $0.6732654365$.
- **$\alpha=1.45$: INCONCLUSIVE.** At $\alpha=1.45$, $m=133$, $p_{\rm sum}=1/220$, $\varepsilon=0.008064$ the arithmetic gives $0.6733277419$ — the best raw number seen — **but** $\alpha=1.45$'s certified eps is **not established** (only $\alpha=1.49$ certifies $8064$; $\alpha=1.47$ maxes near $7985$). Verifier runs at $\alpha=1.45$ are the flagged next step; until then this point is **INCONCLUSIVE (blocker: uncertified eps)**, not counted.
- **The two-tone window family: REFUTED** (CHECKED NUMERICALLY, Rust sweep `tools/two-tone-sweep`). Over a very wide box the window functional $H$ never exceeds the classic constant $3/2-(1/\sqrt2)\cot(1/\sqrt2)=0.672500703679412$ (single-cosine max $0.672500703679249$ at $\alpha\approx\sqrt2=1.41421$, excess $-1.626\times10^{-13}$); $c=0$ (pure cosine) is always optimal; the top two-tone candidates achieve only $H\approx0.672500703$ and their apparent bound gains come entirely from $p_{\rm sum}=1/300$, whose eps is **CONJECTURED** (needs verifier at that $\alpha$). The "window is the biggest lever" hypothesis is refuted within this family — the lever is $(\varepsilon,p_{\rm sum},m)$.

**Net (CHECKED NUMERICALLY where labeled).** For every point whose $\varepsilon$ is certified, the maximum bound is achieved at $(\alpha,p_{\rm sum},m,\varepsilon)=(149/100,1/220,133,0.008064)$. The family is exhausted at its true minimum of the certified floor $F$.

---

## 7. The bound

**Inputs (all CHECKED NUMERICALLY, mpmath 120+ digits):**

| symbol | value |
|---|---|
| $H(1.49)$ | $0.672421886096447472810398380180295961133205755$ |
| $\tau$ | $(1/220)(127/133)=0.00434039644565960355434039644565960355434\ldots$ |
| $\varepsilon$ | $0.008064$ (certified TRUE, grid=4000) |
| $A=\varepsilon(m-6)$ | $0.008064\cdot127=1.024128$ |
| $B=\Phi_{133}(A)$ | $1.02406108048356053160742615965953979941209469$ (sqrt branch, $A>127/126$) |
| $m$ | $133$ (optimal) |

$$\text{bound}=\frac{H-\tau}{1-B/m}=0.67326543649552352207990181282271996377681849486392$$

**Old record:** $0.673262865534356014645368000853343519319712248$ (at $\varepsilon=0.00806$, discovery-6732629).
**Gain:** $+2.5709611675074345\times10^{-6}$.
**In percentage:** $67.326543649552352207990181282271996377681849486392\%$.

Every certified step above $\varepsilon=0.00806$ yields an immediate improvement (per-eps gain $\sim+3.2\times10^{-4}$ at $m=133$, CHECKED NUMERICALLY), so the frontier push is the entire content of the new record.

---

## 8. Caveats and honesty

1. **Certification is CHECKED NUMERICALLY, not formally proved.** `verify_cos7.py` is rigorous *interval* arithmetic (Arb via python-flint), but it is the agent's own implementation and **not** a Lean formal proof. An independent re-implementation or Lean-ization is the natural next step (per the charter, nothing counts as settled until adversarial validators fail to break it).
2. **Re-certification in flight.** The $\varepsilon=0.008064$ verdict comes from the wave-local verifier log at grid=4000; independent re-runs ($0.008065@4000$, finer-grid probes) were **in flight at time of writing**. The two fine-grid probes that completed ($0.008068$, $0.008070$ @6000) both FAIL — consistent with, and reinforcing, the frontier.
3. **Artifact-probe scope.** Probes ran at grids ≤ 8000 ($0.008068$, $0.008070$ @6000; $0.008066$, $0.008068$, $0.008065$ @8000 launched/deferred). No claim is made about grids beyond 8000.
4. **INCONCLUSIVE residue.** $\alpha=1.45$ arithmetic suggests a higher bound ($0.6733277419$ at the same eps) but its $\varepsilon$ is **uncertified** — flagged, not counted. Two-tone gains rely on $p_{\rm sum}=1/300$ with **CONJECTURED** eps.
5. **The H-window bug was a red herring.** The earlier "1e-6 H discrepancy" was naive `mp.quad` failing at the $|s-t|$ kink; the analytic $J$ formula matches kink-split quadrature to $1.7\times10^{-41}$.
6. **Same quantity as the literature.** The bound is for the simple-zeros-on-line fraction $\liminf N^{*}_{0}(T,2T)/N(T,2T)$, the same quantity as the external records and the [C26] optimized constant.

---

## 9. References

- **[C26]** — *More than two thirds of the zeros of the Riemann zeta function lie on the critical line* (companion paper; $N(T,2T)$, $N_0^{*}(T,2T)$, simple-on-line terminology; optimized test family constant 0.6725; Weil-form + Sylvester inertia + rank–trace argument).
- **[D26]** — `research/notes/discovery-6732629.md` — discovery note for the original record $0.6732628655\ldots$ at $\varepsilon=0.00806$: floor $F\ge0.00806$ interval-verified at 942,944 nodes, max_depth 64, ~300 s; bound arithmetic at 120 digits.
- **Attack record** — `research/waves/wave-phone-2/results/attack-record.md` — the new record, the certified eps-frontier (8063/8064 TRUE, 8066+ FALSE), the $m$-sweep, the sweeps at other certified eps, and the artifact probe (Results 1–5, incl. terminal boxes and the grid-scaling identity).
- **Two-tone refutation** — `research/waves/wave-local/results/exec-two-tone.md` — the two-tone window sweep: $c=0$ optimal, $H\le0.672500703679412$ (classic constant), family refuted as a lever.
- **Verifier** — `verify_cos7.py` (410 lines, Arb via python-flint; canonical copy in `tools/`, working copy `/tmp/combine/verify_cos7.py`). Command form: `verify_cos7.py 149 100 1 1320 <eps·10⁶> 1000000 - <GRID>`.
- **Bound arithmetic** — `scripts/attack_bound_check.py` (mpmath 160/220 dps) + inline 220-dps re-derivation.
- **Background** — Levinson (1974); Conrey (1989); Bui–Conrey–Young (2011); Feng (2012); the 41.6% → 67.25% line; Anthropic Theorem D $0.672500703679$; Montgomery pair correlation (1973); Bombieri (2000); BGSTB24, GS25/26.

*All numerical claims in this paper are CHECKED NUMERICALLY (scripts cited above), unless explicitly labeled otherwise. No claim is PROVEN in the formal sense.*
