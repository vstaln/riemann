// logprofile probe — boundary of the margin-2 approach-rate for LP.
// Family b_k(C,D) = k^{-C*k} * ln(k+2)^{-D*k}; margin t_k*k ~ C + D/ln k.
// Deficit-2 profile t_k*k = 2 - 2/ln k  <=>  (C,D) = (2,-2)  [coordinator-corrected sign].
// Reuses S1 probe machinery (tools/s1margin/probe.rs + probe3.rs, std-only):
//   t_k = 1 - exp(d2 log b_k), d2 = 2*lb[k]-lb[k-1]-lb[k+1]; margin reported as t_k*(k+1).
//   Section roots via Aberth-Ehrlich on R_N(w), w=(t/S)^2, S=exp(-lb[N]/(2N)); trust |t|<=0.7*S.
//   Genuine vs artifact via Newton polish on the INFINITE series (quadratic shrink => GENUINE).
// Modes: coarse | refine | xi | point C D
use std::f64::consts::PI;
use std::env;

#[derive(Clone, Copy, Debug)]
struct Cx { re: f64, im: f64 }
impl Cx {
    fn new(re: f64, im: f64) -> Cx { Cx { re, im } }
    fn add(self, o: Cx) -> Cx { Cx::new(self.re + o.re, self.im + o.im) }
    fn sub(self, o: Cx) -> Cx { Cx::new(self.re - o.re, self.im - o.im) }
    fn mul(self, o: Cx) -> Cx { Cx::new(self.re*o.re - self.im*o.im, self.re*o.im + self.im*o.re) }
    fn div(self, o: Cx) -> Cx {
        let n = o.re*o.re + o.im*o.im;
        Cx::new((self.re*o.re + self.im*o.im)/n, (self.im*o.re - self.re*o.im)/n)
    }
    fn abs(self) -> f64 { (self.re*self.re + self.im*self.im).sqrt() }
    fn arg(self) -> f64 { self.im.atan2(self.re) }
}

fn eval_poly(coeffs: &[f64], z: Cx) -> (Cx, Cx) {
    let n = coeffs.len() - 1;
    let mut p = Cx::new(coeffs[n], 0.0);
    let mut dp = Cx::new(0.0, 0.0);
    for k in (0..n).rev() {
        dp = dp.mul(z).add(p);
        p = p.mul(z).add(Cx::new(coeffs[k], 0.0));
    }
    (p, dp)
}

fn aberth(coeffs: &[f64], n: usize, r0: f64, max_iter: usize, tol: f64) -> Vec<Cx> {
    let mut z: Vec<Cx> = (0..n).map(|i| {
        let ang = 2.0*PI*(i as f64)/(n as f64) + 0.7/(n as f64);
        Cx::new(r0*ang.cos(), r0*ang.sin())
    }).collect();
    for _ in 0..max_iter {
        let mut max_delta = 0.0f64;
        let mut newz = z.clone();
        for i in 0..n {
            let (p, dp) = eval_poly(coeffs, z[i]);
            let mut corr = Cx::new(0.0, 0.0);
            if p.abs() > 1e-290 {
                let ratio = p.div(dp);
                let mut s = Cx::new(0.0, 0.0);
                for j in 0..n {
                    if j != i { s = s.add(z[i].sub(z[j]).inv()); }
                }
                let denom = Cx::new(1.0, 0.0).sub(ratio.mul(s));
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

impl Cx {
    fn inv(self) -> Cx { let n = self.re*self.re + self.im*self.im; Cx::new(self.re/n, -self.im/n) }
}

// margin stats: min t_k*(k+1) over k<=kmax; t_k*k at k=300; pointwise gap vs deficit-2 curve
fn margin_stats(lb: &[f64], kmax: usize) -> (f64, f64, f64, f64) {
    let mut minm = f64::INFINITY;
    let mut t300 = 0.0; let mut mingap = f64::INFINITY;
    for k in 1..=kmax {
        let d = 2.0*lb[k] - lb[k-1] - lb[k+1];
        let t = 1.0 - (-d).exp().min(1e300);
        let m = t*(k as f64 + 1.0);
        if m < minm { minm = m; }
        if k == 300 { t300 = t*(k as f64); }
        let gap = t*(k as f64) - (2.0 - 2.0/(k as f64).ln());
        if k >= 10 && gap < mingap { mingap = gap; }
    }
    (minm, t300, mingap, 0.0)
}

// full-series Newton polish (probe3.rs): returns (verdict, final|F|)
fn polish(lb: &[f64], t: Cx) -> (String, f64) {
    let mut z = t;
    let mut steps: Vec<f64> = vec![];
    for _ in 0..14 {
        let (f, fp, conv) = f_and_fp(lb, z);
        if !conv { break; }
        let delta = f.div(fp);
        let d = delta.abs();
        steps.push(d);
        z = z.sub(delta);
        if d < 1e-13 { break; }
    }
    let (f, _, _) = f_and_fp(lb, z);
    let verdict = if steps.len() >= 2 && steps[steps.len()-1] < 1e-10 && steps[steps.len()-2] > steps[steps.len()-1] {
        "GENUINE"
    } else if steps.last().map(|&d| d < 1e-4).unwrap_or(false) {
        "likely GENUINE (slow)"
    } else {
        "ARTIFACT"
    };
    (verdict.to_string(), f.abs())
}

fn f_and_fp(lb: &[f64], z: Cx) -> (Cx, Cx, bool) {
    let lnt = z.abs().ln();
    let arg = z.arg();
    let mut f = Cx::new(1.0, 0.0);
    let mut fp = Cx::new(0.0, 0.0);
    let mut maxterm = 0.0f64;
    for k in 1..1200 {
        let lmag = lb[k] + 2.0*(k as f64)*lnt;
        let mag = lmag.exp();
        if mag > maxterm { maxterm = mag; }
        let ang = 2.0*(k as f64)*arg;
        let sign = if k % 2 == 1 { -1.0 } else { 1.0 };
        f = f.add(Cx::new(sign*mag*ang.cos(), sign*mag*ang.sin()));
        let dang = ang - arg;
        let dmag = (2.0*(k as f64))*(lb[k] + (2.0*(k as f64)-1.0)*lnt).exp();
        fp = fp.add(Cx::new(sign*dmag*dang.cos(), sign*dmag*dang.sin()));
        if k > 30 && mag < 1e-16*maxterm { return (f, fp, true); }
    }
    (f, fp, false)
}

fn lb_family(C: f64, D: f64, N: usize) -> Vec<f64> {
    let mut lb = vec![0.0f64; N];
    for k in 1..N {
        let kf = k as f64;
        lb[k] = -C*kf*kf.ln() - D*kf*((kf + 2.0).ln()).ln();
    }
    lb
}

// scan one (C,D): sections at Ns, polish candidates, print verdict line
fn scan_point(C: f64, D: f64, Ns: &[usize], label: &str) {
    const M: usize = 1300;
    let lb = lb_family(C, D, M);
    let (minm, t300, mingap, _) = margin_stats(&lb, 400);
    // asymptotic margin from form C + D/ln k at k=300:
    let asy = C + D/(300.0f64).ln();
    println!("POINT {} (C={},D={}) | min t_k*(k+1)={:.5} | k*t_k@300={:.4} | asy(C+D/ln300)={:.4} | min gap vs (2-2/lnk)={:+.4}",
        label, C, D, minm, t300, asy, mingap);
    let mut all_cands: Vec<(f64, f64)> = vec![]; // (|t|, arg_deg)
    for &N in Ns {
        let s_ln = -lb[N]/(2.0*N as f64);
        let mut lq: Vec<f64> = (0..=N).map(|k| lb[k] + 2.0*(k as f64)*s_ln).collect();
        let maxlog = lq.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let coeffs: Vec<f64> = (0..=N).map(|k| {
            let v = (lq[k] - maxlog).exp();
            if k % 2 == 0 { v } else { -v }
        }).collect();
        let roots = aberth(&coeffs, N, 3.0, 500, 1e-13);
        let S = s_ln.exp();
        let mut nc = 0;
        for &z in &roots {
            let at = S * z.abs().sqrt();
            let tol = 1e-7*(1.0 + z.re.abs());
            if at <= 0.7*S && (z.im.abs() > tol || z.re < 0.0) {
                // t-candidate: |t|=at, arg(t)=arg(w)/2
                let argdeg = 0.5*z.arg()*180.0/PI;
                all_cands.push((at, argdeg));
                nc += 1;
            }
        }
        println!("   N={}: {} candidate nonreal-t roots", N, nc);
    }
    // dedup by |t| within 2%
    all_cands.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    let mut dedup: Vec<(f64, f64)> = vec![];
    for c in all_cands {
        if let Some(l) = dedup.last() {
            if (c.0 - l.0).abs() < 0.02*l.0 { continue; }
        }
        dedup.push(c);
    }
    let mut n_gen = 0;
    let mut gen_list: Vec<String> = vec![];
    for (at, adeg) in &dedup {
        let a = adeg*PI/180.0;
        let z0 = Cx::new(at*a.cos(), at*a.sin());
        let (v, fabs) = polish(&lb, z0);
        if v == "GENUINE" || v.starts_with("likely") {
            n_gen += 1;
            gen_list.push(format!("|t|={:.3}@{}° (|F|={:.1e})", at, adeg, fabs));
        }
    }
    let verdict = if n_gen > 0 { "NON-LP" } else { "LP-consistent" };
    println!("   VERDICT: {} | genuine nonreal zeros: {}", verdict, if gen_list.is_empty() { "none".to_string() } else { gen_list.join("  ") });
    println!();
}

// log-parse a decimal like "1.234e-5" to f64 (handles underflow by keeping in log space)
fn logparse(s: &str) -> f64 {
    let s = s.trim();
    let (mant, exp) = match s.find('e') {
        Some(i) => (&s[..i], s[i+1..].parse::<f64>().unwrap_or(0.0)),
        None => (s, 0.0),
    };
    mant.parse::<f64>().unwrap().ln() + exp*(10.0f64).ln()
}

fn xi_profile() {
    // parse g02 table: k, M_k, b_k, gamma(k). b_k is col 2 (0-indexed).
    let txt = std::fs::read_to_string("research/notes/g02-moments-oracle-2026-08-18.txt").unwrap();
    let mut lb = vec![0.0f64; 302];
    for line in txt.lines() {
        let t: Vec<&str> = line.split_whitespace().collect();
        if t.len() < 4 { continue; }
        let k: usize = t[0].parse().unwrap();
        if k < 302 { lb[k] = logparse(t[2]); }
    }
    // sanity: t_100*100 should be ~1.5016 (g02 note table)
    for k in [50usize, 100, 150, 200, 250] {
        let d = 2.0*lb[k] - lb[k-1] - lb[k+1];
        let t = 1.0 - (-d).exp();
        let L = (k as f64).ln();
        let c = (2.0/PI).ln();
        let profile = 2.0 - 2.0/L - 2.0*(L.ln() - 1.0 - c)/(L*L);
        let Dk = (2.0 - t*(k as f64)) * L;
        println!("Xi k={} | k*t_k={:.5} | deficit-2 profile 2-2/lnk-2(lnL-1-c)/L^2={:.5} | D(k)=(2-k*t_k)lnk={:.4}",
            k, t*(k as f64), profile, Dk);
    }
    // full k=10..250 sample: min gap vs boundary curve 2-2/lnk
    let mut mingap = f64::INFINITY; let mut mink = 0;
    for k in 10..=250 {
        let d = 2.0*lb[k] - lb[k-1] - lb[k+1];
        let t = 1.0 - (-d).exp();
        let gap = t*(k as f64) - (2.0 - 2.0/(k as f64).ln());
        if gap < mingap { mingap = gap; mink = k; }
    }
    println!("Xi min gap vs (2-2/lnk) over k=10..250: {:.4} at k={}", mingap, mink);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let mode = if args.len() > 1 { args[1].as_str() } else { "coarse" };
    match mode {
        "coarse" => {
            let cs = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.4];
            let ds = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0];
            for &C in &cs { for &D in &ds {
                scan_point(C, D, &[80, 120], &format!("coarse"));
            }}
        }
        "refine" => {
            // dense near the expected boundary: C=2 line (decisive) + neighbors, D in [-3, 0]
            let cs = [1.85, 1.9, 1.95, 2.0, 2.05, 2.1];
            let ds = [-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0];
            for &C in &cs { for &D in &ds {
                scan_point(C, D, &[80, 120], &format!("refine"));
            }}
        }
        "point" => {
            let C: f64 = args[2].parse().unwrap();
            let D: f64 = args[3].parse().unwrap();
            scan_point(C, D, &[80, 120, 160], &format!("point"));
        }
        "xi" => xi_profile(),
        _ => println!("usage: probe [coarse|refine|point C D|xi]"),
    }
}
