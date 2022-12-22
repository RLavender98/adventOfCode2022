import re

data = open('input.txt').read().split('\n\n')
jungle_map = [list(x) for x in data[0].splitlines()]
max_length = max([len(line) for line in jungle_map])
for line in jungle_map:
    while len(line) < max_length:
        line.append(' ')
instructions = re.findall(r'(\d+|[A-Z]+)', data[1])


def print_map(jungle_map_array, ori, posi):
    for key, line in enumerate(jungle_map_array):
        if pos[0] == key:
            copy_of_line = line.copy()
            if ori == 0:
                copy_of_line[posi[1]] = '>'
            if ori == 1:
                copy_of_line[posi[1]] = 'v'
            if ori == 2:
                copy_of_line[posi[1]] = '<'
            if ori == 3:
                copy_of_line[posi[1]] = '^'
            str_line = ''
            for space in copy_of_line:
                str_line += space
            print(str_line)
        else:
            str_line = ''
            for space in line:
                str_line += space
            print(str_line)


start_row = 0
start_column = jungle_map[start_row].index('.')

orientation = 0
pos = [start_row, start_column]

for instruction in instructions:
    if instruction == 'R':
        orientation += 1
        orientation = orientation % 4
        continue
    if instruction == 'L':
        orientation -= 1
        orientation = orientation % 4
        continue
    movement = int(instruction)
    for i in range(movement):
        if orientation == 0:
            if pos[1] + 1 >= len(jungle_map[0]) or jungle_map[pos[0]][pos[1] + 1] == ' ':
                # WRAP OFF THE RIGHT
                # light blue - top
                if pos[0] < 50:
                    if jungle_map[149 - pos[0]][99] == '#':
                        break
                    if jungle_map[149 - pos[0]][99] == '.':
                        pos = [149 - pos[0], 99]
                        orientation = 2
                # light blue - lower
                elif 99 < pos[0] < 150:
                    if jungle_map[49 - (pos[0] - 100)][149] == '#':
                        break
                    if jungle_map[49 - (pos[0] - 100)][149] == '.':
                        pos = [49 - (pos[0] - 100), 149]
                        orientation = 2
                # teal
                elif 49 < pos[0] < 100:
                    if jungle_map[49][100 + pos[0] - 50] == '#':
                        break
                    if jungle_map[49][100 + pos[0] - 50] == '.':
                        pos = [49, 100 + pos[0] - 50]
                        orientation = 3
                # pink
                elif 149 < pos[0] < 200:
                    if jungle_map[149][pos[0] - 100] == '#':
                        break
                    if jungle_map[149][pos[0] - 100] == '.':
                        pos = [149, pos[0] - 100]
                        orientation = 3
            elif jungle_map[pos[0]][pos[1] + 1] == '#':
                break
            else:
                pos = [pos[0], pos[1] + 1]
        elif orientation == 2:
            if pos[1] - 1 < 0 or jungle_map[pos[0]][pos[1] - 1] == ' ':
                # WRAP OFF THE LEFT
                # red - top
                if pos[0] < 50:
                    if jungle_map[149 - pos[0]][0] == '#':
                        break
                    if jungle_map[149 - pos[0]][0] == '.':
                        pos = [149 - pos[0], 0]
                        orientation = 0
                # red - lower
                elif 99 < pos[0] < 150:
                    if jungle_map[49 - (pos[0] - 100)][50] == '#':
                        break
                    if jungle_map[49 - (pos[0] - 100)][50] == '.':
                        pos = [49 - (pos[0] - 100), 50]
                        orientation = 0
                # green
                elif 49 < pos[0] < 100:
                    if jungle_map[100][pos[0] - 50] == '#':
                        break
                    if jungle_map[100][pos[0] - 50] == '.':
                        pos = [100, pos[0] - 50]
                        orientation = 1
                # purple
                elif 149 < pos[0] < 200:
                    if jungle_map[0][pos[0] - 100] == '#':
                        break
                    if jungle_map[0][pos[0] - 100] == '.':
                        pos = [0, pos[0] - 100]
                        orientation = 1
            elif jungle_map[pos[0]][pos[1] - 1] == '#':
                break
            else:
                pos = [pos[0], pos[1] - 1]
        elif orientation == 1:
            if pos[0] + 1 >= len(jungle_map) or jungle_map[pos[0] + 1][pos[1]] == ' ':
                # WRAP OFF THE BOTTOM
                # teal
                if 99 < pos[1] < 150:
                    if jungle_map[pos[1] - 50][99] == '#':
                        break
                    if jungle_map[pos[1] - 50][99] == '.':
                        pos = [pos[1] - 50, 99]
                        orientation = 2
                # pink
                elif 49 < pos[1] < 100:
                    if jungle_map[pos[1] + 100][49] == '#':
                        break
                    if jungle_map[pos[1] + 100][49] == '.':
                        pos = [pos[1] + 100, 49]
                        orientation = 2
                # navy
                elif pos[1] < 50:
                    if jungle_map[0][pos[1] + 100] == '#':
                        break
                    if jungle_map[0][pos[1] + 100] == '.':
                        pos = [0, pos[1] + 100]
                        orientation = 1
            elif jungle_map[pos[0] + 1][pos[1]] == '#':
                break
            else:
                pos = [pos[0] + 1, pos[1]]
        elif orientation == 3:
            if pos[0] - 1 < 0 or jungle_map[pos[0] - 1][pos[1]] == ' ':
                # WRAP OFF THE TOP
                # green
                if pos[1] < 50:
                    if jungle_map[pos[1] + 50][50] == '#':
                        break
                    if jungle_map[pos[1] + 50][50] == '.':
                        pos = [pos[1] + 50, 50]
                        orientation = 0
                # purple
                elif 49 < pos[1] < 100:
                    if jungle_map[pos[1] + 100][0] == '#':
                        break
                    if jungle_map[pos[1] + 100][0] == '.':
                        pos = [pos[1] + 100, 0]
                        orientation = 0
                # navy
                elif 99 < pos[1] < 150:
                    if jungle_map[199][pos[1] - 100] == '#':
                        break
                    if jungle_map[199][pos[1] - 100] == '.':
                        pos = [199, pos[1] - 100]
                        orientation = 3
            elif jungle_map[pos[0] - 1][pos[1]] == '#':
                break
            else:
                pos = [pos[0] - 1, pos[1]]

print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + orientation)


