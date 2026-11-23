
# Task 4: Best, Average and Worst-Case Analysis

## 1. Introduction

The performance of a searching algorithm depends on the location of the target registration number, the arrangement of records and the data structure used. This task analyses the best, average and worst cases of Linear Search, Recursive Binary Search and Hash Table Search.

## 2. Linear Search

### 2.1 Best Case

The target is the first element in the array.

Number of comparisons = 1

T_best(n) = Θ(1)

### 2.2 Average Case

Assume the target is present and equally likely to be at any of the n positions.

The average number of comparisons is:

C_avg(n) = (1 + 2 + ... + n) / n

Using the sum formula:

C_avg(n) = [n(n + 1) / 2] / n

C_avg(n) = (n + 1) / 2

Therefore:

T_avg(n) = Θ(n)

### 2.3 Worst Case

The target is at the last position or is absent from the array.

Number of comparisons = n

T_worst(n) = Θ(n)

## 3. Recursive Binary Search

Assumption: The array is sorted in ascending order.

### 3.1 Best Case

The target is the middle element in the first comparison.

Number of comparisons = 1

T_best(n) = Θ(1)

### 3.2 Average Case

Each comparison reduces the search interval by approximately half. The number of levels grows logarithmically with n.

T_avg(n) = Θ(log n)

This represents the usual asymptotic average-case behaviour under a suitable distribution of successful and unsuccessful searches.

### 3.3 Worst Case

The target is absent or is found only after the maximum number of divisions.

The search interval is repeatedly halved until it becomes empty or contains one element.

T_worst(n) = Θ(log n)

## 4. Hash Table Search

Assumption: A suitable hash function is used, with a controlled load factor and separate chaining for collision handling.

### 4.1 Best Case

The target is located immediately in the expected bucket, with no additional collision checks.

T_best(n) = Θ(1)

### 4.2 Average Case

With a suitable hash function and a controlled load factor, the expected number of bucket checks remains bounded.

T_avg(n) = Θ(1) expected

### 4.3 Worst Case

Many or all registration numbers collide in the same bucket. The algorithm may have to examine every record in that bucket.

T_worst(n) = Θ(n)

## 5. Comparison Table

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Recursive Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash Table Search | Θ(1) | Θ(1) expected | Θ(n) |

## 6. Interpretation

Linear Search performs well when the target is near the beginning but may inspect every record in the worst case.

Binary Search consistently reduces the search interval, making it suitable for sorted records.

Hash Table Search provides fast expected lookups, but collisions can reduce its performance. Therefore, the hash function and collision-handling strategy are important.

## 7. Conclusion

The analysis shows that each algorithm behaves differently under varying input conditions. Linear Search has linear average and worst-case behaviour, Recursive Binary Search has logarithmic average and worst-case behaviour, and Hash Table Search has constant expected lookup time but a linear worst case.

