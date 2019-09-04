# coding=utf-8
"""Anagram Substring Search algorithm Python implementation."""

ALPHABET_SIZE = 256


def compare(ar1, ar2):
    return str(ar1) == str(ar2)


def search(pattern, text):
    m = len(pattern)
    n = len(text)
    cnt_p = [0] * ALPHABET_SIZE
    cnt_t = [0] * ALPHABET_SIZE
    for i in range(m):
        cnt_p[ord(pattern[i])] += 1
        cnt_t[ord(text[i])] += 1
    results = []
    for i in range(m, n):
        if compare(cnt_p, cnt_t):
            results.append(i - m)
        cnt_t[ord(text[i])] += 1
        cnt_t[ord(text[i - m])] -= 1
    if compare(cnt_t, cnt_p):
        results.append(n - m)
    return results


if __name__ == "__main__":
    example_text = "BACDGABCDA"
    example_pattern = "ABCD"
    print(search(example_pattern, example_text))
