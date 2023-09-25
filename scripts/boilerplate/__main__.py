import sys
from pathlib import Path
from aoc_2022.utils import pretty_print_sols
from .part_1 import sol as part_1_sol
from .part_2 import sol as part_2_sol

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Missing input file path.")
    else:
        try:
            # Get input file path
            INPUT_FILE_PATH = Path(args[1])
            if not INPUT_FILE_PATH.exists():
                raise FileNotFoundError

            # Generate solutions
            sol_1 = part_1_sol(INPUT_FILE_PATH)
            sol_2 = part_2_sol(INPUT_FILE_PATH)

            # Print solutions
            pretty_print_sols(sol_1, sol_2)
        except FileNotFoundError:
            print(f"Input file does not exist at the given path {INPUT_FILE_PATH}")
