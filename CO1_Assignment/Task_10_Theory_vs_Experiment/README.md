
# Task 10: Compare Theory with Experimental Behaviour

## 1. Introduction

The purpose of this task is to compare the theoretical time complexity of Linear Search, Recursive Binary Search and Hash Table Search with their experimentally measured execution times.

The theoretical analysis predicts how the number of operations grows with input size, while experimental testing measures the actual execution time on a computer.

## 2. Theoretical Expectations

### 2.1 Linear Search

Linear Search has O(n) worst-case time complexity.

As the number of student records increases, the algorithm may need to examine more records. If the target is absent, every record must be checked.

### 2.2 Recursive Binary Search

Binary Search has O(log n) worst-case time complexity when the input is sorted.

Each comparison reduces the remaining search interval by approximately half. Its performance depends on the data already being sorted.

### 2.3 Hash Table Search

Hash Table Search has O(1) expected lookup time under suitable hashing and load-factor assumptions.

In the worst case, collisions can cause O(n) search time. The time needed to build the hash table must also be considered.

## 3. Experimental Results

Insert the actual execution-time measurements obtained from Task 9.

| Dataset Size | Linear Search | Binary Search | Hash Table Search |
|---:|---|---|---|
| 1,000 | Insert measured time | Insert measured time | Insert measured time |
| 10,000 | Insert measured time | Insert measured time | Insert measured time |
| 100,000 | Insert measured time | Insert measured time | Insert measured time |
| 1,000,000 | Insert measured time | Insert measured time | Insert measured time |

Execution times should be reported in seconds and obtained under consistent test conditions.

## 4. Comparison of Theory and Experiment

### 4.1 Linear Search

The measured execution time is expected to increase as the dataset grows, particularly when searching for a record near the end or when the target is absent.

Compare the measured results with the theoretical linear growth rate.

### 4.2 Recursive Binary Search

The number of comparisons should grow logarithmically as the dataset size increases.

Compare the measured results with the theoretical O(log n) search complexity. If sorting is required, account for its preprocessing time separately.

### 4.3 Hash Table Search

The expected lookup time should remain approximately constant under suitable hashing conditions.

Compare the measured lookup times with the theoretical expected O(1) behaviour. Consider collision handling, table construction and memory usage.

## 5. Reasons for Differences

Actual execution times may differ from theoretical predictions because of:

- Processor speed and system load.
- Python interpreter overhead.
- Memory allocation and cache behaviour.
- Dataset arrangement and target position.
- Hash-table construction and collision handling.
- Measurement overhead and timing variation.

## 6. Interpretation

Use the measured results to determine whether the observed growth agrees with the theoretical analysis.

Distinguish search-only time from preprocessing time. For a fair comparison, report both where preprocessing is required.

Do not claim that an algorithm performed fastest unless the experimental measurements support that conclusion.

## 7. Conclusion

The comparison between theory and experiment helps validate the mathematical analysis of the searching algorithms. The final conclusion should be based on measured execution times, operation counts and preprocessing costs.

