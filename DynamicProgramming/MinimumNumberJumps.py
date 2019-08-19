# coding=utf-8
"""Minimum number jumps problem dynamic programming solution Python implementation."""


def min_jumps(array):
    inf = len(array) + 1
    dp = [inf for x in range(len(array))]
    dp[0] = 0
    for x in range(1, len(array)):
        for y in range(x):
            if array[y] + y >= x:
                dp[x] = min(dp[x], dp[y] + 1)
    return dp[len(array) - 1]


if __name__ == "__main__":
    array = [1, 3, 6, 1, 0, 9]
    print(min_jumps(array))
