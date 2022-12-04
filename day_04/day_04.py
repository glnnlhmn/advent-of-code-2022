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

def evaluate_df_part1(df):
    df['Overlap'] = np.where(((df['Elf_1_Start'] >= df['Elf_2_Start']) & (df['Elf_1_Stop'] <= df['Elf_2_Stop'])) |
                             ((df['Elf_2_Start'] >= df['Elf_1_Start']) & (df['Elf_2_Stop'] <= df['Elf_1_Stop'])), 1, 0)
    return df

def evaluate_df_part2(df):
    df['Overlap'] = np.logical_or(np.logical_or(np.logical_and(df['Elf_2_Start'] >= df['Elf_1_Start'],
                                                               df['Elf_2_Start'] <= df['Elf_1_Stop']),
                                                np.logical_and(df['Elf_2_Stop'] >= df['Elf_1_Start'],
                                                               df['Elf_2_Stop'] <= df['Elf_1_Stop'])),
                                  np.logical_or(np.logical_and(df['Elf_1_Start'] >= df['Elf_2_Start'],
                                                               df['Elf_1_Start'] <= df['Elf_2_Stop']),
                                                np.logical_and(df['Elf_1_Stop'] >= df['Elf_2_Start'],
                                                               df['Elf_1_Stop'] <= df['Elf_2_Stop'])))
    return df
def main():
    df = shape_df(read_data('input.txt'))
    df_part1 = evaluate_df_part1(df)
    print(f'Part 1: {df_part1["Overlap"].sum()}')

    df_part2 = evaluate_df_part2(df)
    print(f'Part 2: {df_part2["Overlap"].sum()}')

if __name__ == '__main__':

    main()


