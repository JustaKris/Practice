# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

"""Test Case 1
2
5
2 1 5 3 4
5
2 5 1 3 4
"""

"""Test Case 2
1
8
1 2 5 3 4 7 8 6
"""
