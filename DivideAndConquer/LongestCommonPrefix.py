# coding=utf-8
"""Longest Common Prefix Problem Divide and Conquer algorithm solution Python implementation."""


def cmn_u(s1, s2):
    result = ""
    n1, n2 = len(s1), len(s2)
    i, j = 0, 0
    while i <= n1 - 1 and j <= n2 - 1:
        if s1[i] != s2[j]:
            break
        result += s1[i]
        i += 1
        j += 1
    return result


def lcp(arr, l, h):
    if l == h:
        return arr[l]
    if h > l:
        m = l + (h - l) // 2
        s1 = lcp(arr, l, m)
        s2 = lcp(arr, m + 1, h)
        return cmn_u(s1, s2)


if __name__ == "__main__":
    print(lcp(["abcde", "abcdddddd", "abcdejffj", "abcd[[[[d"], 0, 3))
