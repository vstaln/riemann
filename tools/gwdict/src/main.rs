// gwdict: finite Guinand-Weil dictionary -> prime-side recomputation of the
// finitet W_T moments.
//   Stage 1: dictionary validation (worked example, generic, three routes).
//   Stage 2: tr W_T cross-check from the prime side.
//   Stage 3: HS^2 two-level.  Stage 4: archimedean tail.
use std::f64::consts::{PI, SQRT_2};
use gwdict::{C, Dict, ExplicitFormula, arch_tail_power, h_plus, prime_powers, uniform_integrate};

fn load_zeros() -> Vec<f64> {
    let mut gams = Vec::new();
    for line in std::fs::read_to_string("/home/vstaln/riemann/tools/data/zeros_1_1000.txt")
        .expect("zeros file")
        .lines()
    {
        let p: Vec<&str> = line.split_whitespace().collect();
        if p.len() >= 2 {
            gams.push(p[1].parse().unwrap());
        }
    }
    gams
}

// arch integral of an EVEN function f: (1/2pi) int_R f = (1/pi) int_0^inf h_+(r) f(r) dr
//
// Envelope method: f(r) = E0(r) + E1(r) cos(2 pi (r-center)/period + phi) + higher,
// where E0 is smooth.  The half-period average E(r) = f(r) + f(r+period/2) = 2 E0(r)
// kills the oscillation, and (1/2pi) int h_+ f = (1/2pi)(1/2) int h_+ E + O(1/omega^2)
// when the integration range is an integer number of periods (boundary sines vanish).
// The smooth integral is cheap (uniform GL, few panels per unit envelope scale).
pub fn arch_even_env(f: &dyn Fn(f64) -> f64, r1: f64, period: f64, center: f64) -> f64 {
    let e = |r: f64| f(r) + f(r + period / 2.0);
    // (1/pi)(1/2) int_0^inf h_+ E = (1/2pi) int_0^inf h_+ E  (arch for the even function f)
    let near = {
        let g = |r: f64| h_plus(r) * e(r);
        (1.0 / (2.0 * PI)) * uniform_integrate(&g, 0.0, r1, period)
    };
    let tail = 2.0 * arch_tail_power(f, r1, period, center); // (1/2pi) int_{r1}^inf h_+ E
    near + tail
}

fn main() {
    let gams = load_zeros();
    println!("loaded {} zeros (gamma_1000 = {:.2})", gams.len(), gams[999]);
    let int_psi2 = 0.5 + SQRT_2.sin() / (2.0 * SQRT_2);
    println!("int psi^2 = {:.15}", int_psi2);

    // ======================================================================
    // STAGE 1: dictionary validation
    // ======================================================================
    println!("\n================ STAGE 1: dictionary validation ================");
    let c = 13.0_f64;
    let l = c.ln();
    let beta2 = (l / (4.0 * PI)).powi(2);
    let v1 = (2.0 / beta2 + 1.0 / (4.0 + beta2) - 3.0 / (16.0 + beta2))
        / (SQRT_2 * (1.0 / beta2 - 1.0 / (1.0 + beta2)));
    let v0 = 2.0 - SQRT_2 * v1;
    let v = [v0, v1, 1.0 / SQRT_2, 0.0, -3.0 / SQRT_2];
    let dict = Dict::new(c, &v);
    let delta = dict.delta;
    let qq = prime_powers(c);
    let arch_f = |r: f64| dict.gv(C::real(r)).re;
    let arch_val = {
        // direct uniform quadrature: g_v has shortest period 1/Delta and decays ~1/r^2
        let g = |r: f64| dict.gv(C::real(r)).re;
        let near = uniform_integrate(&g, 0.0, 20000.0, 0.05);
        let tail = 2.0 * arch_tail_power(&g, 20000.0, 1.0 / delta, 0.0);
        (1.0 / PI) * near + tail
    };
    let zero_1000 = {
        let mut s = 0.0;
        for i in 0..1000 {
            s += dict.gv(C::real(gams[i])).re;
        }
        2.0 * s
    };
    let ef = ExplicitFormula {
        c,
        qq: qq.clone(),
        f: &|z: C| dict.gv(z),
        fhat: &|xi: f64| dict.ghat(xi),
        arch: &arch_f,
        arch_max: 20000.0,
        arch_h: 0.05,
        arch_period: 1.0 / delta,
        arch_center: 0.0,
    };
    let route_c = ef.evaluate();
    println!("worked example c=13 N=4:  zero side = {:.12}  prime side (Route C) = {:.12}  |B-C| = {:.3e}",
        zero_1000, route_c, (zero_1000 - route_c).abs());
    println!("  paper <v,Q_infty v> = 0.049968414571096979730...  (zero-side partial sums matched paper Table 1)");
    println!("  arch integral = {:.12}", arch_val);

    // ======================================================================
    // STAGE 2: tr W_T cross-check from the prime side
    // ======================================================================
    println!("\n================ STAGE 2: tr W_T from the prime side ================");
    let ts: [f64; 10] = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0];
    println!("T       N    | trW/N(finitet) | Pside_all/N | far/N  | (Pside-far)/N | |recompute-tr|/N");
    for &t in &ts {
        let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
        let nwin = gwin.len();
        if nwin == 0 {
            continue;
        }
        // h_tr(s) = (1/int_psi2) sum_{k=0}^{N-1} psi(s-k)^2  (full k-sum, matches finitet)
        let htr = |s: f64| -> f64 {
            let mut ssum = 0.0;
            for k in 0..nwin {
                ssum += gwdict::psi(C::real(s - k as f64)).abs2();
            }
            ssum / int_psi2
        };
        let htr_c = |z: C| -> f64 {
            let mut ssum = 0.0;
            for k in 0..nwin {
                ssum += gwdict::psi(z.sub(C::real(k as f64))).abs2();
            }
            ssum / int_psi2
        };
        // windowed trace from data (finitet route)
        let mut tr_win = 0.0;
        for &g in &gwin {
            let s = (g - t) * (nwin as f64) / t;
            tr_win += htr(s);
        }
        // far correction: all zeros outside the window (positive + mirrors), data-based
        let mut far = 0.0;
        for &g in &gams {
            if g < t || g >= 2.0 * t {
                let s = (g - t) * (nwin as f64) / t;
                far += htr(s);
            }
            let sm = (-g - t) * (nwin as f64) / t;
            far += htr(sm);
        }
        // prime-side all-zeros sum via the EF for the EVEN function H_tr^e
        let band = (nwin as f64) / t;
        let c_ef = (2.0 * PI * band * 1.001).exp();
        let htr_e = |g: f64| -> f64 {
            0.5 * (htr((g - t) * (nwin as f64) / t) + htr((-g - t) * (nwin as f64) / t))
        };
        // FT of H_tr: Htrhat(xi) = (T/N) e^{-2 pi i T xi} htrhat(T/N xi)
        // htrhat(u) = (1/int_psi2) (psi*psi)(u) sum_{k=0}^{N-1} e^{-2 pi i k u}
        let htrhat = |xi: f64| -> C {
            let u = (nwin as f64) / t * xi;
            let ps = gwdict::psi_star_psi(u);
            let mut gsum = C::real(0.0);
            for k in 0..nwin {
                gsum = gsum.add(C::exp_2pi_i(C::real(-(k as f64) * u)));
            }
            C::exp_2pi_i(C::real(-t * xi)).scale((nwin as f64) / t).mul(gsum.scale(ps / int_psi2))
        };
        let fhat_e = |xi: f64| -> C {
            if xi.abs() > band * 1.001 {
                return C::real(0.0);
            }
            htrhat(xi).add(htrhat(-xi)).scale(0.5)
        };
        let qq_ef = prime_powers(c_ef);
        let mut prime = C::real(0.0);
        for &(q, lam) in &qq_ef {
            let xi = q.ln() / (2.0 * PI);
            prime = prime.sub(fhat_e(xi).scale(lam / q.sqrt()));
        }
        let prime = prime.scale(1.0 / PI);
        // pole term: 2 H_tr^e(i/2) = H_tr(i/2) + H_tr(-i/2), with H_tr(z) = htr((z - T) N/T)
        let htr_s = |s: C| -> f64 {
            let mut ssum = 0.0;
            for k in 0..nwin {
                ssum += gwdict::psi(s.sub(C::real(k as f64))).abs2();
            }
            ssum / int_psi2
        };
        let s_half = C::new(0.0, 0.5).sub(C::real(t)).scale((nwin as f64) / t);
        let s_minus_half = C::new(0.0, -0.5).sub(C::real(t)).scale((nwin as f64) / t);
        let pole = htr_s(s_half) + htr_s(s_minus_half);
        // arch: (1/2pi) int h_+ H_tr^e = (1/pi) int_0^inf h_+(r) H_tr^e(r) dr
        // H_tr period in gamma = T/N; decay center T; use h = T/(2N) (2 periods/panel)
        let arch = arch_even_env(&htr_e, 100.0 * t, t / nwin as f64, t);
        if (t - 100.0).abs() < 1e-9 {
            // direct uniform verification (cheap for T=100): h = 0.25 over [0, 3000]
            let direct = {
                let g = |r: f64| h_plus(r) * htr_e(r);
                let near = uniform_integrate(&g, 0.0, 3000.0, 0.25);
                let tail = 2.0 * gwdict::arch_tail_power(&htr_e, 3000.0, t / nwin as f64, t);
                (1.0 / PI) * near + tail
            };
            println!("  [T=100 arch verify] envelope={:.6}  direct(uniform)= {:.6}  diff={:.2e}", arch, direct, (arch - direct).abs());
            // piecewise: int_0^100, int_100^200, int_200^3000 of h_+ htr_e
            let g = |r: f64| h_plus(r) * htr_e(r);
            let p1 = uniform_integrate(&g, 0.0, 100.0, 0.25);
            let p2 = uniform_integrate(&g, 100.0, 200.0, 0.25);
            let p3 = uniform_integrate(&g, 200.0, 3000.0, 0.25);
            println!("  [T=100 pieces] [0,100]={:.3} [100,200]={:.3} [200,3000]={:.3}  htr_e(150)={:.4} htr_e(160)={:.4} htr_e(140)={:.4}",
                p1, p2, p3, htr_e(150.0), htr_e(160.0), htr_e(140.0));
        }
        let pside_all = prime.re + pole + arch;
        if (t - 100.0).abs() < 1e-9 {
            println!("  [debug T=100] prime={:.6e} pole={:.6e} arch={:.6e} band={:.6} c_ef={:.4}", prime.re, pole, arch, band, c_ef);
            for &rr in &[0.0, 50.0, t, 2.0 * t, 10.0 * t, 100.0 * t] {
                println!("    htr_e({:.1}) = {:.6e}   E = {:.6e}", rr, htr_e(rr), htr_e(rr) + htr_e(rr + (t / nwin as f64) / 2.0));
            }
        }
        let recompute = pside_all - far;
        let agree = (recompute - tr_win).abs();
        println!(
            "{:5.0} {:4} | {:.6} | {:.6} | {:.5} | {:.6} | {:.2e}",
            t, nwin, tr_win / nwin as f64, pside_all / nwin as f64, far / nwin as f64,
            recompute / nwin as f64, agree / nwin as f64
        );
    }
}
