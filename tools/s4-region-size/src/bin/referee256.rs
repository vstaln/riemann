// S4 referee: independent high-precision check of the 5 mpmath-claimed points
// (13,200), (14,141), (20,183), (20,184), (20,200) plus a few nearby flags.
// Reuses the main binary's functions via include!, but at 256 bits root-finding
// (PR=128 in main; coefficients span ~1e-484 at d=20,n=200 so higher precision
// is the honest referee). No Python; rug only.
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::cmp::Ordering;
use std::time::Instant;

const PG: u32 = 200; // gamma working precision (~60 digits)
const PR: u32 = 256; // root-finding precision (~77 digits)
const NGL: usize = 48;
const KMAX: usize = 220;

include!("../main_shared.rs");

// constants the shared code relies on (moved out of main.rs)
const NSUM: usize = 8; // n-truncation in Phi
const UMAX: f64 = 4.0; // u-integral cutoff (tail < 1e-3800)
const NPAN: usize = 40; // panels on [0, UMAX]

fn main() {
    let t0 = Instant::now();
    println!("[referee256] gamma at {} bits, aberth at {} bits", PG, PR);
    let gl = gl_nodes(PG);
    let mut gamma: Vec<Float> = Vec::with_capacity(KMAX + 1);
    for k in 0..=KMAX {
        let mk = moment(k, &gl, PG);
        gamma.push(gamma_k(k, &mk, PG));
    }
    // verify gamma[0..8] vs the 60-digit known table
    let known: [&str; 9] = [
        "0.4971207781883141099127737396853977198073",
        "0.0114859721575727187676249382488160851323",
        "0.000246904036140636013780691582989702276272",
        "0.000004994132888313162432028552355067724221758",
        "0.00000009581343723225929219340648631276497622301",
        "0.000000001753923091213315303489457133184146682862",
        "0.00000000003077668832786528369526151242159777679754",
        "0.0000000000005196051571847475304071348853364035054351",
        "0.000000000000008466271866458899923670642823387187309359",
    ];
    let mut ok = true;
    for (i, s) in known.iter().enumerate() {
        let kf = Float::with_val(PG, Float::parse(s).unwrap());
        let diff = Float::with_val(PG, &gamma[i] - &kf);
        let rel = Float::with_val(PG, diff.abs() / &kf);
        if rel.to_f64() > 1e-30 {
            println!("  gamma[{}] MISMATCH rel {:.1e}", i, rel.to_f64());
            ok = false;
        }
    }
    println!("  gamma verification: {}", if ok { "ALL OK at 1e-30" } else { "FAILED" });

    // The 5 mpmath-claimed points + the earliest d>=13 flag + a cluster tail
    let points: [(usize, usize); 8] = [
        (13, 200),
        (14, 141),
        (20, 183),
        (20, 184),
        (20, 200),
        (14, 145), // a flag with sturm_count=5 (bizarre)
        (15, 141), // d=15 onset area
        (17, 163), // a d=17 flag
    ];

    for (d, n) in points.iter() {
        let c = build_coefs(*d, *n, &gamma);
        // ratio init on the real axis (same as main), aberth at 256 bits
        let mut z: Vec<Cx> = Vec::with_capacity(*d);
        for j in 1..=*d {
            let ratio = Float::with_val(PR, &c[j - 1].r / &c[j].r);
            z.push(Cx { r: -ratio, i: zf(PR, 0.0) });
        }
        let (conv, _worst) = aberth(&c, &mut z, 100);
        // classification: all roots real within threshold
        let mut hyp = true;
        let mut max_imag = Float::with_val(PR, 0.0);
        for zi in z.iter() {
            let scale = Float::with_val(PR, zf(PR, 1.0) + zi.r.clone().abs());
            let thr = Float::with_val(PR, zf(PR, 1e-30) * &scale);
            let ai = zi.i.clone().abs();
            if ai > max_imag {
                max_imag = ai.clone();
            }
            if ai > thr {
                hyp = false;
            }
        }
        // Sturm independent check
        let cfl: Vec<Float> = c.iter().map(|x| x.r.clone()).collect();
        let sc = sturm_count_neg(&cfl);
        // residual check: |P(r_j)| relative to coefficient scale, at the found roots
        let mut max_res = Float::with_val(PR, 0.0);
        let mut max_res_scale = Float::with_val(PR, 0.0);
        for zi in z.iter() {
            let (pv, _) = horner(&c, zi);
            let av = czabs(&pv);
            // scale: sum |c_j| |z|^j at the root (rough conditioning proxy)
            let mut scl = zf(PR, 0.0);
            let az = czabs(zi);
            let mut pwr = zf(PR, 1.0);
            for cj in c.iter() {
                scl += Float::with_val(PR, czabs(cj) * &pwr);
                pwr *= &az;
            }
            if av > max_res {
                max_res = av.clone();
            }
            if scl > max_res_scale {
                max_res_scale = scl.clone();
            }
        }
        let rel_res = Float::with_val(PR, &max_res / &max_res_scale);
        println!(
            "  (d,n)=({},{}): aberth conv={} hyp(1e-30)={} max|Im|/scale={:.1e} sturm_count={} (d={})  max|P(r)|/scale={:.1e}",
            d,
            n,
            conv,
            hyp,
            max_imag.to_f64(),
            sc,
            *d,
            rel_res.to_f64()
        );
    }
    println!("[referee256] done in {:.1}s", t0.elapsed().as_secs_f64());
}
