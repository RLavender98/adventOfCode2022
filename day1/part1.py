import numpy as np

data = open('input.txt', 'r', encoding='utf-8').read().splitlines()


def func(x):
    if x == '':
        return 0
    else:
        return int(x)


calories = [func(x) for x in data]

count = 0
counts = []
for i in range(len(calories)):
    if calories[i] == 0:
        counts.append(count)
        count = 0
    else:
        count += calories[i]

print(np.max(counts))
