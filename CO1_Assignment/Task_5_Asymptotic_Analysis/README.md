
# Task 5: Asymptotic Analysis

## 1. Introduction

Asymptotic analysis describes how an algorithm's running time or operation count grows as the input size n becomes large. It allows us to compare algorithms without depending on a particular computer or programming language.

The three commonly used notations are Big O, Big Omega and Big Theta.

## 2. Big O Notation

Big O represents an asymptotic upper bound on an algorithm's growth rate.

Formally, f(n) = O(g(n)) if there exist positive constants c and n0 such that:

0 <= f(n) <= c * g(n), for all n >= n0.

Example:

Linear Search has a worst-case running time of O(n), because it may examine every element.

## 3. Big Omega Notation

Big Omega represents an asymptotic lower bound.

Formally, f(n) = Ω(g(n)) if there exist positive constants c and n0 such that:

0 <= c * g(n) <= f(n), for all n >= n0.

Example:

Linear Search has a best-case running time of Ω(1), because the target may be the first element.

## 4. Big Theta Notation

Big Theta represents a tight asymptotic bound when the function is bounded both above and below by constant multiples of the same growth function.

Formally, f(n) = Θ(g(n)) when f(n) = O(g(n)) and f(n) = Ω(g(n)).

Example:

The worst-case running time of Linear Search is Θ(n), because its operation count grows linearly with n.

## 5. Asymptotic Analysis of the Three Algorithms

### 5.1 Linear Search

- Best case: Θ(1)
- Average case: Θ(n)
- Worst case: Θ(n)

The number of comparisons increases approximately in proportion to the number of records.

### 5.2 Recursive Binary Search

- Best case: Θ(1)
- Average case: Θ(log n)
- Worst case: Θ(log n)

Binary Search requires sorted data and repeatedly reduces the search interval by half.

### 5.3 Hash Table Search

- Best case: Θ(1)
- Average expected case: Θ(1), assuming a suitable hash function and controlled load factor.
- Worst case: Θ(n), when severe collisions require examining many entries.

## 6. Growth Comparison

| Input Size (n) | Linear Search Worst-Case Comparisons | Binary Search Approximate Maximum Levels |
|---:|---:|---:|
| 1,000 | 1,000 | 10 |
| 10,000 | 10,000 | 14 |
| 100,000 | 100,000 | 17 |
| 1,000,000 | 1,000,000 | 20 |

The binary-search figures use ceil(log2(n + 1)) as an approximate maximum comparison count for an unsuccessful search in a conventional binary-search implementation.

## 7. Interpretation for Large Datasets

When the database grows from 1,000 to 1,000,000 records, Linear Search may need to inspect one million records in the worst case.

Binary Search requires only about 20 comparisons for a dataset of one million sorted records.

Hash Table Search can provide constant expected lookup time, but its performance depends on hash distribution, collision handling and load factor. The cost of building or updating the table must also be considered.

## 8. Conclusion

Asymptotic analysis shows that Binary Search and Hash Table Search can reduce the work needed for repeated lookups compared with Linear Search. The final algorithm selection must also consider preprocessing costs, record updates and experimental performance.


