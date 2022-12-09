import numpy as np

data = open('input.txt').read().splitlines()

moves = [x.split(' ') for x in data]


def move_if_needed(position_pair):
    # DIAGONALS
    if position_pair[0][0] > position_pair[1][0] + 1 and position_pair[0][1] > position_pair[1][1] + 1:
        position_pair[1][0] += 1
        position_pair[1][1] += 1
    if position_pair[0][0] > position_pair[1][0] + 1 and position_pair[0][1] < position_pair[1][1] - 1:
        position_pair[1][0] += 1
        position_pair[1][1] -= 1
    if position_pair[0][0] < position_pair[1][0] - 1 and position_pair[0][1] < position_pair[1][1] - 1:
        position_pair[1][0] -= 1
        position_pair[1][1] -= 1
    if position_pair[0][0] < position_pair[1][0] - 1 and position_pair[0][1] > position_pair[1][1] + 1:
        position_pair[1][0] -= 1
        position_pair[1][1] += 1


    if position_pair[0][0] > position_pair[1][0] + 1:
        position_pair[1][0] += 1
        position_pair[1][1] = position_pair[0][1]
    if position_pair[0][1] > position_pair[1][1] + 1:
        position_pair[1][1] += 1
        position_pair[1][0] = position_pair[0][0]
    if position_pair[0][0] < position_pair[1][0] - 1:
        position_pair[1][0] -= 1
        position_pair[1][1] = position_pair[0][1]
    if position_pair[0][1] < position_pair[1][1] - 1:
        position_pair[1][1] -= 1
        position_pair[1][0] = position_pair[0][0]


def propagate_motion(current_positions, visited_positions):
    for i in range(1, len(current_positions)):
        move_if_needed([current_positions[i - 1], current_positions[i]])
    visited_positions.append(f'{current_positions[-1][0]},{current_positions[-1][1]}')


def move_right(number_of_steps, starty_positions, visited_positions):
    for i in range(number_of_steps):
        starty_positions[0][0] += 1
        propagate_motion(starty_positions, visited_positions)


def move_left(number_of_steps, starty_positions, visited_positions):
    for i in range(number_of_steps):
        starty_positions[0][0] -= 1
        propagate_motion(starty_positions, visited_positions)


def move_up(number_of_steps, starty_positions, visited_positions):
    for i in range(number_of_steps):
        starty_positions[0][1] += 1
        propagate_motion(starty_positions, visited_positions)


def move_down(number_of_steps, starty_positions, visited_positions):
    for i in range(number_of_steps):
        starty_positions[0][1] -= 1
        propagate_motion(starty_positions, visited_positions)


def read_move(move, start_positions, visited_positions):
    if move[0] == 'R':
        move_right(int(move[1]), start_positions, visited_positions)
    if move[0] == 'L':
        move_left(int(move[1]), start_positions, visited_positions)
    if move[0] == 'U':
        move_up(int(move[1]), start_positions, visited_positions)
    if move[0] == 'D':
        move_down(int(move[1]), start_positions, visited_positions)


start_positions = [[0, 0] for x in range(10)]
visited_positions = ['0,0']


def grid(positions):
    minx = np.min([x[0] for x in positions])
    miny = np.min([x[1] for x in positions])
    height = np.max([x[1] for x in positions]) - miny
    width = np.max([x[0] for x in positions]) - minx
    transformed = [[x[0] - minx, x[1] - miny] for x in positions]
    gridd = [['O' for x in range(width + 1)] for y in range(height + 1)]
    for point in transformed:
        gridd[height - point[1]][point[0]] = 'X'
    for line in gridd:
        print(line)


for move in moves:
    read_move(move, start_positions, visited_positions)
    grid(start_positions)
    print('==============')

print(len(set(visited_positions)))
