// xiprime — empirical check: zeros of xi'(s) on the critical line.
//
// Facts used:
//   xi(1/2+it) = P(t) * Z(t),  P(t) = (1/2)(t^2 + 1/4) pi^{-1/4} |Gamma(1/4 + it/2)| > 0,
//   Z(t) = e^{i theta(t)} zeta(1/2+it) (real).
//   d/dt xi(1/2+it) = i * xi'(1/2+it) = P'(t) Z(t) + P(t) Z'(t)
//   => xi'(1/2+it) = 0  iff  H(t) := Z(t)*(P'/P)(t) + Z'(t) = 0.
//   P'/P = 2t/(t^2+1/4) - (1/2) Im psi(1/4 + it/2).
//
// We scan each gap (gamma_n, gamma_{n+1}) between consecutive zeta zeros (plus the
// initial interval (0.05, gamma_1)) for sign changes of H, bisect each root, and
// check the root is simple (H changes sign).  This counts the zeros of xi' ON the
// critical line with 0 < Im <= gamma_1000.  Separately we count stationary points
// of Z (zeros of Z', the "extrema" of Hardy's function), one per gap expected.

mod zeta;

use std::env;
use std::fs;
use std::path::PathBuf;

/// Im psi(1/4 + i t/2).  Stirling asymptotic on psi(z + m) with |z+m| >= 10
/// (recursion psi(z) = psi(z+1) - 1/z makes this exact), error < 1e-15.
fn psi_im(t: f64) -> f64 {
    let re = 0.25;
    let im = t / 2.0;
    let mag = (re * re + im * im).sqrt();
    // shift z -> z + m until |z + m| >= 10
    let m = if mag < 10.0 { ((10.0 - mag) as usize) + 1 } else { 0 };
    // Im 1/(z+j) = -im_j/mag_j^2  (subtract: psi(z) = psi(z+m) - sum_{j<m} 1/(z+j))
    let mut corr = 0.0f64;
    for j in 0..m {
        let rej = re + j as f64;
        let magj = rej * rej + im * im;
        corr += im / magj; // -Im[1/(z+j)] = +im/magj^2
    }
    let re2 = re + m as f64;
    let mag2 = re2 * re2 + im * im;
    let arg = im.atan2(re2);
    let mut s = arg;
    // -Im[1/(2z)] = +im/(2 mag2)
    s += im / (2.0 * mag2);
    // -sum_k B_{2k}/(2k) Im(z^{-2k}); z^{-2k} = mag^{-2k}(cos(2k arg) - i sin(2k arg))
    for k in 1..=10 {
        let mag_pow = mag2.powi(-(k as i32));
        let im_part = -mag_pow * (2.0 * k as f64 * arg).sin();
        s -= zeta::bernoulli(2 * k) / (2.0 * k as f64) * im_part;
    }
    s - corr
}

/// P'/P at t.
fn pp_over_p(t: f64) -> f64 {
    2.0 * t / (t * t + 0.25) - 0.5 * psi_im(t)
}

/// Z'(t) by central difference of the Euler–Maclaurin Z.
fn zp(t: f64) -> f64 {
    let h = 1e-4;
    (zeta::zeta_z(t + h) - zeta::zeta_z(t - h)) / (2.0 * h)
}

/// H(t) = Z*(P'/P) + Z'; zeros = zeros of xi' on the line, positive ordinate.
fn h_of_t(t: f64) -> f64 {
    zeta::zeta_z(t) * pp_over_p(t) + zp(t)
}

/// Count sign changes of f on [a, b] on a grid of step h, and bisect each to a root.
/// Returns the roots (and counts them). Simple roots only (sign change).
fn roots_in(f: &dyn Fn(f64) -> f64, a: f64, b: f64, step: f64) -> Vec<f64> {
    let mut out = Vec::new();
    let n = ((b - a) / step).ceil() as usize;
    let mut prev = f(a);
    let mut prev_x = a;
    for i in 1..=n {
        let x = a + (i as f64) * step;
        let cur = f(x);
        if prev * cur < 0.0 {
            // bisect
            let (mut lo, mut hi) = (prev_x, x);
            let (mut flo, mut fhi) = (prev, cur);
            for _ in 0..80 {
                let mid = 0.5 * (lo + hi);
                let fm = f(mid);
                if flo * fm <= 0.0 {
                    hi = mid;
                    fhi = fm;
                } else {
                    lo = mid;
                    flo = fm;
                }
            }
            out.push(0.5 * (lo + hi));
        }
        prev = cur;
        prev_x = x;
    }
    out
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let data_dir = PathBuf::from(env::var("ZETA_DATA").unwrap_or_else(|_| "../data".into()));
    let file = data_dir.join("zeros_1_1000.txt");
    let text = fs::read_to_string(&file).expect("read zeros file");
    let mut gs: Vec<f64> = Vec::new();
    for line in text.lines() {
        let mut it = line.split_whitespace();
        let _idx: usize = it.next().unwrap().parse().unwrap();
        let g: f64 = it.next().unwrap().parse().unwrap();
        gs.push(g);
    }
    let n = gs.len();
    println!("read {} zeta zeros (1..{}), last = {}", n, n, gs[n - 1]);

    // sanity: every gap is a sign change of Z (simple zero on the line).
    // Evaluate Z at the MIDPOINTS of adjacent gaps (the sign AT the rounded gamma is noise-level).
    let mut mid = Vec::new();
    mid.push(zeta::zeta_z((0.0 + gs[0]) / 2.0)); // Z(0) = zeta(1/2) < 0
    for i in 0..n - 1 {
        mid.push(zeta::zeta_z((gs[i] + gs[i + 1]) / 2.0));
    }
    let mut simple = 0;
    for i in 0..n - 1 {
        if mid[i] * mid[i + 1] < 0.0 {
            simple += 1;
        }
    }
    println!("gaps with opposite Z-signs at adjacent midpoints: {}/{} (expect {}: all simple on-line zeros)", simple, n - 1, n - 1);

    // (1) zeros of H (= zeros of xi' on the line) in each gap and in (0.05, gamma_1)
    let step = 0.05;
    let mut total_h = 0usize;
    let mut gaps_with_one = 0usize;
    let mut gap_hist: Vec<usize> = Vec::new();
    let mut roots_all: Vec<f64> = Vec::new();

    let init = roots_in(&h_of_t, 0.05, gs[0] - 1e-9, step);
    println!("H-zeros in (0.05, gamma_1): {}", init.len());
    for r in &init {
        println!("    t = {:.6}", r);
    }
    total_h += init.len();
    roots_all.extend(init);

    for i in 0..n - 1 {
        let rts = roots_in(&h_of_t, gs[i] + 1e-9, gs[i + 1] - 1e-9, step);
        if gap_hist.len() <= rts.len() {
            gap_hist.resize(rts.len() + 1, 0);
        }
        gap_hist[rts.len()] += 1;
        if rts.len() == 1 {
            gaps_with_one += 1;
        }
        total_h += rts.len();
        roots_all.extend(rts);
    }
    println!("gaps (between consecutive zeta zeros): {}", n - 1);
    println!("gaps with exactly one H-zero (xi'-zero on line): {}", gaps_with_one);
    for (k, c) in gap_hist.iter().enumerate() {
        if *c > 0 {
            println!("  gaps with {} H-zeros: {}", k, c);
        }
    }
    println!("total H-zeros in (0.05, gamma_{}] = {}", n, total_h);

    // (2) stationary points of Z (zeros of Z') per gap
    let mut total_zp = 0usize;
    let mut zp_gap1 = 0usize;
    let mut zp_hist: Vec<usize> = Vec::new();
    for i in 0..n - 1 {
        let rts = roots_in(&zp, gs[i] + 1e-9, gs[i + 1] - 1e-9, step);
        if zp_hist.len() <= rts.len() {
            zp_hist.resize(rts.len() + 1, 0);
        }
        zp_hist[rts.len()] += 1;
        if rts.len() == 1 {
            zp_gap1 += 1;
        }
        total_zp += rts.len();
    }
    println!("Z' zeros (stationary points of Z) in gaps: {}", total_zp);
    println!("gaps with exactly one stationary point of Z: {}/{}", zp_gap1, n - 1);
    for (k, c) in zp_hist.iter().enumerate() {
        if *c > 0 {
            println!("  gaps with {} stationary points: {}", k, c);
        }
    }

    // (3) simplicity of each H-root: H changes sign across it (guaranteed by detection),
    // but also evaluate H'(root) numerically to confirm nonzero.
    let mut min_abs_hprime = f64::INFINITY;
    let mut nonsimple = 0usize;
    for r in &roots_all {
        let h2 = 1e-3;
        let d = (h_of_t(r + h2) - h_of_t(r - h2)) / (2.0 * h2);
        if d.abs() < min_abs_hprime {
            min_abs_hprime = d.abs();
        }
        if d.abs() < 1e-6 {
            nonsimple += 1;
        }
    }
    println!(
        "H-roots: {} total; min |H'| at a root = {:.3e}; roots with |H'| < 1e-6: {}",
        roots_all.len(),
        min_abs_hprime,
        nonsimple
    );

    // write the on-line xi' zeros for cross-checking against the winding number
    let out = data_dir.join("xiprime_on_line_1_1000.txt");
    let mut s = String::new();
    for (i, r) in roots_all.iter().enumerate() {
        s.push_str(&format!("{} {:.12}\n", i + 1, r));
    }
    fs::write(&out, s).expect("write xiprime zeros");
    println!("wrote on-line xi'-zeros -> {}", out.display());
}
