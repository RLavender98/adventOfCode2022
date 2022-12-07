import numpy as np

data = open('input_edited.txt').read().splitlines()

files = ['dpllhlcv',
         284723,
         'mgjdlmrz',
         'njstc',
         'nzwbc',
         'qzzfvdh',
         'smvhphf']


def find_dir(file_sys, direc):
    if direc in file_sys:
        return file_sys
    for el in file_sys:
        if type(el) is list:
            x = find_dir(el, direc)
            if type(x) is list:
                return x


def add_to_folder(folder, instruction):
    if instruction.startswith('dir'):
        folder.append(instruction[4:])
    else:
        folder.append(int(instruction.split(' ')[0]))


def folder_from(instructions, start_ind):
    folder = []
    i = start_ind
    while i < len(instructions) and '$' not in instructions[i]:
        add_to_folder(folder, instructions[i])
        i += 1
    return folder


while '$ cd /' in data:
    data.remove('$ cd /')

while '$ cd ..' in data:
    data.remove('$ cd ..')

i = 0
while i < len(data) - 1:
    if data[i].startswith('$ cd') and data[i+1].startswith('$ ls'):
        find_dir(files, data[i][5:]).append(folder_from(data, i+2))
        find_dir(files, data[i][5:]).remove(data[i][5:])
    i += 1


def calculate_folder_sizes(file_sys, subarray_sizes):
    folder_total = 0
    subs = subarray_sizes
    for el in file_sys:
        if type(el) is list:
            ans = calculate_folder_sizes(el, subs)
            folder_total += ans[0]
            subs = ans[1]
        else:
            folder_total += el
    subarray_sizes.append(folder_total)
    return [folder_total, subarray_sizes]


folder_sizes = calculate_folder_sizes(files, [])[1]

maxi = np.max(folder_sizes)

left_over = 70000000 - maxi
needed = 30000000 - left_over

bigguns = [x for x in folder_sizes if x >= needed]

print(np.min(bigguns))
