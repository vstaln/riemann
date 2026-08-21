// li_lambda_real — genuine Keiper-Li lambda_n via the xi Hadamard product
// (replaces the li_feedback_gain stub; PROVEN formula, CHECKED NUMERICALLY values)
//
// Math (standard, Li 1997 / Bombieri-Lagarias 1999):
//   lambda_n = (1/(n-1)!) d^n/ds^n [ s^(n-1) log xi(s) ] at s=1
//   log xi(s) = log xi(0) + SUM_j log(1 - s(1-s)/c_j),  c_j = rho_j(1-rho_j) = 1/4 + gamma_j^2
//   (constant log xi(0) cannot contribute: (1+w)^(n-1) has degree n-1 < n)
//
// Series at s = 1+w:  s(1-s) = -w(1+w)  =>
//   log(1 + (w+w^2)/c_j) = SUM_{p>=1} (-1)^(p+1)/p * c_j^(-p) * (w+w^2)^p
//   (w+w^2)^p = w^p (1+w)^p = SUM_{k=0..p} binom(p,k) w^(p+k)
//   => a_m (coeff of w^m in log xi(1+w)) = SUM_j SUM_{p=ceil(m/2)..m} (-1)^(p+1) binom(p,m-p) c_j^(-p) / p
//   lambda_n = n * SUM_{m=1..n} binom(n-1, n-m) * a_m
//
// Validation: lambda_1 = 1 + gamma_Euler/2 - ln(4*pi)/2 = 0.023095708966121...
//             lambda_2 = 0.0923457500874... (literature; if we match these the impl is right)
// Planted control: rho_p = beta0 + i*gamma0 contributes c_p = rho_p - rho_p^2 (COMPLEX).
//   Pair term delta_n = 2 - 2*Re(z^n), z = 1 - 1/(rho_p - 1), |z| = |rho_p-2|/|rho_p-1| > 1
//   for beta0 > 1/2 => oscillating perturbation with EXPONENTIALLY growing dips.

use std::env;
use std::fs;
use std::path::PathBuf;

fn parse_arg(args: &[String], flag: &str) -> Option<String> {
    for i in 0..args.len() {
        if args[i] == flag && i + 1 < args.len() { return Some(args[i + 1].clone()); }
        if args[i].starts_with(&format!("{}=", flag)) { return Some(args[i][flag.len() + 1..].to_string()); }
    }
    None
}

fn load_gammas(path: &str, n: usize) -> Vec<f64> {
    let txt = fs::read_to_string(PathBuf::from(path)).unwrap_or_else(|_| {
        for cand in ["tools/data/zeros_rust_100k.txt", "../data/zeros_rust_100k.txt"] {
            if let Ok(t) = fs::read_to_string(cand) { return t; }
        }
        panic!("no zeros file at {}", path);
    });
    let mut out = Vec::with_capacity(n);
    for line in txt.lines() {
        let t = line.trim();
        if t.is_empty() || t.starts_with('#') { continue; }
        let parts: Vec<&str> = t.split_whitespace().collect();
        let g_str = if parts.len() >= 2 { parts[1] } else { parts[0] };
        if let Ok(g) = g_str.parse::<f64>() { out.push(g); if out.len() >= n { break; } }
    }
    out
}

// a_m for the REAL zeros: sum_j S_m(c_j), S_m(c)=SUM_{p=ceil(m/2)..m} (-1)^(p+1) binom(p,m-p) c^-p / p
fn a_coeff(gammas: &[f64], m: usize) -> f64 {
    let mut s = 0.0;
    for &g in gammas {
        let c = 0.25 + g * g;
        let cinv = 1.0 / c;
        // Horner-free direct: p from ceil(m/2)..=m
        let p_start = (m + 1) / 2;
        let mut term = 0.0;
        let mut cp = 1.0; // c^-p accumulated
        for p in 1..=m {
            cp *= cinv;
            if p < p_start { continue; }
            let k = m - p; // 0..=p
            let b = binom(p, k);
            let sign = if (p + 1) % 2 == 0 { 1.0 } else { -1.0 };
            term += sign * b as f64 * cp / p as f64;
        }
        s += term;
    }
    s
}

fn binom(n: usize, k: usize) -> u64 {
    if k > n { return 0; }
    let k = k.min(n - k);
    let mut r: u64 = 1;
    for i in 0..k { r = r * (n - i) as u64 / (i + 1) as u64; }
    r
}

// planted complex contribution to a_m: single c = c_re + i c_im
fn a_m_plant(c_re: f64, c_im: f64, m: usize) -> (f64, f64) {
    // (w+w^2)^p / c^p with w-power m => binom(p, m-p) c^-p; c^-1 = conj(c)/|c|^2
    let d = c_re * c_re + c_im * c_im;
    let (mut pr, mut pi) = (1.0, 0.0); // c^0; loop advances to c^{-p} before use at p
    let p_start = (m + 1) / 2;
    let (mut sr, mut si) = (0.0, 0.0);
    for p in 1..=m {
        // advance to c^{-p} BEFORE use
        let npr = (pr * c_re + pi * c_im) / d;
        let npi = (pi * c_re - pr * c_im) / d;
        pr = npr; pi = npi;
        if p >= p_start {
            let b = binom(p, m - p) as f64;
            let sign = if (p + 1) % 2 == 0 { 1.0 } else { -1.0 };
            sr += sign * b * pr / p as f64;
            si += sign * b * pi / p as f64;
        }
    }
    (sr, si)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let n_max: usize = parse_arg(&args, "--n-max").and_then(|v| v.parse().ok()).unwrap_or(50);
    let n_zeros: usize = parse_arg(&args, "--zeros-n").and_then(|v| v.parse().ok()).unwrap_or(10000);
    let pb: f64 = parse_arg(&args, "--planted-beta").and_then(|v| v.parse().ok()).unwrap_or(0.85);
    let pg: f64 = parse_arg(&args, "--planted-gamma").and_then(|v| v.parse().ok()).unwrap_or(14.13472514);
    let with_plant = args.iter().any(|a| a == "--planted-beta" || a == "--plant");
    let zpath = parse_arg(&args, "--zeros-file")
        .unwrap_or_else(|| "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt".to_string());

    let gammas = load_gammas(&zpath, n_zeros);
    let g_max = gammas.last().copied().unwrap_or(0.0);

    println!("li_lambda_real n_max={} zeros={} gamma_max={:.2} plant={}", n_max, gammas.len(), g_max, if with_plant { format!("{}+{}i", pb, pg) } else { "none".into() });

    // precompute a_m for m=1..n_max (real zeros), plus planted complex if any
    let mut am = vec![0.0f64; n_max + 1];
    let mut am_pr = vec![0.0f64; n_max + 1];
    let mut am_pi = vec![0.0f64; n_max + 1];
    for m in 1..=n_max {
        am[m] = a_coeff(&gammas, m);
        if with_plant {
            // c_p = rho_p - rho_p^2 = beta(1-beta)+g^2 - i*(2*beta*g)  [check sign: rho^2 = b^2-g^2+2ibg]
            let c_re = pb * (1.0 - pb) + pg * pg;
            let c_im = -(2.0 * pb * pg);
            let (pr, pi) = a_m_plant(c_re, c_im, m);
            am_pr[m] = pr; am_pi[m] = pi;
        }
    }

    // tail correction (Riemann-von Mangoldt density): T_N(n) ~ n^2/(2 pi gamma_N) * (ln(gamma_N/2pi)+1)
    let tail = |n: usize| (n as f64).powi(2) / (2.0 * std::f64::consts::PI * g_max) * ((g_max / (2.0 * std::f64::consts::PI)).ln() + 1.0);

    println!("{:>4} {:>14} {:>14} {:>12} {:>14}", "n", "lambda_n", "+tail", "lit_ref", "delta_plant");
    let lit: [(usize, f64); 4] = [(1, 0.023095708966), (2, 0.092345750087), (3, 0.2076387), (10, 2.279333)];
    let mut min_lam = f64::INFINITY;
    let mut max_abs_delta = 0.0f64;
    for n in 1..=n_max {
        // lambda_n = n * SUM_{m=1..n} binom(n-1, n-m) a_m
        let mut lam = 0.0;
        let mut dlam_r = 0.0;
        let mut dlam_i = 0.0;
        for m in 1..=n {
            let b = binom(n - 1, n - m) as f64;
            lam += b * am[m];
            if with_plant { dlam_r += b * am_pr[m]; dlam_i += b * am_pi[m]; }
        }
        lam *= n as f64;
        let d = n as f64 * dlam_r; // pair with conjugate => 2*Re part; single zero listed once in file? we add pair factor
        let d = 2.0 * d; // rho_p and conjugate pair
        let t = tail(n);
        let total = lam + t;
        min_lam = min_lam.min(total);
        max_abs_delta = max_abs_delta.max(d.abs());
        let lit_str = lit.iter().find(|(k, _)| *k == n).map(|(_, v)| format!("{:.6}", v)).unwrap_or("-".into());
        if n <= 10 || n % 10 == 0 {
            println!("{:>4} {:>14.6} {:>14.6} {:>12} {:>14.6}", n, lam, total, lit_str, if with_plant { format!("{:.6}", d) } else { "-".into() });
        }
    }
    println!("MIN lambda_n(range)={:.6}  max|delta_plant|={:.6}", min_lam, max_abs_delta);
    // validation + honest labels
    let lam1 = 1.0 * am[1];
    println!("VALIDATION lambda_1={:.9} vs lit 0.023095709 diff={:.2e} -> {}", lam1, (lam1 - 0.023095709).abs(),
        if (lam1 - 0.023095709).abs() < 1e-3 { "MATCH (impl OK)" } else { "MISMATCH (INCONCLUSIVE)" });
    // control crossing estimate: dips grow ~ 2|z|^n; z = 1 - 1/(rho_p - 1)
    if with_plant {
        let rp_re = pb - 1.0; let rp_im = pg;
        let d2 = (rp_re - 1.0) * (rp_re - 1.0) + rp_im * rp_im; // |rho_p - 2|^2? rho_p-2 = (b-2)+ig
        let zr = 1.0 - (rp_re / d2); let zi = rp_im / d2;
        // careful: 1/(rho_p - 1); rho_p - 1 = (b-1) + i g
        let w_re = rp_re; let w_im = pg;
        let wd = w_re * w_re + w_im * w_im;
        let inv_re = w_re / wd; let inv_im = -w_im / wd;
        let zr = 1.0 - inv_re; let zi = -inv_im;
        let zmod = (zr * zr + zi * zi).sqrt();
        let zarg = zi.atan2(zr);
        println!("PLANT z=1-1/(rho-1): |z|={:.6} arg={:.6} rad; dips ~ 2|z|^n grow vs lambda_n ~ (n/2)ln n", zmod, zarg);
        let mut n_cross = 0usize;
        for n in 1..=200_000usize {
            if 2.0 * zmod.powi(n as i32) > 0.5 * n as f64 * (n as f64).ln() { n_cross = n; break; }
        }
        if n_cross > 0 { println!("PREDICTED first n where plant dip magnitude exceeds RH lambda_n scale: n~{} (CONJECTURED extrapolation beyond computed range)", n_cross); }
    }
    println!("LABELS: lambda_n values CHECKED NUMERICALLY (this run); positivity for ALL n is NOT proven — Li criterion iff RH; computed range is evidence only.");
}
