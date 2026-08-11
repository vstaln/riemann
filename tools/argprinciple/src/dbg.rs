mod zeta;
use zeta::*;
fn main() {
    for t in [1001.33, 1001.34, 1001.349483, 1001.35, 1001.3505, 1001.351, 1001.355, 1001.36] {
        let n = ((1.6 * t / (2.0 * std::f64::consts::PI)).ceil().max(10.0)) as usize;
        let lns: Vec<f64> = (0..n).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
        let (re, im, err) = zeta_em_cert(0.5, t, t, n, &lns, 40);
        let (th, _) = theta_cert(t);
        let z = re * th.cos() - im * th.sin();
        let zerr = err + (re.abs() + im.abs()) * (0.0 + 4.0 * 2.220446049250313e-16);
        println!("t={:12.6}  Z={:+.12e}  err={:.2e}  sign-certain: {}", t, z, zerr, z > zerr || z < -zerr);
    }
}
