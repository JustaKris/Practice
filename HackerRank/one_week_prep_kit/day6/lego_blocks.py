# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# Function to generate all possible block configurations

MOD = 10**9 + 7


def generate_block_configs(m):
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
        if i >= 3:
            dp[i] = (dp[i] + dp[i - 3]) % MOD
        if i >= 4:
            dp[i] = (dp[i] + dp[i - 4]) % MOD
    return dp


def legoBlocks(n, m):
    block_configs = generate_block_configs(m)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = block_configs[m]
        for j in range(1, i):
            dp[i] = (dp[i] - dp[j] * block_configs[m - (i - j)]) % MOD
    return dp[n]


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)
        print(result)