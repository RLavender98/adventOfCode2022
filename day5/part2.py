data = open('input.txt').read()

[crates, instructions] = data.split('\n\n')

cratrix = [[x[1], x[5], x[9], x[13], x[17], x[21], x[25], x[29], x[33]] for x in crates.split('\n')]
cratrix.pop()

cratrix_transpose = []

for i in range(len(cratrix[0])):
    cratrix_transpose.append([x[i] for x in cratrix])

for x in cratrix_transpose:
    x.reverse()

for x in cratrix_transpose:
    while ' ' in x:
        x.remove(' ')

inst = instructions.split('\n')

instt = [x.split(' ') for x in inst]

instt.pop()

insttt = [[x[1], x[3], x[5]] for x in instt]


def execute_instruc(a_cratrix, instruc):
    stack = [x for x in a_cratrix[int(instruc[1]) - 1]]
    size = len(stack)
    a_cratrix[int(instruc[1]) - 1] = stack[:(size - int(instruc[0]))]
    for y in stack[(size - int(instruc[0])):]:
        a_cratrix[int(instruc[2]) - 1].append(y)


for instruc in insttt:
    execute_instruc(cratrix_transpose, instruc)

for x in cratrix_transpose:
    print(x[-1])