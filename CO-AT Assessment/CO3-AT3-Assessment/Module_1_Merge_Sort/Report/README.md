# Module 1 – Merge Sort for Nightly Order Consolidation

## 1. Problem Statement

KartIQ is a retail data analytics platform that processes approximately 10,000,000 orders every day.

The nightly audit report requires all orders to be sorted according to their timestamps.

An important requirement is that orders having the same timestamp must maintain their original arrival order because auditors reconcile the orders gateway by gateway.

The sample orders given are:

| Timestamp | Order ID |
|---:|---|
| 105 | O1 |
| 102 | O2 |
| 105 | O3 |
| 101 | O4 |
| 102 | O5 |
| 103 | O6 |

A stable Merge Sort is selected because it provides O(n log n) worst-case time complexity and preserves the relative order of equal keys.

## 2. Why Merge Sort?

Merge Sort follows the divide-and-conquer strategy.

It divides the input into smaller sublists, recursively sorts them, and then combines the sorted sublists.

Merge Sort is appropriate for this problem because:

- It guarantees O(n log n) time complexity.
- Its performance does not depend on whether the input is already sorted or reversed.
- It can be implemented as a stable sorting algorithm.
- It is suitable for external sorting when the complete dataset cannot fit into RAM.

## 3. Divide Step

The six sample orders are divided into two halves.

First division:

```text
[(105,O1), (102,O2), (105,O3)]
        |
        +----------------+
                         |
[(101,O4), (102,O5), (103,O6)]
