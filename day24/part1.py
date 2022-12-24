from numpy import lcm

data = open('input.txt').read().splitlines()
valley = [list(row) for row in data]


def get_blizzard_period(valley_array):
    return lcm(len(valley_array) - 2, len(valley_array[0]) - 2)


def get_blizzard_positions(valley_starting_map):
    blizzard_positions_array = []
    for row_key, row in enumerate(valley_starting_map):
        for column_key, space in enumerate(row):
            if space == '<':
                blizzard_positions_array.append([(row_key, column_key), 'L'])
            if space == '>':
                blizzard_positions_array.append([(row_key, column_key), 'R'])
            if space == '^':
                blizzard_positions_array.append([(row_key, column_key), 'U'])
            if space == 'v':
                blizzard_positions_array.append([(row_key, column_key), 'D'])
    return blizzard_positions_array


def get_free_spaces(blizzard_positions_array, valley_starting_map):
    free_spaces_array = []
    for row_key in range(1, len(valley_starting_map) - 1):
        for column_key in range(1, len(valley_starting_map[0]) - 1):
            if (row_key, column_key) not in [x[0] for x in blizzard_positions_array]:
                free_spaces_array.append((row_key, column_key))
    return free_spaces_array


def move_blizzards(blizzard_positions_array, valley_starting_map):
    new_blizzard_positions = []
    for blizzard in blizzard_positions_array:
        if blizzard[1] == 'L':
            if blizzard[0][1] == 1:
                new_blizzard_positions.append([(blizzard[0][0], len(valley_starting_map[0]) - 2), 'L'])
            else:
                new_blizzard_positions.append([(blizzard[0][0], blizzard[0][1] - 1), 'L'])
        if blizzard[1] == 'R':
            if blizzard[0][1] == len(valley_starting_map[0]) - 2:
                new_blizzard_positions.append([(blizzard[0][0], 1), 'R'])
            else:
                new_blizzard_positions.append([(blizzard[0][0], blizzard[0][1] + 1), 'R'])
        if blizzard[1] == 'U':
            if blizzard[0][0] == 1:
                new_blizzard_positions.append([(len(valley_starting_map) - 2, blizzard[0][1]), 'U'])
            else:
                new_blizzard_positions.append([(blizzard[0][0] - 1, blizzard[0][1]), 'U'])
        if blizzard[1] == 'D':
            if blizzard[0][0] == len(valley_starting_map) - 2:
                new_blizzard_positions.append([(1, blizzard[0][1]), 'D'])
            else:
                new_blizzard_positions.append([(blizzard[0][0] + 1, blizzard[0][1]), 'D'])
    return new_blizzard_positions


def calculate_spaces_throughout_period(valley_starting_map):
    blizzard_period_in_minutes = get_blizzard_period(valley_starting_map)
    blizzard_positions = get_blizzard_positions(valley_starting_map)
    free_spaces_each_minute = []
    for i in range(blizzard_period_in_minutes):
        free_spaces_each_minute.append(get_free_spaces(blizzard_positions, valley_starting_map))
        blizzard_positions = move_blizzards(blizzard_positions, valley_starting_map)
    return free_spaces_each_minute


def remove_duplicate_positions(position_array):
    reduced_positions = []
    for pos in position_array:
        if pos not in reduced_positions:
            reduced_positions.append(pos)
    return reduced_positions


def find_shortest_path_through(valley_starting_map):
    spaces_through_time_array = calculate_spaces_throughout_period(valley_starting_map)
    pos_array = [(0, 1)]
    time = 0
    while True:
        time += 1
        new_pos_array = []
        for pos in pos_array:
            steps_available = list(filter(lambda tup: (abs(tup[0] - pos[0]) <= 1 and tup[1] - pos[1] == 0) or (
                    tup[0] - pos[0] == 0 and abs(tup[1] - pos[1]) <= 1),
                                          spaces_through_time_array[time % len(spaces_through_time_array)]))
            for step in steps_available:
                new_pos_array.append(step)
        pos_array = remove_duplicate_positions(new_pos_array)
        pos_array.append((0, 1))
        if any([pos == (len(valley_starting_map) - 2, len(valley_starting_map[0]) - 2) for pos in pos_array]):
            return time + 1


print(find_shortest_path_through(valley))
