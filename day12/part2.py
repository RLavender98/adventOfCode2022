elevation_map = [list(x) for x in open('input.txt').read().splitlines()]

start_index = [20, 0]
end_index = [20, 132]

values = 'abcdefghijklmnopqrstuvwxyz'

elevation_map[start_index[0]][start_index[1]] = 'a'
elevation_map[end_index[0]][end_index[1]] = 'z'


def pos_to_set_member(pos):
    return f'{pos[0]},{pos[1]}'


def set_member_to_pos(set_member):
    return [int(x) for x in set_member.split(',')]


def shortest_path_to_end(start_pos, end_pos):
    visited = {pos_to_set_member(start_pos)}
    edges = {pos_to_set_member(start_pos)}
    distance = 0
    found = False
    while not found:
        new_edges = edges.copy()
        for str_edge in edges:
            edge = set_member_to_pos(str_edge)
            if edge[1] < len(elevation_map[0]) - 1 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0]][edge[1] + 1]) - 1:
                new_edges.update((pos_to_set_member([edge[0], edge[1] + 1]),))
            if edge[1] > 0 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0]][edge[1] - 1]) - 1:
                new_edges.update((pos_to_set_member([edge[0], edge[1] - 1]),))
            if edge[0] < len(elevation_map) - 1 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0] + 1][edge[1]]) - 1:
                new_edges.update((pos_to_set_member([edge[0] + 1, edge[1]]),))
            if edge[0] > 0 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0] - 1][edge[1]]) - 1:
                new_edges.update((pos_to_set_member([edge[0] - 1, edge[1]]),))

        new_edges = new_edges.difference(edges).difference(visited)
        visited = edges | visited
        edges = new_edges
        distance += 1
        for str_edge in new_edges:
            if str_edge == pos_to_set_member(end_pos):
                found = True
    return distance


def shortest_path_to_d(start_pos):
    visited = {pos_to_set_member(start_pos)}
    edges = {pos_to_set_member(start_pos)}
    distance = 0
    found = False
    reachable = []
    while not found:
        new_edges = edges.copy()
        for str_edge in edges:
            edge = set_member_to_pos(str_edge)
            if edge[1] < len(elevation_map[0]) - 1 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0]][edge[1] + 1]) - 1:
                new_edges.update((pos_to_set_member([edge[0], edge[1] + 1]),))
            if edge[1] > 0 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0]][edge[1] - 1]) - 1:
                new_edges.update((pos_to_set_member([edge[0], edge[1] - 1]),))
            if edge[0] < len(elevation_map) - 1 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0] + 1][edge[1]]) - 1:
                new_edges.update((pos_to_set_member([edge[0] + 1, edge[1]]),))
            if edge[0] > 0 and values.index(elevation_map[edge[0]][edge[1]]) >= values.index(
                    elevation_map[edge[0] - 1][edge[1]]) - 1:
                new_edges.update((pos_to_set_member([edge[0] - 1, edge[1]]),))

        new_edges = new_edges.difference(edges).difference(visited)
        visited = edges | visited
        edges = new_edges
        distance += 1
        for str_edge in new_edges:
            edge = set_member_to_pos(str_edge)
            if elevation_map[edge[0]][edge[1]] == 'd':
                reachable.append(edge)
                found = True
    return distance

min_d = 10000
best_pos = [0, 0]
for i in range(len(elevation_map)):
    distance = shortest_path_to_d([i, 0])
    if min_d > distance:
        min_d = distance
        best_pos = [i, 0]
print(shortest_path_to_end(best_pos, end_index))
