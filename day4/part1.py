data = open('input.txt').read().splitlines()

pairs = [x.split(',') for x in data]
pairs_split = [[x[0].split('-'), x[1].split('-')] for x in pairs]

print(sum(int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1]) or int(y[0]) <= int(x[0]) and int(y[1]) >= int(x[1]) for [x, y] in pairs_split))