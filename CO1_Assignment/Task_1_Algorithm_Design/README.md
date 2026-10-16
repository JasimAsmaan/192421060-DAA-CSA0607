
# Task 1: Algorithm Design

## 1. Domain Overview: Student Registration Number Search

A university maintains a large academic database containing student records. Each student is identified by a unique registration number. Faculty members and administrative staff frequently search for registration numbers to determine whether a student record exists and retrieve the corresponding information.

The database may contain 1,000, 10,000, 100,000 or 1,000,000 or more student records.

The objective is to design and compare different searching algorithms that can efficiently locate a given registration number as the database grows.

Three different algorithmic strategies are proposed:

1. Linear Search
2. Recursive Binary Search
3. Hash Table Search

These algorithms use different approaches to locate records and have different preprocessing requirements and time complexities.

---

## 2. Approach 1: Linear Search

### 2.1 Design Description

Linear Search is a sequential searching algorithm that examines each element of an array one by one until the required registration number is found or the end of the array is reached.

It does not require the records to be sorted.

### 2.2 Working Principle

1. Start from the first element of the array.
2. Compare the current registration number with the target.
3. If both values match, return the position.
4. Otherwise, move to the next element.
5. If the end of the array is reached, report that the record was not found.

### 2.3 Pseudocode

```text
ALGORITHM LinearSearch(A, n, key)

FOR i = 0 TO n - 1
    IF A[i] == key
        RETURN i
    END IF
END FOR

RETURN -1

END ALGORITHM
```

### 2.4 Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input array A, size n and key/]
    B --> C[i = 0]
    C --> D{i < n?}
    D -- No --> E[/Print Not Found/]
    E --> K([End])
    D -- Yes --> F{A[i] == key?}
    F -- Yes --> G[/Print position i + 1/]
    G --> K
    F -- No --> H[i = i + 1]
    H --> D
```

### 2.5 Design Strategy

Linear Search follows an iterative sequential-search strategy. It examines records in their existing order and stops when a match is found.

### 2.6 Preprocessing Requirements

- No sorting is required.
- No additional search data structure is required.
- The records can be searched in either sorted or unsorted order.

### 2.7 Justification for Selection

Linear Search is selected because it is simple to implement and provides a baseline for comparing more efficient searching techniques. It is useful for small datasets and situations where preprocessing is undesirable.

### 2.8 Time Complexity

- Best case: O(1)
- Average case: O(n)
- Worst case: O(n)
- Auxiliary space: O(1)

---

## 3. Approach 2: Recursive Binary Search

### 3.1 Design Description

Binary Search is a divide-and-conquer algorithm that searches a sorted array by repeatedly dividing the search interval into two halves.

Unlike Linear Search, Binary Search requires the registration numbers to be sorted before searching.

### 3.2 Working Principle

1. Identify the middle element of the current search interval.
2. Compare the middle element with the target registration number.
3. If they match, return the position.
4. If the target is smaller, recursively search the left half.
5. If the target is larger, recursively search the right half.
6. If the interval becomes empty, report that the record was not found.

### 3.3 Pseudocode

```text
ALGORITHM BinarySearch(A, low, high, key)

IF low > high
    RETURN -1
END IF

mid = low + (high - low) // 2

IF A[mid] == key
    RETURN mid
ELSE IF key < A[mid]
    RETURN BinarySearch(A, low, mid - 1, key)
ELSE
    RETURN BinarySearch(A, mid + 1, high, key)
END IF

END ALGORITHM
```

### 3.4 Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input sorted array, low, high and key/]
    B --> C{low <= high?}
    C -- No --> D[/Return Not Found: -1/]
    D --> K([End])
    C -- Yes --> E[mid = low + (high - low) // 2]
    E --> F{A[mid] == key?}
    F -- Yes --> G[/Return mid/]
    G --> K
    F -- No --> H{key < A[mid]?}
    H -- Yes --> I[high = mid - 1]
    H -- No --> J[low = mid + 1]
    I --> C
    J --> C
```

### 3.5 Design Strategy

Recursive Binary Search follows the divide-and-conquer strategy. Each recursive call reduces the search interval to approximately half its previous size.

### 3.6 Preprocessing Requirements

- The registration numbers must be sorted.
- If the records are initially unsorted, sorting must be performed before searching.
- Comparison-based sorting, such as Merge Sort, typically requires O(n log n) time.

### 3.7 Justification for Selection

Recursive Binary Search is selected because it significantly reduces the number of comparisons required for large, sorted datasets. It demonstrates how divide-and-conquer improves searching efficiency.

### 3.8 Time Complexity

- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)
- Auxiliary space: O(log n) due to recursive calls

---

## 4. Approach 3: Hash Table Search

### 4.1 Design Description

Hash Table Search uses a hash function to map a registration number to a location in a hash table.

Instead of checking every record sequentially, the algorithm uses the calculated hash value to identify the relevant bucket and searches that bucket for the exact registration number.

A hash table can be implemented using Python dictionaries or sets.

### 4.2 Working Principle

1. Build a hash table containing the existing registration numbers.
2. Receive the target registration number.
3. Calculate its hash value.
4. Access the corresponding bucket.
5. Check whether the target exists in the bucket.
6. Return the matching record or report that it was not found.

### 4.3 Pseudocode

```text
ALGORITHM HashSearch(H, key)

index = HashFunction(key)

FOR each item in H[index]
    IF item.registration_number == key
        RETURN item
    END IF
END FOR

RETURN NOT FOUND

END ALGORITHM
```

This pseudocode assumes a hash table that uses separate chaining to handle collisions.

### 4.4 Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input hash table H and key/]
    B --> C[index = HashFunction(key)]
    C --> D[Access bucket H[index]]
    D --> E{Bucket contains key?}
    E -- Yes --> F[/Return matching record/]
    E -- No --> G[/Print Not Found/]
    F --> K([End])
    G --> K
```

### 4.5 Design Strategy

Hash Table Search follows a hashing-based strategy. A hash function maps each registration number to a bucket, allowing the system to locate the relevant record without scanning the entire dataset under normal conditions.

### 4.6 Preprocessing Requirements

- A hash table must be created and populated with the student registration numbers.
- A suitable hash function must be selected.
- Collisions must be handled correctly, for example, through separate chaining.
- The hash table must be updated when new student records are added.

### 4.7 Justification for Selection

Hash Table Search is selected because the university needs to perform repeated searches using unique registration numbers. Hash-based indexing can provide constant expected lookup time and supports inserting new records without sorting the entire dataset after every insertion.

### 4.8 Time Complexity

- Best case: O(1)
- Average expected case: O(1), assuming suitable hashing and a controlled load factor
- Worst case: O(n), when many records collide in the same bucket
- Auxiliary space: O(n) for the hash table

Building the hash table takes O(n) expected time under suitable hashing assumptions.

---

## 5. Comparative Analysis

| Feature | Linear Search | Recursive Binary Search | Hash Table Search |
|---|---|---|---|
| Strategy | Sequential search | Divide and conquer | Hashing |
| Data requirement | Sorted or unsorted | Sorted | Hash table required |
| Preprocessing | None required | Sorting may be required | Build hash table |
| Best-case time | O(1) | O(1) | O(1) |
| Average expected time | O(n) | O(log n) | O(1) |
| Worst-case time | O(n) | O(log n) | O(n) |
| Auxiliary space | O(1) | O(log n) | O(n) |
| Supports incremental insertion | Yes, in the underlying collection | Depends on how sorted data is maintained | Yes, expected O(1) insertion |

---

## 6. Overall Conclusion

Three different searching strategies have been designed for locating student registration numbers.

Linear Search provides a simple baseline and does not require preprocessing. Recursive Binary Search efficiently searches sorted records by repeatedly dividing the search interval into halves. Hash Table Search uses hashing to support fast expected lookups and incremental insertion of new records.

The algorithms will be mathematically analysed and experimentally tested using datasets of 1,000, 10,000, 100,000 and 1,000,000 records in the subsequent tasks.

The final recommendation will consider search complexity, preprocessing cost, measured execution time, memory usage and the university's requirement to process frequent searches.
