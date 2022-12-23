data = open('input.txt').read().splitlines()

data = [list(x) for x in data]


def increase_field(field_array):
    width = len(field_array[0])
    bigger_field = []
    bigger_field += [['.' for j in range(width * 11)] for i in range(width * 5)]
    for line in field_array:
        bigger_field.append(['.' for j in range(width * 5)] + line + ['.' for j in range(width * 5)])
    bigger_field += [['.' for j in range(width * 11)] for i in range(width * 5)]
    return bigger_field


def get_adjacent_locations(field_array, index_1, index_2):
    return [field_array[index_1 - 1][index_2 - 1],
            field_array[index_1 - 1][index_2],
            field_array[index_1 - 1][index_2 + 1],
            field_array[index_1][index_2 - 1],
            field_array[index_1][index_2 + 1],
            field_array[index_1 + 1][index_2 - 1],
            field_array[index_1 + 1][index_2],
            field_array[index_1 + 1][index_2 + 1]]


def get_move_in_direction_if_poss(field_array, index_1, index_2, direction):
    # North
    if direction == 0:
        if field_array[index_1 - 1][index_2 - 1] == '.' and field_array[index_1 - 1][index_2] == '.' and field_array[index_1 - 1][index_2 + 1] == '.':
            return [index_1 - 1, index_2]
    # South
    if direction == 1:
        if field_array[index_1 + 1][index_2 - 1] == '.' and field_array[index_1 + 1][index_2] == '.' and field_array[index_1 + 1][index_2 + 1] == '.':
            return [index_1 + 1, index_2]
    # West
    if direction == 2:
        if field_array[index_1 - 1][index_2 - 1] == '.' and field_array[index_1][index_2 - 1] == '.' and field_array[index_1 + 1][index_2 - 1] == '.':
            return [index_1, index_2 - 1]
    # East
    if direction == 3:
        if field_array[index_1 - 1][index_2 + 1] == '.' and field_array[index_1][index_2 + 1] == '.' and field_array[index_1 + 1][index_2 + 1] == '.':
            return [index_1, index_2 + 1]
    return 'nope'


def get_desired_move(field_array, index_1, index_2, current_priority):
    priorities = [current_priority, current_priority + 1, current_priority + 2, current_priority + 3]
    priorities = [x % 4 for x in priorities]
    for direction in priorities:
        maybe_move = get_move_in_direction_if_poss(field_array, index_1, index_2, direction)
        if maybe_move != 'nope':
            return maybe_move
    return 'nope'


def get_moves(field_array, current_priority):
    the_moves = []
    for j in range(len(field_array)):
        for i in range(len(field_array[0])):
            if field_array[j][i] == '#':
                if any([loc == '#' for loc in get_adjacent_locations(field_array, j, i)]):
                    move = get_desired_move(field_array, j, i, current_priority)
                    if move != 'nope':
                        the_moves.append([[j, i], move])
    return the_moves


def remove_duplicate_moves(moves_array):
    poss_moves = []
    for key, this_move in enumerate(moves_array):
        if all([other_move[1][0] != this_move[1][0] or other_move[1][1] != this_move[1][1] for other_move in moves_array[:key]])\
                and all([other_move[1][0] != this_move[1][0] or other_move[1][1] != this_move[1][1] for other_move in moves_array[key + 1:]]):
            poss_moves.append(this_move)
    return poss_moves


field = increase_field(data)
cur_priority = 0

finished = False
turn = 1
while not finished:
    moves = get_moves(field, cur_priority)
    if len(moves) == 0:
        finished = True
        print(turn)
    moves = remove_duplicate_moves(moves)
    for move in moves:
        field[move[0][0]][move[0][1]] = '.'
        field[move[1][0]][move[1][1]] = '#'
    cur_priority += 1
    cur_priority = cur_priority % 4
    turn += 1

