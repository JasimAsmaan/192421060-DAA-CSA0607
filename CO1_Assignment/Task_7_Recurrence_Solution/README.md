
# Task 7: Solve the Recurrence Relation

## 1. Introduction

In Task 6, the recurrence relation for Recursive Binary Search was formulated as:

T(n) = T(n/2) + c

where c is the constant work performed at each recursive call.

The recurrence is solved using the iteration method.

## 2. Iteration Method

### 2.1 Initial Recurrence

T(n) = T(n/2) + c

Expanding T(n/2):

T(n/2) = T(n/4) + c

Substituting:

T(n) = T(n/4) + 2c

Expanding again:

T(n) = T(n/8) + 3c

After k expansions:

T(n) = T(n/2^k) + kc

### 2.2 Finding the Number of Expansions

The recursion stops when the subproblem size becomes 1.

Therefore:

n / 2^k = 1

n = 2^k

Taking logarithms to base 2:

k = log2(n)

### 2.3 Substitution

Substituting k = log2(n) into the expanded recurrence:

T(n) = T(1) + c log2(n)

Let T(1) = c0, where c0 is a constant.

Then:

T(n) = c0 + c log2(n)

Since c0 and c are constants, the logarithmic term determines the growth rate.

Therefore:

T(n) = Θ(log n)

## 3. Verification Using the Master Theorem

The recurrence is:

T(n) = aT(n/b) + f(n)

Comparing with:

T(n) = T(n/2) + c

We obtain:

a = 1
b = 2
f(n) = Θ(1)

Calculate:

n^(log_b(a)) = n^(log2(1)) = n^0 = 1

Thus:

f(n) = Θ(n^(log_b(a)))

This satisfies Case 2 of the Master Theorem in its standard form.

Therefore:

T(n) = Θ(log n)

## 4. Interpretation

The recurrence solution demonstrates that the number of recursive levels increases logarithmically as the input size grows.

For one million sorted records:

log2(1,000,000) ≈ 19.93

Therefore, approximately 20 divisions are sufficient to reduce the search interval to a single element.

The exact number of comparisons depends on the target position and the implementation.

## 5. Conclusion

Using both the iteration method and the Master Theorem, the recurrence T(n) = T(n/2) + c is solved as Θ(log n). This confirms the logarithmic worst-case time complexity of Recursive Binary Search on sorted data.

