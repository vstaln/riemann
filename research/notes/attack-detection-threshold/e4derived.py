# Derived quantities for attack-detection-threshold.md — all arithmetic from the
# e4 sweep tables (e4sweep-run1.txt, e4probe-run1.txt, pairdiag-run1.txt).
import math

# --- real-data noise band (e4sweep-run1.txt section A, bound_rank/N) ---
real = {100:0.719228,200:0.716530,300:0.713534,400:0.711225,500:0.711945,600:0.709068,700:0.711259,900:0.707393,1100:0.707096,1300:0.704966}
vals = list(real.values())
band_min, band_max = min(vals), max(vals)
print(f"band_min={band_min:.6f} band_max={band_max:.6f} width={band_max-band_min:.6f}")
s1 = {100:0.703914,200:0.694241,300:0.702511,400:0.702828,500:0.704598,600:0.705395,700:0.706294,900:0.705412,1100:0.705352,1300:0.704010}
print(f"band_s1: [{min(s1.values()):.6f}, {max(s1.values()):.6f}]")

# --- per-pair certificate cost (bound_rank/N drop per pair) ---
# top-clustered T=300 beta=0.05, f=0.5% (1 pair, N=203): 0.713534 -> 0.711361
# scattered T=300 beta=0.05, f=0.5% (1 pair, N=203): 0.713534 -> 0.683531
N300 = 203
for name, (v0, v1) in [("top-clustered", (0.713534,0.711361)), ("scattered", (0.713534,0.683531))]:
    drop = v0 - v1
    print(f"{name} single pair (T=300,N=203): Delta bound_rank/N = {drop:.6f}, per-pair numerator cost = {drop*N300:.2f}")

# --- slack of the real value to band_min at each T ---
for t in (200,300,500):
    slack = real[t] - band_min
    print(f"T={t}: real {real[t]:.6f}, slack to band_min = {slack:.6f}")

# --- f_actual for 1 pair, N/T, imb=beta*N/T, 1/log T ---
for t,N in ((200,123),(300,203),(500,380)):
    print(f"T={t}: N={N} f(1 pair)={1/N:.4f} N/T={N/t:.4f} imb(beta=0.3)={0.3*N/t:.4f} imb(beta=0.05)={0.05*N/t:.4f} 1/logT={1/math.log(t):.4f}")

# --- how many single-scattered-pair drops fit in the band width / slack ---
drop_s = 0.713534-0.683531  # scattered single pair drop at T=300 beta=0.05
print(f"scattered single-pair drop {drop_s:.4f} vs band width {band_max-band_min:.4f}: ratio {drop_s/(band_max-band_min):.2f}x; vs T=300 slack {0.713534-band_min:.4f}: ratio {drop_s/(0.713534-band_min):.2f}x")

# --- n_- threshold: single pair lambda_min(full W) vs beta, from pairdiag ---
# bottom: beta=0.02 -> -1.435e-4 ; bulk: beta=0.1 -> -1.687e-8, beta=0.05 -> -6.492e-11; top: beta=0.5 -> -1.534e-7, beta=0.3 -> -9.55e-13
for name, (b, lm) in [("bottom",(0.02,-1.435e-4)),("bulk",(0.1,-1.687e-8)),("bulk050",(0.05,-6.492e-11)),("top",(0.5,-1.534e-7)),("top030",(0.3,-9.55e-13))]:
    print(f"pairdiag {name} beta={b}: full-W lambda_min={lm:.3e}")

# --- isolated-pair eigenvalues (finitet §7 anchor reproduction) ---
print("isolated pair beta=0.3 bottom: {-0.151694,+1.817579} raw, W units {-0.1786,+2.1403} (pairdiag / finitet §7)")
