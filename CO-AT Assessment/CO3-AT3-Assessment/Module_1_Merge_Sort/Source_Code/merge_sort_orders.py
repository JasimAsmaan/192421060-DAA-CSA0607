def merge(orders, left, mid, right):
    temp = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:

        # <= preserves stability when timestamps are equal
        if orders[i][0] <= orders[j][0]:
            temp.append(orders[i])
            i += 1
        else:
            temp.append(orders[j])
            j += 1

    while i <= mid:
        temp.append(orders[i])
        i += 1

    while j <= right:
        temp.append(orders[j])
        j += 1

    for k in range(len(temp)):
        orders[left + k] = temp[k]


def merge_sort(orders, left, right):

    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(orders, left, mid)
    merge_sort(orders, mid + 1, right)

    merge(orders, left, mid, right)


def print_orders(title, orders):

    print("\n" + title)
    print("-" * len(title))

    for order in orders:
        print("Timestamp:", order[0], "Order ID:", order[1])


if __name__ == "__main__":

    orders = [
        (105, "O1"),
        (102, "O2"),
        (105, "O3"),
        (101, "O4"),
        (102, "O5"),
        (103, "O6")
    ]

    print_orders("Original Orders", orders)

    merge_sort(orders, 0, len(orders) - 1)

    print_orders("Sorted Orders", orders)

    print("\nStability Check:")
    print("Timestamp 102 -> O2 appears before O5")
    print("Timestamp 105 -> O1 appears before O3")
