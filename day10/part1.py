data = open('input.txt').read().splitlines()

cycle_number = 1
in_a_double = False
register_X = 1
sum = 0

current_line = ''

while cycle_number < 221:
    if cycle_number % 40 == 20:
        sum += cycle_number * register_X
    if in_a_double:
        register_X += int(current_line.split(' ')[1])
        in_a_double = False
        cycle_number += 1
        continue
    current_line = data[0]
    data.pop(0)
    if current_line == 'noop':
        cycle_number += 1
        continue
    cycle_number += 1
    in_a_double = True

print(sum)