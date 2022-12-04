# Advent of Code 2022
# Day 04: Camp Cleanup

import pandas as pd
import numpy as np


def read_data(filename):
    df = pd.read_csv(filename, sep=',', header=None)
    df.columns = ['Elf1', 'Elf2']
    return df

def shape_df(df):
    df_elf1 = pd.DataFrame(df.Elf1.str.split("-").to_list(), columns=["Elf_1_Start", "Elf_1_Stop"])
    df_elf2 = pd.DataFrame(df.Elf2.str.split("-").to_list(), columns=["Elf_2_Start", "Elf_2_Stop"])
    df = pd.concat([df_elf1, df_elf2], axis=1)
    # Improvement suggested by Michael Aydinbas
    # df = df.apply(pd.to_numeric)
    df = df.astype(int)

    return df

def solve_part_1(df) -> int:
    df['Duplicates'] = np.where(((df['Elf_1_Start'] >= df['Elf_2_Start']) & (df['Elf_1_Stop'] <= df['Elf_2_Stop'])) |
                             ((df['Elf_2_Start'] >= df['Elf_1_Start']) & (df['Elf_2_Stop'] <= df['Elf_1_Stop'])), 1, 0)
    return df['Duplicates'].sum()

def solve_part_2(df):

    df['Overlap'] = np.logical_or(np.logical_or(df['Elf_2_Start'].between(df['Elf_1_Start'], df['Elf_1_Stop']),
                                                df['Elf_2_Stop'].between(df['Elf_1_Start'], df['Elf_1_Stop'])),
                                  np.logical_or(df['Elf_1_Start'].between(df['Elf_2_Start'], df['Elf_2_Stop']),
                                                df['Elf_1_Stop'].between(df['Elf_2_Start'], df['Elf_2_Stop'])))
    return df['Overlap'].sum()


def solution(filename) -> int:
    """Help the elves reduce duplication of cleanup efforts."""

    # modification to structure inspired by Laura Twardy
    # process data from filename to make it usable by our solving functions
    df = shape_df(read_data('input.txt'))

    duplicates = solve_part_1(df)
    print(f"{duplicates} elves have completely redundant chore assignments.")

    overlaps = solve_part_2(df)
    print(f"{overlaps} pairs of chore assignments contain some duplicated work.")

if __name__ == '__main__':
    solution('input.txt')


