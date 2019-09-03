# coding=utf-8
"""KMP pattern searching.

Knuth Morris Pratt Pattern Searching algorithm Python implementation.
"""


def compute_lps_array(pattern, m, lps):
    """Prepocess pattern to the form used by KMP algorithm."""
    len_ = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i += 1


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
    lps = [0] * m
    compute_lps_array(pattern, m, lps)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return result


if __name__ == "__main__":
    example_text = "AABAACAADAABAAABAA"
    example_pattern = "AABA"
    print(search(example_pattern, example_text))
