# Certified unconditional 67.3192911473% lower bound for simple zeros of the Riemann zeta function

This archive records the certified bound

    liminf_{T -> infinity} N_0^s(T, 2T) / N(T, 2T)
        >= 0.6731929114731422535099843283...
        = 67.3192911473142...%

The argument keeps the cosine window v(s)=cos(1.47 s) and adds a finite-memory
Bellman coboundary correction.  The local target is F_B >= 577/100000, with
block size m=183 and pressure tax 59/19520.

**Repository verification: PASSED.** The repository was independently rerun locally:
the directed-MPFR derivative table was regenerated, the GMP-backed exact-LDL
verifier compiled, and all 64 boxes returned verified=true.  The regenerated
derivative table is **not** byte-identical to the unavailable source ZIP
(local SHA-256 035946b4368fbeab578720109039bb409877f2c3728b672a1c1daff6c3e6f375;
source-package expectation 53e7f31fdc12f60a393dd5cf3963b544e18916859cb7ac8ce9ad935f644e8a24).
**External peer review: pending.** No external independent audit or peer review
has been performed.

The compiled paper is paper/riemann.pdf.  The source proof is
BELLMAN_COBBOUNDARY_PROOF.md, with the finite certificate in certificate/
and tools in tools/.

## Reproduce

On Windows, run scripts/verify.ps1.  It creates only a repository-local
.tmp_test_* workspace, regenerates the derivative table there, compiles the
GMP-backed verifier, and runs all 64 boxes without overwriting tracked data.

The derivative generator is a directed-MPFR reimplementation of the CWD2
format.  The stored CWK2 kernel table remains unchanged
(13213b84960fa629db0eac3ed7891148066313cba84f4fa151cfcce749d8fc2c).

## Result boundary and history

The current root result is the Bellman-coboundary bound above.  The preceding
67.3101784721425...% joint-window result is retained only as historical
material in the old release/tag and Zenodo archive; it is not the current
theorem or certificate.

The analytic framework is imported from the pinned upstream
ainta/zeta-simple-zeros commit
https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d.
Anthropic's nonnegative-window extension and the full trust boundary are
documented in docs/provenance.md.

Current publication metadata:

- Repository: https://github.com/tawanerguo-cn/zeta-simple-zeros
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.21890630
- Paper author: tawanerguo-cn
