// Debug the Newton interpolation with a known polynomial first
use rug::Float;
const PG: u32 = 210;
fn zf(prec: u32, v: f64) -> Float { Float::with_val(prec, v) }
fn interpolate(h: f64, ys: &[Float]) -> Vec<Float> {
    let n = ys.len();
    let mut diff: Vec<Vec<Float>> = vec![ys.to_vec()];
    for k in 1..n {
        let mut row = Vec::new();
        for i in 0..n - k {
            let d = Float::with_val(PG, &diff[k - 1][i + 1] - &diff[k - 1][i]);
            row.push(d);
        }
        diff.push(row);
    }
    let mut mon = vec![zf(PG, 0.0); n];
    for k in (0..n).rev() {
        let mut fact = 1.0;
        for j in 2..=k { fact *= j as f64; }
        let ck = Float::with_val(PG, &diff[k][0] / zf(PG, fact * h.powi(k as i32)));
        if k > 0 {
            let xk = (k as f64 - 1.0) * h;
            let mut shifted = vec![zf(PG, 0.0); n];
            for i in 0..n - 1 {
                shifted[i + 1] += mon[i].clone();
            }
            for i in 0..n {
                let t = Float::with_val(PG, &mon[i] * zf(PG, xk));
                shifted[i] = Float::with_val(PG, &shifted[i] - &t);
            }
            mon = shifted;
        }
        mon[0] = Float::with_val(PG, &mon[0] + &ck);
    }
    mon
}
fn main() {
    // test: y(x) = 6.5 x + 1.0 x^2 + 0.5 x^3 at x = 0, 0.1, ..., 0.6
    let h = 0.1;
    let n = 7;
    let mut ys = Vec::new();
    for i in 0..n {
        let x = i as f64 * h;
        let y = 6.5 * x + 1.0 * x * x + 0.5 * x * x * x;
        ys.push(zf(PG, y));
    }
    let mon = interpolate(h, &ys);
    println!("known poly 6.5x + x^2 + 0.5x^3 -> recovered coeffs:");
    for (i, c) in mon.iter().enumerate() {
        println!("  c{} = {:.12}", i, c.to_f64());
    }
    println!("expected: c0=0, c1=6.5, c2=1.0, c3=0.5, c4..c6=0");
    // now test with near-linear data + small noise
    let mut ys2 = Vec::new();
    for i in 0..n {
        let x = i as f64 * h;
        ys2.push(zf(PG, 6.5 * x + 1e-8 * (x * x)));
    }
    let mon2 = interpolate(h, &ys2);
    println!("\nnoisy-linear test:");
    for (i, c) in mon2.iter().enumerate() {
        println!("  c{} = {:.6e}", i, c.to_f64());
    }
}
