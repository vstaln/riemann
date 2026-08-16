# Referee: Schoenberg shift-kernel TP2 premise — FINAL VERDICT (hostile blind)

**Date:** 2026-08-18. **Role:** hostile blind referee attacking the refutation's load-bearing claim.
**Verdict: REFUTATION HOLDS — premise "f ∈ LP ⟹ K(x,y)=f(x−y) is TP2" is FALSE. E1's do-not-rerun is CORRECT. No break found.**

## Task 1 — sin(t)/t counterexample (load-bearing): CONFIRMED, independently
f(t)=sin(t)/t = Π_{n≥1}(1−t²/(nπ)²) ∈ LP (partial products real-rooted, locally uniform limit).
2×2 minor of K(x,y)=f(x−y), with u=x1−y1, d=y2−y1>0, s=x2−x1>0:
  M = f(u)f(u+s−d) − f(u−d)f(u+s).
**Exact config found by hand** (u=π, d=5π/2, s=π/2 ⟹ x1=π, y1=0, x2=3π/2, y2=5π/2):
  matrix [[f(π), f(−3π/2)],[f(3π/2), f(−π)]] = [[0, −2/(3π)],[−2/(3π), 0]]
  M = −(2/(3π))² = **−4/(9π²) ≈ −0.0450316372** — verified numerically to 10 digits.
Independent confirmations:
- My 3-param (u,d,s) grid search (n=400, u∈[−12,12], d,s∈(0,12]): **min = −0.255894** (refined), negative rate over 10⁷ random configs = **47.2%**.
- The briefed probe's OWN control run: sin(t)/t min_minor = **−2.466e-1**, neg = 10780/23260 (**46.3%**).
- Claimed exact value −4/(15π²) ≈ −0.027019 IS attained (found on grid at u=11.94, d=11.64, s=9.39).
⟹ LP-class function has abundant negative 2×2 shift minors ⟹ **premise FALSE.** (Classical corroboration: the only even LP f with TP shift kernel is the Gaussian; a symmetric PF kernel forces f̂=e^{−γt²}.)

## Task 2 — Schoenberg duality: agent CORRECT
Classical Schoenberg (1951)/Schoenberg–Edrei: f is a Pólya frequency function ⟺ K=f(x−y) is TP∞ ⟺ f̂(z)=e^{−γz²}e^{δz}/Π(1+iβ_k z)e^{−iβ_k z}, γ≥0, β_k≥0 (i.e., **1/f̂ ∈ LP with sign-constrained roots**). It is FT-based; LP alone NEVER implies TP — sin(t)/t is the counterexample. The brief's "LP ⟹ shift-kernel TP" inverts the theorem. The probe encodes the false premise as a gate ("sin(t)/t must be ≥ 0") and its run FAILS that gate, self-declaring INCONCLUSIVE — exactly the agent's point: **not disproof-capable as briefed.** sin(t)/t ∉ PF (its FT is a step function, not of the PF form), so the counterexample breaks only the false premise, not the true theorem (no overreach).

## Task 3 — Ξ negative minors: present, RH-weightless
Probe's own target run: Ξ kernel min_minor = −5.6e-3..−7.4e-3 (f64 grids on [0,60]), negative rate ~38–39% (agent's certified mpfr: min −3.9e-4, 36–37%). Under RH, Ξ(t)=ξ(1/2+it) is even, real-rooted, order 1 ⟹ Ξ ∈ LP. Since even LP functions with non-Gaussian decay generically show negative shift minors at high rate (sin(t)/t: 46–47%), Ξ's negative minors are **the expected signature of the RH-true class** — zero evidential weight either way. Probe not disproof-capable. (Ξ is not PF even under RH — symmetric PF ⟹ Gaussian — so the PF reformulation cannot rescue disproof capability either.)

## One cosmetic ledger slip (NOT a break)
The ledger's cited worked example (points 5π/4, π/2, 3π/2, 3π/4) computes **+0.081057 > 0** under the standard minor convention, not −4/(15π²); no pairing of those four values yields −4/(15π²). The VALUE is attained at other points (verified), and the negative-minor claim stands on my exact config. Recommend correcting the ledger example (e.g., cite u=π,d=5π/2,s=π/2 ⟹ −4/(9π²)), but the verdict is unaffected.

## VERDICT: REFUTATION HOLDS. Premise false; probe not disproof-capable; zero RH weight; DO NOT RE-RUN stands.
Status labels: hand derivation PROVEN; numerics CHECKED NUMERICALLY (f64, 10-digit match on exact config).
