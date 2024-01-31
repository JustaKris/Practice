# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    n = len(arr)

    # Calculate sums for both diagonals
    primary_diagonal_sum = sum(arr[i][i] for i in range(n))
    secondary_diagonal_sum = sum(arr[i][n - 1 - i] for i in range(n))

    # Calculate the absolute difference
    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return absolute_difference


if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

"""Test Case 1
3
11 2 4
4 5 6
10 8 -12
"""
