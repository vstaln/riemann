// Dirichlet characters mod q for small q, via the CRT structure theorem:
//   (Z/qZ)*  =  prod_{p^e || q} (Z/p^e Z)*
// with (Z/p^e Z)* cyclic for odd p (primitive root g), and (Z/2^e Z)* = C2 x C_{2^{e-2}}
// for e >= 3 (generators -1 and 5), C2 for e=2, trivial for e=1.
// A character is a table: value chi[a] for a = 0..q-1, stored as complex f64.

#[derive(Clone)]
pub struct Character {
    pub q: u32,
    pub table: Vec<(f64, f64)>, // chi[a] for a = 0..q-1
    pub conductor: u32,
    pub even: bool,
    pub gauss_sum: (f64, f64), // tau(chi) = sum_a chi(a) e^{2pi i a/q}
    pub order: u32,
}

fn gcd(a: u32, b: u32) -> u32 {
    let (mut a, mut b) = (a, b);
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn pow_mod(a: u32, e: u32, m: u32) -> u32 {
    let mut r = 1u64 % m as u64;
    let mut b = (a % m) as u64;
    let mut e = e;
    while e > 0 {
        if e & 1 == 1 {
            r = (r * b) % m as u64;
        }
        b = (b * b) % m as u64;
        e >>= 1;
    }
    r as u32
}

pub fn euler_phi(q: u32) -> u32 {
    let mut n = q;
    let mut r = q as f64;
    let mut p = 2u32;
    while p * p <= n {
        if n % p == 0 {
            while n % p == 0 {
                n /= p;
            }
            r *= 1.0 - 1.0 / p as f64;
        }
        p += 1;
    }
    if n > 1 {
        r *= 1.0 - 1.0 / n as f64;
    }
    r.round() as u32
}

fn factor(q: u32) -> Vec<(u32, u32)> {
    let mut n = q;
    let mut out = Vec::new();
    let mut p = 2u32;
    while p * p <= n {
        if n % p == 0 {
            let mut e = 0;
            while n % p == 0 {
                n /= p;
                e += 1;
            }
            out.push((p, e));
        }
        p += 1;
    }
    if n > 1 {
        out.push((n, 1));
    }
    out
}

fn is_primitive_root(g: u32, p: u32) -> bool {
    // g mod p, p odd prime: order p-1
    let order = p - 1;
    let mut m = order;
    let mut d = 2u32;
    while d * d <= m {
        if m % d == 0 {
            if pow_mod(g, order / d, p) == 1 {
                return false;
            }
            while m % d == 0 {
                m /= d;
            }
        }
        d += 1;
    }
    if m > 1 && pow_mod(g, order / m, p) == 1 {
        return false;
    }
    true
}

/// Generators for (Z/p^e Z)*: (generator, order). For odd p: single primitive root.
/// For 2^e: e=1 -> none; e=2 -> (3, 2); e>=3 -> (-1, 2), (5, 2^{e-2}).
fn pp_generators(p: u32, e: u32) -> Vec<(u32, u32)> {
    let pe = p.pow(e);
    if p == 2 {
        return match e {
            1 => vec![],
            2 => vec![(3u32, 2u32)],
            _ => {
                let mut gs = vec![(pe - 1, 2u32)];
                // 5 has order 2^{e-2} mod 2^e
                let o = 1u32 << (e - 2);
                gs.push((5u32, o));
                gs
            }
        };
    }
    // find primitive root mod p, lift to p^e
    let mut g = 2u32;
    while !is_primitive_root(g, p) {
        g += 1;
    }
    if pow_mod(g, p - 1, p * p) == 1 {
        g += p;
    }
    vec![(g, euler_phi(pe))]
}

/// Discrete log: find the exponent vector of a mod p^e w.r.t. the generators (brute force).
fn pp_exponents(a: u32, p: u32, e: u32, gens: &[(u32, u32)]) -> Vec<u32> {
    let pe = p.pow(e);
    let mut exps = vec![0u32; gens.len()];
    // try all tuples in lexicographic order
    loop {
        let mut prod = 1u32;
        for (g, ord) in gens.iter().zip(exps.iter()) {
            prod = pow_mod(prod * pow_mod(g.0, *ord, pe) % pe, 1, pe);
        }
        if prod == a {
            return exps;
        }
        let mut i = 0usize;
        loop {
            exps[i] += 1;
            if exps[i] < gens[i].1 {
                break;
            }
            exps[i] = 0;
            i += 1;
            if i == gens.len() {
                panic!("no exponents for a={} mod p^e={}^{}", a, p, e);
            }
        }
    }
}

/// All characters mod q. Each character = choice of root of unity per generator.
struct Pp {
    p: u32,
    e: u32,
    pe: u32,
    gens: Vec<(u32, u32)>, // (generator, order)
}

pub fn all_characters(q: u32) -> Vec<Character> {
    let fac = factor(q);
    let pps: Vec<Pp> = fac
        .iter()
        .map(|&(p, e)| Pp {
            p,
            e,
            pe: p.pow(e),
            gens: pp_generators(p, e),
        })
        .collect();
    // total number of characters = phi(q) = product of orders
    let nchars: u32 = pps.iter().map(|pp| pp.gens.iter().map(|&(_, o)| o).product::<u32>()).product();
    let two_pi = std::f64::consts::TAU;
    let mut chars = Vec::new();
    // k-vector over all generators (flattened)
    let mut k: Vec<u32> = vec![0; pps.iter().map(|pp| pp.gens.len()).sum()];
    let total_gen: usize = k.len();
    let mut done = false;
    while !done {
        // Build the table: for each unit b mod q, compute chi(b) directly.
        let mut table = vec![(0.0f64, 0.0f64); q as usize];
        for b in 1..q {
            if gcd(b, q) != 1 {
                continue;
            }
            let mut arg = 0.0f64;
            let mut gi = 0usize;
            for pp in &pps {
                let a_mod = b % pp.pe;
                let exps = pp_exponents(a_mod, pp.p, pp.e, &pp.gens);
                for (j, (_, o)) in pp.gens.iter().enumerate() {
                    arg += two_pi * k[gi + j] as f64 * exps[j] as f64 / *o as f64;
                }
                gi += pp.gens.len();
            }
            table[b as usize] = (arg.cos(), arg.sin());
        }
        // conductor
        let mut conductor = q;
        for d in 1..=q {
            if q % d != 0 {
                continue;
            }
            let mut ok = true;
            'chk: for b in 1..q {
                if gcd(b, q) != 1 {
                    continue;
                }
                if gcd(b, d) > 1 {
                    if table[b as usize].0.abs() > 1e-9 || table[b as usize].1.abs() > 1e-9 {
                        ok = false;
                        break 'chk;
                    }
                    continue;
                }
                // find b2 = b mod d lifted to a unit mod q
                let b2 = (1..q).find(|&x| x % d == b % d && gcd(x, q) == 1).unwrap();
                let (r1, i1) = table[b as usize];
                let (r2, i2) = table[b2 as usize];
                if (r1 - r2).abs() > 1e-9 || (i1 - i2).abs() > 1e-9 {
                    ok = false;
                    break 'chk;
                }
            }
            if ok {
                conductor = d;
                break;
            }
        }
        let even = table[(q - 1) as usize].0 > 0.999999 && table[(q - 1) as usize].1.abs() < 1e-9;
        // gauss sum
        let mut gs = (0.0f64, 0.0f64);
        for a in 1..q {
            let (cr, ci) = table[a as usize];
            let ang = two_pi * a as f64 / q as f64;
            gs.0 += cr * ang.cos() - ci * ang.sin();
            gs.1 += cr * ang.sin() + ci * ang.cos();
        }
        // order: lcm of the k_i parts where nonzero... order = min n with chi^n = 1:
        // computed as the order of the character = lcm over generators of o_j/gcd(k_j, o_j)
        let mut order = 1u32;
        let mut gi = 0usize;
        for pp in &pps {
            for (j, (_, o)) in pp.gens.iter().enumerate() {
                let kj = k[gi + j];
                let part = if kj == 0 { 1 } else { o / gcd(kj, *o) };
                order = order / gcd(order, part) * part;
            }
            gi += pp.gens.len();
        }
        chars.push(Character {
            q,
            table,
            conductor,
            even,
            gauss_sum: gs,
            order,
        });
        // increment mixed radix
        let mut i = 0usize;
        loop {
            k[i] += 1;
            if k[i] < order_limits(&pps, i) {
                break;
            }
            k[i] = 0;
            i += 1;
            if i == total_gen {
                done = true;
                break;
            }
        }
    }
    assert_eq!(chars.len() as u32, nchars, "character count mismatch for q={}", q);
    chars
}

fn order_limits(pps: &[Pp], idx: usize) -> u32 {
    let mut gi = 0usize;
    for pp in pps {
        for (_, o) in &pp.gens {
            if gi == idx {
                return *o;
            }
            gi += 1;
        }
    }
    unreachable!()
}

/// Primitive even characters mod q (excludes the principal character, conductor 1).
pub fn primitive_even(q: u32) -> Vec<Character> {
    all_characters(q)
        .into_iter()
        .filter(|c| c.conductor == q && c.even)
        .collect()
}

/// All even characters mod q (including imprimitive and principal).
pub fn all_even(q: u32) -> Vec<Character> {
    all_characters(q)
        .into_iter()
        .filter(|c| c.even)
        .collect()
}

fn modinv(a: u64, m: u64) -> u64 {
    // m prime power, a coprime to m; extended euclid
    let (mut t, mut newt) = (0i64, 1i64);
    let (mut r, mut newr) = (m as i64, a as i64);
    while newr != 0 {
        let q = r / newr;
        let tmp = t - q * newt;
        t = newt;
        newt = tmp;
        let tmp2 = r - q * newr;
        r = newr;
        newr = tmp2;
    }
    ((t % m as i64 + m as i64) % m as i64) as u64
}

impl Character {
    /// chi(n) for arbitrary n.
    pub fn value(&self, n: u64) -> (f64, f64) {
        let r = (n % self.q as u64) as usize;
        self.table[r]
    }
}

// ---------------------------------------------------------------------------
// Direct construction for prime moduli (large q).
// For q prime, every non-principal character is primitive, and the even ones
// are exactly those with even exponent k in chi_k(g^a) = exp(2 pi i k a/(q-1)),
// since chi(-1) = chi(g^{(q-1)/2}) = (-1)^k. This lets us build a single
// character's table in O(q) (after an O(q^2) one-time index table), avoiding
// the full phi(q)-character enumeration whose memory cost is prohibitive at
// q ~ 1e3-1e4. All characters below have conductor q (they are primitive).
// ---------------------------------------------------------------------------

/// Smallest primitive root mod the odd prime q.
pub fn primitive_root_prime(q: u32) -> u32 {
    // distinct prime factors of q-1
    let mut n = q - 1;
    let mut fac = Vec::new();
    let mut p = 2u32;
    while p * p <= n {
        if n % p == 0 {
            fac.push(p);
            while n % p == 0 {
                n /= p;
            }
        }
        p += 1;
    }
    if n > 1 {
        fac.push(n);
    }
    let mut g = 2u32;
    loop {
        if fac.iter().all(|&p| pow_mod(g, (q - 1) / p, q) != 1) {
            return g;
        }
        g += 1;
    }
}

/// index table: idx[n] = j with g^j = n (mod q), for n = 1..q-1.
pub fn index_table_prime(q: u32, g: u32) -> Vec<u32> {
    let mut idx = vec![0u32; q as usize];
    let mut cur = 1u32;
    for j in 0..(q - 1) {
        idx[cur as usize] = j;
        cur = (cur as u64 * g as u64 % q as u64) as u32;
    }
    idx
}

/// The character chi_k(g^a) = exp(2 pi i k a/(q-1)) for the odd prime q.
/// k must satisfy 0 < k < q-1 (primitive); even k gives chi(-1) = 1.
pub fn character_prime(q: u32, g: u32, idx: &[u32], k: u32) -> Character {
    let two_pi = std::f64::consts::TAU;
    let mut table = vec![(0.0f64, 0.0f64); q as usize];
    for a in 1..q {
        let j = idx[a as usize];
        let arg = two_pi * k as f64 * j as f64 / (q - 1) as f64;
        table[a as usize] = (arg.cos(), arg.sin());
    }
    // gauss sum
    let mut gs = (0.0f64, 0.0f64);
    for a in 1..q {
        let (cr, ci) = table[a as usize];
        let ang = two_pi * a as f64 / q as f64;
        gs.0 += cr * ang.cos() - ci * ang.sin();
        gs.1 += cr * ang.sin() + ci * ang.cos();
    }
    let order = (q - 1) / gcd(k, q - 1);
    Character {
        q,
        table,
        conductor: q,
        even: k % 2 == 0,
        gauss_sum: gs,
        order,
    }
}

/// ALL characters mod the odd prime q via direct construction (k = 0..q-2).
/// Used for the exact orthogonality experiment at large q, where the CRT
/// enumeration's brute-force discrete log is too slow. O(q^2) total.
pub fn all_prime_chars(q: u32) -> Vec<(u32, Character)> {
    let g = primitive_root_prime(q);
    let idx = index_table_prime(q, g);
    (0..(q - 1)).map(|k| (k, character_prime(q, g, &idx, k))).collect()
}

/// Deterministic sample of `s` distinct even characters mod the odd prime q:
/// k = 2 and s-1 evenly spread even exponents. Returns (k, character) pairs;
/// all have conductor q.
pub fn sample_even_prime(q: u32, s: usize) -> Vec<(u32, Character)> {
    let g = primitive_root_prime(q);
    let idx = index_table_prime(q, g);
    let avail = (q - 3) / 2; // even k in [2, q-3]
    let mut ks = vec![2u32];
    if s > 1 {
        let step = (avail / (s as u32 - 1)).max(1);
        let mut k = 2u32;
        for _ in 1..s {
            k = (k + 2 * step).min(q - 3);
            if !ks.contains(&k) {
                ks.push(k);
            }
        }
    }
    ks.into_iter().map(|k| (k, character_prime(q, g, &idx, k))).collect()
}
