# # Advent of Code 2022
# # Day 05:
#
# import string
#
#
# def read_data(filename):
#     """Process data from filename to make it usable by solving functions"""
#     with open(filename, 'r') as f:
#         data = f.read().strip()
#
#     return data
#
#
# def process_boxes(box_rows: list) -> list:
#     """Process data from filename to make it usable by solving functions"""
#
#     # box_stack = [[] for _letter in box_rows[-1]]
#     # for line in box_rows:
#     #     for index, character in enumerate(line):
#     #         if character.isalpha():
#     #             box_stack[index].append(character)
#     #     box_stack.insert(0, ["dummy"])
#     # return box_stack
#     lines = box_rows.split("\n")
#
#     stacks = [list(line[1:][: 9 * 4 : 4]) for line in lines[:8]]
#
#     piles = [[] for _ in range(9)]
#     for line in stacks:
#         for i, item in enumerate(line):
#             if item in string.ascii_uppercase:
#                 piles[i].insert(0, item)
#
# def process_moves(moves_list: list) -> list:
#     """Process data from filename to make it usable by solving functions"""
#     detailed_moves = []
#     for moves in moves_list:
#         instructions = [int(moves[1]), int(moves[3]), int(moves[5])]
#         detailed_moves.append(instructions)
#     return detailed_moves
#
# def process_data(data):
#     """Process data from filename to make it usable by solving functions"""
#     box_rows = []
#     moves_list = []
#
#     for line in data:
#         if not line:
#             continue
#         if line[0] == 'm':
#             instructions = line.split(' ')
#             moves_list.append(instructions)
#         else:
#             row = []
#             while line:
#                 row.append(line[1:2])
#                 line = line[4:]
#             box_rows.append(row)
#
#     moves = process_moves(moves_list)
#     boxes = process_boxes(box_rows)
#
#     return boxes, moves
# def solve_part_1(data) -> int:
#     solution_part_1 = -1
#     return solution_part_1
#
# def solve_part_2(data) -> int:
#     solution_part_2 = -1
#     return solution_part_2
#
#
# def solution(filename) -> int:
#     """Help the elves reduce duplication of cleanup efforts."""
#
#     data = read_data(filename)
#     boxes, moves = process_data(data)
#
#     solution_part_1 = solve_part_1(data)
#     print(f"{solution_part_1=}")
#
#     solution_part_2 = solve_part_2(data)
#     print(f"{solution_part_2=}")
#
# if __name__ == '__main__':
#     solution('input.txt')
#
#
