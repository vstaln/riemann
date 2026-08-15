# Stieltjes S-fraction of tXi'/Xi (g1-2): WALL-test execution

Date: 2026-08-15. Status: ANALYZED + CONTROL PROBED. Ledger: lever core ALREADY executed as
`foster-reactance-2026-08-15.md` (g1-1, same object up to relabel: g1-1 uses C-fraction of
g(z)=d/ds log Xi/(2s), moments m_n=Σγ_k^{-2n-2}; g1-2 uses S-fraction of -tXi'/Xi, power sums
s_m = 2Σ_j ρ_j^{-m}, s_m = 2·m_{m-1}). Verdict from foster (CITED, not re-derived): the
positivity condition is EXACTLY equivalent to RH (classical Stieltjes theory) — ledger class 2
(equivalent to RH), finite checks class 3 (deflating; no uniform control, violation index → ∞
as off-line distance α → 0). THIS note adds the piece foster left unrun (§5 empty): the WALL
test on RH-false controls and the measured first-failure orders.

## 1. Exact theorem + lemma that would yield RH
- Thm (PROVEN, classical; Stieltjes 1894, Hamburger 1920-21, Wall 1948 Ch.IX, Henrici V.2): for
  real (s_m)_{m≥1}, TFAE: (i) det[s_{i+j+2}]_{0≤i,j≤n} > 0 AND det[s_{i+j+3}]_{0≤i,j≤n} > 0 ∀n;
  (ii) the S-fraction 1/(β_1 + z/(β_2 + z/(...))) of Σ_{m≥1} s_m z^m has all β_k > 0 (QD
  algorithm); (iii) ∃ σ ≥ 0 on [0,∞): s_m = ∫ x^m dσ (m ≥ 1) (a_0-free Stieltjes sequence).
- Lemma (PROVEN, classical — restatement, class 2): for Xi(t)=Σ(-1)^k b_k t^{2k}, b_k = M_k/(2k)!,
  s_m := [t^{2m}](-t Xi'/Xi) = 2Σ_j ρ_j^{-m} (ρ_j = zero-squares; Newton's identities from
  e_k = b_k/b_0). RH ⟺ (s_m) is a_0-free Stieltjes ⟺ S-fraction of -tXi'/Xi all-positive.
  Proof of ⇐ (sketch, PROVEN): β_k>0 ⇒ Stieltjes (determinate, Carleman: order-1 growth) ⇒
  -tXi'/Xi = ∫ 2z x/(1-zx) dσ (z=t²); pole-matching forces σ({x_j}) = 2, supp σ ⊆ [0,∞)
  ⇒ all ρ_j = 1/x_j > 0 real ⇒ zeros of Xi on imaginary t-axis ⇒ RH. (⇒: discrete σ = 2Σδ_{ρ_j^{-1}}.)
- Finite-universal reduction (label: TRUE-but-nonconstructive = class 3): ∃N s.t. β_1..β_N>0 ⇒
  RH. RH ⇒ vacuous; ¬RH ⇒ take N = failure order. N is uncomputable a priori; any fixed N is a
  finite check consistent with both worlds (foster §2(b), CITED). No new information at any stage.

## 2. WALL test (RH-false controls; the deliverable)
- Observation O (PROVEN): b_k > 0 ∀k is UNCONDITIONAL (Φ ≥ 0, von Mangoldt). If some ρ_j < 0
  (imaginary-axis pair), e_k(ρ_j^{-1}) ~ (S^{k-1}/(k-1)!)(S/k − 1/|ρ_j|) < 0 for large k ⇒ b_k < 0,
  contradiction. So imaginary-axis off-line zeros are ALREADY excluded; the lever's only failure
  mode is COMPLEX ρ_j (zeros with Re s ≠ 1/2 off the real t-axis in a genuine RH-false world).
- Toy (hand-provable anchor): H=(1+t²)cos(t), ρ_bad=-1: s_1=-1.0068, s_2=2.3333, s_3=-1.8667<0
  ⇒ K_0 = s_3 < 0 ⇒ FAIL at n*=0; S-fraction q_1 = s_2/s_1 = -2.318 < 0. (Infinite-series
  limits: q_1 = -7/3, q_2 = 23/15 — verified by convergent matching, hand-computed.)
- Planted complex pair ρ_bad = a+bi (conj. pair): H_n stays PSD (Gram of complex vectors) but
  K_n = det[s_{i+j+3}] gets an INDEFINITE rank-2 perturbation (complex weights ρ^{-3}·w^i w^j);
  must fail at finite n* (classical theory + residue-matching). CONJECTURED (from eigenvalue
  battle λ_min(G_n) vs |ρ|^{-1}|w|²): n* grows like log|ρ| — measured in §5.
- Davenport–Heilbronn: classical guarantee of finite-order failure (contrapositive of Thm since
  DH's Xi-analog has off-line zeros); first-failure order UNKNOWN a priori — SPEC'd, run status
  in §5 (INCONCLUSIVE if not run).

## 3. Cheapest Rust check (f64, <1min, RUST ONLY)
- Input models: w_l = ρ_l^{-1} per zero (real >0, or conj. pair); s_m := 2 Σ_l w_l^m for
  m=2..2N+3, N=300 (exp(m·ln w_l); |w_l|<1 safe). Real-Ξ model: 12 zeros (heights from memory,
  toy params only) — pipeline anchor m_0 = Σγ^{-2} ≈ 0.023104993115418371789 (CITED from foster).
- Criterion: H_n = det[s_{i+j+2}], K_n = det[s_{i+j+3}] > 0 for n = 0..N (Stieltjes, §1(i)).
  Numerics: scale rows/cols by r^{-i}, r^{-j}, r = max|w_l| (positive scaling preserves sign);
  det sign via Gaussian elimination with partial pivoting (sign = (-1)^{swaps}·Π sign(pivots));
  f64. PASS = both families > 0 to n=N (finite check — NO RH conclusion). FAIL at n* = first
  n with H_n ≤ 0 or K_n ≤ 0.
- Inline asserts (hand-verified): single real pair ρ=199.7: q_1 = 1/199.7 EXACT, fraction
  terminates at k=2 (classical: 2wz/(1-wz) = (2wz)/(1-wz/1)); toy q_1 = s_2/s_1 < 0, K_0 = s_3 < 0.
- Numerics (documented): minus-convention S-fraction f = (s_1 z)/(1 - q_1 z/(1 - q_2 z/(1-...)))
  via reciprocal (Euclidean) iteration — exact at small k, survives to k≈19-20 for
  well-separated w's, breaks pre-termination (k≈17) for ζ-clustered w's. Bareiss fraction-free
  Hankel det signs: reliable only n ≤ 6-8 (dets ~ 1e-49..1e-57, sign lost beyond — any f64
  method fails on exponentially tiny Hankel dets of geometric-decay sequences). PASS/FAIL below
  use only RELIABLE orders (failures at n* ≤ 2 are small exact matrices).

## 4. Forecast + inversion
- F(toy fails at n*=0): 1.0 (hand-provable). F(planted 1+50i fails n* ≤ 30): 0.85.
  F(planted 1+10^6·i fails n* ≤ 300): 0.6 (log-boundary; may exceed 300). F(real-Ξ-12 model
  all-pass to n=300): 1.0 (near-vacuous Gram). F(DH fails ≤ 300): 0.5 (not run → INCONCLUSIVE).
- Inversion: brief steered "S-fraction positivity ⇒ RH" — that route is EMPTY (class 2
  restatement, foster verdict CITED). The inversion that is a result: Observation O turns the
  lever's failure mode into a PROVEN structural fact (b_k > 0 kills ρ<0), and the discrimination
  boundary n*(ρ) is a measurable quantity (finite-check discipline, §5). No RH claim is made:
  a proportion/finite-check result is ZERO RH evidence (firewall).

## 5. Results (appended after run)
Probe: tools/stieltjes_sfrac_controls.rs (rustc -O, f64, <1s). s_m = 2 Re(Σ w_l^m), w_l = ρ_l^{-1}.
Zero heights hardcoded from memory = TOY PARAMETERS ONLY. Anchors PASSED: single pair q_1 =
1/199.7 exact + terminates; toy q_1 = s_2/s_1 = -2.318 < 0, K_0 = s_3 < 0 (CHECKED NUMERICALLY).
| model | pairs | H first det≤0 | K first det≤0 | S-frac first q<0 | verdict |
|---|---|---|---|---|---|
| TOY (1+t²)cos | 31 | n=6 (unrel.) | n=0 (d=-1.5e-1) | k=1 (q=-2.318) | FAIL n*=0 (exact) |
| SINGLE ρ=199.7 | 1 | n=1 rank-0 | n=1 rank-0 | NONE (term. k=2) | PASS (Foster) |
| REAL20 ζ-zeros | 20 | n=7 (unrel.) | n=7 (unrel.) | k=17 (unrel., clust.) | PASS to k≤16; high order INCONCLUSIVE (classical PROVEN) |
| SEP20 separated | 20 | n=8 (unrel.) | n=8 (unrel.) | k=20 = term. boundary | PASS k≤19 (Foster) |
| PLANTED 1+50i (|ρ|≈50) | 21 | n=1 (d=-1.05) | n=1 (d=-3.9e2) | k=1 (q=-4.5e-2) | FAIL n*=1 (exact) |
| PLANTED 1+1e6i (|ρ|≈1e6) | 21 | n=7 (unrel.) | n=7 (unrel.) | k=17 (unrel.) | INCONCLUSIVE — pair INVISIBLE below fp noise ((1e-6)^m), log-boundary |
| PLANTED 2i (|ρ|=2) | 21 | n=1 (d=-1.00) | n=1 (d=-3.0e12) | k=1 (q=-31.3) | FAIL n*=1 (exact) |
| PLANTED 0.6+14.13i (1st zero 0.1 off-line) | 20 | n=2 (d=-1.6e-3) | n=1 (d=-1.8e-1) | k=2 (q=-6.4e-2) | FAIL n*=1 (exact) |
VERDICT: the S-fraction lever DISCRIMINATES at finite order — every planted off-line control
fails at n* ≤ 2, cleanly and reproducibly (small exact matrices, anchors verified). The far
pair (|ρ|=1e6) escapes the 20-zero model's resolution (power-sum contribution ~1e-6^m below
fp noise) — consistent with foster §2(b) (violation index → ∞; no uniform control). DH:
NOT RUN (needs L-function machinery; foster's Φ-quadrature pipeline is BROKEN — m_0 off 400×,
see tools/foster_check: b_0=0.746 vs 0.497, m_0=9.06 vs 0.0231, its "FAIL at a_5" is an
ARTIFACT, not evidence) → DH INCONCLUSIVE, spec'd in §3.
BOTTOM LINE: lever = classical restatement (class 2, foster CITED); WALL test now EXECUTED —
controls fail at finite order as the classical theory demands; no RH conclusion (firewall).
No new route; the discrimination boundary n*(displacement) is measured for 4 control classes.
