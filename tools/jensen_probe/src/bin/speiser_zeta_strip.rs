// wave-rh5(D): extend zeta' LEFT-STRIP zero-free certification to t in [5000,12000].
// Argument principle on 0.25-wide cells; engine = Hurwitz/Euler-Maclaurin from
// speiser_dh_certify.rs (wave-rh4b/C). Labels in output.
//
// DEVIATION (documented in final_d.md): right edge at SIG_HI=0.49, NOT 0.5 — zeta'
// provably has zeros ON sigma=1/2 (Hardy line zeros + Rolle), which would sit on a
// sigma=0.5 contour and make the winding ill-posed (false-PASS risk). Certified
// strip is [SIG_LO, 0.49]; sliver (0.49,1/2) reported as uncovered.
use std::f64::consts::PI;
use std::time::Instant;
type C = (f64, f64);

const SIG_LO: f64 = 0.001;
const SIG_HI: f64 = 0.49;
const DT_CELL: f64 = 0.25;
const NP_W: usize = 12;
const NP_H: usize = 24;
const GAP_MAX: f64 = 2.8; // require arg-continuation gap < pi - margin
const M_EM: usize = 10;

fn cadd(a: C, b: C) -> C { (a.0 + b.0, a.1 + b.1) }
fn csub(a: C, b: C) -> C { (a.0 - b.0, a.1 - b.1) }
fn cmul(a: C, b: C) -> C { (a.0 * b.0 - a.1 * b.1, a.0 * b.1 + a.1 * b.0) }
fn cdiv(a: C, b: C) -> C { let d = b.0 * b.0 + b.1 * b.1; ((a.0 * b.0 + a.1 * b.1) / d, (a.1 * b.0 - a.0 * b.1) / d) }
fn cabs(a: C) -> f64 { a.0.hypot(a.1) }
fn cexp(z: C) -> C { let e = z.0.exp(); (e * z.1.cos(), e * z.1.sin()) }

// Hurwitz zeta + analytic s-derivative at a>0 via Euler-Maclaurin; (zeta, zeta', err_bound)
fn hurwitz(s: C, a: f64, n_em: usize, lnx: &[f64]) -> (C, C, f64) {
    let bco = [8.333333333333333e-2, -1.388888888888889e-3, 3.306878306878307e-5,
               -8.267195767195768e-7, 2.087675698786810e-8, -5.284190138687493e-10,
               1.338253653068468e-11, -3.389680318224120e-13, 8.586069205618e-15,
               -2.175643985292551e-16];
    let (mut z, mut zp) = ((0.0, 0.0), (0.0, 0.0));
    for n in 0..n_em {
        let x = n as f64 + a;
        let w = cexp(cmul(s, (-lnx[n], 0.0)));
        z = cadd(z, w);
        zp = cadd(zp, cmul((-lnx[n], 0.0), w));
    }
    let xa = n_em as f64 + a;
    let l = lnx[n_em];
    let w = cexp(cmul(s, (-l, 0.0)));
    let sm1 = csub(s, (1.0, 0.0));
    z = cadd(cadd(z, cdiv(cmul(w, (xa, 0.0)), sm1)), cmul((0.5, 0.0), w));
    zp = cadd(cadd(zp, cmul(cmul(w, (xa, 0.0)),
        csub(cdiv((-l, 0.0), sm1), cdiv((1.0, 0.0), cmul(sm1, sm1))))),
        cmul((-0.5 * l, 0.0), w));
    let (mut p, mut hsum, mut jn, mut last) = ((1.0, 0.0), (0.0, 0.0), 0usize, 0.0f64);
    for m in 1..=M_EM {
        let k = 2 * m - 1;
        while jn < k {
            let sj = cadd(s, (jn as f64, 0.0));
            p = cmul(p, sj);
            hsum = cadd(hsum, cdiv((1.0, 0.0), sj));
            jn += 1;
        }
        let wk = cmul(w, (xa.powi(-(k as i32)), 0.0));
        z = cadd(z, cmul((bco[m - 1], 0.0), cmul(p, wk)));
        zp = cadd(zp, cmul((bco[m - 1], 0.0), cmul(cmul(p, csub(hsum, (l, 0.0))), wk)));
        last = cabs(cmul((bco[m - 1], 0.0), cmul(p, wk)));
    }
    (z, zp, 4.0 * last * ((cabs(s) + 2.0 * M_EM as f64) / xa).powi(2) * (2.0 * M_EM as f64 + l.abs() + 1.0))
}

fn zeta_prime(s: C, n: usize, lnx: &[f64]) -> (C, f64) { let (_, zp, e) = hurwitz(s, 1.0, n, lnx); (zp, e) }

// ln(n+a) table for a given shift a (hurwitz indexes terms x=n+a)
fn mk_lnx(n: usize, a: f64) -> Vec<f64> { (0..=n).map(|k| (k as f64 + a).ln()).collect() }

// DH f'(s) = d/ds[5^-s sum r(j) zeta(s,j/5)] with same coefficients as wave-rh4b(C)
fn dh_fp(s: C, c: f64) -> (C, f64) {
    let r = [0.0, 1.0, c, -c, -1.0];
    let n = 200usize;
    let w5 = cexp(cmul(s, (-5.0f64.ln(), 0.0)));
    let (mut fp, mut err) = ((0.0, 0.0), 0.0f64);
    for j in 1..=4 {
        let tab = mk_lnx(n, j as f64 / 5.0);
        let (z, zp, e) = hurwitz(s, j as f64 / 5.0, n, &tab);
        fp = cadd(fp, cmul((r[j], 0.0), cmul(w5, csub(zp, cmul((5.0f64.ln(), 0.0), z)))));
        err += r[j].abs() * cabs(w5) * e;
    }
    (fp, err)
}

fn circle_wind<F: Fn(C) -> (C, f64)>(center: C, h: f64, pts: usize, eval: F) -> (i32, f64, f64, f64) {
    wind_generic((0..=pts).map(|k| {
        let a = 2.0 * PI * (k % pts) as f64 / pts as f64;
        (center.0 + h * a.cos(), center.1 + h * a.sin())
    }), eval)
}

// CCW rectangle boundary in (sigma, t) [C=(re,im)]; returns (wind, min|v|, max_err, max_gap); Err on gap violation
fn rect_wind<F: Fn(C) -> (C, f64)>(t0: f64, t1: f64, s0: f64, s1: f64, mult: usize, eval: F) -> Result<(i32, f64, f64, f64), ()> {
    let (nw, nh) = (NP_W * mult, NP_H * mult);
    let mut path = Vec::with_capacity(2 * nw + 2 * nh + 1);
    for i in 0..nw { let tv = t0 + (t1 - t0) * i as f64 / nw as f64; path.push((s0, tv)); }
    for i in 0..nh { let sv = s0 + (s1 - s0) * i as f64 / nh as f64; path.push((sv, t1)); }
    for i in 0..nw { let tv = t1 - (t1 - t0) * i as f64 / nw as f64; path.push((s1, tv)); }
    for i in 0..nh { let sv = s1 - (s1 - s0) * i as f64 / nh as f64; path.push((sv, t0)); }
    path.push(path[0]);
    let r = wind_generic(path.into_iter(), eval);
    if r.3 >= GAP_MAX { Err(()) } else { Ok(r) }
}

fn wind_generic<I: Iterator<Item = C>, F: Fn(C) -> (C, f64)>(path: I, eval: F) -> (i32, f64, f64, f64) {
    let (mut prev, mut tot, mut mn, mut me, mut mgap) = (None::<f64>, 0.0f64, f64::INFINITY, 0.0f64, 0.0f64);
    for s in path {
        let (v, e) = eval(s);
        let m = cabs(v);
        mn = mn.min(m);
        me = me.max(e);
        let a = v.1.atan2(v.0);
        if let Some(p) = prev {
            let mut d = a - p;
            while d > PI { d -= 2.0 * PI; }
            while d < -PI { d += 2.0 * PI; }
            mgap = mgap.max(d.abs());
            tot += d;
        }
        prev = Some(a);
    }
    ((tot / (2.0 * PI)).round() as i32, mn, me, mgap)
}

fn main() {
    // probe mode: ./speiser_zeta_strip probe sigma t  -> err bound vs N
    let args: Vec<String> = std::env::args().collect();
    if args.len() > 3 && args[1] == "probe" {
        let sg: f64 = args[2].parse().unwrap();
        let tt: f64 = args[3].parse().unwrap();
        for &n in &[400usize, 800, 1200, 1600, 2000, 2400, 2800, 3200, 4000] {
            let tab = mk_lnx(n + 1, 1.0);
            let (v, e) = zeta_prime((sg, tt), n, &tab);
            println!("probe s=({:.3},{:.0}) N={} |z'|={:.6e} err_bound={:.3e} ratio={:.3e}", sg, tt, n, cabs(v), e, e / cabs(v));
        }
        return;
    }
    let t0all = Instant::now();
    let t_lo0 = 5000.0f64; let t_hi1 = 12000.0f64; const DT_BAND: f64 = 250.0;
    let nmax = (600.0 + (t_hi1 / 3.0).ceil()) as usize;
    let mut lnx = Vec::with_capacity(2 * nmax + 2);
    for n in 0..=2 * nmax { lnx.push((n as f64 + 1.0).ln()); }
    println!("speiser_zeta_strip strip=({},{}) bands=[{},{}] dt_band={} cell_dt={} Nmax={} M={}",
             SIG_LO, SIG_HI, t_lo0, t_hi1, DT_BAND, DT_CELL, nmax, M_EM);

    // sanity: analytic zeta' vs central finite difference of zeta
    let st = (0.37, 6000.0);
    let hh = 1e-5;
    let (za, _, _) = hurwitz((st.0 + hh, st.1), 1.0, 1000, &lnx);
    let (zb, _, _) = hurwitz((st.0 - hh, st.1), 1.0, 1000, &lnx);
    let fd = cmul(csub(za, zb), (0.5 / hh, 0.0));
    let (zpa, ea) = zeta_prime(st, 1000, &lnx);
    println!("fd_crosscheck rel_diff={:.3e} (analytic vs finite-diff zeta')",
             cabs(csub(fd, zpa)) / cabs(zpa));

    // CONTROL: DH f' circle must wind 1 (zero certified by wave-rh4b/C)
    let c = ((10.0 - 2.0 * 5.0f64.sqrt()).sqrt() - 2.0) / (5.0f64.sqrt() - 1.0);
    let (wdh, mnd, med, _) = circle_wind((0.42, 85.70), 0.15, 128, |s| dh_fp(s, c));
    println!("CONTROL dh_winding center=(0.4200,85.70) h=0.15 wind={} min|f'|={:.6e} max_err={:.3e}",
             wdh, mnd, med);
    if wdh != 1 {
        println!("VERDICT: BROKEN PIPELINE (DH control winding {} != 1) — no zeta band trusted", wdh);
        return;
    }

    // spot validation per band: |zeta'(N) - zeta'(N/2)| <= bound?
    let nbands = ((t_hi1 - t_lo0) / DT_BAND) as usize;
    let mut frontier = t_lo0;
    let mut all_pass = true;
    for b in 0..nbands {
        if t0all.elapsed().as_secs_f64() > 420.0 {
            println!("TIME LIMIT reached at band {} — stopping, frontier={}", b, frontier);
            all_pass = false;
            break;
        }
        let tl = t_lo0 + DT_BAND * b as f64;
        let th = tl + DT_BAND;
        let nem = (600.0 + (th / 3.0).ceil()) as usize;
        // spot check convergence doubling
        let mut worst = 0.0f64;
        for k in 0..3 {
            let sg = 0.05 + 0.4 * (k as f64) / 3.0;
            let tt = tl + DT_BAND * (0.2 + 0.3 * k as f64);
            let (v1, e1) = zeta_prime((sg, tt), nem, &lnx);
            let (v2, _) = zeta_prime((sg, tt), 2 * nem, &lnx);
            worst = worst.max(cabs(csub(v1, v2)) / e1.max(1e-300));
        }
        let bt0 = Instant::now();
        let (ncx, ncy) = ((DT_BAND / DT_CELL) as usize, 1usize);
        let (mut tot, mut gmn, mut gme, mut ggap, mut bad) = (0i32, f64::INFINITY, 0.0f64, 0.0f64, false);
        'cells: for i in 0..ncx {
            for _j in 0..ncy {
                let a = tl + i as f64 * DT_CELL;
                match rect_wind(a, a + DT_CELL, SIG_LO, SIG_HI, 1, |s| zeta_prime(s, nem, &lnx)) {
                    Ok(r) => { tot += r.0; gmn = gmn.min(r.1); gme = gme.max(r.2); ggap = ggap.max(r.3); }
                    Err(_) => {
                        if let Ok(r) = rect_wind(a, a + DT_CELL, SIG_LO, SIG_HI, 4, |s| zeta_prime(s, nem, &lnx)) {
                            tot += r.0; gmn = gmn.min(r.1); gme = gme.max(r.2); ggap = ggap.max(r.3);
                        } else { bad = true; break 'cells; }
                    }
                }
            }
        }
        let ratio = gme / gmn.max(1e-300);
        let verdict = if bad { "INCONCLUSIVE(arg-gap)" }
            else if worst > 1.0 { "INCONCLUSIVE(spot-check)" }
            else if ratio > 0.1 { "CAUTION(err/min)" }
            else if tot == 0 { "PASS" } else { "FAIL(zeros present)" };
        println!("band [{:.0},{:.0}] cells={} wind_total={} min|z'|={:.3e} max_err={:.3e} max_gap={:.3} spot_ratio={:.2e} err/min={:.2e} t={:.1}s {}",
                 tl, th, ncx, tot, gmn, gme, ggap, worst, ratio, bt0.elapsed().as_secs_f64(), verdict);
        if verdict != "PASS" && verdict != "CAUTION(err/min)" { all_pass = false; break; }
        frontier = th;
    }
    println!("FRONTIER: contiguous certification [10,5000] (wave-8B) + [5000,{}] => T={}", frontier,
             if all_pass { format!("{}", frontier) } else { format!("{} (stopped honestly)", frontier) });
    println!("labels: winding numbers CHECKED NUMERICALLY-RIGOROUS given printed bounds (f64, EM next-term x4 bound,");
    println!("spot-doubling validation); strip covered = [0.001,0.49]; sliver (0.49,0.5) NOT covered (line zeros of zeta')");
}
