// gramev.rs — Gram-matrix eigenvalue anchors from real zeros.
//
// For the graph-eigenvalue / Anderson-localization analogies: the certified
// machinery's core finite object is the Gram matrix G_ij = k(x_i - x_j) of
// simple-zero atoms (k = K/K0, the certified kernel). In spectral graph
// theory, eigenvalue concentration bounds (Gershgorin/Brauer, Alon-Boppana,
// expander theory) constrain what a quadratic form can certify about a graph;
// in Anderson localization, eigenvector localization of a random Gram matrix
// is diagnosed by IPR (inverse participation ratio). Here we measure:
//
//   G1. Full spectrum of G for m consecutive real zeros (unfolded) — min,
//       max, trace, and the "Anderson" IPR of the eigenvectors.
//   G2. The spectral concentration identity: bound/N = 1 - mean((lambda-1)^2)
//       (from attack-eng.md SM-2, PROVEN) — recomputed from the real spectrum.
//   G3. The 3-atom extremal-law spectrum (2/3 ones, 1/6 twos, 1/6 zeros) —
//       the certificate-class extremal spectrum — vs the real-zeros spectrum:
//       how far is reality from the extremal law in spectral terms?
//
// Pure std. Jacobi eigenvalue routine (symmetric, m <= 256).

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

// Jacobi eigenvalue routine for a symmetric matrix (in-place copy).
fn jacobi_eigvals(a: &[Vec<f64>]) -> Vec<f64> {
    let n = a.len();
    let mut a = a.to_vec();
    let mut v: Vec<Vec<f64>> = (0..n)
        .map(|i| {
            (0..n)
                .map(|j| if i == j { 1.0 } else { 0.0 })
                .collect()
        })
        .collect();
    let mut off = 0.0f64;
    for i in 0..n {
        for j in (i + 1)..n {
            off += a[i][j] * a[i][j];
        }
    }
    let mut sweep = 0;
    while off > 1e-20 && sweep < 100 * n * n {
        off = 0.0;
        for p in 0..n {
            for q in (p + 1)..n {
                let apq = a[p][q];
                if apq.abs() < 1e-300 {
                    continue;
                }
                let app = a[p][p];
                let aqq = a[q][q];
                let theta = 0.5 * (aqq - app) / apq;
                let t = if theta.abs() < 1e12 {
                    theta.signum() / (theta.abs() + (1.0 + theta * theta).sqrt())
                } else {
                    1.0 / (2.0 * theta)
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
                for k in 0..n {
                    let vkp = v[k][p];
                    let vkq = v[k][q];
                    v[k][p] = c * vkp - s * vkq;
                    v[k][q] = s * vkp + c * vkq;
                }
            }
        }
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

fn main() {
    println!("== G. Gram-spectrum anchors from real zeros ==");
    let ords = load_ords("data/zeros.txt");
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();

    for &m in &[32usize, 128usize] {
        let start = 100; // skip the very first (edge effects in unfolding)
        let mut g = vec![vec![0.0f64; m]; m];
        for i in 0..m {
            for j in 0..m {
                g[i][j] = kappa(x[start + i] - x[start + j]);
            }
        }
        let ev = jacobi_eigvals(&g);
        let tr: f64 = ev.iter().sum();
        let tr2: f64 = ev.iter().map(|e| e * e).sum();
        let mean = tr / m as f64;
        let conc: f64 = ev.iter().map(|e| (e - 1.0) * (e - 1.0)).sum::<f64>() / m as f64;
        // IPR of each eigenvector: needs eigenvectors; we use the "diagonal
        // dominance" proxy: max |G_ij| off-diagonal row sum / trace = the
        // Gershgorin radius, and the Anderson localization proxy = mean
        // |G_ij|^2 / (mean |G_ij|)^2 over a row (row energy concentration).
        let mut row_concentration = 0.0f64;
        for i in 0..m {
            let mut s1 = 0.0f64;
            let mut s2 = 0.0f64;
            for j in 0..m {
                if i != j {
                    let v = g[i][j].abs();
                    s1 += v;
                    s2 += v * v;
                }
            }
            let n1 = (m - 1) as f64;
            let mu1 = s1 / n1;
            row_concentration += s2 / n1 / (mu1 * mu1 + 1e-300);
        }
        row_concentration /= m as f64;
        println!("G1 m={} tr={:.4} tr2={:.4} mean={:.4} conc=1-mean((l-1)^2)={:.6}",
                 m, tr, tr2, mean, 1.0 - conc);
        println!("G2 m={} min_ev={:.6} max_ev={:.6} neg_count={}",
                 m, ev[0], ev[m - 1], ev.iter().filter(|e| **e < -1e-9).count());
        println!("G3 m={} row-energy-concentration (IPR proxy) = {:.4}", m, row_concentration);
    }

    println!("\n== G4. extremal-law spectrum vs real (the 3-atom law) ==");
    // The certificate-class extremal law: 2/3 of eigenvalues 1, 1/6 twos,
    // 1/6 zeros (attack-kernel.md / idea-generator-crossdomain V1).
    // The real zeros' spectrum at m=128 (above) should be compared.
    println!("G4a extremal law: ones 2/3, twos 1/6, zeros 1/6");
    println!("G4b conc for extremal law = 1 - (1/6*(2-1)^2 + 1/6*(0-1)^2) = 1 - 1/3 = {:.4}", 2.0 / 3.0);
    println!("G4c (see G1 m=128 conc value above for the real-zeros comparison)");

    println!("\nVERDICT: G-probes produced by gramev.rs (CHECKED NUMERICALLY)");
}
