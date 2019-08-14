# coding=utf-8
"""Given coin set calculate ways of expressing given ammount of money."""


def count_coins(coins, value):
    dp = [0 for x in range(value + 1)]
    dp[0] = 1
    for x in range(len(coins)):
        for y in range(coins[x], value + 1):
            dp[y] += dp[y - coins[x]]
    return dp[value]


if __name__ == "__main__":
    coins = [1, 2, 3]
    val = 4
    print(count_coins(coins, val))
