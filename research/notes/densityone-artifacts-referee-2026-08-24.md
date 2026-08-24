# Artifacts referee — zeta-density-one-reproduction (JoshuaHKU, v0.92/v4)

Date: 2026-08-24. Referee: adventurer (read-only static audit; certify84/91 NOT executed —
cheap Fraction arithmetic on the printed constants was run to sanity-check decimals).
Repo (cloned): `~/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction`
HEAD `cdc2e41` ("New Zenodo DOI 10.5281/zenodo.22065921 …").

Headline under test: k=14 rung `simple > 0.9104604105…`, `distinct > 0.9552302052…`,
`lambda_7` an "exact 40-digit rational", Lean certificates, density-one capstone.

## CHECK (a) — do certify84/certify91 outputs contain the claimed constants?

**YES — the claimed k=14 rationals are present verbatim, exact, in both files.**
`certification/certify91.py` targets-dict, n=7 (line ~96):
```
7: (F(352633869846878511557783511830740995191, 7876602339133293193971616991853147607579),
    ...
652.../7876602339133293193971616991853147607579,   <- simple = 1-2*lambda_7
752.../7876602339133293193971616991853147607579,   <- distinct = 1-lambda_7
    F(9104,10000), F(9552,10000))                  <- "beats 0.9104 / 0.9552"
```
(lambda_7 numbers elided above; see file for the 39-digit numerator / 40-digit denominator.)
The chain re-computes `lam = 1/col[0]` by exact Hankel inversion from the moment tower
`m[0..14]` and asserts `lam == lt` (`F-lambda_7 exact value`), plus `zero premium`,
`alternating`, `H7 PD + shifted PD`, `k=14 headline = 1-2*lambda`, `distinct = 1-lambda`,
`beats 9104/10000 and 9552/10000`. So the k=14 rung is substantiated as an **exact rational**
with a self-contained certifier (stdlib `fractions.Fraction`, no external deps).

**Nuance:** certify91 does NOT print/assert the fuzzy decimals `0.9104604105` / `0.9552302052`
itself; it only checks the exact headlines and the coarse beats-thresholds 0.9104 / 0.9552.
The precise decimals live in README.md and `VERDICT_R153_K14.md`. I verified numerically
(CHECKED NUMERICALLY, cheap Fraction arithmetic):
`1 - 2*lambda_7 = 0.9104604105516693…` ✓ equals claim `0.9104604105…`;
`1 - lambda_7   = 0.9552302052758346…` ✓ equals claim `0.9552302052…`.
So the decimals are the correct expansions of the shipped exact rationals — consistent, not fabricated.

`certify84.py` analogously carries k<=8: lambda_3 = 247/2519, lambda_4 = 12241115/162540559,
headlines, and both-84/91 the sigma/m assemblies. certify84 header also self-admits one grade
caveat: none for the constants.

## CHECK (b) — is lambda_7 an exact rational; does Lean prove vs. take as input?

**lambda_7 IS written as an exact rational** in `certify91.py` (targets) and in
`lean/CertificateK14.lean` (as the constant inside the k=14 headline identities, e.g.
`(1 : Rat) - 2*(352633869846878511557783511830740995191/7876602339133293193971616991853147607579)
= 7171334599439536170856049968191665617197/7876602339133293193971616991853147607579 := by grind`).

**But Lean takes the 39/40-digit constant as a fed-in literal and only `grind`s arithmetic
consequences of it.** It proves that `1-2*lambda = headline`, that `headline > 9104/10000`, etc.
It does NOT derive lambda_7 from the moment tower, does not prove it is the Christoffel number,
and does not prove the underlying reduction (the Toeplitz-trace/recentring claims). The Lean
layer is an **arithmetic checker of the headline identities given the constants as inputs** —
a real but thin certificate; the provenance of lambda_7 as a Christoffel number is asserted
from the paper's chain, not formalized. (Not an `axiom`/`assume` — each theorem is proved by
`grind` on the stated Rat arithmetic — but the constants themselves are unproved inputs.)

## CHECK (c) — do the ACCEPTANCE gates test the actual claim or a proxy?

**Mixed: the constant rung is tested directly; the density-one capstone is NOT artifact-tested.**
- `repro/gates/g_certify91.py` ("F-CERT91") literally subprocess-wraps `certification/certify91.py`
  and passes iff the chain exits 0 — a direct test of the exact-rational k<=14 chain.
  `run_all.sh gates` runs 18 gates (incl. g_tt, g_be, g_certify84, g_certify91) → "ALL GATES GREEN".
- `g_be` (branch-equality) re-verifies the counting identities / signed assembly from JSON
  artifacts; `VERDICT_R153_K14.md` records a pre-registration/holdout discipline (deg-order
  adjudicator, timestamped predictions before computation) — these test the actual
  constant-production machinery, not a proxy.
- The **density-one capstone** (`lim N0^s/N = lim Nd/N = 1`) is a paper theorem
  (README: "the analytic chain is graded certified-candidate pending external review");
  it is NOT gated by any reproduce-able artifact. The repo substantiates the deepest *instantiated
  rung* (k=14) numerically/proof-level-for-constants, not the unconditional limit theorem itself.

## CHECK (d) — placeholders / fabrication / mismatches

- **Lean compile-status mismatch (flagged):** README.md states `lean/` "compiled 3/3 modules",
  and REPRODUCTION.md §3 says `lake build -> builds Certificate84, CertificateK1012, CertificateK14`.
  But the shipped .lean files' own headers contradict this:
    - `lean/Certificate84.lean` header: *"…queued for the maintainers' same-machine compile.
      代理核验，待同机编译.* (proxy-verified, awaiting same-machine compile.)"
    - `lean/CertificateK14.lean` header: *"To be compiled on the program director's toolchain."*
  So the repo simultaneously claims "compiled 3/3" (README/REPRODUCTION) while the files
  themselves say "queued / to be compiled". This is at minimum a stale-header inconsistency and,
  absent a compiled `.olean` in-repo, the "compiled" claim is not evidenced by the artifacts.
  (I did not run `lake build`; verdict on actual compileability is INCONCLUSIVE, but the shipped
  headers alone undermine the README claim.)
- **No hardcoded-output fabrication found in the certifiers:** certify84/91 genuinely recompute
  (`inv_col0` exact Gaussian elimination on the Hankel matrix, `minors_pos` leading minors) rather
  than echo constant strings; the printed rationals are the *targets*, recomputed `lam` is asserted
  equal to them. This is a real computation, not a stamped value.
- **Decimal literals are correct expansions** (see (a)) — no misleading digit inflation.
- Verse in `VERDICT_R153_K14.md` r156 correction explicitly confesses a prior 9-digit rounding
  (`0.910460411` → exact `0.9104604105…`), which is the honesty-positive sign of a real chain.
- **Zenodo DOI consistent:** `10.5281/zenodo.22065921` appears in `paper.tex:83-84`,
  `paper-zh.tex:45-46`, and the HEAD commit message. **No CITATION.cff** file found.
- `MANIFEST.json` is a real sha256/short-hash manifest of engines/hosts/constants incl. a
  `grade_note` that honestly admits C8's model-side check "BOUNDS but does not independently
  re-derive" (candidate 7/180 missed true 157/4032 by 4.96e-5). Sign of genuine provenance
  record-keeping, not a legible cover-up.

## OVERALL VERDICT (one line)

**PARTIAL —** the shipped artifacts genuinely substantiate the k=14 exact-rational rung
(0.9104604105…/0.9552302052…, lambda_7 as a 39/40-digit exact rational, with a self-contained
certifier and gates that test the real chain), BUT the Lean "certificates" take lambda_7 as a fed
literal and only grind head-line arithmetic, the README "compiled 3/3" claim is contradicted by the
files' own "queued / to be compiled" headers, and the density-one capstone itself is graded
certified-candidate, not artifact-verified.

## Sharpest quotes (file:line / file header)

1. `certification/certify91.py` (targets, n=7): `F(352633869846878511557783511830740995191,
   7876602339133293193971616991853147607579)` with `check(f"k={2*n} headline = 1-2*lambda",
   1-2*lam == ht)` and `beats {hb}/{db}` — the exact k=14 rational + threshold, re-derived by
   Hankel inversion, not stamped.
2. `lean/CertificateK14.lean` header: `To be compiled on the program director's toolchain.`
   and `lean/Certificate84.lean` header: `queued for the maintainers' same-machine compile.
   代理核验，待同机编译` — vs README.md `compiled 3/3 modules`. Shipped claim contradicts
   its own files.
3. `repro/VERDICT_R153_K14.md` (r156 audit correction): `0.910460411 系九位舍入值；精确小数为
   0.9104604105...` — exact decimal reconciled after a self-reported rounding slip.
4. `repro/MANIFEST.json` grade_note: C8's second path `BOUNDS but does not independently
   re-derive it -- the pre-registered candidate 7/180 missed the true value 157/4032 by
   4.96e-5, so the model check is not a confirmation` — honest non-confirmation is disclosed.
