
# Task 9: Record Experimental Performance

## 1. Introduction

This task records the experimental performance of Linear Search, Recursive Binary Search and Hash Table Search using datasets of increasing sizes.

The measurements will be used to compare practical performance with the theoretical complexity derived in previous tasks.

## 2. Experimental Setup

- Programming language: Python 3
- Dataset sizes: 1,000, 10,000, 100,000 and 1,000,000 records
- Execution-time measurement: time.perf_counter()
- Data: Unique integer registration numbers
- Test conditions: Equivalent datasets and target values for each algorithm

## 3. Performance Measures

### 3.1 Execution Time

Execution time measures how long each algorithm takes to complete a search.

The program should use time.perf_counter() and repeat measurements where appropriate to reduce timing variation.

### 3.2 Number of Comparisons

For Linear Search, count each comparison between the target and an array element.

For Recursive Binary Search, count each comparison with a middle element.

For Hash Table Search, report lookup time separately because Python's internal hash-table operations are not directly counted by the same comparison counter.

## 4. Experimental Results

Run the benchmark program and record the actual measurements in the table below.

| Dataset Size | Linear Search Time | Binary Search Time | Hash Search Time |
|---:|---:|---:|---:|
| 1,000 | To be measured | To be measured | To be measured |
| 10,000 | To be measured | To be measured | To be measured |
| 100,000 | To be measured | To be measured | To be measured |
| 1,000,000 | To be measured | To be measured | To be measured |

Execution time units: seconds.

## 5. Comparison Count Results

| Dataset Size | Linear Search Comparisons (Worst Case) | Binary Search Comparisons (Approximate Worst Case) |
|---:|---:|---:|
| 1,000 | 1,000 | About 10 |
| 10,000 | 10,000 | About 14 |
| 100,000 | 100,000 | About 17 |
| 1,000,000 | 1,000,000 | About 20 |

The Binary Search counts are approximate. Exact counts depend on the implementation and whether the target is present.

## 6. Graphical Representation

Create a line graph with dataset size on the X-axis and measured execution time on the Y-axis.

Plot separate series for Linear Search, Binary Search and Hash Table Search.

Use the actual benchmark measurements to create the graph. Do not use estimated values as measured experimental results.

## 7. Observations

After running the experiment, describe how execution time changes as the dataset increases.

Discuss whether Linear Search shows approximately linear growth, whether Binary Search grows logarithmically, and whether Hash Table Search provides near-constant expected lookup time.

## 8. Conclusion

The measured execution times and comparison counts provide experimental evidence for evaluating the theoretical efficiency of the three algorithms. The final observations should be based on the actual results obtained from the benchmark program.


