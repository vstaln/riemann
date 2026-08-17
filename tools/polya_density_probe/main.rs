// Pony tail probe: log-concavity of the Riemann theta density Phi(u).
// Phi(u) = 2 e^{u/2} (2x^2 theta''(x) + 3x theta'(x)), x = e^{2u}  [campaign-PROVEN theta identity]
// L(u) = Phi*Phi'' - Phi'^2 ; log-concave <==> L <= 0 on meaningful support (Phi > 1e-6).
// Exact chain-rule derivatives of the theta series. f64, no deps, <1s.
use std::f64::consts::PI;

fn theta_series(x: f64) -> [f64; 5] {
    // [theta, theta', theta'', theta''', theta''''] summed to tail < 1e-17
    let mut th = [0f64; 5];
    let mut n = 1f64;
    loop {
        let a = PI * n * n * x;
        if a > 40.0 {
            break;
        }
        let e = (-a).exp();
        if e < 1e-300 {
            n += 1.0;
            continue;
        }
        let q = PI * n * n;
        let q2 = q * q;
        let q3 = q2 * q;
        let q4 = q3 * q;
        th[0] += e;
        th[1] -= q * e;
        th[2] += q2 * e;
        th[3] -= q3 * e;
        th[4] += q4 * e;
        n += 1.0;
    }
    th
}

fn phi_derivs(u: f64) -> [f64; 3] {
    let x = (2.0 * u).exp();
    let th = theta_series(x);
    let t0 = th[0];
    let t1 = th[1];
    let t2 = th[2];
    let t3 = th[3];
    let t4 = th[4];
    // A = 2x^2 t2 + 3x t1
    let a = 2.0 * x * x * t2 + 3.0 * x * t1;
    // A' = 2x(7x t2 + 2x^2 t3 + 3 t1)
    let ap = 2.0 * x * (7.0 * x * t2 + 2.0 * x * x * t3 + 3.0 * t1);
    // A'' = 2x(34x t2 + 26x^2 t3 + 4x^3 t4 + 6 t1)
    let app = 2.0 * x * (34.0 * x * t2 + 26.0 * x * x * t3 + 4.0 * x * x * x * t4 + 6.0 * t1);
    let e = (0.5 * u).exp();
    // identity: Phi(u) = 2 e^{u/2} A  (factor 2 from the campaign theta identity)
    let phi = 2.0 * e * a;
    let php = 2.0 * e * (a + 2.0 * ap);
    let phpp = 2.0 * e * (0.5 * a + 2.0 * ap + 2.0 * app);
    [phi, php, phpp]
}

fn main() {
    // sanity: Phi(0) should be ~0.8933938
    let p0 = phi_derivs(0.0);
    println!("Phi(0) = {:.12}  (known 0.8933938...)", p0[0]);

    let u_min = -2.0f64;
    let u_max = 1.5f64;
    let n = 401usize;
    let mut max_l = f64::NEG_INFINITY;
    let mut min_l = f64::INFINITY;
    let mut u_maxl = 0.0f64;
    let mut pos_count = 0usize;
    let mut pos_first = (0.0f64, 0.0f64); // (u, L)
    let mut any_pos = false;
    let mut prev_u = 0.0f64;
    let mut prev_l = 0.0f64;
    let mut prev_valid = false;

    println!("u\tPhi\tL(u)=Phi*Phi''-Phi'^2");
    for i in 0..=n {
        let u = u_min + (u_max - u_min) * i as f64 / n as f64;
        let pd = phi_derivs(u);
        let phi = pd[0];
        let l = phi * pd[2] - pd[1] * pd[1];
        if phi > 1e-6 {
            if l > max_l {
                max_l = l;
                u_maxl = u;
            }
            if l < min_l {
                min_l = l;
            }
            if l > 0.0 {
                pos_count += 1;
                if !any_pos {
                    any_pos = true;
                    pos_first = (u, l);
                    println!("FIRST LOG-CONVEX POINT u={:.4} L={:.3e}", u, l);
                }
            }
            // sign change detection on meaningful support
            if prev_valid && (l > 0.0) != (prev_l > 0.0) {
                println!("SIGN CHANGE on [u={:.4} (L={:.3e}), u={:.4} (L={:.3e})]", prev_u, prev_l, u, l);
            }
            prev_u = u;
            prev_l = l;
            prev_valid = true;
        } else {
            prev_valid = false;
        }
        if (i % 40) == 0 {
            println!("{:.4}\t{:.6e}\t{:.3e}", u, phi, l);
        }
    }
    println!("---");
    println!("min L on meaningful support: {:.6e} at Phi>1e-6", min_l);
    println!("max L: {:.6e} at u={:.4}", max_l, u_maxl);
    println!("L > 0 count: {} of {} grid points (meaningful region)", pos_count, n + 1);
    if any_pos {
        println!("VERDICT: Phi NOT log-concave (first violation u={:.4}, L={:.3e})", pos_first.0, pos_first.1);
    } else {
        println!("VERDICT: Phi log-concave on sampled meaningful region (L<=0 everywhere)");
    }
}