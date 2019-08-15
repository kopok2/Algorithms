# coding=utf-8
"""Longest palindromic subsequence dynamic programming solution Python implementation."""


def lps(seq):
    dp = [[0 if x != y else 1for y in range(len(seq) + 1)] for x in range(len(seq) + 1)]
    for cl in range(2, len(seq) + 1):
        for i in range(len(seq) - cl):
            j = i + cl - 1
            if seq[i] == seq[j] and cl == 2:
                dp[i][j] = 2
            elif seq[i] == seq[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][len(seq) - 2]


if __name__ == "__main__":
    seq = "GEEKS FOR GEEKS"
    print(lps(seq))
