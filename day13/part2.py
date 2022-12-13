from ast import literal_eval
from functools import cmp_to_key

import numpy as np

packets = open('input.txt').read().splitlines()

while '' in packets:
    packets.remove('')

packets.append('[[2]]')
packets.append('[[6]]')


def compare_packets(left, right):
    for i in range(np.min([len(left), len(right)])):
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] < right[i]:
                return 1
            if right[i] < left[i]:
                return -1
            continue
        if type(left[i]) is list and type(right[i]) is list:
            sub_compare = compare_packets(left[i], right[i])
            if sub_compare == 1:
                return 1
            if sub_compare == -1:
                return -1
            continue
        if type(left[i]) is list:
            sub_compare = compare_packets(left[i], [right[i]])
            if sub_compare == 1:
                return 1
            if sub_compare == -1:
                return -1
            continue
        sub_compare = compare_packets([left[i]], right[i])
        if sub_compare == 1:
            return 1
        if sub_compare == -1:
            return -1
    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return -1
    return 0


def compare(str_left, str_right):
    return compare_packets(literal_eval(str_left), literal_eval(str_right))

comp_key = cmp_to_key(compare)
packets.sort(key=comp_key)
packets.reverse()
print((packets.index('[[2]]') + 1) * (packets.index('[[6]]') + 1))
