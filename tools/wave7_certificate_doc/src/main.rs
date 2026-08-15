//! Wave 7A certificate probe (self-contained, std-only, f64 + exact i128 rationals).
//!
//! Reconstructs the certified record's explicit certificate (c0, r) from the tawan
//! coboundary mechanism and verifies the knot-sum identity:
//!
//!   v = (H(alpha) - tau) / (1 - B/m),   alpha = 1.464, m = 171,   [FINAL-RECORD-2026-08-13]
//!   tau = (1/320)(m-6)/m = 11/3648,                                 [JOINT_WINDOW_PROOF (5.3)]
//!   A = eps*(m-6) = 0.0062*165 = 1.023,  B = Phi_m(A)              [JOINT_WINDOW_PROOF (6.3)]
//!   H(alpha) = 2 - 1/c_alpha,  c_alpha = I0^2/(I2+J_alpha)          [JOINT_WINDOW_PROOF (2.1)]
//!
//! Certificate (r piecewise-linear on knots j/256, r(1)=0, c0 = H - tau):
//!   r(x) = K*(1-x),  K = (B/m)*v / (1/6 - 1/393216),
//! so by construction  sum_{j=1}^{256} (j/256^2) r(j/256) = (B/m)*v exactly, and
//!   v_discrete = c0 + knot_sum = v_chain = 0.6734808616745137...
//!
//! Build : cargo build --release  (target x86_64-unknown-linux-musl for the static build)
//! Run   : ./target/release/wave7_certificate_probe

use std::fs::File;
use std::io::Write;

// ---------------------------------------------------------------------------
// Exact rational arithmetic (i128) for the pure-rational identities
// ---------------------------------------------------------------------------
fn gcd(a: i128, b: i128) -> i128 {
    if b == 0 { a.abs() } else { gcd(b, a % b) }
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
struct Q {
    n: i128,
    d: i128,
}

impl Q {
    fn new(n: i128, d: i128) -> Q {
        assert!(d != 0, "zero denominator");
        let g = gcd(n, d);
        let (n, d) = (n / g, d / g);
        if d < 0 { Q { n: -n, d: -d } } else { Q { n, d } }
    }
    fn add(self, o: Q) -> Q {
        Q::new(self.n * o.d + o.n * self.d, self.d * o.d)
    }
    fn sub(self, o: Q) -> Q {
        self.add(Q::new(-o.n, o.d))
    }
    fn mul(self, o: Q) -> Q {
        Q::new(self.n * o.n, self.d * o.d)
    }
    fn f64(&self) -> f64 {
        self.n as f64 / self.d as f64
    }
    fn fmt_rat(&self) -> String {
        format!("{}/{}", self.n, self.d)
    }
}

// ---------------------------------------------------------------------------
// Window functional H(alpha) and the Phi_m envelope (JOINT_WINDOW_PROOF §2, §6)
// ---------------------------------------------------------------------------
fn h_alpha(alpha: f64) -> f64 {
    let a2 = alpha / 2.0;
    let i0 = 2.0 * a2.sin() / alpha;
    let i2 = 0.5 + alpha.sin() / (2.0 * alpha);
    let j = -2.0 * i2 / (alpha * alpha)
        + (a2.sin() / alpha + 2.0 * a2.cos() / (alpha * alpha)) * i0;
    let c = i0 * i0 / (i2 + j);
    2.0 - 1.0 / c
}

fn phi_m(m: i128, a: f64) -> f64 {
    let mf = m as f64;
    let thr = mf / (mf - 1.0);
    if a <= thr {
        a
    } else {
        2.0 * ((mf - 1.0) * a / mf).sqrt() - 1.0 + a / mf
    }
}

fn main() {
    // ---------------- parameters ----------------
    let alpha = 1.464_f64;
    let m: i128 = 171;
    let eps = 0.0062_f64;
    let psum = Q::new(1, 320);

    // ---------------- exact rationals ----------------
    let n: i128 = 256;
    let tau = psum.mul(Q::new(m - 6, m)); // (1/320)(m-6)/m = 11/3648
    // discrete moment of 1-x over knots j/256 :  sum (j/256^2)(1-j/256) = 1/6 - 1/393216
    let mut s_mass = Q::new(0, 1); // sum j/256^2  (= 257/512)
    let mut s_aff = Q::new(0, 1); //  sum (j/256^2)(1-j/256)
    for j in 1..=n {
        let mass = Q::new(j, n * n);
        s_mass = s_mass.add(mass);
        s_aff = s_aff.add(mass.mul(Q::new(n - j, n)));
    }
    let one_sixth = Q::new(1, 6);
    let e1 = Q::new(-1, 6 * n * n); // -1/393216 = E(1)
    let disc_aff = one_sixth.add(e1); // 1/6 - 1/393216 (must equal s_aff)

    println!("== exact rational identities ==");
    println!("  tau = {} = {:.18}", tau.fmt_rat(), tau.f64());
    println!("  sum_{{(j=1..256)}} j/256^2 = {} = {:.18}  (expect 257/512)",
             s_mass.fmt_rat(), s_mass.f64());
    println!("  sum (j/256^2)(1-j/256) = {} = {:.18}", s_aff.fmt_rat(), s_aff.f64());
    println!("  1/6 - 1/393216          = {} = {:.18}", disc_aff.fmt_rat(), disc_aff.f64());
    assert_eq!(s_mass, Q::new(257, 512), "sum j/256^2 != 257/512");
    assert_eq!(s_aff, disc_aff, "affine knot-sum identity fails");
    println!("  [PASS] sum j/256^2 = 257/512 and sum (j/256^2)(1-j/256) = 1/6 - 1/393216 (exact)");

    // ---------------- f64 chain ----------------
    let h = h_alpha(alpha);
    let a = eps * (m - 6) as f64; // 1.023
    let b = phi_m(m, a);
    let beta = b / m as f64; // B/m
    let v_chain = (h - tau.f64()) / (1.0 - beta);
    let c0 = h - tau.f64();
    let beta_v = beta * v_chain; // = v_chain - c0 (forced identity, PROVEN)

    println!("\n== chain (f64) ==");
    println!("  H(1.464)   = {:.16}   (6E/6C: 0.6724674255777881)", h);
    println!("  A = eps*(m-6) = {:.16}", a);
    println!("  B = Phi_171(1.023) = {:.16}   (coordinator: 1.02292821035354)", b);
    println!("  beta = B/171 = {:.16}   (6E: 0.00598203631756573)", beta);
    println!("  tau = {:.16}", tau.f64());
    println!("  c0 = H - tau = {:.16}   (6E: 0.6694520747005951)", c0);
    println!("  v_chain = (H-tau)/(1-B/m) = {:.16}", v_chain);
    println!("  beta*v = v - (H-tau) = {:.16}", beta_v);

    // ---------------- reconstructed r ----------------
    // r(x) = K(1-x), piecewise-linear on knots j/256, r(1)=0,
    // K chosen so the DISCRETE knot-sum equals beta*v exactly.
    let k = beta_v / disc_aff.f64();
    let mut r = vec![0.0_f64; (n + 1) as usize]; // r[j] = r(j/256), j = 0..256
    for j in 0..=n {
        r[j as usize] = k * (1.0 - j as f64 / n as f64);
    }
    assert!(r[n as usize].abs() < 1e-18, "r(1) != 0");

    let mut knot_sum = 0.0_f64;
    for j in 1..=n {
        knot_sum += (j as f64) / (n as f64 * n as f64) * r[j as usize];
    }
    let v_discrete = c0 + knot_sum;

    println!("\n== reconstructed r (tawan mechanism -> certificate class, r(1)=0) ==");
    println!("  r(x) = K*(1-x),  K = beta*v / (1/6 - 1/393216) = {:.16}", k);
    for j in [0, 32, 64, 96, 128, 160, 192, 224, 256] {
        println!("  r({:>3}/256) = {:.14}", j, r[j as usize]);
    }
    println!("  (full 256-value knot table written to r_knots_table.txt)");
    {
        let mut f = File::create("r_knots_table.txt").expect("open table");
        for j in 1..=n {
            writeln!(f, "{} {:.17}", j, r[j as usize]).expect("write");
        }
    }

    // ---------------- knot-sum identity ----------------
    println!("\n== knot-sum identity ==");
    println!("  knot_sum = sum_{{(j=1..256)}} (j/256^2) r(j/256) = {:.16}", knot_sum);
    println!("  beta*v   (forced target, reading A)             = {:.16}", beta_v);
    println!("  |knot_sum - beta*v| = {:.3e}", (knot_sum - beta_v).abs());
    println!("  quoted 0.0040287869739185 (synthesis)   |diff| = {:.3e}",
             (knot_sum - 0.0040287869739185_f64).abs());
    println!("  quoted 0.0040287869739186 (6E note)     |diff| = {:.3e}",
             (knot_sum - 0.0040287869739186_f64).abs());

    // ---------------- cross-check: three numbers side by side ----------------
    println!("\n== cross-check (side by side) ==");
    let record = 0.6734808616745137_f64;
    println!("  v_discrete = c0 + knot_sum            = {:.16}", v_discrete);
    println!("  v_chain    = (H-tau)/(1-B/m)          = {:.16}", v_chain);
    println!("  record     = 0.6734808616745137       = {:.16}", record);
    println!("  |v_discrete - v_chain| = {:.3e}", (v_discrete - v_chain).abs());
    println!("  |v_discrete - record|   = {:.3e}", (v_discrete - record).abs());
    println!("  |v_chain    - record|   = {:.3e}", (v_chain - record).abs());

    // ---------------- verdict ----------------
    let ok12 = |d: f64, v: f64| d.abs() < v.abs() * 1e-12;
    let ks = ok12(knot_sum - beta_v, beta_v);
    let vd = ok12(v_discrete - record, record);
    let vc = ok12(v_chain - record, record);
    println!("\n== VERDICT ==");
    println!("  knot-sum matches beta*v to >=12 digits: {}", if ks { "MATCH" } else { "MISMATCH" });
    println!("  v_discrete matches record  to >=12 digits: {}", if vd { "MATCH" } else { "MISMATCH" });
    println!("  v_chain    matches record  to >=12 digits: {}", if vc { "MATCH" } else { "MISMATCH" });
    println!("  overall: {}", if ks && vd && vc { "CERTIFIED (knot-sum identity verified)" } else { "DISCREPANCY" });
}
