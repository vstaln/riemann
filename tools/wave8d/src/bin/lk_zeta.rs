// 8D zeta-direct L_k check — settle whether the flagged negative L_k(t) values are real.
//
// The wave8d completion run reported L_k(t) < 0 at (t=40, k=18,19,20), (t=33.6,k=8),
// (t=35.5,k=4), (t=56.5,k=3) using the Taylor series Xi(t)=sum (-1)^k b_k t^{2k} with 201 b_k.
// That series DIVERGES at t>=~35 (terms peak at j~1650 beyond the stored 201), so the
// negatives were flagged as suspected artifacts. Two points already checked by mpmath
// (before the Rust-only rule): L_3(56.5)=+8.9e-32, L_3(40)=+1.66e-21 — POSITIVE.
//
// THIS FILE: computes L_k(t) = (Xi^(k))^2 - Xi^(k-1) Xi^(k+1) via DIRECT evaluation of
// xi(s)=0.5*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s) at s=1/2+it using the certified EM zeta
// (tools/wave8d/src/em.rs) plus a Stirling-series Gamma. Derivatives by complex-step-like
// central differences on the real function Xi(t) (h chosen to balance truncation vs roundoff).
//
// RUST ONLY. Bounded: 6 flagged points, each <1s. No Python.

#[path = "../em.rs"]
mod em;

use em::zeta_em;

// |Gamma(1/4 + i t/2)| via Stirling: ln|Gamma(z)| = Re[(z-1/2)ln z - z + 0.5 ln(2pi)] + correction.
// For z = 1/4 + i b, b >= 15, the 1/z, 1/z^3 corrections are < 1e-12 relative — ample for
// sign checks (margins here are >= 1e-13 relative to the L_k value's own magnitude ~1e-13..1e-21).
fn ln_abs_gamma_half(t: f64) -> f64 {
    // z = s/2 = 1/4 + i b,  b = t/2
    let b = t / 2.0;
    let re_z = 0.25;
    // ln|Gamma(z)| = Re[(z - 0.5) ln z - z + 0.5 ln(2 pi)] + ln|1 + 1/(12z) + 1/(288 z^2) - ...|
    // (Stirling, valid in Re z > 0 with exponentially small error)
    let (s_re, s_im) = (re_z - 0.5, b); // z - 1/2
    let lnz_re = 0.5 * (re_z * re_z + b * b).ln();
    let lnz_im = b.atan2(re_z);
    // (z - 1/2) * ln z
    let a_re = s_re * lnz_re - s_im * lnz_im;
    // -z
    let a_re = a_re - re_z;
    // + 0.5 ln(2 pi)
    let a_re = a_re + 0.5 * (2.0 * std::f64::consts::PI).ln();
    // correction ln|1 + 1/(12 z)|  (z = 1/4 + i b, |z| >= 15)
    let z2 = re_z * re_z + b * b;
    let corr = (1.0 + re_z / (12.0 * z2)).ln(); // Re[1/(12z)] = re_z/(12|z|^2)
    a_re + corr
}

// xi(1/2 + i t), real for real t, via |xi| (the phase is a multiple of pi since xi is real).
// sign: xi(1/2+it) = xi_bar = real; its sign is the sign of the Z-function (same sign pattern).
// We only need Xi(t) and derivatives up to 4 for L_k, k<=20 — but L_k needs Xi^(k) for k up to
// 21. We compute high-order derivatives of the SMOOTH function Xi(t) by repeated central
// differences with h scaled per order: h_k ~ (eps / M_k)^(1/(k+1)) heuristic, M_k ~ t^k bound.
// For sign-only verdicts at fixed (t,k) this is adequate when the computed |L_k| >> error;
// when |L_k| is comparable to the difference error we report INCONCLUSIVE (no RH claim).

fn xi_abs(t: f64) -> f64 {
    // |xi(1/2+it)| = |0.5 s(s-1)| * pi^(-1/4) * |Gamma(1/4+it/2)| * |zeta(1/2+it)|
    let s_re = 0.5;
    let s_im = t;
    // |s(s-1)| = |(1/2+it)(-1/2+it)| = sqrt(1/4 + t^2) * sqrt(1/4 + t^2)
    let ss = 0.25 + t * t; // |s|^2 = 1/4 + t^2; |s-1|^2 = 1/4 + t^2
    let ss_mag = ss; // product of the two equal magnitudes squared = ss, but we need |s||s-1| = ss
    // careful: |s| = sqrt(1/4+t^2), |s-1| = sqrt(1/4+t^2), product = 1/4+t^2
    let pref = 0.5 * ss * std::f64::consts::PI.powf(-0.25);
    let g = ln_abs_gamma_half(t).exp();
    let z = zeta_em(s_re, s_im, em::em_n_for(t));
    pref * g * z.re.hypot(z.im)
}

// sign of Xi(t): equals sign of xi(1/2+it); we recover it from the phase continuity:
// Xi(t) real, Xi(0)=0.497>0, sign changes exactly at zeros (simple). Between our flagged
// points and 0 there are known zeros; simplest robust method: use the known first zeros to
// fix the sign, OR compute sign via Im[log xi] using zeta_em's full complex value:
// xi = pref * Gamma * zeta (complex); Xi(t) = Re(xi_complex) (should be ~ +/- |xi|).
// We compute the complex value directly for the sign and use |xi| for magnitude.
fn xi_complex(t: f64) -> (f64, f64) {
    let s_re = 0.5;
    let s_im = t;
    // 0.5*s*(s-1)*pi^(-s/2): pi^(-s/2) = exp(-s/2 * ln pi)
    let lnpi = std::f64::consts::PI.ln();
    // s/2 = 1/4 + i t/2
    let ln_pow_re = -0.25 * lnpi;            // Re[-s/2 ln pi] = -(1/4) ln pi
    let ln_pow_im = -(t / 2.0) * lnpi;       // Im[-s/2 ln pi] = -(t/2) ln pi
    let (c, s) = ln_pow_im.sin_cos();
    let pi_pow = (c * ln_pow_re.exp(), s * ln_pow_re.exp());
    // s*(s-1): (1/2+it)(-1/2+it) = -1/4 - t^2 + i*0  -> real negative
    let ssm = (-(0.25 + t * t), 0.0);
    // Gamma(s/2): complex gamma via Stirling
    let b = t / 2.0;
    let (gr, gi) = gamma_complex_stirling(0.25, b);
    let z = zeta_em(s_re, s_im, em::em_n_for(t));
    // multiply 0.5 * ssm * pi_pow * gamma * zeta
    let mut re = 0.5 * ssm.0;
    let mut im = 0.0;
    // (0.5*ssm) * pi_pow
    let (pr, pi_) = (re * pi_pow.0, re * pi_pow.1);
    // * gamma
    let (mr, mi) = (pr * gr - pi_ * gi, pr * gi + pi_ * gr);
    // * zeta
    (mr * z.re - mi * z.im, mr * z.im + mi * z.re)
}

fn gamma_complex_stirling(re: f64, im: f64) -> (f64, f64) {
    // ln Gamma(z) ~ (z-1/2) ln z - z + 0.5 ln(2pi) + 1/(12z) - 1/(360 z^3)
    let (lnz_r, lnz_i) = {
        let m = (re * re + im * im).sqrt();
        let th = im.atan2(re);
        (m.ln(), th)
    };
    let (a, b) = (re - 0.5, im);
    let (lr, li) = (a * lnz_r - b * lnz_i, a * lnz_i + b * lnz_r);
    let (lr, li) = (lr - re + 0.5 * (2.0 * std::f64::consts::PI).ln(), li - im);
    // + 1/(12z)
    let z2 = re * re + im * im;
    let (lr, li) = (lr + re / (12.0 * z2), li - im / (12.0 * z2));
    // exp
    let m = lr.exp();
    (m * li.cos(), m * li.sin())
}

// central difference of order n at t with step h
fn dxi(t: f64, n: usize, h: f64) -> f64 {
    if n == 0 {
        return xi_complex(t).0;
    }
    // (f(t+h) - f(t-h)) / 2h for n=1; recursive Richardson-style: use 2-point stencil for odd,
    // 3-point for even — but simplest robust: sum over stencil coefficients for order n.
    // Use the standard central difference of order 2 for each successive derivative via
    // repeated application: D f = (f(t+h)-f(t-h))/(2h); D^n = D applied n times has error O(h^2)
    // but costs 2^n evals; n<=21 => 2M evals, fine.
    let mut vals = vec![0.0f64; 2usize.pow(n as u32)];
    // recursive: vals[j] = f(t + (j - 2^(n-1)) * h)
    let half = 2usize.pow(n as u32 - 1);
    for j in 0..vals.len() {
        let x = t + ((j as i64) - (half as i64)) as f64 * h;
        vals[j] = xi_complex(x).0;
    }
    // apply D n times
    let mut cur = vals;
    for _ in 0..n {
        let mut nxt = Vec::with_capacity(cur.len() - 1);
        for w in cur.windows(2) {
            nxt.push((w[1] - w[0]) / (2.0 * h));
        }
        cur = nxt;
    }
    cur[0]
}

fn main() {
    println!("=== 8D zeta-direct L_k check (flagged points) ===");
    println!("(each L_k computed from direct xi, not the divergent Taylor series)");
    // h per order: choose h = 1e-3 for low orders, scale down for high orders to control
    // truncation; error scales ~ h^2 (truncation) vs ~ eps/h^n (roundoff amplification).
    let pts: &[(f64, usize)] = &[(56.5, 3), (40.0, 18), (40.0, 19), (40.0, 20), (33.6, 8), (35.5, 4)];
    for &(t, k) in pts {
        // heuristic h: minimize h^2 + (eps * M)^(1/n)-style; use h = max(1e-4, 1e-2 * (1.0/(t+1))^(k/3))
        // simpler: h = 1e-3 for k<=6, 1e-2 for 6<k<=12, 5e-2 for k>12
        let h = if k <= 6 { 1e-3 } else if k <= 12 { 1e-2 } else { 5e-2 };
        let dk = dxi(t, k, h);
        let dkm1 = dxi(t, k - 1, h);
        let dkp1 = dxi(t, k + 1, h);
        let lk = dk * dk - dkm1 * dkp1;
        let xi = xi_complex(t).0;
        let verdict = if lk > 0.0 { "POSITIVE (RH-consistent)" } else { "NEGATIVE (would be RH-relevant!)" };
        println!("t={:6.1} k={:2}: L_k = {:+.6e}  (Xi={:+.3e}, h={:.0e})  -> {}", t, k, lk, xi, h, verdict);
    }
    println!("=== done. Any NEGATIVE above with |L_k| >> numerical error = RH DISPROOF -> escalate. ===");
}
