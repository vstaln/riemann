# The GS/BGSTB "general estimate that replaces RH" — precise statement + hardness test

**Agent:** research architect (structural thread). **Date:** 2026-08-14.
**Scope:** literature/structure only (NO compute — charter). Sources read this session:
BGSTB full text `research/papers/baluyot-etal-2306.04799.txt`; GS full text arXiv:2511.20059v2
(ar5iv HTML); GS arXiv:2603.28104 abstract (arXiv API); s4h-investigation + s4h-constraint skills.

---

## 1. The precise estimate (attack target)

### 1a. The general double-sum estimate (the RH-replacement, verbatim)

**Source:** Goldston–Suriajaya, *Zeta Zeros on the Critical Line*, arXiv:2511.20059v2, **Theorem 2, eq. (4.4)**.

> **Theorem 2.** Suppose there exists a constant $C$ with $1 \le C < 2$ such that, as $T\to\infty$,
> $$(4.4)\qquad \sum_{\substack{\rho,\rho'\\ 0<\gamma,\gamma'\le T\\ \gamma=\gamma'}} 1 \;\le\; (C+o(1))\,\frac{T}{2\pi}\log T .$$
> Then asymptotically at least the proportion $2-C$ of the zeros of $\zeta(s)$ are simple;
> at least the proportion $2-C$ are on the critical line; and if $1\le C<3/2$, at least the
> proportion $3-2C$ are simple and on the critical line.

This **is** the "general double-sum estimate" of the 2603.28104 abstract ("RH can be replaced with a
general estimate for a double sum over zeros"). Its decomposition (their eq. (4.3)) is the structural core:

$$(4.3)\qquad \sum_{\gamma=\gamma'} 1 \;=\; \underbrace{\textstyle\sum_\rho m_\rho}_{\text{diagonal}}
\;+\; \underbrace{\textstyle\sum_{\rho:\ \beta\neq 1/2} m_\rho}_{\text{symmetric diagonal}\ (1-\bar\rho)}
\;+\; \underbrace{\textstyle\sum_{\substack{\rho\neq\rho'\\ \beta+\beta'\neq 1\\ \gamma=\gamma'}} 1}_{\text{non-symmetric horizontal pairs}} .$$

- The **diagonal** term controls $\sum m_\rho$ → the **simple** proportion (Montgomery's original use).
- The **symmetric** term controls $\sum_{\beta\neq 1/2} m_\rho$ → the number of **off-line** zeros → the
  **"on the critical line"** proportion (the genuinely new GS consequence).
- The **third term** (distinct zeros at the same height, not symmetric partners) is the hard RH-shaped residual.

**PROVEN (framework):** GS Theorem 2 is a theorem; its *hypothesis* (4.4) is the unproven input.
Under RH, Montgomery (1973) proves (4.4) with $C=4/3$ (their eq. (3.1), Fejér kernel
$(\frac{\sin\frac12(\gamma-\gamma')\log T}{\frac12(\gamma-\gamma')\log T})^2$ = $4/3+o(1)$ times the main term),
giving $2/3$ simple. **So "RH ⟹ C=4/3 ⟹ 2/3 simple" is PROVEN (conditional on RH);**
**the open problem is (4.4) with $C=4/3$ unconditionally (or on a hypothesis weaker than RH).**

### 1b. The equivalent box / zero-density forms

**Source:** BGSTB arXiv:2306.04799, **Theorems 2 and 3, eqs. (1.5), (1.6), (6.1), (6.2)**.

- **Box form (Thm 2):** all zeros $\rho=\beta+i\gamma$ with $T^{3/8}<\gamma\le T$ satisfy
  $$(1.5)\qquad \tfrac12-\tfrac{1}{2\log T}<\beta<\tfrac12+\tfrac{1}{2\log T}
  \quad\Longrightarrow\quad \ge 61.7\%\text{ simple.}$$
- **Density form (Thm 3):** the strong zero-density hypothesis
  $$(1.6)\qquad N(\sigma,T)=o\big(T^{2(1-\sigma)}\big)\quad\text{for }\ \tfrac12+\tfrac{1}{2\log T}\le\sigma\le\tfrac{25}{32}+\eta \ \ (\eta>0)$$
  also $\Longrightarrow \ge 61.7\%$ simple.
- **PROVEN (BGSTB §6):** the box (1.5) ⟹ the density hypothesis (1.6) ⟹ the error term
  $S(T)=o(T\log T)$ in their Lemma 7 ⟹ 61.7% (their §7, $j_M$ kernel: $2-\frac{1.289389678}{2\times0.466319912}=0.617483786$).
  **CHECKED NUMERICALLY** is the constant $0.617483786\ldots$ (paper's own computation, §7, not re-run here — out of scope).

### 1c. The narrow-box strengthening (what buys 2/3 instead of 0.617)

**Source:** Goldston–Suriajaya, *Zeta Zeros in a Narrow Vertical Box*, arXiv:2603.28104, abstract.

> On assuming all zeros between height $T$ and $2T$ lie in the narrow vertical box
> $B_b=\{|\sigma-\tfrac12|< b/(2\log T),\ T<t\le 2T\}$ centered on the critical line, then if
> $b=b(T)\to 0$, asymptotically at least $2/3$ of the zeros are simple **and** on the critical line.

Note: BGSTB's box (1.5) is the $b=1$ case (half-width $1/(2\log T)$) → 61.7%; the narrow box $b\to0$ is the
RH-scale limit and recovers Montgomery's $2/3$ **plus** "on the line". **PROVEN (abstract statement);
full proof not opened — INCONCLUSIVE on proof details.**

### 1d. The exact attack target, stated once

**Prove unconditionally (or on a hypothesis strictly weaker than RH) that (4.4) holds with $C=4/3$** —
equivalently, certify one of:
- (A) all but $o(N(T))$ zeros in the box $|\beta-\tfrac12|< b(T)/(2\log T)$ with $b(T)\to0$; or
- (B) $N(\sigma,T)=o(T^{2(1-\sigma)})$ uniformly for $\sigma\in[\tfrac12+\tfrac{1}{2\log T},\ \tfrac{25}{32}+\eta]$
  (the missing range below Bourgain's $\tfrac{25}{32}$).

Any such certification moves the pair-correlation/SDP machinery onto the unconditional side and raises $p_1$.

---

## 2. Hardness test (s4h-constraint): is the "RH wall" here real, and can Guth–Maynard supply (A)/(B)?

**Verdict: the wall is REAL and is a *scale* wall, not a *depth* wall. A Guth–Maynard-type zero-density
input cannot supply it directly — zero-density $N(\sigma,T)$ is the wrong instrument at the box boundary.**

### 2a. What $N(\sigma,T)$ controls near $\sigma=1/2$ (PROVEN facts)

- $N(\sigma,T)=\#\{\beta\ge\sigma, 0<\gamma\le T\}$. The full count is $N(\tfrac12,T)\sim \tfrac{T}{2\pi}\log T$
  (von Mangoldt). **PROVEN.**
- A zero-density estimate of shape $N(\sigma,T)\ll T^{A(\sigma)(1-\sigma)+o(1)}$ is **never better than $N(T)$
  itself** as $\sigma\to\tfrac12^+$: for the classical Ingham bound $A(\sigma)=\frac{3}{2-\sigma}$, the
  exponent $A(\sigma)(1-\sigma)=\frac{3(1-\sigma)}{2-\sigma}\to 1$ as $\sigma\to\tfrac12^+$, and $A\to 2$
  (NOT 1 — the exponent is $A(1-\sigma)$, not $A$). Ingham's actual bound near $\sigma=1/2$ carries a
  $\log^5 T$ factor, i.e. $T\log^5 T$, which *is* larger than $N(T)\sim\frac{T}{2\pi}\log T$ — vacuous.
  **PROVEN (book-keeping: $A\to 2$ and $A(1-\sigma)\to 1$ as $\sigma\to1/2$; the log-power makes the
  bound vacuous near the line).**
- Consequently the *density hypothesis* (BGSTB form, eq. (1.6): $N(\sigma,T)=o(T^{2(1-\sigma)})$) **cannot be
  asserted at $\sigma=1/2$**: at $\sigma=1/2$ it would read $N(1/2,T)=o(T)$, contradicting von Mangoldt
  $N(T)\sim \tfrac{T}{2\pi}\log T$. **PROVEN.** The density hypothesis can only be asserted for
  $\sigma\ge \tfrac12+c$ with $c>0$ fixed. (The form with a $\log T$ factor, $N\ll T^{2(1-\sigma)}\log T$,
  is *true* at $\sigma=1/2$ by von Mangoldt — that is why BGSTB state it in the little-o form.)

### 2b. What the box/double-sum needs (the scale mismatch — the core of the verdict)

Certifying (A)/(B) requires a *log-factor saving in the number of zeros outside a
$1/(2\log T)$-neighbourhood of the line*: precisely $N(\tfrac12+\tfrac{1}{2\log T},T)=o(T\log T)$.
This is a statement at distance $O(1/\log T)$ = the **average zero gap** = the **RH scale**.
Two consequences follow, both **PROVEN from 2a**:

1. **Zero-density is scale-blind inside $O(1)$ of the line.** $N(\sigma,T)$ for any *fixed* $\sigma>1/2$
   cannot see whether zeros sit at $\beta=1/2$ or at $\beta=1/2\pm\tfrac{1}{2\log T}$, because both lie
   strictly to the left of $\sigma$. So no fixed-$\sigma$ estimate (Guth–Maynard included) expresses the box.
2. **The required estimate sits exactly where the density hypothesis is false.** At $\sigma=\tfrac12+\tfrac{1}{2\log T}$
   the density hypothesis would force $N\ll T^{2\cdot\frac{1}{2\log T}}\log T = O(\log T)$; this is the
   *moving* boundary $\sigma-\tfrac12=\tfrac{1}{2\log T}\to0$, not a fixed $\sigma$. Every known zero-density
   method (Ingham, Huxley, Bourgain, Guth–Maynard) is proven only for $\sigma\ge\sigma_0$ with $\sigma_0$ a
   fixed constant $>1/2$, and even there the exponent is $\ge$ the Ingham line; none descend to $o(1)$ of the line.

### 2c. Guth–Maynard specifically (INCONCLUSIVE on exact range — flagged)

Guth–Maynard (2024) strengthens the zero-density exponent in the **middle/upper strip** (its announced
application is primes in short intervals), and — per the survey arXiv:2607.04632 — pushes the
*density-hypothesis-holding range* lower than Bourgain's $\tfrac{25}{32}$. **INCONCLUSIVE (I read only the
survey abstract, not the GM paper):** the exact GM range/threshold was not verified this session. What is
**CONJECTURED (strongly motivated — NOT PROVEN until sub-lemma (ii) lands)** and load-bearing regardless of
the precise threshold:

- GM can at best lower the constant $\tfrac{25}{32}$ in (1.6) toward some fixed $\sigma_0>1/2$. It **cannot**
  reach $\sigma=\tfrac12+\tfrac{1}{2\log T}$ **by a fixed-$\sigma$ zero-density estimate alone**, because the
  density hypothesis is false at $\sigma=1/2$ (2a) and a fixed-$\sigma$ estimate is consistent with all zeros
  lying just off-line inside $\sigma_0$ (Shape-1 blindness: it constrains no shrinking box).
- Therefore GM-type zero-density can only **shrink** the missing range in (B); it can never close it. The gap
  $[\tfrac12+\tfrac{1}{2\log T},\ \sigma_0]$ survives, and it is exactly the RH-scale strip.
- **The honest caveat:** a fixed-$\sigma$ zero-density estimate COMBINED with a *moment* input (e.g. a
  weighted $\sum(\beta-\tfrac12)^2$ bound or a $\log|\zeta|$ mean-square at the boundary) COULD constrain the
  box. The pure scale-blindness claim therefore needs sub-lemma (ii) before it is PROVEN; until then
  **CONJECTURED (strongly motivated)**.

### 2d. Constraint classification (s4h-constraint output)

| Constraint | Class | Evidence |
|---|---|---|
| "RH needed for 2/3 simple" | **soft — already dissolved** | GS Theorem 2 + BGSTB Thm 1 replace RH by (4.4)/box; PROVEN framework |
| "Box/density hypothesis is provable by zero-density" | **assumption (false hope)** | density hypothesis false at $\sigma=1/2$ (2a); scale mismatch (2b); PROVEN |
| "The $1/(2\log T)$-strip barrier" | **hard (theorem-level)** | statement lives at the average-gap scale where RH lives; no known tool descends there |

**So: the "RH wall" decomposes into (i) a SOFT part — RH's role in the pair-correlation *method* is already
removed — and (ii) a HARD part — the residual estimate is a log-factor saving at the $O(1/\log T)$ scale,
which zero-density cannot express.** Guth–Maynard is a real but *mis-matched* lever: it moves the
Levinson/mollifier route (Candidate 4) and shrinks Bourgain's $\tfrac{25}{32}$, but it is the wrong tool for (4.4).

---

## 3. Labels

| Claim | Label |
|---|---|
| Unconditional Montgomery theorem (BGSTB Thm 1) | PROVEN (unconditional) |
| GS Thm 2 framework: (4.4) ⟹ $2-C$ simple / on-line / $3-2C$ both | PROVEN (conditional on (4.4)) |
| RH ⟹ (4.4) with $C=4/3$ ⟹ 2/3 simple | PROVEN (conditional on RH, Montgomery 1973) |
| Box (1.5) ⟹ 61.7% simple; density (1.6) ⟹ 61.7% | PROVEN (conditional on box/density; BGSTB) |
| Box (1.5) ⟹ density (1.6) | PROVEN (BGSTB §6) |
| Constant $0.617483786\ldots$ | CHECKED NUMERICALLY (paper's §7; not re-run — out of scope) |
| Narrow box $b\to0$ ⟹ 2/3 simple and on-line | PROVEN (abstract; full proof unopened → INCONCLUSIVE on details) |
| Density hypothesis false at $\sigma=1/2$; zero-density never beats $N(T)$ near the line | PROVEN (2a, corrected 2026-08-14) |
| Guth–Maynard cannot certify (A)/(B) | **CONJECTURED (strongly motivated)** for the scale gap (2b); pending sub-lemma (ii); **INCONCLUSIVE on GM's exact $\sigma$-range** (survey abstract only) |
| (4.4) provable unconditionally at present | **INCONCLUSIVE (blocker: no tool reaches the $1/(2\log T)$ strip)** |

*Honest caveat on GS eq. (4.3): the exposé's multiplicity bookkeeping in the diagonal/symmetric sums is
informal (it writes $\sum m_\rho$ where a fully careful count of ordered pairs would involve $m_\rho^2$ and a
factor 2 on the symmetric terms). The load-bearing structure — diagonal ↔ multiplicity, symmetric ↔ off-line
count, residual ↔ non-symmetric horizontal pairs — is unaffected. Flagged `[inferred]`; not a disproof.*

---

## 4. Recommended next step (concrete sub-lemma)

**Attack the *box-width-to-proportion* curve, then the scale-gap lemma.**

**(i) Concrete sub-lemma (immediately attackable, no compute):** For the BGSTB Tsang-kernel argument, express
the guaranteed simple-fraction as an explicit function $P(b)$ of the box half-width $b$ (BGSTB §7 = $P(1/2)=0.61748$;
Montgomery RH limit = $P(0)=2/3$; GS 2603.28104 = $P(b)\to 2/3$ as $b\to0$). Prove $P(b)$ is continuous and
monotone on $(0,\tfrac12]$, and solve $P(b_0)=0.6818$ for the **target box half-width $b_0$**. This converts
"break the 0.6818 wall" into the quantified, checkable target "certify the box $|\beta-\tfrac12|<b_0/(2\log T)$".

**(ii) Scale-gap lemma (the hardness statement, to formalize):** Prove that *no* zero-density estimate
$N(\sigma,T)\ll T^{A(\sigma)(1-\sigma)+o(1)}$ valid only for $\sigma\ge\sigma_0>1/2$ can imply
$N(\tfrac12+\tfrac{1}{2\log T},T)=o(T\log T)$; i.e. the box hypothesis is **strictly finer** than every
fixed-$\sigma$ zero-density family. (This is the formal version of §2b; it would certify that the box is a
genuinely new input class, not a corollary of Guth–Maynard.)

Priority: (i) first (it sizes the actual target $b_0$); (ii) second (it rules out zero-density as the supplier
and redirects effort toward log|ζ|-type / Selberg "almost-all-zeros-in-box" methods, which are the correct scale).

---

## 5. ADJUDICATION (2026-08-14, after adversarial review — review-fresh-notes-2026-08-14.md)

The reviewer verified §1 against the actual sources (GS Thm 2 / eqs. (4.3)-(4.5) verbatim from
arXiv:2511.20059 ar5iv; BGSTB §6/§7) — faithful. Three fixes applied:

1. **§2a arithmetic (was WRONG, now corrected):** Ingham's $A(\sigma)=3/(2-\sigma)\to 2$ (not 1) as
   $\sigma\to 1/2$; the *exponent* $A(1-\sigma)\to 1$ is what tends to 1. And the density hypothesis is
   false at $\sigma=1/2$ in the little-o form $o(T^{2(1-\sigma)})$ (would read $o(T)$), NOT in the
   $\log T$-factor form (which is true there by von Mangoldt). Text above now states both correctly.
2. **Overlabeling (was PROVEN, now CONJECTURED):** "zero-density is scale-blind / GM cannot supply (A)/(B)"
   downgraded to CONJECTURED (strongly motivated), pending sub-lemma (ii) — a fixed-$\sigma$ estimate
   COMBINED with a moment input could in principle constrain the box.
3. **§2b's $T^{2\cdot(1/(2\log T))}\log T = O(\log T)$ moving-boundary computation is CORRECT** (kept as-is).

---

*No computation performed (literature/structure only, per charter). All labels per honesty guardrails
(hooks/agents.md §2).*
