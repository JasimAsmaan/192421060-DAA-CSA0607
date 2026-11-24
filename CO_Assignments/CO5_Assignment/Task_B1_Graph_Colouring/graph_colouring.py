# CO5 Assignment 5
# Task B1 - Implement and Instrument Your Search
# Graph Colouring
#
# The program implements backtracking graph colouring.
# It compares:
# Version 1 - Original/Input vertex order
# Version 2 - Degree-based vertex ordering heuristic
#
# Instrumentation:
# 1. Search nodes visited
# 2. Candidate assignments attempted
# 3. Rejected branches
# 4. Number of backtracks
# 5. Maximum search depth
# 6. Final colouring


class SearchStats:

    def __init__(self):
        self.search_nodes = 0
        self.candidate_assignments = 0
        self.rejected_branches = 0
        self.backtracks = 0
        self.max_depth = 0


def is_safe(graph, vertex, colour, colours):

    for neighbour in graph[vertex]:

        if colours[neighbour] == colour:
            return False

    return True


def get_degree_order(graph):

    vertices = list(range(len(graph)))

    # Higher degree vertices are selected first.
    vertices.sort(
        key=lambda vertex: len(graph[vertex]),
        reverse=True
    )

    return vertices


def graph_colouring(graph, number_of_colours, order):

    colours = [0] * len(graph)
    stats = SearchStats()

    def backtrack(position):

        stats.search_nodes += 1

        if position > stats.max_depth:
            stats.max_depth = position

        # All vertices have been coloured.
        if position == len(order):
            return True

        vertex = order[position]

        for colour in range(1, number_of_colours + 1):

            stats.candidate_assignments += 1

            if is_safe(graph, vertex, colour, colours):

                colours[vertex] = colour

                if backtrack(position + 1):
                    return True

                # Undo assignment during backtracking.
                colours[vertex] = 0
                stats.backtracks += 1

            else:
                stats.rejected_branches += 1

        # No colour works for this vertex.
        stats.rejected_branches += 1

        return False

    result = backtrack(0)

    if result:
        return colours, stats

    return None, stats


def print_result(
    test_name,
    graph,
    number_of_colours,
    version_name,
    order,
    colouring,
    stats
):

    print("\n" + "=" * 70)
    print(test_name)
    print(version_name)
    print("=" * 70)

    print("Number of Vertices:", len(graph))
    print("Number of Colours:", number_of_colours)

    print("Vertex Order:", [v + 1 for v in order])

    if colouring is not None:

        print("Result: COLOURABLE")

        print("Colour Assignment:")

        for vertex in range(len(colouring)):
            print(
                "Vertex",
                vertex + 1,
                "-> Colour",
                colouring[vertex]
            )

    else:

        print("Result: NOT COLOURABLE")

    print("\nInstrumentation:")
    print("Search Nodes Visited:", stats.search_nodes)
    print("Candidate Assignments:", stats.candidate_assignments)
    print("Rejected Branches:", stats.rejected_branches)
    print("Backtracks:", stats.backtracks)
    print("Maximum Search Depth:", stats.max_depth)


def run_test(test_name, graph, number_of_colours):

    print("\n\n")
    print("#" * 70)
    print(test_name)
    print("#" * 70)

    # ---------------------------------------------------------
    # Version 1 - Original/Input Order
    # ---------------------------------------------------------

    original_order = list(range(len(graph)))

    colouring1, stats1 = graph_colouring(
        graph,
        number_of_colours,
        original_order
    )

    print_result(
        test_name,
        graph,
        number_of_colours,
        "VERSION 1 - ORIGINAL / INPUT ORDER",
        original_order,
        colouring1,
        stats1
    )

    # ---------------------------------------------------------
    # Version 2 - Degree-Based Heuristic
    # ---------------------------------------------------------

    heuristic_order = get_degree_order(graph)

    colouring2, stats2 = graph_colouring(
        graph,
        number_of_colours,
        heuristic_order
    )

    print_result(
        test_name,
        graph,
        number_of_colours,
        "VERSION 2 - DEGREE-BASED ORDER",
        heuristic_order,
        colouring2,
        stats2
    )

    # ---------------------------------------------------------
    # Comparison
    # ---------------------------------------------------------

    print("\n" + "-" * 70)
    print("VERSION COMPARISON")
    print("-" * 70)

    print(
        "Search Nodes:",
        stats1.search_nodes,
        "->",
        stats2.search_nodes
    )

    print(
        "Candidate Assignments:",
        stats1.candidate_assignments,
        "->",
        stats2.candidate_assignments
    )

    print(
        "Rejected Branches:",
        stats1.rejected_branches,
        "->",
        stats2.rejected_branches
    )

    print(
        "Backtracks:",
        stats1.backtracks,
        "->",
        stats2.backtracks
    )

    print(
        "Maximum Depth:",
        stats1.max_depth,
        "->",
        stats2.max_depth
    )

    if stats2.search_nodes < stats1.search_nodes:
        print(
            "Observation: The degree-based ordering reduced "
            "the number of search nodes."
        )

    elif stats2.search_nodes > stats1.search_nodes:
        print(
            "Observation: The degree-based ordering increased "
            "the number of search nodes for this instance."
        )

    else:
        print(
            "Observation: Both versions visited the same "
            "number of search nodes."
        )


def main():

    print("=" * 70)
    print("CO5 ASSIGNMENT 5")
    print("TASK B1 - INSTRUMENTED GRAPH COLOURING")
    print("=" * 70)

    # ---------------------------------------------------------
    # TEST CASE 1
    # Colourable Graph
    # ---------------------------------------------------------

    graph1 = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3],
        [1, 2]
    ]

    run_test(
        "TEST CASE 1 - COLOURABLE GRAPH",
        graph1,
        3
    )

    # ---------------------------------------------------------
    # TEST CASE 2
    # Non-Colourable Graph
    #
    # Complete graph K4 requires 4 colours.
    # It cannot be coloured using only 3 colours.
    # ---------------------------------------------------------

    graph2 = [
        [1, 2, 3],
        [0, 2, 3],
        [0, 1, 3],
        [0, 1, 2]
    ]

    run_test(
        "TEST CASE 2 - NOT COLOURABLE WITH 3 COLOURS",
        graph2,
        3
    )

    # ---------------------------------------------------------
    # TEST CASE 3
    # Boundary Case
    #
    # A single vertex graph requires only one colour.
    # ---------------------------------------------------------

    graph3 = [
        []
    ]

    run_test(
        "TEST CASE 3 - BOUNDARY CASE",
        graph3,
        1
    )

    print("\n")
    print("=" * 70)
    print("FINAL COMPLEXITY ANALYSIS")
    print("=" * 70)

    print("Worst-Case Time Complexity: O(M^V)")
    print("Space Complexity: O(V)")
    print()
    print("V = Number of vertices")
    print("M = Number of available colours")


if __name__ == "__main__":
    main()
