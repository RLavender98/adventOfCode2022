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


print(get_value_shouted_by_monkey_with_name('root'))
