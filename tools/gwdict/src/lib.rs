// gwdict: finite Guinand-Weil dictionary (Groskin 2607.02828) -> independent
// prime-side recomputation of tr W_T and ||W_T||^2_HS for the finitet windows
// T = 100..700, hunting the archimedean tail order.
//
// All conventions e^{-2 pi i}, matching Groskin Thm 2.5 verbatim:
//   <v, Q_infty v> = sum_{z in Z*_zeta} g_v(z)
//                  = -(1/pi) sum_{q=p^a<=c} Lam(q)/sqrt(q) ghat_v(log q / 2pi)
//                    + 2 g_v(i/2) + (1/2pi) int_R h_+(r) g_v(r) dr,
//   h_+(r) = Re psi_Gamma(1/4 + i r/2) - log pi,  ghat_v(xi) = pi K_v(1-|xi|/Delta).
//
// Everything below is f64 unless stated. Every number printed carries an honesty
// label in the accompanying note research/notes/attack-gw-dictionary.md.
use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};

// ---------------------------------------------------------------------------
// complex
// ---------------------------------------------------------------------------
#[derive(Clone, Copy, Debug)]
pub struct C {
    pub re: f64,
    pub im: f64,
}
impl C {
    pub fn new(re: f64, im: f64) -> Self {
        C { re, im }
    }
    pub fn real(re: f64) -> Self {
        C { re, im: 0.0 }
    }
    pub fn add(self, o: C) -> C {
        C::new(self.re + o.re, self.im + o.im)
    }
    pub fn sub(self, o: C) -> C {
        C::new(self.re - o.re, self.im - o.im)
    }
    pub fn scale(self, f: f64) -> C {
        C::new(self.re * f, self.im * f)
    }
    pub fn mul(self, o: C) -> C {
        C::new(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    }
    pub fn div(self, o: C) -> C {
        let d = o.re * o.re + o.im * o.im;
        C::new((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)
    }
    pub fn conj(self) -> C {
        C::new(self.re, -self.im)
    }
    pub fn abs2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
    pub fn abs(self) -> f64 {
        self.abs2().sqrt()
    }
    pub fn exp(self) -> C {
        C::new(self.re.exp() * self.im.cos(), self.re.exp() * self.im.sin())
    }
    pub fn ln(self) -> C {
        C::new(0.5 * self.abs2().ln(), self.im.atan2(self.re))
    }
    pub fn sin(self) -> C {
        C::new(self.re.sin() * self.im.cosh(), self.re.cos() * self.im.sinh())
    }
    pub fn exp_2pi_i(angle: C) -> C {
        // exp(2 pi i angle) = exp(-2 pi Im angle) * (cos(2 pi Re angle) + i sin(2 pi Re angle))
        let ph = 2.0 * PI * angle.re;
        let dec = (-2.0 * PI * angle.im).exp();
        C::new(dec * ph.cos(), dec * ph.sin())
    }
}

// psi(s) = int_{-1/2}^{1/2} cos(sqrt2 u) e^{-2 pi i s u} du  (entire, closed form)
pub fn psi(s: C) -> C {
    let s2 = C::real(SQRT_2);
    let d1 = s2.sub(s.scale(2.0 * PI));
    let d2 = s2.add(s.scale(2.0 * PI));
    let mut t1 = C::real(FRAC_1_SQRT_2).sub(s.scale(PI)).sin().div(d1);
    if d1.abs2() < 1e-18 {
        t1 = C::real(0.5);
    }
    let mut t2 = C::real(FRAC_1_SQRT_2).add(s.scale(PI)).sin().div(d2);
    if d2.abs2() < 1e-18 {
        t2 = C::real(0.5);
    }
    t1.add(t2)
}

// psi_profile(u) = cos(sqrt2 u) 1_{|u|<=1/2}
pub fn psi_profile(u: f64) -> f64 {
    if u.abs() <= 0.5 {
        (SQRT_2 * u).cos()
    } else {
        0.0
    }
}

// (psi * psi)(u), even, closed form on [0,1]
pub fn psi_star_psi(u: f64) -> f64 {
    let u = u.abs();
    if u > 1.0 {
        return 0.0;
    }
    0.5 * ((SQRT_2 * u).cos() * (1.0 - u) + (SQRT_2 * (1.0 - u)).sin() / SQRT_2)
}

// digamma, complex, via recurrence to |z|>=10 then asymptotic (12 Bernoulli terms)
pub fn digamma(z: C) -> C {
    let mut z = z;
    let mut shift = C::real(0.0);
    while z.abs() < 10.0 {
        shift = shift.sub(C::real(1.0).div(z));
        z = z.add(C::real(1.0));
    }
    let b: [f64; 12] = [
        1.0 / 6.0,
        -1.0 / 30.0,
        1.0 / 42.0,
        -1.0 / 30.0,
        5.0 / 66.0,
        -691.0 / 2730.0,
        7.0 / 6.0,
        -3617.0 / 510.0,
        43867.0 / 798.0,
        -174611.0 / 330.0,
        854513.0 / 138.0,
        -236364091.0 / 2730.0,
    ];
    let mut sum = z.ln().sub(C::real(0.5).div(z));
    let z2 = z.mul(z);
    let mut zp = z2;
    for k in 0..b.len() {
        sum = sum.sub(C::real(b[k]).div(zp.scale((2 * (k + 1)) as f64)));
        zp = zp.mul(z2);
    }
    sum.add(shift)
}

// h_+(r) = Re psi_Gamma(1/4 + i r/2) - log pi
pub fn h_plus(r: f64) -> f64 {
    let z = C::new(0.25, 0.5 * r);
    digamma(z).re - PI.ln()
}

// ---------------------------------------------------------------------------
// primes & von Mangoldt prime powers q = p^a <= c
// ---------------------------------------------------------------------------
pub fn prime_powers(c: f64) -> Vec<(f64, f64)> {
    // returns (q, Lambda(q)) for all prime powers q <= c
    let cmax = c.ceil() as usize;
    let mut is_comp = vec![false; cmax + 1];
    let mut primes = Vec::new();
    for i in 2..=cmax {
        if !is_comp[i] {
            primes.push(i);
            let mut j = i * i;
            while j <= cmax {
                is_comp[j] = true;
                j += i;
            }
        }
    }
    let mut out = Vec::new();
    for &p in &primes {
        let logp = (p as f64).ln();
        let mut q = p as f64;
        while q <= c {
            out.push((q, logp));
            q *= p as f64;
        }
    }
    out
}

// ---------------------------------------------------------------------------
// Gauss-Legendre 16-point on [0,1], returned as (nodes, weights) on [0,1]
// ---------------------------------------------------------------------------
pub fn gl16() -> (Vec<f64>, Vec<f64>) {
    let x = [
        0.0950125098376374401853193,
        0.2816035507792589132304605,
        0.4580167776572273863424194,
        0.6178762444026437484466718,
        0.7554044083550030338951012,
        0.8656312023878317438804679,
        0.9445750230732325760779884,
        0.9894009349916499325961542,
    ];
    let w = [
        0.1894506104550684962853967,
        0.1826034150449235888667637,
        0.1691565193950025381893121,
        0.1495959888165767320815017,
        0.1246289712555338720524763,
        0.0951585116824927848099251,
        0.0622535239386478928628438,
        0.0271524594117540948517806,
    ];
    let mut nodes = Vec::new();
    let mut weights = Vec::new();
    for i in 0..8 {
        nodes.push(0.5 - 0.5 * x[i]);
        weights.push(0.5 * w[i]);
    }
    for i in (0..8).rev() {
        nodes.push(0.5 + 0.5 * x[i]);
        weights.push(0.5 * w[i]);
    }
    (nodes, weights)
}

// integrate f over [a,b] by composite 16-point Gauss-Legendre with n panels
pub fn integrate(f: &dyn Fn(f64) -> f64, a: f64, b: f64, n: usize) -> f64 {
    let (x, w) = gl16();
    let h = (b - a) / n as f64;
    let mut s = 0.0;
    for p in 0..n {
        let aa = a + p as f64 * h;
        for i in 0..16 {
            s += w[i] * f(aa + h * x[i]);
        }
    }
    s * h
}

// integrate f over [0, max_upper] with geometric panel growth 1,2,4,... (then final)
pub fn integrate_half_line(f: &dyn Fn(f64) -> f64, max_upper: f64) -> f64 {
    let mut s = 0.0;
    let mut lo = 0.0;
    let mut hi = 1.0;
    while hi <= max_upper {
        s += integrate(f, lo, hi, 4);
        lo = hi;
        hi *= 2.0;
    }
    if lo < max_upper {
        s += integrate(f, lo, max_upper, 4);
    }
    s
}

// ---------------------------------------------------------------------------
// The dictionary: v -> T_v -> K_v -> ghat_v -> g_v   (c fixed, N fixed)
// ---------------------------------------------------------------------------
pub struct Dict {
    pub c: f64,
    pub l: f64,     // log c
    pub delta: f64, // L/(2 pi)
    pub n: usize,   // band
    pub u: Vec<f64>, // u[m], m = -N..N (even embedding)
    pub a: Vec<f64>, // a_m = 2 u_m^2
    pub b: Vec<C>,   // b_m = (2/(pi i)) u_m sum_{n!=m} u_n/(m-n)
}

impl Dict {
    pub fn new(c: f64, v: &[f64]) -> Self {
        let l = c.ln();
        let delta = l / (2.0 * PI);
        let n = v.len() - 1;
        let mut u = vec![0.0; 2 * n + 1];
        u[n] = v[0];
        for k in 1..=n {
            u[n + k] = v[k] / SQRT_2;
            u[n - k] = v[k] / SQRT_2;
        }
        let mut a = vec![0.0; 2 * n + 1];
        let mut b = vec![C::real(0.0); 2 * n + 1];
        for m in 0..2 * n + 1 {
            let mm = m as i64 - n as i64;
            a[m] = 2.0 * u[m] * u[m];
            let mut s = 0.0;
            for nn in 0..2 * n + 1 {
                if nn == m {
                    continue;
                }
                let nm = nn as i64 - n as i64;
                s += u[nn] / (mm - nm) as f64;
            }
            // b_m = (2/(pi i)) u_m s  =  (2 u_m s)/(pi i) = -(2 u_m s i)/pi
            b[m] = C::new(0.0, -(2.0 * u[m] * s) / PI);
        }
        Dict { c, l, delta, n, u, a, b }
    }

    // K_v(omega) = sum_m (a_m omega + b_m) e^{2 pi i m omega}
    pub fn kv(&self, omega: C) -> C {
        let mut s = C::real(0.0);
        let n = self.n;
        for m in 0..2 * n + 1 {
            let mm = (m as i64 - n as i64) as f64;
            let e = C::exp_2pi_i(C::real(mm).mul(omega));
            s = s.add(omega.scale(self.a[m]).add(self.b[m]).mul(e));
        }
        s
    }

    // ghat_v(xi) = pi K_v(1 - |xi|/Delta)   (real xi, |xi| <= Delta)
    pub fn ghat(&self, xi: f64) -> C {
        if xi.abs() > self.delta {
            return C::real(0.0);
        }
        let arg = 1.0 - xi.abs() / self.delta;
        self.kv(C::real(arg)).scale(PI)
    }

    // g_v(z) = int_{-Delta}^{Delta} ghat_v(xi) e^{2 pi i z xi} dxi, closed form
    //        = 2 pi Delta sum_m [a_m I1_m(z) + b_m I0_m(z)]
    // I0_m(z) = int_0^1 e^{2 pi i m u} cos(2 pi z Delta (1-u)) du
    //         = (1/2)[ E+ J0(m - z Delta) + E- J0(m + z Delta) ],  E+ = e^{2 pi i z Delta}
    // I1_m(z) likewise with J1.  Valid for complex z.
    pub fn gv(&self, z: C) -> C {
        let n = self.n;
        let mut s = C::real(0.0);
        let ep = C::exp_2pi_i(z.scale(self.delta)); // e^{2 pi i z Delta}
        let em = C::exp_2pi_i(z.scale(-self.delta)); // e^{-2 pi i z Delta}
        for m in 0..2 * n + 1 {
            let mm = (m as i64 - n as i64) as f64;
            let wp = C::real(mm).sub(z.scale(self.delta)); // m - z Delta
            let wm = C::real(mm).add(z.scale(self.delta)); // m + z Delta
            let (j0p, j1p) = Self::j01(wp);
            let (j0m, j1m) = Self::j01(wm);
            let i0 = ep.mul(j0p).add(em.mul(j0m)).scale(0.5);
            let i1 = ep.mul(j1p).add(em.mul(j1m)).scale(0.5);
            s = s.add(omega_scaled_add(self.a[m], i1, self.b[m], i0));
        }
        s.scale(2.0 * PI * self.delta)
    }

    fn j01(w: C) -> (C, C) {
        let two_pi_i_w = C::new(0.0, 2.0 * PI).mul(w);
        if two_pi_i_w.abs2() < 1e-18 {
            (C::real(1.0), C::real(0.5))
        } else {
            let e = two_pi_i_w.exp();
            let j0 = e.sub(C::real(1.0)).div(two_pi_i_w);
            let inv = C::real(1.0).div(two_pi_i_w);
            let j1 = e.mul(inv.sub(inv.mul(inv))).add(inv.mul(inv));
            (j0, j1)
        }
    }
}

// ---------------------------------------------------------------------------
// The explicit formula for an EVEN admissible test function f (Groskin Thm 2.5):
//   sum_{all rho} f(gamma_rho) = -(1/pi) sum_{q<=c} Lam(q)/sqrt(q) fhat(log q/2pi)
//                              + 2 f(i/2) + (1/2pi) int_R h_+(r) f(r) dr
// fhat must be supported in [-log c/2pi, log c/2pi].
// f: Fn(C) -> C  (evaluates f at real ordinates, at i/2, at r)
// fhat: Fn(f64) -> C (fourier transform at real frequencies)
// arch: Fn(f64) -> f64 (the even function restricted to r >= 0 for the integral)
// ---------------------------------------------------------------------------
pub struct ExplicitFormula<'a> {
    pub c: f64,
    pub qq: Vec<(f64, f64)>, // (q, Lambda(q)), q <= c
    pub f: &'a dyn Fn(C) -> C,
    pub fhat: &'a dyn Fn(f64) -> C,
    pub arch: &'a dyn Fn(f64) -> f64, // f(r) for r >= 0 (the even function)
    pub arch_max: f64,
    pub arch_h: f64,     // uniform spacing for the arch quadrature
    pub arch_period: f64, // shortest period of f (for the tail)
    pub arch_center: f64, // decay center for the tail
}

impl<'a> ExplicitFormula<'a> {
    // full value = prime + pole + arch
    pub fn evaluate(&self) -> f64 {
        let mut prime = C::real(0.0);
        for &(q, lam) in &self.qq {
            let xi = q.ln() / (2.0 * PI);
            prime = prime.sub((self.fhat)(xi).scale(lam / q.sqrt()));
        }
        let prime = prime.scale(1.0 / PI);
        let pole = (self.f)(C::new(0.0, 0.5)).scale(2.0);
        // arch: (1/2pi) int_{-inf}^{inf} h_+(r) f(r) dr = (1/pi) int_0^{inf} h_+(r) f(r) dr  (even f)
        let arch = {
            let g = |r: f64| h_plus(r) * (self.arch)(r);
            (1.0 / PI) * integrate_half_line(&g, self.arch_max)
        };
        prime.re + pole.re + arch
    }
}

// helper: a * i1 + b * i0  (a real, b complex, i1/i0 complex)
fn omega_scaled_add(a: f64, i1: C, b: C, i0: C) -> C {
    C::real(a).mul(i1).add(b.mul(i0))
}

// ---------------------------------------------------------------------------
// Robust arch-integral machinery
// ---------------------------------------------------------------------------
// uniform composite GL16 with fixed panel width h (resolves band-limited
// oscillations: h must be <= ~1/(8*maxfreq) where maxfreq is in rad/r)
pub fn uniform_integrate(f: &dyn Fn(f64) -> f64, a: f64, b: f64, h: f64) -> f64 {
    let n = ((b - a) / h).ceil() as usize;
    integrate(f, a, a + n as f64 * h, n)
}

// Tail of (1/2pi) int_R^inf h_+(r) F(r) dr for F(r) ~ E(r) sin^2(pi (r-center)/period + phi)
// with E(r) ~ E_R * ((R-center)/(r-center))^alpha in the tail (alpha fitted from R and 4R).
// E_R recovered by the half-period average: (F(R)+F(R+p/2)) = E(R) for a pure sin^2 envelope.
pub fn arch_tail_power(f: &dyn Fn(f64) -> f64, r: f64, period: f64, center: f64) -> f64 {
    let er1 = f(r) + f(r + period / 2.0);
    let r2 = 4.0 * r;
    let er2 = f(r2) + f(r2 + period / 2.0);
    // E(t) ~ E_r * ((r-c)/(t-c))^alpha  ->  alpha = ln(E(r)/E(r2)) / ln((r2-c)/(r-c))
    let alpha = (er1 / er2).ln() / ((r2 - center) / (r - center)).ln();
    // smooth integral of h_+(t) * E_R * ((R-center)/(t-center))^alpha over [r, inf)
    let g = |t: f64| h_plus(t) / (t - center).powf(alpha);
    let mut s = 0.0;
    let mut lo = r;
    let mut hi = r * 1.5;
    while hi <= 1.0e10 {
        s += integrate(&g, lo, hi, 4);
        lo = hi;
        hi *= 1.5;
    }
    if lo < 1.0e10 {
        s += integrate(&g, lo, 1.0e10, 4);
    }
    let tail = (1.0 / (2.0 * PI)) * 0.5 * er1 * (r - center).powf(alpha) * s;
    tail
}
