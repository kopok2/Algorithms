# coding=utf-8
"""Knapsack Problem Python solution."""


def knapsack(capacity, weights, values):
    dp = [[0 for x in range(capacity + 1)] for y in range(len(weights) + 1)]
    for x in range(len(weights) + 1):
        for y in range(capacity + 1):
            if not x or not y:
                dp[x][y] = 0
            elif weights[x - 1] <= y:
                dp[x][y] = max(values[x - 1] + dp[x - 1][y - weights[x - 1]], dp[x - 1][y])
            else:
                dp[x][y] = dp[x - 1][y]
    return dp[len(weights)][capacity]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print(knapsack(capacity, weights, values))
