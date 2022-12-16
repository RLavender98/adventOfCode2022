import re
from ast import literal_eval

import numpy as np

data = open('input.txt').read().splitlines()


def path_to_set_member(path_list):
    path_list[0].sort()
    return f'{path_list[0]};{path_list[1]};{path_list[2]}'


def set_member_to_path(set_member):
    array = set_member.split(';')
    return [literal_eval(array[0]), literal_eval(array[1]), int(array[2])]


def remove_duplicates(array_of_paths):
    set_of_paths = set([path_to_set_member(array_path) for array_path in array_of_paths])
    array_from_set = [set_member_to_path(z) for z in set_of_paths]
    return array_from_set


def name_pair_matches_str_pair(pair, str_pair):
    pair.sort()
    pair_as_str = f'{pair[0]},{pair[1]}'
    return pair_as_str == str_pair


def remove_same_point_lower_value(array_of_paths, minutes_left_of_flow):
    array_of_paths.sort()
    current_node_pairs = [x[0] for x in array_of_paths]
    for y in current_node_pairs:
        y.sort()
    string_pairs = set([f'{y[0]},{y[1]}' for y in current_node_pairs])
    to_return = []
    for pair in string_pairs:
        paths_at_node_with_names = list(filter(lambda p: name_pair_matches_str_pair(p[0], pair), array_of_paths))
        maxi = np.max([p[2] for p in paths_at_node_with_names])
        maxis = list(filter(lambda p: p[2] >= maxi - minutes_left_of_flow * 24, paths_at_node_with_names))
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

paths = [[['AA', 'AA'], [], 0]]
for i in range(26, 0, -1):
    print(i)
    next_paths = []
    for path in paths:
        current_node_names = path[0]
        my_current_node = current_node_names[0]
        elephants_current_node = current_node_names[1]
        turned_on_valves = path[1]
        if len(turned_on_valves) == 14:
            print(path[2])
        if my_current_node not in turned_on_valves and nodes[my_current_node][0] > 0:
            turned_on_by_me = turned_on_valves.copy()
            turned_on_by_me.append(my_current_node)
            path_updated_by_me = [path[0], turned_on_by_me, path[2] + nodes[my_current_node][0] * (i - 1)]
            if elephants_current_node not in turned_on_by_me and nodes[elephants_current_node][0] > 0:
                turned_on = turned_on_by_me.copy()
                turned_on.append(elephants_current_node)
                path_updated_by_elephant = [path_updated_by_me[0], turned_on, path_updated_by_me[2] + nodes[elephants_current_node][0] * (i-1)]
                next_paths.append(path_updated_by_elephant)
            for connection in nodes[elephants_current_node][1]:
                path_updated_by_elephant = [[path_updated_by_me[0][0], connection], path_updated_by_me[1].copy(), path_updated_by_me[2]]
                next_paths.append(path_updated_by_elephant)
        for me_connection in nodes[my_current_node][1]:
            path_updated_by_me = [[me_connection, path[0][1]], path[1].copy(), path[2]]
            if elephants_current_node not in turned_on_valves and nodes[elephants_current_node][0] > 0:
                turned_on = turned_on_valves.copy()
                turned_on.append(elephants_current_node)
                path_updated_by_elephant = [path_updated_by_me[0], turned_on, path_updated_by_me[2] + nodes[elephants_current_node][0] * (i-1)]
                next_paths.append(path_updated_by_elephant)
            for connection in nodes[elephants_current_node][1]:
                path_updated_by_elephant = [[path_updated_by_me[0][0], connection], path_updated_by_me[1].copy(), path_updated_by_me[2]]
                next_paths.append(path_updated_by_elephant)
    paths = remove_redundant_paths(next_paths, i - 1)

print(np.max([path[2] for path in paths]))