class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspection_count = 0

    def inspect(self):
        self.inspection_count += 1
        under_inspection = self.items[0]
        self.items.pop(0)
        new_worry_level = self.operation(under_inspection) // 3
        if self.test(new_worry_level):
            return [self.if_true, new_worry_level]
        return [self.if_false, new_worry_level]

    def catch(self, item):
        self.items.append(item)


monkeys = [Monkey([50, 70, 54, 83, 52, 78], lambda x: x * 3, lambda x: x % 11 == 0, 2, 7),
           Monkey([71, 52, 58, 60, 71], lambda x: x * x, lambda x: x % 7 == 0, 0, 2),
           Monkey([66, 56, 56, 94, 60, 86, 73], lambda x: x + 1, lambda x: x % 3 == 0, 7, 5),
           Monkey([83, 99], lambda x: x + 8, lambda x: x % 5 == 0, 6, 4),
           Monkey([98, 98, 79], lambda x: x + 3, lambda x: x % 17 == 0, 1, 0),
           Monkey([76], lambda x: x + 4, lambda x: x % 13 == 0, 6, 3),
           Monkey([52, 51, 84, 54], lambda x: x * 17, lambda x: x % 19 == 0, 4, 1),
           Monkey([82, 86, 91, 79, 94, 92, 59, 94], lambda x: x + 7, lambda x: x % 2 == 0, 5, 3)]

for i in range(20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            thrown_item = monkey.inspect()
            monkeys[thrown_item[0]].catch(thrown_item[1])

scores = []
for monkey in monkeys:
    scores.append(monkey.inspection_count)
scores.sort()
print(scores[-1] * scores[-2])
