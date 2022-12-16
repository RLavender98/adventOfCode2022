import re
from ast import literal_eval

import numpy as np

data = open('input.txt').read().splitlines()


def path_to_set_member(path_list):
    return f'{path_list[0]};{path_list[1]};{path_list[2]}'


def set_member_to_path(set_member):
    array = set_member.split(';')
    return [array[0], literal_eval(array[1]), int(array[2])]


def remove_duplicates(array_of_paths):
    set_of_paths = set([path_to_set_member(array_path) for array_path in array_of_paths])
    array_from_set = [set_member_to_path(z) for z in set_of_paths]
    return array_from_set


def remove_same_point_lower_value(array_of_paths, minutes_left_of_flow):
    array_of_paths.sort()
    current_node_names = set([x[0] for x in array_of_paths])
    to_return = []
    for name in current_node_names:
        paths_at_node_with_name = list(filter(lambda p: p[0] == name, array_of_paths))
        maxi = np.max([p[2] for p in paths_at_node_with_name])
        maxis = list(filter(lambda p: p[2] >= maxi - minutes_left_of_flow * 24, paths_at_node_with_name))
        to_return += maxis
    return to_return


def remove_redundant_paths(array_of_paths, minutes_left_of_flow):
    no_duplicate_array = remove_duplicates(array_of_paths)
    return remove_same_point_lower_value(no_duplicate_array, minutes_left_of_flow)


pattern = re.compile("([A-Z][A-Z]|\d+)")
parsed_data = [re.findall(pattern, x) for x in data]

nodes = dict()
for line in parsed_data:
    # name is key, value is flow then connections
    nodes[line[0]] = [int(line[1]), line[2:]]

paths = [['AA', [], 0]]
for i in range(30, 0, -1):
    print(i)
    next_paths = []
    for path in paths:
        current_node_name = path[0]
        turned_on_valves = path[1]
        if current_node_name not in turned_on_valves and nodes[current_node_name][0] > 0:
            turned_on = turned_on_valves.copy()
            turned_on.append(current_node_name)
            path_updated = [path[0], turned_on, path[2] + nodes[current_node_name][0] * (i-1)]
            next_paths.append(path_updated)
        for connection in nodes[current_node_name][1]:
            path_updated = [connection, path[1].copy(), path[2]]
            next_paths.append(path_updated)
    paths = remove_redundant_paths(next_paths, i - 1)
    print(paths)

print(np.max([path[2] for path in paths]))