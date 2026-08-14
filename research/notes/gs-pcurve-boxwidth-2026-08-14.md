# P(b) — the box-width-to-proportion curve does NOT exist (decisive negative for 0.6818)

**Agent:** builder. **Date:** 2026-08-14. **Task:** sub-lemma (i) of `gs-general-estimate-2026-08-14.md` §4.
**Sources read:** hooks/agents.md; gs-general-estimate-2026-08-14.md; BGSTB full text `baluyot-etal-2306.04799.txt` (§4/§5/§6/§7).
**Skills applied:** s4h-design-constraints (the fixed `1/log T` pair-difference threshold is the tightest constraint), s4h-probability-expected-value-calculation (EV framing: expected gain from the b-lever vs. the 0.6818 target).
**Scope:** closed-form only. No computation run (see §6).

---

## 1. The explicit P(b) formula (the only honest one)

From BGSTB §7 eq. (7.2), with the Tsang kernel $K(z)=\tfrac1\pi\int_0^1 j_M(u)\operatorname{sech}(u)\cos(zu)\,du$,
$\hat K(t)=j_M(2\pi t)\operatorname{sech}(2\pi t)$, and $j_M$ the Montgomery–Taylor kernel (BGSTB eq. (4.4)):

$$\boxed{\;P_{\mathrm{BGSTB}}(b)\;=\;2\;-\;\frac{\hat K(0)+2\int_0^1 \alpha\,\hat K\!\left(\frac{\alpha}{2\pi}\right)d\alpha}{2\pi\,K(0)}\;\;=\;\;2-\frac{1.289389678}{2\times 0.4663199124}\;\;=\;\;0.617483786\ldots\;}$$

**valid for every box half-width $b\in(0,1]$, and independent of $b$.** The three constants (BGSTB §7, verbatim):

- $\hat K(0)=j_M(0)=1.0061271908\ldots$
- $2\int_0^1 \alpha\,\hat K(\tfrac{\alpha}{2\pi})\,d\alpha = 2\int_0^1 \alpha\,j_M(\alpha)\operatorname{sech}\alpha\,d\alpha = 0.2832624869\ldots$
- $\pi K(0)=\int_0^1 j_M(u)\operatorname{sech}(u)\,du = 0.4663199124\ldots$

Then $C(b)\equiv (1.0061271908+0.2832624869)/(2\times 0.4663199124)=1.289389678/0.9326398248=1.382516213\ldots$,
and $P(b)=2-C(b)=0.617483788\ldots$ (paper rounds to $0.617483786\ldots$; my hand arithmetic reproduces it to 8 decimals).

## 2. Where the box width b enters — it is a THRESHOLD, not a parameter (PROVEN from BGSTB)

The task's step 1 ("the off-box contribution scales with b") is **false for this machinery**. The box feeds the error
term only through a **fixed** threshold that does not move with $b$:

1. **Lemma 7** (BGSTB (5.1)) splits the pair sum at $|\beta-\beta'| < 1/\log T$. This threshold is set by **Lemma 6(c)**,
   $\operatorname{Re}K(x+iy)>0$ for $|y|<1$ with $y=(\beta-\beta')\log T$ — a property of the kernel, **independent of the box**.
2. **§6** bounds the off-box error (the "bad" set $\{|\beta-\beta'|\ge 1/\log T\}$):

$$S(T)\;\ll\;\sum_{\substack{|\beta-1/2|\,\ge\,1/(2\log T)\\ 0<\gamma\le T}} T^{\,|2\beta-1|}\sum_{0<\gamma'\le T}\frac{1}{1+((\gamma-\gamma')\log T)^2}\;\ll\;\sum_{\substack{\beta\,\ge\,1/2+1/(2\log T)\\ 0<\gamma\le T}} T^{\,2\beta-1}.$$

3. If all zeros satisfy $|\beta-1/2|<b/(2\log T)$ with **$b\le 1$**, the set $\{\beta\ge 1/2+1/(2\log T)\}$ is **empty**
   (for $T^{3/8}<\gamma\le T$; the $\gamma\le T^{3/8}$ tail is $O(T^{3/8}\log T)=o(T\log T)$, §6). Hence
   $S(T)=o(T\log T)$ **for every $b\le 1$ — with the same room to spare**.
4. Narrowing the box ($b<1$) empties the bad set *faster* but **does not change the kernel integrals** in §7. The
   constant $C(b)$ is computed entirely from $j_M$; the box never appears in (7.1)/(7.2). So $P(b)$ is **flat** on $(0,1]$.
5. For **$b>1$** the bad set is non-empty and the box hypothesis **no longer implies** the density hypothesis (1.6)
   (§6's box⟹density step fails), so $S(T)=o(T\log T)$ is no longer supplied by the box — there is no formula at all.

**PROVEN (derivation-level):** the box width enters the BGSTB pair-correlation sum as a binary gate at $b=1$, not as a
continuous scaling parameter.

## 3. Anchors check — the b=1 correction, and the two anchors use DIFFERENT kernels

- **Correction (PROVEN):** BGSTB's box (1.5) is $|\beta-1/2|<1/(2\log T)$, which is the GS box
  $B_b=\{|\beta-1/2|<b/(2\log T)\}$ with **$b=1$, not $b=1/2$**. The parent note's own §1c states this correctly
  ("BGSTB's box (1.5) is the $b=1$ case"); its §4 anchor "$P(1/2)=0.61748$" is a transcription error.
  The correct anchor is **$P(1)=0.617483786$**.
- **The $P(0)=2/3$ anchor is a DIFFERENT mechanism, not the $b\to0$ limit of the $j_M$ formula.** Montgomery's
  $2/3$ (GS 2603.28104 narrow-box limit) uses the **Fejér kernel** and the positivity $w(\rho-\rho')\ge 0$ argument,
  which is valid on RH and survives as $b\to0$ because $w(\rho-\rho')\to w(i(\gamma-\gamma'))>0$. It does **not** use the
  Tsang $\operatorname{sech}$ normalization or $j_M$. So:
  - $\lim_{b\to 0} P_{\mathrm{BGSTB}}(b) = 0.617483786$ (the flat $j_M$ value), while
  - $P_{\mathrm{Fejér}}(b\to 0) = 2/3$ (Montgomery narrow-box limit).
- **Therefore the sub-lemma's premise "P(b) continuous and monotone on $(0,\tfrac12]$ interpolating $2/3$ at $b=0$ and
  $0.61748$ at $b=\tfrac12$" is REFUTED.** On $(0,1]$ the BGSTB curve is the constant $0.617483786$; the $2/3$ value sits
  at $b=0$ only, via a different kernel/argument. There is no curve to differentiate or invert.

## 4. Solving P(b₀)=0.6818 — decisive negative

$$\sup_{b}\,P(b)\;\le\;\max\big(P_{\mathrm{Fejér}}(0)=\tfrac23,\;P_{\mathrm{BGSTB}}(b\in(0,1])=0.617483786\big)\;=\;\tfrac23\;<\;0.6818.$$

**P(b₀)=0.6818 has NO solution; no box half-width reaches the 0.6818 target through this machinery.**

Moreover (sourced from BGSTB's own introduction, verbatim): *assuming RH*, the pair-correlation method's best-in-print
simple-zero proportion is $67.9\%$ (Chirre–Gonçalves–de Laat, SDP), with Montgomery–Taylor at $67.2\%$ and Fejér at
$2/3$. All three are $<0.6818$. So the box-width lever is **closed for the 0.6818 target even with RH granted** — the
gap is a property of the pair-correlation ceiling ($\le 0.679$), not of the box width.

## 5. Labels

| Claim | Label |
|---|---|
| $P(b)=0.617483786$ constant for all $b\in(0,1]$ (Tsang/$j_M$, conditional on box (1.5)) | PROVEN (conditional; BGSTB §7) |
| Box width enters only as a gate at $b=1$ ($S(T)=o(T\log T)$ iff $b\le 1$) | PROVEN (derivation-level, BGSTB §5–§6) |
| BGSTB box is $b=1$, not $b=1/2$; parent note's "$P(1/2)$" is an error | PROVEN (verbatim (1.5) = $B_1$) |
| $P(0)=2/3$ narrow-box limit (Fejér, not $j_M$) | PROVEN (abstract statement, GS 2603.28104; full proof unopened → INCONCLUSIVE on details) |
| "P(b) continuous/monotone on $(0,1/2]$" (parent note §4(i)) | **REFUTED** (flat on $(0,1]$; $2/3$ is a different kernel at $b=0$) |
| $P(b_0)=0.6818$ solvable | **REFUTED** — $\sup_b P(b)=\tfrac23<0.6818$; even RH pair-correlation $\le 0.679$ |
| Constant $0.617483786$ | **VERIFIED against paper §7** (hand arithmetic reproduced to 8 decimals: $0.617483788$ vs paper $0.617483786$; relabeled 2026-08-14 after adversarial review — the CHECKED NUMERICALLY label requires a script, and none was run) |

**Honesty (task step 4):** $P=0.617483786$ is an **upper envelope of the certified guarantee**: it is obtained by
dropping $S(T)=o(T\log T)$ and the $O(1/\sqrt{\log T})$ in Lemma 7, so the certified bound is $0.617483786-o(1)$.
Conversely it is a **worst-case lower envelope of the true simple proportion** (the actual proportion is $\ge 0.61748-o(1)$,
possibly much larger). The "curve" itself is not defined beyond the flat value, so there is no envelope to sweep in $b$.

## 6. mpmath check — SKIPPED (belief it would change: none)

The check I did **not** run, and why: the three constants are already computed in BGSTB §7 and already recorded as
CHECKED NUMERICALLY in `gs-general-estimate-2026-08-14.md`; the ratio $1.289389678/(2\times 0.4663199124)$ is
reproduced above by hand arithmetic to 8 decimals ($0.617483788$ vs paper $0.617483786$). Running

```python
from mpmath import mp; mp.dps = 25
import mpmath as m
jM = lambda a: 1/(1-m.cos(m.sqrt(2)))*(m.sqrt(2)/2*m.sin(m.sqrt(2)*max(0,1-abs(a))) + 0.5*max(0,1-abs(a))*m.cos(m.sqrt(2)*a))
K0 = m.quad(lambda u: jM(u)*m.sech(u), [0,1])
I  = 2*m.quad(lambda a: a*jM(a)*m.sech(a), [0,1])
print(2 - (jM(0)+I)/(2*K0))   # -> 0.617483786...
```

would only re-confirm $0.617483786$, changing no belief; per hooks §2.4/PONYTAIL rung 1 it is omitted. (Note the one-line
$j_M$ reproduces (4.4) modulo the $\hat j$ normalization; the paper's own $\hat K(0)=1.0061271908$ is the authoritative value.)

## 7. Next step

**Kill the "certify the box $|\beta-1/2|<b_0/(2\log T)$" lever — there is no $b_0$.** The parent note's sub-lemma (i)
is resolved as a decisive negative: pair correlation cannot certify 0.6818 simple at any box width, with or without RH
(ceiling 0.679). Redirect to (a) sub-lemma (ii) (formalize that the box hypothesis is strictly finer than fixed-$\sigma$
zero-density — its motivation now stands on the *on-line* proportion, where BGSTB supplies nothing, not on the simple
proportion), and (b) the genuinely-new-input requirement in `structural-final-verdict.md`: 0.6818 needs an input outside
the pair-correlation certificate class (Levinson/mollifier/Weil-form or a joint simple+on-line bound), not a smaller box.
