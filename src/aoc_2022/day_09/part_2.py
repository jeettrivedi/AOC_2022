from .part_1 import parse_input,movement_vector,add_vectors,vector_displacement,BASIS_VECTORS

def sol(input_file_path: str):
    ROPE_LENGTH = 10
    ROPE = []
    for _ in range(ROPE_LENGTH):
        ROPE.append({
            "position": (0,0),
        })

    tail_positions_visited = set([(0,0)])
    steps = parse_input(input_file_path)
    for direction,step in steps:
        for _ in range(int(step)):
            # Move head
            ROPE[0]["position"] = add_vectors(ROPE[0]["position"], BASIS_VECTORS[direction])

            # Update rope position
            for idx in range(1,ROPE_LENGTH):
                displacement = vector_displacement(ROPE[idx]["position"],ROPE[idx - 1]["position"])
                moves = movement_vector(displacement)
                for tail_move in moves:
                    ROPE[idx]["position"] = add_vectors(ROPE[idx]["position"], BASIS_VECTORS[tail_move])

            # Update tail positions visited
            tail_positions_visited.add(ROPE[-1]["position"])
    return len(tail_positions_visited)

if __name__ == "__main__":
    sol('data/9/data.txt')