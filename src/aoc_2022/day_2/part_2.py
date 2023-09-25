# X = Lose
# Y = Draw
# Z = Win
SIGN_VALUE = {"A": 1, "B": 2, "C": 3}

WIN_MOVE_MAP = {"A": "B", "B": "C", "C": "A"}
LOST_MOVE_MAP = {"A": "C", "B": "A", "C": "B"}


def score_round(round_info):
    opponent_move = round_info[0]
    move = round_info[1]
    score = 3 + SIGN_VALUE[opponent_move]
    if move == "X":
        score = SIGN_VALUE[LOST_MOVE_MAP[opponent_move]]
    elif move == "Z":
        score = 6 + SIGN_VALUE[WIN_MOVE_MAP[opponent_move]]
    return score


def sol(input_file_path: str):
    with open(input_file_path) as file:
        score = sum(
            list(
                map(
                    lambda a: score_round(a.split(" ")),
                    file.read().split("\n"),
                )
            )
        )
    return score
