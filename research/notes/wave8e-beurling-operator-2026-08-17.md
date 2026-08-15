# wave8e — Beurling-operator route: finite Gram shadows of the Nyman–Báez-Duarte criterion

Status: IN PROGRESS (seed written at t=5; first attempt killed, resumed fresh)
Date: 2026-08-17
Joint: 8E (retry). Structural twin of 8C (same objects Λ_k, operator side instead of d_N).
Progress log: research/notes/wave8e-beurling-operator.progress
Probe: tools/wave8e/ (Rust, rug/MPFR).

## Plan (from brief)
1. Pin EXACT modern equivalent of RH (operator + spectral condition), cite file+line.
2. Build Gram system G_N(j,k) = <Λ_j,Λ_k>_{L^2(0,1)}, Λ_k(x) = {1/(kx)}; λ_min(N) for N to ~2000 (rug, ill-conditioned); fit decay; cite the rate theorem.
3. OBJECT: eigenVECTORS of G_N → explicit-formula kernel (Burnol); quantify discrepancy. λ_min(N)·√N·(log N)^{1/2} → const: compute, compare to known value.
4. RH-false control FIRST: planted-zero fake — λ_min'(N) must saturate > 0 and eigenvector content visibly different.
5. VERDICT.

## Mathematical anchor points (TO VERIFY against corpus — labels provisional)
- Nyman (1950): RH ⟺ span{θ_a(x) = {a/x} : 0 < a ≤ 1} dense in L²(0,1). Beurling (1955): p-generalization, density in L^p(0,1) ⟺ no zeros in Re(s) > 1/p.
- Báez-Duarte (2003, IMRN "A sequential Nyman–Beurling equivalent for the RH"; Atti Accad. Naz. Lincei 14): RH ⟺ span{Λ_k(x) = {1/(kx)} : k ≥ 1} dense in L²(0,1); RH ⟺ d_N = dist(1, span{Λ_1..Λ_N}) → 0.
- Quantitative rate: KNOWN that if RH ⟹ d_N = O(N^{-1/2} log N) or similar — MUST pin exact statement (Báez-Duarte IMRN 2003, Thm? / Burnol). The brief claims λ_min(N)·√N·(log N)^{1/2} → const is the discriminating number. STATUS: INCONCLUSIVE until cited.
- Burnol: Hilbert-space reformulation via the explicit formula (Fourier–Mellin operator on L²(0,∞)); positivity of the Weil distribution ⟺ RH. Only .pdf available; will pdftotext.

## Key subtlety to resolve (self-check)
λ_min(G_N) → 0 (linear dependence of Λ_1..Λ_N in L²(0,1)) is NOT literally the same as d_N → 0 (1 ∈ closure of span). Need the exact statement: which spectral object the cited theorem uses (smallest eigenvalue of truncated Gram system vs distance d_N vs operator norm of the "M" / Beurling matrix). The brief's "λ_min(N)·√N·(log N)^{1/2} → limit" claims a precise equivalent — find the theorem, else mark INCONCLUSIVE and report d_N-side instead.

## Control (planted-zero fake)
Brief: from 8A/8D ξ′-type fake. Need construction details from ledger/8A notes. λ_min'(N) must saturate > 0. TO DO.

## Closed form of G_N (derive independently; verify vs 8C approach if any artifact found)
Substitute u = kx: <Λ_j,Λ_k> = (1/j)·? — actually compute directly:
<Λ_j,Λ_k> = ∫_0^1 {1/(jx)}{1/(kx)} dx.
On x ∈ (1/(j(m+1)), 1/(jm)] value 1/(jx) - m. Exact rational + ζ(3)-type sums. Derive in probe.
Norm²: ‖Λ_k‖² = (1/k)[ Σ_{m≥1} ∫_0^1 t²/(t+m)² dt + 1 - 1/k ] (derivation: u=kx, split u∈(0,1) steps + u∈(1,k) tail). CHECK NUMERICALLY.

## Verify plan (Rust, rug)
- tools/wave8e/src/main.rs: build G_N exactly (rug rational), compute λ_min via QR/... ill-conditioned → use MPFR with ~256-bit or exact rational then float.
- eigenvector of smallest λ; compare to Burnol kernel (once pinned).
- control: same code with planted-zero-modified object.
