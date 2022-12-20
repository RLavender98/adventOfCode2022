data = open('input.txt').read().splitlines()

file = []
for i in range(len(data)):
    file.append([int(data[i]) * 811589153, i])


def mix(file_array):
    file_length = len(file)
    for grfu in range(file_length):
        index = file_array.index(list(filter(lambda y: y[1] == grfu, file_array))[0])
        movement = file_array[index][0]
        end_index = (index + movement) % (file_length - 1)
        file_array.pop(index)
        file_array.insert(end_index, [movement, grfu])


def mix_10_times(file_array):
    for gfh in range(10):
        mix(file_array)


mix_10_times(file)

file_stripped = [x[0] for x in file]
index_of_zero = file_stripped.index(0)
value_1 = file_stripped[(index_of_zero + 1000) % len(file_stripped)]
value_2 = file_stripped[(index_of_zero + 2000) % len(file_stripped)]
value_3 = file_stripped[(index_of_zero + 3000) % len(file_stripped)]
print(value_1 + value_2 + value_3)
