# coding=utf-8
"""Weighted Job Scheduling problem dynamic programmin solution Python implementation."""

from operator import itemgetter


def lnc(schedule, i):
    for j in range(i - 1, -1, -1):
        if schedule[j][1] <= schedule[i][0]:
            return j
    return -1


def wjs(schedule):
    schedule.sort(key=itemgetter(1))
    n = len(schedule)
    dp = [0] * n
    dp[0] = schedule[0][2]
    for i in range(1, n):
        incl_prof = schedule[i][2]
        latest = lnc(schedule, i)
        if latest != -1:
            incl_prof += dp[latest]
        dp[i] = max(incl_prof, dp[i - 1])
    return dp[n - 1]


if __name__ == "__main__":
    schedule = [
        (3, 10, 20),
        (1, 2, 50),
        (6, 19, 100),
        (2, 100, 200)
    ]
    print(wjs(schedule))
