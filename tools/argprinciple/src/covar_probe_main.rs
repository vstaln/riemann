// covar_probe v2: full 4x4 covariance + phase-alignment structure.
//
// Object under test (agy Direction 2, matrix-valued minorant): the 2x2 minorant acts on
//   V(t) = (Re f, Im f'/theta'), f = (zeta*M)(1/2+it).
// We measure the FULL 4x4 covariance of (Re f, Im f, Re f'/theta', Im f'/theta') and the
// phase-concentration ratios. The SDP-constraint collapse mechanism (Conrey phase
// machinery): if M aligns the phase of zeta*M, then Im f ~ 0 relative to Re f, and any
// positive-definite matrix minorant collapses to scalar. Direct tests:
//   * |Im f|_rms / |Re f|_rms   (phase concentration of the mollified function)
//   * corr(Re f, Im f)          (1 => concentrated)
//   * corr(Re f, Im f'/theta')  (the rank-2 test from v1)
//   * corr(Im f, Re f'/theta')  (the conjugate rank-2 test)
//   * full 4x4 covariance matrix (what the minorant SDP would actually use)
//
// All zeta values certified EM; f' via finite difference (step 1e-3).

use std::f64::consts::PI;

mod zeta;
use zeta::*;

// certified EM evaluation of zeta(1/2+it), N chosen as in z_cert
fn zeta_val(t: f64) -> (f64, f64, f64) {
    let n = ((1.6 * t / (2.0 * PI)).ceil().max(10.0)) as usize;
    let lns: Vec<f64> = (0..n).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
    let (re, im, err) = zeta_em_cert(0.5, t, t, n, &lns, 40);
    (re, im, err)
}

// M(s) = sum_{m<=y} mu(m) m^{-(1/2+it)}  (classical short mollifier)
fn m_val(t: f64, y: usize) -> (f64, f64) {
    let mut re = 0.0f64;
    let mut im = 0.0f64;
    for m in 1..=y {
        let mu = mobius(m);
        if mu == 0 {
            continue;
        }
        let ang = t * (m as f64).ln();
        let (sx, cx) = ang.sin_cos();
        let scale = (mu as f64) / (m as f64).sqrt();
        re += scale * cx;
        im -= scale * sx;
    }
    (re, im)
}

fn theta_prime(t: f64) -> f64 {
    0.5 * (t / (2.0 * PI)).ln() - 1.0 / (48.0 * t * t) - 7.0 / (1920.0 * t * t * t * t)
}

fn mobius(m: usize) -> i32 {
    let mut n = m;
    let mut mu = 1i32;
    let mut p = 2usize;
    while p * p <= n {
        if n % p == 0 {
            n /= p;
            if n % p == 0 {
                return 0;
            }
            mu = -mu;
        }
        p += 1;
    }
    if n > 1 {
        mu = -mu;
    }
    mu
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let t0: f64 = args.get(1).and_then(|s| s.parse().ok()).unwrap_or(1_000_000.0);
    let y: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1);
    let h: f64 = 0.5;
    let ns: usize = 800;
    let hh: f64 = 1e-3;

    // 4-vector W = (Re f, Im f, Re f'/theta', Im f'/theta')
    // moments: sums of products
    let mut mom = [[0.0f64; 4]; 4]; // sum of w_a * w_b
    let mut mean = [0.0f64; 4];
    let mut nf_tot = 0.0f64;
    let mut rms_re = 0.0f64;
    let mut rms_im = 0.0f64;
    let mut max_err = 0.0f64;
    let mut n_pos_re = 0.0f64; // count of Re f > 0 (Levinson counting input)
    let mut n_pos_im = 0.0f64;
    let mut sum_re = 0.0f64; // mean of Re f (drift, not rms)
    let mut sum_im = 0.0f64;

    for i in 0..ns {
        let t = t0 + i as f64 * h;
        let tp = theta_prime(t);
        let (r0, i0, e0) = zeta_val(t);
        let (rp, ip, ep) = zeta_val(t + hh);
        let (rm, im_, em) = zeta_val(t - hh);
        let (mr, mi) = m_val(t, y);
        let (mrp, mip) = m_val(t + hh, y);
        let (mrm, mim) = m_val(t - hh, y);
        // zeta*M at t, t±hh
        let fr0 = r0 * mr - i0 * mi;
        let fi0 = r0 * mi + i0 * mr;
        let frp = rp * mrp - ip * mip;
        let fip = rp * mip + ip * mrp;
        let frm = rm * mrm - im_ * mim;
        let fim = rm * mim + im_ * mrm;
        let re_f = fr0;
        let im_f = fi0;
        let re_fp = (frp - frm) / (2.0 * hh);
        let im_fp = (fip - fim) / (2.0 * hh);
        max_err = max_err.max(e0).max(ep).max(em);

        let w = [re_f, im_f, re_fp / tp, im_fp / tp];
        for a in 0..4 {
            mean[a] += w[a];
            for b in 0..4 {
                mom[a][b] += w[a] * w[b];
            }
        }
        rms_re += re_f * re_f;
        rms_im += im_f * im_f;
        if re_f > 0.0 {
            n_pos_re += 1.0;
        }
        if im_f > 0.0 {
            n_pos_im += 1.0;
        }
        sum_re += re_f;
        sum_im += im_f;
        nf_tot += 1.0;
    }
    println!("Sign/phase structure (Levinson counting input):");
    println!("  P(Re f > 0) = {:.4}   P(Im f > 0) = {:.4}", n_pos_re / nf_tot, n_pos_im / nf_tot);
    println!("  mean Re f = {:.4e}   mean Im f = {:.4e}   (drift, not rms)", sum_re / nf_tot, sum_im / nf_tot);
    println!("  |mean Re f| / rms(Re f) = {:.4}  (phase alignment: ->1 means concentrated)",
        (sum_re / nf_tot).abs() / (rms_re / nf_tot).sqrt());

    // covariance
    let mut cov = [[0.0f64; 4]; 4];
    for a in 0..4 {
        for b in 0..4 {
            cov[a][b] = mom[a][b] / nf_tot - (mean[a] / nf_tot) * (mean[b] / nf_tot);
        }
    }
    let corr = |a: usize, b: usize| -> f64 { cov[a][b] / (cov[a][a].sqrt() * cov[b][b].sqrt()) };

    println!("=== 4x4 covariance probe: W = (Re f, Im f, Re f'/t', Im f'/t'), f=(zeta*M), Y={} ===", y);
    println!("range [{} , {}], samples {}, zeta max err {:.2e}", t0, t0 + ns as f64 * h, ns, max_err);
    println!();
    println!("Covariance matrix (rows a, cols b):");
    for a in 0..4 {
        print!("  [");
        for b in 0..4 {
            print!(" {:9.4e}", cov[a][b]);
        }
        println!(" ]");
    }
    println!();
    println!("RMS ratios and correlations:");
    println!("  |Im f|/|Re f| rms           = {:.6}", (rms_im / rms_re).sqrt());
    println!("  corr(Re f, Im f)            = {:.6}", corr(0, 1));
    println!("  corr(Re f, Im f'/t')        = {:.6}", corr(0, 3));
    println!("  corr(Im f, Re f'/t')        = {:.6}", corr(1, 2));
    println!("  corr(Re f', Im f')          = {:.6}", corr(2, 3));
    println!("  corr(Re f, Re f'/t')        = {:.6}", corr(0, 2));
    println!();
    // eigenvalues of the 2x2 (Re f, Im f'/t') minor and of the full 4x4
    let e2s = eig2(cov[0][0], cov[0][3], cov[3][3]);
    let e4s = eig4(&cov);
    println!("2x2 minor (Re f, Im f'/t') eigenvalues: {:.4} , {:.4}", e2s[1], e2s[0]);
    println!("4x4 eigenvalues: {:.4} , {:.4} , {:.4} , {:.4}", e4s[0], e4s[1], e4s[2], e4s[3]);
    println!("4x4 condition number: {:.3e}", e4s[3] / e4s[0]);
    println!();
    let r = (rms_im / rms_re).sqrt();
    let c01 = corr(0, 1);
    if r < 0.05 || c01.abs() > 0.99 {
        println!("VERDICT: phase is CONCENTRATED (|Im f|/|Re f| = {:.4}, corr(Re,Im) = {:.4})", r, c01);
        println!("=> matrix minorant on (Re f, Im f'/t') collapses to scalar via phase alignment.");
    } else {
        println!("VERDICT: phase NOT concentrated (|Im f|/|Re f| = {:.4}, corr(Re,Im) = {:.4})", r, c01);
        println!("=> no phase-alignment collapse; matrix minorant has a live 2D structure to exploit.");
    }
    println!("(caveat: this measures the covariance of the mollified function along a fixed stretch;");
    println!(" the SDP objective over bandlimited matrix minorants is the definitive test.)");
}

fn eig2(a: f64, b: f64, c: f64) -> [f64; 2] {
    let t = (a + c) / 2.0;
    let d = (((a - c) / 2.0).powi(2) + b * b).sqrt();
    let mut e = [t - d, t + d];
    e.sort_by(|x, y| x.partial_cmp(y).unwrap());
    e
}
// Jacobi eigenvalue algorithm for a symmetric 4x4; returns eigenvalues ascending.
fn eig4(m: &[[f64; 4]; 4]) -> [f64; 4] {
    let mut a = *m;
    let mut v = [[0.0f64; 4]; 4];
    for i in 0..4 {
        v[i][i] = 1.0;
    }
    for _ in 0..100 {
        // find largest off-diagonal
        let mut p = 0usize;
        let mut q = 1usize;
        let mut mx = 0.0f64;
        for i in 0..4 {
            for j in (i + 1)..4 {
                if a[i][j].abs() > mx {
                    mx = a[i][j].abs();
                    p = i;
                    q = j;
                }
            }
        }
        if mx < 1e-30 {
            break;
        }
        let phi = 0.5 * (2.0 * a[p][q]).atan2(a[q][q] - a[p][p]);
        let c = phi.cos();
        let s = phi.sin();
        for k in 0..4 {
            let akp = a[k][p];
            let akq = a[k][q];
            a[k][p] = c * akp - s * akq;
            a[k][q] = s * akp + c * akq;
            a[p][k] = a[k][p];
            a[q][k] = a[k][q];
            let vkp = v[k][p];
            let vkq = v[k][q];
            v[k][p] = c * vkp - s * vkq;
            v[k][q] = s * vkp + c * vkq;
        }
    }
    let mut e = [a[0][0], a[1][1], a[2][2], a[3][3]];
    e.sort_by(|x, y| x.partial_cmp(y).unwrap());
    e
}
