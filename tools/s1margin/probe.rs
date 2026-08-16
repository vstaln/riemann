// S1 margin probe — does margin c (t_k ~ c/k) force real zeros of F(t)=Σ(-1)^k b_k t^{2k}?
// std-only Rust. Aberth–Ehrlich on R_N(w) = Σ (-1)^k q_k w^k, w = (t/S)^2, S = (1/b_N)^{1/(2N)}.
// F(t)=0  <=>  R(w)=0 with w=t^2/S^2.  t real  <=>  w real >= 0.
// Non-real t-zeros <=> non-real w OR real negative w.
use std::f64::consts::PI;

#[derive(Clone, Copy, Debug)]
struct C { re: f64, im: f64 }
impl C {
    fn new(re: f64, im: f64) -> C { C { re, im } }
    fn add(self, o: C) -> C { C::new(self.re + o.re, self.im + o.im) }
    fn sub(self, o: C) -> C { C::new(self.re - o.re, self.im - o.im) }
    fn mul(self, o: C) -> C { C::new(self.re*o.re - self.im*o.im, self.re*o.im + self.im*o.re) }
    fn inv(self) -> C { let n = self.re*self.re + self.im*self.im; C::new(self.re/n, -self.im/n) }
    fn div(self, o: C) -> C { self.mul(o.inv()) }
    fn abs(self) -> f64 { (self.re*self.re + self.im*self.im).sqrt() }
}

// ascending Horner: (P(z), P'(z)), coeffs[0..=n]
fn eval_poly(coeffs: &[f64], z: C) -> (C, C) {
    let n = coeffs.len() - 1;
    let mut p = C::new(coeffs[n], 0.0);
    let mut dp = C::new(0.0, 0.0);
    for k in (0..n).rev() {
        dp = dp.mul(z).add(p);
        p = p.mul(z).add(C::new(coeffs[k], 0.0));
    }
    (p, dp)
}

fn aberth(coeffs: &[f64], n: usize, r0: f64, max_iter: usize, tol: f64) -> Vec<C> {
    let mut z: Vec<C> = (0..n).map(|i| {
        let ang = 2.0*PI*(i as f64)/(n as f64) + 0.7/(n as f64);
        C::new(r0*ang.cos(), r0*ang.sin())
    }).collect();
    for _ in 0..max_iter {
        let mut max_delta = 0.0f64;
        let mut newz = z.clone();
        for i in 0..n {
            let (p, dp) = eval_poly(coeffs, z[i]);
            let mut corr = C::new(0.0, 0.0);
            if p.abs() > 1e-290 {
                let ratio = p.div(dp);
                let mut s = C::new(0.0, 0.0);
                for j in 0..n {
                    if j != i { s = s.add(z[i].sub(z[j]).inv()); }
                }
                let denom = C::new(1.0, 0.0).sub(ratio.mul(s));
                corr = if denom.abs() > 1e-14 { ratio.div(denom) } else { ratio };
                newz[i] = z[i].sub(corr);
            }
            let d = corr.abs();
            if d > max_delta { max_delta = d; }
        }
        z = newz;
        if max_delta < tol { break; }
    }
    // Newton polish
    for _ in 0..8 {
        for i in 0..n {
            let (p, dp) = eval_poly(coeffs, z[i]);
            if dp.abs() > 1e-300 { z[i] = z[i].sub(p.div(dp)); }
        }
    }
    z
}

fn ln_fact(m: usize) -> f64 {
    let mut s = 0.0;
    for j in 2..=m { s += (j as f64).ln(); }
    s
}

// margin stats from log-coeffs lb[0..=kmax+1]
fn margin_stats(lb: &[f64], kmax: usize) -> (f64, f64, f64) {
    let mut minm = f64::INFINITY;
    let mut t10 = 0.0; let mut tK = 0.0;
    for k in 1..=kmax {
        let d = 2.0*lb[k] - lb[k-1] - lb[k+1];
        let t = 1.0 - (-d).exp().min(1e300);
        let m = t*(k as f64 + 1.0);
        if m < minm { minm = m; }
        if k == 10 { t10 = t*(k as f64); }
        if k == kmax { tK = t*(k as f64); }
    }
    (minm, t10, tK)
}

fn analyze_family(name: &str, lb: &[f64], Ns: &[usize]) {
    let (minm, t10, tK) = margin_stats(lb, 100);
    println!("FAMILY {} | min t_k*(k+1)={:.5} | t_10*10={:.4} | t_100*100={:.4}", name, minm, t10, tK);
    for &N in Ns {
        let s_ln = -lb[N]/(2.0*N as f64);       // ln S
        let mut lq: Vec<f64> = (0..=N).map(|k| lb[k] + 2.0*(k as f64)*s_ln).collect();
        let maxlog = lq.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let mut coeffs: Vec<f64> = (0..=N).map(|k| {
            let v = (lq[k] - maxlog).exp();
            if k % 2 == 0 { v } else { -v }
        }).collect();
        let _ = &mut coeffs;
        let roots = aberth(&coeffs, N, 3.0, 500, 1e-13);
        let S = s_ln.exp();
        let mut n_nonreal = 0; let mut n_neg = 0; let mut n_pos = 0; let mut n_out = 0;
        let mut nonreal_list: Vec<(f64, f64, f64)> = vec![];
        let mut neg_list: Vec<f64> = vec![];
        let mut maxres = 0.0f64;
        for &z in &roots {
            let (p, _) = eval_poly(&coeffs, z);
            let r = p.abs() / (1.0 + z.abs().powi(N as i32));
            if r > maxres { maxres = r; }
            let tol = 1e-7*(1.0 + z.re.abs());
            let at = S * z.abs().sqrt();
            if at <= 0.7*S {
                if z.im.abs() > tol {
                    n_nonreal += 1; nonreal_list.push((z.re, z.im, at));
                } else if z.re < 0.0 {
                    n_neg += 1; neg_list.push(at);
                } else { n_pos += 1; }
            } else { n_out += 1; }
        }
        nonreal_list.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap());
        println!("  N={} S={:.2} | trusted posreal={} negreal-w={} nonreal-w={} | outside={} maxres={:.0e}",
            N, S, n_pos, n_neg, n_nonreal, n_out, maxres);
        if !nonreal_list.is_empty() {
            let s: Vec<String> = nonreal_list.iter().take(8).map(|(a,b,t)| format!("w={:.4}{:+.4}i |t|={:.2}", a, b, t)).collect();
            println!("    nonreal-w: {}", s.join("  "));
        }
        if !neg_list.is_empty() {
            let s: Vec<String> = neg_list.iter().take(8).map(|t| format!("|t|={:.2}", t)).collect();
            println!("    negreal-w (=> nonreal t): {}", s.join("  "));
        }
    }
}

fn main() {
    const M: usize = 202;
    // ---------- CONTROL: J0(2t), b_k = 1/(k!)^2 ----------
    let mut lb = vec![0.0f64; M];
    for k in 1..M { lb[k] = -2.0*ln_fact(k); }
    analyze_family("CONTROL J0(2t) b=1/(k!)^2 (margin 2, expect ALL real)", &lb, &[40, 60, 80]);

    // ---------- DIRECT margin-c families: b_k = k^{-c k} k^{-nu} ----------
    let cs = [0.5, 1.0, 1.0696, 1.5, 1.7, 1.9, 2.0, 2.1, 2.5, 3.0];
    for &c in &cs {
        for &nu in &[0.0] {
            let mut lb = vec![0.0f64; M];
            for k in 1..M { lb[k] = -c*(k as f64)*(k as f64).ln() - nu*(k as f64).ln(); }
            analyze_family(&format!("DIRECT c={} nu=0 (margin {})", c, c), &lb, &[60, 80, 100, 120]);
        }
    }
    // nu=1
    for &c in &[1.0696, 1.5, 2.0] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -c*(k as f64)*(k as f64).ln() - 1.0*(k as f64).ln(); }
        analyze_family(&format!("DIRECT c={} nu=1 (margin {})", c, c), &lb, &[60, 80, 100]);
    }

    // ---------- LITERAL task family: b_k = k^{-c k} / (2k)! (margin c+2) ----------
    for &c in &[0.5, 2.0, 3.0] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -c*(k as f64)*(k as f64).ln() - ln_fact(2*k); }
        analyze_family(&format!("LITERAL a_k=k^-{{ck}}, b=a/(2k)! c={} (b-margin {})", c, c+2.0), &lb, &[60, 80, 100]);
    }

    // ---------- PERTURBATION at margin 2: b_k = k^{-2k}(1 + eps cos(w ln k)) ----------
    for &eps in &[0.01, 0.05] {
        for &w in &[2.0, 3.0, 5.0] {
            let mut lb = vec![0.0f64; M];
            for k in 1..M {
                let kf = k as f64;
                lb[k] = -2.0*kf*kf.ln() + (1.0 + eps*(w*kf.ln()).cos()).ln();
            }
            analyze_family(&format!("PERTURB c=2 eps={} w={}", eps, w), &lb, &[60, 100]);
        }
    }

    // ---------- MIXED direct: b_k = exp(-2k ln k + lam k) (margin 2, lam shifts O(1/k)) ----------
    for &lam in &[0.5, 1.0] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -2.0*(k as f64)*(k as f64).ln() + lam*(k as f64); }
        analyze_family(&format!("MIXED direct lam={} (margin 2)", lam), &lb, &[60, 100]);
    }

    // ---------- MIXED literal: b_k = exp(-2k ln k + lam k)/(2k)! (margin 4) ----------
    for &lam in &[0.5] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -2.0*(k as f64)*(k as f64).ln() + lam*(k as f64) - ln_fact(2*k); }
        analyze_family(&format!("MIXED literal lam={} (b-margin 4)", lam), &lb, &[60, 100]);
    }
    println!("DONE");
}
