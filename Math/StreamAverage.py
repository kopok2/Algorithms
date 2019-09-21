# coding=utf-8
"""Stream average."""


def stream_average(stream):
    result = []
    ss = 0
    n = 0
    for a in stream:
        n += 1
        ss += a
        result.append(ss / n)
    return result


if __name__ == '__main__':
    print(stream_average([10, 20, 30, 40, 50, 60, 80]))
