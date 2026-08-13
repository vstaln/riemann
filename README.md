# Riemann Program

## Scoreboard

RH is **not proved**. Nothing below should be read as a proof of the Riemann hypothesis.

| quantity | value | status |
|---|---|---|
| **Certified simple-on-line** (this repo) | **≥ 0.6734808616745137** (67.348%) | CHECKED (Arb coboundary, 3× identical) |
| **Certified distinct zeros** | **≥ 0.8367404308372568** (83.674%) | affine corollary of the simple-on-line bound |
| **In-class ceiling** (256-law, bandwidth ≤ 1) | **0.68182868746** simple fraction $p_0$; attained **$p_0+\frac1{6\cdot256^2}=0.68183123059$** | PROVEN (Lean PairCeiling / LP dual) |
| Gap record → ceiling | $0.00835$ | arithmetic; needs a new input, not a tighter eps |
| Anthropic 2026 (on the line) | ≥ 2/3; optimized **0.6725** $= \tfrac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}$ | PROVEN (Conrey–Goldston; Lean) |
| Anthropic distinct | ≥ 5/6 = 0.8333… | PROVEN |
| Prior record (pre-Anthropic) | 41.6% on the line | Conrey 1989 line |

**Record config** (`research/notes/FINAL-RECORD-2026-08-13.md`): $\alpha=1.464$, coboundary, $p_{\mathrm{sum}}=1/320$, $\varepsilon=0.00620$ (0.00621 fails), $m=171$, $H(1.464)=0.672467425578$, nodes $1{,}096{,}556$. Class exhausted at this saddle — no in-class tick on this pod.

**Other constants**

| quantity | value | status |
|---|---|---|
| $\xi'$ simple-on-line / distinct | $0.85838$ / $0.92919$ | Lean (FGL family); standalone, no interlacing transfer |
| First-prime threshold $a_2=(\log 2)/2$ | $0.346573590280$ | Suzuki: $\lambda_a>0$ for $a<a_2$ |
| $\mathrm{th}(a_2)=2A+1+\log a_2$ | $1.35543263017$ | (4.5) positivity threshold |
| Even mean-zero $\mu_2$ (nested HS) | $\ge 1.6414$ | CHECKED; clears $\mathrm{th}(a_2)$ by $0.286$ |
| Even mean-zero $R$ at $a_2$ | $\ge 0.213$ | CHECKED (Young $\|\rho''\|_1=0.072515$) |
| Cosine $J+\rho-\mathrm{th}$ at $a_2$ | $+2.653824\times10^{-3}$ | CHECKED; dropping $\rho$ fails |
| $\lambda_{a_2}>0$ (all even $w$) | open | ground-ray $O(1/k)$ lemma incomplete |
| 67% record from this Weil line | unchanged | coboundary class is a different object |

Paper draft of the Weil sector: `research/papers/weil-first-prime-even-sector.md`.

## Credits (ideas and code we used)

This repo did not invent the certificate class. The record is a transfer of other people’s machinery (window, rank–trace, coboundary) onto a slightly different $(\alpha,\varepsilon)$. Local mirrors live under `research/external-results/` and `research/lean-zeta-23/`.

**Git repos**

| who / repo | what we took |
|---|---|
| [anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean) | Claude / Anthropic 2026: Theorems A–E (2/3 on-line, 2/3 simple-on-line, 5/6 distinct, $0.6725$ Montgomery–Taylor). Sorry-free Lean. Paper: [Anthropic PDF](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf). Verified by Conrey & Goldston. |
| [ainta/zeta-simple-zeros](https://github.com/ainta/zeta-simple-zeros) | 7-point Gram-stability refinement of rank–trace. Bound $0.673008527927$. Analytic framework (general window, $\min(1,E)$ Gram-defect) that later repos pin. |
| [trmdy/zeta-simple-zeros-673137](https://github.com/trmdy/zeta-simple-zeros-673137) | Trig-polynomial window + weighted 7-point block inequality. Bound $0.673137630699$. |
| [tawanerguo-cn/zeta-simple-zeros](https://github.com/tawanerguo-cn/zeta-simple-zeros) | Bellman coboundary redistribution $(p,q)$. Bound $0.673192911473$ at $\alpha=1.47$. **Our $0.67348086$ uses their $p,q$ unchanged**, moved to $\alpha=1.464$, $\varepsilon=0.00620$, $p_{\mathrm{sum}}=1/320$. Zenodo: [10.5281/zenodo.21890630](https://doi.org/10.5281/zenodo.21890630). |
| [openai/ten-proofs](https://github.com/openai/ten-proofs) | Lean-formalized method examples (not a zeta bound). Mined for certificate / Lean hygiene. |
| [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4) | Lean standard library under the Anthropic formalization. |
| [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) | PNT-in-Lean material used by zeta-23-lean. |

**Papers (the analytic inputs)**

| who | what we took |
|---|---|
| A. Weil (1952) | Explicit formula; $Q_W\ge 0$ for all compactly supported test functions $\Leftrightarrow$ RH. |
| H. Montgomery (1973) | Pair correlation / form factor on bandwidth $\le 1$ (unconditional second moment). |
| N. Levinson (1974); J. B. Conrey (1989); Bui–Conrey–Young (2011); Pratt–Robles–Zaharescu–Zeindler (2020) | Mollifier line: 1/3 → ~40% → 41.05% → **>41.7% on the line**, **>40.75% simple-on-line** (published unconditional records). |
| H. Yoshida (1992); E. Bombieri (2000/2001) | Localization of Weil’s form; $\lambda_a>0$ for small $a$; variational $T$. |
| M. Suzuki [arXiv:2606.09096](https://arxiv.org/abs/2606.09096) | Screw function; $\lambda_a>0$ for $a<(\log 2)/2$; identity (4.5)–(4.6) used in the first-prime notes. |
| Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh [2306.04799](https://arxiv.org/abs/2306.04799), [2501.14545](https://arxiv.org/abs/2501.14545) | Unconditional Montgomery-type pair correlation / Goldston–Suriajaya inputs to the certificate. |
| Rudnick–Sarnak | Unconditional $n$-level sine kernel for $|\lambda|<1$ (unmarked $m_3=5$). |
| X. Wu [arXiv:1206.3737](https://arxiv.org/abs/1206.3737) | Distinct zeros of $\zeta$: $N_d\ge 0.66036\,N$ (pre-Anthropic distinct record). |
| Farmer–Gonek–Lee / FGL $\xi'$ | $\xi'$ simple-on-line $0.85838$, distinct $0.92919$ (Lean in zeta-23). |

If a bound in the scoreboard is “ours,” the **mechanism** is still one of the rows above. Cite the source repo, not this README, as the origin of the idea.

---

A persistent multi-agent research program attacking the **Riemann hypothesis** — and alongside it, any
rigorous, novel mathematics about ζ and its zeros.

> **Transparency note.** This repository is a *work in progress*, not a finished paper. It documents a
> research process: a team of parallel AI agents (dispatched and orchestrated by **DeepSeek V4 running on
> the pi coding agent**), set the task of independently reproducing, verifying, and extending the 2026
> Anthropic result below — the way one would test a new model against a known hard benchmark. Nothing here
> is a claimed proof of the Riemann hypothesis, and no claim here should be read as a peer-reviewed result.
> Every note is honest about its status (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED /
> INCONCLUSIVE), and the whole record — including the failures, the dead ends, and the walls — is public on
> purpose. The underlying result being tested is the LLM-produced paper by Claude (Anthropic); the test
> harness is DeepSeek V4 on pi.

**Operating context:** this project studies and extends the 2026 result *"More than two thirds of the zeros
of the Riemann zeta function lie on the critical line"* (Claude; Anthropic), which proved unconditionally
that ≥ 2/3 of the nontrivial zeros lie on the critical line (≥ 5/6 distinct), with optimized constant
0.6725 — improving the prior record of 41.6%.

**Charter:** `hooks/agents.md` — never-give-up search, honesty guardrails (every claim labeled
PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED; nothing counts as progress until adversarial
validators fail to break it; a wrong confident result is worse than no result), multi-agent research
protocol, and a mandatory code-backed-verification protocol (every number must come from a saved, cited
script).

## Layout

- `PLAN.md` — the plan and round structure
- `hooks/agents.md` — the persistent agent charter (binds every model, every session)
- `research/papers/` — primary sources (PDF + text)
- `research/lean-zeta-23/` — the Lean 4 formalization of the underlying result
  (upstream: https://github.com/anthropics/zeta-23-lean)
- `research/notes/` — the living research record: proof maps, verification reports, attack logs,
  idea catalogs (12+ cross-domain generators), and every documented negative
- `tools/` — numerical toolkit (Rust + Python/mpmath), each with cited run commands

## Open problems under attack

- (P1) close the in-class gap 0.6725 → 0.6818 (second-moment gap Δm₂ = 0.0093)
- (P2) break the two-moment 5/6 distinct wall (third/fourth moments, Rudnick–Sarnak range)
- (P3) form factor / pair correlation beyond α = 1 (both mean and variance functionals: documented dead
  as unconditional inputs)
- (P4) family transport (Dirichlet characters, GL(2) families)
- (P5) the derivative tower (ξ′, ξ″, …) certificates
- (P6) finite-T error terms (C∞ vs hard-cutoff kernel)

## Headline findings so far

- **In-class ceiling 0.6818… is tight** (LP dual; optimal certificate r(x) = 1 − x attains
  p₀ + 1/(6·256²) = 0.68183123; Lean-verified modulo one numerically-checked enclosure)
- **The beyond-α=1 wall is closed from every direction** (mean pair sums, variance, matrix inequalities,
  distributional/CLT inputs, the CvS theorem import, even RH itself does not move the ceiling)
- **The 2/3 deficit is arithmetic** — pair-correlation content, not method-inherent (Ihara-zeta sandbox on
  provably-RH-true objects: the certificate is a rigidity meter, not an RH-meter)
- **The 5/6 distinct wall is robust to the third moment** (identical on both worlds; the separation is a
  fourth-moment phenomenon)
- 12 cross-domain idea catalogs (physics, chemistry, control, crystallography/astronomy, music/linguistics,
  games, human systems, earth sciences, biology, ML/ecology, TCS, history-of-mathematics) + the
  history lesson: tight class limits break by *new objects*, never by sharper inequalities in the class

## Honest status

No proof of RH exists here or is claimed. The search is cumulative: every negative is a documented
finding with a script behind it. See `research/notes/` for the full record.
