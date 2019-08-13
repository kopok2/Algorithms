# coding=utf-8
"""Job sequencing problem Python solution."""

from operator import itemgetter


def schedule(tasks):
    tasks.sort(key=itemgetter(2), reverse=True)
    to_do = [tasks[0][0]]
    time = 1
    profit = tasks[0][2]
    for x in range(1, len(tasks)):
        if tasks[x][1] >= time:
            time += 1
            to_do.append(tasks[x][0])
            profit += tasks[x][2]
    return profit, to_do


if __name__ == "__main__":
    tasks = [
        ('a',      4,        20),
        ('b',      1,        10),
        ('c',      1,        40),
        ('d',      1,        30),
    ]
    print(schedule(tasks))

    tasks = [
        ('a',       2,        100),
        ('b',       1,        19),
        ('c',       2,        27),
        ('d',       1,        25),
        ('e',       3,        15)
    ]
    print(schedule(tasks))
