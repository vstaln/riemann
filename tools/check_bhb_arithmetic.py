#!/usr/bin/env python3
"""Verify hand arithmetic in bhb-zeta2-moment-2026-08-14.md (and M1 gap table).

Claims checked:
  1. slack: E/S2 < 1 - 0.6818*(27/19) = 0.0311
  2. r = 99/1274 ~ 0.0777 (good part)
  3. r' = c(M)/c(S2) = (1/5)/(1/3) = 3/5
  4. b_zeta2only = 0.0311/(2*sqrt(r'))  ~ 0.0201
  5. b_full     = 0.0311/(2*sqrt(2*(r+r'))) ~ 0.0134
  6. M1 boxes: b = 0.0311/(2*sqrt(r)) ~ 0.0558 (diagonal); with net 57/64 -> 0.0494
  7. c(S2) = 1/3 + 7/24 + 49/576 + 13/72 = 57/64
  8. MF = 3*t*P + 3*t^2 P^2 + (1/4t) P'^2 = 107/64; (1/3)(1+MF) = 57/64
"""
import math

def main():
    # 1. slack
    slack = 1 - 0.6818 * (27/19)
    assert abs(slack - 0.0311) < 1e-4, slack
    print(f"1. slack E/S2 < {slack:.6f} (target 0.0311)")

    # 2. r
    r = 99/1274
    print(f"2. r = {r:.6f} (99/1274)")

    # 3. r'
    rp = (1/5)/(1/3)
    assert abs(rp - 0.6) < 1e-12
    print(f"3. r' = {rp} (=(1/5)/(1/3))")

    # 4,5. boxes
    b2 = 0.0311/(2*math.sqrt(rp))
    bf = 0.0311/(2*math.sqrt(2*(r + rp)))
    print(f"4. b_zeta2-only  = {b2:.6f} (claimed 0.0201)")
    print(f"5. b_full F'     = {bf:.6f} (claimed 0.0134)")
    assert abs(b2 - 0.0201) < 1e-3 and abs(bf - 0.0134) < 1e-3

    # 6. M1 boxes
    b_diag = 0.0311/(2*math.sqrt(r))
    # net-S2 version: r_net = (3t^3 int u^2 P^2)/(57/64)  [net S2 constant, not diagonal 91/80]
    t = 1/2
    r_net = (3*t**3 * (33/140)) / (57/64)
    b_net = 0.0311/(2*math.sqrt(r_net))
    print(f"6. M1 boxes: b_diag={b_diag:.5f} (claimed 0.0558), b_net={b_net:.5f} (claimed 0.0494), r_net={r_net:.6f}")
    assert abs(b_diag - 0.0558) < 1e-3 and abs(b_net - 0.0494) < 1e-3

    # 7. c(S2) at t=1/2, P(u) = -t u^2 + (1+t)u  — EXACT rational arithmetic
    from fractions import Fraction as F
    t = F(1, 2)
    iP  = F(7, 12)      # int_0^1 P
    iP2 = F(17, 40)     # int_0^1 P^2
    iPp2 = F(13, 12)    # int_0^1 (P')^2
    cS2 = F(1, 3) + t*iP + t*t*iP*iP + (F(1, 12*t))*iPp2
    print(f"7. c(S2) = {cS2} (claimed 57/64)")
    assert cS2 == F(57, 64)

    # 8. MF
    MF = 3*t*iP + 3*t*t*iP*iP + (F(1, 4*t))*iPp2
    print(f"8. MF = {MF} (claimed 107/64); (1/3)(1+MF) = {(1+MF)/3}")
    assert MF == F(107, 64) and (1+MF)/3 == F(57, 64)

    # 9. M3: pair-form box (new identity E = sum_pairs |F(rho)-F(1-rhobar)|^2, see bhb-m3 note)
    #    E/S2 <= 8 b^2 (r+r')  (quadratic pair form) vs old triangle 2b sqrt(2(r+r'))
    b_pair = math.sqrt(0.031126315789473682 / (8 * (r + rp)))
    print(f"9. pair-form box b_pair = {b_pair:.6f} (claimed 0.0758; triangle-form 0.0134)")
    assert abs(b_pair - 0.0758) < 1e-3

    # 10. M3: GM thresholds (arXiv:2405.20552)
    #     sharper 15/(3+5sigma) on [7/10,8/10]: need c(1/2-D) < 1/2  <=>  D > 19/70
    from fractions import Fraction as F
    D_sharp = F(19, 70)
    D_uniform = F(17, 60)   # uniform 30/13: D > (c-1)/(2c)
    s = 0.5 + 0.28
    exp_gm = 15 * (1 - s) / (3 + 5 * s)
    print(f"10. GM thresholds: D_sharp={float(D_sharp):.6f} (=19/70), D_uniform={float(D_uniform):.6f} (=17/60); "
          f"at Delta=0.28 (sigma={s}): GM exponent {exp_gm:.4f} < 1/2 OK")
    assert float(D_sharp) < 0.28 < 1 / 2 and exp_gm < 0.5

    print("ALL CHECKS PASS")

if __name__ == "__main__":
    main()