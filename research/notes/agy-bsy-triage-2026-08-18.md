# Antigravity BSY route triage — 2026-08-18

## Source

Fresh one-shot `agy` idea spike, instructed to avoid all closure-DAG routes. It returned the
Poisson-weighted critical-line log-modulus integral associated with the Balazard–Saias–Yor
criterion:

`I = (1/pi) integral_0^infinity log|Z(t)|/(1/4+t^2) dt`.

## Adjudication

**Status: DUPLICATE / CONSISTENCY-ONLY — CLOSED.**

The useful identity is the classical potential-theoretic criterion

`I = sum_{beta>1/2} log |rho/(rho-1)|`,

with positive terms for every off-line zero in the right half of the strip. Thus `I >= 0`
unconditionally and `I <= 0` implies RH. But the same identity makes `I=0 <=> RH`; the
proposed inequality is not a genuinely new one-way mechanism, only a restatement with an
inequality wrapper. This is exactly the explicit-formula/potential-theory trap already closed
in `research/notes/crossdomain-hunt-2026-08-18.md`.

The output's expected finite-T values for zeta, planted zeros, and Davenport–Heilbronn were
not accompanied by executable Rust code or certified tail bounds. They are **UNVERIFIED** and
no numerical probe was funded because the closure gate rejects the route before computation.
The RH-false control logic is conceptually correct (an off-line zero contributes positively),
but does not rescue the novelty failure.

## Next move

Do not re-probe BSY, Poisson–Jensen, Weil positivity, or any equivalent log-modulus criterion.
Search for a condition whose hypothesis is strictly weaker than RH and whose proof for zeta
would use a new object rather than evaluating a known RH-equivalent functional.
