// S1 margin probe v2 — stability-matched root analysis + full-series verification
// For each family: Aberth roots of R_N at several N; a nonreal root is GENUINE if
//   (a) |t| is stable (within 2%) across consecutive N, AND
//   (b) the infinite series F(t*) = Σ(-1)^k b_k t*^{2k} evaluates to ~0 at the t-root.
// Artifacts (section truncation) fail (b) and drift in (a).
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
    fn arg(self) -> f64 { self.im.atan2(self.re) }
}

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

fn margin_min(lb: &[f64], kmax: usize) -> f64 {
    let mut minm = f64::INFINITY;
    for k in 1..=kmax {
        let d = 2.0*lb[k] - lb[k-1] - lb[k+1];
        let t = 1.0 - (-d).exp().min(1e300);
        let m = t*(k as f64 + 1.0);
        if m < minm { minm = m; }
    }
    minm
}

// evaluate the infinite series F(t) = Σ(-1)^k b_k t^{2k} (log-space), return (Re, Im, converged)
fn full_series(lb: &[f64], t: C) -> (f64, f64, bool) {
    let mut re = 1.0f64; let mut im = 0.0f64; // k=0 term: b_0 = 1
    let mut maxterm = 0.0f64;
    let lnt_abs = (t.re*t.re + t.im*t.im).sqrt().ln();
    let arg = t.arg();
    for k in 1..600 {
        let lmag = lb[k] + 2.0*(k as f64)*lnt_abs;
        let mag = lmag.exp();
        if mag > maxterm { maxterm = mag; }
        let ang = 2.0*(k as f64)*arg;
        let c = C::new(mag*ang.cos(), mag*ang.sin());
        if k % 2 == 1 { re -= c.re; im -= c.im; } else { re += c.re; im += c.im; }
        if k > 20 && mag < 1e-15*maxterm { return (re, im, true); }
    }
    (re, im, false)
}

fn analyze(name: &str, lb: &[f64], Ns: &[usize]) {
    let mm = margin_min(lb, 400);
    println!("FAMILY {} | min t_k*(k+1) over k<=400 = {:.5}", name, mm);
    // collect nonreal roots per N: (|t|, argdeg)
    let mut per_n: Vec<Vec<(f64, f64)>> = vec![];
    for &N in Ns {
        let s_ln = -lb[N]/(2.0*N as f64);
        let mut lq: Vec<f64> = (0..=N).map(|k| lb[k] + 2.0*(k as f64)*s_ln).collect();
        let maxlog = lq.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let coeffs: Vec<f64> = (0..=N).map(|k| {
            let v = (lq[k] - maxlog).exp();
            if k % 2 == 0 { v } else { -v }
        }).collect();
        let S = s_ln.exp();
        let roots = aberth(&coeffs, N, 3.0, 500, 1e-13);
        let mut nr: Vec<(f64, f64)> = vec![];
        let (mut npos, mut nneg) = (0usize, 0usize);
        for &z in &roots {
            let at = S * z.abs().sqrt();
            if at > 0.8*S { continue; }
            let tol = 1e-7*(1.0 + z.re.abs());
            if z.im.abs() > tol { nr.push((at, z.arg()*180.0/PI/2.0)); } // arg(t) = arg(w)/2
            else if z.re < 0.0 { nneg += 1; } else { npos += 1; }
        }
        nr.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
        println!("  N={} S={:.1} | posreal={} negreal-w={} nonreal-w={} | nonreal|t|: {}",
            N, S, npos, nneg, nr.len(),
            nr.iter().map(|(t, a)| format!("{:.2}@{:.1}°", t, a)).collect::<Vec<_>>().join(" "));
        per_n.push(nr);
    }
    // stability: |t| within 2% across consecutive N; require present in >= 3 consecutive
    let mut stable: Vec<(f64, f64)> = vec![];
    for i in 0..per_n.len() {
        for &(t1, a1) in &per_n[i] {
            let mut chain = 1;
            for j in (i+1)..per_n.len() {
                let found = per_n[j].iter().any(|(t2, _)| (t2 - t1).abs() <= 0.02*t1);
                if found { chain += 1; } else { break; }
            }
            if chain >= 3 && !stable.iter().any(|(t0, _)| (t0 - t1).abs() <= 0.02*t1) {
                stable.push((t1, a1));
            }
        }
    }
    stable.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    for (t, a) in &stable {
        // verify with full series at t* = |t| e^{i a}
        let arg = a*PI/180.0;
        let tstar = C::new(t*arg.cos(), t*arg.sin());
        let (re, im, conv) = full_series(lb, tstar);
        let mag = (re*re + im*im).sqrt();
        println!("  STABLE nonreal |t|={:.3} arg={:.1}° | full-series |F(t*)|={:.2e} conv={} {}",
            t, a, mag, conv, if mag < 1e-6 { "<= GENUINE" } else { "<= ARTIFACT(series nonzero)" });
    }
    if stable.is_empty() { println!("  STABLE nonreal: none (all section artifacts or LP)"); }
}

fn main() {
    const M: usize = 602;
    // CONTROL: J0(2t)
    let mut lb = vec![0.0f64; M];
    for k in 1..M { lb[k] = -2.0*ln_fact(k); }
    analyze("CONTROL J0(2t) b=1/(k!)^2 margin 2 (LP!)", &lb, &[60, 80, 100, 120, 160]);

    // direct margin-c
    for &c in &[1.0, 1.0696, 1.3, 1.5, 1.7, 1.8, 1.9, 2.0, 2.1] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -c*(k as f64)*(k as f64).ln(); }
        analyze(&format!("DIRECT c={} (margin {})", c, c), &lb, &[60, 100, 140, 180]);
    }

    // perturbed margin 2 (stable nonreal seen in v1)
    for &(eps, w) in &[(0.01, 5.0), (0.05, 3.0), (0.05, 5.0)] {
        let mut lb = vec![0.0f64; M];
        for k in 1..M {
            let kf = k as f64;
            lb[k] = -2.0*kf*kf.ln() + (1.0 + eps*(w*kf.ln()).cos()).ln();
        }
        analyze(&format!("PERTURB c=2 eps={} w={}", eps, w), &lb, &[60, 100, 140]);
    }

    // mixed direct lam=0.5
    {
        let mut lb = vec![0.0f64; M];
        for k in 1..M { lb[k] = -2.0*(k as f64)*(k as f64).ln() + 0.5*(k as f64); }
        analyze("MIXED direct lam=0.5 (margin 2)", &lb, &[60, 100, 140]);
    }
    println!("DONE");
}
