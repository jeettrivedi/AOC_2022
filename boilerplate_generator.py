import os
import sys
from datetime import datetime

args_passed = len(sys.argv) > 1
DATE_TODAY = datetime.now().day
print(DATE_TODAY)
if args_passed:
    DATE_TODAY = int(sys.argv[1])
DATE_TODAY = str(DATE_TODAY) if DATE_TODAY > 10 else f"0{DATE_TODAY}"

DIRS_TO_CREATE = [
    f'src/aoc_2022/day_{DATE_TODAY}',
    f'tests/day_{DATE_TODAY}'
]

SOLUTION_FILE_TEXT = f"""def sol(input_file_path: str):
    return input_file_path"""
TEST_P1_TEXT = f"""from aoc_2022.day_{DATE_TODAY}.part_1 import sol

def test_part_1():
    assert sol('tests/day_{DATE_TODAY}/data.txt') == 1"""
TEST_P2_TEXT = f"""from aoc_2022.day_{DATE_TODAY}.part_2 import sol

def test_part_2():
    assert sol('tests/day_{DATE_TODAY}/data.txt') == 1"""
FILE_CREATE_MAP = {
    f'src/aoc_2022/day_{DATE_TODAY}/part_1.py': SOLUTION_FILE_TEXT,
    f'src/aoc_2022/day_{DATE_TODAY}/part_2.py': SOLUTION_FILE_TEXT,
    f'tests/day_{DATE_TODAY}/__init__.py': "",
    f'tests/day_{DATE_TODAY}/test_part_1.py': TEST_P1_TEXT,
    f'tests/day_{DATE_TODAY}/test_part_2.py': TEST_P2_TEXT,
}

if os.path.exists(f'src/aoc_2022/day_{DATE_TODAY}'):
    raise ValueError("Files for this day already exist.")

for dir in DIRS_TO_CREATE:
    os.mkdir(dir)

for filepath,content in FILE_CREATE_MAP.items():
    with open(filepath,'w') as file:
        file.write(content)