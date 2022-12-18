import numpy as np
data = open('input.txt').read().splitlines()

droplets_str = [z.split(',') for z in data]
droplets = [[int(y) for y in x] for x in droplets_str]


def count_adjacencies_in_direction(direc, fixed_dir_1, fixed_dir_2, droplet_array):
    dir_adj_count = 0
    for z in range(np.max([d[fixed_dir_1] for d in droplets]) + 1):
        for y in range(np.max([d[fixed_dir_2] for d in droplets]) + 1):
            dir_drops = [drop[direc] for drop in list(filter(lambda d: d[fixed_dir_2] == y and d[fixed_dir_1] == z, droplet_array))]
            dir_drops.sort()
            for drop_one, drop_two in zip(dir_drops, dir_drops[1:]):
                if drop_two == drop_one + 1:
                    dir_adj_count += 1
    return dir_adj_count


x_adj_count = count_adjacencies_in_direction(0, 1, 2, droplets)
y_adj_count = count_adjacencies_in_direction(1, 0, 2, droplets)
z_adj_count = count_adjacencies_in_direction(2, 0, 1, droplets)

total_sides = len(droplets) * 6

print(total_sides - x_adj_count * 2 - y_adj_count * 2 - z_adj_count * 2)


