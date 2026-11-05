# Module 1 – Merge Sort for Nightly Order Consolidation

## Aim

To sort 10,000,000 retail orders by timestamp using stable Merge Sort while preserving the original arrival order of orders having the same timestamp.

## Input

Each order is represented as:

(timestamp, order_id)

Sample input:

(105, O1), (102, O2), (105, O3), (101, O4), (102, O5), (103, O6)

## Divide-and-Conquer Strategy

### Divide

Divide the list of orders into two approximately equal halves.

Continue dividing each half recursively until every sublist contains one order.

A single order is already sorted.

### Conquer

Recursively sort the left half and the right half.

### Combine

Merge the two sorted halves.

During merging, if two orders have the same timestamp, select the order from the left half first. This preserves the original arrival order and makes the algorithm stable.

## Pseudocode

```text
MERGE_SORT(orders, left, right)

1. IF left >= right
2.     RETURN
3. END IF

4. mid = (left + right) / 2

5. MERGE_SORT(orders, left, mid)
6. MERGE_SORT(orders, mid + 1, right)

7. MERGE(orders, left, mid, right)
