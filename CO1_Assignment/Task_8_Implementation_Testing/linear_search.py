
def linear_search(arr, key):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1

        if arr[i] == key:
            return i, comparisons

    return -1, comparisons


n = int(input("Enter number of records: "))
arr = []

print("Enter registration numbers:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter registration number to search: "))

position, comparisons = linear_search(arr, key)

if position != -1:
    print("Record found at position:", position + 1)
else:
    print("Record not found")

print("Number of comparisons:", comparisons)

