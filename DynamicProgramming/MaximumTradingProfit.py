# coding=utf-8
"""Maximum trade profit problem dynamic programming solution Python implementation."""


def mx_profit(prices):
    n = len(prices)
    profit = [0] * n
    mxp = prices[n - 1]
    for i in range(n - 2, -1, -1):
        mxp = max(mxp, prices[i])
        profit[i] = max(profit[i + 1], mxp - prices[i])
    mnp = prices[0]
    for i in range(1, n):
        mnp = min(mnp, prices[i])
        profit[i] = max(profit[i - 1], profit[i] + (prices[i] - mnp))
    return profit[n - 1]


if __name__ == "__main__":
    prices = [2, 30, 15, 10, 8, 25, 80]
    print(mx_profit(prices))
