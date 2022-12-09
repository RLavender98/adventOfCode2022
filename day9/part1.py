data = open('input.txt').read().splitlines()

moves = [x.split(' ') for x in data]


def move_right(number_of_steps, start_positions, visited_positions):
    for i in range(number_of_steps):
        start_positions[0][0] += 1
        if start_positions[0][0] - start_positions[1][0] > 1:
            start_positions[1][1] = start_positions[0][1]
            start_positions[1][0] = start_positions[0][0] - 1
            visited_positions.append(f'{start_positions[1][0]},{start_positions[1][1]}')
    return start_positions


def move_left(number_of_steps, start_positions, visited_positions):
    for i in range(number_of_steps):
        start_positions[0][0] -= 1
        if start_positions[1][0] - start_positions[0][0] > 1:
            start_positions[1][1] = start_positions[0][1]
            start_positions[1][0] = start_positions[0][0] + 1
            visited_positions.append(f'{start_positions[1][0]},{start_positions[1][1]}')
    return start_positions


def move_up(number_of_steps, start_positions, visited_positions):
    for i in range(number_of_steps):
        start_positions[0][1] += 1
        if start_positions[0][1] - start_positions[1][1] > 1:
            start_positions[1][0] = start_positions[0][0]
            start_positions[1][1] = start_positions[0][1] - 1
            visited_positions.append(f'{start_positions[1][0]},{start_positions[1][1]}')
    return start_positions


def move_down(number_of_steps, start_positions, visited_positions):
    for i in range(number_of_steps):
        start_positions[0][1] -= 1
        if start_positions[1][1] - start_positions[0][1] > 1:
            start_positions[1][0] = start_positions[0][0]
            start_positions[1][1] = start_positions[0][1] + 1
            visited_positions.append(f'{start_positions[1][0]},{start_positions[1][1]}')
    return start_positions


def read_move(move, start_positions, visited_positions):
    if move[0] == 'R':
        return move_right(int(move[1]), start_positions, visited_positions)
    if move[0] == 'L':
        return move_left(int(move[1]), start_positions, visited_positions)
    if move[0] == 'U':
        return move_up(int(move[1]), start_positions, visited_positions)
    if move[0] == 'D':
        return move_down(int(move[1]), start_positions, visited_positions)


start_positions = [[0, 0], [0, 0]]
visited_positions = ['0,0']

for move in moves:
    start_positions = read_move(move, start_positions, visited_positions)

print(len(set(visited_positions)))