# Testing Guide

## 1. Objective

The objective of testing is to verify the correctness and performance of different searching algorithms used in a student record system.

## 2. Algorithms Tested

1. Linear Search
2. Iterative Binary Search
3. Recursive Binary Search
4. Hash Table Search

## 3. Testing Environment

- Programming Language: Python
- Testing Tool: Python interpreter
- Data Type: Student registration numbers
- Dataset Sizes: 1,000, 10,000, 100,000 and 1,000,000 records
- Performance Metric: Execution time in microseconds

## 4. Test Cases

| Test Case | Input Condition | Expected Result |
|---|---|---|
| TC01 | Search for the first record | Record found |
| TC02 | Search for a middle record | Record found |
| TC03 | Search for the last record | Record found |
| TC04 | Search for a missing record | Record not found |
| TC05 | Search an empty dataset | Record not found |
| TC06 | Search with one record | Correct result |
| TC07 | Search using a large dataset | Correct result |
| TC08 | Enter an invalid dataset size | Appropriate validation message |

## 5. Testing Procedure

1. Prepare student registration numbers.
2. Ensure the array is sorted before binary search.
3. Build the hash table before measuring lookup time.
4. Search for existing and missing registration numbers.
5. Compare the results returned by each algorithm.
6. Measure execution time using Python's time.perf_counter().
7. Repeat measurements to reduce timing variation.
8. Record the measured results in a table.
9. Test dataset sizes of 1,000, 10,000, 100,000 and 1,000,000 records.

## 6. Correctness Validation

All algorithms should return the correct record position or indicate that the record was not found. Binary search must use sorted input. Hash Table Search must use a consistent registration-number key.

## 7. Performance Analysis

Linear Search has O(n) worst-case lookup time. Binary Search has O(log n) worst-case lookup time. Hash Table Search has expected O(1) lookup time under suitable hashing assumptions, with O(n) worst-case lookup time.

## 8. Results

Enter actual execution times and test outcomes after running the programs. Do not use estimated values as measured experimental results.

| Dataset Size | Linear Search | Iterative Binary Search | Recursive Binary Search | Hash Table Search |
|---:|---|---|---|---|
| 1,000 | To be measured | To be measured | To be measured | To be measured |
| 10,000 | To be measured | To be measured | To be measured | To be measured |
| 100,000 | To be measured | To be measured | To be measured | To be measured |
| 1,000,000 | To be measured | To be measured | To be measured | To be measured |

## 9. Conclusion

Testing verifies algorithm correctness and helps compare practical performance with theoretical time complexity. The final recommendation should be based on the workload, preprocessing requirements, and actual experimental results.
