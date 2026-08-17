//! Cheap Rust falsification probe for the Gravity prime-resolvent premise.
//!
//! This does not test RH. It tests only whether Lambda(p)>=0 can make the
//! phase sum Re sum_{p<=X} log(p) p^(-sigma-it) nonnegative in sigma<1.
//! A negative value rejects that proposed accretivity premise; it does not
//! establish a replacement theorem.

fn primes_up_to(limit: usize) -> Vec<usize> {
    let mut composite = vec![false; limit + 1];
    let mut out = Vec::new();
    for n in 2..=limit {
        if !composite[n] {
            out.push(n);
            if n <= limit / n {
                let mut m = n * n;
                while m <= limit {
                    composite[m] = true;
                    m += n;
                }
            }
        }
    }
    out
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let limit = args.get(1).and_then(|x| x.parse().ok()).unwrap_or(50_000usize);
    let sigma = args.get(2).and_then(|x| x.parse().ok()).unwrap_or(0.75f64);
    let t_max = args.get(3).and_then(|x| x.parse().ok()).unwrap_or(1_000.0f64);
    let dt = args.get(4).and_then(|x| x.parse().ok()).unwrap_or(0.5f64);
    assert!(limit >= 2 && sigma > 0.0 && dt > 0.0 && t_max >= 0.0);

    let terms: Vec<(f64, f64)> = primes_up_to(limit)
        .into_iter()
        .map(|p| {
            let pf = p as f64;
            (pf.ln() / pf.powf(sigma), pf.ln())
        })
        .collect();

    let at_zero: f64 = terms.iter().map(|(weight, _)| *weight).sum();
    let mut min_value = f64::INFINITY;
    let mut min_t = 0.0;
    let mut max_value = f64::NEG_INFINITY;
    let mut t = 0.0;
    while t <= t_max + 0.5 * dt {
        let value: f64 = terms.iter()
            .map(|(weight, logp)| weight * (t * logp).cos())
            .sum();
        if value < min_value { min_value = value; min_t = t; }
        if value > max_value { max_value = value; }
        t += dt;
    }

    println!("GRAVITY_PRIME_PHASE");
    println!("limit={} primes={} sigma={:.6} t_max={} dt={}",
             limit, terms.len(), sigma, t_max, dt);
    println!("at_t0={:.17e}", at_zero);
    println!("min_re_sum={:.17e} at_t={:.6}", min_value, min_t);
    println!("max_re_sum={:.17e}", max_value);
    println!("verdict={}", if min_value < 0.0 {
        "PREMISE_REFUTED: Lambda>=0 does not imply phase accretivity"
    } else {
        "NOT_REFUTED_BY_THIS_GRID"
    });
}
