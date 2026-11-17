"""Edge-case tests for Task 1."""
from load_vehicle import load_vehicle

cases = [
    ("capacity 0", [("A", 5, 10)], 0, 0.0),
    ("capacity exceeds total weight", [("A", 2, 10), ("B", 3, 15)], 100, 25.0),
    ("single item, partial", [("A", 10, 100)], 4, 40.0),
    ("classic example", [("P1", 10, 60), ("P2", 20, 100), ("P3", 30, 120)], 50, 240.0),
    ("unsorted input", [("C", 6, 18), ("A", 5, 30), ("B", 4, 20)], 8, 45.0),
]
for name, pk, cap, expected in cases:
    got = load_vehicle(pk, cap)[0]
    status = "PASS" if abs(got - expected) < 1e-9 else "FAIL"
    print(f"{status}: {name:<32} expected={expected:<7} got={got:.2f}")
    assert status == "PASS"
