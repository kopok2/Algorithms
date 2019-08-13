# coding=utf-8
"""Find set of coins that constitutes given sum."""


def coins(coin_set, ammount):
    result = []
    coin_set.sort(reverse=True)
    while ammount:
        while coin_set[0] > ammount:
            coin_set.pop(0)
        result += [str(coin_set[0]) for x in range(ammount // coin_set[0])]
        ammount -= (ammount // coin_set[0]) * coin_set[0]
    return result


if __name__ == "__main__":
    coinset = [1, 2, 5, 10, 20, 100, 200]
    print(coins(coinset, 1453))
