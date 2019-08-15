# coding=utf-8
"""Maximum sum increasing subsequence dynamic programming solution Python implementation."""


def msis(seq):
    dp = [x for x in seq]
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j] and dp[i] < dp[j] + seq[i]:
                dp[i] = dp[j] + seq[i]
    return max(dp)


if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100, 4, 5]
    print(msis(arr))
