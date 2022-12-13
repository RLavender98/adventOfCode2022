from ast import literal_eval

import numpy as np

packet_pairs = [x.split('\n') for x in open('input.txt').read().split('\n\n')]


def compare_packets(left, right):
    for i in range(np.min([len(left), len(right)])):
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] < right[i]:
                return 'correct'
            if right[i] < left[i]:
                return 'incorrect'
            continue
        if type(left[i]) is list and type(right[i]) is list:
            sub_compare = compare_packets(left[i], right[i])
            if sub_compare == 'correct':
                return 'correct'
            if sub_compare == 'incorrect':
                return 'incorrect'
            continue
        if type(left[i]) is list:
            sub_compare = compare_packets(left[i], [right[i]])
            if sub_compare == 'correct':
                return 'correct'
            if sub_compare == 'incorrect':
                return 'incorrect'
            continue
        sub_compare = compare_packets([left[i]], right[i])
        if sub_compare == 'correct':
            return 'correct'
        if sub_compare == 'incorrect':
            return 'incorrect'
    if len(left) < len(right):
        return 'correct'
    if len(left) > len(right):
        return 'incorrect'


ans = 0
for i in range(len(packet_pairs)):
    val = compare_packets(literal_eval(packet_pairs[i][0]), literal_eval(packet_pairs[i][1]))
    if val == 'correct':
        ans += i + 1

print(ans)
