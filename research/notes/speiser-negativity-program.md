# Speiser lane — the negativity program: Re(ζ′/ζ) < 0 in 0<σ<1/2

Author: architect subagent, 2026-08-22 session. Status: SKELETON → refining.
Labels used: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.

## 0. Working conjecture (corrected sign, from wave-rh5 ledger)

**(W)** Re(ζ′/ζ)(s) < 0 for all 0<σ<1/2, t≥10 away from zeros of ζ.
Certified numerically on σ∈{0.05..0.45}, t∈[14,70000] step 2 (207210 pts, wave-rh5(E)).
This document derives the exact decomposition behind (W), states the dominance lemma L,
attempts it, and completes the honestly-provable partials.

## 1. Exact Hadamard log-derivative decomposition (derivation)

Completed zeta: ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s), entire, order 1, ξ(s)=ξ(1−s).
Hadamard: ξ(s) = ξ(0)·Π_ρ (1−s/ρ) (product over ALL nontrivial zeros, symmetric-pairing
convergence; Titchmarsh, Theory of ζ, §2.12). Log-derivative:

    ξ′/ξ(s) = Σ_ρ^{reg} 1/(s−ρ),
    ξ′/ξ = 1/s + 1/(s−1) + ½log π + ½ψ(s/2) + ζ′/ζ      (ψ = Γ′/Γ).

Pairing ρ (upper half) with its functional-equation partner 1−ρ̄ = (1−β)+iγ (also upper
half), the regularized series becomes ABSOLUTELY convergent (per-pair O(|2s−1|/γ²),
density log γ dγ ⇒ Σ converges):

**(D)**  ζ′/ζ(s) = −1/s − 1/(s−1) − ½ log π − ½ ψ(s/2) + Σ_{γ>0} [ 1/(s−ρ) + 1/(s−1+\barρ) ]

Archimedean background: **B(s) := −1/s − 1/(s−1) − ½log π − ½ψ(s/2)**;
zero sum: **Z(s) := Σ_{γ>0} P_ρ(s)**, P_ρ(s) = 1/(s−ρ) + 1/(s−1+\barρ) = (2s−1)/((s−ρ)(s−1+\barρ)).
Trivial zeros/pole: already inside B via the ½s(s−1) and Γ(s/2) factors (pole s=1 → −1/(s−1);
trivial zeros −2n live in Γ(s/2) → −½ψ(s/2)); NO separate terms needed. [to be numerically
confirmed below — if it disagrees, THIS FORMULA IS WRONG and gets iterated.]

### Key sign structure (the heart of the lane)

Write ρ = β+iγ. Real part of a pair term at s=σ+it:

    Re P_ρ(s) = (σ−β)/((σ−β)²+(t−γ)²)  +  (σ+β−1)/((σ+β−1)²+(t−γ)²).

**The second term is ALWAYS negative for σ<1/2 (any β∈(0,1)). The first is negative iff β>σ.**
So positivity of Re(ζ′/ζ) can come ONLY from zeros with β<σ near height t.
Under RH (β=1/2>σ) every term is negative ⇒ (W) follows immediately once Re B<0.
This is the classical "RH ⇒ Speiser" made termwise-explicit.

## 2. Lemma L (dominance) — statement and status

**(L)** For all 0<σ<1/2, t≥10:  Z(s) < −Re B(s)   (equivalently Re(ζ′/ζ)(s)<0).
Since Re B(s) = −½ log(|s|/2)·(1+o(1)) + O(1/t) ≈ −½log(t/2π) < 0 for t>2π,
L asks the zero sum to stay below a *negative* moving target — the partners help for free.

Reduction (exact, see Prop B below): L ⟺ for every s in the strip,
Σ_{β_γ<σ} (σ−β_γ)/((σ−β_γ)²+(t−γ)²) < −Re B(s) − (always-negative partners).
A single off-line zero at distance d, depth (σ−β), flips the sign iff roughly
d² ≲ 2(σ−β)/log t. So L is equivalent to a *pointwise-in-t* exclusion of deep-left zeros
at radius ~(σ−β)^{1/2}/√(log t).

Attempted inputs: Montgomery pair correlation (2-pt statistic — averaged, not pointwise);
GOE form factor (same averaging defect); Carneiro–Chandee sharp pointwise bounds for S(t)
(unconditional (¼+o(1))log t — controls arg ζ on the line, not the off-line log-derivative);
zero-density (Huxley N(σ,T) ≪ T^{A(1−σ)}): dies because A(1−σ)>1 for all σ<1/2 ⇒ no
pointwise-per-height control of left zeros. Labels: all four CONJECTURED-or-insufficient
as pointwise inputs; details + citations in §4.

**THE missing estimate (one sentence):** a per-height (non-averaged) upper bound showing
that zeros with β<σ cannot push Σ_{β<σ}(σ−β)/((σ−β)²+(t−γ)²) above −Re B near height t —
no current zero-density method operates pointwise in t for any σ<1/2.

## 3. Unconditional/conditional partial results (full proofs in §5)

- (a) **Prop B (exact reduction, PROVEN below):** the inequality displaying the always-negative
  partner term; reduces L entirely to deep-left-zero kernels.
- (a′) **Prop C (left of the strip, PROVEN below):** Re(ζ′/ζ)(s)<0 uniformly for σ≤−δ, |t| large,
  via χ′/χ(s) − ζ′/ζ(1−s) with Dirichlet-series control at Re(1−s)>1.
- (b) **RH ⇒ (W): PROVEN below** (termwise-negative pairs + Re B<0 + absolute convergence).
  Known to Speiser/literature; our derivation fixes the dependency structure explicitly.
- (c) Monotonicity in σ: CHECKED NUMERICALLY below before any claim.

## 4. Numerical verification of (D) — [run outputs pasted in §6]

Ground truth: mpmath 40-digit ζ′/ζ via mp.diff. Decomposition: repo zeros
(tools/data/zeros_rust_100k.txt) + tail estimate. Acceptance: agreement ≤1e-8 at
s=0.05+16i (target −0.6281573984651) and s=0.45+22016i (target −33.35930407273).
Script: tools/jensen_probe/scripts/speiser_decomp_check.py (ponytail exemption: Python is
mandated by the task for the independent 40-digit recheck wave-rh5 marked INCONCLUSIVE).

## 5. Verdict & next actions

Verdict (draft, to finalize): L is a genuine RH-difficulty open problem; the pairing
reframing ("RH ⟺ deep-left kernels never dominate the always-negative partners") is the
sharpest known form. Ranked next actions in §7.
