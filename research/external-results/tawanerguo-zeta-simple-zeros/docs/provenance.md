# Provenance and trust boundary

The general-window analytic framework and the coarser
`min(1,E)` Gram-defect lemma are imported from the upstream archive
ainta/zeta-simple-zeros at pinned commit
040c5e899e658aed7b56a2a87f501798fe10761d:
https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d

The stability-enhanced rank-trace/Phi envelope used by the preceding v67.310
release was developed in this repository; it is not attributed to that
upstream commit.  The pinned upstream material is likewise not cited as a
proof of the new Bellman-coboundary finite implication.  The
nonnegative-window extension is Anthropic's official PDF, Section 7.1,
equations (7.1)--(7.3):
https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf

The checked Anthropic PDF has SHA-256
6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72e.
At bandwidth lambda=1 its c_lambda(v) formula is the c_1(v) functional used
by the cosine window.

Current new material is the alpha=147/100 joint window, Bellman-coboundary
redistribution, directed-MPFR CWD2 derivative table, convex-tangent
seven-point certificate, exhaustive 64-box driver, and arithmetic combination
leading to 0.6731929114731422535099843283....

The source derivative ZIP/table was unavailable.  The repository therefore
contains an independent directed-MPFR reimplementation with local SHA-256
035946b4368fbeab578720109039bb409877f2c3728b672a1c1daff6c3e6f375.  The
source-package expected hash
53e7f31fdc12f60a393dd5cf3963b544e18916859cb7ac8ce9ad935f644e8a24 is retained
only in certificate/source-package-audit.txt and is not claimed byte-identical.

Repository verification passed locally: the directed final-bound bracket
matched, the GMP-backed exact-LDL verifier compiled, and all 64 boxes passed.
This is not external independent verification, formal proof checking, or peer
review; external peer review remains pending.  The preceding
67.3101784721425...% result is historical material only.
