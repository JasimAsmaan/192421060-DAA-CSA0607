
# Task 6: Formulate the Recurrence Relation

## 1. Introduction

A recurrence relation expresses the running time of a recursive algorithm in terms of the running time of smaller input sizes.

In this task, the recurrence relation for Recursive Binary Search is derived from its algorithm.

## 2. Recursive Binary Search

### 2.1 Input Size

Let n represent the number of elements in a sorted array.

### 2.2 Algorithm Behaviour

Recursive Binary Search compares the target registration number with the middle element.

- If the target matches the middle element, the search terminates.
- If the target is smaller, the algorithm searches the left half.
- If the target is larger, the algorithm searches the right half.

At each recursive step, approximately half of the elements are eliminated.

### 2.3 Components of the Recurrence

1. Original problem size: n elements.
2. Number of recursive calls: One recursive call at most.
3. Subproblem size: Approximately n/2 elements.
4. Work outside the recursive call: A constant amount of work for calculating the middle index and performing comparisons.
5. Base case: The search interval is empty or the target is found.

### 2.4 Deriving the Recurrence Relation

For the worst case, the target is not found at the middle element, so the algorithm continues searching one half.

The recurrence is:

T(n) = T(n/2) + c, for n > 1

where c is the constant work performed at each recursive call.

The base case is:

T(1) = c0

where c0 represents the constant time required for the smallest subproblem.

For an empty search interval, the algorithm terminates immediately, requiring constant time.

## 3. Interpretation

The recurrence shows that the algorithm does not process all n elements at every step. Instead, it continues with only one half of the previous search interval.

This reduction leads to logarithmic search complexity.

## 4. Conclusion

The recurrence relation for Recursive Binary Search is T(n) = T(n/2) + c, with a constant-time base case. It represents one recursive subproblem of approximately half the original size and constant work outside the recursive call. The recurrence will be solved in Task 7.

