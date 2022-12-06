def get_item_priority(item_code: str):
    if item_code.lower() != item_code:
        priority = ord(item_code) - 64 + 26
    else:
        priority = ord(item_code) - 96
    return priority

def get_rucksack_priority(item_list: str):
    size = len(item_list)
    compartment_1 = set(item_list[:size//2])
    compartment_2 = set(item_list[size//2:])
    common_item = [a for a in compartment_1 if a in compartment_2][0]
    rucksack_priority = get_item_priority(common_item)
    return rucksack_priority

def sol(input_file_path: str):
    with open(input_file_path,'r') as file:
        return sum(map(get_rucksack_priority,file.read().split("\n")))