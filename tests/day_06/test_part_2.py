from aoc_2022.day_06.part_2 import detect_start_of_packet_marker
import pytest

TEST_CASES = {
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb': 19,
    'bvwbjplbgvbhsrlpgdmjqwftvncz': 23,
    'nppdvjthqldpwncqszvftbrmjlhg': 23,
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 29,
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 26
}

@pytest.mark.parametrize("message,expected_output",TEST_CASES.items())
def test_part_1(message,expected_output):
    assert detect_start_of_packet_marker(message) == expected_output