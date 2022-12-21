import re

data = open('input.txt').read().splitlines()

monkeys = [re.findall(r'(\d+|\w+|\*|\+|/|-)', monkey) for monkey in data]

monkey_dict = dict()

for monkey in monkeys:
    monkey_dict[monkey[0]] = monkey[1:]

print(monkey_dict)


def get_value_shouted_by_monkey_with_name(name):
    if len(monkey_dict[name]) == 1:
        return int(monkey_dict[name][0])
    if monkey_dict[name][1] == '*':
        return get_value_shouted_by_monkey_with_name(monkey_dict[name][0]) * get_value_shouted_by_monkey_with_name(monkey_dict[name][2])
    if monkey_dict[name][1] == '/':
        return get_value_shouted_by_monkey_with_name(monkey_dict[name][0]) / get_value_shouted_by_monkey_with_name(monkey_dict[name][2])
    if monkey_dict[name][1] == '+':
        return get_value_shouted_by_monkey_with_name(monkey_dict[name][0]) + get_value_shouted_by_monkey_with_name(monkey_dict[name][2])
    if monkey_dict[name][1] == '-':
        return get_value_shouted_by_monkey_with_name(monkey_dict[name][0]) - get_value_shouted_by_monkey_with_name(monkey_dict[name][2])


def search(some_monkeys):
    some_monkeys['humn'] = [5128434600306]
    step = 2**40
    search_val = 51928434600306
    closeness_measure = search_val - get_value_shouted_by_monkey_with_name('rjmz')
    while True:
        while closeness_measure > 0:
            some_monkeys['humn'] = [some_monkeys['humn'][0] - step]
            closeness_measure = search_val - get_value_shouted_by_monkey_with_name('rjmz')
            if closeness_measure == 0:
                return some_monkeys['humn']
            step = step / 2
        while closeness_measure < 0:
            some_monkeys['humn'] = [some_monkeys['humn'][0] + step]
            closeness_measure = search_val - get_value_shouted_by_monkey_with_name('rjmz')
            if closeness_measure == 0:
                return some_monkeys['humn']
            step = step / 2

print(search(monkey_dict))
