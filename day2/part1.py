data = open('input.txt', 'r', encoding='utf-8').read().splitlines()

rounds = [x.split(' ') for x in data]


def parse(x):
    if x == 'X':
        return 'A'
    if x == 'Y':
        return 'B'
    if x == 'Z':
        return 'C'


parsed = [[x[0], parse(x[1])] for x in rounds]


def outcome(x):
    if x[0] == x[1]:
        return 3
    if x[0] == 'A' and x[1] == 'B':
        return 6
    if x[0] == 'B' and x[1] == 'C':
        return 6
    if x[0] == 'C' and x[1] == 'A':
        return 6
    return 0


def choice(x):
    if x == 'A':
        return 1
    if x == 'B':
        return 2
    if x == 'C':
        return 3


outcome_total = sum([outcome(x) for x in parsed])
go_total = sum([choice(x[1]) for x in parsed])

print(outcome_total + go_total)
