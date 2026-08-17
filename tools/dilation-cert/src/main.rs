// dilation-cert — bound chain for scaled (lambda*p, lambda*q) certificates.
// INPUT: certified eps values per lambda (from the sanctioned arb verifier
//        tools/verify_coboundary_floor.py), alpha, H value.
// OUTPUT: best bound over m for each (lambda, eps) pair.
// Bound chain (verified to reproduce the record):  bound = (H - tau)/(1 - B/m)
//   A = eps*(m-6);  B = A if A<=m/(m-1) else 2*sqrt((m-1)*A/m)-1+A/m;
//   tau = psum*(m-6)/m;  psum scales by lambda.
fn h_window(alpha: f64) -> f64 {
    let a = alpha / 2.0;
    let i0 = 2.0 * a.sin() / alpha;
    let i2 = 0.5 + alpha.sin() / (2.0 * alpha);
    let constant = a.sin() / alpha + 2.0 * a.cos() / (alpha * alpha);
    let j = -2.0 * i2 / (alpha * alpha) + constant * i0;
    let c = i0 * i0 / (i2 + j);
    2.0 - 1.0 / c
}
fn bound(eps: f64, m: usize, alpha: f64, psum: f64) -> f64 {
    let h = h_window(alpha);
    let a = eps * (m as f64 - 6.0);
    let thr = m as f64 / (m as f64 - 1.0);
    let b = if a <= thr { a } else { 2.0 * ((m as f64 - 1.0) * a / m as f64).sqrt() - 1.0 + a / m as f64 };
    let tau = psum * (m as f64 - 6.0) / m as f64;
    (h - tau) / (1.0 - b / m as f64)
}
fn main() {
    // args: alpha H psum1_lambda1_eps1 [lambda2_eps2 ...]
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 4 {
        eprintln!("usage: {} <alpha> <H> <psum_base> <lam:eps> [<lam:eps> ...]", args[0]);
        std::process::exit(1);
    }
    let alpha: f64 = args[1].parse().unwrap();
    let h: f64 = args[2].parse().unwrap();
    let psum_base: f64 = args[3].parse().unwrap();
    println!("alpha={} H={} psum_base={} (record baseline: 0.6734808616745137, psum=1/320, eps=0.0062, m=171, alpha=1.464)",
        alpha, h, psum_base);
    for tok in &args[4..] {
        let (lam, eps) = tok.split_once(':').unwrap();
        let lam: f64 = lam.parse().unwrap();
        let eps: f64 = eps.parse().unwrap();
        let psum = psum_base * lam;
        let mut bm: usize = 0;
        let mut bb: f64 = f64::NEG_INFINITY;
        for m in 40..=400 {
            let b = bound(eps, m, alpha, psum);
            if b > bb { bb = b; bm = m; }
        }
        println!("lam={:.4}: eps={:.6} (certified)  psum={:.9}  best m={}  bound={:.16}", lam, eps, psum, bm, bb);
    }
}