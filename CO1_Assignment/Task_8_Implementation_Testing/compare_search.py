
import time


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def hash_search(records, key):
    return records.get(key, -1)


n = int(input("Enter number of records: "))

arr = list(range(1, n + 1))
key = int(input("Enter registration number to search: "))

records = {value: value for value in arr}

start = time.perf_counter()
result1 = linear_search(arr, key)
linear_time = time.perf_counter() - start

start = time.perf_counter()
result2 = binary_search(arr, key)
binary_time = time.perf_counter() - start

start = time.perf_counter()
result3 = hash_search(records, key)
hash_time = time.perf_counter() - start

print("\nSearch Results")
print("------------------------")

print("Linear Search Position:", result1)
print("Linear Search Time:", linear_time, "seconds")

print("\nBinary Search Position:", result2)
print("Binary Search Time:", binary_time, "seconds")

print("\nHash Table Search Result:", result3)
print("Hash Table Search Time:", hash_time, "seconds")

