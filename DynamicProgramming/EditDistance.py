# coding=utf-8
"""Edit distance problem Python solution."""


def edit_dist(s1, s2):
    dp = [[None for y in range(len(s2) + 1)] for x in range(len(s1) + 1)]
    for x in range(len(s1) + 1):
        for y in range(len(s2) + 1):
            if not x:
                dp[x][y] = y
            elif not y:
                dp[x][y] = x
            elif s1[x - 1] == s2[y - 1]:
                dp[x][y] = dp[x - 1][y - 1]
            else:
                dp[x][y] = 1 + min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1])
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    s1 = "sunday"
    s2 = "saturday"
    print(edit_dist(s1, s2))
