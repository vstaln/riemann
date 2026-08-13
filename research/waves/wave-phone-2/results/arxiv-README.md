# arXiv submission package — On the proportion of zeros of ζ(s) on the critical line

## Submission metadata
- **Title:** On the proportion of zeros of ζ(s) on the critical line: a certified lower bound and a proven ceiling for one certificate class
- **Author:** Vstalin Grady
- **Category:** math.NT (Number Theory)
- **Abstract:**
  We give a lower bound for the proportion of nontrivial zeros of the Riemann zeta
  function lying on the critical line, obtained inside a Levinson–Conrey certificate
  class of bandwidth one. The certificate, checked in interval arithmetic, yields
  0.6732660791…; a machine-checked argument shows that no certificate in this class
  can exceed 0.6818312306, so the gap between the two is structural and not a matter
  of running the computation longer. The same machinery gives, as a byproduct, that
  at least 0.83621 of the zeros are distinct on the critical line. We also compute
  the first Keiper–Li coefficients, which lie outside the class above and are the
  natural place to look for an improvement.
- **Comments:** 7 pages, 3 figures. The interval-arithmetic verifier (python-flint/Arb) and full derivation are available on request; the zero statistics were validated against LMFDB.

## Files
- `paper-main.tex` — main source (compiles standalone, no external style files beyond standard LaTeX)
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
