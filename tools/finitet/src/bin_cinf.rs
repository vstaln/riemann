// finitet-cinf: C^infty chi-smoothed phi_T — does smoothing pull ||W||^2_HS/N toward
// c = 1/2 + (1/sqrt2)cot(1/sqrt2) = 1.3274992963205885 (vs the hard-cutoff idealized
// model values 1.265 -> 1.287 at T=100..600 measured in finitet/main.rs)?
//
// Paper construction (anthropic-informal-note): phi_T(x) = chi(N/2T + x) chi(N/2T - x) sqrt(cos(sqrt2 T x/N)),
// chi in C^infty monotone, 0 on (-inf,0], 1 on [1,inf).  Rescaled u = x*T/N:
//     phi_bar(u) = chi((N/T)(u+1/2)) * chi((N/T)(1/2-u)) * sqrt(cos(sqrt2 u)),
// i.e. the chi-ramps have width T/N in u-units (the "paper-realistic" epsilon).
// Concrete chi = Hermite smoothstep sigma_k (C^k, monotone) — a legitimate instance of
// the paper's abstract chi (the theorems only need the listed properties).
//
// Kernel variants:
//   * hard-cos   : phi = cos(sqrt2 u) 1_{|u|<=1/2}         (round-1 idealized model, C^0)
//   * cinf-cos   : phi = chi_e(u) chi_e(-u) cos(sqrt2 u)   (smoothed, C^k)
//   * cinf-sqrt  : phi = chi_e(u) chi_e(-u) sqrt(cos(sqrt2 u)) (literal paper kernel, C^k)
// where chi_e is the ramp 0->1 on [-1/2, -1/2+eps] (chi_e(u)=sigma((u+1/2)/eps)); the
// paper-realistic eps = T/N reproduces chi((N/T)(u+1/2)) exactly.
//
// Closed forms: FT of a piecewise (polynomial x cos)-product reduces to elementary
// functions (sin/cos times polynomials), derived below.  The polynomial-moment
// evaluation is conditioning-fragile at high degree (m up to 68) for moderate
// frequencies, so the numerical engine here is high-order composite Simpson on the
// value functions (uniform, robust), cross-validated against the closed form at
// parameter values where the closed form is well-conditioned, and against the
// (exact, for smooth compactly-supported phi) Poisson identity
//     sum_{k in Z} Phi_hat(s-k) Phi_hat(s'-k) = Phi2_hat(s-s'),  Phi2_hat = FT(phi^2).
//
// W_T = (1/int phi^2) V^T V,  V[rho][k] = Phi_hat(s_rho - k),  s_rho = (gamma_rho - T) N/T.
// ||W||^2_HS/N decomposed as (1/N) sum_{rho,rho'} [(VV^T)_{rho,rho'}/int phi^2]^2
// (diag + offdiag), plus the analytic pair-sum version using the exact Poisson limit
// (VV^T)_{rho,rho'} = Phi2_hat(s_rho - s_rho').
//
// Data: tools/data/zeros_1_1000.txt (LMFDB, 1000 zeros, gamma_1000 = 1419.42) covers
// all windows [T, 2T) for T <= 600 (need gamma <= 1200).  No network fetch required.
use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};

// ---------------------------------------------------------------------------
// complex helper
// ---------------------------------------------------------------------------
#[derive(Clone, Copy, Debug)]
struct C {
    re: f64,
    im: f64,
}
impl C {
    fn new(re: f64, im: f64) -> Self {
        C { re, im }
    }
    fn real(re: f64) -> Self {
        C { re, im: 0.0 }
    }
    fn add(self, o: C) -> C {
        C::new(self.re + o.re, self.im + o.im)
    }
    fn sub(self, o: C) -> C {
        C::new(self.re - o.re, self.im - o.im)
    }
    fn scale(self, f: f64) -> C {
        C::new(self.re * f, self.im * f)
    }
    fn div(self, o: C) -> C {
        let d = o.re * o.re + o.im * o.im;
        C::new((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)
    }
    fn expi(self) -> C {
        // e^z = e^{re}(cos im + i sin im)
        C::new(self.re.exp() * self.im.cos(), self.re.exp() * self.im.sin())
    }
    fn sin(self) -> C {
        C::new(self.re.sin() * self.im.cosh(), self.re.cos() * self.im.sinh())
    }
    fn abs2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
}

// ---------------------------------------------------------------------------
// Hermite smoothstep sigma_k (C^k, monotone): sigma(0)=0, sigma(1)=1,
// sigma^(j)(0)=sigma^(j)(1)=0 for 1 <= j <= k.
//   sigma_k(t) = (1/B(k+1,k+1)) int_0^t s^k (1-s)^k ds,  B = (k!)^2/(2k+1)!
// ---------------------------------------------------------------------------
fn binom(n: usize, k: usize) -> u64 {
    if k > n {
        return 0;
    }
    let mut r: u64 = 1;
    for i in 0..k {
        r = r * (n - i) as u64 / (i + 1) as u64;
    }
    r
}

fn sigma_coeffs(k: usize) -> Vec<f64> {
    // sigma(t) = sum_m c[m] t^m, m = 0..=2k+1
    let mut c = vec![0.0; 2 * k + 2];
    for i in 0..=k {
        let sign = if i % 2 == 0 { 1.0 } else { -1.0 };
        let b = binom(k, i) as f64;
        c[k + i + 1] += sign * b / (k + i + 1) as f64;
    }
    let s1: f64 = c.iter().sum();
    for v in c.iter_mut() {
        *v /= s1;
    }
    c
}

fn sigma_eval(c: &[f64], t: f64) -> f64 {
    let mut r = 0.0;
    for &v in c.iter().rev() {
        r = r * t + v;
    }
    r
}

// ---------------------------------------------------------------------------
// polynomial helpers (low -> high degree)
// ---------------------------------------------------------------------------
fn poly_mul(a: &[f64], b: &[f64]) -> Vec<f64> {
    let mut c = vec![0.0; a.len() + b.len() - 1];
    for (i, &ai) in a.iter().enumerate() {
        if ai == 0.0 {
            continue;
        }
        for (j, &bj) in b.iter().enumerate() {
            c[i + j] += ai * bj;
        }
    }
    c
}

fn poly_pow(a: &[f64], p: usize) -> Vec<f64> {
    let mut r = vec![1.0];
    for _ in 0..p {
        r = poly_mul(&r, a);
    }
    r
}

fn compose_affine(c: &[f64], aa: f64, bb: f64) -> Vec<f64> {
    // sum_m c[m] (aa*u + bb)^m
    let mut res = vec![0.0];
    let mut pw = vec![1.0];
    for &cm in c {
        if cm != 0.0 {
            let term: Vec<f64> = pw.iter().map(|&x| x * cm).collect();
            if res.len() < term.len() {
                res.resize(term.len(), 0.0);
            }
            for (i, &v) in term.iter().enumerate() {
                res[i] += v;
            }
        }
        pw = poly_mul(&pw, &[bb, aa]);
    }
    res
}

// ---------------------------------------------------------------------------
// value-based smoothed kernel
// ---------------------------------------------------------------------------
struct Sm {
    sig: Vec<f64>,
    eps: f64,
    k: usize,
}
impl Sm {
    fn new(eps: f64, k: usize) -> Self {
        Sm { sig: sigma_coeffs(k), eps, k }
    }
    fn chi(&self, u: f64) -> f64 {
        // ramp 0 -> 1 on [-1/2, -1/2+eps]
        let t = (u + 0.5) / self.eps;
        if t <= 0.0 {
            0.0
        } else if t >= 1.0 {
            1.0
        } else {
            sigma_eval(&self.sig, t)
        }
    }
    fn kern(&self, u: f64, sqrtkern: bool) -> f64 {
        let c0 = (SQRT_2 * u).cos(); // >= cos(1/sqrt2) > 0 on [-1/2,1/2]
        let c = if sqrtkern { c0.sqrt() } else { c0 };
        self.chi(u) * self.chi(-u) * c
    }
    fn phi2(&self, u: f64, sqrtkern: bool) -> f64 {
        // phi^2: for cos kernel = chi^2 chi^2 cos^2; for sqrt kernel = chi^2 chi^2 cos
        let cc = self.chi(u) * self.chi(-u);
        let c0 = (SQRT_2 * u).cos();
        cc * cc * if sqrtkern { c0 } else { c0 * c0 }
    }
}

fn simpson<F: Fn(f64) -> f64>(f: F, a: f64, b: f64, n: usize) -> f64 {
    let h = (b - a) / n as f64;
    let mut s = f(a) + f(b);
    for i in 1..n {
        let x = a + i as f64 * h;
        s += if i % 2 == 1 { 4.0 } else { 2.0 } * f(x);
    }
    s * h / 3.0
}

const S_CUT: f64 = 60.0; // |Phi_hat(s)| <= C8*|s|^-9 (C^8 kernel); beyond this entries are <= ~1e-11
const SN: usize = 4097; // Simpson panels on [0,1/2]; abs err ~ (h^4/180)|f''''| ~ 1e-9 at s=60

fn phibar_hat(sm: &Sm, s: f64, sqrtkern: bool) -> f64 {
    if s.abs() > S_CUT {
        return 0.0;
    }
    2.0 * simpson(
        |u| sm.kern(u, sqrtkern) * (2.0 * PI * s * u).cos(),
        0.0,
        0.5,
        SN,
    )
}

fn phibar2_hat(sm: &Sm, s: f64, sqrtkern: bool) -> f64 {
    if s.abs() > S_CUT {
        return 0.0;
    }
    2.0 * simpson(
        |u| sm.phi2(u, sqrtkern) * (2.0 * PI * s * u).cos(),
        0.0,
        0.5,
        SN,
    )
}

fn norm2(sm: &Sm, sqrtkern: bool) -> f64 {
    phibar2_hat(sm, 0.0, sqrtkern)
}

fn norm4(sm: &Sm, sqrtkern: bool) -> f64 {
    // int phi^4 = 2 int_0^{1/2} (phi^2)^2
    2.0 * simpson(|u| { let p = sm.phi2(u, sqrtkern); p * p }, 0.0, 0.5, SN)
}

// ---------------------------------------------------------------------------
// kernel as a precomputed even function on a fine grid + cubic interpolation
// (evaluation cost O(1); avoids re-running Simpson for every (rho,k) pair)
// ---------------------------------------------------------------------------
struct GridFn {
    h: f64,
    vals: Vec<f64>, // vals[i] = f(i*h), i = 0..N (s >= 0)
    nmax: f64,
}
impl GridFn {
    fn from_fn(f: &dyn Fn(f64) -> f64, h: f64, nmax: f64) -> Self {
        let n = (nmax / h).ceil() as usize + 4;
        let mut vals = Vec::with_capacity(n);
        for i in 0..n {
            vals.push(f(i as f64 * h));
        }
        GridFn { h, vals, nmax }
    }
    fn eval(&self, s: f64) -> f64 {
        let a = s.abs();
        if a > self.nmax {
            return 0.0;
        }
        let x = a / self.h;
        let i = x.floor() as isize;
        let t = x - i as f64;
        let xv = i as f64 + t;
        let idx = |j: isize| j.unsigned_abs() as usize; // even function: index -1 -> 1
        let (x0, x1, x2, x3) = ((i - 1) as f64, i as f64, (i + 1) as f64, (i + 2) as f64);
        let (v0, v1, v2, v3) = (
            self.vals.get(idx(i - 1)).copied().unwrap_or(0.0),
            self.vals.get(idx(i)).copied().unwrap_or(0.0),
            self.vals.get(idx(i + 1)).copied().unwrap_or(0.0),
            self.vals.get(idx(i + 2)).copied().unwrap_or(0.0),
        );
        let l0 = (xv - x1) * (xv - x2) * (xv - x3) / ((x0 - x1) * (x0 - x2) * (x0 - x3));
        let l1 = (xv - x0) * (xv - x2) * (xv - x3) / ((x1 - x0) * (x1 - x2) * (x1 - x3));
        let l2 = (xv - x0) * (xv - x1) * (xv - x3) / ((x2 - x0) * (x2 - x1) * (x2 - x3));
        let l3 = (xv - x0) * (xv - x1) * (xv - x2) / ((x3 - x0) * (x3 - x1) * (x3 - x2));
        v0 * l0 + v1 * l1 + v2 * l2 + v3 * l3
    }
}

// ---------------------------------------------------------------------------
// closed form: piecewise (polynomial x cos)-product Fourier transforms
// (used for validation where well-conditioned; derivation in the notes)
//   Phi_hat(s) = 2 sum_pieces int P(t) cos(sqrt2 u) cos(2 pi s u) dt, u = u0 + du t
// ---------------------------------------------------------------------------
fn factorial_f64(n: usize) -> f64 {
    let mut r = 1.0;
    for i in 2..=n {
        r *= i as f64;
    }
    r
}

fn falling(m: usize, r: usize) -> f64 {
    let mut p = 1.0;
    for i in 0..r {
        p *= (m - i) as f64;
    }
    p
}

// int_{a}^{b} t^m cos(c t) dt  -- series for |c|<12, repeated-IBP closed form else
fn integ_tm_cos(m: usize, a: f64, b: f64, c: f64) -> f64 {
    if c.abs() < 12.0 {
        let mut s = 0.0;
        let mut pwc = 1.0; // c^{2k}/(2k)!
        let mut pb = b.powi((m + 1) as i32);
        let mut pa = a.powi((m + 1) as i32);
        for k in 0..400usize {
            let e1 = 2 * k + m + 1;
            let t = pwc * (pb - pa) / e1 as f64;
            s += if k % 2 == 0 { t } else { -t };
            pwc *= c * c / ((2 * k + 2) * (2 * k + 1)) as f64;
            pb *= b * b;
            pa *= a * a;
            if t.abs() < 1e-16 * s.abs().max(1e-300) {
                break;
            }
        }
        s
    } else {
        let ant = |x: f64| -> f64 {
            let mut s = 0.0;
            let mut r = 0usize;
            while 2 * r + 1 <= m {
                let sgn = if r % 2 == 0 { 1.0 } else { -1.0 };
                s += sgn * falling(m, 2 * r + 1) * x.powi((m - 2 * r - 1) as i32)
                    * (c * x).cos()
                    / c.powi((2 * r + 2) as i32);
                r += 1;
            }
            let mut r = 0usize;
            while 2 * r <= m {
                let sgn = if r % 2 == 0 { 1.0 } else { -1.0 };
                s += sgn * falling(m, 2 * r) * x.powi((m - 2 * r) as i32) * (c * x).sin()
                    / c.powi((2 * r + 1) as i32);
                r += 1;
            }
            s
        };
        ant(b) - ant(a)
    }
}

fn integ_tm_sin(m: usize, a: f64, b: f64, c: f64) -> f64 {
    if c.abs() < 12.0 {
        let mut s = 0.0;
        let mut pwc = c; // c^{2k+1}/(2k+1)!
        let mut pb = b.powi((m + 2) as i32);
        let mut pa = a.powi((m + 2) as i32);
        for k in 0..400usize {
            let e1 = 2 * k + m + 2;
            let t = pwc * (pb - pa) / e1 as f64;
            s += if k % 2 == 0 { t } else { -t };
            pwc *= c * c / ((2 * k + 2) * (2 * k + 3)) as f64;
            pb *= b * b;
            pa *= a * a;
            if t.abs() < 1e-16 * s.abs().max(1e-300) {
                break;
            }
        }
        s
    } else {
        let ant = |x: f64| -> f64 {
            let mut s = 0.0;
            let mut r = 0usize;
            while 2 * r <= m {
                let sgn = if r % 2 == 0 { -1.0 } else { 1.0 };
                s += sgn * falling(m, 2 * r) * x.powi((m - 2 * r) as i32) * (c * x).cos()
                    / c.powi((2 * r + 1) as i32);
                r += 1;
            }
            let mut r = 0usize;
            while 2 * r + 1 <= m {
                let sgn = if r % 2 == 0 { 1.0 } else { -1.0 };
                s += sgn * falling(m, 2 * r + 1) * x.powi((m - 2 * r - 1) as i32)
                    * (c * x).sin()
                    / c.powi((2 * r + 2) as i32);
                r += 1;
            }
            s
        };
        ant(b) - ant(a)
    }
}

// pieces for phi^p on [0,1/2]: (P(t) poly, t1, t2, u0, du) with u = u0 + du*t.
// covers eps <= 0.5 (case A: none + hi ramp) and eps >= 1 (case C: single both-ramp piece).
fn closed_pieces(eps: f64, k: usize, p: usize) -> Vec<(Vec<f64>, f64, f64, f64, f64)> {
    let sig = sigma_coeffs(k);
    let mut out = Vec::new();
    if eps <= 0.5 {
        let s_hi = 0.5 - eps;
        if s_hi <= 1e-12 {
            // whole [0, 1/2] is the right ramp
            let pp = poly_pow(&sig, p);
            out.push((pp, 0.0, 1.0, 0.5, -eps));
        } else {
            out.push((vec![1.0], 0.0, s_hi, 0.0, 1.0));
            let pp = poly_pow(&sig, p);
            out.push((pp, 0.0, 1.0, 0.5, -eps));
        }
    } else {
        // eps >= 1: single both-ramp piece, t = (u+1/2)/eps in [1/(2eps), 1/eps]
        let sig2 = compose_affine(&sig, -1.0, 1.0 / eps); // sigma(1/eps - t)
        let pp = poly_mul(&poly_pow(&sig, p), &poly_pow(&sig2, p));
        out.push((pp, 0.5 / eps, 1.0 / eps, -0.5, eps));
    }
    out
}

// int P(t) cos(w u) cos(tw u) dt, u = u0 + du t
fn piece_int_cf(p: &[f64], t1: f64, t2: f64, u0: f64, du: f64, w: f64, tw: f64) -> f64 {
    let a1 = w * u0;
    let b1 = w * du;
    let a2 = tw * u0;
    let b2 = tw * du;
    let mut tot = 0.0;
    for (ap, bp) in [(a1 + a2, b1 + b2), (a1 - a2, b1 - b2)] {
        let mut acc = 0.0;
        for (m, &pm) in p.iter().enumerate() {
            if pm == 0.0 {
                continue;
            }
            let cm = integ_tm_cos(m, t1, t2, bp);
            let sm = integ_tm_sin(m, t1, t2, bp);
            acc += pm * (ap.cos() * cm - ap.sin() * sm);
        }
        tot += acc;
    }
    0.5 * tot
}

fn phibar_hat_cf(s: f64, eps: f64, k: usize) -> f64 {
    let mut tot = 0.0;
    for (pp, t1, t2, u0, du) in closed_pieces(eps, k, 1) {
        // u-integral = |du| * t-integral  (u = u0 + du t)
        tot += du.abs() * piece_int_cf(&pp, t1, t2, u0, du, SQRT_2, 2.0 * PI * s);
    }
    2.0 * tot
}

// FT of phi^2 for the cos kernel: chi^2 chi^2 cos^2(sqrt2 u) = 1/2 + 1/2 cos(2 sqrt2 u)
fn phibar2_hat_cf(s: f64, eps: f64, k: usize) -> f64 {
    let tw = 2.0 * PI * s;
    let mut tot = 0.0;
    for (pp, t1, t2, u0, du) in closed_pieces(eps, k, 2) {
        let jac = du.abs();
        // int P cos(tw u) dt (cos^2 -> 1/2 term)
        let a2 = tw * u0;
        let b2 = tw * du;
        let mut acc = 0.0;
        for (m, &pm) in pp.iter().enumerate() {
            if pm == 0.0 {
                continue;
            }
            let cm = integ_tm_cos(m, t1, t2, b2);
            let sm = integ_tm_sin(m, t1, t2, b2);
            acc += pm * (a2.cos() * cm - a2.sin() * sm);
        }
        tot += jac * 0.5 * acc;
        // int P cos(2 sqrt2 u) cos(tw u) dt (cos^2 -> 1/2 cos(2 sqrt2 u) term)
        tot += jac * 0.5 * piece_int_cf(&pp, t1, t2, u0, du, 2.0 * SQRT_2, tw);
    }
    2.0 * tot
}

// ---------------------------------------------------------------------------
// hard-cutoff idealized kernel (round-1): psi(u) = cos(sqrt2 u) 1_{|u|<=1/2}
// ---------------------------------------------------------------------------
fn psi(s: C) -> C {
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

fn psi2(s: C) -> C {
    let s2 = C::real(SQRT_2);
    let ps = s.scale(PI);
    let mut t1 = ps.sin().div(ps.scale(2.0));
    if ps.abs2() < 1e-18 {
        t1 = C::real(0.5);
    }
    let a = s2.sub(ps);
    let b = s2.add(ps);
    let mut t2 = a.sin().div(a);
    if a.abs2() < 1e-18 {
        t2 = C::real(1.0);
    }
    let mut t3 = b.sin().div(b);
    if b.abs2() < 1e-18 {
        t3 = C::real(1.0);
    }
    t1.add(t2.add(t3).scale(0.25))
}

// ---------------------------------------------------------------------------
// matrix tools
// ---------------------------------------------------------------------------
fn matmul(a: &[Vec<f64>], b: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let n = a.len();
    let mut c = vec![vec![0.0; n]; n];
    for i in 0..n {
        for k in 0..n {
            let aik = a[i][k];
            if aik == 0.0 {
                continue;
            }
            let brow = &b[k];
            let crow = &mut c[i];
            for j in 0..n {
                crow[j] += aik * brow[j];
            }
        }
    }
    c
}

// ---------------------------------------------------------------------------
// Claim 2.1 / Poisson-sum truncation error
// ---------------------------------------------------------------------------
fn poisson_err(kern: &GridFn, kern2: &GridFn, kmax: i64) -> f64 {
    let samples = [0.0_f64, 0.37, 1.9, 5.3, 12.7, 41.2, 3.14, 7.7];
    let mut err = 0.0_f64;
    for &s in &samples {
        for &s2 in &samples {
            let mut sum = 0.0_f64;
            for k in -kmax..=kmax {
                sum += kern.eval(s - k as f64) * kern.eval(s2 - k as f64);
            }
            let target = kern2.eval(s - s2);
            err = err.max((sum - target).abs());
        }
    }
    err
}

// ---------------------------------------------------------------------------
// main W_T / HS pipeline for one (T, kernel) config
// ---------------------------------------------------------------------------
struct Row {
    t: f64,
    n: usize,
    trn: f64,
    hsn: f64,
    hsn_an: f64,
    offdiag_n: f64,
    diag_n: f64,
    boundn: f64,
    delta: f64,
    trw2_chk: f64,
}

fn analyze(
    t: f64,
    gams: &[f64],
    kern: &GridFn,
    kern2: &GridFn,
    nrm2: f64,
) -> Row {
    let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
    let n = gwin.len();
    let s_rho: Vec<f64> = gwin.iter().map(|&g| (g - t) * (n as f64) / t).collect();
    // V[rho][k] = kern(s_rho - k)
    let mut v = vec![vec![0.0; n]; n];
    for r in 0..n {
        let sr = s_rho[r];
        for k in 0..n {
            v[r][k] = kern.eval(sr - k as f64);
        }
    }
    let vt = {
        let mut vt = vec![vec![0.0; n]; n];
        for i in 0..n {
            for j in 0..n {
                vt[i][j] = v[j][i];
            }
        }
        vt
    };
    let g = matmul(&vt, &v);
    let w: Vec<Vec<f64>> = g.iter().map(|row| row.iter().map(|&x| x / nrm2).collect()).collect();
    let tr: f64 = (0..n).map(|i| w[i][i]).sum();
    let trn = tr / n as f64;
    // HS2 via (VV^T)^2 decomposition
    let vvt = matmul(&v, &vt);
    let mut diag2 = 0.0;
    let mut off2 = 0.0;
    for r in 0..n {
        for r2 in 0..n {
            let x = vvt[r][r2] / nrm2;
            if r == r2 {
                diag2 += x * x;
            } else {
                off2 += x * x;
            }
        }
    }
    let hsn = (diag2 + off2) / n as f64;
    // independent check: tr(W^2) must equal hsn*n
    let mut trw2 = 0.0;
    for i in 0..n {
        for j in 0..n {
            trw2 += w[i][j] * w[j][i];
        }
    }
    // analytic pair-sum: (VV^T)_{r,r'} = Phi2_hat(s_r - s_{r'}) (exact, full k-sum)
    let mut off2an = 0.0;
    for r in 0..n {
        for r2 in 0..n {
            if r == r2 {
                continue;
            }
            let x = kern2.eval(s_rho[r] - s_rho[r2]) / nrm2;
            off2an += x * x;
        }
    }
    let hsn_an = (n as f64 + off2an) / n as f64;
    let boundn = 2.0 * trn - hsn;
    let c_bound = 1.5 - FRAC_1_SQRT_2 * FRAC_1_SQRT_2.tan().recip();
    let delta = boundn - c_bound;
    let trw2_chk = (trw2 - hsn * n as f64).abs().max(1e-300) / (hsn * n as f64).abs().max(1e-300);
    Row { t, n, trn, hsn, hsn_an, offdiag_n: off2 / n as f64, diag_n: diag2 / n as f64, boundn, delta, trw2_chk }
}

// Parseval: sum_s |Phi_hat(s)|^2 ds ~= int phi^2  (absolute-scale check on the FT)
fn parseval(sm: &Sm, sqrtkern: bool) -> f64 {
    let ds = 0.01;
    let mut s = 0.0;
    let mut acc = 0.0;
    while s <= S_CUT {
        let v = phibar_hat(sm, s, sqrtkern);
        acc += v * v * ds * 2.0;
        s += ds;
    }
    acc
}

// Variational window functional (attack-kernel.md): Q(v) = (int v^2 + 2 int_0^1 w (v*v)(w) dw)/(int v)^2,
// the asymptotic HS-norm constant for a window whose phi^2 ~ v (v even, supported on [-1/2,1/2]).
// Sanity check: v = cos^2(sqrt2 u) 1_{|u|<=1/2} must give Q = 1/2 + (1/sqrt2)cot(1/sqrt2).
fn q_window(v: &dyn Fn(f64) -> f64) -> f64 {
    let a = 2.0 * simpson(&|u| v(u), 0.0, 0.5, SN);
    let b = 2.0 * simpson(&|u| { let x = v(u); x * x }, 0.0, 0.5, SN);
    let j = simpson(
        &|w| w * simpson(&|u| v(u) * v(w - u), -0.5, 0.5, SN / 2),
        0.0,
        1.0,
        SN / 2,
    );
    (b + 2.0 * j) / (a * a)
}

// ---------------------------------------------------------------------------
fn main() {
    let k = 8usize;
    let c_hs = 0.5 + FRAC_1_SQRT_2 * FRAC_1_SQRT_2.tan().recip();
    let c_bound = 1.5 - FRAC_1_SQRT_2 * FRAC_1_SQRT_2.tan().recip();
    println!("== finitet-cinf: C^infty chi-smoothed phi_T ==");
    println!("Hermite smoothstep order k = {} (C^{})", k, k);
    println!("HS const c = 1/2+(1/sqrt2)cot(1/sqrt2) = {:.15}", c_hs);
    println!("bound const = 3/2-(1/sqrt2)cot(1/sqrt2) = {:.15}", c_bound);

    // ---- load zeros ----
    let mut gams: Vec<f64> = Vec::new();
    for line in std::fs::read_to_string("/home/vstaln/riemann/tools/data/zeros_1_1000.txt")
        .expect("zeros file")
        .lines()
    {
        let p: Vec<&str> = line.split_whitespace().collect();
        if p.len() >= 2 {
            gams.push(p[1].parse().unwrap());
        }
    }
    let gmax = gams.last().copied().unwrap_or(0.0);
    println!("loaded {} zeros, gamma_max = {:.2} (covers windows [T,2T) for T <= 600)", gams.len(), gmax);
    assert!(gmax > 1200.0, "need zeros up to 1200");

    // ---- sigma sanity ----
    {
        let sig = sigma_coeffs(k);
        let h = 1e-6;
        println!("sigma(0)={:.3e} sigma(1)={:.12} sigma'(0)={:.3e} sigma'(1)={:.3e}",
            sigma_eval(&sig, 0.0), sigma_eval(&sig, 1.0),
            (sigma_eval(&sig, h) - sigma_eval(&sig, 0.0)) / h,
            (sigma_eval(&sig, 1.0) - sigma_eval(&sig, 1.0 - h)) / h);
    }

    // ---- closed-form vs Simpson cross-validation ----
    println!("\n-- closed-form vs Simpson (cos kernel) --");
    for &kk_ in &[8usize, 2] {
        println!("  [closed form validated at sigma order {}]", kk_);
        for &eps in &[0.1_f64, 0.5, 2.0] {
        let sm = Sm::new(eps, kk_);
        let mut max_p1 = 0.0_f64;
        let mut max_p2 = 0.0_f64;
        let mut worst_s1 = 0.0_f64;
        let mut worst_s2 = 0.0_f64;
        for &s in &[0.0_f64, 0.1, 0.3, 0.5, 1.0, 2.0, 4.0, 6.0] {
            let cf1 = phibar_hat_cf(s, eps, kk_);
            let sp1 = phibar_hat(&sm, s, false);
            let cf2 = phibar2_hat_cf(s, eps, kk_);
            let sp2 = phibar2_hat(&sm, s, false);
            let e1 = (cf1 - sp1).abs();
            let e2 = (cf2 - sp2).abs();
            if e1 > max_p1 { max_p1 = e1; worst_s1 = s; }
            if e2 > max_p2 { max_p2 = e2; worst_s2 = s; }
        }
        println!(
            "eps={:.2}: max|Phi_cf - Phi_simpson| = {:.3e} (at s={}),  max|Phi2_cf - Phi2_simpson| = {:.3e} (at s={})",
            eps, max_p1, worst_s1, max_p2, worst_s2
        );
        }
    }

    // ---- normalization / moments ----
    println!("\n-- moments (Simpson) --");
    for &eps in &[0.1_f64, 0.5, 2.0] {
        let sm = Sm::new(eps, k);
        for sqrtkern in [false, true] {
            let n2 = norm2(&sm, sqrtkern);
            let n4 = norm4(&sm, sqrtkern);
            println!("eps={:.2} sqrtkern={}  int phi^2 = {:.9}  int phi^4 = {:.9}", eps, sqrtkern, n2, n4);
        }
    }

    // ---- Claim 2.1 truncation: hard cutoff vs smoothed ----
    println!("\n-- Claim 2.1 (Poisson) truncation error --");
    {
        let k_hard = |s: f64| psi(C::real(s)).re;
        let k2_hard = |s: f64| psi2(C::real(s)).re;
        let gk = GridFn::from_fn(&k_hard, 0.005, 2500.0);
        let gk2 = GridFn::from_fn(&k2_hard, 0.005, 2500.0);
        for km in &[50_i64, 200, 2000] {
            println!("hard-cos   K=+-{:5}: max err = {:.3e}", km, poisson_err(&gk, &gk2, *km));
        }
        let eps300 = 300.0 / 203.0; // paper-realistic at T=300 (N=203)
        for (name, eps) in [("eps=0.1", 0.1_f64), ("eps=1.48 (T/N,T=300)", eps300)] {
            let sm = Sm::new(eps, k);
            let kk = |s: f64| phibar_hat(&sm, s, false);
            let kk2 = |s: f64| phibar2_hat(&sm, s, false);
            let gkk = GridFn::from_fn(&kk, 0.005, S_CUT);
            let gkk2 = GridFn::from_fn(&kk2, 0.005, S_CUT);
            for km in &[50_i64, 200] {
                println!("sm-cos {:<19} K=+-{:5}: max err = {:.3e}", name, km, poisson_err(&gkk, &gkk2, *km));
            }
        }
    }

    // ---- main table ----
    let ts = [100.0_f64, 200.0, 300.0, 600.0];
    println!("\n-- main: trW/N, ||W||^2_HS/N, bound/N, delta = bound/N - 0.67250070... --");
    println!(
        "{:<38} {:>5} {:>9} {:>10} {:>10} {:>10} {:>10}",
        "config", "N", "trW/N", "HS2/N", "HS2_an/N", "bound/N", "delta"
    );

    let mut eps_by_t: Vec<(f64, f64)> = Vec::new();
    for &t in &ts {
        let n = gams.iter().filter(|&&g| g >= t && g < 2.0 * t).count();
        eps_by_t.push((t, t / n as f64));
    }

    let gh = 0.01_f64;
    for &t in &ts {
        let n = gams.iter().filter(|&&g| g >= t && g < 2.0 * t).count();
        let eps_paper = t / n as f64;

        // 1. hard-cutoff reference (round-1 methodology, recomputed here; psi ~ 1/|s| decays
        // algebraically, so the reference grid must cover the whole window, |s| <= N ~ 472)
        {
            let k_hard = |s: f64| psi(C::real(s)).re;
            let k2_hard = |s: f64| psi2(C::real(s)).re;
            let gk = GridFn::from_fn(&k_hard, 0.005, 500.0);
            let gk2 = GridFn::from_fn(&k2_hard, 0.005, 500.0);
            let r = analyze(t, &gams, &gk, &gk2, psi2(C::real(0.0)).re);
            println!(
                "T={:<6.0} hard-cos (C^0 ref)             {:>5} {:>9.6} {:>10.6} {:>10.6} {:>10.6} {:>+10.6}",
                t, r.n, r.trn, r.hsn, r.hsn_an, r.boundn, r.delta
            );
        }
        // 2. smoothed cos, paper-realistic eps = T/N
        {
            let sm = Sm::new(eps_paper, k);
            let kk = |s: f64| phibar_hat(&sm, s, false);
            let kk2 = |s: f64| phibar2_hat(&sm, s, false);
            let gkk = GridFn::from_fn(&kk, 0.005, S_CUT);
            let gkk2 = GridFn::from_fn(&kk2, 0.005, S_CUT);
            let r = analyze(t, &gams, &gkk, &gkk2, norm2(&sm, false));
            println!(
                "T={:<6.0} c^inf-cos eps=T/N={:.3}         {:>5} {:>9.6} {:>10.6} {:>10.6} {:>10.6} {:>+10.6}",
                t, eps_paper, r.n, r.trn, r.hsn, r.hsn_an, r.boundn, r.delta
            );
        }
        // 3. smoothed cos, eps = 0.1
        {
            let sm = Sm::new(0.1, k);
            let kk = |s: f64| phibar_hat(&sm, s, false);
            let kk2 = |s: f64| phibar2_hat(&sm, s, false);
            let gkk = GridFn::from_fn(&kk, 0.005, S_CUT);
            let gkk2 = GridFn::from_fn(&kk2, 0.005, S_CUT);
            let r = analyze(t, &gams, &gkk, &gkk2, norm2(&sm, false));
            println!(
                "T={:<6.0} c^inf-cos eps=0.10             {:>5} {:>9.6} {:>10.6} {:>10.6} {:>10.6} {:>+10.6}",
                t, r.n, r.trn, r.hsn, r.hsn_an, r.boundn, r.delta
            );
        }
        // 4. smoothed cos, eps = 0.5
        {
            let sm = Sm::new(0.5, k);
            let kk = |s: f64| phibar_hat(&sm, s, false);
            let kk2 = |s: f64| phibar2_hat(&sm, s, false);
            let gkk = GridFn::from_fn(&kk, 0.005, S_CUT);
            let gkk2 = GridFn::from_fn(&kk2, 0.005, S_CUT);
            let r = analyze(t, &gams, &gkk, &gkk2, norm2(&sm, false));
            println!(
                "T={:<6.0} c^inf-cos eps=0.50             {:>5} {:>9.6} {:>10.6} {:>10.6} {:>10.6} {:>+10.6}",
                t, r.n, r.trn, r.hsn, r.hsn_an, r.boundn, r.delta
            );
        }
        // 5. literal paper kernel: sqrt(cos), paper-realistic eps = T/N
        {
            let sm = Sm::new(eps_paper, k);
            let kk = |s: f64| phibar_hat(&sm, s, true);
            let kk2 = |s: f64| phibar2_hat(&sm, s, true);
            let gkk = GridFn::from_fn(&kk, 0.005, S_CUT);
            let gkk2 = GridFn::from_fn(&kk2, 0.005, S_CUT);
            let r = analyze(t, &gams, &gkk, &gkk2, norm2(&sm, true));
            println!(
                "T={:<6.0} c^inf-sqrtcos eps={:.3}        {:>5} {:>9.6} {:>10.6} {:>10.6} {:>10.6} {:>+10.6}",
                t, eps_paper, r.n, r.trn, r.hsn, r.hsn_an, r.boundn, r.delta
            );
        }
    }

    // ---- independent consistency checks ----
    println!("\n-- consistency checks (Parseval |Phi_hat|^2 ~ int phi^2; tr(W^2) vs (VV^T)^2 decomposition) --");
    {
        for (name, t, eps, sqrtkern) in [
            ("hard-cos", 100.0, 0.0, false),
            ("c^inf-cos eps=0.1", 100.0, 0.1, false),
            ("c^inf-cos eps=T/N", 600.0, 600.0 / 472.0, false),
            ("c^inf-sqrtcos eps=T/N", 600.0, 600.0 / 472.0, true),
        ] {
            if name == "hard-cos" {
                let n2 = psi2(C::real(0.0)).re;
                // Parseval for hard cutoff: sum_s |Psi(s)|^2 ds vs int psi^2
                let ds = 0.01;
                let mut acc = 0.0;
                let mut s = 0.0;
                while s <= S_CUT {
                    let v = psi(C::real(s)).re;
                    acc += v * v * ds * 2.0;
                    s += ds;
                }
                let gk = GridFn::from_fn(&|x: f64| psi(C::real(x)).re, 0.005, 500.0);
                let gk2 = GridFn::from_fn(&|x: f64| psi2(C::real(x)).re, 0.005, 500.0);
                let r = analyze(t, &gams, &gk, &gk2, n2);
                println!(
                    "{} T={:4.0}: Parseval sum|Psi|^2 ds = {:.6} vs int psi^2 = {:.6};  trW-chk {:.1e}",
                    name, t, acc, n2, r.trw2_chk
                );
            } else {
                let sm = Sm::new(eps, k);
                let pv = parseval(&sm, sqrtkern);
                let n2 = norm2(&sm, sqrtkern);
                let gk = GridFn::from_fn(&|x: f64| phibar_hat(&sm, x, sqrtkern), 0.01, S_CUT);
                let gk2 = GridFn::from_fn(&|x: f64| phibar2_hat(&sm, x, sqrtkern), 0.01, S_CUT);
                let r = analyze(t, &gams, &gk, &gk2, n2);
                println!(
                    "{} T={:4.0}: Parseval = {:.6} vs int phi^2 = {:.6} (rel {:.2e});  tr(W^2)-vs-HS2 rel err {:.1e}",
                    name, t, pv, n2, (pv - n2).abs() / n2, r.trw2_chk
                );
            }
        }
    }

    // ---- window-functional Q(v) vs measured HS2_an: is the overshoot a window-shape effect? ----
    println!("\n-- window functional Q(v) = (int v^2 + 2 int_0^1 w (v*v)(w) dw)/(int v)^2  (v = phi^2) --");
    {
        // sanity: hard-cos v = cos^2(sqrt2 u) 1_{|u|<=1/2} must give Q = 1.32750
        let q_hard = q_window(&|u: f64| {
            if u.abs() > 0.5 { 0.0 } else { (SQRT_2 * u).cos().powi(2) }
        });
        println!("Q(cos^2 1_{{|u|<=1/2}}) = {:.9}   (target 1/2+(1/sqrt2)cot(1/sqrt2) = {:.9})", q_hard, c_hs);
        for (name, eps, sqrtkern) in [
            ("c^inf-cos eps=0.1", 0.1, false),
            ("c^inf-cos eps=0.5", 0.5, false),
            ("c^inf-cos eps=T/N(T=600)", 600.0 / 472.0, false),
            ("c^inf-sqrtcos eps=T/N(T=600)", 600.0 / 472.0, true),
        ] {
            let sm = Sm::new(eps, k);
            let v = |u: f64| sm.phi2(u, sqrtkern);
            let q = q_window(&v);
            println!("{}: Q(window) = {:.6}   (target for this window shape)", name, q);
        }
    }

    // ---- one spectral check: T=600, cos eps=T/N ----
    println!("\n-- spectral check T=600, c^inf-cos eps=T/N --");
    {
        let t = 600.0_f64;
        let n = gams.iter().filter(|&&g| g >= t && g < 2.0 * t).count();
        let eps_paper = t / n as f64;
        let sm = Sm::new(eps_paper, k);
        let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
        let s_rho: Vec<f64> = gwin.iter().map(|&g| (g - t) * (n as f64) / t).collect();
        let kk = |s: f64| phibar_hat(&sm, s, false);
        let gkk = GridFn::from_fn(&kk, 0.01, S_CUT);
        let mut v = vec![vec![0.0; n]; n];
        for r in 0..n {
            let sr = s_rho[r];
            for k in 0..n {
                v[r][k] = gkk.eval(sr - k as f64);
            }
        }
        let vt = {
            let mut vt = vec![vec![0.0; n]; n];
            for i in 0..n {
                for j in 0..n {
                    vt[i][j] = v[j][i];
                }
            }
            vt
        };
        let g = matmul(&vt, &v);
        let n2 = norm2(&sm, false);
        let w: Vec<Vec<f64>> = g.iter().map(|row| row.iter().map(|&x| x / n2).collect()).collect();
        // power iteration for lambda_max + trace for the rank-vs-bound summary
        let mut x = vec![1.0; n];
        let mut lam = 0.0;
        for _ in 0..60 {
            let mut y = vec![0.0; n];
            for i in 0..n {
                for j in 0..n {
                    y[i] += w[i][j] * x[j];
                }
            }
            let nrm: f64 = y.iter().map(|v| v * v).sum::<f64>().sqrt();
            let lam_new = {
                let mut d = 0.0;
                for i in 0..n {
                    d += x[i] * y[i];
                }
                d / nrm
            };
            lam = lam_new;
            for v in y.iter_mut() {
                *v /= nrm;
            }
            x = y;
        }
        let tr: f64 = (0..n).map(|i| w[i][i]).sum();
        let min_eig = {
            // Gershgorin-ish: not exact; just report tr and lambda_max ratio info
            0.0
        };
        println!("lambda_max = {:.6}, trW/N = {:.6}, lambda_max/N = {:.6}", lam, tr / n as f64, lam / n as f64);
        println!("(rank = N expected; power iteration only gives lambda_max; min eig not computed here)");
        let _ = min_eig;
    }

    // ---- summary of eps per T ----
    println!("\n-- paper-realistic eps = T/N per T --");
    for (t, eps) in &eps_by_t {
        println!("T={:4.0}  N/T = {:.4}  eps = T/N = {:.4}", t, 1.0 / eps, eps);
    }
}
