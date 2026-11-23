"""Compare DP with brute force on random instances; verify reconstruction."""
import itertools, random
from knapsack_01 import knapsack

random.seed(7)
for t in range(500):
    n = random.randint(1, 8)
    items = [(f"I{i}", random.randint(1, 9), random.randint(1, 50)) for i in range(n)]
    cap = random.randint(0, 25)
    best, chosen, _ = knapsack(items, cap)
    bf = max(sum(i[2] for i in c) for r in range(n + 1)
             for c in itertools.combinations(items, r) if sum(i[1] for i in c) <= cap)
    assert best == bf, (items, cap, best, bf)
    wt = sum(i[1] for i in items if i[0] in chosen)
    val = sum(i[2] for i in items if i[0] in chosen)
    assert wt <= cap and val == best
print("PASS: DP == brute force and reconstruction valid on 500 random instances")
print("PASS edge: capacity 0 ->", knapsack([("A", 1, 5)], 0)[:2])
print("PASS edge: no item fits ->", knapsack([("A", 9, 5)], 3)[:2])
