# Deeper sharpening of the simple zeta-zero bound

This research bundle contains two advances over the preceding
`67.3059279%` sharpening.

## Certified result

`JOINT_WINDOW_PROOF.md` proves, subject to the imported analytic framework,

\[
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge 0.6731017847214250187\ldots .
\]

The central conceptual change is to optimize the analytic cosine window and
the Gram-overlap correction jointly.  The certified window is
`v(s)=cos(1.47 s)`.

Reproduction files:

- `tools/generate_joint_kernel_table.py`
- `tools/verify_joint_seven.cpp`
- `tools/compute_joint_bound.py`
- `data/cos147-kernel.bin`
- `certificate/joint-window-seven-point.txt`
- `certificate/joint-window-boxes.txt`
- `certificate/bound-evaluation.txt`

Compile and run one certificate box with, for example:

```bash
g++ -O3 -std=c++20 -frounding-math -ffp-contract=off \
  tools/verify_joint_seven.cpp -o /tmp/verify_joint_seven
/tmp/verify_joint_seven data/cos147-kernel.bin 22
```

Run all box codes `0,...,63`; every invocation must return `verified=true`.
Regenerate the table with:

```bash
python tools/generate_joint_kernel_table.py \
  --output /tmp/cos147-kernel.bin
cmp /tmp/cos147-kernel.bin data/cos147-kernel.bin
```

## Structural next step

`GLOBAL_SPECTRAL_DUAL.md` derives an exact Fenchel representation of the Gram
defect and a global capacitated-matching certificate.  This removes fixed block
pinching at the matrix-inequality stage.  It also specifies a Bellman-subaction
program for certifying the thermodynamic ground state, which is the main route
toward a materially larger improvement.

## Status

The finite seven-point inequality is exhaustively interval-certified.  The
mathematical manuscript and the new global framework have not yet undergone
independent peer review or formal verification.
