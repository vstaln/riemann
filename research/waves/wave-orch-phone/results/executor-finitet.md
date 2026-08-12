# ROLE 2 — EXECUTOR: numerical probe of the finite-T gap (idealized cosine window)

**Executed by:** orchestrator (inline) — Agent tool unavailable in this environment; the
EXECUTOR role was executed inline with a self-contained script. Honesty labels per
`hooks/agents.md`. Every number below is CHECKED NUMERICALLY — produced by
`results/executor-finitet-probe.py`, run as:
`proot-distro login ubuntu -- bash -c "cd /root/riemann/research/waves/wave-orch-phone/results && python3 executor-finitet-probe.py"`.

**Data:** `tools/data/zeros_computed_10000.txt` (γ₁₀₀₀₀=9879.04) + `zeros_lmfdb_large.txt`
(γ₁₁₀₀₀=10726.26) — windows [T,2T) up to T=5000 (N up to 5622), a 25× larger T range than the
prior notes (T≤600, N≤472).

**Model (from attack-finitet.md):** idealized hard-cutoff ψ(u)=cos(a·u)·1_{|u|≤1/2},
Ψ(s)=½[sinc(s+a/2π)+sinc(s−a/2π)], Ψ₂(s)=½sinc(s)+¼[sinc((a−πs)/π)+sinc((a+πs)/π)],
∫ψ²=½+sin(a)/(2a), W=(1/∫ψ²)VᵀV, bound/N=2·trW/N−‖W‖²_HS/N, window's own asymptotic
constant 2−c_a, c_a=½+(1/a)cot(1/a). The script reproduces the prior notes' HS2 to all printed
digits (T=200: 1.27400 vs 1.274002) — cross-validated.

## 1. The gap table (CHECKED NUMERICALLY)

Window cos(√2·u), own asymptotic constant 2−c_√2 = **0.6725007037**:

| T | N | trW/N | HS2/N | bound/N | Δ = bound/N − 0.6725007 |
|---|---|---|---|---|---|
| 200 | 123 | 0.99899 | 1.27400 | 0.72397 | **+0.05147** |
| 400 | 289 | 0.99947 | 1.28638 | 0.71255 | +0.04005 |
| 800 | 666 | 0.99970 | 1.29021 | 0.70919 | +0.03669 |
| 1600 | 1509 | 0.99985 | 1.29617 | 0.70352 | +0.03102 |
| 3200 | 3371 | 0.99993 | 1.29910 | 0.70075 | +0.02825 |
| 5000 | 5622 | 0.99995 | 1.30214 | 0.69776 | +0.02526 |

Window cos(1.49·u) (the record's α), own asymptotic constant 2−c₁.₄₉ = **0.6548545321**:

| T | N | trW/N | HS2/N | bound/N | Δ = bound/N − 0.6548545 |
|---|---|---|---|---|---|
| 200 | 123 | 0.99904 | 1.27693 | 0.72115 | **+0.06629** |
| 400 | 289 | 0.99949 | 1.28923 | 0.70976 | +0.05490 |
| 800 | 666 | 0.99972 | 1.29303 | 0.70641 | +0.05155 |
| 1600 | 1509 | 0.99986 | 1.29885 | 0.70086 | +0.04601 |
| 3200 | 3371 | 0.99993 | 1.30179 | 0.69807 | +0.04322 |
| 5000 | 5622 | 0.99996 | 1.30478 | 0.69513 | +0.04028 |

## 2. What this establishes

1. **Δ > 0 at every accessible T for BOTH windows** — the finite-T bound overshoots its own
   asymptotic constant from above, in the SAFE direction. This extends the prior notes'
   finding (T≤600) by a factor 8 in T and confirms the α=1.49 record window behaves the same
   way (CHECKED NUMERICALLY).
2. **Decay is slow and monotone**: Δ(√2): 0.0515→0.0253; Δ(1.49): 0.0663→0.0403. Fits
   (intercept = conjectured T→∞ level): 1/log²T gives +0.0101 (√2) / +0.0252 (1.49);
   1/logT gives −0.0157 (√2) / −0.00035 (1.49); 1/T gives +0.027 (√2) / +0.042 (1.49).
   **The asymptote is INCONCLUSIVE from these fits** (rss ~6e-6–2e-5, all comparable) —
   consistent with the validation-001 correction on the prior notes. What is NOT in doubt:
   the sign is positive at every measured T, and the gap is decaying.
3. **trW/N → 1** cleanly (0.9990→0.99995, the Lemma 3.2 o(1) term, edge-truncation controlled);
   **HS2/N is the entire gap**: 1.274→1.302, still 2% below its own window constant
   Q(cos²·1)≈1.333 at T=5000 — the pair-sum deficit persists at heights ~10⁴, consistent with
   the CONJECTURED zero-statistics origin (attack-finitet-cinf.md §7).
4. **Framing caveat (honesty):** this probe measures the *idealized* functional's gap vs ITS OWN
   T→∞ constant. The certified record 0.6732628655 comes from the refined
   bound=(H−τ)/(1−B/m), H(1.49)=0.6724218860964 — different arithmetic. The idealized probe
   establishes the kernel-class direction (overshoot, safe) but does NOT directly certify the
   record's margin; that is the VERIFIER role's job.

## 3. Implication for P6

The "finite-T error terms" of the hard-cutoff cosine window are (i) edge/k-truncation
(tW/N−1, ~1/N, benign), (ii) the HS2 pair-sum deficit below the window constant (~2–4%,
decaying slowly, kernel-independent per attack-finitet-cinf), and (iii) the O(1/K) Poisson
truncation (hard cutoff only; provably killed by C∞ smoothing but at the cost of a worse window
constant — the C∞ kernels tested in the notes make the bound vacuous at accessible T). The
measured gap direction means **finite-T corrections currently help the record, not hurt it.**

RESULT: CHECKED NUMERICALLY — finite-T gap Δ>0 at all T≤5000 for both √2 and α=1.49 windows
(0.025–0.066, decaying ~1/log T); overshoot direction is safe; asymptote of Δ is INCONCLUSIVE.
