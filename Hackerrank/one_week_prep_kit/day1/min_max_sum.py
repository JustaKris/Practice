#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):

    sorted_arr = sorted(arr)

    print(sum(sorted_arr[:4]), end=" ")
    print(sum(sorted_arr[-4:]))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

"""Test Case 1
1 2 3 4 5
"""

"""Test Case 2
7 69 2 221 8974
"""
