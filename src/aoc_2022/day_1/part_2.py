def sol(input_file_path: str):
    with open(input_file_path) as file:
        return sum(
            sorted([sum(map(int, a.split("\n"))) for a in file.read().split("\n\n")])[
                -3:
            ]
        )
