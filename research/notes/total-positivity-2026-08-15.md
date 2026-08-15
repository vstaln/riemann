# Total positivity of the moment Hankel matrix (b_{i+j}) — INVERSION report

Lever g0-0/g3-0 (harvest): "prove TP of (b_{i+j}) via Cauchy–Binet, then Edrei–Thoma ⟹ real zeros."
VERDICT: the lever as briefed points the WRONG WAY — PROVEN and confirmed numerically.
RH ⟹ (b_{i+j}) is NOT totally positive; the true structure is an ALTERNATING Hankel signature
sign det(b_{i_a+j_b}) = (−1)^{r(r−1)/2} = the Turán/Newton family (wave8d's lever). Inversion
delivered: a new cheap discriminator — the planted control breaks the alternation at D_4.

Notation: Xi(t)=ξ(1/2+it)=Σ(−1)^k b_k t^{2k}, b_k=M_k/(2k)!, M_k=2∫_0^∞Φ(u)u^{2k}du,
Φ(u)=2Σ(2π²n⁴e^{9u/2}−3πn²e^{5u/2})e^{−πn²e^{2u}}>0 on (0,∞) (PROVEN: every term >0 for u>0;
matches wave8d's corrected classical Φ). F(z)=Σb_kz^k; Xi(t)=F(−t²); RH ⟺ F zeros all real
negative (PROVEN, exact; b_k = true Taylor coeffs, b_0=ξ(1/2) to 1e-11, b_10 matches wave8d-run5).

## 1. Exact theorem statements (epistemic core)
- ASW–Edrei (Aissen–Schoenberg–Whitney 1952; Edrei 1953; Karlin, Total Positivity 1968 v.2 ch.8):
  a_k≥0 is PF∞ (TOEPLITZ (a_{j−i}) TP) iff F(z)=Σa_kz^k = C e^{γz} z^m Π(1+α_jz)/Π(1−β_jz),
  γ,α_j,β_j≥0, Σ(α_j+β_j)<∞, m∈{0,1}. F entire (no β_j) ⟹ F = C e^{γz}z^mΠ(1+α_jz) — LP class,
  all zeros real ≤0. PROVEN (literature, cited). Growth needed: Σα_j<∞ (auto here: Σ1/γ²<∞).
  This is a TOEPLITZ theorem — the brief's "Hankel TP ⟹ negative real zeros" is NOT this theorem.
- TRUE Hankel-TP fact: b_k=∫x^kdη, η≥0 ⟹ (b_{i+j}) TP (PROVEN §2), and F(z)=Σb_kz^k has all
  zeros REAL but POSITIVE (PROVEN: F=∫dη(x)/(1−xz); Σw_j/(x−a_j), w_j,a_j>0 has zeros interlacing
  the poles, hence real). WRONG sign for RH — moment-Hankel-TP pushes zeros to the +axis.
- Correct classical link (PROVEN: PF∞ ⟹ alternating Hankel minors, two-sided Toeplitz +
  row-reversal sign): b_k≥0, F∈LP* ⟹ det(b_{i_a+j_b}) has sign (−1)^{r(r−1)/2}. Symbolic check:
  b_k=1/k! (e^z): D2<0,D3<0 ✓; b=(1,a+b,ab): D2<0 ✓.
- Necessary condition (PROVEN, Newton): RH ⟹ b_k=b_0e_k(1/γ²), e_k²≥e_{k−1}e_{k+1}(k+1)/k ⟹
  T_k:=b_k²−b_{k−1}b_{k+1}>0 ∀k (Turán). Any T_k<0 = unconditional DISPROOF of RH → escalate.

## 2. Cauchy–Binet — VERIFIED, exponent structure correct, not pointwise
det(M_{i_a+j_b})=∫det(u_b^{i_a+j_b})Πdη; key identity (PROVEN): det(u_b^{i_a+j_b})=(Π_b u_b^{j_b})det(u_b^{i_a})
— no off-by-one — but det(u_b^{i_a})=s_μ(u)·Vandermonde(u) (Schur) changes sign for unsorted u ⟹
raw integrand NOT ≥0 on the whole cube. Correct route = Andreief:
det(M_{i_a+j_b})=(1/r!)∫det(u_b^{i_a})det(u_b^{j_b})Πdη ≥ 0 (symmetric, ≥0 on the simplex).
⟹ (M_{i+j}) TP for η≥0 (M_k IS a moment seq: M_k=∫v^k Φ(√v)v^{−1/2}dv). PROVEN.

## 3. THE INVERSION (PROVEN) — where the lever dies
b_k=M_k/(2k)!: the (2(i+j))! is a factorial-of-sum, NOT a diagonal scaling ((2i)!(2j)!≠(2(i+j))!),
so TP of (M) does NOT transfer to (b). Worse: RH ⟹ T_k>0 ⟹ overlapping 2×2 Hankel minors
det[[b_{k−1},b_k],[b_k,b_{k+1}]]=−T_k<0 and D_2=b_0b_2−b_1²=−T_1<0. So (b_{i+j}) is NOT TP under
RH — proving Hankel-TP provably contradicts the conclusion. Lever must be INVERTED to
"RH ⟹ Hankel minors alternate (−1)^{r(r−1)/2}" (Turán/Newton). Growth is not the failure
point: F is entire of order 1/2 in z, Σ1/γ²<∞ — Edrei hypotheses auto-satisfied; the SIGN kills it.

## 4. Rust probe (f64, 0.09s; tools/tp_hankel_probe/, output total-positivity-2026-08-15.out)
Real b_k from Φ (Simpson 2^18 on [0,3]; b_0=0.49712077819 ✓ vs ξ(1/2), b_10=5.62286e-25 ✓ vs
wave8d-run5; rel err ~1e-11, margins orders above). CHECKED NUMERICALLY:
- REAL: T_k>0 k=1..15 (min t_k·(k+1)=1.0696 ≥1, margin 7%); D_n n=1..8 signs −,−,+,+,−,−,+,+ =
  EXACTLY (−1)^{n(n+1)/2}, log10|D_n| ∈ [−4.2,−186.5] — alternation confirmed, TP refuted.
- CONTROL all-real (15 γ's): identical alternation (machinery validated).
- CONTROL planted (γ_2→0.35±21.1i): D_4 SIGN FLIP (−, expected +, |D_4|~1e-50) — breaks
  alternation ⟹ discriminator FIRES at n=4. T_k>0 still holds for planted (matches wave8d:
  T_k does not fire; L_5(0)=−9.47e-9 is wave8d's detector).
- Wave8d's real-case T_k table (INCOMPLETE there) is now filled for k=1..15: no failure.

## 5. Forecast + inversion
Forecast (wrong-way, per campaign): "Hankel TP of (b) ⟹ RH". Inversion (what checks support):
RH forces Hankel NON-TP with exact alternating signature; live objects: (i) T_k>0 ∀k (finish
real-case table k≤1000 — cheap, any fail = RH disproof → escalate), (ii) NEW: the D_n
alternation as an independent RH-false detector (fires on planted at n=4, unlike Turán).
CONJECTURED: real-case alternation holds ∀n (it is a PROVEN consequence of RH, so its failure
would be an RH disproof; its holding is only consistency). Next: extend probe to n≤12 / k≤24
and to the stronger beta=5.0 planted control (wave8d control_far).
