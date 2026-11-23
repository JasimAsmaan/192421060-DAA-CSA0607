# Module 3 - Binary Search

## Aim

To analyse and implement Binary Search for locating seller scores in a sorted leaderboard.

## Problem

KartIQ maintains seller scores in sorted order. Binary Search is used to quickly locate a particular seller score.

## Divide-and-Conquer Strategy

Binary Search divides the search interval into two halves.

### Divide

Find the middle element of the current search range.

### Conquer

If the search key is smaller than the middle element, search the left half.

If the search key is larger than the middle element, search the right half.

### Combine

No separate combine operation is required because only one half is searched at each step.

## Iterative Binary Search Pseudocode

```text
BINARY_SEARCH(A, key)

1. low = 0
2. high = length(A) - 1

3. WHILE low <= high

4.     mid = (low + high) / 2

5.     IF A[mid] == key
6.         RETURN mid

7.     ELSE IF key < A[mid]
8.         high = mid - 1

9.     ELSE
10.        low = mid + 1

11.    END IF

12. END WHILE

13. RETURN -1
