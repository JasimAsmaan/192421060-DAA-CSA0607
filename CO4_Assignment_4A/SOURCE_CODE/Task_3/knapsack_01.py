"""Task 3 - 0/1 Knapsack by Dynamic Programming with item reconstruction.

State: DP[i][w] = maximum value using only the first i items with capacity w.
Recurrence:
    DP[i][w] = DP[i-1][w]                                  if wt[i] > w
    DP[i][w] = max(DP[i-1][w], val[i] + DP[i-1][w-wt[i]])  otherwise
Base: DP[0][w] = 0 and DP[i][0] = 0.
"""


def knapsack(items, capacity):
    """items: list of (id, weight, value)."""
    n = len(items)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        _, wt, val = items[i - 1]
        for w in range(0, capacity + 1):
            DP[i][w] = DP[i - 1][w]                       # exclude
            if wt <= w:                                   # include is feasible
                DP[i][w] = max(DP[i][w], val + DP[i - 1][w - wt])

    # Reconstruction: walk back from DP[n][capacity]
    chosen, w = [], capacity
    for i in range(n, 0, -1):
        if DP[i][w] != DP[i - 1][w]:                      # item i was included
            chosen.append(items[i - 1][0])
            w -= items[i - 1][1]
    chosen.reverse()
    return DP[n][capacity], chosen, DP


if __name__ == "__main__":
    items = [("P", 2, 12), ("Q", 3, 20), ("R", 4, 25), ("S", 5, 30)]
    capacity = 7
    best, chosen, DP = knapsack(items, capacity)

    print("Items:", items, " Capacity:", capacity)
    print("\nDP table (rows = items considered, columns = capacity 0..%d)" % capacity)
    print("        " + " ".join(f"{w:>3}" for w in range(capacity + 1)))
    labels = ["none"] + [it[0] for it in items]
    for i, row in enumerate(DP):
        print(f"{labels[i]:>6}  " + " ".join(f"{v:>3}" for v in row))

    print("\nMaximum value :", best)
    print("Items selected:", chosen)
    tw = sum(it[1] for it in items if it[0] in chosen)
    print("Total weight  :", tw)
