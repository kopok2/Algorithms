# coding=utf-8


def day_of_week(d, m, y):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 3, 6, 2, 4]
    if m < 3:
        y -= 1
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7


if __name__ == '__main__':
    print(day_of_week(30, 8, 2010))
    print(day_of_week(22, 9, 2019))
