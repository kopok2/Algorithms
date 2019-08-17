# coding=utf-8
"""Palindrome partitioning dynamic programming solution Python implementation."""


def pal_part(pal_str):
    n = len(pal_str)
    cuts = [[0 for y in range(n)] for x in range(n)]
    palindrome = [[False for y in range(n)] for x in range(n)]
    for x in range(n):
        palindrome[x][x] = True
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 2:
                palindrome[i][j] = pal_str[i] == pal_str[j]
            else:
                palindrome[i][j] = pal_str[i] == pal_str[j] and palindrome[i + 1][j - 1]
            if palindrome[i][j]:
                cuts[i][j] = 0
            else:
                cuts[i][j] = n + 1
                for k in range(i, j):
                    cuts[i][j] = min(cuts[i][j], cuts[i][k] + cuts[k + 1][j] + 1)
    return cuts[0][n - 1]


if __name__ == "__main__":
    astr = "ababbbabbababa"
    print(pal_part(astr))
