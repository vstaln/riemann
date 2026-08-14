"""Barrier zoo runner: all four RH-false model worlds + the claim classifier battery.

Run:  uv run --quiet --with numpy python3 tools/barrier_zoo/run_all.py
"""
import model_dh, model_weil, model_epstein, model_beurling, classifier


def main():
    print("=" * 78)
    print("BARRIER ZOO  (rung-0 discipline tool: RH-false model worlds + claim classifier)")
    print("=" * 78)
    results = {}
    for name, mod in [('dh', model_dh), ('weil', model_weil),
                      ('epstein', model_epstein), ('planted', model_beurling)]:
        results[name] = mod.verify()
        print()
    classifier.register_facts(results)
    classifier.demo()
    print()
    print("=" * 78)
    print("MODEL STATUS TABLE")
    for k, v in results.items():
        print(f"  {k:8s}: {v['status']}")
    print()
    print("DISCIPLINE: before dispatching a research run on any claim/lever, run it through")
    print("  classifier.check_claim(text). proves_too_much=True => hypotheses over-reach a world")
    print("  that provably has off-line zeros; weaken or drop the lever.")
    print("=" * 78)


if __name__ == '__main__':
    main()
