# Module 3 - Binary Search
# CO3 AT3 - Divide and Conquer
# KartIQ Retail Data Analytics Platform
#
# This program demonstrates Binary Search on seller scores.
# It compares the number of comparisons for different datasets.

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2

        comparisons += 1

        if arr[mid] == key:
            return mid, comparisons

        elif key < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1, comparisons


def recursive_binary_search(arr, low, high, key):
    if low > high:
        return -1, 0

    mid = (low + high) // 2

    comparisons = 1

    if arr[mid] == key:
        return mid, comparisons

    elif key < arr[mid]:
        position, extra = recursive_binary_search(
            arr, low, mid - 1, key
        )
        return position, comparisons + extra

    else:
        position, extra = recursive_binary_search(
            arr, mid + 1, high, key
        )
        return position, comparisons + extra


def run_test(test_name, scores, key):

    print("\n" + "=" * 60)
    print(test_name)
    print("=" * 60)

    print("Seller Scores:")
    print(scores)

    print("Search Key:", key)

    # Iterative Binary Search
    position, comparisons = binary_search(scores, key)

    print("\nIterative Binary Search:")

    if position != -1:
        print("Seller score found at position:", position + 1)
    else:
        print("Seller score not found.")

    print("Comparisons:", comparisons)

    # Recursive Binary Search
    position_recursive, recursive_comparisons = (
        recursive_binary_search(
            scores,
            0,
            len(scores) - 1,
            key
        )
    )

    print("\nRecursive Binary Search:")

    if position_recursive != -1:
        print(
            "Seller score found at position:",
            position_recursive + 1
        )
    else:
        print("Seller score not found.")

    print("Comparisons:", recursive_comparisons)


def main():

    print("KARTIQ SELLER LEADERBOARD")
    print("BINARY SEARCH PERFORMANCE ANALYSIS")

    # Binary Search requires sorted data
    seller_scores = [
        8, 17, 29, 42, 55, 63, 75, 88
    ]

    # Test Case 1 - Existing seller score
    run_test(
        "TEST CASE 1 - EXISTING SCORE",
        seller_scores,
        55
    )

    # Test Case 2 - First element
    run_test(
        "TEST CASE 2 - FIRST ELEMENT",
        seller_scores,
        8
    )

    # Test Case 3 - Last element
    run_test(
        "TEST CASE 3 - LAST ELEMENT",
        seller_scores,
        88
    )

    # Test Case 4 - Score not present
    run_test(
        "TEST CASE 4 - SCORE NOT FOUND",
        seller_scores,
        50
    )

    # Test Case 5 - Larger dataset
    large_scores = [
        5, 10, 15, 20, 25, 30, 35, 40,
        45, 50, 55, 60, 65, 70, 75, 80,
        85, 90, 95, 100
    ]

    run_test(
        "TEST CASE 5 - LARGER DATASET",
        large_scores,
        75
    )

    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)

    print("Best Case     : O(1)")
    print("Average Case  : O(log n)")
    print("Worst Case    : O(log n)")
    print("Iterative Space : O(1)")
    print("Recursive Space : O(log n)")

    print("\nRequirement:")
    print("The input array must be sorted before Binary Search.")


if __name__ == "__main__":
    main()
