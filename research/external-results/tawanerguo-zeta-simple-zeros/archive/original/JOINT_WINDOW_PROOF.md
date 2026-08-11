# A certified joint-window sharpening to 67.3101784%

## 1. Result

Let

\[
N=N(T,2T),\qquad S=N_0^s(T,2T).
\]

Starting from Anthropic's general-window form of Theorem D and the
stability-enhanced Gram-defect inequality developed in
`ainta/zeta-simple-zeros`, this note proves

\[
\boxed{
\liminf_{T\to\infty}\frac{S}{N}
\ge 0.6731017847214250187272737655\ldots .
}
\]

The new point is not another retuning of the Montgomery--Taylor kernel.
Instead, the analytic test window and the Gram-overlap correction are optimized
jointly.  The Montgomery--Taylor profile is optimal for the two-trace
functional alone, but it need not optimize the strengthened objective once the
geometry of the simple-zero Gram matrix is retained.

The certified profile is

\[
v_\alpha(s)=\cos(\alpha s),\qquad
\alpha=\frac{147}{100},\qquad |s|\le\frac12.
\]

It gives a slightly weaker two-trace baseline than
`alpha=sqrt(2)`, but a sufficiently stronger overlap inequality that the final
simple-zero proportion increases.

## 2. General cosine-window constant

For a nonnegative profile `v` on `[-1/2,1/2]`, Anthropic's scale-free
functional at bandwidth one is

\[
c_1(v)=
\frac{\left(\int v\right)^2}
{\int v^2+\iint |s-t|v(s)v(t)\,ds\,dt}.
\]

The two-trace simple-zero baseline is

\[
H(v)=2-\frac1{c_1(v)}.
\]

For `v_alpha(s)=cos(alpha s)`, put

\[
I_0=\int_{-1/2}^{1/2}\cos(\alpha s)\,ds
    =\frac{2\sin(\alpha/2)}{\alpha},
\]

\[
I_2=\int_{-1/2}^{1/2}\cos^2(\alpha s)\,ds
    =\frac12+\frac{\sin\alpha}{2\alpha}.
\]

If

\[
(Tv)(s)=\int_{-1/2}^{1/2}|s-t|v(t)\,dt,
\]

then `(Tv)''=2v`.  Evenness and the endpoint derivative determine

\[
T v_\alpha(s)=
-\frac{2}{\alpha^2}\cos(\alpha s)
+\frac{\sin(\alpha/2)}{\alpha}
+\frac{2\cos(\alpha/2)}{\alpha^2}.
\]

Consequently

\[
J_\alpha:=\iint |s-t|v_\alpha(s)v_\alpha(t)\,ds\,dt
=-\frac{2I_2}{\alpha^2}
+\left(
\frac{\sin(\alpha/2)}{\alpha}
+\frac{2\cos(\alpha/2)}{\alpha^2}
\right)I_0.
\]

At `alpha=147/100`,

\[
c_\alpha=\frac{I_0^2}{I_2+J_\alpha}
=0.7532722387479082089072381632\ldots,
\]

and hence

\[
H_\alpha=2-\frac1{c_\alpha}
=0.6724587094007293401705106878\ldots . \tag{2.1}
\]

For comparison, the Montgomery--Taylor profile gives
`0.6725007036794116...`; the baseline sacrifice is about
`4.20e-5`.

## 3. The new overlap kernel

The limiting normalized overlap kernel is the normalized Fourier transform of
`v_alpha`:

\[
k_\alpha(x)=
\frac{\displaystyle
\int_{-1/2}^{1/2}\cos(\alpha s)\cos(2\pi xs)\,ds}
{I_0}.
\]

Writing `sinc(z)=sin(z)/z`,

\[
k_\alpha(x)=
\frac{
\tfrac12\left[
\operatorname{sinc}(\pi x-\alpha/2)
+\operatorname{sinc}(\pi x+\alpha/2)
\right]}
{\operatorname{sinc}(\alpha/2)}. \tag{3.1}
\]

Put

\[
w_\alpha(x)=k_\alpha(x)^2.
\]

For retained central simple zeros at bounded normalized separation, the same
Gabor-overlap argument as in the source paper gives

\[
\langle v_\rho,v_{\rho'}\rangle
=k_\alpha(x_\rho-x_{\rho'})+o(1)
\]

uniformly.

## 4. Certified seven-point inequality

For six nonnegative consecutive gaps define

\[
\mathcal F_{6,\alpha}(g_1,\ldots,g_6)
:=\frac1{1920}\sum_{i=1}^6g_i
+\sum_{r=1}^6\frac{2}{7-r}
 \sum_{i=1}^{7-r}
 w_\alpha(g_i+\cdots+g_{i+r-1}). \tag{4.1}
\]

The supplied verifier proves

\[
\boxed{
\mathcal F_{6,\alpha}(g_1,\ldots,g_6)
\ge \frac{563}{100000}
}
\qquad(g_i\ge0). \tag{4.2}
\]

### 4.1 Rigorous kernel table

The table has mesh `1/4000`.  Every endpoint value of (3.1) is enclosed with
MPFR 4.2.2 at 256-bit precision and directed rounding.

The interpolation remainder is controlled without numerical differentiation.
Because `cos(alpha s)>0` on the support,

\[
|k_\alpha''(x)|
\le 4\pi^2
\frac{\int_{-1/2}^{1/2}s^2\cos(\alpha s)\,ds}{I_0}
\le \frac{\pi^2}{3I_0}<4. \tag{4.3}
\]

Indeed, `I0=sinc(0.735)>1-0.735^2/6>0.9` and `pi^2<10`.
Thus on a cell of width `h`, linear interpolation has error at most
`4h^2/8=h^2/2`.

The interval for `k_alpha` on each closed cell is converted into a rigorous
binary64 lower bound for `w_alpha`.

### 4.2 Exhaustive subdivision

The one-coordinate term

\[
U(g)=\frac{g}{1920}+\frac13w_\alpha(g)
\]

reduces every gap to two certified unions of cells:

\[
[3743,4968],\qquad [7004,41739].
\]

In real coordinates these are

\[
[0.93575,1.24225],\qquad[1.751,10.435].
\]

Their Cartesian sixth power gives 64 initial boxes.  On a box, every partial
sum of consecutive gaps is enclosed by integer cell indices.  A range-minimum
table supplies a lower bound for each occurrence of `w_alpha`; all floating
operations used by the branch-and-bound phase are widened outward with
`nextafter`.

The complete run records:

| field | value |
|---|---:|
| initial boxes | 64 |
| visited nodes | 81,269,558 |
| splits | 40,634,747 |
| pressure-pruned leaves | 2,951 |
| interval-pruned leaves | 40,631,860 |
| maximum depth | 71 |
| unresolved terminal cells | 0 |
| kernel-table SHA-256 | `13213b84960fa629db0eac3ed7891148066313cba84f4fa151cfcce749d8fc2c` |

The tree identity

\[
81{,}269{,}558-40{,}634{,}747
=2{,}951+40{,}631{,}860
=40{,}634{,}811
\]

checks that every leaf is accounted for.

## 5. From the local inequality to block energy

Let

\[
y_1<\cdots<y_m,
\qquad
E_m=2\sum_{1\le i<j\le m}w_\alpha(y_j-y_i).
\]

As in the preceding sharpening, sum (4.2) over all consecutive seven-point
windows.  If `a_j` is the number of such windows containing the gap
`y_{j+1}-y_j`, then

\[
E_m+P_m\ge\frac{563}{100000}(m-6),
\qquad
P_m=\frac1{1920}\sum_{j=1}^{m-1}a_j(y_{j+1}-y_j), \tag{5.1}
\]

and

\[
\sum_{j=1}^{m-1}a_j=6(m-6). \tag{5.2}
\]

Averaging over all `m` shifted consecutive block partitions therefore charges
a global gap by at most

\[
\frac{6(m-6)}{1920m}
=\frac{m-6}{320m}. \tag{5.3}
\]

## 6. Spectral conversion

For

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2,
\end{cases}
\qquad
\mathcal D(G)=\operatorname{tr}\Psi(G),
\]

the stability-enhanced rank--trace argument gives

\[
S\ge H_\alpha N+\mathcal D(M^\circ)-o(N). \tag{6.1}
\]

For an `m x m` positive-semidefinite unit-diagonal Gram matrix with

\[
E=\operatorname{tr}(G-I)^2
 =2\sum_{i<j}|G_{ij}|^2,
\]

the sharp trace-and-energy envelope is

\[
\mathcal D(G)\ge\Phi_m(E), \tag{6.2}
\]

where

\[
\Phi_m(E)=
\begin{cases}
E,&0\le E\le\dfrac{m}{m-1},\\[6pt]
2\sqrt{\dfrac{m-1}{m}E}-1+\dfrac Em,
&E\ge\dfrac{m}{m-1}.
\end{cases} \tag{6.3}
\]

The function `Phi_m` is nondecreasing and 1-Lipschitz.  Consequently, from
`E+P>=A`,

\[
\mathcal D(G)+P\ge\Phi_m(A). \tag{6.4}
\]

Choose

\[
m=187,
\qquad
A=\frac{563}{100000}(187-6)
 =\frac{101903}{100000}=1.01903.
\]

Then

\[
B:=\Phi_{187}(A)
=2\sqrt{\frac{9476979}{9350000}}
 -1+\frac{101903}{18700000}
=1.0189842020014185449\ldots . \tag{6.5}
\]

Pinching to the full blocks for each shift, applying (6.4), averaging the
shifts, and using that the total normalized zero interval has length
`N+o(N)` gives

\[
\mathcal D(M^\circ)
\ge \frac{B}{187}S
 -\frac{181}{59840}N-o(N). \tag{6.6}
\]

## 7. Final constant

Substituting (6.6) into (6.1),

\[
\left(1-\frac{B}{187}\right)S
\ge
\left(H_\alpha-\frac{181}{59840}\right)N-o(N).
\]

Therefore

\[
\boxed{
\liminf_{T\to\infty}\frac SN
\ge
\frac{H_\alpha-181/59840}{1-B/187}
=0.6731017847214250187272737655\ldots .
} \tag{7.1}
\]

This is `67.3101784721425...%`.

It improves the repository's committed `0.673008527927...` by
`0.00009325679...`, and improves the preceding certified sharpening
`0.673059279778...` by `0.00004250494...`.

## 8. Trust boundary

The only computer-assisted assertion is (4.2).  The proof from (4.2) to
(7.1) is analytic.  The verifier reconstructs every transcendental endpoint
from the formula; the binary table is included only for reproducibility and is
hash-checked.

This remains a research draft rather than an independently peer-reviewed or
formally verified theorem.  In particular, an external audit should check the
general-window import, the central-overlap asymptotics, and the finite
certificate on an independent implementation.
