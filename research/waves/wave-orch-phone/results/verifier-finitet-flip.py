#!/usr/bin/env python3
"""VERIFIER-FINITET: adversarial analysis of the 0.6732628655 certificate's finite-T robustness.

Mini-orchestration role: VERIFIER (can dropped finite-T terms flip the certified constant?).
Environment: proot Ubuntu (mpmath 1.4.1). Modest compute, high precision.

Certificate (from discovery-6732629.md):
  bound = (H - tau)/(1 - B/m)
    H     = H(alpha=1.49) = 0.6724218860964        (window value, verified to 1.7e-41)
    tau   = psum*(m-6)/m,  psum = 1/220,  m = 133
    B     = Phi_m(eps*(m-6)),  Phi_m(x) = 2*sqrt((m-1)*x/m) - 1 + x/m
    eps   from certified floor F >= 0.00806
  certified: 0.673262865534356014645368000853343519319712248

We compute: (1) the exact arithmetic; (2) the margins against the previous records and against
Theorem D; (3) the flip thresholds: what size of error in each ingredient would drop bound below
each competitor; (4) sign/size comparison with the measured finite-T error terms (executor probe:
Delta = +0.025..+0.066, safe direction).
"""

from mpmath import mp, mpf, sqrt

mp.dps = 80

# --- certificate arithmetic ---
H = mpf("0.6724218860964")
psum = mpf(1) / mpf(220)
m = 133
eps = mpf("0.00806")
rec = mpf("0.673262865534356014645368000853343519319712248")

tau = psum * (m - 6) / m
x = eps * (m - 6)
B = 2 * sqrt((m - 1) * x / m) - 1 + x / m
bound = (H - tau) / (1 - B / m)

print("=== certificate arithmetic (mpmath 80 digits) ===")
print(f"H     = {H}")
print(f"tau   = {tau}")
print(f"B     = {B}")
print(f"B/m   = {B/m}")
print(f"bound = {bound}")
print(f"rec   = {rec}")
print(f"match rec? {abs(bound - rec) < mpf('1e-30')}   diff = {abs(bound-rec)}")
print(f"margin vs previous external record tawanerguo 0.6731929114731422 : {bound - mpf('0.6731929114731422'):.3e}")
print(f"margin vs Theorem D 0.672500703679412                          : {bound - mpf('0.672500703679412'):.3e}")
print(f"margin above own H (i.e. above pre-block functional H):          {bound - H:.3e}")

# --- flip thresholds ---
# bound = (H - tau)/(1 - B/m);  d(bound)/dH = 1/(1-B/m);  d(bound)/d(B/m) = bound/(1-B/m)
den = 1 - B / m
print("\n=== sensitivity (flip thresholds) ===")
print(f"1/(1-B/m) = {1/den}   (d(bound)/dH)")
print(f"bound/(1-B/m) = {bound/den}   (d(bound)/d(B/m))")
dH_rec = rec - H   # if tau and B/m were zero, this is how far H is above the record
print(f"H above rec (with tau,B/m=0): {dH_rec:+.6f} -> H alone is BELOW record; block terms carry the record")

# What delta(H) would drop bound to each competitor?
for name, target in [("tawanerguo 0.6731929", mpf("0.6731929114731422")),
                     ("Theorem D 0.6725007", mpf("0.672500703679412")),
                     ("3/2-1/sqrt2*cot = 0.6725007 (sqrt2 window)", mpf("0.6725007036794116"))]:
    dH_needed = (target * den + tau) - H
    dBm_needed = (H - tau) / target - 1 + 1  # solve (H-tau)/(1-y)=target -> y = 1-(H-tau)/target
    y = 1 - (H - tau) / target
    print(f"  to fall to {name}: need dH <= {dH_needed:+.6f}  OR  B/m >= {y:.6f} (current {B/m:.6f})")

# --- compare with measured finite-T error terms ---
print("\n=== measured finite-T gap vs flip thresholds (executor probe, CHECKED NUMERICALLY) ===")
print("idealized window bound/N at T=200..5000 (a=1.49):")
for T, D in [(200, 0.066291), (400, 0.054901), (800, 0.051554), (1600, 0.046010),
             (3200, 0.043217), (5000, 0.040277)]:
    print(f"  T={T:5d}  Delta=+{D:.6f} (overshoot, SAFE direction)")

# --- the honest structural point: what would it take to refute the liminf? ---
print("\n=== structural verdict inputs ===")
print("1. bound=(H-tau)/(1-B/m) is T-FREE: every ingredient is an exact rational (tau),")
print("   a certified constant (eps -> B), or a verified window value (H). NO T-dependent")
print("   term appears in the formula itself.")
print("2. The dropped terms are the T->infinity derivation errors (Claim 2.1/3.2/3.3).")
print("   For the idealized kernel these are measured POSITIVE (overshoot) at every T<=5000,")
print("   magnitude 0.025..0.066 -- far above the record margin 6.995e-5, in the SAFE direction.")
print("3. To flip the record below tawanerguo, dropped terms would need magnitude >= 6.995e-5")
print("   with NEGATIVE sign at T->infinity. No evidence of negative sign anywhere in the data.")
print("4. Caveats (honest): probes use the idealized functional, not the block-refined one;")
print("   T<=5000 only; asymptote of Delta is INCONCLUSIVE (fits give 1/log2T intercept +0.01..+0.03,")
print("   1/logT intercept -0.016..0). Sign is robust at all measured T, level is not.")

# --- hard-cutoff vs C-infinity for the window constant ---
print("\n=== hard-cutoff vs C-infinity: window constant (attack-kernel.md PROVEN) ===")
print("cosine = global minimizer of Q(v) over all L^2 windows on [-1/2,1/2] (Lean-formalized).")
print("Every C-infinity-smoothed variant has Q(v) > Q(cos): 1.415 (eps=0.1), 2.20 (eps=0.5),")
print("3.86 (eps=T/N) -- from attack-finitet-cinf.md, CHECKED NUMERICALLY.")
print("=> a hard-cutoff kernel does NOT beat the cosine at the window level; the P6 question is")
print("   whether a different kernel+block combo improves the BLOCK functional, which is unprobed.")

print("\nRESULT: CONJECTURED -- certificate is robust to finite-T: formula is T-free, dropped terms")
print("measured safe-direction at all T<=5000, flip needs >=6.995e-5 negative error at T->infinity,")
print("no evidence of one; asymptote level INCONCLUSIVE, refined-functional probe outstanding.")
