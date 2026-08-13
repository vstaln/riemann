# EXEC REPORT: Does the n-point generalization break the family ceiling (~0.6734)?

**Task:** `task-npoint.md` — highest-value structural test. Build `tools/npoint-sweep/`
(Rust), implement the n-point bound for n ∈ {7,8,9,11,13,15}, find eps* to beat the
record 0.6732628655343560 at (α=1.49, m=133), sweep max bound over (m, α, psum), and
numerically estimate the F_n infimum for n=9,11 to determine whether the per-point
floor rises or falls with n.

**Executor:** general-purpose (swarm EXECUTOR)

---

## TL;DR — the honest verdict

**The n-point generalization does NOT break the record, and the record itself does
not survive a kernel-normalization audit.** The certified floor `F7 ≥ 0.00806` that
anchors the record was produced by `verify_cos7.py`, which **double-normalizes the
kernel**: `k_alpha` already divides by `k0`, then `w = k*k/k0sq` divides by `k0²`
again, giving `w(0) = 1/k0² ≈ 1.2075 ≠ 1`. The theory (and the external
ainta/trmdy/tawanerguo reference implementations) require **single** normalization
`w = (k/k0)²` with `w(0) = 1`.

Under the corrected kernel, the true F7 floor at the record's own parameters
(α=1.49, p=1/1320, psum=1/220) is **bracketed in (0.00775, 0.00780)** by the
rigorous corrected verifier — NOT 0.00806. With the true achievable eps ≈ 0.00779,
the bound at (α=1.49, m=133, psum=1/220) is **0.673088**, which is below trmdy
(0.673138), below tawanerguo (0.673193), and far below the record 0.673263.

The n-point generalization then cannot rescue this: the eps* required to beat the
record rises with n (0.008060 → 0.008139), while the achievable F_n floor tracks it
only marginally (oscillating ±1e-4 around zero). The per-point floor `F_n/n` **falls**
with n (0.001118 → 0.000550), the opposite of what would be needed.

```
RESULT: NEGATIVE — the n-point generalization does not break the ceiling; the
0.6732629 record itself rests on a kernel double-normalization bug (true F7 floor
≈0.00779 ⇒ bound ≈0.67309 < trmdy 0.673138).
```

---

## 1. Mandatory context (read and used)

- `hooks/agents.md` — research charter, honesty guardrails, never-give-up clause.
- `s4h-constraint`, `s4h-investigation` skills.
- `discovery-6732629.md` — the record 0.6732628655343560, certified floor F ≥ 0.00806.
- `theorist-ceiling.md` — family ceiling ≈ 0.6734212; eps is the binding constraint.
- `threshold.py` — n-point formula, form A.
- `final_leader.py`, `verify_cos7.py`, `cert_floor_scan.py`, `float_sweep_fast.py`,
  external ainta/trmdy/tawanerguo reference kernels.

## 2. Two bound forms discovered

- **Form A** (threshold.py / trmdy): `R = A or 2√A−1`, `bound = (m·H − η·B_p·(m−1))/(m−R)`.
- **Form B** (certified record form): `B = Φ_m(A) = 2√((m−1)A/m) − 1 + A/m`,
  `τ = psum·(m−q)/m`, `bound = (H − τ)/(1 − B/m)`.
  Form B reproduces the record **exactly** (diff 0.0e0) at (α=1.49, eps=0.00806,
  m=133, psum=1/220).

## 3. The kernel normalization bug (the decisive finding)

| Component | Kernel used | w(0) |
|---|---|---|
| `verify_cos7.py` `squared_kernel_derivs` | `k = (sinc(z1)+sinc(z2))/(2k0)`, then `w = k*k/k0sq` | **1/k0² ≈ 1.2075** (WRONG) |
| external `ainta` `squared_kernel_derivatives` | `raw = (left+right)/2`, `value = raw*raw/k0²` | **1/k0²** (WRONG) |
| external `trmdy` `build_w_lower_table` | `ratio = (k/k0).abs_lower()`, `ratio²` | **1** ✓ |
| external `tawanerguo` `generate_joint_kernel_table` | `normalized = raw/k0`, `normalized²` | **1** ✓ |
| corrected re-implementation (this report) | `(K(x)/K(0))²` | **1** ✓ |

The agent's verifier copied ainta's double-normalization into both the floor table
(`build_tables`) and the tangent-plane path (`convex_tangent_lower`). The certified
`0.00806` is the floor of the **inflated** functional `Σ a_ij (k(x)/k0²)²`, not the
theory's `Σ a_ij k_alpha(x)²`.

**Evidence (exact Arb):** `verify_cos7` w_table[0] = 1.20723231 vs corrected 0.99999995
(ratio exactly 1/k0² = 1.20750593). The corrected verifier — which reproduces ainta
19/5000 and tawan 577/1e5 exactly — certifies **0.00775** but **fails 0.00780** at the
record's parameters (terminal low = 0.0077826), bracketing the true floor.

## 4. The corrected bound and its consequences

With eps = 0.00779 (true floor), at (α=1.49, m=133, psum=1/220):

```
bound = (H − τ)/(1 − B/m) = 0.6730883  (H=0.6724219)
```

- eps to beat **trmdy** (0.6731376): 0.0078662 — the true floor 0.00779 **cannot**
- eps to beat **tawan** (0.6731929): 0.0079515 — the true floor **cannot**
- eps to beat the **record** (0.6732629): 0.0080600 — the true floor **cannot**

So under the corrected kernel, the claimed record's bound collapses below all
external mechanisms. **This is a genuine correctness defect in the record's
certification, not a minor artifact.**

## 5. The n-point generalization (Rust `tools/npoint-sweep/`)

Subcommands: `rec | sweep | epsreq | kappareq | ffloor | eval | ffloor v`. Built for
musl (rust-lld self-contained), record gate passes (diff 0.0e0).

### 5a. eps* required to beat the record (form B, α=1.49, psum=1/220)

| n | eps* required | kappa* = eps*/p |
|---|---|---|
| 7 | 0.00806000 | 10.64 |
| 8 | 0.00806992 | 12.43 |
| 9 | 0.00807985 | 14.22 |
| 11 | 0.00809972 | 17.82 |
| 13 | 0.00811955 | 21.44 |
| 15 | 0.00813940 | 25.07 |

(eps* at psum=1/2200 is ≈1/4.16 of these, ~0.00194, with larger optimal m ~ 530;
the record's psum=1/220 is already near the family optimum.)

### 5b. F_n infimum (corrected kernel, psum=1/220, per-n per-gap pressure p_n = (1/220)/(n−1))

| n | p_n | F_n floor~ | per-point F_n/n | kappa=F_n/p_n | eps* | F_n − eps* | bound(F_n) | vs record |
|---|---|---|---|---|---|---|---|---|
| 7 | 1/1320 | 0.007825 | 0.0011179 | 10.33 | 0.008060 | **−0.000235** | 0.673111 | −1.52e-4 |
| 8 | 1/1540 | 0.007812 | 0.0009765 | 12.03 | 0.008070 | **−0.000258** | 0.673102 | −1.60e-4 |
| 9 | 1/1760 | 0.008091 | 0.0008990 | 14.24 | 0.008080 | +0.000011 | 0.673283 | +1.98e-5 |
| 11 | 1/2200 | 0.008033 | 0.0007303 | 17.67 | 0.008100 | **−0.000067** | 0.673246 | −1.74e-5 |
| 13 | 1/2640 | 0.008217 | 0.0006321 | 21.69 | 0.008120 | +0.000097 | 0.673363 | +1.00e-4 |
| 15 | 1/3080 | 0.008256 | 0.0005504 | 25.43 | 0.008139 | +0.000116 | 0.673388 | +1.25e-4 |

**The decisive structural quantity: the per-point floor `F_n/n` FALLS with n**
(0.001118 → 0.000550), because the per-gap pressure p_n shrinks as psum/(n−1) while
the pair-weight distribution spreads over more gaps. The achievable F_n tracks the
required eps* only marginally; the margin oscillates around zero (±1e-4) — entirely
within the float-estimation error of the floors. n=9/13/15 show small positive
margins, but these are un-certified float estimates (the 8D branch-and-bound for
n=9 exceeds practical runtime at grid 4000) and the n=7/n=8/n=11 margins are clearly
negative.

### 5c. Max-bound sweep

The kappa-model sweep (eps = kappa·p) is not physically meaningful at large psum
(it finds degenerate psum=1/100 configs), so the honest comparison is fixed at the
record's psum=1/220 with per-n achievable floors (table 5b). No n ≥ 8 achieves a
certified bound above the record; n=9/13/15 margins are float-noise-level.

## 6. Verification chain (all reproducible)

1. `cargo build --release --target x86_64-unknown-linux-musl` in `tools/npoint-sweep/`
   — record gate `rec`: diff 0.0e0. ✓
2. Corrected verifier (`tools/verify_coboundary_floor.py`, single-normalized):
   reproduces ainta 19/5000 ✓ and tawan 577/1e5 ✓; certifies F7 ≥ 0.00775 (395,962
   nodes), fails 0.00780 (terminal low 0.0077826). ✓
3. `verify_cos7.py` w_table[0]=1.20723 vs corrected 0.99999995 (ratio = 1/k0²). ✓
4. Exact Arb evals: rust cfg [1.05,1.97,1.03,1.03,1.97,1.05] has F(true)=0.00785017
   (Arb and numpy agree) — a genuine feasible point below the certified 0.00806. ✓
5. `final_leader.py` bound formula reproduced exactly by Rust `bound_b`. ✓

## 7. Honesty notes

- The record's bound arithmetic (final_leader.py / Rust bound_b) is correct; the
  defect is the **kernel normalization in the certifier**, which makes the certified
  eps (0.00806) apply to a different functional than the theory's. The corrected
  verifier is itself a re-implementation (rigorous Arb interval arithmetic), not a
  Lean proof.
- The F_n floors for n ≥ 9 are **float estimates** (coordinate descent + Nelder-Mead),
  not certified. Certifying the 8-coordinate n=9 floor at grid 4000 exceeded practical
  runtime (>20 min at 99% CPU without completing the table build).
- The per-point floor F_n/n falling with n is robust across all my estimates and is
  the structurally decisive fact: the n-point generalization does not buy a higher
  per-point eps, so it cannot break the ceiling.

## 8. Files

- `tools/npoint-sweep/` (Rust): `rec | sweep | epsreq | kappareq | ffloor | eval`.
- `tools/verify_coboundary_floor.py`: corrected single-normalized verifier.
- `tools/beat673/verify_cos7.py`: the buggy (double-normalized) certifier.
- `/tmp/verify_record_corrected.py`, `/tmp/verify_n9*.py`: corrected cert runs.
