def compute_pixel_state(register, clock):
    clock = clock % 40
    sprite_lower = (register - 1) % 40
    sprite_upper = (register + 1) % 40
    state = "."
    if sprite_lower <= clock <= sprite_upper:
        state = "#"
    return state


def execute_instruction(instruction, clock, register, screen_output):
    if instruction[0] == "addx":
        for i in range(2):
            screen_output += compute_pixel_state(register, clock)
            clock += 1
        register += int(instruction[1])
    else:
        screen_output += compute_pixel_state(register, clock)
        clock += 1
    return (clock, register, screen_output)


def sol(input_file_path: str):
    with open(input_file_path) as file:
        instructions = list(map(lambda a: a.split(" "), file.read().split("\n")))
    clock = 0
    cpu_register = 1
    screen_output = ""
    for instruction in instructions:
        (clock, cpu_register, screen_output) = execute_instruction(
            instruction, clock, cpu_register, screen_output
        )

    screen_output_aligned = ""
    for idx, pixel in enumerate(screen_output):
        if idx > 0 and idx % 40 == 0:
            screen_output_aligned += "\n"
        screen_output_aligned += pixel
    return screen_output_aligned
