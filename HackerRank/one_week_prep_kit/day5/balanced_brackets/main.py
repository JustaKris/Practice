# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack or stack[-1] != closing_brackets[bracket]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)

"""Sample Input 1
3
{[()]}
{[(])}
{{[[(())]]}}
"""

"""Sample Input 2
3
{(([])[])[]}
{(([])[])[]]}
{(([])[])[]}[]
"""
