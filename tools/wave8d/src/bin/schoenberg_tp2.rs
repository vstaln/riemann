// Schoenberg shift-kernel TP2 probe — K(x,y) = Xi(x-y), Xi(t) = xi(1/2+it).
//
// Lever (DISPROOF-CAPABLE, never run here): Schoenberg (1951) f in LP  <=>  the
// shift kernel K(x,y)=f(x-y) is totally positive. RH  <=>  Xi in LP (de Bruijn).
// Hence: ANY 2x2 minor det[[Xi(x1-y1),Xi(x1-y2)],[Xi(x2-y1),Xi(x2-y2)]] < 0 with
// x1<x2,y1<y2  =>  Xi not TP  =>  Xi not LP  =>  RH FALSE (escalate).
// No violation found => RH-CONSISTENT ONLY (a finite grid can never prove RH).
//
// NOT the 2026-08-15 Hankel lever (Taylor-coefficient Hankel matrix (b_{i+j}),
// CLOSED: RH forces it ALTERNATING, not TP). Different object; do not merge.
//
// Controls: exp(-t^2) in LP (all minors >= 0, even near zeros it has none),
// sin(t)/t in LP with REAL zeros (stresses near-zero sampling), and
// f(t)=1+t^2-t^4/2 NOT in LP (zeros t=+-1.653 real, +-0.856i imaginary; note
// x=(0,1),y=(0,1) gives minor = 1 - f(1)^2 = -1.25 < 0 by hand) — must be found.

#[path = "../em.rs"]
mod em;

use em::zeta_em;

const N600: usize = 600;   // as lk_zeta.rs (certified err ~1e-100)
const N1200: usize = 1200; // for empirical error estimate

// ---- complex Gamma via Stirling (verbatim from lk_zeta.rs) -------------------
fn gamma_complex_stirling(re: f64, im: f64) -> (f64, f64) {
    let (lnz_r, lnz_i) = {
        let m = (re * re + im * im).sqrt();
        let th = im.atan2(re);
        (m.ln(), th)
    };
    let (a, b) = (re - 0.5, im);
    let (lr, li) = (a * lnz_r - b * lnz_i, a * lnz_i + b * lnz_r);
    let (lr, li) = (lr - re + 0.5 * (2.0 * std::f64::consts::PI).ln(), li - im);
    let z2 = re * re + im * im;
    let z3 = z2 * (re * re + im * im).sqrt();
    let (lr, li) = (
        lr + re / (12.0 * z2) - re / (360.0 * z3),
        li - im / (12.0 * z2) + im / (360.0 * z3),
    );
    let m = lr.exp();
    (m * li.cos(), m * li.sin())
}

// xi(1/2+it), s = 0.5 + i t  (verbatim from lk_zeta.rs, n parametrized)
fn xi_complex(t: f64, n: usize) -> (f64, f64) {
    let s_re = 0.5;
    let s_im = t;
    let lnpi = std::f64::consts::PI.ln();
    let ln_pow_re = -0.25 * lnpi;
    let ln_pow_im = -(t / 2.0) * lnpi;
    let (sn, cs) = ln_pow_im.sin_cos();
    let pi_pow = (cs * ln_pow_re.exp(), sn * ln_pow_re.exp());
    let ssm = (-(0.25 + t * t), 0.0);
    let b = t / 2.0;
    let (gr, gi) = gamma_complex_stirling(0.25, b);
    let z = zeta_em(s_re, s_im, n);
    let re = 0.5 * ssm.0;
    let (pr, pi_) = (re * pi_pow.0, re * pi_pow.1);
    let (mr, mi) = (pr * gr - pi_ * gi, pr * gi + pi_ * gr);
    (mr * z.re - mi * z.im, mr * z.im + mi * z.re)
}

fn xi(t: f64, n: usize) -> f64 {
    xi_complex(t, n).0
}

// ---- deterministic RNG (xorshift64*) -----------------------------------------
struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x >> 12;
        x ^= x << 25;
        x ^= x >> 27;
        self.0 = x;
        x.wrapping_mul(0x2545F4914F6CDD1D)
    }
    fn unif(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1u64 << 53) as f64
    }
}

// generic 2x2-minor probe on [0,tmax]; zeros = near-zero windows (empty = none)
fn probe(label: &str, f: &dyn Fn(f64) -> f64, tmax: f64, zeros: &[f64], px: usize, py: usize) -> (f64, f64, f64, f64, usize, usize) {
    let mut rng = Rng(0x9E3779B97F4A7C15);
    let mut min_minor = f64::INFINITY;
    let mut argmin = (0.0f64, 0.0f64, 0.0f64, 0.0f64);
    let mut n_neg = 0usize;
    let mut n_tot = 0usize;
    // random grid
    for _ in 0..px {
        let u1 = rng.unif();
        let u2 = rng.unif();
        let x1 = u1 * tmax;
        let x2 = x1 + u2 * (tmax - x1);
        for _ in 0..py {
            let v1 = rng.unif();
            let v2 = rng.unif();
            let y1 = v1 * tmax;
            let y2 = y1 + v2 * (tmax - y1);
            let d11 = x1 - y1;
            let d12 = x1 - y2;
            let d21 = x2 - y1;
            let d22 = x2 - y2;
            let m = f(d11) * f(d22) - f(d12) * f(d21);
            n_tot += 1;
            if m < min_minor {
                min_minor = m;
                argmin = (x1, x2, y1, y2);
            }
            if m < 0.0 {
                n_neg += 1;
            }
        }
    }
    // near-zero windows
    for &z in zeros {
        for s in [1.0f64, -1.0f64] {
            for i in 0..20usize {
                let eps1 = ((i as f64) / 20.0 - 0.5) * 0.1; // -0.05..0.05
                let eps2 = ((i as f64) / 20.0 - 0.5) * 0.08;
                let x1 = 30.0;
                let y1 = 30.0 - (s * z + eps1);
                let a = 0.05 + 1.45 * rng.unif();
                let b = 0.05 + 1.45 * rng.unif();
                let x2 = x1 + a;
                let y2 = y1 + b;
                let d11 = x1 - y1;
                let d12 = x1 - y2;
                let d21 = x2 - y1;
                let d22 = x2 - y2;
                let m = f(d11) * f(d22) - f(d12) * f(d21);
                n_tot += 1;
                if m < min_minor {
                    min_minor = m;
                    argmin = (x1, x2, y1, y2);
                }
                if m < 0.0 {
                    n_neg += 1;
                }
            }
        }
    }
    println!(
        "{:28} tmax={:4.0} px={:3} py={:3} zw={:2} : min_minor={:+.6e} at (x1,x2,y1,y2)=({:.3},{:.3},{:.3},{:.3})  neg={}/{}",
        label, tmax, px, py, zeros.len(), min_minor, argmin.0, argmin.1, argmin.2, argmin.3, n_neg, n_tot
    );
    (min_minor, argmin.0, argmin.1, argmin.2, n_neg, n_tot)
}

fn main() {
    let t0 = std::time::Instant::now();
    println!("=== Schoenberg shift-kernel TP2 probe, Xi(t)=xi(1/2+it), n_em=600 ===\n");

    // ---- sanity gates -------------------------------------------------------
    let xi0 = xi(0.0, N600);
    println!("Xi(0) = {:.15}  (expect 0.497120778188314)", xi0);
    // evenness
    let mut ev_max = 0.0f64;
    for i in 0..=60 {
        let t = i as f64;
        let d = (xi(t, N600) - xi(-t, N600)).abs();
        ev_max = ev_max.max(d);
    }
    println!("max |Xi(t) - Xi(-t)| over t=0..60 = {:.3e}", ev_max);
    // zeros
    let gammas = [
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719,
        43.327073, 48.005150, 49.773832, 52.970321, 56.446248,
    ];
    for (i, &g) in gammas.iter().enumerate() {
        let (r, im_) = xi_complex(g, N600);
        println!("|Xi(gamma_{:2})| at t={:9.6} = {:.3e}", i + 1, g, r.hypot(im_));
    }
    // sign pattern
    let mid = [7.6, 17.6, 23.05, 27.7, 31.7, 34.7, 39.2, 42.1, 45.7, 48.9, 51.4, 54.7, 57.9, 62.1, 66.1];
    let mut ok = true;
    for (i, &t) in mid.iter().enumerate() {
        let r = xi(t, N600);
        let s = if r >= 0.0 { 1 } else { -1 };
        let exp = if i % 2 == 0 { 1 } else { -1 };
        ok &= s == exp;
    }
    println!("sign pattern at 15 midpoints: {}", if ok { "ALL OK" } else { "FAILED — STOP" });
    // empirical error: |Xi_600 - Xi_1200|
    let mut err_max = 0.0f64;
    let mut err_t = 0.0f64;
    for i in 0..=60 {
        for &s in &[1.0f64, -1.0f64] {
            let t = s * (i as f64);
            let e = (xi(t, N600) - xi(t, N1200)).abs();
            if e > err_max {
                err_max = e;
                err_t = t;
            }
        }
    }
    println!("empirical Xi error (|Xi_600 - Xi_1200|) max = {:.3e} at t={:.1}\n", err_max, err_t);
    let _ = t0;

    // ---- controls (validate convention + sensitivity) -----------------------
    let exp2 = |t: f64| (-t * t).exp();
    let sin_t: fn(f64) -> f64 = |t: f64| {
        if t.abs() < 1e-9 {
            1.0
        } else {
            t.sin() / t
        }
    };
    let nonlp = |t: f64| 1.0 + t * t - 0.5 * t * t * t * t;
    let sin_zeros: Vec<f64> = (1..=19).map(|k| std::f64::consts::PI * k as f64).collect();
    let nl_zeros = [1.653_073_5f64];
    println!("-- controls --");
    let (c1, ..) = probe("exp(-t^2) [LP]", &exp2, 3.0, &[], 150, 150);
    let (c2, ..) = probe("sin(t)/t [LP, real zeros]", &sin_t, 60.0, &sin_zeros, 150, 150);
    let (c3, ..) = probe("1+t^2-t^4/2 [NOT LP]", &nonlp, 6.0, &nl_zeros, 150, 150);
    let (c4, ..) = probe("1+t^2-t^4/2 [NOT LP] wide", &nonlp, 60.0, &nl_zeros, 150, 150);

    // ---- the target: Xi shift kernel ----------------------------------------
    println!("\n-- target: K(x,y)=Xi(x-y) on [0,60] --");
    let (m1, ..) = probe("Xi (40k grid)", &|t| xi(t, N600), 60.0, &gammas, 200, 200);
    let (m2, ..) = probe("Xi (100k grid)", &|t| xi(t, N600), 60.0, &gammas, 320, 320);

    // ---- verdict --------------------------------------------------------------
    let margin_rule = 1e3 * err_max; // need |minor| >= 1e3 * (abs err of each Xi entry)
    println!("\n-- verdict --");
    println!("controls: exp(-t^2) min={:+.3e} (must be >= 0)", c1);
    println!("          sin(t)/t min={:+.3e} (must be >= 0)", c2);
    println!("          1+t^2-t^4/2 min={:+.3e} (must be < 0)", c3.min(c4));
    println!("target  : Xi min over grids = min({:+.3e}, {:+.3e})", m1, m2);
    println!("Xi err estimate = {:.2e} ; minor margin rule |minor| >= {:.2e}", err_max, margin_rule);
    let mmin = m1.min(m2);
    let gate_ok = c1 >= 0.0 && c2 >= 0.0 && c3.min(c4) < 0.0;
    println!("control gates: {}", if gate_ok { "PASS (probe validated)" } else { "FAIL — DO NOT TRUST TARGET" });
    if !gate_ok {
        println!("VERDICT: INCONCLUSIVE — control gates failed.");
    } else if mmin < 0.0 && mmin.abs() > margin_rule {
        println!("VERDICT: ** RH DISPROOF SIGNAL ** min minor = {:+.6e} < 0, |minor| >> 1e3*err. ESCALATE.", mmin);
    } else if mmin < 0.0 {
        println!("VERDICT: INCONCLUSIVE — negative minor {:.2e} within error margin {:.2e}.", mmin, margin_rule);
    } else {
        println!("VERDICT: RH-CONSISTENT — all tested 2x2 minors >= 0 (min {:+.6e}). Finite grid: consistency only, can never prove RH.", mmin);
    }
    println!("\n=== done ===");
}
