// Direct-RH Gaussian-Perron probe v3 (CORRECTED). Falsification of
// "Delta_{X,alpha} bounded over sigma>1/2 at fixed t" (H1).
//
// v2 BUG (fixed here): v2 summed the *divergent* series
//   (sigma-1/2) Re Sum_{n<=N} Lambda(n) n^{-s} (1 - W(n)),
// where W(n) = 1/2 erfc((log n - log X)/(2 alpha sqrt(Y))).  Since
// 1 - W(n) -> 1 as n -> infinity (W is a LOW-PASS cutoff at X, not a window),
// that series diverges for sigma <= 1; truncating at a fixed N makes the sum
// dominated by the cutoff N (value ~ N^{1-s} - X^{1-s}, DEcreasing in X), not
// by the pole main term.  That is why v2 measured slopes ~ -0.07 / +0.02 and
// the saved "Lorentz" artifact -0.11 / +0.06: both are cutoff artifacts.
//
// v3 computes the actual object:
//   P_{X,alpha}(s) = - Sum_n Lambda(n) n^{-s} W(n)        (converges absolutely:
//                       W decays super-exponentially for n >> X)
//   Delta(s) = (sigma - 1/2) Re[ P - zeta'/zeta(s) ]      (zeta'/zeta via
//                       certified Euler-Maclaurin, tools/wave8b em.rs)
// and fits slope of log|Delta| vs log X.  Expected (pole main term of the
// Gaussian-Perron residue, Thm 3.3 transcription):
//   |pole| ~ X^{(1-sigma) + alpha^2((1-sigma)^2 - t^2)} / |1-s|
// so slope(t=0) = (1-sigma)(1 + alpha^2(1-sigma)) = 0.2525 at (alpha,sigma)=(0.2,0.75),
//    slope(t=1) = (1-sigma) + alpha^2((1-sigma)^2 - 1) = 0.2125.
// Both > 0 => H1 (uniform boundedness) still false, via the pole main term.
//
// Sieve primes to N (bitset); iterate prime powers p^k <= N.  W decays like
// erfc so the n >> X tail contributes < 1e-10 once N >> X e^{6 alpha sqrt(Y)}.
mod em;
use em::{em_n_for, zeta_em};

const N: usize = 100_000_000;

fn erf(x: f64) -> f64 {
    let ax = x.abs();
    let t = 1.0 / (1.0 + 0.3275911 * ax);
    let poly = t * (0.254829592
        + t * (-0.284496736
            + t * (1.421413741 + t * (-1.453152027 + t * 1.061405429))));
    let y = 1.0 - poly * (-ax * ax).exp();
    if x < 0.0 { -y } else { y }
}

fn erfc(x: f64) -> f64 {
    if x >= 0.0 { 1.0 - erf(x) } else { 1.0 + erf(-x) }
}

fn primes_to(n: usize) -> Vec<u32> {
    let mut bits = vec![true; n + 1];
    bits[0] = false;
    bits[1] = false;
    let mut i = 2usize;
    while i * i <= n {
        if bits[i] {
            let mut j = i * i;
            while j <= n {
                bits[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    (2..=n).filter(|&x| bits[x]).map(|x| x as u32).collect()
}

// zeta'/zeta(s) = (zeta'(s)) / (zeta(s)) from certified EM.
fn zeta_prime_over_zeta(s_re: f64, s_im: f64) -> (f64, f64, f64) {
    let e = zeta_em(s_re, s_im, em_n_for(s_im.abs()));
    let d = e.re * e.re + e.im * e.im;
    let r = (e.dre * e.re + e.dim * e.im) / d;
    let i = (e.dim * e.re - e.dre * e.im) / d;
    // crude relative error: |zeta'|/|zeta|^2 * (derr*|zeta| + |zeta'|*err)
    let zp_mag = (e.dre * e.dre + e.dim * e.dim).sqrt();
    let z_mag = (e.re * e.re + e.im * e.im).sqrt();
    let err = (zp_mag * e.err + z_mag * e.derr) / d;
    (r, i, err)
}

fn main() {
    let alpha = 0.2f64;
    let sigma = 0.75f64;
    let xs = [1e4f64, 3e4, 1e5, 3e5, 1e6];
    let ts = [0.0f64, 1.0f64];
    println!("# Gaussian-Perron defect probe v3 (CORRECTED: convergent P, not divergent 1-W sum)");
    println!("# alpha={} sigma={} sieve N={}", alpha, sigma, N);

    let primes: Vec<u32> = primes_to(N);
    println!("# primes up to 100: {}", primes.iter().filter(|&&p| p <= 100).count());

    // self-check: psi(x) = sum_{n<=x} Lambda(n), two independent methods
    let mut psi100 = 0.0f64;
    for &p in &primes {
        if p > 100 { break; }
        let lp = (p as f64).ln();
        let mut pk = p as f64;
        while pk <= 100.0 { psi100 += lp; pk *= p as f64; }
    }
    println!("# self-check psi(100) = {:.6}", psi100);
    let mut psi1e5 = 0.0f64;
    for &p in &primes {
        if p > 100_000 { break; }
        let lp = (p as f64).ln();
        let mut pk = p as f64;
        while pk <= 100_000.0 { psi1e5 += lp; pk *= p as f64; }
    }
    println!("# self-check psi(1e5) = {:.6}", psi1e5);
    // independent psi(1e5): count prime powers via trial division on integers
    let mut psi1e5b = 0.0f64;
    for n in 2..=100_000usize {
        // n is a prime power iff all prime factors are equal; count distinct primes
        let mut mm = n; let mut dist = 0usize; let mut kk = 2usize;
        while kk * kk <= mm {
            if mm % kk == 0 { dist += 1; while mm % kk == 0 { mm /= kk; } }
            kk += 1;
        }
        if mm > 1 { dist += 1; }
        if dist == 1 && n > 1 {
            // prime power p^j: Lambda = ln p = ln n / j, j = number of prime factors with multiplicity
            let mut mmm = n; let mut j = 0usize; let mut kkk = 2usize;
            while kkk * kkk <= mmm {
                while mmm % kkk == 0 { mmm /= kkk; j += 1; }
                kkk += 1;
            }
            if mmm > 1 { j += 1; }
            psi1e5b += (n as f64).ln() / (j as f64);
        }
    }
    println!("# self-check psi(1e5) method B = {:.6}  (match: {})", psi1e5b, (psi1e5 - psi1e5b).abs() < 1e-9);

    for &t in &ts {
        println!("\n## t = {}", t);
        let (zr, zi, _ze) = zeta_prime_over_zeta(sigma, t);
        println!("# zeta'/zeta({}+{}i) = {:.9} {:.9}i", sigma, t, zr, zi);
        println!("X    logX    Re[P-z'/z]   |Delta|   log|Delta|");
        let mut lx: Vec<f64> = Vec::new();
        let mut ly: Vec<f64> = Vec::new();
        for &x in &xs {
            let y = x.ln();
            let wden = 2.0 * alpha * y.sqrt();
            let mut re = 0.0f64;
            let mut im = 0.0f64;
            for &p in &primes {
                let lp = (p as f64).ln();
                let mut pk = p as f64;
                while pk <= N as f64 {
                    let lnk = pk.ln();
                    let u = (lnk - y) / wden;
                    let w = 0.5 * erfc(u);
                    if w > 1e-18 {
                        let theta = -t * lnk;
                        let mag = (-sigma * lnk).exp() * w * lp;
                        re += mag * theta.cos();
                        im += mag * theta.sin();
                    }
                    pk *= p as f64;
                }
            }
            let d_re = -re - zr;
            let d_im = -im - zi;
            let mag = (d_re * d_re + d_im * d_im).sqrt();
            let delta_mag = (sigma - 0.5) * mag;
            println!("{:.0} {:.4} {:.6e} {:.6e} {:.4}", x, y, d_re, delta_mag, delta_mag.abs().ln());
            lx.push(y);
            ly.push(delta_mag.abs().ln());
        }
        // least-squares slope over the log-log points
        let n = lx.len();
        let mx = lx.iter().sum::<f64>() / n as f64;
        let my = ly.iter().sum::<f64>() / n as f64;
        let mut num = 0.0; let mut den = 0.0;
        for i in 0..n {
            num += (lx[i] - mx) * (ly[i] - my);
            den += (lx[i] - mx) * (lx[i] - mx);
        }
        let slope = num / den;
        let pred = (1.0 - sigma) + alpha * alpha * ((1.0 - sigma) * (1.0 - sigma) - t * t);
        println!("# fitted slope = {:.4}   predicted pole-term slope = {:.4}", slope, pred);
        println!("# => H1 (uniform boundedness over sigma>1/2, fixed t) {}", if slope > 0.05 { "FALSE (pole main term grows)" } else { "not falsified by this data" });
    }
    println!("\n# NOTE: |Delta| = (sigma-1/2)|P - zeta'/zeta|; at generic t the zero sum is");
    println!("# exponentially damped (Gaussian factor e^( -alpha^2 Y (gamma-t)^2 )) so the pole term");
    println!("# dominates: slope = (1-sigma) + alpha^2((1-sigma)^2 - t^2). At sigma=0.75, alpha=0.2:");
    println!("# t=0 -> 0.2525, t=1 -> 0.2125. The v2 probe's 1-W divergent-sum was a cutoff artifact.");
}
