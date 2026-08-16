# Corner (d) — ξ′-two-trace DISTINCT-bound transport: does it raise ζ distinct beyond 0.836740?

**Date:** 2026-08-18. **Agent:** builder. **Status:** CLOSED.
**Verdict:** the transport is STRUCTURALLY INVALID — ξ′ distinct-on-line ≥ 0.92919 provides
NO lower bound on ζ distinct-on-line. The 0.836740 distinct-on-line record STANDS as terminal.
No new record. (Firewall binding: this is a proportion/simple-fraction result — zero RH evidence,
in either direction.)

**Labels:** read-class overlap analysis = PROVEN from the structural formulas in attack-xiprime.md
(cited below); transport-failure mechanism = PROVEN analytically + CHECKED NUMERICALLY (toy
interlacing count, Rust); verdict = CHECKED NUMERICALLY / CLOSED.

---

## 0. Summary

- **Part A (read-class):** The ξ′-two-trace certificate reads the SAME data class as the
  0.836740 ζ certificate — a single-window functional {mean + in-band pair-density + integrality}.
  It does NOT use two independent in-band reads at different heights. The "two-trace" name refers
  to the rank-trace structure (mean trace + pair-density trace), which is common to BOTH the ζ and
  ξ′ methods. So the read is INSIDE the ceiling's data class.
- **Part A (transport):** Even if ξ′ distinct were proven = 1, it would NOT force ζ distinct > 0.
  **A double ζ zero collapses to a SIMPLE ξ′ zero**, so ξ′ distinct-on-line is blind to the exact
  mechanism (ζ multiplicity collapse) that lowers ζ distinct-on-line below 1. The transport
  inequality ξ′-distinct ⟹ ζ-distinct does not exist.
- **Part B/C:** The two independent checks are moot because the transport is invalid at the
  structural level. No new record. Corner (d) closes honestly.

---

## 1. Part A — read-class overlap analysis

### 1.1 What the 0.836740 ζ certificate reads (FINAL-RECORD + wave7-certificate-documented)

The ζ record is built from a single cosine-window functional at α=1.464, m=171, with a coboundary
redistribution. Per attack-xiprime.md §3, the ζ-method window functional is

    c_λ(v) = λ(∫v)² / (∫v² + λ²∬_{[−½,½]²} |s−s′| v(s)v(s′) ds ds′),

whose HS-norm constant is 1/c₁(v₀) = Q(v₀) = ½ + (1/√2)cot(1/√2) = 1.3274993…, giving
simple ≥ 2 − Q = 0.67250 and (via the PROVEN affine corollary) distinct = (1+simple)/2
≥ 0.836740. The data read per window is: **mean (∫v)², in-band second moment ∫v², and the
|s−s′| pair-density autocorrelation** — a single window, single trace. This is the data class the
Lean ceiling law (ceiling_law256) governs: {mean + in-band F + integrality}, degree/data-independent.

### 1.2 What the ξ′-two-trace certificate reads (attack-xiprime.md §3, verbatim structure)

The ξ′-method (Remark 7.3, Lean XiPrime/Defs.lean) is:

    c_λ^(1)(v; D₁) = λ(∫v)² / (∫v² + λ·𝒥_{D₁}(λ;v)),  𝒥_{D₁}(λ;v) = 2∫₀¹ D₁(λr)(v⋆v)(r) dr,

with the pair density D₁(r) = r − 4r² + Σ_{k≥0} D1coeff(k)·r^{2k+3} replacing ζ's |s−s′| kernel.
κ₁(λ,v) = 1/c_λ^(1)(v;D₁); distinct ≥ 3/2 − κ₁/2 = 0.92919 (flat). The note states explicitly:
**"Both are rank–trace two-trace certificates; the difference is the trace functional (which
density sits in the second trace)."**

### 1.3 Verdict: the read class is THE SAME, not richer

The decisive structural fact: **"two-trace" does NOT mean "two independent in-band reads at
different heights."** It names the internal rank-trace structure — a mean trace plus a
pair-density (second) trace — which is present in BOTH the ζ and ξ′ methods. The ONLY difference
is WHICH density occupies the second trace (|s−s′| for ζ, D₁ for ξ′), and the object whose zeros
are counted (ζ zeros vs ξ′ zeros). The per-window data read is structurally identical:
{mean, in-band second moment, pair-density autocorrelation}, on a single window.

**Therefore: the ξ′-two-trace read is INSIDE the ceiling's data class, not outside it.** The
brief's hypothesis ("does the two-trace use two independent in-band reads at different heights,
giving genuinely more information") resolves to NO. There is no extra information to escape the
ceiling law.

### 1.4 The transport inequality (Part A Q3) — does ξ′ distinct ⟹ ζ distinct?

This is the deeper and decisive failure. Let ρ_ζ = N_ζ^d/N_ζ (proportion of ζ zeros at distinct
heights) and ρ_ξ′ = N_ξ′^d/N_ξ′.

Interlacing structure (attack-xiprime.md, PROVEN/CHECKED): ξ′ has one zero per gap between
consecutive distinct ζ heights, PLUS a zero of multiplicity (m−1) at any ζ height of multiplicity
m ≥ 2 (Rolle: derivative of a function with a double zero vanishes there).

**Key collapse:** a ζ zero of multiplicity m=2 (a double zero — the cheapest way to lower ζ
distinct) becomes a SIMPLE ξ′ zero. Counting ξ′ distinct, that double-ζ height contributes
1 distinct ξ′ zero (the same as a simple-ζ zero would, via its gap). So:

- ξ′ distinct-on-line counts gap zeros (all at distinct heights) + one per multiple-ζ height.
- The multiplicity collapse in ζ (which is EXACTLY what drives ρ_ζ below 1) is INVISIBLE to ρ_ξ′.

**Explicit counterexample (toy, all-multiplicity-2):** suppose ζ has M distinct heights, each with
multiplicity 2 (and the rest simple). Then N_ζ = 2M, N_ζ^d = M, so ρ_ζ = 1/2. But ξ′ has
(M−1) gap zeros + M simple zeros at the double heights = (2M−1) zeros, ALL at distinct heights,
so ρ_ξ′ = 1. Hence **ρ_ζ = 0.5 with ρ_ξ′ = 1 is fully compatible** — ρ_ξ′ ≥ 0.92919 imposes NO
lower bound on ρ_ζ.

**Transport inequality: there is none.** The brief's framing "how ξ′ distinct 0.92919 constrains
ζ distinct" has the honest answer: it constrains it not at all. ξ′ distinct is blind to exactly the
multiplicity collapse that lowers ζ distinct.

---

## 2. Part B — numerical verification (bounded)

Since the transport is structurally invalid, a full 924k-zero two-window sweep on ζ would only
re-confirm the ceiling (the read class is identical), not produce a record. Instead I verified the
two load-bearing claims with a bounded toy interlacing count:

1. **Double-zero blindness (the mechanism above):** a ζ sequence with double zeros yields ρ_ζ < 1
   while ρ_ξ′ = 1. CHECKED NUMERICALLY (Rust, toy interlacing: build ξ′ zeros as one-per-gap +
   (m−1) per multiple height, count distinct proportions for a planted double-heavy ζ).
2. **Same functional class:** confirmed from the structural formulas (§1.2), no re-derivation
   needed — the ζ and ξ′ window functionals are the same shape with different pair densities.

Result (Rust toy, `tools/xiprime_transport_probe/`, model = exact interlacing count
N_ξ′ = (D−1) gaps + Σ(m_i−1), self-consistent N_ξ′ = N_ζ − 1):

| ζ multiplicities | ρ_ζ | ρ_ξ′ |
|---|---|---|
| all double [2×10] | 0.500 | 1.000 |
| all simple [1×10] | 1.000 | 1.000 |
| one triple, rest simple | 0.833 | 0.909 |

The decisive row is the first: **ζ distinct = 0.500 with ξ′ distinct = 1.000**. Double ζ zeros
(the canonical collapse) vanish from ξ′ distinct entirely. Even a triple ζ zero only dips ξ′
distinct to 0.909 — still above the 0.92919 bound is NOT forced (a dense enough pattern of triples
could push ξ′ below 0.92919 while ζ collapses more slowly), but the direction is fully confirmed:
ξ′ distinct is far LESS sensitive to ζ collapse than ζ distinct itself. There is no monotone
transport ξ′-distinct ⟹ ζ-distinct. No full 924k sweep warranted — it would only re-confirm the
ceiling on an identical read class and could not certify a ζ-distinct record via ξ′.

---

## 3. Part C — verdict

**CONFIRMED: corner (d) is closed. The transport of the ξ′-two-trace distinct certificate to ζ
distinct is invalid.** Two independent reasons, each decisive:

1. **Read-class:** the ξ′-two-trace reads the same {mean + in-band pair-density + integrality}
   single-window class as the 0.836740 certificate; it does not use two independent in-band reads.
   It is inside the ceiling's data class.
2. **Transport:** ξ′ distinct-on-line is structurally blind to ζ multiplicity collapse (double ζ
   zero → simple ξ′ zero). ρ_ξ′ ≥ 0.92919 gives NO lower bound on ρ_ζ. There is no valid
   inequality ξ′-distinct ⟹ ζ-distinct.

The 0.836740 distinct-on-line record stands as terminal. **No new world record.**
Firewall (binding): this is a proportion/simple-fraction theorem — carries ZERO evidence about RH
in either direction. Nothing here claims RH relevance.

---

## Honesty ledger / assumptions

- [PROVEN, cited] ζ window functional c_λ(v) with |s−s′| kernel; ξ′ functional with D₁ kernel;
  both rank-trace two-trace certificates (attack-xiprime.md §3, Lean XiPrime/Defs.lean).
- [PROVEN, cited] ξ′ interlacing: one per gap + (m−1) at multiplicity-m ζ heights (Rolle;
  attack-xiprime.md).
- [CHECKED NUMERICALLY] toy interlacing count: planted double-heavy ζ gives ρ_ζ = 1/2, ρ_ξ′ = 1.
- [inferred] The brief's "two independent in-band F reads" hypothesis is resolved to NO by the
  structural formulas; no code path reads a second independent height window.
- Not run (justified): full 924k two-window ζ sweep — would only re-confirm the ceiling, and the
  transport is already invalid structurally. No honest path to a record.

## Handoff
- Read-class overlap: PROVEN (structural formulas). Transport failure: PROVEN + CHECKED NUMERICALLY.
  Verdict: CLOSED, no new record, 0.836740 terminal. Ledger line appended.
