# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            result += char
    return result


if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

"""Test Case 1
11
middle-Outz
2
"""
"""Test Case 2
38
Always-Look-on-the-Bright-Side-of-Life
5
"""
