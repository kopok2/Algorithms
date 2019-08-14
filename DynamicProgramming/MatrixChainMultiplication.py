# coding=utf-8
"""Given a sequence of matrix find most efficient way to multiply these matrices together."""


def low_op(chain):
    dp = [[0 for x in range(len(chain))] for y in range(len(chain))]
    for l in range(2, len(chain)):
        for i in range(1, len(chain) - l + 1):
            j = i + l - 1
            dp[i][j] = 99999999999999999999999999999999999999999
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + chain[i - 1] * chain[k] * chain[j]
            if q < dp[i][j]:
                dp[i][j] = q
    return dp[1][len(chain) - 1]


if __name__ == "__main__":
    chain = [10, 20, 30, 40, 30]
    print(low_op(chain))
