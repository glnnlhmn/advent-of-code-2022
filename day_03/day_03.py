
def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()

    data = data.split('\n')
    return data

def letter_to_score(letter):
    if ord(letter) >= 97 and ord(letter) <= 122:
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def score_part_1(data):
    score = 0
    for supplies in data:
        midpoint = len(supplies) // 2
        rucksack_1 = supplies[0:midpoint]
        rucksack_2 = supplies[midpoint:]
        in_both = ''

        for supply in rucksack_1:
            if supply in rucksack_2:
                if supply not in in_both:
                    in_both += supply
        score += letter_to_score(in_both)

    return score

def score_part_2(data):
    score = 0
    for elf_groups in data:
        in_multiple = ''
        for supply in elf_groups[0]:
            if supply in elf_groups[1] and supply in elf_groups[2]:
                if supply not in in_multiple:
                    in_multiple += supply
                    score += letter_to_score(in_multiple)
    return score

def reshape_data(data):

    data_2 = []
    for i in range(0,len(data),3):
        data_2.append([data[i], data[i+1], data[i+2]])

    return data_2
def main():
    data = read_data('input.txt')
    print(f'Part 1: {score_part_1(data)}')
    print(f'Part 2: {score_part_2(reshape_data(data))}')

if __name__ == '__main__':

    main()


