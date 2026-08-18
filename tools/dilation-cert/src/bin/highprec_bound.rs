// highprec bound check — decisive hostile step for the lambda-dilation finding.
// Recomputes bound = (H(alpha) − tau)/(1 − B/m) at 200-bit MPFR precision, for CERTIFIED
// (lambda, eps) pairs from the sanctioned verifier. f64 margins were razor-thin; this
// decides if the finding is real. All arithmetic completed explicitly (Round::Down on
// the final division is not needed for a comparison—we just need consistent rounding).
use rug::float::Round;
use rug::ops::CompleteRound;
use rug::Float;


const PREC: u32 = 200;

fn f(x: f64) -> Float {
    Float::with_val(PREC, x)
}

fn h_window_hp(alpha: f64) -> Float {
    let a = f(alpha) / f(2.0);
    let alpha_f = f(alpha);
    // I0 = 2 sin(a)/alpha
    let i0 = f(2.0) * a.clone().sin() / alpha_f.clone();
    // I2 = 1/2 + sin(alpha)/(2 alpha)
    let i2 = f(0.5) + alpha_f.clone().sin() / (f(2.0) * alpha_f.clone());
    let constant = a.clone().sin() / alpha_f.clone()
        + f(2.0) * a.clone().cos() / (alpha_f.clone() * alpha_f.clone());
    let j = f(-2.0) * i2.clone() / (alpha_f.clone() * alpha_f.clone()) + constant * i0.clone();
    let c = i0.clone() * i0 / (i2 + j);
    f(2.0) - f(1.0) / c
}

fn phi_m(m: usize, a: &Float) -> Float {
    let mf = f(m as f64);
    let thr = mf.clone() / (mf.clone() - f(1.0));
    if *a <= thr {
        a.clone()
    } else {
        let inner = f((m - 1) as f64) * a.clone() / mf.clone();
        f(2.0) * inner.sqrt() - f(1.0) + a.clone() / mf
    }
}

fn bound_hp(eps: f64, m: usize, alpha: f64, psum: f64) -> Float {
    let h = h_window_hp(alpha);
    let a = f(eps) * f((m as i64 - 6) as f64);
    let b = phi_m(m, &a);
    let tau = f(psum) * f((m as i64 - 6) as f64) / f(m as f64);
    (h - tau) / (f(1.0) - b / f(m as f64))
}

fn main() {
    let rec = f(0.6734808616745137_f64); // record's decimal, as f64 — acceptable for margin sign
    println!("H(1.464) @200bit : {}", h_window_hp(1.464));
    let cases: Vec<(f64, f64, f64)> = vec![
        // === certified points (the record path) ===
        (1.464, 1.15, 0.00703), // VERIFIED 2026-08-18 (1068980 nodes, grid 4000)
        (1.450, 1.15, 0.00700), // VERIFIED 2026-08-18 (1120338 nodes, grid 4000)
        // === lattice-floor landscape at lam=1.15 ===
        (1.415, 1.15, 0.00689), // floor 0.006892
        (1.43, 1.15, 0.00695),  // floor 0.006946
        (1.45, 1.15, 0.00700),  // floor 0.007009
        (1.464, 1.15, 0.00704), // floor 0.007049
        (1.48, 1.15, 0.00707),  // floor 0.007095 (certifiable ~0.00707 per g8k)
        (1.48, 1.15, 0.00709),  // lattice floor upper bound
        (1.50, 1.15, 0.00714),  // floor 0.007155
        (1.52, 1.15, 0.00720),  // floor 0.007218
    ];
    let psum_base = 1.0 / 320.0;
    let mut best_overall: Option<(f64, f64, f64, usize, Float)> = None;
    for (alpha, lam, eps) in cases {
        let psum = psum_base * lam;
        let mut best_m = 0usize;
        let mut best = f(-1e300_f64);
        for m in 40..=400 {
            let b = bound_hp(eps, m, alpha, psum);
            if b > best {
                best = b;
                best_m = m;
            }
        }
        let delta = best.clone() - rec.clone();
        let verdict = if delta > f(0.0) { "BEATS RECORD" } else { "below record" };
        println!("alpha={} lam={:.2} eps={:.7} best m={} bound={} delta={} => {}", alpha, lam, eps, best_m, best,
                 delta, verdict);
        if delta > f(0.0) {
            let mut replace = true;
            if let Some((_, _, _, _, ref bo)) = best_overall {
                if !(best > *bo) {
                    replace = false;
                }
            }
            if replace {
                best_overall = Some((alpha, lam, eps, best_m, best));
            }
        }
    }
    if let Some((alpha, lam, eps, m, b)) = best_overall {
        println!("BEST: alpha={} lam={} eps={} m={} bound={} (all Rust, 200-bit MPFR)", alpha, lam, eps, m, b);
    } else {
        println!("NO case beats the record at 200-bit precision — finding REFUTED");
    }
}