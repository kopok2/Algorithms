# coding=utf-8
"""Naive Pattern Searching algorithm Python implementation."""


def search(pattern, text):
    """Search for pattern occurrences in text.

    Args:
        pattern: pattern string to be searched (str).
        text: text string to be searched on (str).

    Returns:
        list of indexes of all occurrences.
    """
    result = []
    for x in range(len(text) - len(pattern)):
        if text[x] == pattern[0]:
            valid = True
            for y in range(1, len(pattern)):
                if text[x + y] != pattern[y]:
                    valid = False
                    break
            if valid:
                result.append(x)

    return result


if __name__ == "__main__":
    example_text = "AABAACAADAABAAABAA"
    example_pattern = "AABA"
    print(search(example_pattern, example_text))
