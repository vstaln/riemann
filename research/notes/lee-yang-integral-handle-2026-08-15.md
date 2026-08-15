# Integral-of-h_u superposition handle (lee-yang-integral-handle-2026-08-15)
Status: ABANDONED (superposition principle refuted by an explicit, fully-proven counterexample
inside the exact block family). Residual: the handle reduces to the classical 1859 Riemann
integral / de Bruijn-Newman t=0 slice; no new structure was ever there.

## Setup (PROVEN, from verified context)
- w=(s-1)/s; G(w)=Xi(1/(1-w))=sum c_n w^n, c_n>=0; RH <==> G zero-free in |w|<1.
- h_u(w)=cosh(u(1+w)/(1-w)) has ALL zeros on |w|=1: (u-i*theta_k)/(u+i*theta_k), theta_k=(pi/2+pi*k)/u.
- G(w)=2 int_0^inf Phi(u) h_u(w) du, Phi>0 (wave8d).

## 1. Claim that would imply RH — exact refutation (PROVEN)
- Claim A (the brief's live handle, now FALSE): "the Phi-weighted integral over {h_u} is
  zero-free in |w|<1 for every positive weight in a wide class". The class is NOT closed:
- Counterexample (PROVEN, exact): half-plane zeta=(1+w)/(1-w). For 0<eps<1,
  f(zeta)=cosh(zeta)+eps*cosh(2*zeta) has zeros at zeta=+-arccosh((1+sqrt(1+8e^2))/(4e))+(2m+1)pi*i,
  Re>0. Proof: f=2e*t^2+t-e in t=cosh(zeta); negative root t_-=-(1+sqrt(1+8e^2))/(4e) has
  |t_-|>1 iff eps<1; cosh(zeta)=t<-1 forces Re zeta=arccosh(|t|)>0. Both summands are exact
  h_u blocks (u=1,2), weight eps>0. At eps=1: factors 2cosh(3z/2)cosh(z/2) -> axis-only
  (mechanism calibration). Positivity of the weight does NOT save the class.
- eps=0.7: Re zeta=arccosh(1.14936)=0.5399, zeta=0.5399+pi*i; disk |w|=|(zeta-1)/(zeta+1)|=0.9075<1.
- Robustness: zero simple (|f'|>0); persists under weight perturbation (Rouche; CHECKED below).
  Absolutely-continuous positive weights approximating delta_1+eps*delta_2 also fail. Hence RH
  cannot follow from "Phi>=0 + h_u circle-stable"; any proof must use the SPECIFIC Phi.
## 2. The handle reduces to the classical object (PROVEN)
- f(zeta):=G((zeta-1)/(zeta+1))=2 int Phi(u)cosh(u*zeta)du = L(zeta)+L(-zeta) = Xi(i*zeta),
  L(s)=int Phi(u)e^{us}du. Explicit (v=e^{2u}): L(s)=(1/2)pi^{-1/4-s/2} zeta(1/2+s)[2Gamma(9/4+s/2)
  -3Gamma(5/4+s/2)] — all content sits in the Gamma*zeta product, i.e. in Phi. The "integral over
  circle-stable blocks" IS Riemann's 1859 integral. RH <==> L(zeta)=-L(-zeta) unsolved in Re zeta>0.
## 3. Transfer table (s4h-analogy-domain-transfer)
| Domain | Source theorem | Verdict |
|---|---|---|
| Poyla / de Bruijn-Newman | heat flow preserves real zeros (de Bruijn); Xi_t; RH <==> Lambda<=0; Lambda<=1/2 (Rodgers-Tao) | ADOPT as frame; no closure theorem (t=0 open = RH) |
| Laguerre-Poyla class | closed under limits, NOT under positive convex combos | REJECT (counterexample is a clean LP-class instance) |
| Moments / Stieltjes-Carleman | real zeros of orthogonal polys from moments | REJECT (c_n not a power-basis moment in u) |
| Spectral / probability | f=M(zeta)+M(-zeta), M=MGF of X~Phi | REJECT (two-point X in {1,2}, P~{1,0.7} IS the counterexample) |
| Control / Kharitonov | interval / convex-family stability | REJECT (convex stability not preserved — confirmed exactly) |
| de Branges-Rovnyak | HB-class spaces | REJECT (circular) |
Best transfer: DBN. Transportable lemma: de Bruijn heat-flow preserves real zeros — the wrong
direction for this handle; the handle's question is exactly Lambda<=0.

## 4. Lateral moves (s4h-creativity-lateral-thinking)
- Dominant idea: "a positive superposition of circle-stable functions inherits stability".
- Assumptions escaped: (1) positivity is operative (FALSE — eps in (0,1)); (2) zero-density of
  h_u (spacing pi/u) constrains superpositions (FALSE — two-point measure lives in the family);
  (3) continuous superpositions beat discrete (FALSE — Rouche persistence); (4) shared Cayley
  structure matters (FALSE — it is just cosh(u*zeta)).
- Surviving direction (CONJECTURED, = classical program): attack L(zeta)=-L(-zeta) via the
  Gamma*zeta / Stirling asymptotic argument-principle route. No superposition shortcut exists.
## 5. Rust check (tools/integral_handle_probe.rs, f64, <5 s) — CHECKED NUMERICALLY
- (A) |(u-i*th)/(u+i*th)|=1.000000000000000 for all sampled u in {0.1,0.5,1,2,5}, k<3.
- (B) eps in (0.05,1.5): interior zeros iff 0<eps<1; min Re z = exact arccosh formula to 6 digits
  at every eps (eps=0.05->Re 2.998211,|w|0.7322; eps=0.7->Re 0.539906,|w|0.9075); none for eps>=1.
- (C) eps=0.7 zero: |f(z0)|=2.7e-16, |f'|=1.257 (simple); eps->0.65/0.75 keeps |f(z0)|=8.2e-2
  (Rouche persistence).
- (D) 16 of 40 random 3-term positive superpositions (u in {0.5,1,1.5,2}) have interior zeros
  (min Re z=0.0759): failure is GENERIC in the class, not a two-term fluke. (E) control
  (1-z)^3+(1+z)^3, |z|=1/sqrt(3)=0.577350 reproduced (machinery OK).

## 6. Forecast + inversion
- Forecast: naive principle fails at the margin (small incursions near |w|=1).
- Actual: failure is exact and clean (|w|=0.9075 two-term; 40% generic in 3-term class; mechanism
  is the quadratic-in-cosh resonance |t_-|>1 for eps<1). Inversion: the "structure to exploit"
  (zero spacing pi/u of h_u) is inert for superpositions; the entire content of the handle was in
  Phi — i.e. in the classical integral. No new lever was ever there.

## 7. Verdict
ABANDONED (superposition principle; exact counterexample in the true block family, PROVEN +
CHECKED NUMERICALLY). Residual (CONJECTURED): RH <==> Lambda<=0 (DBN, known) and the classical
Riemann-integral / Gamma-zeta track, unchanged and open. Ledger: integral-of-h_u superposition
DEAD; classical/DBN track unchanged.
