# Adversarial audit — F_T recertification (replaced-mode) claim (2026-08-24)

**Status of this audit:** read-only adversarial pass over the fresh claim
"span-one pairs REPLACED by q_i terms, verified=true at eps=0.0070, bound
0.6729663177639583 (m=151)". All claims labeled. Author: diagnose subagent.

## Target claim under attack
corrected F_T (span-one pairs removed, q_i terms kept): verifier verified=true at
eps=0.0070 for alpha=1.4263026187858052, lambda=1.351623997475116,
raw_p=[895.6,1151.7,952.6,952.6,1151.7,895.6],
raw_q=[0.331829,0.323062,0.343351,0.343351,0.323062,0.331829]; hence
N0(T)/N(T) >= 0.6729663177639583 (m=151).

## Surface 1 — VERIFY_SPAN1_MODE patch (4 insertions)
Code (git diff HEAD, lines 498-501):
```python
mode = os.environ.get("VERIFY_SPAN1_MODE", "added")
w_uniform = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
if mode == "replaced":
    w_uniform = {(i, j): v for (i, j), v in w_uniform.items() if j - i >= 2}
print(f"span1_mode={mode}")
```
- Removes exactly the six span-one pairs: filter j-i>=2 drops (0,1),(1,2),(2,3),(3,4),
  (4,5),(5,6). Matches Tawan F_T (kSpanRationals[1]=0, span 2..6); the ledger identity
  F_V-F_T=(1/3)*sum w(g_i) (each dropped span-one pair weight 2/(7-1)=1/3 -> (1/3)w(g_i)).
  [PROVEN]
- No silent fallback: print echoes the ACTUAL mode var; a typo falls to "added" (F_V) but
  logs the typo, not "replaced". Recorded run sets VERIFY_SPAN1_MODE=replaced. No path
  where logs say replaced but F_V runs. [PROVEN]
- q_i*w(g_i) nearest term is unconditional on mode, so F_T = F_V minus six span-one
  terms. "Replaced" is a misnomer (pair dropped, q_i retained) but code implements F_T
  correctly. [PROVEN]

**Surface 1: no patch bug.**

## Surface 2 — pruning soundness in replaced mode
- One-body prune uses pressure_coeffs/nearest_coeffs (mode-independent), a rigorous lower
  bound; cells with one_body>=target are dropped only when the true F_T>=target already.
  Cannot cut a violating cell; keeps all could-still-violate cells. [PROVEN]
- Pressure prune (sum(part[0])>=cutoff_cells) sound iff min_i p_i >= 1/3000.
  min_i p_i = lam*895.6/1920000 ≈ 6.305e-4 > 3.333e-4. [PROVEN mpmath]
- Unresolved terminal cell returns verified=False (terminal-cell) — cannot silently report
  true. [PROVEN]

**Surface 2: pruning sound; cannot manufacture verified=true.**

## Surface 3 — headline recomputation (mpmath dps=40)
H(alpha)=H_cos=2-1/c = 0.6724988031484523793... (matches claim H). [CHECKED NUMERICALLY]
Phi_m(A): A=eps*(m-6); if A<=m/(m-1): B=A else 2*sqrt((m-1)A/m)-1+A/m. tau=psum*(m-6)/m.
bound=(H-tau)/(1-B/m).

| psum | bound @ m=151 | global max [40,5000] |
|---|---|---|
| lam*sum(raw_p)/1920000 = 0.0042236841979 (CLAIM's stated formula) | 0.67296645387858 | m=151 |
| lam/320 = 0.0042238249921 (sum raw_p rounded to 6000) | 0.6729663177639585 | m=151 |

- Claim's 0.6729663177639583 does NOT reproduce under its own stated formula
  psum=lam*sum(raw_p)/1920000 (gives 0.67296645387858); it matches exactly psum=lam/320
  (sum raw_p=6000; required psum = 0.00422382499210995 = lam/320 exactly). [PROVEN]
- Functional's true linear total = lam*5999.8/1920000 (sum raw_p=5999.8), giving true
  bound 0.67296645387858 — HIGHER. Claim's published value uses larger psum (lam/320),
  hence SMALLER (conservative) bound. Sound understatement, but contradicts its own
  formula; 1.36e-7 low. [PROVEN]
- m>400 growth: NONE. Global max over [40,5000] at m=151 (both conventions); best beyond
  400 is m=401 at 0.6722415. B/m@151=0.0067217 (denominator ~0.99328>0). [PROVEN]

**Surface 3: NUMBER_WRONG (internal inconsistency).** Correct per stated formula:
0.67296645387858; published 0.6729663177639583 follows only from psum=lam/320.

## Surface 4 — H cross-check
H(1.4263026187858052)=0.6724988031484523793... matches claim (12 digits); consistent
with anchors H(1.49)=0.6724218860964 and cosine-optimal H max 0.6725007036794.
[CHECKED NUMERICALLY] Correct.

## FINAL VERDICT: NUMBER_WRONG (headline bound does not follow from its own stated formula)
The replaced-mode machinery is sound (patch removes exactly the six span-one pairs, no
misleading fallback, pruning cannot manufacture verified=true; verified=true at eps=0.0070
is the claimed F_T floor, NOT independently re-run — multi-hour). H correct; m=151 is the
global max; no m>400 growth. Single defect: stated bound 0.6729663177639583 reproduces
only under psum=lam/320 (sum raw_p rounded to 6000), NOT under the claim's own formula
psum=lam*sum(raw_p)/1920000, which yields 0.67296645387858 (+1.36e-7). Published value is
a conservative (sound, safe) understatement, but stated formula and number are mutually
inconsistent. Correct value per stated formula: 0.67296645387858 (m=151).

## Honesty / status labels
- Patch correctness, pruning soundness, pressure-min, H, m=151 argmax, m>400 non-growth,
  psum round-trip: PROVEN (code / mpmath dps=40).
- "verified=true at eps=0.0070" (F_T floor itself): NOT independently re-run; taken as
  claimed, not contradicted by any static read.
- psum ambiguity: certified functional's true linear total = lam*5999.8/1920000; lam/320
  is the prior record's stated convention and is the larger (conservative) value.
