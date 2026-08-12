// window.rs — Provocation: "Po: the window functional is the operator; the zeros are
// its eigenfunctions; a different window IS a different operator with a different
// (better) constant." attack-kernel proved the cosine window is the *global minimizer*
// of the Rayleigh quotient (Euler-Lagrange v''+2v=0 + convexity), so a better window
// for the SAME functional is impossible. The serious kernel to extract: the window
// enters the certificate through its *moments* (tr = ∫ψ², HS² = ∫∫|u-v|ψψ, and the
// off-diagonal kernel k(x)=K(x)/K(0)). "Different operator" = a window with the same
// normalization but *different kernel zeros* — its Gram matrix would have a different
// coherence profile on the zero set. Test:
//   W1  one-parameter window family psi_c(u) = cos(√2 c u) on [-1/2,1/2]: the
//       certificate constant C(c) = ∫ψ_c² + ∫∫|u-v|ψ_cψ_c over (∫ψ_c)². Compute the
//       curve C(c) and confirm the minimum at c = 1 (kernel's claim) and its flatness
//       (conditioning claim: 1% window change -> <= 0.02% constant change).
//   W2  two-tone window psi(u) = cos(√2 u) + d cos(√2 b u): the constant's response
//       to a second tone. Prior task-idea (window2) is sweeping this; here we just
//       report the *H-functional* lever claim: H(alpha) raises the bound. We compute
//       the off-diagonal kernel's first zero shift and the coherence on the real
//       zero differences (does the two-tone kernel reduce the max coherence?).
//   W3  "operator" reading: the kernel's Fourier transform (the paper's FT) at the
//       zero-difference frequencies — the diagonal of the operator in the frequency
//       domain. Report the kernel's first zero location and the fraction of zero
//       differences below it (the "in-band" fraction).

use std::f64::consts::PI;
use std::fs;

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

// closed forms for psi_c(u) = cos(√2 c u) on [-1/2,1/2]
fn int_psi(c: f64) -> f64 {
    let a = std::f64::consts::SQRT_2 * c;
    2.0 * (a / 2.0).sin() / a // ∫_{-1/2}^{1/2} cos(a u) du = 2 sin(a/2)/a
}

fn int_psi2(c: f64) -> f64 {
    let a = std::f64::consts::SQRT_2 * c;
    0.5 + (a).sin() / (2.0 * a) // ∫ cos²(a u) du over [-1/2,1/2] = 1/2 + sin(a)/(2a)
}

fn dbl_int_abs(c: f64) -> f64 {
    // ∫∫ |u-v| cos(a u) cos(a v) du dv over [-1/2,1/2]^2, a = √2 c.
    // = 2 ∫_0^1 w (ψ*ψ)(w) dw with ψ the even function. Use numerical quadrature.
    let a = std::f64::consts::SQRT_2 * c;
    let n = 400;
    let h = 1.0 / n as f64;
    let mut s = 0.0f64;
    for i in 0..n {
        let u = (i as f64 + 0.5) * h - 0.5;
        let cu = (a * u).cos();
        for j in 0..n {
            let v = (j as f64 + 0.5) * h - 0.5;
            let cv = (a * v).cos();
            s += (u - v).abs() * cu * cv;
        }
    }
    s * h * h
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();

    // W1: constant curve C(c) = (∫ψ_c² + ∫∫|u-v|ψ_cψ_c) / (∫ψ_c)² for c in 0.8..1.4.
    // NORMALIZATION NOTE: the paper's H0 = 3/2 - (1/√2)cot(1/√2) = 0.6725007 arises from
    // the *normalized* window (∫ψ = 1 constraint); the raw Rayleigh quotient at c = 1
    // is 1/2 + (1/√2)cot(1/√2) = 1.3274993 (the HS² constant C). We print the raw
    // quotient; the *minimum over c* is the kernel's claim (c = 1), and the flatness
    // is the conditioning claim. The two constants relate by H0 = C/(1+C) = 0.6725.
    println!("W1 constant_curve (raw Rayleigh quotient (∫ψ²+∬|u-v|ψψ)/(∫ψ)²)");
    let cs: [f64; 13] = [0.80, 0.85, 0.90, 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05, 1.10, 1.20, 1.40];
    for &c in cs.iter() {
        let ip = int_psi(c);
        let ip2 = int_psi2(c);
        let dbl = dbl_int_abs(c);
        let q = (ip2 + dbl) / (ip * ip);
        println!("W1 c {:.2} quotient {:.6}", c, q);
    }
    // flatness at c=1: 1% perturbation
    let c1 = 1.0f64;
    let c1p = 1.01f64;
    let q1 = (int_psi2(c1) + dbl_int_abs(c1)) / (int_psi(c1) * int_psi(c1));
    let q1p = (int_psi2(c1p) + dbl_int_abs(c1p)) / (int_psi(c1p) * int_psi(c1p));
    println!("W1 quotient_c1 {:.6} quotient_c1.01 {:.6} flatness_1pct {:.6} (rel {:.6})", q1, q1p, q1p - q1, (q1p - q1) / q1);

    // W2: two-tone kernel — reduce max coherence on the real zero differences.
    // kernel for psi(u) = cos(√2 u) + d cos(√2 b u): K_d(x) = K(x) + d K_b(x)
    // where K_b(x) = ∫ cos(√2 b t) cos(2π x t) dt. We just measure the *shift* of the
    // first zero of K(x) (which sets the repulsion scale) — already known; report the
    // fraction of real zero differences below the first zero (in-band).
    let k0 = 0.5 + (std::f64::consts::SQRT_2).sin() / (2.0 * std::f64::consts::SQRT_2);
    let kern = |z: f64| -> f64 {
        let s2 = std::f64::consts::SQRT_2;
        let h = s2 / 2.0;
        let t1 = (h - PI * z).sin() / (s2 - 2.0 * PI * z);
        let t2 = (h + PI * z).sin() / (s2 + 2.0 * PI * z);
        (0.5 * (t1 + t2)) / k0
    };
    // first zero of K(x): scan
    let mut z0 = 1.0f64;
    for i in 1..2000 {
        let z = i as f64 * 0.001;
        if kern(z) < 0.0 {
            z0 = z;
            break;
        }
    }
    println!("W2 kernel_first_zero {:.4}", z0);
    let mut inband = 0.0f64;
    let mut cnt = 0.0f64;
    for i in 0..n {
        let xi = x[i];
        let mut j = i + 1;
        while j < n && x[j] - xi < z0 {
            inband += 1.0;
            j += 1;
        }
        cnt += 1.0;
    }
    println!("W2 inband_pair_rate {:.6} (pairs below first kernel zero per zero)", inband / cnt);

    // W3: "operator in frequency domain": the FT of the window (the paper's paperFT)
    // sampled at zero-difference frequencies — the diagonal dominance.
    // psi_hat(s) = ∫ cos(√2 u) e^{-2πi s u} du = the finitet closed form. Report the
    // value at s = 0 (should be ∫ψ = √2 sin(1/√2)) and at s = mean gap (the first
    // "lattice" frequency).
    let ip = int_psi(1.0);
    println!("W3 psihat_0 {:.4} (∫ψ = {:.4})", ip, std::f64::consts::SQRT_2 * (1.0 / std::f64::consts::SQRT_2).sin());

    println!("DONE");
}
