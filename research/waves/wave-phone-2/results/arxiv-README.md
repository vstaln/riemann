# arXiv submission package — On the proportion of zeros of ζ(s) on the critical line

## Submission metadata
- **Title:** On the proportion of zeros of ζ(s) on the critical line: a certified lower bound and a proven ceiling for one certificate class
- **Author:** Vstalin Grady
- **Category:** math.NT (Number Theory)
- **Abstract** (matches `paper-main.tex` abstract verbatim; paste this into the arXiv abstract field):

  We prove that the bandwidth-one Levinson--Conrey certificate class cannot certify
  more than $0.6818312306$ of the zeros of $\zeta(s)$ on the critical line, and we
  exhibit a certificate in that class that certifies $0.6732660791\ldots$. The ceiling
  is machine-checked: any certificate reading only the mean density, the
  pair-correlation form factor on $[0,1]$, and multiplicity integrality is valid
  against a witness configuration with simple-point fraction
  $p_0=0.68182868746\ldots$, and the $1/(6\cdot256^2)$ correction is the
  discretization defect of the formalization. The lower bound is certified in interval
  arithmetic (python-flint/Arb) at threshold $\epsilon=8065\times10^{-6}$ on a grid of
  $4000$ points. The two numbers bracket the class. The same bookkeeping gives at
  least $0.83621$ for the proportion of distinct points on the line, and the first
  twelve Keiper--Li coefficients, computed to twenty digits, lie outside the class,
  where the ceiling does not apply.

- **Comments:** 7 pages, 3 figures. The interval-arithmetic verifier (python-flint/Arb) and full derivation live in the companion repository (the riemann git repository, commit hash at publication); the zero statistics were validated against LMFDB.

## Files
- `paper-main.tex` — main source (compiles standalone, standard LaTeX only)
- `figures/fig1_certified_bound.png`, `figures/fig2_li_coefficients.png`, `figures/fig3_spacing_stats.png`

## Compile
```
pdflatex paper-main.tex && pdflatex paper-main.tex
```

## Honesty statement (per the author's charter)
- Theorem 1 (0.6732660791…) is **numerically certified** (interval arithmetic, grid 4000), not a hand-proved theorem.
- Theorem 2 (0.6818312306…) is **machine-checked** within the same framework.
- Theorem 3 (0.83621…) is a **distinct-zeros** bound (N_d = s1+s2+2p), NOT a simple-zeros bound; Section 4 states this explicitly.
- The moments used are unconditional; the bound is not conditional on any pair-correlation conjecture about the zeros. The conjectural barrier to further improvement is the sixth/higher moment of |ζ(1/2+it)| (Keating–Snaith).
- Published unconditional record: 5/12 ≈ 0.4167 (Pratt–Robles–Zaharescu–Zeindler 2020). Our 0.6733 is a certificate-defined statistic, shown against 5/12 for scale in Figure 1.
