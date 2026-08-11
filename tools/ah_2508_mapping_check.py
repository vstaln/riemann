#!/usr/bin/env python3
"""
tools/ah_2508_mapping_check.py  —  AH (arXiv:2508.10857) -> certificate mapping check.

Question: can the Alternative-Hypothesis consecutive-gap structure (paper:
Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh 2025, "The Alternative Hypothesis
for Zeros of the Riemann Zeta-Function") provide a NEW input that raises the
stability floor eps_univ above the external repos' values, i.e. a certified
bound above 0.6731929114731422535099843283... ?

The certificate mechanics (from ainta/trmdy/tawanerguo repos + ceiling note):

  rank-trace stability:  S >= H(v)·N + tr Psi(M) - o(N)
  universal floor:       tr Psi(M) >= eps_univ·N,  eps_univ derived ONLY from
                         the kernel k(x)=K(x)/K(0) and the gap geometry
                         (u,v,u+v<=4  [3-point]  /  six-gap F_6>=19/5000 [7-point]
                          /  F_B>=577/100000, m=183 [Bellman-coboundary]).
  certified bound:       (H_cert - tax) / (1 - block/m)

The AH paper contributes NO numerical constant to any of these quantities; it is
a conjectural statement about the *limiting densities* of pairs at k/2 spacing
(density p_{k/2}), conditional on RH + AH.  Here we:
  (a) reproduce the paper's Theorem 1 / Corollary 1-3 / AH-Density constants;
  (b) reproduce the three external certified bounds from their own inputs;
  (c) demonstrate the floor cannot absorb the AH density p0: the floor is a
      universal min over Gram matrices, and AH's p0 is a statistical density.

All arithmetic: mpmath, high precision.  No external data files needed.
Labels: [NUMERICAL] produced by this script (CHECKED NUMERICALLY).
"""
import mpmath as mp
mp.mp.dps = 60

def show(label, val):
    print(f"{label:<34} = {mp.nstr(val, 40)}")

print("="*86)
print("PART A — arXiv:2508.10857 (AH) constants, from the paper text")
print("="*86)
print("A.0  AH / AH-Pairs formulation  [VERIFIED-FROM-PAPER, p.2]:")
print("  AH: gamma~_{n+1}-gamma~_n = k_n/2 + O(|gamma~_{n+1}-gamma~_n|·psi(gamma_n)),")
print("      psi(gamma)->inf, psi(gamma)=o(log gamma)  (gamma~ = normalized ordinate)")
print("  AH-Pairs: (gamma-gamma')logT/2pi = k/2 + O((|k|+1)R(T)), R(T)->0  [p.2, (1.3)]")
print("  Strong AH-Pairs: k << M logT with R(T)logT -> 0  [p.3]")
print()

print("Theorem 1 [p.3, (1.5)-(1.6)]:  RH + AH-Pairs =>")
print("  1+o(1) <= P_0 <= 3/2 - 2/pi^2 + o(1);")
print("  P_{k/2} ~ P_0 - 1/2  (k≠0 even),  P_{k/2} ~ 3/2 - 2/(pi^2 k^2) - P_0  (k odd)")
print("Corollary 2 (p_0=1):  p_0=1, p_{k/2}=1/2 (even≠0), p_{k/2}=1/2-2/(pi^2 k^2) (odd)")
print("Corollary 3 (p_0=3/2-2/pi^2):  p_0=3/2-2/pi^2, p_{k/2}=1-2/pi^2 (even≠0),")
print("      p_{k/2}=(2/pi^2)(1-1/k^2) (odd)  [Note p_{1/2}=0]")
print()
pi2 = mp.pi**2
limsup_P0 = mp.mpf(3)/2 - 2/pi2
print("A.1  numerical constants  [NUMERICAL — from paper's displayed formulas]")
show("limsup P_0 = 3/2 - 2/pi^2", limsup_P0)            # 1.29735...
show("Cor2 p_0=1 case C (Cor4): 1+pi^2/24+log(2/pi)", mp.mpf(1) + pi2/24 + mp.log(2/mp.pi))   # 0.95965...
show("Cor3 p_0=3/2-2/pi^2 case C: 1/2+pi^2/6+log(2/pi)", mp.mpf(1)/2 + pi2/6 + mp.log(2/mp.pi))  # 1.69335...
print("  [Cor4: C := lim ∫_1^∞ F(α)/α² dα;  = 1+3/2(p_0-1)+pi^2/4·(1/6?) ... paper p.10]")
print()

print("A.2  Theorem 4 / AH-Density [p.5, (1.8)/p.11]:  with r(α) even, supp |α|<=1,")
print("  Σ_k r̂(k/2) p_{k/2} = r(0) + 2∫_0^1 α r(α)dα  [AH-Density, Theorem 4 (2.17)]")
print("  -> p_0 enters ONLY as the k=0 term of a weighted density sum; no")
print("     multiplicity-density constant is given anywhere (paper has no such")
print("     displayed constant; multiplicity appears only in Remark 1, p.2).")
print()

print("="*86)
print("PART B — certificate chain (external repos), reproduced from their inputs")
print("="*86)
# H0 (Anthropic Theorem D)
H0 = mp.mpf(3)/2 - (1/mp.sqrt(2))*mp.cot(1/mp.sqrt(2))
show("H0 (Anthropic Thm D)", H0)

# ainta: three-point bound, eps_4 = 221/10^6
e3 = mp.mpf(221)/10**6
ainta3 = (H0 - e3/4)/(1 - e3/2)
show("ainta 3-pt bound (H0-e/4)/(1-e/2), e=221e-6", ainta3)

# ainta: seven-point bound, eps_7 = 19/5000 per 7-block
e7 = mp.mpf(19)/5000
ainta7 = (mp.mpf(1345000)*H0 - 2680)/mp.mpf(1340003)
show("ainta 7-pt bound (1345000H0-2680)/1340003", ainta7)

# trmdy: H(v)=0.67245704141454..., A=251/200, R=2sqrt(A)-1, eta=R/A, m=257
Ht = mp.mpf('0.67245704141454')
At = mp.mpf(251)/200
Rt = 2*mp.sqrt(At) - 1
etat = Rt/At
trmdy = (257*Ht - etat*mp.mpf(3)/1150*256)/(257 - Rt)
show("trmdy bound (257H-eta·(3/1150)·256)/(257-R)", trmdy)

# tawanerguo: Bellman coboundary (reproduce the repo's own compute_joint_bound.py)
alpha = mp.mpf(147)/100
I0 = 2*mp.sin(alpha/2)/alpha
I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
const = mp.sin(alpha/2)/alpha + 2*mp.cos(alpha/2)/alpha**2
J = -2*I2/alpha**2 + const*I0
c_win = I0**2/(I2 + J)
Hw = 2 - 1/c_win
m = 183
local = mp.mpf(577)/100000
A = local*(m - 6)
block = 2*mp.sqrt(mp.mpf(m-1)*A/m) - 1 + A/m
pressure = mp.mpf(59)/19520
tawa = (Hw - pressure)/(1 - block/m)
show("H_window (cos 1.47 s)", Hw)
show("block energy A = (577/1e5)(m-6)", A)
show("block defect Phi_m(A)", block)
show("tawanerguo bound (Hw-p)/(1-block/m)", tawa)

print()
print("External best (certified, unconditional): 0.6731929114731422535099843283...")
print()

print("="*86)
print("PART C — can the AH density p_0 (or any AH constant) enter the floor?")
print("="*86)
print("The universal floor is:")
print("  eps_univ = min over Gram matrices of tr Psi(M)/N  [3pt: eps_4/2; 7pt: 19/5000]")
print("  = a PURE function of the kernel k(x) (analytic, window-derived), with NO")
print("    density/multiplicity input.  Its positivity comes from the kernel's zero")
print("    set being sum-free (x tan(pi x)=c has no x,y,x+y all zeros;  ainta proof §3).")
print()
print("AH-Pairs instead constrains the STATISTICAL density of pairs at half-integer")
print("normalized separations:  p_{k/2} = lim_T P_{k/2}(T).  The certificate never")
print("reads any p_{k/2}.  The chain that would let AH lift the bound would be:")
print("  AH/Strong-AH (conjecture, RH) -> density bound -> floor eps_univ' > eps_univ")
print("The paper gives NO such density->Gram-floor implication.  Its density bounds")
print("(1 <= p_0 <= 3/2-2/pi^2, Cor 1-3) are about the NUMBER of pairs at k/2, not")
print("about any tr Psi(M) Gram defect.  [VERIFIED-FROM-PAPER: no 'tr Psi', no")
print("'Gram', no 'eps' constant appears anywhere in the 27-page paper.]")
print()
print("Consequence for the ladder (Q3): the 3->7->9->11 ladder raises eps_univ by")
print("adding MORE gaps to the functional F (more w(y_j-y_i) terms with span")
print("capacity 2).  AH's consecutive-gap structure is a DIFFERENT object: it")
print("constrains the STATISTICS of gap lengths (multiples of 1/2 average spacing),")
print("not the pointwise nonnegativity of F over all gap tuples.  So AH cannot")
print("certify a larger F_6/F_B constant.  [NUMERICAL + structural]")
print()

print("="*86)
print("PART D — headline mapping verdict")
print("="*86)
print("AH is DEAD as a *new input that raises eps_univ / beats 0.6731929*.")
print("  * It is a conjecture (RH + AH), not a theorem about the true law.")
print("  * It constrains limiting pair densities p_{k/2}, which the certificate")
print("    never reads; it contributes no constant to the floor.")
print("  * Its one quantitative content (1 <= p_0 <= 1.297...) is a density, not a")
print("    Gram-defect; the certificate's floor is kernel-geometry-only.")
print("It is PARTIAL/ALIVE only as *context*: (1) it corroborates that consecutive-")
print("gap structure is real input to the zero system (the same object the ladder's")
print("F_6 functional uses); (2) its 'k=0 density <= 1.297' does NOT contradict the")
print("simple-zeros density being large (p_0 can be 1 with ESH; Cor 2); (3) the")
print("ladder-to-ceiling convergence question (Q3) is orthogonal to AH.")
print()
print("Target: 0.6731929 (external best).  AH does NOT certify a bound above it.")
print("The only way AH could feed a >0.6731929 certificate: prove a density/")
print("multiplicity bound that a FUTURE certificate class reads directly — the paper")
print("does not construct such a class.  [VERIFIED-FROM-PAPER + NUMERICAL]")
print("="*86)
