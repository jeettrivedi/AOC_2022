BREAKPOINTS = [20, 60, 100, 140, 180, 220]


def execute_instruction(instruction, clock, register, accumalator):
    if instruction[0] == "addx":
        for i in range(2):
            clock += 1
            if clock in BREAKPOINTS:
                accumalator += register * clock
        register += int(instruction[1])
    else:
        clock += 1
        if clock in BREAKPOINTS:
            accumalator += register * clock
    return (clock, register, accumalator)


def sol(input_file_path: str):
    with open(input_file_path) as file:
        instructions = list(map(lambda a: a.split(" "), file.read().split("\n")))
    clock = 0
    cpu_register = 1
    accumalator = 0
    for instruction in instructions:
        (clock, cpu_register, accumalator) = execute_instruction(
            instruction, clock, cpu_register, accumalator
        )
    return accumalator
