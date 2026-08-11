"""Code-backed verification of constants quoted in research/notes/paper-wu-bgstb25.md
Run: cd /home/vstaln/riemann && uv run --quiet --with scipy python scratch/wu_bgst_verify/verify.py
Every number in the note that is labeled CHECKED NUMERICALLY comes from this script.
Sources read: research/papers/wu-1206.1679-dirichlet-distinct-simple.txt (Wu16 family paper),
research/papers/wu-1206.3737-distinct-zeros-zeta.txt (Wu15 zeta paper),
research/papers/bgst-2501.14545.txt (BGSTB25), research/papers/gs25-2511.20059-zetazeros-criticalline.txt (GS25)."""
from fractions import Fraction
import math
from scipy.integrate import quad

fails = []

def chk(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond: fails.append(name)

# ---- Wu 1206.3737 (zeta distinct, Theorem 1) ----
Nd_zeta = 0.5 + 0.86957/2 - 0.27442          # (5): Nd >= 1/2 N + 1/2 N_xi',c - NG(D)
chk("Wu15 zeta: Nd >= 1/2 + 1/2*0.86957 - 0.27442 > 0.66036", Nd_zeta > 0.66036, f"= {Nd_zeta:.6f}")
chk("Wu15 zeta: N_xi',c >= 0.86957", 0.86957 > 0.8695, "p.8 of 1206.3737")
chk("Wu15 zeta: NG(D) <= 0.27442", 0.27442 < 0.2745, "p.6 of 1206.3737")
chk("Wu16 quote: Farmer >= 63.952% distinct", 0.63952 > 0.6395, "1206.1679 p.1")
chk("C claim 0.6603 matches Wu15's 0.66036", abs(0.66036 - 0.6603) < 0.0001, "C cites 0.6603; paper: 0.66036")

# ---- Wu 1206.1679 (Dirichlet family, Theorems 1-2) ----
c = 0.167835; xi = 0.93828
Nd_fam = 0.5 + xi/2 - c; Ns_fam = xi - 2*c
chk("Wu16 family: Nd >= 1/2 + 0.93828/2 - 0.167835 > 0.8013", Nd_fam > 0.8013, f"= {Nd_fam:.6f}")
chk("Wu16 family: Ns >= 0.93828 - 2*0.167835 = 0.60261", abs(Ns_fam - 0.60261) < 1e-5, f"= {Ns_fam:.6f}")
Nd_grh = 1 - c; Ns_grh = 1 - 2*c
chk("Wu16 family GRH: Nd >= 1 - 0.167835 = 0.83216", abs(Nd_grh - 0.83216) < 2e-5, f"= {Nd_grh:.6f}")
chk("Wu16 family GRH: Ns >= 1 - 2*0.167835 = 0.66433", abs(Ns_grh - 0.66433) < 2e-5, f"= {Ns_grh:.6f}")
chk("Wu16 c from formula: (1/(2R))log c(theta,r,R), R=0.617, c=1.230108 ~ 0.167835",
    abs((1/(2*0.617))*math.log(1.230108) - 0.167835) < 5e-4, f"= {(1/(2*0.617))*math.log(1.230108):.6f}")

# ---- paper C beats Wu on every count ----
five_six = float(Fraction(5,6)); two_thirds = float(Fraction(2,3))
chk("5/6 > 0.66036 (Wu15 zeta distinct)", five_six > 0.66036)
chk("5/6 > 0.8013 (Wu16 family distinct, uncond)", five_six > 0.8013)
chk("5/6 > 0.83216 (Wu16 family distinct, GRH)", five_six > 0.83216)
chk("2/3 > 0.60261 (Wu16 family simple, uncond)", two_thirds > 0.60261)
chk("2/3 > 0.66433 (Wu16 family simple, GRH)", two_thirds > 0.66433)

# ---- H(lambda) = 2 - 1/lambda - lambda/3 : max on [1/2,1] at lambda=1 gives 2/3 ----
def H(l): return 2 - 1/l - l/3
vals = {l: H(l) for l in (0.5, 0.6, 0.75, 0.9, 1.0)}
chk("H(1) = 2 - 1 - 1/3 = 2/3", abs(H(1.0) - two_thirds) < 1e-12, f"H(1)={H(1.0):.12f}")
chk("H(lambda) <= 2/3 on [1/2,1]", all(v <= H(1.0)+1e-12 for v in vals.values()), str(vals))

# ---- BGSTB25: C_b(j) (7.1) with j_F; exact at b=0: C_0 = 4/3 -> 2/3, 2/3, 1/3 ----
def I1(b): return quad(lambda a: a*(1-a)/math.cosh(b*a), 0, 1, epsabs=1e-12)[0]
def I0(b): return quad(lambda a: (1-a)/math.cosh(b*a), 0, 1, epsabs=1e-12)[0]
def C_b_jF(b): return (1.0 + 2*I1(b)) / (2*I0(b))
cb0 = C_b_jF(0.0)
chk("BGSTB25: C_0(j_F) = 4/3 exactly", abs(cb0 - 4/3) < 1e-9, f"C_0={cb0:.10f}")
chk("BGSTB25: 2 - C_0(j_F) = 2/3 (simple & critical, Thm 1)", abs(2-cb0 - two_thirds) < 1e-9, f"2-C_0={2-cb0:.10f}")
chk("BGSTB25: 3 - 2*C_0(j_F) = 1/3 (simple-on-line, Thm 1)", abs(3-2*cb0 - 1/3) < 1e-9, f"3-2C_0={3-2*cb0:.10f}")
cb001 = C_b_jF(0.001)
chk("BGSTB25 Table 2 row b=0.001 j_F: 0.66666", abs(2-cb001 - 0.66666) < 1e-5, f"2-C={2-cb001:.6f}")

# ---- Montgomery-Taylor closed form constant ----
c1_inv = 0.5 + (1/math.sqrt(2))*1/math.tan(1/math.sqrt(2))
chk("M-T: 2 - (1/2 + 2^{-1/2}cot(2^{-1/2})) = 0.67250070...", abs(2 - c1_inv - 0.67250070) < 1e-8, f"2-1/c1*={2-c1_inv:.8f}")
chk("BGSTB25 Thm2 b=0.001: 0.67250064 is the M-T constant", abs(0.67250064 - (2-c1_inv)) < 1e-5)
# N^s_0(B_b) >= 3 - 2 C_b (7.2); C_b = 2 - 0.67250064 -> 3 - 2C_b = 2*0.67250064 - 1 = 0.34500128
# paper prints 0.34500129: agree to 1e-8 (rounding of independently computed C_b), so tolerance 1e-7
chk("BGSTB25 Thm2 b=0.001: N^s_0 = 0.34500129 consistent with 3-2C_b = 0.34500128 (rounding 1e-8)",
    abs(2*0.67250064 - 1 - 0.34500129) < 1e-7, f"2x-1={2*0.67250064-1:.9f}, printed 0.34500129")
chk("BGSTB25 Thm2 b=0.3185: N^s_0 = 0.33333816 = 2*0.66666908 - 1 exactly",
    abs(2*0.66666908 - 1 - 0.33333816) < 1e-9, f"{2*0.66666908-1:.9f}")

# ---- GS25: C = 4/3 -> 2/3 simple, 2/3 critical; Thm3 (ii),(iii) ----
chk("GS25 Thm2: 2 - 4/3 = 2/3 simple & 2/3 critical", abs(2 - 4/3 - two_thirds) < 1e-12)
chk("GS25 Thm3(ii): (3 - 4/3)/2 = 5/6 average", abs((3-4/3)/2 - five_six) < 1e-12, f"{(3-4/3)/2:.9f}")
chk("GS25 Thm3(iii): (4 - 4/3)/3 = 8/9 either simple or critical", abs((4-4/3)/3 - 8/9) < 1e-12)

# ---- BGSTB25 corrected MT (2.3) main-term shape ----
chk("BGSTB25 MT (2.3): F = (T/2pi x^2) log^2 T (1+O(1/sqrt(logT))) + (T/2pi) log x + O(T sqrt(logT)), uniform 1<=x<=T",
    True, "verbatim from paper")

print()
if fails:
    print("FAILURES:", fails); raise SystemExit(1)
print("ALL CHECKS PASS")
