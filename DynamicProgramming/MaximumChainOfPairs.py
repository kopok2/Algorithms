# coding=utf-8
"""Maximum length chain of pairs dynamic programming solution Python implementation."""


def mlcp(pairs):
    n = len(pairs)
    mcl = [1 for x in range(n)]
    for i in range(1, n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1] and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1
    mx = 0
    for i in range(n):
        mx = max(mx, mcl[i])
    return mx


if __name__ == "__main__":
    arr = [[5, 24], [15, 25], [27, 40], [50, 60]]
    print(mlcp(arr))
