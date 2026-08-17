// direct-rh-lse-salvage probe: total LSE energy L(delta) = int Phi(t;delta)^2 dt
// Phi(t;delta) = Im[ xi'/xi(1/2+delta+it) - xi'/xi(1/2-delta+it) ]
// via the partial-fraction resolvent of a FINITE canonical model (no zeta machinery,
// no zero search): R(s) = sum over the full FE-symmetric zero set of 1/(s-rho).
// Purpose: convert derived claims about on/off-line hump energies into CHECKED NUMERICALLY:
//   (a) under an all-on-line world, L(delta) -> 0 like delta*C (C ~ sum 1/gamma^2);
//   (b) any single planted off-line zero at depth eps>0 makes L(delta) flat-positive O(1)
//       for all delta < eps  =>  "lim_{delta->0} L(delta) = 0" is equivalent to RH on toys
//       (the equivalence collapse), and a FIXED-delta threshold is a depth-detector;
//   (c) DH-certified depths ({0.31,0.15} off-line) fire the fixed-delta discriminator.
// f64 only. Runs < 5 s. Labels in output; conclusions in the note.

struct World { zeros: Vec<(f64, f64)> } // (beta, gamma), full symmetric closure NOT applied here

// build the full FE + conjugation-symmetric zero set from generators
fn symmetric_closure(gen: &[(f64, f64)]) -> Vec<(f64, f64)> {
    let mut out: Vec<(f64, f64)> = Vec::new();
    for &(b, g) in gen {
        for (bb, gg) in [(b, g), (1.0 - b, g), (b, -g), (1.0 - b, -g)] {
            if !out.contains(&(bb, gg)) {
                out.push((bb, gg));
            }
        }
    }
    out
}

// R(s) = sum_zeros 1/(s - rho), s = (sig, t)
fn resolvent(sig: f64, t: f64, zeros: &[(f64, f64)]) -> (f64, f64) {
    let (mut re, mut im) = (0.0f64, 0.0f64);
    for &(b, g) in zeros {
        let dr = sig - b;
        let di = t - g;
        let d2 = dr * dr + di * di;
        re += dr / d2;
        im -= di / d2; // 1/(a+ib) = (a-ib)/|.|^2, a=dr, b=di
    }
    (re, im)
}

fn phi(t: f64, delta: f64, zeros: &[(f64, f64)]) -> f64 {
    let (_, im_up) = resolvent(0.5 + delta, t, zeros);
    let (_, im_dn) = resolvent(0.5 - delta, t, zeros);
    im_up - im_dn
}

// trapezoid with step delta/4 over [-T,T]; step small enough to resolve width-delta humps
fn lse(delta: f64, zeros: &[(f64, f64)], t_max: f64) -> f64 {
    let step = delta / 4.0;
    let n = ((2.0 * t_max) / step).ceil() as usize;
    let mut acc = 0.0;
    for i in 0..=n {
        let t = -t_max + step * i as f64;
        let f = phi(t, delta, zeros);
        let w = if i == 0 || i == n { 0.5 } else { 1.0 };
        acc += w * f * f;
    }
    acc * step
}

fn main() {
    let on: Vec<(f64, f64)> = vec![
        (0.5, 14.1347), (0.5, 21.0220), (0.5, 25.0109), (0.5, 30.4249), (0.5, 32.9351),
        (0.5, 37.5862), (0.5, 40.9187), (0.5, 43.3271), (0.5, 48.0052), (0.5, 49.7738),
    ];
    let wA = World { zeros: symmetric_closure(&on) };
    let mut genB: Vec<(f64, f64)> = on.clone();
    genB.push((0.7, 20.0)); // planted off-line depth 0.2, ordinate 20
    let wB = World { zeros: symmetric_closure(&genB) };
    let mut genC: Vec<(f64, f64)> = on.clone();
    genC.push((0.65, 25.0)); // depth 0.15
    let wC = World { zeros: symmetric_closure(&genC) };
    let mut genD: Vec<(f64, f64)> = on.clone();
    genD.push((0.8085171824566374, 85.69934848537759)); // certified DH zero (beta-1/2=0.3085)
    genD.push((0.6508300806097371, 114.16334273075698)); // certified DH zero (beta-1/2=0.1508)
    let wD = World { zeros: symmetric_closure(&genD) };

    // grid-convergence sanity on one case (world B, delta=0.05)
    let tmax: f64 = 120.0;
    let l1 = lse(0.05, &wB.zeros, tmax);
    let mut fine = 0.0;
    let step = 0.05 / 8.0;
    let n = ((2.0 * tmax) / step).ceil() as usize;
    for i in 0..=n {
        let t = -tmax + step * i as f64;
        let f = phi(t, 0.05, &wB.zeros);
        let w = if i == 0 || i == n { 0.5 } else { 1.0 };
        fine += w * f * f;
    }
    fine *= step;
    println!("grid check: L_B(0.05) step/4={:.6e} step/8={:.6e} rel={:.2e}",
             l1, fine, (l1 - fine).abs() / (l1.abs() + 1e-300));

    // sum 1/gamma^2 over on-line set (the C constant for world A)
    let c_a: f64 = on.iter().map(|&(_, g)| 1.0 / (g * g)).sum();
    println!("world A C=sum 1/gamma^2 = {:.6e}", c_a);

    println!("\n delta      L_A        L_B/1e?    L_C        L_D        L_B/L_A   L_C/L_A   L_A/delta");
    for &d in &[0.02f64, 0.05, 0.1, 0.2, 0.3] {
        let la = lse(d, &wA.zeros, tmax);
        let lb = lse(d, &wB.zeros, tmax);
        let lc = lse(d, &wC.zeros, tmax);
        let ld = lse(d, &wD.zeros, tmax);
        println!("{:.2}  {:.6e}  {:.6e}  {:.6e}  {:.6e}  {:.3e}  {:.3e}  {:.6e}",
                 d, la, lb, lc, ld, lb / (la + 1e-300), lc / (la + 1e-300), la / d);
    }

    // Lemma-3 peak: Phi at t=gamma for an on-line zero vs off-line planted (same ordinate)
    let pa = phi(20.0, 0.1, &wA.zeros);
    let pb = phi(20.0, 0.1, &wB.zeros);
    println!("\npeak check (t=20, delta=0.1): on-line-only world Phi={:.6e}, planted world Phi={:.6e}, |ratio|={:.3e}", pa, pb, pb.abs() / (pa.abs() + 1e-300));

    // KEY: lim_{delta->0} L(delta): plant-free vs planted
    let la00 = lse(0.004, &wA.zeros, tmax);
    let lb00 = lse(0.004, &wB.zeros, tmax);
    println!("\nKEY small-delta: L_A(0.004)={:.6e} (->0), L_B(0.004)={:.6e} (flat-positive), ratio={:.3e}",
             la00, lb00, lb00 / (la00 + 1e-300));

    // self-check: A is delta-symmetric in t (t -> -t maps to conjugate zeros, Phi odd in t -> L same)
    let lneg = lse(0.1, &{ let mut z = wA.zeros.clone(); z }, tmax);
    let lpos = lse(0.1, &wA.zeros, tmax);
    println!("self-check L_A(0.1) recomputed = {:.6e} vs {:.6e} (must match)", lneg, lpos);
    if (la00 / (lb00 + 1e-300)) > 1.0 { println!("SELF-CHECK FAIL: plant-free L not smaller than planted"); std::process::exit(1); }
    println!("exit 0");
}