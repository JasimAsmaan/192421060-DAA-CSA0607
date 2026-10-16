
# Task 5: Asymptotic Analysis

## 1. Objective

To analyse the growth rate of Linear Search, Iterative Binary Search, Recursive Binary Search, and Hash Table Search using asymptotic notations and compare their theoretical performance for large student databases.

## 2. Asymptotic Notations

### Big-O Notation — O

Big-O represents an asymptotic upper bound on the growth of an algorithm.

Example:
Linear Search has worst-case time complexity O(n).

### Big-Omega Notation — Ω

Big-Omega represents an asymptotic lower bound on the growth of an algorithm.

Example:
Linear Search has best-case time complexity Ω(1).

### Big-Theta Notation — Θ

Big-Theta represents a tight asymptotic bound when upper and lower bounds have the same growth rate.

Example:
Binary Search has Θ(log n) average and worst-case time complexity.

## 3. Complexity of Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Iterative Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Recursive Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash Table Search | Expected Θ(1) | Expected Θ(1) | Θ(n) |

Hash Table Search achieves expected constant-time lookup under suitable hashing and load-factor assumptions. Its worst case is linear.

Binary Search requires sorted input. If sorting is necessary, its preprocessing cost must be included in the overall analysis.

## 4. Theoretical Growth Graph

The following graph illustrates representative growth rates for linear and logarithmic search operations. It is a theoretical illustration, not measured benchmark data.

- Linear Search: f(n) = n
- Binary Search: g(n) = log₂(n)

The graph compares growth rates rather than actual execution times.

## 5. Estimated Maximum Search Steps

For Linear Search, the worst case examines all n records.

For Binary Search, the maximum number of search levels is approximately ceil(log₂(n + 1)).

| Number of Records (n) | Linear Search Worst-Case Comparisons | Binary Search Approximate Maximum Levels |
|---:|---:|---:|
| 1,000 | 1,000 | 10 |
| 10,000 | 10,000 | 14 |
| 100,000 | 100,000 | 17 |
| 1,000,000 | 1,000,000 | 20 |

These are theoretical estimates, not experimentally measured values. Exact binary-search comparison counts depend on the implementation and search outcome.

## 6. Interpretation

Linear Search grows proportionally with the number of records. It can be effective for small or unsorted datasets but becomes expensive for large databases.

Binary Search reduces the search interval by approximately half in each iteration or recursive call. Its logarithmic growth makes it suitable for large sorted datasets.

Hash Table Search provides expected constant-time lookup when hashing distributes keys effectively. However, its construction, memory usage, collisions, and worst-case behaviour must also be considered.

## 7. Conclusion

Asymptotic analysis shows that Binary Search scales much better than Linear Search for large sorted datasets. Hash Table Search can provide expected constant-time lookup and is a strong candidate for frequent student-record queries.

The final recommendation should also consider preprocessing costs and the actual benchmark results collected in Task 9.
