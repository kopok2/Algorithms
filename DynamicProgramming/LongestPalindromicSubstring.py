# coding=utf-8
"""Longest palindromic substring dynamic programming solution Python implementation."""


def lps(string):
    n = len(string)
    dp = [[False for x in range(n)] for y in range(n)]
    mx = 1
    for x in range(n):
        dp[x][x] = True
    start = 0
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = True
            start = i
            mx = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and string[i] == string[j]:
                dp[i][j] = True
                if k > mx:
                    start = i
                    mx = k
    return string[start:start + mx]


if __name__ == "__main__":
    string = "semirrimessss"
    print(lps(string))
