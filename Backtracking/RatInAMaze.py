# coding=utf-8
"""Rat in a Maze Problem Bactracking Algorithm Solution Python implementation."""

N = 4 # maze size


def solve_maze(maze):
    sol = [[0] * N for x in range(N)]
    if not solve_maze_util(maze, 0, 0, sol):
        print("No solution exists.")
    else:
        for row in sol:
            print(row)


def is_safe(maze, x, y):
    if 0 <= x < N and 0 <= y < N:
        if maze[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


def solve_maze_util(maze, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True
    if is_safe(maze, x, y):
        sol[x][y] = 1
        if solve_maze_util(maze, x + 1, y, sol):
            return True
        if solve_maze_util(maze, x, y + 1, sol):
            return True
        sol[x][y] = 0
        return False
    return False


if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1]]
    solve_maze(maze)
