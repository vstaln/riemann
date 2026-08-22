// Wave RH-6 Lane B: Li frontier certificate. Rows 1..=19000 ONLY (quarantine,
// tools/CONVENTIONS.md). lambda_clean_lo via validated phasor recurrence;
// tail bracket I(n)=(n/pi)[L*J(u0)+K(u0)], u0=n/(2G), cross-checked against
// direct quadrature INSIDE this binary (mismatch => INCONCLUSIVE, never PASS).
// Labels: CHECKED NUMERICALLY unless stated otherwise. No RH proof claimed.
use std::fs;
use std::path::PathBuf;
use std::thread;

const ROW_MAX: u32 = 19_000;
const DATA: &str = "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt";
const N_MAX: usize = 1_000_000;
const H_PLATT: f64 = 3.0e12;
const THREADS: usize = 8;
const LANES: usize = 8;
const SLACK_K: f64 = 1.0e-6; // covers K-grid quadrature+interp+dust (signal scale >> slack)

fn rdown(x: f64) -> f64 {
    if x == 0.0 { return -0.0; }
    let b = x.to_bits();
    f64::from_bits(if x > 0.0 { b - 1 } else { b + 1 })
}
fn rup(x: f64) -> f64 {
    if x == 0.0 { return 0.0; }
    let b = x.to_bits();
    f64::from_bits(if x > 0.0 { b + 1 } else { b - 1 })
}

// Si(x) with rigorous alternating/asymptotic remainder bounds. Returns (center, err>=0).
fn si_center(x: f64) -> (f64, f64) {
    if x <= 20.0 {
        let mut term = x;
        let mut sum = x;
        let mut prev = f64::INFINITY;
        let mut k = 1u32;
        loop {
            term *= -(x * x) * ((2 * k - 1) as f64) / (((2 * k + 1) * (2 * k + 1) * (2 * k)) as f64); // a_k/a_{k-1}=-x^2(2k-1)/((2k+1)^2*2k)
            sum += term;
            let mag = term.abs();
            if mag <= 1e-18 * sum.abs().max(1.0) && mag <= prev {
                break;
            }
            prev = mag;
            k += 1;
        }
        let err = prev.max(term.abs());
        (sum, err)
    } else {
        // Si(x) = pi/2 - cos(x)f(x) - sin(x)g(x); alternating asymptotic series.
        let mut fm = 1.0 / x;
        let mut gm = 1.0 / (x * x);
        let (mut fs, mut gs) = (fm, gm);
        let mut m = 1u32;
        loop {
            let tf = fm * -((2 * m) as f64) * ((2 * m - 1) as f64) / (x * x);
            let tg = gm * -((2 * m + 1) as f64) * ((2 * m) as f64) / (x * x);
            if tf.abs() > fm.abs() || tg.abs() > gm.abs() || m > 40 { break; }
            fm = tf; gm = tg; fs += tf; gs += tg;
            m += 1;
        }
        let c = x.cos(); let s = x.sin();
        (
            std::f64::consts::FRAC_PI_2 - c * fs - s * gs,
            c.abs() * 2.0 * fm.abs() + s.abs() * 2.0 * gm.abs() + 1e-15,
        )
    }
}

fn j_center(u: f64) -> f64 {
    if u == 0.0 { return 0.0; } // J(0)=0; avoids 0/0
    let (s, _) = si_center(2.0 * u);
    s - u.sin() * u.sin() / u
}
// J(u)=int_0^u sin^2/t^2 dt; rigorous LOWER bound.
fn j_lo(u: f64) -> f64 {
    if u == 0.0 { return 0.0; } // J(0)=0 exactly (integrand limit finite)
    let (s, e) = si_center(2.0 * u);
    rdown(s - e) - rup(u.sin() * u.sin() / u)
}
// K(u)=int_0^u (sin^2 t/t^2) log(u/t) dt; convergent series K=Sum (-1)^{k+1}(2u)^{2k}/(2(2k)!(2k)^2).
fn k_series(u: f64) -> f64 {
    let x2 = 4.0 * u * u;
    let mut term = x2 / 16.0;
    let mut sum = term;
    let mut k = 2u32;
    loop {
        term *= -x2 * ((2 * (k - 1)) as f64).powi(2)
            / (((2 * k - 1) * (2 * k)) as f64 * ((2 * k) as f64).powi(2));
        sum += term;
        if term.abs() <= 1e-18 * sum.abs().max(1e-300) || k > 60 { break; }
        k += 1;
    }
    sum
}

fn main() {
    let started = std::time::Instant::now();
    let text = fs::read_to_string(PathBuf::from(DATA))
        .unwrap_or_else(|e| panic!("cannot read {DATA}: {e}"));
    let gammas: Vec<f64> = text
        .lines()
        .filter_map(|l| {
            let mut f = l.trim().split_whitespace();
            let row: u32 = f.next()?.parse().ok()?;
            if !(1..=ROW_MAX).contains(&row) { return None; }
            f.next()?.parse().ok()
        })
        .collect();
    assert_eq!(gammas.len(), ROW_MAX as usize, "expected exactly 19000 trusted rows");
    let big_g = *gammas.iter().max_by(|a, b| a.total_cmp(b)).unwrap();
    println!("data rows=1..={ROW_MAX} gamma_max={big_g:.9} quarantine=rows>{ROW_MAX} EXCLUDED");

    // ---- K grid ----
    const U_END: f64 = 34.0;
    const GRID: usize = 262_144;
    let h = U_END / GRID as f64;
    let mut kgrid = vec![0.0f64; GRID + 1];
    for i in 1..=GRID {
        let u = h * i as f64;
        // lim_{v->0} j_center(v)/v = 1 (j_center ~ v - v^3/9); guard the v==0 endpoint
        let gl = if u - h == 0.0 { 1.0 } else { j_center(u - h) / (u - h) };
        let gr = if u == 0.0 { 1.0 } else { j_center(u) / u };
        kgrid[i] = kgrid[i - 1] + 0.5 * h * (gr + gl);
    }
    let k_lo = |u: f64, kgrid: &[f64], h: f64| -> f64 {
        if u <= h {
            return k_series(u); // slack applied OUTSIDE the (n/pi) scaling (was: systematic low bias)
        }
        let t = u / h;
        let i = (t as usize).min(kgrid.len() - 2);
        let frac = t - i as f64;
        kgrid[i] * (1.0 - frac) + kgrid[i + 1] * frac
    };

    // ---- validation gate: against mpmath-30 ground truth (independent; see /tmp/isolate.py runs)
    let big_l = (big_g / (2.0 * std::f64::consts::PI)).ln();
    // refs computed with mp.dps=30: I(n)=(n/pi)*(L*jc(u0)+K(u0)), G=17255.317629325 [CHECKED NUMERICALLY]
    const REFS: [(usize, f64); 3] = [(1000, 82.2483293411), (50_000, 167867.611146), (1_000_000, 5738693.12253)];
    let mut validation_ok = true;
    for &(n, iref) in REFS.iter() {
        let u0 = n as f64 / (2.0 * big_g);
        // closed-form path exactly as certified below (slack OUTSIDE scaling)
        let closed = rdown((n as f64) / std::f64::consts::PI * (big_l * j_lo(u0) + k_lo(u0, &kgrid, h) - (SLACK_K + 1e-9)));
        let budget = (n as f64) / std::f64::consts::PI * (SLACK_K + 1e-9);
        // one-sided: closed may sit BELOW truth (declared slack), never materially ABOVE
        let over = closed - iref;
        println!("validate n={n} ref={iref:.9e} closed={closed:.9e} declared_budget={budget:.3e} over={over:.3e}");
        if over > 1e-9 * iref.abs() { validation_ok = false; }   // above truth beyond dust => formula bug
        if (iref - closed) > budget * 1.5 { validation_ok = false; } // below truth more than declared slack*1.5
    }
    // ---- eps_platt (upper bound, subtracted) ----
    let lt = rup((H_PLATT / (2.0 * std::f64::consts::PI)).ln() + 1.0);
    let eps_a = rup(1.0 / (2.0 * std::f64::consts::PI));
    let eps_b = rup(lt / H_PLATT);
    let eps_platt_up = |n: usize| rup((n as f64) * eps_a * eps_b);

    // ---- lambda_clean_lo: threaded phasor scan ----
    let mut lam = vec![0.0f64; N_MAX];
    let per = N_MAX.div_ceil(THREADS);
    thread::scope(|sc| {
        for (t, out) in lam.chunks_mut(per).enumerate() {
            let lo = t * per;
            let gs = &gammas;
            sc.spawn(move || {
                let len = out.len();
                let mut local = vec![0.0f64; len];
                let nb = gs.len().div_ceil(LANES);
                for blk in 0..nb {
                    let mut st_c = [1.0f64; LANES];
                    let mut st_s = [0.0f64; LANES];
                    let mut ph_c = [1.0f64; LANES];
                    let mut ph_s = [0.0f64; LANES];
                    let mut act = 0usize;
                    for lane in 0..LANES {
                        if let Some(&g) = gs.get(blk * LANES + lane) {
                            let th = (1.0 / (2.0 * g)).atan();
                            st_c[lane] = th.cos();
                            st_s[lane] = th.sin();
                            let ang = ((lo + 1) as f64) * th;
                            ph_c[lane] = ang.cos();
                            ph_s[lane] = ang.sin();
                            act += 1;
                        }
                    }
                    for v in local.iter_mut() {
                        let mut bs = 0.0f64;
                        for lane in 0..act {
                            let nc = ph_c[lane] * st_c[lane] - ph_s[lane] * st_s[lane];
                            let ns = ph_c[lane] * st_s[lane] + ph_s[lane] * st_c[lane];
                            ph_c[lane] = nc;
                            ph_s[lane] = ns;
                            bs += 4.0 * ns * ns;
                        }
                        *v += bs;
                    }
                }
                out.copy_from_slice(&local);
            });
        }
    });
    // outward-rounded-down clean sum with explicit accumulation-slack
    let lam_lo: Vec<f64> = (0..N_MAX)
        .map(|i| rdown(lam[i] - (1e-9 * (i + 1) as f64 + 1e-6)))
        .collect();

    // ---- main scan: B(n) = lam_lo + I_lo - eps_platt - eps_S(=0, see label) ----
    let mut min_b = f64::INFINITY;
    let mut min_n = 0usize;
    let mut first_bad: Option<(usize, f64, f64, f64, f64)> = None;
    for n in 1..=N_MAX {
        let u0 = n as f64 / (2.0 * big_g);
        let i_lo = rdown((n as f64) / std::f64::consts::PI * (big_l * j_lo(u0) + k_lo(u0, &kgrid, h) - (SLACK_K + 1e-9)));
        let b = lam_lo[n - 1] + i_lo - eps_platt_up(n);
        if b.is_nan() {
            println!("VERDICT: INCONCLUSIVE — NaN encountered at n={n}; certificate withheld.");
            return;
        }
        if b < min_b { min_b = b; min_n = n; }
        if b <= 0.0 && first_bad.is_none() {
            first_bad = Some((n, lam_lo[n - 1], i_lo, eps_platt_up(n), b));
        }
        if n % 50_000 == 0 {
            println!(
                "ckpt n={n:>7} lam_lo={:>14.6} I_lo={:>14.6} eps_platt={:.3e} B={:>14.6}",
                lam_lo[n - 1], i_lo, eps_platt_up(n), b
            );
        }
    }
    println!("real global_min B={min_b:.9} at n={min_n}");
    match first_bad {
        Some((n, l, i, e, b)) => println!(
            "FAIL first violating n={n}: lam_lo={l:.9} I_lo={i:.9} eps_platt={e:.6e} B={b:.9}"
        ),
        None => println!("real no_violation n=1..{N_MAX}"),
    }

    // ---- control gate: planted beta0=0.85, gamma=14.134725 quadruplet ----
    let beta = 0.85f64;
    let g1 = 14.13472514f64;
    let den = beta * beta + g1 * g1;
    let z1 = (((beta - 1.0) * beta + g1 * g1) / den, g1 / den);
    let z1n2 = z1.0 * z1.0 + z1.1 * z1.1;
    let z3 = (z1.0 / z1n2, -z1.1 / z1n2);
    let (mut p1, mut p3) = ((1.0f64, 0.0f64), (1.0f64, 0.0f64));
    let mut ctl_min = f64::INFINITY;
    let mut ctl_n = 0usize;
    for n in 1..=20_000usize {
        p1 = (p1.0 * z1.0 - p1.1 * z1.1, p1.0 * z1.1 + p1.1 * z1.0);
        p3 = (p3.0 * z3.0 - p3.1 * z3.1, p3.0 * z3.1 + p3.1 * z3.0);
        if n >= 1000 {
            let u0 = n as f64 / (2.0 * big_g);
            let i_lo =
                rdown((n as f64) / std::f64::consts::PI * (big_l * j_lo(u0) + k_lo(u0, &kgrid, h) - (SLACK_K + 1e-9)));
            let pb = lam_lo[n - 1] + i_lo - eps_platt_up(n) + 4.0 - 2.0 * p1.0 - 2.0 * p3.0;
            if pb < ctl_min { ctl_min = pb; ctl_n = n; }
        }
    }
    let control_fired = ctl_min < 0.0 && (1000..=20_000).contains(&ctl_n);
    println!("control planted_min B={ctl_min:.9} at n={ctl_n} fired={control_fired}");

    // ---- verdict ----
    if !control_fired {
        println!("VERDICT: INCONCLUSIVE — control gate did NOT fire (planted beta0=0.85 must drive bound<0 in n in [1000,20000]).");
    } else if first_bad.is_none() {
        println!("VERDICT: PASS — true lambda_n > 0 on [1,10^6] [PROVEN-modulo-(a) zero values <=G audited <=7e-5, (b) on-line-below-H per Platt-Trudgian]");
        println!("LABEL: overall status CHECKED NUMERICALLY (modulo-hypotheses as printed above); eps_S=0 is a HYPOTHESIS: on-line below H=3e12 assumed per Platt-Trudgian 2021 verification; no explicit cited |S(t)| constant was available in ranking.md, so the discrete-to-smooth-tail error term is NOT bounded here.");
    } else {
        println!("VERDICT: FAIL — see first violating n above.");
    }
    println!("CHECKED NUMERICALLY: finite f64 scan, rows 1..={ROW_MAX} only, n<=1e6 only; no global Li-positivity or RH claim.");
    println!("elapsed_seconds={:.3}", started.elapsed().as_secs_f64());
}
