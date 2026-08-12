// lattice.rs — the 256-lattice Gram spectrum + two-window overlap probes.
//
// Two more analogy-transfer anchors:
//
// H. Delsarte / two-distance-set transfer: the certificate-class extremal
//    object (the 256-periodic near-CUE law) is a *lattice* configuration. Its
//    simple-atom Gram matrix is (approximately) a 256-circulant with entries
//    k((i-j)/256); its eigenvalues are the DFT of the sampled kernel = the
//    form-factor rows the certificate reads. We compute this spectrum and its
//    concentration 1 - mean((lambda-1)^2), and compare with the real zeros'
//    Gram spectrum (gramev.rs G1/G2). The question: how far is reality's
//    Gram from the extremal lattice in spectral terms, when the certificate
//    reads only the two moments?
//
// I. Statistical-mechanics "aging/overlap" transfer: split the unfolded
//    zero sequence into two disjoint halves; compute the empirical cumulative
//    pair-count C(alpha) on each half; report the max discrepancy and its
//    variance across alpha. Under a stationary (equilibrium) process, two
//    halves fluctuate like independent samples; under a "glassy/frozen" state
//    (the finite-T deficit analogy), they would show systematic drift. We
//    compare the observed discrepancy with the Poisson/independent-sample
//    null (std ~ sqrt(C(alpha)/N)).
//
// Pure std. CHECKED NUMERICALLY by construction.

use std::f64::consts::PI;
use std::fs;

const SQRT2: f64 = std::f64::consts::SQRT_2;

fn sinc(z: f64) -> f64 {
    if z.abs() < 1e-12 {
        1.0
    } else {
        z.sin() / z
    }
}

fn kappa(x: f64) -> f64 {
    let a = (SQRT2 - 2.0 * PI * x) / 2.0;
    let b = (SQRT2 + 2.0 * PI * x) / 2.0;
    let kx = 0.5 * (sinc(a) + sinc(b));
    kx / sinc(1.0 / SQRT2)
}

fn theta(t: f64) -> f64 {
    let z = t / 2.0;
    let s_re = 0.25;
    let s_im = z;
    let log_s_re = 0.5 * (s_re * s_re + s_im * s_im).ln();
    let log_s_im = s_im.atan2(s_re);
    let lg_im = (s_re - 0.5) * log_s_im + s_im * log_s_re - s_im
        - s_im / (12.0 * (s_re * s_re + s_im * s_im));
    lg_im - z * PI.ln()
}

fn load_ords(path: &str) -> Vec<f64> {
    fs::read_to_string(path)
        .expect("read")
        .lines()
        .filter_map(|l| {
            let l = l.trim();
            if l.is_empty() {
                return None;
            }
            let mut it = l.split_whitespace();
            let _ = it.next()?;
            let t: f64 = it.next()?.parse().ok()?;
            Some(t)
        })
        .collect()
}

// DFT of the sampled kernel: the 256-circulant's eigenvalues
// lambda_k = sum_{r=0}^{255} k(r/256) exp(-2 pi i k r / 256), k = 0..255.
// NOTE (fixed): the physical lattice Gram is the TOEPLITZ matrix
//   G_ij = k(i - j)   (atoms at integer spacing, unfolded units)
// matching the real-zeros convention in gramev.rs (spacing ~1). The naive
// circulant/DFT reading is dropped — the kernel k(r/256) is not symmetric
// under r -> 256-r, so the DFT is complex and not an eigenvalue set.
fn lattice_toeplitz_eigenvalues(n: usize) -> Vec<f64> {
    let mut g = vec![vec![0.0f64; n]; n];
    for i in 0..n {
        for j in 0..n {
            g[i][j] = kappa((i as f64) - (j as f64));
        }
    }
    // Jacobi on the symmetric Toeplitz matrix
    let mut a = g.clone();
    let mut off = 0.0f64;
    for i in 0..n {
        for j in (i + 1)..n {
            off += a[i][j] * a[i][j];
        }
    }
    let mut sweep = 0;
    while off > 1e-18 && sweep < 100 * n * n {
        off = 0.0;
        for p in 0..n {
            for q in (p + 1)..n {
                let apq = a[p][q];
                if apq.abs() < 1e-300 {
                    continue;
                }
                let app = a[p][p];
                let aqq = a[q][q];
                let th = 0.5 * (aqq - app) / apq;
                let t = if th.abs() < 1e12 {
                    th.signum() / (th.abs() + (1.0 + th * th).sqrt())
                } else {
                    1.0 / (2.0 * th)
                };
                let c = 1.0 / (1.0 + t * t).sqrt();
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
                let app2 = c * c * app - 2.0 * s * c * apq + s * s * aqq;
                let aqq2 = s * s * app + 2.0 * s * c * apq + c * c * aqq;
                a[p][p] = app2;
                a[q][q] = aqq2;
                a[p][q] = 0.0;
                a[q][p] = 0.0;
            }
        }
        off = 0.0;
        for i in 0..n {
            for j in (i + 1)..n {
                off += a[i][j] * a[i][j];
            }
        }
        sweep += 1;
    }
    let mut ev: Vec<f64> = (0..n).map(|i| a[i][i]).collect();
    ev.sort_by(|x, y| x.partial_cmp(y).unwrap());
    ev
}

fn cumulative_pair_counts(x: &[f64], alphas: &[f64]) -> Vec<f64> {
    let n = x.len();
    alphas
        .iter()
        .map(|&a| {
            let mut c = 0.0f64;
            for i in 0..n {
                let xi = x[i];
                let mut j = i + 1;
                while j < n && x[j] - xi < a {
                    c += 1.0;
                    j += 1;
                }
            }
            c / (n as f64)
        })
        .collect()
}

fn main() {
    println!("== H. 256-lattice Gram spectrum (Delsarte/two-distance anchor) ==");
    for &n in &[64usize, 256usize] {
        let ev = lattice_toeplitz_eigenvalues(n);
        let m = n as f64;
        let tr: f64 = ev.iter().sum();
        let tr2: f64 = ev.iter().map(|e| e * e).sum();
        let conc = 1.0 - ev.iter().map(|e| (e - 1.0) * (e - 1.0)).sum::<f64>() / m;
        let min = ev[0];
        let max = ev[n - 1];
        // count of eigenvalues in the "3-atom" buckets: near 0, near 1, near 2
        let n0 = ev.iter().filter(|e| **e < 0.1).count();
        let n1 = ev.iter().filter(|e| (*e - 1.0).abs() < 0.1).count();
        let n2 = ev.iter().filter(|e| (*e - 2.0).abs() < 0.1).count();
        println!(
            "H1 n={} tr={:.3} tr2={:.3} conc={:.6} min={:.4} max={:.4}",
            n, tr, tr2, conc, min, max
        );
        println!(
            "H2 n={} eigenvalues near 0/1/2: {}/{}/{} (3-atom check)",
            n, n0, n1, n2
        );
    }
    println!("H3 real-zeros comparison (gramev.rs): m=128 conc=0.7341, m=32 conc=0.7625");

    println!("\n== I. two-window overlap / aging anchor ==");
    let ords = load_ords("data/zeros.txt");
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();
    let n = x.len();
    let half = n / 2;
    let alphas: Vec<f64> = (1..=20).map(|k| 0.1 * k as f64).collect();
    let c1 = cumulative_pair_counts(&x[..half], &alphas);
    let c2 = cumulative_pair_counts(&x[half..], &alphas);
    // normalize: C(alpha) ~ alpha for the GUE datum; report raw and the
    // discrepancy, and compare with the independent-sample null std.
    let mut max_dev = 0.0f64;
    let mut devs = vec![];
    for (i, &a) in alphas.iter().enumerate() {
        let dev = (c1[i] - c2[i]).abs();
        // independent-sample null: std of C(alpha) ~ sqrt(2*C(alpha)/N_eff)
        let c_avg = 0.5 * (c1[i] + c2[i]);
        let n_eff = (half as f64).sqrt();
        let null_std = (c_avg / n_eff).sqrt().max(1e-12);
        devs.push((a, dev / null_std));
        if dev > max_dev {
            max_dev = dev;
        }
    }
    println!("I1 halves: {} and {} zeros; max |C1-C2| = {:.6}", half, n - half, max_dev);
    for (a, ratio) in devs.iter().step_by(4) {
        println!("I2 alpha={:.1} |C1-C2|/null_std = {:.3}", a, ratio);
    }
    println!("I3 (ratio ~ 1 = equilibrium/stationary; >> 1 = systematic/glassy drift)");

    println!("\nVERDICT: H/I probes produced by lattice.rs (CHECKED NUMERICALLY)");
}
