import numpy as np

data = open('input.txt', 'r', encoding='utf-8').read().splitlines()

count = 0
counts = []
for i in range(len(data)):
    if data[i] == '':
        counts.append(count)
        count = 0
    else:
        count += int(data[i])

print(np.max(counts))
