UNIQUE ideas: 15

== g0-0 ==
ASSUMPTION-EXCAVATOR. Hidden assumption: the moment representation b_k=2∫_0^∞ Φ(u)u^{2k}du/(2k)! gives a nonnegative density Φ, so the Hankel matrix of shifted moments is totally positive. Move: prove this total positivity directly by the Cauchy–Binet determinant formula: det(b_{i_a+j_b}) = ∫...∫ det(u_l^{i_a+j_b}) ∏ Φ(u_l) du_l, which is >0 because the kernel (u_l^{i_a+j_b}) is a Vandermonde-type totally positive kernel on (0,∞). Then invoke Edrei–Thoma's theorem that a totally positive Hankel 

== g0-1 ==
CROSS-DOMAIN ANALOGY. Solved problem: the Lee–Yang theorem for the Ising model shows the partition function has all zeros on the unit circle; the key operator is the Asano contraction that preserves half-plane properties. Isomorphism: J_{n,d}(z)=∫Φ(u)u^{2n}(1+u^2 z)^d du is the mixture of the d-fold product of degree-one Lee-Yang polynomials (1+u^2 z), each of whose zeros is -1/u^2 on the negative real line. Transportable step: treat ∫Φ(u)u^{2n} du as a statistical-mechanics average over an exte

== g0-2 ==
CONSTRAINT-HARDNESS-TESTING. Apparent wall: RH is an infinite universal condition; every finite prefix of Jensen polynomials can be hyperbolic while a later one is not, so no finite coefficient computation decides the all-quantifier. Move: route around by compactness via Gaussian quadrature. Lemma: for every N there exists a discrete positive measure μ_N, with N atoms, whose first 2N moments equal the moments of Φ, because the moment matrix is positive definite; the polynomial Q_N(z)=∫(1+u^2 z)^

== g1-0 ==
1) ASSUMPTION-EXCAVATOR. Hidden assumption: every calculation that starts from H(t)=∫ cos(tu)Φ(u)du treats positivity of Φ as already forcing Laguerre–Pólya behavior, but a positive measure can have non-real Fourier–cosine zeros (e.g. 1+a(e^{it}+e^{-it}) for 0<a<1/2). The silently used extra ingredient is total positivity of the cosine family as a kernel in u. Move: prove the lemma that H(t)=Xi(1/2+it) has only real zeros iff the normalized coefficient sequence c_k=M_k/(2k)! is a Pólya frequency

== g1-1 ==
2) CROSS-DOMAIN ANALOGY. Domain: electrical circuit theory, Foster's reactance theorem. Solved problem: a passive LC one-port has an odd immittance Z(s) with Re Z(s)≥0 for Re s>0 iff Z(s)=Σ c_n s/(s²+ω_n²), c_n≥0, ω_n∈R; this forces all poles and zeros of Z to be real and to interlace. Transferable step: identify F(s)= d/ds log Xi(1/2+is) with the immittance of an infinite LC network. Conjecture/prove: F is a positive-real odd function. By Foster's theorem this is equivalent to F(s)=Σ c_n s/(s²+

== g1-2 ==
3) CONSTRAINT-HARDNESS-TESTING. Apparent wall: no finite set of Laguerre or Turán inequalities at sampled points can settle RH, because a nonreal pair of zeros can be inserted by changing only far-tail Taylor coefficients while preserving every finite prefix. Move: route around the wall by showing RH is equivalent to positivity of the continued-fraction coefficients in the S-fraction t H'(t)/H(t)=1/(b_1 + t²/(b_2 + t²/(b_3+...))). By the classical Stieltjes continued-fraction theorem, all b_k>0 

== g2-0 ==
Idea 1 (Assumption-excavator): The hidden assumption silently used by finite Taylor-coefficient tests is that Xi already belongs to the Laguerre-Polya class, i.e. that all Jensen polynomials J_n(Xi)(x) are hyperbolic for every n and every real x; this is equivalent to RH by Hermite-Poulain. Lemma to prove: the continuous family of Laguerre inequalities D_n(x) = sum_{k=0}^n (-1)^k binom(n,k) Xi^{(k)}(x) Xi^{(n-k)}(x) >= 0 holds for all real x and all n. Candidate mechanism: substitute Xi^{(k)}(x)

== g2-1 ==
Idea 2 (Cross-domain analogy, statistical mechanics / Lee-Yang circle theorem): The solved problem is the Lee-Yang theorem proving Ising partition functions have all zeros on the unit circle by Asano contractions and Ruelle correlation inequalities; the critical line Re(s)=1/2 is mapped to |w|=1 by w=(s-1)/s, with s=1/(1-w), so RH is exactly the statement that G(w)=Xi(1/(1-w)) has no zeros with |w|<1. Lemma to prove: the N-th Taylor truncations G_N(w) of G(w) are Lee-Yang polynomials, i.e. G_N(w

== g2-2 ==
Idea 3 (Constraint-hardness-testing): The apparent wall is that no finite Taylor prefix can force RH, since high-degree perturbations can always create a conjugate pair off the critical line without changing any finite prefix. Move: route around the wall by proving a deformation statement: the de Bruijn heat-deformed family H_t(z)= integral_0^infty e^{t u^2} Phi(u) cos(z u) du has only real zeros for every t>0; then argument-principle continuity H_t -> H_0 forces H_0=Xi to have only real zeros. 

== g3-0 ==
Lens ASSUMPTION-EXCAVATOR. Hidden assumption: every finite Taylor check treats positivity of finitely many Laguerre expressions as evidence of real zeros, but RH requires all of them. Move: prove the coefficient sequence b_k is strictly totally positive (STP). Lemma (Edrei–Karlin): if all minors of H=(b_{i+j-2})_{i,j≥0} are positive, then F(z)=∑ b_k z^k has only negative real zeros, so Xi(s)=F(s^2) has only real zeros. Exactly prove STP by applying the Karlin–McGregor determinant identity to the

== g3-1 ==
Lens CROSS-DOMAIN ANALOGY. Domain: signal processing / Pólya-frequency theory. Solved problem: Schoenberg characterized kernels whose Fourier transform has only real zeros — a PF density convolved with itself gives B-splines and Fourier transforms like sinc^N with all real zeros. Isomorphic structure: Xi(t)=2∫Φ(u)cos(tu)du is the cosine transform of Φ; in Schoenberg's theorem the Fourier transform of a PF density has a product representation with only real zeros. Transportable step: do not attac

== g3-2 ==
Lens CONSTRAINT-HARDNESS-TESTING. Apparent wall: coefficient-only criteria (Newton, Hutchinson) cannot be necessary and sufficient for entire functions — for Xi, the normalized coefficient ratio b_{k-1}b_{k+1}/b_k^2 tends near equality, so any 4-ratio inequality wall is real for that route. Route around the wall: reduce to the Lee–Yang circle theorem from statistical mechanics. Lemma: for every N, the polynomial Q_N(z)=∑_{k=0}^N b_k z^k belongs to the Lee-Yang class (zeros on |z|=1) after the sc

== g4-0 ==
1. Domain: statistical mechanics (Lee-Yang theorem). Solved problem there: proving that ferromagnetic Ising partition-function zeros in a complex magnetic field lie on the unit circle; the transferable mechanism is Asano contraction plus a positivity/cone argument. Structural isomorphism: RH is equivalent to every Jensen polynomial g_n(z)=Σ_{k=0}^n C(n,k) γ_k z^k being real-rooted; Lee-Yang theory produces exactly the same shape by contracting product polynomials and forcing zeros of a limit to 

== g4-1 ==
2. Domain: signal processing / moment problems (Carathéodory-Fejér, Pólya frequency sequences). Solved problem there: deciding whether a moment/autocorrelation sequence comes from a positive measure by checking total positivity of a Hankel/Toeplitz kernel; the mechanism is that variation-diminishing kernels force interlacing/real-rootedness. Structural isomorphism: Xi(t) is an even entire function with coefficients c_k=M_k/(2k)!; RH asserts Xi is in the Laguerre-Pólya class, which can be certifi

== g4-2 ==
3. Domain: control theory / Hurwitz stability and positive-real (passive) transfer functions. Solved problem there: proving a feedback system is stable by showing its impedance/reflection function is positive real; positivity of real parts implies root locations via the Herglotz-Nevanlinha representation. Structural isomorphism: let H(t)=Xi'(t)/Xi(t). If all zeros of Xi are real, then H maps the upper half-plane to the upper half-plane, i.e. H is Herglotz; equivalently Z(s)=-i H(i s) is positive

---
SOURCE: LangGraph swarm wave-20 (killed after exponential-dup bug discovered; the 15 unique
ideas above are the uncorrupted harvest). All labels CONJECTURED — none verified.
CONVERGENCE: Lee-Yang / Asano-contraction route appeared in generators 0, 2, 3, 4 independently
(g0-1, g2-1, g3-2, g4-0). Foster-reactance (g1-1), total-positivity/Cauchy-Binet (g0-0, g3-0),
S-fraction Stieltjes continued fraction (g1-2), de Bruijn heat-deformation (g2-2) also present.
STATUS: harvest only. Next: route each through pi-native subagents (builder/executor + hostile
reviewer), not through the LangGraph script.
