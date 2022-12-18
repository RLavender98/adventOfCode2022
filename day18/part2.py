from ast import literal_eval

import numpy as np
data = open('input.txt').read().splitlines()


droplets_str = [z.split(',') for z in data]
droplets = [[int(y) for y in x] for x in droplets_str]


directions = [[0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]]


def air_gap_is_trapped(air_gap_coords, droplet_array):
    droplet_array_str = [f'{point}' for point in droplet_array]
    x_min = np.min([d[0] for d in droplet_array])
    x_max = np.max([d[0] for d in droplet_array])
    y_min = np.min([d[1] for d in droplet_array])
    y_max = np.max([d[1] for d in droplet_array])
    z_min = np.min([d[2] for d in droplet_array])
    z_max = np.max([d[2] for d in droplet_array])
    visited = {f'{air_gap_coords}'}
    edges = {f'{air_gap_coords}'}
    while True:
        new_edges = [[literal_eval(edge)[0] + d[0], literal_eval(edge)[1] + d[1], literal_eval(edge)[2] + d[2]] for edge in edges for d in directions]
        new_edges = list(filter(lambda e: f'{e}' not in droplet_array_str and f'{e}' not in edges, new_edges))
        new_edges = list(filter(lambda e: f'{e}' not in visited, new_edges))
        visited.update(edges)
        edges = set([f'{e}' for e in new_edges])
        if not all([x_min < e[0] < x_max and y_min < e[1] < y_max and z_min < e[2] < z_max for e in new_edges]):
            return False
        if len(edges) == 0:
            return True


def fill_interior_holes(droplet_array):
    new_droplet_array = droplet_array.copy()
    for x in range(np.min([d[0] for d in droplet_array]), np.max([d[0] for d in droplet_array]) + 1):
        for y in range(np.min([d[1] for d in droplet_array]), np.max([d[1] for d in droplet_array]) + 1):
            dir_drops = [drop[2] for drop in list(filter(lambda d: d[1] == y and d[0] == x, droplet_array))]
            dir_drops.sort()
            # print(dir_drops)
            for drop_one, drop_two in zip(dir_drops, dir_drops[1:]):
                if drop_two != drop_one + 1:
                    if air_gap_is_trapped([x, y, drop_one + 1], droplet_array):
                        for z_gap in range(drop_one + 1, drop_two):
                            print([x, y, z_gap])
                            new_droplet_array.append([x, y, z_gap])
    return new_droplet_array


def count_adjacencies_in_direction(direc, fixed_dir_1, fixed_dir_2, droplet_array):
    dir_adj_count = 0
    for z in range(np.max([d[fixed_dir_1] for d in droplet_array]) + 1):
        for y in range(np.max([d[fixed_dir_2] for d in droplet_array]) + 1):
            dir_drops = [drop[direc] for drop in list(filter(lambda d: d[fixed_dir_2] == y and d[fixed_dir_1] == z, droplet_array))]
            dir_drops.sort()
            for drop_one, drop_two in zip(dir_drops, dir_drops[1:]):
                if drop_two == drop_one + 1:
                    dir_adj_count += 1
    return dir_adj_count


droplets_filled = fill_interior_holes(droplets.copy())

x_adj_count = count_adjacencies_in_direction(0, 1, 2, droplets_filled)
y_adj_count = count_adjacencies_in_direction(1, 0, 2, droplets_filled)
z_adj_count = count_adjacencies_in_direction(2, 0, 1, droplets_filled)

total_sides = len(droplets_filled) * 6

print(total_sides - x_adj_count * 2 - y_adj_count * 2 - z_adj_count * 2)


