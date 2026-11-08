# Module 4 - Strassen Matrix Multiplication

## Aim

To implement Strassen's Matrix Multiplication algorithm using the divide-and-conquer technique and analyse its time and space complexity.

## Problem Statement

KartIQ requires efficient matrix multiplication for processing analytical data.

The conventional matrix multiplication method performs eight recursive multiplications when a matrix is divided into four submatrices.

Strassen's algorithm reduces the number of recursive multiplications from eight to seven.

## Divide-and-Conquer Strategy

Strassen's algorithm divides each matrix into four submatrices.

For two matrices A and B:

```text
A = | A11  A12 |
    | A21  A22 |

B = | B11  B12 |
    | B21  B22 |
