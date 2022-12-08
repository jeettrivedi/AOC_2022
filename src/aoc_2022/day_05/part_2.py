from typing import List
from .part_1 import (parse_stacks,
                     parse_steps)


def execute_step(stack:dict[List], step: dict[str]):
    stack[step['to']] += stack[step['from']][-step['count']:]
    stack[step['from']] = stack[step['from']][:-step['count']]
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