import re

data = open('input.txt').read().splitlines()


coords = [re.findall(r'\d+', x) for x in data]

def get_taxi_dist(coord1, coord2):
    x_diff = abs(coord1[0] - coord2[0])
    y_diff = abs(coord1[1] - coord2[1])
    return x_diff + y_diff


def get_dead_region(sensor_coords, beacon_coords, y_value):
    taxi_dist = get_taxi_dist(sensor_coords, beacon_coords)
    y_dist = abs(sensor_coords[1] - y_value)
    max_x_dist = taxi_dist - y_dist
    if max_x_dist < 0:
        return 'nope'
    return [sensor_coords[0] - max_x_dist, sensor_coords[0] + max_x_dist]


dead_regions = [get_dead_region([int(coord_set[0]), int(coord_set[1])], [int(coord_set[2]), int(coord_set[3])], 2000000) for
                coord_set in coords]

while 'nope' in dead_regions:
    dead_regions.remove('nope')

print(dead_regions)
dead_regions.sort()
print(dead_regions)

count = 4208796 + 671176

beacon_x = set()
for coord in coords:
    if int(coord[3]) == 9:
        beacon_x.update((int(coord[2]),))

for x in beacon_x:
    if any([region[0] <= x <= region[1] for region in dead_regions]):
        count -= 1

print(count)