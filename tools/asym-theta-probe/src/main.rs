//! Exploratory Rust scan for the asymmetric theta-Mellin idea from Antigravity.
//! It can falsify a strict modulus inequality but cannot prove one.
use std::f64::consts::PI;

#[derive(Clone, Copy)]
struct C { re: f64, im: f64 }
impl C {
    fn zero() -> Self { Self { re: 0.0, im: 0.0 } }
    fn add(self, o: Self) -> Self { Self { re: self.re + o.re, im: self.im + o.im } }
    fn scale(self, a: f64) -> Self { Self { re: self.re * a, im: self.im * a } }
    fn abs(self) -> f64 { self.re.hypot(self.im) }
}

fn phi(u: f64) -> f64 {
    let e2 = (2.0 * u).exp();
    let e45 = (4.5 * u).exp();
    let e25 = (2.5 * u).exp();
    let mut s = 0.0;
    for n in 1..=14 {
        let n2 = (n * n) as f64;
        let e = (-PI * n2 * e2).exp();
        s += (2.0 * PI * PI * n2 * n2 * e45 - 3.0 * PI * n2 * e25) * e;
    }
    2.0 * s
}

fn f_plus(x: f64, y: f64, samples: usize) -> C {
    let upper = 4.0;
    let h = upper / samples as f64;
    let mut sum = C::zero();
    for k in 0..=samples {
        let u = k as f64 * h;
        let weight = if k == 0 || k == samples { 1.0 } else if k % 2 == 1 { 4.0 } else { 2.0 };
        let a = phi(u) * (-y * u).exp();
        sum = sum.add(C { re: a * (x * u).cos(), im: a * (x * u).sin() }.scale(weight));
    }
    sum.scale(h / 3.0)
}

fn main() {
    let samples = 4000usize;
    let mut worst_log_ratio = f64::INFINITY;
    let mut worst = (0.0, 0.0, 0.0, 0.0);
    let mut tested = 0usize;
    for ix in 0..=100 {
        let x = ix as f64 * 0.5;
        for iy in 1..=20 {
            let y = iy as f64 * 0.05;
            let a = f_plus(x, y, samples);
            let b = f_plus(-x, -y, samples);
            let ratio = (b.abs() / a.abs()).ln();
            if ratio < worst_log_ratio {
                worst_log_ratio = ratio;
                worst = (x, y, a.abs(), b.abs());
            }
            tested += 1;
        }
    }
    println!("ASYM_THETA_SCAN samples={} points={}", samples, tested);
    println!("worst_log(|F+(-z)|/|F+(z)|)={:.17e} at x={} y={}", worst_log_ratio, worst.0, worst.1);
    println!("magnitudes F+(z)={:.17e} F+(-z)={:.17e}", worst.2, worst.3);
    println!("verdict={}", if worst_log_ratio <= 0.0 {
        "REVERSED_DOMINANCE_REFUTED_ON_GRID"
    } else {
        "REVERSED_DOMINANCE_NOT_REFUTED_ON_GRID"
    });
}
