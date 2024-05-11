# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def pairs(k, arr):
    pairs_count = 0
    arr_set = set(arr)

    for num in arr_set:
        if num + k in arr_set:
            pairs_count += 1

    return pairs_count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)


""" Sample Input 1
5 2
1 5 3 4 2
"""
