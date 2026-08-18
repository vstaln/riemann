// bound_probe: compute 200-bit bound for arbitrary (alpha, lam, eps) — probe only.
use rug::float::Round;
use rug::ops::CompleteRound;
use rug::Float;

const PREC: u32 = 200;
fn f(x: f64) -> Float { Float::with_val(PREC, x) }

fn h_window_hp(alpha: f64) -> Float {
    let a = f(alpha) / f(2.0);
    let alpha_f = f(alpha);
    let i0 = f(2.0) * a.clone().sin() / alpha_f.clone();
    let i2 = f(0.5) + alpha_f.clone().sin() / (f(2.0) * alpha_f.clone());
    let constant = a.clone().sin() / alpha_f.clone() + f(2.0) * a.clone().cos() / (alpha_f.clone() * alpha_f.clone());
    let j = f(-2.0) * i2.clone() / (alpha_f.clone() * alpha_f.clone()) + constant * i0.clone();
    let c = i0.clone() * i0 / (i2 + j);
    f(2.0) - f(1.0) / c
}

fn phi_m(m: usize, a: &Float) -> Float {
    let mf = f(m as f64);
    let thr = mf.clone() / (mf.clone() - f(1.0));
    if *a <= thr { a.clone() } else {
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
    let args: Vec<String> = std::env::args().collect();
    let alpha: f64 = args[1].parse().unwrap();
    let lam: f64 = args[2].parse().unwrap();
    let eps: f64 = args[3].parse().unwrap();
    let psum = 1.0 / 320.0 * lam;
    let mut best_m = 0usize; let mut best = f(-1e300_f64);
    for m in 40..=400 {
        let b = bound_hp(eps, m, alpha, psum);
        if b > best { best = b.clone(); best_m = m; }
    }
    println!("alpha={} lam={} eps={}: m={} bound={}", alpha, lam, eps, best_m, best);
    let dist = (best.clone() + f(1.0)) / f(2.0);
    println!("  distinct = {}", dist);
}
