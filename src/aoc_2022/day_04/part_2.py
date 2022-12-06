def assignment_overlaps(assignment_pair):
    [left_assignment,
     right_assignment] = list(map(lambda a: list(map(int, a.split('-'))),
                                  assignment_pair.split(",")))
    left_assignment = set(range(left_assignment[0], left_assignment[1] + 1))
    right_assignment = set(range(right_assignment[0], right_assignment[1] + 1))
    return int((left_assignment - right_assignment != left_assignment)
                or (right_assignment - left_assignment != right_assignment))


def sol(input_file_path: str):
    with open(input_file_path, 'r') as file:
        return sum(map(assignment_overlaps,file.read().split("\n")))