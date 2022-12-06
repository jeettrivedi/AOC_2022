from typing import List

def parse_stacks(stacks: str):
    stacks = stacks.split('\n')
    stack_labels = [int(a) for a in stacks[-1].strip().split(" ") if a != '']
    stacks_dict = {stack: [] for stack in stack_labels}
    m = len(stacks) - 2
    n = max(stack_labels)
    for i in range(m,-1,-1):
        for j in range(0,n,1):
            if stacks[i][4*j + 1] != ' ':
                stacks_dict[j+1].append(stacks[i][4 * j + 1])
    return stacks_dict


def parse_steps(steps: str):
    steps = steps.split("\n")
    return [{
        'from': int(step[3]),
        'to': int(step[-1]),
        'count': int(step[1]),
    } for step in map(str.split,steps)]


def execute_step(stack:dict[List], step: dict[str]):
    for i in range(step['count']):
        stack[step['to']].append(stack[step['from']].pop(-1))
    return stack


def sol(input_file_path: str):
    with open(input_file_path) as file:
        [stacks,
         steps] = file.read().split("\n\n")
    stacks = parse_stacks(stacks)
    steps = parse_steps(steps)
    for step in steps:
        stacks = execute_step(stacks,step)
    return ''.join([a[-1] for a in stacks.values()])