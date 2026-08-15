// Referee 6C — second-machine independent re-derivation of the 0.673481 certificate.
// SEPARATE implementation, DIFFERENT numerical strategy: f64 high-order Gauss-Legendre
// quadrature (fixed 256-pt, error by 128->256 doubling) instead of mpmath quad.
// Build: cargo build --release --target x86_64-unknown-linux-musl (or plain --release)

fn legendre_gauss(n: usize) -> (Vec<f64>, Vec<f64>) {
    let mut x = vec![0.0; n];
    let mut w = vec![0.0; n];
    for i in 0..n {
        let mut xi = (((i as f64 + 0.75) / (n as f64 + 0.5)) * std::f64::consts::PI).cos();
        for _ in 0..60 {
            let (mut p0, mut p1) = (1.0_f64, xi);
            for k in 1..n {
                let p2 = ((2 * k + 1) as f64 * xi * p1 - k as f64 * p0) / (k + 1) as f64;
                p0 = p1;
                p1 = p2;
            }
            let dp = (n as f64) * (xi * p1 - p0) / (xi * xi - 1.0);
            xi -= p1 / dp;
        }
        let (mut p0, mut p1) = (1.0_f64, xi);
        for k in 1..n {
            let p2 = ((2 * k + 1) as f64 * xi * p1 - k as f64 * p0) / (k + 1) as f64;
            p0 = p1;
            p1 = p2;
        }
        let dp = (n as f64) * (xi * p1 - p0) / (xi * xi - 1.0);
        x[i] = xi;
        w[i] = 2.0 / ((1.0 - xi * xi) * dp * dp);
    }
    (x, w)
}

fn quad<F: Fn(f64) -> f64>(f: F, n: usize) -> f64 {
    let (x, w) = legendre_gauss(n);
    w.iter().zip(x.iter()).map(|(wi, xi)| wi * f(0.5 * (xi + 1.0)) * 0.5).sum()
}

fn j_integral(a: f64, n: usize) -> f64 {
    // J = 2 * int_0^1 u*[(1-u)/2 cos(au) + sin(a(1-u))/(2a)] du
    2.0 * quad(
        |u: f64| u * ((1.0 - u) / 2.0 * (a * u).cos() + (a * (1.0 - u)).sin() / (2.0 * a)),
        n,
    )
}

fn hcos(a: f64) -> f64 {
    let iv = 2.0 * (a / 2.0).sin() / a;
    let iv2 = (1.0 + a.sin() / a) / 2.0;
    let j = j_integral(a, 256);
    2.0 - (iv2 + j) / (iv * iv)
}

fn main() {
    println!("=== 6C independent re-derivation (f64 Gauss-Legendre) ===");
    println!("quad sanity int_0^1 x^2 = {:.16} (expect 0.3333333333333333)", quad(|x| x * x, 256));

    // (1) H values
    for (name, a) in [("sqrt2", std::f64::consts::SQRT_2), ("1.464", 1.464_f64), ("1.49", 1.49_f64), ("1.47", 1.47_f64)] {
        let h = hcos(a);
        let err = (j_integral(a, 256) - j_integral(a, 128)).abs();
        println!("H({}) = {:.16}  (J quadr err est {:.1e})", name, h, err);
    }
    println!("reference: H(sqrt2)=0.6725007036794116  H(1.464)=0.6724674255777881  H(1.49)=0.6724218860964475");

    // (2) bound chain with closed-form B = Phi_m(eps*(m-6)), Phi_m(A)=2 sqrt((m-1)A/m) - 1 + A/m
    let m = 171.0_f64;
    let psum = 1.0 / 320.0;
    let eps = 0.0062_f64;
    let tau = psum * (m - 6.0) / m;
    let a_phi = eps * (m - 6.0);
    let b_phi = 2.0 * ((m - 1.0) * a_phi / m).sqrt() - 1.0 + a_phi / m;
    let h = hcos(1.464);
    let bound = (h - tau) / (1.0 - b_phi / m);
    println!("\n--- bound chain, closed-form B ---");
    println!("tau  = {:.16}", tau);
    println!("A    = eps*(m-6) = {:.10}", a_phi);
    println!("B    = Phi_m(A)  = {:.12}", b_phi);
    println!("B/m  = {:.12}", b_phi / m);
    println!("bound= (H-tau)/(1-B/m) = {:.16}", bound);
    println!("target = 0.6734808616745137 ; abs diff = {:.2e}", (bound - 0.6734808616745137).abs());

    // (3) back-out: what B reproduces the target EXACTLY?
    let num = h - tau;
    let b_back = m * (1.0 - num / 0.6734808616745137);
    println!("B_backout (target-exact) = {:.12} ; diff vs Phi_m = {:.2e}", b_back, b_back - b_phi);

    // (4) cross-checks on leaderboard entries
    let tau149 = psum * (m - 6.0) / m;
    let b149 = 2.0 * ((m - 1.0) * eps * (m - 6.0) / m).sqrt() - 1.0 + eps * (m - 6.0) / m;
    println!("\n[cross a=1.49, m=171, eps=0.0062] bound={:.10} (record says 0.673435)",
        (hcos(1.49) - tau149) / (1.0 - b149 / m));
    let m2 = 183.0_f64;
    let tau2 = psum * (m2 - 6.0) / m2;
    let eps2 = 0.00577_f64;
    let a2 = eps2 * (m2 - 6.0);
    let b2 = 2.0 * ((m2 - 1.0) * a2 / m2).sqrt() - 1.0 + a2 / m2;
    println!("[cross a=1.47, m=183, eps=0.00577] bound={:.10} (record says 0.673193)",
        (hcos(1.47) - tau2) / (1.0 - b2 / m2));

    // (5) eps consistency: relation between eps, tau, and the redistribution gain
    let gain = bound - h;
    println!("\nredistribution gain bound - H = {:.10}; tau = {:.10}; eps = {:.10}", gain, tau, eps);
}
