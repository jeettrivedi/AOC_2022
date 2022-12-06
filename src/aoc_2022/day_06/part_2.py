def detect_start_of_packet_marker(message: str):
    for i in range(len(message)-14):
        if len(set(message[i:i+14])) == 14:
            return i + 14

def sol(input_file_path: str):
    with open(input_file_path) as file:
        return detect_start_of_packet_marker(file.read())