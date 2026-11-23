
# Task 8: Implementation and Testing

## 1. Introduction

This task implements and tests three different searching strategies:

1. Linear Search
2. Recursive Binary Search
3. Hash Table Search

All algorithms will be tested using datasets of increasing sizes to verify their correctness and evaluate their performance.

## 2. Programming Language and Environment

- Programming language: Python 3
- Development environment: VS Code
- Dataset sizes: 1,000, 10,000, 100,000 and 1,000,000 records
- Performance measures: Execution time and number of comparisons

## 3. Test Dataset

Registration numbers are represented by unique integers.

For each dataset size n, the records contain values from 1 to n.

For a fair comparison, the algorithms use equivalent datasets and the same target values.

## 4. Test Cases

| Test Case | Description | Expected Result |
|---|---|---|
| TC01 | Target is the first record | Record found |
| TC02 | Target is a middle record | Record found |
| TC03 | Target is the last record | Record found |
| TC04 | Target is absent | Record not found |
| TC05 | Dataset contains one record | Correct result |
| TC06 | Dataset contains one million records | Correct result |

## 5. Implementation Plan

### 5.1 Linear Search

The program compares the target with each record until it finds a match or reaches the end of the dataset.

### 5.2 Recursive Binary Search

The program searches a sorted list by repeatedly dividing the search interval into halves.

### 5.3 Hash Table Search

The program stores registration numbers in a Python set or dictionary and uses membership lookup to check whether a target exists.

A Python set provides hash-based membership testing. Its expected lookup time is constant under normal hashing assumptions, although worst-case behaviour can be linear.

## 6. Correctness Validation

Each algorithm must return the correct result for successful and unsuccessful searches.

The test program should compare the results of all three algorithms against the expected answer.

## 7. Performance Measurement

Use Python's time.perf_counter() to measure execution time.

Run the same test cases multiple times and record the average time where appropriate.

Record the number of comparisons for Linear Search and Binary Search. For Hash Table Search, record execution time and document the limitations of counting internal operations in Python.

## 8. Reproducibility

Use the same generated registration numbers, target values and testing environment for all algorithms.

Record the Python version, dataset size and test conditions so that the experiment can be repeated.

## 9. Conclusion

The implementations and test cases provide a basis for evaluating the correctness and efficiency of the searching algorithms. Actual execution times and comparison counts will be documented in Task 9.

