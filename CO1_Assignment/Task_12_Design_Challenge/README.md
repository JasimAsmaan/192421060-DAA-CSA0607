
# Task 12: Re-evaluate and Adapt the Design

## 1. Introduction

The university has changed its requirements. The database now contains 1,000,000 student records and must process 50,000 search requests per hour. New student records are added only once per day.

This task evaluates whether the original searching strategy should be retained, modified or redesigned.

## 2. A. Impact Analysis

### 2.1 Changed Requirements

The updated requirements are:

- Database size: 1,000,000 student records.
- Search frequency: 50,000 requests per hour.
- Record additions: Once per day.
- Main objective: Support frequent searches efficiently.

### 2.2 Effect on the Original Design

The system must handle repeated searches without scanning the complete database for every request.

Linear Search could perform up to 1,000,000 comparisons for a single unsuccessful search. Repeating this for 50,000 requests would result in a very large number of comparisons.

The high search frequency makes lookup efficiency especially important.

Since new records are added only once per day, the system can build or update an index without sorting the complete dataset for every search request.

## 3. B. Evaluation of the Original Design

### 3.1 Linear Search

Linear Search is not suitable as the primary strategy for this workload because its worst-case search complexity is O(n).

For one million records, an unsuccessful search may examine all one million records.

Across 50,000 requests, the theoretical upper bound on element comparisons would be:

50,000 × 1,000,000 = 50,000,000,000 comparisons per hour.

This is an operation-count estimate, not a measured execution time.

### 3.2 Recursive Binary Search

Binary Search requires sorted records and has O(log n) search complexity.

For one million records:

log2(1,000,000) ≈ 19.93

Therefore, approximately 20 comparisons are sufficient in the usual worst-case scale.

However, the cost of sorting the data and maintaining sorted order must be considered.

### 3.3 Hash Table Search

Hash Table Search offers expected O(1) lookup time under suitable hashing and load-factor assumptions.

Because new records are added only once per day, the system can construct the hash index initially and insert new records when required.

The cost of building the index is spread across many search requests.

## 4. C. Adaptation or Redesign

### 4.1 Final Decision: Modify the Design

The original design is modified to use a hash-based index keyed by the unique student registration number.

### 4.2 Revised Workflow

1. Load the existing student records.
2. Build a hash-based index using registration numbers as keys.
3. Receive a registration-number search request.
4. Calculate the hash value and locate the relevant bucket.
5. Verify the exact registration number.
6. Return the matching student record or report that it is absent.
7. Insert new records into the index when the daily update occurs.

### 4.3 Complexity of the Revised Design

| Operation | Expected Complexity |
|---|---|
| Initial index construction | O(n) |
| Search | O(1) expected |
| Insert one new record | O(1) expected or amortized |

Worst-case search time can still be O(n) when collisions are severe.

The actual performance depends on the hash function, load factor, memory availability and implementation.

## 5. D. Evidence-Based Defence

### 5.1 Mathematical Evidence

Linear Search has O(n) worst-case search complexity.

Binary Search has O(log n) search complexity but requires sorted data.

Hash Table Search has O(1) expected search complexity under suitable assumptions.

For frequent searches on one million records, hash-based indexing reduces the expected amount of work per request.

### 5.2 Search Frequency

The system processes:

50,000 searches per hour.

Average request rate:

50,000 / 3,600 ≈ 13.89 searches per second.

This average rate indicates that the system should be tested under repeated and potentially concurrent requests. Actual peak traffic may be higher.

### 5.3 Preprocessing Cost

Building the hash index requires expected O(n) time.

Because records are added only once per day, the index can be updated incrementally rather than rebuilding the entire structure for every request.

### 5.4 Experimental Evidence

Before final submission, include measured results from Task 9 for all required dataset sizes.

Measure search time separately from index construction time. Use repeated trials and consistent test conditions.

The benchmark should also verify correct results for existing and missing registration numbers.

### 5.5 Trade-offs

Advantages:
- Expected constant-time lookup.
- Supports frequent searches.
- New records can be inserted into the index.
- Avoids sorting the entire dataset after every insertion.

Limitations:
- Requires additional memory.
- Hash collisions may reduce performance.
- Requires correct collision handling and index maintenance.

For a production university system, a database index may be preferable because it supports persistence, transactions and concurrent access.

## 6. Final Conclusion

The original design should be modified to use a hash-based index for registration-number lookups. Its expected O(1) search time and support for incremental insertions make it suitable for a database containing one million records and 50,000 searches per hour.

The final design must be validated with actual benchmark measurements and tested under realistic workloads before deployment.

