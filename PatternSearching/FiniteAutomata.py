# coding=utf-8
"""Finite Automata Python implementation."""

ALPHABET_SIZE = 255


def compute_trans_fun(pattern, m, TF):
    lps = 0
    TF[0][ord(pattern[0])] = 1
    for i in range(1, m):
        for x in range(ALPHABET_SIZE):
            #print(i, x)
            TF[i][x] = TF[lps][x]
        TF[i][ord(pattern[i])] = i + 1
        if i < m:
            lps = TF[lps][ord(pattern[i])]


def search(pattern, text):
    m = len(pattern)
    n = len(text)
    TF = [[0] * ALPHABET_SIZE for x in range(m + 1)]
    compute_trans_fun(pattern, m, TF)
    j = 0
    results = []
    for i in range(n):
        j = TF[j][ord(text[i])]
        if j == m:
            results.append(i - m + 1)
    return results


if __name__ == "__main__":
    example_text = "AABAACAADAABAAABAAAAABA"
    example_pattern = "AABA"
    print(search(example_pattern, example_text))
