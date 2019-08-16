# coding=utf-8
"""Longest bitonic subsequence dynamic programming solution Python implementation."""


def lbs(sequence):
    lis = [1 for x in range(len(sequence))]
    lds = [1 for x in range(len(sequence))]
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    for i in range(len(sequence) - 2, -1, -1):
        for j in range(len(sequence) - 1, i, -1):
            if sequence[i] > sequence[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    mx = 0
    for i in range(len(sequence)):
        mx = max(mx, lis[i] + lds[i] - 1)
    return mx


if __name__ == "__main__":
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(lbs(arr))
