# coding=utf-8
"""Rabing-Karp Pattern Searching algorithm Python implementation."""

# Prime number
Q = 101
# Alphabet size
D = 256


def search(pattern, text):
    """Search for pattern occurrences in text.

    Args:
        pattern: pattern string to be searched (str).
        text: text string to be searched on (str).

    Returns:
        list of indexes of all occurrences.
    """
    result = []
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0
    t = 0
    for i in range(m - 1):
        h = (h * D) % Q
    for i in range(m):
        p = (D * p + ord(pattern[i])) % Q
        t = (D * t + ord(text[i])) % Q

    for i in range(n - m + 1):
        if p == t:
            valid = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    valid = False
                    break
            if valid:
                result.append(i)
        if i < n - m:
            t = (D * (t - ord(text[i]) * h) + ord(text[i + m])) % Q
            if t < 0:
                t += Q

    return result


if __name__ == "__main__":
    example_text = "AABAACAADAABAAABAA"
    example_pattern = "AABA"
    print(search(example_pattern, example_text))
