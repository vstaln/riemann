#!/usr/bin/env python3
"""attack_sweep.py -- certified-bound sweep over (alpha, psum, m) using CERTIFIED eps values
from the discovery/logs. CHECKED NUMERICALLY (mpmath 60 dps).
Certified eps used (grid=4000 verifier):
  psum=1/220 (p=1/1320): max certified eps = 0.008064 (prior run certified 0.008064, log);
                         record used 0.00806. Use 0.008064 as certified upper (8064/1e6 True).
  psum=1/225 (p=1/1350): max certified eps = 0.007909 (7909/1e6 True).
Note: sweep below is a *bound* computation at these certified eps — NOT new verifications.
Only claims about bound arithmetic here; verifier cert status from logs."""
import mpmath as mp
mp.mp.dps = 60

def H_cosine(alpha):
    I0 = 2*mp.sin(alpha/2)/alpha
    I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
    constant = mp.sin(alpha/2)/alpha + 2*mp.cos(alpha/2)/alpha**2
    J = -2*I2/alpha**2 + constant*I0
    c = I0**2/(I2+J)
    return 2 - 1/c

def Phi(E, m):
    E, m = mp.mpf(E), mp.mpf(m)
    thr = m/(m-1)
    return E if E <= thr else 2*mp.sqrt((m-1)*E/m) - 1 + E/m

def bound_from_eps(alpha, eps, m, psum):
    H = H_cosine(alpha)
    A = eps*(m-6); B = Phi(A, m); tau = psum*(m-6)/m
    return (H-tau)/(1-B/m)

record = mp.mpf("0.673262865534356014645368000853343519319712248")
print(f"record = {mp.nstr(record, 42)}")
# certified eps by psum (from exec-eps-max-runs.log / prior run)
cert = {220: mp.mpf(8064)/10**6, 225: mp.mpf(7909)/10**6}
best = (record, None)
for psum_inv, eps in cert.items():
    psum = mp.mpf(1)/psum_inv
    for m in range(130, 141):
        for ai in range(145, 154):
            alpha = mp.mpf(ai)/100
            b = bound_from_eps(alpha, eps, m, psum)
            if b > best[0]:
                best = (b, (ai, psum_inv, m, eps))
print("max certified bound over psum in {1/220,1/225}, m in 130..140, alpha in 1.45..1.53:")
print(f"  {mp.nstr(best[0], 45)}  at (alpha={best[1][0]/100}, psum=1/{best[1][1]}, m={best[1][2]}, eps={mp.nstr(best[1][3],12)})")
print(f"  beats record: {best[0] > record}")
# print the grid near the top for context
print("--- top rows (bound, alpha, psum_inv, m) ---")
rows = []
for psum_inv, eps in cert.items():
    psum = mp.mpf(1)/psum_inv
    for m in range(130, 141):
        for ai in range(145, 154):
            alpha = mp.mpf(ai)/100
            rows.append((bound_from_eps(alpha, eps, m, psum), ai, psum_inv, m))
rows.sort(reverse=True)
for b, ai, pi, m in rows[:8]:
    print(f"  {mp.nstr(b, 40)} alpha={ai/100} psum=1/{pi} m={m}")
