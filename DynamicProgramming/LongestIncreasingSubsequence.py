# coding=utf-8
"""Longest increasing subsequence dynamic programming solution."""


def lis(array):
    _li = [0 for x in range(len(array))]
    for i in range(len(array)):
        _li[i] = 1
        for j in range(len(array)):
            if array[i] > array[j] and _li[i] < _li[j] + 1:
                _li[i] = _li[j] + 1
    return max(_li)


if __name__ == "__main__":
    ar = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(ar))
