import numpy as np

data = open('input.txt').read().splitlines()

paths = [[y.split(',') for y in z] for z in [x.split(' -> ') for x in data]]

x_max = np.max([int(x[0]) for y in paths for x in y])
x_min = np.min([int(x[0]) for y in paths for x in y])
y_max = np.max([int(x[1]) for y in paths for x in y])

caves = [['.' for i in range(x_max - x_min + 1 + 2 * y_max)] for j in range(y_max + 1 + 2)]
entry_point = [0, 500 - x_min + y_max]
caves[entry_point[0]][entry_point[1]] = '+'

for path in paths:
    for point, next_point in zip(path[:-1], path[1:]):
        x_diff = int(next_point[0]) - int(point[0])
        if x_diff > 0:
            x_range = range(x_diff + 1)
        elif x_diff < 0:
            x_range = range(x_diff, 1)
        else:
            x_range = range(1)
        for x in x_range:
            y_diff = int(next_point[1]) - int(point[1])
            if y_diff > 0:
                y_range = range(y_diff + 1)
            elif y_diff < 0:
                y_range = range(y_diff, 1)
            else:
                y_range = range(1)
            for y in y_range:
                caves[int(point[1]) + y][int(point[0]) - x_min + y_max + x] = 'X'

caves[-1] = ['X' for i in range(x_max - x_min + 1 + 2 * y_max)]


def fill_with_sand(tunnels, sand_point):
    full = False
    sand_count = 0
    while not full:
        current_pos = sand_point.copy()
        landed = False
        while not landed:
            if current_pos[0] + 1 >= len(tunnels):
                full = True
                landed = True
                break
            if tunnels[current_pos[0] + 1][current_pos[1]] == '.':
                current_pos = [current_pos[0] + 1, current_pos[1]]
                continue
            if current_pos[1] - 1 < 0:
                full = True
                landed = True
                break
            if tunnels[current_pos[0] + 1][current_pos[1] - 1] == '.':
                current_pos = [current_pos[0] + 1, current_pos[1] - 1]
                continue
            if current_pos[1] + 1 > len(tunnels[0]):
                full = True
                landed = True
                break
            if tunnels[current_pos[0] + 1][current_pos[1] + 1] == '.':
                current_pos = [current_pos[0] + 1, current_pos[1] + 1]
                continue
            tunnels[current_pos[0]][current_pos[1]] = 'o'
            sand_count += 1
            if current_pos[0] == sand_point[0] and current_pos[1] == sand_point[1]:
                full = True
            landed = True
    print(sand_count)


fill_with_sand(caves, entry_point)
for x in caves:
    line = ''
    for y in x:
        line += y
    print(line)
