# Gravity one-shot ideas — first adversarial triage (2026-08-18)

## Status

**INCONCLUSIVE overall; two ideas have immediate structural problems, one remains a possible line.**
These are direct-RH ideas only. The certified proportion record is not RH evidence.

## 1. Prime-resolvent accretivity — test first

Gravity proposed a uniform positive spectral/accretivity gap built from the prime sum
`Re sum_{p<=X} (log p) p^(-sigma-it)` for sigma in (1/2,1).

Immediate load-bearing concern: Lambda(p)>=0 does not make this phase sum nonnegative when
`t != 0`; each term contains `cos(t log p)`. Absolute convergence of the Euler log derivative
also begins at sigma>1, not throughout the claimed half-plane. A Rust sieve/probe will search for
negative real prime sums on the zeta-side itself. If found, it refutes this proposed sufficient
condition as stated, not RH.

Label before probe: **CONJECTURED**.

## 2. Vertical Hamburger moments

For a fixed real window, the proposed measure
`dmu(t)=|zeta(1/2+it)|^2 exp(-(t-T)^2/H^2) dt` is nonnegative. Its Hankel moment matrices are
therefore positive semidefinite by
`c^T H c = integral |sum c_j (t-T)^j|^2 dmu >= 0`.

Thus positive Hankel minors cannot distinguish RH from an RH-false model unless the object is
changed to include a signed/off-line-sensitive measure. A claim that Davenport-Heilbronn gives
negative minors for this exact positive energy measure is structurally suspect.
Label: **ABANDONED as stated**; possible replacement would need a signed Weil/de Branges form.

## 3. de Branges phase velocity

`E(z)=xi(1/2-iz)-i xi'(1/2-iz)` is a genuine structural object. Hermite-Biehler theory makes
boundary phase monotonicity relevant, but `theta'(t)>0` on the real boundary alone may be an
RH-equivalent condition or only necessary. It survives as **INCONCLUSIVE**, pending a lemma that
turns a strictly verifiable inequality into RH without simply assuming the Hermite-Biehler
hypothesis. The required control is Davenport-Heilbronn with a certified phase defect.

## Next action

Run the Rust prime-phase falsification probe. If it finds negative values for zeta's own prime
sum, close Gravity idea 1 and focus the next cheap work on whether phase velocity has a genuinely
one-way formulation.

## Probe result — prime-resolvent line

Rust `tools/gravity-probe` scanned the exact finite prime phase sum
`Re sum_{p<=X} log(p) p^(-sigma-it)`:

```text
X=50000, sigma=.75, t in [0,1000], step=.5
min = -14.8133131654325911 at t=1
```

The negative sign persists on the same X/t grid at sigma=.51 (`-173.010166...`), sigma=.75
(`-14.813313...`), and sigma=.99 (`-2.381127...`). This is **CHECKED NUMERICALLY** and
refutes the proposed implication `Lambda(p)>=0 => phase accretivity` for the zeta-side prime
sum. It does not refute RH and does not rule out a different resolvent inequality.

Decision: **ABANDONED as stated**. The phase-velocity line remains the only Gravity survivor,
label **INCONCLUSIVE** pending a one-way lemma and DH phase-defect control.
