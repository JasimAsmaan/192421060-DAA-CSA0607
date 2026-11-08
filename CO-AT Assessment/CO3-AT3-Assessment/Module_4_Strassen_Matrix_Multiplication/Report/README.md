# Module 4 - Strassen Matrix Multiplication Report

## 1. Problem Statement

KartIQ requires efficient matrix multiplication for processing analytical data.

Traditional matrix multiplication requires O(n³) time.

Strassen's Matrix Multiplication algorithm improves the multiplication process by reducing the number of recursive multiplications from eight to seven.

## 2. Objective

The objectives of this module are:

1. Implement Strassen's Matrix Multiplication algorithm.
2. Understand its divide-and-conquer approach.
3. Demonstrate the divide, conquer and combine operations.
4. Verify the result against conventional matrix multiplication.
5. Analyse the recurrence relation.
6. Determine time and space complexity.

## 3. Strassen's Matrix Multiplication

Consider two matrices:

```text
A = | A11  A12 |
    | A21  A22 |

B = | B11  B12 |
    | B21  B22 |
