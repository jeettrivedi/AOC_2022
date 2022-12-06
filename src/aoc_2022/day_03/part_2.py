from typing import List
from .part_1 import get_item_priority


def find_group_priority(group_rucksacks: List[str]):
    rucksack_set = list(map(set, group_rucksacks))
    common_1_2 = [item for item in rucksack_set[0] if item in (
        b for b in rucksack_set[1] if b in rucksack_set[2])][0]
    return get_item_priority(common_1_2)


def sol(input_file_path: str):
    with open(input_file_path, 'r') as file:
        items_data = file.read().split("\n")
    grouped_data = []
    idx = 0
    while idx < len(items_data) - 2:
        grouped_data.append(items_data[idx:idx+3])
        idx += 3
    return sum(map(find_group_priority, grouped_data))
