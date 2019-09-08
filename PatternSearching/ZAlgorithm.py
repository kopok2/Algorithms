# coding=utf-8
"""Z Algorithm Python implementation."""


def getzarr(cnc, Z):
    n = len(cnc)
    L = 0
    R = 0
    for i in range(1, n):
        if i > R:
            L = i
            R = i
            while True:
                if R >= n:
                    break
                if cnc[R - L] != cnc[R]:
                    break
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while True:
                    if R >= n:
                        break
                    if cnc[R - L] != cnc[R]:
                        break
                    R += 1
                Z[i] = R - L
                R -= 1


def search(pattern, text):
    """Search for pattern occurrences in text.

    Args:
        pattern: pattern string to be searched (str).
        text: text string to be searched on (str).

    Returns:
        list of indexes of all occurrences.
    """
    cnc = pattern + "$" + text
    l = len(cnc)
    Z = [0] * l
    getzarr(cnc, Z)
    results = []
    for i in range(l):
        if Z[i] == len(pattern):
            results.append(i - len(pattern) - 1)
    return results


if __name__ == "__main__":
    example_text = "AABAACAADAABAAABAA"
    example_pattern = "AABA"
    print(search(example_pattern, example_text))
