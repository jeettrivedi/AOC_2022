BASIS_VECTORS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def add_vectors(v1, v2):
    """Returns the sum of two vectors"""
    return tuple(v1[i] + v2[i] for i in range(len(v1)))


def vector_displacement(v1, v2):
    """Returns the vector displacement from v1 to v2"""
    return tuple((v2[i] - v1[i]) for i in range(len(v1)))


def movement_vector(displacement):
    moves = []
    if abs(displacement[0]) < 2 and abs(displacement[1]) < 2:
        return moves
    else:
        if displacement[0] > 0:
            moves.append("R")
        elif displacement[0] < 0:
            moves.append("L")

        if displacement[1] > 0:
            moves.append("U")
        elif displacement[1] < 0:
            moves.append("D")

    return moves


def parse_input(input_file_path: str):
    with open(input_file_path, "r") as f:
        lines = (line.strip().split(" ") for line in f.readlines())
    return lines


def sol(input_file_path: str):
    head = {
        "position": (0, 0),
    }
    tail = {
        "position": (0, 0),
        "places_visited": set([(0, 0)]),
    }

    steps = parse_input(input_file_path)
    for direction, step in steps:
        for _ in range(int(step)):
            # Move head
            head["position"] = add_vectors(head["position"], BASIS_VECTORS[direction])

            # Update tail position
            displacement = vector_displacement(tail["position"], head["position"])
            moves = movement_vector(displacement)
            for tail_move in moves:
                tail["position"] = add_vectors(
                    tail["position"], BASIS_VECTORS[tail_move]
                )
            tail["places_visited"].add(tail["position"])

    return len(tail["places_visited"])


if __name__ == "__main__":
    sol("data/9/data.txt")
