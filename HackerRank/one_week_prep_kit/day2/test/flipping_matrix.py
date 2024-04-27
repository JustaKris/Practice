# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

def flippingMatrix(matrix) -> int:
    n = len(matrix) // 2  # Calculate the size of the submatrix
    # Iterate over each quadrant
    total_sum = 0
    for i in range(n):
        for j in range(n):
            # Select the maximum element from each quadrant and add it to the total sum
            total_sum += max(matrix[i][j], matrix[i][2 * n - 1 - j], matrix[2 * n - 1 - i][j],
                             matrix[2 * n - 1 - i][2 * n - 1 - j])
    return total_sum


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        print(str(result) + '\n')


""" Test Input 1
1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108
"""