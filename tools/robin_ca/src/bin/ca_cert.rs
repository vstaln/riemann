// Robin 1984 (JMPA 63) certificate probe: RH <=> sigma(n) < e^gamma * n * ln ln n for all n >= 5041.
// Any violation must occur at a colossally abundant number [PROVEN, Robin 1984]; every CA
// number is superabundant [PROVEN]. We enumerate a SUPERSET of SA/CA candidates (all
// non-increasing exponent patterns, n <= 10^60) and certify R(n)=sigma(n)/(e^g n ln ln n) < 1.
// HONEST SCOPE: passing certifies "no violation among tested candidates <= 10^60"
// [CHECKED NUMERICALLY] only — NOT full Robin coverage. Finite-check => RH is [CONJECTURED].
const LIMIT_LN: f64 = 60.0 * std::f64::consts::LN_10; // n <= 10^60, log space
const GAMMA: f64 = 0.5772156649015328606;

fn sieve(limit: usize) -> Vec<u64> {
    let mut isp = vec![true; limit + 1];
    let mut ps = Vec::new();
    for i in 2..=limit {
        if isp[i] {
            ps.push(i as u64);
            let mut j = i * i;
            while j <= limit {
                isp[j] = false;
                j += i;
            }
        }
    }
    ps
}

// log(sigma(n)/n) from factorization, stable form: sum [ln(1-p^-(a+1)) - ln(1-p^-1)]
fn log_sigma_ratio(fac: &[(usize, u32)], lnp: &[f64]) -> f64 {
    fac.iter().map(|&(i, a)| {
        (1.0f64 - (-((a + 1) as f64) * lnp[i]).exp()).ln() - (1.0f64 - (-lnp[i]).exp()).ln()
    }).sum()
}

struct State {
    total: u64,
    max_r: f64,
    argmax: Vec<(usize, u32)>,
    argmax_logn: f64,
    violations: u64,
}

fn main() {
    let primes = sieve(200);
    let lnp: Vec<f64> = primes.iter().map(|&p| (p as f64).ln()).collect();
    let nmin_ln = 5041f64.ln();

    fn rec(
        idx: usize, prev_a: u32, logn: &mut f64, lratio: &mut f64, lnp: &[f64],
        fac: &mut Vec<(usize, u32)>, st: &mut State,
    ) {
        let nmin = 5041f64.ln();
        if !fac.is_empty() && *logn >= nmin {
            st.total += 1;
            // R = sigma/(e^gamma * n * ln ln n) => log R = lratio - gamma - ln(ln ln n)
            let r = (*lratio - GAMMA - logn.ln().ln()).exp();
            let err_l = ((fac.len() + 3) as f64) * 4.0 * f64::EPSILON;
            let err = r * (err_l + err_l / (logn.ln() * logn.ln().ln()));
            if r > st.max_r {
                st.max_r = r;
                st.argmax = fac.clone();
                st.argmax_logn = *logn;
            }
            if r - err >= 1.0 {
                st.violations += 1;
            }
        }
        if idx >= lnp.len() { return; }
        let lp = lnp[idx];
        let max_a = (((LIMIT_LN - *logn) / lp).floor() as u32).min(prev_a);
        for a in (1..=max_a).rev() {
            let term = (1.0f64 - (-((a + 1) as f64) * lp).exp()).ln()
                - (1.0f64 - (-lp).exp()).ln();
            *logn += a as f64 * lp;
            *lratio += term;
            fac.push((idx, a));
            rec(idx + 1, a, logn, lratio, lnp, fac, st);
            fac.pop();
            *logn -= a as f64 * lp;
            *lratio -= term;
        }
    }
    let _ = nmin_ln;

    let mut st = State { total: 0, max_r: 0.0, argmax: Vec::new(), argmax_logn: 0.0, violations: 0 };
    let mut logn = 0.0f64;
    let mut lratio = 0.0f64;
    let mut fac: Vec<(usize, u32)> = Vec::new();
    rec(0, u32::MAX, &mut logn, &mut lratio, &lnp, &mut fac, &mut st);

    println!("candidates_enumerated {}", st.total);
    println!("max_R {:.17e}", st.max_r);
    println!("argmax_n ~ 10^{:.4}", st.argmax_logn / std::f64::consts::LN_10);
    let facs: String = st.argmax.iter().map(|&(i, a)| format!("{}^{}", primes[i], a)).collect::<Vec<_>>().join("*");
    println!("argmax_factorization {}", facs);

    // CONTROL: bump largest-prime exponent by +1; R must respond (increase)
    if !st.argmax.is_empty() {
        let mut fac2 = st.argmax.clone();
        let li = fac2.last().unwrap().0;
        fac2.last_mut().unwrap().1 += 1;
        let logn2 = st.argmax_logn + lnp[li];
        let r2 = (log_sigma_ratio(&fac2, &lnp) - GAMMA - logn2.ln().ln()).exp();
        println!("control_perturbed_R {:.17e}", r2);
        // At a genuine R-maximum a single-exponent bump may DECREASE R; the sound
        // requirement is that R responds measurably (|delta| >> error bound), not that it rises.
        let delta = (r2 - st.max_r).abs();
        println!("control_delta {:.3e} control_responds {}", delta, delta > 1e-9);
    }

    if st.violations > 0 {
        println!("ESCALATE {} candidate(s) with R >= 1 within error bound", st.violations);
    } else {
        println!("no_violation all tested candidates have R(n) < 1");
    }
    println!("verdict coverage=tested-candidates-only<=10^60 [CHECKED NUMERICALLY]; reduction-to-CA=Robin1984-JMPA63 [PROVEN]; finite-checks-imply-RH [CONJECTURED]");
}
