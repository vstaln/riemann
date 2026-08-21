// wave-rh4(A): Speiser / Davenport-Heilbronn RH-false control probe (Lane D, ranking.md).
// Honesty: winding numbers are CHECKED NUMERICALLY (f64); Speiser-transfer-for-DH stays CONJECTURED.
use std::f64::consts::PI;

const NMAX: u64 = 2000;
const SIG_LO: f64 = 0.05;
const SIG_HI: f64 = 0.50;
const T_LO: f64 = 10.0;
const T_HI: f64 = 120.0;
const H: f64 = 0.15;
const CIRCLE_PTS: usize = 64;
const ABS_CAP: u64 = 1_000_000; // cap for the literal |r| log n n^-0.05 tail sum (it diverges)

fn c_coef() -> f64 {
    // Source: research/waves/wave-rh4/ranking.md Lane D spec.
    let s5 = 5.0f64.sqrt();
    ((10.0 - 2.0 * s5).sqrt() - 2.0) / (s5 - 1.0)
}

#[inline]
fn r(n: u64, c: f64) -> f64 {
    match n % 5 {
        1 => 1.0,
        2 => c,
        3 => -c,
        4 => -1.0,
        _ => 0.0,
    }
}

// f'(s) = -sum_{n=2}^{NMAX} r(n) ln(n) n^{-s}; returns (re, im)
fn fp(sigma: f64, t: f64, c: f64) -> (f64, f64) {
    let (mut re, mut im) = (0.0f64, 0.0f64);
    for n in 2..=NMAX {
        let rn = r(n, c);
        if rn == 0.0 {
            continue;
        }
        let ln = (n as f64).ln();
        let a = (-sigma * ln).exp();
        let th = t * ln;
        let m = -rn * ln * a;
        re += m * th.cos();
        im -= m * th.sin();
    }
    (re, im)
}

// CONTROL: truncated zeta'-analog without r weights (as specified by the task).
fn zp(sigma: f64, t: f64) -> (f64, f64) {
    let (mut re, mut im) = (0.0f64, 0.0f64);
    for n in 2..=NMAX {
        let ln = (n as f64).ln();
        let a = (-sigma * ln).exp();
        let th = t * ln;
        let m = -ln * a;
        re += m * th.cos();
        im -= m * th.sin();
    }
    (re, im)
}

fn winding(center: (f64, f64), h: f64, use_zeta: bool, c: f64) -> i32 {
    let mut prev: Option<f64> = None;
    let mut total = 0.0f64;
    for k in 0..=CIRCLE_PTS {
        let ang = 2.0 * PI * (k as f64) / (CIRCLE_PTS as f64);
        let (s, t) = (center.0 + h * ang.cos(), center.1 + h * ang.sin());
        let v = if use_zeta { zp(s, t) } else { fp(s, t, c) };
        let a = v.1.atan2(v.0);
        if let Some(p) = prev {
            let mut d = a - p;
            while d > PI {
                d -= 2.0 * PI;
            }
            while d < -PI {
                d += 2.0 * PI;
            }
            total += d;
        }
        prev = Some(a);
    }
    (total / (2.0 * PI)).round() as i32
}

fn main() {
    let c = c_coef();
    println!("speiser_dh_control Nmax={} c={:.12}", NMAX, c);

    // STEP 1+2: scan rectangle for |f'| minimum
    let (mut best, mut bs, mut bt) = (f64::INFINITY, SIG_LO, T_LO);
    let mut sig = SIG_LO;
    while sig <= SIG_HI + 1e-9 {
        let mut t = T_LO;
        while t <= T_HI + 1e-9 {
            let v = fp(sig, t, c);
            let m = (v.0 * v.0 + v.1 * v.1).sqrt();
            if m < best {
                best = m;
                bs = sig;
                bt = t;
            }
            t += 0.05;
        }
        sig += 0.01;
    }
    println!("dh_fprime_min sigma={:.4} t={:.2} val={:.6e}", bs, bt, best);

    // Remainder bounds (honest accounting):
    // (a) literal task bound sum_{n>Nmax} |r(n)| ln n n^{-0.05} — this series DIVERGES
    //     (exponent 0.05 < 1); printed with cap ABS_CAP to show magnitude only.
    let mut abs_cap = 0.0f64;
    for n in (NMAX + 1)..=ABS_CAP {
        abs_cap += r(n, c).abs() * (n as f64).ln() * (n as f64).powf(-0.05);
    }
    println!("rem_abs_literal cap=1e6 val={:.6e} NOTE=diverges_as_n->inf", abs_cap);
    // (b) certified Dirichlet-test bound: partial sums of r bounded by B=1+c,
    //     Abel summation gives |R_N| <= 2B ln(N+1)/N^sigma for the f' series.
    let b_part = 1.0 + c;
    let rem_dir = 2.0 * b_part * ((NMAX + 1) as f64).ln() / (NMAX as f64).powf(bs);
    let vc = fp(bs, bt, c);
    let val_c = (vc.0 * vc.0 + vc.1 * vc.1).sqrt();
    println!(
        "dh_rembound dirichlet={:.6e} at sigma={:.4}; |f'|_center={:.6e} ratio={:.3}",
        rem_dir, bs, val_c, rem_dir / val_c.max(1e-300)
    );

    // STEP 3: winding of f' on circle radius H around the minimum
    let wind_dh = winding((bs, bt), H, false, c);
    println!("dh_winding circle_center=({:.4},{:.2}) h={} pts={} wind={}", bs, bt, H, CIRCLE_PTS, wind_dh);

    // CONTROL: same circle, truncated zeta' analog; wave-8B certified real strip empty => must be 0
    let wind_zeta = winding((bs, bt), H, true, c);
    println!("zeta_control_winding center=({:.4},{:.2}) h={} wind={}", bs, bt, H, wind_zeta);

    // PASS/FAIL per task spec
    let ok_wind = wind_dh == 1;
    let ok_ctrl = wind_zeta == 0;
    let ok_rem = rem_dir < 0.1 * val_c;
    if ok_wind && ok_ctrl && ok_rem {
        println!("VERDICT: PASS (dh wind=1, zeta control wind=0, remainder<10%|f'|)");
    } else {
        println!(
            "VERDICT: FAIL dh_wind_ok={} zeta_ctrl_ok={} remainder_ok={} (discriminator {})",
            ok_wind,
            ok_ctrl,
            ok_rem,
            if !ok_ctrl { "BROKEN" } else { "uncertified/absent" }
        );
    }
}
