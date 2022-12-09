# Advent of Code 2022
# Day 07:

import string
import pandas as pd

def read_data(filename):
    """Process data from filename to make it usable by solving functions"""
    with open(filename, 'r') as f:
        data = f.read().strip()
    data = data.split('\n')
    return data

def parse_data(data) -> list:

    directory_tree = []
    df = pd.DataFrame(columns=['path', 'file', 'size',])
    for line in data:
        directory_tree.append(line.split(' '))

    directory_path = '/'
    #
    for directory in directory_tree:
        if directory[0] == '$':
            # Command
            if directory[1] == "cd":
                # Change directory
                if directory[2] == "/":
                    directory_path = '/'
                elif directory[2] == "..":
                    directory_path = directory_path[0:directory_path[:directory_path.rfind("/")].rfind("/")+1]
                else:
                    directory_path = directory_path + directory[2] + '/'
            elif line[2:] == "ls":
                pass

        elif directory[0] == 'dir':

            pass

        else:
            list = [directory_path, directory[0], directory[1]]
            a_series = pd.Series(list, index=df.columns)
            df = df.append(a_series, ignore_index=True)


    return df

def solve_part_1(data) -> int:


    return -1

def solve_part_2(data) -> int:

    return -1


def solution(filename) -> int:
    """Help the elves reduce duplication of cleanup efforts."""

    data = parse_data(read_data(filename))
    print(data)

    solution_part_1 = solve_part_1(data)
    print(f"{solution_part_1=}")

    solution_part_2 = solve_part_2(data)
    print(f"{solution_part_2=}")

if __name__ == '__main__':
    solution('input_sample.txt')


