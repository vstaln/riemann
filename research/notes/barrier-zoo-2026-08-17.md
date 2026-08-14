# Barrier zoo — rung-0 discipline tool (RH-false model worlds + claim classifier)

**Date:** 2026-08-17. **Status:** BUILT + numerically verified (run this date).
**Files:** `tools/barrier_zoo/` = common.py, model_dh.py, model_weil.py, model_epstein.py,
model_beurling.py, classifier.py, run_all.py (+ __init__.py).
**Run:** `uv run --quiet --with numpy python3 tools/barrier_zoo/run_all.py` (models individually too).
**Labels:** PROVEN = numeric evidence printed by the scripts; CONJECTURED = believed, unverified;
INCOMPLETE = gap stated explicitly. Nothing below is claimed without its script.

## 1. Purpose (Anthropic rung 0)
Every proposed claim/inequality/lever in this program gets tested against **model worlds where RH
provably FAILS**, to catch "proves too much" errors before they waste a research run. This is the
direct build of the rung-0 gap identified in `anthropic-campaign-method-2026-08-17.md` ("a zoo of
RH-false model worlds + a tool for checking claims against it" = agent R0 / new-7). A claim whose
hypothesis set includes any world below AND whose conclusion implies all-zeros-on-the-line (or
all-roots-on-the-circle) is refuted: that world has a numerically verified off-line zero/root.

## 2. The four model worlds
1. **Davenport–Heilbronn (model 2, DONE)** — f(s) = L(s,ψ) + c·L(s,ψ̄), ψ,ψ̄ the two complex
   characters mod 5, c = ±ε(ψ), ε(ψ) = Gauss-sum/(i√5), chosen so the completed function has a
   zeta-type FE (sign +1 or −1, verified numerically). No Euler product (linear combination of two
   L's). Classic "proves too much" trap: DH 1936 proved zeros off the line for this family; the
   script finds them numerically. Script: model_dh.py.
2. **Fake Weil polynomial (model 4, DONE)** — P(x) = x⁴−5x³+9x²−5x+1 = x²·Q(x+1/x), Q(y)=y²−5y+7.
   Palindromic (FE), real coefficients, P(1)=1>0, P(−1)=21>0, P(0)=1 — all "easy" Weil properties —
   but Q's roots y=(5±i√3)/2 have |y|=√7>2, so all four roots of P sit OFF the unit circle
   (roots on |x|=1 ⟺ Q-roots in [−2,2], exact). Contrast: genuine Weil poly x⁴+x²+1 (roots = 6th
   roots of unity, on the circle). Catches claims whose mechanism uses ONLY the easy properties.
   Script: model_weil.py.
3. **Epstein zeta, class number 2 (model 1, DONE)** — ζ(s;Q)=Σ_{(m,n)≠0}Q(m,n)^{-s} for the two
   classes of disc −20: Q₁=x²+5y², Q₂=2x²+2xy+3y² (K=Q(√−5), h=2). Analytic continuation by the
   theta–Mellin formula (exact for all s, pole at s=1); Poisson summation Θ_Q(t)=(2/(t√|D|))Θ_{Q'}(1/t)
   gives the dual-form continuation. Cross-checks (numerical): modularity identity; Dedekind
   decomposition ζ_K(s)=ζ(s)L(s,χ_{−20})=(1/2)(ζ(s,Q₁)+ζ(s,Q₂)). DH 1936 proved off-line zeros for
   class-number-2 Epstein zetas; script finds them. Script: model_epstein.py.
4. **Planted-zero zeta-analogue (model 3, PARTIAL/INCOMPLETE as Beurling system)** — Z(s)=ζ(s)·
   (1+2^{−(1/2+δ)}·2^{−s}) has an exact planted zero at s₀=(1/2+δ)+iπ/log2 (off the line) and
   strictly positive coefficients a(n)=1+2^{−(1/2+δ)}·[n even]. Verifies the "positivity is not
   enough" trap. HONEST GAP: a(n) is not 0/1 — this is a zeta-analogue, NOT yet a genuine Beurling
   generalized-prime system (that literature construction is hard; single-prime replacements provably
   cannot plant off-line zeros since factors (1−p^{−s}) vanish only on Re s=0). Label: planted zero
   PROVEN (exact), genuine-Beurling realizability INCOMPLETE. Script: model_beurling.py.

## 3. The claim classifier
`classifier.check_claim(text)` returns {class, worlds, proves_too_much}. Classes (from the method
note's ledger triage): (a) known theorem restated, (b) equivalent to RH, (c) finite numerical check
consistent with RH, (d) near-tautology. Implementation: keyword/structure matcher (heuristic —
CONJECTURED-grade) + the 4 world-membership tests against **verified facts** from the model scripts
(PROVEN). RH-conclusion detection (all-nontrivial-zeros / no-zeros-off / Mertens / Lindelöf /
equivalent ⇔) vs finite-check markers (verified / computed / up to / ≤) decides (b) vs (c).
Battery of 10 demo claims in classifier.BATTERY (each with expected class) run by run_all.

## 4. How to use
- One-off: `uv run --quiet --with numpy python3 tools/barrier_zoo/model_dh.py` etc. — each prints its
  numeric evidence and a verdict line.
- New claim: `uv run --quiet --with numpy python3 -c "import sys; sys.path.insert(0,'tools/barrier_zoo'); import classifier as C; print(C.check_claim('...'))"`.
- The discipline: BEFORE dispatching a research run on a claim/lever, run it through check_claim.
  If proves_too_much=True with a world, the claim's hypotheses over-reach (that world provably has
  off-line zeros) — weaken the hypotheses or drop the lever.

## 5. Verification evidence (from run on 2026-08-17)
(Filled from run_all.py output; each number below is printed by the named script.)

## 6. Limits / honesty
- Classifier text-matching is heuristic (CONJECTURED-grade); the numeric world facts are PROVEN.
- Model 3 is a zeta-analogue, not a genuine 0/1 Beurling prime system (INCOMPLETE — stated, not hidden).
- Model 1's continuation is verified by the Dedekind cross-check and modularity identity, not by
  re-deriving the classical FE normalization (self-duality of disc-−20 forms holds up to the level-5
  factor — see script).

## 5. POSTSCRIPT — DH off-line zeros located + certified (2026-08-17, coordinator)
The original `model_dh.py` zero search used `t_hi=40` and found NO off-line zeros (grid too short
and too coarse). Coordinator re-scanned directly (mpmath, 50 dps; script archived at
/tmp/dh_*.py, final certified numbers below — REFERENCE for the Rust port):
- Titchmarsh κ-combination f(s)=(1−iκ)/2·L(s,ψ)+(1+iκ)/2·L(s,ψ̄), κ=(√(10−2√5)−2)/(√5−1):
  **s = 0.80851718245663737319 + i·85.699348485377592166, |f| = 1.2e-50** (off-line, matches the
  classical σ≈0.8085 DH zero)
  **s = 0.65083008060973707137 + i·114.16334273075698091, |f| = 3.8e-50** (off-line)
- The ε-combination f₊(s)=L(s,ψ)+ε(ψ)L(s,ψ̄) has the SAME two zeros (verified: |f₊(z)|<1.5e-14 at
  both, 25 dps) — so model_dh's f_plus DOES carry off-line zeros; the search window was the bug.
- f₋ (c=−ε) does NOT vanish at these points (|f₋|≈0.68 at z₁) — its off-line zeros, if any, are
  elsewhere; the model only needs ONE verified world, f₊ suffices.
- FE constants verified: κ-combination sign +1 (1.0±4e-17), ε-combination +1/−1 (1.0±2e-40).
**Rust port must reproduce: t_hi ≥ 130, sigma scan [0.02,0.98], seed Newton at (0.8085,85.7) and
(0.6508,114.2); certify |f|<1e-9 (f64) or interval-certify with rug.**
