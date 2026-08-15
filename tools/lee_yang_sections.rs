// lee_yang_sections.rs — g2-1: are Taylor sections of G(w) = Xi(1/(1-w)) disk-stable?
// Test of Lemma LY: all roots of G_N(w) = sum_{n<=N} c_n w^n satisfy |w| >= 1.
// Rust std only, f64. Build/run: rustc -O lee_yang_sections.rs -o /tmp/l && /tmp/l
use std::f64::consts::PI;

#[derive(Clone, Copy, Debug)]
struct C { re: f64, im: f64 }
impl C {
    fn new(re: f64, im: f64) -> C { C { re, im } }
    fn norm(self) -> f64 { (self.re * self.re + self.im * self.im).sqrt() }
}
impl std::ops::Add for C { type Output = C; fn add(self, o: C) -> C { C::new(self.re + o.re, self.im + o.im) } }
impl std::ops::Sub for C { type Output = C; fn sub(self, o: C) -> C { C::new(self.re - o.re, self.im - o.im) } }
impl std::ops::Mul for C { type Output = C; fn mul(self, o: C) -> C { C::new(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re) } }
impl std::ops::Div for C { type Output = C; fn div(self, o: C) -> C { let d = o.re * o.re + o.im * o.im; C::new((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d) } }

// Phi(u) = 2 * sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
// (verified form, wave8d ground truth; anchors b_0=xi(1/2)=0.4971207781883141, c_0=xi(1)=0.5)
fn phi(u: f64) -> f64 {
    let e2u = (2.0 * u).exp();
    let e5h = (2.5 * u).exp();
    let e9h = (4.5 * u).exp();
    let mut s = 0.0;
    for n in 1..=5 {
        let n2 = (n * n) as f64;
        let n4 = n2 * n2;
        s += (2.0 * PI * PI * n4 * e9h - 3.0 * PI * n2 * e5h) * (-PI * n2 * e2u).exp();
    }
    2.0 * s
}

// (P_n(x), P_n'(x))
fn legendre(n: usize, x: f64) -> (f64, f64) {
    if n == 0 { return (1.0, 0.0); }
    let (mut p0, mut p1) = (1.0f64, x);
    let (mut d0, mut d1) = (0.0f64, 1.0f64);
    for k in 1..n {
        let kk = k as f64;
        let p2 = ((2.0 * kk + 1.0) * x * p1 - kk * p0) / (kk + 1.0);
        let d2 = d0 + (2.0 * kk + 1.0) * p1;
        p0 = p1; p1 = p2; d0 = d1; d1 = d2;
    }
    (p1, d1)
}

// Gauss-Legendre nodes/weights mapped to (0,1)
fn gl(npts: usize) -> (Vec<f64>, Vec<f64>) {
    let mut x = vec![0.0; npts];
    let mut w = vec![0.0; npts];
    for i in 0..npts / 2 {
        let mut xi = (PI * (i as f64 + 0.75) / (npts as f64 + 0.5)).cos();
        for _ in 0..60 {
            let (p, d) = legendre(npts, xi);
            let dx = p / d;
            xi -= dx;
            if dx.abs() < 1e-16 { break; }
        }
        let (_, d) = legendre(npts, xi);
        let wi = 2.0 / ((1.0 - xi * xi) * d * d);
        x[i] = -xi; x[npts - 1 - i] = xi;
        w[i] = wi; w[npts - 1 - i] = wi;
    }
    if npts % 2 == 1 {
        let (_, d) = legendre(npts, 0.0);
        x[npts / 2] = 0.0; w[npts / 2] = 2.0 / (d * d);
    }
    for v in x.iter_mut() { *v = (*v + 1.0) / 2.0; }
    for v in w.iter_mut() { *v /= 2.0; }
    (x, w)
}

// b_k = M_k/(2k)!, M_k = 2 int_0^1 Phi(-ln x) (-ln x)^{2k} dx/x
fn bs(kmax: usize) -> Vec<f64> {
    let (x, w) = gl(512);
    let mut m = vec![0.0; kmax + 1];
    for j in 0..512 {
        let u = -x[j].ln();
        let p = phi(u);
        if p == 0.0 { continue; }
        let u2 = u * u;
        let mut pw = 1.0;
        for k in 0..=kmax {
            m[k] += w[j] * p * pw / x[j];
            pw *= u2;
        }
    }
    let mut b = vec![0.0; kmax + 1];
    for k in 0..=kmax {
        let mut f = 1.0f64;
        for j in 2..=(2 * k) { f *= j as f64; }
        b[k] = 2.0 * m[k] / f;
    }
    b
}

fn conv(a: &[f64], b: &[f64], n: usize) -> Vec<f64> {
    let mut r = vec![0.0; n + 1];
    for i in 0..=n {
        for j in 0..=(n - i) { r[i + j] += a[i] * b[j]; }
    }
    r
}

// c_n = sum_k b_k [w^n] A^{2k}, A(w) = (1+w)/(2(1-w)) = 1/2 + w + w^2 + ...
fn coeffs(b: &[f64], n: usize) -> Vec<f64> {
    let mut a = vec![0.0; n + 1];
    a[0] = 0.5;
    for i in 1..=n { a[i] = 1.0; }
    let a2 = conv(&a, &a, n);
    let mut s = vec![0.0; n + 1];
    s[0] = 1.0;
    let mut c = vec![0.0; n + 1];
    let ksum = (2 * n + 10).min(b.len() - 1);
    for k in 0..=ksum {
        let bk = b[k];
        for i in 0..=n { c[i] += bk * s[i]; }
        if k < ksum { s = conv(&s, &a2, n); }
    }
    c
}

fn eval(p: &[C], z: C) -> C {
    let mut r = C::new(0.0, 0.0);
    for &c in p.iter().rev() { r = r * z + c; }
    r
}

fn roots(poly: &[f64], n: usize, iters: usize) -> (Vec<C>, f64) {
    let p: Vec<C> = poly.iter().map(|&v| C::new(v, 0.0)).collect();
    let mut z: Vec<C> = (0..n).map(|i| {
        let th = 2.0 * PI * (i as f64) / (n as f64) + 0.131 * (i as f64);
        C::new(1.3 * th.cos(), 1.3 * th.sin())
    }).collect();
    for _ in 0..iters {
        let mut md = 0.0;
        for i in 0..n {
            let pz = eval(&p, z[i]);
            let mut den = C::new(1.0, 0.0);
            for j in 0..n { if j != i { den = den * (z[i] - z[j]); } }
            let d = pz / den;
            z[i] = z[i] - d;
            md = if d.norm() > md { d.norm() } else { md };
        }
        if md < 1e-13 { break; }
    }
    let mut maxres = 0.0;
    for &zi in &z {
        let r = eval(&p, zi);
        if r.norm() > maxres { maxres = r.norm(); }
    }
    (z, maxres)
}

fn report(name: &str, c: &[f64], n: usize) {
    let (z, res) = roots(c, n, 3000);
    let mut mn = f64::MAX;
    let mut cnt = 0;
    let mut cnt2 = 0;
    for &zi in &z {
        let m = zi.norm();
        if m < mn { mn = m; }
        if m < 1.0 - 1e-9 { cnt += 1; }
        if m < 0.99 { cnt2 += 1; }
    }
    println!("{:>3} N={:2}  min|root|={:.8}  inside(1-1e-9):{}  inside(0.99):{}  maxres={:.1e}",
        name, n, mn, cnt, cnt2, res);
}

fn main() {
    let b = bs(65);
    println!("b[0]={:.12} (anchor xi(1/2)=0.4971207781883141)", b[0]);
    println!("b[1..4] = {:.6e} {:.6e} {:.6e} {:.6e}", b[1], b[2], b[3], b[4]);
    let c8 = coeffs(&b, 8);
    print!("c[0..=8] =");
    for v in &c8 { print!(" {:.6}", v); }
    println!();
    println!("(anchor: c_0 = sum_k b_k 4^-k should equal xi(1) = 0.5; got {:.12})", c8[0]);
    let sweep: Vec<usize> = vec![2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 30, 40];
    for &n in &sweep {
        let c = coeffs(&b, n);
        report("G", &c, n);
    }
    println!("-- planted-zero control: G~ = (1-2w)G, zero at w=1/2 --");
    for &n in &[6usize, 10, 16, 20, 30, 40] {
        let c = coeffs(&b, n);
        let mut cp = vec![0.0; n + 1];
        cp[0] = c[0];
        for i in 1..=n { cp[i] = c[i] - 2.0 * c[i - 1]; }
        report("G~", &cp, n);
    }
}
