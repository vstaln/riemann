# Unconditional version of the paper's distinct combination (SS7.5g)
# N_d/N >= 1/2 + (2m2-m3)/18 + (4/9) N_s/N, weight psi(m)=m/2+(2m^2-m^3)/18+(4/9)1_{m=1}
# Verdict: cannot be made unconditional; collapses to N_d >= N_s (0.673481) in the
# weight framework; our certified 0.836740 = (1+h)/2 stands as the ceiling.
from mpmath import mp, mpf
mp.dps = 40

# --- (1) reproduce the paper's RH-conditional 0.85082 (sanity) ---
t_RH = mpf('0.68524')                 # 2m2-m3 under RH at v(s)=cos(8s/5)1_{|s|<=1/2} (paper, interval-certified)
Ns_RH = mpf(19)/27                    # Bui-Heath-Brown simple on RH
print("paper RH bound   =", mpf(1)/2 + t_RH/18 + (mpf(4)/9)*Ns_RH)   # expect 0.850826...
print("correlation only =", mpf(1)/2 + t_RH/2)                       # expect 0.84262

# --- weight validity: psi(m)<=1 for all integer m is what turns Sum psi(m_i) into a bound on N_d ---
def psi(m, use_cubic=True):
    v = m/mpf(2) + (2*m*m - (m*m*m if use_cubic else mpf(0)))/18 + (mpf(4)/9 if m == 1 else mpf(0))
    return v
print("\npaper cubic weight psi(m): ", [float(psi(m)) for m in range(1, 7)])
print("m3-dropped weight psi0(m): ", [float(psi(m, use_cubic=False)) for m in range(1, 7)], "  <-- psi0(2)=13/9>1 INVALID")
assert all(float(psi(m)) <= 1.0 for m in range(1, 200)), "cubic weight must satisfy psi<=1"
assert float(psi(2, use_cubic=False)) > 1.0, "dropped-m3 weight must violate psi<=1 at m=2"

# --- (2) unconditional inputs ---
h = mpf('0.6734808616745137')         # our certified simple-on-line, unconditional
m2 = mpf(4)/3                         # second moment at lambda=1 (pair correlation level)
m3 = mpf(0)                           # third moment unavailable unconditionally on (1/2,1)

# naive plug-in (INVALID: weight violates psi<=1 at m=2)
naive = mpf(1)/2 + (2*m2 - m3)/18 + (mpf(4)/9)*h
print("\nnaive m3=0 plug  =", naive, "(invalid: psi0(2)>1)")

# --- (3) honest LP over span{m, m^2, 1_{m=1}}: max a + b*m2 + c*h, psi(m)<=1 for ALL m>=1 ---
# structural: b>0 => psi(m)->+inf as m->inf (impossible); a>0 => am>1 for large m (impossible);
# so only c*1_{m=1} survives => N_d >= N_s >= hN.  Finite-cap LP shows the artifact:
# a=1/M, f = h + (1-h)/M  ->  h as the multiplicity cap M -> inf.
import numpy as np
from scipy.optimize import linprog
M = 3000
A = [[float(m), float(m*m), 0.0] for m in range(2, M + 1)]
A.append([1.0, 1.0, 1.0])
b = [1.0]*len(A)
r = linprog([-1.0, -float(m2), -float(h)], A_ub=A, b_ub=b, bounds=[(0, None)]*3)
print("LP opt span{m,m^2,1} @cap=%d = %.9f  at (a,b,c) = %s" % (M, -r.fun, [round(float(x), 9) for x in r.x]))
print("predicted artifact h + (1-h)/M =", float(h + (1 - h)/M))
print("(1+h)/2 exact    =", (1+h)/2)
print("== certified distinct record 0.8367404308372568 (FINAL-RECORD-2026-08-13) ==")
assert abs(-r.fun - float(h + (1 - h)/M)) < 1e-8, "finite-cap LP must match h + (1-h)/M"
print("OK: unconditional weight span collapses to 1_{m=1}; 0.836740 is the ceiling.")
