# Module 4 - Strassen Matrix Multiplication
# CO3 AT3 - Divide and Conquer
# KartIQ Retail Data Analytics Platform

def add_matrix(A, B):
    n = len(A)

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result


def subtract_matrix(A, B):
    n = len(A)

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(A[i][j] - B[i][j])

        result.append(row)

    return result


def split_matrix(A):
    n = len(A)
    mid = n // 2

    A11 = []
    A12 = []
    A21 = []
    A22 = []

    for i in range(mid):
        A11.append(A[i][:mid])
        A12.append(A[i][mid:])

    for i in range(mid, n):
        A21.append(A[i][:mid])
        A22.append(A[i][mid:])

    return A11, A12, A21, A22


def combine_matrix(C11, C12, C21, C22):
    n = len(C11)

    result = []

    for i in range(n):
        result.append(C11[i] + C12[i])

    for i in range(n):
        result.append(C21[i] + C22[i])

    return result


def conventional_multiply(A, B):
    n = len(A)

    result = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


def strassen(A, B):
    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide matrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Seven Strassen products
    M1 = strassen(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2 = strassen(
        add_matrix(A21, A22),
        B11
    )

    M3 = strassen(
        A11,
        subtract_matrix(B12, B22)
    )

    M4 = strassen(
        A22,
        subtract_matrix(B21, B11)
    )

    M5 = strassen(
        add_matrix(A11, A12),
        B22
    )

    M6 = strassen(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7 = strassen(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    # Calculate result submatrices
    C11 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M4),
            M5
        ),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        add_matrix(
            subtract_matrix(M1, M2),
            M3
        ),
        M6
    )

    # Combine result
    return combine_matrix(
        C11,
        C12,
        C21,
        C22
    )


def print_matrix(matrix):
    for row in matrix:
        print(row)


def run_test(test_name, A, B):

    print("\n" + "=" * 60)
    print(test_name)
    print("=" * 60)

    print("\nMatrix A:")
    print_matrix(A)

    print("\nMatrix B:")
    print_matrix(B)

    result = strassen(A, B)

    print("\nStrassen Matrix Multiplication Result:")
    print_matrix(result)

    conventional_result = conventional_multiply(A, B)

    print("\nConventional Matrix Multiplication Result:")
    print_matrix(conventional_result)

    if result == conventional_result:
        print("\nVerification: PASSED")
    else:
        print("\nVerification: FAILED")


def main():

    print("KARTIQ RETAIL DATA ANALYTICS PLATFORM")
    print("STRASSEN MATRIX MULTIPLICATION")

    # Test Case 1 - 2 x 2 matrices
    A1 = [
        [1, 2],
        [3, 4]
    ]

    B1 = [
        [5, 6],
        [7, 8]
    ]

    run_test(
        "TEST CASE 1 - 2 x 2 MATRICES",
        A1,
        B1
    )

    # Test Case 2 - 4 x 4 matrices
    A2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    B2 = [
        [16, 15, 14, 13],
        [12, 11, 10, 9],
        [8, 7, 6, 5],
        [4, 3, 2, 1]
    ]

    run_test(
        "TEST CASE 2 - 4 x 4 MATRICES",
        A2,
        B2
    )

    # Test Case 3 - Small values
    A3 = [
        [2, 0],
        [1, 3]
    ]

    B3 = [
        [1, 4],
        [2, 5]
    ]

    run_test(
        "TEST CASE 3 - SMALL VALUE MATRICES",
        A3,
        B3
    )

    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)

    print("Conventional Matrix Multiplication : O(n^3)")
    print("Strassen Matrix Multiplication    : O(n^log2(7))")
    print("Approximate Strassen Complexity   : O(n^2.807)")
    print("Auxiliary Space Complexity        : O(n^2)")

    print("\nRecurrence Relation:")
    print("T(n) = 7T(n/2) + O(n^2)")


if __name__ == "__main__":
    main()
