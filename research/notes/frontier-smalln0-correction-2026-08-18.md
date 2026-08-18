# Frontier-smalln0-slice: PROVEN-CLOSED verdict VOID — sign/criterion error (CORRECTION)

Date: 2026-08-18. Labels: **CORRECTION — the prior verdict is void**; underlying claims
re-verified from the certified 210-bit g02 table (`research/notes/g02-moments-oracle-2026-08-18.txt`).
Antigravity second opinion (`agy`, gemini-3.7-flash-high default) independently confirmed the sign
analysis; every number below was re-computed in Rust from the certified table
(`tools/g02-oracle/src/bin/jensen_check.rs`, output `research/notes/jensen-check-output-2026-08-18.txt`).

## What the frontier note claimed

`frontier-smalln0-slice-2026-08-18.md` closed the campaign's last structural opening — the fixed-n0
Jensen slice (GJT-completion) — as **PROVEN-STUCK**:

> Hankel det2(γ) = γ0·γ2 − γ1² = −9.19e-6 < 0 ⟹ "γ is NOT a moment sequence" ⟹
> "no Hankel/Toeplitz positivity of gamma can be inherited from Phi > 0" ⟹
> "the small-n Jensen decomposition route is now PROVEN CLOSED as a one-way path."

The destroying result: the n!/(2n)! renormalization breaks the Hankel total positivity that the
positive measure Φ>0 gives to the moment sequence M. Verdict: PROVEN-STUCK.

## The error: the note tested the WRONG criterion and got the SIGN backwards

**1. Sign error.** The degree-2 Jensen polynomial is J^{2,0}(X) = γ0 + 2γ1X + γ2X². Its discriminant is

    Δ = (2γ1)² − 4γ0γ2 = 4(γ1² − γ0γ2) = −4·det2(γ).

Hyperbolicity (two real roots) ⟺ Δ ≥ 0 ⟺ γ1² ≥ γ0γ2 ⟺ **det2(γ) ≤ 0**. The note's "destroying"
number det2 = −9.19e-6 < 0 is *exactly* the hyperbolicity condition for J^{2,0}. The moment-sequence
test (det2 ≥ 0) has the OPPOSITE sign requirement: a moment sequence would make J^{2,0} **non**-hyperbolic.

**2. Criterion error.** The note tested Hankel (moment) minors. Jensen hyperbolicity in the GJT
setting is a Toeplitz / Pólya-frequency criterion, not a Hankel one — the campaign's own
li-structure-audit states verbatim: "Jensen criterion = PF (Toeplitz TP), never Hankel." Hankel
positivity of γ is neither necessary nor sufficient for Jensen hyperbolicity.

**3. The correct PF sequence passes.** The relevant PF sequence is the Taylor-coefficient sequence
a_k = γ_k/k! = M_k/(2k)! (with the alternating sign of Ξ's Taylor expansion factored out), NOT γ_k
itself — the k! factor destroys Toeplitz-TP. Verified from the certified table (all Rust, f64):

| Test | Sequence | Result |
|------|----------|--------|
| PF2 (log-concavity) | a_k = γ_k/k! | ✓ all n ≤ 39 |
| Toeplitz 3×3 minors | a_k | ✓ all ≥ 0, rows(1..9) |
| Toeplitz 4×4 minor | a_k | ✓ +1.1167e-9 |
| J^{2,n} real roots | γ | ✓ n ≤ 19 |
| J^{3,n} 3 real roots | γ | ✓ n ≤ 11 (cubic Δ > 0) |
| J^{4,n} 4 real roots | γ | ✓ n ≤ 7 |
| log-concavity γ(n+1)²−γ(n)γ(n+2) | γ | ✓ all n ≤ 39 (this was the note's OWN unreported check) |

For contrast: γ itself fails the Toeplitz 3×3 test (det = −7.0e-8) — that is the *renormalized*
sequence, not the Taylor coefficients, and it is irrelevant to the Jensen criterion. The fast-thinker
hand-computed the same 3×3 minor on a: +3.1118e-7; my Rust: +3.1121e-7. Match.

## The corrected verdict

- **The PROVEN-STUCK verdict on the small-n Jensen slice is VOID** as stated: it rests on a
  sign-inverted Hankel test applied to the wrong sequence. The GJT-completion opening is NOT closed
  by this argument.
- What the note's data *actually* established: M is a moment sequence (true, Φ>0), and γ is not a
  Hankel moment sequence (true, but irrelevant — Jensen is Toeplitz/PF).
- What survives: the *structural* part of the note's argument — a fixed-n0 hyperbolicity proof
  covers measure-zero of the (n0,d) lattice and cannot reach RH without a global argument. That is
  the genuine (hard) content of GJT-completion; it is Farmer's diagnostic, not a closure.
- The finite PF2/PF3/PF4 passes are **consistency diagnostics only**: PF_∞ (all minors, all orders)
  ⟺ Ξ ∈ LP ⟺ RH, so a finite pass is RH-consistent evidence, never a proof, and a finite check
  cannot certify the infinite PF property. (This is the same firewall as every other finite probe.)

## Honest status of the route

The small-n Jensen slice is **OPEN** again (it was closed by an erroneous argument), but its
difficulty is unchanged: RH ⟺ all J^{d,n} hyperbolic, the large-(d,n) wedge is proven, and the
small-n complement is the RH-equivalent core. The moment-structure mechanism (Φ>0 ⟹ PF of the Taylor
coefficients) is NOT established: PF is a stronger statement than any finite check, and no theorem
transports the positive-measure structure of M to PF_∞ of a. This correction reopens the lane for
future levers; it does not by itself advance a proof.

## Antigravity note (process)

Per hooks/agents.md, one fresh `agy -p` second opinion was used (gemini-3.7-flash-high, high effort;
the CLI default model is that model — the `--model`/`--effort` flags currently trigger a greeting-only
bug in print mode, so the working invocation is plain `agy -p "<prompt>"`). Its output was treated as
an idea source only; all claims were re-verified in Rust against the certified table.

## Files

- Probe: `tools/g02-oracle/src/bin/jensen_check.rs`; output: `research/notes/jensen-check-output-2026-08-18.txt`
- Corrected note: this file. Prior: `frontier-smalln0-slice-2026-08-18.md` (verdict section now
  superseded; see DAG + ledger updates).
