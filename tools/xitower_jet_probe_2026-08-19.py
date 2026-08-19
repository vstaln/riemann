#!/usr/bin/env python3
"""Grounding probe for xitower-jet-impossibility-2026-08-19.md (v2, fixed derivative calls).
Checks:
  1. xi(1/2+it) real, xi'(1/2+it) pure imaginary (FE-forced).
  2. Re(zeta'/zeta)(1/2+it) == gamma-only (invariant to off-line zeros).
  3. At zeros: xi(rho)=0, xi'(rho)!=0 (simple). Cauchy effective counts on first N zeros.
  4. H0 baseline.
"""
import mpmath as mp
mp.mp.dps = 30

def xi(s):
    return mp.mpf('0.5')*s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)

print("=== 1. FE-forced purity: xi(1/2+it) real, xi'(1/2+it) pure imaginary ===")
for t in ['17.5', '30.7', '100.3']:
    s = mp.mpc('0.5', t)
    v = xi(s)
    print(f"t={t}: xi real={mp.nstr(v.real,5)}, imag={mp.nstr(v.imag,5)} (imag ~ noise)")
    h = mp.mpf('1e-6')
    d = (xi(s+1j*h) - xi(s-1j*h))/(2j*h)
    print(f"   xi' real={mp.nstr(d.real,5)}, imag={mp.nstr(d.imag,5)} (pure imaginary: real ~ noise)")

print("\n=== 2. Re(zeta'/zeta)(1/2+it) == gamma-only invariant ===")
def gamma_only_Re(t):
    # invariant: Re(zeta'/zeta)(1/2+it) = log(pi)/2 - Re psi(1/4+it/2)/2  (FE-forced)
    return mp.log(mp.pi)/2 - mp.psi(0, mp.mpc('0.25', t/2)).real/2
for t in ['17.5', '30.7', '100.3']:
    s = mp.mpc('0.5', t)
    true_Re = (mp.zeta(s, derivative=1)/mp.zeta(s)).real
    g = gamma_only_Re(mp.mpf(t))
    print(f"t={t}: true Re(z'/z) = {mp.nstr(true_Re,8)}, gamma-only = {mp.nstr(g,8)}, diff = {mp.nstr(true_Re-g,8)}")

print("\n=== 3. At zeros: xi(rho)=0, xi'(rho)!=0; Cauchy effective counts (first N zeros) ===")
N = 200
Gz = mp.mpf(0); Hz = mp.mpf(0); Gx = mp.mpf(0); Hx = mp.mpf(0)
topGx = mp.mpf(0); gmax = mp.mpf(0)
wvals = []
for k in range(1, N+1):
    rho = mp.zetazero(k)
    gam = rho.imag
    zd = mp.zeta(rho, derivative=1)      # zeta'(rho)
    az = abs(zd)
    w = 1/(az*az)
    Gz += w; Hz += 1/(az**4); wvals.append(w)
    xi_rho = xi(rho)
    if k == 1:
        print(f"  rho_1: |xi(rho)| = {mp.nstr(abs(xi_rho),4)} (should be ~0), |xi'(rho)| = {mp.nstr(abs(xi(rho+1j*mp.mpf('1e-6')) - xi(rho-1j*mp.mpf('1e-6')))/(2*mp.mpf('1e-6')), 4)} (should be >0)")
    # Stirling form (PROVEN in audit): |xi'(rho)| = (pi/2)^(1/4) g^(7/4) e^(-pi g/4) |zeta'(rho)|
    xi_mag = mp.power(mp.pi/2, mp.mpf('0.25')) * mp.power(gam, mp.mpf('1.75')) * mp.exp(-mp.pi*gam/4) * az
    wx = 1/(xi_mag*xi_mag)
    Gx += wx; Hx += 1/(xi_mag**4)
    if wx > topGx: topGx = wx
    if gam > gmax: gmax = gam

effz = Gz*Gz/Hz
effx = Gx*Gx/Hx
print(f"N = {N} (g_max = {mp.nstr(gmax,6)}):")
print(f"  G_zeta = {mp.nstr(Gz,6)}, H_zeta = {mp.nstr(Hz,6)}")
print(f"  eff_zeta = G^2/H = {mp.nstr(effz,6)} -> fraction of N: {mp.nstr(effz/N,5)}")
print(f"  G_xi = {mp.nstr(Gx,6)}, H_xi = {mp.nstr(Hx,6)}")
print(f"  eff_xi = G_xi^2/H_xi = {mp.nstr(effx,6)} (O(1) per Kill 1)")
print(f"  top-zero share of G_xi = {mp.nstr(topGx/Gx,6)} (exponential concentration)")
G2 = sum(wvals[:100]); H2 = sum(w**2 for w in wvals[:100])
print(f"  eff_zeta on first 100 zeros: {mp.nstr(G2*G2/H2,6)} of 100 -> {mp.nstr((G2*G2/H2)/100,5)}")

print("\n=== 4. H0 baseline ===")
H0 = mp.mpf(3)/2 - mp.cot(1/mp.sqrt(2))/mp.sqrt(2)
print(f"H0 = {mp.nstr(H0,8)}")
