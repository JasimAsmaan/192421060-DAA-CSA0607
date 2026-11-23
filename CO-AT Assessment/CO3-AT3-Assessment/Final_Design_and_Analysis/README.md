# Final Design and Analysis

## 1. Overview

This section presents the final design and analysis of the four divide-and-conquer algorithms implemented in the KartIQ Retail Data Analytics Platform case study.

The algorithms considered are:

1. Merge Sort
2. Quick Sort
3. Binary Search
4. Strassen Matrix Multiplication

## 2. Algorithm Comparison

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Binary Search | O(1) | O(log n) | O(log n) |
| Strassen Matrix Multiplication | O(n².807) | O(n².807) | O(n².807) |

## 3. Space Complexity

| Algorithm | Space Complexity |
|---|---|
| Merge Sort | O(n) |
| Quick Sort | O(log n) average recursion stack |
| Binary Search | O(1) iterative / O(log n) recursive |
| Strassen Matrix Multiplication | O(n²) auxiliary space |

## 4. Divide-and-Conquer Design

All four algorithms use the divide-and-conquer principle.

### Merge Sort

The array is divided into two halves, each half is sorted recursively, and the sorted halves are merged.

### Quick Sort

The array is divided using a pivot. Elements are partitioned around the pivot and the two partitions are processed recursively.

### Binary Search

The sorted search space is divided into two halves. Only the half containing the required element is searched.

### Strassen Matrix Multiplication

Matrices are divided into four submatrices. Seven recursive matrix multiplications are performed and the results are combined.

## 5. Performance Analysis

Merge Sort provides consistent O(n log n) performance.

Quick Sort provides O(n log n) average performance but can degrade to O(n²) when partitions become highly unbalanced.

Binary Search provides O(log n) searching when the input data is sorted.

Strassen's algorithm improves the asymptotic complexity of matrix multiplication compared with conventional O(n³) multiplication.

## 6. Recommendations

- Use Merge Sort when predictable sorting performance is required.
- Use Quick Sort when average-case performance and in-place processing are important.
- Use Binary Search when searching frequently in sorted data.
- Use Strassen's algorithm for sufficiently large matrix multiplication problems.

## 7. Final Conclusion

The four algorithms demonstrate different applications of the divide-and-conquer strategy.

The experimental implementations, complexity analysis and verification results show how dividing a problem into smaller subproblems can improve algorithmic efficiency.
