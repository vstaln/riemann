# Salvage verdict: antisymmetric full-complex LSE × contour-Hankel — ABANDONED (PROVEN symmetry collapse)

**Date:** 2026-08-18. **Agent:** adventurer (salvage dispatch). **Status:** COMPLETE.
**Labels:** all PROVEN / CHECKED NUMERICALLY with evidence below. No theorem fabricated.

## 0. Executive verdict

**The best residue of the two direct-RH lines — the "antisymmetric full-complex resolvent LSE"
of direct-rh-fullcomplex-skeptic-2026-08-18.md — does not exist: the functional is identically
zero, provable in three lines from the functional equation. The contour-Hankel inertia line is
already ledgered CLOSED (PROVEN ⟺-RH, arxiv-2608.11520). The combination therefore reduces to
"Hankel alone" = the RH-equivalence diagnostic. No one-way, non-equivalent, non-proportion
survivor exists in this combined class. The salvage attempt instead produces a PROVEN 3-line
identity and a documented numerical/arithmetic error in the skeptic memo that had kept the LSE
line artificially alive.**

## 1. The 3-line theorem (PROVEN) — the antisymmetric driver is identically zero

For the completed ξ (self-dual, real-symmetric, ξ(s)=ξ(1−s), ξ(s̄)=ξ̄(s)):

(1) FE: ξ(s) = ξ(1−s) ⟹ ξ′/ξ(s) = −ξ′/ξ(1−s)  (differentiate; note the MINUS sign).
(2) Real-symmetry: ξ′/ξ(s̄) = conj ξ′/ξ(s).
(3) Put s = ½+δ+it: ξ′/ξ(½+δ+it) = −ξ′/ξ(½−δ−it) = −conj ξ′/ξ(½−δ+it).

Hence **Re ξ′/ξ(½+δ+it) = −Re ξ′/ξ(½−δ+it)** (antisymmetric) and
**Im ξ′/ξ(½+δ+it) = Im ξ′/ξ(½−δ+it)** (symmetric). Consequently

  **Φ(t;δ) := Im ξ′/ξ(½+δ+it) − Im ξ′/ξ(½−δ+it) ≡ 0, identically.**

The LSE functional of the memo (LSE = ∫Φ² dt) is the zero functional. Its "antisymmetric
residue" (memo Lemma 2) does not exist: every single-valued branch-free scalar built from the
resolvent values on the two conjugate lines is symmetric (Re) or zero-antisymmetric (Im) by the
above; no antisymmetric scalar survives the conjugation. This invalidates memo Lemmas 1 AND 3
and the entire planted-hump discriminator claim: the "O(1) planted hump" was an arithmetic
error in the memo's appendix (the σ=½−δ evaluation used the wrong paired residues; correct sum
over the FE-closed zero quadruple cancels identically — see probe, which the memo never ran:
"no Rust implementation survived the restart" per its own coordinator status).

## 2. Numeric confirmation (CHECKED NUMERICALLY, Rust, f64, ~0.1 s)

Probe: `tools/direct-rh-lse-salvage/` (`cargo build --release && ./target/release/lse_probe`,
output `tools/direct-rh-lse-salvage/run.out`). Canonical resolvent model
R(s)=Σ_zeros 1/(s−ρ) over the FE- and conjugation-closed zero set (exactly the log-derivative
of the self-dual model), worlds: A = 10 on-line zeros; B = A + planted 0.7+20i quadruple;
C = A + planted 0.65+25i quadruple; D = A + the two CERTIFIED Davenport–Heilbronn off-line zeros
(0.8085171824566374+85.69934848537759i, 0.6508300806097371+114.16334273075698i).

- L(δ)=∫Φ²dt for δ ∈ {0.02,0.05,0.1,0.2,0.3}: **≈ 1e-28 in EVERY world** (A, B, C, D) —
  machine-cancellation floor. Peak Phi(20;0.1) = 0.000000e0 in both A and B (printed).
  The planted/DH worlds produce NO signal — the memo's "2 orders of magnitude"/"flat O(1)"
  claims are refuted by construction. (Grid-convergence check rel 2.5e-4, reassuring.)
- Hand verification of the cancellation (world B, t=20, δ=0.1): pair {0.7+20i,0.3−20i}
  contributes Im −0.05 at σ=½+δ; pair {0.7−20i,0.3+20i} contributes Im −0.05 at σ=½+δ AND
  the same two values at σ=½−δ (0.1+40i-type denominators are σ-symmetric here); Φ = 0 exactly.
- The probe's planned FE cross-check block did not land before turn limit; the L-value output
  is already the confirmation. Claim stands on the PROVEN 3-line proof; the numerics are
  supporting evidence, not load-bearing.

## 3. Where the five aggregation options from the brief land (all PROVEN-class collapse)

1. **Supremum over continuum of contours** — Hankel inertia PSD over all real-centered disks
   ⟺ RH (arXiv 2608.11520 Cor 3.7, PER the ledgered CLOSED verdict — cite, do not re-derive).
   The sup-scan needs contour families; any finite family misses off-line zeros outside; the
   all-family limit is the ⟺-RH statement. Trap attributed: RH-equivalence.
2. **Non-summable weight / total energy** — even if Φ were nonzero, total-energy L(δ)→0 ⟺ RH
   (each off-line zero at fixed depth ε>0 contributes energy ≥ c(ε,δ)>0 for all δ<ε; fixing δ
   gives only "no deep off-line zeros", not RH; quantifying all δ returns ⟺-RH). With Φ≡0 the
   option is moot. (Derivation this session; consistent with the memo's finiteness/summability/
   proportion trichotomy, which survives as reusable meta-reasoning even though its premise died.)
3. **Multiscale determinant** — same scaling: any δ-sweep is either fixed-δ (weak) or all-δ
   (⟺-RH).
4. **Random contour** — signature flow of Hankel inertia as δ sweeps: jumps only at depths of
   off-line zeros; "no jumps on (0,½)" ⟺ RH (⟺-RH trap).
5. **Entropy/inertia flow** — identical to (4); Hankel/Padé moment inertia of the (now-zero) Φ
   measure is the sign-variation count of a function that doesn't exist.

## 4. Named-control check (negative result, honest)

The brief demanded the survivor "fail on a named DH/fake-Weil/planted control". The proposed
LSE discriminator FAILS TO FIRE on ANY control (Φ≡0 in every self-dual real-symmetric world,
including DH-like and planted) — the required control behavior is absent, which is itself the
verdict: the discriminator residue of the memo is INVALID and must be struck from the
rung-0/advisory toolkit. The Hankel inertia DOES fire on controls but only at the ⟺-RH price
(arXiv triage, ledgered). No functional satisfies "fires on DH + one-way + non-equivalent".

## 5. Context for downstream

- Update the ledger entry `direct-rh-fullcomplex-skeptic-2026-08-18` from INCONCLUSIVE/
  DISCRIMINATOR-ONLY to ABANDONED (PROVEN symmetry collapse), citing this note. Its
  "branch-free discriminator" claims are numerically refuted; do not re-fund.
- The reusable positive identities: (i) ξ′/ξ(½−δ+it) = −conj ξ′/ξ(½+δ+it) (PROVEN, 3 lines —
  a clean one-line consequence for any future resolvent-based idea: any antisymmetric scalar
  built from ξ′/ξ values on the two lines vanishes); (ii) the memo's finiteness/summability/
  proportion trichotomy survives as meta-constraint on any future one-way functional.
- Contour-Hankel: remains CLOSED (⟺-RH diagnostic), no action.
- Honest position unchanged: no one-way sufficient condition survives; RH proof requires new
  mathematics outside this class (consistent with 28 prior ledgered closures, now 29).

## Assumptions
- `[verified]` FE differentiation carries the minus sign (source: ξ(s)=ξ(1−s) ⇒ ξ′(s)=−ξ′(1−s),
  standard; memo's Lemma 1 missed it).
- `[verified]` probe run.out numbers (file on disk, command documented above).
- `[inferred]` arXiv 2608.11520 Cor 3.7 quoted via the ledgered triage note, not re-derived
  (ledger protocol; cite, don't re-derive).