
# Task 3: Derive the Time-Complexity Function Mathematically

## 1. Introduction

Time complexity describes how the number of operations performed by an algorithm changes as the input size n increases.

This task derives the time complexity of Linear Search, Recursive Binary Search and Hash Table Search, including preprocessing costs where applicable.

## 2. Linear Search

### 2.1 Input Size

Let n represent the number of student registration numbers in the array.

### 2.2 Mathematical Derivation

In the worst case, Linear Search compares the target with every element.

The number of comparisons is:

C(n) = n

Assuming each comparison takes constant time c, the running time can be expressed as:

T(n) = an + b

where a and b represent constant costs associated with comparisons and other operations.

Therefore:

T(n) = Θ(n)

### 2.3 Preprocessing Cost

Linear Search does not require sorting. If the array is already available, its search cost is Θ(n) in the worst case.

If reading or creating the dataset is included, the cost of processing n records must also be considered.

## 3. Recursive Binary Search

### 3.1 Input Size

Let n be the number of elements in a sorted array.

### 3.2 Mathematical Derivation

Each comparison eliminates approximately half of the remaining search interval.

The recurrence relation is:

T(n) = T(n/2) + c, for n > 1

T(1) = c0

After k recursive divisions, the remaining interval is approximately:

n / 2^k = 1

Rearranging:

2^k = n

Taking logarithms:

k = log2(n)

Since each level performs constant work, the total running time is:

T(n) = Θ(log n)

### 3.3 Preprocessing Cost

Binary Search requires sorted data.

If the records must be sorted first using a comparison-based sorting algorithm such as Merge Sort, the preprocessing cost is Θ(n log n).

The total cost for sorting once and performing one search is:

T_total(n) = Θ(n log n) + Θ(log n)

Therefore:

T_total(n) = Θ(n log n)

If the data is already sorted, the search itself takes Θ(log n).

## 4. Hash Table Search

### 4.1 Input Size

Let n represent the number of student records stored in the hash table.

### 4.2 Mathematical Derivation

A hash function maps a registration number to a table index. With a suitable hash function and controlled load factor, the expected number of bucket checks remains bounded.

Therefore, the expected search time is:

T_search(n) = Θ(1)

However, in the worst case, all records may collide in the same bucket. Searching that bucket can require up to n comparisons:

T_worst(n) = Θ(n)

### 4.3 Preprocessing Cost

Building a hash table containing n records generally takes Θ(n) expected time when insertion operations have constant expected cost.

The total expected cost of building the table and performing one search is:

T_total(n) = Θ(n) + Θ(1)

Therefore:

T_total(n) = Θ(n)

This construction cost can be shared across many searches while the table remains available.

## 5. Mathematical Comparison

| Algorithm | Search Cost | Preprocessing Cost | Total Cost for One Search |
|---|---|---|---|
| Linear Search | Θ(n) worst case | None required | Θ(n) |
| Recursive Binary Search | Θ(log n) | Θ(n log n) if sorting is required | Θ(n log n) if sorting first |
| Hash Table Search | Θ(1) expected | Θ(n) expected to build | Θ(n) expected including construction |

## 6. Interpretation

Linear Search has a search cost that grows proportionally with the number of records.

Binary Search requires fewer comparisons as the dataset grows, but its records must be sorted.

Hash Table Search offers constant expected lookup time after construction, although collisions can cause its worst-case search time to become linear.

For a database with repeated searches, preprocessing costs should be evaluated across the expected number of searches rather than considering only one lookup.

## 7. Conclusion

The mathematical derivations show that Linear Search has Θ(n) worst-case complexity, Recursive Binary Search has Θ(log n) search complexity on sorted data, and Hash Table Search has Θ(1) expected lookup complexity under suitable assumptions. These results will be compared with experimental measurements in the following tasks.


