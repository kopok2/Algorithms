# coding=utf-8
"""All String Permutations using Backtracking Algorithm Python implementation."""


def permute(string, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(string) - 1
    string = list(string)
    if l == r:
        print("".join(string))
    else:
        for i in range(l, r + 1):
            string[l], string[i] = string[i], string[l]
            permute(string, l + 1, r)
            string[l], string[i] = string[i], string[l]


if __name__ == "__main__":
    permute("ABC")
    print("#" * 64)
    permute("SEMIR")
