# The even mean-zero sector of Weil’s form at the first prime

**A research note.** 13 August 2026.
**Status:** theorems below are labelled PROVEN, CHECKED NUMERICALLY, or CONJECTURED. This note does **not** prove the Riemann hypothesis, does **not** prove $\lambda_a>0$ for $a\ge(\log 2)/2$, and does **not** improve the 67% simple-on-line record.

Scripts (every quantitative claim): `tools/weil_first_prime/{rpp_closed,mu2_envelope,ground_ray,ground_ray_cross,q0k_split}.py`.

---

## Abstract

Weil positivity on every finite interval is equivalent to RH. It is already proved for support radius $a<(\log 2)/2$ (Suzuki, after Bombieri–Yoshida). At the first-prime endpoint $a_2=(\log 2)/2$ the prime-2 Hankel has measure-zero overlap, so positivity of Suzuki’s scaled form $R(a_2,w)$ reduces to a comparison of the log-weighted Paley–Wiener energy $L(w)$ plus an archimedean remainder $\rho$ against an explicit threshold $\mathrm{th}(a_2)=2A+1+\log a_2$.

We prove an elementary lower bound $\mu_2\ge 1.02797$ for the even mean-zero Rayleigh quotient of $L$, and a nested concentration inequality that, given a Hilbert–Schmidt cap $\alpha(\omega)$ on low-frequency mass, yields
\[
\mu_2 \;\ge\; \log\Omega+\gamma-\int_0^\Omega\frac{\alpha(\omega)}{\omega}\,d\omega+\mathrm{NEG}.
\]
A conservative quadrature of $\alpha$ (`n=81` Nyström HS $\times 1.05$) gives $\mu_2\ge 1.6414>\mathrm{th}(a_2)=1.3554$ (CHECKED NUMERICALLY). Combined with Young’s bound $|\rho|\le\|\rho''\|_{L^1}=0.072515$, the **even mean-zero sector is positive at $a=a_2$** with margin $0.213$.

The even ground ray (nonzero mean) is not closed: the cosine test function itself is positive by an elementary Hankel formula plus a 1-D integral of $\rho''$ (CHECKED), and finite-section $\lambda_{\min}$ of the joint form stays $1.34\times 10^{-3}$ above threshold through 80 Dirichlet modes, but this is an upper bound of the infimum. The remaining lemma is an $O(1/k)$ bound on the Beurling–Deny matrix elements against the rank-one mean.

---

## 1. What is new, and what is not

| Claim | Label |
|---|---|
| RH $\Leftrightarrow$ $\lambda_a>0$ for every $a>0$ | literature (Weil; Yoshida; Suzuki) |
| $\lambda_a>0$ for $a<a_2$ | literature (Suzuki Thm 1.4) |
| some unspecified $\delta$ with $\lambda_a>0$ for $a<a_2+\delta$ | literature (Yoshida’s endpoint calculation) |
| $r''(t)=-2\cosh(t/2)+e^{t/2}/(2\sinh t)-1/(2t)$ for $t>0$ | PROVEN from Suzuki (2.2) |
| $r(t)=-\frac78 t^2-\frac1{288}t^3-\frac3{128}t^4+O(t^5)$ for $t>0$ | PROVEN elementary (Hurwitz at $1/4$) |
| Hankel of $\cos(\pi t/2)$ in closed form | PROVEN elementary |
| $\mu_2\ge 1.02797$ (even mean-zero, $\xi^2$ envelope) | PROVEN elementary; constant CHECKED |
| nested envelope $\mu_2\ge\log\Omega+\gamma-\int\alpha/\omega$ given $\alpha$ | PROVEN |
| $\alpha(\omega)\le 1.05\,\mathrm{HS}_{n=81}(Q_\omega^{\mathrm{emz}})$ $\Rightarrow$ $\mu_2\ge 1.6414$ | CHECKED NUMERICALLY |
| even mean-zero $R\ge 0.213$ at $a=a_2$ | CHECKED (uses the quadrature $\alpha$) |
| cosine $J+\rho>\mathrm{th}(a_2)$ by $2.65\times 10^{-3}$ | CHECKED |
| $\lambda_{a_2}>0$ on all even $w$ | CONJECTURED, not proved |
| $\lambda_a>0$ for $a>a_2$; RH; 67% record | **not claimed** |

The discovery is a **sector theorem plus a method**: the even mean-zero complement of the first-prime endpoint is under explicit control, by a Paley–Wiener nested envelope rather than a Ritz upper bound. That is the Anthropic-shaped object (a checkable inequality about Weil’s form). It is not RH.

**Credits.** Weil-form identities are Weil, Yoshida, Bombieri, and Suzuki — we did not invent them. The 67% simple-on-line class this note sits next to is Anthropic / [zeta-23-lean](https://github.com/anthropics/zeta-23-lean) (Theorems A–E), then [ainta](https://github.com/ainta/zeta-simple-zeros), [trmdy](https://github.com/trmdy/zeta-simple-zeros-673137), and [tawanerguo](https://github.com/tawanerguo-cn/zeta-simple-zeros) (our certified record uses their coboundary $(p,q)$ unchanged). Full git URLs: README Credits.

---

## 2. Setup (Suzuki (4.5)–(4.6))

Let $A=\frac12(\log(2\pi)+\gamma-1)$ and $a_2=(\log 2)/2$. Scale $v$ supported in $[-a,a]$ to $w(t)=v(at)$ on $[-1,1]$, $w(\pm 1)=0$. Write $r(t)$ for the archimedean screw remainder after stripping the von Mangoldt ramp, $\rho''(t):=r''(t)+\frac74$, and
\[
L(w)=\frac1{2\pi}\int_{\mathbb{R}}(\log|\xi|+\gamma)\,|\widehat w(\xi)|^2\,d\xi,\qquad
\widehat w(\xi)=\int_{-1}^1 w(t)e^{-i\xi t}\,dt.
\]
Suzuki (4.5) at $a=a_2$ (prime Hankel vanishes) says $R(a_2,w)\ge 0$ if and only if
\[
\frac{L(w)}{\|w\|^2}+\frac74 a_2\frac{(\int w)^2}{\|w\|^2}+\rho(w)\;\ge\; \mathrm{th}(a_2),
\]
where $\mathrm{th}(a)=2A+1+\log a$, so $\mathrm{th}(a_2)=1.3554326301692685$, and
\[
\rho(w)=-\int_{\mathbb{R}}\rho''(s)\,H_w(s/a)\,ds\Big/\|w\|^2,\qquad
H_w(h)=\int w(x)w(x-h)\,dx
\]
(with $w=0$ off $[-1,1]$). Young’s inequality gives $|\rho(w)|\le\|\rho''\|_{L^1[-2a,2a]}$.

Define
\[
\mu_2:=\inf\Bigl\{\frac{L(w)}{\|w\|^2_{L^2(-1,1)}}:w\text{ even},\;\int_{-1}^1 w=0,\;\mathrm{supp}\,w\subset[-1,1],\;w\not=0\Bigr\}.
\]

---

## 3. Elementary lower bound for $\mu_2$

**Lemma 3.1 (PROVEN).** For even mean-zero $w$ on $[-1,1]$,
\[
|\widehat w(\xi)|\;\le\;\frac{\xi^2}{2}\sqrt{\frac25}\,\|w\|,
\]
hence Plancherel mass in $|\xi|<\Omega$ is at most $\Omega^5/(50\pi)$.

*Proof.* $\widehat w(\xi)=\int w(t)(\cos(\xi t)-1)\,dt$ since $\int w=0$ and $w$ is even. $|{\cos(\xi t)-1}|\le \xi^2 t^2/2$, so $|\widehat w|\le(\xi^2/2)\int t^2|w|\le(\xi^2/2)\|t^2\|_{L^2[-1,1]}\|w\|=(\xi^2/2)\sqrt{2/5}\,\|w\|$. Then $|\widehat w|^2\le \xi^4/10\,\|w\|^2$ and
\[
\frac1{2\pi}\int_{|\xi|<\Omega}|\widehat w|^2\,d\xi\Big/\|w\|^2
\;\le\;\frac1{2\pi}\cdot\frac2{10}\int_0^\Omega\xi^4\,d\xi
=\frac{\Omega^5}{50\pi}.
\]

**Lemma 3.2 (PROVEN given the mass cap).** If the Plancherel mass in $|\xi|<\Omega$ is $\le\ell$, then
\[
\mu_2\;\ge\;(1-\ell)(\log\Omega+\gamma)+\mathrm{NEG},
\]
where $\mathrm{NEG}$ is the contribution of $\{\log|\xi|+\gamma<0\}$ against the $\xi^4$ envelope: $\mathrm{NEG}=-(e^{-5\gamma})/(250\pi)=-7.09\times 10^{-5}$ (CHECKED; the formula is elementary).

**Corollary 3.3 (PROVEN elementary, constant CHECKED).**
\[
\mu_2\;\ge\;\max_{\Omega>1}\Bigl(1-\frac{\Omega^5}{50\pi}\Bigr)(\log\Omega+\gamma)+\mathrm{NEG}
=1.02797
\]
at $\Omega=1.865$ (`l_fourier.py`). This does **not** clear $\mathrm{th}(a_2)=1.355$.

---

## 4. Nested concentration

Let $Q_\omega$ be the integral operator on $L^2(-1,1)$ with kernel $\sin(\omega(x-y))/(\pi(x-y))$, and $Q_\omega^{\mathrm{emz}}$ its compression to even mean-zero functions. Low-frequency mass in $|\xi|<\omega$ equals $\langle Q_\omega w,w\rangle/\|w\|^2\le\|Q_\omega^{\mathrm{emz}}\|_{\mathrm{op}}\le\|Q_\omega^{\mathrm{emz}}\|_{\mathrm{HS}}$.

**Lemma 4.1 (PROVEN).** Let $F(\omega)$ be the Plancherel mass of $w$ in $|\xi|<\omega$, with $F(\infty)=1$. Then
\[
\frac{L(w)}{\|w\|^2}
=\log\Omega+\gamma-\int_0^\Omega\frac{F(\omega)}{\omega}\,d\omega
+\int_{|\xi|>\Omega}(\log|\xi|-\log\Omega)\,d\mu(\xi).
\]
The last integral is $\ge 0$ for $\Omega\ge 1$. If $F(\omega)\le\alpha(\omega)$ for all $\omega\in(0,\Omega]$ and $\alpha(\omega)=O(\omega^5)$ as $\omega\to 0$, the infimum of the right-hand side is attained by greedy fill $F=\alpha$, and
\[
\mu_2\;\ge\;\log\Omega+\gamma-\int_0^\Omega\frac{\alpha(\omega)}{\omega}\,d\omega+\mathrm{NEG}.
\]

*Proof.* Stieltjes integration by parts. The boundary term at $0$ vanishes by the $O(\omega^5)$ cap. The tail $\xi>\Omega$ has log-weight $\ge\log\Omega+\gamma$. $\mathrm{NEG}$ only makes the bound more conservative on the negative-log arc.

**Numerical input (CHECKED, not interval).** Nyström trapezoid of $\|Q_\omega^{\mathrm{emz}}\|_{\mathrm{HS}}$ at $n=81$, inflated by $1.05$ (coarser grids are larger: $n=81\to 321$ at $\Omega=2.4$ gives $0.125775\to 0.125675$). Command: `python3 tools/weil_first_prime/mu2_envelope.py`.

| $\Omega$ | $\alpha_{\mathrm{cons}}$ | nested $\mu_2$ |
|---:|---:|---:|
| $2.2$ | $0.0938$ | $1.3429$ |
| $2.4$ | $0.1321$ | $1.4202$ |
| $3.2$ | $0.3570$ | $\mathbf{1.6414}$ |
| $6.0$ | $1.0000$ | $1.8159$ (HS cap saturates) |

Thus $\mu_2\ge 1.6414>\mathrm{th}(a_2)$ with margin $0.286$, **conditional on the HS quadrature**. Hard cutoff (mass in $(0,\Omega)$ treated as log-weight $0$) saturates at $1.270$ and cannot reach $1.355$ even with exact $\lambda_{\max}$: nesting is load-bearing. The bound does not clear $\mathrm{th}(a_3)=1.816$.

---

## 5. Remainder $\rho$ and the even mean-zero sector

**Lemma 5.1 (PROVEN from Suzuki (2.2)).** For $t>0$,
\[
r''(t)=-2\cosh(t/2)+\frac{e^{t/2}}{2\sinh t}-\frac1{2t},\qquad r''(0+)=-\frac74.
\]
Hence $\rho''(0+)=0$. Taylor: $r(t)=-\frac78 t^2-\frac1{288}t^3-\frac3{128}t^4+O(t^5)$, using $\zeta(0,1/4)=\frac14$, $\zeta(-1,1/4)=\frac1{96}$, $\zeta(-2,1/4)=-\frac1{64}$ (Bernoulli–Hurwitz; $B_2(1/4)=-\frac1{48}$, not $\frac5{96}$).

**Lemma 5.2 (CHECKED on $(0,20]$).** $\rho''<0$ on $(0,20]$ and $\rho''\le-\frac3{10}t^2$ there (`rpp_closed.py`: $\min(-\rho''/t^2)=0.30026$ at $t\approx 1.501$). In particular $\rho''\le 0$ on $[0,2a_2]=[0,\log 2]$.

**Lemma 5.3 (PROVEN Young, constant CHECKED).** $|\rho(w)|\le\int_{-2a_2}^{2a_2}|\rho''(s)|\,ds$. Under Lemma 5.2 this equals $-m(0)=0.07251498$, where $m(\eta)=\int_{-2a_2}^{2a_2}\rho''(s)\cos(\eta s)\,ds$ (`ground_ray.py`).

**Theorem 5.4 (even mean-zero sector at $a=a_2$).** Assume the quadrature of §4, so $\mu_2\ge 1.6414$. Then for every even mean-zero $w$ vanishing at $\pm 1$,
\[
R(a_2,w)\;\ge\;\mu_2-\mathrm{th}(a_2)-0.072515\;\ge\;0.213\;>\;0.
\]
Label: CHECKED NUMERICALLY. The inequality structure is PROVEN; the constant $1.6414$ is the HS quadrature. This is **not** $\lambda_{a_2}>0$, because the ground ray $\int w\not=0$ is excluded.

---

## 6. The cosine, and why $\rho$ cannot be dropped

**Lemma 6.1 (PROVEN elementary).** For $\varphi(t)=\cos(\pi t/2)$ on $[-1,1]$ and $h\in[0,2]$,
\[
H(h)=\int\varphi(x)\varphi(x-h)\,dx
=\frac{2-h}{2}\cos\Bigl(\frac{\pi h}{2}\Bigr)+\frac1\pi\sin\Bigl(\frac{\pi h}{2}\Bigr).
\]
($H(0)=1$, $H(2)=0$.)

**Proposition 6.2 (CHECKED).** With jumping-form $L(\varphi)/\|\varphi\|^2=0.365641812186$ and rank-one $\frac74 a_2(\int\varphi)^2=0.983224371719$,
\[
J(\varphi)=1.348866183905,\qquad J-\mathrm{th}=-6.566446\times 10^{-3}.
\]
The closed Hankel plus $\rho''$ gives $\rho(\varphi)=0.009220270414$, hence $J+\rho-\mathrm{th}=+2.653824\times 10^{-3}>0$. Command: `python3 tools/weil_first_prime/ground_ray.py`.

**Corollary 6.3.** Any proof that *drops* $\rho$ fails on the approximate ground state, already at $a=a_2$. The first-prime obstruction is even and nonnegative: the rank-one is too small by $6.6\times 10^{-3}$, and $\rho$ supplies $9.2\times 10^{-3}$.

The Fourier multiplier of $\rho$ changes sign ($m(0)=-0.0725$, $m(5.5)=+0.0523$), so $\rho$ is not a positive form. High-frequency even functions can have $\rho<0$; they are saved by $L$, not by $\rho$.

---

## 7. Ground ray: what is known, what is open

Let $Q=L+\frac74 a_2|1\rangle\langle 1|+\rho$ on even functions vanishing at $\pm 1$, and $V_K=\mathrm{span}\{\cos((k+\tfrac12)\pi t):0\le k<K\}$. Fourier assembly of $Q$ (`ground_ray_cross.py`, Plancherel of $\varphi_0$ to $1.1\times 10^{-7}$):

| $K$ | $\lambda_{\min}(Q|_{V_K})$ | $\lambda_{\min}-\mathrm{th}$ |
|---:|---:|---:|
| $1$ | $1.35807446$ | $2.642\times 10^{-3}$ |
| $24$ | $1.35682359$ | $1.391\times 10^{-3}$ |
| $80$ | $1.35677238$ | $1.340\times 10^{-3}$ |

Monotone decreasing, always above threshold. This is an **upper** bound of $\inf Q$. A $1/K$ extrapolation of the gap is $\approx 1.32\times 10^{-3}$ (CONJECTURED).

Schur of the $V_K$-ground state against the tail closes if $k|(Qv)_k|\le 0.096$ for all $k\ge 80$ (`C²/budget=0.25` at $M=64$). CHECKED for $k<80$; not proved.

**Lemma 7.1 (structure of $Q(\varphi_0,\varphi_k)$, CHECKED).** Split $L=\mathrm{jump}+\mathrm{pot}$. Then $\varphi_0\varphi_k=\frac12(\cos((k+1)\pi t)+\cos(k\pi t))$, so $\mathrm{pot}=-\frac14(I(k+1)+I(k))$ with $I(n)=\int_{-1}^1\log(1-t^2)\cos(n\pi t)\,dt$. One integration by parts gives $I(n)=O(1/n)$; adjacent frequencies cancel to $O(1/k^2)$. CHECKED: $k^2\,\mathrm{pot}\to\approx 0.24$. The $O(1/k)$ cancellation against the rank-one is entirely in the Beurling–Deny jump: $|k(\mathrm{jump}+\kappa\,\mathrm{mean}_0\mathrm{mean}_k)|\le 0.10$ for $k\le 32$ (`q0k_split.py`). That is the remaining elementary estimate.

---

## 8. What would make this a theorem of $\lambda_{a_2}>0$, and what would prove RH

- **Even mean-zero at $a_2$:** replace the $1.05\times$ Nyström HS by an interval/`rug` enclosure of $\|Q_\omega^{\mathrm{emz}}\|_{\mathrm{HS}}$. Lemma 4.1 then makes Theorem 5.4 PROVEN.
- **Ground ray:** prove $|\mathrm{jump}(\varphi_0,\varphi_k)+\kappa\,\mathrm{mean}_0\mathrm{mean}_k|\le C/k$ with $C\lesssim 0.12$. Section 7’s Schur becomes a theorem, and with the mean-zero sector one has $\lambda_{a_2}>0$ on even functions. Odd functions are safer on the sine test function ($L+\rho-\mathrm{th}=+0.152$) but still need a $\mu_{\mathrm{odd}}$ envelope.
- **Past $a_2$:** prime-2 overlap of length $2\varepsilon$ eats a Hankel of size $O(\varepsilon)$. The mean-zero margin $0.213$ can absorb a crude overlap for small $\varepsilon$; the ground-ray margin is only $10^{-3}$. An explicit $\delta$ is a 1-parameter problem after the endpoint is closed, not a sweep.
- **RH:** uniform-in-$a$ positivity. Primes accumulate; the local $ct^2$ remainder plus rank-one is not a Gårding inequality as $a\to\infty$. Suzuki’s $W(a,\theta;z)\to\xi/\xi'$ assumes the form stays positive. We do not have this path.

---

## 9. Reproduce

```
python3 tools/weil_first_prime/rpp_closed.py
python3 tools/weil_first_prime/mu2_envelope.py
python3 tools/weil_first_prime/ground_ray.py
python3 tools/weil_first_prime/ground_ray_cross.py
python3 tools/weil_first_prime/q0k_split.py
```

(`python3` + numpy; exploratory `f64`, not `rug`/`arb`.)

---

## References

- E. Bombieri, *A variational approach to the Riemann hypothesis*, 2000.
- M. Suzuki, *The Weil quadratic form and the screw function of the Riemann zeta function*, arXiv:2606.09096.
- A. Weil, *Sur les “formules explicites” de la théorie des nombres premiers*, 1952.
- H. Yoshida, *On Hermitian forms attached to zeta functions*, 1992.

Companion lab notes: `research/notes/attack-weil-first-prime.md` §§21–23.
