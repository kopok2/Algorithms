# coding=utf-8
"""Boolean parenthesization problem dynamic programming solution Python implementation."""


def bpw(var, expr):
    n = len(var)
    dpt = [[0 for x in range(n)] for y in range(n)]
    dpf = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        dpf[i][i] = 1 if var[i] else 0
        dpt[i][i] = 0 if var[i] else 1
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            dpt[i][j] = dpf[i][j] = 0
            for g in range(gap):
                k = i + g
                tik = dpt[i][k] + dpf[i][k]
                tkj = dpt[k + 1][j] + dpf[k + 1][j]
                if expr[k] == "&":
                    dpt[i][j] += dpt[i][k] * dpt[k + 1][j]
                    dpf[i][j] += tik * tkj - dpt[i][k] * dpt[k + 1][j]
                if expr[k] == "|":
                    dpf[i][j] += dpf[i][k] * dpf[k + 1][j]
                    dpt[i][j] += tik * tkj - dpf[i][k] * dpf[k + 1][j]
                if expr[k] == "^":
                    dpt[i][j] += dpf[i][k] * dpt[k + 1][j] + dpt[i][k] * dpf[k + 1][j]
                    dpt[i][j] += dpt[i][k] * dpt[k + 1][j] + dpf[i][k] * dpf[k + 1][j]
            i += 1
    return dpt[0][n - 1]


if __name__ == "__main__":
    var = [True, True, False, True]
    expr = ["|", "&", "^"]
    print(bpw(var, expr))
