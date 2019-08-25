# coding=utf-8
"""Subset sum problem dynamic programming solution Python implementation."""


def has_subset_sum(array, sum_target):
    n = len(array)
    dp = [[False for x in range(sum_target + 1)] for y in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, sum_target + 1):
        dp[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum_target + 1):
            if j < array[i - 1]:
                dp[i][j] = dp[i - 1][j]
            if j >= array[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - array[i - 1]]
    return dp[n][sum_target]


if __name__ == "__main__":
    array = [3, 34, 4, 12, 5, 2]
    print(has_subset_sum(array, 9))
    print(has_subset_sum(array, 40))
    print(has_subset_sum(array, 47))
