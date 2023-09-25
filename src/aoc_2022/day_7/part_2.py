from .part_1 import calculate_dir_size


def sol(input_file_path: str):
    FS_SIZE = 70000000
    UPDATE_SIZE = 30000000
    with open(input_file_path) as file:
        commands = file.read().split("\n")
    dir_sizes = {"root": 0}
    dir_sizes = calculate_dir_size(dir_sizes, ["root"], commands[1:])
    del dir_sizes[""]
    smallest_dir = FS_SIZE
    for key in dir_sizes:
        if (dir_sizes["root"] - dir_sizes[key]) + UPDATE_SIZE <= FS_SIZE:
            if smallest_dir > dir_sizes[key]:
                smallest_dir = dir_sizes[key]
    return smallest_dir
