# Trace--energy envelope

This note supplies the finite-dimensional step used in §6 of
`JOINT_WINDOW_PROOF.md`; it is included here so that the numerical certificate
is not asked to certify an unstated sharp inequality.

Let `G` be an `m × m` positive-semidefinite matrix with unit diagonal. Write
its eigenvalues as `lambda_i >= 0`, so `sum lambda_i = m`, and put

```
E = tr(G-I)^2 = sum_i (lambda_i-1)^2,
D = tr Psi(G) = sum_i Psi(lambda_i),
Psi(t) = (t-1)^2       (0 <= t <= 2),
         2*t-3         (t >= 2).
```

The current Bellman application needs the following implication (with
`A=1.02129` and `m=183`): whenever `E+P >= A` and `P >= 0`,

```
D+P >= Phi_m(A),
Phi_m(E) = E                                      (0 <= E <= m/(m-1)),
           2*sqrt((m-1)E/m) - 1 + E/m              (E >= m/(m-1)).
```

## Derivation

Set `x_i = lambda_i-1`. Thus `x_i >= -1`, `sum x_i=0`, and
`sum x_i^2=E`. For `x <= 1`, `Psi(1+x)=x^2`; for `x > 1`,
`Psi(1+x)=2*x-1`. If every `x_i <= 1`, then `D=E`. Conversely, if some
`x_i>1`, Cauchy--Schwarz on the other `m-1` coordinates gives

```
E >= x_i^2 + x_i^2/(m-1) >= m/(m-1),
```

so this is exactly the point at which a second branch can occur.

Here is a direct proof of exactly that implication, without assuming a global
minimizer classification. Let `L={i:x_i>1}`, `k=|L|`,
`R=sum_{L} x_i`, and `Q=sum_{L} x_i^2`. Since the linear branch replaces
`x_i^2` by `2*x_i-1`,

```
D = E + 2*R - k - Q.
```

If `k=0`, then `D=E`. If `k>=2`, Cauchy on the `m-k` remaining entries gives
`E-Q >= R^2/(m-k)`, and hence

```
D >= 2*R-k+R^2/(m-k) >= k*m/(m-k) > 2.
```

For `A=1.02129`, this already exceeds `Phi_m(A)<2`. It remains to consider
`k=1`, writing the large coordinate as `r>1`. Cauchy gives
`r <= sqrt((m-1)E/m)`. Therefore

```
D >= E + 2*r - 1 - r^2.
```

The last correction is decreasing for `r>=1`, so for `E>=A` this is at least
`Phi_m(E) >= Phi_m(A)`. For `E<A`, the first Cauchy observation at the top
shows that `k<=1`; the available pressure `P>=A-E` and the monotonic decrease
of `Phi_m(E)-E` on the second branch give
`D+P >= Phi_m(A)`. (On the first branch `D=E` and the same inequality is
immediate.) This proves the required finite-block step for the value of `A`
used in the certificate. The function `Phi_m` is nondecreasing and 1-Lipschitz
on its two displayed branches.

For this repository, `m=183`, `A=577*(183-6)/100000=1.02129`, which is on the
second branch and yields the `B` printed in the certificate.
