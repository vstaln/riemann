// M4-proper probe: partial sums of the a2 coefficient series
//   S1(X) = sum_{m<=X} a2_0(m),  a2_0 = -(Lambda * log * log)  [coeffs of (zeta'/zeta)*zeta'^2]
//   S(X)  = sum_{m<=X} at2_0(m), at2_0 = -(Lambda * log2 * log2) [coeffs of (zeta'/zeta)*zeta''^2]
// Targets (Perron residue at s=1):
//   S1(X) ~ -X*L^4/24   (Gonek; validator E-ii CHECKED 0.556..0.595)
//   S(X)  ~ -X*L^6/180  (this note's claim)
// Build: cargo build --release --target x86_64-unknown-linux-musl --manifest-path tools/m4_proper_probe/Cargo.toml

fn sieve_lambda(n: usize) -> Vec<f64> {
    // Lambda(k) = ln p if k = p^a for prime p, else 0
    let mut is_prime = vec![true; n + 1];
    if n >= 0 { is_prime[0] = false; }
    if n >= 1 { is_prime[1] = false; }
    let mut p = 2usize;
    while p * p <= n {
        if is_prime[p] {
            let mut m = p * p;
            while m <= n { is_prime[m] = false; m += p; }
        }
        p += 1;
    }
    let mut lam = vec![0f64; n + 1];
    for p in 2..=n {
        if is_prime[p] {
            let lp = (p as f64).ln();
            let mut pk = p as usize;
            while pk <= n { lam[pk] = lp; pk = pk.saturating_mul(p); if pk == 0 { break; } }
        }
    }
    lam
}

fn main() {
    // log-prefix sums H2(z) = sum_{e<=z} (ln e)^2 ; H1(z) = sum_{e<=z} (ln e)
    let xs = [50_000usize, 100_000, 200_000];
    let n = *xs.last().unwrap();
    let mut h2 = vec![0f64; n + 1];
    let mut h1 = vec![0f64; n + 1];
    for e in 1..=n {
        let le = (e as f64).ln();
        h2[e] = h2[e - 1] + le * le;
        h1[e] = h1[e - 1] + le;
    }
    // g2(m) = sum_{d|m} (ln d)^2 (ln m/d)^2  (Dirichlet square of (ln)^2)
    // g1(m) = sum_{d|m} (ln d) (ln m/d)      (Dirichlet square of ln)
    let mut g2 = vec![0f64; n + 1];
    let mut g1 = vec![0f64; n + 1];
    for d in 1..=n {
        let ld = (d as f64).ln();
        let ld2 = ld * ld;
        let mut m = d;
        while m <= n {
            let lr = ((m / d) as f64).ln();
            g2[m] += ld2 * lr * lr;
            g1[m] += ld * lr;
            m += d;
        }
    }
    // prefix sums G2(y), G1(y)
    for i in 1..=n { g2[i] += g2[i - 1]; g1[i] += g1[i - 1]; }

    let lam = sieve_lambda(n);

    for &x in &xs {
        let lx = (x as f64).ln();
        // S1(x) = -sum_{d<=x} Lambda(d) * G1(x/d)
        let mut s1 = 0f64;
        // S(x)  = -sum_{d<=x} Lambda(d) * G2(x/d)
        let mut s = 0f64;
        for d in 1..=x {
            if lam[d] > 0.0 {
                s1 -= lam[d] * g1[x / d];
                s -= lam[d] * g2[x / d];
            }
        }
        let pred1 = -(x as f64) * lx.powi(4) / 24.0;
        let pred = -(x as f64) * lx.powi(6) / 180.0;
        println!("X={:>7}  S1={:>14.1}  -X L^4/24={:>14.1}  ratio1={:.4}   S={:>15.1}  -X L^6/180={:>15.1}  ratio={:.4}",
                 x, s1, pred1, s1 / pred1, s, pred, s / pred);
    }
}
