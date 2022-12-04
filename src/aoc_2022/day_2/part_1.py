SIGN_VALUE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

RPS_MAP = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}


def sol(input_file_path: str):
    with open(input_file_path) as file:
        return sum(map(lambda game: RPS_MAP[game[0]][game[1]] + SIGN_VALUE[game[1]],
                   [a.split(" ") for a in file.read().split("\n")]))
