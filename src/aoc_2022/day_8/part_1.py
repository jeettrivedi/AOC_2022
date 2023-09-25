from typing import List


def is_visible(row: List, col: List, pos: List):
    row = [tree_height - row[pos[0]] for tree_height in row]
    col = [tree_height - col[pos[1]] for tree_height in col]

    visible_from_left = True
    for i in range(pos[0]):
        if row[i] >= 0:
            visible_from_left = False
            break

    visible_from_right = True
    for i in range(pos[0] + 1, len(row)):
        if row[i] >= 0:
            visible_from_right = False
            break

    visible_from_top = True
    for i in range(pos[1]):
        if col[i] >= 0:
            visible_from_top = False
            break

    visible_from_bottom = True
    for i in range(pos[1] + 1, len(row)):
        if col[i] >= 0:
            visible_from_bottom = False
            break

    return (
        visible_from_left
        or visible_from_right
        or visible_from_top
        or visible_from_bottom
    )


def parse_and_transpose_grid(input_file_path: str):
    with open(input_file_path) as file:
        grid = [list(map(int, a)) for a in file.read().split("\n")]
    grid_T = list(map(list, zip(*grid)))
    return (grid, grid_T)


def sol(input_file_path: str):
    # Parse grid and create transposed copy
    (grid, grid_T) = parse_and_transpose_grid(input_file_path)

    # Trees on the boundary of the grid
    grid_size = len(grid)
    visible_trees = 2 * grid_size + 2 * (grid_size - 2)

    # Sum up visible trees in the interior
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            visible_trees += 1 if is_visible(grid[i], grid_T[j], [j, i]) else 0
    return visible_trees
