# coding=utf-8
"""Partition problem dynamic programming solution Python implementation."""


def has_partition(array):
    ss = sum(array)
    if ss % 2:
        return False
    else:
        dp = [[False for y in range(ss // 2 + 1)] for y in range(len(array) + 1)]
        for x in range(len(array) + 1):
            dp[x][0] = True
        for x in range(ss // 2 + 1):
            for y in range(len(array) + 1):
                dp[y][x] = dp[y - 1][x]
                if x >= array[y - 1]:
                    dp[y][x] = dp[y][x] or dp[y - 1][x - array[y - 1]]
        return dp[len(array)][ss // 2]


if __name__ == "__main__":
    array = [3, 1, 1, 2, 2, 1]
    print(has_partition(array))
    array = [3, 1, 1, 2, 2, 100]
    print(has_partition(array))
