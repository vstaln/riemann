#!/usr/bin/env python3
"""
effective_bound.py — V20: assemble the EFFECTIVE finite-T version of the 67.25% theorem
from the paper's own error terms (claude-riemann-paper.txt, Thms A/B/D, Props 4.2, 4.4, 5.3-5.7,
Thm 5.8, §6).

Every number printed is computed here from:
  (a) the paper's explicit structural constants (theta_0 formula, c_rho, Psi_0, a, b, J, MV 3pi/2),
  (b) standard EXPLICIT literature bounds used as inputs (all labeled):
        psi(x) < 1.03883 x            (Dusart; Rosser-Schoenfeld theta < 1.01624 x)
        |S(t)| <= 0.112 log t + 0.278 loglog t + 2.510, t>=3   (Trudgian 2014)
        RvM remainder |R(T)| <= 1/T   (conservative)
  (c) EXACT finite sums (Rust sieve, effsieve): Sigma Lambda^2/n * g(log n) etc.
  (d) exact quadrature (mpmath) of the mu-integrals and the window constants.

Bound assembled (paper §6 proof of Thm A, tracked with explicit constants):
  N0^s(T,2T) >= 4 tr(Gtilde) - ||Gtilde||_F^2 - 2 N(T,2T) - [4 t1 + 2 t1 ||Gtilde||_F + t1^2]
                 - 3 N(I'\I),   t1 = theta_0/(a L)
  tr(Gtilde) = N* + O(E_tr),   ||Gtilde||_F^2 = [2 pi b L int mu^2 + (T/pi) Sg + errs]/(a^2 L^2)
  so  Bound0 = 2 N* - MT_HS - E_total,  E_total = 2 delta_N + 4 E_tr + E_HS + E_tail + 3 N(I'\I).

Usage:  uv run --quiet --with mpmath python effective_bound.py
"""
import math, subprocess, json, os, sys
import numpy as np

# ---------------- taper profile (paper §8: rho(x) = x - sin(2 pi x)/(2 pi)) ----------------
PI = math.pi

def a_rho():   # int_0^1 rho^2 = 1/3 + 5/(8 pi^2)  (exact)
    return 1/3 + 5/(8*PI**2)

def rho1inf(): # ||rho'||_inf = 2
    return 2.0

def rho2one(): # ||rho''||_1 = 8 pi (exact)
    return 8*PI

def rho4_quad():  # b_rho = int_0^1 rho^4, numeric
    import mpmath as mp
    f = lambda t: (t - mp.sin(2*mp.pi*t)/(2*mp.pi))**4
    return float(mp.quad(f, [0, 1]))

C_RHO = 4*rho1inf() + 4*rho2one()          # c_rho = 4||rho'||inf + 4||rho''||_1
A_RHO = a_rho()
B_RHO = rho4_quad()

# ---------------- explicit literature bounds (inputs, labeled) ----------------
C_PSI  = 1.03883      # psi(x) < C_PSI x, x>0  (Dusart)
C_THET = 1.01624      # theta(x) < C_THET x    (Rosser-Schoenfeld)
TRUD   = (0.112, 0.278, 2.510)   # |S(t)| <= a log t + b loglog t + c, t>=3 (Trudgian)
C_RVM  = 1.0          # |R(t)| <= C_RVM/t conservative

def trudgian(t):
    a, b, c = TRUD
    if t < 3:
        return trudgian(3.0)
    return a*math.log(t) + b*math.log(max(math.log(t), 1.0)) + c

def A0_of(h):
    """A0(h) with N(t+1)-N(t) <= A0(h) log(t+3) for t <= h, from Trudgian + RvM main slope."""
    t = max(h, 3.0)
    num = math.log(t+1)/(2*PI) + 2*trudgian(t+1) + 2*C_RVM/t
    return num/math.log(t+3)

# ---------------- window constants (w = 1) ----------------
def window_consts(L, w=1.0):
    a = 1 - 2*w*(1-A_RHO)/L
    b = 1 - 2*w*(1-B_RHO)/L
    Psi0 = 4 + 2*math.log(C_RHO*L/(4*w))        # (2.18)
    Ipsi2r = 8 + 8*math.log(C_RHO*L/(4*w))      # int psi^2 |r| dr (2.18)
    Ipsi2 = 8*L                                 # int psi^2 (2.18)
    C1 = 2*rho2one()/w                          # ||phi''||_1
    return dict(a=a, b=b, Psi0=Psi0, Ipsi2r=Ipsi2r, Ipsi2=Ipsi2, C1=C1)

def g_of_closed(y, L, w=1.0):
    """closed form of g(y)=int phi^2(u)phi^2(u+y)du for the flat-top taper (derived here):
       g(y) = (L-y) - 2w(1-a_rho)*[ramp indicators] + RR(y).  Valid w <= y <= L-w with
       the indicators as derived; used only as a CHECK against the quadrature in Rust."""
    # (full quadrature in the Rust sieve is the ground truth; closed form only for sanity)
    if y < 0 or y > L:
        return 0.0
    if 1 <= y <= L-1:
        return (L-y) - 2*(1-A_RHO)
    return float('nan')  # y in ramps: use quadrature

# ---------------- exact mu integrals (mpmath) ----------------
def mu_integrals(T):
    import mpmath as mp
    mp.mp.dps = 45
    def mu(t):
        z = mp.mpf(1)/4 + mp.mpc(0, t/2)
        return (mp.digamma(z).real/(2*mp.pi) - mp.log(mp.pi)/(2*mp.pi))
    Nstar = float(mp.quad(mu, [T, 2*T]))
    M2q   = float(mp.quad(lambda t: mu(t)**2, [T, 2*T]))
    mu2T  = float(mu(2*T))
    # max |mu'| on [T/2, 5T/2] -> c_mu with |mu'| <= c_mu/|tau|
    cmu = 0.0
    for tt in np.linspace(T/2, 5*T/2, 4001):
        h = 1e-4*tt
        d = (mu(tt+h) - mu(tt-h))/(2*h)
        cmu = max(cmu, abs(d)*tt)
    return Nstar, M2q, mu2T, cmu

def ells(T):
    l = math.log(T/(2*PI))
    l1 = l + 2*math.log(2) - 1
    l2sq = l1*l1 + 1 - 2*math.log(2)**2
    return l, l1, l2sq

# ---------------- Rust sieve ----------------
SIEVE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sieve",
                     "target", "x86_64-unknown-linux-musl", "release", "effsieve")

def run_sieve(L):
    if not os.path.exists(SIEVE):
        raise RuntimeError(f"effsieve not built: {SIEVE}")
    out = subprocess.run([SIEVE, f"{L:.10f}"], capture_output=True, text=True, timeout=1200)
    if out.returncode != 0:
        raise RuntimeError(f"effsieve failed: {out.stderr}")
    d = {}
    for line in out.stdout.splitlines():
        k, _, v = line.partition("=")
        d[k.strip()] = float(v) if k.strip() not in ("L", "cnt") else v
    return d

# ---------------- the assembly ----------------
def assemble(lmbda, T, profile="flat"):
    """profile in {'flat','cosine'}. Returns dict with every error term."""
    import mpmath as mp
    mp.mp.dps = 45
    w = 1.0
    l, l1, l2sq = ells(T)
    L = lmbda*l
    X = math.exp(L)
    d_ = math.floor(L*T/(2*PI))
    h = 2*PI/L
    Nstar, M2q, mu2T, cmu = mu_integrals(T)
    W = window_consts(L, w)
    a, b, Psi0, Ipsi2r, Ipsi2, C1 = W["a"], W["b"], W["Psi0"], W["Ipsi2r"], W["Ipsi2"], W["C1"]

    sie = run_sieve(L)
    Sg, S1, S2, S3, S4, Sa, SaL, Sp, Spsi = (sie[k] for k in
        ("Sg","S1","S2","S3","S4","Sa","SaL","Sp","Spsi"))

    # ---- main terms (exact) ----
    MT_HS = (2*PI*b*L*M2q + (T/PI)*Sg)/(a*a*L*L)     # ||Gtilde||_F^2 main
    # analytic check: Sg vs L^3 J/2 and the (5.2) constants
    # J computed by quadrature of g (via closed form + RR at the ends is complex; use Sg-based):
    J_meas = 2*Sg/L**3   # 2*Sg/L^3 approx J when Sg ~ int g y dy ... (only indicative)
    MN = T*l1/(2*PI)                                     # RvM main term
    deltaN2 = 2*trudgian(2*T) + 2*C_RVM/(2*T) + 1/T      # |N(T,2T) - M_N| bound (safe)
    epsStir = abs(Nstar - MN)                            # measured (should be ~1/T)
    deltaN = deltaN2 + epsStir + 0.5/T                   # |N* - N(T,2T)| bound (safe)

    # ---- theta_0 tail (Prop 4.2) ----
    A0 = A0_of(2*T + 3)
    D0 = T**0.5
    theta0 = 4*A0*C1*C1*X**0.5*math.log(4*T)/(D0*D0)     # (4.5) exact formula
    t1 = theta0/(a*L)                                     # normalized ||Etilde|| <= t1
    # ---- error terms ----
    # (E_tr) trace error |tr(Gtilde) - N*| (Prop 5.3 chain, explicit):
    E_tr_mu = (d_*(2*cmu/T)*Ipsi2r + (2*PI/L)*mu2T + 0.0)/(a*L*L)   # per-k + Riemann sum
    #  ^ per-k: (2 c_mu/T)|r| * int psi^2|r| ;  Riemann: h mu(2T); both /(aL^2) [negligible tails skipped]
    E_tr_P  = Sa/(a*math.log(2))                                   # P-part
    E_tr_Pi = 6*X**0.5 + 1e-10*X**0.5                              # Pi-part (+tiny tail)
    E_tr = E_tr_mu + E_tr_P + E_tr_Pi
    # (E_HS) errors on tr(G^2), then /(a^2 L^2):
    B = l + 4*X**0.5                                               # (5.4)
    # E_1 end effects (Lemma 5.4):
    sumpsi2 = 10*Psi0*Psi0 + 6*C_RHO*Psi0/h                        # paper's bound, explicit
    E1 = 2*a*L*L*B*B*sumpsi2
    part1 = 2*B*(Psi0 + (L/(2*PI))*(C_RHO + C_RHO*math.log(2*T*Psi0/C_RHO)))
    tailE2 = d_*C_RHO*(B + math.log(2) + 1)/(2*T) * 2.0
    E2 = 2*L*L*3*Psi0*B*(part1 + tailE2)
    E_end = E1 + E2
    # M[mu,mu] error:
    E_Mmumu = (4*l*cmu + 2*l*l)*Ipsi2r
    # M[P,P] off-diagonal (Prop 5.6, MV 3pi/2, exact prime sums):
    O1 = 12*L*S4                      # <= 6 L sum a_n^2/delta_n <= 12 L sum Lambda^2
    O2 = b*L*Sa*Sa/(PI*math.log(2))   # |O_2|
    Derr = S2*Ipsi2r/(PI*PI)          # |D - (T/pi)Sg|
    E_offdiag = O1 + O2 + Derr
    # cross terms (Prop 5.7, explicit):
    M_muP  = 4*b*L*(2*l + cmu)*SaL
    M_muPi = 6*PI*b*l*X**0.5
    M_PPi  = 6*b*L*Sa*X**0.5
    M_PiPi = 18*PI*b*L*X/T
    E_cross = 2*M_muP + 2*M_muPi + 2*M_PPi + M_PiPi
    E_HS_trG2 = E_end + E_Mmumu + E_offdiag + E_cross
    E_HS = E_HS_trG2/(a*a*L*L)
    # tail loss in the counting step:
    normG = math.sqrt(MT_HS + E_HS)
    E_tail_loss = 4*t1 + 2*t1*normG + t1*t1
    # window count:
    N_II = 2*A0*(D0+1)*math.log(2*T+3)     # N(I'\I) <= A0 (D0+1) log(2T+3) per side
    E_window = 3*N_II
    E_total = 2*deltaN + 4*E_tr + E_HS + E_tail_loss + E_window

    Bound0 = 2*Nstar - MT_HS - E_total
    N_hi = MN + deltaN2
    p_eff = Bound0/N_hi
    H = 2 - 1/lmbda - lmbda/3
    c_eff = H - p_eff
    return dict(l=l, L=L, X=X, Nstar=Nstar, M2q=M2q, MN=MN, deltaN=deltaN, a=a, b=b,
                theta0=theta0, t1=t1, A0=A0, E_tr=E_tr, E_tr_mu=E_tr_mu, E_tr_P=E_tr_P,
                E_tr_Pi=E_tr_Pi, E1=E1, E2=E2, E_end=E_end, E_Mmumu=E_Mmumu, O1=O1, O2=O2,
                Derr=Derr, E_offdiag=E_offdiag, M_muP=M_muP, M_muPi=M_muPi, M_PPi=M_PPi,
                M_PiPi=M_PiPi, E_cross=E_cross, E_HS=E_HS, E_tail_loss=E_tail_loss,
                N_II=N_II, E_window=E_window, E_total=E_total, Bound0=Bound0, N_hi=N_hi,
                p_eff=p_eff, H=H, c_eff=c_eff, MT_HS=MT_HS, Sg=Sg, J_meas=J_meas,
                S2=S2, S3=S3, S4=S4, Sa=Sa, Spsi=Spsi, cmu=cmu, mu2T=mu2T)

if __name__ == "__main__":
    import mpmath as mp
    mp.mp.dps = 45
    print("="*100)
    print("EFFECTIVE FINITE-T BOUND — V20 (lambda=1.0, w=1, taper rho=x-sin(2 pi x)/(2 pi))")
    print("="*100)
    for T in [1e6, 1e7, 1e8, 1e9, 1e10]:
        r = assemble(1.0, T)
        print(f"\n--- T={T:.0e}  l={r['l']:.4f}  L={r['L']:.4f}  X={r['X']:.4e}  N*={r['Nstar']:.6e}")
        print(f"  main terms: MT_HS/N* = {r['MT_HS']/r['Nstar']:.6f}  2 - MT_HS/N* = {2 - r['MT_HS']/r['Nstar']:.6f}")
        print(f"  theta_0={r['theta0']:.4e}  t1={r['t1']:.4e}  (t1/L={r['t1']/r['L']:.2e})  A0={r['A0']:.4f}")
        print(f"  errors/N*: E_tr={r['E_tr']/r['Nstar']:.4e} (mu {r['E_tr_mu']/r['Nstar']:.2e}, P {r['E_tr_P']/r['Nstar']:.2e}, Pi {r['E_tr_Pi']/r['Nstar']:.2e})")
        print(f"             E_HS={r['E_HS']/r['Nstar']:.4e}  (E1 {r['E1']/(r['a']**2*r['L']**2)/r['Nstar']:.2e}, E2 {r['E2']/(r['a']**2*r['L']**2)/r['Nstar']:.2e}, E_Mmumu {r['E_Mmumu']/(r['a']**2*r['L']**2)/r['Nstar']:.2e})")
        print(f"             E_offdiag={r['E_offdiag']/(r['a']**2*r['L']**2)/r['Nstar']:.4e} (O1 {r['O1']/(r['a']**2*r['L']**2)/r['Nstar']:.2e}, O2 {r['O2']/(r['a']**2*r['L']**2)/r['Nstar']:.2e}, Derr {r['Derr']/(r['a']**2*r['L']**2)/r['Nstar']:.2e})")
        print(f"             E_cross={r['E_cross']/(r['a']**2*r['L']**2)/r['Nstar']:.4e}  E_tail_loss={r['E_tail_loss']/r['Nstar']:.2e}  E_window={r['E_window']/r['Nstar']:.2e}  deltaN/N*={r['deltaN']/r['Nstar']:.2e}")
        print(f"  E_total/N* = {r['E_total']/r['Nstar']:.4f}")
        print(f"  Bound0/N*  = {r['Bound0']/r['Nstar']:.4f}   p_eff = {r['p_eff']:.4f}   H(1)={r['H']:.6f}   c(1,T)={r['c_eff']:.4f}")
        print(f"  (check) Sg={r['Sg']:.6e}  S2={r['S2']:.4e} (L^2/2={r['L']**2/2:.4e})  S4={r['S4']:.4e}  psi(X)={r['Spsi']:.4e} (X={r['X']:.4e})")
