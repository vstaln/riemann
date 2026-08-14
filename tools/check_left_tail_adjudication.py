"""Adjudication of validator attack C (left tail): |E| <= 2*S2 is FALSE.
Adjudicator: main loop, 2026-08-14. Resolution recorded in
research/notes/bhb-lefttail-adjudication-2026-08-14.md.

Setup (BHB program definitions):
  S2 := sum_rho F(rho)F(1-rho)          (BHB Lemma 1 evaluates THIS, ~ (T/2pi)L^3 * 57/64)
  E  := sum_rho F(rho)[F(rhobar)-F(1-rho)] = sum_pairs |F(rho)-F(1-rhobar)|^2  (pair identity, >= 0)
  M2 := sum_rho |F(rho)|^2 = S2 + E     (exact algebra; NOT evaluated by Lemma 1)

The validator claimed |E| <= 2*S2 exactly (C-S "with sum|F(1-rho)|^2 = sum|F(rho)|^2 = S2").
The flaw: sum|F(rho)|^2 = M2 = S2 + E, NOT S2. E can exceed 2*S2.

Check 1: single FE-consistent pair, exact arithmetic.
  F real coefficients => F(rhobar) = conj F(rho), F(1-rhobar) = conj F(1-rho).
  Pair (rho, 1-rhobar) with F(rho) = A, F(1-rho) = B real:
    E_pair  = |A - conj(B)|^2 = (A-B)^2
    S2_pair = F(rho)F(1-rho) + F(1-rhobar)F(rhobar) = 2AB
  A=100, B=1: E_pair = 9801, S2_pair = 200 -> ratio 49.005 > 2. |E| <= 2*S2 FALSE.

Check 2: FE-consistent left-heavy model at T = 10^4, 10^5, 10^6 (the M3-note worst case).
  N_pairs = floor(T^0.478) left zeros at beta = 0.22 (FE partners at 0.78; GM-consistent).
  Convexity/FE pointwise bounds: |F(0.22+it)| ~ T^0.39 * L, |F(1-rho)| ~ T^0.11 * L, L = log(T/2pi).
  E = sum_pairs |F(rho)-F(1-rhobar)|^2 ~ N_pairs * T^0.78 * L^2 = T^1.258 * L^2  =>  E/S2 -> inf.
  Consistency with BHB Lemma 1: left pairs' own S2-contribution ~ N_pairs * T^0.5 * L^2
  = T^0.978 L^2 << (T/2pi)L^3 (ratio -> 0): no contradiction with S2 ~ (T/2pi)L^3 * 57/64.
"""
import math

print("Check 1: single FE-consistent pair disproves |E| <= 2*S2 (exact arithmetic)")
A, B = 100.0, 1.0
E_pair = (A - B) ** 2
S2_pair = 2 * A * B
print(f"  A=F(rho)=100, B=F(1-rho)=1:  E_pair={E_pair:.0f}  S2_pair={S2_pair:.0f}  E/S2={E_pair/S2_pair:.3f}  >2 -> |E|<=2*S2 FALSE")

print("\nCheck 2: FE-consistent left-heavy model, E/S2 -> inf at the predicted rate T^0.258/L")
alpha = 0.478        # count exponent N(1/2+Delta,T) ~ T^alpha (GM at sigma = 0.78, Delta = 0.28)
beta = 0.22
expF = 1 - beta      # |F(rho)|^2 ~ T^{1-beta} L^2 (FE + convexity: 2*mu(beta) = 1-beta)
expG = 1 - expF      # |F(1-rho)| ~ T^{beta/2}... |F(1-rho)|^2 ~ T^{2 mu(1-beta)} = T^{beta}
for T in (1e4, 1e5, 1e6):
    L = math.log(T / (2 * math.pi))
    N = int(T ** alpha)
    E = N * T ** expF * L ** 2          # sum_pairs |F(rho)-F(1-rhobar)|^2, left dominates
    S2_left = N * T ** ((expF + expG) / 2) * L ** 2  # sum over left pairs |F(rho)F(1-rho)| ~ T^0.5 L^2
    S2_lemma = (T / (2 * math.pi)) * L ** 3 * 57 / 64
    ratio = E / S2_lemma
    pred = T ** (alpha - (1 - alpha)) / L   # T^{2alpha-1}/L with 2alpha-1 = -0.044? NO: see below
    # predicted E/S2 ~ T^{1-beta+alpha} L^2 / (T L^3) = T^{alpha+beta}/L ... recompute cleanly:
    pred_clean = T ** (alpha + beta - 1 + (1 - beta) - (1 - beta)) * L ** 2 / ((T / (2 * math.pi)) * L ** 3)
    # E/S2_lemma = T^{alpha} T^{1-beta} L^2 / (T L^3) = T^{alpha-beta} / L ... verify:
    pred_final = T ** (alpha - beta) / L
    print(f"  T=10^{int(math.log10(T))}:  N={N}  E/S2_lemma={ratio:.4f}  predicted T^(alpha-beta)/L={pred_final:.4f}  "
          f"left-S2/S2_lemma={S2_left/S2_lemma:.6f} (->0: consistent with Lemma 1)")
print("  => E/S2 -> infinity at rate T^{0.258}/L: left-tail obstruction STANDS; "
      "validator's 'E/S2 -> O(1)' is FALSE")
