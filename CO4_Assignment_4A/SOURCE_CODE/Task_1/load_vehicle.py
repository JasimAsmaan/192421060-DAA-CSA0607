"""Task 1 - Repaired LoadVehicle algorithm (Fractional Knapsack, greedy).

Greedy-choice rule: always take the package with the highest value/weight ratio.
Packages may be divided, so the last package can be taken partially.
"""


def load_vehicle(packages, capacity):
    """packages: list of (id, weight, value). Returns (total_value, loaded)."""
    # Preprocessing: compute ratio and sort descending by ratio
    items = [(pid, w, v, v / w) for pid, w, v in packages]
    items.sort(key=lambda x: x[3], reverse=True)

    remaining = capacity
    total_value = 0.0
    loaded = []  # (id, fraction, weight_taken, value_gained)

    for pid, w, v, ratio in items:
        if remaining <= 0:          # termination: vehicle full
            break
        if w <= remaining:          # package fits completely
            loaded.append((pid, 1.0, w, v))
            remaining -= w
            total_value += v
        else:                       # partial package: fill remaining capacity
            fraction = remaining / w
            loaded.append((pid, fraction, remaining, v * fraction))
            total_value += v * fraction
            remaining = 0
    return total_value, loaded, remaining


if __name__ == "__main__":
    packages = [("P1", 10, 60), ("P2", 20, 100), ("P3", 30, 120)]
    capacity = 50
    print("Packages (id, weight, value):", packages)
    print("Vehicle capacity:", capacity)
    total, loaded, left = load_vehicle(packages, capacity)
    print("\nLoaded packages:")
    for pid, frac, wt, val in loaded:
        print(f"  {pid}: fraction={frac:.2f}, weight={wt}, value={val:.2f}")
    print(f"\nTotal value = {total:.2f}")
    print(f"Unused capacity = {left}")

    # Second test: partial package needed
    packages2 = [("A", 5, 30), ("B", 4, 20), ("C", 6, 18)]
    total2, loaded2, left2 = load_vehicle(packages2, 8)
    print("\nTest 2 capacity=8:", packages2)
    for pid, frac, wt, val in loaded2:
        print(f"  {pid}: fraction={frac:.2f}, weight={wt}, value={val:.2f}")
    print(f"Total value = {total2:.2f}")
