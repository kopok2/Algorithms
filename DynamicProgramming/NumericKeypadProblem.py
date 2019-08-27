# coding=utf-8
"""Numeric keypad problem dynamic programming solution Python implementation."""


def nmkp(keypad, n):
    if not n or not keypad:
        return 0
    elif n == 1:
        return 10
    dpo = [1] * 10
    dpe = [0] * 10
    uo = 0
    for j in range(2, n + 1):
        uo = 1 - uo
        if uo == 1:
            dpe[0] = dpo[0] + dpo[8]
            dpe[1] = dpo[1] + dpo[2] + dpo[4]
            dpe[2] = dpo[2] + dpo[1] + dpo[3] + dpo[5]
            dpe[3] = dpo[3] + dpo[2] + dpo[6]
            dpe[4] = dpo[4] + dpo[1] + dpo[5] + dpo[7]
            dpe[5] = dpo[5] + dpo[2] + dpo[4] + dpo[8] + dpo[6]
            dpe[6] = dpo[6] + dpo[9] + dpo[3] + dpo[5]
            dpe[7] = dpo[7] + dpo[4] + dpo[8]
            dpe[8] = dpo[8] + dpo[0] + dpo[7] + dpo[5] + dpo[9]
            dpe[9] = dpo[9] + dpo[8] + dpo[6]
        else:
            dpo[0] = dpe[0] + dpe[8]
            dpo[1] = dpe[1] + dpe[2] + dpe[4]
            dpo[2] = dpe[2] + dpe[1] + dpe[3] + dpe[5]
            dpo[3] = dpe[3] + dpe[2] + dpe[6]
            dpo[4] = dpe[4] + dpe[1] + dpe[5] + dpe[7]
            dpo[5] = dpe[5] + dpe[2] + dpe[4] + dpe[8] + dpe[6]
            dpo[6] = dpe[6] + dpe[9] + dpe[3] + dpe[5]
            dpo[7] = dpe[7] + dpe[4] + dpe[8]
            dpo[8] = dpe[8] + dpe[0] + dpe[7] + dpe[5] + dpe[9]
            dpo[9] = dpe[9] + dpe[8] + dpe[6]
    return sum(dpe) if uo else sum(dpo)


if __name__ == "__main__":
    keyboard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]
    for row in keyboard:
        print(row)
    for x in range(5):
        print(x + 1, nmkp(keyboard, x + 1))
