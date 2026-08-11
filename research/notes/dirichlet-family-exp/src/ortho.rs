// Prime-side experiment: the family-averaged second moment of the prime sums
// P_{X,chi}(tau) = -(1/pi) sum_{n<=X} Lambda(n) chi(n) n^{-1/2} cos(tau log n).
// The paper's Prop 5.6 splits M[P_X,P_X] into a diagonal (n=m) and an off-diagonal
// O_1 (n != m). For a SINGLE character O_1 is controlled by Montgomery–Vaughan only
// when X <= T^{1-eps}; the family average over chi mod q kills O_1 by orthogonality
// for X < q. We measure this directly.

use crate::characters::Character;

fn gcd(a: u32, b: u32) -> u32 {
    let (mut a, mut b) = (a, b);
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

/// Prime powers up to X with their Lambda(n) values.
fn prime_powers(x: f64) -> Vec<(f64, f64)> {
    let lim = x.ceil() as usize;
    let mut is_prime = vec![true; lim + 1];
    if lim >= 0 {
        is_prime[0] = false;
    }
    if lim >= 1 {
        is_prime[1] = false;
    }
    let mut p = 2usize;
    while p * p <= lim {
        if is_prime[p] {
            let mut m = p * p;
            while m <= lim {
                is_prime[m] = false;
                m += p;
            }
        }
        p += 1;
    }
    let mut out = Vec::new();
    for p in 2..=lim {
        if !is_prime[p] {
            continue;
        }
        let lp = (p as f64).ln();
        let mut pk = p as f64;
        while pk <= x {
            out.push((pk, lp));
            pk *= p as f64;
        }
    }
    out
}

/// Diagonal: sum_{n<=X, (n,q)=1} Lambda(n)^2 / n.
pub fn q_diag(x: f64, q: u32) -> f64 {
    let mut s = 0.0;
    for (n, lam) in prime_powers(x) {
        if gcd(n as u32, q) != 1 {
            continue;
        }
        s += lam * lam / n;
    }
    s
}

/// Single character second moment: |sum_{n<=X} Lambda(n) chi(n) n^{-1/2-i tau}|^2.
pub fn q_single(x: f64, tau: f64, chi: &Character) -> f64 {
    let mut re = 0.0;
    let mut im = 0.0;
    for (n, lam) in prime_powers(x) {
        let (cr, ci) = chi.value(n as u64);
        if cr == 0.0 && ci == 0.0 {
            continue;
        }
        // chi(n) n^{-1/2} e^{-i tau ln n}
        let mag = lam / n.sqrt();
        let (s, c) = (tau * n.ln()).sin_cos();
        // chi * (c - i s)
        re += mag * (cr * c - ci * (-s));
        im += mag * (cr * (-s) + ci * c);
    }
    re * re + im * im
}

/// Family-averaged second moment over a list of characters:
/// (1/|F|) sum_chi |sum_n Lambda(n) chi(n) n^{-1/2-i tau}|^2.
pub fn q_family(x: f64, tau: f64, chars: &[Character]) -> f64 {
    let mut s = 0.0;
    for chi in chars {
        s += q_single(x, tau, chi);
    }
    s / chars.len() as f64
}

/// Exact character orthogonality over the given family: (1/|F|) sum_chi chi(n) conj(chi(m)).
pub fn orthogonality(n: u32, m: u32, chars: &[Character]) -> f64 {
    let mut s = 0.0;
    for chi in chars {
        let (cn, sn) = chi.value(n as u64);
        let (cm, sm) = chi.value(m as u64);
        // chi(n) * conj(chi(m))
        s += cn * cm + sn * sm;
    }
    s / chars.len() as f64
}

/// How many characters in the family are nonzero at n (i.e. (n, q) = 1).
pub fn support_fraction(n: u32, chars: &[Character]) -> f64 {
    let mut c = 0;
    for chi in chars {
        let (r, i) = chi.value(n as u64);
        if r != 0.0 || i != 0.0 {
            c += 1;
        }
    }
    c as f64 / chars.len() as f64
}
