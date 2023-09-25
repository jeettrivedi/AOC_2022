from aoc_2022.day_6.part_1 import detect_start_of_packet_marker
import pytest

TEST_CASES = {
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
}


@pytest.mark.parametrize("message,expected_output", TEST_CASES.items())
def test_part_1(message, expected_output):
    assert detect_start_of_packet_marker(message) == expected_output
