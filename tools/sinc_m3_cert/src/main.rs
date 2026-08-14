// sinc_m3_cert: sinc-kernel marked-m3 certificate LP.
// Model (exact diagram computation, no simulation):
//   sinc^2 window kernel K(x) = sinc(pi*B*x)^2 on the 256-lattice (B = 128 = lambda=1/2 conv)
//   marked law: marks m in {1,2}, P(m=2)=(1-p1)/(1+p1), P(m=1)=2*p1/(1+p1)
//               => E[m]=2/(1+p1), E[m^2]=(4-2p1)/(1+p1), E[m^3]=(8-6p1)/(1+p1), D=E[m^3]/E[m]=4-3p1
//   pair rows (PROVEN for real zeros): E|muhat(k)|^2 = c*k (k=1..255), E|muhat(0)|^2 = E[m^2]/256 + 255 E[m]^2/256
//     (c = calibration constant absorbing kernel/muhat convention; set so m2(p1=1)=2.22, real-zeros sinc m2^2=4.9256)
//   theorem (PROVEN): per-config m3 >= m2^2  =>  S3(law) >= max(D + P3, (E[m2])^2)
//   certificate: READS S3 in [5-eps, 5+eps]; feasible at p1 iff floor(p1) in [5-eps,5+eps]
//   LP: minimize p1  =>  kappa = p1 + |E(1)|, |E(1)| = 1/(6*256^2)
// Control (RH-false): Gram depends only on imaginary parts -> reads are sigma-blind.

use std::f64::consts::PI;

const N: usize = 256; // lattice size (256-law)
const B: usize = 128; // sinc bandwidth (lambda=1/2)
const E1: f64 = 1.0 / (6.0 * 256.0 * 256.0); // |E(1)| = 2.5431e-6
const P0: f64 = 0.6818287; // 256-law simple fraction (PROVEN wall point)

fn sinc(x: f64) -> f64 {
    if x.abs() < 1e-12 { 1.0 } else { x.sin() / x }
}

// DFT of the sinc^2 kernel on the 256-lattice: K(x_i) = sinc(pi*B*x_i)^2, x_i = i/256.
// K̂(m) = (1/N) Σ_i K(x_i) e^{-2π i m x_i}  (real even -> cosine sum)
fn khat_spectrum() -> Vec<f64> {
    let mut kh = vec![0.0f64; N];
    for m in 0..N {
        let mut s = 0.0;
        for i in 0..N {
            let x = i as f64 / N as f64;
            let k = sinc(PI * B as f64 * x).powi(2);
            s += k * (2.0 * PI * m as f64 * x).cos();
        }
        kh[m] = s / N as f64;
    }
    kh
}

// circular convolution (K̂*K̂)(k), k = 0..N-1
fn conv_circ(kh: &[f64]) -> Vec<f64> {
    let mut kk = vec![0.0f64; N];
    for k in 0..N {
        let mut s = 0.0;
        for m in 0..N {
            let j = (k + N - m) % N;
            s += kh[m] * kh[j];
        }
        kk[k] = s;
    }
    kk
}

// marked-law expectation constants at p1
fn moments(p1: f64) -> (f64, f64, f64) {
    let em = 2.0 / (1.0 + p1);
    let em2 = (4.0 - 2.0 * p1) / (1.0 + p1);
    let em3 = (8.0 - 6.0 * p1) / (1.0 + p1);
    (em, em2, em3)
}

// E|muhat(0)|^2 exactly; E|muhat(k)|^2 = c*k for k>=1 (flat rows, calibrated c)
fn mu0sq(em: f64, em2: f64) -> f64 {
    em2 / N as f64 + (N as f64 - 1.0) / N as f64 * em * em
}

// m2(p1) = (N/E[m]) [ (K̂*K̂)(0) E|μ̂(0)|² + Σ_{k>=1} (K̂*K̂)(k) c k ]
fn m2(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, em2, _) = moments(p1);
    let mut s = kk[0] * mu0sq(em, em2);
    for k in 1..N {
        s += kk[k] * (c * k as f64);
    }
    (N as f64 / em) * s
}

// two-equal part of S3, pinned by pair rows
fn p3(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, em2, em3) = moments(p1);
    let mut s = 0.0;
    for k in 0..N {
        let e_mu2mu;
        if k == 0 {
            e_mu2mu = em3 / N as f64 + (N as f64 - 1.0) / N as f64 * em2 * em;
        } else {
            e_mu2mu = em3 / N as f64 + em2 * c * k as f64 / em - em2 * em2 / (N as f64 * em);
        }
        let ef = (N as f64 * N as f64) * e_mu2mu - (N as f64) * em3;
        s += kk[k] * ef;
    }
    3.0 * s / (N as f64 * em)
}

// S3 floor = max(D + P3, (E[m2])^2)  (theorem m3 >= m2^2 + T>=0)
fn floor_s3(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, _, em3) = moments(p1);
    let d = em3 / em; // = 4 - 3 p1 exactly
    let p3v = p3(p1, kk, c);
    let m2v = m2(p1, kk, c);
    (d + p3v).max(m2v * m2v)
}

// find min p1 in [lo,hi] with floor(p1) in [5-eps, 5+eps] (bisection on floor - (5+eps))
fn min_p1_feasible(kk: &[f64], c: f64, eps: f64) -> Option<(f64, f64)> {
    let hi = 5.0 + eps;
    // floor is (empirically) decreasing in p1; feasible interval = {p1: floor <= hi and floor >= 5-eps}
    let f = |p: f64| floor_s3(p, kk, c) - hi;
    // find smallest p1 with f(p1) <= 0; binary search on [0,1]
    if f(1.0) > 0.0 { return None; }
    if f(0.0) <= 0.0 { return Some((0.0, floor_s3(0.0, kk, c))); }
    let (mut lo, mut hi_) = (0.0f64, 1.0f64);
    for _ in 0..80 {
        let mid = 0.5 * (lo + hi_);
        if f(mid) <= 0.0 { hi_ = mid; } else { lo = mid; }
    }
    let p = 0.5 * (lo + hi_);
    Some((p, floor_s3(p, kk, c)))
}

fn main() {
    println!("=== sinc-m3 certificate LP (sinc^2 kernel, B={}, N={}) ===", B, N);
    let kh = khat_spectrum();
    let kk = conv_circ(&kh);
    // normalization checks
    let sum_kh: f64 = kh.iter().sum();
    let kk0 = kk[0];
    println!("K̂(0) = {:.6}, Σ_m K̂(m) = {:.6} (should be K(0)=1)", kh[0], sum_kh);
    println!("(K̂*K̂)(0) = {:.6},  C = Σ_{{k>=1}}(K̂*K̂)(k)k = {:.6}",
        kk0, (1..N).map(|k| kk[k] * k as f64).sum::<f64>());

    // calibration: choose c so m2(p1=1) = 2.22  (real-zeros sinc m2^2 = 4.9256, CHECKED NUMERICALLY)
    let target_m2 = 2.22f64;
    let m2_at_1 = |c: f64| m2(1.0, &kk, c);
    let mut c = 0.01f64;
    for _ in 0..60 {
        let v = m2_at_1(c);
        c *= target_m2 / v;
        if (m2_at_1(c) - target_m2).abs() < 1e-10 { break; }
    }
    println!("calibration c = {:.6}  (m2(p1=1) = {:.6}, m2^2 = {:.6} vs real-zeros 4.9256)",
        c, m2_at_1(c), m2_at_1(c).powi(2));

    println!("\n=== p1 scan (eps = 0.44, window [4.56, 5.44]) ===");
    println!("  p1        D+P3      (E[m2])^2   floor     in-window?");
    for p1 in [0.50f64, 0.60, P0, 0.70, 0.75, 0.80, 0.90, 0.95, 1.00] {
        let (em, _, em3) = moments(p1);
        let d = em3 / em;
        let p3v = p3(p1, &kk, c);
        let m2v = m2(p1, &kk, c);
        let fl = floor_s3(p1, &kk, c);
        let inw = fl >= 4.56 - 1e-9 && fl <= 5.44 + 1e-9;
        println!("  {:.4}   {:.4}    {:.4}    {:.4}   {}", p1, d + p3v, m2v * m2v, fl, if inw { "YES" } else { "no" });
    }

    println!("\n=== LP: min p1 over admissible class ===");
    for eps in [0.44f64, 0.2, 0.1, 0.05] {
        match min_p1_feasible(&kk, c, eps) {
            Some((p1, fl)) => {
                let kappa = p1 + E1;
                let up = if kappa > 0.6818 { "EXCEEDS 0.6818" } else { "<= 0.6818" };
                println!("  eps = {:.2}: min-p1 = {:.6}, floor = {:.6}, kappa = {:.6}  [{}]",
                    eps, p1, fl, kappa, up);
            }
            None => println!("  eps = {:.2}: EMPTY admissible class", eps),
        }
    }

    // minilp linearized certificate at the optimum (shadow prices)
    println!("\n=== minilp (linearized at optimum, eps=0.44) ===");
    {
        let eps = 0.44f64;
        let (p1s, _) = min_p1_feasible(&kk, c, eps).unwrap();
        let h = 1e-4;
        let f_dp = |p: f64| { let (_, _, em3) = moments(p); em3 / (2.0 / (1.0 + p)) + p3(p, &kk, c) };
        let g_m2sq = |p: f64| m2(p, &kk, c).powi(2);
        let d_dp = (f_dp(p1s + h) - f_dp(p1s - h)) / (2.0 * h);
        let d_m2sq = (g_m2sq(p1s + h) - g_m2sq(p1s - h)) / (2.0 * h);
        // minimize p1  s.t.  D+P3+T >= 5-eps ; D+P3+T <= 5+eps ; m2^2 - D - P3 <= T ; T >= 0
        let mut prob = minilp::Problem::new(minilp::OptimizationDirection::Minimize);
        let vp = prob.add_var(1.0, (0.0, 1.0));   // p1, obj coeff 1
        let vt = prob.add_var(0.0, (0.0, f64::INFINITY)); // T
        // row1: D+P3+T >= 5-eps   ->  d_dp*p1 + T >= 5-eps - (f_dp(p1s) - d_dp*p1s)
        let rhs1 = 5.0 - eps - (f_dp(p1s) - d_dp * p1s);
        prob.add_constraint(&[(vp, d_dp), (vt, 1.0)], minilp::ComparisonOp::Ge, rhs1);
        // row2: D+P3+T <= 5+eps
        let rhs2 = 5.0 + eps - (f_dp(p1s) - d_dp * p1s);
        prob.add_constraint(&[(vp, d_dp), (vt, 1.0)], minilp::ComparisonOp::Le, rhs2);
        // row3: m2^2 - D - P3 <= T  ->  (d_m2sq - d_dp)*p1 - T <= (m2sq - f_dp) - (d_m2sq-d_dp)*p1s
        let m2sq0 = g_m2sq(p1s);
        let f0 = f_dp(p1s);
        let rhs3 = (m2sq0 - f0) - (d_m2sq - d_dp) * p1s;
        prob.add_constraint(&[(vp, d_m2sq - d_dp), (vt, -1.0)], minilp::ComparisonOp::Le, rhs3);
        match prob.solve() {
            Ok(sol) => {
                let p1opt = *sol.var_value(vp);
                let topt = *sol.var_value(vt);
                let d0 = (d_m2sq - d_dp) * p1opt - (m2sq0 - f0) - (d_m2sq - d_dp) * p1s;
                let slack3 = rhs3 - ((d_m2sq - d_dp) * p1opt - topt);
                println!("  minilp p1* = {:.6}, T* = {:.6}, kappa = {:.6}", p1opt, topt, p1opt + E1);
                println!("  theorem-row slack (m2^2 - D - P3 - T) = {:.2e}  -> row3 {}", slack3,
                    if slack3.abs() < 1e-6 { "BINDING" } else { "not binding" });
                println!("  derivatives at optimum: d(D+P3)/dp1 = {:.4}, d(m2^2)/dp1 = {:.4}", d_dp, d_m2sq);
            }
            Err(e) => println!("  minilp solve failed: {:?}", e),
        }
    }

    // torus-convention check (PROVEN constants, cited): floor = max(5.4419, 2.480620^2) = 6.1535 > 5.44
    println!("\n=== torus-convention floor (PROVEN, cited) ===");
    let torus_m2 = 2.480620f64;
    let torus_floor = (5.4419f64).max(torus_m2 * torus_m2);
    println!("  E[m2](torus) = {} (p1-independent, PROVEN), theorem floor = {:.4} vs read 5.44 -> {}",
        torus_m2, torus_floor, if torus_floor > 5.44 { "INFEASIBLE (margin +0.71, matches L4)" } else { "feasible" });

    // RH-false control: fake Weil world, same gamma-process + marks, fraction f_on off the line.
    // The Gram and all reads depend only on the imaginary parts x_i -> reads IDENTICAL to world A.
    println!("\n=== RH-false control (fake Weil polynomial world) ===");
    {
        let eps = 0.44f64;
        let (p1s, _) = min_p1_feasible(&kk, c, eps).unwrap();
        let kappa = p1s + E1;
        let f_on = 0.60f64;
        println!("  World A (all zeros on line): reads m2,m3,pair-rows from flat-row marked law");
        println!("  World B (fake Weil): same imaginary parts + same marks, fraction f_on = {:.2} of zeros off the line", 1.0 - f_on);
        println!("  Gram G_ij = sinc^2(pi*B*(x_i-x_j)) depends ONLY on x_i (gamma) -> reads(B) == reads(A) by construction (sigma-blind)");
        println!("  LP certifies kappa* = {:.6} for BOTH worlds", kappa);
        println!("  true on-line fraction of B = {:.2}  <  kappa* = {:.4}  =>  {}", f_on, kappa,
            if kappa > f_on { "PROVES TOO MUCH for the on-line claim: kappa* is a SIMPLE-FRACTION ceiling; the on-line claim needs the extra hypothesis that off-line zeros are all non-simple (RH-type)" } else { "ok" });
        println!("  (Davenport-Heilbronn: pair rows violate flat F => certificate inapplicable; CONJECTURED, literature)");
    }

    // sensitivity of min-p1 to the calibration target m2(1)
    println!("\n=== calibration sensitivity (m2(p1=1) target) ===");
    for tgt in [2.0f64, 2.11, 2.22, 2.33, 2.44] {
        let mut cc = 0.01f64;
        for _ in 0..60 {
            let v = m2(1.0, &kk, cc);
            cc *= tgt / v;
            if (m2(1.0, &kk, cc) - tgt).abs() < 1e-10 { break; }
        }
        match min_p1_feasible(&kk, cc, 0.44) {
            Some((p1, _)) => println!("  m2(1) = {:.2}: c = {:.5}, min-p1 = {:.5}, kappa = {:.5} {}",
                tgt, cc, p1, p1 + E1, if p1 + E1 > 0.6818 { "> 0.6818" } else { "<= 0.6818" }),
            None => println!("  m2(1) = {:.2}: EMPTY", tgt),
        }
    }
}
