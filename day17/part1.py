import numpy as np

data = open('input.txt').read()


# data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
air_jets = list(data)

# print(air_jets)


def start_pos_of_rock_1(highest_block):
    base_y = highest_block + 4
    return [[2, base_y], [3, base_y], [4, base_y], [5, base_y]]


def start_pos_of_rock_2(highest_block):
    base_y = highest_block + 4
    return [[2, base_y + 1], [3, base_y], [3, base_y + 1], [3, base_y + 2], [4, base_y + 1]]


def start_pos_of_rock_3(highest_block):
    base_y = highest_block + 4
    return [[2, base_y], [3, base_y], [4, base_y], [4, base_y + 1], [4, base_y + 2]]


def start_pos_of_rock_4(highest_block):
    base_y = highest_block + 4
    return [[2, base_y], [2, base_y + 1], [2, base_y + 2], [2, base_y + 3]]


def start_pos_of_rock_5(highest_block):
    base_y = highest_block + 4
    return [[2, base_y], [3, base_y], [2, base_y + 1], [3, base_y + 1]]


def fall_one(rock, highest_blocks, rocks):
    if any([highest_blocks[point[0]] == point[1] - 1 for point in rock]):
        return 'stops'
    if any([[point[0], point[1] - 1] in rocks for point in rock]):
        return 'stops'
    return [[point[0], point[1] - 1] for point in rock]


def apply_air_jet(rock, air_jet_direction, rocks):
    if air_jet_direction == '>':
        if any([point[0] == 6 for point in rock]):
            return rock
        if any([[point[0] + 1, point[1]] in rocks for point in rock]):
            return rock
        return [[point[0] + 1, point[1]] for point in rock]
    if any([point[0] == 0 for point in rock]):
        return rock
    if any([[point[0] - 1, point[1]] in rocks for point in rock]):
        return rock
    return [[point[0] - 1, point[1]] for point in rock]


def update_max_heights(heights, rock):
    for column in range(7):
        if any([point[0] == column for point in rock]):
            max_rock_in_column = np.max([point[1] for point in rock if point[0] == column])
            if max_rock_in_column > heights[column]:
                heights[column] = max_rock_in_column


column_width = 7
highest_block_in_column = [0 for j in range(column_width)]
air_jet_pos = 0
rocks = []

for i in range(2022):
    if i % 1000000 == 0:
        print(i)
    # select rock
    rock_number = i % 5 + 1
    rock_pos = []
    if rock_number == 1:
        rock_pos = start_pos_of_rock_1(np.max(highest_block_in_column))
    if rock_number == 2:
        rock_pos = start_pos_of_rock_2(np.max(highest_block_in_column))
    if rock_number == 3:
        rock_pos = start_pos_of_rock_3(np.max(highest_block_in_column))
    if rock_number == 4:
        rock_pos = start_pos_of_rock_4(np.max(highest_block_in_column))
    if rock_number == 5:
        rock_pos = start_pos_of_rock_5(np.max(highest_block_in_column))
    # move rock into resting place
    stopped = False
    while not stopped:
        # air jet
        rock_pos = apply_air_jet(rock_pos, air_jets[air_jet_pos], rocks)
        air_jet_pos += 1
        if air_jet_pos >= len(air_jets):
            air_jet_pos = 0
        # fall down
        result_of_fall = fall_one(rock_pos, highest_block_in_column, rocks)
        if result_of_fall == 'stops':
            stopped = True
        else:
            rock_pos = result_of_fall
    # update highest heights
    update_max_heights(highest_block_in_column, rock_pos)
    rocks += rock_pos

print(np.max(highest_block_in_column))