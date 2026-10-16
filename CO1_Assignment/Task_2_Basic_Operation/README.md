
# Task 2: Identify the Basic Operation

## 1. Introduction

The basic operation is the operation that contributes most significantly to the execution time of an algorithm. Identifying it helps us analyse how an algorithm behaves as the input size increases.

In this assignment, the basic operations of Linear Search, Recursive Binary Search and Hash Table Search are identified.

## 2. Linear Search

### 2.1 Basic Operation

The basic operation is the comparison between the current array element and the target registration number.

### 2.2 Location in the Algorithm

The comparison occurs inside the loop:

    IF A[i] == key

### 2.3 Why It Is Important

Linear Search examines elements one by one. The number of comparisons depends on the position of the target or whether the target exists.

### 2.4 Operation Count

- Best case: 1 comparison.
- Average case: Approximately n/2 comparisons for a successful search with an equally likely target position.
- Worst case: n comparisons.

Therefore, the worst-case time complexity is O(n).

## 3. Recursive Binary Search

### 3.1 Basic Operation

The basic operation is the comparison between the target registration number and the middle element of the sorted array.

### 3.2 Location in the Algorithm

The comparison occurs when checking:

    A[mid] == key

The algorithm then compares the target with the middle element to determine which half should be searched.

### 3.3 Why It Is Important

Binary Search eliminates approximately half of the remaining search elements during each recursive call.

### 3.4 Operation Count

For a sorted array, the search interval is reduced approximately as follows:

    n, n/2, n/4, n/8, ...

After k divisions:

    n / 2^k = 1

Therefore:

    2^k = n
    k = log2(n)

The worst-case time complexity is O(log n).

## 4. Hash Table Search

### 4.1 Basic Operation

The basic operations are calculating the hash value and checking the relevant hash-table bucket for the target registration number.

### 4.2 Location in the Algorithm

The operations occur when calculating:

    index = HashFunction(key)

The algorithm then examines the corresponding bucket to locate the required record.

### 4.3 Why It Is Important

Hashing maps a registration number to a table location, avoiding a sequential scan of all records in the average case.

### 4.4 Operation Count

- Average case: A constant expected number of operations, assuming a suitable hash function and controlled load factor.
- Worst case: Up to O(n) operations if many keys collide in the same bucket.

Building the hash table also requires preprocessing time, typically O(n) expected time for n records.

## 5. Comparison of Basic Operations

| Algorithm | Basic Operation | Average Search Complexity | Worst-Case Complexity |
|---|---|---|---|
| Linear Search | Element-key comparison | O(n) | O(n) |
| Recursive Binary Search | Middle-element comparison | O(log n) | O(log n) |
| Hash Table Search | Hash calculation and bucket checks | O(1) expected | O(n) |

## 6. Conclusion

The basic operation differs across the three searching strategies. Linear Search depends on sequential comparisons, Binary Search reduces the search interval by half, and Hash Table Search uses hashing to locate a relevant bucket. These operation counts form the basis for the mathematical complexity analysis in Task 3.
