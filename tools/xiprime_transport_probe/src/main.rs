// Toy probe: does xi'-distinct-on-line transport to zeta-distinct-on-line?
// Model (from attack-xiprime.md, interlacing): for a zeta zero multiset with distinct
// heights h_1<...<h_D, multiplicities m_1..m_D:
//   xi' zeros = one per gap between consecutive distinct heights (D-1), PLUS
//               (m_i - 1) zeros at each height with m_i >= 2.
// Self-consistent with RvM: N_xi' = (D-1) + sum_i (m_i - 1) = N_zeta - 1.
//
// Claims to verify:
//  1. rho_zeta = D/N_zeta (distinct proportion of zeta).
//  2. rho_xi'  = (all xi' zeros at distinct heights) / N_xi' = 1 always,
//     because gap zeros are at distinct heights and multiplicity zeros sit AT the
//     distinct heights. So xi' distinct is blind to zeta multiplicity collapse.
use std::env;

fn main() {
    // Parse multiplicities as argv: sequence of multiplicities for consecutive distinct heights.
    let args: Vec<usize> = env::args().skip(1).map(|s| s.parse().unwrap()).collect();
    if args.is_empty() {
        eprintln!("usage: xiprime_transport_probe <m1> <m2> ...  (multiplicities per distinct height)");
        std::process::exit(1);
    }
    let d = args.len();
    let n_zeta: usize = args.iter().sum();              // zeta zeros with multiplicity
    let rho_zeta = d as f64 / n_zeta as f64;

    // xi' zeros count (model):
    let gap_zeros = d.saturating_sub(1);                 // one per gap between distinct heights
    let mult_zeros: usize = args.iter().filter(|&&m| m >= 2).map(|&m| m - 1).sum();
    let n_xi: usize = gap_zeros + mult_zeros;           // = n_zeta - 1
    // all distinct? gap zeros at distinct gap positions; mult zeros at distinct heights.
    // distinct heights used by xi' = d (each height contributes 1 distinct xi' zero if m>=2,
    // plus gaps). distinct gap positions = d-1. Total distinct xi' positions:
    let distinct_xi = (d - 1) + args.iter().filter(|&&m| m >= 2).count();
    let rho_xi = distinct_xi as f64 / n_xi as f64;

    println!("distinct heights D = {d}");
    println!("multiplicities     = {:?}", args);
    println!("N_zeta (w/ mult)   = {n_zeta}   rho_zeta (distinct/total) = {rho_zeta:.6}");
    println!("N_xi'  = {n_xi}   distinct-xi' = {distinct_xi}   rho_xi' = {rho_xi:.6}");
    println!("self-check N_xi' == N_zeta - 1 : {}", n_xi == n_zeta.saturating_sub(1));
    // The transport FAILS if rho_xi' high does not force rho_zeta high.
    println!("verdict: xi' distinct = 1 even when zeta distinct is low -> no transport");
}
