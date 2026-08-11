# A global spectral dual for the simple-zero Gram defect

## 1. Motivation

The current proof chain first compresses a Gram block to its total pair energy,
then pinches the full Gram matrix into fixed-size blocks.  This loses two kinds
of information:

1. which overlaps share a vertex;
2. coherent overlap information across block boundaries.

The following exact Fenchel dual works directly on the full Gram matrix.  It
turns the spectral defect into a capacitated weighted-edge problem and removes
the need to commit to a block size at the matrix-inequality stage.

## 2. Exact trace Fenchel formula

Define

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

For every `t>=0`,

\[
\Psi(t)=\sup_{h\le2}
\left\{h(t-1)-\frac{h^2}{4}\right\}. \tag{2.1}
\]

Indeed, the maximizer is `h=2(t-1)` for `t<=2`, and `h=2` for `t>=2`.
Functional calculus and the trace conjugacy of spectral functions give the
matrix identity

\[
\boxed{
\operatorname{tr}\Psi(M)
=
\sup_{H=H^*,\ H\preceq2I}
\left[
\operatorname{tr}H(M-I)-\frac14\operatorname{tr}H^2
\right].
} \tag{2.2}
\]

The optimizer is `H=2(M-I)` on the spectral subspace `M<=2I` and is clipped
to `2I` above eigenvalue two.

## 3. Connection-Laplacian certificate

Let `M` be a positive-semidefinite unit-diagonal Gram matrix.  Choose any
undirected graph `E` on its indices and nonnegative edge variables `q_ij`.
Put

\[
a_{ij}=|M_{ij}|,
\qquad
\omega_{ij}=\frac{M_{ij}}{|M_{ij}|}
\]

when `M_ij` is nonzero.  Let `L(q)` be the Hermitian connection Laplacian
whose diagonal is

\[
d_i=\sum_{j:\{i,j\}\in E}q_{ij},
\]

and whose off-diagonal entries are

\[
L_{ij}=-q_{ij}\omega_{ij}.
\]

Each edge contributes a rank-one positive-semidefinite matrix, so
`L(q)>=0`.  Set

\[
S=\operatorname{diag}(\min(d_i,2)),
\qquad
H=S-L(q).
\]

Then

\[
2I-H=(2I-S)+L(q)\succeq0,
\]

so `H<=2I`.  Substitution into (2.2) gives

\[
\boxed{
\operatorname{tr}\Psi(M)
\ge
2\sum_{\{i,j\}\in E}q_{ij}a_{ij}
-\frac12\sum_{\{i,j\}\in E}q_{ij}^2
-\frac14\sum_i(d_i-2)_+^2.
} \tag{3.1}
\]

This is already a global certificate: edges may cross arbitrary former block
boundaries.

## 4. Hard-capacity form

If the edge variables obey

\[
\sum_{j:\{i,j\}\in E}q_{ij}\le2
\qquad\text{for every }i,
\]

then the last term vanishes:

\[
\boxed{
\operatorname{tr}\Psi(M)
\ge
\max_{\substack{q_{ij}\ge0\\ \sum_jq_{ij}\le2}}
\sum_{\{i,j\}\in E}
\left(2q_{ij}a_{ij}-\frac12q_{ij}^2\right).
} \tag{4.1}
\]

This is a concave capacitated fractional matching problem.  Its dual is

\[
\min_{\lambda_i\ge0}
\left[
2\sum_i\lambda_i
+\frac12\sum_{\{i,j\}\in E}
(2a_{ij}-\lambda_i-\lambda_j)_+^2
\right]. \tag{4.2}
\]

Thus both lower witnesses (`q`) and independent upper checks (`lambda`) are
available.

### Relation to the earlier graph lemma

If `E` has maximum degree two and one chooses `q_ij=a_ij`, then every vertex
has capacity at most two because `a_ij<=1`.  Equation (4.1) becomes

\[
\operatorname{tr}\Psi(M)
\ge\frac32\sum_{\{i,j\}\in E}|M_{ij}|^2,
\]

which is exactly the coefficient used by the earlier three-point argument.
Hence (4.1) strictly generalizes that lemma rather than introducing an
unrelated device.

For a matching, `q_ij=2a_ij` is feasible and gives the exact two-by-two value
`2a_ij^2` on every selected edge.

## 5. An explicit capacity-normalized witness

For a chosen finite-range graph, define

\[
A_i=\sum_{j:\{i,j\}\in E}a_{ij},
\qquad
D_{ij}=\max(1,A_i,A_j),
\]

and set

\[
q_{ij}=\frac{2a_{ij}}{D_{ij}}. \tag{5.1}
\]

This is automatically feasible, because

\[
\sum_jq_{ij}
\le
\frac{2A_i}{\max(1,A_i)}\le2.
\]

Therefore

\[
\boxed{
\operatorname{tr}\Psi(M)
\ge
\sum_{\{i,j\}\in E}
2a_{ij}^2\frac{2D_{ij}-1}{D_{ij}^2}.
} \tag{5.2}
\]

In a low-overlap configuration `A_i<1`, this recovers the entire selected pair
energy `2 sum a_ij^2`.  In a cluster, the normalization automatically lowers
edge variables rather than allowing a large spectral spike to destroy a
trace-energy estimate.

## 6. Application to zeta-zero atoms

Take vertices to be the retained central simple zeros in increasing order and
let `E_R` join pairs at index distance at most `R`.  On bounded normalized
separations,

\[
a_{ij}=|k(x_i-x_j)|+o(1).
\]

Equation (5.2) then produces a translation-invariant finite-range potential in
the consecutive gaps.  Unlike fixed-block pinching, every overlap is charged
through a globally capacity-consistent witness.

The remaining problem is no longer a spectral problem.  It is a one-dimensional
thermodynamic ground-state problem:

\[
\inf_{(g_i)}
\liminf_{n\to\infty}
\frac1n
\left(
J_R(g_1,\ldots,g_n)+\beta\sum_{i=1}^ng_i
\right). \tag{6.1}
\]

Floating-point reconnaissance indicates that the adverse configurations are
not uniform lattices.  They are dimerized patterns whose short and long gaps
track different zeros of the overlap kernel.  This explains why merely
tightening one six-dimensional pointwise minimum gives diminishing returns.

## 7. How to certify the thermodynamic bound without another local minimum

For a finite-range potential `V`, a bounded function `U` of the boundary state
is a Bellman subaction if

\[
V(g_i,\ldots,g_{i+R-1})+eta g_i
+U(g_{i+1},\ldots,g_{i+R-1})
-U(g_i,\ldots,g_{i+R-2})
\ge C. \tag{7.1}
\]

Summing (7.1) telescopes the `U` terms and proves an average lower bound `C`
for every infinite or long finite configuration.  Crucially, individual
windows may lie below `C`; only globally compatible sequences are constrained.
This is precisely the information discarded by pointwise branch-and-bound.

A concrete rigorous workflow is:

1. choose `R` and the capacity-normalized witness (5.1), or solve the local
   fractional-matching dual;
2. discretize the boundary state and solve a linear program for a
   piecewise-affine subaction `U`;
3. lift the discrete solution to interval boxes;
4. certify (7.1) with directed rounding and adaptive subdivision;
5. optimize the test window and the pressure parameter jointly.

This route attacks the global incompatibility of near-zero pair distances,
rather than extracting another decimal from a single local minimizer.

## 8. Status

Equations (2.2), (3.1), (4.1), and (5.2) are analytic theorems.  Their
conversion into a better zeta-zero proportion than the certified
`67.3101784%` result has not yet been completed.  Numerical experiments are
only reconnaissance; no thermodynamic constant from (6.1) should be quoted as
a theorem until a Bellman/interval certificate is produced.
