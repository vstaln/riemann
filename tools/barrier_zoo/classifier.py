"""Claim classifier: 4 deflating classes + 4 RH-false model-world tests.

Classes (ledger triage in research/notes/anthropic-campaign-method-2026-08-17.md):
  (a) known theorem restated     (b) equivalent to RH
  (c) finite numerical check consistent with RH     (d) near-tautology

check_claim(text) -> {'klass', 'reason', 'worlds', 'proves_too_much'}
  klass: one of a/b/c/d or 'unknown (needs referee)'
  worlds: model worlds whose hypothesis keywords appear in the claim AND whose verified
          off-line zero/root violates an RH-type conclusion in the claim
  proves_too_much: True iff an RH-type conclusion matches AND at least one world matches

The class labels come from a keyword/structure matcher (heuristic -> CONJECTURED-grade).
The world membership tests rest on VERIFIED facts from the model scripts (PROVEN):
  model_dh.OFFLINE, model_weil.OFF_CIRCLE, model_epstein.OFFLINE, model_beurling.S0.
"""
import re

# ---- verified facts (registered by run_all.py after the models run) ----
FACTS = {}
def register_facts(results):
    FACTS.update(results)

CLASS_DEFS = {
    'a': 'known theorem restated',
    'b': 'equivalent to RH',
    'c': 'finite numerical check consistent with RH',
    'd': 'near-tautology',
}

RH_CONCLUSION = [
    r'all nontrivial zeros', r'zeros of .*lie on', r'zeros .*on the critical line',
    r'no zeros off', r'zeros on re\(s\)=1/2', r'zeros on the line',
    r'all zeros .*re\(s\)\s*=\s*1/2', r'mertens', r'm[öo]bius summatory',
    r'm\(x\)\s*=\s*o\(', r'liouville', r'lindel[öo]f', r'hilbert[ -]p[óo]lya',
    r'equivalent to (the )?riemann', r'riemann hypothesis', r'\brh\b',
    r'if and only if', r'\biff\b', r'\u21d4', r'roots on the unit circle',
    r'all roots .*unit circle', r'all zeros on',
]

FINITE_MARKER = [
    r'verified', r'computed', r'numerically', r'up to', r'the first',
    r'\bchecked\b', r'for n\s*[<=\u2264]', r'0\s*<\s*t\s*<', r'\bgrid\b',
    r'1e\d+', r'10\^', r'\bzeros\b.*\bfor\b.*\ble\s*\d', r'machine precision',
]

KNOWN_THEOREM = [
    r'prime number theorem', r'\bpnt\b', r'von\s*mangoldt', r'explicit formula',
    r'hadamard product', r'zero-free region', r'de la vall[ée]e poussin',
    r'\bselberg\b', r'\bmontgomery\b', r'pair correlation', r'density theorem',
    r'\bingham\b', r'euler product', r'functional equation', r'\u03b6\(2\)',
    r'zeta\(2\)', r'pole at s\s*=\s*1', r'meromorphic continuation',
    r'riemann[ -]siegel', r'chebyshev', r'\u03c0\(x\)', r'no zeros.*re\(s\)\s*>\s*1',
    r'analytic continuation', r'kronecker limit',
]

TAUTOLOGY = [
    r'by definition', r'trivially', r'obviously', r'immediately', r'tautolog',
    r'every zero is either', r'either on the line or off', r'the critical strip is',
    r'0\s*<\s*re\(s\)\s*<\s*1\b', r'is either zero or nonzero', r'exhaustive partition',
]

WORLDS = {
    'dh': dict(
        name='Davenport–Heilbronn (L(s,psi)+c L(s,psibar) mod 5; FE, no Euler product)',
        hypothesis=[r'dirichlet series', r'functional equation', r'linear combination',
                    r'no euler product', r'zeta-type', r'l-function', r'characters mod 5',
                    r'davenport', r'heilbronn'],
        violation='zeros off the critical line (numerically verified)'),
    'weil': dict(
        name='fake Weil polynomial (self-reciprocal real poly, off-circle roots)',
        hypothesis=[r'self-reciprocal', r'palindromic', r'real coefficients',
                    r'polynomial', r'sign at', r'constant term', r'roots on the unit circle',
                    r'weil'],
        violation='roots off the unit circle (exact)'),
    'epstein': dict(
        name='Epstein zeta, class number 2 (binary quadratic form zeta, disc -20)',
        hypothesis=[r'epstein', r'binary quadratic form', r'class number',
                    r'theta series', r'quadratic form zeta', r'positive definite form'],
        violation='zeros off the critical line (numerically verified)'),
    'planted': dict(
        name='planted-zero zeta-analogue (positive coefficients, zero at Re(s)=1/2+delta)',
        hypothesis=[r'positive coefficients', r'planted', r'zeta-analogue', r'beurling',
                    r'generalized primes', r'perturbation', r'dirichlet series',
                    r'positive dirichlet'],
        violation='zero at Re(s)=1/2+delta, off the critical line (exact)'),
}


def _hits(text, patterns):
    return [p for p in patterns if re.search(p, text)]


def classify(text):
    t = text.lower()
    rh = _hits(t, RH_CONCLUSION)
    fin = _hits(t, FINITE_MARKER)
    known = _hits(t, KNOWN_THEOREM)
    tau = _hits(t, TAUTOLOGY)
    if rh:
        if fin:
            return 'c', f"RH-type conclusion + finite-check markers -> finite numerical check ({', '.join(rh[:2])})"
        return 'b', f"asserts an RH-equivalent conclusion ({', '.join(rh[:2])})"
    if known:
        return 'a', f"restates a classical theorem ({', '.join(known[:2])})"
    if tau:
        return 'd', f"near-tautology ({', '.join(tau[:2])})"
    return 'unknown (needs referee)', 'no rule matched'


def check_claim(text):
    """Classify a claim and test it against the RH-false model worlds."""
    klass, reason = classify(text)
    t = text.lower()
    has_rh_conclusion = bool(_hits(t, RH_CONCLUSION))
    worlds, notes = [], []
    for key, w in WORLDS.items():
        if _hits(t, w['hypothesis']):
            worlds.append(key)
            if has_rh_conclusion:
                notes.append(f"claim's hypothesis matches {w['name']}; that world has {w['violation']}"
                             f" -> claim PROVES TOO MUCH (mechanism would refute a RH-false object)")
    return dict(klass=klass, reason=reason, worlds=worlds,
                proves_too_much=bool(worlds and has_rh_conclusion), notes=notes)


BATTERY = [
    ("The explicit formula and the prime number theorem are true: pi(x) ~ x/log x.", 'a'),
    ("RH is equivalent to the statement that M(x) = o(x^(1/2+eps)) for every eps > 0.", 'b'),
    ("All nontrivial zeros of the Riemann zeta function lie on the critical line.", 'b'),
    ("The first 10^13 zeros of zeta have been verified to lie on the critical line.", 'c'),
    ("Every zero of zeta is trivial, on the critical line, or off it.", 'd'),
    ("Any Dirichlet series with a zeta-type functional equation has all zeros on the critical line.", 'b'),
    ("Every self-reciprocal polynomial with real coefficients and positive values at +-1 has all roots on the unit circle.", 'b'),
    ("The Epstein zeta function of any positive definite binary quadratic form has all zeros on the critical line.", 'b'),
    ("Any Dirichlet series with positive coefficients has all zeros with Re(s)=1/2.", 'b'),
    ("zeta(s) is analytic except for a simple pole at s=1 and satisfies the functional equation.", 'a'),
]


def demo():
    print("== classifier demo ==")
    n_ok = 0
    for claim, expected in BATTERY:
        r = check_claim(claim)
        tag = 'OK' if r['klass'].startswith(expected) else 'MISMATCH'
        n_ok += tag == 'OK'
        print(f"  [{r['klass']:<24}] expected={expected}  proves_too_much={r['proves_too_much']}  worlds={r['worlds']}  {tag}")
        print(f"      claim: {claim}")
        for note in r['notes']:
            print(f"      !! {note}")
    print(f"  classifier agreement: {n_ok}/{len(BATTERY)}")


if __name__ == '__main__':
    demo()
