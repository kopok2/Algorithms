# coding=utf-8
"""Sudoku Backtracking Algorithm solution Python implementation."""

N = 9 # Sudoku size

def used_in_row(grid, row, num):
    return num in grid[row]


def used_in_col(grid, col, num):
    for r in range(N):
        if grid[r][col] == num:
            return True
    return False


def used_in_box(grid, bsr, bsc, num):
    for r in range(3):
        for c in range(3):
            if grid[r + bsr][c + bsc] == num:
                return True
    return False


def is_safe(grid, row, col, num):
    return (not used_in_row(grid, row, num)) and (not used_in_col(grid, col, num)) and\
           (not used_in_box(grid, row - row % 3, col - col % 3, num)) and (not grid[row][col])



def find_unassigned_location(grid):
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                return i, j
    return False


def solve_sudoku(grid):
    r_c = find_unassigned_location(grid)
    if not r_c:
        return True
    else:
        row, col = r_c[0], r_c[1]
        for num in range(1, 10):
            if is_safe(grid, row, col, num):
                grid[row][col] = num
                if solve_sudoku(grid):
                    return True
                else:
                    grid[row][col] = False
        return False


if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if solve_sudoku(grid):
        for r in grid:
            print(r)
    else:
        print("No solution exists.")
