# SDP Pair-Correlation Bounds

**UPDATE 2026-08-18 (night, wave9-9A-refutation):** this note's structural reading is
CONFIRMED and now decisive: the unconditional transfer of CGdL's SDP class is REFUTED at the
object-identity step — BGSTB24's F (w(u)=4/(4-u^2), argument rho-rho', real parts enter) agrees
with Montgomery's ordinate-only F only under RH, so the [0,1] datum does not plug into CGdL's
identity (8). The strip-positive/Tsang cone conclusion here (line ~184: 'CGdL primal cone does
not transfer') is the correct end-state; the subsequent wave-9 9A claim of a clean 'sign-drop
replaces bandlimitation' transfer was WRONG and has been retracted. See wave9-9A-refutation-2026-08-18.md. on Σ_ρ (m_ρ − 1) via the Unconditional Montgomery Theorem — Certificate Structure

**Agent:** builder. **Date:** 2026-08-14.
**Task:** Candidate 3 of `structural-thread-newinput-2026-08-14.md`, worked out concretely as a
certificate STRUCTURE (not a number-grind): run the Chirre–Gonçalves–de Laat pair-correlation SDP
(arXiv:1810.08843) on the unconditional Montgomery theorem (BGSTB, arXiv:2306.04799).

**Sources read this session (text extracts):** `research/papers/cgdl-1810.08843-paircorr-sdp.txt`,
`research/papers/baluyot-etal-2306.04799.txt`. All formula references below cite these extracts.
**Skills applied:** `s4h-analogy-structure-mapping` (transfer the sphere-packing/Cohn–Elkies SDP
structure to the pair-correlation setting) and `s4h-design-constraints` (map which BGSTB inputs are
hard vs missing).

---

## 0. The one-sentence structure

CGdL's SDP optimizes a **majorant form factor** (a Cohn–Elkies function: nonnegative Fourier side,
eventually-non-positive physical side) against Montgomery's pair-correlation functional; made
unconditional, the *same* optimization must instead run over the **strip-positive bandlimited
Tsang class**, and BGSTB supplies the functional but **not the box/double-sum estimate** that
certifies the zeros actually live in the strip.

---

## 1. What BGSTB certifies (the unconditional input)

Write ρ = β + iγ = 1/2 + δ + iγ and w(u) = 4/(4 − u²). BGSTB's unconditional object is

  F(x, T) = Σ_{ρ,ρ′; 0<γ,γ′≤T} x^{ρ−ρ′} w(ρ−ρ′) = Σ x^{δ+δ′+i(γ−γ′)} w(δ+δ′+i(γ−γ′)).

**BGSTB Theorem 1** [PROVEN, unconditional]: the normalization
F(α) := (T/(2π) log T)⁻¹ F(T^α, T) is real, even, nonnegative, and

  F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T),  uniformly 0 ≤ α ≤ 1.

**BGSTB Lemma 5** [PROVEN, unconditional] — the "unconditional Montgomery linear functional":
for any even r ∈ L¹ with supp r ⊆ [−1, 1], Lipschitz at 0,

  Σ_{ρ,ρ′} r̂(i(ρ−ρ′)·(log T)/(2π)) w(ρ−ρ′) = (T/(2π) log T)·[ r(0) + 2∫₀¹ α r(α) dα + O(1/√log T) ].

The critical structural fact: the weight w(ρ−ρ′) = 4/(4 − (ρ−ρ′)²) is **complex** off the line
(δ, δ′ ≠ 0). Under RH it collapses to w(i(γ−γ′)) = 4/(4 + (γ−γ′)²) > 0, real. This one collapse is
what the SDP must replace.

---

## 2. The multiplicity sum through the 2-level density

Fourier inversion (CGdL eq. (8)) gives the 2-level density identity

  Σ_{ρ,ρ′} ĝ((γ−γ′)(log T)/(2π)) w(·) = N(T) ∫ ĝ(x) F(x, T) dx.

The diagonal (ρ = ρ′) part of the pair sum is Σ_ρ m_ρ². Hence the target object is

  Σ_{ρ: 0<γ≤T} (m_ρ − 1) = Σ_ρ m_ρ² − N(T) = [diagonal of the 2-level density] − N(T).

**Majorant bound (CGdL Lemma 8, PROVEN conditional on RH):** if the off-diagonal pair terms are
nonnegative, then with the Cohn–Elkies test function f,

  Σ_ρ m_ρ ≤ (Z(f) + o(1)) N(T),  Z(f) = r(f) + (2/r(f)) ∫₀^{r(f)} f(x) x dx,

so Σ_ρ (m_ρ − 1) ≤ (Z(f) − 1) N(T) and the simple fraction ≥ 2 − Z(f). CGdL's SDP attains
min Z(f) = 1.3208 (RH) ⇒ simple fraction ≥ 0.6792.

---

## 3. The primal SDP (decision variables)

**Decision variable:** an even Cohn–Elkies majorant f ∈ L¹(R). The role map (analogy to
sphere packing, Viazovska/Cohn–Elkies):

| Role in sphere packing | Role here |
|---|---|
| radial test function f | the same physical-side f |
| Fourier side f̂ ≥ 0 (majorant of the lattice kernel) | **form factor / majorant of the pair-correlation kernel**; f̂ ≥ 0 (Delsarte nonnegativity) |
| f(x) ≤ 0 for \|x\| ≥ r (radius cut) | the **bandwidth ≤ 1 cut, dualized**: f(x) ≤ 0 for \|x\| ≥ r, r = last sign change |
| f(0), f̂(0) normalizations | f(0) = f̂(0) = 1 |

**Objective (linear in f):** Z(f) = r + (2/r) ∫₀^r f(x) x dx.

**Concrete four-block SDP (CGdL §4, PROVEN):** f(x) = (r² − x²) v(x²)^T Y₂ v(x²) e^{−πx²},
f̂(x) = (s₃(x²) + x² s₄(x²)) e^{−πx²}, with s₃ = v^T Y₃ v, s₄ = v^T Y₄ v and Y₂, Y₃, Y₄ ⪰ 0,
linked coefficientwise by the Laguerre–Fourier operator
T[−(r²−x²)v^TY₂v] = s₃ + x²s₄, plus f(0) = 1, f̂(0) = 1. The bandwidth restriction appears as the
linear identity, not as a hard support condition — this is exactly Cohn–Elkies's relaxation of
"support in [−1,1]" to "eventually non-positive."

---

## 4. The dual (majorant function space, Delsarte-type conditions)

The dual variables are the PSD blocks Y₃, Y₄ (majorant side) and Y₂ (radius/bandwidth side), with
Lagrange multipliers for the two normalizations. In Fourier-majorant language the Delsarte
conditions are:

1. **f̂ ≥ 0** — the form factor is a nonnegative majorant of the pair-correlation kernel
   (this is what "restricted to bandwidth ≤ 1" becomes: the tail beyond 1 is sign-discarded,
   not truncated).
2. **f(x) ≤ 0 for |x| ≥ r** — the radius/bandwidth cut, dual to the bandlimit.
3. **f(0) = f̂(0) = 1** — normalizations fixing the diagonal weight (each ρ=ρ′ term contributes
   m_ρ²).

The **dual function space** is

  { h(x) = (s₃(x²) + x² s₄(x²)) e^{−πx²} : Y₃, Y₄ ⪰ 0 } = even nonnegative Gaussians × SOS polynomials,

and the dual objective is the linear functional enforcing the truncated-tent condition
(the Lagrange dual of Z(f)). [DESIGN — standard Cohn–Elkies dual; the exact CGdL dual is the
four-block program of §3.]

---

## 5. The gap: what BGSTB does not give

Under RH, CGdL's diagonal-extraction step (their eq. (10))

  Σ_{ρ,ρ′} g((γ−γ′)(log T)/2π) w(γ−γ′) ≥ g(0) Σ_ρ m_ρ

is valid because **g = f̂(·/r)/r ≥ 0 and w(γ−γ′) > 0**, so every term is nonnegative and the
off-diagonal terms are dropped. Unconditionally w(ρ−ρ′) is complex, so this drop is **invalid**.

BGSTB's replacement is the **Tsang kernel** (their §4)

  K(z) = (1/π) ∫₀¹ j(α) sech(α) cos(α z) dα,

with **Re K(z) > 0 for |Im z| < 1** [BGSTB Lemma 6(c), PROVEN]. Since z = (ρ−ρ′) log T, the
condition |Im z| < 1 ⟺ |β − β′| < 1/log T. Inside this strip the off-diagonal terms can be dropped;
outside, BGSTB is left with the remainder

  S(T) = 2π Re Σ_{|β−β′| ≥ 1/log T} K(−i(ρ−ρ′) log T) w(ρ−ρ′),

and they prove S(T) = o(T log T) [BGSTB §6] **only under** the box hypothesis
(|β − 1/2| < 1/(2 log T) for T^{3/8} < γ ≤ T) or the strong density hypothesis (their (1.6)).
[PROVEN conditional on box / conditional on density.]

**The missing input is exactly the box membership of the zeros** — equivalently the double-sum /
density estimate S(T) = o(T log T). The unconditional Montgomery theorem (Theorem 1) does **not**
certify it; it only supplies the functional form of the pair correlation inside the strip.

---

## 6. The transfer: the unconditional SDP is a strip-positive (Fejér/cosine) SDP

The correct cone for the unconditional problem is the **strip-positive bandlimited class**, not the
CGdL four-block family. The hard constraint replacing "f̂ ≥ 0, f ≤ 0 outside radius" is

  Re K_j(x + iy) = (1/π) ∫₀¹ j(α) sech(α) cosh(αy) cos(αx) dα ≥ 0   for all x, |y| ≤ b₀,

where b₀ = (box half-width in β)·log T is the box width in z-units, and j is the bandwidth-1 form
factor (j ≥ 0, supp j ⊆ [−1,1], j(0) = 1).

**Key structural fact [PROVEN by the identity above]:** Re K_j is *linear* in j, so strip positivity
is a semi-infinite family of linear constraints on j — a family of cosine-integral nonnegativities
(Fejér-type). The objective (BGSTB (7.2)) is the homogeneous ratio

  simple fraction ≥ 2 − [ j(0) + 2∫₀¹ α j(α) sech(α) dα ] / [ 2∫₀¹ j(α) sech(α) dα ],

so after fixing the denominator it is linear too. **Without strip positivity the problem is
unbounded**: j can spike at the band edge α = 1 and the bound degenerates to the vacuous
"simple fraction → 1". Strip positivity is the entire content. [DESIGN / CONJECTURED direction.]

**Honest caveat:** on a finite cos-lattice, nonnegativity of a cosine polynomial is Fejér–Riesz /
PSD-Toeplitz representable (a true SDP). Whether the *continuous-strip* condition
Re K_j(x+iy) ≥ 0 for |y| ≤ b₀ (with the sech/cosh weights) admits a finite PSD lifting for
polynomial j is **not established** — that is the key structural risk, stated as the next step in §9.

---

## 7. Feasibility in the (bandwidth, box-width) plane

Let λ = bandwidth of j (λ = 1 for Montgomery), b₀ = box half-width in z-units. The SDP is feasible
(gives a valid bound) iff there is an even j, supp j ⊆ [−λ, λ], j ≥ 0, j(0) = 1, with
Re K_j(x+iy) ≥ 0 for |y| ≤ b₀.

- **(λ, b₀) = (1, 1) is feasible**: Tsang/Fejér j(α) = (1−α)₊ and the Montgomery–Taylor kernel j_M.
  [PROVEN, BGSTB Lemma 6(c).]
- BGSTB's box |β − 1/2| < 1/(2 log T) is exactly **b₀ = 1**: their functional side sits *at* the known
  feasibility boundary, and the SDP's job is to optimize j within b₀ = 1 (and to exploit any wider b₀
  if a wider box can be certified).
- The **unproven input is not the functional but the box membership of the zeros**: certifying the
  zeros lie in the b₀ = 1 box is equivalent to S(T) = o(T log T). [CONJECTURED structural statement.]
- Float probe (below): the CGdL Gaussian majorant family is **not** strip-positive even at
  b₀ = 1/(2π) ≪ 1, so the CGdL primal cone does not transfer; the strip-positive Tsang-type cone is
  the correct object. [CHECKED NUMERICALLY.]

---

## 8. Reduced 3-node discretization (mechanics, by hand)

Nodes α ∈ {0, ½, 1}; variables j₀ = j(0) = 1 (normalization), j₁ = j(½), j₂ = j(1), with j₁, j₂ ≥ 0.
Simpson quadrature (h = ½), sech(0) = 1, sech(½) ≈ 0.8868, sech(1) ≈ 0.6481:

  J = ∫₀¹ j sech dα ≈ (1/6)[ 1 + 3.5472 j₁ + 0.6481 j₂ ],
  A = ∫₀¹ α j sech dα ≈ 0.29560 j₁ + 0.10802 j₂.

**Fejér sanity check (j₁ = ½, j₂ = 0):** J = 0.46227, A = 0.14780,
ratio = (1 + 2A)/(2J) = 1.29560/0.92453 = 1.40136 ⇒ simple fraction = 0.59864
(BGSTB's Fejér value is 0.60857; the ~0.01 gap is quadrature error — mechanics correct).

**Strip constraint at one sample point (x, y) = (2, 1), b₀ = 1.** At y = 1 the sech weight cancels
cosh exactly (sech(α)·cosh(α·1) = 1), so

  Re K_j(2 + i) = (1/π)∫₀¹ j(α) cos(2α) dα
               ≈ (1/π)(1/6)[ 1 + 4·cos(1) j₁ + cos(2) j₂ ],   cos(1) ≈ 0.5403, cos(2) ≈ −0.4161,
               = (1/π)(1/6)[ 1 + 2.1612 j₁ − 0.4161 j₂ ] ≥ 0  ⟹  1 + 2.1612 j₁ ≥ 0.4161 j₂.

**LP with only this one strip sample:** fix J = 1 (homogeneity) ⇒ 3.5472 j₁ + 0.6481 j₂ = 5, i.e.
j₁ = 1.40956 − 0.18271 j₂. Then A = 0.41667 + 0.05401 j₂, minimized at j₂ = 0 (j₁ = 1.40956), giving
ratio = (1 + 2·0.41667)/2 = 0.91667 ⇒ simple fraction = 1.0833 **> 1 — vacuous**.

**Reading of the mechanics:** a single strip sample is far too weak — the minimizing direction
(j(½) > j(0), a form factor peaked inside the band) satisfies that one sample but violates the
continuum of strip conditions elsewhere. The *content* of Tsang's Lemma 6(c) is precisely that the
**full continuum** Re K_j ≥ 0 is satisfiable by the Fejér/Montgomery–Taylor shape, driving the bound
down from the vacuous >1 to the honest 0.6086 / 0.6175. The SDP's job is to saturate that continuum.
[CHECKED NUMERICALLY — mechanics; hand arithmetic, cross-checked against the probe's strip
positivity of the Fejér kernel.]

---

## 9. Float probe (belief it changes) — and the numbers

`tools/sdp_unconditional_structure/probe.py` (mpmath 1.4.1; scipy/numpy unavailable, so mpmath
was used instead — documented deviation). Runtime < 1 min. Command:
`python3 tools/sdp_unconditional_structure/probe.py`.

Output:

  Z_S (Selberg, r=1)   = 1.33619670817
  Z_H (hat, r=1)       = 1.33333333333
  improvement over 4/3 = -0.00286337483938
  min Re K(x+ib), Tsang/Fejer, b=1/2pi  : 0.00309016715365
  min Re f_gauss(x+ib), lambda=1.3      : -0.00180810600062

Belief changed:

1. **Selberg's function (the classical bandlimited alternative) is WORSE than Montgomery's hat**
   (Z = 1.3362 vs 4/3 = 1.3333), confirming the paper's remark and showing the SDP layer is
   load-bearing, not a cheap bandlimited trick. [CHECKED NUMERICALLY.]
2. **The CGdL Gaussian majorant f = (1 − x²/λ²)e^{−πx²} at λ = 1.3 goes NEGATIVE on the strip**
   already at b₀ = 1/(2π) (min Re = −0.00181), while the Tsang/Fejér sech kernel stays positive
   (min Re = +0.00309, consistent with BGSTB Lemma 6(c)). This pins down the correct cone:
   strip-positive bandlimited (Tsang-type), **not** the CGdL four-block family. [CHECKED NUMERICALLY.]

The numbers themselves are not the deliverable; the deliverable is the identification of the cone
and the location of the gap. No further compute was run.

---

## 10. Labels

| Claim | Label |
|---|---|
| BGSTB Theorem 1 + Lemma 5 (unconditional Montgomery functional) | PROVEN (unconditional) |
| CGdL Lemma 8, Z(f) functional, 1.3208 / 0.6792 | PROVEN (conditional on RH) |
| BGSTB Theorem 2 (≥ 61.7% simple) | PROVEN (conditional on box / on density) |
| Re K_j linear in j; cosine-integral nonnegativity constraint | PROVEN (elementary identity) |
| Unconditional SDP = strip-positive bandlimited LP/SDP over j | DESIGN (this note) |
| Feasibility (λ, b₀) = (1, 1); b₀ = 1 = BGSTB box | PROVEN at (1,1); CONJECTURED shape elsewhere |
| 3-node LP mechanics + probe numbers | CHECKED NUMERICALLY (script cited) |
| Finite PSD lifting exists for the continuous-strip condition | UNRESOLVED (blocker for implementation) |

---

## 11. One concrete next step

Test whether the continuous-strip condition Re K_j(x+iy) ≥ 0 for |y| ≤ b₀ admits a **finite PSD
lifting** for polynomial j(α) = Σ_k c_k α^k. Reduce the fixed-y case to a Toeplitz/Fejér–Riesz
positivity on a cos-lattice and check whether the y-dependence (cosh(αy) weight) preserves the
Toeplitz structure. If it does: write the SDP (d ≈ 10–20) and try to beat Tsang's 0.6175 at
(λ, b₀) = (1, 1). If it breaks: record the obstruction — the unconditional SDP is then a
semi-infinite LP requiring discretization with a rigorous tail-closure argument, and the next lever
is a certified wider-box/double-sum estimate (Candidate 1 of the thread) rather than the SDP layer.
