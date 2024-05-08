# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # If n has only one digit, return n
    if len(n) == 1:
        return int(n)

    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in n)

    # Repeat the process if k > 1
    if k > 1:
        digit_sum *= k

    # Recursively calculate super digit
    return superDigit(str(digit_sum), 1)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)

"""Test Case 1
9875 4
"""

"""Test Case 2
123 3
"""
