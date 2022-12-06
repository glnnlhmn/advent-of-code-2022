# Advent of Code 2022
# Day 06:

import string


def read_data(filename):
    """Process data from filename to make it usable by solving functions"""
    with open(filename, 'r') as f:
        data = f.read().strip()

    return data

def marker_found(test_marker:str, marker_length: int = 4) -> bool:
    """Look for a match of any char in a string"""
    _marker_found = True
    test_marker_length = len(test_marker)

    if len(test_marker) != marker_length:
        return not _marker_found
    for i in range(test_marker_length):
        if test_marker[i] in test_marker[i+1:]:
            _marker_found = False
            break



    return _marker_found

def solve_part_1(data) -> int:

    start_of_packet = 3

    while start_of_packet < len(data) -1:
        if marker_found(data[start_of_packet-3:start_of_packet+1]):
            return start_of_packet + 1
        start_of_packet += 1
    return -1

def solve_part_2(data) -> int:
    start_of_packet = 13

    while start_of_packet < len(data) -1:
        if marker_found(data[start_of_packet-13:start_of_packet + 1], 14):
            return start_of_packet + 1
        start_of_packet += 1
    return -1


def solution(filename) -> int:
    """Help the elves reduce duplication of cleanup efforts."""

    data = read_data(filename)


    solution_part_1 = solve_part_1(data)
    print(f"{solution_part_1=}")

    solution_part_2 = solve_part_2(data)
    print(f"{solution_part_2=}")

if __name__ == '__main__':
    solution('input.txt')


