# Exact-S₃ certificate: rebuilding the sinc-m3 read on the exact identity (no E[T]≥0)

**Agent:** IDEA/ATTEMPT PROBE (exact-s3-certificate). **Date:** 2026-08-17.
**Model:** opencode-go/deepseek-v4-flash, background. **Probe:** tools/exact_s3_probe/ (Rust, musl).
**VERDICT: the m₃-read lever is FINALLY CLOSED — the exact certificate does NOT beat the wall.**

## 0. The exact identity (PROVEN, cited)
Per config (marked measure μ = Σ_j m_j δ_{x_j}, x_j = j/256, m_j ∈ {1,2}, ν = μ/M, G = K²,
K = sinc²(π·128·x), T1 = (G*μ)/M, unnormalized DFT μ̂(k) = Σ_j m_j e^{−2πikj/N}):
m₂ = N·M·⟨1,T1⟩_ν, m₃ = N²·M²·‖T1‖²_ν, and **m₃ = m₂² + N²M²·Var(T1), Var(T1) ≥ 0** (CS).
Equality (Var(T1) = 0) ⟺ G*μ constant on supp. Extremals: all-2 (mass-p₁=0) AND all-1 (p₁=1).

**Verified numerically (probe §1):** random configs, |m₃ − (m₂² + N²M²Var(T1))| ≤ 5.8e-11
[IDENTITY VERIFIED]; max(m₂² − m₃) = 0 [CS HOLDS]. Extremals all-2 / all-1: m₃ − m₂² =
−4.8e-9 / −1.2e-9 ≈ 0, m₂ = 597.33 / 298.67 (matches rederivation's m₂ ≈ 554 for uniform).

## 1. The exact envelope → min-p₁
For any admissible law (marks ∈ {1,2}, marginal p, pair rows E|μ̂(k)|² = c·k):
  E[m₃] = (E[m₂](p))² + Var(m₂) + N²M²·E[Var(T1)]  ⇒  **min S₃(p) ≥ (E[m₂](p))²**
(the identity's ONLY certified consequence; the variance terms are ≥ 0 but carry no
class-level lower bound derivable from the identity). max S₃(p): no upper bound from the
axioms; the super-law realizes ≈ 7.9 at count-p₁ ≈ 0.68 (so max-envelope ≥ 7.9 there).

**Recomputed min-p₁** (probe §2; old-cert parameter p = MASS fraction, count = 2p/(1+p);
calibration c = 3.484e-5 ⟸ m₂(1) = 2.22, C = 127.4583):

| p (mass) | count | (E[m₂])² | D+P₃ (broken floor, for reference) |
|---|---|---|---|
| 0.422384 | 0.593909 | 5.4400 | 6.3050 |
| 0.5173 (wall mass) | 0.6819 | **5.2487** | 6.0435 |
| 0.6818 | 0.8108 | 5.0386 | 5.6184 |
| 0.7488 | 0.8564 | 4.9876 | 5.4400 |

**min-p₁ = 0.422384 (mass) / 0.593909 (count)** — smallest p with (E[m₂])² ≤ 5.44.
Wall count-p₀ = 0.6818287 ⇒ **count 0.5939 < 0.6818: does NOT beat the wall** (CHECKED
NUMERICALLY, matches referee-A proven-floor 0.4224/0.5939 exactly — ledger).

## 2. Why the variance term cannot save it
To beat the wall the certificate needs min-achievable [Var(m₂) + N²M²E[Var(T1)]] ≥
5.44 − 5.2487 = **0.19** at the wall's mass-p₁ = 0.5173, for ALL admissible laws. The
identity gives Var(T1) ≥ 0 only — no positive uniform lower bound. The super-law's large
variance term (m₃ ≈ 7.9 vs m₂² ≈ 5.25 ⇒ Var-term ≈ 2.65) shows the upper end is huge but
says nothing about the min. Per-config probe (§3): simple families at p₁ ≈ 0.68 (spread,
block, random, alternating) violate flat rows by 19–110× (flat-dev ≫ 1) — all OUT of the
admissible class, so no control law from these (consistent with regenerate-256law: the
exact-CUE ramp is unachievable by simple families — the flat-row class is tightly
constrained). Whether an in-class law at mass-p₁ = 0.5173 with E[m₃] ≤ 5.44 exists is
OPEN, but the certificate needs to EXCLUDE it, and no theorem does.

## 3. The 256-law / super-law control
- The 256-law's exact marked S₃ is **NOT computable** (its configuration is private,
  cert_N256_blk_b128m.json; regenerate-256law: exact-CUE ramp f̄(j)=j not recoverable from
  public constraints). INCONCLUSIVE by data availability.
- Super-law sibling (independent re-verification, adversarial-m3-reverify): marked
  m₃(1/2) = 7.935 ± 0.041 bias-corr at simple fraction 0.679 — ≫ 5.44, **excluded from
  [4.56, 5.44] by its exact value, no floor needed** (CHECKED NUMERICALLY, cited).
- BUT: super-law count-p₁ = 0.679 > min-p₁ = 0.5939 — it is ABOVE the certified ceiling,
  so its exclusion is consistent with the certificate yet cannot lift min-p₁. Excluding
  one law (even the wall law) does not exclude the class.

## 4. DH control (RH-false, mandatory) — FIREWALL OK
barrier_zoo_rs `dh` built and run: FE signs both ± true; 6 off-line zeros certified
(|f| < 1e-9): 0.808517±i·85.699348, 0.191483+i·85.699348, 0.650830±i·114.163343,
0.349170+i·114.163343, 0.306597±i·77.346941, 0.693403+i·77.346941; "RH FALSE in this
model world" (CHECKED NUMERICALLY, its own verdict). DH **violates flat rows** (CONJECTURED,
literature-grounded; refereeB concurred — not re-derived here) ⇒ DH is OUTSIDE the
admissible class ⇒ the certificate is VACUOUS for DH, not false — no "proves too much".
Independent of class membership: the certificate's conclusion is only min-p₁ = 0.5939
(count), weaker than the wall, so no RH-false world can contradict it (nothing claimed
above the wall).

## 5. Final verdict
**The exact-S₃ certificate does NOT beat the wall, and the m₃-read lever is FINALLY
closed.** The exact identity's only certified content is the bound E[m₃] ≥ (E[m₂](p))²,
giving min-p₁ = **0.593909 (count) / 0.422384 (mass)**, both below the wall 0.6818287. The
old certificate's 0.7488 was entirely an artifact of the unproven E[T] ≥ 0 (the D+P₃
floor, FALSE per-config — referee A's 3×3 PSD counterexample). The variance term
N²M²E[Var(T1)] ≥ 0 can only raise min-p₁, but the identity provides no positive class-level
lower bound; the needed ≥ 0.19 at the wall's p₁ is unproven, and per-config search finds
no in-class candidate law at all (flat rows are the binding constraint, not S₃).
Conditional for ANY future m₃-read claim: (H1 flat rows ∧ H2 read S₃ ∈ [4.56,5.44] ∧ H3
exact-S₃ identity) ⇒ p₁ ≥ 0.5939 (count) — a ceiling BELOW the existing 0.6818/0.6735
records. The 256-law's exclusion (S₃ ≈ 7.9) is genuine but single-law; it does not
constitute a record. The DH control cannot be violated by this (vacuous for DH).

## Labels
- Identity m₃ = m₂² + N²M²Var(T1), extremals: PROVEN (cited) + CHECKED NUMERICALLY
  (probe §1, |diff| ≤ 5.8e-11; all-2/all-1 slack ≈ −5e-9).
- Envelope (E[m₂])²(p) and min-p₁ = 0.422384/0.593909: CHECKED NUMERICALLY (probe §2,
  command below) — independently reproduces referee-A proven-floor numbers.
- Config flat-row violations (19–110×): CHECKED NUMERICALLY (probe §3).
- 256-law exact marked S₃: INCONCLUSIVE (config private; super-law sibling ≈ 7.9 cited).
- DH off-line zeros / RH-false: CHECKED NUMERICALLY (barrier_zoo_rs dh). DH flat-row
  failure: CONJECTURED (literature; refereeB).
- Verdict "does not beat wall": PROVEN-BY-ARGUMENT from the certified bound + numerics.

**Command:** `cargo build --release --target x86_64-unknown-linux-musl --manifest-path
tools/exact_s3_probe/Cargo.toml && ./tools/exact_s3_probe/target/x86_64-unknown-linux-musl/release/exact_s3_probe`
(and `tools/barrier_zoo_rs ... dh` for §4).
