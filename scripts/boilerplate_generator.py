import sys
from pathlib import Path
from datetime import datetime
from shutil import copyfile

args_passed = len(sys.argv) > 1
DATE_TODAY = datetime.now().day
if args_passed:
    DATE_TODAY = int(sys.argv[1])
DATE_TODAY = str(DATE_TODAY)
REFERENCE_DIR = Path("scripts/boilerplate")

DIRS_TO_CREATE = [
    Path(f"data/{DATE_TODAY}"),
    Path(f"src/aoc_2022/day_{DATE_TODAY}"),
    Path(f"tests/day_{DATE_TODAY}"),
]

for dir in DIRS_TO_CREATE:
    if dir.exists():
        raise ValueError(
            "Some of the files for this day already exist. Please delete them and try again."
        )

TEST_P1_TEXT = f"""from aoc_2022.day_{DATE_TODAY}.part_1 import sol

def test_part_1():
    assert sol('tests/day_{DATE_TODAY}/data.txt') == 1"""
TEST_P2_TEXT = f"""from aoc_2022.day_{DATE_TODAY}.part_2 import sol

def test_part_2():
    assert sol('tests/day_{DATE_TODAY}/data.txt') == 1"""
FILE_CREATE_MAP = {
    f"tests/day_{DATE_TODAY}/test_part_1.py": TEST_P1_TEXT,
    f"tests/day_{DATE_TODAY}/test_part_2.py": TEST_P2_TEXT,
}

# Create directories
for dir in DIRS_TO_CREATE:
    dir.mkdir(parents=True, exist_ok=False)

# CREATE src files
copyfile(REFERENCE_DIR / "part_1.py", f"src/aoc_2022/day_{DATE_TODAY}/part_1.py")
copyfile(REFERENCE_DIR / "part_1.py", f"src/aoc_2022/day_{DATE_TODAY}/part_2.py")
copyfile(REFERENCE_DIR / "__init__.py", f"src/aoc_2022/day_{DATE_TODAY}/__init__.py")
copyfile(REFERENCE_DIR / "__main__.py", f"src/aoc_2022/day_{DATE_TODAY}/__main__.py")

# CREATE data files
copyfile(REFERENCE_DIR / "data.txt", f"data/{DATE_TODAY}/data.txt")
copyfile(REFERENCE_DIR / "data.txt", f"tests/day_{DATE_TODAY}/data.txt")

# CREATE test files
for file_path, text in FILE_CREATE_MAP.items():
    with open(file_path, "w") as f:
        f.write(text)
