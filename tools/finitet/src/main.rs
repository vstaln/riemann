// finitet: finite-T compressed Weil form W_T — numerical verification of the
// 67.25% structural claims (Claim 2.1, Lemmas 3.2, 3.3, 3.4 + hyperbolic plane).
//
// Idealized model per round-1 brief: phi_T(x) = psi(x*T/N), psi(u) = cos(sqrt2 u) 1_{|u|<=1/2}.
// Closed forms (e^{-2 pi i} convention):
//   psi(s)  = sin(1/sqrt2 - pi s)/(sqrt2 - 2 pi s) + sin(1/sqrt2 + pi s)/(sqrt2 + 2 pi s)
//   psi2(s) = sin(pi s)/(2 pi s) + 1/4 [ sin(sqrt2 - pi s)/(sqrt2 - pi s) + sin(sqrt2 + pi s)/(sqrt2 + pi s) ]
//   int psi^2 = 1/2 + sin(sqrt2)/(2 sqrt2)
// V[rho][k] = psi(s_rho - k),  s_rho = (gamma_rho - T)*N/T,  k = 0..N-1
// W_T = (1/int_psi2) * V^T V   (the T/(N int phi^2) prefactor cancels exactly)
use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};

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
    fn conj(self) -> C {
        C::new(self.re, -self.im)
    }
    fn abs2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
    fn sin(self) -> C {
        C::new(self.re.sin() * self.im.cosh(), self.re.cos() * self.im.sinh())
    }
}

// psi(s) = int_{-1/2}^{1/2} cos(sqrt2 u) e^{-2 pi i s u} du  (closed form, entire)
fn psi(s: C) -> C {
    let s2 = C::real(SQRT_2);
    let d1 = s2.sub(s.scale(2.0 * PI));
    let d2 = s2.add(s.scale(2.0 * PI));
    let mut t1 = C::real(FRAC_1_SQRT_2).sub(s.scale(PI)).sin().div(d1);
    if d1.abs2() < 1e-18 {
        t1 = C::real(0.5); // removable pole 2 pi s = sqrt2
    }
    let mut t2 = C::real(FRAC_1_SQRT_2).add(s.scale(PI)).sin().div(d2);
    if d2.abs2() < 1e-18 {
        t2 = C::real(0.5);
    }
    t1.add(t2)
}

// psi2(s) = transform of psi^2 at rescaled argument
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

// Jacobi eigenvalues of a real symmetric matrix (diagonal entries at the end)
fn jacobi_eig(a0: &[Vec<f64>]) -> Vec<f64> {
    let n = a0.len();
    let mut a = a0.to_vec();
    let mut sweeps = 0;
    loop {
        sweeps += 1;
        let mut off = 0.0;
        for i in 0..n {
            for j in i + 1..n {
                off += a[i][j] * a[i][j];
            }
        }
        if off < 1e-28 || sweeps > 60 {
            break;
        }
        for p in 0..n {
            for q in p + 1..n {
                let apq = a[p][q];
                if apq.abs() < 1e-300 {
                    continue;
                }
                let app = a[p][p];
                let aqq = a[q][q];
                let theta = (aqq - app) / (2.0 * apq);
                let t = if theta >= 0.0 {
                    1.0 / (theta + (theta * theta + 1.0).sqrt())
                } else {
                    1.0 / (theta - (theta * theta + 1.0).sqrt())
                };
                let c = 1.0 / (t * t + 1.0).sqrt();
                let s = t * c;
                for k in 0..n {
                    if k != p && k != q {
                        let akp = a[k][p];
                        let akq = a[k][q];
                        a[k][p] = c * akp - s * akq;
                        a[p][k] = a[k][p];
                        a[k][q] = s * akp + c * akq;
                        a[q][k] = a[k][q];
                    }
                }
                a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq;
                a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq;
                a[p][q] = 0.0;
                a[q][p] = 0.0;
            }
        }
    }
    (0..n).map(|i| a[i][i]).collect()
}

// least squares slope/intercept + residual sum of squares for y ~ a*x + b
fn fit(x: &[f64], y: &[f64]) -> (f64, f64, f64) {
    let n = x.len() as f64;
    let mx = x.iter().sum::<f64>() / n;
    let my = y.iter().sum::<f64>() / n;
    let mut num = 0.0;
    let mut den = 0.0;
    for i in 0..x.len() {
        num += (x[i] - mx) * (y[i] - my);
        den += (x[i] - mx) * (x[i] - mx);
    }
    let a = num / den;
    let b = my - a * mx;
    let rss: f64 = x
        .iter()
        .zip(y.iter())
        .map(|(xi, yi)| (yi - (a * xi + b)).powi(2))
        .sum();
    (a, b, rss)
}

fn main() {
    // ---- constants ----
    let int_psi2 = psi2(C::real(0.0)).re; // 1/2 + sin(sqrt2)/(2 sqrt2)
    let cot = FRAC_1_SQRT_2.tan().recip();
    let c_hs = 0.5 + FRAC_1_SQRT_2 * cot; // 1/2 + (1/sqrt2) cot(1/sqrt2)
    let c_bound = 1.5 - FRAC_1_SQRT_2 * cot; // 3/2 - (1/sqrt2) cot(1/sqrt2)
    let c1_star = SQRT_2 * FRAC_1_SQRT_2.tan() / (1.0 + FRAC_1_SQRT_2 * FRAC_1_SQRT_2.tan());
    println!("int psi^2                  = {:.15}", int_psi2);
    println!("HS const c=1/2+(1/sqrt2)cot = {:.15}  (brief's 0.75329 is actually c1* = 1/c)", c_hs);
    println!("c1* = sqrt2 tan/(1+u tan)   = {:.15}", c1_star);
    println!("1/c1*                       = {:.15}", 1.0 / c1_star);
    println!("bound const 3/2-(1/sqrt2)cot = {:.15}  (brief: 0.6725007036794116)", c_bound);

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
    println!("loaded {} zeros", gams.len());

    // ---- Claim 2.1 check: sum_k psi(s-k) psi(s'-k) = psi2(s-s') over Z ----
    // NOTE: idealized hard-cutoff phi_T has only O(1/omega) decay (cosine does not
    // vanish at +-N/2T), so the k-sum converges like 1/K (the paper's C-infinity
    // phi_T has |z|^{-2} decay -> O(1/K^2)). Report err at several K to show the law.
    let samples = [0.0_f64, 0.37, 1.9, 5.3, 12.7, 41.2, 3.14, 7.7];
    let mut c21_prev: f64 = 0.0;
    for &kmax in &[50_i64, 200, 2000] {
        let mut c21_err: f64 = 0.0;
        for &s in &samples {
            for &s2 in &samples {
                let mut sum = 0.0_f64;
                for k in -kmax..=kmax {
                    sum += psi(C::real(s - k as f64)).re * psi(C::real(s2 - k as f64)).re;
                }
                let target = psi2(C::real(s - s2)).re;
                c21_err = c21_err.max((sum - target).abs());
            }
        }
        let ratio = if kmax > 50 { c21_prev / c21_err } else { 0.0 };
        println!(
            "Claim 2.1 (Poisson) K=+-{:5}: max err = {:.3e}   (err ratio vs previous K = {:.1}x, expect ~K-ratio for O(1/K))",
            kmax, c21_err, ratio
        );
        c21_prev = c21_err;
    }

    // ---- main windows ----
    let ts = [100.0_f64, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0];
    let mut rows: Vec<(f64, usize, f64, f64, f64, f64)> = Vec::new(); // T, N, trN, hsn, boundN, delta
    for &t in &ts {
        let s_rho: Vec<f64> = {
            let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
            let n = gwin.len();
            gwin.iter().map(|&g| (g - t) * (n as f64) / t).collect()
        };
        let n = s_rho.len();
        if n == 0 {
            continue;
        }
        // V[rho][k] = psi(s_rho - k)
        let mut v = vec![vec![0.0; n]; n];
        for r in 0..n {
            for k in 0..n {
                v[r][k] = psi(C::real(s_rho[r] - k as f64)).re;
            }
        }
        // G = V^T V, W = G / int_psi2
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
        let w: Vec<Vec<f64>> = g.iter().map(|row| row.iter().map(|&x| x / int_psi2).collect()).collect();

        // 1. symmetry
        let mut asy = 0.0_f64;
        for i in 0..n {
            for j in 0..n {
                asy = asy.max((w[i][j] - w[j][i]).abs());
            }
        }
        // 3. trace
        let tr: f64 = (0..n).map(|i| w[i][i]).sum();
        let trn = tr / n as f64;
        // 4. HS norm, decomposed: HS2 = (1/int2)^2 sum_{rho,rho'} (VV^T)_{rho,rho'}^2
        let vvt = matmul(&v, &vt); // N x N, (VV^T)_{rho,rho'} = sum_k psi(s_rho-k) psi(s_rho'-k)
        let mut diag2 = 0.0_f64;
        let mut off2 = 0.0_f64;
        for r in 0..n {
            for r2 in 0..n {
                let x = vvt[r][r2] / int_psi2;
                if r == r2 {
                    diag2 += x * x;
                } else {
                    off2 += x * x;
                }
            }
        }
        let hsn = (diag2 + off2) / n as f64;
        // analytic approximation: (VV^T)_{rho,rho'} ~ psi2(s_rho - s_rho') [Claim 2.1, full k-sum]
        let mut off2_an = 0.0_f64;
        for r in 0..n {
            for r2 in 0..n {
                if r == r2 {
                    continue;
                }
                let x = psi2(C::real(s_rho[r] - s_rho[r2])).re / int_psi2;
                off2_an += x * x;
            }
        }
        let hsn_an = (n as f64 + off2_an) / n as f64;
        // 5. rank from Jacobi eigenvalues at several relative thresholds; report spectrum
        let eig = jacobi_eig(&w);
        let eig_sum: f64 = eig.iter().sum();
        let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
        let mut esort = eig.clone();
        esort.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let r1e6 = eig.iter().filter(|&&x| x > 1e-6 * lmax).count();
        let r1e8 = eig.iter().filter(|&&x| x > 1e-8 * lmax).count();
        let r1e10 = eig.iter().filter(|&&x| x > 1e-10 * lmax).count();
        let boundn = 2.0 * trn - hsn;
        let delta = boundn - c_bound;
        rows.push((t, n, trn, hsn, boundn, delta));
        println!(
            "T={:4.0} N={:4} | sym={:.1e} | trW/N={:.6} | HS2/N={:.6} (diag {:.4} + offdiag {:.4}) | HS2_an/N={:.6} | bound/N={:.6} delta={:+.6} | rank(e>1e-6)={} (1e-8)={} (1e-10)={} | tr-chk={:.1e} | eig5min={:.2e},{:.2e},{:.2e},{:.2e},{:.2e}",
            t, n, asy, trn, hsn, diag2 / n as f64, off2 / n as f64, hsn_an, boundn, delta, r1e6, r1e8, r1e10,
            (tr - eig_sum).abs(),
            esort[0] / lmax, esort[1] / lmax, esort[2] / lmax, esort[3] / lmax, esort[4] / lmax
        );
    }

    // ---- 6. error-term fits ----
    println!("\n-- finite-T deviation delta(T) = bound/N - 0.67250... --");
    for (t, n, trn, hsn, boundn, delta) in &rows {
        println!(
            "T={:4.0} N={:4} trW/N={:.6} HS2/N={:.6} bound/N={:.6} delta={:+.6}  delta*N={:+.4}",
            t, n, trn, hsn, boundn, delta, delta * (*n as f64)
        );
    }
    let tarr: Vec<f64> = rows.iter().map(|r| r.0).collect();
    let darr: Vec<f64> = rows.iter().map(|r| r.5).collect();
    let logt: Vec<f64> = tarr.iter().map(|&t| t.ln()).collect();
    for (name, x) in [
        ("1/log T", tarr.iter().map(|&t| 1.0 / t.ln()).collect::<Vec<_>>()),
        ("1/T     ", tarr.iter().map(|&t| 1.0 / t).collect::<Vec<_>>()),
        ("1/log^2T", tarr.iter().map(|&t| 1.0 / t.ln().powi(2)).collect::<Vec<_>>()),
        ("1/N     ", rows.iter().map(|r| 1.0 / r.1 as f64).collect::<Vec<_>>()),
    ] {
        let (a, b, rss) = fit(&x, &darr);
        println!("fit delta ~ a*x+b : x={}  a={:+.4} b={:+.6} rss={:.3e}", name, a, b, rss);
    }
    // log-log slope of |delta| vs 1/T (decay rate)
    let (a, _, rss) = fit(&tarr.iter().map(|&t| -t.ln()).collect::<Vec<_>>(), &darr.iter().map(|d| d.abs().ln()).collect::<Vec<_>>());
    println!("log|delta| ~ a*log(1/T)+b : a={:.4} (decay rate in 1/T), rss={:.3e}", a, rss);
    let (a2, _, _) = fit(&logt.iter().map(|l| -l).collect::<Vec<_>>(), &darr.iter().map(|d| d.abs().ln()).collect::<Vec<_>>());
    println!("log|delta| ~ a*log(1/log T)+b : a={:.4} (decay rate in 1/log T)", a2);

    // ---- 7. synthetic off-line pair ----
    println!("\n-- synthetic off-line pair (T=200, first zero in window, beta=0.3) --");
    let t = 200.0_f64;
    let beta = 0.3_f64;
    let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
    let n = gwin.len();
    let gamma = gwin[0];
    let s = (gamma - t) * (n as f64) / t;
    let imb = -beta * (n as f64) / t; // s_rho = s + i*imb
    let v: Vec<C> = (0..n).map(|k| psi(C::new(s - k as f64, imb))).collect();
    let wv: Vec<C> = (0..n).map(|k| psi(C::new(s - k as f64, -imb))).collect();
    let mut conj_err = 0.0_f64;
    for k in 0..n {
        conj_err = conj_err.max((wv[k].re - v[k].conj().re).abs().max((wv[k].im - v[k].conj().im).abs()));
    }
    println!("gamma={:.3} s={:.3} beta*N/T={:.4} | max|v_(1-rho) - conj(v_rho)| = {:.3e}", gamma, s, beta * n as f64 / t, conj_err);
    // pair form M = v v^T + conj(v) conj(v)^T = 2(a a^T - b b^T), a=Re v, b=Im v
    let a: Vec<f64> = v.iter().map(|c| c.re).collect();
    let b: Vec<f64> = v.iter().map(|c| c.im).collect();
    let aa: f64 = a.iter().map(|x| x * x).sum();
    let bb: f64 = b.iter().map(|x| x * x).sum();
    let ab: f64 = a.iter().zip(b.iter()).map(|(x, y)| x * y).sum();
    let trg = 2.0 * (aa - bb);
    let detg = -4.0 * (aa * bb - ab * ab);
    let disc = (trg * trg - 4.0 * detg).max(0.0);
    let lam_p = (trg + disc.sqrt()) / 2.0;
    let lam_m = (trg - disc.sqrt()) / 2.0;
    println!(
        "2x2 Gram (basis a=Re v, b=Im v): tr={:+.6} det={:+.6} -> eigenvalues {{ {:+.6}, {:+.6} }} (hyperbolic (1,1) iff one >0 one <0)",
        trg, detg, lam_p, lam_m
    );
    // direct: nonzero eigenvalues of full N x N real symmetric M
    // M = 2(aa^T - bb^T); build and jacobi
    let mut m = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            m[i][j] = 2.0 * (a[i] * a[j] - b[i] * b[j]);
        }
    }
    let meig = jacobi_eig(&m);
    let mut nz: Vec<f64> = meig.iter().copied().filter(|&x| x.abs() > 1e-10).collect();
    nz.sort_by(|x, y| x.abs().partial_cmp(&y.abs()).unwrap());
    println!("full M eigenvalues (nonzero, |.|>1e-10): {} -> {:+.6}, {:+.6}", nz.len(), nz[nz.len()-2], nz[nz.len()-1]);
    println!("n+(M) = {}, n-(M) = {}  (Claim 2.3: off-line pairs give one positive direction each)",
        meig.iter().filter(|&&x| x > 1e-10).count(),
        meig.iter().filter(|&&x| x < -1e-10).count());
}

