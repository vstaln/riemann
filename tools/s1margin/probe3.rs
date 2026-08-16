// S1 margin probe v3 — Newton polish on the FULL series F(t)=Σ(-1)^k b_k t^{2k} at candidate
// nonreal roots. The step |Δ|=|F/F'| shrinks quadratically iff the candidate is a genuine zero.
// Immune to cancellation noise in |F| (the ratio F/F' is accurate to ~1e-16 relative).
use std::f64::consts::PI;

#[derive(Clone, Copy, Debug)]
struct C { re: f64, im: f64 }
impl C {
    fn new(re: f64, im: f64) -> C { C { re, im } }
    fn add(self, o: C) -> C { C::new(self.re + o.re, self.im + o.im) }
    fn sub(self, o: C) -> C { C::new(self.re - o.re, self.im - o.im) }
    fn mul(self, o: C) -> C { C::new(self.re*o.re - self.im*o.im, self.re*o.im + self.im*o.re) }
    fn div(self, o: C) -> C {
        let n = o.re*o.re + o.im*o.im;
        C::new((self.re*o.re + self.im*o.im)/n, (self.im*o.re - self.re*o.im)/n)
    }
    fn abs(self) -> f64 { (self.re*self.re + self.im*self.im).sqrt() }
    fn arg(self) -> f64 { self.im.atan2(self.re) }
    fn scale(self, s: f64) -> C { C::new(self.re*s, self.im*s) }
}

// F(z) and F'(z) via the infinite series; returns (F, F', converged)
fn F_and_Fp(lb: &[f64], z: C) -> (C, C, bool) {
    let lnt = z.abs().ln();
    let arg = z.arg();
    let mut f = C::new(1.0, 0.0); // k=0
    let mut fp = C::new(0.0, 0.0);
    let mut maxterm = 0.0f64;
    for k in 1..1200 {
        let lmag = lb[k] + 2.0*(k as f64)*lnt;
        let mag = lmag.exp();
        if mag > maxterm { maxterm = mag; }
        let ang = 2.0*(k as f64)*arg;
        let sign = if k % 2 == 1 { -1.0 } else { 1.0 };
        f = f.add(C::new(sign*mag*ang.cos(), sign*mag*ang.sin()));
        let dang = ang - arg; // derivative: d/dz z^{2k} = 2k z^{2k-1}, |z^{2k-1}| = |z|^{2k-1}
        let dmag = (2.0*(k as f64))* (lb[k] + (2.0*(k as f64)-1.0)*lnt).exp();
        fp = fp.add(C::new(sign*dmag*dang.cos(), sign*dmag*dang.sin()));
        if k > 30 && mag < 1e-16*maxterm { return (f, fp, true); }
    }
    (f, fp, false)
}

fn polish(lb: &[f64], t: C, label: &str) {
    let mut z = t;
    let mut steps: Vec<f64> = vec![];
    for _ in 0..14 {
        let (f, fp, conv) = F_and_Fp(lb, z);
        if !conv { break; }
        let delta = f.div(fp);
        let d = delta.abs();
        steps.push(d);
        z = z.sub(delta);
        if d < 1e-13 { break; }
    }
    let (f, _, _) = F_and_Fp(lb, z);
    let s = steps.iter().map(|x| format!("{:.1e}", x)).collect::<Vec<_>>().join(" ");
    let verdict = if steps.len() >= 2 && steps[steps.len()-1] < 1e-10 && steps[steps.len()-2] > steps[steps.len()-1] {
        "GENUINE"
    } else if steps.last().map(|&d| d < 1e-4).unwrap_or(false) {
        "likely GENUINE (slow)"
    } else {
        "ARTIFACT"
    };
    println!("{} | start z={:.5}{:+.5}i | Newton steps: {} | final |F|={:.2e} | {}", label, t.re, t.im, s, f.abs(), verdict);
}

fn lb_direct(c: f64) -> Vec<f64> {
    let mut lb = vec![0.0f64; 1300];
    for k in 1..1300 { lb[k] = -c*(k as f64)*(k as f64).ln(); }
    lb
}
fn lb_perturb(eps: f64, w: f64) -> Vec<f64> {
    let mut lb = vec![0.0f64; 1300];
    for k in 1..1300 {
        let kf = k as f64;
        lb[k] = -2.0*kf*kf.ln() + (1.0 + eps*(w*kf.ln()).cos()).ln();
    }
    lb
}
fn lb_j0() -> Vec<f64> {
    let mut lb = vec![0.0f64; 1300];
    let mut lf = 0.0;
    for k in 1..1300 { lf += (k as f64).ln(); lb[k] = -2.0*lf; }
    lb
}

fn cand(t: f64, adeg: f64) -> C {
    let a = adeg*PI/180.0;
    C::new(t*a.cos(), t*a.sin())
}

fn main() {
    // CONTROL J0 — must be ALL artifacts (J0 provably LP)
    let lbj = lb_j0();
    println!("--- CONTROL J0(2t): candidates from section must be ARTIFACT ---");
    for (t, a) in [(19.213, 6.0), (21.171, 11.1), (23.252, 15.2)] {
        polish(&lbj, cand(t, a), &format!("J0 |t|={} @{}°", t, a));
    }
    println!("--- DIRECT margin-c families ---");
    for (c, cands) in &[
        (1.0, vec![(4.234, 30.9), (5.865, 36.5), (7.151, 38.8), (8.25, 40.1)]),
        (1.0696, vec![(4.471, 26.9), (6.372, 32.9), (7.891, 35.3), (9.195, 36.7)]),
        (1.3, vec![(5.194, 12.9), (8.248, 20.7), (10.762, 23.8), (12.998, 25.4), (14.461, 18.0), (15.736, 31.3)]),
        (1.5, vec![(10.173, 10.2), (13.872, 13.8), (17.275, 15.7), (20.164, 3.8)]),
        (1.7, vec![(17.632, 3.7), (22.658, 5.9), (27.220, 8.5), (29.372, 13.1)]),
        (1.8, vec![(31.639, 5.3), (34.879, 9.6), (37.378, 14.4), (40.309, 18.9)]),
        (1.9, vec![(38.14, 2.8), (51.472, 17.9)]),
        (2.0, vec![(50.834, 6.3), (55.459, 11.7), (60.856, 16.1)]),
    ] {
        let lb = lb_direct(*c);
        println!("FAMILY c={} (margin {})", c, c);
        for (t, a) in cands { polish(&lb, cand(*t, *a), &format!("  |t|={} @{}°", t, a)); }
    }
    println!("--- PERTURBED margin-2 ---");
    for &(eps, w, t, a) in &[(0.01, 5.0, 21.512, 23.1), (0.05, 3.0, 10.836, 13.5), (0.05, 5.0, 6.480, 15.1), (0.05, 5.0, 20.400, 38.6)] {
        let lb = lb_perturb(eps, w);
        polish(&lb, cand(t, a), &format!("  eps={} w={} |t|={} @{}°", eps, w, t, a));
    }
    println!("DONE");
}
