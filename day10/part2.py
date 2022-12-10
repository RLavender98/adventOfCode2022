data = open('input.txt').read().splitlines()

cycle_number = 1
in_a_double = False
register_X = 2

current_line = ''
crt_line = ''

while cycle_number < 241:
    if register_X - 1 <= cycle_number % 40 <= register_X + 1:
        crt_line += '#'
    else:
        crt_line += '.'
    if cycle_number % 40 == 0:
        print(crt_line)
        crt_line = ''
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
