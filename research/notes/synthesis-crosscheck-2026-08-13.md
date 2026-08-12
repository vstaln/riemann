# SYNTHESIS CROSS-CHECK — the window-frequency contradiction is RESOLVED

**Date:** 2026-08-13 (overnight synthesis). **Method:** s4h — combining existing research,
resolving cross-source contradictions before any new computation. **Labels:** PROVEN / CHECKED
NUMERICALLY / CONJECTURED per hooks/agents.md.

## The contradiction (two sources disagreed, and it was the highest-stakes disagreement in the corpus)

- `research/waves/wave-blast/results/idea-constraint.md` (constraint-inversion catalog) ranks as
  its **#1 idea "W-1"**: "change the window frequency α from √2 to 1.0 → H0 jumps from 0.6725 to
  0.8579, a +27.5pp increase, three orders above every other lever." It tabulates
  `H0(0.9)=0.9499, H0(1.0)=0.8579, H0(√2)=0.6725, H0(1.8)=0.6051` and calls this "the single
  highest-leverage idea in this document."
- `research/notes/attack-kernel.md` (executioner, Lean-backed + validator-corrected) PROVES
  cos(√2u) is the **global** minimizer of the Montgomery functional Q and that every other window
  (cos(λu), λ≠√2, and polynomials) is *worse*. "0.6725 is the window ceiling."

These cannot both be true. A synthesis that doesn't resolve this would either (a) waste compute
chasing a phantom +27.5pp, or (b) re-derive a proven wall.

## The resolution (CHECKED NUMERICALLY — exact mpmath, commands below)

The catalog's `H0(α) = 3/2 − (1/α)·cot(1/α)` is a **naive scalar substitution** of √2 → α inside
the Theorem D constant. That substitution is only valid AT α = √2, where it equals the true value
1/2 + (1/√2)cot(1/√2) = 1.3274992963. For general λ, the Montgomery functional is

  Q(λ) = [∫v² + ∬|s−s′|v(s)v(s′)] / (∫v)² ,  v = cos(λu) on [−1/2,1/2]

and its true values are:

| window cos(λu) | Q(λ) | true proportion 2−Q(λ) |
|---|---|---|
| λ=0.9 | 1.329646 | 0.670354 |
| λ=1.0 | 1.329029 | 0.670971 |
| λ=1.2 | 1.327989 | 0.672011 |
| **λ=√2=1.4142** | **1.327498** | **0.6725017 (MAX)** |
| λ=1.6 | 1.328017 | 0.671983 |
| λ=1.8 | 1.330135 | 0.669865 |

**The true function is non-monotonic with a clean global maximum at λ = √2.** The catalog's
"0.8579 at λ=1.0" is an artifact of mis-extrapolating the scalar formula. `attack-kernel.md` is
correct; the catalog's #1 idea is **REFUTED (units error, not a real lever)**.

## Consequence for the synthesis

- The window is NOT a lever (re-confirmed). H = 0.6725007 is the window ceiling, and α in
  `tools/bound-sweep`'s `h_window` is a *kernel frequency* parameter, not the window width — the
  two parameters are distinct, and the catalog conflated them.
- The corrected ε-floor work (retraction-673-invalid.md) already folded this in: the honest bound
  is 0.6730690, below trmdy/tawanerguo.
- **Remaining live levers** (from the corpus, after removing the refuted W-1): the in-class gap
  0.6725→0.6818 (V2 LP dual), the read-constrained τ-floor (E-1), the third moment (V3), and the
  B/m quadratic interval (B-3). These are the *combinations* to pursue next — see the synthesis
  plan (next note).

## Commands (reproducible)

```bash
cd /home/vstaln/riemann
uv run --with mpmath python3 -c "
import mpmath as mp; mp.mp.dps=30
def Q(lam):
    v=lambda s: mp.cos(lam*s)
    Iv=mp.quad(lambda s: v(s),[-0.5,0.5]); Iv2=mp.quad(lambda s:v(s)**2,[-0.5,0.5])
    D=mp.quad(lambda s: mp.quad(lambda sp: abs(s-sp)*v(s)*v(sp),[-0.5,0.5]),[-0.5,0.5])
    return (Iv2+D)/(Iv*Iv)
for lam in [0.9,1.0,1.2,mp.sqrt(2),1.6,1.8]: print(lam, mp.nstr(Q(lam),12), mp.nstr(2-Q(lam),12))
"
```

## Honesty ledger

- PROVEN: cos(√2u) is the global minimizer of Q (attack-kernel.md, Lean `Zeta23/ThmD`).
- CHECKED NUMERICALLY: the Q(λ) table above (mpmath 30-digit quadrature).
- REFUTED: idea-constraint.md's "W-1" (the 0.8579 value is a units/extrapolation error).
- The corrected bound 0.6730690 stands (retraction-673-invalid.md); this cross-check does not
  change it, it removes a phantom lever from the search space.
