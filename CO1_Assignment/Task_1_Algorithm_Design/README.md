
# Task 1: Algorithm Design

## 1. Domain Overview: Student Registration Number Search

A university maintains a large database of student records. Each student is identified by a unique registration number. The objective is to design efficient algorithms to determine whether a registration number exists in the database.

The dataset may contain 1,000, 10,000, 100,000, or 1,000,000 student records.

Three different searching strategies are considered:

1. Linear Search
2. Binary Search
3. Hash Table Search

## 2. Approach 1: Linear Search

### 2.1 Design Description and Working Principle

Linear Search examines each registration number sequentially until the required number is found or the end of the dataset is reached.

- Input: List of registration numbers and target registration number.
- Output: Position of the matching record or a message indicating that it was not found.
- Preprocessing: No sorting is required.

### 2.2 Pseudocode

ALGORITHM LinearSearch(A, n, key)

FOR i = 0 TO n - 1
    IF A[i] == key
        RETURN i
    END IF
END FOR

RETURN -1

### 2.3 Design Strategy

Linear Search uses an iterative sequential-search strategy. It works on both sorted and unsorted data.

## 3. Approach 2: Recursive Binary Search

### 3.1 Design Description and Working Principle

Binary Search repeatedly divides a sorted dataset into two halves. It compares the target with the middle element and continues searching in the relevant half.

- Input: Sorted list and target registration number.
- Output: Position of the matching record or -1 if absent.
- Preprocessing: The records must be sorted.

### 3.2 Pseudocode

ALGORITHM BinarySearch(A, low, high, key)

IF low > high
    RETURN -1
END IF

mid = (low + high) // 2

IF A[mid] == key
    RETURN mid
ELSE IF key < A[mid]
    RETURN BinarySearch(A, low, mid - 1, key)
ELSE
    RETURN BinarySearch(A, mid + 1, high, key)
END IF

### 3.3 Design Strategy

Recursive Binary Search uses divide-and-conquer. Each recursive call reduces the search interval approximately by half.

## 4. Approach 3: Hash Table Search

### 4.1 Design Description and Working Principle

A hash table stores registration numbers using a hash function. The function maps each registration number to a table location, allowing the system to locate records efficiently.

- Input: Hash table and target registration number.
- Output: Matching record or a message indicating that it was not found.
- Preprocessing: Registration numbers must be inserted into the hash table.
- Collision handling: Collisions can be handled using separate chaining.

### 4.2 Pseudocode

ALGORITHM HashSearch(H, key)

index = HashFunction(key)

SEARCH the bucket at H[index]

IF key is present
    RETURN the matching record
ELSE
    RETURN NOT FOUND
END IF

### 4.3 Design Strategy

Hash Table Search uses hashing to support fast average-case lookups. Its performance depends on the hash function, load factor and collision handling.

## 5. Initial Comparison

| Algorithm | Strategy | Data Requirement | Average Search Time |
|---|---|---|---|
| Linear Search | Sequential | Sorted or unsorted | O(n) |
| Recursive Binary Search | Divide-and-conquer | Sorted | O(log n) |
| Hash Table Search | Hashing | Hash table prepared | O(1) average |

## 6. Conclusion

The three algorithms use different searching strategies. Their mathematical complexity, preprocessing requirements and measured execution times will be analysed in the following tasks.
