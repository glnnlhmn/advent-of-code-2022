# Advent of Code 2022
# Day 08:

import string
import pandas as pd

def read_data(filename):
    """Process data from filename to make it usable by solving functions"""
    with open(filename, 'r') as f:
        data = f.read().strip()
    data = data.split('\n')
    return data

def is_visible(row_pos, col_pos, tree_row, tree_column) -> bool:
    """Check if tree is visible from the given coordinates"""

    this_tree_height = tree_row[col_pos]

    visible = \
        (all(other_tree_height < this_tree_height for other_tree_height in tree_row[:col_pos])
        or all(other_tree_height < this_tree_height for other_tree_height in tree_row[col_pos+1:])
        or all(other_tree_height < this_tree_height for other_tree_height in tree_column[:row_pos])
        or all(other_tree_height < this_tree_height for other_tree_height in tree_column[row_pos+1:]))

    return visible


def calculate_individual_scenic_score(height, heights) -> int:
    """Calculate the scenic score of the given coordinates"""

    return next(
        (score for score, hgt in enumerate(heights[1:], start=1) if hgt >= height),
        len(heights) - 1,
    )


def calculate_scenic_score(row_pos, col_pos, tree_row, tree_column) -> int:
    """Calculate the scenic score of the given coordinates"""

    this_tree_height = tree_row[col_pos]

    view_1 = calculate_individual_scenic_score(this_tree_height, tree_row[col_pos::-1])
    view_2 = calculate_individual_scenic_score(this_tree_height, tree_row[col_pos:])
    view_3 = calculate_individual_scenic_score(this_tree_height, tree_column[row_pos::-1])
    view_4 = calculate_individual_scenic_score(this_tree_height, tree_column[row_pos:])

    return view_1 * view_2 * view_3 * view_4
def parse_data(data) -> list:

    rows = []

    for line in data:
        new_line = []
        for char in line:
            new_line.append(int(char))

        rows.append(new_line)

    columns = [list(col) for col in zip(*rows)]

    return rows,  columns


def solve_part_1(forrest) -> int:

    heights_by_rows, heights_by_columns = forrest

    len_of_row = len(heights_by_rows)
    len_of_column = len(heights_by_columns)

    visible_trees = 0

    for row_index in range(len_of_row):
        for column_index in range(len_of_column):

            if (row_index in (0, len_of_row - 1)) or (column_index in (0, len_of_column - 1)):
                visible_trees += 1
            elif is_visible(row_index, column_index, heights_by_rows[row_index], heights_by_columns[column_index]):
                visible_trees += 1

    return visible_trees

def solve_part_2(forrest) -> int:

    heights_by_rows, heights_by_columns = forrest

    len_of_row = len(heights_by_rows)
    len_of_column = len(heights_by_columns)

    max_score = 0

    for row_index in range(len_of_row):
        for column_index in range(len_of_column):

            score = calculate_scenic_score(row_index, column_index, heights_by_rows[row_index], heights_by_columns[column_index])

            max_score = max(max_score, score)

    return max_score


def solution(filename) -> int:
    """Help the elves reduce duplication of cleanup efforts."""

    data = parse_data(read_data(filename))

    solution_part_1 = solve_part_1(data)
    print(f"{solution_part_1=}")

    solution_part_2 = solve_part_2(data)
    print(f"{solution_part_2=}")

if __name__ == '__main__':
    solution('input.txt')


