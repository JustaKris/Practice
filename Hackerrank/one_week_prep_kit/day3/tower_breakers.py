# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        print(result)

"""Test Case 1
2
2 2
1 4
"""
"""Test Case 2
2
1 7
3 7
"""
"""Test Case 3
2
1 7
3 7
"""
