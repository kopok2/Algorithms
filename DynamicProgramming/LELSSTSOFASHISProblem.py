# coding=utf-8
"""DP problem solution Python implementation."""


def lelsst(string):
    ans = 0
    n = len(string)
    for i in range(n - 1):
        l, r = i, i + 1
        lsum = 0
        rsum = 0
        while r < n and l >= 0:
            lsum += int(string[l])
            rsum += int(string[r])
            if lsum == rsum:
                ans = max(ans, r - l + 1)
            l -= 1
            r += 1
    return ans


if __name__ == "__main__":
    print(lelsst("777123123777"))
