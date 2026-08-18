// jensen_gap: GORZ root-cluster CENTER scaling for J^{d,n}(X) built from gamma(n) = 8 n! b_n.
//
// GORZ (arXiv:1902.07321): with L(n_hat) solving n_hat = L(pi e^L + 3/4) (n_hat = 2n-2),
// K = (1/L+1/L^2) n_hat - 3/4, A(n) = log(n L^2/(4 n_hat^2)) + (L-1)/(L^2 K) + n_hat(L+2)/(L^4 K^2),
// the roots of J^{d,n}(X) cluster around X = -exp(-A(n)). We verify the cluster center (mean of
// the roots found by wide bracketing) against -exp(-A(n)) for d = 2,3,4 and n = 10..250.
// (The exact Hermite-shape scaling in the paper's delta(n) is a finer statement; here we certify
// the robust first-order prediction: center ~ -exp(-A(n)).)
use rug::Float;
use std::fs;

const PG: u32 = 210;

fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt").unwrap();
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 2 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) { b.push(Float::with_val(PG, v)); }
        }
    }
    println!("loaded b_k k=0..{}", b.len() - 1);

    let lkda = |n: usize| -> (f64, f64) {
        let nh = (2 * n - 2) as f64;
        let pi = std::f64::consts::PI;
        let mut L = (nh / nh.max(1.0).ln()).ln().max(0.1);
        for _ in 0..200 {
            let f = L * (pi * L.exp() + 0.75) - nh;
            let fp = pi * L.exp() * (L + 1.0) + 0.75;
            let d = f / fp;
            L -= d;
            if d.abs() < 1e-15 { break; }
        }
        let K = (1.0 / L + 1.0 / (L * L)) * nh - 0.75;
        let A = (n as f64 * L * L / (4.0 * nh * nh)).ln() + (L - 1.0) / (L * L * K)
            + nh * (L + 2.0) / (L * L * L * L * K * K);
        (-(-A).exp(), A) // predicted center = -exp(-A), also return A
    };

    let mkpoly = |d: usize, n: usize| -> Vec<f64> {
        let gn = &b[n];
        let mut r: Vec<f64> = Vec::with_capacity(d + 1);
        let mut prod = Float::with_val(PG, 1);
        for j in 0..=d {
            if j > 0 { prod *= (n + j) as f64; }
            let num = Float::with_val(PG, &prod * &b[n + j]);
            let ratio = Float::with_val(PG, num / gn);
            let mut binom = 1.0f64;
            for i in 0..j { binom *= (d - i) as f64 / (i + 1) as f64; }
            r.push(binom * ratio.to_f64());
        }
        r
    };
    let pval = |c: &[f64], x: f64| -> f64 { c.iter().rev().fold(0.0, |s, &a| s * x + a) };
    let pder = |c: &[f64], x: f64| -> f64 {
        let d = c.len() - 1;
        (1..=d).rev().fold(0.0, |s, j| s * x + (j as f64) * c[j])
    };

    println!("\n{:>5} | {:>14} {:>14} {:>12} | {:>10} {:>10}", "n", "GORZ center", "mean roots", "rel dev", "nroots", "spread");
    for &n in &[10usize, 20, 40, 60, 100, 150, 200, 250] {
        let (center_pred, _) = lkda(n);
        for &d in &[2usize, 3, 4] {
            if n + d > b.len() - 1 { continue; }
            let c = mkpoly(d, n);
            // wide scan centered at prediction, generous width: +/- max(500, 8*|center|)
            let wid = 600.0f64.max(8.0 * center_pred.abs());
            let lo = center_pred - wid;
            let hi = center_pred + wid;
            let npts = 120000usize;
            let mut roots: Vec<f64> = Vec::new();
            let mut prev = pval(&c, lo).signum();
            let mut prevx = lo;
            for i in 1..=npts {
                let x = lo + (hi - lo) * (i as f64) / (npts as f64);
                let s = pval(&c, x).signum();
                if s != prev {
                    let mut xr = (prevx + x) / 2.0;
                    for _ in 0..100 {
                        let f = pval(&c, xr);
                        let fp = pder(&c, xr);
                        if fp == 0.0 { break; }
                        let dx = f / fp;
                        xr -= dx;
                        if dx.abs() < 1e-14 { break; }
                    }
                    roots.push(xr);
                    prev = s;
                }
                prevx = x;
            }
            if roots.len() == d {
                let mean: f64 = roots.iter().sum::<f64>() / d as f64;
                let dev = (mean - center_pred).abs() / center_pred.abs().max(1.0);
                let spread = roots.iter().map(|r| (r - mean).abs()).fold(0.0f64, f64::max);
                println!("d={} {:>4} | {:>14.4} {:>14.4} {:>12.2e} | {:>10} {:>10.3}",
                         d, n, center_pred, mean, dev, roots.len(), spread);
            } else {
                println!("d={} {:>4} | {:>14.4} {:>14} {:>12} | {:>10} {:>10}",
                         d, n, center_pred, "-", "-", roots.len(), "-");
            }
        }
        println!();
    }
    println!("(GORZ prediction: root cluster centered at -exp(-A(n)); rel dev -> 0 confirms the");
    println!(" first-order scaling on certified coefficients. gamma = 8 n! b_n is the GORZ object,");
    println!(" NOT Toeplitz-PF (certified 3x3 = -7.009e-8) — different criterion than PF of b_n.)");
}
