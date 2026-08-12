"""FINAL LEADER: exact high-precision certified bound.
alpha = 149/100, p = 1/1320 (psum = 6/1320 = 1/220), certified eps = 8060/10^6.
"""
import mpmath as mp
mp.mp.dps = 120
alpha = mp.mpf(149)/100
# Window functional H
I0 = 2*mp.sin(alpha/2)/alpha
I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
constant = mp.sin(alpha/2)/alpha + 2*mp.cos(alpha/2)/alpha**2
J = -2*I2/alpha**2 + constant*I0
c = I0**2/(I2+J)
H = 2 - 1/c
eps = mp.mpf(8060)/10**6
psum = mp.mpf(1)/220
m = 133
A = eps*(m-6)
thr = mp.mpf(m)/(m-1)
B = A if A <= thr else 2*mp.sqrt((m-1)*A/m) - 1 + A/m
tau = psum*(m-6)/m
bound = (H - tau)/(1 - B/m)
print(f"alpha = {mp.nstr(alpha, 25)}")
print(f"H     = {mp.nstr(H, 35)}")
print(f"eps   = {mp.nstr(eps, 25)}")
print(f"m     = {m}")
print(f"A     = {mp.nstr(A, 30)}")
print(f"thr   = {mp.nstr(thr, 30)}")
print(f"B     = {mp.nstr(B, 35)}")
print(f"tau   = {mp.nstr(tau, 30)}")
print(f"bound = {mp.nstr(bound, 45)}")
print(f"percent = {mp.nstr(100*bound, 30)}")
record = mp.mpf("0.6731929114731422535099843283")
print(f"record = {mp.nstr(record, 30)}")
print(f"GAIN  = {mp.nstr(bound - record, 25)}")
# trmdy comparison
trmdy = mp.mpf("0.67313763069934451465")
print(f"trmdy = {mp.nstr(trmdy, 30)}")
print(f"gain over trmdy = {mp.nstr(bound - trmdy, 25)}")
