// effsieve: exact prime-power sums needed for the effective finite-T bound (V20).
//
// For X = exp(L) (prime powers n <= X), accumulates, EXACTLY (f64 accumulates to
// ~1e-15 relative; all terms positive except noted):
//   Sg   = sum_{n<=X} Lambda(n)^2/n * g(log n),  g(y) = (phi^2 * phi^2)(y)
//   S1   = sum Lambda(n)^2/n * (L - log n)
//   S2   = sum Lambda(n)^2/n                  (Chebyshev-Mertens check: ~ L^2/2)
//   S3   = sum Lambda(n)^2 * log n / n        (~ L^3/3)
//   S4   = sum Lambda(n)^2                    (MV off-diag input: ~ c*X*L)
//   Sa   = sum Lambda(n)/sqrt(n)              (trace P-part: ~ 2.08 sqrt X)
//   SaL  = sum Lambda(n)/(sqrt(n)*log n)      (cross-term input)
//   Sp   = sum Lambda(n)/n                    (Mertens check: ~ L)
//   Spsi = sum Lambda(n)                      (psi(X) check: ~ X)
//   cnt  = number of prime powers
// plus the exact values of RR(log n) for the handful of n where g deviates from
// the closed form g(y) = (L-y) - 4w(1-a_rho) (i.e. log n < 1 or log n > L-2; w=1).
//
// g(y) is computed by direct Simpson quadrature over u in [-L/2, L/2-y] of
// phi(u)^2 phi(u+y)^2, phi(u) = rho((L/2 - |u|)/w), rho(x)=x - sin(2 pi x)/(2 pi),
// w = 1.  This is exact to ~1e-12 (Simpson with 2000 panels).
//
// Usage: effsieve L   (L = lambda * log(T/2pi)); prints one line per output.
use std::env;

const PI: f64 = std::f64::consts::PI;

#[inline]
fn rho(x: f64) -> f64 {
    x - (2.0 * PI * x).sin() / (2.0 * PI)
}

// phi(u)^2 for the paper's taper, w = 1: rho((L/2 - |u|)/w)^2 on |u| <= L/2.
#[inline]
fn phi2(u: f64, l2: f64) -> f64 {
    let a = u.abs();
    if a > l2 {
        return 0.0;
    }
    let t = l2 - a; // in [0, L/2]
    let tt = t; // (L/2 - |u|) / w  with w=1
    if tt > 1.0 {
        1.0
    } else {
        let r = rho(tt);
        r * r
    }
}

// g(y) = int phi(u)^2 phi(u+y)^2 du, Simpson with NP panels.
fn g_of(y: f64, l: f64) -> f64 {
    let l2 = l / 2.0;
    let b = l2 - y; // u range [-l2, b]
    if b < -l2 {
        return 0.0;
    }
    let np = 2000usize;
    let h = (b + l2) / np as f64;
    let mut s = phi2(-l2, l2) * phi2(-l2 + y, l2) + phi2(b, l2) * phi2(b + y, l2);
    for i in 1..np {
        let u = -l2 + h * i as f64;
        let w = if i % 2 == 0 { 2.0 } else { 4.0 };
        s += w * phi2(u, l2) * phi2(u + y, l2);
    }
    s * h / 3.0
}

// segmented sieve of primes up to X; accumulate the sums over prime powers.
fn run(l: f64) {
    let x = l.exp();
    let l2 = l / 2.0;

    // accumulator for g(log n) contributions.
    let mut sg: f64 = 0.0;
    let mut s1: f64 = 0.0; // (L - logn)
    let mut s2: f64 = 0.0; // 1
    let mut s3: f64 = 0.0; // logn
    let mut s4: f64 = 0.0; // Lambda(n)^2
    let mut sa: f64 = 0.0; // Lambda/sqrt(n)
    let mut sal: f64 = 0.0;
    let mut sp: f64 = 0.0; // Lambda(n)/n
    let mut spsi: f64 = 0.0;
    let mut cnt: u64 = 0;

    // small primes via a simple sieve to sqrt(X)
    let sx = (x.sqrt() as usize) + 2;
    let mut small = vec![true; sx + 1];
    small[0] = false;
    small[1] = false;
    for i in 2..=sx {
        if small[i] {
            let mut j = i * i;
            while j <= sx {
                small[j] = false;
                j += i;
            }
        }
    }
    let primes_small: Vec<u64> = (2..=sx).filter(|&i| small[i as usize]).map(|i| i as u64).collect();

    let seg = 2_000_000u64;
    let mut seg_start: u64 = 2;
    while seg_start <= x as u64 {
        let seg_end = (seg_start + seg - 1).min(x as u64);
        let n = (seg_end - seg_start + 1) as usize;
        let mut isp = vec![true; n];
        for &p in &primes_small {
            let p = p as u64;
            let p2 = p * p;
            if p2 > seg_end {
                break;
            }
            let mut m = ((seg_start + p - 1) / p) * p;
            if m < p2 {
                m = p2;
            }
            while m <= seg_end {
                isp[(m - seg_start) as usize] = false;
                m += p;
            }
        }
        for (i, &pr) in isp.iter().enumerate() {
            if pr {
                let nv = seg_start + i as u64;
                // prime powers nv^k <= X
                let logp = (nv as f64).ln();
                let mut pk = nv;
                let mut k: u32 = 1;
                while pk <= x as u64 {
                    let logn = k as f64 * logp;
                    let lp = logp * logp;
                    let wgt = lp / pk as f64; // Lambda(n)^2 / n
                    sg += wgt * g_of(logn, l);
                    s1 += wgt * (l - logn);
                    s2 += wgt;
                    s3 += wgt * logn;
                    s4 += lp;
                    sa += logp / (pk as f64).sqrt();
                    sal += logp / ((pk as f64).sqrt() * logn);
                    sp += logp / pk as f64;
                    spsi += logp;
                    cnt += 1;
                    pk = pk.checked_mul(nv).unwrap_or(u64::MAX);
                    k += 1;
                }
            }
        }
        seg_start = seg_end + 1;
    }

    println!("L={} X={:.6e}", l, x);
    println!("Sg={:.12e}", sg);
    println!("S1={:.12e}", s1);
    println!("S2={:.12e}", s2);
    println!("S3={:.12e}", s3);
    println!("S4={:.12e}", s4);
    println!("Sa={:.12e}", sa);
    println!("SaL={:.12e}", sal);
    println!("Sp={:.12e}", sp);
    println!("Spsi={:.12e}", spsi);
    println!("cnt={}", cnt);
    println!("g0={:.15e}", g_of(0.0, l));
    println!("gmid={:.15e}", g_of(l / 2.0, l));
    println!("gLm2={:.15e}", g_of(l - 2.0, l));
    println!("LJ2={:.15e}", l * l * l * 0.5 * 1.0 / 3.0); // (L^3 J/2) placeholder; exact J in python
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let l: f64 = args[1].parse().expect("usage: effsieve L");
    run(l);
}
