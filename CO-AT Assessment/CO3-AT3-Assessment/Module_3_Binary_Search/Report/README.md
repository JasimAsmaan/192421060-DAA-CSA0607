# Module 3 - Binary Search Report

## 1. Problem Statement

KartIQ maintains seller scores in a sorted leaderboard.

The system needs to locate a particular seller score quickly.

A linear search may require checking many elements one by one. Binary Search improves the search process by repeatedly dividing the search range into two halves.

## 2. Binary Search

Binary Search is a divide-and-conquer searching algorithm.

It requires the input data to be sorted.

For every iteration:

1. Find the middle element.
2. Compare the middle element with the search key.
3. If they are equal, the element is found.
4. If the key is smaller, search the left half.
5. If the key is larger, search the right half.
6. Repeat until the element is found or the search range becomes empty.

## 3. Example

Consider the sorted seller scores:

```text
8, 17, 29, 42, 55, 63, 75, 88
