
def selection_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1

    return a, comparisons, swaps


def bubble_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(a)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return a, comparisons, swaps


def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                movements += 1
                j -= 1
            else:
                break

        a[j + 1] = key
        movements += 1

    return a, comparisons, movements


def test_sorting_algorithms(name, data):
    print("\nDataset:", name)
    print("Original:", data)

    algorithms = [
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort)
    ]

    for algorithm_name, algorithm in algorithms:
        result, comparisons, movements = algorithm(data)

        print("\n", algorithm_name)
        print("Sorted Output:", result)
        print("Comparisons:", comparisons)
        print("Swaps/Movements:", movements)


def main():
    random_data = [45, 12, 78, 23, 56, 9, 34]
    nearly_sorted = [10, 20, 30, 50, 40, 60, 70]
    sorted_data = [10, 20, 30, 40, 50, 60, 70]
    reverse_data = [70, 60, 50, 40, 30, 20, 10]

    test_sorting_algorithms("Random Data", random_data)
    test_sorting_algorithms("Nearly Sorted Data", nearly_sorted)
    test_sorting_algorithms("Already Sorted Data", sorted_data)
    test_sorting_algorithms("Reverse Sorted Data", reverse_data)


if __name__ == "__main__":
    main()

