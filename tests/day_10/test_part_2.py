from aoc_2022.day_10.part_2 import sol


def test_part_2():
    with open("tests/day_10/test_2_sol.txt", "r") as file:
        assert sol("tests/day_10/data.txt") == file.read()
