data = open('input.txt').read().splitlines()

file = [[int(x), False] for x in data]


def mix(file_array):
    file_length = len(file)
    index = 0
    while index < file_length:
        if not file_array[index][1]:
            movement = file_array[index][0]
            end_index = (index + movement) % (file_length - 1)
            file_array.pop(index)
            file_array.insert(end_index, [movement, True])
        else:
            index += 1


mix(file)

file_stripped = [x[0] for x in file]
index_of_zero = file_stripped.index(0)
value_1 = file_stripped[(index_of_zero + 1000) % len(file_stripped)]
value_2 = file_stripped[(index_of_zero + 2000) % len(file_stripped)]
value_3 = file_stripped[(index_of_zero + 3000) % len(file_stripped)]
print(value_1 + value_2 + value_3)
