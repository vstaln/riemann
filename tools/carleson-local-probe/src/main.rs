//! Local pole-model stress test for the proposed Carleson bound.
//! This is not a zeta computation. It asks whether a pi*R bound can survive
//! simple on-line zero configurations before any global theorem is attempted.

use std::f64::consts::PI;

fn local_energy(r: f64, ordinates: &[f64], multiplicities: &[f64], n: usize) -> f64 {
    let h_delta = r / n as f64;
    let h_t = r / n as f64;
    let mut sum = 0.0;
    for i in 0..n {
        let delta = (i as f64 + 0.5) * h_delta;
        for j in 0..n {
            let v = (j as f64 + 0.5) * h_t - r / 2.0;
            let mut re = 0.0;
            let mut im = 0.0;
            for (gamma, mult) in ordinates.iter().zip(multiplicities) {
                // on-line pole: rho = 1/2 + i gamma; s-rho = delta+i(t-gamma)
                let dv = v - gamma;
                let den = delta * delta + dv * dv;
                re += mult * delta / den;
                im -= mult * dv / den;
            }
            sum += delta * (re * re + im * im) * h_delta * h_t;
        }
    }
    sum
}

fn main() {
    let n = 900usize;
    let r = 1.0;
    let configs = [
        ("one on-line zero", vec![0.0]),
        ("two separated on-line zeros", vec![-0.25, 0.25]),
        ("two close on-line zeros", vec![-0.01, 0.01]),
        ("double on-line zero", vec![0.0]),
    ];
    for (name, ordinates) in configs {
        let mult = if name == "double on-line zero" { vec![2.0] } else { vec![1.0; ordinates.len()] };
        let e = local_energy(r, &ordinates, &mult, n);
        println!("{}: energy/R={:.12e}, ratio_to_pi={:.12e}", name, e / r, e / (PI * r));
    }
}
