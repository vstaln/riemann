# Task: LIT — arXiv sweep on simple zeros / critical-line proportions / related techniques

## Role
LITERATURE SCOUT. Network is available directly from the phone (curl/urllib). Read PLAN.md and
`research/notes/discovery-gram-stability-673.md` for context first.

## Explicitly OUT OF SCOPE
Do NOT query "sixth moment + Riemann zeta" — another agent is already running that exact search on
the main machine. Do not duplicate it. Query the following DIFFERENT targets instead.

## Targets (run each against the arXiv API, sorted by submittedDate desc)
Use the export API: http://export.arxiv.org/api/query?search_query=...&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending
(with a polite UA, retries/backoff; the phone has direct internet).

1. **Simple zeros:** `all:"simple zeros" AND all:"Riemann zeta"` — recent results on the proportion
   of simple zeros (pre-2026 literature: Conrey–Ghosh–Gonek ~5/12 via mollifier; anything newer,
   ˝any unconditional improvements, or records).
2. **Zeros on the critical line (proportion records):** `all:"zeros on the critical line" AND
   (cat:math.NT)` or `all:"critical line" AND all:"proportion"` — anything post-2025 improving the
   Bui–Conrey–Young 41.05% / 41.28% / 41.6% records, and any papers citing or building on the
   Anthropic 67.25% result (search `all:"67.25"`, `all:"two thirds of the zeros"`).
3. **Weil quadratic form / rank–trace technique:** `all:"Weil quadratic form" AND all:"zeta"`,
   `all:"rank-trace inequality"`, `all:"von Neumann trace inequality" AND all:"zeta"` — is the
   compression/rank–trace technique being extended elsewhere?
4. **Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh:** `all:"Baluyot"` — the pair-correlation /
   simple-zeros inputs (arXiv:2306.04799, 2501.14545); any follow-ups.
5. **Gram-matrix / determinantal refinements:** `all:"Gram matrix" AND all:"Riemann zeta"`,
   `all:"gap distribution" AND all:"zeros"` — anything on consecutive-gap structure of ζ zeros.

For each found item: record arXiv id, title, date, one-line relevance to THIS program (simple-zeros
constant, on-line proportion, distinct zeros, stability refinement, the in-class ceiling), and
whether it's worth a deep read. If a paper is clearly irrelevant, skip it (keep the list tight).

## Deliverables
- `research/notes/literature-sweep-simplezeros.md` — dated table with the above columns, plus a
  "warm leads" paragraph: 3–5 items (if they exist) most worth the main program chasing, with a
  reason each. Be honest: an empty-but-honest sweep is a result; padding is not.
- Save the raw API responses used under `scratch/lit-*/` (one file per query) so numbers are
  reproducible.

## Compute budget
< 10 min wall; mostly network + parsing.
