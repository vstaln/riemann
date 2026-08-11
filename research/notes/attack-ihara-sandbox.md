# Attack: Ihara-zeta sandbox — the two-moment certificate on a PROVEN-RH finite object (vector G1 / V7 realization)

**Agent:** EXECUTIONER (analogy-domain-transfer + investigation + epistemology)
**Task:** G1 from `idea-generator-ml-eco.md` — run the two-moment (Weil-form) certificate pipeline on the
Ihara zeta of small regular graphs, where RH is **proven** (zeros on |u| = 1/√q iff Ramanujan) and
everything is finite and exact. Calibration target for the V7 question: "is the 2/3 deficit arithmetic
or method-inherent?"
**Date:** Round 1/2.
**Code:** `tools/ihara-sandbox/` (new directory — canonical; `tools/finitet` untouched, owned by the
finitet round). Scratch copy `scratch/ihara_sandbox/`. All commands cited per row below.
**Verdict up front:** **The V7 dichotomy (≈2/3 ⇒ method-inherent; ≈1 ⇒ arithmetic) is FALSE. The
certificate does not measure RH.** On RH-true objects it takes values from **−22.9 to +0.98**,
determined entirely by the zero configuration's *pair structure*, not by whether RH holds: the rigid
lattice (RH-true) saturates at **0.977**, the ζ zeros (RH-true, GUE-correlated) sit at **0.6725**,
random-regular Ramanujan graphs at **+0.32/+0.36**, and the small Ramanujan graphs (repeated
eigenvalues → coincident angles) collapse to **−0.9 … −22.9**. The method is **not** inherently capped
at 2/3; the ζ-world's 0.6725 is pinned by the realized (GUE, Montgomery) pair correlation of the zeros.
The certificate is literally the functional `cert(g) = 1 − (1/∫ψ²)²·∫g(u)Ψ₂(u)²du` of the pair-correlation
law g. The ceiling theorem (0.6818, PROVEN Lean) still binds the two-moment class on bandwidth-1 data, so
the real-zeros program's only routes past 0.6725 are the in-class gap (V2) and new inputs (V3/V4/V5) —
confirming the catalog's funding.

---

## 1. The object: the Ihara zeta of a regular graph (all PROVEN, classical)

Let G be a (d)-regular graph on V vertices, adjacency A, and set **q := d − 1**.

- **Ihara determinant formula** (Ihara 1966; Bass 1992): `Z_G(u)⁻¹ = (1−u²)^{(q−1)V/2} · det(I − A u + q u²)`.
- **Trivial zeros:** u = ±1 with multiplicity (q−1)V/2 each (the analog of ζ's trivial zeros); NOT on the circle.
- **Nontrivial zeros:** roots of `det(I − A u + q u²)`; each eigenvalue λ solves `q u² − λ u + 1 = 0`, i.e.
  `u = (λ ± √(λ²−4q))/(2q)`. For |λ| < 2√q: `|u|² = (λ² + 4q − λ²)/(4q²) = 1/q` — on the circle `|u| = 1/√q`.
- **RH for the Ihara zeta (PROVEN):** the nontrivial zeros lie on |u| = 1/√q iff G is Ramanujan,
  i.e. |λ| ≤ 2√q for all eigenvalues λ ≠ ±d. **Every graph in this note is Ramanujan, so RH holds
  by theorem.** Code-verified here: max error of |u|² vs 1/q over all nontrivial roots ≤ 1.1e-16
  (all graphs, `tools/ihara-sandbox` §2, "Ihara-RH |u|=1/sqrt q err" column).
- **Functional equation pairing:** the map u ↦ 1/(q·u) pairs the roots (on the circle it is
  conjugation u ↦ ū). Each conjugate pair {u, ū} is represented once by its **angle**
  θ ∈ (0, π), `cos θ = λ/(2√q)`.
- **"Weyl law":** the exact count of nontrivial zeros is 2·(V−1) (non-bipartite) or 2·(V−2)
  (bipartite); N = V−1 or V−2 angles. For large regular graphs the angle density tends to the
  Kesten–McKay law pulled back through cos θ = λ/(2√q):
  `ρ_θ(θ) = (2dq/π)·sin²θ/(d²−4q·cos²θ)`, which **vanishes at θ = 0, π** (the eigenvalue density
  vanishes at ±2√q) and is concentrated at θ = π/2. Verified: the random-regular angle histogram is
  KM-shaped (bins `[4,14,23,29,28,30,28,25,16,2]` for the 4-regular V=200 graph).
- **Explicit formula:** `log Z_G(u) = −Σ_{γ primitive} log(1 − u^{ℓ(γ)})`; equivalently
  `u·d/du log Z_G(u) = Σ_{n≥1} N_n uⁿ` with N_n = number of closed geodesics of length n.
  (Classical; the zero structure above is the piece verified numerically here.)

**Labels:** all six bullets PROVEN (classical literature); the "verified" claims CHECKED NUMERICALLY
(script + command in §5).

## 2. The pipeline port (exactly as in `tools/finitet`, verified to reproduce it)

The finitet pipeline (attack-finitet.md, `tools/finitet/src/main.rs`): zeros γ ∈ [T, 2T) rescaled to
s_ρ = (γ−T)·N/T ∈ [0, N) at unit density; kernel ψ(u) = cos(√2·u)·1_{|u|≤1/2} with closed forms
Ψ(s), Ψ₂(s), ∫ψ² = 0.849227999318304; V[ρ][k] = Ψ(s_ρ − k); **W = VᵀV/∫ψ²**; certificate
`bound/N = (2·tr W − ‖W‖²_HS)/N`, compared to the paper constant 0.672500703679412 and the ceiling
0.6818286874638.

**Ihara port:** the "zeros" are the angles θ_i ∈ (0, π) of the nontrivial roots on |u| = 1/√q
(one per nontrivial eigenvalue, with multiplicity). Unit-density rescaling over the full window (0, π):
`s_i = θ_i · N/π ∈ (0, N)`, grid k = 0..N−1. Same W, same moments, same certificate. For each graph
the truth is s1 = N (all zeros on the circle), so the certificate must satisfy bound/N ≤ 1 (validity
checked "OK" for every row).

**Fidelity (section 0 of the run):** the port reproduces the finitet / attack-sandbox numbers
**exactly** — zeta-real T=200: bound/N = **0.716530** (finitet 0.716530); T=500: **0.711945**;
lattice N=122: **0.967689**; N=379: **0.973487**; poisson: **0.210369 / 0.099999**; jitter:
**0.893328 / 0.903354**. CHECKED NUMERICALLY (two independent implementations — Rust and numpy —
agree to all 6 printed decimals).

## 3. Main table — the certificate on RH-true worlds (all Ihara rows: RH PROVEN, zeros on |u|=1/√q)

| world | d | N | tr W/N | ‖W‖²_HS/N | ‖W‖²_HS,an/N | cert = (2tr−HS²)/N | rank | Δ vs 0.6725 |
|---|---|---|---|---|---|---|---|---|
| ζ zeros T=200 (on-line) | — | 123 | 0.988856 | 1.261182 | 1.274002 | **+0.716530** | 121 | +0.044029 |
| ζ zeros T=500 (on-line) | — | 380 | 0.996327 | 1.280708 | 1.285953 | **+0.711945** | 374 | +0.039444 |
| ζ zeros T=900..1300 | — | 766–1183 | 0.9990–0.9995 | 1.291–1.294 | — | **0.705–0.707** | — | +0.032..+0.035 |
| rigid lattice N=122 / 379 | — | 122/379 | 0.9899/0.9963 | 1.0121/1.0192 | 1.0229/1.0230 | **0.9677 / 0.9735** | 122/379 | +0.295/+0.301 |
| jitter N=122 / 379 | — | 122/379 | — | — | — | **0.8933 / 0.9034** | — | — |
| poisson N=122 / 379 | — | 122/379 | — | — | — | **0.2104 / 0.1000** | — | −0.462/−0.573 |
| **K4** (complete) | 3 | 3 | 0.979659 | 2.879193 | 3.000000 | **−0.919876** | 1 | −1.592 |
| **K5** | 4 | 4 | 0.926725 | 3.435274 | 4.000000 | **−1.581825** | 1 | −2.254 |
| **K8** | 7 | 7 | 0.999385 | 6.991392 | 7.000000 | **−4.992622** | 1 | −5.665 |
| **Petersen** | 3 | 9 | 0.973086 | 4.312063 | 4.565254 | **−2.365890** | 2 | −3.038 |
| **Cube Q3** | 3 | 6 | 0.966630 | 2.831859 | 3.050978 | **−0.898599** | 2 | −1.571 |
| **Clebsch** | 5 | 15 | 0.982825 | 8.086436 | 8.338404 | **−6.120785** | 2 | −6.793 |
| **Icosahedron** | 5 | 11 | 0.974196 | 3.720245 | 3.917290 | **−1.771853** | 3 | −2.444 |
| **Q4 (4-cube)** | 4 | 14 | 0.993160 | 4.833685 | 4.889816 | **−2.847365** | 3 | −3.520 |
| **Hoffman–Singleton** | 7 | 49 | 0.998673 | 24.943889 | 25.001016 | **−22.946544** | 2 | −23.619 |
| random 4-regular V=200 (Ramanujan, 0 off-circle) | 4 | 199 | 0.999070 | 1.642180 | 1.643786 | **+0.355959** | 158 | −0.317 |
| random 5-regular V=120 (Ramanujan, 0 off-circle) | 5 | 119 | 0.998588 | 1.675585 | 1.678059 | **+0.321592** | 92 | −0.351 |

All 9 Ihara graphs: spectrum verified against the known exact spectra by Jacobi on the constructed
adjacency matrix (✓), Ramanujan (✓), Ihara-RH |u| = 1/√q to ≤ 1.1e-16 (✓). The independent Python
cross-check (`tools/ihara-sandbox/crosscheck.py`, hand-entered spectra) reproduces every certificate
value to 6 decimals. All rows satisfy bound/N ≤ truth s1/N = 1 (validity "OK").

**Structure of the collapse (PROVEN closed form, verified):** with N angles arranged in multiplicity
groups m_g, the analytic pair-sum gives `HS²_an/N = 1 + (1/N)·Σ_groups m_g(m_g−1) + cross-pairs`, so for
the complete graphs (N coincident angles, m = N): `HS²_an/N = N` and `cert_an = 2 − N` exactly
(measured: K4 → 3.000000 and −0.92 ≈ 2−3; K5 → 4.000000, 2−4; K8 → 7.000000, 2−7; HS (groups 28, 21):
1 + (28·27+21·20)/49 = 25.001, cert ≈ 2−25 = −22.95 ✓).

## 4. The theory curve: the certificate is a pair-correlation functional

For a unit-density configuration with pair-correlation function g, the certificate (tr/N = 1) is
`cert = 2 − [1 + (1/∫ψ²)²·∫g(u)Ψ₂(u)²du] = 1 − (1/∫ψ²)²·∫g(u)Ψ₂(u)²du`. Numerically (Simpson, step
5e-4, range [0, 400], tail ≈ 2.5e-4; CHECKED NUMERICALLY):

| pair-correlation law g | c = 1 + (1/∫ψ²)²∫gΨ₂² | cert = 2 − c |
|---|---|---|
| Montgomery/GUE: g = 1 − sinc²(πu) | 1.332559 | **0.667441** |
| Poisson: g = 1 | 2.022976 | **−0.022976** |
| rigid lattice: g = Σ_{m≠0}δ(u−m) | 1.023094 | **0.976906** |
| paper's assumption-free constant | 1.327499 (paper) | **0.672501** |
| ceiling (near-CUE law) | — | **0.681829** |

Notes: (i) the GUE-pair value 0.6674 is **0.005 below** the paper's assumption-free 0.6725 — the paper's
MVH/variational constant is slightly conservative relative to the Montgomery-pair prediction; which is
the true asymptote of the ζ HS² moment is **INCONCLUSIVE** from the finite-T data (measured HS²/N
1.284–1.294 at T=700–1300 sits below both, converging slowly ~1/log T — see attack-finitet.md §5);
(ii) the measured worlds interpolate the theory: ζ-zeros → 0.67-regime, lattice → 0.977, poisson → ~0,
random-regular → between Poisson and GUE (its KM angle density is non-uniform, inflating the pair sum).

## 5. Honesty labels (every number above is script + command)

| claim | label | script | command |
|---|---|---|---|
| Ihara determinant formula / RH-iff-Ramanujan / FE / Weyl law / explicit formula | PROVEN (classical) | — | — |
| |u|=1/√q for all 9 graphs | CHECKED NUMERICALLY | `tools/ihara-sandbox/src/main.rs` §2 | `cd /home/vstaln/riemann/tools/ihara-sandbox && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/ihara-sandbox` (output `run-final.txt`) |
| all spectra (Jacobi vs known exact) | CHECKED NUMERICALLY | same | same |
| fidelity vs finitet/attack-sandbox | CHECKED NUMERICALLY (exact match) | same, §0 | same |
| all Ihara certificates, moments, ranks | CHECKED NUMERICALLY (2 independent impls agree to 6 dp) | Rust `src/main.rs`; Python `crosscheck.py` | above + `cd /home/vstaln/riemann/tools/ihara-sandbox && uv run --quiet --with numpy python crosscheck.py` |
| theory curve (GUE/poisson/lattice) | CHECKED NUMERICALLY (Simpson 5e-4, tail 2.5e-4) | `src/main.rs` §1 | above |
| paper constant 0.672500703679412, ceiling 0.6818286874638 | PROVEN (Lean, prior rounds) | — | — (attack-ceiling.md; `tools/qi_sweep.py`, `tools/lpdual/`) |
| "ζ zeros on-line & simple" for the 1000 zeros | CHECKED NUMERICALLY (prior round) | `tools/finitet` | attack-finitet.md §1 (LMFDB-verified file) |
| "which constant is the true HS² asymptote" | INCONCLUSIVE (data can't resolve at T ≤ 1300) | — | — |
| the interpretation in §6 | CONJECTURED (inference from measurements, not a theorem) | — | — |

Pipeline mechanics additionally triangulated by `diag_check.py` and
`fidelity_check.py` (uv run, numpy; canonical copies in `tools/ihara-sandbox/`): the finitet numbers were reproduced independently
before the Ihara port, and the "diag/N ≈ 1.13" puzzle in the sandbox output was resolved as a
labeling difference (grid-based vs zero-based decomposition of the same total ‖W‖²_HS — the total,
which feeds the certificate, is identical).

## 6. The answer: is the 2/3 deficit arithmetic or method-inherent?

**Neither — as posed. The certificate does not measure RH; it measures the pair-correlation rigidity
of the zero configuration.** The evidence (all code-backed, §3–§4):

1. **The method is NOT inherently capped at 2/3.** The rigid lattice is an RH-true world (all zeros
   on the line/circle, exactly) and the certificate reaches **0.9677–0.9754** (theory limit 0.9769).
   If the two-moment method were inherently lossy at 2/3, no world would exceed it. So 0.6725 is not a
   method floor.
2. **The 2/3 is pinned by the realized pair correlation of the ζ zeros, not by RH.** The ζ zeros used
   here are all on the line (RH-true in the tested range) and the certificate is 0.705–0.719 at
   T=100–700 → 0.6725 (paper) / 0.6674 (GUE-pair theory). Other RH-true worlds give 0.98 (lattice),
   0.32–0.36 (random regular Ramanujan), and −0.9…−22.9 (coincident-atom Ramanujan graphs). RH-true-ness
   alone determines **nothing** about the certificate; the zeros' GUE-like pair correlation
   (Montgomery: F(α) = 1 on [0,1], PROVEN unconditional per attack-ceiling.md input (a)) does. The
   deficit is "arithmetic" in the precise sense that the realized zero statistics fix the constant.
3. **The ceiling theorem still governs the real-zeros program.** Within the certificate class on
   bandwidth-1 data (F ≡ 1 on [0,1]), no certificate beats **0.6818** (PROVEN Lean, attack-ceiling.md).
   The lattice's 0.98 does not contradict this — the lattice violates the F ≡ 1 datum (its form factor
   is a comb), so it lies outside the ceiling's hypothesis set. On the actual ζ zeros the two-moment
   ceiling is 0.6818 (V2's in-class target), and beyond that only new inputs help (V3/V4/V5).
4. **NEW Ihara-specific finding — the method presupposes distinct zeros.** Repeated adjacency
   eigenvalues produce *coincident* Ihara angles; the W-rank collapses to the number of distinct angles
   (rank = 1 for K_n, 2 for Petersen/Clebsch/HS, 3 for Icosa/Q4) and HS²/N ~ N, so the certificate goes
   to **2 − N** (PROVEN closed form, verified). The G1 note's "Ramanujan graphs = the crystal-like end"
   is **REFUTED for the certificate**: the small Ramanujan graphs are atom-degenerate (the worst
   certificates measured), while the actual crystal (uniform lattice) is best (0.98). The certificate
   sees pair structure, not Ramanujan-ness. This is a clean statement of why the ζ-side "simple zeros"
   hypothesis is load-bearing for the method.

**Consequence for funding the real-zeros program:** the V7 "is the method the bottleneck?" question is
answered in a sharper, code-backed way: the method is not the bottleneck (rigid worlds saturate at
~0.98), the realized GUE pair correlation pins ~2/3, and the certificate class is bounded at 0.6818 on
bandwidth-1 data (proven). The only routes to a higher certificate on the real zeros are **new inputs**:
fund **V2** (in-class 0.6725 → 0.6818, the only proven-inputs constant gain), **V3** (third moment —
bypasses the two-moment wall), **V4/V5** (moment-capacity roadmap — prices each conjectural input),
**L1** (independent prime-side cross-check). Consistent with attack-ceiling.md and the catalog's ranking;
the Ihara sandbox opens no new door past 0.6725 on the realized zeros, but it removes the "maybe the
method itself is the 2/3 wall" hypothesis from the strategy space.

## 7. Caveats / weakest links

- f64 arithmetic; single sample per world (except the two random-regular seeds); the Ihara graphs are
  small (N ≤ 49), so boundary/truncation effects shift the direct certificate slightly from the
  analytic pair-sum (both reported per row; the qualitative collapse is robust — it is driven by the
  exact coincident-pair term).
- The paper's HS constant (1.32750) vs the GUE-pair value (1.33256) differ by 0.005; the finite-T data
  (1.284–1.294 at T=700–1300) cannot distinguish the true asymptote — flagged INCONCLUSIVE, and it does
  not affect the strategic conclusion (both are ≈ 2/3, far from 1 and from the lattice 0.98).
- The Ihara "GUE-like end" (per the G1 note) is not realized by random regular graphs in this
  certificate sense: their KM angle density is non-uniform after rescaling, inflating the pair sum
  (certificate +0.32/+0.36). A GUE-correlated *unit-density* angle configuration is the only thing that
  reproduces ~0.67; the ζ zeros are the only such object measured here.
- The off-line injection worlds (V7's branch (b)) were already covered by `research/notes/attack-sandbox/`
  (forced pairs lower the certificate monotonically, certificate stays valid); this note adds the
  RH-true exact-object worlds (branch (c)) and the theory curve.

**Honest closing:** G1 set out to "settle whether the method's 0.6725 is arithmetic or inherent". The
answer is: **neither label fits the dichotomy** — the certificate is a pair-correlation functional; it
saturates near 1 on rigid worlds, sits at ~2/3 on GUE-like worlds (which the ζ zeros are), and collapses
on coincident-zero worlds. The 2/3 is the correct two-moment answer for the realized (GUE) zero
statistics; the method is not the 2/3 wall; the ceiling theorem is; new inputs (V3/V4/V5) are the only
way past it. This **funds the real-zeros program's input roadmap** and closes the strategic
"is-the-method-the-bottleneck" hypothesis with code.
