# coding=utf-8
"""Given start and finish times select the maximum number of activities that can be performed."""

from operator import itemgetter
from random import randrange


def activity_selection(times):
    times.sort(key=itemgetter(1), reverse=True)
    selected = [times.pop()]
    finish_time = selected[0][1]
    while times:
        time = times.pop()
        if time[0] >= finish_time:
            finish_time = time[1]
            selected.append(time)
    return selected


if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    s_f_times = [(start[x], finish[x]) for x in range(len(start))]
    print(activity_selection(s_f_times))

    start = [randrange(1, 1000) for x in range(100)]
    finish = [start[x] + randrange(1, 50) for x in range(100)]
    s_f_times = [(start[x], finish[x]) for x in range(len(start))]
    print(activity_selection(s_f_times))
