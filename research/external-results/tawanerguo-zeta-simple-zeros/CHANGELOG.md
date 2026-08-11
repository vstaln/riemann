# Changelog

## 0.1.4 — 2026-08-12

- Promoted the Bellman-coboundary result to the current theorem:
  0.6731929114731422535... (67.3192911473...%), with local target
  F_B >= 577/100000, block size m=183, and pressure tax 59/19520.
- Added the CWD2 derivative-table generator, GMP-backed exact-rational LDL
  verifier, new certificate logs, and the tracked derivative table.
- Independent local rerun passed all 64 boxes. The source ZIP expected
  derivative hash was unavailable; the locally regenerated table has a
  different hash and is explicitly labeled as an independent reimplementation.

## 0.1.3 — 2026-08-11

- Corrected the preferred citation target from the first archived version DOI
  `10.5281/zenodo.21890631` to the all-versions concept DOI
  `10.5281/zenodo.21890630`, so the citation resolves to the latest archived
  release containing the paper.
- Verification: recompiled the paper, visually inspected the affected page,
  and regenerated and checked the complete SHA-256 manifest.

## 0.1.2 — 2026-08-11

- Added an all-English mathematical paper in LaTeX and compiled PDF form,
  presenting the certified `67.3101784721425...%` theorem, proof architecture,
  interval certificate, trust boundary, and reproducibility procedure.
- Linked the paper and the first published Zenodo archive from the README, and
  initially recorded version DOI `10.5281/zenodo.21890631` in the citation
  metadata; version `0.1.3` switches the preferred citation to the concept DOI.
- Verification: the paper was compiled and visually inspected page by page;
  the complete repository verification and manifest checks were rerun after
  adding the publication artifacts.

## 0.1.1 — 2026-08-11

- Rewrote public-facing prose in English and updated the README first screen
  with searchable theorem terms for the unconditional simple-zero lower bound.
- Expanded citation keywords and aligned the citation metadata with the
  fixed research release identifier `67.3101784`; the local verification
  status remains explicit about the absence of external independent audit or
  peer review.
- Full local verification rerun passed after the documentation-only changes:
  the bound was reproduced, the MPFR kernel table was byte-identical, all 64
  certificate boxes returned `verified=true`, and manifest coverage and hashes
  remained consistent.

## 0.1.0 — 2026-08-11

- Archived the `67.3101784721425...%` joint-window proof, certificates, MPFR
  kernel table, and verifier tools.
- Added a self-contained trace--energy envelope derivation, provenance pin,
  manifest coverage, a Windows rerun script, deterministic LF checkouts, and
  local build-artifact ignores.
- Local rerun passed: bound reproduced, kernel table byte-identical, and all
  64 certificate boxes returned `verified=true`; no external independent audit
  or peer review has been performed.
