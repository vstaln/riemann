# arXiv:2608.11520 — contour Hankel dynamics triage

Date screened: 2026-08-18
Source: https://arxiv.org/abs/2608.11520
Title: *Contour Hankel dynamics and indicator fields for the Riemann Xi-function*

## Status

**CLOSED — RH EQUIVALENCE / CONSISTENCY FORMULATION, not a new one-way condition.**

The paper defines contour moments of `Xi'/Xi` and finite Hankel matrices. For a
conjugation-compatible contour, its Theorem 3.4 gives the exact inertia

`In(H_m) = (r_0+c, c, m-r)`

once the matrix order is at least the number of distinct coordinate nodes: every real node
contributes positive inertia, and every nonreal conjugate pair contributes one positive and one
negative direction. Therefore PSD is equivalent to absence of nonreal enclosed pairs.

Corollary 3.7 explicitly states that PSD for every real-centered disk and every admissible
matrix order is equivalent to RH. The paper's Remark 3.8 explicitly says that proving this
positivity from analytic/arithmetic structure without prior zero information remains unresolved.
The moving-contour flow and rank-two crossing impulses are a useful diagnostic/reconstruction
framework, but they recover zero locations from `Xi'/Xi`; they do not supply the missing
unconditional positivity theorem.

## RH-false control

A Davenport–Heilbronn or planted conjugate pair produces the predicted rank-two indefinite
inertia by the paper's own theorem. Thus the control fires, but only because the criterion is
an RH equivalence. A finite contour misses zeros outside its disk, so no fixed finite scan can
be promoted to RH.

## Decision

Do not fund a new Rust implementation of the paper's quadrature or inertia: the load-bearing
implication and the unresolved step are already stated exactly in the source, and a numerical
reproduction would be consistency evidence only. Register it in the closure DAG as an
independent confirmation of the Hankel/zero-location equivalence trap. The proportion certificate
remains untouched and is not RH evidence.
