// integral_handle_probe.rs — tests the "integral-of-h_u superposition" handle.
// Build/run: rustc -O tools/integral_handle_probe.rs -o /tmp/ihp && /tmp/ihp
// (A) h_u circle-stability formula sanity: |(u-i*th)/(u+i*th)| == 1.
// (B) KILLER: two-term positive superposition cosh(z)+eps*cosh(2z), Re z > 0.05.
//     Exact prediction: interior zeros iff 0<eps<1, Re z = arccosh((1+sqrt(1+8e^2))/(4e)),
//     Im z = pi. None for eps>=1. Verify by grid+Newton and against the exact value.
// (C) Rouche robustness of the eps=0.7 zero under weight perturbation.
// (D) random 3-term positive superpositions (u in {0.5,1,1.5,2}): interior-zero rate.
use std::f64::consts::PI;

fn c(a: f64, b: f64) -> (f64, f64) { (a, b) }
fn cadd(a: (f64, f64), b: (f64, f64)) -> (f64, f64) { (a.0 + b.0, a.1 + b.1) }
fn cmul(a: (f64, f64), b: (f64, f64)) -> (f64, f64) { (a.0 * b.0 - a.1 * b.1, a.0 * b.1 + a.1 * b.0) }
fn cdiv(a: (f64, f64), b: (f64, f64)) -> (f64, f64) {
    let d = b.0 * b.0 + b.1 * b.1;
    ((a.0 * b.0 + a.1 * b.1) / d, (a.1 * b.0 - a.0 * b.1) / d)
}
fn cabs2(a: (f64, f64)) -> f64 { a.0 * a.0 + a.1 * a.1 }
fn ccosh(z: (f64, f64)) -> (f64, f64) { (z.0.cosh() * z.1.cos(), z.0.sinh() * z.1.sin()) }
fn csinh(z: (f64, f64)) -> (f64, f64) { (z.0.sinh() * z.1.cos(), z.0.cosh() * z.1.sin()) }

fn wabs(z: (f64, f64)) -> f64 {
    // |w| = |(zeta-1)/(zeta+1)| for zeta = a+ib, a>0
    ((z.0 - 1.0).powi(2) + z.1.powi(2)).sqrt() / ((z.0 + 1.0).powi(2) + z.1.powi(2)).sqrt()
}

// grid + Newton scan for zeros with Re z > 0.05; returns sorted-by-Re unique zeros.
fn scan<F1: Fn((f64, f64)) -> (f64, f64), F2: Fn((f64, f64)) -> (f64, f64)>(f: &F1, fd: &F2) -> Vec<(f64, f64)> {
    let mut found: Vec<(f64, f64)> = Vec::new();
    let mut re = 0.05f64;
    while re <= 4.5 {
        let mut im = 0.05f64;
        while im <= 12.0 {
            let mut z = (re, im);
            let mut ok = true;
            for _ in 0..80 {
                let fv = f(z);
                if cabs2(fv).sqrt() < 1e-13 { ok = true; break; }
                let dv = fd(z);
                let d2 = cabs2(dv);
                if d2 < 1e-30 { ok = false; break; }
                let nz = cadd(z, cdiv(c(-fv.0, -fv.1), dv)); // z - f/f'
                if cabs2(nz).sqrt() > 200.0 { ok = false; break; }
                z = nz;
            }
            if ok && f(z).0.abs() < 1e-11 && f(z).1.abs() < 1e-11 && z.0 > 0.05 {
                if !found.iter().any(|w| (w.0 - z.0).abs() < 1e-3 && (w.1 - z.1).abs() < 1e-2) {
                    found.push(z);
                }
            }
            im += 0.25;
        }
        re += 0.2;
    }
    found.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    found
}

fn main() {
    println!("== A: h_u zero formula sanity: |(u-i*th)/(u+i*th)| ==");
    for &u in &[0.1f64, 0.5, 1.0, 2.0, 5.0] {
        for k in 0..3 {
            let th = (PI / 2.0 + PI * k as f64) / u;
            let w = cdiv(c(u, -th), c(u, th));
            println!("  u={} k={} |w|={:.15}", u, k, cabs2(w).sqrt());
        }
    }

    println!("\n== B: two-term cosh(z)+eps*cosh(2z): interior zeros (Re z>0.05) ==");
    let mut eps_list: Vec<f64> = Vec::new();
    let mut e = 0.05f64;
    while e <= 1.5 { eps_list.push(e); e += 0.05; }
    for &eps in &[0.7f64, 1.0] { eps_list.push(eps); }
    eps_list.sort_by(|a, b| a.partial_cmp(b).unwrap());
    eps_list.dedup();
    let mut min_re_overall = f64::MAX;
    let mut arg_at_min = (0.0, 0.0);
    for &eps in &eps_list {
        let f = |z| cadd(ccosh(z), cmul(c(eps, 0.0), ccosh(cmul(c(2.0, 0.0), z))));
        let fd = |z| cadd(csinh(z), cmul(c(2.0 * eps, 0.0), csinh(cmul(c(2.0, 0.0), z))));
        let zs = scan(&f, &fd);
        if zs.is_empty() {
            println!("  eps={:.2}: no interior zero (Re>0.05)", eps);
        } else {
            let z0 = zs[0];
            let exact = if eps < 1.0 {
                let t = (1.0 + (1.0 + 8.0 * eps * eps).sqrt()) / (4.0 * eps);
                t.acosh()
            } else { 0.0 };
            println!(
                "  eps={:.2}: min Re z={:.6} (Im={:.4}, |w|={:.4}, n={}) | exact arccosh={:.6}",
                eps, z0.0, z0.1, wabs(z0), zs.len(), exact
            );
            if z0.0 < min_re_overall { min_re_overall = z0.0; arg_at_min = z0; }
        }
    }
    println!("  -> overall min Re z over eps-scan: {:.6} at z={:.3},{:.3}", min_re_overall, arg_at_min.0, arg_at_min.1);

    println!("\n== C: Rouche robustness at eps=0.7 zero (a=arccosh(1.14936..), b=pi) ==");
    let a0: f64 = ((1.0f64 + (1.0f64 + 8.0f64 * 0.49f64).sqrt()) / 2.8f64).acosh();
    println!("  exact a = arccosh((1+sqrt(1+8*0.49))/2.8) = {:.9}", a0);
    for &e2 in &[0.65f64, 0.70, 0.75] {
        let z0 = (a0, PI);
        let fz = cadd(ccosh(z0), cmul(c(e2, 0.0), ccosh(cmul(c(2.0, 0.0), z0))));
        let fd = cadd(csinh(z0), cmul(c(2.0 * e2, 0.0), csinh(cmul(c(2.0, 0.0), z0))));
        println!("  eps={}: |f(z0)|={:.3e}  |f'(z0)|={:.3e}  (|w(z0)|={:.4})", e2, cabs2(fz).sqrt(), cabs2(fd).sqrt(), wabs(z0));
    }

    println!("\n== D: random 3-term positive superpositions, u in {{0.5,1,1.5,2}} ==");
    let us = [0.5f64, 1.0, 1.5, 2.0];
    let mut seed: u64 = 12345;
    let mut rnd = || {
        seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        (seed >> 33) as f64 / (1u64 << 31) as f64
    };
    let mut fail = 0usize;
    let mut min_re_d = f64::MAX;
    for trial in 0..40 {
        let mut wts = [0f64; 3];
        let mut uu = [0f64; 3];
        for i in 0..3 { wts[i] = rnd() + 0.05; uu[i] = us[(rnd() * 4.0) as usize]; }
        let f = |z| {
            let mut acc = (0.0, 0.0);
            for i in 0..3 { acc = cadd(acc, cmul(c(wts[i], 0.0), ccosh(cmul(c(uu[i], 0.0), z)))); }
            acc
        };
        let fd = |z| {
            let mut acc = (0.0, 0.0);
            for i in 0..3 { acc = cadd(acc, cmul(c(wts[i] * uu[i], 0.0), csinh(cmul(c(uu[i], 0.0), z)))); }
            acc
        };
        let zs = scan(&f, &fd);
        if !zs.is_empty() {
            fail += 1;
            min_re_d = min_re_d.min(zs[0].0);
            if fail <= 4 {
                println!(
                    "  trial {}: w={:+.3},{:+.3},{:+.3} u={},{},{} -> Re z={:.4}, |w|={:.4}",
                    trial, wts[0], wts[1], wts[2], uu[0] as i64, uu[1] as i64, uu[2] as i64, zs[0].0, wabs(zs[0])
                );
            }
        }
    }
    println!("  -> {} of 40 trials had interior zeros; min Re z = {:.4}", fail, min_re_d);

    println!("\n== E: control calibration: (1-z)^3+(1+z)^3 = 2+6z^2, |z|=1/sqrt(3)=0.5774 (disk-variable known) ==");
    println!("  (analytic, no scan needed): zeta-root of 1+zeta^3 at e^(i*pi/3): Re=0.5, |w|=|tan(pi/6)|={:.6}", 1.0 / 3.0f64.sqrt());
}
