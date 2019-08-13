# coding=utf-8
"""Longest common subsequence dynamic programming Python implementation."""


def lcs(seq1, seq2):
    """Find length of longest common subsequence in two sequences."""
    dp = [[None for x in range(len(seq2) + 1)] for y in range(len(seq1) + 1)]
    for x in range(len(seq1) + 1):
        for y in range(len(seq2) + 1):
            if not x or not y:
                dp[x][y] = 0
            elif seq1[x - 1] == seq2[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
    for d in dp:
        print(d)
    return dp[len(seq1)][len(seq2)]


if __name__ == "__main__":
    a1 = "AGGTAB"
    a2 = "GXTXAYB"
    print(lcs(a1, a2))
