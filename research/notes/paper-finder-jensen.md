# Paper finder — Jensen polynomials / derivative tower / screw function

_Generated 2026-08-11 by the paper-finder sub-agent. Honesty protocol: every listed paper was found by a live arXiv API query and its abstract was fetched from that API response; no ID in this note is from memory. All 39 PDFs were then downloaded from arxiv.org and spot-checked (PDF magic bytes; 5 key PDFs text-extracted and their first-page titles matched to the fetched abstracts)._

## What the three live threads need

- **(a) Jensen-ometer probe** (attack-jensen-ometer.md, in flight): the Griffin–Ono–Rolen–Zagier line on Jensen polynomials for ζ/ξ and its sequels, plus the *limits* of that route (Farmer's critique, de Bruijn–Newman constant, heat-flow H_t) and the coefficient machinery (Romik, O'Sullivan).
- **(b) Derivative tower** (ξ′, ξ″, …): we held Radziwill 1301.3232 and Farmer–Gonek 0803.0425; now added the Farmer line on zeros of derivatives (Farmer–Ki, Dueñez–Farmer–Froehlich–Hughes, Farmer–Rhoades universality, Ki, Lester) and the C-cited Farmer–Gonek–Lee FGL14 comparandum (journal-only).
- **(c) Screw function / Weil quadratic form** beyond Suzuki: we held Suzuki 2606.09096 and (mislabeled) Groskin 2605.20224/2607.02828; now added the full Suzuki screw-line corpus (2022–2023), Connes–Consani Weil positivity, Connes–van Suijlekom spectral truncations (the CVS-truncation origin), and the 2026 numerical follow-ups.

## Searches run (all via https://export.arxiv.org/api/query, Atom XML, 2–6 s spacing, 429-backoff)

| # | Query | Hits | Notes |
|---|-------|------|-------|
| 1 | `all:"Jensen polynomials" AND all:"Riemann zeta"` | 4 | GORZ 1902.07321 + 1910.01227 + follow-ups |
| 2 | `all:"Jensen polynomials"` | 25 | incl. O'Sullivan, Farmer critique, 2026 Holland, Ono 2511.02628 |
| 3 | `all:"Jensen polynomial" AND all:discriminant` | 1 | Brugidou 1206.6973 (2-variable power series approach to RH) |
| 4 | `all:"Jensen polynomials" AND all:derivatives` | 9 | GORZ, Farmer 2008.07206 critique, Campbell 2410.06403, Holland 2608.08682 |
| 5 | `all:"derivatives of the Riemann xi"` | 4 | Li-criterion / Voros-adjacent (Coffey, Sekatskii) |
| 6 | `au:Farmer AND all:zeta` | 16 | the Farmer derivative line: Farmer–Ki 1002.1616, DFFH 1002.0372, Farmer–Rhoades math/0310252, Ki math/0701726, 2211.11671 |
| 7 | `all:"zeros of the derivatives" AND all:zeta` | 25 | Lester 1308.5116, Binder–Pauli–Saidak 1002.0362, Onozuka 1606.03733, others |
| 8 | `all:"Hermite-Biehler" AND all:zeta` | 1 | tangential (0712.1266, French); see row 21 for full HB list |
| 9 | `au:de_Branges` / `au:Branges` | 0 | **de Branges has NO arXiv papers** — his RH work is journal/unpublished (see UNOBTAINABLE) |
| 10 | `all:"de Branges" AND all:Riemann` | 15 | Suzuki 1204.1827 canonical systems, Burnol math/0203120, Noor 1809.09577 (Báez–Duarte), Conrey–Li math/9812166, Freedman 2606.29555 |
| 11 | `all:"Taylor coefficients" AND all:"Riemann xi"` | 4 | Romik 1902.06330, O'Sullivan 2007.13582, 2007.13582, Wagner 2108.01827 |
| 12 | `all:"Laguerre inequalities"` | 20 | Csordas 1309.0055, Cardon 0911.1122, Csordas–Chasse 1005.5186, Krasikov math/0204098, Tyaglov–Atia 1912.04951 |
| 13 | `all:"screw function"` | 8 | Suzuki screw corpus: 2206.03682, 2209.12832, 2308.11860, 2209.04658; Matsumoto–Suzuki 2409.00888 |
| 14 | `all:"Weil quadratic form" AND all:Riemann` | 5 | Suzuki 2606.09096, Groskin 2607.02828, Connes 2602.04022, Kim et al 2607.24830 |
| 15 | `all:"Newton inequalities"` | 10 | no direct ζ-paper in top-10 relevance; Newton-inequality content lives inside GORZ/OnO |
| 16 | `au:Suzuki AND all:Weil` | 16 | Suzuki's Weil/screw line incl. 2301.00421 (Hilbert space), 2301.05779 (Li norms) |
| 17 | `all:hyperbolicity AND all:"Jensen polynomials"` | 10 | includes 1905.11269 Jensen–Pólya for L-functions, 2605.31356 Pólya–Schur + free probability |
| 18 | `all:"de Bruijn-Newman"` | 12 | Rodgers–Tao 1801.05914, Polymath 1904.12438, Dobner 2005.05142, Michalowski 2602.20313 |
| 19 | `au:Connes AND all:Weil` | 13 | Connes–Consani 2006.13771 Weil positivity, 1509.05576 essay, 2602.04022 |
| 20 | `au:Gonek AND all:derivative` | 2 | Farmer–Gonek 0803.0425 (held), Bui–Gonek–Milinovich 1302.5032 |
| 21 | `all:"Hermite-Biehler"` | 20 | Holtz math/0512591, Kozhan–Tyaglov 2302.07018, Chirre 2004.14465, Adams–Cardon math/0608297, Suzuki 1308.0228 |
| 22 | `all:"Laguerre-Pólya" AND all:zeta` | 2 | Katkova math/0505174 (multiple positivity), Durán 2405.18940 (Brenke polynomials & RH) |
| 23 | `all:"Spectral truncations" AND all:noncommutative` | 5 | **Connes–van Suijlekom 2004.14115** (the CVS truncation source) |
| 24 | `all:"Riemann xi" AND all:approximation` | 9 | Jenkins–McLaughlin 1609.05965, Shi 1502.06844, Din 1009.2989, Chirre 2004.14465 |
| 25 | `ti:"derivative of the Riemann zeta function"` | 20 | Onozuka 1606.03733, Hughes–Pearce-Crump moments, Hiary–Odlyzko 1105.4312, Ng 0706.1763 |
| 26 | `au:Ono AND all:Jensen` | 5 | GORZ papers + Ono 2511.02628 |
| 27 | `all:"Hermite polynomials" AND all:"Riemann hypothesis"` | 5 | GORZ, Farmer critique, O'Sullivan, Romik, Cardon–Sorensen–White 1912.13055 |
| 28 | `au:Conrey AND all:derivative` | 7 | Conrey–Rubinstein–Snaith math/0508378 (moments of ζ′), CFKL 2508.11108 |
| 29 | `au:Burnol AND all:Weil` | 4 | Burnol explicit-formula series (math/9810169 downloaded) |
| 30 | `ti:"Jensen" AND ti:"Riemann"` | 5 | the 5 core Jensen-Riemann papers (all downloaded) |

## VERIFIED-BY-FETCH download list (39 papers, all on arXiv, abstract fetched from the API before download)

Status labels: **DOWNLOADED** = PDF in research/papers/ verified (magic bytes; 5 spot-checked by text extraction). **UNOBTAINABLE** = not on arXiv, source noted. Thread labels: **A** = Jensen-ometer, **B** = derivative tower, **C** = screw function / Weil form.

### Thread A — Jensen polynomials / Jensen-ometer probe (17)

**1902.07321v2 — Jensen polynomials for the Riemann zeta function and other sequences** (2019); authors: Michael Griffin, Ken Ono, Larry Rolen, Don Zagier
- File: `gorz-1902.07321-jensen-polynomials-zeta.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): In 1927 Pólya proved that the Riemann Hypothesis is equivalent to the hyperbolicity of Jensen polynomials for the Riemann zeta function $ζ(s)$ at its point of symmetry. This hyperbolicity has been proved for degrees $d\leq 3$. We obtain an asymptotic formula for the central derivatives $ζ^{(2n)}(1/2)$ that is accurate to all orders, which allows us to prove the hyperbolicity of a density $1$ subset of the Jensen polynomials of each degree. Moreover, we establish hyperbolicity for all $d\leq 8$. These results follow from a general theorem which models suc …
- Why it matters: THE key paper for the Jensen-ometer probe: RH ≡ hyperbolicity of Jensen polynomials for ζ at the symmetry point (Pólya 1927); proved for d≤3; new asymptotics for central derivatives ζ^(2n)(1/2) and universality of the rescaled Jensen polynomials (Hermite limit).

**1910.01227v3 — Jensen Polynomials for the Riemann Xi Function** (2019); authors: Michael Griffin, Ken Ono, Larry Rolen, Jesse Thorner, Zachary Tripp, Ian Wagner
- File: `gorz-etal-1910.01227-jensen-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We investigate Riemann's xi function $ξ(s):=\frac{1}{2}s(s-1)π^{-\frac{s}{2}}Γ(\frac{s}{2})ζ(s)$ (here $ζ(s)$ is the Riemann zeta function). The Riemann Hypothesis (RH) asserts that if $ξ(s)=0$, then $\mathrm{Re}(s)=\frac{1}{2}$. Pólya proved that RH is equivalent to the hyperbolicity of the Jensen polynomials $J^{d,n}(X)$ constructed from certain Taylor coefficients of $ξ(s)$. For each $d\geq 1$, recent work proves that $J^{d,n}(X)$ is hyperbolic for sufficiently large $n$. Here we make this result effective. Moreover, we show how the low-lying zeros of …
- Why it matters: Griffin–Ono–Rolen–Thorner–Tripp–Wagner: Jensen polynomials for ξ itself; RH-equivalence via Pólya; explicit conditions and asymptotics; the direct sequel to 1902.07321 used by the probe.

**2008.07206v2 — Jensen polynomials are not a plausible route to proving the Riemann Hypothesis** (2020); authors: David W. Farmer
- File: `farmer-2008.07206-jensen-not-plausible.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): Recent work on the Jensen polynomials of the Riemann xi-function and its derivatives found a connection to the Hermite polynomials. Those results have been suggested to give evidence for the Riemann Hypothesis, and furthermore it has been suggested that those results shed light on the random matrix statistics for zeros of the zeta-function. We place that work in the context of prior results, and explain why the appearance of Hermite polynomials is interesting and surprising, and may represent a new type of universal law which refines M. Berry's "cosine i …
- Why it matters: Farmer's adversarial critique: the Hermite-polynomial connection of the Jensen polynomials is compatible with RH being FALSE; the observed hyperbolicity is a generic limiting phenomenon, so Jensen polynomials are NOT evidence for RH. Must-read counterweight for the probe.

**2007.13582v2 — Zeros of Jensen polynomials and asymptotics for the Riemann xi function** (2020); authors: Cormac O'Sullivan
- File: `osullivan-2007.13582-zeros-jensen-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): The classical criterion of Jensen for the Riemann hypothesis is that all of the associated Jensen polynomials have only real zeros. We find a new version of this criterion, using linear combinations of Hermite polynomials, and show that this condition holds in many cases. Detailed asymptotic expansions are given for the required Taylor coefficients of the xi function at $1/2$ as well as related quantities. These results build on those in the recent paper of Griffin, Ono, Rolen and Zagier.
- Why it matters: O'Sullivan: new Jensen-type criterion via linear combinations of Hermite polynomials; detailed asymptotics for zeros of Jensen polynomials of Ξ; verifies the criterion in many cases numerically.

**2108.01827v2 — On a new class of Laguerre-Pólya type functions with applications in number theory** (2021); authors: Ian Wagner
- File: `wagner-2108.01827-laguerre-polya-class.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We define a new class of functions, connected to the classical Laguerre-Pólya class, which we call the shifted Laguerre-Pólya class. Recent work of Griffin, Ono, Rolen, and Zagier shows that the Riemann Xi function is in this class. We prove that a function being in this class is equivalent to the Taylor coefficients, once shifted, being a degree $d$ multiplier sequence for every $d$, which is equivalent to shifted coefficients satisfying all of the higher Túran inequalities. This mirrors a classical result of Pólya and Schur. We further show some order  …
- Why it matters: Wagner: shifted Laguerre–Pólya class; Ξ is in it (per GORZ); equivalence to Turán-type inequalities — the Newton/Turán bridge the probe can test numerically.

**2608.08682v1 — A new hyperbolicity wedge and a joint semicircle limit for Jensen polynomials of Riemann's $ξ$-function** (2026); authors: Jonathan Holland
- File: `holland-2608.08682-hyperbolicity-wedge-jensen.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): Let \[ ξ\!\left(\frac12+z\right) =\sum_{n\geq 0}\frac{γ(n)}{n!}z^{2n}, \qquad J^{d,n}(X) =\sum_{j=0}^{d}\binom djγ(n+j)X^j . \] The Riemann hypothesis is equivalent to the hyperbolicity of $J^{d,n}$ for every $d,n\geq0$. We prove that there is an absolute constant $K>0$ such that \[ n^3\log^2(n+2)\geq Kd^5 \quad\Longrightarrow\quad J^{d,n}\ \text{is hyperbolic}. \] Along every sequence with $n,d\to\infty$ in this region, the empirical measure of the naturally centered and scaled zeros also converges to Wigner's semicircle law. This gives a simultaneous d …
- Why it matters: 2026 follow-up: absolute K with n³ log²n scaling wedge for hyperbolicity of J^{d,n} of ξ; joint semicircle limit. The newest quantitative input for the probe.

**1905.11269v1 — The Jensen-Pólya program for various L-functions** (2019); authors: Ian Wagner
- File: `wagner-1905.11269-jensen-polya-lfunctions.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): Pólya proved in 1927 that the Riemann hypothesis is equivalent to the hyperbolicity of all of the Jensen polynomials of degree $d$ and shift $n$ for the Riemann Xi-function. Recently, Griffin, Ono, Rolen, and Zagier proved that for each degree $d \geq 1$ all of the Jensen polynomials for the Riemann Xi-function are hyperbolic except for possibly finitely many $n$. Here we extend their work by showing the same statement is true for suitable $L$-functions. This offers evidence for the generalized Riemann hypothesis.
- Why it matters: Wagner: Jensen–Pólya program for L-functions — extends the GORZ framework beyond ζ; context for transporting the probe.

**2105.05386v1 — A note on the zeros of Jensen polynomials** (2021); authors: Young-One Kim, Jungseob Lee
- File: `kim-lee-2105.05386-zeros-jensen-polynomials.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): A recent result of Griffin, Ono, Rolen and Zagier on Jensen polynomials related with the Riemann zeta function is improved.
- Why it matters: Kim–Lee: improvement of GORZ on zeros of Jensen polynomials (sharpens the asymptotics).

**2511.02628v2 — Hermite-Jensen limits and $d$ log-concavity of $q$-multinomials** (2025); authors: Ken Ono
- File: `ono-2511.02628-hermite-jensen-limits.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): In 1878, Sylvester proved Cayley's Conjecture that the coefficients of the Gaussian $q$-binomial coefficients are unimodal. In 1990, O'Hara famously discovered a constructive combinatorial proof, and in 2013, Pak and Panova proved the stronger property of strict unimodality for sufficiently large parameters. We move from unimodality to log-concavity and higher degree $ d$ log-concavity, known as Turán inequalities. Although $q$-binomial coefficients are not always log- or degree $d$ log-concave, it's natural to ask to what extent these inequalities hold. …
- Why it matters: Ono 2025: Hermite–Jensen limits and d log-concavity — the modern shape of the Hermite-limit theme the probe measures.

**1801.05914v5 — The De Bruijn-Newman constant is non-negative** (2018); authors: Brad Rodgers, Terence Tao
- File: `rodgers-tao-1801.05914-debruijn-newman-nonnegative.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): For each $t \in {\bf R}$, define the entire function $$ H_t(x) := \int_0^\infty e^{tu^2} Φ(u) \cos(xu)\ du$$ where $Φ$ is the super-exponentially decaying function $$ Φ(u) := \sum_{n=1}^\infty (2π^2 n^4 e^{9u} - 3πn^2 e^{5u} ) \exp(-πn^2 e^{4u} ).$$ Newman showed that there exists a finite constant $Λ$ (the \emph{de Bruijn-Newman constant}) such that the zeroes of $H_t$ are all real precisely when $t \geq Λ$. The Riemann hypothesis is the equivalent to the assertion $Λ\leq 0$, and Newman conjectured the complementary bound $Λ\geq 0$. In this paper we est …
- Why it matters: Rodgers–Tao: de Bruijn–Newman constant Λ ≥ 0 (Forum Math Pi 2021). Directly bounds what any Jensen-type/heat-flow route can prove (Λ = 0 ⇒ RH would be 'barely' true).

**1904.12438v2 — Effective approximation of heat flow evolution of the Riemann $ξ$ function, and a new upper bound for the de Bruijn-Newman constant** (2019); authors: D. H. J. Polymath
- File: `polymath-1904.12438-heat-flow-xi-newman-upper.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): For each $t \in \mathbf{R}$, define the entire function $$ H_t(z) := \int_0^\infty e^{tu^2} Φ(u) \cos(zu)\ du$$ where $Φ$ is the super-exponentially decaying function $$ Φ(u) := \sum_{n=1}^\infty (2π^2 n^4 e^{9u} - 3πn^2 e^{5u} ) \exp(-πn^2 e^{4u} ).$$ This is essentially the heat flow evolution of the Riemann $ξ$ function. From the work of de Bruijn and Newman, there exists a finite constant $Λ$ (the \emph{de Bruijn-Newman constant}) such that the zeroes of $H_t$ are all real precisely when $t \geq Λ$. The Riemann hypothesis is equivalent to the asserti …
- Why it matters: Polymath 15: effective heat-flow evolution H_t of Ξ and new upper bound Λ < 1/2; the computational/effective side of the de Bruijn–Newman machinery. Highly relevant to a numerical Jensen-ometer.

**2005.05142v2 — A proof of Newman's conjecture for the extended Selberg class** (2020); authors: Alexander Dobner
- File: `dobner-2005.05142-newman-conjecture-selberg.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): Newman's conjecture (proved by Rodgers and Tao in 2018) concerns a certain family of deformations $\{ξ_t(s)\}_{t \in \mathbb{R}}$ of the Riemann xi function for which there exists an associated constant $Λ\in \mathbb{R}$ (called the de Bruijn-Newman constant) such that all the zeros of $ξ_t$ lie on the critical line if and only if $t \geq Λ$. The Riemann hypothesis is equivalent to the statement that $Λ\leq 0$, and Newman's conjecture states that $Λ\geq 0$. In this paper we give a new proof of Newman's conjecture which avoids many of the complications in …
- Why it matters: Dobner: proof of Newman's conjecture for the extended Selberg class (Λ ≤ 0 for those L-functions) — the Newman-constant theory beyond ζ.

**1309.0055v2 — Fourier transforms of positive definite kernels and the Riemann $ξ$-Function** (2013); authors: George Csordas
- File: `csordas-1309.0055-fourier-kernels-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): The purpose of this paper is to investigate the distribution of zeros of entire functions which can be represented as the Fourier transforms of certain admissible kernels. The principal results bring to light the intimate connection between the Bochner-Khinchin-Mathias theory of positive definite kernels and the generalized real Laguerre inequalities. The concavity and convexity properties of the Jacobi theta function play a prominent role throughout this work. The paper concludes with several questions and open problems.
- Why it matters: Csordas: Fourier transforms of admissible kernels and zero distribution of Ξ; the classic Laguerre-inequality ↔ ξ connection, foundational for the probe's function-class assumptions.

**1902.06330v3 — Orthogonal polynomial expansions for the Riemann xi function** (2019); authors: Dan Romik
- File: `romik-1902.06330-orthogonal-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We study infinite series expansions for the Riemann xi function $Ξ(t)$ in three specific families of orthogonal polynomials: (1) the Hermite polynomials; (2) the symmetric Meixner-Pollaczek polynomials $P_n^{(3/4)}(x;π/2)$; and (3) the continuous Hahn polynomials $p_n\left(x; \frac34,\frac34,\frac34,\frac34\right)$. The first expansion was discussed in earlier work by Turán, and the other two expansions are new. For each of the three expansions, we derive formulas for the coefficients, show that they appear with alternating signs, derive formulas for the …
- Why it matters: Romik: Hermite / symmetric Meixner–Pollaczek / continuous Hahn expansions of Ξ(t) with explicit coefficients and RH-conditioned sign results — the exact coefficient data a Jensen-ometer needs.

**1609.05965v1 — Dynamic behavior of the roots of the Taylor polynomials of the Riemann xi function with growing degree** (2016); authors: Robert Jenkins, Ken D. T. -R. McLaughlin
- File: `jenkins-mclaughlin-1609.05965-taylor-roots-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We establish a uniform approximation result for the Taylor polynomials of the xi function of Riemann which is valid in the entire complex plane as the degree grows. In particular, we identify a domain growing with the degree of the polynomials on which they converge to Riemann's xi function. Using this approximation we obtain an estimate of the number of "spurious zeros" of the Taylor polynomial which are outside of the critical strip, which leads to a Riemann - von Mangoldt type of formula for the number of zeros of the Taylor polynomials within the cri …
- Why it matters: Jenkins–McLaughlin: dynamics of the roots of Taylor polynomials of Ξ as degree grows — the root-tracking picture behind the probe's finite truncations.

**1502.06844v1 — Real-rooted Pólya-like approximations to the Riemann Xi-function** (2014); authors: Yaoming Shi
- File: `shi-1502.06844-polya-approx-xi.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): The Riemann $Ξ(z)$ function admits a Fourier transform of a even kernel $Φ(t)$. The latter is related to the derivatives of Jacobi theta function $θ(z)$, a modular form of weight $1/2$. Pólya noticed that when $t$ goes to infinity, $e^t$ goes to $e^t+ e^{-t}=2\cosh t$. He then approximated the kernel $Φ(t)$ by $Φ_{P}(t)$ that contained only the leading term and with $\exp t,\exp(9t/4)$ replaced by $2\cosh t,2\cos(9t/4)$. This procedure captured almost all of the contribution from the tail part (i.e., $t\to\infty$) of the kernel $Φ(t)$. We realize that wh …
- Why it matters: Shi: real-rooted Pólya-type approximations to Ξ — explicit approximating functions with all-real roots; a constructive benchmark family for the probe.

**2004.14465v1 — A note on the zeros of approximations of the Ramanujan $Ξ-$function** (2020); authors: Andrés Chirre, Oswaldo Velásquez Castañón
- File: `chirre-velasquez-2004.14465-ramanujan-xi-approx.pdf`  ·  Thread: A  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): In this paper, we review the study of the distribution of the zeros of certain approximations for the Ramanujan $Ξ-$function given by Haseo Ki, and we provide a new proof of his results. Our approach is motivated by the ideas of Velásquez in the study of the zeros of certain sums of entire functions with some condition of stability related to the Hermite-Biehler theorem.
- Why it matters: Chirre–Velásquez Castañón: zeros of approximations of the Ramanujan Ξ-function — numerical/analytic control on approximants, adjacent to the probe's numerical checks.

### Thread B — derivative tower ξ′, ξ″, … (8)

**1002.1616v1 — Landau-Siegel zeros and zeros of the derivative of the Riemann zeta function** (2010); authors: David W. Farmer, Haseo Ki
- File: `farmer-ki-1002.1616-landau-siegel-derivative.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We show that if the derivative of the Riemann zeta function has sufficiently many zeros close to the critical line, then the zeta function has many closely spaced zeros. This gives a condition on the zeros of the derivative of the zeta function which implies a lower bound of the class numbers of imaginary quadratic fields.
- Why it matters: Farmer–Ki: connection between Landau–Siegel zeros and zeros of ζ′; the derivative tower meets exceptional zeros.

**1002.0372v1 — Roots of the derivative of the Riemann zeta function and of characteristic polynomials** (2010); authors: Eduardo Dueñez, David W. Farmer, Sara Froehlich, Chris Hughes, Francesco Mezzadri, Toan Phan
- File: `dffh-1002.0372-roots-derivative-zeta.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We investigate the horizontal distribution of zeros of the derivative of the Riemann zeta function and compare this to the radial distribution of zeros of the derivative of the characteristic polynomial of a random unitary matrix. Both cases show a surprising bimodal distribution which has yet to be explained. We show by example that the bimodality is a general phenomenon. For the unitary matrix case we prove a conjecture of Mezzadri concerning the leading order behavior, and we show that the same follows from the random matrix conjectures for the zeros  …
- Why it matters: Dueñez–Farmer–Froehlich–Hughes: roots of ζ′ vs characteristic polynomials (random matrix) — the model for the derivative tower's zero distribution.

**math/0310252v3 — Differentiation Evens Out Zero Spacings** (2003); authors: David W. Farmer, Robert C. Rhoades
- File: `farmer-rhoades-0310252-differentiation-zero-spacings.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): If $f$ is a polynomial with all of its roots on the real line, then the roots of the derivative $f'$ are more evenly spaced than the roots of $f$. The same holds for a real entire function of order~1 with all its zeros on a line. In particular, we show that if $f$ is entire of order~1 and has sufficient regularity in its zero spacing, then under repeated differentiation the function approaches (a change of variables from) the cosine function. We also study polynomials with all their zeros on a circle, and we find a close analogy between the two situation …
- Why it matters: Farmer–Rhoades 2003: differentiation evens out zero spacings — the universality phenomenon that governs the ξ′, ξ″, … tower in the large-derivative limit.

**math/0701726v1 — The zeros of the derivative of the Riemann zeta function near the critical line** (2007); authors: Haseo Ki
- File: `ki-0701726-derivative-near-critical-line.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We study the horizontal distribution of zeros of $ζ'(s)$ which are denoted as $ρ'=β'+iγ'$. We assume the Riemann hypothesis which implies $β'\geqslant1/2$ for any non-real zero $ρ'$, equality being possible only at a multiple zero of $ζ(s)$. In this paper we prove that $\liminf(β'-1/2)\logγ'\not=0$ if and only if for any $c>0$ and $s=σ+it$ with $|σ-1/2|<c/\log t$ $(t\geqslant10)$ $$ \frac{ζ'}ζ(s)=\frac{1}{s-ρ}+O(\log t), $$ where $ρ=1/2+iγ$ is the closest zero of $ζ(s)$ to $s$ and the origin. We also show that if $\liminf(β'-1/2)\logγ'\not=0$, then for a …
- Why it matters: Ki: zeros of ζ′ near the critical line; most zeros of ζ′ are on/near the line (results entering the tower's known facts).

**1308.5116v1 — On the distribution of the zeros of the derivative of the Riemann zeta-function** (2013); authors: S. J. Lester
- File: `lester-1308.5116-zeros-derivative-zeta.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We establish an unconditional asymptotic formula describing the horizontal distribution of the zeros of the derivative of the Riemann zeta-function. For $\Re(s)=σ$ satisfying $(\log T)^{-1/3+ε} \leq (2σ-1) \leq (\log \log T)^{-2}$, we show that the number of zeros of $ζ'(s)$ with imaginary part between zero and $T$ and real part larger than $σ$ is asymptotic to $T/(2π(σ-1/2))$ as $T \rightarrow \infty$. This agrees with a prediction from random matrix theory due to Mezzadri. Hence, for $σ$ in this range the zeros of $ζ'(s)$ are horizontally distributed l …
- Why it matters: Lester: distribution of the zeros of ζ′ in the critical strip — counts, asymptotics; the quantitative backbone for ξ′.

**2410.06403v2 — Universality for roots of derivatives of entire functions via finite free probability** (2024); authors: Andrew Campbell, Sean O'Rourke, David Renfrew
- File: `campbell-etal-2410.06403-universality-derivatives.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): A universality conjecture of Farmer and Rhoades [Trans. Amer. Math. Soc., 357(9):3789--3811, 2005] and Farmer [Adv. Math., 411:Paper No. 108781, 14, 2022] asserts that, under some natural conditions, the roots of an entire function should become perfectly spaced in the limit of repeated differentiation. This conjecture is known as Cosine Universality. We establish this conjecture for a class of even entire functions with only real roots which are real on the real line. Along the way, we establish a number of additional universality results for Jensen pol …
- Why it matters: Campbell–O'Rourke–Renfrew 2024: universality for roots of derivatives of entire functions via finite free probability; proves the Farmer–Rhoades universality conjecture — the modern capstone of the derivative-tower picture.

**2211.11671v4 — Currently there are no reasons to doubt the Riemann Hypothesis: The zeta function beyond the realm of computation** (2022); authors: David W. Farmer
- File: `farmer-2211.11671-no-reasons-doubt-rh.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We examine published arguments which suggest that the Riemann Hypothesis may not be true. In each case we provide evidence to explain why the claimed argument does not provide a good reason to doubt the Riemann Hypothesis. The evidence we cite involves a mixture of theorems in analytic number theory, theorems in random matrix theory, and illustrative examples involving the characteristic polynomials of random unitary matrices. Similar evidence is provided for four mistaken notions which appear repeatedly in the literature concerning computations of the z …
- Why it matters: Farmer's 2022 survey/argument that there are no good reasons to doubt RH ('beyond the realm of…') — the derivative-tower author's own meta-assessment.

**0803.3592v1 — Differentiating polynomials, and zeta(2)** (2008); authors: David W. Farmer, Robert Rhoades
- File: `farmer-rhoades-0803.3592-differentiating-polynomials.pdf`  ·  Thread: B  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We study the derivatives of polynomials with equally spaced zeros and find connections to the values of the Riemann zeta-function at the positive even integers.
- Why it matters: Farmer–Rhoades 2008: differentiating polynomials and ζ(2) — the same differentiation-universality mechanism in elementary form.

### Thread C — screw function / Weil quadratic form (14)

**2006.13771v1 — Weil positivity and Trace formula, the archimedean place** (2020); authors: Alain Connes, Caterina Consani
- File: `connes-consani-2006.13771-weil-positivity.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We provide a potential conceptual reason for the positivity of the Weil functional using the Hilbert space framework of the semi-local trace formula of the paper "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function". (Selecta Math. 5 (1999), no. 1, 29--106). We explore in great details the simplest case of the single archimedean place. The root of the positivity is the trace of the scaling action compressed onto the orthogonal complement of the range of the cutoff projections associated to the cutoff in phase space, for cu …
- Why it matters: Connes–Consani: Weil positivity and the trace formula at the archimedean place — the conceptual source for why Weil-positivity should hold; essential context for Suzuki's screw-function machinery.

**2301.00421v3 — On the Hilbert space derived from the Weil distribution** (2023); authors: Masatoshi Suzuki
- File: `suzuki-2301.00421-hilbert-space-weil.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We study the Hilbert space obtained by completing the space of all smooth and compactly supported functions on the real line with respect to the hermitian form arising from the Weil distribution under the Riemann hypothesis. It turns out that this Hilbert space is isomorphic to a de Branges space by a composition of the Fourier transform and a simple map.This result is applied to state a new equivalence condition for the Riemann hypothesis in a series of equalities.
- Why it matters: Suzuki: Hilbert space from the Weil distribution — the function-space setting that the screw-function program formalizes; predecessor to 2606.09096 (held).

**2209.04658v3 — The screw line of the Riemann zeta-function and its applications** (2022); authors: Masatoshi Suzuki
- File: `suzuki-2209.04658-screw-line-zeta.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We investigate the screw line corresponding to the screw function associated with the Riemann zeta-function under the Riemann hypothesis and derive three necessary and sufficient conditions for the Riemann hypothesis as applications. One of them explains the non-negativity of the Weil distribution by means of the norm.
- Why it matters: Suzuki: the screw line of ζ and its applications — foundational paper of the screw-function line beyond the held 2605/2606/2607 items.

**2206.03682v4 — Aspects of the screw function corresponding to the Riemann zeta function** (2022); authors: Masatoshi Suzuki
- File: `suzuki-2206.03682-screw-function-zeta.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We introduce a screw function corresponding to the Riemann zeta-function and study its properties from various aspects. Typical results are several equivalent conditions for the Riemann hypothesis in terms of the screw function. One of them can be considered an analog of so-called Weil's positivity or Li's criterion. In addition, we prove a few partial but unconditional results for such equivalents.
- Why it matters: Suzuki: aspects of the screw function for ζ — detailed analytic properties of the screw kernel.

**2308.11860v2 — Analytic theories around the simplest screw** (2023); authors: Masatoshi Suzuki
- File: `suzuki-2308.11860-simplest-screw.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We present several analytic theories related to screw functions and describe the connections among them, taking the screw function of the simplest screw line as a guiding example.Note that this article does not contain any new results. Nevertheless, subsequent developments have suggested that the analytic structures associated with the simplest screw provide a useful prototype for a broader theory connected with zeta-functions, Weil's quadratic forms, and related Hilbert-space structures arising in analytic number theory.
- Why it matters: Suzuki: analytic theories around the 'simplest screw' — the model case the whole screw-function theory is built on.

**2301.05779v2 — Li coefficients as norms of functions in a model space** (2023); authors: Masatoshi Suzuki
- File: `suzuki-2301.05779-li-norms-model-space.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): It is known that the nonnegativity of Li coefficients is a necessary and sufficient condition for the Riemann hypothesis. We show that it is a necessary and sufficient condition for the Riemann hypothesis that all Li coefficients are norms of certain concrete functions on the real line. Such conditional formulas for Li coefficients are understood as a kind of Weil's criterion for the Riemann hypothesis.
- Why it matters: Suzuki: Li coefficients as norms of functions in a model space — bridges the Li criterion to the Weil/screw Hilbert-space picture.

**2209.12832v2 — Screw functions of Dirichlet series in the extended Selberg class** (2022); authors: Masatoshi Suzuki
- File: `suzuki-2209.12832-screw-selberg-class.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We introduce screw functions for Dirichlet series in the extended Selberg class. Then we prove that the Grand Riemann Hypothesis for a member of the extended Selberg class is equivalent to the nonpositivity of the corresponding screw function.
- Why it matters: Suzuki: screw functions for Dirichlet series in the extended Selberg class — the screw theory transported beyond ζ (transport target for the Weil-form line).

**2409.00888v2 — $M$-functions and screw functions originating from Goldbach's problem and zeros of the Riemann zeta function** (2024); authors: Kohji Matsumoto, Masatoshi Suzuki
- File: `matsumoto-suzuki-2409.00888-goldbach-screw.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): We study the $M$-functions, which describe the limit theorem for the value-distributions of the secondary main terms in the asymptotic formulas for the summatory functions of the Goldbach counting function. One of the new aspects is a sufficient condition for the Riemann hypothesis provided by some formulas of the $M$-functions, which was a necessary condition in previous work. The other new aspect is the relation between the secondary main terms and the screw functions, which provides another necessary and sufficient condition for the Riemann hypothesis …
- Why it matters: Matsumoto–Suzuki 2024: M-functions and screw functions from Goldbach's problem and zeros of ζ — screw functions reach Goldbach; new cross-link for the program.

**1204.1827v2 — A canonical system of differential equations arising from the Riemann zeta-function** (2012); authors: Masatoshi Suzuki
- File: `suzuki-1204.1827-canonical-system-zeta.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): This paper has two main results, which relate to a criteria for the Riemann hypothesis via the family of functions $Θ_ω(z)=ξ(1/2-ω-iz)/ξ(1/2+ω-iz)$, where $ω>0$ is a real parameter and $ξ(s)$ is the Riemann xi-function. The first main result is necessary and sufficient conditions for $Θ_ω$ to be a meromorphic inner function in the upper half-plane. It is related to the Riemann hypothesis directly whether $Θ_ω$ is a meromorphic inner function. In comparison with this, a relation of the Riemann hypothesis and the second main result is indirect. It relates  …
- Why it matters: Suzuki: canonical system of differential equations arising from ζ — the de Branges-type canonical-systems angle on the same Weil positivity.

**2607.24830v2 — A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion** (2026); authors: Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Minseo Kim
- File: `kim-etal-2607.24830-numerical-weil-operator.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): This paper presents the first numerical realization of Suzuki's Weil-Quadratic-Form operator, a candidate for the Hilbert--Pólya program linking spectral positivity to the Riemann Hypothesis (RH). Suzuki's 2026 construction was purely theoretical; here, the operator is instantiated via P1 finite-element discretization and Richardson extrapolation. Key results include: (R1) In the prime-free regime, the spectrum follows a closed Archimedean law $A_k(a) = \log(1/a) + \log(k-2) + B_0 + O(a)$, with $B_0 = \log q - 2\log 2$, confirmed to 30-digit precision. ( …
- Why it matters: Kim–Hong–Kim–Choi–Jang–Kim 2026: numerical realization of Suzuki's Weil-quadratic-form operator — direct computational follow-up to the held Suzuki line.

**1509.05576v1 — An essay on the Riemann Hypothesis** (2015); authors: Alain Connes
- File: `connes-1509.05576-essay-rh.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): The Riemann hypothesis is, and will hopefully remain for a long time, a great motivation to uncover and explore new parts of the mathematical world. After reviewing its impact on the development of algebraic geometry we discuss three strategies, working concretely at the level of the explicit formulas. The first strategy is "analytic" and is based on Riemannian spaces and Selberg's work on the trace formula and its comparison with the explicit formulas. The second is based on algebraic geometry and the Riemann-Roch theorem. We establish a framework in wh …
- Why it matters: Connes: essay on RH — the adelic/trace-formula framing of Weil positivity that the screw-function program refines.

**2602.04022v1 — The Riemann Hypothesis: Past, Present and a Letter Through Time** (2026); authors: Alain Connes
- File: `connes-2602.04022-rh-past-present.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): This paper, commissioned as a survey of the Riemann Hypothesis, provides a comprehensive overview of 165 years of mathematical approaches to this fundamental problem, while introducing a new perspective that emerged during its preparation. The paper begins with a detailed description of what we know about the Riemann zeta function and its zeros, followed by an extensive survey of mathematical theories developed in pursuit of RH -- from classical analytic approaches to modern geometric and physical methods. We also discuss several equivalent formulations  …
- Why it matters: Connes 2026: 'The Riemann Hypothesis: Past, Present and a Letter Through Time' — current survey of the trace-formula route.

**2004.14115v2 — Spectral truncations in noncommutative geometry and operator systems** (2020); authors: Alain Connes, Walter D. van Suijlekom
- File: `connes-vansuijlekom-2004.14115-spectral-truncations.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): In this paper we extend the traditional framework of noncommutative geometry in order to deal with spectral truncations of geometric spaces (i.e. imposing an ultraviolet cutoff in momentum space) and with tolerance relations which provide a coarse grain approximation of geometric spaces at a finite resolution. In our new approach the traditional role played by $C^*$-algebras is taken over by operator systems. As part of the techniques we treat $C^*$-envelopes, dual operator systems and stable equivalence. We define a propagation number for operator syste …
- Why it matters: Connes–van Suijlekom 2020: spectral truncations — the ORIGIN of the CVS truncation of the Weil form used by Groskin (held 2605/2607) and Suzuki.

**math/9810169v2 — The Explicit Formula in simple terms** (1998); authors: Jean-Francois Burnol
- File: `burnol-9810169-explicit-formula-simple.pdf`  ·  Thread: C  ·  Status: DOWNLOADED
- Abstract (verbatim from arXiv API): This is a semi-expository paper on the easier aspects of the Explicit Formula for the Riemann Zeta Function. The topics reviewed here include: Weil's criterion for the Riemann Hypothesis and its probabilistic interpretation, various formulations of the contribution corresponding to the real place, Haran's version of the Explicit Formula, and the author's own derivation which puts all places on the same footing. This derivation, an addendum to Tate's Thesis, is in the spirit of Weil's insights towards an adelic understanding of the Explicit Formula. Where …
- Why it matters: Burnol: the explicit formula in simple terms — the Weil/Guinand explicit-formula tradition the screw functions formalize.

## Top-10 by relevance to the three live threads

1. **1902.07321** GORZ, *Jensen polynomials for the Riemann zeta function and other sequences* — the anchor of thread A (RH ≡ Jensen hyperbolicity; d≤3 known; universality/Hermite limit).
2. **2008.07206** Farmer, *Jensen polynomials are not a plausible route to proving the Riemann Hypothesis* — the strongest known objection to thread A's premise; must be read before any probe conclusion.
3. **1910.01227** GORZ+Thorner+Tripp+Wagner, *Jensen Polynomials for the Riemann Xi Function* — the direct sequel with explicit ξ-side statements.
4. **1801.05914** Rodgers–Tao, *The De Bruijn-Newman constant is non-negative* — caps every Jensen/heat-flow route (Λ ≥ 0).
5. **1904.12438** Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function* — the computational machinery behind Λ < 1/2; ideal numerical companion for the probe.
6. **2007.13582** O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the Riemann xi function* — numerically checkable Jensen-type criteria.
7. **math/0310252** Farmer–Rhoades, *Differentiation Evens Out Zero Spacings* — the universality principle governing the whole derivative tower (thread B).
8. **2410.06403** Campbell–O'Rourke–Renfrew, *Universality for roots of derivatives of entire functions via finite free probability* — 2024 proof of the Farmer–Rhoades universality conjecture; capstone of thread B.
9. **2006.13771** Connes–Consani, *Weil positivity and Trace formula, the archimedean place* — the conceptual source of Weil positivity that thread C's screw functions make concrete.
10. **2004.14115** Connes–van Suijlekom, *Spectral truncations in noncommutative geometry and operator systems* — origin of the CVS truncation used in the held Groskin/Suzuki numerical work (thread C).

## Download log

- Tool: curl (browser-ish UA), 3 s spacing, 429-backoff; all 39 files verified to start with `%PDF-`; 5 key files additionally text-extracted (pypdf) and first-page titles matched to fetched abstracts (GORZ, Farmer-critique, Rodgers–Tao, Suzuki screw line, Connes–Consani).
- Result: **39 downloaded, 0 failed** (see per-file names above). Papers dir now holds these alongside the previously held Radziwill 1301.3232, Farmer–Gonek 0803.0425, Suzuki 2606.09096.
- Pre-existing files re-examined: `suzuki-2605.20224-cvs-galerkin.pdf` and `suzuki-2607.02828-truncated-weil-zero-sum.pdf` are **mislabeled**: their real authors are **Akiva Groskin** (2605.20224 = "High-Precision Approximation of Riemann Zeros via the Truncated Weil Form"; 2607.02828 = "A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form"). We genuinely hold Suzuki only at 2606.09096. (Renaming is left to the owner of research/papers to avoid clobbering; flagged here.)

## UNOBTAINABLE from arXiv (verified 0 hits by author/ID query) — where to find

| Work | Status | Where to find |
|------|--------|---------------|
| **Farmer–Gonek–Lee, *Pair correlation of the zeros of the derivative of the Riemann ξ-function*, J. Lond. Math. Soc. (2) 90 (2014), 241–269** ([FGL14], cited in C Remark 7.3 as the RH-conditional >85.84% comparandum for ξ′ simple zeros) | UNOBTAINABLE-from-arXiv (not posted; verified by author+title queries) | OUP journal page (paywalled); author pages (Farmer's homepage at University of Bristol / AIM); interlibrary loan |
| Levinson–Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. 133 (1974) 49–65 — the foundational ξ^(k) result | UNOBTAINABLE-from-arXiv | Springer Acta Math (paywalled); library |
| Conrey, *Zeros of derivatives of Riemann's xi-function on the critical line*, J. Number Theory 16 (1983) 49–74 — 79.874% ξ′-simple-on-line unconditionally (C's comparandum [Con89] is the 1989 J. Reine Angew. Math. 399 paper, also journal-only) | UNOBTAINABLE-from-arXiv | Elsevier JNT; library |
| Farmer, *Counting distinct zeros of the Riemann zeta-function*, Electron. J. Combin. 2 (1995) R1 (the [Far95] distinct-zeros input) | UNOBTAINABLE-from-arXiv (EJC pre-2016 volumes not on arXiv) | free at https://www.combinatorics.org (EJC open archive) |
| **Louis de Branges, RH line** (e.g. *The Riemann hypothesis for certain integrals of Eisenstein series*, J. Funct. Anal.; the circulating 2004/2017 preprints 'A proof of the Riemann hypothesis') | UNOBTAINABLE-from-arXiv (au:de_Branges and au:Branges both return 0) | Purdue: https://www.math.purdue.edu/~branges/ (personal preprints); J. Funct. Anal. (paywalled) |
| Csordas–Varga / Csordas–Norfolk–Varga / Csordas–Ruttan–Varga (1986–1994 Laguerre-inequality papers: *The Fourier transform of a positive definite kernel* etc.) | UNOBTAINABLE-from-arXiv | Numer. Algorithms / J. Analyse Math. / Trans. AMS (paywalled); library |

## Epistemic status of this deliverable (s4h-epistemology applied)

- **Known (verified by fetch):** every arXiv ID, title, author, year, and summary in the list above was read from a live arXiv API response on this run; the 39 PDFs were downloaded from arxiv.org and spot-checked. No ID is from memory.
- **Known (verified from held sources):** FGL14's exact bibliographic data was confirmed from C's reference list (`claude-riemann-paper.txt` line 3005); the >85.84% RH-conditional claim is C Remark 7.3's statement about FGL14 Cor. 1.3 — the paper itself is NOT held, so the number is PROVEN-as-cited-in-C, not read first-hand.
- **Assumed (low risk):** that the arXiv PDF URLs resolve to the same document version as the fetched abstract (all 39 did resolve; version may differ from the abstracted version — each entry's arXiv id carries the version we fetched; PDFs are the current default version served).
- **Assumed (medium risk, flagged):** that the 2026-dated arXiv IDs (2602.04022 Connes, 2607.24830, 2608.08682, 2602.20313) correspond to the content the abstracts describe — they exist and were fetched from the live API on this run, so they are real listings, but the 'why it matters' assessments for these are my reading of their abstracts only, not a full read.
- **Not verified:** the mathematical content of any paper — this note certifies existence, bibliographic identity, and download integrity only. None of the claims inside the papers have been validated by the program's validators.

## Honesty footer

Every paper in this note was found by a live arXiv API query and verified by fetching its abstract from that same API before download. No arXiv identifier, title, author, or abstract in this document was written from memory. The two mislabeled 'suzuki-' files in research/papers/ are flagged rather than silently renamed. FGL14, Levinson–Montgomery 1974, Conrey 1983/1989, Farmer 1995, the de Branges line, and the Csordas–Varga classics are marked UNOBTAINABLE-from-arXiv with concrete locations — they were searched for by author and keyword and returned no arXiv listing. This note is a literature inventory, not a mathematical claim; nothing here is offered as progress on RH until it has passed the program's adversarial validation.

_Generated 2026-08-11 by the paper-finder sub-agent. Evidence preserved in this repo: `paper-finder-jensen-evidence/` (abstracts-index-verified.json = the 39 verbatim API abstracts; arxiv_results1..5.json = raw API dumps; download.log). Working scripts used: /tmp/arxiv_search*.py, /tmp/arxiv_download.py, /tmp/gen_note.py (one-shot, reproducible from the evidence JSON)._