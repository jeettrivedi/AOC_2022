def pretty_print_header(text: str, padding_size: int = 12, height: int = 3):
    """Prints out a pretty header of the form
    ******************************
    *           <text>           *
    ******************************
    """
    text_len = len(text)
    horizontal_border = "*" * (text_len + padding_size * 2)
    left_padding = "*" + " " * (padding_size - 1)
    right_padding = " " * (padding_size - 1) + "*"
    title = left_padding + text + right_padding
    text = horizontal_border + "\n" + title + "\n" + horizontal_border
    print(text)


def pretty_print_sols(sol_part_1, sol_part_2, **kwargs):
    """Prints out the solutions for part 1 and part 2 in a pretty format."""
    pretty_print_header("Part 1", **kwargs)
    print(f"\nSolution for part 1: {sol_part_1}\n")
    pretty_print_header("Part 2", **kwargs)
    print(f"\nSolution for part 2: {sol_part_2}\n")
