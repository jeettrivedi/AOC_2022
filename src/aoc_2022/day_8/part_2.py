from .part_1 import parse_and_transpose_grid
from typing import List


def compute_scenic_score(row: List, col: List, pos: List):
    row = [tree_height - row[pos[0]] for tree_height in row]
    col = [tree_height - col[pos[1]] for tree_height in col]

    view_left = 0
    view_right = 0
    view_top = 0
    view_bottom = 0
    for i in range(pos[0] - 1, -1, -1):
        if row[i] >= 0:
            view_left += 1
            break
        view_left += 1

    for i in range(pos[0] + 1, len(row)):
        if row[i] >= 0:
            view_right += 1
            break
        view_right += 1

    for i in range(pos[1] - 1, -1, -1):
        if col[i] >= 0:
            view_top += 1
            break
        view_top += 1

    for i in range(pos[1] + 1, len(col)):
        if col[i] >= 0:
            view_bottom += 1
            break
        view_bottom += 1

    return view_left * view_right * view_top * view_bottom


def sol(input_file_path: str):
    (grid, grid_T) = parse_and_transpose_grid(input_file_path)
    grid_size = len(grid)
    max_scenic_score = 0
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            max_scenic_score = max(
                max_scenic_score,
                compute_scenic_score(grid[i], grid_T[j], [j, i]),
            )
    return max_scenic_score
