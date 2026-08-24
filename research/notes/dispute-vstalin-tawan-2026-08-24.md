# Dispute check: vstalin verifier vs Tawan's coboundary theorem

Date: 2026-08-24
Status: PROVEN (against the source, cross-checked in three independent places:
proof markdown, paper TeX, and the verifier C++ that is actually run).
Scope: read ONLY inside research/external-results/tawanerguo-zeta-simple-zeros/
(BELLMAN_COBBOUNDARY_PROOF.md, paper/riemann.tex, tools/verify_coboundary.cpp,
README.md). No repo tooling touched. Nothing fixed.

--------------------------------------------------------------------
## (a) Exact statement of Tawan's local-to-global lemma / per-window inequality
--------------------------------------------------------------------

The theorem is stated verbatim in BELLMAN_COBBOUNDARY_PROOF.md (lines 5-12):

> With the nonnegative window `v(s)=cos(1.47 s)` on `[-1/2,1/2]`, the certified
> unconditional lower bound is
> `liminf N_0^s(T,2T)/N(T,2T) >= 0.6731929114731422535099843283...`.

The per-window object is built in BELLMAN_COBBOUNDARY_PROOF.md (lines 18-30):

> For six gaps, let `F_0` be the uniform seven-point functional and define
> `U(g1,...,g5) = (54 g1 - 123 g2 + 123 g4 - 54 g5)/1920000
>                 + 5971/300000 [w(g1)+w(g2)-w(g4)-w(g5)]`
> `F_B(g1,...,g6) = F_0(g1,...,g6) + U(g2,...,g6) - U(g1,...,g5).`
> The redistributed coefficients are
> `p = (946,1177,877,877,1177,946)/1920000`
> `q = (31343/100000, 1/3, 105971/300000, 105971/300000, 1/3, 31343/100000).`
> They satisfy `sum(p)=1/320`, `sum(q)=2`; longer-span coefficients still sum
> to `2`.  Thus the coboundary telescopes on periodic sequences while retaining
> nonnegative finite-block pressure.

The same object, in the paper, paper/riemann.tex lines 162-178:

> For six consecutive gaps $g_1,\ldots,g_6\ge 0$, start from the seven-point
> functional $F_0$ and add the explicit five-gap coboundary
> $U(g_1,\ldots,g_5)=\cdots$, $F_B(g_1,\ldots,g_6)=F_0(\cdots)+U(g_2,\ldots,g_6)-U(g_1,\ldots,g_5)$.
> The resulting **pressure and nearest-neighbour coefficients** are
> $(p_1,\ldots,p_6)=(946,1177,877,877,1177,946)/1920000$, and
> $(q_1,\ldots,q_6)=(31343/100000,\ 1/3,\ 105971/300000,\ 105971/300000,\ 1/3,\ 31343/100000)$.
> Here $\sum p_i=1/320$, $\sum q_i=2$, so the coboundary telescopes while
> preserving global pair-energy accounting.  Its directed-MPFR CWD2 certificate
> proves $\mathcal F_B(g_1,\ldots,g_6)\ge 577/100000$, $\alpha=147/100$.

--------------------------------------------------------------------
## (b) THE question: are q_i·w(g_i) IN ADDITION TO span-one pair terms or IN PLACE OF them?
--------------------------------------------------------------------

IN PLACE OF. The audit's mass-counting argument is FAITHFUL to the source.

Decisive evidence — the verifier that is actually run,
tools/verify_coboundary.cpp, lines 239-247:

```
constexpr std::uint64_t kPressureDenominator = 1920000;
constexpr std::array<Rational, 6> kNearestRationals = {
    Rational{31343, 100000}, Rational{1, 3},
    Rational{105971, 300000}, Rational{105971, 300000},
    Rational{1, 3}, Rational{31343, 100000}};
constexpr std::array<Rational, 7> kSpanRationals = {
    Rational{0, 1}, Rational{0, 1}, Rational{2, 5}, Rational{1, 2},
    Rational{2, 3}, Rational{1, 1}, Rational{2, 1}};
```

- `kNearestRationals` (= q) is the span-one layer: nearest[j] = q, applied to
  w(g_{j+1}) (see loops at lines 291-295 and 472-477).
- `kSpanRationals` = (0,0, 2/5, 1/2, 2/3, 1, 2), indexed by span r=0..6. The
  **span-one entry (index 1) is 0/1** — there is NO span-one pair term in the
  longer-span layer. The pair terms loop starts at `span=2` (lines 296-297
  `for (int span = 2; span <= 6; ++span)`; and 479-480).

So the functional the code certifies is exactly

  F_B = Σ p_i·g_i + Σ q_i·w(g_i) + Σ_{r=2}^{6} (2/(7−r))·Σ_{i=0}^{6−r} w(y_{i+r}−y_i)

because span[r] = 2/(7−r): 2/5, 1/2, 2/3, 1, 2 correspond to r = 2..6.
This is precisely the audit's F_T. The q_i REPLACE the span-one layer; they do
NOT sit on top of it. The paper calls q "the nearest-neighbour coefficients",
i.e. q IS the span-one layer after redistribution.

Mass check (audit's argument): in the uniform seven-point functional, the
span-one pair terms would be 6 terms × 2/(7−1) = 6 × 1/3 = 2. The q vector has
Σ q_i = 31343/100000·2 + 1/3·2 + 105971/300000·2 = 2. Equal mass → replacement,
not an additional layer. PROVEN.

(Cross-confirmation of the arithmetic of "redistribution": the coboundary adds
∓5971/300000 to the span-one coefficients at indices 1,3,4,6 — exactly
31343/100000 = 1/3 − 5971/300000 and 105971/300000 = 1/3 + 5971/300000 — while
leaving indices 2,5 at 1/3. So F_B's span-one layer is literally F_0's span-one
layer modified by the coboundary = the q_i, with no extra span-one pair mass.)

Consequence for the dispute: a verifier certifying F_V as written in the audit
concerns — q·w(g) PLUS "ALL pair terms" including span-one at coefficient
2/(7−1)=1/3 — would DOUBLE-COUNT the span-one mass (2 + 2 = 4, not 2) and would
NOT match Tawan's theorem. Tawan's certified F_B = F_T, with q on span-one and
zero span-one pair terms, longer spans 2/(7−r).

--------------------------------------------------------------------
## (c) What must be proven window-by-window for the global N_0/N bound
--------------------------------------------------------------------

Per-window inequality (the sole computer-assisted assertion, paper line ~180)
BELLMAN_COBBOUNDARY_PROOF.md lines 37-40 and paper riemann.tex:

  F_B(g_1,...,g_6) >= 577/100000,  for all admissible 7-tuples of consecutive
  gaps g_1,...,g_6 >= 0, alpha = 147/100.

The admissible set is the six-fold Cartesian product of the one-body pressure
two-cell component partition = 2^6 = 64 initial boxes (verified all true).
The verifier bounds F_B below by: pressure + Σ q_i·w(g_{i+1}) + Σ_{r=2}^{6}
(2/(7−r))·Σ_i w(y_{i+r}−y_i), checked via convex-tangent, interval, and
exact-positive-definite-LDL Hessian bounds.

Global step (BELLMAN proof lines 42-52):
- Sum the seven-point inequality over the block of m=183 gaps:
  E_m + P_m >= (577/100000)(m−6).
- The redistributed pressure tax is (m−6)/320 averaged → 59/19520
  (Σ p_i = 1/320).
- Trace-energy envelope (docs/trace_energy_envelope.md) gives
  B = 1.0212287852929821661489401766...
- Final: (H_alpha − 59/19520)/(1 − B/183) = 0.6731929114731422535099843283...

So the invariant shape the local-to-global lemma needs is exactly
"F_B ≥ eps (eps = 577/100000) on the admissible set", summed over windows, with
the telescope making the coboundary cancel on periodic sequences.

--------------------------------------------------------------------
## (d) Verdict
--------------------------------------------------------------------

THEOREM REQUIRES F_T.

The q_i w(g_i) terms sit IN PLACE OF the span-one pair terms; the audit's
mass-counting (Σq = 2 vs 6·(1/3) = 2, replacements not an additional layer) is
faithful to the source. Tawan's actual verifier certifies exactly F_T, not a
span-one-doubled F_V.
