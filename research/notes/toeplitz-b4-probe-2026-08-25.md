# Toeplitz / Determinantal b=4 Probe — Consistency Check

**Date:** 2026-08-25
**Source lens:** `xdom-repthy-2026-08-24.md` (Tier 3, Rung 1 — "first separating
rung" b=4 / H_3 test)
**Method:** exact rational arithmetic (`fractions.Fraction`), read-only.
**Verdict (label):** INSTANTIATED — *moment-side* claims; NOT_FORMULATED —
*Toeplitz/Borodin–Okounkov* reduction. Inequality direction HOLDS.

---

## 1. Recompute the three numbers from their defining formulas

The formulas ARE written down, in `fourth_moment_analysis.md`
(`/home/vstaln/riemann/research/notes/fourth_moment_analysis.md`), and
re-derivation reproduces all three exactly. All arithmetic below was recomputed
here with `fractions.Fraction` (exact, no floats).

**CUE side, m_4 = 346/105 (PROVEN — re-derived).** The sine-kernel trace moment
at λ=1 assembles as
`m_4(1) = 1 + 6(1/3) + 2/3 + A_4(1)`, with `A_4(1) = −13/35`
(T_1=1, 6J/λ²=12/3, E=12/35, F=1/2, G=2/5). Sum:
`1 + 2 + 2/3 − 13/35 = 11/3 − 13/35 = 346/105 = 3.295238…`  ✓ (matches note §3.3)

**Extremal 5/6 configuration, m_4 = 10/3 (PROVEN — re-derived).** The sharpness
config (s_1 = 2/3 N simple atoms weight 1, s_2 = 1/6 N double atoms weight 2)
gives moments `m_k = (2/3)·1^k + (1/6)·2^k`:
`m_4 = 2/3 + (1/6)·16 = 2/3 + 8/3 = 10/3 = 3.333…`  ✓ (matches note §3.3)
Difference Δ = 10/3 − 346/105 = (350−346)/105 = **+4/105** (PER THE NOTE'S
CONVENTION: extremal is LARGER — see §3 caveat).

**Hankel H_3 (PROVEN — re-derived).** H_3 = 3×3 Hamburger moment Hankel
`(H_3)_{ij}=m_{i+j}`, i,j ∈ {0,1,2}, built on (m_0..m_4):
- **CUE:** m = (1, 1, 4/3, 2, 346/105) → `det H_3 = 58/945 = +0.06138` (> 0) ✓
- **Extremal:** m = (5/6, 1, 4/3, 2, 10/3) → `det H_3 = 0` exactly (rank collapse 3→2) ✓

All three claimed numbers are exact rationals, self-consistent under their
documented formulas.

## 2. Dimensional consistency

- **Matrix sizes comparable.** Both H_3 objects are 3×3 (indices 0..2), built
  from the same 5-moment window (m_0..m_4). No size mismatch. ✓
- **Normalization caveat (flag).** The two sequences share m_1,m_2,m_3 =
  (1, 4/3, 2) — the documented k≤3 degeneracy the argument exploits — but differ
  in **m_0**: CUE uses m_0 = 1 (true probability measure, total mass 1) while the
  extremal uses m_0 = 5/6 (sum of atom weights 2/3+1/6 = 5/6, i.e. the distinct-
  atom mass, NOT a normalized probability). The comparison is therefore between
  a normalized and an unnormalized moment sequence. This does not break the
  discriminator — the CUE 3×3 minor remains PD and the extremal remains rank-2
  regardless of the m_0 scale factor — but it means the "CUE vs extremal" object
  comparison is not literally measure-vs-measure; the CUE object is a measure
  and the extremal object is an atom configuration with mass < 1. Any future
  Borodin–Okounkov argument must place both on the same normalization.
- **Inequality direction HOLDS, and is the direction the argument needs.**
  The b=4/H_3 test needs CUE `det > 0` (positive-definite Hankel → full rank 3)
  versus extremal `det = 0` (rank collapse to 2). Re-derivation gives exactly
  +58/945 vs 0. A genuine determinantal/CUE spectral measure is PD (hence
  det>0); the 5/6 wall is rank-degenerate (det=0). This is the required
  separation and a non-CUE control fires it. ✓

## 3. What the probe actually instantiates — and what it does NOT

Honest split of the claim:

- **INSTANTIATED (moment side):** 346/105, 58/945, 10/3, 0 are all pinned by
  exact arithmetic from documented formulas in `fourth_moment_analysis.md`
  (§3.2–3.4), corroborated by `kloosterman_dispersion_proof.md` (m_4(1)=346/105
  certified) and the m_4 piece tools (`m4_pieces.py`, E=12/35, G=2/5, J_2=1/3).
- **NOT_FORMULATED (Toeplitz/Borodin–Okounkov side):** the objects actually
  computed are *Hamburger moment Hankel* determinants (Stieltjes/Carleman
  realization objects). The `xdom-repthy` Tier-3 claim — that layer-(b) is one
  *Toeplitz-determinant-sign* statement obtained via Borodin–Okounkov (the
  n-level Toeplitz determinants being Fredholm determinants of the sine kernel)
  — is **asserted, never instantiated**: no Toeplitz determinant (entries
  h_{i−j} from the symbol's Fourier coefficients, in the Toeplitz/ASW sense)
  is computed anywhere I found (grep of the note and the
  `zeta-density-one-reproduction` repo returns only the *moment* Hankel H_3 and
  H^n files, never a Toeplitz matrix of sine-kernel symbol coefficients).
  A moment-Hankel determinant is a different object from a Toeplitz determinant,
  and the reduction that would bridge them (sine-kernel ⇒ Toeplitz minors'
  alternating/positive signature) is CONJECTURED, not derived.

Consequence (the finding): the b=4 probe is a *consistent numerical discriminator*
between two hand-specified spectral objects, but it does **not** test the
Toeplitz/determinantal reduction it is presented under. To certify layer-(b) at
b=4 via Borodin–Okounkov, the theorem must be stated on the Toeplitz object.

## 4. Precise statement a Borodin–Okounkov-type theorem must prove (to certify layer-(b) at b=4)

> Let the n-level correlation kernel of the relevant arithmetic spectral measure
> be asymptotically the sine kernel S(x) = sin(πx)/(πx), and let φ be its symbol
> on the unit circle with Fourier coefficients a_k (k ∈ ℤ). Define the Toeplitz
> minors T_n = det( a_{i−j} )_{0≤i,j≤n−1}. A Borodin–Okounkov-type certification
> of layer-(b) at b=4 requires: (i) **normalizing both candidates to a single
> measure** (the same m_0 convention, fixing the §2 caveat); and (ii) proving, for
> the CUE/sine-kernel symbol, the Toeplitz minors keep the strictly-positive /
> alternating signature at order n=4 — concretely `T_4 > 0` with the correct sign
> signature — while the *arithmetic* symbol demonstrably shares that signature to
> the order at which `m_4(T) → m_4 = 346/105`, and separating it from the
> 5/6-extremal symbol whose corresponding Hankel/Toeplitz object collapses
> (det = 0). Until T_4 and its alternating-sign minor sequence are computed from
> an actual symbol (not the Hamburger moment matrix), the reduction remains
> NOT_FORMULATED and the b=4 test stands only as a moment-severity discriminator.

---
**Labels used:** PROVEN = exact rational arithmetic, re-derived here.
NOT_FORMULATED = the Toeplitz/Borodin–Okounkov object is asserted but no
instantiating formula exists in the note or `zeta-density-one-reproduction`.
