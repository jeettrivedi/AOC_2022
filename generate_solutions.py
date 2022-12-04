from aoc_2022.utils import pretty_print_header
from aoc_2022.day_1.part_1 import sol as d1p1
from aoc_2022.day_1.part_2 import sol as d1p2
from aoc_2022.day_2.part_1 import sol as d2p1
from aoc_2022.day_2.part_2 import sol as d2p2

pretty_print_header(1)
print(f'The solution to day 1 part 1 is {d1p1("data/1/data.txt")}')
print(f'The solution to day 1 part 2 is {d1p2("data/1/data.txt")}')

pretty_print_header(2)
print(f'The solution to day 2 part 1 is {d2p1("data/2/data.txt")}')
print(f'The solution to day 2 part 2 is {d2p2("data/2/data.txt")}')