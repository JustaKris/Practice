# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.


def gridChallenge(grid):
    # Sort characters in each row
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    # Check if columns are sorted
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i - 1][j]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)


"""Sample Input 1
1
5
ebacd
fghij
olmkn
trpqs
xywuv
"""

"""Sample Input 2
3
3
abc
lmp
qrt
3
mpxz
abcd
wlmf
4
abc
hjk
mpq
rtv
"""