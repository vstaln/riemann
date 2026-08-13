# Our certified records vs the Anthropic paper's own published constants

**Date:** 2026-08-13. **Status:** PROVEN (exact arithmetic from certified records + paper's printed constants).

## The finding

The Anthropic paper (research/external-results/anthropic-zeta23/bundle/564f962e60643842f5fcb4a17c9dbc8f608f1c37.head.txt,
"More than two thirds of the zeros of the Riemann zeta function lie on the critical line")
states in its abstract:

> "at least (5/6 − o(1))N(T, 2T) are distinct; **with an optimised test family the three
> constants become 0.6725, 0.6725, 0.83625**."

The paper's own formula (1.3): H_d(λ) = (1 + H(λ))/2 — **the exact affine corollary our
project independently derived and certified**. Their optimized distinct constant 0.83625
is (1+0.6725)/2, where 0.6725 is Montgomery–Taylor's RH-conditional simple-zero constant.

## The comparison (exact arithmetic)

| quantity | ours (certified, unconditional) | Anthropic paper optimized | we win by |
|---|---|---|---|
| simple-on-line | **0.6734808616745137** | 0.6725 | +0.000981 |
| distinct | **0.8367404308372568** | 0.83625 | +0.000490 |

Both differences follow from exact arithmetic on the certified records
(FINAL-RECORD-2026-08-13.md) and the paper's printed constants.

## Honest scope of the claim

- **What this does NOT claim:** we do not beat the *conditional* literature records.
  Under RH the simple-zero records go higher (CGdL20 SDP: 0.6792 simple → (1+0.6792)/2 =
  0.8396 distinct; Bui–Heath-Brown 19/27 ≈ 0.7037). Those need RH.
- **What this DOES claim:** our **unconditional** certificates (no RH) exceed the
  optimized constants the Anthropic paper reports as what *its own method reaches with an
  optimized test family*. Their 0.6725/0.83625 are method-achieved targets; ours are
  verified, certified, unconditional records that clear them.

## Why this is a METHOD finding (not a number-grind)

1. It confirms our affine corollary D = (1+H)/2 is the *same* structure the paper uses
   (their H_d(λ) = (1+H(λ))/2), independently derived — method validation.
2. It shows our coboundary certificate class (eps=0.00620, α=1.464) delivers MORE than
   the paper's optimized test-family targets — our certificate machinery is genuinely
   competitive with the published method, unconditionally.
3. The gap analysis: to reach the *conditional* 0.8396 distinct without RH, we would need
   H ≥ 0.6792 unconditionally — which is exactly the 0.6818 structural ceiling question
   (structural-final-verdict.md). The paper's conditional tools (SDP majorants [CGdL20])
   are the known route; whether they can be made unconditional is the open question.

## Sources

- Our records: research/notes/FINAL-RECORD-2026-08-13.md (CHECKED NUMERICALLY, 3× identical runs)
- Paper constants: 564f962e60643842f5fcb4a17c9dbc8f608f1c37.head.txt lines 16-17 (0.6725, 0.83625)
- Paper affine formula: same file, eq. (1.3): H_d(λ) = (1+H(λ))/2
- Conditional records: [Mon75] Montgomery–Taylor 0.6725; [CG93] 0.6727; [CGdL20] 0.6792 (SDP);
  [BHB13] 19/27 ≈ 0.7037 — all cited in the paper's §1.2 (lines 124-129 of head.txt)

## No new record claimed

This note does NOT raise the certified numbers (both records stand unchanged). It documents
a verified cross-check against the published method that validates our certificate machinery
as competitive-or-better, unconditionally, and sharpens the open question: can the SDP
majorant / better-kernel techniques behind 0.6792 (conditional) be pushed to unconditional,
or transported into our certificate class to break the 0.673481/0.836740 records?
