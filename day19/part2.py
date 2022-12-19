import re

from ast import literal_eval

import numpy as np

data = open('input.txt').read().splitlines()

blueprints_str = [re.findall(r'\d+', blueprint) for blueprint in data]

# [0] - id
# [1] - ore cost of ore bot
# [2] - ore cost of clay bot
# [3], [4] - ore and clay cost of obsidian bot
# [5], [6] - ore and obsidian cost of geode bot
blueprints = [[int(y) for y in x] for x in blueprints_str]

# [0] - ore
# [1] - clay
# [2] - obsidian
# [3] - geodes
reserves = [0, 0, 0, 0]

# [0] - ore bots
# [1] - clay bots
# [2] - obsidian bots
# [3] - geode bots
bots = [1, 0, 0, 0]


def get_minutes_worth_of_mining(bot_array):
    return bot_array.copy()


def can_make_bot(material_array, cost_array):
    return all([x >= y for x, y in zip(material_array, cost_array)])


def can_make_geode_bot(reserve_array, blueprint_array):
    return can_make_bot([reserve_array[0], reserve_array[2]], [blueprint_array[5], blueprint_array[6]])


def can_make_obsidian_bot(reserve_array, blueprint_array):
    return can_make_bot([reserve_array[0], reserve_array[1]], [blueprint_array[3], blueprint_array[4]])


def can_make_clay_bot(reserve_array, blueprint_array):
    return can_make_bot([reserve_array[0]], [blueprint_array[2]])


def can_make_ore_bot(reserve_array, blueprint_array):
    return can_make_bot([reserve_array[0]], [blueprint_array[1]])


def make_geode_bot(reserve_array, blueprint_array, time_left):
    reserve_array[2] -= blueprint_array[6]
    reserve_array[0] -= blueprint_array[5]
    reserve_array[3] += time_left - 1


def make_obsidian_bot(reserve_array, bot_array, blueprint_array):
    reserve_array[1] -= blueprint_array[4]
    reserve_array[0] -= blueprint_array[3]
    bot_array[2] += 1


def make_clay_bot(reserve_array, bot_array, blueprint_array):
    reserve_array[0] -= blueprint_array[2]
    bot_array[1] += 1


def make_ore_bot(reserve_array, bot_array, blueprint_array):
    reserve_array[0] -= blueprint_array[1]
    bot_array[0] += 1


def increase_reserves(reserve_array, new_mined_stuff):
    reserve_array[0] += new_mined_stuff[0]
    reserve_array[1] += new_mined_stuff[1]
    reserve_array[2] += new_mined_stuff[2]
    reserve_array[3] += new_mined_stuff[3]


def increase_state_reserves(state_array, new_mined_stuff):
    for state in state_array:
        increase_reserves(state[0], new_mined_stuff)


def remove_duplicates(state_array):
    state_set = set([f'{state[0]};{state[1]}' for state in state_array])
    state_array_str = [state.split(';') for state in state_set]
    state_array_str_str = [[literal_eval(state[0]), literal_eval(state[1])] for state in state_array_str]
    return [[[int(x) for x in state[0]], [int(y) for y in state[1]]] for state in state_array_str_str]


def reduce_states(state_array, time_left):
    state_array = remove_duplicates(state_array)
    max_geodes = np.max([state[0][3] for state in state_array])
    # max_obsidian_bots = np.max([state[1][2] for state in state_array])
    filtered_states = []
    for state in state_array:
        if state[0][3] >= max_geodes - time_left:
            filtered_states.append(state)
    print(max_geodes)
    print(np.min([state[0][3] for state in state_array]))
    return filtered_states


# breadth first
def get_blueprint_quality_level(blueprint_array, reserve_array, bot_array):
    states = [[reserve_array, bot_array]]
    for i in range(32, 0, -1):
        print(i)
        print(len(states))
        round_states = []
        for state in states:
            reserve_array = state[0]
            bot_array = state[1]
            new_mined_stuff = get_minutes_worth_of_mining(bot_array)
            new_states = [state]
            geo_bot_made = False
            if can_make_geode_bot(reserve_array, blueprint_array):
                new_reserve_array = reserve_array.copy()
                new_bot_array = bot_array.copy()
                make_geode_bot(new_reserve_array, blueprint_array, i)
                new_states = [[new_reserve_array.copy(), new_bot_array.copy()]]
                geo_bot_made = True
            if not geo_bot_made and can_make_obsidian_bot(reserve_array, blueprint_array) and bot_array[2] < blueprint_array[6]:
                new_reserve_array = reserve_array.copy()
                new_bot_array = bot_array.copy()
                make_obsidian_bot(new_reserve_array, new_bot_array, blueprint_array)
                new_states.append([new_reserve_array.copy(), new_bot_array.copy()])
            if not geo_bot_made and can_make_clay_bot(reserve_array, blueprint_array) and bot_array[1] < blueprint_array[4]:
                new_reserve_array = reserve_array.copy()
                new_bot_array = bot_array.copy()
                make_clay_bot(new_reserve_array, new_bot_array, blueprint_array)
                new_states.append([new_reserve_array.copy(), new_bot_array.copy()])
            if not geo_bot_made and can_make_ore_bot(reserve_array, blueprint_array) and bot_array[0] < 4:
                new_reserve_array = reserve_array.copy()
                new_bot_array = bot_array.copy()
                make_ore_bot(new_reserve_array, new_bot_array, blueprint_array)
                new_states.append([new_reserve_array.copy(), new_bot_array.copy()])
            increase_state_reserves(new_states, new_mined_stuff)
            for new_state in new_states:
                round_states.append(new_state)
        states = round_states
        states = reduce_states(states, i)
    return np.max([state[0][3] for state in states])


one = get_blueprint_quality_level(blueprints[0], reserves.copy(), bots.copy())
two = get_blueprint_quality_level(blueprints[1], reserves.copy(), bots.copy())
three = get_blueprint_quality_level(blueprints[2], reserves.copy(), bots.copy())
print(one * two * three)