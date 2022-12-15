import re
import numpy as np

data = open('input.txt').read().splitlines()

coords = [re.findall(r'\d+', x) for x in data]


def get_taxi_dist(coord1, coord2):
    x_diff = abs(coord1[0] - coord2[0])
    y_diff = abs(coord1[1] - coord2[1])
    return x_diff + y_diff


def get_dead_region(sensor_coords, beacon_coords):
    taxi_dist = get_taxi_dist(sensor_coords, beacon_coords)
    return [[sensor_coords[0], sensor_coords[1] - taxi_dist],
            [sensor_coords[0] + taxi_dist, sensor_coords[1]],
            [sensor_coords[0], sensor_coords[1] + taxi_dist],
            [sensor_coords[0] - taxi_dist, sensor_coords[1]]]


dead_regions = [get_dead_region([int(coord_set[0]), int(coord_set[1])], [int(coord_set[2]), int(coord_set[3])]) for coord_set in coords]


def get_pos_line_intercepts(regions):
    intercepts = set()
    for region in regions:
        intercepts.update((region[0][1] - region[0][0],))
        intercepts.update((region[2][1] - region[2][0],))
    return intercepts


def get_neg_line_intercepts(regions):
    intercepts = set()
    for region in regions:
        intercepts.update((region[0][1] + region[0][0],))
        intercepts.update((region[2][1] + region[2][0],))
    return intercepts


pos_intercepts = get_pos_line_intercepts(dead_regions)
neg_intercepts = get_neg_line_intercepts(dead_regions)


def get_middle_of_close_intercepts(intercepts):
    middles = set()
    for i in range(len(intercepts) - 1):
        for j in range(i+1, len(intercepts)):
            if abs(intercepts[i] - intercepts[j]) == 2:
                middles.update((np.min([intercepts[i], intercepts[j]])+1,))
    return middles


def get_crossings(pos_line_intercepts, neg_line_intercepts):
    crossings = []
    for pos in pos_line_intercepts:
        for neg in neg_line_intercepts:
            x = int((neg - pos) / 2)
            y = x + pos
            crossings.append([x, y])
    return crossings


middle_crossings = get_crossings(get_middle_of_close_intercepts(list(pos_intercepts)), get_middle_of_close_intercepts(list(neg_intercepts)))
print(middle_crossings)


print(3131431 * 4000000 + 2647448)
