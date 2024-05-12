import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    heapq.heapify(A)  # Convert the list into a min-heap
    operations = 0

    while len(A) > 1:
        if A[0] >= k:
            return operations

        # Extract the two cookies with the least sweetness
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)

        # Combine the cookies and calculate the new sweetness
        new_cookie = least_sweet + (2 * second_least_sweet)
        operations += 1

        # Add the new cookie back to the heap
        heapq.heappush(A, new_cookie)

    if A[0] >= k:
        return operations
    else:
        return -1  # If it's not possible to reach sweetness k


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)


"""Sample Input 1
6 7
1 2 3 9 10 12
"""

"""

"""
