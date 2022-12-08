# Solution using if-else
# def calculate_dir_size(dir_sizes, current_path, commands):
#     if len(commands) > 0:
#         cmd = commands[0].split(" ")
#         if cmd[0] == "$":
#             if cmd[1] == "cd":
#                 if cmd[2] == "..":
#                     return calculate_dir_size(dir_sizes, current_path[:-1], commands[1:])
#                 else:
#                     return calculate_dir_size(dir_sizes, current_path + [cmd[2]], commands[1:])
#             else:
#                 return calculate_dir_size(dir_sizes, current_path, commands[1:])
#         else:
#             if cmd[0] != "dir":
#                 for i in range(len(current_path) + 1):
#                     dir_sizes["/".join(current_path[:i])] = dir_sizes.get(
#                         "/".join(current_path[:i]), 0) + int(cmd[0])
#             return calculate_dir_size(dir_sizes, current_path, commands[1:])
#     return dir_sizes


def calculate_dir_size(dir_sizes, current_path, commands):
    if len(commands) > 0:
        cmd = commands[0].split(" ")
        match cmd:
            case ["$", "cd", ".."]:
                return calculate_dir_size(dir_sizes, current_path[:-1], commands[1:])
            case ["$", "cd", _]:
                return calculate_dir_size(dir_sizes, current_path + [cmd[2]], commands[1:])
            case ["$", _] | ["dir", _]:
                return calculate_dir_size(dir_sizes, current_path, commands[1:])
            case _:
                for i in range(len(current_path) + 1):
                    dir_sizes["/".join(current_path[:i])] = dir_sizes.get(
                        "/".join(current_path[:i]), 0) + int(cmd[0])
                return calculate_dir_size(dir_sizes, current_path, commands[1:])
    return dir_sizes


def sol(input_file_path: str):
    with open(input_file_path) as file:
        commands = file.read().split("\n")
    dir_sizes = {
        "root": 0
    }
    dir_sizes = calculate_dir_size(dir_sizes, ["root"], commands[1:])
    return sum([a for a in dir_sizes.values() if a <= 100000])

