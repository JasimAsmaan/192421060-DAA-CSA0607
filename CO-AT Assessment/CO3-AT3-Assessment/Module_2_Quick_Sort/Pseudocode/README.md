## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

## Space Complexity

### Balanced Recursion

The recursion depth is:

`O(log n)`

### Worst-Case Recursion

The recursion depth can become:

`O(n)`

## Reason for Poor Performance

When the seller scores are nearly sorted and the first element is always selected as the pivot, the pivot may repeatedly become the smallest or largest element.

This produces highly unbalanced partitions and results in `O(n²)` performance.

## Improved Pivot Strategy

The Median-of-Three method selects three elements:

- First element
- Middle element
- Last element

The median of these three values is selected as the pivot.

This generally produces more balanced partitions and improves performance on sorted and nearly sorted data.

## Advantages of Median-of-Three

- Reduces the chance of selecting an extreme pivot.
- Performs better on sorted and nearly sorted data.
- Produces more balanced partitions in many cases.
- Reduces the likelihood of worst-case behaviour.
- Requires only a small amount of additional work.

## Experimental Test Cases

### Test Case 1 – Random Data

```text
42, 17, 63, 8, 55, 29
```

### Test Case 2 – Sorted Data

```text
10, 20, 30, 40, 50, 60, 70, 80
```

### Test Case 3 – Reverse Sorted Data

```text
80, 70, 60, 50, 40, 30, 20, 10
```

### Test Case 4 – Nearly Sorted Data

```text
10, 20, 30, 40, 50, 35, 60, 70
```

## Experimental Comparison

Run the Python program and record the actual comparison counts.

| Dataset | First-Element Pivot | Median-of-Three |
|---|---:|---:|
| Random | Actual value | Actual value |
| Sorted | Actual value | Actual value |
| Reverse Sorted | Actual value | Actual value |
| Nearly Sorted | Actual value | Actual value |

## Recommendation

For the KartIQ live seller leaderboard, the first-element pivot is not ideal because the data is frequently nearly sorted.

The Median-of-Three strategy is recommended because it reduces the probability of choosing an extreme pivot.

## Conclusion

Quick Sort is an efficient divide-and-conquer algorithm when the pivot creates balanced partitions.

For balanced partitions, the time complexity is `O(n log n)`.

For highly unbalanced partitions, the time complexity becomes `O(n²)`.

Since the KartIQ leaderboard is frequently nearly sorted, Median-of-Three pivot selection is a better strategy than always selecting the first element.
