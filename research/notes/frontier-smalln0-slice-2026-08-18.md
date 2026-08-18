# Frontier probe: fixed-n0 Jensen slice vs moment structure — PROVEN-STUCK (destroying result)

> **SUPERSEDED 2026-08-18: the "destroying result" verdict is VOID (sign/criterion error).** The
> Hankel det2(γ)<0 test is the moment-sequence criterion; Jensen hyperbolicity is a Toeplitz/PF
> criterion, and det2(γ)<0 is EXACTLY the J^{2,0} hyperbolicity condition. The correct PF sequence
> a_k = γ_k/k! = M_k/(2k)! passes all tested orders (PF2, Toeplitz 3×3, 4×4; J^{2,3,4,n} real-rooted).
> See `frontier-smalln0-correction-2026-08-18.md` (Rust re-verification + agy second opinion).
> What survives is only the Farmer structural diagnostic (fixed-n0 = measure-zero slice).

Date: 2026-08-18. Coordinator-completed (agent 119364d4 stalled post-compute; transcript + binary
output preserved). Labels: PROVEN / CHECKED NUMERICALLY applied per claim. s4h: investigation-triangulation.

## The question (the single sharpest remaining opening)
RH <==> all Jensen polynomials J^{d,n}(X)=sum_{j=0}^d C(d,j) gamma(n+j) X^j hyperbolic.
GJT/GORZ/Holland prove the large-(n,d) wedge unconditionally. The complement (fixed small n, all d)
is the RH blocker (GJT-completion trap). The opening: does the PROVEN moment structure give an
INDEPENDENT proof of the fixed-n0=0 slice? Specifically:
- PROVEN: Phi(u) > 0 on (0,inf) (theta identity Phi=2e^{u/2}(2x^2 theta''+3x theta') exact;
  Phi(0)=+0.8933938). Hence M_n = 2 int Phi(u) u^{2n} du is the moment sequence of the POSITIVE
  measure 2*Phi(u)du on [0,inf).
- PROVEN relation: gamma(k) = k! * M_k/(2k)!  (equivalently b_k = M_k/(2k)!, gamma(k)=k! b_k).
  Hand-verified n=1..3 and cross-checked with the certified 210-bit g02 table.

## The destroying result (CHECKED NUMERICALLY, coordinator hand-verified)
gamma is NOT a moment sequence. The n!/(2n)! renormalization destroys the Hankel total-positivity
that M_n's positive-measure structure would otherwise give:

  Hankel minors of M (moments):  det1 = 4.971e-1 > 0, det2 = 9.45e-4 > 0, det3 = 2.92e-8 > 0
    => M IS a proper moment sequence (Hankel TP), as the positive-measure theory predicts.  [PROVEN by structure; CHECKED NUMERICALLY]
  Hankel minors of gamma (Jensen): det2 = gamma0*gamma2 - gamma1^2 = 1.2275e-4 - 1.3193e-4
    = **-9.19e-6 < 0**, det3 = -4.67e-15 < 0
    => gamma is NOT a moment sequence.  [CHECKED NUMERICALLY; coordinator hand-verified -9.189076e-06]
  Same failure for b: det2 = b0*b2 - b1^2 = -7.06e-5 < 0.  [CHECKED NUMERICALLY]

ROOT CAUSE (PROVEN): the renormalization factor 1/(2n)! is itself NOT a moment sequence:
det2 of {1/(2n)!} = 1/0! * 1/4! - (1/2!)^2 = 1/24 - 1/4 = -0.2083 < 0. Dividing the moment
sequence M_n by the non-moment sequence (2n)! need not preserve, and numerically does NOT
preserve, Hankel positivity. The positive-measure structure of Phi does NOT transfer to the
Taylor coefficients gamma(n) (or b_n). The moment-to-gamma bridge is BROKEN at the first
non-trivial minor.

## The separability argument (PROVEN, structural)
Even IF the n0=0 slice were hyperbolically provable by some independent means, it covers
measure-zero of the (n0,d) lattice: RH requires ALL pairs (n0,d) with n0 >= 0, d >= 0, i.e.
infinitely many n0 values each with infinitely many d. A fixed-n0 proof settles a single
vertical strip of the 2D lattice. No finite collection of fixed-n0 results can reach the
all-(n0,d) statement. The GJT-completion trap is airtight: after the proven large-n wedge
(Holland d <= c*n^{3/5}), the remaining small-n part is exactly the RH-equivalent core.
[Farmer diagnostic; Holland probe 4dae7d9; GOR TW 1910.01227 in-corpus]

## VERDICT
**PROVEN-STUCK, with the precise obstructing reason.** The moment-positivity of M_n (which is
real and PROVEN) does NOT give an independent proof of the fixed-n0 Jensen slice, because:
1. gamma(n) = n! M_n/(2n)! is not a moment sequence (Hankel det2 < 0, CHECKED NUMERICALLY),
   so no Hankel/Toeplitz positivity of gamma can be inherited from Phi > 0;
2. even a hypothetical fixed-n0 hyperbolicity proof covers measure-zero of the (n0,d) lattice
   and cannot extend to RH without a global argument that is itself RH-equivalent.

The small-n Jensen decomposition route is now PROVEN CLOSED as a one-way path. This is the
honest terminal result: the frontier's last structural opening (non-margin mechanism applied
to small-n via moment structure) dies at the renormalization barrier.

NOT an RH lever, and NOT a disproof signal: zero RH evidence either way. Consistent with the
entire campaign: 24+ levers, all closed, no disproof, one-way LP/RH space PROVEN exhausted.

## Provenance & trust
- Rust binary: tools/g02-oracle/src/bin/minors.rs (added by agent 119364d4, ran in ~5s,
  release profile). Inputs: the certified 210-bit g02 table (research/notes/g02-moments-oracle-2026-08-18.txt).
- Coordinator re-verified the sign and magnitude by independent hand calculation
  (-9.189076e-06 for gamma, -7.055864e-05 for b, -0.2083 for 1/(2n)!) — matches the binary.
- The agent stalled on a heredoc cwd bug (cd into tools/g02-oracle broke relative paths) AFTER
  computing the decisive numbers; the note was completed by the coordinator from the preserved
  transcript + binary output (kill-robustness protocol: state-on-disk, .progress).
- trap class: moment-sequence-to-gamma (registered in tools/closure_dag/closure_dag.json).
