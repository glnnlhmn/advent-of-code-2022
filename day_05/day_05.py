# Advent of Code 2022
# Day 05:

import pandas as pd
import numpy as np


def read_data(filename):
    """Process data from filename to make it usable by solving functions"""
    with open(filename, 'r') as f:
        data = f.read().strip()
    data = data.split('\n')
    return data


def process_boxes(box_rows: list) -> list:
    """Process data from filename to make it usable by solving functions"""
    box_columns = []
    for i in range(len(box_rows)):
        column = ''
        # for row in box_rows:
        #     column += row[i]
        box_columns.append(column)
    return box_columns

def process_moves(moves_list: list) -> list:
    """Process data from filename to make it usable by solving functions"""
    detailed_moves = []
    for moves in moves_list:
        instructions = [int(moves[1]), int(moves[3]), int(moves[5])]
        detailed_moves.append(instructions)
    return detailed_moves

def process_data(data):
    """Process data from filename to make it usable by solving functions"""
    box_rows = []
    moves_list = []

    for line in data:
        if len(line) > 0 and line[0] == 'm':
            instructions = line.split(' ')
            moves_list.append(instructions)
        else:

            box_rows.append(line)

    # TODO: process boxes need to turn rows to columns
    moves = process_moves(moves_list)
    boxes = process_boxes(box_rows)

    return boxes, moves
def solve_part_1(data) -> int:
    solution_part_1 = -1
    return solution_part_1

def solve_part_2(data) -> int:
    solution_part_2 = -1
    return solution_part_2


def solution(filename) -> int:
    """Help the elves reduce duplication of cleanup efforts."""

    data = read_data('input.txt')
    boxes, moves = process_data(data)

    solution_part_1 = solve_part_1(data)
    print(f"{solution_part_1=}")

    solution_part_2 = solve_part_2(data)
    print(f"{solution_part_2=}")

if __name__ == '__main__':
    solution('input.txt')


