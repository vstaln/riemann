// stieltjes_sfrac_controls.rs v3 — WALL test for the Stieltjes S-fraction lever (g1-2).
// Models = explicit zero data: s_m = 2 * Re(Sum_l w_l^m), w_l = rho_l^-1.
// Criterion (Stieltjes/Wall Ch.IX): (s_m) is a_0-free Stieltjes iff
//   H_n = det[s_{i+j+2}] > 0 AND K_n = det[s_{i+j+3}] > 0 for all n,
//   iff the minus-convention S-fraction f = (s_1 z)/(1 - q_1 z/(1 - q_2 z/(1-...)))
//   has all q_k > 0. Primary numerics: Bareiss fraction-free determinant (stable, no
//   pivot-sign flips) on the r-scaled matrix M_ij = s_{i+j+off} * r^{-(i+j)} (positive
//   scaling preserves sign). Cross-check: reciprocal-iteration S-fraction coefficients.
// rustc -O stieltjes_sfrac_controls.rs -o stieltjes_sfrac_controls && ./stieltjes_sfrac_controls

use std::f64::consts::PI;

#[derive(Clone, Copy)]
struct C { re: f64, im: f64 }

fn cpow(w: C, m: usize) -> C {
    let r = (w.re*w.re + w.im*w.im).sqrt();
    if r == 0.0 { return C { re: 0.0, im: 0.0 }; }
    let th = w.im.atan2(w.re);
    let rr = r.powf(m as f64);
    C { re: rr * (m as f64 * th).cos(), im: rr * (m as f64 * th).sin() }
}

fn s_series(ws: &[C], mmax: usize) -> Vec<f64> {
    let mut s = vec![0.0f64; mmax + 1];
    for &w in ws {
        for m in 1..=mmax { s[m] += 2.0 * cpow(w, m).re; }
    }
    s
}

// Bareiss fraction-free det of (n+1)x(n+1). Returns (det, zero_flag); det sign is the
// exact sign unless the matrix is nearly singular (then |det| ~ 0 and sign unreliable).
fn det_bareiss(mut m: Vec<Vec<f64>>, n: usize) -> (f64, bool) {
    let mut prev = 1.0f64;
    for k in 0..n {
        if m[k][k].abs() < 1e-300 { return (0.0, true); }
        for i in (k + 1)..=n {
            for j in (k + 1)..=n {
                m[i][j] = (m[k][k] * m[i][j] - m[i][k] * m[k][j]) / prev;
            }
        }
        prev = m[k][k];
    }
    if !m[n][n].is_finite() { return (0.0, true); }
    (m[n][n], m[n][n].abs() < 1e-280)
}

fn hankel_scan(s: &[f64], n: usize, offset: usize, r: f64) -> (i64, f64, bool) {
    // first n with det <= 0; returns (n, sign, zeroflag); -1 if all positive
    let ln_r = r.ln();
    for nn in 0..=n {
        let dim = nn + 1;
        let mut m = vec![vec![0.0f64; dim]; dim];
        for i in 0..dim {
            for j in 0..dim {
                let k = offset + i + j;
                m[i][j] = (s[k] / s[offset]) * (-(i as f64 + j as f64) * ln_r).exp();
            }
        }
        let (d, zf) = det_bareiss(m, nn);
        if d <= 0.0 { return (nn as i64, d, zf); }
    }
    (-1, 1.0, false)
}

// minus-convention S-fraction coefficients q_1..q_n (reciprocal iteration); (q, term_k)
fn sfrac_coeffs(s: &[f64], n: usize) -> (Vec<f64>, usize) {
    let mut l = n + 3;
    let a: Vec<f64> = (0..l).map(|i| if i == 0 { 1.0 } else { s[i + 1] / s[1] }).collect();
    let mut fser = {
        let mut r = vec![0.0f64; l];
        r[0] = 1.0;
        for i in 1..l {
            let mut acc = 0.0;
            for j in 1..=i { acc += a[j] * r[i - j]; }
            r[i] = -acc;
        }
        r
    };
    let mut q = vec![0.0f64; n + 1];
    let mut terminated = 0usize;
    for k in 1..=n {
        q[k] = -fser[1];
        if !fser[1].is_finite() || fser[1].abs() < 1e-12 { terminated = k; break; }
        let g: Vec<f64> = (0..l - 1).map(|i| if i == 0 { q[k] } else { -fser[i + 1] }).collect();
        if g[0].abs() < 1e-300 { terminated = k; break; }
        let gg: Vec<f64> = g.iter().map(|x| x / g[0]).collect();
        // inverse of gg (const 1) length l-1
        let mut r = vec![0.0f64; l - 1];
        r[0] = 1.0;
        for i in 1..l - 1 {
            let mut acc = 0.0;
            for j in 1..=i { acc += gg[j] * r[i - j]; }
            r[i] = -acc;
        }
        fser = r;
        l -= 1;
    }
    (q, terminated)
}

fn report(name: &str, ws: &[C], n: usize) {
    let mmax = n + 5;
    let s = s_series(ws, mmax);
    let r = ws.iter().map(|w| (w.re*w.re + w.im*w.im).sqrt()).fold(0.0f64, f64::max);
    let (nh, dh, zh) = hankel_scan(&s, n, 2, r);
    let (nk, dk, zk) = hankel_scan(&s, n, 3, r);
    let (q, term) = sfrac_coeffs(&s, n);
    let mut first_neg = 0usize;
    let mut qfail = 0.0;
    for k in 1..=n {
        if q[k] < 0.0 { first_neg = k; qfail = q[k]; break; }
    }
    let pairs = ws.iter().filter(|w| w.im == 0.0).count() + ws.iter().filter(|w| w.im != 0.0).count() / 2;
    let artifact = first_neg > 0 && first_neg as usize >= pairs.saturating_sub(2);
    println!("MODEL {} (pairs={}): H: first det<=0 n={} (d={:.3e} zf={}) | K: first det<=0 n={} (d={:.3e} zf={}) | Sfrac first q<0 k={} (q={:.3e}){} | term={}",
        name, pairs, nh, dh, zh, nk, dk, zk,
        if first_neg > 0 { first_neg.to_string() } else { "NONE".into() },
        if first_neg > 0 { qfail } else { 0.0 },
        if artifact { " [ARTIFACT? near termination]" } else { "" }, term);
}

fn main() {
    let g: Vec<f64> = vec![
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
        40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
        59.347044, 60.831778, 65.112544, 67.079811, 69.546402, 72.067158,
        75.704691, 77.144840,
    ];
    let good: Vec<C> = g.iter().map(|x| C { re: 1.0 / (x * x), im: 0.0 }).collect();

    let mut toy: Vec<C> = vec![C { re: -1.0, im: 0.0 }];
    for j in 1..=30 { toy.push(C { re: 1.0 / ((j as f64 - 0.5) * PI).powi(2), im: 0.0 }); }

    let single = vec![C { re: 1.0 / 199.7, im: 0.0 }];
    let real20 = good.clone();

    let mut m3 = good.clone();
    m3.push(C { re: 1.0 / 2501.0, im: -50.0 / 2501.0 });
    m3.push(C { re: 1.0 / 2501.0, im: 50.0 / 2501.0 });

    let mut m4 = good.clone();
    let m4r = 1.0 + 1e12;
    m4.push(C { re: 1.0 / m4r, im: -1e6 / m4r });
    m4.push(C { re: 1.0 / m4r, im: 1e6 / m4r });

    let mut m5 = good.clone();
    m5.push(C { re: 0.0, im: -0.5 });
    m5.push(C { re: 0.0, im: 0.5 });

    let mut m6: Vec<C> = Vec::new();
    let a = 0.6f64; let b = 14.134725f64;
    let rho2 = (a*a - b*b).powi(2) + (2.0*a*b).powi(2);
    m6.push(C { re: (a*a - b*b) / rho2, im: -2.0*a*b / rho2 });
    m6.push(C { re: (a*a - b*b) / rho2, im: 2.0*a*b / rho2 });
    for j in 1..g.len() { m6.push(C { re: 1.0 / (g[j]*g[j]), im: 0.0 }); }

    // anchors
    let s_toy = s_series(&toy, 8);
    println!("ANCHOR toy: s1={:.10} s2={:.10} s3={:.10} | q1(=s2/s1)={:.10} (<0: {}) | K0=s3 (<0: {})",
        s_toy[1], s_toy[2], s_toy[3], s_toy[2]/s_toy[1], s_toy[2]/s_toy[1] < 0.0, s_toy[3] < 0.0);
    let s_single = s_series(&single, 8);
    println!("ANCHOR single: q1={:.10} (expect 1/199.7 = {:.10}, >0: {})",
        s_single[2]/s_single[1], 1.0/199.7, s_single[2]/s_single[1] > 0.0);

    report("TOY    (1+t^2)cos", &toy, 40);
    report("SINGLE real pair ", &single, 8);
    report("REAL20 zeta-zeros", &real20, 40);
    // SEP20: well-separated positive w's (pipeline accuracy check at high order)
    let sep20: Vec<C> = (0..20).map(|j| C { re: 0.5 * 0.68f64.powi(j as i32), im: 0.0 }).collect();
    report("SEP20 separated   ", &sep20, 40);
    report("PLANTED 1+50i    ", &m3, 40);
    report("PLANTED 1+1e6i   ", &m4, 40);
    report("PLANTED 2i       ", &m5, 40);
    report("PLANTED 0.6+14.13i", &m6, 40);
}
