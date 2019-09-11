# coding=utf-8
"""Knight Tour Problem Backtracking Algorithm solution Python implementation."""

N = 8 # board size


def is_safe(x, y, sol):
    if 0 <= x < N and 0 <= y < N:
        if sol[x][y] == -1:
            return True
        else:
            return False
    else:
        return False


def solve_util(x, y, move, sol, xmove, ymove):
    if move == N * N:
        return True
    for k in range(N):
        next_x = x + xmove[k]
        next_y = y + ymove[k]

        if is_safe(next_x, next_y, sol):

            sol[next_x][next_y] = move
            if solve_util(next_x, next_y, move + 1, sol, xmove, ymove):
                return True
            else:
                sol[next_x][next_y] = -1
    return False


def kt():
    sol = [[-1] * N for x in range(N)]
    xmove = [2, 1, -1, -2, -2, -1, 1, 2]
    ymove = [1, 2, 2, 1, -1, -2, -2, -1]
    sol[0][0] = 0
    solve_util(0, 0, 1, sol, xmove, ymove)
    for row in sol:
        print(row)


if __name__ == "__main__":
    kt()
