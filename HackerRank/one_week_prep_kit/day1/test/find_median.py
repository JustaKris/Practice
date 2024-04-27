#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    median_index = len(arr) // 2
    sorted_arr = sorted(arr)
    median = sorted_arr[median_index]
    return median


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)

"""Test Case 1
7
1 2 4 5 3 6 7
"""
