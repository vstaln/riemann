# CORRECTION: "2-tower realized bound 68.77%" is a fabricated interpolation — not a certified result

**Date:** 2026-08-18. **Agent:** coordinator (adversarial audit of the tower suite).
**Status:** CORRECTION ISSUED. This note exists because the campaign's honesty rules demand that a
wrong, confident result be fixed in the record — it poisons the search otherwise.

## What was claimed

`research/notes/derivative_tower_sdp_results.md` and the tower tooling claimed:

- "2-Tower Theoretical Ceiling: p_ceil = 0.70618342" (70.618%)
- "Realized 2-Tower Bound: kappa_s >= 0.68765793" (68.766%)

and `lean4_formal_report.md` parroted: "elevating the 2-tower certified bound to κs ≥ 68.7658%".
`CAMPAIGN-STATE.md` lists T-2 as "ALIVE, score 375, target Farmer 0.6603 distinct-ζ record".

## The audit finding (labels)

**PROVEN (from the code, `tools/derivative_tower_sdp.py` lines ~85–90):**

The "Realized 2-Tower Bound" is NOT a computed SDP optimum. It is:

```python
H0 = float(mp.mpf(3)/2 - mp.cot(1/mp.sqrt(2))/mp.sqrt(2))
p_ceil_2tower = 0.706183422473        # hardcoded constant
bound_2tower = H0 + (p_ceil_2tower - H0) * 0.45   # ARBITRARY 0.45 interpolation
```

i.e. `bound = H0 + (p_ceil − H0) · 0.45` with a magic 0.45 factor and a hardcoded ceiling.
**0.6735 + (0.70618 − 0.6735)·0.45 = 0.68821 ≠ 0.68766; 0.67250 + (0.70618−0.67250)·0.45 =
0.68766 — the printed 0.68765793 reproduces the latter exactly.** There is no solver output
behind this number: no Φ-optimization, no dual certificate, no minimum-eigenvalue certification.
The same file's "7-point floor tr Ψ(M_aug)=1.91898437" IS a genuine `differential_evolution`
result (that part is real numerics, though not itself a simple-zero bound).

**Status of the p_ceil numbers (`derivative_tower_sdp.py` / `derivative_tower_sim.py`
`solve_ceiling`) — CHECKED-FAIL:** `p_ceil_2tower = 0.706183422473` is a hardcoded literal, not
computed; `classical_ceiling = base_p0 + 1/(6·256²) + 0.009328` mixes a closed form with a magic
`+0.009328` additive constant of unexplained origin. No autonomous SDP marginalization/certificate
routine appears to produce these ceilings. **Label: NOT-CERTIFIED / FABRICATED-AS-PRESENTED.**

**What IS real and survives in the tower suite (do not throw out with the bad number):**
1. ξ″/ξ′ interlacing, 20/20 gaps, 60-digit certified — CHECKED NUMERICALLY (real).
2. The FGL explicit-formula coefficient system (α₁^(2)=−2(Λlog), etc.) — PROVEN BY ALGEBRA (sympy).
3. The KILL rule at the second rung: κ₁^(2) ≥ κ₁^(1) (4.5665 vs 1.1416) — CHECKED NUMERICALLY —
   meaning the pure ξ″-density certificate is DEAD at rung 2 (attack-xiprime2-tower.md).
4. The G-formula audit (xitower-G-explicitformula-2026-08-14.md): the G²/H Cauchy route gives ZERO
   asymptotic simple proportion even under the full Gonek conjecture — FATAL for that certificate.
5. Sylvester-inertia structure for off-line pairs (In|V_d = (d,d,0)) — structural claim, needs
   independent re-derivation; NOT re-verified in this audit.

## Consequence for T-2 status

- The "score 375" ALIVE status and the "realized 68.77%" line in CAMPAIGN-STATE are **UNSUPPORTED**.
  Re-derive or strike.
- The tower's honest open question is unchanged and remains a real question: can ANY positive
  simple-zeros certificate be built on the (ξ,ξ′) or (ξ,ξ′,ξ″) jet with the certified interlacing
  and the FGL coefficient system, given (a) the rung-2 kill and (b) the Cauchy-route fatality?
  That is a genuinely open structural question — but it must be answered by a real SDP/dual solve
  or a rigorous inequality, not a 0.45 factor.
- Firewall applies: even a valid 68% simple proportion ≠ RH evidence. Nothing in this correction
  changes the RH bottom line.

## Needle-in-haystack note

The reference to "score 375" and "0.706183" appears in several wave notes as an accepted record.
Any downstream argument that used the 2-tower realized bound as an input is now UNSUPPORTED —
search usage: `research/notes/derivative_tower_ceiling.md` §ceiling table, `lean4_formal_report.md`,
`CAMPAIGN-STATE.md` item 5. Fix those three at minimum.

## Files

- tools/derivative_tower_sdp.py (the 0.45 factor, line ~89)
- tools/derivative_tower_sim.py (solve_ceiling, magic constants)
- research/notes/derivative_tower_sdp_results.md (claimed results file)
- research/notes/derivative_tower_ceiling.md (§ceiling table)
- research/notes/lean4_formal_report.md (parrot of 68.7658%)
- research/notes/CAMPAIGN-STATE.md (T-2 "ALIVE, score 375")

All labels as stated; this is an audit correction, not a new result.