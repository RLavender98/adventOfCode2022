import re

# data = open('example_input.txt').read().split('\n\n')
data = open('input.txt').read().split('\n\n')
jungle_map = [list(x) for x in data[0].splitlines()]
max_length = max([len(line) for line in jungle_map])
for line in jungle_map:
    while len(line) < max_length:
        line.append(' ')
instructions = re.findall(r'(\d+|[A-Z]+)', data[1])

start_row = 0
start_column = jungle_map[start_row].index('.')

orientation = 0
pos = [start_row, start_column]

for instruction in instructions:
    print(instruction)
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
                pos_before = pos.copy()
                for j in range(len(jungle_map[pos[0]])):
                    if jungle_map[pos[0]][j] == '#':
                        break
                    if jungle_map[pos[0]][j] == '.':
                        pos = [pos[0], j]
                        break
                if pos[1] == pos_before[1]:
                    break
            elif jungle_map[pos[0]][pos[1] + 1] == '#':
                break
            else:
                pos = [pos[0], pos[1] + 1]
        if orientation == 2:
            if pos[1] - 1 < 0 or jungle_map[pos[0]][pos[1] - 1] == ' ':
                pos_before = pos.copy()
                for j in range(len(jungle_map[pos[0]]) - 1, -1, -1):
                    if jungle_map[pos[0]][j] == '#':
                        break
                    if jungle_map[pos[0]][j] == '.':
                        pos = [pos[0], j]
                        break
                if pos[1] == pos_before[1]:
                    break
            elif jungle_map[pos[0]][pos[1] - 1] == '#':
                break
            else:
                pos = [pos[0], pos[1] - 1]
        if orientation == 1:
            if pos[0] + 1 >= len(jungle_map) or jungle_map[pos[0] + 1][pos[1]] == ' ':
                pos_before = pos.copy()
                for j in range(len(jungle_map)):
                    if jungle_map[j][pos[1]] == '#':
                        break
                    if jungle_map[j][pos[1]] == '.':
                        pos = [j, pos[1]]
                        break
                if pos[0] == pos_before[0]:
                    break
            elif jungle_map[pos[0] + 1][pos[1]] == '#':
                break
            else:
                pos = [pos[0] + 1, pos[1]]
        if orientation == 3:
            if pos[0] - 1 < 0 or jungle_map[pos[0] - 1][pos[1]] == ' ':
                pos_before = pos.copy()
                for j in range(len(jungle_map) - 1, -1, -1):
                    if jungle_map[j][pos[1]] == '#':
                        break
                    if jungle_map[j][pos[1]] == '.':
                        pos = [j, pos[1]]
                        break
                if pos[0] == pos_before[0]:
                    break
            elif jungle_map[pos[0] - 1][pos[1]] == '#':
                break
            else:
                pos = [pos[0] - 1, pos[1]]

print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + orientation)


