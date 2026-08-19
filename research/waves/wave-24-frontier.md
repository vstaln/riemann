# Wave 24 frontier — open direct-RH inputs ONLY (2026-08-19)

**Generator rule (binding):** propose ONLY one-way objects that (a) are not on the
do-not-repeat ledger, (b) attach an RH-false control (Davenport–Heilbronn, planted-zero
Beurling, fake-Weil via tools/barrier_zoo), (c) are checkable by real compute (script +
numeric run), and (d) lead with the INPUT — NOT the fallback. Known ⟺RH equivalences
re-proposed as "success = prove RH" will be rejected by the GATE before compute.

**Negative-pattern blocklist (fresh kills, do NOT re-propose):**
- agy wave-24 C1: normalized curvature ratio Q_n = Re[ζ″/(L·ζ′)] at zeros — its own probe
  (ζ″ at height γ≈14..35) is numerically unstable (~1e29 spurious values). Dead as stated.
- agy wave-24 C2: 4th-order Turán/jet determinant Φ(t)=L₁J₂−…>0 — lane #3 structurally
  PROVEN closed (rung-2 kill κ₁^(2)=4.57≫κ₁^(1)=1.14; G²/H Cauchy fatality). Dead.
- agy wave-24 C3: Báez–Duarte coefficient-energy V(N)=(1/d_N²)Σ k·a_k² — normalized
  V/(N log N) ≈ 19–26, ~100× above claimed 0.182 (REFUTED, two independent runs). The
  unnormalized U(N)=Σ k·a_k² has no clean law (log-log slope ~1.4 noisy). Planted control
  reduces to the stored BD-criterion (restatement). ABANDONED.
- agy wave-24 C4: Mellin–Möbius Hankel radius — radius of convergence of 1/ζ at s=2 is
  pole-location (RH restated). Dead.
- Older closed majors: Gram spectral-gap → d_N; Speiser winding beyond certleft band;
  Li-positivity; Rouché-winding; Nyquist–Bode; Lee–Yang Ising; Wiener–Tauberian;
  Direction-2 soundstate 2×2 SDP (μ*≥1 measured); T-2 tower Gonek trace (G²/H Cauchy fatal);
  GS-2026 diagonal C<2; Bui–Heath-Brown (no route clears p₀); r′=3/5; weighted-L² d_N(θ)
  (shifts Mellin line, not RH); sinc-PF duality; Sturm/_1F_1.

New data since wave 23 (all CHECKED NUMERICALLY):
- r′(T): 0.8168/0.8447/0.8623/0.8688/0.8882/**0.8979** at T=150/300/600/900/3000/**6000**
  (N=5401, 96.5% capture). T=6000 came in BELOW both 1/L (0.955) and 1/L² (0.930) predictions
  → tail shallower than either pure power law. 6-point fits: 1/L → r∞=0.965 (MSE 1.05e-6,
  best), logL/L² → 0.940, 1/L² → 0.914. BHB box b≤0.059–0.063 (harder, not easier).
- Báez–Duarte δ(N)=d_N²·log N is FLAT 0.0448–0.0525 over N=10..5000 (certified MPFR),
  gentle O(1/log N) bend; d_N·√(log N)≈0.212 flat; the "rising 0.113→0.153" curve from
  wave-23-frontier was the WRONG-BASIS artifact, retracted (commit 2d43766).
- λ_min(G_N)≈0.634·N^(−1.837): spectral-gap/diagonal-dominance → d_N routes DEAD (10⁶×
  below the 1/log N bar at N=2^16). D_N G_N D_N exactly singular (D_N(1,1)=√log1=0).
- μ* Direction-2 probe: 2×2-minor λ₂/λ₁ = 0.0657→0.0111 (Y=1..1000) → μ*≥1, scalar
  Levinson extremal c₁*=0.753296 stands. Full 4×4 rank-4 (top eig 50–63% trace).

## OPEN lanes (fundable — lead with the INPUT)

1. **S₂-limit r∞ ≈ 0.91–0.97, lean 0.94–0.97 via 1/L.** The ONLY open value is a sharper
   constraint on the BHB framework (b≤0.059–0.063, harder). No positive RH route. Do not
   re-propose as RH proof.
2. **8C Báez–Duarte finite-N correction structure** (consistency-level only): extend the
   certified d_N·√(log N)≈0.212 flat law / δ(N) flat law beyond N=5000 (MPFR Cholesky OOMs
   at ≥3000); explain the small-N=10 bump (δ=0.0525 vs ~0.048 elsewhere). Genuinely new:
   any NEW structural object on this route whose planted-zero world gives a DIFFERENT law.
   Controls mandatory. NOTE: d_N bounds using only spectral info are provably wrong-shaped.
3. **ξ,ξ′ jet / positive simple-zeros certificate** — structural question: given rung-2 kill
   + G²/H Cauchy fatality, can ANY positive (simple, on-line) certificate exist on
   (ξ,ξ′)/(ξ,ξ′,ξ″) jets? Propose a real SDP/dual inequality or a proof of impossibility.
   Control: Davenport–Heilbronn must fail any candidate certificate.
4. **Weil positivity / sub-prime densities** — NEW test-function families only;
   cosine-Gram, specific-prime, sub-prime, Slepian classes are all closed.
5. **Genuinely new one-way objects.** Highest value. New arithmetic objects with ζ-value
   constraints, new discriminants that separate the RH world from a planted-zero world BY
   COMPUTATION (not equivalent restatement). The C3 coefficient-energy line just died
   (restatement risk); any new object must have a control that is NOT a stored equivalence.

## Closed / do-not-propose (recent majors)

- agy wave-24 C1–C4 (above). Gram spectral-gap; Speiser winding; Li-positivity;
  Rouché-winding; Nyquist–Bode; Lee–Yang Ising; Wiener–Tauberian; Direction-2 SDP;
  T-2 tower; GS-2026; Bui–Heath-Brown; r′=3/5; weighted-L² d_N(θ); sinc-PF; Sturm/_1F_1.
- The 0.213 proportion record and all λ-dilation saturation numbers: proportion-theorem only,
  NOT RH evidence — never propose as proof input.

## Deliverable format

For each funded probe: one file under research/waves/wave-24/ stating the object, the exact
computation, labels (PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE),
and the RH-false control verdict. No claim is progress until the control fails to break it.
