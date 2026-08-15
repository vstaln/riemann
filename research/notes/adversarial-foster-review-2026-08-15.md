# Adversarial referee review: foster-reactance (F = d/ds log Xi PR <=> RH)

Hostile blind referee. Attack: research/notes/foster-reactance-2026-08-15.md + tools/foster_check/.
Verdict: lemma VERIFIED (PROVEN); numeric check PARTIALLY VERIFIED (a_1..a_30, NOT a_40 as claimed);
f64 accuracy claims FALSE; control discriminator FIRES (not dead). Note's self-framing (equivalent-to-RH
restatement, finite check, no uniform control) is CORRECT and preserved.

## 1. Two-line lemma - VERIFIED (PROVEN), airtight
- F(s)=sum_j 2s/(s^2-s_j^2) over zero PAIRS (Hadamard, genus-1); F'(0)=sum_j -2/s_j^2=2*sum 1/g^2=0.04621=2b_1/b_0. CHECKED.
- (=>) RH: s_j=+-i*w; Re[2s/(s^2+w^2)] = 2*sigma(sigma^2+tau^2+w^2)/|s^2+w^2|^2 >= 0 iff sigma >= 0. Sum of nonneg >= 0. AIRTIGHT.
- (<=) zero at Re(s_k)=alpha>0: F = m/(s-s_k)+O(1), residue m = multiplicity > 0; at s = s_k-eps (0<eps<alpha, Re s > 0): F ~ -m/eps < 0. Sign correct, no off-by-one. AIRTIGHT.
- Corollary (Stieltjes/Foster): PROVEN classical. m_n = sum g^-2n-2 = Stieltjes seq of positive measure
  mu = sum g_j^-2 delta_{1/g_j^2} => all Hankel dets > 0 => all TRUE a_k > 0 (unconditional theorem).

## 2. Independent recomputation (my mpmath 220-500 digits, own CF recursion)
- From b.txt (the note's input: 18 sig figs ON DISK, not 400): a_1..a_21 > 0, then SPURIOUS NEGATIVES
  a_24=-12.19, a_25, a_27, a_28, a_32, a_33, a_38, a_39 < 0. 220-digit arithmetic does NOT fix it.
- From zeros file (33-digit zeros + analytic m_0 tail): ALL a_1..a_40 > 0 (reproduces /tmp/cf_hp2.py).
- The two routes agree in sign ONLY through a_20; a_24 flips sign between routes.
- Conditioning (measured): relative moment noise 1e-16 moves a_17 >10%; 1e-32 moves a_31; 1e-64 moves
  none to a_40. Zeros-route input profile (m_n ~ 1e-32, m_0 ~ 1.25e-5 tail err) certifies a_1..a_30.
  b_txt profile (5e-16) certifies only ~a_15. => a_1..a_30 > 0 CHECKED NUMERICALLY; a_31..a_40
  numerically UNCERTIFIED (needs ~1e-64 moments; available 1e-32), positive by theorem only.
- Note's label "a_1..a_40 all > 0 at 200-digit precision" is OVERSTATED and NOT reproducible from the
  checked-in b.txt. Also tools/cf_hp2 (cited in note) is NOT in the repo - found only in /tmp.

## 3. f64 claims in the note - FALSE
- main.rs f64 diverges from 200-digit already at a_12 (67.382807 vs 67.382779, err 3e-5) and a_15
  (0.226958 vs 0.227454, err 2e-3). "a_1..a_18 exact to ~1e-13" FALSE (off ~8 orders by a_12).
- f64 SIGN collapse at a_19 (main.rs a_19 = -0.039) is real and IS an artifact (my a_19 = +0.239).

## 4. Destructive control (RH-FALSE model) - discriminator FIRES, not dead
- Exact control: D_ctrl(z) = D(z)(1 - 2Re(1/w) z + z^2/|w|^2)/(1 + z/g_2^2), w = (alpha+21.1i)^2
  (exact polynomial division; b_0 unchanged; zero at Re = alpha > 0 => RH false).
- alpha=0.35: first non-positive a_12 = -9.09 (robust: two independent routes -9.11 / -9.09).
  alpha=0.50: a_11. alpha=0.05: a_15 = -7.7e-3. alpha=0.01: a_17. Violation index grows as alpha -> 0
  (matches note's continuity claim; near-line zeros evade ANY finite N).
- RH-TRUE side: no genuine negative a_k exists (theorem); b_txt-route negatives at a_24+ are input
  artifacts, not real coefficients.

## 5. What was NOT checked
- b_k tower correctness (taken as given; cross-validated m_0..m_8 vs zero-power sums, consistent).
- The >=30 digit details of a_31..a_40 (uncertifiable at available input precision).

## Verdict
VERIFIED (with documented precision limits): the two-line lemma is PROVEN and airtight; the finite
C-fraction check is certified numerically through a_30 only (a_31..a_40 positive by theorem, not by
the run as labeled); the planted RH-false control breaks the check at a_11..a_12 (discriminator alive
but finite); f64 accuracy ("1e-13 to a_18") and the "a_40 at 200 digits" labels are overstated and
should be corrected in the note. No weakening of the validator was performed.
