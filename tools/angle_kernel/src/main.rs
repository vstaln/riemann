// angle_kernel: variational problem behind the 67.25% Riemann-program constant.
//
// Definitive statement (Lean: Zeta23/ThmD/Functional.lean, [eq:cv]):
//   maximize  c_1(v) = (int v)^2 / ( int v^2 + intint_{[-1/2,1/2]^2} |s-s'| v(s) v(s') )
//   over v on [-1/2,1/2];  the optimum is v*(s) = cos(sqrt2 s) with
//   c_1* = sqrt2 tan(1/sqrt2) / (1 + (1/sqrt2) tan(1/sqrt2)) = 0.7532960...
//   and the proportion of zeros on the line is  2 - 1/c_1* = 3/2 - (1/sqrt2) cot(1/sqrt2) = 0.6725007...
//   (rank-trace step: proportion = 2 - Q(v),  Q(v) = 1/c_1(v) = [int v^2 + intint |s-s'| v v]/(int v)^2).
//
// The bandwidth constraint: supp v in [-1/2,1/2] (c <= 1/2), and the paper's lambda parameter
// (Gabor undersampling) is bounded by lambda <= 1. We check c*_lambda is increasing in lambda on (0,1].
//
// We also keep the "quartic quotient" Q_quart(v) = [int v^4 + 2 int_0^1 z (v^2*v^2)(z) dz]/(int v^2)^2
// as a DIAGNOSTIC: an OCR reading of the informal note's Lemma 3.3 suggested this object, but it does
// NOT equal 1.3275 at the cosine (it gives ~1.3328) -- the Lean formalization confirms the quadratic
// quotient is the true objective; the quartic reading is a garbled extraction.
//
// All quadrature: plain trapezoid, f64.

use std::f64::consts::PI;

fn main() {
    let n: usize = 4001; // grid on [-1/2, 1/2]
    let (u, w) = grid(-0.5, 0.5, n);
    let r2 = 2.0f64.sqrt();
    let s = 1.0 / r2; // 1/sqrt2

    println!("=== exact constants (lambda = 1) ===");
    let q0 = 0.5 + s * s.cos() / s.sin(); // 1/2 + (1/sqrt2) cot(1/sqrt2) = 1/c1*
    let prop = 2.0 - q0;
    let c1 = r2 * s.tan() / (1.0 + s * s.tan());
    println!("Q0   = 1/2 + (1/sqrt2)cot(1/sqrt2) = {:.16}", q0);
    println!("c1*  = sqrt2 tan(s)/(1+s tan(s))  = {:.16}", c1);
    println!("prop = 2 - 1/c1* = 3/2 - (1/sqrt2)cot(1/sqrt2) = {:.16}  (brief: 0.6725007036794116)", prop);
    // Lean closed forms of the moments: a* = int v*, b* = int v*^2, J* = intint |s-s'| v* v*
    let a_star = r2 * s.sin();
    let b_star = 0.5 + (2.0 * s).sin() / (4.0 * s);
    let j_star = (2.0 * s).sin() / (8.0 * s.powi(3)) - (2.0 * s).cos() / (4.0 * s * s);
    println!("Lean moments: a* = {:.8}, b* = {:.8}, J* = {:.8};  b*+J* = {:.8}; a*^2/(b*+J*) = {:.8}",
        a_star, b_star, j_star, b_star + j_star, a_star * a_star / (b_star + j_star));
    println!();

    // ---- identity checks at the cosine ----
    println!("=== identity checks at v* = cos(sqrt2 u) on |u|<=1/2 ===");
    let psi_cos: Vec<f64> = (0..n).map(|i| (r2 * u[i]).cos()).collect();
    let (q2, q4) = quotients(&u, &w, &psi_cos);
    let i2 = dot(&w, &psi_cos, &psi_cos);
    let i1 = dot(&w, &psi_cos, &vec![1.0; n]);
    println!("Q_quad(v*)  = {:.12}   (target 1/c1* = {:.12})", q2, q0);
    println!("Q_quart(v*) = {:.12}   (diagnostic only; NOT 1/c1*)", q4);
    println!("int v^2 = {:.8},  int v = {:.8}", i2, i1);
    // quadratic identity: int v^2 + 2 int_0^1 w (v*v)(w) dw = q0 (int v)^2   (use conv for even v)
    let conv_lin = conv_int(&u, &w, &psi_cos, &psi_cos);
    let lhs_q = i2 + 2.0 * conv_lin;
    let rhs_q = q0 * i1 * i1;
    println!("quad identity: int v^2 + 2 int w(v*v) = {:.10}  vs q0 (int v)^2 = {:.10}  diff {:.3e}",
        lhs_q, rhs_q, lhs_q - rhs_q);
    // quartic identity (should FAIL): int v^4 + 2 int z (v^2*v^2) =? q0 (int v^2)^2
    let psi2: Vec<f64> = psi_cos.iter().map(|x| x * x).collect();
    let i4 = dot(&w, &psi2, &psi2);
    let conv4 = conv_int(&u, &w, &psi2, &psi2);
    let lhs_q4 = i4 + 2.0 * conv4;
    let rhs_q4 = q0 * i2 * i2;
    println!("quart identity: int v^4 + 2 int z(v^2*v^2) = {:.10}  vs q0 (int v^2)^2 = {:.10}  diff {:.3e}",
        lhs_q4, rhs_q4, lhs_q4 - rhs_q4);
    println!();

    // ---- candidate table ----
    println!("=== candidate windows on |u|<=1/2  (objective Q_quad; proportion 2 - Q_quad) ===");
    let mut cands: Vec<(String, Vec<f64>)> = Vec::new();
    cands.push(("flat  1".to_string(), vec![1.0; n]));
    cands.push(("v* = cos(sqrt2 u)  [MT]".to_string(), psi_cos.clone()));
    for lam in [1.0f64, 1.2, 1.4142135623730951, 1.6, 2.0, 3.0, PI] {
        let v: Vec<f64> = (0..n).map(|i| (lam * u[i]).cos()).collect();
        cands.push((format!("cos({:.3} u)", lam), v));
    }
    for k in 1..=4usize {
        let v: Vec<f64> = (0..n).map(|i| (1.0 - 4.0 * u[i] * u[i]).powi(k as i32)).collect();
        cands.push((format!("(1-4u^2)^{}", k), v));
    }
    {
        // quartic window from the paper's Remark 7.3 (xi' zeros): v(s) = 1 - 7/100 (2s)^2 - 51/200 (2s)^4
        let v: Vec<f64> = (0..n)
            .map(|i| 1.0 - 0.07 * (2.0 * u[i]).powi(2) - 0.255 * (2.0 * u[i]).powi(4))
            .collect();
        cands.push(("xi'-quartic profile (on zeta)".to_string(), v));
    }
    {
        let v: Vec<f64> = (0..n).map(|i| 1.0 + u[i]).collect();
        cands.push(("1 + u (tilt, non-even)".to_string(), v));
    }
    {
        let v: Vec<f64> = (0..n).map(|i| (r2 * u[i]).cos() + 0.5 * (PI * u[i]).sin()).collect();
        cands.push(("cos + 0.5 sin(pi u) (non-even)".to_string(), v));
    }

    for (name, v) in &cands {
        let (q2, _q4) = quotients(&u, &w, v);
        println!("{:<34} Q_quad = {:.6}   2-Q_quad = {:.6}", name, q2, 2.0 - q2);
    }
    println!();

    // ---- support-width family: v_c = cos(sqrt2 u) 1_{|u|<=c} ----
    println!("=== support width c (bandwidth constraint: c <= 1/2) ===");
    println!("analytic Q_quad(c) = c + (1/sqrt2) cot(sqrt2 c):");
    for c in [0.30f64, 0.40, 0.45, 0.50, 0.55, 0.60, 0.80, 1.00, PI / (2.0 * r2)] {
        let q2a = c + s * (r2 * c).cos() / (r2 * c).sin();
        let flag = if c > 0.5 { "  <-- VIOLATES bandwidth<=1" } else { "" };
        println!("  c = {:.4}: Q_quad = {:.6}  2-Q = {:.6}{}", c, q2a, 2.0 - q2a, flag);
        let nc = 4001;
        let (uc, wc) = grid(-c, c, nc);
        let v: Vec<f64> = (0..nc).map(|i| (r2 * uc[i]).cos()).collect();
        let (q2n, _) = quotients(&uc, &wc, &v);
        println!("        numeric: Q_quad = {:.6}", q2n);
    }
    println!();

    // ---- global minimizer of Q_quad over ALL grid functions (no evenness imposed) ----
    println!("=== grid minimizer of Q_quad (free, no evenness) ===");
    let (psi_star, q_star) = grid_minimizer(&u, &w);
    println!("Q* = {:.12}  (target 1/c1* = {:.12})  diff = {:.3e}", q_star, q0, q_star - q0);
    let norm_cos: Vec<f64> = psi_cos.iter().map(|x| x / i1).collect();
    let mut diff_max = 0.0f64;
    for i in 0..n {
        let d = (psi_star[i] - norm_cos[i]).abs();
        if d > diff_max {
            diff_max = d;
        }
    }
    let mut asym = 0.0f64;
    for i in 0..n {
        let j = n - 1 - i;
        asym = asym.max((psi_star[i] - psi_star[j]).abs());
    }
    println!("||psi* - cos/int cos||_inf = {:.3e};  max |psi*(u)-psi*(-u)| = {:.3e}", diff_max, asym);
    println!();

    // ---- lambda scan: c*_lambda increasing on (0,1]? and Q_quad of cos(sqrt2 lam u) ----
    println!("=== lambda family v*_lam(s) = cos(sqrt2 lam s),  c*_lam = sqrt2 tan(theta)/(1+theta tan(theta)), theta = lam/sqrt2 ===");
    for lam in [0.2f64, 0.4, 0.6, 0.8, 0.9, 0.95, 1.0] {
        let th = lam / r2;
        let cl = r2 * th.tan() / (1.0 + th * th.tan());
        println!("  lambda = {:.2}: c*_lam = {:.8}   2 - 1/c*_lam = {:.8}", lam, cl, 2.0 - 1.0 / cl);
    }
}

// ---------- utilities ----------

fn grid(a: f64, b: f64, n: usize) -> (Vec<f64>, Vec<f64>) {
    let h = (b - a) / (n - 1) as f64;
    let u: Vec<f64> = (0..n).map(|i| a + i as f64 * h).collect();
    let w: Vec<f64> = (0..n)
        .map(|i| {
            let c = if i == 0 || i == n - 1 { 0.5 } else { 1.0 };
            c * h
        })
        .collect();
    (u, w)
}

fn dot(w: &[f64], a: &[f64], b: &[f64]) -> f64 {
    w.iter().zip(a).zip(b).map(|((&wi, &ai), &bi)| wi * ai * bi).sum()
}

// int_0^1 z * (f * g)(z) dz, z = m*h. Correct trapezoid weights on each sub-interval [x_m, x_{n-1}]
// (endpoints of the convolution interval get weight 0.5*h, interiors h).
fn conv_int(u: &[f64], w: &[f64], f: &[f64], g: &[f64]) -> f64 {
    let n = u.len();
    let h = u[1] - u[0];
    let mut wz = vec![0.0; n];
    for m in 0..n {
        wz[m] = if m == 0 || m == n - 1 { 0.5 } else { 1.0 } * h;
    }
    let mut out = 0.0;
    for m in 1..n {
        let z = m as f64 * h;
        if z > 1.0 + 1e-12 {
            break;
        }
        let mut s = 0.0;
        for i in m..n {
            // trapezoid weights for the integral over [x_m, x_{n-1}]: 0.5h at i=m and i=n-1
            let wgt = if i == m || i == n - 1 { 0.5 * h } else { h };
            s += wgt * f[i] * g[i - m];
        }
        out += wz[m] * z * s;
    }
    out
}

fn quotients(u: &[f64], w: &[f64], psi: &[f64]) -> (f64, f64) {
    let n = u.len();
    // Q_quad = [int psi^2 + intint |u-v| psi psi] / (int psi)^2   (the true objective, 1/c_1)
    let i1 = dot(w, psi, &vec![1.0; n]);
    let i2 = dot(w, psi, psi);
    let mut dbl = 0.0;
    for i in 0..n {
        for j in 0..n {
            dbl += w[i] * w[j] * (u[i] - u[j]).abs() * psi[i] * psi[j];
        }
    }
    let q2 = (i2 + dbl) / (i1 * i1);
    // Q_quart (diagnostic): [int psi^4 + 2 int_0^1 z (psi^2 * psi^2)(z) dz] / (int psi^2)^2
    let psi2: Vec<f64> = psi.iter().map(|x| x * x).collect();
    let i4 = dot(w, &psi2, &psi2);
    let conv4 = conv_int(u, w, &psi2, &psi2);
    let q4 = (i4 + 2.0 * conv4) / (i2 * i2);
    (q2, q4)
}

// min v^T M v  s.t. w^T v = 1,  M = diag(w) + W K W,  K_ij = |u_i - u_j|;  Q* = 1/(w^T M^-1 w)
fn grid_minimizer(u: &[f64], w: &[f64]) -> (Vec<f64>, f64) {
    let n = u.len();
    let mut x = vec![0.0f64; n];
    let mut r = w.to_vec();
    let mut p = r.clone();
    let mut rsold: f64 = r.iter().map(|v| v * v).sum();
    for _iter in 0..500 {
        let mp = matvec(u, w, &p);
        let denom: f64 = p.iter().zip(&mp).map(|(a, b)| a * b).sum();
        if denom.abs() < 1e-300 {
            break;
        }
        let alpha = rsold / denom;
        for i in 0..n {
            x[i] += alpha * p[i];
            r[i] -= alpha * mp[i];
        }
        let rsnew: f64 = r.iter().map(|v| v * v).sum();
        if rsnew.sqrt() < 1e-13 {
            break;
        }
        let beta = rsnew / rsold;
        for i in 0..n {
            p[i] = r[i] + beta * p[i];
        }
        rsold = rsnew;
    }
    let wtx: f64 = w.iter().zip(&x).map(|(a, b)| a * b).sum();
    for xi in x.iter_mut() {
        *xi /= wtx;
    }
    (x, 1.0 / wtx)
}

fn matvec(u: &[f64], w: &[f64], x: &[f64]) -> Vec<f64> {
    let n = u.len();
    let mut y = vec![0.0f64; n];
    for i in 0..n {
        let mut s = 0.0;
        for j in 0..n {
            s += w[j] * (u[i] - u[j]).abs() * x[j];
        }
        y[i] = w[i] * x[i] + w[i] * s;
    }
    y
}
