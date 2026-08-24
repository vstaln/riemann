//! cert-floor-rs — port of the certification-floor chain drivers.
//!
//! Original Python: tools/cert_floor_driver.py (record chain),
//! tools/cert_param_sweep.py (coefficient families F1..F4, master chain).
//!
//! What this computes:
//!   record chain (tawanerguo):  bound = (H(alpha) - tau)/(1 - B/m)
//!     tau = psum*(m-6)/m          (pressure sum psum = sum p_i = 1/320)
//!     A   = eps*(m-6)             (local certified floor eps x windows)
//!     B   = Phi_m(A, m)           (trace-energy envelope)
//!   master chain (param_sweep):  bound = (m*H - eta*Bp*(m-1))/(m - R)
//!     A = eps*(m-q), R = h(A) or Phi_m(A,m), eta = R/A, Bp = q*p.
//!
//! Honesty labels (program guardrails):
//!   CERTIFIED   = the eps (local floor) input was verified by the interval
//!                 verifier (tools/verify_coboundary_floor.py, sanctioned).
//!                 We do NOT re-verify here.
//!   FLOAT-PROBE = double-precision (f64) arithmetic of the chain only.
//!                 H(alpha) constant is truncated to 12 decimals, chain is
//!                 plain f64 — NOT interval arithmetic.

/// H(alpha) in f64 — port of cert_floor_driver.H_cos (float, matches mpmath ~1e-15).
fn h_cos(alpha: f64) -> f64 {
    let a = alpha;
    let i0 = 2.0 * (a / 2.0).sin() / a;
    let i2 = 0.5 + a.sin() / (2.0 * a);
    let c_const = (a / 2.0).sin() / a + 2.0 * (a / 2.0).cos() / (a * a);
    let jv = -2.0 * i2 / (a * a) + c_const * i0;
    let c = i0 * i0 / (i2 + jv);
    2.0 - 1.0 / c
}

/// tawanerguo trace-energy envelope Phi_m(A) — port of cert_floor_driver.phi_m.
fn phi_m(a: f64, m: f64) -> f64 {
    if a <= m / (m - 1.0) {
        a
    } else {
        2.0 * ((m - 1.0) * a / m).sqrt() - 1.0 + a / m
    }
}

/// Sharp profile h(E) = E (E<=1), 2*sqrt(E)-1 (E>=1) — port of cert_param_sweep.h_profile.
fn h_profile(e: f64) -> f64 {
    if e <= 1.0 {
        e
    } else {
        2.0 * e.sqrt() - 1.0
    }
}

/// Record chain: bound = (H - tau)/(1 - B/m), tau = psum*(m-6)/m, B = Phi_m(eps*(m-6)).
fn joint_bound(h: f64, eps: f64, m: f64, psum: f64) -> f64 {
    let a = eps * (m - 6.0);
    let b = phi_m(a, m);
    let tau = psum * (m - 6.0) / m;
    (h - tau) / (1.0 - b / m)
}

/// Record chain with sqrt-tail cap: bound = (H - tau)/(1 - B/m), mirroring joint_bound
/// (which hard-codes q=6 and the cap phi_m) but with B = h_profile(eps*(m-q)),
/// i.e. h(E) = E for E<=1 else 2*sqrt(E)-1.
fn record_chain_sqrt_tail(h: f64, eps: f64, p: f64, m: f64, q: f64) -> f64 {
    let a = eps * (m - q);
    let b = h_profile(a);
    let tau = p * (m - q) / m;
    (h - tau) / (1.0 - b / m)
}

/// Master chain — port of cert_param_sweep.block_bound_master. cap: "h" | "phi".
fn block_bound_master(h: f64, eps: f64, p: f64, m: f64, q: f64, cap: &str) -> f64 {
    let a = eps * (m - q);
    let r = if cap == "h" { h_profile(a) } else { phi_m(a, m) };
    let eta = r / a;
    let bp = q * p;
    (m * h - eta * bp * (m - 1.0)) / (m - r)
}

const TARGET: f64 = 0.6734808616745137;

fn main() {
    // subcommand: `cargo run -- chains <h> <eps> <psum>` — print record (phi_m cap) and
    // record_sqrt_tail (h_profile cap) chains side by side over m in [40, 400].
    let args: Vec<String> = std::env::args().collect();
    if args.len() >= 5 && args[1] == "chains" {
        let h: f64 = args[2].parse().unwrap();
        let eps: f64 = args[3].parse().unwrap();
        let psum: f64 = args[4].parse().unwrap();
        println!("=== CHAINS side by side (m in [40,400]) h={h} eps={eps} psum={psum} ===");
        println!("    m   |  record (phi_m cap)  |  record_sqrt_tail (h_profile cap) ");
        let mut m: f64 = 40.0;
        while m <= 400.0 + 1e-9 {
            let q = 6.0_f64;
            let rec = joint_bound(h, eps, m, psum);
            let rec_t = record_chain_sqrt_tail(h, eps, psum, m, q);
            println!(" {m:>5.0} |  {rec:.12}  |  {rec_t:.12}");
            m += 1.0;
        }
        return;
    }
    println!("cert-floor-rs — certification-floor chain (port of cert_floor_driver.py / cert_param_sweep.py)");
    println!("Honesty: [C] = CERTIFIED input eps (interval-verified elsewhere), chain arithmetic = f64 FLOAT-PROBE (not interval).\n");

    // ------------------------------------------------------------------
    // 0. constants
    // ------------------------------------------------------------------
    let h0: f64 = 1.5 - 1.0 / (std::f64::consts::SQRT_2 * (1.0 / std::f64::consts::SQRT_2).tan()); // ainta H0

    // ------------------------------------------------------------------
    // 1. RECORD reproduction: eps=0.0062, m=171, H(1.464)=0.672467425578
    // ------------------------------------------------------------------
    let h_record = 0.672467425578_f64; // stated constant (12 digits, truncated)
    let eps_record = 0.0062_f64;
    let m_record = 171.0_f64;
    let psum_record = 1.0 / 320.0;
    let bound = joint_bound(h_record, eps_record, m_record, psum_record);
    let diff = bound - TARGET;
    println!("=== RECORD CHAIN (tawanerguo) ===");
    println!("  H(1.464) = {:.15}   [C input: window value; truncated to 12 digits]", h_record);
    println!("  eps = {eps_record}, psum = 1/320 [C: local floor eps], m = {m_record}");
    println!("  bound     = {bound:.16}");
    println!("  target    = {TARGET:.16}  (record bound)");
    println!("  |diff|    = {:.3e}   (pass <= 1e-12: {})", diff.abs(), diff.abs() <= 1e-12);
    let h_float = h_cos(1.464);
    println!("  H_cos(1.464) in f64 = {h_float:.15}  (bound with this H: {:.16})", joint_bound(h_float, eps_record, m_record, psum_record));
    // driver's tawan committed anchor, m=183 tax=59/19520 at alpha=1.47, local 577/1e5
    let h147 = h_cos(1.47);
    let a183 = (577.0 / 1e5) * 177.0;
    let b183 = (h147 - 59.0 / 19520.0) / (1.0 - phi_m(a183, 183.0) / 183.0);
    println!("  [cross-check] tawanerguo F4 alpha=1.47, local=577/1e5 [C], m=183, tax=59/19520: {b183:.15}");
    println!("    (repo committed 0.6731929114731423; f64 chain arithmetic)");
    println!();

    // ------------------------------------------------------------------
    // 2. EPS-SWEEP: eps x m table around the optimum; m=171 should be argmax
    // ------------------------------------------------------------------
    println!("=== EPS-SWEEP (H = 0.672467425578 [C H], psum = 1/320 [C]) ===");
    // coarse: argmax m over 60..600 per eps, then fine table around optimum
    let eps_vals: Vec<f64> = (0..=12).map(|k| 0.0056 + k as f64 * 0.0001).collect();
    println!("  argmax m per eps (float chain):");
    for &e in &eps_vals {
        let mut best = (0.0_f64, 0.0_f64);
        let mut mm = 60.0;
        while mm <= 600.0 {
            let b = joint_bound(h_record, e, mm, psum_record);
            if b > best.0 {
                best = (b, mm);
            }
            mm += 1.0;
        }
        println!("    eps={e:.4}  m*={:>3.0}  bound={:.15}", best.1, best.0);
    }
    println!();
    println!("  fine table around the optimum (eps x m, rows = eps, cols = m):");
    let fine_m: Vec<f64> = (167..=176).map(|x| x as f64).collect();
    print!("       eps\\m ");
    for &m in &fine_m {
        print!("{m:>12.0}");
    }
    println!();
    for &e in &eps_vals {
        // rows: every 2nd eps for readability
        if (e * 10000.0).round() as i64 % 2 != 0 {
            continue;
        }
        print!("{e:.4}  ");
        for &m in &fine_m {
            let b = joint_bound(h_record, e, m, psum_record);
            let mark = if (e - eps_record).abs() < 1e-12 && (m - m_record).abs() < 1e-12 { "*" } else { " " };
            print!("{b:12.9}{mark}");
        }
        println!();
    }
    // explicit argmax check at eps=0.0062
    let mut best = (0.0_f64, 0.0_f64);
    let mut mm = 60.0;
    while mm <= 600.0 {
        let b = joint_bound(h_record, eps_record, mm, psum_record);
        if b > best.0 {
            best = (b, mm);
        }
        mm += 1.0;
    }
    println!("  argmax at eps=0.0062: m = {:.0}, bound = {:.15}  (expect m=171)", best.1, best.0);
    // argmax at eps=0.0063, 0.0061 for context
    for &e in &[0.0061, 0.0063] {
        let mut b2 = (0.0_f64, 0.0_f64);
        let mut m2 = 60.0;
        while m2 <= 600.0 {
            let v = joint_bound(h_record, e, m2, psum_record);
            if v > b2.0 {
                b2 = (v, m2);
            }
            m2 += 1.0;
        }
        println!("  argmax at eps={e:.4}: m = {:.0}, bound = {:.15}", b2.1, b2.0);
    }
    println!();

    // ------------------------------------------------------------------
    // 3. PARAM-SWEEP: psum (pressure sum) x m at fixed certified eps, H;
    //    then coefficient families F1..F4 with their exact certified eps.
    // ------------------------------------------------------------------
    println!("=== PARAM-SWEEP (a): pressure sum psum x m, eps=0.0062 [C], H=0.672467425578 [C] ===");
    let psums = [1.0 / 640.0, 1.0 / 480.0, 1.0 / 320.0, 1.0 / 240.0, 1.0 / 160.0];
    for &ps in &psums {
        let mut best = (0.0_f64, 0.0_f64);
        let mut m2 = 60.0;
        while m2 <= 600.0 {
            let v = joint_bound(h_record, eps_record, m2, ps);
            if v > best.0 {
                best = (v, m2);
            }
            m2 += 1.0;
        }
        println!("  psum={:.6} = 1/{:<4}  best m = {:.0}, bound = {:.15}", ps, (1.0 / ps).round(), best.1, best.0);
    }
    println!("  (bound rises as psum drops: pressure charge lowers the bound)");
    println!();

    println!("=== PARAM-SWEEP (b): coefficient-family table (external formula families, exact repo constants) ===");
    // F1 ainta 3-point: (H0 - eps/4)/(1 - eps/2), eps certified 221/1e6
    let f1 = |e: f64| -> f64 { (h0 - e / 4.0) / (1.0 - e / 2.0) };
    let b1 = f1(221.0 / 1e6);
    // F2 ainta 7-point: master chain m=269, p=1/3000, q=6, cap h, eps certified 19/5000
    let b2 = block_bound_master(h0, 19.0 / 5000.0, 1.0 / 3000.0, 269.0, 6.0, "h");
    // F3 trmdy: H=672457/1e6, eps 1/200 [C], p=1/2300, m=257, q=6, cap h
    let b3 = block_bound_master(672457.0 / 1e6, 1.0 / 200.0, 1.0 / 2300.0, 257.0, 6.0, "h");
    // F4 tawanerguo: alpha=1.47, H = H_cos, local eps 577/1e5 [C], m=183, tax 59/19520
    let b4 = (h147 - 59.0 / 19520.0) / (1.0 - phi_m(a183, 183.0) / 183.0);
    // F4 via master chain: the python's p-equivalence (p = tax*m/(q*(m-1)))
    // drops the eta = R/A factor, so the match is NOT exact (~1.8e-7 here).
    // Using p4_eta = p4/eta reproduces the joint form to roundoff.
    let p4 = (59.0 / 19520.0) * 183.0 / (6.0 * 182.0);
    let b4m = block_bound_master(h147, 577.0 / 1e5, p4, 183.0, 6.0, "phi");
    let a183_ = (577.0 / 1e5) * 177.0;
    let r183 = phi_m(a183_, 183.0);
    let eta183 = r183 / a183_;
    let b4m_eta = block_bound_master(h147, 577.0 / 1e5, p4 / eta183, 183.0, 6.0, "phi");
    println!("  H0 (ainta) = {h0:.15}");
    println!("  F1 ainta 3pt     : bound = {b1:.15}   [C eps 221/1e6]");
    println!("  F2 ainta 7pt     : bound = {b2:.15}   [C eps 19/5000, m=269, p=1/3000, q=6]");
    println!("  F3 trmdy         : bound = {b3:.15}   [C eps 1/200, H=672457/1e6, p=1/2300, m=257]");
    println!("  F4 tawanerguo    : bound = {b4:.15}   [C local 577/1e5, alpha=1.47, m=183, tax 59/19520]");
    println!("  F4 via master    : bound = {b4m:.15}  (python-equivalence, drops eta -> mismatch {:.1e})", (b4m - b4).abs());
    println!("  F4 via master    : bound = {b4m_eta:.15}  (with eta = R/A in p -> match to roundoff, diff {:.1e})", (b4m_eta - b4).abs());
    // param sweep over p for the F3/F4 chains: sensitivity to the pressure
    // coefficient p at fixed (certified) eps. F4's pressure enters only via
    // the product q*p = tax*m/(m-1) (certified design fixes it); here we hold
    // eps fixed and vary p to show the chain's pressure sensitivity.
    println!();
    println!("  (c) sensitivity: trmdy/tawanerguo chain vs pressure p at fixed eps:");
    let tax4 = 59.0 / 19520.0;
    let p4_nom = tax4 * 183.0 / (6.0 * 182.0); // p such that q*p*(m-1)/m = tax
    for &p in &[1.0 / 4600.0, 1.0 / 2300.0, 1.0 / 1150.0] {
        let v3 = block_bound_master(672457.0 / 1e6, 1.0 / 200.0, p, 257.0, 6.0, "h");
        // F4: same certified chain shape, p scaled about its nominal value
        let v4 = block_bound_master(h147, 577.0 / 1e5, p4_nom * (p / (1.0 / 2300.0)), 183.0, 6.0, "phi");
        println!("    p={:.6}: F3 trmdy = {v3:.15}   F4 tawan = {v4:.15}", p);
    }
    println!("    (nominal F4 p_q=6 = {p4_nom:.8}; bound decreases as pressure charge p rises)");
    println!();

    println!("=== VERDICT ===");
    println!("  record bound reproduced to {:.3e} (tolerance 1e-12): {}", diff.abs(), if diff.abs() <= 1e-12 { "PASS" } else { "FAIL" });
    println!("  all chain arithmetic = f64 FLOAT-PROBE; certified inputs are the eps values (interval-verified by the sanctioned verifier) and H constants.");
}