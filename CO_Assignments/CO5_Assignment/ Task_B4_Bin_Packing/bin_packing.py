# CO5 Assignment 5
# Task B4 - Final Engineering Decision
# Bin Packing Under a Production Constraint
#
# Strategy:
# First Fit Decreasing (FFD)
#
# The workloads are sorted in decreasing order.
# Each workload is placed into the first server
# having sufficient remaining capacity.


def first_fit_decreasing(workloads, capacity):

    # Sort workloads from largest to smallest
    sorted_workloads = sorted(
        workloads,
        reverse=True
    )

    servers = []

    for workload in sorted_workloads:

        placed = False

        # Try existing servers first
        for server in servers:

            if server["remaining"] >= workload:

                server["workloads"].append(workload)
                server["remaining"] -= workload

                placed = True
                break

        # Open a new server if required
        if not placed:

            new_server = {
                "workloads": [workload],
                "remaining": capacity - workload
            }

            servers.append(new_server)

    return servers


def print_result(test_name, workloads, capacity, servers):

    print("\n" + "=" * 70)
    print(test_name)
    print("=" * 70)

    print("Server Capacity:", capacity)

    print("\nOriginal Workloads:")
    print(workloads)

    print("\nWorkloads in Decreasing Order:")
    print(sorted(workloads, reverse=True))

    print("\nServer Allocation:")

    for index, server in enumerate(servers, start=1):

        print(
            "Server",
            index,
            ":",
            server["workloads"]
        )

        print(
            "Used Capacity:",
            capacity - server["remaining"]
        )

        print(
            "Remaining Capacity:",
            server["remaining"]
        )

    print("\nTotal Servers Used:", len(servers))


def run_test(test_name, workloads, capacity):

    servers = first_fit_decreasing(
        workloads,
        capacity
    )

    print_result(
        test_name,
        workloads,
        capacity,
        servers
    )

    return servers


def main():

    print("=" * 70)
    print("CO5 ASSIGNMENT 5")
    print("TASK B4 - BIN PACKING")
    print("FIRST FIT DECREASING")
    print("=" * 70)

    # ---------------------------------------------------------
    # TEST CASE 1 - Normal Production Workloads
    # ---------------------------------------------------------

    workloads1 = [
        7, 5, 6, 4, 3, 2, 8, 5, 4, 6
    ]

    capacity = 10

    run_test(
        "TEST CASE 1 - NORMAL WORKLOADS",
        workloads1,
        capacity
    )

    # ---------------------------------------------------------
    # TEST CASE 2 - Challenging Input
    #
    # Designed to demonstrate that a heuristic does not
    # necessarily produce the optimal solution.
    # ---------------------------------------------------------

    workloads2 = [
        6, 6, 6, 4, 4, 4, 4, 4, 4
    ]

    run_test(
        "TEST CASE 2 - CHALLENGING WORKLOADS",
        workloads2,
        capacity
    )

    # ---------------------------------------------------------
    # TEST CASE 3 - Larger Production-Style Input
    # ---------------------------------------------------------

    workloads3 = [
        9, 8, 7, 6, 5,
        9, 8, 7, 6, 5,
        4, 4, 3, 3, 2,
        8, 7, 6, 5, 4,
        3, 2, 1, 9, 8
    ]

    run_test(
        "TEST CASE 3 - LARGER WORKLOAD SET",
        workloads3,
        capacity
    )

    print("\n" + "=" * 70)
    print("ENGINEERING DECISION")
    print("=" * 70)

    print(
        "Chosen Strategy: First Fit Decreasing"
    )

    print(
        "Reason: It provides a practical balance"
        " between solution quality and computation."
    )

    print(
        "Production Benefit: Fast allocation without"
        " exhaustive enumeration of all possibilities."
    )

    print(
        "Limitation: It does not guarantee the"
        " minimum possible number of servers."
    )


if __name__ == "__main__":
    main()
